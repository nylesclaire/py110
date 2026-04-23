

data_set = {1, 2, 3, 4, 5}

data_list = list(data_set)
for item in data_list:
    if item % 2 == 0:
        data_list.remove(item)
    
print(data_list)