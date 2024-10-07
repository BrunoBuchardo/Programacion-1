
def contar_positivos_negativos(numeros):
    """Cuenta la cantidad de números positivos y negativos."""
    positivos = 0
    negativos = 0
    for numero in numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    return positivos, negativos

def sumatoria_pares(numeros):
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

def mayor_impar(numeros):
    mayor = None
    for numero in numeros:
        if numero % 2 != 0:
            if mayor is None or numero > mayor:
                mayor = numero
    return mayor

def listar_numeros(numeros):
    return numeros

def listar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares = pares + [numero]  
    return pares


def listar_impares_posiciones(numeros, i=1):
    if i >= len(numeros):
        resultado = []
    else:
        resultado = [numeros[i]] + listar_impares_posiciones(numeros, i + 2)
    return resultado

