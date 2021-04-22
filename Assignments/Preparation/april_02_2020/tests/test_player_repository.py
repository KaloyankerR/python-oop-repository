import unittest

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.player_repo = PlayerRepository()
        self.beginner = Beginner('Noob')
        self.advanced = Advanced('Pro')

    def test_initialization_should_return_correct_attributes(self):
        self.assertEqual(self.player_repo.players, [])

    def test_add_should_add_a_player_to_the_players_list(self):
        self.player_repo.add(self.beginner)
        self.player_repo.add(self.advanced)

        self.assertEqual(self.player_repo.players, [self.beginner, self.advanced])

    def test_add_should_raise_error_when_player_adding_existing_player(self):
        self.player_repo.add(self.beginner)

        with self.assertRaises(ValueError) as cm:
            self.player_repo.add(self.beginner)
        self.assertEqual(str(cm.exception), "Player Noob already exists!")

    def test_remove_should_remove_player_from_the_players_list(self):
        self.player_repo.add(self.beginner)
        self.player_repo.add(self.advanced)

        self.player_repo.remove(self.advanced.username)
        self.assertEqual(self.player_repo.players, [self.beginner])

    def test_remove_should_raise_error_when_there_is_no_name_for_card(self):
        self.player_repo.add(self.beginner)

        with self.assertRaises(ValueError) as cm:
            self.player_repo.remove('')
        self.assertEqual(str(cm.exception), "Player cannot be an empty string!")

    def test_find_should_return_the_found_card(self):
        self.player_repo.add(self.beginner)
        self.player_repo.add(self.advanced)

        self.assertEqual(self.player_repo.find(self.advanced.username), self.advanced)

    def test_count_should_return_the_length_of_the_players_correctly(self):
        self.player_repo.add(self.beginner)
        self.player_repo.add(self.advanced)

        self.assertEqual(self.player_repo.count, 2)

if __name__ == '__main__':
    unittest.main()
