
def merge_sets1(list_1, list_2):
    return set(list_1 + list_2)

def merge_sets2(list_1, list_2):
    return set(list_1) | set(list_2)

def merge_sets(list_1, list_2):
    return (set(list_1)).union(set(list_2))

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True