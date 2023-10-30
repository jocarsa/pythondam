from tkinter import *

marco = Frame(width=300,height=30)
marco.pack(padx=30,pady=30)

lienzo = Canvas()
lienzo.create_line(10,100,10,10,40,10,40,100)
lienzo.create_line(10,50,40,50)



lienzo.pack(side=TOP)
