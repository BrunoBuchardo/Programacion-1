def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    intentos = 0
    resultado = None  
    
    while intentos < reintentos:
        numero = input(mensaje)
        
        if numero.isdigit():
            numero = int(numero)
            if minimo <= numero <= maximo:
                resultado = numero  
                break  
            else:
                print(mensaje_error)  
        else:
            print(mensaje_error)  
        
        intentos += 1  
    
    return resultado  

numero = get_int("Ingrese un número entre 1 y 10: ", "Error: número inválido", 1, 10, 3)
print(f"Número ingresado: {numero}")