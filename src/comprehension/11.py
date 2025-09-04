# Invertir claves y valores
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}