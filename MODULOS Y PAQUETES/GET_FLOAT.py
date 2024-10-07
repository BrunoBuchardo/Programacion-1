def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    intentos = 0
    resultado = None  
    
    while intentos < reintentos:
        numero = input(mensaje)
        
        if numero:
            numero = float(numero)
            if minimo <= numero <= maximo:
                resultado = numero  
                break  
            else:
                print(mensaje_error)  
        else:
            print(mensaje_error)  
        
        intentos += 1  
    
    return resultado  

numero = get_float("Ingrese un número entre 0.5 y 1.5: ", "Error: número inválido", 0.5, 1.5, 3)
print(f"Número ingresado: {numero}")