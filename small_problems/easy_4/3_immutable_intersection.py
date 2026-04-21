def intersection(list_1, list_2):
    big_set = set(list_1) & set(list_2)
    return frozenset(big_set)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True