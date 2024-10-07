def calcular_fibonacci(numero: int) -> int:
    if numero == 1:
        resultado = 1
    elif numero == 0:
        resultado = 0
    else:
        resultado = calcular_fibonacci (numero - 1) + calcular_fibonacci (numero - 2)

    return resultado

variable = 10
resultado = calcular_fibonacci(variable)
print(resultado)
    