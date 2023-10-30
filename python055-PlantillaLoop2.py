import tkinter as tk

class Persona(object):
    def __init__(self,canvas,*argumentos,**masargumentos):
        self.canvas = canvas
        self.id = canvas.create_oval(*argumentos,**masargumentos)
        self.vx = 5
        self.vy = 0
    def mover():
        #quiero que los elementos se muevan aleatoriamente
        

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        #Este método se va a ejecutar una sola vez
        self.canvas = tk.Canvas(self.master,width=512,height=512)
        self.canvas.pack()
        #Aqui ahora voy a pintar uno o varios ovalos
        self.personas = [
            Persona(self.canvas,50,50,10,10,outline="black",fill="green"),
            Persona(self.canvas,250,250,30,30,outline="red",fill="blue"),

            ]
        self.canvas.pack()
        ## Desde el constructor quiero arrancar una vez el bucle
        self.master.after(1000,self.bucle)
    def bucle(self):
        #Este método se va a ejecutar de forma continua
        
        #El metodo se llama a si mismo
        self.master.after(33,self.bucle)
        

        
root = tk.Tk()
aplicacion = Aplicacion(root)
