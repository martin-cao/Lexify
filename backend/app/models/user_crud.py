from app.models.user import User, UserLibraryProgress
from app import db

# CRUD for Users
def create_user(username, password_sha256, email, description=None):
    user = User(username=username, password_sha256=password_sha256, email=email, description=description)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.get(username)

# CRUD for UserLibraryProgress
def create_user_library_progress(user_id, word_id, library_id, status, proficiency, last_review, next_review, review_count, ease_factor):
    progress = UserLibraryProgress(
        user_id=user_id,
        word_id=word_id,
        library_id=library_id,
        status=status,
        proficiency=proficiency,
        last_review=last_review,
        next_review=next_review,
        review_count=review_count,
        ease_factor=ease_factor
    )
    db.session.add(progress)
    db.session.commit()
    return progress

def get_user_library_progress_by_id(progress_id):
    return UserLibraryProgress.query.get(progress_id)

def update_user_library_progress(progress_id, **kwargs):
    progress = UserLibraryProgress.query.get(progress_id)
    for key, value in kwargs.items():
        setattr(progress, key, value)
    db.session.commit()
    return progress

def delete_user_library_progress(progress_id):
    progress = UserLibraryProgress.query.get(progress_id)
    db.session.delete(progress)
    db.session.commit()
    return progress