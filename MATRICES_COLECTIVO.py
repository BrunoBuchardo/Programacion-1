from Package_Input.Input import *
import random


"""
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes 
(cada uno con un legajo distinto generado aleatoriamente).

Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 
Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer 
está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más 
de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede 
tener varias recaudaciones diarias.
Mostrar la recaudación de cada coche y línea.
Calcular y mostrar recaudación por línea.
Calcular y mostrar recaudación por coche.
Calcular y mostrar la recaudación total.
Salir

Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, 
generación y verificación de existencia de legajo, cálculos, etc.
"""

# Matriz de legajos de choferes
legajo_colectiveros = [
    [3014, 5451, 8745, 9854, 1496],
    [4758, 3625, 4561, 9874, 3219],
    [6958, 1425, 4510, 6547, 8793]
]


# Validar legajo del chofer
def validar_legajo(legajo_colectiveros: list):
    while True:
        ingrese_legajo = get_int("Ingrese su numero de legajo: ", "Ingrese un numero de legajo valido: ", 1000, 9999, 3)

        for fila in legajo_colectiveros:
            if ingrese_legajo in fila:
                return True  # Legajo encontrado
        
        print("Legajo inválido. Por favor, reingrese el legajo.")


# Crear matriz de recaudaciones
def matriz_lineas_coches(filas, columnas):
    return [[0] * columnas for _ in range(filas)]


# Ingresar recaudaciones por línea y coche
def ingresar_datos(matriz):
    while True:
        columna = get_int("Ingrese el coche: ", "Error, ingrese un coche valido: ", 1, 5, 3)
        fila = get_int("Ingrese la linea: ", "Error, ingrese una linea valida: ", 1, 3, 3)

        recaudacion = get_float("Ingrese la recaudacion: ", "Error, ingrese una recaudacion valida: ", 0, 999999, 3)
        matriz[fila - 1][columna - 1] += recaudacion

        continuar = input("¿Desea cargar otra recaudación? (S/N): ")
        if continuar.upper() != 'S':
            break


# Mostrar recaudación por coche y línea
def mostrar_recaudacion_por_coche_y_linea(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"Línea {i+1}, Coche {j+1}: ${matriz[i][j]}")
        print()


# Calcular y mostrar recaudación por línea
def recaudacion_por_linea(matriz):
    for i in range(len(matriz)):
        recaudacion_total_linea = 0  # Se inicializa fuera del bucle interno
        for j in range(len(matriz[i])):
            recaudacion_total_linea += matriz[i][j]
        print(f"Recaudación total para la línea {i+1}: ${recaudacion_total_linea}")
    print()


# Calcular y mostrar recaudación por coche
def recaudacion_por_coche(matriz):
    for j in range(len(matriz[0])):
        recaudacion_total_coche = 0  # Se inicializa fuera del bucle interno
        for i in range(len(matriz)):
            recaudacion_total_coche += matriz[i][j]
        print(f"Recaudación total para el coche {j+1}: ${recaudacion_total_coche}")
    print()


# Calcular y mostrar recaudación total
def recaudacion_total(matriz):
    total = 0
    for fila in matriz:
        for valor in fila:
            total += valor
    print(f"Recaudación total de todas las líneas y coches: ${total}")
    print()


# Menú de opciones
def menu_opciones():
    if not validar_legajo(legajo_colectiveros):
        print("Legajo inválido.")
        return

    matriz = matriz_lineas_coches(3, 5)
    ingresar_datos(matriz)

    while True:
        print("Menu:\n"
              "A. Mostrar la recaudación de cada coche y línea.\n"
              "B. Calcular y mostrar recaudación por línea.\n"
              "C. Calcular y mostrar recaudación por coche.\n"
              "D. Calcular y mostrar la recaudación total.\n"
              "E. Salir")

        opcion = input("Seleccione una opcion: ").upper()

        match opcion:
            case "A":
                mostrar_recaudacion_por_coche_y_linea(matriz)
            case "B":
                recaudacion_por_linea(matriz)
            case "C":
                recaudacion_por_coche(matriz)
            case "D":
                recaudacion_total(matriz)
            case "E":
                break


menu_opciones()
