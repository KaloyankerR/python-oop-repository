import unittest

# from project.appliances.appliance import Appliance
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('TestRoom', 1000, 1)

    def test_correct_initialization(self):
        self.assertEqual(self.room.family_name, 'TestRoom')
        self.assertEqual(self.room.budget, 1000)
        self.assertEqual(self.room.members_count, 1)
        self.assertEqual(self.room.children, [])
        # self.assertEqual(self.room.appliances, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_should_be_set_correctly(self):
        self.room.expenses = 20
        self.assertEqual(self.room.expenses, 20)

    def test_expenses_should_raise_error_when_value_is_negative(self):
        with self.assertRaises(ValueError) as cm:
            self.room.expenses = -20
        self.assertEqual(str(cm.exception), "Expenses cannot be negative")

    # def test_calculate_expenses_should_calculate_the_expenses_for_one_month_and_should_be_set_to_expenses(self):
    #     appliance = Appliance(2)
    #     self.room.calculate_expenses([appliance])
    #     self.assertEqual(self.room.expenses, 60)


if __name__ == '__main__':
    unittest.main()
