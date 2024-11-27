def init_routes(app):
    from .user_routes import user_bp
    # from .word_routes import word_bp
    # from .vocabulary_routes import vocabulary_bp

    app.register_blueprint(user_bp)
    # app.register_blueprint(word_bp)
    # app.register_blueprint(vocabulary_bp)