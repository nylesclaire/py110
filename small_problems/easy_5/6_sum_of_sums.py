### Problem
# input: list of numbers
# output: integer
# rules: 
#   - list must contain at least one number

### Algorithm
# 1) loop through the list and generate a sublist representing each 
# leading subsequence. Append this to a master working list.
# 2) For each sublist, find the sum. 
# 3) For all the sublists together, find & return the sum. 


def sum_of_sums(given_list):
    working_list = [given_list[:idx + 1] for idx in range(len(given_list))]
    return sum([sum(sublist) for sublist in working_list])

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True