

import turtle
import random

t = turtle.Turtle()
t.speed(0)


def domcek(d):
    t.rt(-90)
    t.fd(d)
    t.rt(45)
    t.fd((((d/2)**2)+((d/2)**2))**(1/2))
    t.rt(90)
    t.fd((((d/2)**2)+((d/2)**2))**(1/2))
    t.rt(45)
    t.fd(d)
    t.rt(90+45)
    t.fd(((d**2)+(d**2))**(1/2))
    t.rt(90+45)
    t.fd(d)
    t.rt(90+45)
    t.fd(((d**2)+(d**2))**(1/2))
    t.rt(180+45)
    t.fd(d)


# t.rt(5)
# domcek(100)
# domcek(50)
# domcek(80)

turtle.exitonclick()
