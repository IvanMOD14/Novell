screen combat_screen(players, enemies, background_image):
    frame:
        background background_image

    # Display enemy information and pictures at the top half of the screen
    hbox:
        yalign 0.02 xalign 0.5
        for enemy in enemies:
            vbox:
                frame:
                    background "frame_bg.png"
                    padding (150, -5)
                    xalign 0.5
                    vbox:
                        text "[enemy.name]"
                        text "HP: [enemy.hp] / [enemy.max_hp]"
                if enemy.is_alive:
                    hbox:
                        xalign 0.5
                        # Make the enemy image a clickable button
                        imagebutton:
                            idle enemy.picture
                            hover enemy.picture
                            action Function(attack_action, enemy)
    # Display player Fighter information at the bottom half of the screen
    hbox:
        yalign 0.69 xalign 0.5
        for player in players:
            $ frame_bg = player.frame_background
            frame:
                background frame_bg
                padding (200, -5)
                vbox:
                    text "[player.name]"
                    text "HP: [player.hp] / [player.max_hp]"
                    text "EP: [player.ep] / [player.max_ep]"