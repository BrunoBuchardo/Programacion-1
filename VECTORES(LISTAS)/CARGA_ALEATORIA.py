def crear_lista(limite: int, valor_inicial: any) -> list:
    lista = [valor_inicial] * limite
    return lista

def mostrar_lista(lista: list) ->  None:
    for i in range(len(lista)):
        if lista[i] != None:
            print(f"Elementos: {i+1} -> {lista[i]}")

def acumular(lista):
    acumular = 0
    for i in range(len(lista)):
        if lista[i] != None:
            acumular += lista[i]
    return acumular



seguir = "si"
lista = crear_lista(limite = 10, valor_inicial = None)


while seguir == "si":
    numero = int(input("Ingrese un numero: "))
    #validar
    posicion = int(input("Ingrese una posicion 1 al 10: "))

    lista[posicion-1] = numero


    seguir = input("Desea ingresar otro: ")


total = acumular(lista)
print(total)
mostrar_lista(lista)