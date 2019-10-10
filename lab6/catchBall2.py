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


delta_t = 50

ball = {}


def new_ball():
    global ball
    canv.delete(ALL)
    x = ball["x"] = rnd(100, 700)
    y = ball["y"] = rnd(100, 500)
    r = ball["r"] = rnd(30, 50)
    ball["dy"] = rnd(-20, 20)
    ball["dx"] = rnd(-20, 20)
    ball["id"] = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(2000, new_ball)


def ball_move():
    global ball
    id = ball["id"]
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    canv.move(id, ball["dx"], ball["dy"])
    check(ball)
    root.after(delta_t, ball_move)


def check(ball):
    x = ball['x']
    y = ball['y']
    r = ball['r']
    if x>800 - r or x<r :
            ball['dx'] *=(-1)
            ball['dx'] += rnd(-1, 2)
    if y>600 - r or y<r:
            ball['dy'] *=(-1)
            ball['dy'] += rnd(-1, 2)


def click(event):
    coords = canv.coords(ball['id'])
    r = ball["r"]
    x = coords[0] + r
    y = coords[1] + r
    if ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 < r:
        add_point()


new_ball()
ball_move()
lb.pack()
canv.bind('<Button-1>', click)
mainloop()
