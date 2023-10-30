from tkinter import *
import random

marco = Frame(width=300,height=30)
marco.pack(padx=30,pady=30)

lienzo = Canvas()
lienzo.create_line(10,10,10,200,200,200)

xanterior = 10
yanterior = 200

for i in range(0,30):
    xactual = xanterior + 10
    yactual = random.randint(10,200)
    lienzo.create_rectangle(xactual,200,xactual+10,200-yactual,outline="#ff0000",fill="#00ff00")
    xanterior = xactual
    yanterior = yactual


lienzo.pack(side=TOP)
