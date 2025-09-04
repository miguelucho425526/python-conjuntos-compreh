grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Elena", "Fernando", "Gabriela", "Carlos"}

# Personas que están solo en el grupo A
solo_en_a = grupo_a - grupo_b
print(solo_en_a)  # {'Ana', 'David'}