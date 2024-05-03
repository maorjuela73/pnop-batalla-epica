import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name} ataca a {enemy.name} y le inflige {damage} de daño.")
        enemy.take_damage(damage)
        print(f"{enemy.name} tiene {enemy.health} HP restantes.")

    def __str__(self):
        return f"{self.name} ({self.health} HP, {self.attack} ATK)"
