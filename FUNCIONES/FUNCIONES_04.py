#Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario.

def verificar_paridad(numero):
    par = numero % 2 == 0
    if par:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
    
    return par

numero = input("Ingrese el número: ")
numero = int(numero)

resultado = verificar_paridad(numero)
print(f"El resultado es: {resultado}")
