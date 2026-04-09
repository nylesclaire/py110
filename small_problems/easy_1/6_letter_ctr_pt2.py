def word_sizes(given_str):
    cleaned_str = ''
    for char in given_str:
        if char.isspace() or char.isalnum():
            cleaned_str += char
    words_list = cleaned_str.split()
    result_dict = {}
    for word in words_list:
        if result_dict.get(len(word)):
            result_dict[len(word)] += 1
        else:
            result_dict[len(word)] = 1
    return result_dict


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})