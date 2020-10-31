
import turtle


def kriziky(n, a, pocet):
    if (n == 0):
        return

    if n % 2 == 0:
        t.setheading(45)
    else:
        t.setheading(0)

    for i in range(pocet):
        t.fd(a)
        h = t.heading()
        kriziky(n-1, a/3, pocet)
        t.setheading(h)
        t.fd(-a)
        t.rt(360/pocet)


t = turtle.Turtle()
t.speed(0)


kriziky(4, 200, 4)

turtle.exitonclick()
