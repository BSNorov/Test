import pygame

pygame.init()

W, H = 800, 600  # W - width (ширина), H - height (высота)
display = pygame.display.set_mode((W, H))

class Crosshair():
    def __init__(self):
        self.sprite = pygame.Surface([80, 80])
        self.sprite.fill('red')
        self.hitbox = self.sprite.get_rect()

    def draw(self):
        display.blit(self.sprite, self.hitbox)

    def move(self):
        self.hitbox.center =  pygame.mouse.get_pos()

class Target():
    def __init__(self):
        ...

    def ???():
        ...

    def ???():
        ...

crosshair = Crosshair()



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
        # ------------------
        # 3) Отрисовка обновленного состояния
        display.fill('black')
        crosshair.draw()
        pygame.display.update()
        pygame.time.delay(1000 // 60)

main()
