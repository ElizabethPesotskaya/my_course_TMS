with open("text.txt", "w") as file:
    for i in range(6):
        text = input("Введите строку " + str(i + 1) + ": ")
        file.write(text + "\n")  # записываем строку в файл

print("Файл создан и заполнен.")
