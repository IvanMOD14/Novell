default max_ap = 2
default ap = 2

default day_count = 0
default work_day_count = 0

default fen_coins = 0
default fen_payment = 10
default murry_payment = 10

default personal_service = False

#Events
default first_freeday_done = False
default first_workday_done = False
default first_cooking_done = False
default first_workend_done = False
default first_workpay_done = False
default first_day_activity_done = False
default first_backyard_gunther = False
default first_market_done = False
default first_market_murry = False
default first_bathhouse_luxury = False
default first_bathhouse_intro = False
default first_marcus_serve = False
default first_khaleb_serve = False
default niall_bond_02pre_done = False

#List of Trigger Events
default first_gunther_taketo_bathhouse = False
default terrance_bond02_done = False
default gunther_bond_02_first = False
default odachi_event_01_first = False
default odachi_bond_02_first = False

default relicshop_open = False

#Main story progression

default raise_01_done = False

#Day cicle

label day_start:
    scene bg black
    with s_dissolve

    centered "-Next day-"
    with s_dissolve
    #morning animation

    #Add events here

    if niall_bond_02pre_done == False and bond04 == 1 and bondexp04 >= 5:
        $ niall_bond_02pre_done = True
        jump niall_bond_02pre
    
    else:
        pass

    scene bg fenroom
    with s_dissolve

    play sound "audio/birds.ogg" volume 3.0
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0

    $ day_start_text = renpy.random.choice(['1', '2','3','4'])

    if day_start_text == '1':
        "The morning sun shines upon your face."

        "Ready or not, it's time to start the day."

    if day_start_text == '2':
        "The morning sun shining down on your face is rather annoying this morning."
        
        "Grunting, you force yourself to get up and start the day."

    if day_start_text == '3':

        "You hardly got any sleep at all so are groggy and a bit cranky when you get up."
        
        "Time to start the day."

    if day_start_text == '4':

        "As daylight emerges, it's time to embrace the start of a fresh day."

    #if event_trigger = true
    #else pass
    #Do this for all trigger events, in the order of from top to down 

    jump day_activity


label night_start:
    #sunset animation

    stop music fadeout 3.0

    scene bg kitchen_night1
    with s_dissolve
    "Before you know it, the sun has set."

    "After having dinner together, you and Gunther are ready to start the evening at the tavern."

    jump work_start

label day_end:
    scene bg black
    with s_dissolve
    stop music fadeout 3.0

    #Things that need reset
    $ already_masturbated = False

    pause

    $_dismiss_pause = False
    
    #IF and Else Pass here for every dream Fen is going to have
    scene bg fenroom_night
    with s_dissolve

    $ day_end_text = renpy.random.choice(['1', '2','3','4'])

    if day_end_text == '1':
        "It's getting late, after a brief wash, you climb into your bed."
    
    if day_end_text == '2':
        "After the long day, you feel so tired you immediately pass out as soon as you get into your bed."

    if day_end_text == '3':
        "You decide to have some drinks tonight as a treat. Once done, you feel refreshed and relaxed. Climbing into bed you fall asleep almost at once."

    if day_end_text == '4':
        "You don't feel particularly tired, so you end up staring at the ceiling wondering about all sorts of things before finally falling asleep."

    scene bg black
    with s_dissolve

    show transition sleep 01
    with s_dissolve
    play sound "audio/Transition1.ogg" volume 1.0
    
    pause(3.0)

    $_dismiss_pause = True

    #fen sleep animation
    if work_day_count == 3:
        $ work_day_count = 0
        jump free_day

    else:
        jump day_start

label free_day:
    #day count
    $ day_count += 1
    #events here
    
    if bond02 == 2 and terrance_bond_03pre_done == True:
        jump terrance_bond_03
    
    else:
        pass

    scene bg black
    with s_dissolve

    centered "-Next day-"
    with s_dissolve

    play sound "audio/birds.ogg" volume 3.0
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    scene bg fenroom
    with s_dissolve
    #morning animation

    "The morning sun shines upon your face."

    #events here
    if day_count >= 12 and first_gunther_taketo_bathhouse == False:

        $ first_gunther_taketo_bathhouse = True

        scene bg kitchen
        with s_dissolve

        jump gunther_event_03
    
    else:
        pass

    scene bg kitchen
    with s_dissolve 
    "After a relaxing breakfast, you are ready for the day."

    if bond03 >= 2:
        $ show_freeday_option('go to tailservice')

    else:
        pass

    if first_freeday_done == False:

        "{color=#16f58d}{i}During the days you are off work, you can go other places.{/i}{/color}"

        "{color=#16f58d}{i}Some characters are not guests in the tavern, so it's a good opportunity to pay a visit.{/i}{/color}"

        $ first_freeday_done = True
    
    else:
        pass

    show fen 2 normal at left1
    show bg kitchen_blur
    with dissolve

