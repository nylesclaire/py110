
LIST_OF_CONSONANTS = [
                    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 
                    "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]

LIST_OF_VOWELS = ["a" ,"e", "i", "o", "u"]


def sort_by_consonant_count(given_list_of_strings):
    given_list_of_strings.sort(reverse=True, key=count_max_adjacent_consonants)
    return given_list_of_strings

def count_max_adjacent_consonants(given_string):
    adj_consonants_substring = ""
    max_num = 0
    for char in given_string:
        if char in LIST_OF_CONSONANTS:
            adj_consonants_substring += char
        elif char in LIST_OF_VOWELS:
            if (len(adj_consonants_substring) != 1) and (len(adj_consonants_substring) > max_num):
                max_num = len(adj_consonants_substring)
            adj_consonants_substring = ""
    if (len(adj_consonants_substring) != 1) and (len(adj_consonants_substring) > max_num):
        max_num = len(adj_consonants_substring)
    return max_num


# Test cases
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list)) # ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list)) # ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list)) # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list)) # ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list)) # ['xxxx', 'xxxb', 'xxxa']