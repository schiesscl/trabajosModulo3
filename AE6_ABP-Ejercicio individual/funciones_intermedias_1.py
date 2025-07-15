"""
Autor: Hans Schiess
"""
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

matriz[1][0] = 6
print(matriz,end="\n\n")

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes,end="\n\n")

ciudades["México"][2] = "Monterrey"
print(ciudades,end="\n\n")

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas,end="\n\n")

def iterar_diccionario(lista):
    """
    Itera sobre una lista de diccionarios e imprime los valores de 'nombre' y 'país'.

    Parámetros:
        lista (list): Una lista de diccionarios que contienen las claves 'nombre' y 'país'.
    """
    for elemento in lista:
        # Usamos acceso directo a las claves específicas
        print(f"nombre - {elemento['nombre']}, país - {elemento['país']}\n\n")

cantantes_2 = [
    {"nombre": "Ricky Martin", "país": "Puerto Rico"},
    {"nombre": "Chayanne", "país": "Puerto Rico"},
    {"nombre": "José José", "país": "México"},
    {"nombre": "Juan Luis Guerra", "país": "República Dominicana"}
]

iterar_diccionario(cantantes_2)

def iterar_diccionario_2(llave, lista):
    """
    Itera sobre una lista de diccionarios e imprime el valor de la clave especificada.

    Parámetros:
        llave (str): La clave a buscar en los diccionarios.
        lista (list): La lista de diccionarios a iterar.
    """
    for diccionario in lista:
        # Verificamos si la clave existe en el diccionario antes de acceder a ella
        
        if llave in diccionario:
            print(diccionario[llave], end="\n\n")
        else:
            print(f"clave '{llave}' no encontrada.")

iterar_diccionario_2("nombre", cantantes_2)
print()

iterar_diccionario_2("país", cantantes_2)

def imprimir_informacion(diccionario):
    """
    Imprime la información contenida en un diccionario.

    Parámetros:
        diccionario (dict): El diccionario que se desea imprimir.

    Retorna:
        None
    """
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}\n")
        for elemento in lista:
            print(elemento, end="\n\n")

costa_rica = {

    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

imprimir_informacion(costa_rica)
