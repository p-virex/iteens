"""
Цель: добавить интерфейс в игру
"""
from copy import deepcopy
from random import choice, randrange

import pygame

# игровое поле 10 на 20 квадратов
W, H = 10, 20
#  размер квадрата
TILE = 45
# размер окна
GAME_RES = W * TILE, H * TILE
RES = 750, 940

pygame.init()
screen = pygame.display.set_mode(RES)
game_screen = pygame.Surface(GAME_RES)
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

# экземпляр rect для отрисовки
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

# массив представляющий и хранящий в себе расположение фигур на игровом поле. Простыми словами карта игрового поля
field = [[0 for _ in range(W)] for _ in range(H)]

# счетчик анимации, скорость анимации, лимит анимации при достижении которого надо сдвинуть фигуру вниз
anim_count, anim_speed, anim_limit = 0, 60, 2000

# текущая фигура, ее необходимо копировать из оригинала, т.к. если мы будем работать с оригинальным экземпляром то
# это может привести к неприятным последствиям в виде того, что следующая фигру уже будет изменена
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

bg = pygame.image.load('bg.jpg').convert()
game_bg = pygame.image.load('bg2.jpg').convert()


big_font = pygame.font.SysFont('calibri', 65)
small_font = pygame.font.SysFont('calibri', 45)

title = big_font.render('TETRIS', True, (155, 50, 0))
title_score = big_font.render('Score', True, (0, 220, 0))

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

def check_game_borders():
    # если координата фигуры выходит за левый край или за правый с учетом поправки на 1 клетку, то вернем ложь
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    # если фигура достигла дна или попала на другу фигуру то вренем ложь
    # проверка с длругой фигурой осуществлояется проверкой значения в карте игрового поля
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def random_color():
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)

color, next_color = random_color(), random_color()

while True:
    # координата которая двигает фигуру по X и флаг для вращения фигуры
    move_x, rotate = 0, False
    # заполняем поле черным
    # game_screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(game_screen, (20, 20))
    game_screen.blit(game_bg, (0, 0))
    for i in range(lines):
        pygame.time.wait(200)

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
            elif event.key == pygame.K_UP:
                # ускорим падение фигуры засчет уменьшения лимита анимации
                rotate = True
    # сохраним теккущую фигуру, т.к. ниже будут проверки не покинула ли фигура границы игрового поля
    figure_old = deepcopy(figure)
    # сдвигаем фигуру по Х
    for i in range(4):
        figure[i].x += move_x
        if not check_game_borders():
            # если получено ложь то восстановим фигуру из копии (получим предыдущую фигуру)
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
                for i in range(4):
                    # сохраним цвет упавшей фигуры в карту игрвого поля, пока будем брать красный
                    # field[figure[i].y][figure[i].x] = (255, 0, 0)
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                # выбираем случайною фигуру при приземлении старой
                next_figure, next_color = deepcopy(choice(figures)), random_color()
                # вернем лимит если былдо нажато ускорение (клавиша вниз)
                anim_limit = 2000
                break
    # вращение фигур
    figure_old = deepcopy(figure)
    if rotate:
        center_rotate = figure[0]
        for i in range(4):
            # для каждой координаты плитки фигуры надо расчитать разницу между координатами фигуры и центром вращения,
            # а потом получить новые координаты плитки. для центра врещения из Х вычесть разницу полученную для
            # оси координат. А для Y координат центра вращения прибавить разницу для абсцисс
            x = figure[i].y - center_rotate.y
            y = figure[i].x - center_rotate.x
            figure[i].y = center_rotate.y + y
            figure[i].x = center_rotate.x - x
            if not check_game_borders():
                # если получено ложь то восстановим фигуру из копии (получим предыдущую фигуру)
                figure = deepcopy(figure_old)
                break
    # возьмем последнюю линию на игровом поле
    line, lines = H - 1, 0
    # двигаемся от последнего ряда к первому
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    score += scores[lines]

    # проходимся по каждому квадрата из списка и отрисовываем его
    for rect in grid:
        # поверхность на которой рисуем, цвет, объект из списка, отступ в пикселах.
        pygame.draw.rect(game_screen, (40, 40, 40), rect, 1)
    # отрисуем текущую фигуру
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_screen, color, figure_rect)
    # отрисуем карту игрового поля с фигурами
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(game_screen, col, figure_rect)
    for i in range(4):
        figure_rect.x = next_figure[i].x * TILE + 380
        figure_rect.y = next_figure[i].y * TILE + 185
        pygame.draw.rect(screen, next_color, figure_rect)
    screen.blit(title, (485, 20))
    screen.blit(title_score, (535, 780))
    screen.blit(small_font.render(str(score), True, (255, 255, 255)),(550, 840))

    # game over
    for i in range(W):
        if field[0][i]:
            # set_record(record, score)
            field = [[0 for i in range(W)] for i in range(H)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0
            for i_rect in grid:
                pygame.draw.rect(game_screen, random_color(), i_rect)
                screen.blit(game_screen, (20, 20))
                pygame.display.flip()
                clock.tick(200)

    pygame.display.update()
    clock.tick(60)
