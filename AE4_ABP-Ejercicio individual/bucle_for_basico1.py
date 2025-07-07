#Hans Schiess

# 1. Básico
print("1. Básico")
for i in range(101):
    print(i)
# 2. Múltiplos de 2
print("\n2. Múltiples de 2")
for numero in range(2, 501, 2):
    print(numero)
# 3. "Contando Vanilla Ice"
print("\n3. Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
# 4. Wow, Número gigante a la vista
print("\n4. Wow, Número gigante a la vista")
suma_total = sum(range(0, 500001, 2))
print(suma_total)
# 5. Regrésame al 2
print("\n5. Regrésame al 2")
for i in range(2024, 1, -3):
    print(i)
# 6. Contador dinámico
print("\n6. Contador dinámico")
# Variables personalizables
numInicial = 3
numFinal = 10
multiplo = 2

# Bucle para recorrer desde numInicial hasta numFinal
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)