from sqlalchemy import Column, Integer, String, Text, ForeignKey

from model.base import Base


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
