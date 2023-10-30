archivo = open("agenda.txt",'r')


linea = archivo.read()
print(linea)

partido = linea.split(",")
print(partido)
