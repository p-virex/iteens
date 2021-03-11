from random import choice

import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 400))
clock = pg.time.Clock()
bg_color = (207, 199, 223)
screen.fill(bg_color)
game = True
f1 = pg.font.Font(None, 36)

size = 30
y_bird = 100
i = 150
size_rect = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# y_rect, x_rect =
x = 500
y = choice(size_rect)
score = 0
while game is True:
    clock.tick(50)
    text1 = f1.render(f'{clock.get_fps()}', True, (0, 0, 0))
    screen.blit(text1, (10, 10))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    if x < 150 + size and x + 30 > 150 - size:
        # если шарик над платформой
        if y_bird + size > y:
            # если шарик цепляет платформу, то проиграли
            game = False
            pg.time.delay(3000)
        if x == 150:
            score += 1
            print(score)

    screen.fill(bg_color)
    pg.draw.circle(screen, (255, 0, 0), (150, y_bird), size)
    pg.draw.rect(screen, (0, 255, 0), (x, y, 30, 400))
    pressed_keys = pg.key.get_pressed()
    if pressed_keys[pg.K_SPACE]:
        y_bird -= 15

    y_bird += 3
    x -= 2
    if x <= 0 - 30:
        x = 500
        y = choice(size_rect)

    pg.display.update()

pg.quit()
