def find_columns_with_and_without_h(matrix, h):
    columns_with_h = []
    columns_without_h = []

    m = len(matrix)
    n = len(matrix[0])

    for j in range(n):
        found_h_in_column = False
        for i in range(m):
            if matrix[i][j] == h:
                found_h_in_column = True

        if found_h_in_column:
            columns_with_h.append(j)
        else:
            columns_without_h.append(j)

    return columns_with_h, columns_without_h

h = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols_with_h, cols_without_h = find_columns_with_and_without_h(matrix, h)

print("Столбцы с числом H:", cols_with_h)
print("Столбцы без числа H:", cols_without_h)
