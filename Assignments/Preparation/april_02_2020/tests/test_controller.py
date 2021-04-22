import unittest

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

        self.beginner = Beginner('Noob')
        self.advanced = Advanced('Pro')
        self.magic_card = MagicCard('Magic')
        self.trap_card = TrapCard('Trap')

    def test_initialization_should_return_correct_attributes(self):
        self.assertEqual(self.controller.player_repository.__class__.__name__, "PlayerRepository")
        self.assertEqual(self.controller.card_repository.__class__.__name__, "CardRepository")

    def test_add_player_should_add_player_to_the_player_repository(self):
        self.assertEqual(self.controller.add_player('Advanced', 'Pro'),
                         "Successfully added player of type Advanced with username: Pro")
        self.assertEqual(self.controller.player_repository.count, 1)

    def test_add_card_should_add_card_to_the_card_repository(self):
        self.assertEqual(self.controller.add_card('TrapCard', 'Trap'),
                         "Successfully added card of type TrapCardCard with name: Trap")
        self.assertEqual(self.controller.card_repository.count, 1)

    def test_add_player_card_should_add_card_in_players_repository(self):
        self.controller.add_player('Beginner', 'Noob')
        self.controller.add_card('MagicCard', 'Magic')

        self.assertEqual(self.controller.add_player_card('Noob', 'Magic'),
                         'Successfully added card: Magic to user: Noob')

    def test_fight_should_make_both_players_fight(self):
        self.controller.add_player('Advanced', 'Pro1')
        self.controller.add_player('Advanced', 'Pro2')

        self.assertEqual(self.controller.fight('Pro1', 'Pro2'), 'Attack user health 250 - Enemy user health 250')

    def test_report_should_return_correctly_the_result(self):
        self.controller.add_player('Beginner', 'Noob')
        self.controller.add_card('MagicCard', 'Magic')

        self.assertEqual(self.controller.report(), 'Username: Noob - Health: 50 - Cards 0\n')


if __name__ == '__main__':
    unittest.main()
