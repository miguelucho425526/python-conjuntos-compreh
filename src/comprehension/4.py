# Extraer nombres de una lista de diccionarios
usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Elena", "edad": 23}
]

nombres = [usuario["nombre"] for usuario in usuarios]
print(nombres)  # ['Ana', 'Carlos', 'Elena']