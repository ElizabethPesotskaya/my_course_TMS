from dataclasses import dataclass

@dataclass
class Pizza:
    size: str = None
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    onions: bool = False
    bacon: bool = False

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.mushrooms:
            ingredients.append("mushrooms")
        if self.onions:
            ingredients.append("onions")
        if self.bacon:
            ingredients.append("bacon")

        size_str = f"Size: {self.size}"
        ingredients_str = ", ".join(ingredients)

        return f"Pizza {size_str}\n ingredients: {ingredients_str}"


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size: str):
        self._pizza.size = size
        return self

    def add_cheese(self):
        self._pizza.cheese = True
        return self

    def add_pepperoni(self):
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self._pizza.mushrooms = True
        return self

    def add_onions(self):
        self._pizza.onions = True
        return self

    def add_bacon(self):
        self._pizza.bacon = True
        return self

    def build(self):
        return self._pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_size("Large")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.add_bacon()
        return self.builder.build()

if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.make_pizza()
    print(pizza)


