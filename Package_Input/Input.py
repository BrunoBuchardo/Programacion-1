from Package_Input.Validate import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    intentos = 0
    resultado = None
    
    while intentos < reintentos:
        numero = input(mensaje)
        
        
        if validate_length(numero, 1, 10):
            if numero[0] == '-' and len(numero) > 1 and numero[1:].isdigit():
                numero = int(numero)
            elif numero.isdigit():
                numero = int(numero)
            else:
                numero = None  
            
            
            if numero is not None and validate_number(numero) and minimo <= numero <= maximo:  
                resultado = numero
                break
            else:  
                print(mensaje_error)
        else:
            print(mensaje_error)
        
        intentos += 1
    
    return resultado


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    intentos = 0
    resultado = None
    
    while intentos < reintentos:
        numero = input(mensaje)
        numero = float(numero)
        if validate_number(numero) and minimo <= numero <= maximo:  
            resultado = numero
            break
        else:
            print(mensaje_error)
        
        intentos += 1
    
    return resultado

def get_string(longitud: int) -> str|None:
    cadena = input(f"Ingresa una cadena de longitud {longitud}: ")

    if validate_length(cadena, longitud, longitud):
        result = cadena
    else:
        result = None
    
    return result
