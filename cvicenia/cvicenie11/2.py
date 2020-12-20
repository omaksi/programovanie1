import turtle
import random

t = turtle.Turtle()
t.speed(0)


def slnko(pocet, velkost):
    t.pensize(10)
    t.pencolor('gold')
    t.dot(velkost, 'gold')
    for i in range(pocet):
        t.fd(velkost)
        t.pu()
        t.rt(180)
        t.fd(velkost)
        t.rt(180)
        t.pd()
        t.rt(360/pocet)


# slnko(10, 100)

turtle.exitonclick()
