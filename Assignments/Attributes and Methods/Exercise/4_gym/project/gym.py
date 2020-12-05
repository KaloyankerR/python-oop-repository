class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        def get_customer():
            customer = [x for x in self.customers if x.id == subscription.customer_id]
            if customer:
                return f"{customer[0]}\n"
            return ''

        def get_trainer():
            trainer = [x for x in self.trainers if x.id == subscription.trainer_id]
            if trainer:
                return f"{trainer[0]}\n"
            return ''

        def get_equipment():
            equipment_id = [x.equipment_id for x in self.plans if x.id == subscription.exercise_id]
            if equipment_id:
                equipment_id = equipment_id[0]
                equipment = [x for x in self.equipment if x.id == equipment_id]
                if equipment:
                    return f"{equipment[0]}\n"
            return ''

        def get_exercise_plan():
            exercise_plan = [x for x in self.plans if x.id == subscription.exercise_id]
            if exercise_plan:
                return f"{exercise_plan[0]}"
            return ''

        data = f""
        subscription = [x for x in self.subscriptions if x.id == subscription_id]

        if subscription:
            subscription = subscription[0]
            data += f"{subscription}\n"
            data += get_customer()
            data += get_trainer()
            data += get_equipment()
            data += get_exercise_plan()

        return data
