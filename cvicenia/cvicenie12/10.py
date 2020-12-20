
import turtle


def stvorec(v):
    t.pu()
    t.setheading(90)
    t.fd(v/2)
    t.pd()
    t.rt(90)
    t.fd(v/2)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v/2)
    t.pu()
    t.rt(90)
    t.fd(v/2)


def stvorec2(v):
    t.pu()
    t.setheading(45)
    t.fd(v/2)
    t.pd()
    t.rt(90)
    t.fd(v/2)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v)
    t.rt(90)
    t.fd(v/2)
    t.pu()
    t.rt(90)
    t.fd(v/2)


def vpisane4(n, a):
    if (n == 0):
        return
    s = a
    for i in range(n):
        s = (((s/2)**2)+((s/2)**2))**(1/2)
    if n % 2 == 0:
        stvorec2(s)
    else:
        stvorec(s)
    vpisane4(n-1, a)


t = turtle.Turtle()
t.speed(9)


# vpisane4(10, 500)

turtle.exitonclick()
