class Personaje:
    def __init__(self, id, nombre, nanotecnologia, vuela, super_poder, poder_pelea):#Constructor
        self.id = id #Asigno al atributo el parametro formal del metodo
        self.nombre_personaje = nombre
        self.usa_nanotecnologia = nanotecnologia
        self.puede_volar = vuela
        self.super_poder = super_poder
        self.poder_pelea = poder_pelea 

    def retornar_descripcion(self)-> str:
        string_formato = f"Hola soy: {self.nombre_personaje}\n"
        if self.usa_nanotecnologia == True:
            string_formato += "Uso nanotecnologia.\n"
        else:
            string_formato += "No uso nanotecnologia.\n"
        string_formato += f"Mi super poder es: {self.super_poder}\n"
        string_formato += f"Mi poder de pelea es: {self.poder_pelea}\n"

        string_formato += "*"*50

        return string_formato
    
    def volar(self, altura, velocidad):
        pass

    def atacar(self, un__personaje: "Personaje"):
        if self.poder_pelea > un__personaje.poder_pelea:
            self.poder_pelea -= un__personaje.poder_pelea
            un__personaje.poder_pelea = 0
            print(f"GANO: {self.nombre_personaje}")
        elif un__personaje.poder_pelea > self.poder_pelea:
            un__personaje.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
            print(f"GANO: {un__personaje.nombre_personaje}")
        else:
            self.poder_pelea -= self.poder_pelea * 10/100
            un__personaje.poder_pelea = self.poder_pelea
            print("EMPATE")