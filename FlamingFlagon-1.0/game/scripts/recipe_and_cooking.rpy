#Flags
default cooking_start_menu_done = False
default cooking_unlock_bakedapple_done = False
default cooking_unlock_peasoup_done = False


#Menu for choose recipies

label cooking_start_menu:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    #Add events here
    if cooking_start_menu_done == False:
        $ cooking_start_menu_done = True

        Fen "Hmmm... Let's start by cooking some simple dishes."

        $ set_recipe_unlock('toastbutter')
        $ set_recipe_unlock('toastegg')
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}'Toast' recipe now avilable for develop!{/i}{/color}"

        $ set_recipe_unlock('bakedpotato')
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}'Baked Potato' recipe now avilable for develop!{/i}{/color}"

        $ set_recipe_unlock('steak')
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}'Steak' recipe now avilable for develop!{/i}{/color}"

        $ set_recipe_unlock('baconsandwich')
        $ set_recipe_unlock('shrimpsandwich')
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}'Sandwich' recipe now avilable for develop!{/i}{/color}"
        
    
    else:
        pass

    if bond02 >= 3 and cooking_unlock_bakedapple_done == False:
        $   cooking_unlock_bakedapple_done = True

        Fen "That baked apple I made for Terrance, maybe I can add that to the menu too."

        $ set_recipe_unlock('bakedapple')
        $ set_recipe_unlock('bakedapplecream')
        $ show_chooserecipe_option('cookingbakedapple')
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}'Baked Apple' recipe now avilable for develop!{/i}{/color}"

    else:
        pass

    Fen "Now, what should i cook today?"

    call chooserecipe_entry(_("I choose...")) from _call_chooserecipe_entry
    if _return == 'cookingbakedapple':
        jump cooking_bakedapple
    if _return == 'cookingtoast2':
        jump cooking_toast2
    if _return == 'cookingsandwich':
        jump cooking_sandwich
    if _return == 'cookingbakedpotato':
        jump cooking_bakedpotato
    if _return == 'cookingsteak':
        jump cooking_steak
    if _return == 'cookingnone':
        jump night_start

    jump day_end




#Script for recipie and cooking texts

label cooking_animation:
    stop music fadeout 2.0
    scene bg kitchen_blur
    with vq_dissolve

    play sound "audio/Transition3.ogg" volume 1.0

    show transition cook 01
    with vq_dissolve
    
    pause(4.0)

    hide transition cook 01
    with dissolve

    return


#Script for each recipie
label cooking_toast:

    show fen normal at left3
    hide gunther
    show bg kitchen_blur
    with dissolve

    stop music fadeout 2.0
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0

    call show_cooking(
        ['toast_tomato','toast_lettuce'],
        ['toast_bread'],
        'dishes/bread09_03.png'
    ) from _call_show_cooking

    Fen "All we need is bread for making toast, and some fresh veggies to go with it..."

    Fen "Yep, tomato and lettuce should do."

    "{color=#16f58d}{i}To the right are ingredients you can pick from, click on them to add.{/i}{/color}"

    "{color=#16f58d}{i}Here in center are where the ingredients will be added, click again to remove them.{/i}{/color}"
    
    "{color=#16f58d}{i}Note that some ingredients will be pre-picked and can't be removed.{/i}{/color}"

    "{color=#16f58d}{i}After you have added all wanted ingredients, press COOK to continue.{/i}{/color}"

    call start_cooking() from _call_start_cooking

    if _return == 2:
        call cooking_animation from _call_cooking_animation

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show bread09_03 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        scene bg kitchen_blur
        show fen smile at left1
        show gunther normal at right1
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        with dissolve
        Fen "Ta-da!! Toast Plate! Give it a try!"

        #Crisp sound
        play sound "audio/crunch.ogg" volume 2.0
        show gunther stern2
        "You can hear the loud crunch of the crispy toast as Gunther takes a bite."
        
        show gunther smile with q_dissolve
        "His face starts to crack into a smile as he chews."

        Gunther grin "Mmm, you are right! It's simple, tasty, and perfectly crunchy. I approve."

        Fen normal "Nice, I'll work on expanding the menu from now on."

        Gunther smile2 "Heh, that's the spirit."

        $ show_recipe_button = True
        $ set_recipe_unlock('vegetablesoup')
        $ set_recipe_success('vegetablesoup')
        $ set_recipe_unlock('toast')
        $ set_recipe_success('toast')
        "{color=#16f58d}{i}'Toast Plate' now added to Flaming Flagon menu!{/i}{/color}"

        "{color=#16f58d}{i}From now on, you'll have the ability to develop new dishes during your workdays.{/i}{/color}"

        "{color=#16f58d}{i}Dishes approved by Gunther will be added to the menu, and you can track your menu progress on the 'Recipe' page.{/i}{/color}"

        "{color=#16f58d}{i}Expanding the menu will advance the main story. Certain dishes will also attract more guests, unlocking additional characters.{/i}{/color}"

        jump night_start

    else:
        Fen stern "Wait, I didn't get it right. Let me try again."
        jump cooking_toast

