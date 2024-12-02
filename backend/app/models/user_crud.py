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
def create_user_library_progress(user_id, library_id, random_seed, progress_index=0, status='in_progress'):
    progress = UserLibraryProgress(
        user_id=user_id,
        library_id=library_id,
        random_seed=random_seed,
        progress_index=progress_index,
        status=status
    )
    db.session.add(progress)
    db.session.commit()
    return progress