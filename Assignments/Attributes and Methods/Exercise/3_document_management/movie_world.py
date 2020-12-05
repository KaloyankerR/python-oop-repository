class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        customer = [x for x in self.customers if x.id == customer_id][0]

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in customer.rented_dvds if x.id == dvd_id]
        if not dvd:
            return f"{customer.name} does not have that DVD"
        dvd = dvd[0]
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        # return '\n'.join([repr(x) for x in (self.customers + self.dvds)])
        data = ''
        for c in self.customers:
            data += f'{c}\n'
        for d in self.dvds:
            data += f'{d}\n'
        return data
