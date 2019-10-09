from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']

points = []
point = 0
lb = Label(root, bg='black', fg='white', width=30, height=1, text="счет: 0")


def add_point():
    global point, l, points
    point += 1
    points = ['счет: ', str(point)]
    lb['text'] = ''.join(points)


def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def click(event):
    if ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 < r:
        add_point()


new_ball()
lb.pack()
canv.bind('<Button-1>', click)
mainloop()
