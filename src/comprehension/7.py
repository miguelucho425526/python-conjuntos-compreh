# Supongamos que tenemos datos de ventas por producto
ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

# Calcular el valor total de ventas por producto
valor_por_producto = [item["unidades"] * item["precio"] for item in ventas]
print(valor_por_producto)  # [16000, 1250, 450, 2000]

# Encontrar productos con ventas superiores a $1000
productos_alto_valor = [item["producto"] for item in ventas if item["unidades"] * item["precio"] > 1000]
print(productos_alto_valor)  # ['laptop', 'teclado', 'monitor']