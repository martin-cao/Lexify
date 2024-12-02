from app.models.word import Word
from app import db

# CRUD for Words
def create_word(word, part_of_speech, definition, example=None):
    word_entry = Word(word=word, part_of_speech=part_of_speech, definition=definition, example=example)
    db.session.add(word_entry)
    db.session.commit()
    return word_entry

def get_word_by_id(word_id):
    return Word.query.get(word_id)

def delete_word(word_id):
    word_entry = Word.query.get(word_id)
    if word_entry:
        db.session.delete(word_entry)
        db.session.commit()
    return word_entry