import numpy as np

coleccion1 = np.array(['Juan','Jorge','Jose','Julia','Javier','Jacobo'])

coleccion2 = np.array(['Pablo','Pedro','Paco','Pio','Paloma'])


juntado = np.concatenate((coleccion1,coleccion2))

print(juntado)

separado = np.array_split(juntado,3)
print("Que sepas que la primera parte del partido es")
print(separado[0])
print("Que sepas que la segunda parte del partido es")
print(separado[1])
print("Que sepas que la tercera parte del partido es")
print(separado[2])
