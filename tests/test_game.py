import pytest

from app import game


def test_game_visit_cell():
    board = game.Board(mines=[(1, 1), (4, 5), (1, 3)])
    assert board.mines == [(1, 1), (4, 5), (1, 3)]

    assert board.cells == []

    board.visit_cell(1, 5)
    assert len(board.cells) == 1

    with pytest.raises(game.AlreadyVisitedError):
        board.visit_cell(1, 5)

    assert not board.over
    board.visit_cell(1, 1)
    assert board.over
