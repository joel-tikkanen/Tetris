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

for square in range(0, PIXELS):
    if (square + 1) % 12 == 0:
        board.append(GREY)
    elif square % 12 == 0:
        board.append(GREY)
    elif square >= PIXELS - BOARD_WIDTH:
        board.append(GREY)
    else:
        board.append(EMPTY)

score = 0
left_top_pos = (RES[0] / 2, 100)
game_on = True

screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

pg.display.set_caption("Tetris")


def run():
    global game_on, score, left_top_pos
    pg.init()
    while game_on:
        pg.display.flip()
        clock.tick(FPS)
        screen.fill(EMPTY)
        draw_board()
        draw_tetromino(left_top_pos, tetrominos[2])


def draw_board():
    x, y = 0, 0
    for square_index in range(0, len(board)):
        pg.draw.rect(screen, board[square_index], pg.Rect((x, y), SQUARE_SIZE))
        x += SQUARE_SIDE
        if (square_index + 1) % 12 == 0 and square_index != 0:
            y += SQUARE_SIDE
            x = 0


def rotate(rotation_number):
    pass


def move(ltop, direction):
    return ltop + BOARD_WIDTH + direction


def collisions():
    pass


def lines():
    pass


def user_input():
    pass


def draw_tetromino(ltop, tetromino):
    px, py = ltop
    for x in range(0, 4):
        for y in range(0, 4):
            pg.draw.rect(screen, tetromino[x*4+y], pg.Rect((py + y * SQUARE_SIDE, px + x * SQUARE_SIDE), SQUARE_SIZE))
            # Border
            pg.draw.rect(screen, EMPTY, pg.Rect((py + y * SQUARE_SIDE, px + x * SQUARE_SIDE), SQUARE_SIZE), 1)

