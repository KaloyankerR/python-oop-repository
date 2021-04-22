class Child:
    def __init__(self, food_cost: int, *args):
        self.cost = food_cost + sum(args)

    def get_monthly_expense(self):
        return self.cost * 30