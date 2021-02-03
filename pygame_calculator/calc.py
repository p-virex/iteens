import pygame  # Импорт PyGame
import GUI  # Наш модуль с GUI
import sys

pygame.init()

screen = pygame.display.set_mode((192, 300))

pygame.display.set_caption('калькулятор')
clock = pygame.time.Clock()

# Кнопки, и другие виджеты
i = []  # Создаем массив, чтоб легче было хранить виджеты

i.append(GUI.Button(screen, '0', width=32, height=32, y=268, x=32))  # Создаём кнопку
i.append(GUI.Button(screen, '1', width=32, height=32, y=236, x=0))  # Ещё кнопка :)
i.append(GUI.Button(screen, '2', width=32, height=32, y=236, x=32))
i.append(GUI.Button(screen, '3', width=32, height=32, y=236, x=64))
i.append(GUI.Button(screen, '4', width=32, height=32, y=204, x=0))
i.append(GUI.Button(screen, '5', width=32, height=32, y=204, x=32))
i.append(GUI.Button(screen, '6', width=32, height=32, y=204, x=64))
i.append(GUI.Button(screen, '7', width=32, height=32, y=172, x=0))
i.append(GUI.Button(screen, '8', width=32, height=32, y=172, x=32))
i.append(GUI.Button(screen, '9', width=32, height=32, y=172, x=64))

i.append(GUI.Button(screen, '.', width=32, height=32, y=268, x=64))
i.append(GUI.Button(screen, '=', width=64, height=64, y=236, x=128, hover_color=(100, 255, 100)))
i.append(GUI.Button(screen, 'C', width=32, height=32, y=268, x=0, hover_color=(255, 100, 100)))

i.append(GUI.Button(screen, '/', width=32, height=32, y=268, x=96, hover_color=(255, 255, 100)))
i.append(GUI.Button(screen, '*', width=32, height=32, y=236, x=96, hover_color=(255, 255, 100)))
i.append(GUI.Button(screen, '-', width=32, height=32, y=204, x=96, hover_color=(255, 255, 100)))
i.append(GUI.Button(screen, '+', width=32, height=32, y=172, x=96, hover_color=(255, 255, 100)))

i.append(GUI.Label(screen, '', y=16, x=16))  # 17
while True:  # Основной цикл

    clock.tick()

    screen.fill((60, 60, 60))  # Заполняем экран цветом (60, 60, 60) по RGB

    for value in range(len(i)):  # Перебираем все виджеты
        i[value].update()  # Обновляем виджет

    for event in pygame.event.get():  # Все события

        if event.type == pygame.QUIT:  # Если был клик по крестику
            sys.exit()  # Выход из программы

        elif event.type == pygame.MOUSEBUTTONDOWN:  # События мышки

            for value in range(10):
                if i[value].active(key=event.button):
                    i[17].add_text(str(value))

            if i[10].active(key=event.button):
                i[17].add_text('.')
            elif i[11].active(key=event.button):
                try:
                    i[17].set_text(str(eval(i[17].get_text())))
                except:
                    i[17].set_text('Ошибка!')
            elif i[12].active(key=event.button):  # Проверяем виджеты на клик
                i[17].set_text('')  # Если был клик, выполняем условие, согласно правилам калькулятора
            elif i[13].active(key=event.button):
                i[17].add_text('/')
            elif i[14].active(key=event.button):
                i[17].add_text('*')
            elif i[15].active(key=event.button):
                i[17].add_text('-')
            elif i[16].active(key=event.button):
                i[17].add_text('+')
    pygame.display.update()  # Обновляем экран