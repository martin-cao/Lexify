from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def initialize_database(self):
        import model  # Make sure all models are imported
        model.Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session