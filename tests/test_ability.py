import unittest
from game_logic.character import Character
from game_logic.ability import Ability

class TestAbility(unittest.TestCase):
    def setUp(self):
        self.hero = Character("Héroe", 100, 20)
        self.monster = Character("Monstruo", 80, 15)
        self.fireball = Ability("Bola de Fuego", 30)

    def test_ability_initialization(self):
        self.assertEqual(self.fireball.name, "Bola de Fuego")
        self.assertEqual(self.fireball.damage, 30)

    def test_use_ability(self):
        initial_health = self.monster.health
        self.fireball.use(self.hero, self.monster)
        self.assertTrue(self.monster.health < initial_health)

    def test_ability_effectiveness(self):
        self.fireball.use(self.hero, self.monster)
        damage_done = 80 - self.monster.health
        self.assertTrue(0 <= damage_done <= 30)

if __name__ == '__main__':
    unittest.main()
