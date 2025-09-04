# Productos vendidos en diferentes tiendas
tienda_centro = {"laptop", "teléfono", "tablet", "auriculares", "cámara"}
tienda_norte = {"laptop", "teléfono", "smartwatch", "altavoces"}
tienda_sur = {"tablet", "auriculares", "smartwatch", "monitor"}

# Productos que se venden en todas las tiendas
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
print(f"Productos vendidos en todas las tiendas: {productos_comunes}")

# Productos únicos de la tienda centro (que no se venden en las otras)
productos_exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
print(f"Productos exclusivos de tienda centro: {productos_exclusivos_centro}")

# Productos que se venden en al menos una tienda
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
print(f"Catálogo completo: {catalogo_completo}")

# Comprobar si todas las tiendas venden productos distintos
son_disjuntos = tienda_centro.isdisjoint(tienda_norte) and tienda_centro.isdisjoint(tienda_sur) and tienda_norte.isdisjoint(tienda_sur)
print(f"¿Todas las tiendas venden productos distintos? {son_disjuntos}")

# Productos que se venden en exactamente una tienda
solo_centro = tienda_centro - (tienda_norte | tienda_sur)
solo_norte = tienda_norte - (tienda_centro | tienda_sur)
solo_sur = tienda_sur - (tienda_centro | tienda_norte)
productos_exclusivos = solo_centro | solo_norte | solo_sur
print(f"Productos que se venden en una sola tienda: {productos_exclusivos}")