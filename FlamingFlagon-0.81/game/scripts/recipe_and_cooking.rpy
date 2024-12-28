#Script for recipie and cooking texts

label cooking_animation:
    scene bg kitchen

    show transition cook 01
    with dissolve
    play sound "audio/Transition3.mp3" volume 1.0
    
    pause(3.0)

    hide transition cook 01
    with dissolve

    return


#Script for each recipie
label cooking_toast:

    show fen stern at left3
    show bg kitchen_blur

    stop music fadeout 2.0

    call show_cooking(
        ['toast_tomato','toast_lettuce'],
        ['toast_bread'],
        'dishes/bread09_03.png'
    ) from _call_show_cooking

    Fen "All we need is bread for making toast, and some fresh veggies to go with it..."

    Fen "Yep, tomato and lettuce should do."

    "To the right are ingredients you can pick from, click on them to add."

    "Here are where the ingredients will be added, click again to remove them."
    
    "Note that some ingredients will be pre-picked and can't be removed."

    "After you have added all wanted ingredients, press COOK to continue."

    call start_cooking() from _call_start_cooking

    if _return == 2:
        call cooking_animation from _call_cooking_animation

        pause

        Fen "Ta-da!! Toast Plate! Give it a try!"

        "You can hear the loud crunch of the crispy toast as Gunther takes a bite. His face starts to crack into a smile as he chews."

        Gunther "Mmm, you are right! It's simple, tasty, and perfectly crunchy. I approve."

        Fen "Nice, I'll work on expanding the menu from now on."

        Gunther "Heh, that's the spirit."

        "{color=#16f58d}{i}'Toast Plate' now added to Flaming Flagon menu!{/i}{/color}"

        "{color=#16f58d}{i}From now on, you'll have the ability to develop new dishes during your workdays.{/i}{/color}"

        "{color=#16f58d}{i}Dishes approved by Gunther will be added to the menu, and you can track your menu progress on the 'Recipe' page.{/i}{/color}"

        "{color=#16f58d}{i}Expanding the menu will advance the main story. Certain dishes will also attract more guests, unlocking additional characters.{/i}{/color}"

        jump taste_toast

    else:
        Fen "Wait, I didn't get it right. Let me try again."
        jump cooking_toast

label cooking_toast2:

    show fen stern at left3
    show bg kitchen_blur

    Fen "Sandwich can be nice additions to the menu, what combo of fillings should I use..."

    Fen "There's quite a selection of ingredients to pick."

    stop music fadeout 2.0

    call show_cooking(
        ['toast_egg','toast_butter'],
        ['toast_bread','toast_tomato','toast_lettuce'],
        'dishes/bread09_03.png'
    ) from _call_show_cooking_1

    Fen "What else do we have laying around?"

    Fen "I'll start with a fresh piece of toast, add tomato and lettuce, and next..."

    call start_cooking() from _call_start_cooking_1

    if _return == 12:
        call cooking_animation from _call_cooking_animation_1

        pause

        Fen "Butter Toast! Simply adding butter on top really does some magic."

        jump taste_bakedapple

    if _return == 32:
        call cooking_animation from _call_cooking_animation_2

        pause
            
        Fen "Sunny Toast! Butter fried egg with crispy edges and half soft yolk, perfect with toast!"

        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_3

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

    stop music fadeout 2.0

    call show_cooking(
        ['bakedapple_honey','bakedapple_hotpepper','bakedapple_mint','bakedapple_cinnamon','bakedapple_cream'],
        ['bakedapple_apple'],
        'dishes/apple01_01.png'
    ) from _call_show_cooking_2

    call start_cooking() from _call_start_cooking_2

    if _return == 5:
        call cooking_animation from _call_cooking_animation_4

        pause

        "Yep, this is exactly the stuff!"
        jump taste_bakedapple

    if _return <= 4 and _return >= 0:
        call cooking_animation from _call_cooking_animation_5

        pause
            
        "Hmmm, it's not bad, but not exactly what I remembered. Something is missing, I should give it another go."
        jump night_start

    if _return <= -1:
        call cooking_animation from _call_cooking_animation_6

        pause

        "Eh, the hot pepper does not fit in as I imagined, better leave it out next time."
        jump night_start

    if _return == 12:
        call cooking_animation from _call_cooking_animation_7

        pause

        "Nice, the cream topping also tastes very good with this sauce, it worked out well."
        jump taste_bakedapplecream

    if _return >= 13:
        call cooking_animation from _call_cooking_animation_8

        pause

        "Hmmm, it's not bad, but there are too many ingredients all fighting with each other."
        "Next time I better leave some ingredients off."
        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_9

        pause

        "Hmmm, it's not bad, but not exactly what I remembered. Something is missing, I should give it another go."
        jump night_start

