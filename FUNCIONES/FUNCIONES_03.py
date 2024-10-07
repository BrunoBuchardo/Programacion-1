#Crea una función que verifique si un número dado es par o impar. 
#La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_paridad(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

numero = input("Ingrese el numero: ")
numero = int(numero)

resultado = verificar_paridad(numero)
