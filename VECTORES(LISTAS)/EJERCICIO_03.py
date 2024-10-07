# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def calcular_producto(lista_enteros):
    producto = 1  
    
    for numero in lista_enteros:
        producto *= numero

    return producto


lista = [10, 20, 30, 40, 50]
resultado_producto = calcular_producto(lista)
print(f"El producto es: {resultado_producto}")
