# Problem
# input: an unordered list
# output: the duplicate value
# rules: 
#   -every value occurs once except 1 value, which occurs twice
#   -input list will always have exactly one duplicate value

# Data structures
# lists. probably a nested loop.

# Algorithm
# 1. Loop through the values in the list, each one momentarily the 
# "being checked" value
#   - Loop through again and compare "being checked value" to every
#   *other* value for equality. 
#   - When an equality statement comes back true, break the top loop
#   and return the value. 

def find_dup(list1):
    for being_checked in list1:
        avoid_idx = list1.index(being_checked)
        for comparison_value in list1[(avoid_idx + 1):]:
            if being_checked == comparison_value:
                return being_checked

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True



# alternatively with a perf method
def find_dup2(list1):
    for being_checked in list1:
        if list1.count(being_checked) > 1:
            return being_checked