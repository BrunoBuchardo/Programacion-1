#Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def pedir_cadena():
    cadena = input("Ingrese una cadena: ")
    cadena = str(cadena)
    
    return cadena

cadena = pedir_cadena()
print(cadena)