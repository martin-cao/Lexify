from .word import Word
from Lexify import session

# CRUD for Words
def create_word(word, part_of_speech, definition, example=None):
    word_entry = Word(word=word, part_of_speech=part_of_speech, definition=definition, example=example)
    session.add(word_entry)
    session.commit()
    return word_entry

def get_word_by_id(word_id):
    return session.query(Word).get(word_id)

def delete_word(word_id):
    word_entry = session.query(Word).get(word_id)
    if word_entry:
        session.delete(word_entry)
        session.commit()
    return word_entry