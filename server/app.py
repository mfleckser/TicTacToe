import random

from flask import Flask, request, Response, jsonify
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

    response = jsonify({"success": False})

    with open("data.txt", "r") as db:
        for entry in db:
            id, board = entry.strip().split(",")

            if id == requestId:
                response = jsonify({"success": True, "board": board})
                break
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/play", methods=["POST"])
def play():
    return None