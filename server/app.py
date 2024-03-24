from flask import Flask
from game.board import Board

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"