# Extraer información específica de una lista de diccionarios
estudiantes = [
    {"id": 1, "nombre": "Ana", "nota": 8.5},
    {"id": 2, "nombre": "Carlos", "nota": 7.2},
    {"id": 3, "nombre": "Elena", "nota": 9.3}
]

# Crear un diccionario con id como clave y nombre como valor
id_nombre = {estudiante["id"]: estudiante["nombre"] for estudiante in estudiantes}
print(id_nombre)  # {1: 'Ana', 2: 'Carlos', 3: 'Elena'}

# Crear un diccionario con nombre como clave y nota como valor
nombre_nota = {estudiante["nombre"]: estudiante["nota"] for estudiante in estudiantes}
print(nombre_nota)  # {'Ana': 8.5, 'Carlos': 7.2, 'Elena': 9.3}

# Crear un diccionario con nombres en mayúsculas y notas redondeadas
nombre_nota_formateado = {
    estudiante["nombre"].upper(): round(estudiante["nota"])
    for estudiante in estudiantes
}
print(nombre_nota_formateado)  # {'ANA': 8, 'CARLOS': 7, 'ELENA': 9}