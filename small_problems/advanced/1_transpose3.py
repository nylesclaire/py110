#### Problem
# input: a list of lists that represents a 3x3 matrix
# output: the same, but with the values transposed.

### Data Structures
# - nested lists
# - in this case, integers

### Algorithm
# perhaps build each inner list with a list comprehension?
# for index of each item in o.g. inner list,
#   list comprehension to append the item at that index
#   to the new inner list w/ the same index?

def transpose(og_matrix):
    new_mat = []
    for index in range(0,len(og_matrix)):
        current_new_inner_list = [inner_list[index] for inner_list in og_matrix]
        new_mat.append(current_new_inner_list)
    return new_mat


# Examples
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True