class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def perform_turn(self, damage_messages):
        if self.player.is_alive() and self.enemy.is_alive():
            damage = self.player.attack_enemy(self.enemy)
            damage_messages.append(f"{self.player.name} inflicted {damage} damage!")
            print(f"{self.player.name} inflicted {damage} damage!")
            if self.enemy.is_alive():
                damage = self.enemy.attack_enemy(self.player)
                damage_messages.append(f"{self.enemy.name} inflicted {damage} damage!")
                print(f"{self.enemy.name} inflicted {damage} damage!")
        return self.player.is_alive(), self.enemy.is_alive()
