import tkinter as tk


def oval():
    canvas.func = canvas.create_oval


def rectangle():
    canvas.func = canvas.create_rectangle


def color(color):
    canvas.color = color


def clear(event):
    canvas.old = None


def make(event):
    if canvas.old:
        x, y = event.x, event.y
        x1, y1 = canvas.old
        canvas.func(x, y, x1, y1, outline=canvas.color)
        canvas.old = None
    else:
        x, y = event.x, event.y
        canvas.old = x, y


def make_motion(event):
    #  'char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num',
    #  'send_event', 'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y_bird', 'y_root'

    x, y = event.x, event.y
    if canvas.obj:
        canvas.delete(canvas.obj)
    if canvas.old:
        x1, y1 = canvas.old
        canvas.obj = canvas.func(x1, y1, x, y, outline=canvas.color)


root = tk.Tk()
root.geometry('400x600')
root['bg'] = 'white'
canvas = tk.Canvas(root, width=400, height=400, cursor="pencil")
canvas.grid(row=0, column=0, columnspan=2)
canvas.old = None
canvas.func = canvas.create_oval
canvas.obj = None
canvas.color = 'black'

tk.Button(root, text='oval', bd=5, fg='red', font=('Calibry', 14), command=oval).grid(row=1, column=0)
tk.Button(root, text='rectangle', bd=5, fg='red', font=('Calibry', 14), command=rectangle).grid(row=1, column=1)
tk.Button(root, text='red', bd=5, fg='red', font=('Calibry', 14), command=lambda: color('red')).grid(row=2, column=0)
tk.Button(root, text='blue', bd=5, fg='red', font=('Calibry', 14), command=lambda: color('blue')).grid(row=2, column=1)
tk.Button(root, text='fill', bd=5, fg='red', font=('Calibry', 14), command=rectangle).grid(row=4, column=0)

root.bind('<1>', make)
root.bind('<3>', clear)

root.bind('<Motion>', make_motion)

root.mainloop()
