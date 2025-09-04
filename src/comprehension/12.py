# Crear un diccionario a partir de dos listas
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]
persona = {claves[i]: valores[i] for i in range(len(claves))}
print(persona)  # {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}

# Alternativa usando zip (más idiomático en Python)
persona = {clave: valor for clave, valor in zip(claves, valores)}
print(persona)  # {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}