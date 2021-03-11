# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random

WIDTH, HEIGHT = 500, 400

# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали
# из класса Tk() — он есть в графической библиотеке
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('PingPong')
# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()


# Описываем класс Ball, который будет отвечать за шарик
class Ball:
    # конструктор — он вызывается в момент создания нового объекта на основе этого класса
    def __init__(self, canvas, paddle, score, color):
        # задаём параметры объекта, которые нам передают в скобках в момент создания
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.speed = 1
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство ball, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.ball = canvas.create_oval(10, 10, 25, 25, fill=color)
        # помещаем шарик в точку с координатами 245,100
        self.canvas.move(self.ball, 0, 0)
        # выбираем вектор движения шара
        self.x = random.choice([random.randint(-5, -1), random.randint(1, 5)])
        # в самом начале он всегда падает вниз, поэтому уменьшаем значение по оси y_bird
        self.y = -5
        # свойство, которое отвечает за то, достиг шарик дна или нет. Пока не достиг, значение будет False
        self.hit_bottom = False

    # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos
    # (левая верхняя и правая нижняя точки)
    def hit_paddle(self):
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.paddle)
        pos = self.canvas.coords(self.ball)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if all([pos[3] >= paddle_pos[1], pos[3] <= paddle_pos[3]]):
                # увеличиваем счёт (обработчик этого события будет описан ниже)
                self.score.hit(self)
                # возвращаем метку о том, что мы успешно коснулись
                return True
        # возвращаем False — касания не было
        return False

    # метод, который отвечает за движение шарика
    def draw(self):

        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.ball)
        # если шарик падает сверху
        if pos[1] <= 0:
            # задаём падение на следующем шаге = 2
            self.y = self.speed
        # если шарик правым нижним углом коснулся дна
        if pos[3] >= HEIGHT:
            # помечаем это в отдельной переменной
            self.hit_bottom = True
            # выводим сообщение и количество очков
            canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        # если было касание платформы
        if self.hit_paddle():
            # отправляем шарик наверх
            self.y = -self.speed
        # если коснулись левой стенки
        if pos[0] <= 0:
            # движемся вправо
            self.x = self.speed
        # если коснулись правой стенки
        if pos[2] >= WIDTH:
            # движемся влево
            self.x = -self.speed
        # передвигаем шарик на заданный вектор x и y_bird
        self.canvas.move(self.ball, self.x, self.y)


#  Описываем класс Paddle, который отвечает за платформы
class Paddle:
    # конструктор
    def __init__(self, canvas, color):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя
        self.paddle = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # задаём список возможных стартовых положений платформы
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # выбираем первое из перемешанных
        self.starting_point_x = random.choice(start_1)
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.paddle, self.starting_point_x, 300)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        # задаём обработчик нажатий
        self.canvas.bind_all('<KeyPress>', self.on_key_press)
        self.canvas.bind_all('<KeyRelease>', self.on_key_release)
        # пока платформа не двигается, поэтому ждём
        self.started = False
        # как только игрок нажмёт Enter — всё стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # двигаем влево или вправо по вектору Х взависимости от нажатой кнопки
    def on_key_press(self, event):
        if event.keysym == 'Left':
            self.x = -6
        elif event.keysym == 'Right':
            self.x = 6

    # если кнопка отпущена то останавливаем платформу
    def on_key_release(self, event):
        if event.keysym in ('Left', 'Right'):
            self.x = 0

    # игра начинается
    def start_game(self, event):
        # меняем значение переменной, которая отвечает за старт движения платформы
        self.started = True

    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.paddle, self.x, 0)
        # получаем координаты холста
        pos = self.canvas.coords(self.paddle)
        # если мы упёрлись в левую границу
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
            self.canvas.move(self.paddle, 4, 0)
        # если упёрлись в правую границу
        elif pos[2] >= WIDTH:
            # останавливаемся
            self.x = 0
            # не даем платформе уйти ха пределы холста
            self.canvas.move(self.paddle, -4, 0)


#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    # конструктор
    def __init__(self, canvas, color):
        # в самом начале счёт равен нулю
        self.score = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт, делаем его нужно цвета и запоминаем
        # внутреннее имя этой надписи
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    # обрабатываем касание платформы
    def hit(self, ball):
        # увеличиваем счёт на единицу
        self.score += 1
        # пишем новое значение счёта
        self.canvas.itemconfig(self.id, text=self.score)
        # увеличиваем скорость шарика каждые 2 очка
        if self.score % 2 == 0:
            ball.speed += 0.5


# создаём объект — зелёный счёт
score = Score(canvas, 'green')
# создаём объект — белую платформу
paddle = Paddle(canvas, 'White')
# создаём объект — красный шарик
ball = Ball(canvas, paddle, score, 'red')
# ball2 = Ball(canvas, paddle, score, 'black')
# пока шарик не коснулся дна
while not ball.hit_bottom:
    # если игра началась и платформа может двигаться
    if paddle.started:
        # двигаем шарик
        ball.draw()
        # двигаем платформу
        paddle.draw()
    # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
    tk.update_idletasks()
    # обновляем игровое поле и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
    tk.update()
    # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно
    time.sleep(0.01)

tk.mainloop()
