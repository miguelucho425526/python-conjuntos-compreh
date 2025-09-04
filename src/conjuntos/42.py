equipo_a = {"Juan", "María", "Carlos", "Ana"}
equipo_b = {"Carlos", "Ana", "Pedro", "Lucía"}

miembros_exclusivos = equipo_a ^ equipo_b
print(miembros_exclusivos)  # {'Juan', 'María', 'Pedro', 'Lucía'}