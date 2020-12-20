

import turtle
import random

t = turtle.Turtle()
t.speed(0)


def stvorec(velkost):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    t.fd(velkost)
    t.rt(-90)
    t.fd(velkost)
    t.rt(-90)
    t.fd(velkost)
    t.rt(-90)
    t.fd(velkost)
    t.rt(-90)
    t.end_fill()
    t.pu()
    t.fd(velkost)
    t.pd()


# for i in range(10):
#     stvorec(random.randint(20, 50))


turtle.exitonclick()
