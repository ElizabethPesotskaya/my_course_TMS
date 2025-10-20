class Calculator:
    def run(self):
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            operation = input("Выберите операцию: +, -, *, /, %, ^, √: ")

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                result = a / b
            elif operation == "%":
                result = a % b
            elif operation == "^":
                result = a ** b
            elif operation == "√":
                result = a ** (1 / b)
            else:
                raise ValueError("Недопустимая операция.")
            print("Ваш результат =", result)


        except ValueError as ve:
            print("Ошибка ввода:", ve)


calc = Calculator()
calc.run()
