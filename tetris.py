import sys

import pygame as pg
from constants import *
from random import randint
from pygame import mixer
from pygame.locals import *

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

start_pos = int(BOARD_WIDTH // 3), int(BOARD_HEIGHT // 9)
print(start_pos)
left_top_pos = start_pos
game_on = True
rotation = 0
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
direction_x = 0
direction_y = 0
t_i = 0

pg.display.set_caption("Tetris")
mixer.init()
mixer.music.load('Original Tetris theme (Tetris Soundtrack).mp3')
mixer.music.play(loops=-1)


def run():
    global game_on, score, left_top_pos, direction_x, direction_y, rotation, t_i
    k = 0
    pg.init()

    tetromino = tetrominos[0][0]
    t_i = 0

    while game_on:
        pg.display.flip()
        clock.tick(FPS)
        screen.fill(EMPTY)
        draw_board()
        draw_score()
        new_pos = left_top_pos

        tetromino = tetrominos[t_i][rotation]
        if not can_fit((new_pos[0], new_pos[1] + 1), tetromino, 2):
            fit_piece(tetromino, left_top_pos)
            if left_top_pos[1] < 5:
                print("END")
                break
            left_top_pos = start_pos
            r = randint(0, 4)
            rotation = 0
            tetromino = tetrominos[r][rotation]
            t_i = r
            continue
        elif k == 10:
            k = 0
            left_top_pos = left_top_pos[0], left_top_pos[1] + 1

        new_pos = left_top_pos[0] + direction_x, left_top_pos[1] + direction_y
        if can_fit(new_pos, tetromino, 2):
            left_top_pos = new_pos

        k += 1
        direction_x = 0
        direction_y = 0
        draw_tetromino(left_top_pos, tetromino)
        delete_rows(check_rows())
        user_input()


def draw_board():
    x, y = 0, 0
    for square_index in range(0, len(board)):
        pg.draw.rect(screen, board[square_index], pg.Rect((x, y), SQUARE_SIZE))
        pg.draw.rect(screen, EMPTY, pg.Rect((x, y), SQUARE_SIZE), 1)
        x += SQUARE_SIDE
        if (square_index + 1) % 12 == 0 and square_index != 0:
            y += SQUARE_SIDE
            x = 0


def lines():
    pass


def user_input():
    global rotation, left_top_pos, direction_x, direction_y
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        key_input = pg.key.get_pressed()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                if rotation < len(tetrominos[t_i]) - 1 and rotate(left_top_pos, t_i, rotation + 1):
                    rotation += 1
                elif rotate(left_top_pos, t_i, 0):
                    rotation = 0

        if key_input[pg.K_a]:
            # right
            direction_x = -1
        if key_input[pg.K_d]:
            # left
            direction_x = 1
        if key_input[pg.K_s]:
            # right
            direction_y = 1


def draw_tetromino(ltop, tetromino):
    px, py = ltop
    for x in range(0, 4):
        for y in range(0, 4):
            if tetromino[x * 4 + y] != EMPTY:
                pg.draw.rect(screen, tetromino[x * 4 + y],
                             pg.Rect((SCALE * px + y * SQUARE_SIDE, SCALE * py + x * SQUARE_SIDE), SQUARE_SIZE))
                # Border
                pg.draw.rect(screen, EMPTY,
                             pg.Rect((SCALE * px + y * SQUARE_SIDE, SCALE * py + x * SQUARE_SIDE), SQUARE_SIZE), 1)


def can_fit(ltop, tetromino, rotation_n):
    i = to_board_index(ltop)
    for x in range(0, 4):
        for y in range(0, 4):
            ind = i + x * BOARD_WIDTH + y
            if ind < len(board):
                if board[ind] != EMPTY and tetromino[x * 4 + y] != EMPTY:
                    return False
    return True


def to_board_index(ltop):
    px, py = ltop
    return BOARD_WIDTH * py + px


def fit_piece(piece, ltop):
    global board
    board_index = to_board_index(ltop)
    for x in range(0, 4):
        for y in range(0, 4):
            ind = board_index + x * BOARD_WIDTH + y
            if ind < len(board):
                if board[ind] == EMPTY:
                    board[ind] = piece[x * 4 + y]


def check_rows():
    rows = []
    for row in range(0, BOARD_HEIGHT):
        if EMPTY not in board[row * BOARD_WIDTH:(row * BOARD_WIDTH + BOARD_WIDTH)]:
            if row != 25:
                rows.append(row)
    return rows


def delete_rows(rows):
    global score
    s = 0
    for row in rows:
        for i in range(1, BOARD_WIDTH - 1):
            board[row * BOARD_WIDTH + i] = EMPTY
        move_down()
        s += 1
    score += s ** 2 * 100


def move_down():
    for i in range(BOARD_WIDTH, len(board) - BOARD_WIDTH):
        j = len(board) - i
        k = j - BOARD_WIDTH
        board[j] = board[k]


def rotate(ltop, index, r_number):
    t = tetrominos[index][r_number]
    if can_fit(ltop, t, r_number):
        return True
    return False


def draw_score():
    font = pg.font.Font('freesansbold.ttf', 15)
    text = font.render(f"score: {score}", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (180, 40)
    screen.blit(text, text_rect)
