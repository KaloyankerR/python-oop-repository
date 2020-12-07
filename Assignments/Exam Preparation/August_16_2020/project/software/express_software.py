from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name=name, type="Express", capacity_consumption=capacity_consumption, memory_consumption=memory_consumption)
        self.memory_consumption = int(self.memory_consumption * 2)
