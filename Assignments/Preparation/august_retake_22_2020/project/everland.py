from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumptions = sum(list(map(lambda x: x.expenses + x.room_cost, self.rooms)))
        return f"Monthly consumption: {total_consumptions}$."

    def pay(self):
        result = []
        for family in self.rooms:
            money_needed = family.expenses + family.room_cost
            budget = family.budget
            if family.budget >= money_needed:
                family.budget -= money_needed
                result.append(f"{family.family_name} paid {money_needed:.2f}$ and have {budget:.2f}$ left.")
            else:
                self.rooms.remove(family)
                result.append(f"{family.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(result)

    def status(self):
        all_people_in_the_hotel = sum(list(map(lambda x: x.members_count, self.rooms)))
        result = [f"Total population: {all_people_in_the_hotel}"]

        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for n, child in enumerate(room.children, start=1):
                    result.append(f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$")

            all_appliances_cost = sum(x.get_monthly_expense() for x in room.appliances)
            result.append(f"--- Appliances monthly cost: {all_appliances_cost:.2f}$")

        return '\n'.join(result)
