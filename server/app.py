import random
import json

from flask import Flask, request, Response, jsonify
from funcs import loadBoard, updateBoard, resetBoard

app = Flask(__name__)

# returns id of newly created game
@app.route("/create")
def create():
    id = str(random.randint(0, 999999))
    id = "0" * (6 - len(id)) + id
    board = "-" * 9

    with open("data.txt", "a") as db:
        db.write(id + "," + board + "\n")

    response = jsonify({"id": id})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# /get?id=123456
@app.route("/get")
def get():
    requestId = request.args.get("id", type=str)

    response = jsonify({"success": False})

    board = loadBoard(requestId, True)
    if board != "Invalid ID":
        response = jsonify({"success": True, "board": board})
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# request must contain json with id and coordinates
# returns new state of the board and updates database
@app.route("/play", methods=["POST"])
def play():
    req = json.loads(request.data.decode("utf-8")) # dict w/ keys: id, x, y
    board = loadBoard(req["id"])
    responseContent = {"success": False}

    if board != "Invalid ID" and board.play((req["x"], req["y"])): # successfully loaded board and made move
        responseContent["success"] = True
        responseContent["board"] = str(board)
        updateBoard(req["id"], str(board))
    
    response = jsonify(responseContent)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# /reset?id=123456
# returns success or failue and updates database
@app.route("/reset")
def reset():
    requestId = request.args.get("id", type=str)

    success = resetBoard(requestId)
    
    response = jsonify({"success": success})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)