label freeday_acts:

    #Checks for open and close options
    if bond02 >= 3:
        $ show_freeday_option('go to village')

    else:
        pass

    call freeday_entry(_("Where should I go?")) from _call_freeday_entry
    if _return == 'go to market':
        jump market
    if _return == 'go to backyard':
        jump backyard_gunther
    if _return == 'go to room':
        jump my_room
    if _return == 'go to bathhouse':
        jump bathhouse
    if _return == 'go to tailservice':
        jump fen_tailservice_00
    if _return == 'go to village':
        jump mjolnik_home
    jump day_end


label day_activity:
    if terrance_bond02_done == False and bond02 == 1 and bondexp02 >= 10:
        jump terrance_bond_02

    else:
        pass


    if first_day_activity_done == False:
        $ first_day_activity_done = True

        show gunther normal at right1
        show bg fenroom_blur
        with dissolve
        Gunther "Hey! Get up, sleepy head!"

        Fen "Mmm, I'm up."

        "You rub the sleep from your eyes to see your boss standing at your bedroom door."

        Gunther wink "'Atta boy."

        Gunther normal "Now get dressed and help me clean up."

        Fen "I'm going, I'm going."

        "You push yourself out of bed and start your day."

        jump gunther_event_01

    label day_activity_menu:
        menu:
            Fen "What to do now."

            "Help Gunther with cleaning":
                jump gunther_event_01

            "Lunch service" if day_count >= 5:
                jump lunch_service
            
            "Develop recipes" if day_count >= 2:

                #$ disable_back = True
                
                

                #jump day_activity_menu

                if first_cooking_done == False:
                    $ first_cooking_done = True
                    jump gunther_unlockcooking
                
                else:
                    stop music fadeout 3.0
                    scene bg kitchen
                    with s_dissolve
                    "After completing your usual kitchen duties, you finally have some time to experiment with new recipes."

                    scene bg kitchen_blur
                    show fen normal at left3
                    with dissolve
                    jump cooking_start_menu

                #$ show_recipe_button = True

                #jump cooking_bakedapple

    jump night_start

label work_start:
    if first_workday_done == False:
        scene bg fenroom
        with s_dissolve
        "You gather your now dry clothes and change into your work uniform."

        show bg kitchen
        with dissolve
        "Once dressed, you head downstairs to see Gunther setting down a box of new plates."

        show gunther normal at right1
        show bg kitchen_blur
        with dissolve
        Gunther "Help me with these last two boxes."

        show fen normal at left1
        with dissolve
        Fen "Sure."

        #they head outside
        scene bg tavernback
        with s_dissolve
        "You follows Gunther to the backyard."

        show terrance normal at right1
        show bg tavernback_blur
        with dissolve
        Terrance "Hi [name]."

        "The big horse greets you as he sets down a couple of boxes beside his cart." with vpunch

        Terrance smile "Gotta finish one more delivery, fare well."

        show fen smile at left1
        with dissolve
        Fen "Bye Terrance."

        hide terrance
        hide fen
        show bg tavernback
        with dissolve
        "You have only a moment to wave at the stallion as he trots off."

        show bg kitchen
        with dissolve
        "Gunther and you return to the kitchen with your boxes and quickly put everything away."

        show bg kitchen_night1
        with dissolve
        stop music fadeout 3.0
        "You spend the rest of afternoon preparing soup for the evening."

        scene bg tavern1
        with s_dissolve
        play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0

        show gunther normal at center1
        show bg tavern1_blur
        with dissolve
        Gunther "Alright, that's it. Time to open."

        Gunther "Customers will start coming in. I'm sure you'll see some familiar faces and probably some new ones too."

        Gunther wink "But don't be shy. Get out there and introduce yourself. People love new faces."

        hide gunther
        show bg tavern1
        with dissolve
        "{color=#16f58d}{i}You are starting your nightly shift at The Flaming Flagon.{/i}{/color}"

        "{color=#16f58d}{i}Every night, new and old faces will show up on the right side of the screen.{/i}{/color}"

        "{color=#16f58d}{i}[name] is limited by his action points for how many interactions he's allowed during a single shift.{/i}{/color}"

        "{color=#16f58d}{i}Interactions can increase your bond with the character. Max Bond levels will increase for some characters as the game gets updated.{/i}{/color}"

        "{color=#16f58d}{i}[name]'s action points can increase through story events and items.{/i}{/color}"

        show gunther normal at right1
        show bg tavern1_blur
        show fen normal at left1
        with dissolve
        Gunther "I can handle the bar. Now get out there and take some orders."

        show fen smile
        Fen "Yes boss!"

        Gunther blush "I told ya, you don't have to call me that..."

        Fen blush "Sorry, I guess it just feels natural."

        #perhaps hint to Fen calling his dad "Boss" when they worked

        $ ap = 2
        $ max_ap = 2

        scene bg tavern1
        with s_dissolve
        
        stop music fadeout 3.0
        "As Gunther opens the Flaming Flagon for the night, the guests start to take their seats."

        $ first_workday_done = True

        jump work
    
    else:
        pass

    scene bg tavern1
    with s_dissolve

    #Lean new work option, happens befor bathhouse
    if personal_service == False and day_count >= 8:
        jump unlock_personal_service

    else:
        pass


    show gunther normal at center1
    show bg tavern1_blur
    with dissolve
    Gunther "It's about time, get ready!"

    "As Gunther opens the Flaming Flagon for the night, the guests start to take their seats."

    jump work



