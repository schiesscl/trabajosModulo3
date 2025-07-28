# tarjeta_de_credito.py
"""
Módulo para gestionar tarjetas de crédito.

Este módulo define la clase TarjetaDeCredito, que permite realizar operaciones de compra y pago.
"""
class TarjetaDeCredito:
    """
    Clase que representa una tarjeta de crédito.

    Atributos:
        balance_due (float): El saldo a pagar de la tarjeta.
        credit_limit (float): El límite de crédito de la tarjeta.
        interest_rate (float): La tasa de interés de la tarjeta.

    Métodos:
        purchase(amount): Realiza una compra con la tarjeta de crédito.
        payment(amount): Realiza un pago con la tarjeta de crédito.
        show_card_info(): Muestra la información de la tarjeta.
        charge_interest(): Cobra intereses sobre el saldo a pagar.
    """
    # Método constructor que inicializa los atributos de la tarjeta de crédito
    def __init__(self, balance_due=0, credit_limit=20000, interest_rate=0.015):
        self.balance_due = balance_due  # Atributo que guarda el saldo a pagar de la tarjeta
        self.credit_limit = credit_limit  # Atributo que guarda el límite de crédito de la tarjeta
        self.interest_rate = interest_rate  # Atributo que guarda la tasa de interés de la tarjeta

    # Método para realizar una compra
    def purchase(self, amount):
        """
        Realiza una compra con la tarjeta de crédito.

        Verifica si la compra excede el límite de crédito y actualiza el saldo a pagar.

        Args:
            amount (float): El monto de la compra.
        """
        # Verificamos si la compra excede el límite de crédito
        if self.balance_due + amount > self.credit_limit:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")  # Mensaje si se excede el límite
        else:
            self.balance_due += amount  # Aumentamos el saldo a pagar con el monto de la compra

    # Método para realizar un pago
    def payment(self, amount):
        """
        Realiza un pago con la tarjeta de crédito.

        Disminuye el saldo a pagar con el monto del pago.

        Args:
            amount (float): El monto del pago.
        """
        self.balance_due -= amount  # Disminuimos el saldo a pagar con el monto del pago

    # Método para mostrar la información de la tarjeta
    def show_card_info(self):
        """
        Muestra la información de la tarjeta.

        Imprime el saldo a pagar de la tarjeta.
        """
        print(f"Saldo a Pagar: ${self.balance_due}")  # Imprimimos el saldo a pagar de la tarjeta

    # Método para cobrar intereses sobre el saldo a pagar
    def charge_interest(self):
        """
        Cobra intereses sobre el saldo a pagar.

        Aumenta el saldo a pagar con los intereses calculados según la tasa de interés.
        """
        self.balance_due += self.balance_due * self.interest_rate  # Aumentamos el saldo a pagar con los intereses
