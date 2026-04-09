# Problem
# input: two lists
# output: a set containing the union of values from the 2 lists
# rules:
#   -arguments will always be lists

def union(list1, list2):
    return set(list1) | set(list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True