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

    micursor.execute("UPDATE personas SET telefono = '987654'")
    mibd.commit()

except:
    print("ha ocurrido algun error en la base de datos")

