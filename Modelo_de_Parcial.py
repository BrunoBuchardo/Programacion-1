# Una empresa se dedica al almacenamiento y posterior distribución de
# cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA,
# que generalmente se encuentran en las inmediaciones de las estaciones del
# ferrocarril.

# Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo,
# cebada y centeno.

# La oficina central, recibe mensualmente una planilla de existencias donde se
# indican las existencias de cada cereal para cada depósito.

# Realizar un menú de opciones:
# 1. Obtener existencias: para ello deberá crear una función que cargue la
# existencia de cada grano en todos los depósitos. Los valores estarán
# comprendidos entre 5000 Kg y 20000 Kg.
# 2. Calcular por cada depósito la cantidad total de kilos almacenados entre
# todos los cereales.
# 3. Nombre del cereal que almaceno menos kilos en cada depósito.
# 4. Máxima cantidad de kilos almacenados de cada cereal.
# 5. Depósito con mayor recaudación, teniendo en cuenta que disponemos
# de un vector con los valores por kilo de cada tipo de cereal.
# 6. Cantidad de depósitos que hayan almacenado más de 50000 kilos
# entre los 4 cereales.
# 7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
# Además mostrar el nombre del cereal con el máximo porcentaje.
# 8. Generar un informe con la recaudación de cada depósito, ordenada de
# mayor a menor.

import random
from os import system

# Constantes
numero_depositos = 20
cereales = ["maíz", "trigo", "cebada", "centeno"]
minimo_kg = 5000
maximo_kg = 20000

# Valores por kilo de cada cereal (opción 5)
valores_por_kg = [10, 8, 12, 7]  # Ejemplo de precios por kilo

# 1. Obtener existencias
def cargar_existencias():
    existencias = []
    for i in range(numero_depositos):
        deposito = []
        for j in range(len(cereales)):
            deposito += [random.randint(minimo_kg, maximo_kg)]  
        existencias += [deposito]  
    return existencias
# 2. Calcular total de kilos por depósito
def calcular_totales_depositos(existencias):
    totales = [0] * numero_depositos
    for i in range(numero_depositos):
        total = 0
        for j in range(len(cereales)):
            total += existencias[i][j]
        totales[i] = total
    return totales
# 3. Nombre del cereal que almacenó menos kilos en cada depósito
def cereal_menor_en_deposito(existencias):
    menor_cereales = [""] * numero_depositos
    for i in range(numero_depositos):
        menor = existencias[i][0]
        indice_menor = 0
        for j in range(1, len(cereales)):
            if existencias[i][j] < menor:
                menor = existencias[i][j]
                indice_menor = j
        menor_cereales[i] = cereales[indice_menor]
    return menor_cereales
#4 Máxima cantidad de kilos almacenados de cada cereal.
def maxima_cantidad_por_cereal(existencias):
    maximos = [0] * len(cereales)
    for i in range(numero_depositos):
        for j in range(len(cereales)):
            if existencias[i][j] > maximos[j]:
                maximos[j] = existencias[i][j]
    return maximos
#5 Depósito con mayor recaudación, 
def deposito_mayor_recaudacion(existencias, valores_por_kg):
    mayor_recaudacion = 0
    deposito_mayor = -1
    for i in range(numero_depositos):
        recaudacion = 0
        for j in range(len(cereales)):
            recaudacion += existencias[i][j] * valores_por_kg[j]
        if recaudacion > mayor_recaudacion:
            mayor_recaudacion = recaudacion
            deposito_mayor = i + 1
    return deposito_mayor, mayor_recaudacion
#6Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales.
def contar_depositos_mas_50000(existencias):
    cantidad = 0
    for i in range(numero_depositos):
        total_kilos = 0
        for j in range(len(cereales)):
            total_kilos += existencias[i][j]
        if total_kilos > 50000:
            cantidad += 1
    return cantidad
