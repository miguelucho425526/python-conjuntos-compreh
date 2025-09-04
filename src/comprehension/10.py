# Convertir valores de un diccionario a mayúsculas
frutas = {"a": "apple", "b": "banana", "c": "cherry"}
frutas_mayusculas = {clave: valor.upper() for clave, valor in frutas.items()}
print(frutas_mayusculas)  # {'a': 'APPLE', 'b': 'BANANA', 'c': 'CHERRY'}