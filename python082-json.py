import json 


micadena = '{"Juan":"juan@correo.com","Jorge":"jorge@correo.com","Javier":"javier@correo.com","Julia":"julia@correo.com","Jacobo":"jacobo@correo.com"}'

carga = json.loads(micadena)
print(type(micadena))
print(type(carga))

print(carga["Juan"])
