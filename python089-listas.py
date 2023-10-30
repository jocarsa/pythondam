nombres = ['Jose','Juan','Jorge']
print(nombres)

print(nombres[1])

print(nombres[-1])

# Mutables

# nombres[3] = 'Julia'
nombres.append('Julia')
print(nombres)
nombres.pop(0)
print(nombres)
nombres[0] = 'Julia'
