
def remove_vowels(list_of_strings):
    new_lst = []
    for substring in list_of_strings:
        new_substr = ""
        for char in substring: 
            if char.lower() not in "aeiou":
                new_substr += char
        new_lst.append(new_substr)
    return new_lst

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True