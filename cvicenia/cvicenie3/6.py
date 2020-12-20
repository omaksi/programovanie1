import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

x, y = 180, 250
sizes = [[200, 50], [150, 50], [100, 50], [50, 50]]
farba = ['green',  'forestgreen', 'limegreen', 'lime']

for i in range(4):
    canvas.create_rectangle(x - (sizes[i][0]/2), y - (i*sizes[i][1]), x - (sizes[i][0]/2) + sizes[i][0],
                            y - (i*sizes[i][1]) + sizes[i][1], fill=farba[i])


tkinter.mainloop()
