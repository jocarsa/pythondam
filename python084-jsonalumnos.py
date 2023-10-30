import json 

archivo = open("alumnos.json",'r')

micadena = archivo.read().replace('\n', '')

carga = json.loads(micadena)
print(type(micadena))
print(type(carga))
print(carga['glossary']['GlossDiv']['title'])


