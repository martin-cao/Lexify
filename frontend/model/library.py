from sqlalchemy import Column, Integer, String, Text, ForeignKey

from database.database import DatabaseConnection
from model.base import Base

db_conn = DatabaseConnection()
session = db_conn.get_session()

class Library(Base):
    # Model for the library table
    __tablename__ = "libraries"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class LibraryWord(Base):
    # Model for the library_words table
    __tablename__ = "library_words"

    id = Column(Integer, primary_key=True)
    library_id = Column(Integer, ForeignKey("libraries.id"), nullable=False)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)


# CRUD for Library
def create_library(name, description=None):
    library = Library(name=name, description=description)
    session.add(library)
    session.commit()
    return library

def get_library_by_id(library_id):
    return session.query(Library).get(library_id)

def update_library(library_id, name=None, description=None):
    library = session.query(Library).get(library_id)
    if library:
        if name:
            library.name = name
        if description:
            library.description = description
        session.commit()
    return library

def delete_library(library_id):
    library = session.query(Library).get(library_id)
    if library:
        session.delete(library)
        session.commit()
    return library

# CRUD for LibraryWords
def add_word_to_library(library_id, word_id):
    library_word = LibraryWord(library_id=library_id, word_id=word_id)
    session.add(library_word)
    session.commit()
    return library_word

def get_all_libraries():
    return session.query(Library).all()