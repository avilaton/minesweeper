from flask_restplus import Api, Resource, fields, Model
from app import game

api = Api()

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
        "id": fields.Integer(),
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
        return board, 201


@api.route("/boards/<int:board_id>")
class BoardAPI(Resource):

    @api.marshal_with(board_model)
    def get(self, board_id):
        board = game.get_board(board_id)
        return board


@api.route("/boards/<int:board_id>/cells/<int:x>/<int:y>")
class BoardCellAPI(Resource):

    @api.marshal_with(board_model)
    def put(self, board_id, x, y):
        board = game.get_board(board_id)
        game.visit_cell(board, x, y)
        return board
