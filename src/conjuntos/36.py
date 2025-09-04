vegetales = {"zanahoria", "pepino", "lechuga"}
frutas = {"manzana", "plátano", "naranja"}
print(vegetales.isdisjoint(frutas))  # True - No tienen elementos en común

numeros_pares = {2, 4, 6, 8}
numeros_primos = {2, 3, 5, 7}
print(numeros_pares.isdisjoint(numeros_primos))  # False - Comparten el 2