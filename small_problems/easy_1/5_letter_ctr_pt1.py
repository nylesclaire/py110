## Problem
# input: string w/ zero or more words
# output: dict showing the number of words of different sizes
# rules:
#   explicit: 
#       -words consist of any sequence of non-space characters.
#       -input string can be empty & should return empty dict in that case
#   implicit:
#       -dictionary should have length of the words as keys, and number
#       of words of that length (instances) as values

## Data Structures
# strings, their lengths and quantity as integers, our final dict
# maybe a list of the words, if I want to split the string on spaces

## Algorithm
# 1. Take input string and split it on whitespace chars. Probably save
# resulting words into a list.
# 2. Initiate empty result dictionary.
# 3. Iterate through the list, taking the length of each word, and 
# adding that length to the result dict with value of 1, or if that key 
# already exists, adding another instance to the value.
# 4. Return the result dict.

def word_sizes(given_str):
    words_list = given_str.split()
    result_dict = {}
    for word in words_list:
        if result_dict.get(len(word)):
            result_dict[len(word)] += 1
        else:
            result_dict[len(word)] = 1
    return result_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})