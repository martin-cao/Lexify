from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Word(Base):
    # Model for the Words table
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(255), nullable=False)
    part_of_speech = Column(String(50), nullable=True)
    definition = Column(Text, nullable=False)
    example = Column(Text, nullable=True)