label work:

    play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0

    if ap == 0:
        jump work_end
    
    else:
        pass

    scene bg tavern1_blur
    show fen normal at left1
    with dissolve

    label work_menu:
        call workday_entry(_("Who to serve?                                                      Action Points left {b}[ap]/[max_ap]{/b}")) from _call_workday_entry
        if _return == 'terrance_meet_option':
            jump terrance_intro
        if _return == 'terrance_work_option':
            jump serve_terrance
        if _return == 'odachi_meet_option':
            jump odachi_intro
        if _return == 'odachi_work_option':
            jump serve_odachi
        if _return == 'niall_meet_option':
            jump niall_intro
        if _return == 'niall_work_option':
            jump serve_niall
        if _return == 'marcus_work_option':
            jump serve_marcus
        if _return == 'khaleb_work_option':
            jump serve_khaleb

        "[_return]"

label work_end:
    $ work_day_count += 1
    $ day_count += 1
    $ ap += max_ap
            
    if work_day_count == 3:
        jump work_end_free

    else:
        jump work_end_normal

label work_end_normal:
    if first_workend_done == False:
        scene bg tavern1
        with s_dissolve
        "It's closing time. The last wave of customers have taken their leave."

        show gunther normal at center1
        show bg tavern1_blur
        with dissolve
        Gunther "That wasn't so bad, right?"

        "It was not easy, but you feel you are getting better at it."

        Gunther smile "Keep it up, you will get handy at it in no time."

        $ first_workend_done = True
        $ max_ap += 1
        $ ap += 1

        "{color=#16f58d}{i}Max Action Point increased!{/i}{/color}"

        jump day_end

    else:
        pass

    if day_count >= 16:
        if bondexp01 >= 20:
            if gunther_bond_02_first == False:
                $ gunther_bond_02_first = True
                jump gunther_bond_02

            else:
                pass

        else:
            pass

    else:
        pass

    scene bg tavern2
    with s_dissolve
    "It's closing time. The last wave of customers have taken their leave."

    show gunther smile2 at center1
    show bg tavern2_blur
    with dissolve
    Gunther "We are done for today. Good job, cub."

    jump day_end

