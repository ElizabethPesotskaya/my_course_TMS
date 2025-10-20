class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def increase(self):
        self.__speed += 5

    def decrease(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def display(self):
        print("текущая скорость", self.__speed, "км/ч")

    def reversal(self):
        self.__speed = -self.__speed
