from .user import LearningProgress
from Lexify import session

# CRUD for LearningProgress
def create_learning_progress(word_id, status, proficiency, last_review, next_review, review_count):
    progress = LearningProgress(
        word_id=word_id,
        status=status,
        proficiency=proficiency,
        last_review=last_review,
        next_review=next_review,
        review_count=review_count
    )
    session.add(progress)
    session.commit()
    return progress

def get_learning_progress_by_id(progress_id):
    return session.query(LearningProgress).get(progress_id)

def update_learning_progress(progress_id, **kwargs):
    progress = session.query(LearningProgress).get(progress_id)
    for key, value in kwargs.items():
        setattr(progress, key, value)
    session.commit()
    return progress

def delete_learning_progress(progress_id):
    progress = session.query(LearningProgress).get(progress_id)
    session.delete(progress)
    session.commit()
    return progress