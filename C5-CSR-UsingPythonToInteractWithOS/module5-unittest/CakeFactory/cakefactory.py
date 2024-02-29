from typing import List

class CakeFactory():
    def __init__(self, cake_type: str, size: str) -> None:
        self.cake_type = cake_type
        self.size = size
        self.toppings = []

        self.__price = 10 if self.cake_type == "chocolate" else 8
        self.__price += 2 if self.size == "medium" else 4 if self.size == "large" else 0
    
    def add_topping(self, *topping: str) -> None:
        for x in topping:
            self.toppings.append(x)
            self.__price += 1

    def check_ingredients(self) -> List[str]:
        ingredients = ['flour', 'sugar', 'eggs']
        ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
        ingredients += self.toppings
        return ingredients 

    def check_price(self) -> float:
        return self.__price

if __name__ == "__main__":
    cake = CakeFactory("vanilla", "large")
    cake.add_topping("sprinkles","cherries")
    cake_ingredients = cake.check_ingredients()
    price = cake.check_price()

    print(cake, price, cake_ingredients)