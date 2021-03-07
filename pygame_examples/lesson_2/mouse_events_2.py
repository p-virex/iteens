

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

LEFT_BUTTON = 1
WHEEL_BUTTON = 2

game = True
screen.fill((30, 30, 30))
while game:
    clock.tick(120)

    pygame.display.set_caption(str(int(clock.get_fps())))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        pygame.draw.circle(screen, (255, 0, 0), pos, 5)

    pygame.display.update()

pygame.quit()
