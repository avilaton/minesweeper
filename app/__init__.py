from flask import Flask
from flask_restplus import Api, Resource

api = Api()

board = {
    "id": 2,
    "dimensions": [6, 6],
    "mines": [(1, 1), (4, 5), (1, 3)],
    "cells": [{"position": [0, 0], "value": 0}],
    "over": False,
}


@api.route("/boards")
class BoardsAPI(Resource):

    def get(self):
        return [
            {"id": 1, "over": True},
            {"id": 2, "over": False},
            {"id": 3, "over": False},
            {"id": 4, "over": False},
        ]

    def post(self):
        return board, 201


@api.route("/boards/<int:id>")
class BoardAPI(Resource):

    def get(self, id):
        return board


@api.route("/games/<int:game_id>/cells/<int:x>/<int:y>")
class GameCellAPI(Resource):

    def put(self, game_id, x, y):
        return board

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    return app
