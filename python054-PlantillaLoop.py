import tkinter as tk

class Persona(object):
    def saluda():
        print("yo soy una persona")

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        #Este método se va a ejecutar una sola vez
        print("este es el metodo constructor")
        ## Desde el constructor quiero arrancar una vez el bucle
        self.master.after(1000,self.bucle)
    def bucle(self):
        #Este método se va a ejecutar de forma continua
        print("el programa ha arrancando y empezará a dar vueltas")
        #yo hago cosas
        #... y esas cosas tardan 100 milisegundos en hacerse
        #yo hago cosas
        self.master.after(33,self.bucle)
        

        
root = tk.Tk()
aplicacion = Aplicacion(root)
