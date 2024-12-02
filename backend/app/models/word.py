from app import db

class Word(db.Model):
    # Model for the Words table
    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255), nullable=False)
    part_of_speech = db.Column(db.String(50), nullable=True)
    definition = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text, nullable=True)