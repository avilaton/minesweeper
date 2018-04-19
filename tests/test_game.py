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

    assert board.validate_cell(0, 0)
    assert board.validate_cell(0, 5)
    assert not board.validate_cell(0, 10)
    assert not board.validate_cell(-1, 0)
    assert not board.validate_cell(0, -1)
    assert not board.validate_cell(20, 0)
    assert not board.validate_cell(0, 20)
    assert not board.validate_cell(6, 0)

    rv = board.get_cell_neighbours(0, 0)
    assert set(rv) == {(0, 1), (1, 1), (1, 0)}

    rv = board.get_cell_neighbours(0, 1)
    assert set(rv) == {(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)}
