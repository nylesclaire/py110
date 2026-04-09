## Problem
# input: a string of words separated by spaces
# output: a string of the same length w/ 1st & last letters of each word
#           swapped.
# rules:
#   -explicit: 
#       -no input string will be empty
#       -no input string will have chars that aren't alphabetic or spaces
#       -no input string will have leading, trailing, or repeated spaces
#   -implicit:
#       -if a word is 1 letter, it remains the same
#       -case is retained after swaps.

## Data structures
# strings. Maybe will convert to a list and back to strings? 

## Algorithm
# 1. Make a list of words, split on spaces.
# 2. Initiate an empty list, "new list"
# 2. For each word in the list:
#   -save the first and last chars as variables
#   -reassign the first char in the word as the last_char variable, and 
#   vice versa
#   -save this word to "new list"
# 3. Join the list of words back together in a string, return that string

def swap(words_str):
    words_list = words_str.split()
    new_list = []
    for word in words_list:
        if len(word) == 1:
            new_list.append(word)
        else:
            orig_1st = word[0]
            orig_last = word[-1]
            new_list.append(orig_last + word[1:-1] + orig_1st)
    return(' '.join(new_list))

# Examples/ Test cases
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True