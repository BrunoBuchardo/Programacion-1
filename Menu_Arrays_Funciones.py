"""Menú - Arrays -  Funciones
Actividades

Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
Mostrar la cantidad de números positivos y negativos.
Mostrar la sumatoria de los números pares.
Informar el mayor de los números impares.
Listar todos los números ingresados.
Listar todos los números pares.
Listar los números de las posiciones impares.  
Salir

Notas:
Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.
Todas las opciones deberán ser programadas en funciones: habrá funciones específicas 
(por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). 
Tener en cuenta las características de la programación funcional.
Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. 
Todos estos módulos deben estar integrados en el paquete Package_Arrays.
Utilizar las funciones input del paquete Package_Input.
Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar los módulos y paquetes."""""

from os import system
from Package_Input.Input import *
from Package_Arrays.Array_Generales import *


def ingresar_numeros():
    """Ingresa 10 números enteros entre -1000 y 1000."""
    numeros = [0] * 10  
    for i in range(10):
        numeros[i] = get_int("Ingrese un número entero entre -1000 y 1000: ", "Error", -1000, 1000, 3)
    return numeros

def menu():
    """Muestra el menú y maneja las opciones."""
    numeros_ingresados = False
    numeros = []
    
    while True:
        opcion = input(
            "1. Ingresar números\n"
            "2. Mostrar cantidad de números positivos y negativos\n"
            "3. Mostrar la sumatoria de los números pares\n"
            "4. Informar el mayor de los números impares\n"
            "5. Listar todos los números ingresados\n"
            "6. Listar todos los números pares\n"
            "7. Listar los números de las posiciones impares\n"
            "8. Salir\n"
            "Elija una opción: "
        )

        match opcion:
            case "1":
                numeros = ingresar_numeros()
                numeros_ingresados = True
                print("Números ingresados correctamente.")
            
            case "2":
                if numeros_ingresados:
                    positivos, negativos = contar_positivos_negativos(numeros)
                    print(f"Números positivos: {positivos}, Números negativos: {negativos}")
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "3":
                if numeros_ingresados:
                    suma_pares = sumatoria_pares(numeros)
                    print(f"La sumatoria de los números pares es: {suma_pares}")
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "4":
                if numeros_ingresados:
                    mayor = mayor_impar(numeros)
                    if mayor is not None:
                        print(f"El mayor de los números impares es: {mayor}")
                    else:
                        print("No hay números impares.")
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "5":
                if numeros_ingresados:
                    print("Números ingresados:", listar_numeros(numeros))
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "6":
                if numeros_ingresados:
                    print("Números pares:", listar_pares(numeros))
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "7":
                if numeros_ingresados:
                    print("Números en posiciones impares:", listar_impares_posiciones(numeros))
                else:
                    print("Primero debe ingresar los números (opción 1).")
            
            case "8":
                print("Saliendo...")
                break
            
            case _:
                print("No eligió una opción correcta.")
        
        system("pause")
        system("cls")


if __name__ == "__main__":
    menu()

    
       
