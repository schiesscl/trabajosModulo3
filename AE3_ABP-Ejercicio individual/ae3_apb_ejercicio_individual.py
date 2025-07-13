# MÓDULO DOCSTRING: Añadido para describir el propósito del script.
"""
Este script calcula el descuento aplicable a una compra basándose en
la cantidad de productos, el historial del cliente, el monto total y si es
un día de promoción. También gestiona la entrada de productos por parte
del usuario.
"""

# FUNCIÓN SIMPLIFICADA: Se eliminaron todas las ramas anidadas y redundantes.
# La lógica ahora es lineal y mucho más fácil de leer y mantener.
# También se corrigió el error de la variable 'times_bought_before'.
def calculate_discount(qty, times_bought, purchase_total, is_sale_day):
    """
    Calcula el porcentaje de descuento a aplicar según varios criterios.

    Parámetros:
        qty (int): Cantidad de productos comprados.
        times_bought (int): Número de compras previas del cliente.
        purchase_total (float): Monto total de la compra.
        is_sale_day (bool): True si es día de promoción especial.

    Retorna:
        int: Porcentaje total de descuento aplicado (máximo 30%).
    """
    discount = 0

    if qty > 10:
        discount += 10
    if times_bought > 5:
        discount += 5
    if purchase_total > 500:
        discount += 7
    if is_sale_day:
        discount += 15

    # Limita el descuento máximo al 30% de una forma más concisa.
    return min(discount, 30)

if __name__ == "__main__":
    times_bought_input = int(input("Ingrese la cantidad de veces que ha comprado antes: "))
    sale_day_input = input("¿Es un día de promoción especial? (sí/no): ").strip().lower() == "s"

    PRODUCT_QTY = 0
    TOTAL_SUM = 0.0

    print("Ingrese el precio de cada producto. Para terminar, ingrese 0.")

    while True:
        price_str = input("Precio del producto (o 0 para terminar): ")
        try:
            price = float(price_str)
            if price == 0:
                break
            if price < 0:
                print("El precio no puede ser negativo.")
                continue

            PRODUCT_QTY += 1
            TOTAL_SUM += price
            
            # Se usan los nombres de variable correctos al llamar a la función
            current_discount = calculate_discount(PRODUCT_QTY, times_bought_input, TOTAL_SUM, sale_day_input)
            discount_dollars = TOTAL_SUM * (current_discount / 100)
            print(f"Total acumulado: ${TOTAL_SUM:.2f}")
            print(f"Descuento acumulado: {current_discount}% (${discount_dollars:.2f})\n")

        except ValueError:
            print("Por favor, ingrese un número válido o 0 para terminar.")

    # Muestra el resumen final de la compra
    final_discount = calculate_discount(PRODUCT_QTY, times_bought_input, TOTAL_SUM, sale_day_input)
    final_discount_amount = TOTAL_SUM * (final_discount / 100)
    final_total = TOTAL_SUM - final_discount_amount

    print("\n--- Resumen Final ---")
    print(f"Total de productos: {PRODUCT_QTY}")
    print(f"Monto total: ${TOTAL_SUM:.2f}")
    print(f"Descuento final aplicado: {final_discount}% (${final_discount_amount:.2f})")
    print(f"Total a pagar: ${final_total:.2f}")