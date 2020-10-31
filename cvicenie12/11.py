
import turtle


def kriziky4(n, a):
    if (n == 0):
        return

    if n % 2 == 0:
        t.setheading(45)
    else:
        t.setheading(0)

    t.fd(a)
    kriziky4(n-1, a/3)
    t.fd(-2*a)
    kriziky4(n-1, a/3)
    t.fd(a)
    t.lt(90)
    t.fd(a)
    t.lt(-90)
    kriziky4(n-1, a/3)
    t.lt(90)
    t.fd(-2*a)
    t.lt(-90)
    kriziky4(n-1, a/3)
    t.lt(90)
    t.fd(a)
    t.lt(-90)

    if n % 2 == 0:
        t.setheading(0)
    else:
        t.setheading(45)


t = turtle.Turtle()
t.speed(0)


# kriziky4(4, 200)

turtle.exitonclick()
