from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof-woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()


if __name__ == "__main__":
    factory = AnimalFactory()

    animal1 = factory.create_animal("dog")
    print(animal1.speak())

    animal2 = factory.create_animal("cat")
    print(animal2.speak())


