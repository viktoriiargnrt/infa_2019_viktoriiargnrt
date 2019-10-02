from math import *
from graph import *

time = 0
dt = 60


def bg():
    brushColor(102, 0, 51)
    rectangle(0,0, 500, 400)


def ball(x0, y0):
    penColor("black")
    brushColor("white")
    circle(x0, y0, 20)


def ball_anim(time):
    x0 = 0 + time
    y0 = 0 + time*time /1000
    ball(x0,y0)


def anim():
    global time
    bg()
    ball_anim(time)
    time += dt

onTimer(anim, dt)

run()
