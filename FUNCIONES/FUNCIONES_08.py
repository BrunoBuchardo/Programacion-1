# Crear una función que (utilizando la función del punto 11 for), muestre todos los números primos comprendidos entre la 
# unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados.

def contar_primos(numero):
    contador_primos = 0

    for x in range(2, numero + 1):
        es_primo = True
        
        for i in range(2, x):
            if x % i == 0:
                es_primo = False
                break

        if es_primo:
            contador_primos += 1
            print(x)

    return contador_primos

numero = input("Ingrese un numero: ")
numero = int(numero)

resultado = contar_primos(numero)
print(f"Se encontraron: {resultado} números primos.")
