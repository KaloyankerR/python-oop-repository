from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name=name, type='Power', capacity=capacity, memory=memory)
        self.capacity = int(capacity * 0.25)
        self.memory = int(memory * 1.75)

