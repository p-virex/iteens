"""
Цель: добавить в сетку двигающиеся фигуры.
Сделать фигуры на основе координатной сетки и определить центр вращения каждой фигуры: coord_grid.png

Всего 7 возможных фигур, каждая состоит из 4 квадратов и для каждой нудно ее описать в виде массива координат,
где первый элемент это центр вращения.

Добавить управление и анимацию фигурами
"""
from copy import deepcopy
from random import choice

import pygame

# игровое поле 10 на 20 квадратов
W, H = 10, 20
#  размер квадрата
TILE = 45
# размер окна
GAME_RES = W * TILE, H * TILE

pygame.init()
game_screen = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

grid = []

# делаем сетку из квадратов на игрвоом поле
# итерируемся по высоте и внутри берем каждый квадрат по ширине и создаем
# rect с своими координатами помещая их в список
for y in range(H):
    for x in range(W):
        rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
        grid.append(rect)

# координаты фигур, пример coord_grid.png
# первый кортеж, центр вращения
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)], [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)], [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)], [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

# массив объектов rect описывающий фигуры
figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]

# можно распечатать координаты фигуры в сетке
# for fig in figures:
#     for f in fig:
#         print(f.x, f.y)
#     print('*'*20)
# 4 1  палочка
# 3 1   ****
# 5 1
# 6 1
# ********************
# 5 0 квадрат
# 4 0   **
# 4 1   **
# 5 1
# ********************
# 4 1
# 4 2   *
# 5 1  **
# 5 0  *
# ********************
# 5 1
# 4 1  *
# 5 2  **
# 4 0   *
# ********************
# 5 1
# 5 0 **
# 5 2  *
# 4 0  *
# ********************
# 5 1
# 5 0 **
# 5 2 *
# 6 0 *
# ********************
# 5 1
# 5 0  *
# 5 2 **
# 4 1  *
# ********************

# экземпляр rect для отрисовки
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)


anim_count, anim_speed, anim_limit = 0, 60, 2000

# текущая фигура, ее необходимо копировать из оригинала, т.к. если мы будем работать с оригинальным экземпляром то
# это может привести к неприятным последствиям в виде того, что следующая фигру уже будет изменена
figure = deepcopy(choice(figures))

def check_game_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    return True

while True:
    # координата которая двигает фигуру по X
    move_x = 0
    # заполняем поле черным
    game_screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -1
            elif event.key == pygame.K_RIGHT:
                move_x = 1
            elif event.key == pygame.K_DOWN:
                # ускорим падение фигуры засчет уменьшения лимита анимации
                anim_limit = 100
    figure_old = deepcopy(figure)
    # сдвигаем фигуру по Х
    for i in range(4):
        figure[i].x += move_x
        if not check_game_borders():
            figure = deepcopy(figure_old)
            break
    # смещаем фигуру вниз для этого каждый кадр увеличиваем anim_count на скорость анимации и
    # если был достигнут лимит анимации, то обнуляем счетчик, а саму фигуру сдвигаем на 1 клетку вниз
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        # сдвигаем фигуру по Y
        for i in range(4):
            figure[i].y += 1
            if not check_game_borders():
                figure = deepcopy(figure_old)
                # вернем лимит если былдо нажато ускорение (клавиша вниз)
                anim_limit = 2000
                break

    # проходимся по каждому квадрата из списка и отрисовываем его
    for rect in grid:
        # поверхность на которой рисуем, цвет, объект из списка, отступ в пикселах.
        pygame.draw.rect(game_screen, (40, 40, 40), rect, 1)
    # отрисуем текущую фигуру
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_screen, (255, 0, 0), figure_rect)
    pygame.display.update()
    clock.tick(60)
