frutas_locales = {"manzana", "pera", "naranja"}
frutas_importadas = {"piña", "mango", "kiwi"}
# Añade todas las frutas importadas a las locales
frutas_locales.update(frutas_importadas)
print(frutas_locales)  # {'manzana', 'pera', 'naranja', 'piña', 'mango', 'kiwi'}