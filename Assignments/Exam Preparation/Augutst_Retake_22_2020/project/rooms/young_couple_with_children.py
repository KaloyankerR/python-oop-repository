from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=(salary_one + salary_two), members_count=2 + len(children))
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]

        for _ in children:
            self.appliances.extend([TV(), Fridge(), Laptop()])

        self.calculate_expenses(self.appliances, self.children)
