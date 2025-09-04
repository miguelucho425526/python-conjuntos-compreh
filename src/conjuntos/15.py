frutas = {"manzana", "naranja", "plátano"}
frutas.remove("naranja")
print(frutas)  # {'manzana', 'plátano'}

# Si intentamos eliminar un elemento que no existe:
# frutas.remove("uva")  # KeyError: 'uva'