"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]


# input: string
# output: list of strings (a new object)
# rules: 
#   Explicit requirements:
#       -Every palindromic substring of at least two characters should 
#       be added to our list. 
#       -palindromic substrings are case sensitive.
#       -palindromic substrings that are contained in other palindromic
#       substrings should be included as separate list items
#       -a palindromic substring need not be its own word, it can be 
#       part of a word.
#   Implicit requirements:
#       -if the string is empty, it should return an empty list.
#       -if there are no palindromic substrings, it should return 
#       an empty list
#       -for this, let's assume all inputs are strings. 