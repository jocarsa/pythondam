import mysql.connector as my
try:
    mibd = my.connect(
        host = "localhost",
        port = "8889",
        user = "josevicente",
        password = "josevicente",
        database = "cursopython"
        )

    ##print(mibd)

    micursor = mibd.cursor()

    micursor.execute("SELECT * FROM personas")

    miresultado = micursor.fetchall()

    ##print(miresultado)

    for i in miresultado:
        print("tengo un resultado que es:")
        print(i[1])
except:
    print("ha ocurrido algun error en la base de datos")

