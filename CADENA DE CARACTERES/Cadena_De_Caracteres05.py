# Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

def suprimir_vocales(cadena):
    vocales = "aeiouAEIOU"
    resultado = ""

    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

# Ejemplo de uso
cadena = "Hola"
resultado = suprimir_vocales(cadena)
print(resultado)  # Salida: "Hl"
