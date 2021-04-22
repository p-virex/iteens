"""
Цель: создать простое окно pygame и заполнить его квадратами.
Создание игрового поля по которому будут двигаться фигуры из игры
"""
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


while True:
    # заполняем поле черным
    game_screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # проходимся по каждому квадрата из списка и отрисовываем его
    for rect in grid:
        # поверхность на которой рисуем, цвет, объект из списка, отступ в пикселах.
        pygame.draw.rect(game_screen, (40, 40, 40), rect, 1)
    pygame.display.update()
    clock.tick(60)
