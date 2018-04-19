from flask import current_app
from flask_restplus import Api, Resource, fields
from app import game

api = Api()


@api.errorhandler(LookupError)
def handle_lookup_error(error):
    """Return a custom message and 400 status code"""
    return {"message": "Not found"}, 404


@api.errorhandler(game.AlreadyVisitedError)
def handle_already_visited_error(error):
    """Return a custom message and 400 status code"""
    return {"message": "Already visited"}, 409


cell_model = api.model(
    "Cell",
    {
        "x": fields.Integer(),
        "y": fields.Integer(),
        "value": fields.Integer(),
        "flag": fields.Boolean(),
        "question": fields.Boolean(),
    },
)

board_model = api.model(
    "Board",
    {
        "id": fields.String(),
        "dimensions": fields.List(fields.Integer()),
        "cells": fields.List(fields.Nested(cell_model)),
        "over": fields.Boolean(),
    },
)


@api.route("/boards")
class BoardsAPI(Resource):

    @api.marshal_with(board_model, as_list=True)
    def get(self):
        return game.get_boards()

    @api.marshal_with(board_model, as_list=True)
    def post(self):
        board = game.create_board()
        current_app.logger.info(board.id)
        current_app.logger.info(board.mines)
        return board, 201


@api.route("/boards/<board_id>")
class BoardAPI(Resource):

    @api.marshal_with(board_model)
    def get(self, board_id):
        board = game.get_board(board_id)
        return board


@api.route("/boards/<board_id>/cells/<int:x>/<int:y>")
class BoardCellAPI(Resource):

    @api.marshal_with(board_model)
    def put(self, board_id, x, y):
        board = game.get_board(board_id)
        board.visit_cell(x, y)
        board.save()
        return board
