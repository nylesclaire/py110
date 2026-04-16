## Problem
# input: 2 lists w/ integer elements
# output: 1 new list w/ same number of indices as the provided lists, 
#       each one the product of the provided 2 lists' values at that same index
# rules: all arguments will have the same length.

## Algorithm
# 1) initiate empty result list
# 2) start with the first given list and multiply the first element by the first 
#   element from the second given list. Append to the result list.
# 3) increase the index number and loop, repeating step 2 until end of the list.
# 4) return result list.

def multiply_list(lst1, lst2):
    result_lst = []
    for index in range(len(lst1)):
        result_lst.append(lst1[index] * lst2[index])
    return result_lst

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True