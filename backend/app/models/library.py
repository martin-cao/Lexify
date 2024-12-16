from app import db


class Library(db.Model):
    # Model for the library table
    __tablename__ = "libraries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)


class LibraryWord(db.Model):
    # Model for the library_words table
    __tablename__ = "library_words"

    id = db.Column(db.Integer, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey("libraries.id"), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"), nullable=False)


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