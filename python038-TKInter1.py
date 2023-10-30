from tkinter import *

marco = Frame(width=300,height=300)
marco.pack(padx=30,pady=30)

titulo = Label(marco,text="Programa agenda v0.1",fg="black",font=("Arial,Verdana,sans-serif",24))
titulo.pack(side=TOP)

autor = Label(marco,text="Jose Vicente Carratala",fg="grey",font=("Arial,Verdana,sans-serif",16))
autor.pack(side=TOP)

foto = PhotoImage(file="josevicente4.png",width=100,height=100)

textofoto = Label(marco,image=foto)
textofoto.pack(side=TOP)

mainloop()
