### Problem
# input: number representing index in Fibonacci sequence
# output: number at that index in the sequence.
# rules:
#  F(1) = 1     
#  F(2) = 1
#  F(n) = F(n - 1) + F(n - 2)    (where n > 2)


### Algorithm
# 1) initiate list w/ 0 (idx 0), 1 (idx 1), 1 (idx 2) to represent 
# the first few numbers in the sequence
# 2) In each loop:
#   -n is our increasing index until we reach the given index
#   -we append the number we get to the list


def fibonacci1(target_idx):
    fib = [0, 1, 1]
    if target_idx < 3:
        return fib[target_idx]
    idx = 3
    while idx <= target_idx:
        current_answer = fib[(idx - 1)] + fib[(idx - 2)]
        fib.append(current_answer)
        idx += 1
    return current_answer

# duh get that while loop outta there
def fibonacci(target_idx):
    fib = [0, 1, 1]
    if target_idx < 3:
        return fib[target_idx]
    for idx in range(3, (target_idx +1)):
        current_answer = fib[(idx - 1)] + fib[(idx - 2)]
        fib.append(current_answer)
    return current_answer



### Test cases
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True