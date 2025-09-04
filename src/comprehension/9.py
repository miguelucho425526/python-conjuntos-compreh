# Con bucle tradicional
pares_cuadrados = {}
for numero in range(10):
    if numero % 2 == 0:
        pares_cuadrados[numero] = numero ** 2

print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Con dict comprehension
pares_cuadrados = {numero: numero ** 2 for numero in range(10) if numero % 2 == 0}
print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}