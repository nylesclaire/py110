# EXAMPLE OF RECURSION
def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n - 1)

### REMINDER OF THE GENERAL FORMULA
# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1

    return fibonacci(nth - 1) + fibonacci(nth - 2)



# Test cases
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True