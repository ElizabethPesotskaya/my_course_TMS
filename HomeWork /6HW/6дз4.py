a = int(input("введите первое число "))
b = int(input("введие второе число "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("НОД = ", a)