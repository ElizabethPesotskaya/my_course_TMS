with open("my_file.txt", "r") as file:
    line1 = file.readline()
    print("Первая строка", line1)

with open("my_file.txt", "r") as file:
    file_lines5 = file.readlines()
    print("Пятая строка ", file_lines5[4])

with open("my_file.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    line5 = file.readline()
    print("Первые пять строк ")
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

with open("my_file.txt", "r") as file:
    file_lines = file.readlines()
    print("Строки с 1 по 2 ", file_lines[0], file_lines[1])

with open("my_file.txt", "r") as file:
    file_lines = file.read()
    print("Весь текст ", file_lines)


