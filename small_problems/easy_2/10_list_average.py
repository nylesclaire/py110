def average(list_of_ints):
    total = sum(list_of_ints)
    return total // (len(list_of_ints))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True