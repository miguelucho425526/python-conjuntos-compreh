# Definimos dos conjuntos
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Crear un conjunto con los elementos que están en A o B, multiplicados por 2
union_doble = {elemento * 2 for elemento in A.union(B)}
print(union_doble)  # {2, 4, 6, 8, 10, 12, 14, 16}

# Crear un conjunto con los elementos comunes a A y B, elevados al cuadrado
interseccion_cuadrado = {elemento ** 2 for elemento in A.intersection(B)}
print(interseccion_cuadrado)  # {16, 25}