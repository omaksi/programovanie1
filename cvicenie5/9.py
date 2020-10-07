import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def koleso(x, y, r=15, color='blue'):
    canvas.create_oval(x-(r), y-(r), x+(r), y+(r), fill=color)


def doska(x, y, a=100, b=20, color='red'):
    canvas.create_rectangle(x-(a/2), y-b, x+(a/2), y, fill=color)


def vozik(x, y):
    doska(x, y)
    koleso(x-30, y)
    koleso(x+30, y)


def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x-35, y, 25, 'orange')
    koleso(x+35, y, 25, 'orange')


vozik(200, 100)
velky_vozik(150, 200)
vozik(300, 210)

tkinter.mainloop()
