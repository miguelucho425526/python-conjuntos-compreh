# Eliminar duplicados de una lista
numeros = [1, 2, 2, 3, 4, 3, 5, 5, 1]
numeros_unicos = {numero for numero in numeros}
print(numeros_unicos)  # {1, 2, 3, 4, 5}