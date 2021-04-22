import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard("Taro")

    def test_initialization_is_done_correctly(self):
        self.assertEqual(self.card.name, "Taro")
        self.assertEqual(self.card.damage_points, 5)
        self.assertEqual(self.card.health_points, 80)

    def test_name_setter_with_empty_str_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.name = ""
        self.assertEqual(str(cm.exception), "Card's name cannot be an empty string.")

    def test_damage_points_with_negative_value_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.damage_points = -10
        self.assertEqual(str(cm.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_with_negative_value_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.health_points = -10
        self.assertEqual(str(cm.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
