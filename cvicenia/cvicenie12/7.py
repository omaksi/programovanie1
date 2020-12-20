import turtle

zoznam = []


def strom(d):
    t.fd(d)
    if d > 20:
        t.lt(40)
        strom(d*.7)
        t.rt(90)
        strom(d*.6)
        t.lt(50)
    else:
        nt = turtle.Turtle()
        nt.speed(0)
        nt.pu()
        nt.setpos(t.pos()[0], t.pos()[1])
        nt.pd()
        zoznam.append(nt)
    t.fd(-d)


turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.lt(90)
t.pu()
t.setpos(0, -200)
t.pd()
zoznam = []
strom(150)

for p in zoznam:
    p.color('green')
    p.shape('turtle')
while True:
    for p in zoznam:
        p.lt(15)


turtle.exitonclick()
