import sys

import pygame as pg
from constants import *
from random import randint
from pygame import mixer


class Tetris:
    def __init__(self, screen):

        self.screen = screen
        self.board = []
        self.init_board()
        self.score = 0
        self.game_on = True

        self.rotation = 0
        self.tetromino_index = 0
        self.current_tetromino = tetrominos[self.tetromino_index][self.rotation]

        self.direction = (0, 0)
        self.left_top_pos = START_POS

        self.k = 0

    def init_board(self):
        for square in range(0, PIXELS):
            if (square + 1) % 12 == 0:
                self.board.append(GREY)
            elif square % 12 == 0:
                self.board.append(GREY)
            elif square >= PIXELS - BOARD_WIDTH:
                self.board.append(GREY)
            else:
                self.board.append(EMPTY)

    def draw_score(self):
        font = pg.font.Font('freesansbold.ttf', 15)
        text = font.render(f"score: {self.score}", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (180, 40)
        self.screen.blit(text, text_rect)

    def rotate(self, rotation):
        t = tetrominos[self.tetromino_index][rotation]
        if self.can_fit(self.left_top_pos, t):
            return True
        return False

    def set_current(self):
        self.current_tetromino = tetrominos[self.tetromino_index][self.rotation]

    def move_down(self, row):
        for i in range(row * BOARD_WIDTH + BOARD_WIDTH, BOARD_WIDTH, -1):
            i1 = i
            i2 = i1 - BOARD_WIDTH
            self.board[i1] = self.board[i2]

    def delete_rows(self, rows):
        for row in rows:
            for i in range(1, BOARD_WIDTH - 1):
                self.board[row * BOARD_WIDTH + i] = EMPTY
        for row in rows:
            self.move_down(row)
        return len(rows) ** 2 * 100

    def check_rows(self):
        rows = []
        for row in range(0, BOARD_HEIGHT):
            if EMPTY not in self.board[row * BOARD_WIDTH:(row * BOARD_WIDTH + BOARD_WIDTH)]:
                if row != 25:
                    rows.append(row)
        return rows

    def fit_piece(self):
        board_index = self.to_board_index(self.left_top_pos)
        for x in range(0, 4):
            for y in range(0, 4):
                ind = board_index + x * BOARD_WIDTH + y
                if ind < len(self.board):
                    if self.board[ind] == EMPTY:
                        self.board[ind] = self.current_tetromino[x * 4 + y]

    @staticmethod
    def to_board_index(left_top_pos):
        px, py = left_top_pos
        return BOARD_WIDTH * py + px

    def can_fit(self, left_top_pos, tetromino):
        i = self.to_board_index(left_top_pos)
        for x in range(0, 4):
            for y in range(0, 4):
                ind = i + x * BOARD_WIDTH + y
                if ind < len(self.board):
                    if self.board[ind] != EMPTY and tetromino[x * 4 + y] != EMPTY:
                        return False
        return True

    def draw_tetromino(self):
        px, py = self.left_top_pos

        for x in range(0, 4):
            for y in range(0, 4):
                if self.current_tetromino[x * 4 + y] != EMPTY:
                    pg.draw.rect(self.screen, self.current_tetromino[x * 4 + y],
                                 pg.Rect((SCALE * px + y * SQUARE_SIDE, SCALE * py + x * SQUARE_SIDE), SQUARE_SIZE))
                    # Border
                    pg.draw.rect(self.screen, EMPTY,
                                 pg.Rect((SCALE * px + y * SQUARE_SIDE, SCALE * py + x * SQUARE_SIDE), SQUARE_SIZE), 1)

    def draw_board(self):
        x, y = 0, 0
        for square_index in range(0, len(self.board)):
            pg.draw.rect(self.screen, self.board[square_index], pg.Rect((x, y), SQUARE_SIZE))
            pg.draw.rect(self.screen, EMPTY, pg.Rect((x, y), SQUARE_SIZE), 1)
            x += SQUARE_SIDE
            if (square_index + 1) % 12 == 0 and square_index != 0:
                y += SQUARE_SIDE
                x = 0

    def down(self):
        self.direction = (0, 1)

    def left(self):
        self.direction = (-1, 0)

    def right(self):
        self.direction = (1, 0)

    def new_rotation(self):
        if self.rotation < len(tetrominos[self.tetromino_index]) - 1 and self.rotate(self.rotation + 1):
            self.rotation += 1
            self.set_current()
        elif self.rotate(0):
            self.rotation = 0
            self.set_current()

    def check_pos(self):
        x, y = self.left_top_pos
        if not self.can_fit((x, y + 1), self.current_tetromino):
            self.fit_piece()
            if self.left_top_pos[1] < 5:
                self.game_on = False
            self.left_top_pos = START_POS
            r = randint(0, 4)
            rotation = 0
            self.current_tetromino = tetrominos[r][rotation]
            self.tetromino_index = r
            return True
        return False

    def update(self):
        self.draw_board()
        self.draw_score()
        if self.check_pos():
            return True
        elif self.k == 10:
            self.k = 0
            self.left_top_pos = self.left_top_pos[0], self.left_top_pos[1] + 1
        self.k += 1
        new_pos = self.left_top_pos[0] + self.direction[0], self.left_top_pos[1] + self.direction[1]
        if self.can_fit(new_pos, self.current_tetromino):
            self.left_top_pos = new_pos
        self.direction = (0, 0)
        self.draw_tetromino()
        self.score += self.delete_rows(self.check_rows())
