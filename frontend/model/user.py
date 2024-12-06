from sqlalchemy import Column, Integer, String, Text, ForeignKey, Time, Float
from sqlalchemy.sql import func

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