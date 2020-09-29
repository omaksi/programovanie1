import tkinter
import random

canvas = tkinter.Canvas(bg="navy")
canvas.pack()

n = 200

for i in range(n):
    canvas.create_text(random.randint(0, 300), random.randint(0, 200), text='*', anchor='center',
                       fill='yellow', font=f"arial {random.randint(10, 20)}")

tkinter.mainloop()
