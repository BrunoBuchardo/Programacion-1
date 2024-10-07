def get_string(longitud: int) -> str|None:
    
    cadena = input(f"Ingresa una cadena de longitud {longitud}: ")

    if len(cadena) == longitud: 
        return cadena
    else:
        None

resultado = get_string(5)
if resultado:
    print(f"Cadena válida: {resultado}")
else:
    print("La longitud de la cadena es incorrecta.")