#7  Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Además mostrar el nombre del cereal con el máximo porcentaje.
def calcular_porcentajes_y_maximo(existencias):
    total_general = [0] * len(cereales)
    total_kilos = 0
    
    for i in range(numero_depositos):
        for j in range(len(cereales)):
            total_general[j] += existencias[i][j]
            total_kilos += existencias[i][j]
    
    mayor_porcentaje = 0
    cereal_mayor_porcentaje = ""
    
    for i in range(len(cereales)):
        if total_kilos > 0:  # Evitar división por cero
            porcentaje = (total_general[i] / total_kilos) * 100
            print(f"Porcentaje de {cereales[i]}: {porcentaje}%")
            if porcentaje > mayor_porcentaje:
                mayor_porcentaje = porcentaje
                cereal_mayor_porcentaje = cereales[i]
    
    return cereal_mayor_porcentaje
#8 Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
def generar_informe_recaudacion(existencias, valores_por_kg):
    recaudaciones = [[i + 1, 0] for i in range(numero_depositos)]
    
    for i in range(numero_depositos):
        for j in range(len(cereales)):
            recaudaciones[i][1] += existencias[i][j] * valores_por_kg[j]

    # Algoritmo de ordenamiento burbuja
    for i in range(numero_depositos - 1):
        for j in range(numero_depositos - 1 - i):
            if recaudaciones[j][1] < recaudaciones[j + 1][1]:
                # Intercambio de elementos
                recaudaciones[j], recaudaciones[j + 1] = recaudaciones[j + 1], recaudaciones[j]

    return recaudaciones


def menu():
    """Muestra el menú y maneja las opciones."""
    existencias_cargadas = False
    existencias = []

    while True:
        opcion = input(
            "1. Obtener existencias\n"
            "2. Calcular total de kilos por depósito\n"
            "3. Cereal con menos kilos en cada depósito\n"
            "4. Máxima cantidad de kilos almacenados de cada cereal\n"
            "5. Depósito con mayor recaudación\n"
            "6. Cantidad de depósitos con más de 50000 kilos\n"
            "7. Porcentaje de kilos por cereal\n"
            "8. Generar informe de recaudación\n"
            "9. Salir\n"
            "Elija una opción: "
        )

        match opcion:
            case "1":
                existencias = cargar_existencias()
                existencias_cargadas = True
                print("Existencias cargadas correctamente.")

            case "2":
                if existencias_cargadas:
                    totales = calcular_totales_depositos(existencias)
                    for i in range(numero_depositos):
                        print(f"Depósito {i + 1}: {totales[i]} kilos en total.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "3":
                if existencias_cargadas:
                    menor_cereales = cereal_menor_en_deposito(existencias)
                    for i in range(numero_depositos):
                        print(f"Depósito {i + 1}: El cereal con menos kilos es {menor_cereales[i]}.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "4":
                if existencias_cargadas:
                    maximos = maxima_cantidad_por_cereal(existencias)
                    for i in range(len(cereales)):
                        print(f"Máxima cantidad de {cereales[i]}: {maximos[i]} kilos.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "5":
                if existencias_cargadas:
                    deposito_mayor, recaudacion_mayor = deposito_mayor_recaudacion(existencias, valores_por_kg)
                    print(f"El depósito con mayor recaudación es el depósito {deposito_mayor} con {recaudacion_mayor} unidades monetarias.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "6":
                if existencias_cargadas:
                    cantidad = contar_depositos_mas_50000(existencias)
                    print(f"Cantidad de depósitos con más de 50000 kilos: {cantidad}.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "7":
                if existencias_cargadas:
                    cereal_mayor_porcentaje = calcular_porcentajes_y_maximo(existencias)
                    print(f"El cereal con el mayor porcentaje es {cereal_mayor_porcentaje}.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "8":
                if existencias_cargadas:
                    recaudaciones = generar_informe_recaudacion(existencias, valores_por_kg)
                    print("Recaudaciones ordenadas de mayor a menor:")
                    for i in range(numero_depositos):
                        print(f"Depósito {recaudaciones[i][0]}: {recaudaciones[i][1]} unidades monetarias.")
                else:
                    print("Primero debe cargar las existencias (opción 1).")

            case "9":
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida, intente de nuevo.")


        system("pause")
        system("cls")

if __name__ == "__main__":
    menu()


