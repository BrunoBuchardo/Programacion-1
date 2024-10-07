#Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma_numeros = 0
contador_promedio = 0

for i in range(10):
    numero = input("Ingrese un número: ")
    numero = int(numero)
    if numero == 0:
        break
    suma_numeros += numero
    contador_promedio += 1

if contador_promedio > 0:
    promedio = suma_numeros / contador_promedio
else:
    promedio = 0

print(f"Suma de los números: {suma_numeros}")
print(f"Promedio de los números: {promedio}")

