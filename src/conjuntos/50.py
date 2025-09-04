# Preferencias de usuarios sobre géneros de películas
usuario1 = {"acción", "comedia", "ciencia ficción", "aventura"}
usuario2 = {"drama", "comedia", "romance", "documental"}
usuario3 = {"acción", "aventura", "fantasía", "ciencia ficción"}

# Géneros comunes entre usuario1 y usuario3
generos_comunes_1_3 = usuario1 & usuario3
print(f"Géneros comunes entre usuario1 y usuario3: {generos_comunes_1_3}")

# Todos los géneros que le gustan al usuario1 o al usuario2
todos_generos_1_2 = usuario1 | usuario2
print(f"Todos los géneros de usuario1 y usuario2: {todos_generos_1_2}")

# Géneros que le gustan al usuario1 pero no al usuario2
solo_usuario1 = usuario1 - usuario2
print(f"Géneros exclusivos del usuario1: {solo_usuario1}")

# Géneros que le gustan a exactamente uno de usuario2 o usuario3
exclusivos_2_3 = usuario2 ^ usuario3
print(f"Géneros que gustan a usuario2 o usuario3, pero no a ambos: {exclusivos_2_3}")

# Verificar si usuario1 tiene más preferencias que usuario2
tiene_mas_preferencias = len(usuario1) > len(usuario2)
print(f"¿Usuario1 tiene más preferencias que usuario2? {tiene_mas_preferencias}")

# Verificar si todas las preferencias de usuario3 están incluidas en usuario1
todas_incluidas = usuario3 <= usuario1
print(f"¿Todas las preferencias de usuario3 están en usuario1? {todas_incluidas}")