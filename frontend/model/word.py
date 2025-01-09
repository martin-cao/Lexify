from sqlalchemy import Column, Integer, String, Text

from model.library import LibraryWord

from database.database import DatabaseConnection
from .base import Base

db_conn = DatabaseConnection()
session = db_conn.get_session()

class Word(Base):
    # Model for the Words table
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(255), nullable=False)
    pronunciation = Column(String(255), nullable=True)
    part_of_speech = Column(String(50), nullable=True)
    definition = Column(Text, nullable=False)
    example = Column(Text, nullable=True)


# CRUD for Words
def create_word(word, part_of_speech, definition, example=None):
    word_entry = Word(word=word, part_of_speech=part_of_speech, definition=definition, example=example)
    session.add(word_entry)
    session.commit()
    return word_entry

def get_word_by_id(word_id):
    return session.query(Word).get(word_id)

def get_word_by_word(word):
    return session.query(Word).filter_by(word=word).first()

def delete_word(word_id):
    word_entry = session.query(Word).get(word_id)
    if word_entry:
        session.delete(word_entry)
        session.commit()
    return word_entry

def get_words_by_library(library_id):
    return (
        session.query(Word)
        .join(LibraryWord, Word.id == LibraryWord.word_id)
        .filter(LibraryWord.library_id == library_id)
        # .options(joinedload(Word))
        .all()
    )