class Bicicleta:
    def __init__(self, id, marca, modelo, disponibilidad, precio):
        try:
            if not isinstance(precio, (int, float)) or precio <= 0:
                raise ValueError("El precio debe ser un número positivo")
            if not isinstance(id, str):
                raise TypeError("El ID debe ser una cadena de texto")
            
            self.id = id
            self.marca = marca
            self.modelo = modelo
            self.disponibilidad = disponibilidad
            self.precio = precio
        except (ValueError, TypeError) as e:
            print(f"Error al crear bicicleta: {e}")
            raise

    def mostrar_info(self):
        try:
            print(f"Bicicleta ID: {self.id}")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}")
            print(f"Precio por hora: ${self.precio:.2f}")
            print("-" * 30)
        except (AttributeError, ValueError, TypeError) as e:
            print(f"Error al mostrar información: {e}")

    def registrar(self):
        try:
            return (f"{self.id},{self.marca},{self.modelo},{self.disponibilidad},{self.precio}")
        except (AttributeError, ValueError, TypeError) as e:
            print(f"Error al registrar bicicleta: {e}")
            return None