# Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.

def suprimir_repetidos_consecutivos(cadena):
    resultado = ""
    longitud = len(cadena)

    for i in range(longitud):
        if i == 0 or cadena[i] != cadena[i - 1]:
            resultado += cadena[i]
    
    return resultado

# Ejemplo de uso
cadena = "Hooola"
resultado = suprimir_repetidos_consecutivos(cadena)
print(resultado)  # Salida: "Hola"
