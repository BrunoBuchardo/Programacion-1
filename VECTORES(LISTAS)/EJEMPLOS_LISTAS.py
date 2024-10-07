# lista = [5, 7, -6, 1, 4, -9]
# print(id(lista))
# print(id(lista[2]))
# print(id(lista[5]))
def cargar_lista(lista: list) -> None:
    for i in range(len(lista)):
        lista[i] = int(input("Ingrese un numero:"))

def mostrar_lista(lista: list) ->  None:
    for i in range(len(lista)):
        print(lista[i])

def contar_negativos(lista: list) -> int:
    contador_negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador_negativos += 1
    return contador_negativos

def buscar_positivos(lista: list) -> bool:
    encontro = False
    for i in range(len(lista)):
        if lista[i] > 0:
            encontro = True
            break

    return encontro

def crear_lista(limite: int, valor_inicial: any) -> list:
    lista = [valor_inicial] * limite
    return lista

######################MAIN###############################################
lista = crear_lista(10, 0) #construir lista


cargar_lista(lista)
print("Listado:")
mostrar_lista(lista)

cantidad = contar_negativos(list)
print(f"Se ingresaron {cantidad} numeros negativos")

encontro_positivos = buscar_positivos(list)

if encontro_positivos == True:
    print("Se encontro por lo menos un positivo")
else:
    print("No se encontro ningun numero positivo")

    
# print("Numero impares: ")
# for i in range(len(lista)):
#     if not (lista[i] % 2 == 0):
#         print(lista[i])

# print()
# contador_negativos = 0
# for i in range(len(lista)):
#     if lista[i] < 0:
#         contador_negativos += 1

# print(f"Se ingresaron {contador_negativos} numeros negativos")

# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista[i]

# print(f"La suma es: {acumulador}")


# encontro = False
# for i in range(len(lista)):
#     if lista[i] > 0:
#         encontro = True
#         break

# if encontro == True:
#     print("Se encontro por lo menos un positivo")
# else:
#     print("No se encontro ningun numero positivo")