from Tetris import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        mixer.init()
        mixer.music.load('Original Tetris theme (Tetris Soundtrack).mp3')
        mixer.music.play(loops=-1)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self.screen)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.tetris.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            key_input = pg.key.get_pressed()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.tetris.new_rotation()
            if key_input[pg.K_a]:
                self.tetris.left()
            if key_input[pg.K_d]:
                self.tetris.right()
            if key_input[pg.K_s]:
                self.tetris.down()

    def run(self):
        while self.tetris.game_on:
            self.update()
            self.check_events()
