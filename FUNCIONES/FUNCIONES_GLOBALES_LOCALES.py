def incrementar_contador():
    global contador
    contador += 1

def decrementar_contador():
    global contador
    contador -= 1

def mostar_contador():
    print(contador)
   

# NO USAR VARIABLES LOCALES
#######################MAIN###################################


incrementar_contador()
mostar_contador()
decrementar_contador()
mostar_contador()