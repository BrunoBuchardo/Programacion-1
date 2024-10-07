# Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

def contar_subcadena(cadena, subcadena):
    contador = 0
    longitud_cadena = len(cadena)
    longitud_subcadena = len(subcadena)
    
    for i in range(longitud_cadena - longitud_subcadena + 1):
        if cadena[i:i + longitud_subcadena] == subcadena:
            contador += 1
    
    return contador

# Ejemplo de uso
resultado = contar_subcadena("El pan del panadero", "pan")
print(resultado)  # Salida: 2
