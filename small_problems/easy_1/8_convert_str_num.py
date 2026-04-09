## Problem
# input: string filled with digits
# output: integer represented by those digits
# rules:
#   -explicit:
#       -my program cannot use the int() function or other conversion fncs
#       -all input characters will be numeric
#       -"do not worry about leading '+' or '-' signs".... literally
#       whatever that means


## Algorithm
# brainstorm: the chars in the string can be converted to their 
# unicode number and back with "ord" and "chr"... not sure if these
# count as 'standard' conversion functions... but also "chr" still 
# returns a string so. Might be pointless.

# okay having looked at the answer I see they want us to use 
# something like a dict to convert digits to numbers, and then
# multiply by the tens or hundreds or whatever based on what 
# digit it is in the number. Gonna make my own version!

# 1. reverse your string so you can work with the ones digits
# first, tens digit second, and so on.
# 2. Initiate your result value at 0
# 3. Loop through the chars in the string with a range the length
# of the string. 
#   -convert each char to a digit based on the dict
#   -multiply it by 10 to the degree of the idx in the range
#   -add the result to your result value
# 4. Return the result value.

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def digit_char_to_digit(character):
    return DIGITS[character]    

def string_to_integer(given_string):
    working_str = given_string[::-1]
    result_val = 0
    for idx in range(len(working_str)):
        result_val += digit_char_to_digit(working_str[idx]) * (10 ** idx)
    return result_val


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True