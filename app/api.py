from flask import current_app
from flask_restplus import Api, Resource, fields, Namespace
from app.game import Board, AlreadyVisitedError


ns = Namespace("boards")


@ns.errorhandler(LookupError)
def handle_lookup_error(error):
    """Return a custom message and 400 status code"""
    return {"message": "Not found"}, 404


@ns.errorhandler(AlreadyVisitedError)
def handle_already_visited_error(error):
    """Return a custom message and 400 status code"""
    return {"message": "Already visited"}, 409



cell_model = ns.model(
    "Cell",
    {
        "x": fields.Integer(),
        "y": fields.Integer(),
        "value": fields.Integer(),
        "flag": fields.Boolean(),
        "question": fields.Boolean(),
    },
)

board_model = ns.model(
    "Board",
    {
        "id": fields.String(),
        "dimensions": fields.List(fields.Integer()),
        "cells": fields.List(fields.Nested(cell_model)),
        "over": fields.Boolean(),
    },
)


@ns.route("")
class BoardsAPI(Resource):

    @ns.marshal_with(board_model, as_list=True)
    def get(self):
        return Board.get_all()

    @ns.marshal_with(board_model, as_list=True)
    def post(self):
        board = Board.create()
        current_app.logger.info(board.id)
        current_app.logger.info(board.mines)
        return board, 201


@ns.route("/<board_id>")
class BoardAPI(Resource):

    @ns.marshal_with(board_model)
    def get(self, board_id):
        board = Board.get_by_id(board_id)
        return board


@ns.route("/<board_id>/cells/<int:x>/<int:y>")
class BoardCellAPI(Resource):

    @ns.marshal_with(board_model)
    def put(self, board_id, x, y):
        board = Board.get_by_id(board_id)
        board.visit_cell(x, y)
        board.save()
        return board
