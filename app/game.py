import uuid


class Board:
    id = None
    dimensions = [6, 6]
    mines = []
    cells = []
    over = False

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.mines = [(1, 1), (4, 5), (1, 3)]
        self.cells = [{"x": 0, "y": 0, "value": 0}]

    def visit_cell(self, x, y):
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


def visit_cell(board_id, x, y):
    """Visit a cell in a board:
    - check if cell is visited already
    - if not, evaluate if it is a bomb
    - if it is a positive cell, add to visited
    - if it is a zero, find neighbours and repeat
    """
    board = get_board(board_id)
    return board
