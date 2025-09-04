lenguajes = {"Python", "Java", "C++"}
nuevos_lenguajes = {"Go", "Rust", "TypeScript"}

# Equivalente a: lenguajes = lenguajes | nuevos_lenguajes
lenguajes |= nuevos_lenguajes
print(lenguajes)  # {'Python', 'Java', 'C++', 'Go', 'Rust', 'TypeScript'}