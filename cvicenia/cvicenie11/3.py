import turtle
import random

t = turtle.Turtle()
t.speed(0)


def terc(pocet):
    color = 1
    for i in range(pocet, 0, -1):
        t.dot(i*15,  'blue' if color else 'yellow')
        color = 1 - color


# terc(40)
turtle.exitonclick()
