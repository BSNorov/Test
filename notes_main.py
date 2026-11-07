import pygame
import random

pygame.init()

W, H = 800, 600  # W - width (ширина), H - height (высота)
display = pygame.display.set_mode((W, H))

def draw_score(score):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, 48)
    render = font.render(str(score), 1, 'green')
    render_hitbox = render.get_rect(topleft=(0, 0))
    display.blit(render, render_hitbox)

class Crosshair():
    def __init__(self):
        self.sprite = pygame.image.load('crosshair_small.png')
        self.hitbox = self.sprite.get_rect()

    def draw(self):
        display.blit(self.sprite, self.hitbox)

    def move(self):
        self.hitbox.center =  pygame.mouse.get_pos()

class Target():
    def __init__(self):
        self.sprite = pygame.image.load('target_small.png')
        self.hitbox = self.sprite.get_rect()
        self.hits_number = 0

    def move(self):
        if self.is_clicked(crosshair):
            w = self.hitbox.width
            h = self.hitbox.height
            self.hitbox.x = random.randint(0, W - w)
            self.hitbox.y = random.randint(0, H - h)
            self.hits_number += 1


    def draw(self):
        display.blit(self.sprite, self.hitbox)

    def is_clicked(self, crosshair: Crosshair):
        if where_mouse_pressed(0):
            horiz = self.hitbox.left < crosshair.hitbox.centerx < crosshair.hitbox.right
            vert = self.hitbox.top < crosshair.hitbox.centery < crosshair.hitbox.bottom
            return horiz and vert

crosshair = Crosshair()
target = Target()


def is_key_pressed(key):
    return pygame.key.get_pressed()[key]

def where_mouse_pressed(mouse_key):
    buttons = pygame.mouse.get_pressed(num_buttons=5)
    if buttons[mouse_key]:
        return pygame.mouse.get_pos()

def main():
    while True:
        # 1) Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        # ------------------
        # 2) Обновление состояния игры
        crosshair.move()
        target.move()
        # ------------------
        # 3) Отрисовка обновленного состояния
        display.fill('black')
        draw_score(target.hits_number)
        target.draw()
        crosshair.draw()
        pygame.display.update()
        pygame.time.delay(1000 // 60)

main()
