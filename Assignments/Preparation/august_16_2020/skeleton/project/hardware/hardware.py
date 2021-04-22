from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_capacity(self):
        return sum([x.capacity_consumption for x in self.software_components])

    @property
    def used_memory(self):
        return sum([x.memory_consumption for x in self.software_components])

    @property
    def express_software_components_length(self):
        return len([x for x in self.software_components if x.type == "Express"])

    @property
    def light_software_components_length(self):
        return len([x for x in self.software_components if x.type == "Express"])

    @property
    def software_components_names(self):
        return [x.name for x in self.software_components]

    def install(self, software: Software):
        if (software.capacity_consumption + self.used_capacity) > self.capacity or (software.memory_consumption + self.used_memory) > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)
