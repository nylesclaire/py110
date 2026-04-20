### Problem
# input: two integers - a count and the start_num
# output: a list w/ count number of items
# rules:
#   - count will always be a nonnegative integer
#   - start_num will always be an (any) integer
#   - if count is zero, it should return an empty list

### Data Structures
# ints, lists. Probably a range

### Algorithm
# 1) initiate an empty list
# 2) for every index in a range from 1 to count, inclusive:
#   - append start_num times index
# 3) return the list


def sequence(count, start_num):
    return [(start_num * idx) for idx in range(1, (count + 1))]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True