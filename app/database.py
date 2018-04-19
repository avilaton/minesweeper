import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Board(db.Model):

    id = sa.Column(sa.String, primary_key=True)
    mine_count = sa.Column(sa.Integer, default=3)
    mines = sa.Column(sa.JSON)
    cells = sa.Column(sa.JSON)
