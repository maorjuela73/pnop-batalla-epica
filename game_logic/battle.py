class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print(f"Comienza la batalla: {self.player.name} vs {self.enemy.name}")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack_enemy(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack_enemy(self.player)

        if self.player.is_alive():
            print(f"{self.player.name} ha ganado la batalla.")
        else:
            print(f"{self.enemy.name} ha ganado la batalla.")
