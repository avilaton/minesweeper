import uuid

board = {
    "id": 2,
    "dimensions": [6, 6],
    "mines": [(1, 1), (4, 5), (1, 3)],
    "cells": [{"x": 0, "y": 0, "value": 0}],
    "over": False,
}

boards = [
    {"id": 1, "over": True},
]


def create_board():
    new_id = str(uuid.uuid4())
    new_board = {'id': new_id, "over": False}
    boards.append(new_board)
    return new_board


def get_boards():
    return boards


def get_board(board_id):
    return board


def visit_cell(board_id, x, y):
    """Visit a cell in a board:
    - check if cell is visited already
    - if not, evaluate if it is a bomb
    - if it is a positive cell, add to visited
    - if it is a zero, find neighbours and repeat
    """
    return board
