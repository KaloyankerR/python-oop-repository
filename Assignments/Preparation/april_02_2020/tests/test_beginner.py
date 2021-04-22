import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.player = Beginner("Tony")

    def test_initialization_is_done_correctly(self):
        self.assertEqual(self.player.username, "Tony")
        self.assertEqual(self.player.health, 50)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")


if __name__ == '__main__':
    unittest.main()
