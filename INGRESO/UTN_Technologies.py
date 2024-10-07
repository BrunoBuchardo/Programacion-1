'''UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete 
revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
- Inteligencia artificial (IA),
- Realidad virtual/aumentada (RV/RA),
- Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
- nombre del empleado
- edad (no menor a 18)
- género (Masculino - Femenino - Otro)
- tecnologia (IA, RV/RA, IOT)

B) Cargar por terminal 10 encuestas.

C) Determinar:
- Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
- Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
- Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.'''

# Inicializamos variables para los cálculos
count_masc_iot_ia = 0
count_no_ia = 0
mayor_edad_masc = -1
nombre_mayor_edad_masc = ""
tecnologia_mayor_edad_masc = ""

# Realizamos la encuesta a 10 empleados
for i in range(10):
    print(f"\nEncuesta {i+1}:")

    # Nombre del empleado
    nombre_del_empleado = input("Ingrese el nombre del empleado: ")

    # Edad del empleado
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Edad no válida, reingrese su edad (mayor o igual a 18): "))

    # Género del empleado
    genero = input("Ingrese el género (MASCULINO - FEMENINO - OTRO): ")
    while genero != "MASCULINO" and genero != "FEMENINO" and genero != "OTRO":
        genero = input("Género no válido, reingrese el género: ")

    # Tecnología elegida por el empleado
    tecnologia = input("Ingrese la tecnología (IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Tecnología no válida, reingrese la tecnología (IA, RV/RA, IOT): ")

    # Cálculos dentro del bucle
    # 1. Cantidad de empleados masculinos que votaron por IOT o IA y tienen entre 25 y 50 años
    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and 25 <= edad <= 50:
        count_masc_iot_ia += 1

    # 2. Porcentaje de empleados que no votaron por IA bajo ciertas condiciones
    if tecnologia != "IA" and (genero != "Femenino" or 33 <= edad <= 40):
        count_no_ia += 1

    # 3. Empleado masculino con mayor edad
    if genero == "Masculino" and edad > mayor_edad_masc:
        mayor_edad_masc = edad
        nombre_mayor_edad_masc = nombre_del_empleado
        tecnologia_mayor_edad_masc = tecnologia

# Cálculo del porcentaje para la segunda métrica
porcentaje_no_ia = (count_no_ia / 10) * 100

# Resultados
print(f"\nCantidad de empleados masculinos que votaron por IOT o IA y tienen entre 25 y 50 años: {count_masc_iot_ia}")
print(f"Porcentaje de empleados que no votaron por IA bajo las condiciones dadas: {porcentaje_no_ia:.2f}%")
if mayor_edad_masc != -1:
    print(f"Empleado masculino con mayor edad: {nombre_mayor_edad_masc}, Tecnología votada: {tecnologia_mayor_edad_masc}")
else:
    print("No se encontró ningún empleado masculino.")