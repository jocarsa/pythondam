'''
Programa calculadora
(c) 2020 Jose Vicente Carratala
v0.1
'''
## Bienvenida al programa
print("bienvenido al programa calculadora")
print("Introduce tu nombre")
nombre = input()
print("Hola",nombre,"te doy la bienvenida al programa calculadora")
def calculadora():
    ## Indica la operacion
    print("Ahora elige la operación que vas a realizar"+
        "\n1.-Suma"+
        "\n2.-Resta"+
        "\n3.-Multiplicacion"+
        "\n4.-Division"+
          "")
    operacion = int(input())
    print("La operacion que has elegido es",operacion)
    ## Introduce dos numeros
    print("Ahora introduce un numero")
    numero1 = int(input())
    print("Ahora introduce otro numero")
    numero2 = int(input())

    ## Realiza la operacion
    if operacion == 1:
        print("El resultado es:",(numero1+numero2))

    if operacion == 2:
        print("El resultado es:",(numero1-numero2))

    if operacion == 3:
        print("El resultado es:",(numero1*numero2))

    if operacion == 4:
        print("El resultado es:",(numero1/numero2))

    calculadora()

calculadora()

