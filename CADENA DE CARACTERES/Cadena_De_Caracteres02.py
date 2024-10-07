# Crear una función que reciba una cadena y un caracter. 
# La función deberá devolver el índice en el que se encuentre la primera ocurrencia de dicho caracter,
#  o -1 en caso de que no esté.

def encontrar_caracter(cadena, caracter):
    indice = -1  
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i
            break  
    return indice


cadena = "Hola, mundo!"
caracter = "m"
indice = encontrar_caracter(cadena, caracter)
print(indice)  
