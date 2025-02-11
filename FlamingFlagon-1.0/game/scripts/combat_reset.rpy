init python:
    # Function to reset an enemy's state
    def reset_enemy(enemy):
        enemy.hp = enemy.max_hp
        enemy.ep = enemy.max_ep
        enemy.status_effects = []

    # Function to reset all enemies
    def reset_all_enemies(enemies_list):
        for enemy in enemies_list:
            reset_enemy(enemy)