import numpy as np

coleccion1 = np.array(['Juan','Jorge','Jose','Julia','Javier','Jacobo'])

coleccion2 = np.array(['Pablo','Pedro','Paco','Pio','Paloma'])


juntado = np.concatenate((coleccion1,coleccion2))

print(juntado)
