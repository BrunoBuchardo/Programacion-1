# Crear una función llamada ordenar_vector que reciba como parámetro un vector de números enteros
# y lo ordene de forma ascendente.
# La función debe implementar como algoritmo de ordenamiento el método de la burbuja.
# Además, como parámetro opcional debe recibir un booleano (que por default está en False),
# que en caso de ser True ordena el vector en forma descendente.

def ordenar_vector(vector: int, descendente=False):
    numero = len(vector)
    for i in range(numero - 1):
        for j in range(i + 1, numero):
            if (not descendente and vector[i] > vector[j]) or (descendente and vector[i] < vector[j]):
                auxiliar = vector[i]
                vector[i] = vector[j]
                vector[j] = auxiliar
                
    return vector

vector = [10, 5, 15, -20, 22]
print(ordenar_vector(vector))  
print(ordenar_vector(vector, descendente=True)) 