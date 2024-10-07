#Realizar un programa que permita mostrar una pirámide de números.

numero = input("Introduce la altura de la pirámide: ")
numero = int(numero)

for i in range(1, numero + 1):
    # Imprimir espacios
    for j in range(numero - i):
        print(" ", end="")
    
    # Imprimir números ascendentes
    for j in range(1, i + 1):
        print(j, end="")
    
    # Imprimir números descendentes
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()