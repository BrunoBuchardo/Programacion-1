from os import system


while True:
    opcion = input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\nElija una opcion: ")
    match opcion:
        case "1":
            print("Estoy sumando...")
        case "2":
            print("Estoy restando...")
        case "3":
            print("Estoy multiplicando...")
        case "4":
            print("Estoy diviendo...")
        case "5":
            print("Estoy saliendo...")
            break
        case _:
            print("No eligio una opcion correcta")
        
    system("pause")
    system("cls")



# from os import system

# def mostrar_menu():
#     print("=" * 40)
#     print("         Bienvenido al menú         ")
#     print("=" * 40)
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")
#     print("=" * 40)

# while True:
#     system("cls")
#     mostrar_menu()
    
#     opcion = input("Elija una opción: ")
#     print()  # Salto de línea para mayor claridad

#     match opcion:
#         case "1":
#             print("🔢 Estoy sumando... ¡Gracias por esperar!")
#         case "2":
#             print("➖ Estoy restando... ¡Gracias por esperar!")
#         case "3":
#             print("✖ Estoy multiplicando... ¡Gracias por esperar!")
#         case "4":
#             print("➗ Estoy dividiendo... ¡Gracias por esperar!")
#         case "5":
#             print("👋 ¡Gracias por usar nuestro programa! ¡Hasta pronto!")
#             break
#         case _:
#             print("⚠ No eligió una opción correcta, por favor intente nuevamente.")
    
#     print()  # Salto de línea para mayor claridad
#     system("pause")

# # Al final, se puede limpiar la pantalla si lo deseas:
# system("cls")
