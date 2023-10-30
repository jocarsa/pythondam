import mysql.connector as my
import matplotlib.pyplot as plt
import numpy as np

## Parte de la base de datos
mibd = my.connect(
    host = "localhost",
    port = "8889",
    user = "josevicente",
    password = "josevicente",
    database = "cursopython"
    )

micursor = mibd.cursor()

micursor.execute("SELECT COUNT(Nombre) AS cuenta, Nombre FROM Alumnos GROUP BY Nombre ORDER BY cuenta DESC LIMIT 100")
miresultado = micursor.fetchall()
longaniza = "'hola'";
performance = [0]
for i in miresultado:

        longaniza += ",'"+str(i[1])+"'"
        performance.append(i[0])

people = eval(longaniza) 
print(people)
plt.rcdefaults()
fig, ax = plt.subplots()

# Example data

y_pos = np.arange(len(people))

print(performance)
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('Frecuencia de nombres')

plt.show()







