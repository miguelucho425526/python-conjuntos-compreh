# Con bucle tradicional
pares = []
for numero in range(10):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)  # [0, 2, 4, 6, 8]

# Con list comprehension
pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]