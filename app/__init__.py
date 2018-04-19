import os
import click
from flask import Flask, send_from_directory
from flask_restplus import Api
from flask_cors import CORS

from app.api import ns
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:////tmp/test.db"
    )

    db.init_app(app)
    CORS(app)

    @app.route("/")
    def index():
        # return 'helo'
        return send_from_directory('static', 'index.html')

    @app.route("/<path:path>")
    def static_over(path):
        return send_from_directory('static', path)

    api = Api(doc="/docs")
    api.add_namespace(ns, path="/api/boards")
    api.init_app(app)

    @app.cli.command()
    def initdb():
        """Initialize the database."""
        click.echo("Init the db")
        db.create_all()

    @app.cli.command()
    def dropdb():
        """Drop the database."""
        click.echo("Drop the db")
        db.drop_all()

    return app