label cooking_toast2:

    show fen stern at left3
    show bg kitchen_blur

    Fen "That toast recipe... I think I can improve it a bit."

    Fen "What else do we have laying around?"

    Fen normal "I'll start with a fresh piece of toast, add tomato and lettuce, and next..."

    call show_cooking(
        ['toast_egg','toast_butter'],
        ['toast_bread','toast_tomato','toast_lettuce'],
        'dishes/bread09_03.png'
    ) from _call_show_cooking_1

    call start_cooking() from _call_start_cooking_1

    if _return == 12:
        call cooking_animation from _call_cooking_animation_1

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show bread09_02 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Butter Toast! Simply adding butter on top really does some magic."

        jump taste_toastbutter

    if _return == 32:
        call cooking_animation from _call_cooking_animation_2

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show bread09_01 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause
            
        Fen "Sunny Toast! Butter fried egg with crispy edges and half soft yolk, perfect with toast!"

        jump taste_toastegg

    else:
        call cooking_animation from _call_cooking_animation_3

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Yep, it's the same old toast plate. I should try to add something to it."

        jump night_start

label cooking_bakedapple:
    
    show fen stern at left3
    show bg kitchen_blur
    with dissolve
    Fen "I used apple and honey, what else did I use?"

    Fen "It might also be a good idea to change it up a bit. Hmm..."

    show fen normal at shock
    Fen "Anyway, let's start!"

    call show_cooking(
        ['bakedapple_honey','bakedapple_hotpepper','bakedapple_mint','bakedapple_cinnamon','bakedapple_cream'],
        ['bakedapple_apple'],
        'dishes/apple01_01.png'
    ) from _call_show_cooking_2

    call start_cooking() from _call_start_cooking_2

    if _return == 5:
        call cooking_animation from _call_cooking_animation_4

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show apple01_01 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Yep, this is exactly the stuff!"
        jump taste_bakedapple

    if _return <= 4 and _return >= 0:
        call cooking_animation from _call_cooking_animation_5

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause
            
        Fen "Hmmm, it's not bad, but not exactly what I remembered. Something is missing, I should give it another go."
        jump night_start

    if _return <= -1:
        call cooking_animation from _call_cooking_animation_6

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Eh, the hot pepper does not fit in as I imagined, better leave it out next time."
        jump night_start

    if _return == 12:
        call cooking_animation from _call_cooking_animation_7

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show apple01_02 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Nice, the cream topping also tastes very good with this sauce, it worked out well."
        jump taste_bakedapplecream

    if _return >= 13:
        call cooking_animation from _call_cooking_animation_8

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Hmmm, it's not bad, but there are too many ingredients all fighting with each other."
        Fen "Next time I better leave some ingredients off."
        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_9

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Hmmm, it's not bad, but not exactly what I remembered. Something is missing, I should give it another go."
        jump night_start

