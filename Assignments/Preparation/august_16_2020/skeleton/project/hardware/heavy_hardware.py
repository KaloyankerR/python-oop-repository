from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name=name, type="Heavy", capacity=capacity, memory=memory)
        self.capacity = int(self.capacity * 2)
        self.memory = int(self.memory * 0.75)
