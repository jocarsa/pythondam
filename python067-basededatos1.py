import mysql.connector as my
import matplotlib.pyplot as plt

## Parte de la base de datos
mibd = my.connect(
    host = "localhost",
    port = "8889",
    user = "josevicente",
    password = "josevicente",
    database = "cursopython"
    )

micursor = mibd.cursor()

micursor.execute("SELECT COUNT(Nombre) AS cuenta, Nombre FROM Alumnos GROUP BY Nombre ORDER BY cuenta DESC LIMIT 25")
miresultado = micursor.fetchall()



sizes = [0]

longaniza = "'hola'"
for i in miresultado:

        sizes.append(i[0])
        longaniza += ",'"+str(i[1])+"'"

labels = eval(longaniza) 

print("vamos a comprobar")
print(labels)
print(sizes)
print("quiero ver el tipo de dato")
print(type(labels))


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()




