# Filtrar números mayores que 5
numeros = [2, 8, 1, 6, 3, 9, 4]
mayores_que_cinco = [num for num in numeros if num > 5]
print(mayores_que_cinco)  # [8, 6, 9]

# Filtrar palabras que empiezan con 'a'
frutas = ["manzana", "banana", "arándano", "pera", "aguacate"]
frutas_con_a = [fruta for fruta in frutas if fruta.startswith('a')]
print(frutas_con_a)  # ['arándano', 'aguacate']