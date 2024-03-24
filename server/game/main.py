import sys
import pygame
from board import Board
from minimaxboard import MinimaxBoard

pygame.init()

COLORS = {
    "lines": (0, 0, 0),
    "reset_button": (250, 130, 80),
    "background": (255, 255, 255),
    "p_one": (0, 0, 255),
    "p_two": (255, 0, 0),
}
SIZE = 150  # Size of one box


def main():
    board = None
    if sys.argv[-1] == "BOT-OFF":
        board = Board(SIZE, COLORS)
    else:
        board = MinimaxBoard(SIZE, COLORS)

    # setup window
    win = pygame.display.set_mode((SIZE * 4, SIZE * 4))
    pygame.display.set_caption("Tic Tac Toe")

    # build reset button surface
    font = pygame.font.SysFont("Comic Sans MS", SIZE // 4)
    textSurface = font.render("Reset", False, COLORS["lines"])
    buttonSurface = pygame.Surface((textSurface.get_width() * 2, textSurface.get_height() * 2))
    buttonSurface.fill(COLORS["reset_button"])
    buttonSurface.blit(textSurface, (buttonSurface.get_width() // 2 - textSurface.get_width() // 2,
             buttonSurface.get_height() // 2 - textSurface.get_height() // 2))

    # coordinates to draw each component
    boardCoords = (SIZE // 2, SIZE, SIZE * 3, SIZE * 3)
    resetCoords = (SIZE * 4 - buttonSurface.get_width(), 0,
             buttonSurface.get_width(), buttonSurface.get_height())
    turnCoords = (10, 10)
    
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                handleClick(board, mouse, resetCoords, boardCoords)

            if event.type == pygame.KEYDOWN:
                # if space bar pressed then reset game
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    board = Board(SIZE, COLORS)

        # draw
        win.fill(COLORS["background"])
        win.blit(board.getGameSurface(), boardCoords[:2])
        win.blit(buttonSurface, resetCoords[:2])
        win.blit(board.getTurnSurface(), turnCoords)
        pygame.display.update()


# checks if (x, y) is within either rect and responds accordingly. If it is
# in the reset box, the board is reset to its original state. If the click is
# in the board rect and the game is not over, the method will attempt to place
# a piece in the correct square.
def handleClick(board, mouse, resetCoords, boardCoords):
    # game not over and click is on the board
    if withinRect(mouse, boardCoords) and board.evaluate() is None:
        gameX = (mouse[0] - boardCoords[0]) // board.size
        gameY = (mouse[1] - boardCoords[1]) // board.size
        board.play((gameX, gameY))
    elif withinRect(mouse, resetCoords): # click is on the reset button
        board.reset()

# returns true if (x, y) is within rect, false otherwise
# x: x coordinate
# y: y coordinate
# rect: rectangle bounds given by (x, y, width, height), x, y is top left corner
def withinRect(pos, rect):
    return ((pos[0] > rect[0] and pos[1] > rect[1]) and
            (pos[0] < rect[0] + rect[2] and pos[1] < rect[1] + rect[3]))


if __name__ == "__main__":
    main()