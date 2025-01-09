from datetime import date, timedelta
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

def fetch_new_word_progress_dict(words):
    today = date.today()

    progresses = []
    for w in words:
        progresses.append({
            "progress_id": -1, # 临时量
            "word": w.word,
            "word_id": w.id,
            "definition": w.definition,
            "proficiency": 0,
            "mode": "new"
        })

    return progresses

def start_learning(uid: int, library_id: int, limit: int = 20):
    words = fetch_new_words_from_user(uid, library_id, limit)
    progresses = fetch_new_word_progress_dict(words)
    return progresses

def find_pf_for_word(word: str, new_proficiencies: list) -> int:
    """
    在形如 [ {'hello':95}, {'apple':60}, ... ] 的列表中，
    找到 key=word 对应的熟练度值。如果找不到，默认返回 0。
    """
    for d in new_proficiencies:
        if word in d:
            return d[word]
    return 0


def finish_learning(progresses: list[dict], new_proficiencies: list[dict], uid: int):
    """
    :param progresses: memorize_view_model.finish_memorize_session() 里传来的单词数据
                       形如: [
                         {
                           "progress_id": -1 or 123,
                           "word": "apple",
                           "definition": "...",
                           "proficiency": 0,
                           "mode": "new"/"review",
                           "n": ...,
                           "done": True/False,
                           ...
                         },
                         ...
                       ]
    :param new_proficiencies: 一个list[dict]，形如 [ {'apple': 80}, {'hello':90}, ... ]
                             表示每个单词最后算出来的新熟练度
    :param uid: 当前用户ID
    :return: None
    """

    today = date.today()
    records_to_add = []

    for p in progresses:
        # 找到对该单词计算出的最终熟练度
        final_pf = find_pf_for_word(p["word"], new_proficiencies)

        if p["progress_id"] == -1:
            # ============ 情况1：新学单词，数据库里还没记录，要新建 ============
            from model.word import get_word_by_word
            word_id = get_word_by_word(p["word"]).id
            if not word_id:
                # 万一没查到id，则跳过或做别的处理
                continue

            record = LearningProgress(
                user_id=uid,
                word_id=word_id,
                proficiency=final_pf,
                last_review=today,
                next_review=get_next_review_date(review_count=1, proficiency=final_pf),
                review_count=1
            )
            records_to_add.append(record)

        else:
            # ============ 情况2：已有进度(复习)，更新对应progress记录 ============
            existing_progress = (
                session.query(LearningProgress)
                .filter(LearningProgress.id == p["progress_id"])
                .first()
            )
            if not existing_progress:
                # 如果没查到，对应记录可能被删掉/出错，可根据需要决定报错或忽略
                continue

            existing_progress.last_review = today
            existing_progress.proficiency = final_pf
            existing_progress.review_count += 1
            existing_progress.next_review = get_next_review_date(
                existing_progress.review_count,
                final_pf
            )
            # 也可根据需要更新 status、或其他字段

    # 统一把新建的记录插入数据库
    if records_to_add:
        session.add_all(records_to_add)

    # 提交更新/新建
    session.commit()

    print(f"[DEBUG] finish_learning() -> Added {len(records_to_add)} new records, "
          f"updated {len(progresses) - len(records_to_add)} existing ones.")


#         p.last_review = today
#         # if not in new_proficiencies, use old proficiency
#         new_pf = new_proficiencies.get(p.id, p.proficiency)
#         p.proficiency = new_pf
#         p.review_count += 1
#         p.next_review = get_next_review_date(p.review_count, new_pf)
#
#     session.commit()
#     print(f"[DEBUG] Updated {len(progresses)} records in review_words().")

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


def start_reviewing(uid: int, library_id: int, limit: int = 20):
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
