import tkinter as tk


def motion(event):
    x, y = event.x + 3, event.y + 7

    canvas.delete(canvas.circle)

    radius = 20
    x_max = x + radius
    x_min = x - radius
    y_max = y + radius
    y_min = y - radius

    canvas.circle = canvas.create_oval(x_max, y_max, x_min, y_min, outline="black")


root = tk.Tk()
root.bind("<Motion>", motion)

canvas = tk.Canvas(root)
canvas.circle = 0
canvas.pack()

root.mainloop()
