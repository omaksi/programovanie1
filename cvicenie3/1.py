import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 50

canvas.create_rectangle(x, y, x+100, y+100, fill='red')
canvas.create_text(x+50, y+50, text='červený', anchor='center',
                   fill='yellow', font='arial 20')
canvas.create_rectangle(x + 110, y, x+210, y+100, fill='blue')
canvas.create_text(x+160, y+50, text='modrý', anchor='center',
                   fill='yellow', font='arial 20')

tkinter.mainloop()
