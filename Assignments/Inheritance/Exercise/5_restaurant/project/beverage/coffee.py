from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, price=self.__class__.COFFEE_PRICE, milliliters=self.__class__.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value
