
import turtle


def trojuholnik(v):
    t.setheading(0)
    t.fd(v/2)
    t.lt(120)
    t.fd(v)
    t.lt(120)
    t.fd(v)
    t.lt(120)
    t.fd(v/2)
    t.pu()
    t.fd(v/2)
    t.rt(120)
    t.fd(v)
    t.pd()


def trojuholnik2(v):
    t.setheading(0)
    t.lt(60)
    t.fd(v)
    t.lt(120)
    t.fd(v)
    t.lt(120)
    t.fd(v)


def vpisane3(n, a):
    if (n == 0):
        return
    s = a
    for i in range(n):
        s = s/2
    if n % 2 == 0:
        trojuholnik2(s)
    else:
        trojuholnik(s)
    vpisane3(n-1, a)


t = turtle.Turtle()
t.speed(2)


# vpisane3(5, 500)

turtle.exitonclick()
