

### Problem
# Write a function that calculates and returns the index 
# of the first Fibonacci number that has the number of digits 
# specified by the argument. 

# input: integer representing target number of digits
# output: integer representing the index aka our "nth" from prev 
#   Fibonacci problems
# Rules: 
#   -The first Fibonacci number has an index of 1. 
#   -You may assume that the argument is always an integer 
#   greater than or equal to 2

### Data Structures
#   -dictionary table to store fibonacci values
#   -ints obvs.
#   -strings to see digit length. 

### Algorithm
# 1. Initialize an index at 1. 
# 2. create a while True loop:
#   A) feed that index to the fib function and get the result, called 
#   fib_num. (This will also add that pair of values to the memo table.) 
#   B) determine the length of the fib_num. If it is the target number 
#   of digits, return the index number (and of course exit the loop &
#   function)
#   C) increase the index.

import sys
sys.set_int_max_str_digits(50_000)


memo = {}
def fibonacci(n):
    if n <= 2:
        return 1
    
    elif n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def find_fibonacci_index_by_length(target_digits):
    idx = 1
    while True:
        fib_num = fibonacci(idx)
        if len(str(fib_num)) == target_digits:
            return idx            
        idx += 1


### Test cases
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)