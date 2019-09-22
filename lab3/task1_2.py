from graph import *
from typing import Any

penColor('purple')
rectangle(0, 0, 500, 400)
brushColor(204, 255, 255)
rectangle(0, 0, 500, 200)
brushColor(0, 0, 102)
rectangle(0, 200, 500, 300)
penColor(255, 204, 0)
brushColor(255, 204, 0)
circle(400, 100, 50)
rectangle(0, 300, 500, 400)
n = 13
r = 500 / (n * 2)
x = r
for i in range(n):
    circle(x, 310, r)
    x += 2 * r
penColor(102, 51, 0)
penSize(5)
line(55, 280, 55, 390)
brushColor(255, 69, 0)
penSize(1)
polygon([(5, 280), (55, 260), (60, 260), (110, 280)])
brushColor(128, 0, 0)
penColor(128, 0, 0)
from math import cos, pi, sin

pol=[]
i=1
t=0
while t !=pi/2:
    t = i / 200 * pi
    dx =250- 30 * cos(t)
    dy = 220+ 30 * sin(t)
    pol.append((dx, dy))
    i+=1
polygon(pol)
polygon([(250,250),(350,250),(420,220),(220,220)])
penSize(5)
penColor(50,0,0)
line(295,220,295,120)
penSize (2)
brushColor(200,200,200)
polygon([(295,220),(390,170),(320,170),(295,220)])
polygon([(295,120),(390,170),(320,170),(295,120)])
circle(356,235,9)
x=100
y=70
penSize(1)
penColor(0,0,240)
brushColor(240,240,240)
for i in range (3):
    circle(x,y,15)
    x+=15
y+=12
x+=-20
for i in range(2):
    circle(x,y,12)
    x-=15





run()
