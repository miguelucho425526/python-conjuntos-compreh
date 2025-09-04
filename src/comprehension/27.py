# Verificar pertenencia en un conjunto es más rápido que en una lista
numeros_grandes = range(10000)
conjunto_numeros = {n for n in numeros_grandes}

# Esto es muy eficiente
print(9999 in conjunto_numeros)  # True