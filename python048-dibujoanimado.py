from tkinter import *
import time

marco = Frame(width=300,height=30)
marco.pack(padx=30,pady=30)

lienzo = Canvas()


while 1:
    print("hola")
    lienzo.create_rectangle(10,10,200,200,outline="#ff0000",fill="#00ff00")

    lienzo.create_oval(50,50,200,200,fill="#0000ff",outline="#ffffff",width=5)

    lienzo.pack(side=TOP)
    time.sleep(1)
