init python:
    def player_turn(players, enemies):
        global combat_active
        # Example logic to check if combat should continue
        if not players or all(player.hp <= 0 for player in players):
            combat_active = False
            return  # Exit the function early if combat ends

        # Implement the rest of the player turn logic here

    def enemy_turn(enemies):
        global combat_active
        # Example logic to check if combat should continue
        if not enemies or all(enemy.hp <= 0 for enemy in enemies):
            combat_active = False
            return  # Exit the function early if combat ends

        # Implement the rest of the enemy turn logic here


define e = Character('Narrator')

label combat_loop:
    while combat_active:
        # Correctly show the combat screen with the current information and dynamic background
        $ renpy.show_screen("combat_screen", current_player_Fighters, current_enemies, background_image=combat_background)
        $ renpy.pause(0.5)  # Adjust the duration as needed

        $ player_turn(current_player_Fighters, current_enemies)
        "Player Turn"
        if combat_active:
            "Enemy Turn"
            $ enemy_turn(current_enemies)
        
        # Refresh the combat screen after player and enemy turns if their actions significantly change the game state
        $ renpy.show_screen("combat_screen", current_player_Fighters, current_enemies, background_image=combat_background)
        $ renpy.pause(0.5)  # Adjust the pause duration as needed.

        if combat_active:
            # Additional checks or operations
            pass
        
    $ renpy.hide_screen("combat_screen")
    "Combat has ended."
    return

label end_combat:
    python:
        reset_all_enemies(current_enemies)
    "The battle is over. All enemies have been reset."
    return