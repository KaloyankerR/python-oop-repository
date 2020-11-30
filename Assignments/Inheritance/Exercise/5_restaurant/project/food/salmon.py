from project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, grams=self.__class__.SALMON_GRAMS)
