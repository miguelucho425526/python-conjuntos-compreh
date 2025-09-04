# Supongamos que tenemos datos de ventas por región
ventas_por_region = [
    {"region": "Norte", "producto": "A", "ventas": 100},
    {"region": "Norte", "producto": "B", "ventas": 200},
    {"region": "Sur", "producto": "A", "ventas": 300},
    {"region": "Sur", "producto": "B", "ventas": 150},
    {"region": "Este", "producto": "A", "ventas": 250},
    {"region": "Oeste", "producto": "B", "ventas": 50}
]

# Crear un diccionario con el total de ventas por región
total_por_region = {}
for venta in ventas_por_region:
    region = venta["region"]
    if region in total_por_region:
        total_por_region[region] += venta["ventas"]
    else:
        total_por_region[region] = venta["ventas"]

print(total_por_region)
# {'Norte': 300, 'Sur': 450, 'Este': 250, 'Oeste': 50}

# La misma operación con dict comprehension y defaultdict
from collections import defaultdict

# Primero agrupamos las ventas por región
ventas_agrupadas = defaultdict(int)
for venta in ventas_por_region:
    ventas_agrupadas[venta["region"]] += venta["ventas"]

# Luego convertimos el defaultdict a un diccionario normal
total_por_region = dict(ventas_agrupadas)
print(total_por_region)
# {'Norte': 300, 'Sur': 450, 'Este': 250, 'Oeste': 50}

# O de forma más directa con dict comprehension (para casos simples)
# Nota: esto funciona porque estamos creando un nuevo diccionario, no agrupando
productos_a = {venta["region"]: venta["ventas"] for venta in ventas_por_region if venta["producto"] == "A"}
print(productos_a)
# {'Norte': 100, 'Sur': 300, 'Este': 250}