label cooking_sandwich:

    show fen stern at left3
    show bg kitchen_blur
    with dissolve

    Fen "Sandwich can be nice additions to the menu, what combo of fillings should I use..."

    Fen "There's quite a selection of ingredients to pick."

    stop music fadeout 2.0

    call show_cooking(
        ['sandwich_cheese','sandwich_tomato','sandwich_avocado','sandwich_bacon','sandwich_shrimp'],
        ['sandwich_bread'],
        'dishes/sandwich01_01.png'
    ) from _call_show_cooking_3

    call start_cooking() from _call_start_cooking_3

    if _return == 42:
        call cooking_animation from _call_cooking_animation_10

        pause

        Fen "Ah yes, shrimp and avocado go together greatly."

        jump taste_shrimpsandwich
    
    if _return == 12:
        call cooking_animation from _call_cooking_animation_11

        pause

        Fen "Delicious, can't go wrong with a bacon sandwich."

        jump taste_baconsandwich

    if _return >= 50:
        call cooking_animation from _call_cooking_animation_12

        pause

        Fen "Ops, bacon and shrimp don't go too well together, I must pick one..."

        jump night_start

    if  _return <= 9:
        call cooking_animation from _call_cooking_animation_13

        pause

        Fen "It tastes fine but not quite satisfying, bacon or shrimp might be necessary..."

        jump night_start

    else:
        call cooking_animation from _call_cooking_animation_14

        pause

        Fen "Not quite the taste I'm looking for, I should try to add more fitting ingredients next time..."

        jump night_start

label cooking_bakedpotato:

    show fen stern at left3
    show bg kitchen_blur
    with dissolve

    Fen "Baked Potato, very simple and popular. I wonder why Gunther didn't have it on the menu..."

    stop music fadeout 2.0

    call show_cooking(
        ['bakedpotato_butter','bakedpotato_salt'],
        ['bakedpotato_potato'],
        'dishes/apple01_01.png'
    ) from _call_show_cooking_4

    call start_cooking() from _call_start_cooking_4

    if _return == 2:
        call cooking_animation from _call_cooking_animation_15

        pause

        Fen "Warm, filling and delicious, as baked potatoes should be."

        jump taste_bakedpotato

    else:
        call cooking_animation from _call_cooking_animation_16

        pause

        Fen "It's 'baked potato' for sure, but I can do something more with it..."

        jump night_start

