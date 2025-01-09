from datetime import date
from sqlalchemy import func

from model.user import LearningProgress
from model.library import LibraryWord

from database.database import DatabaseConnection

db_conn = DatabaseConnection()
session = db_conn.get_session()

def get_today_study_count(user_id, library_id):
    """计算今日学习/复习的词数"""
    today = date.today()
    count = (
        session.query(LearningProgress)
        .filter(
            LearningProgress.user_id == user_id,
            func.date(LearningProgress.last_review) == today
        )
        .count()
    )
    return count

def get_total_study_count(user_id):
    """计算累计学习的词数"""
    count = (
        session.query(LearningProgress)
        .filter(
            LearningProgress.user_id == user_id,
            LearningProgress.proficiency > 0
        )
        .count()
    )
    return count

def get_library_study_count(user_id, library_id):
    """计算当前词书的累计学习词数"""
    count = (
        session.query(LearningProgress)
        .filter(
            LearningProgress.user_id == user_id,
            LearningProgress.proficiency > 0
        )
        .count()
    )
    return count

def get_library_total_word_count(library_id):
    """计算词书的总词数"""
    count = (
        session.query(LibraryWord)
        .filter(LibraryWord.library_id == library_id)
        .count()
    )
    return count