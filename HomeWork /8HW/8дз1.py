try:
    mass = float(input("Вес, кг  "))
    height = float(input("Рост, м  "))
    if mass <= 0:
        print("Ошибка! Масса тела должна быть больше 0")
    else:
        bmi = mass / height **2
        print("Индекс массы тела равен ", bmi)

    if bmi < 16:
        categ = "Выраженный дефицит массы тела"
    elif bmi >= 16 and bmi < 18.5:
        categ = "Недостаточная (дефицит) масса тела"
    elif bmi >= 18.5 and bmi < 25:
        categ = "Норма"
    elif bmi >= 25 and bmi < 30:
        categ = "Избыточная масса тела (предожирение)"
    elif bmi >= 30 and bmi < 35:
        categ = "Ожирение первой степени"
    elif bmi >= 35 and bmi < 40:
        categ = "Ожирение второй степени"
    elif bmi >= 40:
        categ = "Ожирение третьей степени (морбидное)"
    print("Категория: ", categ)
except ValueError:
    print("Ошибка! Введите значения роста/веса в числовом начении")

