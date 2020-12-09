from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name=name, capacity_consumption=capacity_consumption,
                                           memory_consumption=memory_consumption)
        try:
            hardware[0].install(express_software)
            System._software.append(express_software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        light_software = LightSoftware(name=name, capacity_consumption=capacity_consumption,
                                       memory_consumption=memory_consumption)
        try:
            hardware[0].install(light_software)
            System._software.append(light_software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_hardware(hardware_name)
        software = System.get_software(software_name)

        if not (hardware or software):
            return "Some of the components do not exist"

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        used_memory = int(sum([x.used_memory for x in System._hardware]))
        total_memory = int(sum([x.memory for x in System._hardware]))
        used_capacity = int(sum([x.used_capacity for x in System._hardware]))
        total_capacity = int(sum([x.capacity for x in System._hardware]))

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            express_os_count = len([x for x in hardware.software_components if x.type == 'Express'])
            light_os_count = len([x for x in hardware.software_components if x.type == 'Light'])
            used_memory = int(hardware.used_memory)
            total_memory = int(hardware.memory)
            used_capacity = int(hardware.used_capacity)
            total_capacity = int(hardware.capacity)

            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {express_os_count}\n" \
                      f"Light Software Components: {light_os_count}\n" \
                      f"Memory Usage: {used_memory} / {total_memory}\n" \
                      f"Capacity Usage: {used_capacity} / {total_capacity}\n" \
                      f"Type: {hardware.type}\n" \
                      f"Software Components: {hardware.software_components_names()}"

        return result

    @staticmethod
    def get_hardware(hardware_name):
        return [x for x in System._hardware if x.name == hardware_name]

    @staticmethod
    def get_software(software_name):
        return [x for x in System._software if x.name == software_name]
