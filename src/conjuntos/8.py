def todos_unicos(items):
    return len(items) == len(set(items))

print(todos_unicos([1, 2, 3, 4]))     # True
print(todos_unicos([1, 2, 3, 1, 4]))  # False