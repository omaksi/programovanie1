import turtle


def kmit(a):
    if a > 230:
        t.color('grey')
        t.lt(10)
    else:
        t.fd(a)
        t.rt(170)
        t.fd(a+5)
        t.lt(170)
        kmit(a+10)
        t.fd(a+5)
        t.lt(170)
        t.fd(a)
        t.rt(170)


t = turtle.Turtle()
t.speed(9)
t.pu()
t.setpos(-250, 0)
t.pd()
t.lt(85)
kmit(100)

turtle.exitonclick()
