import uuid
import random


class AlreadyVisitedError(Exception):
    "Cell was already revealed."
    pass


class Board:
    id = None
    dimensions = [6, 6]
    mines = []
    cells = []
    over = False

    def __init__(self, mines=None):
        self.id = str(uuid.uuid4())
        if mines:
            self.mines = mines
        else:
            self.mines = random.sample(
                [
                    (x, y)
                    for x in range(self.dimensions[0])
                    for y in range(self.dimensions[1])
                ],
                10,
            )

    def visit_cell(self, x, y):
        """Visit a cell in a board:
        - check if cell is visited already
        - if not, evaluate if it is a mine
        - if it is a positive cell, add to visited
        - if it is a zero, find neighbours and repeat
        """
        existing = [cell for cell in self.cells if cell["x"] == x and cell["y"] == y]
        if existing:
            raise AlreadyVisitedError()

        mines = [mine for mine in self.mines if mine[0] == x and mine[1] == y]
        if mines:
            self.over = True

        self.cells.append({"x": x, "y": y, "value": 0})

        return


boards = []


def create_board():
    board = Board()
    boards.append(board)
    return board


def get_boards():
    return boards


def get_board(board_id):
    try:
        board = next(item for item in boards if item.id == board_id)
    except StopIteration:
        raise LookupError()

    return board
