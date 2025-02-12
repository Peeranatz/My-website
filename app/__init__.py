from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    from .routes import main

    app.register_blueprint(main)  # 🔥 ต้องลงทะเบียน Blueprint

    with app.app_context():
        db.create_all()

    return app
