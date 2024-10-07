# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.


def encontar_posicion_maximo(lista: list) -> int | None:
    posicion_maximo = None

    if type(lista) == list:
        posicion_maximo = -1

        if len(lista) > 0:
        
            bandera = False
            maximo = 0

            for i in range(len(lista)):
                if lista[i] > maximo or bandera == False: 
                    maximo = lista[i]
                    posicion_maximo = i
                    bandera = True

    return posicion_maximo

# lista = [-5, -7, -8, -3]
lista = []
posicion = encontar_posicion_maximo(lista)
if posicion == None:
    print("Hubo un error!!!")
elif posicion == -1:
    print("La lista esta vacia")
else:
    print(posicion)