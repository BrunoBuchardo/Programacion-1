#Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia(base, exponente):
    return base ** exponente

base = input("Ingrese la base: ")
base = int(base)
exponente = input("Ingrese el exponente: ")
exponente = int(exponente)

resultado = potencia(base, exponente)
print(resultado)