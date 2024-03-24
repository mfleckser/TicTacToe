import pygame


class Board:
    def __init__(self, size=0, colors={}, other=None):
        if other is not None: # copy constructor
            self.turn = other.turn
            self.size = other.size
            self.colors = other.colors
            self.board = [i for i in other.board]
        else:
            self.board = [0 for _ in range(9)]
            self.turn = 1
            self.size = size
            self.colors = colors

    # returns pygame surface including game board and all pieces
    def getGameSurface(self):
        surface = pygame.Surface((self.size * 3, self.size * 3))

        surface.fill(self.colors["background"])

        pygame.draw.line(surface, self.colors["lines"],
                         (self.size, 0), (self.size, self.size * 3), 6)
        pygame.draw.line(surface, self.colors["lines"],
                         (self.size * 2, 0), (self.size * 2, self.size * 3), 6)
        pygame.draw.line(surface, self.colors["lines"],
                         (0, self.size), (self.size * 3, self.size), 6)
        pygame.draw.line(surface, self.colors["lines"],
                         (0, self.size * 2), (self.size * 3, self.size * 2), 6)

        for i, piece in enumerate(self.board):
            if piece != 0:
                self.drawPiece(surface, (i % 3, i // 3), piece)

        self.drawResult(surface)

        pygame.draw.rect(surface, (0, 0, 0), (0, -50, 50, 50))

        return surface

    # draws individual piece at position onto surface
    def drawPiece(self, surface, pos, id):
        upperLeft = [pos[0] * self.size, pos[1] * self.size]

        if id == 1:  # draw X
            pygame.draw.line(surface, self.colors["p_one"],
                (upperLeft[0] + 30, upperLeft[1] + 15),
                (upperLeft[0] + self.size - 30, upperLeft[1] + self.size - 15), 20)
            pygame.draw.line(surface, self.colors["p_one"],
                (upperLeft[0] + self.size - 30, upperLeft[1] + 15),
                (upperLeft[0] + 30, upperLeft[1] + self.size - 15), 20)
        elif id == -1:  # draw O
            pygame.draw.circle(surface, self.colors["p_two"],
                (upperLeft[0] + self.size // 2, upperLeft[1] + self.size // 2),
                self.size // 2 - 15, 20)
            
    # checks if the game is over and displays appropriate message onto surface
    def drawResult(self, surface):
        result = self.evaluate()
        if result is not None: # game over
            s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            font = pygame.font.SysFont("Comic Sans MS", self.size // 2)
            s.fill((100, 100, 100, 200))

            text = ""
            color = None

            if result == 1:
                text = "X Wins!"
                color = self.colors["p_one"]
            elif result == -1:
                text = "O Wins!"
                color = self.colors["p_two"]
            else:
                text = "It's a Tie!"
                color = self.colors["lines"]

            bg = [i // 3 for i in color] if result else (200, 200, 200)

            textSurface = font.render(text, False, color, bg)
            pos = (
                self.size * 3 / 2 - textSurface.get_width() / 2,
                self.size * 3 / 2 - textSurface.get_height() / 2,
            )
            s.blit(textSurface, pos)
            surface.blit(s, (0, 0))

    # returns surface with rendered text displaying who's turn it is
    def getTurnSurface(self):
        font = pygame.font.SysFont("Comic Sans MS", self.size // 3)
        player = "X" if self.turn == 1 else "O"
        turnSurface = font.render(player + "'s Turn", False, self.colors["lines"])
        return turnSurface
            
    # returns the id of the piece at the given 2D location
    def get(self, x, y):
        return self.board[3 * y + x]
    
    # if the space is available, this method will update the board
    # and switch the current player
    # returns True if move is made, False is spot is taken
    def play(self, pos):
        if self.board[3 * pos[1] + pos[0]] == 0:
            self.board[3 * pos[1] + pos[0]] = self.turn
            self.turn *= -1
            return True
        return False
    
    # resets board to original state
    def reset(self):
        self.board = [0 for _ in range(9)]
        self.turn = 1
    
    # checks if the game is finish, and if so the winner
    # returns- tie: 0, X: 1, O: -1, Game in progress: None
    def evaluate(self):
        winner = None
        if all(self.board):
            winner = 0
        for i in range(3):
            if abs(sum(self.board[i * 3: i * 3 + 3])) == 3:  # rows
                winner = self.board[i * 3]
            if abs(sum(self.board[i: i + 7: 3])) == 3:  # columns
                winner = self.board[i]
        if (
            (self.board[0] == self.board[4] and self.board[4] == self.board[8])
            or (self.board[2] == self.board[4] and self.board[4] == self.board[6])
        ) and self.board[4] != 0:
            winner = self.board[4]
        return winner

    def childBoards(self):
        for i, val in enumerate(self.board):
            if val == 0:
                new_board = Board(other=self)
                new_board.play((i % 3, i // 3))
                yield (new_board, i)  # return child board and changed index