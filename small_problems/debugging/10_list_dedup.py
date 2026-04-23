

def unique_data(given_list):
    result_list = []
    for item in given_list:
        if item not in result_list:
            result_list.append(item)
    return result_list

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
print(unique_data(data) == [4, 2, 1, 3]) # order not guaranteed




