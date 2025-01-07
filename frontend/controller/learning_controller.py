import random
from datetime import date, datetime, timedelta
from sqlalchemy.sql import func

from dict.load_data import LibraryWords
from model.word import Word
from model.user import LearningProgress

from database.database import DatabaseConnection
from viewmodel.message import show_popup_message

db_conn = DatabaseConnection()
session = db_conn.get_session()



def get_next_review_date(review_count: int, proficiency: int) -> date:
    '''
    Return the next review date according to current review count and proficiency.
    :param review_count:
    :param proficiency:
    :return review_date:
    '''
    base_intervals = [1, 2, 4, 7, 15, 30]
    index = min(review_count - 1, len(base_intervals) - 1)
    days = base_intervals[index]

    if proficiency < 30:
        days = int(days * 0.8) if days > 1 else 1
    elif proficiency > 70:
        days = int(days * 1.2)

    review_date = date.today() + timedelta(days=days)
    return review_date


def fetch_new_words_from_user(uid: int, library_id: int, limit: int = 20):
    '''
    Randomly fetch new words that the user is going to learn.
    Condition: Randomly choose 20 (or other number of) words, which don't have any learning progress or whose proficiency is 0.

    :param uid:
    :param limit:
    :return words:
    '''

    # Get word ids that already has learning records
    learning_word_ids = (
        session.query(LearningProgress.word_id)
        .filter(LearningProgress.user_id == uid)
        .distinct()
    )

    # Randomly select words that don't have any learning records
    words_query = (
        session.query(Word)
        .join(LibraryWords, Word.id == LibraryWords.word_id)
        .filter(LibraryWords.library_id == library_id)
        .filter(~Word.id.in_(learning_word_ids))
        .order_by(func.random())  # May cause performance issue
        .limit(limit)
    )

    words = words_query.all()
    return words

def start_learning_new_words(uid: int, words):
    '''
    Put these words into the table "learning_progress", then set
        proficiency = 0
        last_review = today
        next_review = get_next_review_date()
        review_count = 1

    :param uid:
    :param words:
    :return:
    '''

    today = date.today()

    for w in words:
        progress = LearningProgress(
            user_id=uid,
            word_id=w.id,
            proficiency=0,
            last_review=today,
            next_review=get_next_review_date(1, 0), # review_count=1, proficiency=0
            review_count=1
        )

        session.add(progress)
    session.commit()

def learn_new_words(uid: int, library_id: int, limit: int = 20):
    '''
    Called after pressed "新学", find maximally "limit" words for the user, then make records in the table "learning_progress".
    :param uid:
    :param limit:
    :return new_words:
    '''

    new_words = fetch_new_words_from_user(uid, library_id=library_id, limit=limit)
    print(f"[DEBUG] learn_new_words -> new_words \n{new_words}")
    if not new_words:
        print("[WARNING] No new words to learn.")
        # 呼出弹窗
        show_popup_message(message="没有新单词可以背了", title="", msg_type="info")
        return []

    start_learning_new_words(uid, new_words)

    # Find the progresses just created
    progresses = (
        session.query(LearningProgress)
        .filter(LearningProgress.user_id == uid)
        .order_by(LearningProgress.id.desc())
        .limit(len(new_words))
        .all()
    )

    result = []
    for p in progresses:
        w = session.query(Word).get(p.word_id)
        if w:
            result.append({
                "progress_id": p.id,
                "word": w.word,
                "definition": w.definition,
                "proficiency": p.proficiency,
                "mode": "new"
            })

    print(f"[DEBUG] Successfully add {len(new_words)} words into learning_progress.")
    return result

def fetch_words_to_review(uid: int, library_id: int, limit: int = 20):
    '''
    Fetch words from a specific library that need to be reviewed (next_review <= today).

    :param uid: user ID
    :param library_id: which library
    :param limit: how many
    :return: list of LearningProgress objects
    '''
    today = date.today()

    # First, find all word_ids in that library
    subq_library_word_ids = (
        session.query(LibraryWords.word_id)
        .filter(LibraryWords.library_id == library_id)
    )

    # Then filter learning_progress by that library + next_review <= today
    progress_list = (
        session.query(LearningProgress)
        .filter(LearningProgress.user_id == uid)
        .filter(LearningProgress.word_id.in_(subq_library_word_ids))
        .filter(LearningProgress.next_review <= today)
        .order_by(LearningProgress.id)
        .limit(limit)
        .all()
    )

    return progress_list


def start_reviewing_words(uid: int, library_id: int, limit: int = 20):
    '''
    1) Fetch up to `limit` words from this library that are due for review.
    2) Return a list of dict for front-end usage:
       [
         { "progress_id", "word", "definition", "proficiency", "is_revise":True },
         ...
       ]

    :param uid: user ID
    :param library_id: library ID
    :param limit: how many
    :return result: list of dict
    '''
    to_review = fetch_words_to_review(uid, library_id, limit)
    if not to_review:
        print("[WARNING] No words to review.")
        show_popup_message(message="没有单词可以复习了", title="", msg_type="info")
        return []

    result = []
    for p in to_review:
        w = session.query(Word).get(p.word_id)
        if w:
            result.append({
                "progress_id": p.id,
                "word": w.word,
                "definition": w.definition,
                "proficiency": p.proficiency,
                "mode": "review"
            })

    print(f"[DEBUG] Found {len(result)} words to review in library_id={library_id}.")
    return result


def review_words(progress_ids: list, new_proficiencies: dict):
    '''
    Final step: UPDATE the progress records with new proficiency & typical fields:
      - last_review = today
      - review_count += 1
      - next_review = get_next_review_date(review_count, new_pf)

    :param progress_ids: list of progress IDs
    :param new_proficiencies: dict { progress_id: new_proficiency }
    '''
    today = date.today()

    progresses = (
        session.query(LearningProgress)
        .filter(LearningProgress.id.in_(progress_ids))
        .all()
    )

    for p in progresses:
        p.last_review = today
        # if not in new_proficiencies, use old proficiency
        new_pf = new_proficiencies.get(p.id, p.proficiency)
        p.proficiency = new_pf
        p.review_count += 1
        p.next_review = get_next_review_date(p.review_count, new_pf)

    session.commit()
    print(f"[DEBUG] Updated {len(progresses)} records in review_words().")
