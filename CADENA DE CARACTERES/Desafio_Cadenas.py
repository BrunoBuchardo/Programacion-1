# Muestra de ADN encontrada en la escena del crimen
muestra_crimen = "CGTTTAATG"

# Muestras de ADN de los sospechosos
sospechosos = {
    "Juan Pérez": "CGGGGCTAAAATTTTTTACGATCG",
    "María Rodríguez": "AACGTTTAATGTTCTAAGCTGCG",
    "Carlos Sánchez": "CGGGGCTAAAATTTTTTACGATCG"
}

# Variable para almacenar el nombre del sospechoso
asesino = None

# Comparar la muestra encontrada con las muestras de los sospechosos
for nombre, muestra in sospechosos.items():
    # Verifica si la muestra del crimen está contenida en la muestra del sospechoso
    coincidencia = True
    for base in muestra_crimen:
        if base not in muestra:
            coincidencia = False
            break
    if coincidencia:
        asesino = nombre
        break  # Sale del bucle al encontrar una coincidencia

# Mostrar el resultado
if asesino:
    print(f"El asesino es: {asesino}")
else:
    print("SON TODOS INOCENTES")
