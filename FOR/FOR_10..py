#Ingresar un número. Determinar si el número es primo o no.

numero = 5
es_primo = True
for i in range(2, numero):
    if numero % i == 0:                    #BUSQUEDA
        es_primo = False
        break

if numero > 1 and es_primo == True:
    print("Es primo")
else:
    print("No es primo")