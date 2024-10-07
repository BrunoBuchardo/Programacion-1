# Escribir una función parecida a la anterior, 
# pero la misma deberá calcular y devolver el promedio de los números positivos.

def calcular_promedio(lista_enteros):
    suma = 0
    cantidad = 0
    
    for numero in lista_enteros:
        if numero > 0:
            suma += numero
            cantidad += 1

    if cantidad == 0:
        resultado = 0  
    else:
        resultado = suma / cantidad  

    return resultado  


lista = [10, 20, -30, 40, -50]
resultado = calcular_promedio(lista)
print(f"El promedio de los numeros positivos es: {resultado}")