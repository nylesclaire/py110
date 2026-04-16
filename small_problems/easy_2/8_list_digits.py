
def digit_list1(given_int):
    result_list = []
    str_lst = list(str(given_int))
    for item in str_lst:
        result_list.append(int(item))
    return result_list

# Okay because my solution was fairly inelegant let's retry this one after I finish
# the lesson on comprehensions! 

# Tried again 4-16-26:
def digit_list(given_int):
    return [int(char) for char in list(str(given_int))]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True