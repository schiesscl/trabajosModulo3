from persona import Persona
from tamagotchi import Tamagotchi

gozarutchi = Tamagotchi(nombre="Gozarutchi", color="Azul")
persona3 = Persona(nombre="Hans", apellido="Schiess", tamagotchi=gozarutchi)

persona3.jugar_con_tamagotchi()
persona3.darle_comida()
persona3.curarlo()
gozarutchi.mostrar_estado()