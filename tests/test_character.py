import unittest
from game_logic.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.hero = Character("Héroe", 100, 20)
        self.monster = Character("Monstruo", 80, 15)

    def test_character_initialization(self):
        self.assertEqual(self.hero.name, "Héroe")
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.attack, 20)

    def test_is_alive_true(self):
        self.assertTrue(self.hero.is_alive())

    def test_is_alive_false(self):
        self.hero.take_damage(100)
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_partial(self):
        self.hero.take_damage(50)
        self.assertEqual(self.hero.health, 50)

    def test_take_damage_excessive(self):
        self.hero.take_damage(200)
        self.assertEqual(self.hero.health, 0)  # or set to 0 if handling negative health

    def test_attack_enemy(self):
        initial_health = self.monster.health
        self.hero.attack_enemy(self.monster)
        self.assertTrue(self.monster.health < initial_health)

    def test_str_representation(self):
        self.assertEqual(str(self.hero), "Héroe (100 HP, 20 ATK)")

if __name__ == '__main__':
    unittest.main()
