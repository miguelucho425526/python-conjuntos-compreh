inventario = {"laptop", "teléfono", "tablet", "auriculares"}
vendidos = {"laptop", "auriculares"}
disponibles = inventario.difference(vendidos)
print(disponibles)  # {'teléfono', 'tablet'}