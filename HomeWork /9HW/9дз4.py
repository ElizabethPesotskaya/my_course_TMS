with open("my_file.txt", "r") as file1, open("file2.txt", "r") as file2:
    file_lines1 = file1.readlines()
    file_lines2 = file2.readlines()

    if len(file_lines1) != len(file_lines2):
        print("Количество строк в первом файле не соответствует количеству строк во втором файле")
    else:
        for i in range(len(file_lines1)):
            if file_lines1[i].strip() != file_lines2[i].strip():
                print("Строки отличаются на строке", i + 1)
                break
        else:
            print('Все строки совпадают')

