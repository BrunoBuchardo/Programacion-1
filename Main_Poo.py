from Class_Personaje import *

un_personaje = Personaje(10, "Ironman", True, True, "Filantropo Y Millonario", 400)
otro_personaje = Personaje(5, "Thor", False, True, "Rayo loco", 600)


print(un_personaje.retornar_descripcion())
print(otro_personaje.retornar_descripcion())

un_personaje.atacar(otro_personaje)