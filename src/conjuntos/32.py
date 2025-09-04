usuarios_activos = {"user1", "user2", "user3", "user4"}
usuarios_premium = {"user2", "user4", "user5"}
# Actualiza usuarios_activos para contener solo usuarios activos que también son premium
usuarios_activos.intersection_update(usuarios_premium)
print(usuarios_activos)  # {'user2', 'user4'}