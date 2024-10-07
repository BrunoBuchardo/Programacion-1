# Crear una función que reciba como parámetro un vector de números enteros. 
# La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

def ordenar_vector(vector: int):
    # Se utiliza un solo bucle para mover y ordenar al mismo tiempo
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            # Si ambos son negativos, ordenarlos en forma decreciente
            if vector[i] < 0 and vector[j] < 0 and vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
            # Si ambos son positivos, ordenarlos en forma creciente
            elif vector[i] >= 0 and vector[j] >= 0 and vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
            # Mover los negativos a la izquierda
            elif vector[i] >= 0 and vector[j] < 0:
                vector[i], vector[j] = vector[j], vector[i]

    
    print(vector)



mi_vector = [7, -2, 5, -7, 0, -4, 22]
ordenar_vector(mi_vector)





