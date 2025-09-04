A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

# Elementos que están en A y B, pero no en C
resultado = (A & B) - C
print(resultado)  # {3, 4}

# Elementos que están en A o en C, pero no en B
resultado2 = (A | C) - B
print(resultado2)  # {1, 2, 7, 8}
# Estas dos expresiones son equivalentes en funcionalidad y rendimiento
