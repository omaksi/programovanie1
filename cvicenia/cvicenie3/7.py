import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

x, y = 10, 100
d = 20
n = 16

for i in range(0, n, 2):
    canvas.create_line(x + (i*d), y + (d * (i % 2)),  x+(i*d) + d,
                       y + (d * ((i % 2) + 1)), fill='blue', width=5)
    canvas.create_line(x + (i*d)+d, y + (d * ((i % 2) + 1)),  x+(i*d) + d + d,
                       y + (d * ((i % 2))), fill='blue', width=5)

tkinter.mainloop()
