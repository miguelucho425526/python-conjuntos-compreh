# Crear un diccionario con números como claves y sus cuadrados como valores
cuadrados = {}
for numero in range(5):
    cuadrados[numero] = numero ** 2

print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# El mismo resultado con dict comprehension
cuadrados = {numero: numero ** 2 for numero in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}