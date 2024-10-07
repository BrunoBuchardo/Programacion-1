#Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = input("Ingrese un numero: ")
numero = int(numero)

for i in range(numero + 1):
    print(i)
