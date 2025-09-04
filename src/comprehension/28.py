# Crear un diccionario donde las claves son palabras únicas y los valores son sus longitudes
texto = "el perro corre tras el gato y el gato corre tras el ratón"
palabras = texto.split()
diccionario_longitudes = {palabra: len(palabra) for palabra in {p for p in palabras}}
print(diccionario_longitudes)
# {'perro': 5, 'el': 2, 'corre': 5, 'tras': 4, 'gato': 4, 'y': 1, 'ratón': 5}