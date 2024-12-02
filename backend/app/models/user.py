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
    library_id = db.Column(db.Integer, db.ForeignKey("library.id"), nullable=False)
    progress_index = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.String(50), default="in_progress", nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    random_seed = db.Column(db.Integer, nullable=False)