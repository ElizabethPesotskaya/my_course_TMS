import random

matrix = []

m = int(input("Введите количество строк "))
n = int(input("Введите количество столбцов "))

for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1,100))
    matrix.append(row)

for row in matrix:
    for num in row:
        print(f"{num: n}", end = " ")
    print( )






