### Problem
# input: an integer
# output: the next featured number greater than the int
# rules for a featured number:
# - an odd number
# - a multiple of 7
# - all digits occurring only once
# other rules:
# - an error message must display for numbers past 9876543201

### Data Structures
# ints
# convert to string for digit-by-digit comparison


### Algorithm
# -if the number is 9876543201 or greater, return error message
# -start iterating through a range from the given int to the final 
#   featured number (9876543201)
# -for each number in the range, continue if:
#       -the number is not odd
#       -the number is not divisible by 7
#       -when the int is converted to a str, the length of that 
#          string is greater than the length of the string converted
#          to a set (aka, all chars are not unique)
# -if the given number makes it through those checks, return it, 
# it's the featured number!

def next_featured(given_int):
    error = ("There is no possible number that "
         "fulfills those requirements.")
    final_feat_num = 9876543201

    if given_int >= final_feat_num:
        return error
    for num in range((given_int + 1), (final_feat_num + 1)):
        if num % 2 == 0:
            continue
        elif num % 7 != 0:
            continue
        elif ((len(str(num)) > (len(set(str(num)))))):
            continue
        return num



### Test Cases
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True