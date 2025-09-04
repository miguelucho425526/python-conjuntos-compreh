# Esto NO crea un conjunto vacío, sino un diccionario vacío
no_es_conjunto = {}
print(type(no_es_conjunto))  # <class 'dict'>

# Forma correcta de crear un conjunto vacío
conjunto_vacio = set()
print(type(conjunto_vacio))  # <class 'set'>