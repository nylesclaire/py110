

# multiple ways to fix this
def get_key_value1(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None
    
def get_key_value2(my_dict, key):
    if key in my_dict.keys():
        return my_dict[key]
    else:
        return None
    
def get_key_value(my_dict, key):
    return my_dict.get(key, "It's not in here")

print(get_key_value({"a": 1}, "b"))