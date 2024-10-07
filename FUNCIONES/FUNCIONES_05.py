#Define una función que encuentre el máximo de tres números. 
#La función debe aceptar tres argumentos y devolver el número más grande.

def max_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = input("Ingrese el número 1: ")
num1 = int(num1)
num2 = input("Ingrese el número 2: ")
num2 = int(num2)
num3 = input("Ingrese el número 3: ")
num3 = int(num3)

resultado = max_de_tres(num1, num2, num3)
print("El número mayor es:", resultado)