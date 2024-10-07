def mostrar_matriz(matriz: list) ->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def multiplicar_matriz_escalar(matriz: list, escalar: int) -> list:
    resultado = crear_matriz(len(matriz), len(matriz[0]), None)
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            resultado[i][j] = escalar * matriz [i][j]

    return resultado


def restar_matrices(primer_matriz: list, segunda_matriz: list) -> list:
    resultado = crear_matriz(len(primer_matriz), len(primer_matriz[0]), None)

    negada = multiplicar_matriz_escalar(segunda_matriz, -1)
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            resultado[i][j] = primer_matriz[i][j] + negada[i][j]

    return resultado


def sumar_matrices(primer_matriz: list, segunda_matriz: list) -> list:
    resultado = crear_matriz(len(primer_matriz), len(primer_matriz[0]), None)
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            resultado[i][j] = primer_matriz[i][j] + segunda_matriz[i][j]

    return resultado


matriz_a = [
    [4,8],
    [3,9],
    [2,1]
]

matriz_b = [
    [2,3],
    [1,3],
    [4,5]
]

suma = sumar_matrices(matriz_a, matriz_b)
mostrar_matriz(suma)