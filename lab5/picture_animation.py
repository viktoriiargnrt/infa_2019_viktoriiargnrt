from graph import *
from math import *


# фон
def sky():
    penColor('purple')
    rectangle(0, 0, 500, 400)
    red = 249
    green = 17
    blue = 71
    y = 0
    y1 = 2
    for i in range(100):
        brushColor(red, green, blue)
        penColor(red, green, blue)
        # brushColor(204, 255, 255)
        rectangle(0, y, 500, y1)  # y=0 y1=200
        red += -1
        green += 1
        blue += 1
        y += 2
        y1 += 2


def earth():
    brushColor(0, 0, 102)
    rectangle(0, 200, 500, 400)
    penColor(255, 204, 0)
    brushColor(255, 204, 0)
    rectangle(0, 300, 500, 400)


# солнце
def sun(x0, y0):
    # x0=400 y0=100
    penColor(255, 204, 0)
    brushColor(255, 204, 0)
    circle(x0,y0, 50)


def waves(number):
    brushColor(255, 204, 0)
    r = 500 / (number * 2)
    x = r
    for i in range(number):
        circle(x, 310, r)
        x += 2 * r


time = 0
dt = 50


def sun_anim(time):
    x0 = 200 - 150 * cos(time)
    y0 = 200 + 150 * sin(time)
    sun(x0, y0)

def cloud(x, y, width):
    brushColor(200, 200, 250)
    penColor(150, 150, 150)
    if width >= 5:
        penSize(3)
    elif width < 5 and width > 3:
        penSize(2)
    else:
        penSize(1)
    pol = []
    i = 1
    t = 0
    for i in range(1000):
        t = i / 200 * pi
        dx = x + width * t * cos(t)
        dy = y - t * width / 2 * sin(t)
        pol.append((dx, dy))
        i += 1
    polygon(pol)
    pol1 = []
    for i in range(800):
        t = i / 200 * pi
        dx1 = dx + width * t * cos(t)
        dy1 = dy - t * width / 2 * sin(t)
        pol1.append((dx1, dy1))
        i += 1
    polygon(pol1)

def cloud1_anim(time):
    x=100+time
    y=50
    cloud(x,y, 5)

def anim():
    global time
    sky()
    sun_anim(time)
    cloud1_anim(time)
    earth()
    time+=dt


onTimer(anim, dt)

run()
