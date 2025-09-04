# Obtener las vocales únicas en un texto
texto = "python es un lenguaje de programación versátil"
vocales = {letra for letra in texto.lower() if letra in "aeiou"}
print(vocales)  # {'a', 'e', 'i', 'o', 'u'}