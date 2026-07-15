

### Algorithm
# I could do a solution making copies of the o.g. lists and then
# using pop. But let me see if I can do a solution w/o making
# any copies.


# 1. initialize a new empty list.
# 2. initialize an index number at 0.
# 3. loop through o.g. list 1. For each element:

#   - while element is > element at index x in o.g. list 2,
#       -append element from list 2 to new list
#       -advance the index number.
#   - when element is <= element it's compared to:
#       -append element from first list to new list, move forward.
# 4. return the new list


def merge(list1, list2):
    merged = []
    idx = 0
    for element in list1:
        while idx < len(list2) and element > list2[idx]:
            merged.append(list2[idx])
            idx += 1
        merged.append(element)
    while idx < len(list2):
        merged.append(list2[idx])
        idx += 1
    return merged


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)