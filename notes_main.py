import pygame as pg
import random

pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
PIPE_WIDTH = 80
PIPE_GAP = 250
SPEED = 5
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Bird(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('bird.png')
        self.image = pg.transform.scale(
            self.image, size=[BIRD_WIDTH, BIRD_HEIGHT]
        )
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        )
        self.gravity = 1
        self.lift = -15
        self.velocity = 0

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = self.lift

class Pipe(pg.sprite.Sprite):
    TOP = 1
    BOTTOM = 2

    def __init__(self, type, gap_start):
        super().__init__()
        self.image = pg.image.load('pipe.png')
        self.image = pg.transform.scale(
            self.image, [PIPE_WIDTH, self.image.get_height() / 2]
        )
        if type == self.TOP:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(
                bottomleft=(SCREEN_WIDTH, gap_start)
            )
        elif type == self.BOTTOM:
            self.rect = self.image.get_rect(
                topleft=(SCREEN_WIDTH, gap_start + PIPE_GAP)
            )

    def update(self):
        self.rect.x -= SPEED
        if self.rect.right < 0:
            self.kill()


bird = Bird()
pipes = pg.sprite.Group()

def make_pipes():
    gap_start = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
    top_pipe = Pipe(Pipe.TOP, gap_start)
    bottom_pipe = Pipe(Pipe.BOTTOM, gap_start)
    pipes.add(top_pipe, bottom_pipe)

make_pipes()

def main():
    while True:
        # 1
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    bird.jump()

        # 2
        bird.update()
        pipes.update()
        if pipes.sprites()[-1].rect.x <= SCREEN_WIDTH / 2:
            make_pipes()
        # 3
        screen.fill(WHITE)
        pipes.draw(screen)
        screen.blit(bird.image, bird.rect)
        pg.display.update()
        pg.time.delay(30)

main()
