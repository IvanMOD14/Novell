init python:
    def attack_action(enemy):
        if enemy.is_alive:
            # Example damage calculation
            damage = 20  # Placeholder damage value
            enemy.hp -= damage
            if enemy.hp <= 0:
                enemy.hp = 0
                # Handle enemy defeat logic here
            # Update the combat state as needed