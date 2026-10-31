import pygame

pygame.init()

W, H = 800, 600  # W - width (ширина), H - height (высота)
display = pygame.display.set_mode((W, H))

image = pygame.Surface([80, 80])
image.fill('red')
rect = image.get_rect()

image2 = pygame.Surface([160, 160])
image2.fill('green')
rect2 = image2.get_rect()

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

        if is_key_pressed(pygame.K_d):
            rect2.x += 5

        if is_key_pressed(pygame.K_s):
            rect2.y += 5
        # ------------------
        # 2) Обновление состояния игры
        # ------------------
        # 3) Отрисовка обновленного состояния
        display.fill('black')
        display.blit(image2, rect2)
        display.blit(image, rect)
        pygame.display.update()
        pygame.time.delay(1000 // 60)

main()
