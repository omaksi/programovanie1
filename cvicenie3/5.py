import tkinter

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

x, y = 50, 50
n = 20
w, h = 135, 90

canvas.create_rectangle(x, y, x + w, y+(h/3), fill='black')
canvas.create_rectangle(x, y+(h/3), x + w, y + (h/3) + (h/3), fill='red')
canvas.create_rectangle(x, y+(h/3)+(h/3), x + w, y +
                        (h/3) + (h/3) + (h/3), fill='yellow')

x, y = 200, 50
canvas.create_rectangle(x, y, x + (w/3), y+h, fill='green')
canvas.create_rectangle(x + (w/3), y, x + (w/3) + (w/3),
                        y + h, fill='white')
canvas.create_rectangle(x + (w/3) + (w/3), y, x + (w/3) +
                        (w/3) + (w/3), y + h, fill='red')

x, y = 50, 160
canvas.create_rectangle(x, y, x + (w/3), y+h, fill='blue')
canvas.create_rectangle(x + (w/3), y, x + (w/3) + (w/3),
                        y + h, fill='white')
canvas.create_rectangle(x + (w/3) + (w/3), y, x + (w/3) +
                        (w/3) + (w/3), y + h, fill='red')

x, y = 200, 160
canvas.create_rectangle(x, y, x + w, y+(h/3), fill='white')
canvas.create_rectangle(x, y+(h/3), x + w, y + (h/3) + (h/3), fill='blue')
canvas.create_rectangle(x, y+(h/3)+(h/3), x + w, y +
                        (h/3) + (h/3) + (h/3), fill='red')


tkinter.mainloop()
