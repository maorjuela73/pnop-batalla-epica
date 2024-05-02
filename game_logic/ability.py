import random

class Ability:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use(self, character, enemy):
        damage = random.randint(0, self.damage)
        print(f"{character.name} utiliza {self.name} y le inflige {damage} de daño a {enemy.name}.")
        enemy.take_damage(damage)
