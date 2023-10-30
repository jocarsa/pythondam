archivo = open("miarchivo.txt",'r')

##print(archivo.readline())
##print(archivo.readline())

##print(archivo.read())
contador = 0
for i in range(0,10):
    contador += 1
    print(archivo.readline())
    if archivo.readline() == "" and contador > 5:
        break


