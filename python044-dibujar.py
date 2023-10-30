from tkinter import *

marco = Frame(width=300,height=30)
marco.pack(padx=30,pady=30)

lienzo = Canvas()
lienzo.create_line(15,25,200,250)
lienzo.create_line(15,55,200,270,dash=(4,8))


lienzo.pack(side=TOP)
