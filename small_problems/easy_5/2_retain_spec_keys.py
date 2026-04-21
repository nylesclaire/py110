def keep_keys(given_dict, list_of_keys):
    return {key: value 
            for key, value in given_dict.items() 
            if key in list_of_keys}

# Test case
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True