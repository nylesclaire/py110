### Problem
# input: matrix of arbitrary length and width, at least 1 row & column
# output: the same matrix, rotated 90 degrees

### Data Structures
# nested lists

### Algorithm
# I THINK....
# Transpose the matrix.
# Then reverse the order of the elements in each row.


def transpose(matrix):
    transposed = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count):
        transposed.append([])

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            transposed[col_idx].append(matrix[row_idx][col_idx])

    return transposed


def rotate90(matrix):
    new_matrix = transpose(matrix)
    for row in new_matrix:
        row.reverse()
    return new_matrix





matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)