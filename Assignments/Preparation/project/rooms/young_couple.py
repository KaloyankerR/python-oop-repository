from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_ne: float, salary_two: float):
        super().__init__(name=family_name, budget=(salary_ne + salary_two), members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances)

    def get_monthly_expense(self):
        return sum([x.get_monthly_expense() for x in self.appliances])
