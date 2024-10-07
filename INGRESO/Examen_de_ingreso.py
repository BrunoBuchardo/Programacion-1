import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
"bruno buchardo division A"
#Enunciado:

# #De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
# Nombre
# Tipo (gato ,perro o exotico)
# Peso ( entre 10 y 80)
# Sexo( F o M )
# Edad(mayor a 0)
# Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál fue el sexo mas ingresado (F o M)
# Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
# Informe C- El nombre de la mascota más pesada
# Informe D- El sexo y nombre del gato más viejo
# Informe E- El promedio de edad de todas las mascotas


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_f = 0
        contador_m = 0
        contador_perro = 0
        contador_gato = 0
        contador_exotico = 0
        nombre_mascota_mas_pesada = ""
        peso_mas_pesado = 0
        nombre_gato_mas_viejo = ""
        sexo_gato_mas_viejo = ""
        mayor_edad_gato = 0
        suma_edades_mascotas = 0
        sexo_mas_ingresado = ""
        




        for mascotas in range(5):

            nombre_mascota = prompt("ingreso","ingrese el nombre de la mascota")

            edad = prompt("ingreso","ingrese su edad")
            edad = int(edad)
            while edad < 0:
                edad = prompt("error ingreso"," reingrese su edad")
                edad = int(edad)

            tipo_mascota = prompt("ingreso","ingrese el tipo de mascota")
            while tipo_mascota != "perro" and tipo_mascota != "gato" and tipo_mascota!= "exotico":
                tipo_mascota = prompt("error ingreso"," reingrese el tipo de mascota")

            peso_mascota = prompt("ingreso","ingrese su peso_mascota")
            peso_mascota = int(peso_mascota)
            while peso_mascota < 10 or peso_mascota > 80:
                peso_mascota = prompt("error ingreso"," reingrese su peso_mascota")
                peso_mascota = int(peso_mascota)

            sexo_mascota = prompt("ingreso","ingrese el sexo de su mascota")
            while sexo_mascota != "f" and sexo_mascota != "m": 
                sexo_mascota = prompt("error ingreso"," reingrese el sexo de su mascota")

            # Informe A- Cuál fue el sexo mas ingresado (F o M)
            if sexo_mascota == "f":
                contador_f += 1
            else:
                contador_m += 1

            # Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
            # Informe D- El sexo y nombre del gato más viejo
            match tipo_mascota:
                case "perro":
                    contador_perro += 1
                    suma_edades_mascotas = suma_edades_mascotas + edad
                case "gato":
                    contador_gato += 1
                    suma_edades_mascotas = suma_edades_mascotas + edad
                    if edad > mayor_edad_gato:
                        sexo_gato_mas_viejo = sexo_mascota
                        nombre_gato_mas_viejo = nombre_mascota
                        mayor_edad_gato = edad
                      
                case "exotico":
                    contador_exotico += 1
                    suma_edades_mascotas = suma_edades_mascotas + edad

                

            
            # Informe C- El nombre de la mascota más pesada
            if peso_mascota > peso_mas_pesado:
                peso_mas_pesado = peso_mascota
                nombre_mascota_mas_pesada = nombre_mascota

        if contador_f > contador_m:
            sexo_mas_ingresado = "f"
        else:
            sexo_mas_ingresado = "m"

        # Informe E- El promedio de edad de todas las mascotas
        porcentaje_perro = (contador_perro / 5) * 100
        porcentaje_gato = (contador_gato / 5) * 100
        porcentaje_exotico = (contador_exotico / 5) * 100

        contador_mascotas = contador_exotico + contador_gato + contador_perro
        promedio_edades = suma_edades_mascotas / contador_mascotas

        mensaje = (
        f"Informe A: El sexo más ingresado es {sexo_mas_ingresado}\n"
        f"Informe B: Porcentaje de perros: {porcentaje_perro}%\n"
        f"          Porcentaje de gatos: {porcentaje_gato}%\n"
        f"          Porcentaje de exóticos: {porcentaje_exotico}%\n"
        f"Informe C: La mascota más pesada es {nombre_mascota_mas_pesada}\n"
        f"Informe D: El gato mas viejo se llama: {nombre_gato_mas_viejo} y su sexo es {sexo_gato_mas_viejo}\n"
        f"Informe E: El promedio de edad es de {promedio_edades}")
        print(mensaje)
            

            
       



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
