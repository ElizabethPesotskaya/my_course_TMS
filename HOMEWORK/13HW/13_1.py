def cycle_numbers():
    while True:
        yield 1
        yield 2
        yield 3

def main():
    n = int(input("Введите количество чисел для вывода "))
    generator = cycle_numbers()
    for i in range(n):
        print(next(generator), end=' ')

if __name__ == "__main__":
    main()