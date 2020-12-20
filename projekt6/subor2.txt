import turtle
t = turtle.Turtle()
t.lt(90)
t.pu()
t.fd(100)
t.rt(30)
t.pd()
for _ in range(4):
    t.fd(50)
    t.lt(30)
    for _ in range(3):
        t.fd(30)
        t.rt(120)
    t.lt(60)
t.rt(30)
t.fd(70)
turtle.mainloop()