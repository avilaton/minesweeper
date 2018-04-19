import uuid
import random

import sqlalchemy as sa
import sqlalchemy.exc
from app.database import db


class AlreadyVisitedError(Exception):
    "Cell was already revealed."
    pass


class Board(db.Model):

    id = sa.Column(sa.String, primary_key=True)

    dimensions = sa.Column(sa.JSON)
    mine_count = sa.Column(sa.Integer, default=3)
    mines = sa.Column(sa.JSON)
    cells = sa.Column(sa.JSON)
    over = sa.Column(sa.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())
        self.mine_count = kwargs.get('mine_count', 3)
        self.dimensions = kwargs.get('dimensions', [6, 6])
        self.cells = []

        if 'mines' in kwargs:
            self.mines = kwargs.get('mines')
        else:
            self.mines = random.sample(
                [
                    (x, y)
                    for x in range(self.dimensions[0])
                    for y in range(self.dimensions[1])
                ],
                self.mine_count,
            )

    def visit_cell(self, x, y):
        """Visit a cell in a board:
        - check if cell is visited already
        - if not, evaluate if it is a mine
        - if it is a positive cell, add to visited
        - if it is a zero, find neighbours and repeat
        """
        cells = [c for c in self.cells] or []
        existing = [c for c in cells if c["x"] == x and c["y"] == y]
        if existing:
            raise AlreadyVisitedError()

        mines = [m for m in self.mines if m[0] == x and m[1] == y]
        if mines:
            self.over = True
            cells.append({"x": x, "y": y, "value": None})
            self.cells = cells
            return

        value = self.count_neighbour_mines(x, y)
        cells.append({"x": x, "y": y, "value": value})
        self.cells = cells

    def save(self):
        db.session.commit()

    def get_cell_neighbours(self, x, y):
        """
        Find coordinates for all valid cell neighbours.
        :param x:
        :param y:
        :return:
        """
        deltas = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        candidates = [(x + i, y + j) for i, j in deltas]
        neighbours = [
            cell for cell in candidates if self.validate_cell(cell[0], cell[1])
        ]
        return neighbours

    def count_neighbour_mines(self, x, y):
        """
        Count the number of mines which are direct neighbours of this cell.
        :param x:
        :param y:
        :return:
        """
        neighbours = self.get_cell_neighbours(x, y)
        neighbour_mines = [m for m in self.mines if m in neighbours]
        return len(neighbour_mines)

    def validate_cell(self, x, y):
        """
        Ensure a cell has valid coordinates in this board.
        :param x:
        :param y:
        :return:
        """
        return 0 <= x < self.dimensions[0] and 0 <= y < self.dimensions[1]



def get_boards():
    return db.session.query(Board).all()


def get_board(board_id):
    try:
        board = db.session.query(Board).filter_by(id=board_id).one()
    except sa.exc.SQLAlchemyError:
        raise LookupError()
    return board


def create_board():
    board = Board()
    db.session.add(board)
    db.session.commit()
    return board
