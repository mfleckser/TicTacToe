import random

from flask import Flask, request, Response
from game.board import Board

app = Flask(__name__)

@app.route("/create")
def create():
    id = "123456"
    board = "-" * 9

    with open("data.txt", "a") as db:
        db.write(id + "," + board + "\n")

    return id

# /get?id=123456
@app.route("/get")
def get():
    requestId = request.args.get("id", type=str)

    response = Response("Invalid Board ID", status=404)

    with open("data.txt", "r") as db:
        for entry in db:
            id, board = entry.split(",")

            if id == requestId:
                response = Response(board, status=200)
                break
            
    return response


@app.route("/play", methods=["POST"])
def play():
    return None