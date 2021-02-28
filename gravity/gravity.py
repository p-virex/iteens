import sys
import pygame

# инициализируем pygame
pygame.init()
# установим размер окна, сразу же распакуем ширину и высоту
size = width, height = 1200, 800
# установим скорость по Х и У
x, y = 15, 1
# установим гравитацию (условно) скорость с которой шарик будет прижиматься к полу
G = 10
# создаим холст с нужным размером
screen = pygame.display.set_mode(size)
# загрузим изображение шарика
ball = pygame.image.load("ball.PNG")
ball_rect = ball.get_rect()

clock = pygame.time.Clock()


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # каждый кадр, прибавляем к вертикальной скорости нашу константу гравитации
    y += G
    # двигаем шарик по вектору
    ball_rect = ball_rect.move((x, y))
    # если сталкиваемся с бордюром, то меняем вектор на противоположный
    if ball_rect.left < 0 or ball_rect.right > width:
        x = -x
    if ball_rect.bottom > height:
        y = -y
    # если вектор мячика превышает границу бордюра, то остановим его установив нижниюю координату в виде высоты
    ball_rect.bottom = min(ball_rect.bottom, height)
    # обновляем экран заливая его черным
    screen.fill((0, 0, 0))
    # рисуем мяч в новых координатах
    screen.blit(ball, ball_rect)
    # обновляем холст
    pygame.display.flip()
