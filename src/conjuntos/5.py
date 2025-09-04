# Esto funciona (todos los elementos son inmutables)
conjunto_valido = {1, "hola", (1, 2)}

# Esto produce un error (las listas son mutables)
# conjunto_invalido = {1, [2, 3]}  # TypeError: unhashable type: 'list'