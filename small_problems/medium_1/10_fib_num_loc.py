

### Problem
# Write a function that calculates and returns the index 
# of the first Fibonacci number that has the number of digits 
# specified by the argument. 


table = {}
def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1

    table.update({(nth - 1): fibonacci(nth - 1)})
    table.update({(nth - 2): fibonacci(nth - 2)})

    return table[(nth - 2)] + table[(nth - 1)]

def find_fibonacci_index_by_length(num_of_digits):
    idx = 1
    while len(str(fibonacci(idx))) < num_of_digits:
        idx += 1
    return idx




### Test cases
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10))# == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)