import uuid
import random


class AlreadyVisitedError(Exception):
    "Cell was already revealed."
    pass


class Board:
    id = None
    dimensions = [6, 6]
    mine_count = 3
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
                self.mine_count,
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
            self.cells.append({"x": x, "y": y, "value": None})
            return

        value = self.count_neighbour_mines(x, y)
        self.cells.append({"x": x, "y": y, "value": value})

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
