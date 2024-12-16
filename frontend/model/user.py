from sqlalchemy import Column, Integer, String, Text, ForeignKey, Time, Float
from sqlalchemy.sql import func

from database.database import session
from .base import Base


class User:
    # Model for the user

    def __init__(self, username):
        self.username = username

class LearningProgress(Base):
    # Model for the learning_progress table
    __tablename__ = "learning_progress"

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    status = Column(String(50), default="in_progress", nullable=False)
    proficiency = Column(Integer, nullable=False)
    last_review = Column(Time, nullable=True)
    next_review = Column(Time, nullable=True)
    review_count = Column(Integer, nullable=False)


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