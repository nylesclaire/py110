




def transpose1(og_matrix):
    new_mat = []
    for index in range(0,len(og_matrix)):
        current_new_inner_list = [inner_list[index] for inner_list in og_matrix]
        new_mat.append(current_new_inner_list)
    return new_mat

def transpose(matrix):
    transposed = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count):
        transposed.append([])

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            transposed[col_idx].append(matrix[row_idx][col_idx])

    return transposed




# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)