import os
from flask import Flask
from app.api import api
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:////tmp/test.db"
    )

    db.init_app(app)
    api.init_app(app)
    return app
