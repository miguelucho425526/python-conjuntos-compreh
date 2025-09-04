# Registro inicial de asistentes
asistentes_dia1 = {"Ana", "Carlos", "Elena", "David", "Beatriz"}
asistentes_dia2 = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Añadir nuevos asistentes al día 1
asistentes_dia1.add("Héctor")
print(f"Asistentes día 1: {asistentes_dia1}")

# Personas que asistieron ambos días
asistentes_ambos_dias = asistentes_dia1.intersection(asistentes_dia2)
print(f"Asistieron ambos días: {asistentes_ambos_dias}")

# Eliminar a alguien que canceló su asistencia
asistentes_dia1.discard("David")
print(f"Asistentes día 1 actualizado: {asistentes_dia1}")

# Comprobar si todos los del día 2 asistieron también el día 1
todos_repiten = asistentes_dia2.issubset(asistentes_dia1)
print(f"¿Todos los del día 2 asistieron el día 1?: {todos_repiten}")

# Total de asistentes únicos en ambos días
total_asistentes = len(asistentes_dia1.union(asistentes_dia2))
print(f"Total de asistentes únicos: {total_asistentes}")