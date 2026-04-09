# Problem
# input: 2 lists
# output: new list w/ all elements from both lists, taken in alternation
# rules:
#   -both lists are non-empty
#   -the lists have the same number of elements

# data structures:
# lists.

# Algorithm:
# 1. Initiate an empty list for the result
# 2. determine length of one list (which'll be the same for both)
# 3. Loop through a range that's the length plus 1, this'll be your idx
#   -append list1's element at idx
#   -append list2's element at idx
# 4. When loop concludes, return the result list

def interleave(lst1, lst2):
    result_lst = []
    for idx in range(len(lst1)):
        result_lst.append(list1[idx])
        result_lst.append(list2[idx])
    return result_lst

#alternative solution using zip()
def interleave2(lst1, lst2):
    big_list = list(zip(lst1, lst2))
    result_lst = []
    for idx in range(len(big_list)):
        result_lst.extend(big_list[idx])
    return result_lst

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2)) #== expected)      # True