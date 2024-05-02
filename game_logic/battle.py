class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def perform_turn(self):
        if self.player.is_alive() and self.enemy.is_alive():
            self.player.attack_enemy(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack_enemy(self.player)
        return self.player.is_alive(), self.enemy.is_alive()
