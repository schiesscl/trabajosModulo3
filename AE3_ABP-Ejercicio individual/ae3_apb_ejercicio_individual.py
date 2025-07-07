def calculate_discount(product_qty, times_bought_before, total_sum, sale_day):
    discount = 0  # Inicializa el descuento en 0

    # Si se compran más de 10 productos
    if product_qty > 10:
        discount += 10
        # Si además es cliente frecuente
        if times_bought_before > 5:
            discount += 5
            # Si además el total supera $500
            if total_sum > 500:
                discount += 7
                # Si además es día de promoción especial
                if sale_day:
                    discount += 15
            elif sale_day:
                discount += 15
        elif total_sum > 500:
            discount += 7
            if sale_day:
                discount += 15
        elif sale_day:
            discount += 15
    # Si no compró más de 10 productos, pero es cliente frecuente
    elif times_bought_before > 5:
        discount += 5
        if total_sum > 500:
            discount += 7
            if sale_day:
                discount += 15
        elif sale_day:
            discount += 15
    # Si no es cliente frecuente ni compró más de 10 productos, pero el total supera $500
    elif total_sum > 500:
        discount += 7
        if sale_day:
            discount += 15
    # Solo día de promoción especial
    elif sale_day:
        discount += 15

    # Limita el descuento máximo al 30%
    if discount > 30:
        discount = 30

    # Si ninguna condición se cumple, el descuento será 0%
    # (Esto ya está cubierto porque discount inicia en 0 y solo se suma si alguna condición se cumple)

    return discount  # Devuelve el porcentaje total de descuento

if __name__ == "__main__":
    # Solicita al usuario la cantidad de compras previas
    times_bought_before = int(input("Ingrese la cantidad de veces que ha comprado antes: "))
    # Pregunta si es día de promoción especial (sí/no)
    sale_day = input("¿Es un día de promoción especial? (sí/no): ").strip().lower() == "s"

    product_qty = 0  # Contador de productos
    total_sum = 0.0  # Acumulador del monto total

    print("Ingrese el precio de cada producto. Para terminar, ingrese 0.")

    # Bucle para ingresar los precios de los productos
    while True:
        price = input("Precio del producto (o 0 para terminar): ")
        try:
            price = float(price)  # Convierte el input a número decimal
            if price == 0:
                break  # Si el usuario ingresa 0, termina el ingreso de productos
            if price < 0:
                print("El precio no puede ser negativo.")
                continue  # Si el precio es negativo, pide el dato de nuevo
            product_qty += 1  # Suma uno al contador de productos
            total_sum += price  # Suma el precio al total acumulado
            # Calcula el descuento actual según los criterios
            discount = calculate_discount(product_qty, times_bought_before, total_sum, sale_day)
            discount_dollars = total_sum * (discount / 100)  # Calcula el descuento en dólares
            print(f"Total acumulado: ${total_sum:.2f}")
            print(f"Descuento acumulado: {discount}% (${discount_dollars:.2f})\n")
        except ValueError:
            print("Por favor, ingrese un número válido o 0 para terminar.")

    # Muestra el resumen final de la compra
    print(f"\nTotal final: ${total_sum:.2f}")
    print(f"Descuento final aplicado: {discount}% (${total_sum * (discount / 100):.2f})")
    print(f"Total a pagar: ${total_sum - (total_sum * (discount / 100)):.2f}")

# Notas sobre condiciones de borde:
# - Si el usuario ingresa exactamente 10 productos, NO recibe el 10% de descuento (debe ser más de 10).
# - Si el total es exactamente $500, NO recibe el 7% de descuento (debe ser más de $500).
# - Si el usuario ingresa exactamente 5 compras previas, NO recibe el 5% de descuento (debe ser más de 5).
# - Si ninguna condición se cumple, el descuento será 0% (esto es el comportamiento por defecto).