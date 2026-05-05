

table = {}
def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1

    table.update({(nth - 1): fibonacci(nth - 1)})
    table.update({(nth - 2): fibonacci(nth - 2)})

    return table[(nth - 2)] + table[(nth - 1)]


# Test cases
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True