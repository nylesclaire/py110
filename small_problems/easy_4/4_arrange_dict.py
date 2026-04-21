### Problem
# input: a dictionary
# output: a list of keys, sorted by the values

### Data Structures
# dictionary
# list
# sort or sorted function... need a helper function w/ one keyword arg?

### Algorithm
# 1) get a list of tuples for the dict (.items())]
# 2) use a list comprehension or similar to swap the order of the items
#   in each tuple
# 3) sort the list
# 4) make a new list w/ just the first element of each tuple, return it

def order_by_value(given_dict):
    swapped = [(value, key) for (key, value) in list(given_dict.items())]
    swapped.sort()
    return [key for value, key in swapped]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True