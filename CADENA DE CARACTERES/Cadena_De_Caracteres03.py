# Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. 
# Deberá retornar un valor booleano indicando lo sucedido.

def es_palindromo(cadena):
    longitud = len(cadena)
    es_palindrome = True  # Inicializa como True
    
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            es_palindrome = False
            break  # Sale del bucle si no es un palíndromo
            
    return es_palindrome

cadena1 = "anilina"
cadena2 = "hola"
print(es_palindromo(cadena1))  # Salida: True
print(es_palindromo(cadena2))  # Salida: False
