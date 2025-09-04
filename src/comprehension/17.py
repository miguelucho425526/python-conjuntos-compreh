# Crear un conjunto con los cuadrados de los números del 0 al 4
cuadrados = set()
for numero in range(5):
    cuadrados.add(numero ** 2)

print(cuadrados)  # {0, 1, 4, 9, 16}
# El mismo resultado con set comprehension
cuadrados = {numero ** 2 for numero in range(5)}
print(cuadrados)  # {0, 1, 4, 9, 16}