import turtle
import random

t = turtle.Turtle()
t.speed(0)


def bodka(velkost, farba):
    t.pensize(velkost)
    t.pencolor(farba)
    t.fd(0)


def posun():
    t.pu()
    t.setpos(random.randint(-300, 300), random.randint(-300, 300))
    t.seth(random.randint(-30, 30))
    # t.pd()


for i in range(100):
    posun()
    x = random.randint(0, 2)
    if (x == 0):
        # bodka(50, 'red')
        t.dot(50, 'red')
    else:
        # bodka(30, 'blue')
        t.dot(30, 'blue')


turtle.exitonclick()
