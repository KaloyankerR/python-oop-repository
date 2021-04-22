import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.card = TrapCard("Taro")

    def test_initialization_is_done_correctly(self):
        self.assertEqual(self.card.name, "Taro")
        self.assertEqual(self.card.damage_points, 120)
        self.assertEqual(self.card.health_points, 5)


if __name__ == '__main__':
    unittest.main()
