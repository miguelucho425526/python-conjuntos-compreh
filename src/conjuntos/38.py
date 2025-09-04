# Ejemplo de rendimiento con conjuntos grandes
import time

# Crear dos conjuntos grandes
conjunto_a = set(range(10000))
conjunto_b = set(range(5000, 15000))

# Medir tiempo para operación de intersección
inicio = time.time()
interseccion = conjunto_a.intersection(conjunto_b)
fin = time.time()

print(f"Elementos en la intersección: {len(interseccion)}")
print(f"Tiempo para calcular intersección: {(fin - inicio)*1000:.2f} ms")