label cooking_sandwich:

    show fen normal at left3
    show bg kitchen_blur
    with dissolve

    Fen normal "Sandwich can be nice additions to the menu, what combo of fillings should I use..."

    Fen "There's quite a selection of ingredients to pick."

    call show_cooking(
        ['sandwich_cheese','sandwich_tomato','sandwich_avocado','sandwich_bacon','sandwich_shrimp'],
        ['sandwich_bread'],
        'dishes/sandwich01_01.png'
    ) from _call_show_cooking_3

    call start_cooking() from _call_start_cooking_3

    if _return == 47:
        call cooking_animation from _call_cooking_animation_10

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show sandwich01_02 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Ah yes, shrimp and avocado go together greatly."

        jump taste_shrimpsandwich
    
    if _return == 32:
        call cooking_animation from _call_cooking_animation_11

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show sandwich01_01 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Delicious, can't go wrong with a bacon sandwich."

        jump taste_baconsandwich

    if _return >= 55:
        call cooking_animation from _call_cooking_animation_12

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Ops, bacon and shrimp don't go too well together, I must pick one..."

        jump night_start

    if  _return <= 24:
        call cooking_animation from _call_cooking_animation_13

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "It tastes fine but not quite satisfying, bacon or shrimp might be necessary..."

        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_14

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "Not quite the taste I'm looking for, I should try to add more fitting ingredients next time..."

        jump night_start

label cooking_bakedpotato:

    show fen stern at left3
    show bg kitchen_blur
    with dissolve

    Fen "Baked Potato, very simple and popular. I wonder why Gunther didn't have it on the menu..."

    call show_cooking(
        ['bakedpotato_butter','bakedpotato_salt'],
        ['bakedpotato_potato'],
        'dishes/potato01_01.png'
    ) from _call_show_cooking_4

    call start_cooking() from _call_start_cooking_4

    if _return == 2:
        call cooking_animation from _call_cooking_animation_15

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show potato01_01 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        Fen "Warm, filling and delicious, as baked potatoes should be."

        jump taste_bakedpotato

    else:
        call cooking_animation from _call_cooking_animation_16

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        Fen "It's 'baked potato' for sure, but I can do something more with it..."

        jump night_start

label cooking_steak:

    show fen stern at left3
    show bg kitchen_blur
    with dissolve

    Fen normal "Let's see... we have some good fresh meat, potato for side, and ingredients for seasonings..."

    Fen smile "Gunther is going to love this."

    call show_cooking(
        ['steak_saltpepper','steak_hotpepper','steak_garlic','steak_ginger','steak_rosemary'],
        ['steak_meat'],
        'dishes/steak04_01.png'
    ) from _call_show_cooking_5

    call start_cooking() from _call_start_cooking_5

    if _return >= 11:
        call cooking_animation from _call_cooking_animation_17

        play sound "audio/cooking/ding.ogg" volume 2.0
        show ray at truecenter
        show steak04_01 at truecenter:
            zoom 2
        show sparkle animation 01:
            zoom 1
            ypos 100
            xpos 200
        show sparkle animation 01 as sparkle01:
            zoom 0.5
            ypos 420
            xpos 1600
        show sparkle animation 01 as sparkle02:
            zoom 1
            ypos 700
            xpos 1200
        show sparkle animation 01 as sparkle03:
            zoom 0.6
            ypos 850
            xpos 1450
        show sparkle animation 01 as sparkle04:
            zoom 0.8
            ypos 500
            xpos 150
        show sparkle animation 01 as sparkle05:
            zoom 0.4
            ypos 300
            xpos 350
        show sparkle animation 01 as sparkle06:
            zoom 0.7
            ypos 50
            xpos 1050
        show sparkle animation 01 as sparkle07:
            zoom 0.4
            ypos 850
            xpos 650
        with dissolve

        pause

        "'Steak' is done!"

        "The perfect sear on the outside leaves distinct marks that accent the cooked meat. No doubt the inside is tender and juicy."
        
        "A mouthwatering aroma steams off the surface as some of the juice pools around the centerpiece of the plate."

        jump taste_steak

    if _return <= -1:
        call cooking_animation from _call_cooking_animation_18

        play sound "audio/cooking/ding.ogg" volume 2.0

        pause

        "The steak is nice and tender, but the seasoning is too much, making it hard to taste the meat."

        Fen "I can do better. I should try again."

        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_19

        pause

        "The steak is nice and tender, but you feel like there is a lack of seasoning or sides."

        Fen "I can do better. I should try again."

        jump night_start


