import os
import click
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

    @app.cli.command()
    def initdb():
        """Initialize the database."""
        click.echo('Init the db')
        db.create_all()


    @app.cli.command()
    def dropdb():
        """Drop the database."""
        click.echo('Drop the db')
        db.drop_all()

    return app
