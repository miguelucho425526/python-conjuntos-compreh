# Con bucle tradicional
pares_cuadrados = set()
for numero in range(10):
    if numero % 2 == 0:
        pares_cuadrados.add(numero ** 2)

print(pares_cuadrados)  # {0, 4, 16, 36, 64}

# Con set comprehension
pares_cuadrados = {numero ** 2 for numero in range(10) if numero % 2 == 0}
print(pares_cuadrados)  # {0, 4, 16, 36, 64}