#Gunther taste dishes
label taste_bakedapple:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the freshly baked apple."

    show gunther stern2
    "You watch as he takes a big bite."

    Gunther stern "I don't normally eat apples, but this is pretty good."
    
    Gunther normal "Simple and tasty, we can totally add these to the menu."

    show fen smile at shock
    Fen "Nice!"

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('bakedapple')
    "{color=#16f58d}{i}'Baked Apple' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_bakedapplecream:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the freshly baked apple."

    show gunther stern2
    "You watch as he takes a big bite, then licks the cream from his lips clean."

    Gunther stern "Hmm... The cream on top really takes this to another level."
    
    Gunther normal "Let's add this one to the menu, sweets lovers are going to love it."

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('bakedapplecream')
    "{color=#16f58d}{i}'Baked Apple & Cream' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_toastbutter:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the toast."
    
    play sound "audio/crunch.ogg" volume 2.0
    show gunther stern2
    "As the tiger takes a big bite, you hear the satisfying crunch."

    Gunther grin "Whoa! And I thought the toast was simple and delicious. The butter is soaking into the hot toast, adding more to each bite."

    Gunther smile "Approved."

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('toastbutter')
    "{color=#16f58d}{i}'Butter Toast' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_toastegg:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the toast."
    
    play sound "audio/crunch.ogg" volume 2.0
    show gunther stern2
    "As the tiger takes a big bite, you hear the satisfying crunch."

    "A few drops of soft egg yolk fall onto his beard, and with a quick lick, he cleans them up before continuing to devour the rest of the plate."

    Gunther grin "This is amazing, the egg is fried perfectly. The runny yolk adds savouriness to the whole thing. I want more."

    Fen smile "Heh, I take that as approval then."

    Fen normal "I'll have another plate ready in no time, but don't eat too much before dinner."

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('toastegg')
    "{color=#16f58d}{i}'Sunny Toast' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_bakedpotato:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the freshly baked potato."

    show gunther stern at shock
    Gunther stern "Oh wow, it's hot."

    show gunther stern2
    "The tiger blows on the steaming potato a few times before attempting a bite."

    Gunther smile "Okay, it's pretty good!"

    Fen stern "I noticed it used to be on the menu, why'd you take it off?"

    Gunther stern "Well you see..."

    Gunther sweat "I'd get distracted serving at the bar and end up forgetting about them until I could smell them burning."

    Fen "Oh..."
    
    Fen normal "Well, I'll just be sure to take them out and wrap them in a towel so they'll stay hot."

    Gunther smile "That's a great idea!"

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('bakedpotato')
    "{color=#16f58d}{i}'Baked Potato' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_steak:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the still hot steak."

    show gunther stern2
    "Gunther cuts off a piece and takes a bite."
    
    show gunther stern
    "His eyes go wide as his hands start cutting another piece."
    
    show gunther smile
    "The big cat devours two more bites before setting down the fork."

    Gunther normal "Oh man, you are good with meat, I can see this being a staple here."

    Fen "It really isn't that difficult. The meat is of decent quality, we just need a hot pan and a little bit of salt and pepper."

    Fen lick "Adding a bit of rosemary or garlic will enhance the flavor even more."

    Fen normal "The trick is to get the sear on the outside with high heat, and then use a lower heat to gently cook the inside."

    show gunther smile
    "Gunther devours the rest of the meat as you explain how the steaks are prepared."

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('steak')
    "{color=#16f58d}{i}'Steak' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_baconsandwich:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the sandwich as well."
    
    show gunther stern2
    "He grabs it with both hands and takes a large bite."

    Gunther grin "This is one of the most delicious sandwich I've ever tasted."

    Gunther smile "The smoky salty bacon is perfect in this sandwich. Put this on the menu now!"

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('baconsandwich')
    "{color=#16f58d}{i}'Bacon Sandwich' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_shrimpsandwich:
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen_blur
    show fen normal at left1
    show gunther normal at right1
    with dissolve
    "You call Gunther over to taste the sandwich as well."

    show gunther stern2
    "He grabs it with both hands and takes a large bite."

    Gunther "Mmm, I never would have thought to put shrimp on bread like that. This is super tasty."

    Gunther smile "I like it, let's put it on the menu."

    play sound "audio/bondexpup.ogg" volume 2.0
    $ set_recipe_success('shrimpsandwich')
    "{color=#16f58d}{i}'Shrimp Sandwich' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start


