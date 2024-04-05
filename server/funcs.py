from game.board import Board

def loadBoard(id, asString=False):
    with open("data.txt", "r") as db:
        for game in db:
            entryId, board = game.strip().split(",")
            
            if entryId == id:
                if asString:
                    return board
                
                boardObj = Board(size=0, colors={}, other=None, boardString=board)
                return boardObj
            
    return "Invalid ID"

def updateBoard(id, board):
    with open("data.txt", "r+") as db:
        games = []

        for game in db:
            entryId = game.split(",")[0]

            if entryId == id:
                games.append(entryId + "," + board)
            else:
                games.append(game)

        db.seek(0)
        db.write("".join(games))

def resetBoard(id):
    if loadBoard(id, True) == "Invalid ID":
        return False
    
    updateBoard(id, "---------")
    return True