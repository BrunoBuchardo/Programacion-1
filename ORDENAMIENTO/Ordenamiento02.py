# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, 
# y devuelva un único vector también ordenado. 
# La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.

def intercalar_vectores(vector_uno: int, vector_dos: int, descendente=False):
    i, j = 0, 0
    numero_uno, numero_dos = len(vector_uno), len(vector_dos)
    resultado = [0] * (numero_uno + numero_dos)  # Vector de tamaño adecuado
    vector_resultado = 0  # Índice para el vector resultado

    while i < numero_uno and j < numero_dos:
        if (not descendente and vector_uno[i] <= vector_dos[j]) or (descendente and vector_uno[i] > vector_dos[j]):
            resultado[vector_resultado] = vector_uno[i]
            i += 1
        else:
            resultado[vector_resultado] = vector_dos[j]
            j += 1
        vector_resultado += 1

    while i < numero_uno:
        resultado[vector_resultado] = vector_uno[i]
        i += 1
        vector_resultado += 1

    while j < numero_dos:
        resultado[vector_resultado] = vector_dos[j]
        j += 1
        vector_resultado += 1

    if descendente:
        for i in range(len(resultado) // 2):
            auxiliar = resultado[i]
            resultado[i] = resultado[len(resultado) - 1 - i]
            resultado[len(resultado) - 1 - i] = auxiliar

    return resultado

vector_uno = [1, 3, 5, 7]
vector_dos = [2, 4, 6, 8]

print(intercalar_vectores(vector_uno, vector_dos)) 
print(intercalar_vectores(vector_uno, vector_dos, descendente=True))
