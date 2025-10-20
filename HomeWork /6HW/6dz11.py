matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix[0])
sum_main = 0
sum_side = 0
for i in range(n):
    sum_main += matrix[i][i]
    sum_side += matrix[i][n - i - 1]

print("Сумма основной диагонали матрицы", sum_main)
print("Сумма побочной диагонали матрицы", sum_side)