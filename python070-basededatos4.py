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
longaniza = "'hola'";
performance = [0]

micursor.execute("SELECT COUNT(id) AS cuenta FROM 	registros3 WHERE `browser` LIKE ('%Macintosh%')")
miresultado = micursor.fetchall()
for i in miresultado:
        longaniza += ",'Macintosh'"
        performance.append(i[0])

micursor.execute("SELECT COUNT(id) AS cuenta FROM 	registros3 WHERE `browser` LIKE ('%Windows%')")
miresultado = micursor.fetchall()
for i in miresultado:
        longaniza += ",'Windows'"
        performance.append(i[0])

micursor.execute("SELECT COUNT(id) AS cuenta FROM 	registros3 WHERE `browser` LIKE ('%Linux%')")
miresultado = micursor.fetchall()
for i in miresultado:
        longaniza += ",'Linux'"
        performance.append(i[0])


micursor.execute("SELECT COUNT(id) AS cuenta FROM 	registros3 WHERE `browser` LIKE ('%iPhone%')")
miresultado = micursor.fetchall()
for i in miresultado:
        longaniza += ",'iPhone'"
        performance.append(i[0])

micursor.execute("SELECT COUNT(id) AS cuenta FROM 	registros3 WHERE `browser` LIKE ('%Android%')")
miresultado = micursor.fetchall()
for i in miresultado:
        longaniza += ",'Android'"
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
ax.set_title('Sistemas operativos')

##plt.show()
plt.plot('foo.png')







