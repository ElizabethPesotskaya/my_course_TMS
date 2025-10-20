#создаем рандомайзер для чисел и строим их по возрастанию
from random import randint

a = [ ]
for i in range(10):
    a.append(randint(-50,50))
a.sort()
print(a)
value = int(input())

#создаем функцию, выполняющую рекурсивный алгоритм бинарного поиска
lower = 0
upper = len(a) - 1
mid = (lower + upper)//2

while value != a [mid]:
    if value > a[mid]:
        lower = mid + 1
    else:
        upper = mid - 1
    mid = (lower + upper) // 2

print("позиция искомого элемента в исходном списке", mid)




