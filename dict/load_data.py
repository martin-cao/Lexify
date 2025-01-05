# This file includes data from the project "DictionaryData" (https://github.com/LinXueyuanStdio/DictionaryData)
# licensed under the Apache-2.0 License.

# Please clone the repository mentioned above into Lexify/dict before running this file.
# The data from "DictionaryData" is not included in this repo.

import os
import time

import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Construct database models
Base = declarative_base()

class Libraries(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

class LibraryWords(Base):
    __tablename__ = 'library_words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)
    word_id = Column(Integer, ForeignKey('words.id'), nullable=False)

class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    pronunciation = Column(String, nullable=True)
    part_of_speech = Column(String, nullable=True)
    definition = Column(Text, nullable=False)
    example = Column(Text, nullable=True)

def main():
    # Link the database
    # db_path = "../backend/app/database/database_be.db"
    db_path = "../frontend/database/database_fe.db"
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    # Read the CSV files
    print("[DEBUG] Start reading CSV files...")

    book = pd.read_csv('DictionaryData/book.csv', sep=">")
    word = pd.read_csv('DictionaryData/word.csv', sep=">")
    relation_book_word = pd.read_csv('DictionaryData/relation_book_word.csv', sep=">")
    word_translation = pd.read_csv('DictionaryData/word_translation.csv', sep=',')

    print("[DEBUG] CSV file read complete.")

    # Construct mappings
    book_id_mapping = {}
    word_id_mapping = {}
    word_str_mapping = {}

    passed_items = []

    # Insert libraries
    print("[DEBUG] Start inserting libraries...")
    start_time = time.time()

    for idx, row in tqdm(book.iterrows(), total=len(book), desc="[Libraries]"):
        original_id = row.get("bk_id")
        title = str(row.get("bk_name"))

        if not title:
            passed_items.append(title)
            continue

        library_obj = Libraries(name=title)
        session.add(library_obj)
        session.flush()

        # Log the mapping
        book_id_mapping[original_id] = library_obj.id

    session.commit()
    end_time = time.time()
    print(f"[DEBUG] libraries import complete. Imported {len(book_id_mapping)} records. Took {end_time - start_time:.2f} seconds")
    if len(passed_items) != 0:
        print("Following libraries passed:\n")
        for item in passed_items:
            print(item)
    passed_items = []

    # Insert words
    print("[DEBUG] Start inserting words...")
    start_time = time.time()

    for idx, row in tqdm(word.iterrows(), total=len(word), desc="[Words]"):
        original_id = row.get("vc_id")
        w_word = str(row.get("vc_vocabulary", ""))
        w_pron = str(row.get("vc_phonetic_uk", ""))
        w_diff = row.get("vc_difficulty")

        if not w_word:
            passed_items.append(w_word)
            continue

        word_obj = Words(
            word=w_word,
            pronunciation=w_pron,
            definition=""
        )
        session.add(word_obj)
        session.flush()

        word_id_mapping[original_id] = word_obj.id
        word_str_mapping[word_obj.word] = word_obj.id

    session.commit()
    end_time = time.time()
    print(f"[DEBUG] words import complete. Imported {len(word_id_mapping)} records. Took {end_time - start_time:.2f} seconds")
    if len(passed_items) != 0:
        print("Following words passed:\n")
        for item in passed_items:
            print(item)
    passed_items = []

    # Insert translations
    print("[DEBUG] Start inserting translations...")
    start_time = time.time()

    rows_updated = 0

    for idx, row in tqdm(word_translation.iterrows(), total=len(word_translation), desc="[Translations]"):
        word_str = row.get("word", "")
        translation_str = str(row.get("translation", ""))

        if not word_str or not translation_str:
            passed_items.append(f"{word_str}; {translation_str}")
            continue

        if word_str not in word_str_mapping:
            passed_items.append(f"{word_str}; {translation_str}")
            continue

        db_word_id = word_str_mapping[word_str]
        word_obj = session.query(Words).get(db_word_id)

        if word_obj:
            word_obj.definition += translation_str
            rows_updated += 1

    session.commit()
    end_time = time.time()
    print(f"[DEBUG] translations import complete. Imported {rows_updated} records. Took {end_time - start_time:.2f} seconds.")
    # if len(passed_items) != 0:
    #     print("Following words passed:\n")
    #     for item in passed_items:
    #         print(item)
    passed_items = []

    # Insert library_words
    print("[DEBUG] Start inserting library_words...")
    start_time = time.time()

    link_count = 0

    for idx, row in tqdm(relation_book_word.iterrows(), total=len(relation_book_word), desc="[LibraryWords]"):
        original_book_id = row.get("bv_book_id")
        word_str = row.get("bv_voc_id")
        if original_book_id not in book_id_mapping:
            passed_items.append(f"{original_id}; {word_str}")
            continue

        if word_str not in word_id_mapping:
            passed_items.append(f"{original_id}; {word_str}")
            continue

        db_lib_id = book_id_mapping[original_book_id]
        db_word_id = word_id_mapping[word_str]

        # Build the link
        link_obj = LibraryWords(library_id=db_lib_id, word_id=db_word_id)
        session.add(link_obj)
        link_count += 1

    session.commit()
    end_time = time.time()

    print(f"[DEBUG] library_words import complete. Imported {link_count} records. Took {end_time - start_time:.2f} seconds.")
    if len(passed_items) != 0:
        print("Following links passed:\n")
        for item in passed_items:
            print(item)
    passed_items = []

    # session.execute("""
    # DELETE FROM words
    # WHERE definition = ''
    # """)
    # session.commit()

    session.close()
    print(f"[DEBUG] All data imported. Database path: {os.path.abspath(db_path)}")

if __name__ == "__main__":
    main()