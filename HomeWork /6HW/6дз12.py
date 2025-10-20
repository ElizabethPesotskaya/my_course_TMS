matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

for row in matrix:
    row.append(sum(row) % 2)

for row in matrix:
    print(row)