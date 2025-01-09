from app import db
from sqlalchemy.sql import func

class User(db.Model):
    # Model for the users table
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_sha256 = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)

class UserLibraryProgress(db.Model):
    """Model for the UserLibraryProgress table."""
    __tablename__ = "user_library_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    last_review = db.Column(db.Date, nullable=True)
    next_review = db.Column(db.Date, nullable=True)
    review_count = db.Column(db.Integer, nullable=False)
    ease_factor = db.Column(db.Float, nullable=False)


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

def username_exists(username):
    return User.query.filter_by(username=username).first() is not None

def check_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    return user.password_sha256 == password

def set_password(user: User, new_password):
    user.password_sha256 = new_password
    db.session.commit()

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