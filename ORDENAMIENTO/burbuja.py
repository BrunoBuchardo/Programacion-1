lista = [4,9,8,-4,7,3,-6]

for i in range(len(lista)-1): #Verde
    for j in range(i+1, len(lista)): #Naranja
        if lista[i] > lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

print(lista)
