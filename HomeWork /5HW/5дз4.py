#создаем список чисел
n = input("Введите список чисел ")

#переводим данные числа в стоку
chisla = list(map(int, n.split()))

#преобразуем строки в числа
for i in range(len(chisla)):
    chisla[i] = int(chisla[i])

# Создаём список для повторяющихся чисел
povtor = []

# Проверяем каждое число на повтор в списке
for num in chisla:
    if chisla.count(num) > 1: #ищет число повторов
        if num not in povtor: #проверяем, что мы ещё не добавляли это число в список повторов
            povtor.append(num)

# Выводим результат
if len(povtor) == 0:
    print("Все элементы уникальны ")
else:
    print("Есть повторяющиеся числа:")
    for d in povtor:
        print("Число", d, "встречается", chisla.count(d), "раза")