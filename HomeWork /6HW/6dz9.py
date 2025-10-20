matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list = [ ]

for row in matrix:
    for value in row:
        list.append(value)

summa = sum(list)
print("Сумма элементов каждого столбца", summa)

columns = len(matrix[0])
sum_columns = [0] * columns
for row in matrix:
        for i in range(columns):
            sum_columns[i] += row[i]

column_percent = []
for col_sum in sum_columns:
    percent = (col_sum / summa) * 100
    column_percent.append(percent)

print("Сумма элементов каждого столбца к доле общей суммы матрицы ", column_percent)