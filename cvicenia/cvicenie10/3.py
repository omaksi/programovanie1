import tkinter
import random


coords = [None, None]


def klik(event):
    if coords[0] == None:
        coords[0] = event.x
        coords[1] = event.y
    else:
        canvas.create_rectangle(
            coords[0], coords[
                1], event.x, event.y, fill=f'#{random.randrange(256**3):06x}'
        )
        coords[0] = None
        coords[1] = None


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)


tkinter.mainloop()
