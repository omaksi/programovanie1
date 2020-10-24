import tkinter
import random

isMoving = [False]
offset = [0, 0]
size = [50, 50]
position = [50, 50]


def klik(event):
    if not isMoving[0]:
        isMoving[0] = True
        offset[0] = event.x - position[0]
        offset[1] = event.y - position[1]


def move(event):
    if isMoving[0]:
        canvas.coords(
            'movingRect', event.x-offset[0], event.y-offset[1], event.x-offset[0]+size[0], event.y-offset[1]+size[1])


canvas = tkinter.Canvas(width=500, height=400)
redRect = canvas.create_rectangle(
    position[0], position[1], position[0]+size[0], position[1]+size[1], fill="red", tag="movingRect")
canvas.pack()
canvas.tag_bind(redRect, '<ButtonPress-1>', klik)
canvas.bind('<Motion>', move)


tkinter.mainloop()
