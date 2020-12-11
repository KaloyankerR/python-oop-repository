import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('Test', 'Power', 100, 100)

    def test_correct_initialization(self):
        self.assertEqual(self.hardware.name, 'Test')
        self.assertEqual(self.hardware.type, 'Power')
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_should_add_software_to_the_software_components(self):
        software = Software('Windows', 'Light', 50, 50)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)
        # self.assertEqual(len(self.hardware.software_components), 1)

    def test_install_should_raise_error_if_capacity_or_memory_are_more_than_the_hardware_ones(self):
        software = Software('Windows', 'OS', 150, 150)

        with self.assertRaises(Exception) as cm:
            self.hardware.install(software)
        self.assertEqual(str(cm.exception), "Software cannot be installed")

    def test_uninstall_should_remove_software_from_the_software_components(self):
        software = Software('Windows', 'OS', 25, 25)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)


if __name__ == '__main__':
    unittest.main()
