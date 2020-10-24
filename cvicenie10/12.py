import tkinter
import random

coords = []
line = [None]


def klik(event):
    if len(coords) == 0:
        coords.append((event.x, event.y))
        line[0] = canvas.create_line(
            (event.x, event.y), (event.x, event.y), fill="red", tag="movingRect")
        return
    coords.pop(0)
    coords.append((event.x, event.y))


def move(event):
    if len(coords) == 1:
        canvas.coords(
            line[0], coords[0][0], coords[0][1], event.x, event.y)


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<Motion>', move)
tkinter.mainloop()
