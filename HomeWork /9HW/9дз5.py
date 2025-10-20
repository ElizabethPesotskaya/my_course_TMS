import json
import csv
import os

#второй/третий подпункт
with open("json2.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for item in data:
    if isinstance(item.get("languages"), list):
        item["languages"] = ", ".join(item["languages"])

headers = data[0].keys()

with open("output.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

#четвертый подпункт
def add_employee():
    with open("json2.json", "r", encoding="utf-8") as file:
        data = json.load(file)

print("Введите информацию о новом сотруднике:")
name = input("Имя и фамилия: ")
birthday = input("Дата рождения (ДД.ММ.ГГГГ): ")
height = int(input("Рост (в см): "))
weight = float(input("Вес (в кг): "))
car_input = input("Есть ли машина? (да/нет): ").strip().lower()
car = True if car_input == "да" else False
languages_input = input("Какие языки программирования знает? (через запятую): ")
languages = [lang.strip() for lang in languages_input.split(",")]

new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }

data.append(new_employee)

with open("json2.json", 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Сотрудник", "name", "успешно добавлен в", "json2.json")

#пятый подпункт
new_employee["languages"] = ", ".join(new_employee["languages"])

file_exists = os.path.isfile("output.csv")

with open("output.csv", 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow(new_employee)

print("Сотрудник", name, "успешно добавлен в output.csv")

#шестой подпункт
def find_by_name():
    with open("json2.json", "r") as file:
        data = json.load(file)
    name = input("Введите имя сотрудника: ")
    for employee in data:
        if employee["name"] == name:
            print(employee)

#седьмой подпункт
def filter_by_language():
    with open("json2.json", "r") as file:
        data = json.load(file)
    language = input("Введите язык программирования: ")
    for employee in data:
        if language in employee["languages"]:
            print(employee)

#восьмой подпункт
def filter_by_year():
    with open("json2.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    year = int(input("Введите год рождения: "))
    total_height = 0
    count = 0
    for employee in data:
        birth_year = int(employee["birthday"].split(".")[2])
        if birth_year < year:
            total_height += employee["height"]
            count += 1
    if count > 0:
        average = total_height / count
        print("Средний рост:", round(average, 2), "см")

#девятый подпункт
def main():
    while True:
        print("\nМеню:")
        print("1 – Добавить сотрудника")
        print("2 – Найти по имени")
        print("3 – Фильтр по языку")
        print("4 – Фильтр по году рождения")
        print("5 – Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            find_by_name()
        elif choice == "3":
            filter_by_language()
        elif choice == "4":
            filter_by_year()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


