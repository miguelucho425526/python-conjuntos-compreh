# Supongamos que tenemos datos de productos comprados por diferentes clientes
compras = [
    {"cliente": "Ana", "producto": "laptop"},
    {"cliente": "Juan", "producto": "teléfono"},
    {"cliente": "Ana", "producto": "auriculares"},
    {"cliente": "Pedro", "producto": "laptop"},
    {"cliente": "Juan", "producto": "auriculares"},
    {"cliente": "Ana", "producto": "teléfono"}
]

# Obtener el conjunto de productos únicos comprados
productos_unicos = {compra["producto"] for compra in compras}
print(productos_unicos)  # {'laptop', 'teléfono', 'auriculares'}

# Obtener el conjunto de clientes que compraron laptops
compradores_laptop = {compra["cliente"] for compra in compras if compra["producto"] == "laptop"}
print(compradores_laptop)  # {'Ana', 'Pedro'}

# Obtener las primeras letras de los nombres de clientes
iniciales_clientes = {cliente["cliente"][0] for cliente in compras}
print(iniciales_clientes)  # {'A', 'J', 'P'}