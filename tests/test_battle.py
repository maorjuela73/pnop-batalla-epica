import unittest
from game_logic.character import Character
from game_logic.battle import Battle

class TestBattle(unittest.TestCase):
    def setUp(self):
        self.hero = Character("Héroe", 100, 20)
        self.monster = Character("Monstruo", 50, 10)
        self.battle = Battle(self.hero, self.monster)

    def test_battle_initialization(self):
        self.assertEqual(self.battle.player.name, "Héroe")
        self.assertEqual(self.battle.enemy.name, "Monstruo")

    def test_battle_end_hero_wins(self):
        #performs turns until game ends
        while self.hero.is_alive() and self.monster.is_alive():
            self.battle.perform_turn()
        self.assertTrue(self.hero.is_alive())
        self.assertFalse(self.monster.is_alive())

    def test_battle_end_monster_wins(self):
        self.hero.take_damage(90)
        while self.hero.is_alive() and self.monster.is_alive():
            self.battle.perform_turn()
        self.assertFalse(self.hero.is_alive())
        self.assertTrue(self.monster.is_alive())

if __name__ == '__main__':
    unittest.main()