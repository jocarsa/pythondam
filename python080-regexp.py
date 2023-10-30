import re

mitexto = "Segismundo"
busqueda = re.search("^Se",mitexto)
print(busqueda)
if busqueda:
    print("he encontrado un resultado")
else:
    print("no he encontrado ningun resultado")
