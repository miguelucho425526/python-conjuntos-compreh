productos_tienda_a = {"laptop", "teléfono", "tablet", "auriculares"}
productos_oferta = {"laptop", "auriculares", "cámara"}

# Mantiene solo los productos que están en oferta
productos_tienda_a &= productos_oferta
print(productos_tienda_a)  # {'laptop', 'auriculares'}