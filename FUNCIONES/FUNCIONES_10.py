#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def pedir_numero():
    numero = input("Ingrese un numero: ")
    numero = int(numero)

    return numero

numero = pedir_numero()
print(numero)