import pytest

from app import game


def test_game_visit_cell():
    board = game.Board()

    assert board.cells == []

    board.visit_cell(1, 5)
    assert len(board.cells) == 1

    with pytest.raises(game.AlreadyVisitedError):
        board.visit_cell(1, 5)
