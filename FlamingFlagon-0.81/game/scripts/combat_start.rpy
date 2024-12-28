label combat_start(encounter_type="regular"):
    $ combat_active = True
    if encounter_type == "sneak_attack":
        $ player_turn(current_player_Fighters, current_enemies)
    elif encounter_type == "ambush":
        $ enemy_turn(current_enemies)
    call combat_loop from _call_combat_loop
    return