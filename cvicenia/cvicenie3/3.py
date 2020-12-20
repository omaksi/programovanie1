import tkinter

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

x, y = 50, 50
a1, a2 = 180, 100

canvas.create_rectangle(x, y, x+a1, y+a1, fill='indian red')
canvas.create_text(x, y, text='A', anchor='se',
                   fill='black', font='arial 10')
canvas.create_text(x+a1, y, text='B', anchor='sw',
                   fill='black', font='arial 10')
canvas.create_text(x, y+a1, text='C', anchor='ne',
                   fill='black', font='arial 10')
canvas.create_text(x+a1, y+a1, text='D', anchor='nw',
                   fill='black', font='arial 10')
canvas.create_text(x+a1, y+(a1/2), text=str(a1), anchor='w',
                   fill='black', font='arial 10')

d = ((a1/2)-(a2/2))
canvas.create_rectangle(x + d, y + d, x+d+a2, y+d+a2, fill='light blue')
canvas.create_text(x+d+(a2/2), y+d+(a2), text=str(a2), anchor='s',
                   fill='black', font='arial 10')

tkinter.mainloop()
