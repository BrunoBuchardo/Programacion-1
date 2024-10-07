#Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base: int, exponente: int) ->int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    
    return resultado

resultado = calcular_potencia(2, 4)
print(resultado)