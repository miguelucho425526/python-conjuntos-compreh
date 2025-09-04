ingredientes_disponibles = {"harina", "huevos", "azúcar", "leche", "mantequilla"}
ingredientes_usados = {"harina", "huevos", "azúcar"}

ingredientes_restantes = ingredientes_disponibles - ingredientes_usados
print(ingredientes_restantes)  # {'leche', 'mantequilla'}