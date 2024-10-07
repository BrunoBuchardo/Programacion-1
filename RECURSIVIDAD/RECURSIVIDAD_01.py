
#Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero: int) ->int:
    if numero >= 1:
        resultado = numero + sumar_naturales(numero-1)
    else:
        resultado = 0

    return resultado

resultado = sumar_naturales(6)
print(resultado)

