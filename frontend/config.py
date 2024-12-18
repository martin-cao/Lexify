import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database", "database_fe.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = 'your_secret_key'
    SERVER_URL = "http://127.0.0.1:5000"