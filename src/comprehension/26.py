# Si necesitas mantener el orden y eliminar duplicados
numeros = [5, 2, 3, 1, 4, 3]
numeros_unicos_ordenados = list(dict.fromkeys(numeros))  # Truco para mantener orden
print(numeros_unicos_ordenados)  # [5, 2, 3, 1, 4]
# Esto causará un error
# conjunto_invalido = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# Pero puedes usar tuplas (que son inmutables)
conjunto_valido = {(1, 2), (3, 4)}
print(conjunto_valido)  # {(1, 2), (3, 4)}