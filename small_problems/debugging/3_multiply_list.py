
# with original loop concept
def multiply_list1(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item * 2)
    return new_lst

# with list comprehension
def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])