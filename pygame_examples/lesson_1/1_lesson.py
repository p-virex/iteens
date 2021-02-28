import time

import pygame
import sys

pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
x = y = 0
speed_y = speed_x = 2
clock = pygame.time.Clock()


while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    # screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 75, 75))
    pygame.display.update()

    # квадрат будет уходить за правую стенку и взвращаться слева
    if x > width-75:
        x = 1200-75
        speed_x = -2
    if x < 0:
        x = 0
        speed_x = 2
    x += speed_x

    # квадрат будет отталкивать от верхней стенки и от нижней
    if y > height-75:
        y = 800-75
        speed_y = -2
    if y < 0:
        y = 0
        speed_y = 2
    y += speed_y
    pygame.display.set_caption(str(int(clock.get_fps())))
    # clock.tick(60)
