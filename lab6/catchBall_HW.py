from tkinter import *
from random import randrange as rnd, c

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)

point = 0
ptr = 1
balls = []
points = []

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'cyan', 'purple', 'pink']

delta_t = 50


class Ball:

    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dy = rnd(-20, 20)
        self.dx = rnd(-20, 20)
        self.obj = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                    fill=choice(colors), width=0)

    def check(self):
        if self.x > 800 - self.r or self.x < self.r:
            self.dx *= (-1)
        if self.y > 600 - self.r or self.y < self.r:
            self.dy *= (-1)

    def ball_move(self):
        self.x += self.dx
        self.y += self.dy
        canv.move(self.obj, self.dx, self.dy)

    def delete(self):
        self.x = 10000
        self.y = 10000
        canv.delete(self.obj)


def update():
    for b in balls:
        b.ball_move()
        b.check()

    root.after(delta_t, update)


lb = Label(root, bg='white', fg='black', width=30, height=1, text="счет: 0")


n = rnd(2, 10)


def setting_balls():
    global n
    canv.bind('<Button-1>', click)
    for i in range(n):
        balls.append(Ball())


def click(event):
    global point, points, n
    for b in balls:
        if (event.x - b.x) ** 2 + (event.y - b.y) ** 2 <= b.r ** 2:
            point += 1
            b.delete()
        points = ['счет: ', str(point)]
        lb['text'] = ''.join(points)

    if point >= n:
        canv.delete(ALL)
        lb['text'] = 'CONGRATS, YOU WON'


setting_balls()
update()

lb.pack()
root.mainloop()
