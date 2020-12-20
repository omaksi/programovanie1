import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

x, y = 70, 100
r = 50
dx, dy = 120, 60


canvas.create_oval(x-r, y-r, x+r, y+r, outline='blue', width=15)
canvas.create_oval(x-r+dx, y-r, x+r+dx, y+r, outline='black', width=15)
canvas.create_oval(x-r+dx+dx, y-r, x+r+dx+dx, y+r, outline='red', width=15)

canvas.create_oval(x-r+(dx/2), y-r+(dy), x+r+(dx/2),
                   y+r+(dy), outline='yellow', width=15)
canvas.create_oval(x-r+(dx/2)+dx, y-r+(dy), x+r+(dx/2) +
                   dx, y+r+(dy), outline='green', width=15)

tkinter.mainloop()
