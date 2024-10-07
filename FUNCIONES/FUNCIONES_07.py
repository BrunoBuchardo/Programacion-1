#Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def numero_primo(numero):
    if numero <= 1:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break 
    return es_primo

numero = input("Ingrese un numero: ")
numero = int(numero)

resultado = numero_primo(numero)
print(resultado)