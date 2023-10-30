import mysql.connector as my

mibd = my.connect(
    host = "localhost",
    user = "josevicente",
    password = "josevicente"
    )

print(mibd)