label work_end_free:
    #Events
    if get_success_recipe_count() >= 5 and raise_01_done == False:
        $ raise_01_done = True

        jump raise_01
    
    else:
        pass

    if first_workpay_done == False:
        $ first_workpay_done = True

        scene bg tavern2
        with s_dissolve
        "It's closing time. The last wave of customers have taken their leave."

        show gunther normal at right1
        show bg tavern2_blur
        with dissolve
        Gunther "It's been a few days of work now. How are you feeling?"

        show fen normal at left1
        with dissolve
        Fen "I think I'm getting the hang of things."

        Gunther smile "Great, I'm gonna give you the day off tomorrow."

        Fen smile "Thanks."

        Gunther normal "Oh, also here's your payment."

        Fen normal "Payment?"

        Gunther "Yes, word of your food is already going around town. We're getting more business so that means more money."

        $ fen_coins += 10
        play sound "audio/payment.ogg" volume 3.0
        show gunther at right2
        with dissolve
        "The tiger hands you a small stack of ten coins."

        show gunther at right1
        with dissolve

        menu:
            "Ten coins?":
                jump thats_it

            "Ten coins!":
                jump thankful_fen

        label thats_it:
            Fen stern "Oh, that's it?"

            Gunther stern "Hey cub, your room and food come out of that too."

            Fen "Yes, of course..."

            Fen normal "Thank you, Gunther."

            jump payment_cont

        label thankful_fen:

            show fen smile at shock
            Fen "Oh wow, ten coins!"

            Gunther smile2 "And I'm sure as your skills improve and business continues to pick up, I'll be able to pay you more."

            Fen normal "Thank you... for everything."

            Gunther normal "Aww, don't mention it."

            jump payment_cont

        label payment_cont:

            Gunther normal "I'll pay you every three days. Make good use of them."

            Fen "Yes, I will continue to do my best."

            stop music fadeout 3.0
            Gunther wink "I know you will, cub. Enjoy your day off tomorrow."

            hide fen
            hide gunther
            show bg tavern2
            with dissolve

            call bondlvup0101 from _call_bondlvup0101

            jump day_end

    else:
        pass

    scene bg tavern2
    with s_dissolve
    "It's closing time. The last wave of customers have taken their leave."

    show gunther normal at center1
    show bg tavern2_blur
    with dissolve
    Gunther "Good job. Here's your share."

    $ fen_coins += fen_payment
    play sound "audio/payment.ogg" volume 3.0
    "Gunther hands over [fen_payment] coins."

    Gunther smile2 "Have a good day tomorrow."

    jump day_end

#Work day events labels
label serve_terrance:

    #IF events here
    
    if bond02 == 0:
        if bondexp02 >= 3:
            jump terrance_bond_01

        else:
            pass
    
    else:
        pass

    if bond02 == 2 and bondexp02 >= 20 and terrance_bond_03pre_done == False:
            jump terrance_bond_03pre

    else:
        pass
    


    label serve_terrance_menu:
        menu:
            "You are now serving Terrance."

            "Serve":
                jump terrance_serve_01

            "Chat":
                jump terrance_talk_01

            "Attentive Service" if personal_service == True and bond02 >= 1:
                jump terrance_personal_01


label serve_odachi:

    #IF events here
    if bond03 == 0:
        if bondexp03 >= 3:
            jump odachi_bond_01

        else:
            pass
    
    else:
        pass

    if bond03 == 1:
        if day_count >= 3 and odachi_event_01_first == False:
            $ odachi_event_01_first = True
            jump odachi_event_01

        else:
            pass
    
    else:
        pass

    if bond03 == 1 and bondexp03 >= 10:
        if day_count >= 5 and odachi_bond_02_first == False:
            $ odachi_bond_02_first = True
            jump odachi_bond_02

        else:
            pass
    
    else:
        pass

    if bond03 == 1 and bondexp03 >= 10:
        if day_count >= 6 and odachi_bond_02_done == True:
            jump odachi_bond_02b

        else:
            pass
    
    else:
        pass

    label serve_odachi_menu:
        menu:
            "You are now serving Odachi."

            "Serve":
                jump odachi_serve_01
                return

            "Chat":
                jump odachi_talk_01

            "Attentive Service" if personal_service == True and bond03 >= 1:
                jump odachi_personal_01

label serve_niall:

    #IF events here
    if bond04 == 0:
        if bondexp04 >= 3:
            jump niall_bond_01

        else:
            pass
    
    else:
        pass
    
    if bond04 == 1 and bondexp04 >= 10 and work_day_count <= 2 and niall_bond_02pre_done == True:
        jump niall_bond_02    
    else:
        pass

    label serve_niall_menu:
        menu:
            "You are now serving Niall."

            "Serve":
                jump niall_serve_01
                return

            "Chat":
                jump niall_talk_01

            "Attentive Service" if personal_service == True and bond04 >= 1:
                jump niall_personal_01


