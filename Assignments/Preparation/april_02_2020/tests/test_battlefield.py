import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battlefield = BattleField()

    def test_if_one_from_the_players_is_dead_should_raise_error(self):
        attacker = Advanced('Thor')
        enemy = Beginner('War-Machine')

        enemy.health = 0

        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_attacker_beginner_should_increase_his_attributes(self):
        attacker = Beginner('Tony')
        enemy = Advanced('Thanos')
        card = MagicCard('SomeCard')

        attacker.card_repository.cards.append(card)
        self.battlefield.fight(attacker, enemy)

        self.assertEqual(attacker.health, 170)
        self.assertEqual(enemy.health, 215)
        self.assertEqual(card.damage_points, 35)

    def test_enemy_beginner_should_increase_his_attributes(self):
        enemy = Beginner('Tony')
        attacker = Advanced('Thanos')
        card = MagicCard('SomeCard')

        enemy.card_repository.cards.append(card)
        self.battlefield.fight(attacker, enemy)

        self.assertEqual(enemy.health, 170)
        self.assertEqual(attacker.health, 215)
        self.assertEqual(card.damage_points, 35)

    def test_fight_should_decrease_the_health_of_both_players(self):
        attacker = Advanced('Quil')
        enemy = Beginner('Peter')
        attacker_card = MagicCard('AnotherCard')
        enemy_card = TrapCard('JustACard')

        attacker.card_repository.cards.append(attacker_card)
        enemy.card_repository.cards.append(enemy_card)
        self.battlefield.fight(attacker, enemy)

        self.assertEqual(attacker.health, 180)
        self.assertEqual(enemy.health, 90)

    def test_player_dies_in_fight(self):
        attacker = Advanced('Peter')
        enemy = Beginner('SomeOne')

        attacker_card = TrapCard('AttackerCard')
        enemy_card = MagicCard('EnemyCard')

        attacker.card_repository.cards.append(attacker_card)
        enemy.card_repository.cards.append(enemy_card)

        self.battlefield.fight(attacker, enemy)
        self.battlefield.fight(attacker, enemy)
        self.battlefield.fight(attacker, enemy)
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")




if __name__ == '__main__':
    unittest.main()
