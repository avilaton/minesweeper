from flask import Flask
from flask_restplus import Api, Resource

api = Api()

board = {
    "id": 1,
    "dimensions": [6, 6],
    "mines": [(1, 1), (4, 5), (1, 3)],
    "cells": [{"position": [0, 0], "value": 0}],
}


app = Flask(__name__)
api.init_app(app)
