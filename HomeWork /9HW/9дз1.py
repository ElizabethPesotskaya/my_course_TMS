import os

#Первый пункт
print("Операционная система ", os.name)

#Второй пункт
print("Путь до папки, в которой находимся ", os.getcwd())

#Третий пункт
files = os.listdir()

if not os.path.exists("txt_files"):
    os.mkdir("txt_files")
if not os.path.exists("py_files"):
    os.mkdir("py_files")
for file in files:
    if os.path.isfile(file):
        if file.endswith(".txt"):
            os.rename(file, os.path.join("txt_files", file))
            print("Файл", file, "перемещён в папку txt_files")
        elif file.endswith(".py"):
            os.rename(file, os.path.join("py_files", file))
            print("Файл", file, "перемещён в папку py_files")

#четвертый пункт
txt_files = os.listdir("txt_files")
py_files = os.listdir("py_files")

txt_count = 0
txt_size = 0

for file in txt_files:
    path = os.path.join("txt_files", file)
    if os.path.isfile(path):
        txt_count += 1
        txt_size += os.path.size(path)

py_count = 0
py_size = 0
for file in py_files:
    path = os.path.join("py_files", file)
    if os.path.isfile(path):
        py_count += 1
        py_size += os.path.size(path)

# Переводим байты в гигабайты
txt_gb = round(txt_size / (1024 ** 3), 2)
py_gb = round(py_size / (1024 ** 3), 2)

# Выводим итоговые сообщения
print("В папке с текстовыми файлами перемещено", txt_count, "файлов, их суммарный размер –", txt_gb, "гигабайт")
print("В папке с python-файлами перемещено", py_count, "файлов, их суммарный размер –", py_gb, "гигабайт")

#пятый пункт
os.rename("test.py", "test2.py")
print("Файл test.py был переименован в test2.py")

#шестой пункт
os.path.join("test2.py", "py_files")