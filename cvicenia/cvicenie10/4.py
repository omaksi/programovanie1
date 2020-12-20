import tkinter
import random


coords = []


def klik(event):
    canvas.create_text(event.x, event.y, text="+")
    if len(coords) < 2:
        coords.append((event.x, event.y))
        return
    canvas.create_polygon(
        coords[0], coords[
            1], (event.x, event.y), fill=f'#{random.randrange(256**3):06x}'
    )
    coords.pop(0)
    coords.append((event.x, event.y))


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)


tkinter.mainloop()
