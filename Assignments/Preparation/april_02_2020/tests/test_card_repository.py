import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.card_repo = CardRepository()
        self.magic_card = MagicCard('Magic')
        self.trap_card = TrapCard('Trap')

    def test_initialization_is_returns_correct_attributes(self):
        self.assertEqual(self.card_repo.cards, [])

    def test_add_should_add_a_card_to_the_cards(self):
        self.card_repo.add(self.magic_card)
        self.card_repo.add(self.trap_card)

        self.assertEqual(self.card_repo.cards, [self.magic_card, self.trap_card])

    def test_add_should_raise_error_card_already_in_cards(self):
        self.card_repo.add(self.magic_card)

        with self.assertRaises(ValueError) as cm:
            self.card_repo.add(self.magic_card)
        self.assertEqual(str(cm.exception), f"Card Magic already exists!")

    def test_remove_should_remove_existing_card(self):
        self.card_repo.add(self.magic_card)
        self.card_repo.remove('Magic')

        self.assertEqual(self.card_repo.cards, [])

    def test_remove_should_raise_error_when_the_card_name_is_empty_str(self):
        self.card_repo.add(self.trap_card)

        with self.assertRaises(ValueError) as cm:
            self.card_repo.remove('')
        self.assertEqual(str(cm.exception), "Card cannot be an empty string!")

    def test_find_should_return_the_found_card(self):
        self.card_repo.add(self.magic_card)
        self.card_repo.add(self.trap_card)

        self.assertEqual(self.card_repo.find(self.trap_card.name), self.trap_card)

    def test_count_should_return_the_length_of_the_cards_properly(self):
        self.card_repo.add(self.magic_card)
        self.card_repo.add(self.trap_card)

        self.assertEqual(self.card_repo.count, 2)

if __name__ == '__main__':
    unittest.main()
