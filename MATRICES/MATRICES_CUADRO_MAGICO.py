def es_un_cuadrado_magico(matriz):
    numero = len(matriz)
    constante_magica = numero * (numero * numero + 1) // 2
    numeros_validos = [False] * (numero * numero + 1)
    es_magico = True 

    for i in range(numero):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            if valor < 1 or valor > numero * numero or numeros_validos[valor]:
                es_magico = False
            numeros_validos[valor] = True

    for i in range(len(matriz)):
        sumar_fila = 0
        for j in range(len(matriz[i])):
            sumar_fila += matriz[i][j]
        if sumar_fila != constante_magica:
            es_magico = False

    for j in range(numero):
        sumar_columna = 0
        for i in range(len(matriz)):
            sumar_columna += matriz[i][j]
        if sumar_columna != constante_magica:
            es_magico = False
    
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(numero):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][numero - 1 - i]

    if suma_diagonal_principal != constante_magica or suma_diagonal_secundaria != constante_magica:
        es_magico = False

    return es_magico

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]  
]

resultado = es_un_cuadrado_magico(matriz)
if resultado:
    print("La matriz es un cuadrado mágico.")
else:
    print("La matriz no es un cuadrado mágico.")
    
    

    
