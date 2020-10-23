import tkinter


def kresli(event):
    canvas.create_line(event.x, event.y, event.x+100, event.y)


def zmaz(event):
    canvas.delete("all")


canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', kresli)
canvas.bind('<ButtonPress-2>', zmaz)
canvas.bind('<ButtonPress-3>', zmaz)
tkinter.mainloop()
