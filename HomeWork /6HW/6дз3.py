n = int(input("Введите число "))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print("Число простое")
else:
    print("Число не является простым")