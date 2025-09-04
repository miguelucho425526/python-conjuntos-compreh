# Obtener las longitudes únicas de palabras en una lista
palabras = ["casa", "perro", "sol", "luna", "mar", "montaña"]
longitudes_unicas = {len(palabra) for palabra in palabras}
print(longitudes_unicas)  # {3, 4, 5, 7}