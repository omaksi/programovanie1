import tkinter
import random
import math


canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

a = [10, 100]
b = [250, 10]
c = [300, 250]


def linelen(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def midpoint(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)


while linelen(a[0], a[1], b[0], b[1]) > 30 and linelen(b[0], b[1], c[0], c[1]) > 30 and linelen(c[0], c[1], a[0], a[1]) > 30:
    farba = "%06x" % random.randint(0, 0xFFFFFF)
    canvas.create_polygon(a[0], a[1], b[0], b[1], c[0],
                          c[1], fill=f'#{farba}')
    newA = midpoint(a[0], a[1], b[0], b[1])
    newB = midpoint(b[0], b[1], c[0], c[1])
    newC = midpoint(c[0], c[1], a[0], a[1])
    a = newA
    b = newB
    c = newC

tkinter.mainloop()
