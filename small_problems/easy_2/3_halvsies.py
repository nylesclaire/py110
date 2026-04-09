# Problem
# input: a list
# output: a list containing two lists
# rules: 
#   -if orig list has odd number, put middle element in the 1st
#   half list

# Data structures
# lists! 

# Algorithm
# 1. Determine if the length of the original list is odd or even. 
# 2. Take the length of the original list and floor divide by 2. 
#   -if even, save that number as "half idx"
#   -if odd, add 1 and save that number as "half idx"
# 3. Return two new lists w/ slicing around the "half idx"


def halvsies(orig_list):
    half_idx = len(orig_list) // 2
    if len(orig_list) % 2 != 0:
        half_idx += 1
    return [orig_list[:(half_idx)], orig_list[half_idx:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])