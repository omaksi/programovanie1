# 2. zadanie: spirala
# autor: Ondrej Makši
# datum: 4.10.2020

import tkinter


n = int(input())
increment = int(input())
total = int(input())
# n = 20
# increment = 3
# total = 2950

canvas = tkinter.Canvas()
canvas.pack()

x, y = 100, 100

direction = 0
counter = 0

while counter < total:
    if counter + n > total:
        d = total - counter
        o = round((d**2 / 2) ** (1/2), 2)
        if direction == 0:
            canvas.create_line(x, y, x+o, y+o)
        elif direction == 1:
            canvas.create_line(x, y, x-o, y+o)
        elif direction == 2:
            canvas.create_line(x, y, x-o, y-o)
        elif direction == 3:
            canvas.create_line(x, y, x+o, y-o)
        counter = total + 1
    else:
        d = n
        counter = counter + n
        o = round((d**2 / 2) ** (1/2), 2)
        if direction == 0:
            canvas.create_line(x, y, x+o, y+o)
            x = x+o
            y = y+o
            direction = 1
        elif direction == 1:
            canvas.create_line(x, y, x-o, y+o)
            x = x-o
            y = y+o
            direction = 2
        elif direction == 2:
            canvas.create_line(x, y, x-o, y-o)
            x = x-o
            y = y-o
            direction = 3
        elif direction == 3:
            canvas.create_line(x, y, x+o, y-o)
            x = x+o
            y = y-o
            direction = 0

        n = n + increment


tkinter.mainloop()
