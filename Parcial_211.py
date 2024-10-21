# Desarrolle una función que reciba una cadena de caracteres y 
# verifique si todos los caracteres en la cadena son digitos hexadecimales. 
# Los números hexadecimales están compuestos por los dígitos del 0 al 9 y las letras de la A a la F. 
# Si todos los caracteres son válidos en el sistema hexadecimal, la función debe devolver True. 
# Si alguno de los caracteres no pertenece al conjunto de los hexadecimales, la función debe devolver False.

# La función debe estar debidamente documentada y adornada.


def es_hexadecimal(cadena: str) -> bool:
    es_valido = True
    for i in range(cadena):
        if 0 <= cadena <= 9:
            es_valido = True
        elif "A" <= cadena <= "F":
            es_valido = True
        elif "a" <= cadena <= "f":
            es_valido = True
        else:
            es_valido = False
            break
    return es_valido

cadena = es_hexadecimal
print(es_hexadecimal)


#######################################################################################
from os import system

precio_apple = 70
precio_tesla = 90
precio_nvidia = 105

acciones_clientes = [[0,0,0] for _ in range(15)]

def cargar_acciones():
    for i in range(15):
        print(f"Ingreso de acciones por cliente {i + 1}")
        

    acciones_apple = int(input("Ingrese la cantidad de acciones de Apple (0-500): "))
    while acciones_apple < 0 or acciones_apple > 500:
        acciones_apple = int(input("Error ingrese una cantidad de acciones validaa."))
    acciones_clientes[0] = acciones_apple

    acciones_tesla = int(input("Ingrese la cantidad de acciones de Tesla (0-500): "))
    while acciones_tesla < 0 or acciones_tesla > 500:
        acciones_tesla = int(input("Error ingrese una cantidad de acciones validaa."))
    acciones_clientes[1] = acciones_tesla

    acciones_nvidia = int(input("Ingrese la cantidad de acciones de Nvidia (0-500): "))
    while acciones_nvidia < 0 or acciones_nvidia > 500:
        acciones_nvidia = int(input("Error ingrese una cantidad de acciones validaa."))
    acciones_clientes[2] = acciones_nvidia


def mostrar_acciones():
    for i in range(15):
        print(f"Cliente {i + 1}: Apple: {acciones_clientes[i][0]}, Tesla: {acciones_clientes[i][1]}, Nvidia: {acciones_clientes[i][2]}")

def calcular_porcentajes():
    total_apple, total_tesla, total_nvidia = 0, 0, 0
    total_acciones = 0
    for i in range(15):
        total_apple += acciones_clientes[i][0]
        total_tesla += acciones_clientes[i][1]
        total_nvidia += acciones_clientes[i][2]

    total_acciones = total_apple + total_tesla + total_nvidia

    if total_acciones > 0:
        porcentaje_apple = (total_apple * 100) / total_acciones
        porcentaje_tesla = (total_tesla * 100) / total_acciones
        porcentaje_nvidia = (total_nvidia * 100) / total_acciones
    else:
        porcentaje_apple = porcentaje_tesla = porcentaje_nvidia = 0

    print(f"Porcentaje de Apple: {porcentaje_apple}%")
    print(f"Porcentaje de Tesla: {porcentaje_tesla}%")
    print(f"Porcentaje de Nvidia: {porcentaje_nvidia}%")
















def menu():
    """""Muestra el menu y maneja las opciones"""""
    while True:
        opcion = input(
            "1. Cantidad de acciones que dispone cada cliente.\n"
            "2. Porcentaje de cada tipo de accion, sobre el total de acciones y accion con menor porcentaje.\n"
            "3. Total de inversion en dolares de cada cliente.\n"
            "4. Informe sobre las teniencias en dolares de cada cliente ordenadas de mayor a menor.\n"
            "5. Cantidad de clientes que hayan invertido en Apple pero no en Tesla y porcentaje que representa esa cantidad.\n"
            "6. Salir\n"
            "Elija una opcion: "
        )

        match opcion:
            case "1":

            case "2":

            case "3":

            case "4":

            case "5":

            case "6":
                print("Saliendo del programa. ")
                break

            case _:
                print("Opcion no valida, intente de nuevo")

    system("pause")
    system("cls")

if __name__ == "__main__":
    menu()
