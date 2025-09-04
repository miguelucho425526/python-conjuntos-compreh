tareas_pendientes = {"informe", "reunión", "correos", "presentación"}
tareas_completadas = {"informe", "correos"}

# Elimina las tareas completadas
tareas_pendientes -= tareas_completadas
print(tareas_pendientes)  # {'reunión', 'presentación'}