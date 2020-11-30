from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def _AIR_CONDITIONERS(self):
        pass

    @abstractmethod
    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._AIR_CONDITIONERS)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    _AIR_CONDITIONERS = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._AIR_CONDITIONERS)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _AIR_CONDITIONERS = 1.6

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._AIR_CONDITIONERS)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
