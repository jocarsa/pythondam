nombres = ('Jose','Juan','Jorge')

print(nombres)
print(nombres[0])

##nombres[0] = 'Julia'

##nombres.append('Julia')

#truco

lnombres = list(nombres)
lnombres.append('Julia')
nombres = tuple(lnombres)
print(nombres)
