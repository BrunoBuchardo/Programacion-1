from Package_Input.Input import *

numero = get_int("Ingrese un número entre 1 y 10: ", "Error: número inválido", 1, 10, 3)
print(f"Número ingresado: {numero}")


numero = get_float("Ingrese un número entre 0,5 y 1.0: ", "Error: número inválido", 0.5, 1.0, 3)
print(f"Número ingresado: {numero}")

resultado = get_string(4)
if resultado:
    print(f"Cadena válida: {resultado}")
else:
    print("La longitud de la cadena es incorrecta.")

