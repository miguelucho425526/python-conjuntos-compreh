# Filtrar elementos de un diccionario por valor
stock = {"manzanas": 10, "plátanos": 3, "naranjas": 25, "peras": 0}
disponibles = {fruta: cantidad for fruta, cantidad in stock.items() if cantidad > 0}
print(disponibles)  # {'manzanas': 10, 'plátanos': 3, 'naranjas': 25}