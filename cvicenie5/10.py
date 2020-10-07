import tkinter
import random


def randomColor():
    return ('#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def kruhy(x, y):
    for i in range(11, 1, -1):
        canvas.create_oval(x-(i*5), y-(i*5), x+(i*5),
                           y+(i*5), fill=randomColor())


for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))


tkinter.mainloop()
