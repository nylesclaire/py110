## Problem:
# input: string
# output: bool
# rules:
#   -explicit:
#       -case-insensitive.
#       -ignore all non-alphanumeric characters
#   -implicit: 
#       -numbers still need to be included/ palindromes

## Data Structures
# strings, maybe lists again, but let me try to keep it to strings.

## Algorithm - high level
# 1. Take input string, convert to all lowercase, save as "working 
# string"
# 2. Remove all non-alphanumeric characters from "working string"
# 3. Reverse that "working 1st string" and compare it to the reversed
# version for equality. Return True if equal
# (This last step could be a helper function - like from prev exercise)

def is_palindrome(input_str):
    return input_str == input_str[::-1]

def is_real_palindrome(input_str):
    working_str = input_str.casefold()
    no_extras_str = ''
    for char in working_str:
        if char.isalnum():
            no_extras_str += char
    return is_palindrome(no_extras_str)

# Test cases
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True