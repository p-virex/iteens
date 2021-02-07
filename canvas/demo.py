# from tkinter import Tk, Canvas, LAST
#
# root = Tk()
# c = Canvas(root, width=200, height=200, bg='white')
# c.pack()
# c.create_line(10, 10, 190, 10, dash=(10,2),)
# c.create_line(20, 20, 190, 20)
# c.create_line(30, 30, 190, 30)
# c.create_line(40, 40, 190, 40)
# root.mainloop()


# from tkinter import Tk, Canvas
#
# root = Tk()
# c = Canvas(root, width=200, height=200, bg='white')
# c.pack()
#
# c.create_oval(10, 80, 180, 10, activefill='lightgreen')
#
# root.mainloop()

# from tkinter import Tk, Canvas
#
# WIDTH, HEIGHT = 500, 500
#
# root = Tk()
# root.geometry(f'{WIDTH}x{HEIGHT}')
# c = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
# c.pack()
#
# c.create_rectangle(100, 250, 400, 490, width=5, fill='red')
# c.create_line(100, 250, 250, 20, width=5)
# c.create_line(250, 20, 400, 250, width=5)
#
# root.mainloop()

from tkinter import Tk, Canvas, FIRST, LAST, TOP

WIDTH, HEIGHT = 500, 500

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
c = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
c.pack()

c.create_line(250, 5, 250, 495, width=3, arrow=FIRST)
c.create_line(0, 250, 500, 250, width=3, arrow=LAST)
start, coord = 0, 12
for d in range(25):
    start += 20
    c.create_line(245, start, 255, start, width=3)
    c.create_text(235, start, text=f'{coord}', font=('Calibri', 10))
    if coord == 1:
        coord -= 1
    coord -= 1

start, coord = 0, 12
for d in range(25):
    start += 20
    c.create_line(start, 245, start, 255, width=3)
    c.create_text(start, 235, text=f'{coord}', font=('Calibri', 10))
    if coord == 1:
        coord -= 1
    coord -= 1

c.create_text(220, 20, text='y', font=('Calibri', 20))
c.create_text(20, 220, text='x', font=('Calibri', 20))

root.mainloop()