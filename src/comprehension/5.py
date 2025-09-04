# Convertir una lista de palabras a mayúsculas
palabras = ["python", "es", "genial"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['PYTHON', 'ES', 'GENIAL']

# Extraer la primera letra de cada palabra
primeras_letras = [palabra[0] for palabra in palabras]
print(primeras_letras)  # ['p', 'e', 'g']