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

board = [[EMPTY for row in range(10)] for column in range(24)]

game_on = True
score = 0

while game_on:
    pass


def draw_board():
    pass


def rotate():
    pass


def move():
    pass


def collisions():
    pass


def lines():
    pass
