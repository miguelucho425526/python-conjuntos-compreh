# Crear una lista con los cuadrados de los números del 0 al 9
cuadrados = []
for numero in range(10):
    cuadrados.append(numero ** 2)

print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]