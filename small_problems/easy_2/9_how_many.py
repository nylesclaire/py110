vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def count_occurrences1(lst):
    for item in set(lst):
        print(f"{item} => {lst.count(item)}")


# Try to solve the problem when words are case insensitive, 
# e.g. "suv" and "SUV" represent the same vehicle type.
def count_occurrences(lst):
    working_lst = [item.lower() for item in lst]
    for item in set(working_lst):
        print(f"{item} => {working_lst.count(item)}")

count_occurrences(vehicles)