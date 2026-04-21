### Problem
# input: this very specific list of integers, 0-19
# output: sorted list of integers

### Data Structures
# lists, ints, strings, possibly a dict

### Algorithm
# 1) create a helper function that will take an integer and convert it to its 
#   string counterpart
# 2) sort the initial list w/ key argument of the helper function. 

INT_NAMES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven", 
    8: "eight", 
    9: "nine", 
    10: "ten", 
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen", 
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen", 
    19: "nineteen",
}

def int_to_name(given_int):
    return INT_NAMES[given_int]

def alphabetic_number_sort(given_list):
    return sorted(given_list, key=int_to_name)


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True