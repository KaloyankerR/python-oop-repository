from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.animal_type} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.worker_type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [x for x in self.workers if x.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum([x.salary for x in self.workers])
        if workers_salaries <= self.__budget:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_tend_money = sum([x.get_needs() for x in self.animals])
        if animals_tend_money <= self.__budget:
            self.__budget -= animals_tend_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x.__repr__() for x in self.animals if isinstance(x, Lion)]
        tigers = [x.__repr__() for x in self.animals if isinstance(x, Tiger)]
        cheetahs = [x.__repr__() for x in self.animals if isinstance(x, Cheetah)]

        NEW_LINE = '\n'

        return f'''You have {len(self.animals)} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}'''

    def workers_status(self):
        keepers = [x.__repr__() for x in self.workers if isinstance(x, Keeper)]
        caretakers = [x.__repr__() for x in self.workers if isinstance(x, Caretaker)]
        vets = [x.__repr__() for x in self.workers if isinstance(x, Vet)]

        NEW_LINE = '\n'

        return f'''You have {len(self.workers)} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}'''
