from random import randrange as rnd, choice
import tkinter as tk
from math import *
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown', 'magenta'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 1.3
        self.vy /= 1.06
        self.vx /= 1.06
        canv.move(self.id, self.vx, self.vy)

        if self.x > 800 - self.r and self.vx > 0:
            self.vx *= (-1)
        if self.y > 570 - self.r and self.vy > 0:
            self.vy *= (-1)

        self.live -= 0.5

        if self.live < 0:
            canv.delete(self.id)
            balls.remove(self)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * cos(self.an)
        new_ball.vy = self.f2_power * sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * cos(self.an),
                    450 + max(self.f2_power, 20) * sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class reminders():
    def __init__(self):
        self.xt = 300
        self.yt = 400
        self.color = choice(['blue', 'green', 'black', 'brown', 'purple'])
        self.id_reminder = canv.create_text(self.xt, self.yt, text="", font="28", fill=self.color)
        self.vxt = 1
        self.vyt = 1
        self.set_reminder()
        self.moving()

    def moving(self):
        self.xt += self.vxt
        self.yt += self.vyt
        self.vyt -= 0.1
        canv.move(self.id_reminder, self.vxt, self.vyt)

    def set_reminder(self):
        if bullet == 1:
            k = "."
        elif bullet == 2 or bullet == 3 or bullet == 4:
            k = "а."
        else:
            k = "ов."
        canv.itemconfig(self.id_reminder, text="Цель сбита за " + str(bullet) + " выстрел" + k)


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 0
        self.y = 0
        self.vy = rnd(-7, 7)
        self.vx = rnd(-7, 7)
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, point=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += point
        canv.itemconfig(self.id_points, text='')

    def move_target(self):
        self.y += self.vy
        self.x += self.vx
        canv.move(self.id, self.vx, self.vy)
        self.vy += 0.9
        if self.y <= self.r and self.vx < 0:
            self.vy = -self.vy
        elif self.y >= 550 - self.r and self.vy > 0:
            self.vy *= -1
        if self.x <= self.r and self.vx < 0:
            self.vx = -self.vx
        elif self.x >= 800 - self.r and self.vx > 0:
            self.vx = -self.vx


screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()


def new_game():
    global screen1, balls, bullet, target
    bullet = 0
    balls = []
    n = 2
    targets = []
    hits = 0
    reminder_1 = []
    ttl = 0
    for i in range(n):
        new_target = target()
        targets.append(new_target)
        ttl += targets[i].live
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    while ttl or balls:
        deathnote = []
        for j in range(n):
            targets[j].move_target()
        for i, b in enumerate(balls):
            b.move()
            for j in range(n):
                if b.hittest(targets[j]) and targets[j].live:
                    ttl -= targets[j].live
                    targets[j].live = 0
                    targets[j].hit()
                    hits += 1
                    if hits == n:
                        new_reminder = reminders()
                        reminder_1.append(new_reminder)
                for r in reminder_1:
                    r.moving()

            if b.live < 0:
                deathnote.append(i)
                canv.delete(b.id)

            for i in range(len(deathnote) - 1):
                del balls[deathnote[i]]

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

root.mainloop()
