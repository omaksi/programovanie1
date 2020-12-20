import tkinter


size = [1]


def kresli(event):
    canvas.create_oval(event.x, event.y, event.x +
                       size[0], event.y+size[0], fill='yellow')
    size[0] += 1


def zmaz(event):
    canvas.delete("all")


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', kresli)
canvas.bind('<ButtonPress-2>', zmaz)
canvas.bind('<ButtonPress-3>', zmaz)

tkinter.mainloop()
