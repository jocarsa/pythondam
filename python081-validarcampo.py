import re

print("Introduce un numero")
email = input()
regla = r'^([\s\d]+)$'

validacion = re.search(regla,email)

if validacion:
    print("ok")
else:
    print("no ok")
