# main.py
"""
Módulo principal del programa.

Este módulo crea instancias de la clase TarjetaDeCredito y realiza operaciones con ellas.
"""
from tarjeta_de_credito import TarjetaDeCredito  # Importamos la clase CreditCard desde el archivo tarjeta_credito.py

# Creamos instancias de CreditCard
card1 = TarjetaDeCredito()  # Primera tarjeta de crédito
card2 = TarjetaDeCredito()  # Segunda tarjeta de crédito
card3 = TarjetaDeCredito()  # Tercera tarjeta de crédito

# Operaciones para la primera tarjeta
card1.purchase(100)  # Realizamos una compra de $100
card1.purchase(50)   # Realizamos otra compra de $50
card1.payment(30)     # Realizamos un pago de $30
card1.charge_interest()  # Cobrar intereses sobre el saldo a pagar
card1.show_card_info()  # Mostramos la información de la tarjeta

# Operaciones para la segunda tarjeta
card2.purchase(200)  # Realizamos una compra de $200
card2.purchase(150)  # Realizamos otra compra de $150
card2.purchase(100)  # Realizamos otra compra de $100
card2.payment(50)     # Realizamos un pago de $50
card2.payment(100)    # Realizamos otro pago de $100
card2.charge_interest()  # Cobrar intereses sobre el saldo a pagar
card2.show_card_info()  # Mostramos la información de la tarjeta

# Operaciones para la tercera tarjeta
card3.purchase(5000)  # Realizamos una compra de $5000
card3.purchase(8000)  # Realizamos otra compra de $8000
card3.purchase(7000)  # Realizamos otra compra de $7000
card3.purchase(3000)  # Realizamos otra compra de $3000
card3.purchase(2000)  # Intentamos realizar otra compra de $2000 (esto debería exceder el límite de crédito)
card3.show_card_info()  # Mostramos la información de la tarjeta
