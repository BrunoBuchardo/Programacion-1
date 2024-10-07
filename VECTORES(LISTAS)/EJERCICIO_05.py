# Escribir una función que reciba como parámetros una lista de enteros 
# y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def encontrar_posiciones_maximo(lista: list) -> list | None:
    posiciones_maximo = []
    retorno = None  # Variable para el retorno

    if type(lista) == list:
        if len(lista) > 0:
            maximo = lista[0]
            posiciones_maximo = [0] * len(lista)  # Crear lista del mismo tamaño que la original
            contador = 0  # Contador para manejar las posiciones

            # Encontrar el valor máximo en la lista
            for numero in lista:
                if numero > maximo:
                    maximo = numero

            # Guardar todas las posiciones donde se encuentra el valor máximo
            for i in range(len(lista)):
                if lista[i] == maximo:
                    posiciones_maximo[contador] = i
                    contador += 1

            retorno = posiciones_maximo[:contador]  # Ajustar el tamaño de la lista según el contador
        else:
            retorno = -1  # La lista está vacía
    else:
        retorno = None  # Tipo de dato incorrecto

    return retorno


lista = [3, 5, 2, 5, 1, 5]
posiciones = encontrar_posiciones_maximo(lista)
if posiciones == None:
    print("Hubo un error!!!")
elif posiciones == -1:
    print("La lista está vacía")
else:
    print(f"El valor máximo se encuentra en las posiciones: {posiciones}")

