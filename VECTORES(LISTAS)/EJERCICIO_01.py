# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

def calcular_promedio(lista_enteros):
    suma = 0
    cantidad = 0
    
    for numero in lista_enteros:
        suma += numero
        cantidad += 1

    if cantidad == 0:
        resultado = 0  
    else:
        resultado = suma / cantidad  

    return resultado  

# Ejemplo de uso
lista = [10, 20, 30, 40, 50]
resultado = calcular_promedio(lista)
print(f"El promedio es: {resultado}")
