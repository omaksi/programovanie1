

import turtle
import random

t = turtle.Turtle()
t.speed(0)


def strom(kmen, koruna):
    t.rt(-90)
    t.pensize(15)
    t.pencolor('brown')
    t.fd(kmen)
    t.pensize(40)
    t.pencolor('green')
    t.fd(koruna)
    t.rt(180)
    t.pu()
    t.fd(kmen)
    t.fd(koruna)
    t.rt(-90)


# for i in range(8):
#     strom(random.randint(30, 60), random.randint(10, 40))
#     t.pu()
#     t.fd(50)
#     t.pd()


turtle.exitonclick()
