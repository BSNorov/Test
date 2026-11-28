import pygame as pg
import random

pg.init()
W, H = 480, 640
display = pg.display.set_mode((W, H))

GRAVITY = 1
JUMP = -30
PLATFORM_WIDTH = 105
MIN_GAP = 90
MAX_GAP = 180

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_left = pg.image.load('img/doodle_left.png')
        self.image = self.image_left
        self.image_right = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(W // 2, H // 2))
        self.speed = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
            self.image = self.image_left
        if keys[pg.K_RIGHT]:
            self.rect.x += 5
            self.image = self.image_right

        if self.rect.left > W:
            self.rect.left = 0
        if self.rect.right < 0:
            self.rect.right = W

        self.speed += GRAVITY
        self.rect.y += self.speed

    def draw(self):
        if self.rect.y > H:
            self.rect.y = H // 2
            # draw_text('Game Over', W // 2 - 30, H // 2 - 10)
        else:
            display.blit(self.image, self.rect)

class BasePlatform(pg.sprite.Sprite):
    def __init__(self, x, y, sprite):
        super().__init__()
        self.image = pg.image.load(sprite)
        self.rect = self.image.get_rect(topleft=(x, y))

    def on_collision(self, player):
        player.speed = JUMP

    def update(self):
        if self.rect.top > H:
            self.kill()

class NormalPlatform(BasePlatform):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/green.png')

class SpringPlatform(BasePlatform):
    ...

class BreakablePlatform(BasePlatform):
    ...

class MovingPlatform(BasePlatform):
    ...

platforms = pg.sprite.Group()

def spawn_platform():
    platform = platforms.sprites()[-1]
    y = platform.rect.y - random.randint(MIN_GAP, MAX_GAP)
    x = random.randint(0, W - PLATFORM_WIDTH)
    types = [
         # MovingPlatform, # BreakablePlatform, # SpringPlatform,
        NormalPlatform
    ]
    Plat = random.choice(types)
    platform = Plat(x, y)
    platforms.add(platform)

doodle = Player()

platform = NormalPlatform(W // 2 - PLATFORM_WIDTH // 2, H - 50)
platforms.add(platform)

def main():
    while True:
        #1
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return
        #2
        doodle.update()
        platforms.update()
        if pg.sprite.spritecollide(doodle, platforms, False):
            doodle.speed = JUMP
        if len(platforms) < 25:
            spawn_platform()
        if doodle.speed < 0 and doodle.rect.bottom < H / 2:
            doodle.rect.y -= doodle.speed
            for platform in platforms:
                platform.rect.y -= doodle.speed
        #3
        display.fill('white')
        platforms.draw(display)
        doodle.draw()
        pg.display.update()
        pg.time.delay(1000 // 60)

if __name__ == '__main__':
    main()
