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
    ball["dy"] = rnd(-10, 10)
    ball["dx"] = rnd(-10, 10)
    ball["id"] = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def ball_move():
    global ball
    id = ball["id"]
    canv.move(id, ball["dx"], ball["dy"])
    root.after(delta_t, ball_move)


def click(event):
    coords = canv.coords(ball['id'])
    print(coords,event)
    r=ball["r"]
    x = coords[0]+r
    y = coords[1]+r
    if ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 < r:
        add_point()


new_ball()
ball_move()
lb.pack()
canv.bind('<Button-1>', click)
mainloop()
