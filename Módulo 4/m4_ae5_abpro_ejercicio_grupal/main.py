"""
M4_AE5_ABPRO-Ejercicio grupal

BIKECITY

Integrantes:
* Jorge Cárdenas
* Hans Schiess
* Catalina Villegas
"""
from datetime import datetime, timedelta
from bicicleta import Bicicleta
from reserva import Reserva
from excepciones import ReservaInvalidaException

# Crear bicicletas
print("=== Creación de Bicicletas ===")
bici1 = Bicicleta("B001", "Oxford", "Urbana", True, 2500)
bici2 = Bicicleta("B002", "Bianchi", "Urbana", True, 2000)
bici3 = Bicicleta("B003", "Treck", "Urbana", True, 3000)

# Mostrar información inicial
print("\n=== Información Inicial de Bicicletas ===")
bici1.mostrar_info()
bici2.mostrar_info()
bici3.mostrar_info()

# Fechas correctas
inicio = datetime.now()
termino = inicio + timedelta(hours=3)

print("\n=== Prueba 1: Reserva válida ===")
reserva1 = Reserva("12.345.678-9", "R001", bici1, inicio, termino)
reserva1.reservar()
reserva1.total_renta()
reserva1.pagar()
reserva1.cancelar_reserva()
    
# === RESERVA 2: MISMA BICI (DEBERÍA FALLAR) ===
print("\n=== Prueba 2: Reserva duplicada (misma bicicleta) ===")
reserva2 = Reserva("22.222.222-2", "R002", bici1, inicio, termino)
reserva2.reservar()

# === RESERVA 3: FECHAS INVÁLIDAS (inicio > término) ===
print("\n=== Prueba 3: Reserva con fechas inválidas ===")
inicio_invalido = datetime.now()
termino_invalido = inicio_invalido - timedelta(hours=2)

try:
    reserva3 = Reserva("33.333.333-3", "R003", bici2, inicio_invalido, termino_invalido)
except ReservaInvalidaException:
    pass # Se imprime el error desde la clase

# === RESERVA 4: OBJETO NO ES BICICLETA ===
print("\n=== Prueba 4: Objeto inválido (no es Bicicleta) ===")
try:
    reserva4 = Reserva("44.444.444-4", "R004", "no_es_bici", inicio, termino)
except ReservaInvalidaException:
    pass # Se imprime el error desde la clase

# === RESERVA 5: CANCELAR Y VOLVER A CANCELAR ===
print("\n=== Prueba 5: Cancelar dos veces ===")
reserva5 = Reserva("55.555.555-5", "R005", bici3, inicio, termino)
reserva5.reservar()
reserva5.cancelar_reserva()
reserva5.cancelar_reserva()  # Esto debe fallar

# === RESERVA 6: Pagar una reserva ya cancelada ===
print("\n=== Prueba 6: Intentar pagar reserva cancelada ===")
reserva5.pagar()  # Esto también debe fallar

# === ESTADO FINAL ===
print("\n=== Estado Final de las Bicicletas ===")
bici1.mostrar_info()
bici2.mostrar_info()
bici3.mostrar_info()