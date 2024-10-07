# Crear una función que reciba como parámetro una cadena y 
# determine la cantidad de vocales que hay de cada una (individualmente). 
# La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.

def contar_vocales(cadena):
    # Definimos las vocales y la matriz para contar
    vocales = ['a', 'e', 'i', 'o', 'u']
    matriz_vocales = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]

    # Recorremos cada carácter de la cadena
    for caracter in cadena:
        # Comprobamos si el carácter es una vocal (en minúscula o mayúscula)
        if caracter == 'a' or caracter == 'A':
            matriz_vocales[0][1] += 1
        elif caracter == 'e' or caracter == 'E':
            matriz_vocales[1][1] += 1
        elif caracter == 'i' or caracter == 'I':
            matriz_vocales[2][1] += 1
        elif caracter == 'o' or caracter == 'O':
            matriz_vocales[3][1] += 1
        elif caracter == 'u' or caracter == 'U':
            matriz_vocales[4][1] += 1

    return matriz_vocales

# Ejemplo de uso
cadena = "pancichueco"
resultado = contar_vocales(cadena)

# Imprimir el resultado
for fila in resultado:
    print(f"'{fila[0]}'\n{fila[1]}")
