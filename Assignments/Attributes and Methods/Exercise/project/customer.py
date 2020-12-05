class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        dvds_names = ", ".join([x.name for x in self.rented_dvds])
        # dvds_names = ", ".join(list(map(lambda x: x.name, self.rented_dvds)))
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({dvds_names})"
