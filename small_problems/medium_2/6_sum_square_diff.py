
# First attempt- works but inelegant
def sum_square_difference1(count):
    minuend_list = []
    for num in range(count + 1):
        minuend_list.append(num)
    minuend = (sum(minuend_list))**2
    subtrahend_list = []
    for num in range(count + 1):
        subtrahend_list.append(num**2)
    subtrahend = sum(subtrahend_list)
    return minuend - subtrahend

# Better
def sum_square_difference(count):
    minuend = 0
    subtrahend = 0
    for num in range(count + 1):
        minuend += num
        subtrahend += num**2
    return minuend**2 - subtrahend


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True