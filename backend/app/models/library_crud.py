from app.models.library import Library, LibraryWord
from app import db

# CRUD for Library
def create_library(name, description=None):
    library = Library(name=name, description=description)
    db.session.add(library)
    db.session.commit()
    return library

def get_library_by_id(library_id):
    return Library.query.get(library_id)

def update_library(library_id, name=None, description=None):
    library = Library.query.get(library_id)
    if library:
        if name:
            library.name = name
        if description:
            library.description = description
        db.session.commit()
    return library

def delete_library(library_id):
    library = Library.query.get(library_id)
    if library:
        db.session.delete(library)
        db.session.commit()
    return library

# CRUD for LibraryWords
def add_word_to_library(library_id, word_id):
    library_word = LibraryWord(library_id=library_id, word_id=word_id)
    db.session.add(library_word)
    db.session.commit()
    return library_word