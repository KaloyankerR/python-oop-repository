from project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000
    CAKE_PRICE = 5

    def __init__(self, name):
        super().__init__(name, price=self.__class__.CAKE_PRICE, grams=self.__class__.CAKE_GRAMS, calories=self.__class__.CAKE_CALORIES)
