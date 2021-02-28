from random import choice

import pygame
import sys

pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
x = width
y = height-300
speed = 2
size = 75
clock = pygame.time.Clock()


while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, size, size))
    pygame.display.update()

    # квадрат будет уходить за правую стенку и взвращаться слева
    if x < 0 - size:
        x = width
        y = height - choice([50, 100, 150, 200, 250, 300, 356, 400])
    else:
        x -= 2

    clock.tick(120)
