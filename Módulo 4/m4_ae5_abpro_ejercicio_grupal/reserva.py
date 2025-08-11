from datetime import datetime
from bicicleta import Bicicleta
from excepciones import ReservaInvalidaException

class Reserva:
    def __init__(self, rut_cliente: str, id_reserva: str, bicicleta: Bicicleta, fecha_inicio: datetime, fecha_termino: datetime):
        try:
            if not isinstance(fecha_inicio, datetime) or not isinstance(fecha_termino, datetime):
                raise ReservaInvalidaException("Las fechas deben ser objetos datetime")

            if not isinstance(bicicleta, Bicicleta):
                raise ReservaInvalidaException("El objeto debe ser una instancia de Bicicleta")

            if fecha_inicio >= fecha_termino:
                raise ReservaInvalidaException("La fecha de inicio debe ser anterior a la fecha de término")

            self.rut_cliente = rut_cliente
            self.id_reserva = id_reserva
            self.bicicleta = bicicleta
            self.fecha_inicio = fecha_inicio
            self.fecha_termino = fecha_termino
            self.estado = "activa"

        except ReservaInvalidaException as e:
            print(f"Error al crear reserva: {e}")
            raise

    def reservar(self):
        try:
            if not self.bicicleta.disponibilidad: #Al decir que la bicicleta no esta disponible, forzamos el error personalizado a proposito
                raise ReservaInvalidaException("La bicicleta ya está reservada") #Si ocurre un error como este salta except
            self.bicicleta.disponibilidad = False
            print("Reserva realizada")
        except ReservaInvalidaException as e: #Captura las excepciones del tipo ReservaInvalidaException y guarda el mensaje de error 
            print(f"Error en la reserva: {e}")
        finally:
            print("Fin del proceso de reserva \n")
    
    def total_renta(self):
        try:
            duracion = (self.fecha_termino - self.fecha_inicio).seconds // 3600
            if duracion <= 0:
                duracion = 1
            return int(duracion * self.bicicleta.precio)
        except (TypeError, AttributeError, ValueError) as e:
            print(f"Error al calcular el total: {e}")
            return 0
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            print("Cálculo de renta finalizado")
    def pagar(self):
        try:
            if self.estado != "activa":
                raise ReservaInvalidaException("La reserva no está activa")
            total = self.total_renta()
            if total <= 0:
                raise ValueError("El total a pagar no puede ser cero o negativo")
            print(f"Total a pagar: ${total}")
            self.estado = "finalizada"
            return True
        except (ReservaInvalidaException, ValueError) as e:
            print(f"Error en el pago: {e}")
        except Exception as e:
            print(f"Error inesperado en el pago: {e}")
        finally:
            print("Proceso de pago finalizado \n")

    def cancelar_reserva(self):
        if self.estado != "activa":
            print("No se puede cancelar una reserva que no está activa")
            return False
        self.estado = "cancelada"
        self.bicicleta.disponibilidad = True
        print("Reserva cancelada exitosamente")
        return True