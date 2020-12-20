import tkinter

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

x, y = 150, 150
n = 20

colours = ['red', 'blue', 'yellow']
for i in reversed(range(n)):
    d = ((10 * i)/2)
    canvas.create_rectangle(x - d, y - d, x + (d),
                            y+(d), fill=colours[i % 3])


tkinter.mainloop()
