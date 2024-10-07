# def cuenta_regresiva(contador: int) -> None:
#     for i in range(contador, -1, -1):
#         print(i)

# cuenta_regresiva(10)


# LA FUNCION SE TIENE QUE LLAMAR ASI MISMA
# DEBE EVALUAR ALGUNA CONDICION DE CORTE (PARA QUE LA FX NOSE LLAME NUEVAMENTE)
# OPERAN CON UN CONJUNTO DE DATOS MAS CHICO O MAS GRANDE 

# def cuenta_regresiva(contador: int) -> None:
#     if contador >= 0:
#         print(contador)
#         cuenta_regresiva(contador - 1)

# cuenta_regresiva(1000)


# def calcular_factorial(numero: int) -> int:
#     factorial = 1
#     for i in range(numero, 0, -1):
#         factorial *= i

#     return factorial

# resultado = calcular_factorial(5)
# print(resultado)

# LA FUNCION SE TIENE QUE LLAMAR ASI MISMA
# DEBE EVALUAR ALGUNA CONDICION DE CORTE (PARA QUE LA FX NOSE LLAME NUEVAMENTE)
# OPERAN CON UN CONJUNTO DE DATOS MAS CHICO O MAS GRANDE 

# def calcular_factorial(numero: int) -> int:
#     if numero >= 1:
#         factorial = numero * calcular_factorial(numero-1)
#     else:
#         factorial = 1

#     return factorial

# resultado = calcular_factorial(5)
# print(resultado)
################################################################################
# def calcular_potencia(base: int, exponente: int) -> float:
#     if exponente == 0:
#         resultado = 1  # Cualquier número elevado a 0 es 1
#     elif exponente < 0:
#         resultado = 1 / calcular_potencia(base, -exponente)  # Exponentes negativos
#     else:
#         resultado = base * calcular_potencia(base, exponente - 1)  # Exponentes positivos
    
#     return resultado

# # Ejemplo de uso
# print(calcular_potencia(2, 4))   # 2^4 = 16
# print(calcular_potencia(2, -2))  # 2^-2 = 0.25
# print(calcular_potencia(2, 0))   # 2^0 = 1


#POSITIVOS NEGATIVOS 0
