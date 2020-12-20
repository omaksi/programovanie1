
import tkinter
import random


def randomColor():
    return ('#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def stv(y, x, color='white'):
    canvas.create_rectangle(5+(30*x), 5+(30*y), 5 +
                            (30*x)+30, 5+(30*y)+30, fill=color, outline="")


# for i in range(8):
#     for j in range(12):
#         if i == j:
#             stv(i, j)
#         else:
#             stv(i, j, randomColor())

for i in range(8):
    for j in range(12):
        stv(i, j, '#%02x%02x%02x' %
            (255, int((128/(8))*i + (128/(12))*j), 0))


tkinter.mainloop()
