

import turtle
import random

# t = turtle.Turtle()
# t.speed(0)


def vyrob(n, poz):
    t = []
    for i in range(n):
        newTurtle = turtle.Turtle()
        newTurtle.speed(0)
        newTurtle.pencolor(f'#{random.randrange(256**3):06x}')
        newTurtle.pensize(5)
        newTurtle.pu()
        newTurtle.setpos(random.randint(-300, 300), random.randint(-300, 300),)
        newTurtle.pd()

        uhol = newTurtle.towards(poz[0], poz[1])
        newTurtle.seth(uhol)
        t.append(newTurtle)
    return t


def smerom(zoznam, poz):
    for i in range(50):
        for t in zoznam:
            t.fd(t.distance(poz[0], poz[1]) / 50)


# def stvorec(velkost):
#     t.fillcolor(f'#{random.randrange(256**3):06x}')
#     t.begin_fill()
#     t.fd(velkost)
#     t.rt(-90)
#     t.fd(velkost)
#     t.rt(-90)
#     t.fd(velkost)
#     t.rt(-90)
#     t.fd(velkost)
#     t.rt(-90)
#     t.end_fill()
#     t.pu()
#     t.fd(velkost)
#     t.pd()


pp = (0, -300)
zoz = vyrob(100, pp)
smerom(zoz, pp)


turtle.exitonclick()
