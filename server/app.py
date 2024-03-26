import random

from flask import Flask
from game.board import Board

app = Flask(__name__)

@app.route("/create")
def create():
    id = "mark"
    board = "-" * 9

    with open("data.txt", "a") as file:
        file.write(id + ":" + board + "\n")

    return id

@app.route("/play", methods=["POST"])
def play():
    return None