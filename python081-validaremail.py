import re

print("Dime un correo electronico")
email = input()
regla = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

validacion = re.search(regla,email)

if validacion:
    print("Lo que has introducido es un correo electronico y lo voy a meter en la base de datos")
else:
    print("Lo que has introducido no es un correo electronico")
