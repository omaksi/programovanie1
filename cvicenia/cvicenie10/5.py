import tkinter
import random


coords = []


def klik(event):
    coords.append(
        (event.x, event.y, canvas.create_text(event.x, event.y, text="+")))
    if len(coords) > 2 and abs(event.x - coords[0][0]) < 5 and abs(event.y - coords[0][1]) < 5:
        canvas.create_polygon(
            *[(x[0], x[1]) for x in coords], fill=f'#{random.randrange(256**3):06x}')
        coords.clear()


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)


tkinter.mainloop()
