# Obtener las primeras letras únicas de una lista de palabras
palabras = ["manzana", "banana", "mango", "melón", "mora", "naranja"]
primeras_letras = {palabra[0] for palabra in palabras}
print(primeras_letras)  # {'m', 'b', 'n'}