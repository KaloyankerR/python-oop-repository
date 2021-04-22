class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.room_cost = 0
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = sum([x.get_monthly_expense() for arg in args for x in arg])
        self.__expenses = result

    def get_monthly_expense(self):
        return sum([x.get_monthly_expense() for x in self.appliances])