label serve_marcus:
    #IF events here

    if first_marcus_serve == False:

        $ first_marcus_serve = True
        jump marcus_bond_01

    else:
        pass  

    label serve_marcus_menu:
        menu:
            "You are now serving Marcus."

            "Serve":
                jump marcus_serve_01
                return

            "Chat":
                jump marcus_talk_02

            "Attentive Service" if personal_service == True and bond06 >= 1:
                jump marcus_personal_01

label serve_khaleb:
    if bondexp07 >= 10 and bond07 == 0:
        jump khaleb_bond_01

    else:
        pass
    #IF events here

    if first_khaleb_serve == False:

        $ first_khaleb_serve = True
        jump khaleb_event_01

    else:
        pass  

    label serve_khaleb_menu:
        menu:
            "You are now serving Khaleb and co."

            "Serve":
                jump khaleb_serve_01

            "Chat":
                jump khaleb_talk_01

            "Attentive Service" if personal_service == True and bond07 >= 1:
                jump khaleb_personal_01


#label for locations

label my_room:
    scene bg fenroom
    with s_dissolve

    label my_room_menu:
        menu:
            "Rest":
                jump fen_rest_01

            "Take care of some urges...":
                if already_masturbated == True:
                    "That was enough for now..."

                    jump my_room_menu
                
                else:
                    if fen_masturbate_count >= 1:
                        if bond01 >= 2:
                            if fen_masturbate_02_first == False:
                                jump fen_masturbate_02

                            else:
                                pass
                        else:
                            pass
                        
                    else:
                        pass
                    jump fen_masturbate_01


label backyard_gunther:
    scene bg tavernback
    with s_dissolve

    #IfElse other stuff here if needed 

    if first_backyard_gunther == False:
        $ first_backyard_gunther = True
        stop music fadeout 3.0
        "As you reach the backyard, the first thing you spot is Gunther in nothing but his underwear."

        play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
        show gunther uw normal at right1
        show bg tavernback_blur
        with dissolve
        Gunther "Hey, weren't you going out?"

        show fen 2 blush at left1
        with dissolve
        Fen  "..err."

        #Fen eyes_closed

        Fen "I mean, what are you doing out here in nothing but your undies?"

        Gunther uw normal "Why I'm getting ready to work out!"

        Gunther uw wink "These muscles don't just keep themselves pumped on their own."

        show gunther at shock
        "The bar owner strikes an impressive pose to emphasize his point."

        #show Gunther blush

        Gunther uw normal "So if you're not heading anywhere, you can come get sweaty with me!"

        #insert anime nosebleed meme of Fen XD

        Fen "I...uh... I'll consider."

        hide fen
        show gunther at center1
        with dissolve

        jump backyard_gunther_menu

    else:
        pass
    
    show gunther uw normal at center1
    show bg tavernback_blur
    with dissolve
    "As you reach the backyard, you spot Gunther in nothing but his underwear, ready for workout."

    label backyard_gunther_menu:
        menu:
            "Talk":
                jump gunther_talk_01

            "Train with Gunther":
                jump gunther_event_02

            "That offer..." if fen_masturbate_02_first == True:

                Fen "Since we both are free, I'm thinking..."

                Gunther "Yes?"

                Fen "Are you up to... you know?"

                "You stare at his prominently bulging crotch as you make this request."

                if gunther_decline_sex1_first == True:
                    $ gunther_decline_sex1_first = False
                    Gunther uw smile2 "Heh, can use some help after all?"

                Gunther uw wink "Sure thing, pup."

                "Without hesitation, the Tiger agrees to your request."
                
                "You both head upstairs into your room, and strip off all your clothes for what's to come next..."

                scene bg black
                with dissolve

                scene bg fenroom
                with dissolve

                jump gunther_nsfw_01

label market:
    scene bg market
    with s_dissolve
    if first_market_done == False:
        $ first_market_done = True
        "This is your first time coming to the market alone."

        "There are smells of all kinds of food, flowers, and pedestrians coming and going."

        "Just like in the tavern, many walking here are dressed like adventurers."

        Fen "Now... where do I go?"

    else:
        pass

    label market_menu:
        menu:
            "Murry's booth":
                jump market_murry
            
            #"Look for ingredients":
                #"COMING SOON"
                #jump market_menu

            #"Relic shop" if relicshop_open == True:
                #"COMING SOON"
                #jump market_menu

            "Go else where.":
                show fen 2 normal at left1
                show bg market_blur

                call freeday_acts from _call_freeday_acts_2

