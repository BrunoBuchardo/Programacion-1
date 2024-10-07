#Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar validaciones.

def pedir_numero_int(mensaje, minimo, maximo, mensaje_error):
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(mensaje_error)
        numero = int(numero)

    return numero
#########################################################################
def pedir_numero_float(mensaje, minimo, maximo, mensaje_error):
    numero = input(mensaje)
    numero = float(numero)
    while numero < minimo or numero > maximo:
        numero = input(mensaje_error)
        numero = float(numero)

    return numero
###########################################################################
def pedir_cadena(mensaje, longitud_min, longitud_max, mensaje_error):
    cadena = input(mensaje)
    cadena = str(cadena)
    while len(cadena) < longitud_min or len(cadena) > longitud_max:
        cadena = input(mensaje_error)
        cadena = str(cadena)

    return cadena
############################MAIN#############################################

min_legajo = 1
max_legajo = 1000

legajo = pedir_numero_int("Ingrese un legajo: ",min_legajo, max_legajo,
f"Error. Reingrese el legajo entre: {min_legajo} y {max_legajo}: ")

print(legajo)
                                                                                     
nota = pedir_numero_int("Ingrese una nota: ", 1, 10, "Nota invalida: ")

print(nota)
#######################################################################################

min_altura = 1.50
max_altura = 1.95

altura = pedir_numero_float("Ingrese la altura de una pared: ",min_altura, max_altura,
f"Error. Reingrese la altura entre: {min_altura} y {max_altura}: ")

print(altura)

#########################################################################################
