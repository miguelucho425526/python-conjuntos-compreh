ciencias = {"física", "química", "biología", "matemáticas"}
artes = {"literatura", "música", "pintura", "matemáticas"}
exclusivos = ciencias.symmetric_difference(artes)
print(exclusivos)  # {'física', 'química', 'biología', 'literatura', 'música', 'pintura'}