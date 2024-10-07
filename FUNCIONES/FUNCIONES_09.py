# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación.
# Por defecto es del 1 al 10.

def tabla_multiplicar(numero, inicio, fin):
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

numero = input("Ingrese un numero: ")
numero = int(numero) 
inicio = input("Ingrese un numero: ")
inicio = int(inicio)
fin = input("Ingrese un numero: ")
fin = int(fin)

resultado = tabla_multiplicar(numero, inicio, fin)

