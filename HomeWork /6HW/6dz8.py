matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

min_value = matrix[0][0]
max_value = matrix[0][0]
min_row = 0
min_col = 0
max_row = 0
max_col = 0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        value = matrix[i][j]
        if value < min_value:
            min_value = value
            min_row = i
            min_col = j
        if value > max_value:
            max_value = value
            max_row = i
            max_col = j

print("Минимальный элемент:", min_value)
print("индекс строки:", min_row, "индекс столбца: ", min_col)
print("Максимальный элемент:", max_value)
print("индекс строки:", max_row, "индекс столбца: ", max_col)