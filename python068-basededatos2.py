import matplotlib.pyplot as plt
import mysql.connector as my

## Parte de la base de datos
mibd = my.connect(
    host = "localhost",
    port = "8889",
    user = "josevicente",
    password = "josevicente",
    database = "cursopython"
    )

micursor = mibd.cursor()

micursor.execute("select FROM_UNIXTIME(`utc`, '%d.%m.%Y') as ndate,  count(id) as post_count from registros3 group by ndate")
miresultado = micursor.fetchall()

lista = []

for i in miresultado:
    lista.append(i[1])
    print(str(i[1])+" - "+str(i[0]))



plt.plot(lista)
plt.ylabel('visitas')
plt.show()
