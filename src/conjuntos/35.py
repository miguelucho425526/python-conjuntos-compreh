grupo1 = {"Ana", "Carlos", "David"}
grupo2 = {"Carlos", "Elena", "Fernando"}
# Actualiza grupo1 para contener solo personas que están en un grupo pero no en ambos
grupo1.symmetric_difference_update(grupo2)
print(grupo1)  # {'Ana', 'David', 'Elena', 'Fernando'}