## Problem
# inputs: a string
# outputs: a bool
# rules: 
#    explicit: -a palindrome reads the same backwards as forwards
#       -case matters - palindromic chars must match in case.
#       -all characters matter including spaces, punctuation, etc.

## data structures 
# strings. Probably will convert to list for the reversed func.

## algorithm
# - take input string and reverse it, save as variable
# - compare input string to the new variable to see if equal.
# - if equal return True, if not return False.

def is_palindrome(str_input):
    list_input = list(str_input)
    rev_list_input = list(reversed(list_input))
    rev_str = ''.join(rev_list_input)
    return str_input == rev_str

# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)