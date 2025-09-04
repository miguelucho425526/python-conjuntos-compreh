# Ejemplo de sobrescritura de claves
letras = ["a", "b", "a", "c"]
conteo = {letra: letras.count(letra) for letra in letras}
print(conteo)  # {'a': 2, 'b': 1, 'c': 1}

# Para evitar duplicados, puedes usar un conjunto
conteo = {letra: letras.count(letra) for letra in set(letras)}
print(conteo)  # {'a': 2, 'b': 1, 'c': 1}