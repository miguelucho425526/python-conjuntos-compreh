# Eliminar duplicados de una lista manteniendo el orden original
def eliminar_duplicados(secuencia):
    return list(dict.fromkeys(secuencia))

lista_con_duplicados = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(eliminar_duplicados(lista_con_duplicados))  # [3, 1, 4, 5, 9, 2, 6]