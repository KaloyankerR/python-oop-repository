import unittest

from project.hardware.hardware import Hardware
# from project.hardware.power_hardware import PowerHardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('CPU', 'Hardware', 100, 100)

    def test_initialization(self):
        self.assertEqual(self.hardware.name, 'CPU')
        self.assertEqual(self.hardware.type, 'Hardware')
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)

    def test_install_should_raise_error_when_there_is_not_enough_memory_or_capacity(self):
        software = Software('Windows', 'Software', 110, 110)

        with self.assertRaises(Exception) as cm:
            self.hardware.install(software)
        self.assertEqual(str(cm.exception), "Software cannot be installed")

    def test_install_should_add_a_software_to_the_software_components(self):
        software = Software('Windows', 'Software', 100, 100)
        self.assertEqual(len(self.hardware.software_components), 0)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_uninstall_should_remove_software_from_the_software_components(self):
        software = Software('Windows', 'Software', 100, 100)
        self.hardware.install(software)

        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_uninstall_should_not_remove_the_software_if_it_is_not_in_the_software_components(self):
        software = Software('Windows', 'Software', 100, 100)
        self.hardware.install(software)

        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)


if __name__ == '__main__':
    unittest.main()
