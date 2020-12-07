from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name=name, type="Power", capacity=capacity, memory=memory)
        self.capacity = int(self.capacity * 0.25)
        self.memory = int(self.memory * 1.75)
