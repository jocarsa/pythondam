import json 

archivo = open("agenda.json",'r')

micadena = archivo.readline()

carga = json.loads(micadena)
print(type(micadena))
print(type(carga))

print(carga["Jose"])
