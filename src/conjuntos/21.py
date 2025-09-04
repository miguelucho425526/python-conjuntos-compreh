original = {1, 2, 3}
copia = original.copy()
copia.add(4)
print(original)  # {1, 2, 3} - No se modifica
print(copia)     # {1, 2, 3, 4}