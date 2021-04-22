from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([(x.expenses + x.room_cost) for x in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            budget = room.budget
            needed_money = (room.expenses + room.room_cost)

            if budget >= needed_money:
                room.budget -= needed_money
                result.append(f"{room.family_name} paid {needed_money:.2f}$ and have {budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(result)

    def status(self):
        result = [f"Total population: {sum([x.members_count for x in self.rooms])}"]

        for room in self.rooms:
            family_name = room.family_name
            members_count = room.members_count
            budget = room.budget
            expenses = room.expenses
            result.append(
                f"{family_name} with {members_count} members. Budget: {budget:.2f}$, Expenses: {expenses:.2f}$")

            for n, child in enumerate(room.children, start=1):
                result.append(f"--- Child {n} monthly cost: {child.cost * 30:.2f}$")

            result.append(f"--- Appliances monthly cost: {room.get_monthly_expense():.2f}$")

        return '\n'.join(result)
