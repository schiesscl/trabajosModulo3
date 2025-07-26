"""
Este script define estructuras de datos iniciales para un proyecto.

Autor: Hans Schiess
"""
# 1. Definición de las estructuras de datos iniciales
matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "país": "Puerto Rico"},
    {"nombre": "Chayanne", "país": "Puerto Rico"}
]


ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}


coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

matriz[1][0] = 6
print(matriz,end="\n\n")

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes,end="\n\n")

ciudades["México"][2] = "Monterrey"
print(ciudades,end="\n\n")

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas,end="\n\n")

# 2. Recorrer una lista de diccionarios
for cantante in cantantes:
    print(f"Nombre: {cantante['nombre']}, País: {cantante['país']}",end="\n\n")

# 3. Obtener valores específicos desde una lista de diccionarios
for cantante in cantantes:
    print(cantante["nombre"],end="\n\n")

for cantante in cantantes:
    print(cantante["país"],end="\n\n")

# 4. Recorrer un diccionario con listas como valores
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, lista in costa_rica.items():
    print(f"{len(lista)} elementos en {clave.upper()}:")
    for elemento in lista:
        print(elemento)
