from board import Board
import pygame


class MinimaxBoard(Board):
    def __init__(self, size=0, colors={}, other=None):
        super().__init__(size, colors, other)

    # Overrides superclass method
    # First plays in position, then calculates the optimal next
    # move and plays in that position as well.
    def play(self, pos):
        super().play(pos)
        if self.evaluate() is None:
            super().play(self.findBestMove())

    # recursive minimax algorithm to determine "value" of a given board
    # depending on whose turn it is
    @staticmethod
    def minimax(board):
        if board.evaluate() is not None:
            return board.evaluate()
        if board.turn == 1:
            value = float("-inf")
            for child, _ in board.childBoards():
                value = max(value, MinimaxBoard.minimax(child))
            return value
        else:
            value = float("inf")
            for child, _ in board.childBoards():
                value = min(value, MinimaxBoard.minimax(child))
            return value


    def findBestMove(self):
        index = None
        if self.turn == -1:
            best = float("inf")
            for child, i in self.childBoards():
                score = MinimaxBoard.minimax(child)
                if score < best:
                    best = score * 1
                    index = i
        else:
            best = float("-inf")
            for child, i in self.childBoards():
                score = MinimaxBoard.minimax(child)
                if score > best:
                    best = score * 1
                    index = i
        
        return (index % 3, index // 3)
    
    # Overrides superclass method
    # Returns surface with rendered text saying "You are X"
    def getTurnSurface(self):
        font = pygame.font.SysFont("Comic Sans MS", self.size // 3)
        turnSurface = font.render("You are X", False, self.colors["lines"])
        return turnSurface