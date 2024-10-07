#Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base = input("Ingrese un numero: ")
base = int(base)
altura = input("Ingrese otro numero: ")
altura = int(altura)    

resultado = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo es: {resultado}")
