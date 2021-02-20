from tkinter import *

root = Tk()
root.geometry('600x600+100+100')
canv = Canvas(root, width=600, height=600, bg='gray')
canv.pack(fill=BOTH, expand=1)


def click(event):
    x = event.x
    y = event.y
    canv.create_line(x, y, x, y + 10, fill='orange', tag='ball', width=5)


canv.bind('<B1-Motion>', click)

root.mainloop()
