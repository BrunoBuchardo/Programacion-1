#Minificacion: N0
#Depuracion y Modificacion: +-
#Reutibilizacion: NO
#Independencia: NO
def sumar_1():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es {suma}")
########################################################################
#Minificacion: +-
#Depuracion y Modificacion: +-
#Reutibilizacion: +-
#Independencia: +-
def sumar_2(un_numero, otro_numero):
    suma = un_numero + otro_numero
    print(f"La suma es {suma}")
##########################################################################
#Minificacion: +-
#Depuracion y Modificacion: +-
#Reutibilizacion: +-
#Independencia: +-
def sumar_3():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma
###########################################################################
#Minificacion: SI
#Depuracion y Modificacion: SI
#Reutibilizacion: SI
#Independencia: SI
def sumar_4(un_numero, otro_numero):
    suma = un_numero + otro_numero
    return suma
######################################MAIN################################
# print("Inicio del programa")
# sumar_1()                                       1 (4TO PUESTO)
# print("Fin del programa")

############################################################################
#sumar_2(40,99)                                   2 (2DO PUESTO)

###########################################################################
# resultado = sumar_3()
# if resultado > 5:                               3 (3ER PUESTO)
    # print("Hola")
# print(f"El resultado es {resultado}")

###########################################################################
# un_numero = input("Ingrese un numero: ")
# un_numero = int(un_numero)
# otro_numero = input("Ingrese otro numero: ")
# otro_numero = int(otro_numero)                  4 (1ER PUESTO)

# resultado = sumar_4(un_numero, otro_numero)

# print(f"El resultado es: {resultado}")
##############################################################################
