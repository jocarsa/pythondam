import os
import time


os.system('./soycyescribo')

time.sleep(2)


archivo = open("datos.txt",'r')
misdatos = archivo.readline()
print(misdatos)
