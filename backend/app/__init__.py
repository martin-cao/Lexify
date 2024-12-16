from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app.routes import init_routes
        init_routes(app)  # Initialize all routes

        db.create_all()  # Create database tables

    return app