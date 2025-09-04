inventario_actual = {"mesa", "silla", "lámpara", "estantería"}
nueva_entrega = {"mesa", "sofá", "alfombra", "estantería"}

# Actualiza el inventario: elimina duplicados y añade nuevos
inventario_actual ^= nueva_entrega
print(inventario_actual)  # {'silla', 'lámpara', 'sofá', 'alfombra'}