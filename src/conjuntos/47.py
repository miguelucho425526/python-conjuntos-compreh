conjunto_a = {1, 2, 3}
conjunto_b = {3, 1, 2}  # Mismo contenido, diferente orden
conjunto_c = {1, 2, 3, 4}

print(conjunto_a == conjunto_b)  # True
print(conjunto_a == conjunto_c)  # False

numeros_pares = {2, 4, 6}
numeros = {1, 2, 3, 4, 5, 6, 7}

print(numeros_pares <= numeros)  # True - todos los elementos están en el segundo conjunto

conjunto_a = {1, 2}
conjunto_b = {1, 2, 3}
conjunto_c = {1, 2}

print(conjunto_a < conjunto_b)  # True - subconjunto propio
print(conjunto_a < conjunto_c)  # False - son iguales