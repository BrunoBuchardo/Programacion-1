#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio):
    pi = 3.14
    return  pi * radio ** 2

radio = input("Ingrese el radio: ")
radio = int(radio)

resultado = area_circulo(radio)
print(f"El area del circulo es: {resultado}")