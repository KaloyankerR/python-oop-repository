from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def hardware_name(name):
        return [x for x in System._hardware if x.name == name]

    @staticmethod
    def software_name(name):
        return [x for x in System._software if x.name == name]

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.hardware_name(hardware_name)
        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        # print(len(System._software))

        if not hardware:
            return "Hardware does not exist"

        try:
            hardware[0].install(new_software)
            System._software.append(new_software)
        except Exception as cm:
            return str(cm)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.hardware_name(hardware_name)
        new_software = LightSoftware(name, capacity_consumption, memory_consumption)

        if not hardware:
            return "Hardware does not exist"

        try:
            hardware[0].install(new_software)
            System._software.append(new_software)
        except Exception as cm:
            return str(cm)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.hardware_name(hardware_name)
        software = System.software_name(software_name)

        if hardware and software:
            hardware[0].uninstall(software[0])
            System._software.remove(software[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        used_memory = sum([x.memory_consumption for x in System._software])
        total_memory = sum([x.memory for x in System._hardware])

        used_capacity = sum([x.capacity_consumption for x in System._software])
        total_capacity = sum([x.capacity for x in System._hardware])

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            express_components = sum([x.express_software_components_length for x in System._hardware])
            light_components = sum([x.light_software_components_length for x in System._hardware])

            used_memory = sum([x.memory_consumption for x in System._software])
            total_memory = sum([x.memory for x in System._hardware])

            used_capacity = sum([x.capacity_consumption for x in System._software])
            total_capacity = sum([x.capacity for x in System._hardware])

            software_components_names = "None"
            if hardware.software_components_names:
                software_components_names = ', '.join(hardware.software_components_names)
            result += f"Hardware Component - {hardware.name}\n"

            result += f"Express Software Components: {express_components}\n"

            result += f"Light Software Components: {light_components}\n"

            result += f"Memory Usage: {used_memory} / {total_memory}\n"

            result += f"Capacity Usage: {used_capacity} / {total_capacity}\n"

            result += f"Type: {hardware.type}\n"

            result += f"Software Components: {software_components_names}"

            return result
