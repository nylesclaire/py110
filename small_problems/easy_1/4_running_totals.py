## Problem
# input: list of integers
# output: list of integers
# rules:
#   explicit:
#       -the returned list must have the same number of elements as 
#       the original list
#       -each element's value must be the running total of elements at
#       that index in the orginal list. 
#   implicit: 
#       -an input empty list should return an empty list. 
# question: Should the orginal list be mutated, or return a new list?
#   -Not clear from problem or test cases; could try to solve both ways

## Data structures
# working with lists and with integers

## Algorithm
# 1. Initiate an empty list that will hold your result
# 2. Initiate a sum value of 0
# 3. Iterate through the given list. On each iteration:
#   -add each element to the sum value
#   -take the sum value and append it to the result list
# 4. Return the result list

def running_total(given_list):
    result_list = []
    sum_so_far = 0
    for item in given_list:
        sum_so_far += item
        result_list.append(sum_so_far)
    return result_list

# Test Cases
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True