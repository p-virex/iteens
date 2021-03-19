from random import choice

import pygame as pg


def draw_text(msg, pos, size=25):
    font = pg.font.Font(None, size)
    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, pos)


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
size_rect = [i for i in range(190, 270) if i % 10 == 0]

x = 500
y = choice(size_rect)
y_vert = y - 120
score = 0
while game is True:
    clock.tick(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    if x < 150 + (size - 10) and x + 30 > 150 - (size - 10):
        # если шарик над платформой
        if y_bird + (size - 10) > y or y_bird - (size - 10) < y_vert:
            # если шарик цепляет платформу, то проиграли
            game = False
        if x == 150:
            score += 1
            print(score)

    screen.fill(bg_color)
    pg.draw.circle(screen, (255, 0, 0), (150, y_bird), size)
    pg.draw.rect(screen, (0, 255, 0), (x, y, 30, 400))
    pg.draw.rect(screen, (0, 255, 255), (x, 0, 30, y_vert))

    draw_text(f'{int(clock.get_fps())}', (10, 10))
    draw_text(f'{score}', (480, 10))
    pressed_keys = pg.key.get_pressed()
    if pressed_keys[pg.K_SPACE]:
        y_bird -= 5

    y_bird += 2
    x -= 2
    if x <= 0 - 30:
        x = 500
        y = choice(size_rect)
        y_vert = y - 150

    pg.display.update()

draw_text(f'Вы проиграли! Ваш счет: {score}', (150, 400/2))
pg.display.update()
pg.time.delay(5000)
pg.quit()
