import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.player = Advanced("Tony")

    def test_initialization_is_done_correctly(self):
        self.assertEqual(self.player.username, "Tony")
        self.assertEqual(self.player.health, 250)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")

    def test_username_raises_error_when_trying_to_set_it_to_empty_str(self):
        with self.assertRaises(ValueError) as cm:
            self.player.username = ""
        self.assertEqual(str(cm.exception), "Player's username cannot be an empty string.")

    def test_health_raises_error_when_trying_to_set_it_below_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.player.health = -1
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead_returns_false_if_health_is_positive(self):
        self.assertEqual(self.player.is_dead, False)

    def test_is_dead_returns_true_if_health_is_not_positive(self):
        self.player.health = 0
        self.assertEqual(self.player.is_dead, True)

    def test_take_damage_raises_error_when_damage_points_are_less_than_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.player.take_damage(-10)
        self.assertEqual(str(cm.exception), "Damage points cannot be less than zero.")

    def test_take_damage_decreases_health_when_damage_points_is_positive_number(self):
        self.player.take_damage(30)
        self.assertEqual(self.player.health, 220)


if __name__ == '__main__':
    unittest.main()