label market_murry:
    scene bg stall
    with s_dissolve

    stop music fadeout 2.0
    
    #Add events here    
    if first_market_murry == False:
        $ first_market_murry = True
        "You are greeted by the familiar scent of cottonwood and...cum."

        play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0

        show murry normal at right1:
            ypos 1900
        show bg stall_blur
        with dissolve
        Murry "Why if it isn't Gunther's young protégée!"

        show murry normal at right1
        with easeinbottom
        "The shorter man hops up on his crate so that you can see him."

        show fen 2 normal at left1
        with dissolve
        Fen "Hey Murry."

        Murry "Just you today?"

        Fen "Yep, Gunther's pretty busy."

        Murry smile "Is there anything I can help you find today?"

        Fen 2 stern "Hmm, I'm just looking."

        Murry normal "Well if you have more free time, I could use an assistant of my own here."

        Fen "Me work here?"

        show murry smile at shock
        Murry smile "Why yes!"

        Murry normal "I need a courier to deliver messages and paperwork, also another person to help run a stall here at the square."

        Murry angry "The merchants are getting lazy, I should really start charging them more for this service."

        Fen 2 normal "I will consider it."

        Murry hot "Well then perhaps I could interest you in something more...alluring?"

        Fen 2 stern "..."

        Fen 2 blush "Like what?"

        Murry smile "Heh, I knew I liked you the first time I saw you."

        Murry hot "Well I have in my possession, a very detailed replica of Gunther's c-"

        "Another customer walks up to the stall."

        Murry blush "Oh, excuse me."

        show murry normal at flip
        with dissolve
        "Murry turns to address the woman waiting impatiently at the far end of the counter from you."

        Murry smile "Madam, I have your order ready. I need just a moment to fetch it from the back!"

        show murry normal at flipback
        with dissolve 
        Murry "Please excuse me, lad. I'll be back in just a bit if you still need me."

        hide murry
        hide fen
        show bg stall
        with dissolve
        "He darts off to fetch the woman's order, leaving you at the counter by yourself."

        show murry normal at center1
        show bg stall_blur
        with dissolve
        Murry "So what can I do for you?"

        jump market_murry_menu

    if bond05 == 0 and bondexp05 >= 5:
        jump murry_bond_01

    else:
        
        show murry normal at center1
        show bg stall_blur
        with dissolve
        Murry "So what can I do for you?"
        play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0

        jump market_murry_menu


label market_murry_menu:
    menu:
        "Talk":
            jump murry_talk_01

        "Shop":
            call screen murry_shop

            jump market_murry_menu
        
        "Help out":
            jump murry_help_01

        "Back":
            jump market 

label bathhouse:

    if fen_coins <= 5:
        show fen 2 stern
        "You would like to go to bathhouse, but you got no money."

        jump freeday_acts

    else:
        pass

    stop music fadeout 3.0
    scene bg bathhousehall
    with s_dissolve

    play music "audio/Sir Gawain.ogg" volume 1.0 fadein 3.0

    #unlock work at bathhouse
    if bond06 >= 1 and bath_work_unlock == False:
        jump bath_work_start
    else:
        pass

    "You enter the bathhouse and spot the proprietor behind the counter."
    show bg bathhousehall_blur
    show marcus normal at center1
    with dissolve

    #bond event 01
    if first_bathhouse_intro == False:
        $ first_bathhouse_intro = True
        jump marcus_event_01
    
    else:
        pass
    
    #bond event 02
    if bond06 == 1 and bondexp06 >= 20 and bath_work_unlock == True:
        jump marcus_bond_02
    else:
        pass

    label bathhouse_menu:
        Marcus "What can I do for you today?"

        $ config.menu_include_disabled = True

        menu:
            "What would you like to do."

            "Talk":
                $ config.menu_include_disabled = False
                jump marcus_talk_01

            "Delphinium Pool - 5 coins" if fen_coins >= 5:
                $ config.menu_include_disabled = False
                jump bathhouse_common 

            "Narcissus Pool - 10 coins" if fen_coins >= 10:
                $ config.menu_include_disabled = False
                jump bathhouse_luxury

            "Belladonna Pool - 30 coins (CHA 10)" if FenCHA >= 10 and fen_coins >= 30:
                $ config.menu_include_disabled = False
                jump bathhouse_private 
