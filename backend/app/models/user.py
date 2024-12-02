from app import db
from sqlalchemy.sql import func

class User(db.Model):
    # Model for the users table
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_sha256 = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

class UserLibraryProgress(db.Model):
    """Model for the UserLibraryProgress table."""
    __tablename__ = "user_library_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey("libraries.id"), nullable=False)
    status = db.Column(db.String(50), default="in_progress", nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    last_review = db.Column(db.Time, nullable=True)
    next_review = db.Column(db.Time, nullable=True)
    review_count = db.Column(db.Integer, nullable=False)
    ease_factor = db.Column(db.Float, nullable=False)