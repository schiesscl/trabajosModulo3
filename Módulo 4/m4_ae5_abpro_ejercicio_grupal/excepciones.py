class ReservaInvalidaException(Exception):  # Crear una nueva clase de error que hereda de exception
    def __init__ (self, mensaje):
        super().__init__(mensaje)