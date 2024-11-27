from flask import Blueprint

example_bp = Blueprint('example', __name__)

@example_bp.route('/')
def hello_world():
    return 'Hello World!'