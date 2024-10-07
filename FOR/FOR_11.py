#Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = 10
contador_primos = 0

for x in range(2, numero + 1):
    es_primo = True
    for i in range(2, x):
        if x % i == 0:                    
            es_primo = False
            break

    if numero > 1 and es_primo:
        contador_primos += 1
        print(x)

print(f"Se encontraron: {contador_primos}")

