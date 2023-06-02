import pygame as pg
from constants import *

tetrominos = [
    [
        BLUE, BLUE, BLUE, BLUE,
        EMPTY, EMPTY, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY
    ],
    [
        YELLOW, YELLOW, YELLOW, EMPTY,
        YELLOW, YELLOW, YELLOW, EMPTY,
        YELLOW, YELLOW, YELLOW, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY
    ],
    [
        PURPLE, PURPLE, PURPLE, EMPTY,
        EMPTY, PURPLE, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY
    ],
    [
        ORANGE, EMPTY, EMPTY, EMPTY,
        ORANGE, EMPTY, EMPTY, EMPTY,
        ORANGE, EMPTY, EMPTY, EMPTY,
        ORANGE, ORANGE, EMPTY, EMPTY
    ],
    [
        EMPTY, EMPTY, EMPTY, EMPTY,
        EMPTY, GREEN, GREEN, EMPTY,
        GREEN, GREEN, EMPTY, EMPTY,
        EMPTY, EMPTY, EMPTY, EMPTY
    ]
]


# Create board with borders

board = []

for square in range(0, PIXELS+1):
    if (square+1) % 12 == 0:
        board.append(GREY)
    elif square % 12 == 0:
        board.append(GREY)
    elif square >= PIXELS-ORIGINAL_RES[0]:
        board.append(GREY)
    else:
        board.append(EMPTY)


game_on = True
score = 0

screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

pg.display.set_caption("Tetris")


def run():
    pg.init()
    while game_on:
        pg.display.flip()
        clock.tick(FPS)
        screen.fill(EMPTY)
        draw_board()


def draw_board():
    x, y = 0, 0
    for square_index in range(0, len(board)):
        pg.draw.rect(screen, board[square_index], pg.Rect((x, y), SQUARE_SIZE))
        x += SQUARE_SIDE
        if (square_index+1) % 12 == 0 and square_index != 0:
            y += SQUARE_SIDE
            x = 0


def rotate():
    pass


def move():
    pass


def collisions():
    pass


def lines():
    pass


def user_input():
    pass


def new_tetromino():
    pass
