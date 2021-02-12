from tkinter import *

root = Tk()
root.geometry('600x600+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)

# начальная скорость
canv.speed_x = 2
canv.speed_y = 1
# размер шара
r = 10
# стартовое положение
canv.x = 0
canv.y = 0


def update():
    canv.x += canv.speed_x
    canv.y += canv.speed_y
    # проверим, что если координаты шара выходят за рамку слева или справа, то изменит скорость на противоположну
    # тем самым изменим его направление
    if canv.x > 590 or canv.x < 0:
        canv.speed_x *= -1
    if canv.y > 590:  # проверяем что если шарик столкнулся с нижней рамкой,
        # то изменим вертикальную скорость на противоположную
        canv.speed_y *= -0.6
        canv.y = 590  # вернем шарик на нижнюю часть
        canv.speed_x *= 0.9  # немного изменим горизонтальную скорость
    canv.speed_y += 1

    canv.delete('ball')  # удалим старый шар
    # создаим новый шар по новым координатам
    canv.create_oval(canv.x - r, canv.y - r, canv.x + r, canv.y + r, fill='red', tag='ball')

    root.after(30, update)  # вызываем фсами себя через каждые 30 милисекунд


# добавим функцию которая подкидывает шарик при нажатии на левую клавишу мыши

def click(event):
    canv.speed_y = -20


canv.bind('<1>', click)

update()  # вызываем 1 раз функцию для старта

root.mainloop()
