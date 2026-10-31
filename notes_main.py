import pygame

pygame.init()

W, H = 800, 600  # W - width (ширина), H - height (высота)
display = pygame.display.set_mode((W, H))

image = pygame.Surface([80, 80])
image.fill('red')
rect = image.get_rect()


def main():
    while True:
        # 1) Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # ------------------
        # 2) Обновление состояния игры
        # ------------------
        # 3) Отрисовка обновленного состояния
        display.blit(image, rect)
        pygame.display.update()
        pygame.time.delay(1000 // 60)

main()
