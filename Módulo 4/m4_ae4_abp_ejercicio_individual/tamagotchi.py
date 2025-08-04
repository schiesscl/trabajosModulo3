class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=80):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print("Aumenta su felicidad en 10 y disminuye su salud en 5.")
        self.mostrar_estado()

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print("Aumenta su felicidad en 5 y aumenta su salud en 10.")
        self.mostrar_estado()

    def curar(self):
        self.felicidad -= 5
        self.salud += 20
        print("Disminuye su felicidad en 5 y aumenta su salud en 20.")
        self.mostrar_estado()

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}, Color: {self.color}, Salud: {self.salud}, Felicidad: {self.felicidad}, Energía: {self.energia}")
        
class Gozarutchi(Tamagotchi):
    def jugar(self):
        self.felicidad += 15
        self.salud -= 3
        print("Gozarutchi está jugando y se siente más feliz.")
        self.mostrar_estado()

    def comer(self):
        self.felicidad += 10
        self.salud += 5
        print("Gozarutchi comió y se siente mejor.")
        self.mostrar_estado()

    def curar(self):
        self.felicidad -= 2
        self.salud += 15
        print("Gozarutchi fue curado y se siente más saludable.")
        self.mostrar_estado()