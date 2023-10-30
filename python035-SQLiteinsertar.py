##Para poder trabajar con bases de datos
import sqlite3 as lite
import sys

##Me conecto a una base de datos llamada agenda
conexion = lite.connect("agenda.sqlite")

##Establezco un cursor para saber en que punto de la base de datos voy a trabajar
cursor = conexion.cursor()

##Le pido algo a la base de datos en lenguaje SQL
cursor.execute("INSERT INTO contactos VALUES(NULL,'Jorge','222222','jorge@correo.com');")

conexion.commit()
