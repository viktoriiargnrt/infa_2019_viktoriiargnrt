from graph import *
from typing import Any
from math import *

penColor('purple')
rectangle(0, 0, 500, 400)
brushColor(204, 255, 255)
rectangle(0, 0, 500, 200)
brushColor(0, 0, 102)
rectangle(0, 200, 500, 300)
penColor(255, 204, 0)
i = 1
t = 0

for i in range(400):      # солнце
    t = i / 150 * pi
    dx = 400 - 80 * cos(t)
    dy = 100 - 80 * sin(t)
    i += 1
    line(400, 100, dx, dy)

brushColor(255, 204, 0)
rectangle(0, 300, 500, 400)

n = 13                   # волны
r = 500 / (n * 2)
x = r
for i in range(n):
    circle(x, 310, r)
    x += 2 * r

penColor(102, 51, 0)
penSize(5)
line(55, 280, 55, 390)
brushColor(230, 30, 0)
penSize(1)
polygon([(5, 280), (55, 260), (60, 260), (110, 280)])

penSize(5)
line(125, 260, 125, 360)
brushColor(230, 30, 0)
penSize(1)
polygon([(75, 260), (125, 240), (130, 240), (180, 260)])


brushColor(128, 0, 0)
penColor(128, 0, 0)

from math import cos, pi, sin

pol = []
i = 1
t = 0
while t != pi / 2:
    t = i / 200 * pi
    dx = 250 - 30 * cos(t)
    dy = 220 + 30 * sin(t)
    pol.append((dx, dy))
    i += 1
polygon(pol)
polygon([(250, 250), (350, 250), (420, 220), (220, 220)])

pol = []
i = 1
t = 0
while t != pi / 2:
    t = i / 200 * pi
    dx = 110 - 25 * cos(t)
    dy = 210 + 25 * sin(t)
    pol.append((dx, dy))
    i += 1
polygon(pol)
polygon([(110, 235), (180, 235), (240, 210), (85, 210)])

penSize(5)
penColor(50, 0, 0)
line(295, 220, 295, 120)
line(152,210,152,110)

penSize(2)
brushColor(200, 200, 200)
polygon([(295, 220), (390, 170), (320, 170), (295, 220)])
polygon([(295, 120), (390, 170), (320, 170), (295, 120)])
polygon([(152, 210), (240, 160), (180, 160), (152, 210)])
polygon([(152, 110), (240, 160), (180, 160), (152, 110)])
penColor(0,0,0)
brushColor('white')
circle(356, 235, 9)
circle(188,222,7)
penSize(1)
penColor(0, 0, 240)
brushColor(240, 243, 247)


def oval(x, y, axemin, axemax):
    pol = []
    i = 1
    t = 0
    for i in range(400):
        t = i / 200 * pi
        dx = x + axemax * cos(t)
        dy = y - axemin * sin(t)
        pol.append((dx, dy))
        i += 1
    polygon(pol)


x1 = 150
for i in range(3):
    oval(x1, 90, 20, 40)
    x1 += -30
x1 += 50
for i in range(2):
    oval(x1, 110, 15, 30)
    x1 += 30
x1+=-150
for i in range(3):
    oval(x1,50,10,20)
    x1+=15
x1+=-15
for i in range (2):
    oval(x1,40,8,15)
    x1+=-10
x=80
for i in range(3):
    circle(x,30,10)
    x+=15
x+=-20
for i in range(2):
    circle(x,22,8)
    x+=-15
run()