label cooking_steak:

    show fen stern at left3
    show bg kitchen_blur
    with dissolve

    "Let's see... we have some good fresh meat, potato for side, and ingredients for seasonings..."

    "Gunther is going to love this."

    stop music fadeout 2.0

    call show_cooking(
        ['steak_saltpepper','steak_hotpepper','steak_garlic','steak_ginger','steak_rosemary'],
        ['steak_meat'],
        'dishes/apple01_01.png'
    ) from _call_show_cooking_5

    call start_cooking() from _call_start_cooking_5

    if _return >= 11:
        call cooking_animation from _call_cooking_animation_17

        pause

        "The perfect sear on the outside leaves distinct marks that accent the cooked meat. No doubt the inside is tender and juicy."
        
        "A mouthwatering aroma steams off the surface as some of the juice pools around the centerpiece of the plate."

        jump taste_steak

    if _return <= -1:
        call cooking_animation from _call_cooking_animation_18

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

    "You call Gunther over to taste the freshly baked apple."

    Gunther "I don't normally eat apples, but this is pretty good."
    
    Gunther "Simple and tasty, we can totally add these to the menu."

    Fen "Nice!"

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('bakedapple')
    $ set_recipe_success('bakedapple')
    "{color=#16f58d}{i}'Baked Apple' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_bakedapplecream:
    
    "You call Gunther over to taste the freshly baked apple."

    "You watch as he takes a big bite, then licks the cream from his lips clean."

    Gunther "The cream on top really takes this to another level."
    
    Gunther "Let's add this one to the menu, sweets lovers are going to love it."

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('bakedapplecream')
    $ set_recipe_success('bakedapplecream')
    "{color=#16f58d}{i}'Baked Apple & Cream' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_toastbutter:

    "You call Gunther over to taste the toast. As the tiger takes a big bite, you hear the satisfying crunch."

    Gunther "Whoa! And I thought the toast was simple and delicious. The butter is soaking into the hot toast, adding more to each bite."

    Gunther "Approved."

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('toastbutter')
    $ set_recipe_success('toastbutter')
    "{color=#16f58d}{i}'Butter Toast' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_toastegg:

    "You call Gunther over to taste the toast. As the tiger takes a big bite, you hear the satisfying crunch."

    "A few drops of soft egg yolk fall onto his beard, and with a quick lick, he cleans them up before continuing to devour the rest of the plate."

    Gunther "This is amazing, the egg is fried perfectly. The runny yolk adds savouriness to the whole thing. I want more."

    Fen "Heh, I take that as approval then."

    Fen "I'll have another plate ready in no time, but don't eat too much before dinner."

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('toastegg')
    $ set_recipe_success('toastegg')
    "{color=#16f58d}{i}'Sunny Toast' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_bakedpotato:

    "You call Gunther over to taste the freshly baked potato."

    Gunther "Oh wow, it's hot."

    "The tiger blows on the steaming potato a few times before attempting a bite."

    Gunther "Okay, it's pretty good!"

    Fen "I noticed it used to be on the menu, why'd you take it off?"

    Gunther "Well you see..."

    Gunther sweat "I'd get distracted serving at the bar and end up forgetting about them until I could smell them burning."

    Fen "Oh..."
    
    Fen "Well, I'll just be sure to take them out and wrap them in a towel so they'll stay hot."

    Gunther "That's a great idea!"

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('bakedpotato')
    $ set_recipe_success('bakedpotato')
    "{color=#16f58d}{i}'Baked Potato' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_steak:

    "You call Gunther over to taste the still hot steak."

    "Gunther cuts off a piece and takes a bite. His eyes go wide as his hands start cutting another piece."
    
    "The big cat devours two more bites before setting down the fork."

    Gunther "Oh man, you are good with meat, I can see this being a staple here."

    Fen "It really isn't that difficult. The meat is of decent quality, we just need a hot pan and a little bit of salt and pepper."

    Fen "Adding a bit of rosemary or garlic will enhance the flavor even more."

    Fen "The trick is to get the sear on the outside with high heat, and then use a lower heat to gently cook the inside."

    "Gunther devours the rest of the meat as you explain how the steaks are prepared."

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('steak')
    $ set_recipe_success('steak')
    "{color=#16f58d}{i}'Steak' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start

label taste_baconsandwich:

    "You call Gunther over to taste the sandwich as well. He grabs it with both hands and takes a large bite."

    Gunther "This is one of the most delicious sandwich I've ever tasted."

    Gunther "The smoky salty bacon is perfect in this sandwich. Put this on the menu now!"

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('baconsandwich')
    $ set_recipe_success('baconsandwich')
    "{color=#16f58d}{i}'Bacon Sandwich' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start


label taste_shrimpsandwich:

    "You call Gunther over to taste the sandwich as well. He grabs it with both hands and takes a large bite."

    Gunther "Mmm, I never would have thought to put shrimp on bread like that. This is super tasty."

    Gunther "I like it, let's put it on the menu."

    play sound "audio/bondexpup.wav" volume 2.0
    $ set_recipe_unlock('shrimpsandwich')
    $ set_recipe_success('shrimpsandwich')
    "{color=#16f58d}{i}'Shrimp Sandwich' now added to Flaming Flagon menu!{/i}{/color}"

    jump night_start


