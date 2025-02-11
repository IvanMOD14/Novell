#mainstory progression flags
default fen_remembers_father = False

#Fen progression counts
default fen_masturbate_count = 0
default already_masturbated = False
default fen_tailservice = False
default fen_tailservice_count = 0

#talk options flags
default terrance_worktalk_first = False

#events flags
default odachi_tailservice_seen = False
default gunther_workout_done = False
default gunther_clean_done = False
default odachi_bathhouse_first = False
default niall_bathhouse_first = False
default khaleb_bathhouse_first = False
default lunch_service_first = False
default fen_masturbate_02_first = False
default gunther_decline_sex1_first = False
default gunther_offer_done = False
default khaleb_event_01_asked = False
default odachi_bond_02_done = False
default bath_work_unlock = False
default bath_work_time = 0
default private_bath1_done = False
default khaleb_talk_01_done = False
default terrance_bond_03pre_done = False
default niall_bond_02_hug = False
default niall_bond_02pre_help = False
default mjolnik_visit_01_done = False
default mjolnik_visit_02_done = False
default mjolnik_talk_about_farming = False
default mjolnik_talk_about_terrance = False
default mjolnik_talk_about_family = False
default terrance_jerk_seen = False
default terrance_bond_03_sex_done = False
default watch_the_bull_work_done = False
default help_the_bull_with_chores_done = False
default mjolnik_generic_massage_done = False
default mjolnik_generic_cooking_done = False
default mjolnik_generic_chores_done = False
default mjolnik_haystack_2_done = False
default mjolnik_cooking_fruit_done = False
default mjolnik_massage_front_done = False
default mjolnik_gold_in_field_done = False
default bathhouse_murry_done = False
default ask_murry_bath_done = False
default bathhouse_odachi_done = False
default bathhouse_niall_done = False
default bathhouse_khaleb_done = False


#Oil Mix
default oil_mix_value = 0
default oil_mix_counter = 0

#SXP flags
default gunther_sxp_1 = False
default gunther_sxp_2 = False
default fguards_sxp_1 = False
default cguards_sxp_1 = False
default eguards_sxp_1 = False
default sguards_sxp_1 = False
default marcus_sxp_1 = False
default murry_sxp_1 = False
default murry_sxp_2 = False
default service_bunnies_bottom_sxp = False
default service_bunnies_top_sxp = False
default service_bear_top_sxp = False
default service_bear_bottom_sxp = False
default service_bear_hyper_sxp = False


label unlock_personal_service:

    show gunther normal at right1
    show bg tavern1_blur
    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    with dissolve
    Gunther "[name], I want to talk to you about something real quick."

    show fen normal at left1
    with dissolve
    Fen "Sure, what is it?"

    show gunther smile at left2
    with dissolve
    "The red tiger pats you on the head and smiles."

    show gunther at right1
    show fen blush
    with dissolve
    Gunther "You're doing a great job. We're getting more customers and as much as I hate to say, there certainly seems to be a fan group growing around you."

    "Your tail wags at his warm touch and words."

    show fen at shock
    Fen blush "Oh wow, I have fans?!"

    Gunther stresse "Much to my ... um, annoyance, you do."

    Gunther grin "And so there is a business opportunity. With the increase of new faces, perhaps future customers may seek your personal attention."

    Fen normal "I see."

    Gunther normal "You have proven to be a reliable individual and I hear nothing but compliments from our regulars."

    Gunther "It's clear that you've got a handle on all the regular duties, so enjoy yourself a bit. The customers definitely seem to enjoy you."

    Fen blush "Thanks, Gunther."

    Gunther "You're taking care of yourself, and you don't have to rely on just me anymore. The tavern is bustling and you're putting a smile on their faces."

    Gunther grin "You're not the helpless kid I found at death's door anymore. Continue making connections with people and cut your own path in this world."

    Gunther "It might also help you recover your memories—just a gut feeling."

    Fen smile "I will do my best."

    show gunther smile at left2
    with dissolve
    "He ruffles your hair again and surprises you with a hug."

    hide gunther
    hide fen
    show bg tavern1
    with dissolve
    "As he pulls away, he looks like he wanted to say more, but the customers are already walking through the door."

    stop music fadeout 3.0
    play sound "audio/bondexpup.ogg" volume 2.0
    "{color=#16f58d}{i}'Attentive Service' unlocked.{/i}{/color}"

    "{color=#16f58d}{i}When serving guests with a bond level of 1 or higher, you can now select the 'Attentive Service' option.{/i}{/color}"

    "{color=#16f58d}{i}This allows you to spend all your remaining AP for the day on a single guest, earning an equivalent number of bond points.{/i}{/color}"

    $ personal_service = True

    jump work

label raise_01:
    scene bg tavern1
    with s_dissolve
    "Another day of work comes to an end, and you're starting to feel more at home with your new life here."

    "Though you still don't know much about the drinks, cooking and serving food feels second nature. You must have done this kind of work before you ended up here."
    
    stop music fadeout 3.0
    "The tavern has also seen an uptick in guests since you started, no doubt thanks to the new items on the menu."

    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    show gunther normal at right1
    show bg tavern1_blur
    with dissolve
    Gunther "Great work today, [name]."

    Gunther "Your food is as tasty as ever."

    show fen normal at left1
    with dissolve
    Fen "Just doing my job. I've actually been enjoying coming up with new dishes."

    Gunther smile "Yeah, your idea of adding new items really paid off."

    Gunther stern "And your cooking skill... I have to admit, I'm always looking forward to the next dish you come up with."

    Gunther normal "Thanks to you, the numbers are looking better too."

    $fen_payment = 20
    $ fen_coins += fen_payment
    play sound "audio/payment.ogg" volume 3.0
    show gunther at center1
    with dissolve
    "Gunther hands over a small but noticeably heavier bag of coins."

    show gunther at right1
    with dissolve
    Gunther "A raise for ya, pup—20 coins. Here you go!"

    Fen stern "Oh wow, does that mean..."

    Gunther smile "Yep, just like I promised—the more we earn, the more you'll get too."

    Fen normal "I'll keep that in mind. More new dishes on the way!"

    Gunther smile "That's the spirit!"

    Gunther normal "Now, get some rest, and enjoy your day off tomorrow."

    stop music fadeout 3.0
    scene bg fenroom_night
    with s_dissolve

    "Getting ready for bed, you're in a good mood."
    
    "The usual bed feels extra soft and inviting."
    
    scene bg black
    with s_dissolve
    "As you lie down, thoughts of new dishes drift through your mind, lulling you into a peaceful sleep..."

    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    scene bg kitchen2
    with s_dissolve
    "You find yourself in a different kitchen, though unfamiliar, you instinctively know your way around."
    
    show bg at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "The table is crowded with ingredients, and once again, you're creating new dishes."
    
    "You don't know exactly what you're making, but you keep adding more to the bubbling pot."

    Fen "Cheese... Mushroom... Carrot..."
    
    Fen "Meat... Cheese... and more cheese."

    "You stir the pot, and just then, an older canine walks in."

    show bg kitchen2_blur:
        zoom 1
    hide ratio1
    show ragnar normal at center1, flip
    with dissolve
    "???" "That smells amazing! I could catch the scent two streets away!"

    Fen "New dish for the menu. Want a taste?"

    show ragnar smile2 at shock
    "???" "How could I say no to that!"

    hide ragnar
    show bg kitchen2
    with dissolve
    "With excitement, the old canine grabs a spoonful of whatever's in the pot and eagerly takes a bite."

    "???" "AH-H! HOT! HOT! HOT!!"

    Fen "Haha, careful, don't burn your tongue."

    stop music fadeout 3.0
    scene bg fenroom_blur
    with s_dissolve

    Fen "Careful..."

    show bg fenroom
    with s_dissolve
    "And with that, you wake up."

    Fen "It's... that man again. Maybe I should tell Gunther..."

    "You pause and shake your head."

    Fen "No, that won't help. I need to remember more... at least a name, or some other clue."

    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    show bg fenroom_blur
    show fen 2 normal at left1
    with dissolve
    "After taking a moment to gather your thoughts, you stretch and prepare yourself for the day ahead."

    $ work_day_count = 0
    
    jump freeday_acts

label terrance_personal_01:
    scene bg tavern4_blur
    show terrance smile at center1
    with dissolve

    $ bondexp02 += ap
    $ ap = 0
    call bondexpup02 from _call_bondexpup02_5
    "You make sure to spend extra attention on Terrance tonight and it's obvious from his happy expression he's enjoying it."
    
    "Every so often he shifts to give you a good view of his body in thanks, giving you a wink or sly smile each time he does so."

    jump work

label odachi_personal_01:
    scene bg tavern4_blur
    show odachi smile at center1
    with dissolve

    $ bondexp03 += ap
    $ ap = 0
    call bondexpup03 from _call_bondexpup03_7
    "You make the effort to devote as much of your attention as possible towards entertaining Odachi. He seems greatly interested to hear more about Feldan lifestyles and customs from you."
    
    "You think it's just adorable whenever he tries really hard to draw parallels back to things from his home country and put it into words."

    jump work

label niall_personal_01:
    scene bg tavern4_blur
    show niall smile at center1
    with dissolve

    $ bondexp04 += ap
    $ ap = 0
    call bondexpup04 from _call_bondexpup04_7
    "Thinking of Niall, you let him know it's okay to talk to you as much as he wants tonight while you're working."
    
    "With glowing enthusiasm, he takes you up on the offer and talks your ear off about the myths and monsters he's read up on and what guild rumors are still hot on his mind."
    
    "It exhausts you a little towards the end, but at least you seem to have brightened up his evening."

    jump work

label marcus_personal_01:
    scene bg tavern4_blur
    show marcus smile at center1
    with dissolve

    $ bondexp06 += ap
    $ ap = 0
    call bondexpup06 from _call_bondexpup06_10

    "You spend the evening frequenting Marcus's table. He appreciates your playful banter and sneaks a few gropes."
    
    "You return the favor here and there when you pass by with another order of hot food or cold drink."

    jump work

label khaleb_personal_01:
    scene bg tavern4_blur
    show khaleb smile at center1
    show arek smile at left3, flip
    show trei smile at right3
    with dissolve

    $ bondexp07 += ap
    $ ap = 0
    call bondexpup07 from _call_bondexpup07_6
    "You take extra care around The Renegades' table tonight, and not just because you're afraid of what trouble they might start."
    
    "At some point, they ask you to bet on drinking games with them and share stories with you about their recent adventures, always making them sound so dirty..."
    
    "All-in-all, though, you manage to have a pretty okay time, somehow, and they end up looking fairly content, themselves, when they leave."

    jump work

label fen_rest_01:
    "You decides to enjoy your free day by rest in your room."

    "After a nap and some well earned private time, you feel totally refreshed."

    $ ap += 2

    "{color=#16f58d}{i}Action points for next day incressed by 2!{/i}{/color}"

    jump day_end

label fen_masturbate_01:
    scene bg fenroom at truecenter:
        zoom 2
    show ratio1
    with s_dissolve
    stop music fadeout 3.0
    "You go lie back down in bed, planning to take some time to yourself and enjoy the soft morning light pouring in through the window wash over you."

    "You feel so cosy like that, snuggling up with your pillow, and especially remembering the long and tiring day you had yesterday."

    "A certain growing part of you feels like doing something with all this good energy."

    "You know you woke up this morning feeling pent up, but now that you've had breakfast, even a slight brush against it through your underwear causes you to blush."

    show fen hard hot at truecenter behind ratio1:
        zoom 1.5
        ypos 900
    show bg fenroom_blur at truecenter:
        zoom 2
    with dissolve
    "Impatient to get to it, you let your hand wander down the taut curves of your own body to touch the aching erection between your legs."

    play music "audio/stroking_slow_rhythmic_01.ogg" volume 1.0 fadein 3.0
    "You stroke it furiously beneath the sheets."

    "Some part of your still half-asleep mind is dulling your usual inhibitions about this kind of thing."

    play sound "audio/light moan 1.ogg" volume 1.0 loop fadein 3.0
    "It makes you feel feral; like the beast you can only be when no one's watching..."

    "The instant your fingers brush up against the heavy wet spots of pre, now staining your sheets, you get a powerful desire to do something more."
    
    $ fen_masturbate_count += 1

    menu:
        "What should it be?"

        "Focus more on stroking.":
            jump about_fen_jerking_solo
        
        "Explore further down below.":
            jump about_fen_fingering_solo
    
    label about_fen_jerking_solo:
        show fen hard hot at truecenter behind ratio1:
            zoom 1.5
            ypos 500
        with ease
        "Throwing off the bed sheets, you look down and breathe in the smell of your fresh morning wood."

        "You continue to jerk, gripping tighter whenever your fingers get up near the head."

        show fen hard hot at truecenter behind ratio1:
            zoom 2
            ypos 500
        with dissolve
        "This makes you start leaking so much, a dribble runs right over your hand and makes its landing down on your stomach, right over your pubic fur."

        "The muskiness of it smells stronger the more comes out."

        "Gods, you're such a horny dog..."

        show fen hard hot at truecenter behind ratio1:
            zoom 2
            ypos 1400
        with dissolve
        "You close your eyes and just let your wild daydreams take you for a ride, making use of your other hand to twist your own nipple for extra fun."

        "All of the sensuous men you get to see everyday, each of them either hunky, cute, or somewhere in the middle between both; they make you feel so lucky."

        hide fen
        with dissolve
        play music "audio/stroking_fast_rhythmic_01.ogg" volume 1.0 fadein 3.0
        "As you imagine them stripping down and splaying out their holes, you can't help but fantasise about you being the one who gets to take on them."

        "Your heart races at the thought, no matter how untrue to life it might be."

        "The bigger ones grunt and purr as you inch your cock lovingly into their tight, unmolested but huge muscly asses."

        "Meanwhile, the smaller ones pant, almost gasping for breath, with their heads empty and eyes glazed over as you break them in to be your toys."

        "They've realised that nobody in the world can make them as happy as you can and want to make you happy back by being pumped like balloons full of your cum."

        "Each of your imaginary couplings ends and moves on to a new partner the moment that one turns around and smiles, full of pride in you."

        "You're worried you might cum the moment you imagine one of them saying those two magic words that always come with that look."

        "Even though you want to hear it so bad, you also don't want this beautiful high to end any time soon."

        show fen hard hot3 at truecenter behind ratio1:
            zoom 2
            ypos 1400
        with dissolve
        Fen "Grrghh...Mmmmhh..."

        Fen "Ah! Ah-Aah!"

        hide fen
        with dissolve
        "But on a whim, the part of you that wants it gives in."

        "'Good boy', says one of the figments to you, with nothing but pure love in his voice."

        "And at that, your eyes burst open to the sight of your dick erupting."

        stop music fadeout 1.0
        play sound "audio/light climax 1.ogg" volume 1.0
        show fen cum at left2 behind ratio1:
            zoom 1.5
        with dissolve
        "The load sprays out so forcefully from all the passionate edging you did that your whole body tenses up and shakes while you're just left to watch."

        Fen "Awooo...!"

        "A half-restrained howl escapes your lips before devolving into demure, very canine whimpers as you come down off from the climax."

        hide fen
        show bg fenroom at truecenter:
            zoom 2
        with dissolve
        "You fall back limp against your pillow, tongue lolling out the side of your face, while so much of your fur is now just caked with spunk and sweat seeping through."

        "You're briefly pulled back into a blissful nap by the afterglow before getting up again to start the new day off in earnest."

        scene bg tavernback
        with s_dissolve
        "Taking care not to forget, you gather up your underwear and sheets to go wash them thoroughly and put them up to dry."

        "Hopefully, Gunther won't find it too suspicious if he catches you stepping out for a quick bath while it's still so early."

        $ already_masturbated = True

        show fen 2 blush at left1
        show bg kitchen_blur
        with dissolve

        call freeday_acts from _call_freeday_acts

    label about_fen_fingering_solo:
        show fen hard hot at truecenter behind ratio1:
            zoom 1.5
            ypos 500
        with ease
        "You throw off the bed sheets and roll over to get into a good position; one with your elbows and knees comfortably pressing into the mattress."

        hide fen
        with s_dissolve
        "Excitedly, one of your hands wanders down the plump, sagging heft of your pecs and over the rigid grooves of your abs, tensing, before making its way behind."

        "Feeling for your taint, you stick out a finger and rub it up and down the area between your cheeks before getting to the hole."

        "Anything down there always feels better when you tease it a little bit first."

        "Once it seems like everything's ready, you wriggle in a finger just up to the first joint to test the waters."

        "And it immediately gets sucked in by the suction-tight grip of your hungry pucker."

        "Gods, you have such a needy hole..."

        "As you work to fit in more and more, you close your eyes and just let your daydreams run absolutely wild with you."

        play music "audio/stroking_fast_rhythmic_01.ogg" volume 1.0 fadein 3.0
        "All of the sensuous men you get to see everyday, each of them either hunky, cute, or somewhere in the middle between both; they make you feel so lucky."

        "As you imagine them stripping down and getting into position to mount you, you can't help but fantasise about how well they're going to take care of you."

        "Your heart races at the thought of being their favourite pet to breed and cuddle."

        "The bigger ones towering over you with their bulk, holding you in place by your shoulders or sides while they plough into you and stretch you from inside."

        "And the smaller ones thrusting into you with a passionate vigour, faces flushed and spasming with need as you milk their modest cocks like a machine."

        "They've realised that nobody in the world can make them as happy as you can and they all fight to claim you as theirs by seeding you full of their cum."

        "Each of your imaginary couplings ends and moves on to a new partner the moment that one leans in to speak with their breath hot right in your ear."

        "You're worried you might cum the moment you imagine one of them saying those two magic words that always come with that sultry tone."

        "Even though you want to hear it so bad, you also don't want this beautiful high to end any time soon."

        show fen hard hot at truecenter behind ratio1:
            zoom 2
            ypos 1400
        with dissolve
        Fen "Grrghh...Mmmmhh..." 

        Fen "Ah! Ah-Aah!"

        hide fen
        with dissolve
        "But on a whim, the part of you that wants it gives in."

        "'Good boy', says one of the figments to you, with nothing but proud ownership in his voice."

        stop music fadeout 1.0
        play sound "audio/light climax 1.ogg" volume 1.0
        show fen cum at left2 behind ratio1:
            zoom 1.5
        with dissolve
        "And at that, your eyes burst open to the sight of your dick erupting onto the sheets, while ass juices coat your hand that's in you almost up to the wrist."

        "The load sprays out so hard from how much pressure there is against your prostate that your whole body tenses up and shakes."

        "All you can do is look down with your tongue flopping out as it happens."

        Fen "Awooo...!"

        "A half-restrained howl escapes your lips before devolving into demure, very canine whimpers as you come down off from the climax."

        hide fen
        show bg fenroom at truecenter:
            zoom 2
        with dissolve
        "You collapse on top of the mattress, the big mess you just made now seeping into the fur around your stomach, crotch, and legs in addition to the sheets."

        "You're briefly pulled back into a blissful nap by the afterglow before getting up again."

        "It takes you a minute to peel your body off the dried cum that's glueing you to the bed until you're ready to start the new day off in earnest."

        scene bg tavernback
        with s_dissolve
        "Taking care not to forget, you gather up your underwear and sheets to go wash them thoroughly and put them up to dry."

        "Hopefully, Gunther won't find it too suspicious if he catches you stepping out for a quick bath while it's still so early."

        $ already_masturbated = True

        show fen 2 blush at left1
        show bg kitchen_blur
        with dissolve

        call freeday_acts from _call_freeday_acts_1

label fen_masturbate_02:

    $ fen_masturbate_02_first = True

    scene bg fenroom at truecenter:
        zoom 2
    show ratio1
    with s_dissolve
    stop music fadeout 3.0

    "As you settle down in your bed, naked and prepared to unwind, you hear a creak outside."

    hide ratio1
    show bg fenroom at truecenter:
        zoom 1
    with dissolve
    play sound "audio/Door Open 2.ogg" volume 1.0
    "The door suddenly opens and Gunther barges in."

    show gunther normal at right1
    show bg fenroom_blur
    with dissolve
    Gunther "[name], I wanted to sho-"

    show fen naked shock at left1
    with dissolve
    Fen "Ah!"

    show fen naked blush
    with dissolve
    "You jump up from your bed, startled by the sudden intrusion."

    Gunther stern "Whoa! Sorry to interrupt."

    "You watch his gaze slowly drift down and then back up."

    Fen "It's alright..."

    Gunther normal "No need to be shy, [name]."

    Gunther grin "So... Would you like a hand then?"

    menu:
        "Take Gunther up on his offer?"

        "Yes!":
            jump gunther_sex1

        "Nah...":
            jump gunther_decline_sex1

    label gunther_decline_sex1:

        $ gunther_decline_sex1_first = True

        Fen "I...um."

        "You are taken aback by the sudden offer."

        Gunther normal "Hey, no pressure. I just figured I'd offer a helping hand."

        "You've grown accustomed to the casual nudity, but casual 'offers' are still a bit...direct for you."

        "Even though you'd happily welcome the big cat over to toss your bed sheets around, you let your shyness get the better of you."

        Fen "I'm good, but thanks for the offer."

        Gunther wink "Anytime."

        hide gunther
        with dissolve
        play sound "audio/Door Close.ogg" volume 1.0
        "Gunther winks and closes the door behind him as he departs."

        Fen "..."

        hide fen
        show bg fenroom
        with s_dissolve
        "You sit alone on the bed, pondering what just happened."
        
        "Perhaps you should have agreed to him earlier?"
        
        "But he did say anytime... which means there's still room for reconsideration, right?"

        "Your mind is filled with thoughts of Gunther, and you spend the day idly rolling around in bed, accomplishing nothing."

        jump day_end

        #continue

    label gunther_sex1:
        show fen at shock
        Fen "Yes!"
        
        Fen naked blush"I mean... Sure, if you want..."

        Gunther smile2 "Great, let's have some fun."

        hide fen
        hide gunther
        show bg fenroom
        with dissolve
        play sound "audio/Door Close.ogg" volume 1.0
        "A wide smile spreads across Gunther's muzzle as he closes the door behind him and approaches your bed."

        "He starts to strip off his work clothes and a moment after, he's just as naked as you are."

        #show Gunther naked and fen blushing 
        show gunther naked normal at top:
            zoom 1.5
        show bg fenroom_blur at top:
            zoom 1.5
        with dissolve
        "You've seen him naked many times before, but the excited look in his eye sends your heart racing."

        "The big cat gives you a hungry look as he creeps closer."

        "His gaze locks onto yours as he saunters over."

        jump gunther_nsfw_01

label fen_tailservice_00:
    stop music fadeout 1.0
    scene bg alley2
    with s_dissolve
    "You enter the alleyway meant for 'Tail Service'."

    play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
    show fen 2 blush at center1
    show bg alley2_blur
    with dissolve
    Fen "So... this is the place Odachi mentioned. I hope I didn't get it wrong."

    $ fen_tailservice_count += 1

    label fen_tailservice_menu:

        menu:
            "Offer tail service.":

                jump fen_tailservice_offer

            "look for tail service.":
                if fen_coins >= 20:
                    jump fen_tailservice_look
                
                else:
                    Fen "I don't have extra coins for that..."

                    jump fen_tailservice_menu

label fen_tailservice_offer:
    hide fen
    show bg alley2
    with dissolve
    "After some simple 'preparation', you linger there comfortably, alone, and wait for somebody to come."

    jump fen_tailservice_guards
    
label fen_tailservice_guards:
    hide fen
    show bg alley2
    with dissolve
    "A bit of time passes before a figure approaches through the same way you came." 
    
    "It was one of the town guards, though it's hard for you to make out which one through his lowered visor."
    
    "At first, you're unsure if he's really here for what you think he is."
    
    "But you turn around and lift up your tail expectantly for him all the same, intrigued to see what happens."

    $ tailservice_guards = renpy.random.choice(['FGuard', 'CGuard','EGuard','SGuard'])

    if tailservice_guards == 'FGuard':
        jump fen_tailservice_fussyguard
    
    if tailservice_guards == 'CGuard':
        jump fen_tailservice_carefreeguard

    if tailservice_guards == 'EGuard':
        jump fen_tailservice_energeticguard

    if tailservice_guards == 'SGuard':
        jump fen_tailservice_stoicguard
    
    else:
        pass

label fen_tailservice_fussyguard:

    show guards fussy normal at right1
    show bg alley2_blur
    with dissolve
    FGuard "Hmmm..."

    "The guard stands there with his chin rested on his thumb in what sounds like deep contemplation."
    
    "He stays that way long enough to make you wonder if maybe you had been wrong about this."

    FGuard "I mean, I like it, and all. Just not sure about those clothes, though. Looks like they've seen messy work to me..."

    show fen 2 stern at left1
    with dissolve
    Fen "Uh, yeah. It kind of happens with my job."

    FGuard fussy smile "No worries, let's just get you out of those, and take it from there."
    
    FGuard "Lose it all, one piece at a time. And you can take your time doing it, too..."

    hide fen
    hide guards
    show bg alley2
    with dissolve
    "From the sultry tone of voice with which he says this, it's not hard for you to pick up on what he's asking to see."
    
    stop music fadeout 3.0
    show bg alley2_blur at truecenter:
        zoom 1.5
    show fen 3 blush at top:
        ypos -200
        zoom 1.5
    show ratio1
    with dissolve
    "As instructed, you get to work undressing yourself, first with your shirt..."
    
    show fen uw blush at top:
        ypos -300
    with dissolve
    "...then pants..."
    
    show fen naked blush at top:
        ypos -500
    with dissolve
    "...and finally your underwear."

    hide fen
    show bg alley2_blur at truecenter:
        zoom 2
    with dissolve
    "With each article, you try to make it look like you're almost peeling it off your body with how slow your hands are moving."
    
    "You smile a bit sheepishly and try to keep eye contact with the guard as much as possible while doing it."
    
    "Canines have never really been known to be discreet about how much they love a tease, and this man in front of you was certainly no exception."
    
    hide ratio1
    show bg alley2_blur at truecenter:
        zoom 1.5
    show guards fussy hot at top:
        zoom 1.5
    with dissolve
    "The guard's jaw unhinges, and his tongue rolls out of his muzzle as he starts panting and groping himself through his uniform while he eats you with his eyes."
    
    "You can tell exactly what parts of you he's hungry for the most when his breath gets quicker."
    
    show bg alley2_blur at truecenter:
        zoom 1.5
    hide guards
    show fen naked normal at truecenter:
        zoom 2
    show ratio1
    with dissolve
    "It's for your abs, after you took your time revealing them bit-by-bit while tugging off your shirt."
    
    "For the curvature of where your thigh and buttocks meet, after you ran your fingers over it pulling down your pants."
    
    "You don't even really think you're doing much that special, but his reactions are the kind you might expect a real professional at this would get!"

    hide fen
    hide ratio1
    show bg alley2_blur at truecenter:
        zoom 1.5
    show guards fussy hot at top:
        zoom 1.5
    with dissolve
    FGuard "Rrrrffh...Oh, yeah. That's it, puppy. Come here."

    hide guards
    show bg alley2 at truecenter:
        zoom 1
    with dissolve
    "Once you're standing bare naked in front of him, the guard goes over to the side and pulls out a clean, white handkerchief from his side satchel."
    
    "He lays it down on top of a sturdy-looking crate, and ushers you to come sit on it."
    
    "When you do, you realise he must have done it as a precaution against the spread of dust and grime more than anything."
    
    show bg alley2 at truecenter:
        zoom 2
    show ratio1
    with dissolve
    "The cloth itself offers little cushioning for your rear against the hardwood."
    
    "You're not able to pay it that much mind, though, before a more interesting piece of hard 'wood' captures your attention..."
    
    show bg alley2_blur
    show guards fussy hard blush at center1 behind ratio1:
        zoom 2
        ypos 1600
    with dissolve
    "The guard closes in on you with the front drape of his tunic held clenched in his mouth and his underwear pulled down just enough for his dick to come poking out."
    
    "He spreads your legs out wide, forcing you to lean back against the alley's brick wall, as he brings it level with your exposed pucker."

    hide guards
    show bg alley2
    show ratio1
    with dissolve
    FGuard "Hehe...You prepped it good for me, huh? Gonna have to toss in a little bit extra for such fine service."

    "You're about to thank him for the compliment but get stopped short by the overpowering need to let out a gasp."
    
    play music "audio/light moan 1.ogg" volume 0.5 fadein 1.0
    play nsfw1 "audio/mid growls 1.ogg" volume 1.0 fadein 1.0
    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    show guards fussy hot at top behind ratio1:
        zoom 3
        ypos -200
    show bg alley2_blur at top
    with dissolve
    "He slides right into you with no further warning and starts pounding away."
    
    "At first, you whine a little miserably about it."
    
    "It's more as a way to let out the built-up anxiety you were feeling over this new partner than over any actual pain you were experiencing."
    
    "But then, he starts slowing down his pace a bit for you, which lets the waves of pleasure he's making start flooding your mind surprisingly quickly."

    FGuard "Sorry, I–Mmph! I guess I just really needed this today."
    
    FGuard "Ugh, ugh! Oh, yeahhh... Is it good for you too, puppy?"
    
    FGuard "I do lots of hard work making sure this town stays in good order, you know that?"
    
    FGuard fussy hot2 "You can feel how much I care about getting a job done right, huh?"
    
    FGuard fussy hot "Urrf...I want you to tell me what good work I'm doing fucking you..."

    hide guards
    show bg alley2_blur at truecenter:
        zoom 2
    with dissolve
    "It takes you a while to figure out what it is about his motions that feel so enthralling to you."
    
    "It's that almost every one of his thrusts are hitting you right in your g-spot with confident precision and thoroughness."
    
    "It feels not only erogenous but also kind of reassuring to be coupling with someone who puts so much care into what he's doing to you."

    show fen naked hot2 at top behind ratio1:
        zoom 2
    with dissolve
    Fen "Yes! Oh, fuck, yes...!"
    
    Fen "Hahhhh, you're doing such great work, sir! You're a good boy!"
    
    Fen "A good, good, good, good boy! Ahh!"
    
    Fen "And I...I want to be one for you, too...!"

    show fen hard hot at top:
        ypos -1000
    with dissolve
    "Pressed up like this into a corner by the guard's skillful yet greedy love-making, your baser instincts start to make you get lost in the moment with him."
    
    "With no hesitation, you grab hold of your own cock, which has been bobbing freely in front of him until now, and beat it off eagerly to the rhythm he's going."
    
    "Your show of acceptance is rewarded when he leans in even closer and whispers words of encouragement back right in your ear."

    "The hot dampness of his breath mixed with thoughts of approval and safety drive you over the edge."
    
    stop music fadeout 0.5
    play sound "audio/light climax 1.ogg" volume 1.0
    show fen cum with vpunch
    "In mere moments after touching yourself, you feel your dick erupt with cum in the middle of him still giving you hushed praises."
    
    "It seems to take the guard a moment to register that it happened, and he pulls back into an upright position to make sure."
    
    show terrance cg1 14 at truecenter, flip behind ratio1:
        zoom 2
        ypos -200
    with dissolve
    "You open your eyes to see that copious amounts of it landed all across your stomach."
    
    "Some of it even sprays all the way up to the lower parts of your chest below the nipples."
    
    "As impressive of a load it must've been, you probably looked like quite a mess right now..."

    hide fen
    hide terrance
    show guards fussy hot at top behind ratio1:
        zoom 3
        ypos -200
    show bg alley2_blur at top
    with dissolve
    FGuard "Haha! Aw, poor boy."
    
    FGuard "Was that all supposed to be for me? Well, it's the thought that counts, so I still appreciate it."
    
    show guards:
        ease 0.5 zoom 3.3

    FGuard "In fact, here. I'll make sure nothing goes to waste."

    "As he says that, he gets out of you and moves up to straddle over top of your torso, placing a hand at the base of your neck for leverage."

    FGuard fussy hot3 "Huff, Huff. I'm so close...Nghhh...Ngggghhhh!"

    stop nsfw1 fadeout 0.5
    play sound "audio/mid climax 1.ogg" volume 1.0
    hide guards
    show bg white
    with dissolve
    "The guard's cumshot spews down on you in a warm little shower, intermixing with much of your own where it falls."
    
    stop fuck fadeout 3.0
    stop ball fadeout 3.0
    show terrance cg1 14 at truecenter, flip behind ratio1:
        zoom 2
        ypos 100
    with dissolve
    "His gets up a bit further along your chest than yours did, and there's now enough batter shared between the two of you for it to run dribbling down off the side of your stomach."
    
    hide ratio1
    hide terrance
    show bg alley2
    with dissolve
    "Then, after letting himself bask in the high of the deed for a few seconds, the guard hunkers down even more over you and does something you find kind of strange."
    
    play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
    "He gets to work lapping up the cum on your fur in a quick flurry of licks and suckles, as though polishing off a meal he can't get enough of."

    Fen "Hehehe! Hey, cut it out! That tickles."

    show bg alley2_blur at top:
        zoom 2
    show guards fussy smile at top:
        zoom 3
    with dissolve
    FGuard "Mmm. Sorry, no can do, boy."
    
    FGuard "Wouldn't want to let you go off looking all dirty like this, would we?"
    
    FGuard "This is the fastest way to get you all cleaned up and ready for whoever comes along next."

    FGuard "I can assure you, it's my pleasure to help out such a fine working man such as yourself."
    
    if guards_bond_ui == False:
        stop music fadeout 3.0
        show bg alley2 at center1:
            zoom 1
        with dissolve

        $ guards_bond_ui = True
        call bondlvup0800 from _call_bondlvup0800

    else:
        call bondexpup08 from _call_bondexpup08
        $ bondexp08 += 3

    stop music fadeout 3.0
    hide guards
    scene bg alley2 at truecenter:
        zoom 1
    with dissolve
    "Not that he's really giving you a choice in the matter, but you let the guard do you the favour of a tongue bath before finishing up your business together."
    
    play sound "audio/payment.ogg" volume 3.0
    "Afterward, he waits for you to get dressed again before handing you your payment for the service."
    
    "You even get an extra compliment as he tells you there's potential for you to grow into one of the finest he's seen on these streets!"
    
    "Wow! If only all your customers could be this nice, whether they were the ones who expected to bonk with you or not..."

    if fguards_sxp_1 == False:
        $ fguards_sxp_1 = True

        call sxp_up from _call_sxp_up_5

    else:
        pass

    $ fen_coins += 15
    play sound "audio/payment.ogg" volume 3.0
    "You received 15 coins for your service."

    jump day_end

label fen_tailservice_carefreeguard:
    "As you do so, though, something odd of what the guard is carrying registers in your brain, so you peer back out of the corner of your eye to make sure."
    
    show bread02_01 at truecenter
    show ratio1
    show bg alley2_blur at truecenter:
        zoom 2
    with dissolve
    "It looks like he's holding... a basket full of pastries?"
    
    hide ratio1
    hide bread02_01
    show bg alley2_blur at top:
        zoom 1
    show guards carefree eat at top:
        zoom 1.5
    with dissolve
    "And he's just standing there, pulling one out to bite into it..."
    
    "Not walking away or so much as saying anything... while you're also there, stuck in that raunchy pose, offering yourself to him like that..."
    
    "He just... keeps on eating it and pulls out another..."

    hide guards
    show fen 2 stern at left1
    show bg alley2_blur at center:
        zoom 1
    with dissolve
    Fen "Uhhh, hello?"

    show guards carefree eat at right1
    with dissolve
    CGuard "Hi."

    "That's about all the answer you get out of that in between the sounds of him slurping the filling out of a bun."
    
    "After licking his fingers clean, he takes out another and offers it to you."
    
    show fen at center1
    show guards behind fen
    with dissolve
    "Still unsure about what this is supposed to mean, you go over to him and take it."
    
    hide fen
    hide guards
    show bread02_01 at truecenter
    show ratio1
    show bg alley2_blur at truecenter:
        zoom 2
    with dissolve
    "Just one bite into the puffy, egg washed bun is enough for its thick cream to burst into your mouth."
    
    "The dough is sugary and light, while its filling is just a bit sour and rich, making for a superb combination."

    hide ratio1
    hide bread02_01
    show bg alley2_blur at top:
        zoom 1
    show fen 2 eat2 at left1
    with dissolve
    Fen "Oh, wow! That's so tasty!"

    show guards carefree eat at right1
    with dissolve
    CGuard "I know, right? I get them from this little bakery on River Street that makes them fresh every morning."
    
    show guards carefree grin at shock
    CGuard "So worth waiting in line for before work!"

    hide fen
    hide guards
    show bg alley2_blur at top:
        zoom 1.5
    with dissolve
    "You take a seat on one of the discarded barrels nearby and savour the rest of your treat while enjoying the time passing by."
    
    "It feels nice. He doesn't talk to you all that much, but there's something about his presence that's very relaxing."
    
    "The tranquillity almost makes you lose sight of why you're there, but then you realise he never let you know what his business was."

    stop music fadeout 3.0
    Fen "Hey, so what are y–Ah!"

    show bg alley2_blur at truecenter:
        zoom 1.5
    show guards carefree hard at center1:
        zoom 1.5
    show ratio1
    with dissolve
    "Going back to him, you're startled to see him casually standing there with the front of his tunic parted, pulling his fully erect cock out of his underwear."
    
    "He doesn't pause at all after seeing your reaction."
    
    show guards:
        zoom 2.5
        ypos 2000
        xpos 1300
    with dissolve
    "Instead, he takes another one of his sweet buns and starts squeezing the cream in a line all along the top of his shaft."
    
    "It's thick like an overstuffed sausage and completely sheathed in foreskin, and it looks so fresh and glossy like it hasn't been touched in weeks."

    show guards fussy hot2 at top:
        zoom 2.5
    with dissolve
    CGuard "Huff... Gotta say, I'm really glad I found you here today."
    
    CGuard "There really hasn't been all that many I've seen lately who are worth the trouble. And I can't do it on my own."

    Fen "O-Oh. So, I guess you are here for that, then."

    CGuard "Yeah, man. You're real heckin' cute, you know. It's why I'm busting out for you my special treat. Hehe..."

    show guards carefree hard pre at center1:
        zoom 2.5
        ypos 2000
        xpos 1300
    with dissolve
    "He gives the underside of his rod an absent-minded stroke, and it makes him shiver as a dollop of pre leaks out from the tip."

    show guards fussy hot at top:
        zoom 2.5
    with dissolve
    CGuard "Aw, damn. It's been too long. My balls, they feel so full."
    
    CGuard "Hey, come on, buddy. You liked the snack, right? How's about coming in for seconds already?"

    show guards carefree hard pre at center1:
        zoom 2.5
        ypos 2000
        xpos 1300
    with dissolve
    "The invitation makes you swallow hard. You've got to admit, this is sort of an unusual way for somebody to go about this kind of business."
    
    "But you wouldn't want to seem unprofessional for stalling things by asking too much."
    
    "And certainly not after having made a new friend who's so very... generous."
    
    show guards:
        zoom 2.75
    with dissolve
    "You drop down to your knees and sidle up to his fun-sized treat."
    
    play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
    "Watching him gasp and shudder when you bring your lips to curl around it makes you feel much more confident about this."
    
    "His body is basically begging you to devour him."
    
    "You go in to try and start by working just the tip, but then the guard bucks his hips, making the whole of it plunge down your throat at once."
    
    "You gag on it and suck off all the custard as you reflexively pull it back out."

    CGuard "Oops. Ahaha! Guess that's what happens when you're eager."
    
    CGuard "You okay? Here. I got it covered."

    "He takes out another bun and puts on a second squirt of cream."
    
    "This time, you're determined not to hesitate."
    
    "Gripping the base of his cock and stroking it, you eagerly gobble down as much of the length as you can fit."
    
    "The milky sweetness of the cream and mild, salty drops of the wolfman's pre mingling together on your tongue creates such an exotically addicting flavour."

    show guards fussy hot at top:
        zoom 2.5
    with dissolve
    CGuard "Ahhh, yeah! Yeah, that's what I'm talkin' about. Suck out my cub juice!"
    
    CGuard "Ohhh, yeah, you love the way that dick tastes, huh? Here..."

    show guards carefree hard pre at center:
        ypos 2800
        xpos 1000
    with dissolve
    "He grabs your paw and puts it against his abs so you can feel them up."
    
    "They're rock solid and perfectly cut."

    CGuard "Wondering how I keep 'em so in shape while eating sweets everyday?"
    
    CGuard "It's all thanks to the motivation I get from the Captain and the rest of my pack."
    
    CGuard "I gotta train twice as hard as them to keep it up enough to serve and still enjoy what I want to."
    
    CGuard "But I don't mind it much at all. Cause I'm just a guy with that much love to give, and all this to show for it."

    "He flexes both his arms for you, making twin peaks like the tops of mountains with his biceps."

    CGuard "And you want a guy like this to breed your cute little, doggie throat, don't you?"

    show guards at center1:
        zoom 2.5
        ypos 2000
        xpos 1300
    with dissolve
    "You do. And the frantic speed you're now going with your cocksucking tells him just that."
    
    "Just the salty drops you've been getting aren't enough for you."
    
    "There's a cloying lump left at the back of your throat from when you scarfed down so much custard, and you desperately need something to help wash it down."
    
    "And even though he's offering you so much, you know that behaving like this is nothing but greedy of you."
    
    "It makes you feel like a starved animal, and you love it."

    show guards fussy hot3 at top:
        zoom 2.5
    with dissolve
    CGuard "Hahh! Close..."
    
    CGuard "I'm getting close for you, dude."
    
    CGuard "M-My balls are–Ngh!–tensing up."
    
    play sound "audio/mid climax 1.ogg" volume 1.0
    CGuard "Yeah! Oh, fuck yeah...!"
    
    CGuard "Ooohhhh–!" with vpunch

    hide guards
    hide ratio1
    show bg white
    with dissolve
    "The cumshot pours into your mouth like taking a swig from a mug of ale."
    
    show ratio1
    show bg alley2 at truecenter:
        zoom 2
    with dissolve
    "For a second, you're not sure what to do, as he keeps cumming so much after that, it starts actually filling your cheeks and dripping down your chin."
    
    "But then, in a small moment of courage, you swallow, gulping down everything you can until the tap runs dry."
    
    "The guard throws his head back to look up at the sky, winded."
    
    "An odd, yet warm, feeling of fullness comes over your stomach."
    
    stop music fadeout 3.0
    show guards fussy hot at top behind ratio1:
        zoom 2
    show bg alley2_blur at top:
        zoom 2
    with dissolve
    CGuard "Hah...Hah...Phew! Oh gods, I needed that."
    
    CGuard "Thanks, bud. Hey, you don't mind if I start up a tab for the payment, do you?"
    
    CGuard "I'm not sure I really got the coin for this after how much I spent on my bakery run this morning."

    Fen "W-What!?"

    play sound "audio/payment.ogg" volume 3.0
    show guards fussy hot2 at shock
    CGuard fussy hot2 "Haha! Nah, just kidding! Here ya go, man. Worth every piece."
    
    if guards_bond_ui == False:

        scene bg alley2

        $ guards_bond_ui = True
        call bondlvup0800 from _call_bondlvup0800_1

    else:
        call bondexpup08 from _call_bondexpup08_1
        $ bondexp08 += 3
        CGuard "I'll definitely tell the rest of the guys about you, if you plan on showing up around here more often."

    scene bg alley2 at center:
        zoom 1
    with dissolve
    "With that, the guard walks away to return to his post, crumpling up the empty pastry basket and discarding it on the ground before exiting the alleyway."

    if cguards_sxp_1 == False:
        $ cguards_sxp_1 = True

        call sxp_up from _call_sxp_up_6

    else:
        pass

    $ fen_coins += 16
    play sound "audio/payment.ogg" volume 3.0
    "You received 16 coins for your service."

    jump day_end

label fen_tailservice_energeticguard:

    "This guard reacts to seeing you by letting out an unexpected cry of joy."
    
    "It's high-pitched, as if he's trying to imitate the sound of a young puppy."

    show guards energetic tongue at right1
    show bg alley2_blur
    with dissolve
    EGuard "Oh, my gosh! A new face! Hiiii! Hello, there."

    "You turn around and see him running towards you with his tail wagging."

    show fen 2 normal at left1
    with dissolve
    Fen "Oh, uh...Hi."

    show guards at shock
    EGuard "It's so nice to meet you here! Love to see a new pretty face on this side of town."
    
    EGuard "I can already tell you're going to be a big hit around these parts if you're not already."
    
    EGuard "That boyish, good-looking face of yours on top of that bulging, beefcake bod is something that no other guy in the neighbourhood's got."
    
    EGuard "And I should know. I've been around a few times on my patrols. Ahahaha!"

    Fen 2 smile "A-heh... Well, thanks, I guess?"

    EGuard "I'm Leven, by the way. Well, actually, that's short for Levendig, but I think it's super not cute to leave it unshortened like that."
    
    EGuard "So, yeah. Hey, you got a routine figured out yet? Like, is there any way you like to do it for a standard?"
    
    EGuard "Cause a lot of street workers I hear about tend to have that going on."
    
    EGuard "And anything apart from that counts as 'special services', which often comes with a surcharge."
    
    EGuard energetic normal "And that's just a liiittle bit greedy of them, if you ask me. I mean, not that I'm judging you or anything, if that's you too."
    
    show guards energetic tongue at shock
    EGuard "But, like, if it's not, then awesome!"
    
    EGuard "I could so get you situated by showing you some of my favourite tricks, which also happen to be some of the more popular ones. A-haha!"

    show fen 2 stern with dissolve
    "All his talking is really starting to grate on your ears."

    Fen 2 stern "S-So, is there any way you want it right now, or–"

    EGuard energetic normal "Hmm...Hmmmm....Well, I guess it'd be best if I'd rather let you decide on that, to be honest."
    
    EGuard "After all, I wouldn't want to be too much of an influence on your particular style of approach, you know."
    
    EGuard energetic grin "Make no mistake, guys who just listen to the advice of any ol' schmoe with two cents to give often end up working against their own natural potential."
    
    EGuard "And we wouldn't want that for you, right?"

    Fen "......."

    EGuard "Like, I've seen waaay too many drop-dead gorgeous guys who had just heap loads of lovin' to give prematurely crash n' burn their own careers."
    
    EGuard "And all because they decided to pull some lame–"

    stop music fadeout 1.0
    show fen 2 angry at right2
    with ease
    Fen 2 angry "...rrrrrRRHH!" with hpunch

    hide fen
    hide guards
    show bg alley2
    with dissolve
    "You pounce on him, unable to wait for him to finish up any longer."
    
    show guards energetic naked at center1:
        zoom 2.5
        ypos 1900
        xpos 1150
    show bg alley2_blur at truecenter:
        zoom 2.5
    show ratio1
    with dissolve
    "He falls to the cold, hard ground with you in surprise as you pull aside the folds of his uniform before hungrily burying your muzzle in his crotch."
    
    show guards energetic hard
    with dissolve
    "His dick springs to attention pretty quickly with you tickling the bottom of his tip ever so eagerly."
    
    play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
    play nsfw1 "audio/mid moan 1.ogg" volume 1.0 fadein 1.0
    EGuard "H-Huff...mmph, mmphh!"

    "Suddenly, all you can hear from him is the sounds of him whining for you in pure pleasure."

    hide guards
    show bg alley2_blur at top
    show fen hard hot2 at top behind ratio1:
        ypos 50
        zoom 3
    with dissolve
    Fen "What's wrong, sir? This is what a mouth is best used for, isn't it?"

    hide fen
    show guards energetic hot at top behind ratio1:
        zoom 3
        ypos -160
    with dissolve
    EGuard "Ooooh-yeeaah!!! Rffh! Mmm, your tongue's all wet and slobbery over my dick!"
    
    EGuard energetic hot2 "And that ass...Fuck, it's so good seeing the curves of that big thing shake from over here."
    
    EGuard "Rfh, I bet you do a ton of work to keep up a body that gorgeous, huh?"

    hide guards
    hide ratio1
    show bg alley2 at center:
        zoom 1
    with dissolve
    "You roll your eyes instinctively after seeing he's still got enough wind in him to go on yapping so much."
    
    "Hopefully, he's not paying your face enough attention to notice..."

    show guards energetic hard at top:
        zoom 2
        ypos -500
    show bg alley2_blur:
        zoom 1.5
    with dissolve
    EGuard "Me too, you know? Heh, check it out."

    "He tries to flex his arms for you, but looks a little dissatisfied by the results."
    
    "It seems like the position he's in right now under you doesn't allow for him to tense up his body much."
    
    stop music fadeout 3.0
    stop nsfw1 fadeout 3.0
    hide guards
    show bg alley2
    with dissolve
    "Then, suddenly, his expression lights up, as though he just got hit with a really great idea."
    
    "He asks you to get up for him, and with a confused eyebrow raised, you shrug and do what he says."
    
    show bg alley2:
        zoom 1.5
    with dissolve
    "The guard makes you stand with your back against the cold alley wall as he takes your exposed member into his dextrous grip."
    
    "You wince a little at how fast his paw does it."

    show guards energetic hard at top:
        zoom 2
    show bg alley2_blur at top:
        zoom 1.5
    with dissolve
    EGuard "Oh, my gods! That was so cute~ Haha! But don't be scared or nothing, puppy."
    
    EGuard "This is gonna be an eyeful for us both..."

    play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
    play nsfw1 "audio/light moan 1.ogg" volume 1.0 fadein 1.0
    show fen hard blush at left3 behind guards:
        zoom 2
        ypos 1800
    show guards energetic hard at right3:
        zoom 2
        ypos 1800
    show bg alley2_blur at truecenter
    show ratio1
    with dissolve
    "He closes the distance between you, slides his own dick into the hand that's also grabbing yours, and begins jerking the both of them together."
    
    "It feels really tight for you, your schlong being made to rub against his, squeezed around his rough, battle hardened fingers like this."

    "He tries flexing an arm again after getting a good rhythm going."
    
    hide fen
    show guards energetic hard at top:
        zoom 2
    show bg alley2_blur at top:
        zoom 1.5
    show ratio1
    with dissolve
    "This time, he looks very proud of the bulging bicep he's showing you and engages your eyes eagerly for a sign of what you think."
    
    "With sultry eyes, you nod your approval, and he playfully nudges you with his free hand as a way of saying, 'now you try.'"
    
    "You put both hands on your hips and show off to him back with your best frontal lat spread, which sends in swooning."
    
    "You start to let out a laugh as he pretends to fan himself dramatically, but it's cut short."
    
    hide guards
    show fen hard hot at center1 behind ratio1:
        zoom 2
        ypos 1600
    show bg alley2_blur at truecenter
    with dissolve
    "It kind of amazes you how good the feeling of both your sensitive parts stimulating each other is getting, and you can't help but just pant and moan over it."

    EGuard "Really feelin' it down there, sexy?"

    "All you do is nod as he whispers that in your ear, eyes closed and teeth clenched in a long grunt."
    
    "You don't want this to end just yet."

    hide fen
    show guards energetic hard at top behind ratio1:
        zoom 2
    show bg alley2_blur at top:
        zoom 1.5
    with dissolve
    EGuard "Aww, what's a matter? Don't wanna watch anymore?"
    
    EGuard "Scared of losing it too quick to me and all my beautiful...assets? Heehee!"

    show guards energetic hard at top:
        zoom 2
        ypos -500
    show bg alley2_blur at truecenter
    with move
    "He flexes his bicep again, but this time goes in to lick and kiss it for you."
    
    "You pry open one eye out of curiosity to see him smirk as he drags his tongue from deep in his pit all the way up over his rocky peak and back down again."
    
    "Eventually, he closes his own eyes as he continues doing this, and, strangely, seems to put you out of mind for some reason."
    
    "It's like he's getting lost in his own thoughts daydreaming now, and whatever it might be about is making him get even more happy and frantic."
    
    "And in between the frenzy of smooching sounds, you can hear him talking to himself."
    
    "Or is it...to you still?"

    EGuard "Mmph! Mmmmm...yeah, that's big."
    
    EGuard "Fuck, I forgot how long it was since I got this big."
    
    EGuard "Mm-Mm-Mmwaa! Huff. More. I want to get even bigger!"
    
    EGuard "For the Captain, mmmh! And the other guys. I love them the sooo friggin much, you don't understand!"
    
    EGuard "This whole body's a temple for them, and I just want to fill it with even more love!"
    
    play sound "audio/mid climax 1.ogg" volume 1.0
    show guards energetic hot3 at top:
        zoom 2.5
    show bg at top
    with dissolve
    EGuard "Oh! Oh, Captain! I-I-Aaaaahhh...Oh, fuck! Oh, fuck, I'm gonna–"

    hide ratio1
    hide guards
    show bg white
    with dissolve
    "His load busts all over you and him like a geyser raining down droplets of thick cream."
    
    hide guards
    show bg alley2 at truecenter
    with dissolve
    "It takes him maybe a moment to recompose himself after climax, but to your absolute surprise, his hand is still going with all the same speed and intensity."
    
    "The residual that leaks down his shaft naturally also gets all over yours, and makes the friction between your two frotting dicks and his hand very slick."

    show fen hard hot3 at top behind ratio1:
        zoom 2.5
    show bg alley2_blur at top
    show ratio1
    with dissolve
    Fen "W-Wait! Oh, no. I-It feels...too good."
    
    stop music fadeout 1.0
    stop nsfw1 fadeout 1.0
    play sound "audio/light climax 1.ogg" volume 1.0
    Fen "I can't–Hah!–I can't stop m–Ohh! Aaaaaaaaagghh! Ah!"

    "Despite your best efforts to make it last, the intense bout of stimulation is enough to send you flying over the edge."
    
    hide ratio1
    show bg white
    hide fen
    with dissolve
    "You erupt in much the same way he did, with big shots going everywhere between the two of you and then a messy trickle."
    
    show bg alley2 at center:
        zoom 1
    with dissolve
    "In the immediate afterglow, you realise he's made you pretty heavily tired."
    
    "And there's enough musk and sweat left lingering on your fur to warrant a full evening's trip to the bathhouse to get it all washed off."

    show guards energetic naked at center1
    show bg alley2_blur
    with dissolve
    EGuard "Woo! Dang, that was good."
    
    EGuard "Six-point-eight-out-of-ten for sure. Okaaay, welp, here you go."

    play sound "audio/payment.ogg" volume 3.0
    hide guards
    show bg alley2
    with dissolve
    "He tosses you a bag full of coins as payment from the pile of discarded clothes before making himself decent again."

    Fen "How... How are you not even sweating right now!?"

    show guards energetic grin at center1
    show bg alley2_blur
    with dissolve
    EGuard "Hmm? Oh! Hahaha! Honey, please."
    
    EGuard "You think that little workout we just had is enough to get me all hot'n bothered so that it shows?"
    
    EGuard energetic tongue "Maybe I should invite you to one of the monthly drill practises the Captain puts us through, so you get a better idea."
    
    EGuard "By the way, sorry if I might've said anything that sounded a little... well, weird while we were doing it."
    
    EGuard "My mind just sort of has a way of bouncing around from place to place when it's all excited and stuff."
    
    if guards_bond_ui == False:
        scene bg alley2
        with dissolve

        $ guards_bond_ui = True
        call bondlvup0800 from _call_bondlvup0800_2
    else:
        call bondexpup08 from _call_bondexpup08_2
        $ bondexp08 += 3
        EGuard energetic grin "But yeah, Big Boy, thanks for the awesome time! I just know you're gonna do great!"

    scene bg alley2
    with dissolve
    "Too fatigued to even try and find a way to interrupt him so you can return the compliment, you let him speak the last of his erratic thoughts at you."
    
    "And before long, he finally moves on."

    if eguards_sxp_1 == False:
        $ eguards_sxp_1 = True

        call sxp_up from _call_sxp_up_7

    else:
        pass

    $ fen_coins += 12
    play sound "audio/payment.ogg" volume 3.0
    "You received 12 coins for your service."

    jump day_end

label fen_tailservice_stoicguard:

    show guards stoic normal at right1
    show bg alley2_blur
    with dissolve
    SGuard "......"

    "You stand there, tail raised as you feel the guard eyes boring into you."
    
    "You begin to get a bit uncomfortable with the silence, but you notice the guard is rubbing the ample bulge in his pants."

    show fen 2 normal at left1
    with dissolve
    Fen "Hey, interested in tail service Sir? I enjoy..."

    "You pause for a moment to think about what to say, still a bit unnerved by the guards intense gaze." 

    Fen 2 smile "Showing my appreciation for all the hard work you guards do for the city?"

    hide fen
    hide guards
    show bg alley2
    with dissolve
    "Your voice goes up slightly as you end with a question. You wince at how foolish that statement sounded."
    
    "You hear a slight chuckle and you see the guard adjust his helmet before leaning his halberd against the wall." 

    show guards stoic grin at top:
        zoom 2.5
    show bg alley2_blur at top:
        zoom 2
    with dissolve
    SGuard "Mhmm..."

    stop music fadeout 3.0
    "The guard walks up to you and you can see the mischievous smile on his face..."
    
    show guards stoic normal at top:
        zoom 2.5
        ypos -1600
    show bg alley2_blur at truecenter:
        zoom 2
    with move
    "...and the even larger bulge under his clothe."
    
    "This one is by far the best equipped of any of the various other guards and you're wondering what this quiet one wants."

    "The answer comes quickly as he swifty grabs you by the shoulders and kicks your legs out from under you." with hpunch
    
    hide guards
    show bg alley2 at center:
        zoom 1.5
    with dissolve
    "You yelp in surprise, but the guard guides you to the ground where you end up on all fours, your tail still lifted high in the air."

    Fen "What the... what are you doing?"

    "You hear nothing but the slightly heavy breathing of the guard but..."
    
    show bg alley2:
        zoom 2
    show ratio1
    with dissolve
    "He grab the back of your pants and yank them down, exposing your tailhole to him."

    "Waiting for the feeling of that massive cock filling you, you tense up, preparing for what is surely going to be a sudden jolt of pain..."
    
    "...But instead you start forward slightly as you feel something warm against your behind."

    "You can't help but moan in pleasure as the guard's tongue licks you over and over..."
    
    "...Even washing over your balls."
    
    "You feel the guard's hand pushing your shirt up over your back and then over your head."

    "Relaxing, you writhe in pleasure under the guards expert administration."
    
    "After a while, he stops and you hear him stand to his feet and the unwapping of belt."
    
    "Then one word."

    SGuard "Steady..."

    show bg alley2_blur at truecenter:
        zoom 2.5
    show fen naked blush at left1, flip behind ratio1:
        ypos 2800
        zoom 2.5
    show guards stoic grin at right1 behind fen:
        ypos 2800
        zoom 2.5
    with dissolve
    "His hands grab your thighs and he leans over your back."
    
    "You can feel his hot breath over your shoulder. You try to relax as you know what's coming."
    
    play sound "audio/light gasp 1.ogg" volume 1.0
    hide fen
    show guards stoic hard at center1:
        ypos 2000
        xpos 1100
    show bg alley2_blur at center
    with dissolve
    "And come it does as with one mighty thrust, the guard fully buries his massive cock, into you." with hpunch

    "You gasp as a wave of pain washes over you and the guard pauses as if waiting for you to react."
    
    "The pain subsides soon enough and you feel a pleasant fullness as you get used to the cock deep inside you."

    hide guards
    show bg alley2_blur at truecenter:
        zoom 2.5
    show fen hard hot at center1, flip behind ratio1:
        ypos 3000
        zoom 2.5
    with dissolve
    Fen "I'm fine, go ahead, just be a bit gent..."
    
    play music "audio/light moan 1.ogg" volume 0.5 fadein 1.0
    play nsfw1 "audio/mid growls 1.ogg" volume 1.0 fadein 3.0
    play fuck "audio/fuck fast 1.ogg" volume 1.0
    play ball "audio/ball hits 2.ogg" volume 2.0
    Fen hard hot3 "Ah!" with vpunch

    "Before you can finish, the guard begins slamming into you."
    
    hide fen
    show bg alley2 at center:
        zoom 2
    with dissolve
    "Your claws dig into the ground, gouging into the cobblestones as every thrust sends shockwaves through you." with hpunch
    
    "You cry out once in both agony and ecstasy, but the guard's hand wraps around your muzzle, closing it."

    stop music fadeout 0.5
    SGuard "Shush..."

    "Nodding, the guard releases his grip, his hand returning to your hip as he picks up speed." with hpunch
    
    "Your head spinning from all the sensations, your arms give way, and your head and upper body slumps to the ground, your lower half staying up due to the grip of the guard." with hpunch

    "Minutes pass and your body tenses up and you feel an orgasm coming up, but the guard reaches down to the base of your cock and wraps around it." with hpunch
    
    "Your body spasms as it tries to cum, but the grip prevents it." with hpunch
    
    "You're not even sure exactly what the guard is doing to stop your orgasm, but it's simultaneously frustrating and arousing."

    Fen "C'mon, I want to..."

    "The guard ignores you and your body writhes in exquisite agony as you are denied the orgasm you crave." with hpunch
    
    "You feel the relentless assault on your ass continue." with hpunch
    
    "The guard keeps slamming full force into you, every thrust going as deep inside you as it can, hitting every button you possess and still the grip of iron prevents relief." with hpunch

    Fen "Please... let me cum."

    hide guards
    show bg alley2_blur at truecenter:
        zoom 2.5
    show guards fussy hot3 at center1, behind ratio1:
        ypos 3300
        zoom 2.5
    with dissolve
    "You feel the guard resting his head on your shoulder and hear the deep panting in your ear, which drives you even crazier."
    
    "Finally you hear him speak."

    SGuard "Whine, bitch."

    hide guards
    show bg alley2 at center:
        zoom 2
    with dissolve
    "Obliging, you whine like a lost puppy, hoping that satisfies the relentless guard."

    stop nsfw1 fadeout 0.5
    play sound "audio/mid climax 1.ogg" volume 1.0
    "Your submissive behaviour is what he obviously wanted as you hear a grunt and feel the guard's load filling your inside." with hpunch
    
    stop music fadeout 0.5
    play vocal1 "audio/light climax 1.ogg" volume 1.0
    "As he cums, he releases his grip and you immediately cum as well."

    "You can't help but moan as your body shakes and you feel the guard continuing to breed you like a bitch in heat."
    
    stop fuck fadeout 3.0
    stop ball fadeout 3.0
    "Finally, the guard slows down and then stops and you feel an emptiness inside you as he pulls out."

    show bg alley2 at center:
        zoom 1
    with dissolve
    "Sighing in contentment you begin to raise yourself up..."
    
    show bg alley2 at center:
        zoom 2
    with vpunch
    "...but a sudden foot in the centre of your back forces you completely to the ground."

    SGuard "Stay."

    "You whine again in compliance and the pressure on your back goes away as the guard removes his foot."
    
    "Wriggling slightly on the ground in discomfort, you hear the guard warpping his belt up..."
    
    play sound "audio/payment.ogg" volume 3.0
    "...And then the slight thud as a money pouch lands by your head."

    "You feel the guard gently scratch behind one of your ears before you hear him grab his halberd and begin to walk off."
    
    "As he does, you hear him say a few words."

    if guards_bond_ui == False:
        $ guards_bond_ui = True
        call bondlvup0800 from _call_bondlvup0800_3
    else:
        call bondexpup08 from _call_bondexpup08_3
        $ bondexp08 += 3
    

    scene bg alley2_blur at center:
        zoom 1
    show guards stoic smile at center1
    with dissolve
    SGuard "Good boy, I'll be back."

    hide guards
    show bg alley2
    with dissolve
    "As you slowly pick yourself off the ground to get dressed, you have to admit..."
    
    "You might be looking forward to it."

    if sguards_sxp_1 == False:
        $ sguards_sxp_1 = True

        call sxp_up from _call_sxp_up_8

    else:
        pass

    $ fen_coins += 20
    play sound "audio/payment.ogg" volume 3.0
    "You received 20 coins for your service."

    jump day_end

label fen_tailservice_look:
    hide fen
    show bg alley2
    with dissolve
    "Feeling a bit adventurous and seeking some 'fun' on your own terms, you wander through the back alleys, keeping an eye out for anyone offering tail services."
    
    "The atmosphere buzzes with quiet anticipation, and you're curious to see who might be available for a little excitement."

    #Make 2 pools over random encounters that do not overlap
    $ tailservice_look1 = renpy.random.choice(['rabbit', 'rabbit'])

    $ tailservice_look2 = renpy.random.choice(['bear', 'bear'])

    menu:
        "Today you see..."
        
        "Pair of bunnies." if tailservice_look1 == 'rabbit':
            jump fen_tailservice_rabbit

        "A white furred bear." if tailservice_look2 == 'bear':
            jump fen_tailservice_bear

label fen_tailservice_rabbit:

    if service_bunnies_top_sxp == False and service_bunnies_bottom_sxp == False:

        show bg:
            zoom 1.5
        show ratio1
        with dissolve
        "You catch sight of someone who piques your interest."

        "Or, in this case, a pair of someones."

        "Chatting amongst themselves behind what looks like an old, abandoned tool shop are two rabbits with mostly cream coloured fur."

        "One of them has red accents in places like his ears, cheeks, and tail, while the other has blue."

        "Both of them are dressed in little more than a matching pair of silky briefs and arm warmers, showcasing their skinny fit physiques."

        "From the looks of it all, you're sure you know what it is they're waiting for..."

        Fen "Heya! Nice day, isn't it?"

        "They both turn to acknowledge you from down the alley."

        "The coy smiles that creep onto their faces a moment later lets you know right away that they're interested in what they see."

        BlueBunny "Yeah, I guess it is a nice day, huh? Want us to make it a little nicer for you? ❤"
        
        RedBunny "Oh my gosh, big bro, stop it~! You didn't even say 'hello' first."

        BlueBunny "Whoops, my bad. Sorry, little bro, guess I got ahead of myself."

        BlueBunny "I'll fix that for you right now..."

        "As you get close, the blue bunny runs up to your side."

        "Neither one of them stands taller than your chest in height, but he makes up for it by hopping in the air to plant you a kiss on the cheek."

        play sound "audio/shock light.ogg" volume 2.0
        "The moment his lips make contact, you feel a faint electric jolt travel across your face."

        "His brother, all the while, watches your surprised reaction, licking his lips."

        RedBunny "Mmm, now that's more like it. My turn next!"

        "The red bunny dashes over to you, too, before suddenly dropping to his knees."

        "You barely register what's going on before he goes and traces his tongue against the bulge of your pants!"

        Fen "What the—Ah! Ahhh~!"

        play sound "audio/shock light.ogg" volume 2.0
        "That same weak electric shock passes through your junk this time."

        "You can't help but instantly go hard from the stimulation."

        RedBunny "Aww, how cute! He's excited already!"

        BlueBunny "Hard not to be with you around, little bro."

        "The blue one then reaches around and gropes you from behind."

        "He keeps the sensation going with his staticky touch spreading all across and in between your asscheeks."

        BlueBunny "How's about it, big pup? You interested in what we got to offer?"

        Fen "M-Mmph! Y-Yes! Yes, yes, I am!"

    else:

        show bg:
            zoom 1.5
        show ratio1
        with dissolve

        "You catch sight of those bunnies again."

        "Before you can say a word, they approach you eagerly, nuzzling against your side with playful attitude."

        BlueBunny "Hello, bro! Back for some fun again?"

        Fen "Yes, yes!"

    RedBunny "Neat! So, do you want us to take the lead on this, or do you wanna?"

    menu:
        Fen "U-U-Uhh..."

        "I want to top.":
            jump about_service_bunnies_top
        
        "I want to bottom.":
            jump about_service_bunnies_bottom
    
    label about_service_bunnies_top:
        "They both nod and giggle at your answer in unison before guiding you over to a sturdy crate next to the old tool shop's window."

        "With a playful little shimmy, the red bunny strips down out of his underwear and then goes over to help his brother do the same."

        "Even though they're still flaccid currently, their cocks look really long and snake-like, with their plump ballsacks complimenting them nicely."

        "You love how spoiled you are for bigger things..."

        "The blue bunny then sits down on the crate, lounging with his head resting on his hands, while his brother gets down on his hands and knees."

        "The red one presses his cheek against his brother's splayed inner thigh and starts to nuzzle it, and you get to watch his exposed ass shake in front of you."

        "They both moan and get more erect as this goes on, occasionally throwing demure glances your way."

        "Fuck, they just look so...so cute and vulnerable like that. And at the same time, so very tender and loving."

        BlueBunny "What's the matter, handsome? Aren't you going to help take care of my brother from behind?"

        RedBunny "Mmm, I treat all of my brothers with this much love. I want you to be my brother, too!"

        stop music fadeout 3.0
        "You don't need to hear anything more."
        
        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 1.ogg" volume 2.0 fadein 1.0
        "Letting out a hungry snarl by accident, you shuck down your pants and ram your achingly hard cock right into the red bunny's waiting pucker."

        play sound "audio/shock light.ogg" volume 1.0
        "The instant you do, you start to feel that familiar electric current swelling all around your dick as you thrust it in and out."

        "He's loose like he's done this so, so many times before, but the lack of tightness is made up for with the constant, gentle massage of that energy."

        "It feels like nothing you've ever felt before with people of their affinity."

        "It's so much more steady and controlled, though you're not sure if that's just because they're not very strong with it."

        BlueBunny "Okay, little bro, that's enough keeping me waiting. Show me how much you really need my love."

        "Just as you have that thought, though, the red bunny takes his brother's dick into his mouth and starts slurping it like his favourite candy."

        play sound "audio/shock light.ogg" volume 2.0
        "When that happens, another wave of electric shock passes through you, stronger than before."

        play sound "audio/shock light.ogg" volume 2.0
        "And then another, even stronger..."

        play sound "audio/shock light.ogg" volume 3.0
        "And then another...much stronger."

        #Electric shock noise
        play sound "audio/shock light.ogg" volume 4.0
        Fen "Yeow! Z-Z-Z-Zzzt!" with hpunch

        "Pleasure quickly gives way to and blends in with pain, as the earth now looks like it's quaking violently around you."

        "Yet, even still, you for some reason don't want to stop thrusting."

        "Like, it hurts and that's obvious, sure. But strangely, there's still a great deal of excitement coursing through your system beneath it."

        BlueBunny "Aww, look little bro. I don't think he can handle us together yet."

        RedBunny "Better—Mmph!—Better give him some help with that before he passes out on us, huh—Ugh!?"

        "You've lost track of how many minutes it's been now since your fur started to smell burnt."

        "But at some point, in the midst of your wild fucking, the blue bunny pulls you in by the shoulder and forces you into a kiss."

        play sound "audio/shock light.ogg" volume 2.0
        "When he does, you notice the strength of the electric current begin to even out drastically."

        "It's still definitely there and pretty strong, but it's no longer quite so intense and irregular as before."

        "It's as if the three of you now being linked together in an almost triangle formation has created a closed circuit for the electricity!"

        "You can't really stop to marvel at it, though, because now that the sensation's become steadier, you realise just how close you are to release..."
        
        stop fuck fadeout 1.0
        stop ball fadeout 1.0
        play sound "audio/light climax 1.ogg" volume 1
        "You let out a long and desperate moan right into the blue bunny's mouth and manage to thrust a few more times into his brother before you cum."

        "As your seed floods his juicy little rear to the point of overflow, the brothers break their connection first."

        "That lets you down off the charge slowly, as you're left to bask in the gentle stimulation for a bit as you finish up your orgasm."

        Fen "Holy...Huff. Holy shit..."

        RedBunny "Had a good time with us, new bro?"

        if service_bunnies_top_sxp == False:
            $ service_bunnies_top_sxp = True
            call sxp_up from _call_sxp_up_12
        
        else:
            pass

        Fen "Huff...You bet."

        BlueBunny "Good! That'll be 20 coins, please!"

        $ fen_coins -= 20
        play sound "audio/payment.ogg" volume 3.0
        "You pays 20 coins for the service."

        if service_bunnies_bottom_sxp == False and service_bunnies_top_sxp == False:
            "You've got to admit, you weren't expecting their service to be quite so expensive."

            "Although, it probably makes sense considering there are two of them and their talents must be considered quite special by someone."

            "Maybe they're worth revisiting someday when you know you definitely have the extra money to spare."

        else:
            RedBunny "Thank you! Hope you come back again, big pup!"

        jump day_end

    label about_service_bunnies_bottom:
        "They both nod and giggle at your answer in unison before guiding you over to a spot in front of the old tool shop's window."

        "With a playful little shimmy, the red bunny strips down out of his underwear and then goes over to help his brother do the same."

        "Even though they're still flaccid currently, their cocks look really long and snake-like, with their plump ballsacks complimenting them nicely."

        "You love how spoiled you are for bigger things..."

        "They tell you to take all your clothes off as well and get down on your hands and knees."

        "For a minute, it sounds like they're just teasing you for being naked out in the open as they poke and prod you from in front and behind."

        stop music fadeout 3.0
        "But then, you notice that they're both getting more erect over time, and their touches are slowly becoming rougher and more sensual."

        RedBunny "O–Kay! Let's dig in!"

        BlueBunny "One, two...!"

        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 1.ogg" volume 2.0 fadein 1.0        
        "They coordinate to force you to take both of them at the same time."

        "You're made to suckle on the red bunny's slender carrot-sized dick, while the blue one inserts his into your rear all in one motion."

        "At first, it really isn't anything all that impressive..."
        
        play sound "audio/shock light.ogg" volume 2.0
        "Until you start feeling that electric surge pass through you again."

        "The elating series of jolts bounces back and forth all throughout your body, swelling up enough to get to just before the point where it really hurts you."

        play sound "audio/shock light.ogg" volume 2.0
        "Pretty soon, your whole body is vibrating and just feels so activated all over. Your dick's rock hard and you feel energised enough to run a marathon!"

        "It feels like nothing you've ever felt before with people of their affinity."

        play sound "audio/shock light.ogg" volume 2.0
        "It's so much more steady and controlled, though you're not sure if that's just because they're not very strong with it."

        BlueBunny "Like our shock therapy, big guy?"

        RedBunny "Because of us indirectly touching, the voltage is just right enough not to be painful."

        BlueBunny "And it feels {i}so{/i} good for us too this way!"

        RedBunny "So, thanks so much for agreeing to be our cocksleeve. Hehe!"

        BlueBunny "Here comes more of our service ❤"

        play sound "audio/shock light.ogg" volume 2.0
        "Their thrusts inside you are shallow, but each one seems to ping another wave of that current through you."

        play sound "audio/shock light.ogg" volume 2.0
        "It's like you can tell whenever they're timed just right to hit each other, because your abs and spine briefly tingle in a way that's oh-so-good!"

        "It feels so good, in fact, that your body just craves more!"

        "Soon enough, you learn how to clench your cheeks and your jowls at just the right time to make sure they're in sync every time..."

        "And fuck, are you rewarded with maximum pleasure!"

        RedBunny "Ahhh~!"

        BlueBunny "The feedback's hitting so intense!"

        RedBunny "B-Bro! I'm already gonna—!"

        BlueBunny "No! Come on, this pup's making me feel so great, I wan—Ah! A-Ahh!"

        "Uncontrollably, you make them both orgasm into you at the same time."

        "Their long dicks fill you with a pretty large amount of rabbit seed, but that's not too surprising considering how worked up you got them."

        "The moment that they pull away and cut the current is when you finally decide it's time to join them in release."

        stop fuck fadeout 1.0
        stop ball fadeout 1.0
        play sound "audio/light climax 1.ogg" volume 1.0
        "You let out a half-howling moan as soon as the bunny pops out of your mouth like a pacifier, and you spooge all over the alley cobblestone, handsfree."

        Fen "Holy...Huff. Holy shit..."

        RedBunny "Had a good time with us, new bro?"

        if service_bunnies_bottom_sxp == False:
            $ service_bunnies_bottom_sxp = True
            call sxp_up from _call_sxp_up_13
        
        else:
            pass

        Fen "Huff...You bet."

        BlueBunny "Good! That'll be 20 coins, please!"

        $ fen_coins -= 20
        play sound "audio/payment.ogg" volume 3.0
        "You pays 20 coins for the service."

        if service_bunnies_bottom_sxp == False and service_bunnies_top_sxp == False:
            "You've got to admit, you weren't expecting their service to be quite so expensive."

            "Although, it probably makes sense considering there are two of them and their talents must be considered quite special by someone."

            "Maybe they're worth revisiting someday when you know you definitely have the extra money to spare."

        else:
            RedBunny "Thank you! Hope you come back again, big pup!"

        jump day_end

label fen_tailservice_bear:

    if service_bear_bottom_sxp == False and service_bear_top_sxp == False:
        Fen "So far, so quiet..."

        "Then, someone walked out from the nearby inn unexpectedly."

        Fen "ACK!"

        show bg at top:
            zoom 1.5
        show ratio1
        with dissolve
        "You are suddenly bombarded with the sight of a white-furred bear strolling out of the back of the nearby inn..."
        
        "...and right away your eyes fixated on their lack of undergarments."

        "White Bear" "Ahhh..." 

        "This bear seemed straight out of a snow-capped forest, as their beard was more icy than just being blue-haired..."
        
        "No wait, those were not ice-colored regular beard, those were icicles! Who would have thought?"

        "White Bear" "Well howdy, traveler. You here for some tail service?"

        Fen "Erm..."

        "White Bear" "You there? C'mon, it'll be fun! You a top or a bottom?" 

        "The bear was persistent, leaning onto a nearby box as if so confident of your choice in joining them for a morning romp."

        menu:
            "I would prefer to top.":

                Fen "I think I would prefer... topping."

                jump tailservice_bear_start

            "I would prefer to bottom.":

                Fen "I think I would prefer... being bottom."

                jump tailservice_bear_start

        label tailservice_bear_start:

            "White Bear" "Works for me. Let's do this!"

            Fen "WHOA!" with vpunch

            scene bg black
            with dissolve
            "Without skipping a beat, your consent got yourself hauled into the inn with the bear taking point."

            "Inside, your nose is immediately being assaulted with the various smells of people who have also had tail service, presumably last night."
            
            "It makes you a bit dizzy."

            Fen "H-hold on!" 

            "You started getting dragged along when hesitating, however."

            scene bg room3
            with dissolve
            "By the time you are given a break, you are standing within a simple bedroom."
            
            show bg at truecenter:
                zoom 1.5
            show ratio1
            with dissolve
            "There is not much inside but a bed that is ruffled enough to look recently used."

            "White Bear" "C'mon, boy, you want this, don'tcha?" 

            "The icy bear sounded impatient, but they were at least caring enough to consider your feelings."

            Fen "I just...th-this is a little fast and I..."

            "White Bear" "Relax. It's too early for some of that backalley action. Indoors is more cozy."

            "You rub the back of your head, still processing this happening as it was all going on so quickly."
            
            "Your eyes dart to the bear's cock, but you catch yourself before you stare too blatantly."

            Fen "I was j-just exploring is all...! I heard about this place and...well..."

            "White Bear" "...oh, you're a virgin!"

            "That is not at all what you were implying."

            "White Bear" "Hahahahah! That's adorable! Wanted your first time with a quick lay with a real man! Get the experience under your belt for your friends!"

            Oran "It's alright, boy, Oran's gonna treat you right. Consider that much free of charge!"

            stop music fadeout 3.0
            "Oran steps up to your face and pulls your shirt up, slowly working your body to nudity while he remains bottomless."

            "Despite being around Terrance and Gunther, you feel oddly anxious about standing there in no clothes with this guy, covering yourself as best you can."

            Oran "Still a li'l scared, huh? Don't worry, I got something that'll help ya ease up."

            Oran "I like to think of it as a therapy thing. It's my best asset after all~." 

            "Oran comes in closer, reaching in to grab your hand and guides it to his butt."

            Fen "Woah..."

            "Your heart races as your warm fingers touch cool white fur. The coat brushes against your palm with a cathartic softness that draws you in to grip more firmly."

            "The plush fur surrounding Oran's butt does little to cushion out the malleable squishiness below the fluffy surface. You would sink your fingers into it as well."

            Fen "{i}'Goodness...!'{/i}" 

            "You were feeling up a stranger's butt, within minutes of you two having just met!"
            
            "With each passing second, your arousal grew more obvious, but your hesitation makes you stop."

            Fen "Uhm..."

            "Oran catches onto your tentativeness and asserts a tone of reassurance."

            Oran "Don't be ashamed now, boy. We're here to get busy, not show off."
            
            Fen "R-r-right..."

            Oran "Do you want me on top-"

            "Oran proceeded to flex, showing off their bulky muscles that accentuated their thick limbs but also made their gut stand out considerably."
            
            "Their cock twitched while on display, drawing your eye to it again."

            "You had to force yourself to look up from it after nearly tracing along the veins throbbing along its side and sucked in some saliva that tried to ooze out."

            "Being a bear, their chest looked pillowy, like you could sink your face in there and fall asleep right away."
            
            "Their belly is pressed beneath their pectorals, round and prominently defined."

            Oran "-or...do you want me under you?"

            "Oran turns away and bends over, showing off his sizable butt in more clear detail."
            
            "You can see that the fur did not tuck away the curvature, and it was easy to track where one may find his taint."

            "Oran took the view one step further and spread his cheeks apart for you to see his hole - taut but not exactly unused."
            
            "The air is filled with a promising musk that tickles your nose as he stands there, ready."

    else:
        "You spot the white bear at his usual spot."

        "Naked, of course."

        Oran "Howdy, [name]. Here for more tail service?"

        Fen "Y-yeah."

        Oran "God boi~ Let's do this!"

        Fen "WHOA!"

        "Without skipping a beat, your consent got yourself hauled into the inn with the bear taking point."

        scene bg black
        with dissolve
        "Inside, the air is thick with lingering scents of tail service, alcohol, smoke, and other dizzying aromas."
            
        "Before you know it, you're back in the same bedroom as last time."

        "Oran comes in closer, reaching in to grab your hand and guides it to his thick bear meat."

        Oran "Do you want me on top today-"

        "Oran proceeded to flex, showing off their bulky muscles that accentuated their thick limbs but also made their gut stand out considerably."
            
        "Their cock twitched while on display, drawing your eye to it again."

        "You had to force yourself to look up from it after nearly tracing along the veins throbbing along its side and sucked in some saliva that tried to ooze out."

        "Being a bear, their chest looked pillowy, like you could sink your face in there and fall asleep right away."
            
        "Their belly is pressed beneath their pectorals, round and prominently defined."

        Oran "-or... under you?"

        "Oran turns away and bends over, showing off his sizable butt in more clear detail."
            
        "You can see that the fur did not tuck away the curvature, and it was easy to track where one may find his taint."

        "Oran took the view one step further and spread his cheeks apart for you to see his hole - taut but not exactly unused."
            
        "The air is filled with a promising musk that tickles your nose as he stands there, ready."

    menu:
        "Have Oran under you.":
            jump tailservice_bear_top

        "Let Oran on top.":
            jump tailservice_bear_bottom

    label tailservice_bear_top:
        "As you weigh your thoughts on each option, you find yourself much more easily gravitating to Oran being under you."
        
        "Both the thought of laying on someone to top them and the sight of them bent over swaying your choice."

        Fen "Under! U-uh, yeah, under."

        "Oran snickered at your outburst before wiggling their buttcheeks towards you."
        
        "Your drool comes back with a vengeance, seeping past your lips before you can lick them dry."

        Oran "Well how 'bout you show me why I should be under you, boy~"

        Fen "..."

        "With as much heft yet some thought put into it, you walk up and shove Oran onto the bed in front of them-"
        
        "Being mindful not to make them hit the headboard but otherwise asserting yourself all the same."

        "He lands perfectly onto his stomach, which keeps his ass hiked up in the air for you to ogle."
        
        "You can see it wobbling in place for a few moments before coming to a stop, so entrancingly fat..."

        Fen "Sheesh...How do you get it to be that big...?"

        "Oran gives you a wink."

        Oran "A bear's got some secrets...But I bet you got an eruption tucked in there~" 

        "Such subtle vulgarity has you heated up, cock so hard that it hardly moved an inch as it throbbed in the open air."

        Fen "Wouldn't you like to know...?"

        Oran "Oh now I'm dying to know for sure, boy~"

        "Feeling less tentative, you relax yourself and breathe in the somewhat rank air within the bedroom."

        "You climb onto the bed and position yourself somewhat over Oran's back."
        
        "You grab his butt and spread them apart to make room for your cock. A faint shininess shows the bear was already lubed up."

        "Oran's face shows a mix of amusement and not-so-hidden glee at how you cupped his ass."

        Oran "You ready, boy?" 

        "Your heart is loud in your ears, your cock slowly wedging into Oran's asscrack."
        
        "Your body twitched with anticipation, but you were in fact ready. This is it. You were about to fuck the bear with all you got!"

        Fen "Yep..." 

        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        "Your cock pushes in, prompting a grunt out of Oran that sounded too pleased to be discomforted from your size."
        
        "He keeps up his grin and gives you another wink."

        Fen "Unnnnmmph..."

        Oran "Nice and meaty, I like it~"

        "Oran lets out a baritone moan as you press deeper, a sign you have gotten far enough to brush their sensitive spots. - a lesson from Odachi - "
        
        "You idle there for only a moment to ride out the sudden clench before proceeding on."

        "You soon reach the point where no more can fit on the first go, surprised at how easily you slid right through."
        
        "Oran must be a very frequent bottom."

        Fen "Mm-mmmh..."

        Fen "{i}'Feels so good...'{/i}"

        "The cool interior was very enrapturing, complimenting the heat radiating off of your fully erect cock."

        "The smooth insertion jolts your hips into moving back out of reflex from the pleasure encapsulating your shaft."

        Oran "Hoooo, yeah~"

        "Oran's face fills your topside view, goading you on with his moxie shining on his face with every inch of you buried in."

        play ball "audio/ball hits 1.ogg" volume 2.0 fadein 1.0
        "Once you have your fill, you pull back far enough for your liking, and you begin to fuck the bear."

        "{i}PLAP PLAP PLAP{/i}"
        
        "{i}PLAP PLAP PLAP PLAP{/i}"

        Fen "Unnnngh..."

        Oran "Hrrrrgh, yeah...give it to me good, boy..."

        "{i}PLAP PLAP PLAP PLAP{/i}"

        "{i}PLAP PLAP PLAP PLAP PLAP{/i}"

        Oran "Fuck...just like that..."

        Fen "Mmmmnn-nnnh..."

        "The pleasure is phenomenal. Every time you push in or pull back, it is like Oran's ass puts you in a chokehold, urging you to work hard."

        "Your face is dotted with sweat already, but it was more from the humid air of the situation as you indulge in the bear's ass."

        "Your motions naturally speed up, the pace growing more heated by the second."
        
        "You can feel Oran's butt bouncing and jiggling against your hips with each thrust."

        "You begin breathing heavier. The effort was getting to you already. Faintly visible puffs of hot air erupt from your mouth."

        Fen "Hrrrrgh...GRRRRRFH!" 

        "Oran was not loosening up, remaining snug around your cock as you got into a good momentum."
        
        "Your hands shift from keeping him spread open to just holding onto something."

        play fuck "audio/fuck fast 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 2.0 fadein 1.0
        "Your indulgence compels you to go harder, making Oran moan more frequently while your grip on him grows more possessive."

        "{i}PLAP PLAP PLAP PLAP PLAP PLAP{/i}"

        Oran "Ooouuugh...hnnnf~"

        "The bear's moaning pushes you to go all-out, instincts giving you the necessary guide towards a pleasurable pace."

        "Your cock hardly leaves Oran's hole. Making it nice and hot inside, the air grows thick with the stench of your actions."

        Oran "Don't be 'fraid now, youngin'. I can handle a little roughin' up..."

        Oran "Once you start, you better not stop until we're finished, ya hear?" 

        "Oran's encouragement was all you needed to release the tentative power behind your thrusts."

        "No need to be gentle? That was fine with you."

        "Your hips get straight to work, gyrating so fluidly that you can hardly tell what it felt like to not be inside Oran's hole."
        
        "Your fingers sink into the fat of his ass, providing the leverage to slip into a much more assertive pace."

        Fen "Hhhhhfff...hhfff...hnf...ghhhuh..." 

        "You puff out small plumes of fire, and your body moves involuntarily until you are bear-hugging Oran until you slowly press down on his back."

        "Within seconds, you mount Oran's body and your thrusts shift straight forward instead of at an angle."

        Oran "Hnnng...C'mon...b-boy..."

        "Oran was getting impatient."
        
        "At this rate, his ass was cushioning a genuine onslaught from your hips, and his experience really shined in being able to handle your vigor."

        "His buttcheeks ripple at every impact, so deliciously hypnotic that you almost wish you could see for yourself but otherwise riding out the 'wavy' sensation against your thighs."

        "Oran's face begins to scrunch up with repressed intention, and his hole quivers against your cock."
        
        "He's close, but he can put it on hold for someone on a whim."

        Oran "I know you got a lot in ya...! L-let's...hrrrfh, have it!"

        "He was right, you had the will to truly give it your all and no reason not to."
        
        "So you finally allow the instincts to take over, making your hips barely visible and your vision haze over."

        "You can feel the pressure of an orgasm rising up within you, a sign that this would soon end."
        
        "Your cock begins to spray hot precum inside of Oran, eliciting another pleased groan out of the bear."

        "Your thrusts have reached their true potential, the fastest you can go and the hardest you can manage."

        "Oran shows no sign of being in pain, feeding into your desire to bed him with no mercy."
        
        "The room echoes with the sound of your lust, drowning out everything else around you and deafening meaningless ambience."

        "PAP-PAP-PAP-PAP-PAP-PAP-PAP"

        Oran "Fuck...fff-huck, I'm gonna..."

        Oran "GHHHAAAHH...!"

        "Before you could regard Oran's words, the bear's hole suddenly clamped shut around you, nearly slowing you down but not tight enough to hinder the might behind your pace."

        "The faint smell of salt wafts into your flared nostrils and a growing dampness spreads towards your toes."
        
        "His ass clenches rhythmically and hypnotically, as you can follow it up with a thrust each time."

        "Soon his cum would become visible beyond the snow white fur of his nude bottom half, showing off just how much he himself had to offer from a hands-free load."

        "As this occurs, the tightened softness of Oran's hole begins to tempt you towards the edge, driving you towards your orgasm, abandoning your rhythm in the search for release."

        Oran "Auuuugh..."

        "One last cry from Oran, and his hole slowly relaxed, allowing you to fuck him back at relatively normal speed, giving you that final push while your body curls inward."

        Fen "Yes...Hng...gonna...blow..."

        "You can feel it deep within your being."
        
        "Everything that has happened thus far has led to this inevitability."
        
        "Your balls were churning, revving up the load that would send things off with a bang."

        "Once you are back to your true speed, you feel the compelling urge to bite down on Oran's neck, more impulsive than a need."

        "Oran falls into a slump and exposes it as well, practically giving you the opportunity."

        "{i}HOMF{/i}"

        "Before you can waste any further time, your teeth sink into Oran's neck, embedded far enough to stay but not to draw blood."

        Oran "GUH!"

        Oran "Y-you're a...beast..."

        "Oran's compliments are distant in spite of his proximity to your ears."
        
        "Your mind was honed in on one thing - finishing the task at hand."

        "Your hips are back at a blur, pummeling the bear's butt to the point where the noise drowned out the world around you."
        
        "Your orgasm was gnawing at you, progressive in rising up but at least surely coming."

        "{i}PAPPAPPAPPAPPAPPAPPAPPAPPAPPAPPAP{/i}"

        play sound "audio/light climax 1.ogg" volume 1.0
        stop fuck fadeout 1.0
        stop ball fadeout 1.0
        Fen "UUNNNNNNNFH!" with hpunch

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "Before you knew it, the explosive blast of a climax shot through you before you could register it."
        
        "Your entire body tensing up from head to toe to the point of trembling like you were hit with a frigid wind."

        "The first shot lands deep inside, but you can hardly feel it."
        
        "The rest are more rapid and runny, however, like massage oil and spread all over the place inside of Oran."

        "Your balls are scrunching, able to sense the strength of the way they flex from how much white fills your eyes from each round of volleys that escape your cock into Oran's ass."

        "The bliss coursing through your veins incite you to hump, leaving the follow-up that did not come through the initial stream to spread and smear around Oran's hole and taint instead."

        "{i}SPLRT SQULCH SPLOOSH{/i}"

        "The harmony of cum oozing out of Oran, shooting through his ass, and pooling inside his body was pure music to you."
        
        if service_bear_top_sxp == False:
            $ service_bear_top_sxp = True
            call sxp_up from _call_sxp_up_14
        
        else:
            pass
            
        "A sonata you wanted to hear all the time - at least, in your current state of mind."

        stop music fadeout 3.0
        "This sensation was very sudden, but came off as normal all the same, so you let it pass naturally."

        Oran "So h-hot..."

        "Within time, the bear's breathing slowly comes into your perception of sound, and you too come to recover from such an overwhelming orgasm."

        "The bedroom fills your eyes and you steadily return to some form of rationale as your afterglow hits."
        
        "A tingle coursing through your mind from the residual pleasure hanging off your hypersensitive cock."

        Fen "Hooooh..."

        "You were winded, not exactly tired. You can feel your cock still throbbing with alacrity, as if awaiting another round."

        Oran "Unnngh..."

        "Oran stirs up before too long passes."

        Oran "You got some spunk t'ya, boy..."

        Oran "I like that~"

        Fen "Thanks..."

        Fen "You have a...great butt..."

        "The faltering compliment was not lost on Oran as he began beaming with pride."

        Oran "Best ass in the alley, I'll tell you that."
        
        Oran "I can get anyone into it, all this heft really gives me a good edge~"

        if service_bear_top_sxp == False:
            $ service_bear_top_sxp = True
            call sxp_up from _call_sxp_up_15
        
        else:
            pass
        "You nod your head in agreement."
        
        "You try to pull out, but are met with the resistance of Oran's butt muscles clenching down on you instantly."

        Oran "Hold on now, who said we were one-and-done?"

        Fen "Oh?"

        if service_bear_top_sxp == False and service_bear_bottom_sxp == False:
            Oran "You're payin' to top after all. Gotta treat your first time just right, y'know?"
        
        else:
            Oran "You're payin' to top after all. Gotta treat you just right, y'know?"

        "At the mention of pay, you look at your clothes."
        
        "Your allowance resides inside, some spare coins from all the hard work you have been doing up until today."

        Oran "Show me the coins and I'll show you a little secret I keep for those good boys I get in here~"

        "The playful tease oddly excites you to the point of your tail wagging and you bite back a reflexive bark."

        "You extract your cock from Oran before grabbing your pants, fishing out your sack of coins."

        Oran "It's 10 by the way. Usually 20 coins, but I can't let a cute guy like you feeling drained in your purse for that."

        Fen "Th-thanks..."

        $ fen_coins -= 10
        play sound "audio/payment.ogg" volume 3.0
        "Blushing the whole while, you hand over the money without any objection."

        Oran "Thank you, thank you."

        Fen "Of course."

        Oran "Now about this surprise..."

        "Oran reaches over to the right-hand corner of the bed, pulling the mattress up to show a faint glowing red residing there."

        show bg room3_blur
        show growth_relic at truecenter:
            zoom 2
        with dissolve
        "He pulls out a strange object that makes you squint when he brings it into view, the light emanating from it drawing your attention."

        "A heart-shaped, crystalline relic resides in Oran's hands when the light settles in your vision."

        Fen "Is that a treasure from nearby dungeons?"

        Oran "Sure is, boy."

        Fen "Where'd you get that? It's so..."

        "You stare at it in awe."
        
        "A treasure truly worthy of adventurers willing to risk their lives for its allure."
        
        "Your eyes filled with its visage the longer you looked."

        Oran "An adventurer gave me this when they wanted to spend their last night in Felda getting laid."

        Oran "Didn't tell me what it did, but I found out for myself when I had an off day to myself."

        Oran "Wanna see?"

        menu:
            "Yes!":
                jump tailservice_bear_hyper

            "Maybe next time...":
            
                hide growth_relic
                show bg room3
                with dissolve
                Fen "Maybe next time... I'm too spend..."

                Oran "Heh, no pressure. I'll be around whenever you get the urge."

                "The two of you cuddle for a while, basking in the afterglow."

                "You spend a bit longer enjoying the feel of Oran's round belly before you're ready to head out."

                "Once you've cleaned up as best as you can, you put on your clothes and prepare to leave."

                Oran "See you around, boy~"

                jump day_end
                
    label tailservice_bear_hyper:
        
        Fen "Yes!"

        "The thought of an relic having an applicable power that had room to be applied to this scene gave you all the excitement."

        Oran "I knew you'd like it. Now hold still boy."

        hide growth_relic
        show bg room3
        with dissolve
        "Oran turns around and lays your cock on his palm, the crystal slowly being lowered to touch your throbbing girth."

        "The crystal, despite being in a warm room, is cold to the touch, but only gives a slight shiver to you when it makes contact."

        Fen "HMM!?" with vpunch

        "As soon as Oran presses it harder, your cock throbs with a hardness you never felt before, only to steadily swell up in size before your eyes." with vpunch

        "Your length extended close to the likes of Terrance, before slowly coming to a stop."

        "Your girth reaches a thickness that was juicy enough to make one drool on sight with it, assuring you that there would be no shortage of peeks if you ever found something to cover up with."

        "Your balls slowly crawled up to match to scale, refilling with the seed you spent and increasingly growing fatter by the second."
        
        "The growing weight tugging against your extremities before settling just over your knees."

        Fen "{i}'This is...incredible!'{/i}"

        "A treasure capable of such power was certainly worth keeping a secret."
        
        "This only refuels your curiosity about being an adventurer."

        "Oran pulls the crystal away and your growth stops immediately."

        "Your cock was more than likely bigger than most in Felda, both long enough to be a third leg and thick enough to boot."
        
        "Your balls feel laden, full of unspent seed despite having emptied your reserves minutes ago."

        "The strength behind having such a size slowly hits you and you begin breathing harder as a result."

        Fen "I feel...funny..."

        Oran "Hahahahahah."

        Oran "Well I wouldn't expect anyone to just be able to handle all that meat on the first try. It'd be a miracle, I'll tell you that."

        Oran "But don't worry, you're supposed to feel like that."
        
        Oran "Part of your body adjusting to having all that much meat 'tween your legs. You definitely came out of that looking like a prize yourself, boy."

        Fen "Phew..."

        "You begin sweating profusely, the room suddenly feeling hotter."
        
        "You look between Oran and your own massive junk, visible clouds of its scent radiating off of the surface like it was fresh out of a cauldron of soup."

        "The dizziness sets in more profoundly, making you fall onto your back."

        "Oran fills your view of the ceiling while standing over you, your cock pulsing as it stands tall between his thighs."

        Oran "Looks like I'll be the one on top this time. Always wanted a big hung boy like yourself for my li'l treats~"

        "The bear climbs onto your body, straddling your waistline and knowingly wedging your new cock between his asscheeks."

        "Every throb felt like a full-body cumshot."
        
        "Euphoria rushes through your veins and you can feel the drizzle of precum running down your cock as sweat beads off of your face and back."

        Oran "I'm gonna be enjoying this~"

        "You watch Oran rise up, bringing his hips away from your body while his ass steadily comes over your dick."
        
        "By the time he makes it to the tip, you already miss the way the soft fur of his butt cradled your meat."

        Oran "Hup!"

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "With a bit of a start, Oran drops his ass back down, engulfing your cock in the ruins of the mess you made earlier."

        Fen "HNNNNPH!"

        "Despite having already fucked, Oran's hole was back to having a vice grip on you - as a result of your enhanced girth."
        
        "But on top of that, you reach far deeper than your normal size achieved, as a new chill contrasts your heat."

        "A phallic bulge coincidentally makes itself known from Oran's belly."

        Oran "Hooooh....hough-kay...Easy does it."

        "Oran's eagerness can barely hide inexperience from this."
        
        "You watch on, paralyzed to the bed, as he tries taking more of you inside, making the abdominal bulge bigger and more defined in tandem."

        "You realize that it is your cock doing that and whimper in increasing ecstasy."

        Fen "HNGH! RRRFH!"

        "The more of your cock Oran gets inside of his body, the better it feels."
        
        "You crave the idea of him being able to take it all, drooling onto the mattress involuntarily, and feel your hands make their way to his hips."

        "You pull down the second your hands make contact."

        "{i}SHLRP{/i}"

        Oran "RRRRRNNNFH!"

        "Oran's face scrunches up, and a moment's reprieve makes you believe you hurt him."
        
        "You panics, nearly enough to make you go flaccid while still being fully buried inside the bear."

        "Oran relaxes moments later and gives you a reassuring wink before gyrating his hips."

        Oran "I've been..t-training for this. Don't gotta worry 'bout hurtin' me none."

        Oran "But I think you need to get ready for the best ride of your life, boy. I don't slow down for big cocks."

        "That leaves an unnerving pit in your belly and you gulp down in response, staring wide-eyed as Oran slowly makes his way back up your cock."

        "An impatient feeling fills you watching more and more of your cock reappear in your peripheral vision."
        
        "You want to see it all gone, deep inside of Oran again. A growl slips into the tone of your breathing."

        "Your hands make their way back to Oran's hips, but he grabs your wrists."

        Oran "Ah ah ah. It's my turn, boy. Bad dogs gotta wait."

        "Your hands are yanked further up and placed onto Oran's butt, too far to influence his pace yet too alluring to pull away."
        
        "The familiarity of his plush ass renders you content - for now."

        "Oran makes it halfway up your cock before slowly coming back down, re-enveloping your shaft with his guts."
        
        "To think he can just swallow it all up his hole with growing ease..."

        "Once more, the need to hump crosses your mind, but you are distracted when Oran plants his hands on your fluffy chest."

        stop music fadeout 2.0 
        Oran "Time to milk me a dog like a cow~"

        play fuck "audio/fuck mid 1.ogg" volume 3.0 fadein 1.0
        play ball "audio/ball hits 1.ogg" volume 3.0 fadein 1.0
        "Oran barely allows you to rest every inch of your cock inside of his ass before rising back up, only letting out a significant portion from his depths before you were slipping back in more firmly."
        
        "{i}SH-PAP SHLLLK SH-PAP SHLLLK SH-PAP{/i}"

        "The methodical pace of Oran pushing his ass down on you and letting your cock pulse and spray inside of him before rising up slowly was a tantalizing endeavor."

        "You can practically feel the precum being siphoned out of you as he relentlessly plants his ass into your lap, smothering your cock with his massaging muscles keeping your tender flesh placated."

        "With his hips gyrating, it was easy to follow along like watching a metronome in motion, bobbing your head with each drop that sent more lightning-fast bliss through your nerves."

        Fen "Unfh...Guh...Hhhh...auhhh..."

        Oran "Feels good...don't it, boy?"

        "Hearing you moan made Oran go a bit faster, no doubt trying to incite a much louder reaction from you."
        
        "And he succeeded thanks to your mind still adapting to being equipped nearly as big as Terrance."

        Fen "UNGH!"

        Oran "'Bout to make you a singer t'day, boy. Hope you don't mind screamin'~"

        play fuck "audio/fuck fast 1.ogg" volume 3.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 3.0 fadein 1.0
        "Oran's momentum slowly picked up speed, showing the progress of his capabilities of handling your enhanced cock from tip to base."
        
        "You grow obsessed over the way his hole clamps over the last inch."

        "The constant slam of his soft ass landing on your thighs brings veins to your balls, pushing them to work overtime to provide the precum necessary to visually represent your sky-high arousal."

        "Oran squeezes your pecs every time you take longer than a millisecond to blink."

        Oran "Lookin' cute down there boy...Don't be shy now...lemme hear how much ya like it~"

        "You can barely form words with Oran riding you, getting to a point where the mattress was starting to make a constant {i}THUD{/i} every time he took all of you in."

        "{i}SHLRP SHLRP SHLRP SHLRP SHLRP SHLRP SHLRP{/i}"

        "Oran was allowing more of you out of his ass, you felt more of the room's air against your red-hot cock."
        
        "But he was taking you right back inside as quickly as possible, trapping you inside their voracious depths."

        show bg room3_blur
        with dissolve
        "Your eyelids flutter as you dance between being conscious and passing out..."
        
        "As time goes on and Oran continues delivering physical contact, you remain in a state of uplifted-ness - like you're flying."

        "The white in your eyes from earlier seeps into your vision, promising you that you were going to have your orgasm soon, pulsing like a fireplace being given more wood to burn with."

        "Oran vice grips your chest before somehow managing to go harder, knocking the air out of you and keeping your mouth wide open."

        "He leans in for a kiss."

        "Oran makes the plunge, descending upon your mouth and takes your lips for a smooch, returning it just in time to make sure he presses in more affirmatively."

        "He did not use tongue, just lips, which allowed you to breathe while he was slamming down onto your lap still, and also bring his cold beard to your chin."

        "The droplets running off such frosty facial hair has you shivering under him, but at no point does it take away any of the heat in the air, nor does your cock recoil from it."
        
        "In fact, it just makes you throb in defiance."

        "The moment's intimacy leaves saliva connecting your lips with his when Oran pulls back."
        
        "You watch him swab his mouth clean and smirk down at you, your reflection barely visible in the icicles under his chin."

        Oran "You're lookin' to erupt, boy...I can feel it inside, right here~"

        "Vocalized descriptions of your own reach inside Oran's body brought a shudder to your spine."
        
        "You truly were this monstrous cock-bearing beast that he had toted you up to be earlier."

        "And you loved it."

        "With your new size, you can feel a hint of your inner glans spreading open, allowing more and more of your precum to stream into Oran's belly."
        
        "It is too much, most of it flushes out of his ass."

        "And then it stopped. One pulse tells you that you are near and there is no going back to buildup from here."

        Fen "Auugh...mnf...mmmh...MMMMMNPH!"

        Oran "That's it boy...don't even think about holding it back..."

        Oran "I want all that good stuff inside me...I better look as big as that rhino at the bathhouse when you're done~"

        "The mental image of Oran managing to stomach your load was all you needed to guarantee that he would make you cum."
        
        "No holding off, no trying to downplay it, the bear was milking you for everything you got."

        stop fuck fadeout 2.0
        stop ball fadeout 2.0
        play sound "audio/light climax 1.ogg" volume 1.5
        Fen "AHHHHH!" with vpunch

        play music "audio/Schlop.ogg" volume 3.0 fadein 1.0
        scene bg white
        with dissolve
        "With a coincidental eruption, you feel your cum blast from your cock while it resides within Oran, the bear stopping to make sure they were completely wrapped around you."

        "The first volley is visible, pushing out against Oran's belly like one pumping water into a barrel."
        
        "You can feel the viscosity and volume as your cock resides within the growing pull of semen."

        "{i}SPLOOSH{/i}" with vpunch

        Fen "Oooough..."

        "Each successful volley makes you gasp. The white in your eyes nearly blinds you from the nirvana coursing through your body."

        "{i}SPLOOSH{/i}"with vpunch

        "Oran's belly slowly loses the phallic bulge and grows bigger instead, making more room as you remain inside to spray and erupt as a volcano would, slowly but surely weighing you down."

        Oran "All this hot spunk...all for me~"

        "{i}SPLRSH{/i}" with vpunch

        "The bear's moxie holds no bounds."
        
        "You give him more, knowing that you cannot resist the influence of his ass. You throw your head back once your orgasm reaches the tipping point."

        "{i}GLORSH{/i}" with vpunch

        Fen "AhhhhHHHH!"

        "The pleasure is immeasurable."
        
        "Your eyes almost succeed in rolling into the back of your head from your continued orgasm, trying to ride out the insurmountable euphoria making your balls pulse and send more cum into Oran."

        "The bear's belly becomes a dome, growing more and more taut by the second as you continue to fill him and fill him and fill him beyond anything you could have ever imagined, slowly losing sight of him."

        "{i}GLRSH...GLRSH...GLRSH...GLRSH...{/i}" with vpunch

        stop music fadeout 3.0
        "The echoes of your bellowing climax slowly fade as you come to a calm, just barely in the nick of time from the contented look on Oran's face."

        show bg room3 at truecenter:
            zoom 1.5
        show ratio1
        with dissolve
        Oran "Now that's a fill up~"

        Fen "Guuuhhh..."

        "Your brain is still recovering, mind racing with all sorts of imagery - whether recent experience or distant memory, you cannot tell through the blurriness."
        
        "You grunt when your cock throbs in the afterglow."

        Oran "You still up? Great, we're just getting started~"

        "More? You only paid ten coins for a round of topping, and not only were you given a second round for free, there was even more coming your way?"

        "Oran's generosity is noted right before he sends you into another fit of paralysis from standing up suddenly, extracting your cum-coated cock from his ass."

        "{i}SHPLRT{/i}"

        "Cum ejects from his hole, your cock having acted as a stopper for the excess that had not made its way into his stomach."
        
        "His ass was matted down, a full mess of creamy white that stained the edge of the bed and the floor."

        "Your cock was still hard and towering over your body while your cum oozed down towards your crotch."

        Fen "Hnnnngh..."

        Oran "I think I earned my turn...What d'ya say?"

        Fen "Unnnnh..."

        "To be frank, if Oran was doing all of this for you, why would it be a bad idea?"
        
        "You have the day off, and everyone else is busy with their thing. Plus, it may just be free, which means coins saved."

        "You, unable to form words at the moment, nod your head in agreement."

        "Oran smiles and winks at you, grateful for your answer before he grabs your legs."

        Oran "Always wanted to fuck someone with a bigger cock than me...Look at all this."

        Oran "Can barely keep my mouth away from it~"

        "Oran shows just how tantalizing it is to keep away from your mighty meat as he licks across its surface, prompting it to pulsate similarly to something in an earthquake - trembling with great power."

        Fen "Hnnnnfh...!"

        "Even though you just came and were not in the machinations of sex..."
        
        "...it felt like every little touch upon your embiggened cock was bound to send tidal waves of pure ecstasy to your mind, threatening to make you pass out."

        "Oran's tongue, surprisingly cool but not cold enough to tarnish the mood, explores the numerous inches that made up your cock, steadily swabbing it clean of the mess that was not pooled in with the rest."

        "Slowly, your cock would be rid of any cum stains, simply shiny from all the leftover saliva."

        Oran "Good on ya keeping still. Felt like you were fixing to nut on mah face there."

        "Oran snorts before hiking up your legs further, spreading them wide so that there was nothing that could tuck away the sight of your own butt."

        "You can feel sweat beads trailing down your taint and into your tail fur as he brings his head in and puffs air onto your asshole."
        
        "It clenches in anticipation, not ready despite knowing it will have to be soon."

        Oran "Gotta make sure you can handle me for now."

        Oran "Wouldn't wanna break ya, boy~"

        "Oran gives a quick reassuring wink, before a slimy cold intruder makes its way through your pucker with ease."

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        Fen "Ah-ahhhnh!"

        "Once it wiggled, it was clear that the invasion was being done by Oran's tongue."
        
        "The recurring theme of cold was prevalent still as the bear traversed your anus, progressively easing your muscles down from within."

        "You feel that tension from having something in your butt fade, and you feel more and more of his tongue enter you before he was downright kissing your hole."

        Oran "Mmmmhhhph~"

        #"You never asked Terrance about it, but you never knew what your ass must be like for someone to 'eat' until now, and it seemed your tender care for hygiene has earned yourself a new connoisseur."

        #"Of course, things were shaping up to be just as magical once Oran found your sweet spot, prodding it firmly enough to make your cock shoot enough precum to hit the ceiling.
        
        "Things are shaping up to be magical once Oran found your sweet spot, prodding it firmly enough to make your cock shoot enough precum to hit the ceiling."

        stop music fadeout 3.0
        "Oran's spelunking comes to an end soon enough, unfortunately, leaving you whining as the shift from topping to bottoming reawakened your inhibitions once more."

        Fen "C-come on, I was close..."

        Oran "That's just what gettin' your prostate licked feels like."

        Oran "You'll nut when I say you can~"

        "Somehow, the idea of Oran controlling whether or not you would be allowed to embrace release was... oddly thrilling."
        
        "To have so much cock to offer just to have it denied one of its basic functions..."

        "You are pulled from your thoughts, however messy and hazed, when Oran's digit finds its way up your butt."
        
        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        Fen "Unfh! Umfh! Guh!"

        "For some reason, Oran was hooking his finger around inside your hole..."
        
        "...and feeling it curtly brush just a little bit of your prostate was like feeling your orgasm on the rise but being dragged aside from reaching your peak."

        "So torturous. You whine some more, even going as far as showing begging eyes that could melt even the most stone-cold heart on sight."

        "Oran merely grins with mischief."

        Oran "Sorry boy, gotta keep you ready for me no matter what. I ain't exactly easy to take."

        "Those words almost made you clench your hole on his finger, but you were stopped when he added another, plowing through your ass as if he was already fucking you as-is."

        Fen "Hhhh...! HHHHMPH!"

        "You can feel it. The agonizing delay."
        
        "Oran did not even need to hold your bloated balls hostage in order to bring it about - it just felt like you were so close yet none of this was enough to make you blow."

        Oran "Good boy...I think you're ready."

        "Oran probably felt this, but as soon as he said that, your tail started going a mile a second on the spot."

        stop music fadeout 3.0
        "Oran pulls out of your hole, leaving it shiny and convulsing against the open air as his spit covers both inside and out."
        
        "Then he rises back up, putting your legs onto his shoulders and you feel his cock prod your butt."

        "You gulp when it makes contact with your hole, and grit your teeth when it slips inside on the first try."

        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        Fen "MMMPH!"

        Oran "Auhhh...Love me some hot hole~"

        "Oran's cock was by no means cold, yet it felt like the coldest object Fen could ever bother using as a toy as it slid into you, aided and abetted by the prior stretching and lubrication."

        "You feel him edge closer to your prostate and you unknowingly tense up in hopes that he would focus on that spot, even just a little, only to whine as he merely drags over it."

        "A silent smirk comes down to you and you know he is doing that on purpose."

        "Soon, you feel his hips meet your asscheeks, and it was like being given a revelation in that moment."
        
        "You took all of him, no pain, no discomfort."

        Oran "You fire affinity types always give me the best kinda lays. Hot nut and hot butts plenty...But let's see if you can handle a li'l 'chill'~"

        "Oran reinforces his grip on your ankles and you feel him pull back, making your hole tug against him as he was thick enough to touch down on your prostate the whole time."

        "A moment's thought flashes through your mind and you feel compelled to bring it up."

        Fen "G-gentle, please... I don't do this...like you do..."

        Oran "Oh relax, boy. I know you're a virgin."

        "Again with this. But you had no room to argue when you had a bear's cock in your ass - or at least, half of one at this time, especially when he pushed back inside to silence your whining."
        
        play ball "audio/ball hits 1.ogg" volume 2.0 fadein 1.0
        "{i}WHAP{/i}"

        Fen "Ooooough..."

        Oran "Tight and hot...best combo~"

        "Oran was not as fluffy as you, so your butt was a little bit more cushioned than his as he got started, at first thinking he was trying to go hard before realizing you simply had the fur to handle it better."

        "But, you prefer to ride things out as they are now, to ease yourself into this."

        "Oran stares you down from above, and you can see your face in his simple black pupils."
        
        "You see a needy dog hoping to cum, and it sends a shiver down your spine as your tail sways with more passion."

        "{i}WHAP WHAP WHAP WHAP WHAP WHAP WHAP{/i}"

        Oran "Unnngh..."

        Fen "Hooough..."

        "You can already tell you were going to love tail service if this was going to be what it was like."

        "Oran winks at you, probably already knowing you were interested in doing this way more often than not."

        "As your ass was repeatedly thrust into, you slowly lost that anxious feeling in your belly, the pit that made you worry about your experience receiving being tainted."
        
        "As a result, the repressed pleasure kicked in."

        Fen "Hmmmmrrrph..."

        Oran "What's that, boy...?"

        "You feel your face heat up to the point of being flustered."

        Fen "Mmrrrrph..."

        Oran "Can't hear you from up here. Gonna have to speak up~"

        Fen "M-more...!"

        "You finally managed to breathe it out, just to gasp when Oran immediately shifts from steady to rough in that instant."

        Oran "Can do."

        play fuck "audio/fuck fast 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 2.0 fadein 1.0
        "With that affirmative tone, you can only brace yourself against the mattress as Oran really gives it to you."
        
        "You can feel the effort in his every move, knowing he wants to do you in like you had earlier."

        "{i}WAP WAP WAP WAP WAP WAP WAP WAP{/i}"

        Fen "Urrrrgh...!"

        Oran "Mmh-hmmh...this'll really give you a good 'un~"

        "You quickly find out what Oran was insinuating when his thrusts shifted upward and you feel his cock DRAG across your prostate like one dragging a heavy log across the ground."
        
        "You see genuine stars in your eyes."

        Fen "AUUUUUUH!"

        "You swore you came, you thought the white was just your seed getting into them."
        
        "But no, when you came to from that flash of euphoria, you realized that your cock was just pulsing between you and Oran still."

        "No cum. Not yet."

        Oran "Be on your toes, boy. You look like the adventurin' type, them monsters ain't no j-joke~"

        "You throw your head back as Oran coyly pummels your ass."
        
        "He's not humping you, he's fucking you, and you're loving every second of it."
        
        "His pace was not as breakneck as yours, but the power in his hips was phenomenal."

        Fen "Puh...pl-PLEASH!"

        Oran "Not yet, boy...I need my turn~"

        "You whimper with depravity as you are left feeling the climb trickle away, the prostate beating coming to an abrupt halt and going back to riding out the sensation of Oran plowing your hole."

        "But you love it."
        
        "You love the way Oran was making you melt like ice in his hands."
        
        "In time, you perceive the world past looking up at the ceiling where your precum resided and look down."

        "His cock is in your guts, and only disappearing every time he pulls back, just to confirm any suspicions you may have about it."

        Fen "{i}'He's doing me in...and he hasn't even used the crystal on himself...!'{/i}"

        "Your foreshadowing was left to hang in the dank air as your tongue found its way out of your mouth..."
        
        "...eyes clamped shut as the loop of feeling unfathomable bliss just to feel it ebb away enough racked your nerves."

        Oran "Here it comes...!"

        "Oran's warning felt like such a dismissive gesture that you did not pay heed to it, so when he lurched up and had your back off the bed, it took you for a surprise."

        play sound "audio/deep climax 1.ogg" volume 1.0
        stop fuck fadeout 2.0
        stop ball fadeout 3.0
        Oran "URRRRRRNFH!"

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "The bear unloads, and an avalanche of chilly seed pours into your body, making you sigh as if it was like taking a cold bath after being out in the heat all day."

        "All manner of tension fades from you as it spreads in your stomach, leaving you to watch the smallest sign of storage within your belly form before Oran doubled over and nearly fell on you."

        Oran "Whew...! Been a while...since my last client...was a fire affinity..."

        Oran "But hey...Looks like I got my turn~"

        stop music fadeout 2.0
        play fuck "audio/fuck fast 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 2.0 fadein 1.0
        "You only have half a second before Oran recovers on the spot, his hips right back to working in overdrive as his cock goes straight into the motions of fucking you once more."

        play sound "audio/light climax 1.ogg" volume 1.0
        Fen "AUUUUUGH!" with vpunch

        "You were not ready for it, so you did not get to feel the cataclysmic way you came."

        scene bg white with dissolve        
        play music "audio/Schlop.ogg" volume 3.0 fadein 1.0
        "You shot your cum through your cock in a straight beeline for the ceiling, splattering it with your creamy white spunk."

        "It was like white-hot fire was streaming out of you with how Oran managed to fuck you through your orgasm, unyielding despite how much you clenched over him."

        "{i}SPLRTCH SPLRSH SPLRTCH{/i}" with vpunch

        "Every other volley was sending more of your cum to the ceiling, leaving it to grow messy and rain down your own fluids onto the bed and your body."
        
        "Seeing a glob hit Oran on the head did not stop him from getting more out of you."

        Fen "Ahhh! O-o-oran! WAIT!" with vpunch

        "But he keeps going, and you feel the apex of your orgasm hit and silence EVERYTHING."
        
        stop fuck fadeout 3.0
        stop ball fadeout 3.0
        stop music fadeout 3.0
        "You cannot hear, see past the white, nor smell anything. All you can do is feel him fucking the cum out of you."

        "Pure nirvana at its finest."

        show bg room3 at truecenter:
            zoom 1.5
        show ratio1
        with s_dissolve
        "By the time you come to, you are still cumming, most likely a result of having such massive junk, and you sink into a slump as Oran finally slows down, allowing you to actually ride out your orgasm."

        "{i}SPLAT{/i}"

        "As you close your eyes, you are met with a cum glob to your face, much to Oran's amusement and your immediate recovery as your fatigue faded on the spot."

        Fen "Oh man...this is a lot..."

        Fen "Should we be making such a big mess?"

        Oran "Who said we? You're the one with the big cock~"

        "Oran playfully winks at your pouting face, before coming down to lick your nose while sandwiching your cock between both of your bodies."

        Fen "H-hey, that tickles!"

        Oran "Nothin' wrong with that."

        "It takes a bit considering your jerkish reactions, but you slowly come to find out that Oran was cleaning you off, ridding you of that sticky feeling from being all over your facial fur."

        "But you feel plenty in other areas, and no doubt Oran was messy too..."

        "Oran jolts with surprise when you reach in and bend his head towards your chest, dragging your tongue along the back of his neck since that's where your cum landed."

        Oran "Well look at you. Here I was thinking you had no juice left in ya."

        Fen "It's...only right. You cleaned me off."

        Oran "Guess ya got me there, boy. Take your time."

        #"It was not your first time giving someone a tongue bath - and certainly not the first time you've done it in this context, so Oran was starting to look relatively clean after a few minutes of thorough swabbing.

        "after a few minutes of thorough swabbing, Oran is starting to look relatively clean."

        "You spit out some stray fur clumps from your tongue."

        Oran "Alright, that'll do, boy. Now it's time I get my other turn..."

        Oran "And remember, you cum when I say~"

        Fen "Mnnh. Okay..."

        "You may sound tentative, but you're still going to enjoy this all the same."

        "Oran finally pulled out, having felt so good being in there that it felt like you were being yanked away from bliss when his cock popped out of you."

        "{i}SPLURT{/i}"

        "A few globs exit from your yawning hole, coating your tail base and taint in fresh bear cum."

        Oran "Been a bit since I used it myself."

        show bg room3_blur
        show growth_relic at truecenter:
            zoom 2
        with dissolve
        "The bear went ahead and grabbed the crystal artifact, its crimson glow filling your view with wonder as he brought it up from under the bed."
        
        "This time, however, he put it on his cock."

        hide growth_relic
        show bg room3
        with dissolve
        "From an onlooker's perspective, it was almost terrifying watching Oran's dick rise back up to full hardness just to grow longer on the spot."
        
        "As someone who has just gotten into this, you were having second thoughts."

        "But, the allure of seeing someone grow so big with the intent to fuck you was enamoring."
        
        # IF bond02 something in future
        "Surely you would want to know what it feels like, even once - least you never get your chance with Terrance."

        "So you relax, allowing yourself to take in the sight of Oran's massive cock casting a shadow over your face."

        Oran "I figured ya'd jus' stare, so I took a guess at what you could handle."

        "Oran presses his overgrown cock against yours, and you realize that they're somewhat on par."
        
        "Either he was good at guessing, or he got lucky that he did, though you were both a way away from being as big as Terrance."

        "Either way, it was time to take it."

        Oran "Don't worry 'bout hurtin', you saw how I took it."

        Fen "B-but you're uh...used to it...right?"

        Oran "Pffft, naw, that was the first cock I've taken that was that big. That relic don't work that well on just anyone."

        Oran "Guess you popped my cherry, boy~"

        "A hint of pride fills you where the anxiety was trying to settle, dispelling it as he decided on the position he wanted you in."

        "All fours. Just like how this started, it would be how this ended, it seemed."

        Oran "Dogs like gettin' mounted, right boy~?"

        Fen "Y-yeah..."

        Oran "Can't hear ya...Speak up."

        "You shudder as you feel the cock head touch your hole..."
        
        "...so gargantuan when it was pressed against you compared to feeling it thrust against your own mega-sized shaft, yet you do not feel your ass close up."

        Fen "I'm ready...t-to get mounted."

        Oran "Heheh, good boy."

        "The bear's hands plant down on your back, keeping your torso pinned to the mattress while your ass stays up."
        
        "Oran's cock starts gaining headway, seemingly impossible, before it pops in."

        play fuck "audio/fuck mid 1.ogg" volume 3.0 fadein 1.0
        "{i}SHPLP{/i}"

        Fen "GAH!"

        "He was right. There was no pain whatsoever, just the alien sensation of being stretched open so obscenely."
        
        "It was...well, there was no word for it just yet, as it was only the tip."

        Oran "Easy does it now. First time's gonna rock your world..."

        "Oran pushes on, and you can hardly keep air inside of your lungs the entire time."
        
        "It was so big, reaching in so deep...you can feel it bulging through your stomach, much more than he already has."

        "You swore it would never end by the time it did."

        Oran "All in, boy...Took it like a champ."

        Fen "Unnnfh..."

        "You can feel it pulsing between your chest and belly, just a few inches shy from being right next to your own beating heart."
        
        "Only reason you can tell it was that deep was from its much slower throbbing."

        "You breathe out, trying not to get inundated by such an intense feeling."
        
        "You shudder, when Oran moves and the girth jolts your entire body from head to toe like you had been zapped by something."

        Fen "MMMPH!"

        Oran "Here we go..."

        "Slow and steady was the best way to go about this."
        
        "You may not be screaming for mercy from the nonexistent agony, but you certainly needed some time - time Oran was willing to give."

        "You could count each and every single inch that brushed over your prostate..."
        
        "...losing thoughts by the twentieth, and nearly rolling your eyes back all the way into your head once he was past halfway out of you."

        play ball "audio/ball hits 1.ogg" volume 3.0 fadein 1.0
        "Then it was all back in, with a simple thrust."

        "{i}PAP{/i}"

        Fen "AUUUH!"

        "Feeling it all rush back in had you breathless, struggling to breathe without sounding like you were trying not to - raspy and hoarse."
        
        "Oran digs back into your body, stretching your entire being from the inside."

        "Your fingers and toes ball up every single time, the pleasure immeasurable and the waves of lust slamming your rationale into a heap."

        "Your prostate was crushed, but it was the good kind."
        
        "Whenever Oran's cock would throb, it would send all the right singles into that spot and practically give you a full-body orgasm, Blissful."

        Oran "You're doing good, b-boy...Almost thought you passed out..."

        Fen "Hnnfh...n-n-no..."

        Oran "Heheh."

        Oran "Guess I'll speed up then~"

        play fuck "audio/fuck fast 1.ogg" volume 3.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 3.0 fadein 1.0
        "Your back arches when Oran lives up to such a promise, hips barreling into your ass and making you moan to the gunked-up ceiling above."

        "His balls were smacking you now, reminding you of how full and heavy they were with seed he intended to pump into you, and you bite your lip in anticipation for that."

        "{i}PAP PAP PAP PAP PAP PAP PAP{/i}"

        "You can hardly process anything else around you."
        
        "All you can feel is the indomitable presence of Oran's cock running through you back and forth, and the noise made when it slid back in."

        "You feel a growing fire in your core, as if your affinity was being drawn out by such pleasure."
        
        "But it turned out to be a howl that came to be from Oran slipping in a little too fast and knocking the precum out of you again."

        Oran "Hoooffh...still a hugger in there, boy...Keep that up~"

        "There was no way you couldn't."
        
        "You were clenching down on Oran no matter what, too deep to even try to relax while he plowed you like fertile soil."
        
        "At this rate, if you don't cum within the next five seconds, it'd be a miracle."

        Oran "Tell me...how it feels...I wanna hear...just how badly you want me to finish...H-heheh..."

        "A heated exchange, but not out of your scope."

        Fen "Ghhhah! Am-m-mazing...! UMPH! D-don't stop...!"

        Oran "Good boy~"

        "Even though you felt ready to give out at a moment's notice should Oran find a way to make things feel better, you still find yourself on the receiving end of some real fucking as Oran ramps up the force."

        "Your ears ring with the sound of hips slamming forth into your ass, and you can even feel your buttcheeks jiggle - not like water, but giving away that there was some pudge in you at least."

        "And at some point, it was not enough for the bear, and Oran's pace hastened after a particular throb had him groaning."

        "{i}PAP-PAP-PAP-PAP-PAP-PAP-PAP-PAP-PAP{/i}"

        "{i}PAP-PAP-PAP-PAP-PAP-PAPPAPPAPPAP{/i}"

        Fen "AUUUGH!...PL-PLEASE! ORAN! I C-C-CAN'T...!"

        Oran "Y-yesh...you can....rrrnnngh...Hold it, boy...I wanna savor this - HNNNFH!"

        "Despite their composure, you can tell Oran was not holding up so well either."
        
        "He was going to cum soon, and you would have to wait to get your own - truly inhumane stuff."

        "Yet, you cannot help but be in this dreamlike state, the pleasure reaching a scale that almost has you white out from the moment."
        
        "To be able to fathom this would take ages, and you were still getting more."

        Oran "Unnnfh...it's coming...f-fuck...ffff-fu-huck..."

        play sound "audio/deep climax 2.ogg" volume 2.0
        Oran "GNNNNHRRRGH!" with vpunch

        stop music fadeout 3.0
        stop fuck fadeout 3.0
        stop ball fadeout 3.0
        scene bg white
        with dissolve
        "You gasp one last time and everything goes mute again, the sheer power in Oran's pulsating cock rendering you immobile as their lustful peak sent fireworks through your prostate in tandem."

        play music "audio/Schlop.ogg" volume 3.0 fadein 1.0
        "The first blast erased any trace of Oran's cock being inside your body, replacing somewhat hardened abs molded by hard work into nothing but a spherical weight of cum."

        "It pools within you, having so much room and plenty of reason to expand that you cannot help it any longer."
        
        "You cum before he even reaches the start of the real orgasm."

        "{i}SPLOOOSH GLOORSH SPLRSH SHSPLRT SPLRT{/i}" with vpunch

        "Your shared orgasm was something of a messy marvel."
        
        "You, with your mouth open for a silent scream of bliss, paint the wall behind the bed to the point of it scaling up to the ceiling."

        "Oran, on the other hand, paints the entirety of your insides white as his cum settled inside your body with gusto, forcing your cock to aim lower as it pressed down onto your heated flesh."

        "You can feel Oran's balls flexing against the back of your thighs, dragging their hefty size against your fur as if marking you with the sweat beads running off of them."

        "Yet your own were doing the same, freely bobbing between your legs to show just how hard you were dispensing all that hot spunk out into the room while Oran stuffed you with his own."

        "There were no words to spare when you both would enter the final rush of ecstasy almost simultaneously though."
        
        "Oran filled you up with so much of it that you had cum come out of your mouth."

        "But you certainly looked to be trying to remodel the room you were in with how much space you turned white from your own load, putting Oran's cock in an inescapable chokehold the whole time."

        show bg room3 at truecenter:
            zoom 1.5
        show ratio1
        with s_dissolve
        "It takes so much time for the white in your eyes to even fade, to where you actually thought you got your own cum on your face again, but you do come to after some time."

        "You can feel Oran breathing down on the back of your head, a sign that you were still conscious, and one means to help you recover as your cock finally settled."

        Fen "Hnnngh..."

        "You feel bloated, like you just took a Terrance's worth of water in a sitting ten times in a row without thinking, and your stomach makes an audible noise when you shift around."

        "{i}SLOOSH{/i}"

        stop music fadeout 3.0
        "There was no need to guess what all that could be when the culprit was still pulsing inside your stomach."

        Oran "Whew...now th-that...is how you empty your balls."

        Fen "N-n-no kidding..."

        "Whether it was your own endurance from all the work you've been doing in the Flaming Flagon, or some other third thing, you were still not exhausted."

        "You reason that the crystal was to blame, considering that any logical explanation would have you on the ground passed out from having such an impressive monument of a cock between your legs."

        "And you see it in the corner of your eye, its crimson glow promising that if its surface found your cock again, you would certainly lose yourself in the lust and hump anything that breathes."

        "Oran surprises you with a headpat while you were getting entranced by the artifact."

        Oran "You did good, boy. If you were anyone else, I'd might have made you pay rates that'll make you furious."

        Fen "Th-thank goodness..."

        "You were confident that any price that was not coincidentally over your current budget could be dealt with here."

        "Oran hums before you feel him back away, your cock jolting back up to life as movement means feeling him twitch against your prostate some more."

        Fen "M-meant to ask but..."

        Oran "Hmm?"

        Fen "Is this supposed to last long - ERFH!"

        "You are cut off when Oran yanks out the last few inches still inside your ass, leaving your buttcheeks swamped with his cum."

        if service_bear_hyper_sxp == False:
            $ service_bear_hyper_sxp = True
            call sxp_up from _call_sxp_up_16
        
        else:
            pass        
        "Most of what resided in your hole poured out of you like a waterfall."

        Oran "Not if you're not wearin' it. If you ain't in a hurry, should come down very soon."

        Fen "O-okay..."

        Oran "Phew..."

        play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
        "Oran lies down beside you, leaving your trembling legs to leave you planted on the mattress as well."
        
        "You feel sticky all over, as residual cum from the ceiling and the load on your butt continue to trickle."

        "You come to a state of relative normalcy, no more breathing lethargically at least and take to Oran's prone form."

        "Turning, he watches you in curiosity as you crawl onto his body and lay on his chest, listening to his heart steadily calm down from all that action."

        "He simply smiles and drapes an arm on your shoulder while you sigh in relief at the comforting gesture."

        Fen "Stuffy in here..."

        Oran "We'll be fine. Trip to that bathhouse'll clean you right up. Inside and out."

        Fen "Wouldn't Marcus charge extra for that?"

        Oran "Only if you hop in right away without rinsin'."

        Fen "For sure."

        "Idle chatter helps bring the mood down a bit more, and you stop feeling like you need to fuck something every single second you aren't while you stare at your cock."

        "Oran's words hold true soon enough, and it was almost comical watching how your cock would seamlessly shrink back down from its oversized state."
        
        "Almost like it was going soft but at a more dramatic scale."

        "Soon, you would be back to your old self, just in time for Oran's cock to do the same."

        "Once both of you are back to your normal sizes, you nuzzle into his chest and get a squeeze on your bicep in return."

        Fen "I had a great time...Didn't know it was gonna be like this."

        Oran "Oh?"

        "Oran perks up at this."

        Oran "You weren't a client?"

        Fen "No...I was, still looking..."

        "Oran guffaws at the misunderstanding, leaving you to blush as you should have told him sooner than after all was said and done."

        Oran "Guess I was being a bit hasty. Doing it outside only feels better when the moon's out."

        Oran "Less folks to get in the way an' try to score a freebie from me."

        Fen "People do that?"

        Oran "Mmh."

        "Oran adopts a sour look and you feel the room get a little tense."

        Oran "When I first started this kinda thing, folks were dashing on me left and right."

        Oran "Best ass in the alley I always say, but it didn't feel like it back when folks would pump'n dump without even sayin' a word."

        Fen "That's... I'm sorry you had to go through that."

        "Oran's forlorn expression fades when he looks down to you, as if your condolences were enough to brighten up his mood alone, and he smiles a little."

        Oran "Don't worry 'bout it, that was a while back, and these days folks wish they can have me that easy."

        Oran "It's why I always call the shots."
        
        Oran "When folks're real desperate for more, I remind 'em to pay, and that rush to decide whether they wanna skip or get their dick wet turns in my favor."

        Oran "Ain't had a runner in months."

        Fen "Wow..."

        "You wonder if you'll ever have that kind of sexual charm to make sure people would want to pay that much."

        Oran "What got you here, boy?"

        Fen "Oh, a friend of mine taught me about this."

        Oran "He a weird fella, got a sword?"

        Fen "You know 'em?"

        Oran "Heheh...Boy do I~"

        "It was cryptic, but your mind was able to piece things together about Oran and Odachi potentially knowing each other, and you were satisfied with the deduction."

        Oran "Welp, gettin' pretty late. You might wanna head on out, get cleaned up before it gets too sticky."

        Fen "Right."

        "Indeed, you can feel the mess over your body start to harden, and you know if you wait longer then you'll be brushing out matted fur clumps later."

        "You rise out of bed, a limp to your stride since you did take a massive cock up your butt."

        Fen "Phew."

        Oran "See you around, boy~"

        #"You feel the warm rush of excitement hit you at such words, beaming right at Oran as he sat up in the bed."

        jump day_end

    label tailservice_bear_bottom:

        "Oran smiles and winks at you, grateful for your answer before he grabs your legs."

        Fen "Hnnnnfh...!"

        "Oran's tongue, surprisingly cool but not cold enough to tarnish the mood, explores the inches that made up your cock."

        Oran "Good on ya keeping still."

        "Oran snorts before hiking up your legs further, spreading them wide so that there was nothing that could tuck away the sight of your own butt."

        "You can feel sweat beads trailing down your taint and into your tail fur as he brings his head in and puffs air onto your asshole."
        
        "It clenches in anticipation, not ready despite knowing it will have to be soon."

        Oran "Gotta make sure you can handle me for now."

        Oran "Wouldn't wanna break ya, boy~"

        "Oran gives a quick reassuring wink, before a slimy cold intruder makes its way through your pucker with ease."

        Fen "Ah-ahhhnh!"

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "Once it wiggled, it was clear that the invasion was being done by Oran's tongue."
        
        "The bear traversed your anus, progressively easing your muscles down from within."

        "You feel that tension from having something in your butt fade, and you feel more and more of his tongue enter you before he was downright kissing your hole."

        Oran "Mmmmhhhph~"

        #"You never asked Terrance about it, but you never knew what your ass must be like for someone to 'eat' until now, and it seemed your tender care for hygiene has earned yourself a new connoisseur."

        #"Of course, things were shaping up to be just as magical once Oran found your sweet spot, prodding it firmly enough to make your cock shoot enough precum to hit the ceiling.
        
        "Things are shaping up to be magical once Oran found your sweet spot, prodding it firmly enough to make your cock shoot enough precum to hit the ceiling."

        stop music fadeout 3.0
        "Oran's spelunking comes to an end soon enough, unfortunately, leaving you whining as the shift from topping to bottoming reawakened your inhibitions once more."

        Fen "C-come on, I was close..."

        Oran "That's just what gettin' your prostate licked feels like."

        Oran "You'll nut when I say you can~"

        "Somehow, the idea of Oran controlling whether or not you would be allowed to embrace release was... oddly thrilling."

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "You are pulled from your thoughts, however messy and hazed, when Oran's digit finds its way up your butt."

        Fen "Unfh! Umfh! Guh!"

        "For some reason, Oran was hooking his finger around inside your hole..."
        
        "...and feeling it curtly brush just a little bit of your prostate was like feeling your orgasm on the rise but being dragged aside from reaching your peak."

        "So torturous. You whine some more, even going as far as showing begging eyes that could melt even the most stone-cold heart on sight."

        "Oran merely grins with mischief."

        Oran "Sorry boy, gotta keep you ready for me no matter what. I ain't exactly easy to take."

        "Those words almost made you clench your hole on his finger, but you were stopped when he added another, plowing through your ass as if he was already fucking you as-is."

        Fen "Hhhh...! HHHHMPH!"

        "You can feel it. The agonizing delay."
        
        "Oran did not even need to hold your bloated balls hostage in order to bring it about - it just felt like you were so close yet none of this was enough to make you blow."

        Oran "Good boy...I think you're ready."

        "Oran probably felt this, but as soon as he said that, your tail started going a mile a second on the spot."

        stop music fadeout 3.0
        "Oran pulls out of your hole, leaving it shiny and convulsing against the open air as his spit covers both inside and out."
        
        "Then he rises back up, putting your legs onto his shoulders and you feel his cock prod your butt."

        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        "You gulp when it makes contact with your hole, and grit your teeth when it slips inside on the first try."

        Fen "MMMPH!"

        Oran "Auhhh...Love me some hot hole~"

        "Oran's cock was by no means cold, yet it felt like the coldest object Fen could ever bother using as a toy as it slid into you, aided and abetted by the prior stretching and lubrication."

        "You feel him edge closer to your prostate and you unknowingly tense up in hopes that he would focus on that spot, even just a little, only to whine as he merely drags over it."

        "A silent smirk comes down to you and you know he is doing that on purpose."

        "Soon, you feel his hips meet your asscheeks, and it was like being given a revelation in that moment."
        
        "You took all of him, no pain, no discomfort."

        Oran "You fire affinity types always give me the best kinda lays. Hot nut and hot butts plenty...But let's see if you can handle a li'l 'chill'~"

        "Oran reinforces his grip on your ankles and you feel him pull back, making your hole tug against him as he was thick enough to touch down on your prostate the whole time."

        "A moment's thought flashes through your mind and you feel compelled to bring it up."

        Fen "G-gentle, please... I don't do this...like you do..."

        #If first time
        Oran "Oh relax, boy. I know you're a virgin."

        "Again with this. But you had no room to argue when you had a bear's cock in your ass - or at least, half of one at this time, especially when he pushed back inside to silence your whining."

        #Else
        #"But you had no room to argue when you had a bear's cock in your ass - or at least, half of one at this time, especially when he pushed back inside to silence your whining."
        play ball "audio/ball hits 1.ogg" volume 2.0 fadein 1.0
        "{i}WHAP{/i}"

        Fen "Ooooough..."

        Oran "Tight and hot...best combo~"

        "Oran was not as fluffy as you, so your butt was a little bit more cushioned than his as he got started, at first thinking he was trying to go hard before realizing you simply had the fur to handle it better."

        "But, you prefer to ride things out as they are now, to ease yourself into this."

        "Oran stares you down from above, and you can see your face in his simple black pupils."
        
        "You see a needy dog hoping to cum, and it sends a shiver down your spine as your tail sways with more passion."

        "{i}WHAP WHAP WHAP WHAP WHAP WHAP WHAP{/i}"

        Oran "Unnngh..."

        Fen "Hooough..."

        "You can already tell you were going to love tail service if this was going to be what it was like."

        "Oran winks at you, probably already knowing you were interested in doing this way more often than not."

        "As your ass was repeatedly thrust into, you slowly lost that anxious feeling in your belly, the pit that made you worry about your experience receiving being tainted."
        
        "As a result, the repressed pleasure kicked in."

        Fen "Hmmmmrrrph..."

        Oran "What's that, boy...?"

        "You feel your face heat up to the point of being flustered."

        Fen "Mmrrrrph..."

        Oran "Can't hear you from up here. Gonna have to speak up~"

        Fen "M-more...!"

        "You finally managed to breathe it out, just to gasp when Oran immediately shifts from steady to rough in that instant."

        Oran "Can do."

        play fuck "audio/fuck fast 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 2.0 fadein 1.0
        "With that affirmative tone, you can only brace yourself against the mattress as Oran really gives it to you."
        
        "You can feel the effort in his every move, knowing he wants to do you in like you had earlier."

        "{i}WAP WAP WAP WAP WAP WAP WAP WAP{/i}"

        Fen "Urrrrgh...!"

        Oran "Mmh-hmmh...this'll really give you a good 'un~"

        "You quickly find out what Oran was insinuating when his thrusts shifted upward and you feel his cock DRAG across your prostate like one dragging a heavy log across the ground."
        
        "You see genuine stars in your eyes."

        Fen "AUUUUUUH!"

        "You swore you came, you thought the white was just your seed getting into them."
        
        "But no, when you came to from that flash of euphoria, you realized that your cock was just pulsing between you and Oran still."

        "No cum. Not yet."

        Oran "Be on your toes, boy. You look like the adventurin' type, them monsters ain't no j-joke~"

        "You throw your head back as Oran coyly pummels your ass."
        
        "He's not humping you, he's fucking you, and you're loving every second of it."
        
        "His pace was not as breakneck as yours, but the power in his hips was phenomenal."

        Fen "Puh...pl-PLEASH!"

        Oran "Not yet, boy...I need my turn~"

        "You whimper with depravity as you are left feeling the climb trickle away, the prostate beating coming to an abrupt halt and going back to riding out the sensation of Oran plowing your hole."

        "But you love it."
        
        "You love the way Oran was making you melt like ice in his hands."
        
        "In time, you perceive the world past looking up at the ceiling where your precum resided and look down."

        "His cock is in your guts, and only disappearing every time he pulls back, just to confirm any suspicions you may have about it."

        Fen "{i}'He's doing me in...!'{/i}"

        "Your foreshadowing was left to hang in the dank air as your tongue found its way out of your mouth, eyes clamped shut as the loop of feeling unfathomable bliss just to feel it ebb away enough racked your nerves."

        Oran "Here it comes...!"

        "Oran's warning felt like such a dismissive gesture that you did not pay heed to it, so when he lurched up and had your back off the bed, it took you for a surprise."

        play sound "audio/deep climax 1.ogg" volume 1.0
        stop fuck fadeout 2.0
        stop ball fadeout 2.0
        Oran "URRRRRRNFH!" with vpunch

        play music "audio/Schlop.ogg" volume 3.0 fadein 1.0
        "The bear unloads, and an avalanche of chilly seed pours into your body, making you sigh as if it was like taking a cold bath after being out in the heat all day."

        "All manner of tension fades from you as it spreads in your stomach, leaving you to watch the smallest sign of storage within your belly form before Oran doubled over and nearly fell on you."

        Oran "Whew...! Been a while...since my last client...was a fire affinity..."

        play fuck "audio/fuck fast 1.ogg" volume 2.0 fadein 1.0
        play ball "audio/ball hits 2.ogg" volume 2.0 fadein 1.0
        "You only have half a second before Oran recovers on the spot, his hips right back to working in overdrive as his cock goes straight into the motions of fucking you once more."

        play sound "audio/light climax 1.ogg" volume 1.0
        Fen "AUUUUUGH!" with vpunch

        "You were not ready for it, so you did not get to feel the cataclysmic way you came."

        "It was like white-hot fire was streaming out of you with how Oran managed to fuck you through your orgasm, unyielding despite how much you clenched over him."

        "{i}SPLRTCH SPLRSH SPLRTCH{/i}" with vpunch

        "Every other volley was sending more of your cum to the air, and rain down onto the bed and your body, seeing a glob hit Oran on the head yet not stop him from getting more out of you."

        Fen "Ahhh! O-o-oran! WAIT!" with vpunch

        stop music fadeout 3.0
        stop fuck fadeout 3.0
        stop ball fadeout 3.0
        scene bg white
        with dissolve
        "But he keeps going, and you feel the apex of your orgasm hit and silence EVERYTHING."
        
        "You cannot hear, see past the white, nor smell anything. All you can do is feel him fucking the cum out of you."

        "Pure nirvana at its finest."

        show bg room3 at truecenter:
            zoom 1.5
        show ratio1
        with s_dissolve
        "By the time you come to, you are still cumming, and you sink into a slump as Oran finally slows down, allowing you to actually ride out your orgasm."

        Fen "Oh man...this is a lot..."

        "Oran playfully winks at your pouting face, before coming down to lick your nose."

        Fen "H-hey, that tickles!"

        Oran "Nothin' wrong with that."

        "It takes a bit considering your jerkish reactions, but you slowly come to find out that Oran was cleaning you off, ridding you of that sticky feeling from being all over your facial fur."

        "But you feel plenty in other areas, and no doubt Oran was messy too..."

        "Oran jolts with surprise when you reach in and bend his head towards your chest, dragging your tongue along the back of his neck since that's where your cum landed."

        Oran "Well look at you. Here I was thinking you had no juice left in ya."

        Fen "It's...only right. You cleaned me off."

        Oran "Guess ya got me there, boy. Take your time."

        #"It was not your first time giving someone a tongue bath - and certainly not the first time you've done it in this context, so Oran was starting to look relatively clean after a few minutes of thorough swabbing.

        "after a few minutes of thorough swabbing, Oran is starting to look relatively clean."

        "You spit out some stray fur clumps from your tongue."

        Oran "Alright, that'll do, boy."

        "Oran finally pulled out, having felt so good being in there that it felt like you were being yanked away from bliss when his cock popped out of you."

        "{i}SPLURT{/i}"

        if service_bear_bottom_sxp == False:
            $ service_bear_bottom_sxp = True
            call sxp_up from _call_sxp_up_17
        
        else:
            pass
        "A few globs exit from your yawning hole, coating your tail base and taint in fresh bear cum."

        #some farvel words from top scene
        "The two of you cuddle for a while, basking in the afterglow."

        "You spend a bit longer enjoying the feel of Oran's round belly before you're ready to head out."

        "Once you've cleaned up as best as you can, you put on your clothes and prepare to leave."

        Oran "It's 10 by the way. Usually 20 coins, but I can't let a cute guy like you feeling drained in your purse for that."

        Fen "Th-thanks..."

        $ fen_coins -= 10
        play sound "audio/payment.ogg" volume 3.0
        "Blushing the whole while, you hand over the money without any objection."

        Oran "Thank you, thank you."

        Fen "Of course."

        #some end from hyper version

        Oran "See you around, boy~"

        jump day_end


label gunther_nsfw_01:
    show bg fenroom_blur at truecenter:
        zoom 1.5
    show fen naked hot2 at left1:
        ypos 1700
        zoom 1.5
    show gunther naked normal at right1:
        ypos 1700
        zoom 1.5
    show ratio1
    with s_dissolve
    "You can feel the heat coming off Gunther as he reaches out with his paws."

    "The big cat's hands stroke your fur. His touch is gentle and nice, causing your tail to wag."

    "He purrs as you return the favor and strokes his coarser fur."

    "His claw tips gently scritch your fur and he leans down to nip and nuzzle your ear."

    "Your meat rods rub against each other, quickly becoming erect."

    Gunther "Where would you like me?"

    $ gunther_offer_done = True

    $ config.menu_include_disabled = True

    menu:
        "What position do you want Gunter in?"

        "Push him on to the bed (STR 8)" if FenSTR >= 8:
            $ config.menu_include_disabled = False
            jump gunther_nsfw_01a

        "Hop onto all fours on your own":
            $ config.menu_include_disabled = False
            jump gunther_nsfw_01b

label gunther_nsfw_01a:
    scene bg fenroom
    with s_dissolve
    "Your workouts are paying off."

    "You place a hand into Gunther's shoulder and gently, but firmly, push him onto the bed."

    Fen "Now spread those legs."

    Gunther "Heh, sure thing."

    scene gunther cg1 00 at topleft:
        zoom 1.5
    with s_dissolve
    "The tavern owner rolls onto his back and spreads his legs for you."

    "His muscular thighs pull apart to reveal his toned midsection and ample cock."

    "Your boss looks up at you with a grin as he eyes his young employee's arousal."

    "Gunther's form is exposed for your pleasure, inviting you to do anything you'd like to the sexy being in your bed."

    "Your hands waste no time exploring his well toned muscles."

    "He purrs as your paws roam across his bulging pecs and down his belly."

    #Zoom on his cock
    "You see his thick cock throb as your paws finally reach between his legs."

    "You give the pulsing shaft a good squeeze that causes Gunther to moan softly."

    "The big strong cat looks quite cute like that. It only takes a moment before that hungry look returns and you find yourself staring at a predator once more."

    Gunther "Don't keep this cat waiting."

    "He reaches out with his paw and strokes your soft fur. You can hear him purring as his hand slides down your belly."

    Fen "Ah."

    "You gasp as he grips your hard cock and gently pulls you closer."

    "Gunther seems eager and so are you."

    scene gunther cg1 00 at truecenter:
        zoom 1
    with s_dissolve
    "You position yourself between his legs, letting your shaft throb against Gunther's."

    "He grinds and frots against you, purring louder every second."

    "You can feel the heat start to rise in the room as does your lust and arousal."

    "His length presses against yours. You grind back against him, your cock leaking beads of pre as you rub on one another."

    "Gunther is panting harder. You look beside you to see his toes stretching and curling as he pushes himself against your crotch."

    "The room continues to heat up as you see how needy Gunther's become."

    #zoom on Cock lines up with hole
    scene gunther cg1 01 at truecenter
    with s_dissolve
    "You pull the cat's leg over to the side and let the tip of your length rest against his tailhole."

    "Your precovered tip pulses against his winking ring while his expression tells you that he's more than ready."

    scene gunther cg1 02 at topleft:
        zoom 1.5
    with s_dissolve
    "With a gentle thrust of your hips, the head of your cock spreads Gunther's ring open with a muted pop."

    Gunther "Mmm." 

    "He leans back, moaning again as you push more of your length into him."

    "The hot and tight tunnels welcome you inside with a few gentle spasms."

    scene gunther cg1 02 at truecenter:
        zoom 1
    with s_dissolve
    "You gasp as you feel him relax and more of your cock slides in."

    "His tail slaps at your backside as you feel his warmth slide all the way to the base of your crotch."

    "The heat causes you to pant and moan as the cat's ass swallows your cock."

    Fen "Feeling good?"

    Gunther "Feels great, keep goin'."

    scene gunther cg1 03 at truecenter
    with s_dissolve
    play music "audio/light moan 1.ogg" volume 2.0 fadein 1.0
    play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    "You start to draw back a bit before pushing yourself right back down to the base."

    "Another loud moan rolls out from the cat's muzzle as you work at a slow but steady pace."

    "His tunnel continues to squeeze and slide easily over your throbbing arousal."

    scene gunther cg1 04 at truecenter
    with s_dissolve
    "You pull his leg tight against your side as you start to drill in a bit deeper."

    Gunther "F-Fuck."

    "He grunts and purrs as you fuck him harder."

    "Your balls slap against Gunther's chiseled ass cheeks as you push yourself further into him."

    Fen "Oh Gunther."

    "You moan his name as you work your cock in and out of his amazing hole."

    "He twitches and pants beneath you as your bodies radiate with energy."

    scene gunther cg1 05 at truecenter
    with s_dissolve
    "Heated breath from both your moans and grunts cause the ambient temperature in the room to rise."

    "As your lust continues to escalate, so does the radiant heat coming off your bodies."

    "Sweat drips off you and splatters against the cat's red fur as your bodies entwine."

    "His hole milks your cock with constant contractions each time you bottom out into him."

    "Gunther's cock throbs and leaks as you plow his ass. Your cock head grinds into his prostate causing him to purr and moan loudly."

    scene gunther cg1 06 at truecenter
    with s_dissolve
    "You hold onto the cat as you continue to rock your hips, thrusting deeply."

    "It feels like a constant tide of pleasure, rising and falling like waves as you hump away into your boss."

    "Each crest of the wave peaks just a bit higher until you find yourself at the tipping point."

    Fen "G-Gunther, I'm gonna..."

    Gunther "Fuck yeah, give it to me."

    "The big guy growls as he clenches harder around your rod."

    scene gunther cg1 07 at truecenter
    with s_dissolve
    play music "audio/light moan 1.ogg" volume 2.0 fadein 1.0
    play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
    play fuck "audio/fuck fast 1.ogg" volume 2.0
    play ball "audio/ball hits 2.ogg" volume 2.0
    "Encouraged by his cries of passion, you give it your all."

    "Bracing against his leg and the bed, you pound away."

    "You thrust with wild abandon, plowing your canine cock into Gunther's slick hole."

    "The loud wet slap of your sweat covered balls echo in the room as they slap against Gunther's rump."

    "More sweat pours down your brow as you thrust away like an animal in rut."

    Fen "F-fuck!"

    "His ass feels too good, the perfect amount of tightness and the constant contractions in time with the throbbing of his cock bobbing below you sends you over the edge."

    scene gunther cg1 08 at truecenter
    with s_dissolve
    play sound "audio/light climax 1.ogg" volume 1.0
    play vocal1 "audio/deep climax 1.ogg" volume 1.0
    stop music fadeout 0.5
    stop nsfw1 fadeout 0.5
    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    "You howl as you climax. Your hot seed pumps into Gunther's ass."

    "Jets of thick cum erupt from your tip, injecting your load right into the fiery cat below you."

    stop fuck fadeout 2.0
    stop ball fadeout 2.0
    "The jolt running down your spine leaves ripples of tingling pleasure every time a rope of cum shoots out."

    "Your balls almost ache from the force of which they were just emptied."

    scene gunther cg1 09 at truecenter
    with s_dissolve
    "The big cat's cock spasms as his own load starts to leak out from all the stimulation."

    "You watch in amazement as a content stream of cum runs down the side of his pulsing length."

    scene gunther cg1 10 at truecenter
    with s_dissolve
    "Both drenched with sweat and panting hard, Gunther gives your neck a nuzzle and looks down at the large wet spot in your sheets."

    Gunther "Ah, sorry...I'll help clean this up."

    if gunther_sxp_1 == False:
        $ gunther_sxp_1 = True
        call sxp_up from _call_sxp_up
    
    else:
        pass

    scene bg fenroom
    with s_dissolve
    "Your sheets are soaked in sweat and cum, but Gunther already found some fresh sheets."

    "You pull off the soiled covers and the both of you quickly make a fresh bed ready to be slept on."

    show bg fenroom_blur
    show gunther naked smile2 at center1
    with dissolve
    Gunther "That was nice, let's do it again sometime."

    Fen blush "Yes, of course!"

    hide gunther
    show bg fenroom
    with s_dissolve
    "Gunther leaves to wash the sheets he helped dirty while you enjoy a lazy day reminiscing about all the cute faces and sounds Gunther makes when you fucked him."

    show bg fenroom_night2
    with s_dissolve
    "By the time the night grows late and you return to your bedroom."

    "It still smells of Gunther, his scent always makes you feel safe. You fall asleep quickly."

    scene bg black
    with s_dissolve

    $renpy.end_replay()

    show transition sleep 01
    with s_dissolve
    play sound "audio/Transition1.ogg" volume 1.0
    
    pause(3.0)

    jump day_start

label gunther_nsfw_01b:
    hide ratio1
    hide fen
    hide gunther
    show bg fenroom at truecenter:
        zoom 1.5
    with s_dissolve
    "You hop onto all fours and lift your fluffy tail."

    Gunther "Heh, I see exactly where you'd like me."

    play sound "audio/Slap 5.ogg" volume 2.0
    "The big cat smacks your hams with his strong hands before pulling them closer."

    Gunther "Mmm, such a nice hole."

    Fen "Ah~"

    "You gasp as Gunther gives your ring a long and slow lick."

    "His hands spread your cheeks apart before his mouth devours your exposed hole."

    scene gunther cg2 00
    with s_dissolve
    play music "audio/light moan 2.ogg" volume 1.0 fadein 1.0
    "You moan and squirm against his grip as he proceeds to eat you out."

    "It may have only been a minute or two, but you are gasping and leaking with quivering knees by the time his lips leave your backside."

    Gunther "Looks like you're ready."

    Fen "{i}*Incoherent moaning*{/i}"

    Gunther "I'll take that as a yes."

    scene gunther cg2 01
    with s_dissolve
    "You feel his larger body slide on top of yours and something hot grinds beneath your tail."

    "The heft of his heavy chests presses onto your back and you can hear panting huffs against your ear."

    "An intense heat radiates off his body matching the same warmth growing inside of you."

    "His arms wrap around your sides, sliding slowly down to your hips."

    "You squirm and arch your back, trying to press more of yourself against him."

    Gunther "Mmm, I'm going to put it in now."

    "Gunther gently guides the tip of his cock right against your pucker."

    "You feel his pulsing head push against your ring until it slowly starts to sink in."

    scene gunther cg2 02
    with s_dissolve
    Fen "Ah.."

    Gunther "Just relax, like that."

    "He murrs softly as you let more of his thickness slide into you."

    "You take a deep breath, letting out another long and soft moan as Gunther slides the rest of the way in."

    "A pleasant stretch works its way deeper into you as the cat's thick cock sheaths itself within your backside."

    "You can feel it throb in your tunnel, the pulse of his shaft presses gently against your prostate, causing your own cock to jump."

    #Slow and light animation
    scene gunther cg2 03
    with s_dissolve
    play music "audio/light moan 1.ogg" volume 1.0 fadein 1.0
    play nsfw1 "audio/deep growls 1.ogg" volume 1.0 fadein 1.0
    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    "He starts slow, just pumping his hips enough to grind his girth inside your tight ass."

    "You grunt as his crotch slaps softly against your butt cheeks, burying the whole thing into your hole."

    "It fills the entire passageway, stretching you almost to the point of discomfort."

    "You feel so full with his meat rod stuffed all the way in."

    "As you keep breathing and letting your muscles relax, it starts to sink in just a bit more."

    "His thick tool hits all the right spots along the walls of the insides, making you kick your feet."

    "Gunther moans deeply as he feels your insides wrap around his length."

    "The tips of his claws drag against your skin as he holds you tight."

    Gunther "Are you ready?"

    "He growls into your ear, sending another shiver down your spine."
    
    "His teeth drag against the rim of your ear with hot breath washing down the side of your neck."

    "You answer his question by lifting your hips and grinding your ass back into his crotch."

    Gunther "Mmm, good answer."
    
    #Slow and Deep animation
    scene gunther cg2 04
    with s_dissolve
    "Slowly, he withdraws about half of his length before pushing it all the way back in."

    Fen "Hng."

    Gunther "Fuck, your ass feels nice."

    "He pulls out and sinks in again, working his entire shaft all the way to the tip now."

    "You moan as he thrusts deeply, rocking your entire body against the thickness impaling you."

    #Slow and Deep animation with sweat
    scene gunther cg2 05
    with s_dissolve
    "Gunther pants as sweat rolls off his brow and onto your back." 

    "Your boss begins to work on your insides with his girth. His cock grinds your prostate like a butter churn."

    "The tiger's fat dick treats your prostate like a punching bag, assaulting it with blow after blow."

    "His thrusts twist your insides up into pleasurable knots, sending muscle spasms to everything below your waist."

    "You whimper and moan into your bed sheets as the big cat continues to destroy your fuzzy rump."

    "Bouncing back and forth, your own cock thrusts against the bed below you as Gunther plows your fuzzy rump."

    Fen "A-Ah!"

    Gunther "Damn, you're so soft."

    #Fast Deep and breath
    scene gunther cg2 06
    with s_dissolve
    play music "audio/light moan 3.ogg" volume 1.0 fadein 1.0
    play nsfw1 "audio/deep growls 1.ogg" volume 2.0 fadein 1.0
    play fuck "audio/fuck fast 1.ogg" volume 2.0
    play ball "audio/ball hits 2.ogg" volume 2.0
    "He nuzzles into your neck as he continues to hump faster. You blush while he continues to pump his thick cock into your ass."

    "You push back against him, attempting to drive him deeper with each thrust."

    "Your tongue hangs to the side of your muzzle as your employer breeds your backside."

    Fen "F-Fuck..."

    "Moaning and grunting, Gunther shows no slowing down as he continues to drill your hole."

    "Your incredibly fit boss shows no signs of tiring."

    #Fast Deep and breath, with air also hot
    scene gunther cg2 07
    with s_dissolve
    "By now the room is sweltering hot, sweat steams off your bodies from the heated passion of two that possess the fire affinity."

    "It's as warm as Marcus's sauna, but it didn't seem to bother either of you as Gunther continued to rail away your backside."

    Gunther "I'm getting close, [name]."

    "Your own body nears the threshold of orgasm as you squirm beneath the muscular cat."

    Fen "G-give it to me!"

    Gunther "GRRRRR!"

    #Cum version
    scene gunther cg2 08
    with s_dissolve
    play sound "audio/light climax 1.ogg" volume 1.0
    play vocal1 "audio/deep climax 1.ogg" volume 1.0
    stop music fadeout 0.5
    stop nsfw1 fadeout 0.5
    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    "Both bodies in heated sync, Gunther growls as he unleashes a torrent of tiger cream right into your bowels."

    "The hot eruption sets off your own orgasm as you cock spasms and empties its load beneath you."

    scene gunther cg2 09
    with s_dissolve
    stop ball fadeout 1.0
    stop fuck fadeout 1.0
    "Grunts and moans continue for a while as Gunther deposits his fresh load off inside your ass."

    "You pant hard, feeling drop after drop of sweat roll off your face."
    
    "The salty streaks catch a drop on your hanging tongue that you lap up greedily."

    scene gunther cg2 06a at right:
        zoom 1.5
    show ratio1
    with s_dissolve
    "Gunther rolls over next to you, his paws still holding onto your sides."

    "You can feel his chest pumping against your back as he catches his breath."

    "His cock still throbs inside your ass. You decide to shake your hips a bit."

    "He growls into your ear."

    Gunther "Careful now, you don't want to be up too late."

    menu:
        "Tease Gunther?"

        "Do it":
            jump gunther_nsfw_01b_again

        "Perhaps not":
            jump gunther_nsfw_01b_end

    label gunther_nsfw_01b_again:

        "You press your luck and keep grinding your cum covered hole against him."

        Gunther "-Growl-"

        Fen "Gah!" with hpunch

        scene gunther cg2 07a
        with s_dissolve
        "You feel his claws dig into your hips, dragging your ass back towards him."

        Gunther "I warned you..."

        scene gunther cg2 06
        with s_dissolve
        play music "audio/light moan 3.ogg" volume 1.0 fadein 1.0
        play nsfw1 "audio/deep growls 1.ogg" volume 2.0 fadein 1.0
        play fuck "audio/fuck fast 1.ogg" volume 2.0
        play ball "audio/ball hits 2.ogg" volume 2.0
        "His still throbbing cock sinks right back into your stretched insides."

        "He's even rougher this time around, no doubt {b}you will be sore tomorrow{/b}."

        "You bite your pillow and endure the full force railing your poor ass is about to be subjected to."

        "Surely this is worth it..."

        scene bg black
        with s_dissolve

        #fade to black, if there are nsfw slapping noises, keep playing it during the fade

        "..."

        pause

        stop music fadeout 3.0
        stop nsfw1 fadeout 3.0
        stop ball fadeout 3.0
        stop fuck fadeout 3.0

        $renpy.end_replay()

        if gunther_sxp_2 == False:
            $ gunther_sxp_2 = True
            call sxp_up from _call_sxp_up_1
    
        else:
            pass

        scene bg black
        with dissolve

        pause

        $ ap -= 2

        centered "-Next day-"
        with s_dissolve
        #morning animation
        scene bg fenroom
        with s_dissolve

        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0

        "You must have passed out at some point. Your body feels sore and your ass definitely aches."

        "{color=#16f58d}{i}Action points for today decressed by 2!{/i}{/color}"

        "Gunther can be heard downstairs working in the kitchen, but it seems he managed to change your sheets at some point."

        jump day_activity


    label gunther_nsfw_01b_end:

        Fen "Alright, I'm exhausted."

        if gunther_sxp_2 == False:
            $ gunther_sxp_2 = True
            call sxp_up from _call_sxp_up_3
    
        else:
            pass

        show bg fenroom
        with s_dissolve
        "Gunther nuzzles your neck again and looks around for some fresh sheets."

        "In a few moments, he helps you throw on some clean bed sheets."

        scene bg fenroom_blur
        show gunther naked normal at center1
        with dissolve
        Gunther "Are you satisfied?"

        Fen "Mm... Yeah. Thank you."

        Gunther "No need to, I needed that too."

        Gunther naked wink "Just ask if you want another round."

        hide gunther
        show bg fenroom
        with dissolve
        play sound "audio/Door Close.ogg" volume 1.0
        "He waves and saunters out of your room naked, closing the door behind him with his tail."

        "Now you won't have to sleep in a wet blanket, but the room still smells of your sweat and sex."

        "You welcome bask in Gunther's scent, the familiar smell makes you feel... something."

        scene bg fenroom_night2
        with s_dissolve
        "Tonight, you will sleep well."

        scene bg black
        with s_dissolve

        $renpy.end_replay()

        show transition sleep 01
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
    
        pause(3.0)

        jump day_start

#Talk with gunther in backyard
label gunther_talk_01:
    menu:
        "About Niall..." if bond04 == 2:
            jump gunther_talk_topic5

        "How did you get so big?":
            jump gunther_talk_topic1

        "Have you always been the owner of Flaming Flagon?":
            jump gunther_talk_topic2

        "What do you do for fun?":
            jump gunther_talk_topic3

        "Do you have any family?":
            jump gunther_talk_topic4

        "Back":
            jump backyard_gunther_menu

    
    label gunther_talk_topic1:
        Fen "So how did you get so fit? It can't just be from working at the bar."

        Gunther uw smile2 "Ha, a little of it is from operating the tavern. Those barrels can get pretty heavy."

        Gunther uw normal "But I also work out regularly. In another life, I was trained to keep myself in tip top shape both physically and mentally."

        Fen "Another life?"

        Gunther uw stern"I might tell you more about it someday..."

        Gunther uw normal "But as you can see, being strong definitely has many advantages."

        Gunther "No one dares start a fight in my tavern, I threw out the one and only guy who ever did."

        Gunther "People say he is still falling from the sky to this day."

        Fen "Seriously?"

        Gunther uw smile2 "No, of course not. But he did land on the other side of the street."

        Fen "That's still really impressive."

        Gunther "Everyone else thought so too."

        jump gunther_talk_01

    label gunther_talk_topic2:
        Fen "Have you always operated the tavern?"

        Gunther uw normal "Yep. I took out a loan, and had the building constructed here."

        Fen "You're a real entrepreneur."

        Gunther uw wink "That's right."

        Gunther uw smile2 "I'm the first and only owner of The Flaming Flagon."

        Gunther "And this tavern has serviced the people of Felda for a few years now. It's become a staple for most people to stop by for a drink after their work day."

        Gunther uw normal "Taking care of the tavern is pretty much all I have time for."

        Gunther "Without extra coin, I've been having to do everything myself."

        Gunther "Well that was until you came along."

        Fen "Aww, you did save my life."

        Gunther uw stern "I couldn't just let you die there..."

        "Gunther seems really sad for a moment."

        jump gunther_talk_01

    label gunther_talk_topic3:
        Fen "So what do you do for fun?"

        Gunther uw stern "Fun? Well I guess the little time I'm not working or working out, I like to walk along the countryside."

        Gunther uw normal "That's actually how I started getting better deals on my alcohol."

        Gunther "I see them working out in their fields on my walks and finally one farmer waved at me and started chatting."

        Gunther "They were always looking for more people to buy their goods and they cut me a deal."

        Gunther "I go visit them from time to time to sample anything new and renegotiate sales."

        Gunther "Actually, I was on my way back from sampling some new beer when I found you."

        Fen "Oh, I had no idea."

        Gunther uw smile2 "Glad I did, you still been still layin' out there otherwise."

        jump gunther_talk_01
    
    label gunther_talk_topic4:
        Fen "Do you have any family?"

        Gunther uw normal "Not really. My parents separated when I was young."

        Gunther "I was left with my father until he passed away many years ago"
        
        Gunther "I don't really remember my mother and as far as I know, I'm their only child."

        Fen "Aww."

        Gunther "I don't suppose you remember anything about your family?"

        #Flash silhouette of Fen's dad

        scene bg kitchen2_blur
        show ratio1
        with s_dissolve
        "You try to remember." 


        show ragnar normal_blur at center1 behind ratio1:
            ypos 1900
            zoom 1.5
        with s_dissolve
        "You know you had to have had a mother...and a father."

        "Trying to remember their faces and drawing only a blank makes you sad."

        scene bg tavernback
        with dissolve
        Fen "I...I don't."

        show gunther uw normal at center1
        show bg tavernback_blur
        with dissolve
        Gunther "Aww, don't fret."

        Gunther uw smile2 "I'm sure with such a good lad like you, your family would be looking for you."

        Fen "Thanks."

        show gunther uw blush3:
            ypos 1700
            zoom 1.3
        with dissolve
        "You lean over and give Gunther a hug."

        show gunther at center1:
            zoom 1
        with dissolve

        jump gunther_talk_01

    label gunther_talk_topic5:
        Fen "Niall is back. I talked with him, and he should be fine now."

        Gunther uw stern "Well, that's good news."

        Fen "Yes, it is. Don't you have something else to say?"

        Gunther uw stresse4 "..."

        Gunther "Sorry, I messed up that night."

        Fen "And?"

        Gunther "Thank you for covering for me."

        Fen "Heh, I'll take it."
        
        Fen "I know it's not entirely your fault. Niall was acting a bit off that night as well—he realized that too."

        Fen "So... you said the stories he told about you were exaggerated."

        Fen "How much of them are actually true?"

        Gunther uw stern "Well, I was an adventurer once, that much is true."

        Fen "Sure..."

        "It's clear Gunther isn't ready to share more for now."

        jump gunther_talk_01

#Cleaning with Gunther
label gunther_event_01:

    if gunther_clean_done == False:
        $ gunther_clean_done = True
        stop music fadeout 3.0
        scene bg tavern3
        with s_dissolve
        "Gunther stands there with brooms, buckets, and washcloths."

        show gunther normal at center1
        show bg tavern3_blur
        with dissolve
        Gunther "Alright, let's get the tables and counters wiped down."

        hide gunther
        show bg tavern3
        with dissolve
        "You both take a bucket and get to cleaning."

        Gunther "Once all the surfaces are wiped, go ahead and sweep the floors."

        Fen "Got it!"

        "Gunther continues to wipe down the bar's counter while you sweep up the floors."

        $ bondexp01 += 2
        call bondexpup01 from _call_bondexpup01_3

        "With your efforts combined, you both make quick work of the remaining cleaning and the bar is ready to open."

        jump night_start

    else:
        pass

    stop music fadeout 3.0
    scene bg kitchen_nofire
    with s_dissolve

    $_dismiss_pause = False

    "After getting some breakfast, you joins Gunther in cleaning work."

    play sound "audio/Transition2.ogg" volume 1.0
    scene bg tavern3
    show transition clean 01
    with s_dissolve
    pause (3.0)

    "With your combined efforts, you make quick work of the cleaning and soon the bar is ready for opening."

    $ bondexp01 += 2
    call bondexpup01 from _call_bondexpup01_4

    $_dismiss_pause = True

    jump night_start

# Workout with Gunther
label gunther_event_02:

    if gunther_workout_done == False:
        $ gunther_workout_done = True

        show gunther uw wink with dissolve
        Gunther uw wink "'Atta boy! Get ready. You're gonna be sore when I get through with you."

        hide gunther
        show bg tavernback
        with dissolve
        "You decide to take off your shirt so that it won't get soaked in the expected sweat."

        #Fen shirtless
        "As you strip it off, you feel the gentle breeze against your chest fur."

        show fen 3 normal at left1
        show bg tavernback_blur
        with dissolve
        Fen 3 normal "Oh, I'm ready!"

        show gunther uw smile2 at right1
        with dissolve
        Gunther "That's the spirit. Let's get started then."

        hide fen
        show bg tavernback_blur at truecenter:
            zoom 1.5
        show gunther uw normal at center1:
            ypos 2000
            zoom 1.5
        show ratio1
        with dissolve
        "Gunther begins the workout with a quick warmup."

        show gunther uw normal at center1:
            ypos 1500
            zoom 1.5
        with move
        "You watch the big cat start with stretching. He bends over and grabs his ankles without any issues."

        "His tail stands straight up behind him."

        hide ratio1
        show gunther at right1:
            zoom 1
        show bg tavernback_blur:
            zoom 1
        with dissolve
        Gunther "It's important to always stretch, lowers the chances of injuring yourself."

        show fen 3 blush at left1
        with dissolve
        Fen "Ah, that makes sense."

        hide fen
        hide gunther
        show bg tavernback
        with dissolve
        "You try to follow Gunther's exercises, but the cat is much more flexible than you."

        "After some stretching, you both get your heart rates up by jogging around in a circle for a few minutes."

        show gunther uw smile2 at center1
        show bg tavernback_blur
        with dissolve
        Gunther "Alright, got the blood flowin'!"

        "The bartender hasn't broken a sweat, but you can already feel a few beads running down the sides of your face."

        Gunther "Now, the real workout begins."

        hide gunther
        show bg tavernback_blur at center:
            zoom 1.5
        show log at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "The cat walks over to a heavy and scratched up log."

        hide ratio1
        show gunther uw normal at center1
        show bg tavernback_blur:
            zoom 1
        with dissolve
        Gunther "This is a log from an ironwood tree. They are incredibly heavy, dense, and a little fire resistant."

        "Gunther grabs both ends of the log with his claws and lifts it off the ground and up to his chest waist before setting it back down." with vpunch

        "He repeats the motions nine more times." with vpunch

        Gunther "Phew~ Alright, [name]. You give it a try."

        Fen "Okay."

        hide gunther
        show bg tavernback_blur at center:
            zoom 1.5
        show log at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "You walk up to the log and try to pick it up."

        "It weighs less than a barrel full of ale, but not by much."

        hide log
        hide ratio1
        show bg tavernback_blur at center:
            zoom 1
        show fen 3 stresse2 at center1
        with dissolve
        Fen "Hngg!"

        "With some effort, you are able to lift the log off the ground." with vpunch

        hide fen
        show bg tavernback
        with dissolve
        "The first three reps feel okay, but you can feel your arms and back burning halfway through your fourth rep."

        show gunther uw normal at center1
        show bg tavernback_blur
        with dissolve
        Gunther "Careful now, don't overdo it. We're just working out."

        "You drop the log, unable to hold onto it for a fifth lift."

        $ bondexp01 += 3
        call bondexpup01 from _call_bondexpup01_1
        Gunther uw wink "Not bad, looks like you have a few muscles under all that fluff after all."

        show gunther uw normal
        "Gunther continues on with a few more exercises that each leave your muscles aching while he only breaks out into a light sweat." with vpunch

        hide gunther
        show bg tavernback
        with dissolve
        "Your body feels sore but pumped. It is a good ache."

        stop music fadeout 3.0
        Fen "Mmm."

        if str_from_workout < 5:
            $ str_from_workout += 1
            call str_up from _call_str_up        
            "Your strength increases as a result of the workout!"

        else:
            "It seems like you can't gain any more strength from this activity."
            pass

        jump day_end

    
    else:
        pass


    Gunther uw normal "Ready to get sweaty?"

    Fen "Heh, yes. Of course!"

    Gunther uw smile2 "Good lad, let's get to it!"

    hide gunther
    show bg tavernback
    with dissolve
    "You both stretch and begin another intense workout session."

    $ bondexp01 += 2
    call bondexpup01 from _call_bondexpup01_2

    "Sore but good, you wipe the hard earned sweat from your brows."

    if str_from_workout < 5:
        $ str_from_workout += 1
        call str_up from _call_str_up_1
        "Your strength increases as a result of the workout!"

    else:
        "It seems like you can't gain any more strength from this activity."
        pass

    jump day_end

# Takes you to bathhouse
label gunther_event_03:
    show gunther normal at right1
    show bg kitchen_blur
    with dissolve 
    Gunther "Mornin'."

    show fen normal at left1
    with dissolve
    Fen normal "Good morning."

    Fen stern3 "Yawn."

    Gunther "Still tired? Sleep in."

    Fen smile "I might."

    Gunther stresse "Well at least make some breakfast first..."

    Fen normal "Alright, alright."

    hide fen
    hide gunther
    show bg kitchen
    with dissolve
    "You light the stove and whip a few eggs in a bowl."

    "In a few minutes, you have a jiggly yellow mass wobbling on a plate."

    show fen smile at left1
    show bg kitchen_blur
    with dissolve
    Fen "Breakfast is served."

    show gunther smile at right1
    with dissolve
    Gunther "Good boi."

    show fen eat
    show gunther stern
    with dissolve
    "As you dig in, Gunther pokes his fork at you."

    Gunther "You should also do something about your fur."

    Fen stresse "What do you mean?"

    Gunther "You're normally floofy, but now ya got all these tangles and matted patches everywhere."

    Fen sweat "I suppose I need to go buy a brush."

    Gunther normal "I should take you down to the bathhouse, they sell brushes and stuff to get that fur of yours straightened out."

    Fen normal "Alright, it'd be nice to get these knots out."

    Gunther "Alright cub, we'll when we're done eating."

    Fen eat "Mhmm."

    show gunther smile at shock
    Gunther "This is tasty!"

    Fen "It's just scrambled eggs."

    Gunther "But they're so fluffy, unlike your fur."

    Fen eat "..."

    stop music fadeout 2.0

    hide fen
    hide gunther
    show bg kitchen
    with dissolve
    "You both finish your tasty breakfast and prepare to visit the bathhouse."

    scene bg townstreet
    with s_dissolve
    play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
    "After breakfast, you leave through the kitchen and head towards a large marble building."

    #scene change to daytime outside the tavern

    show gunther normal at center1
    show bg townstreet_blur
    with dissolve
    Gunther "It's not too far from here. It's just a couple of streets down from the market."

    Fen "Do you go there often?"

    Gunther "Not really."

    Gunther wink "This tiger takes pretty good care of his fur."

    Fen "Ah...So is it popular?"

    Gunther smile "Yeah, they offer spa treatments."

    Fen "I've never heard of a spa before."

    show gunther shock at shock
    Gunther "What? You gotta be kidding!"

    Fen "I am not. What's a spa?"

    Gunther stern "Cub..."

    Fen sad "What?"

    Gunther "You keep surprising me sometimes."

    Fen "Is that...weird?"

    Gunther normal "A little, but maybe it's the memory loss."

    Gunther wink "Nevermind that, as the saying goes. \"Take care of your employees, and they'll take care of you.\""

    Gunther "And I'm gonna take {b}good{/b} care of you."

    show gunther normal
    "Gunther's looking at you like some sort of investment."

    Fen sweat "So a spa?"

    Gunther smile "Yes! Massages, skin and fur treatments, the whole works."

    Gunther normal "Anyone can find something there, they help those with thick and leathery hides and even those with scales."

    Fen "People are into that sorta thing?"

    Gunther "Of course. Healthy and clean skin isn't just hygienic, it's part of your overall wellness."

    Fen "I suppose you're right."

    Gunther "Great, let's get there."

    scene bg market
    with s_dissolve
    "It's particularly warm today as the sun shines brightly in the sky."

    show gunther smile at right1, flip
    show bg market_blur
    with dissolve
    Gunther "Beautiful day."

    show fen sweat at left1
    with dissolve
    Fen sweat "Kinda warm."

    show gunther normal at flipback
    with dissolve
    Gunther "You'll feel better once we get that fur sorted out."

    Fen "Of course, thanks again."

    Gunther smile "You're welcome! I can't have my staff looking all mangy and unkept."

    Fen sweat "Yeah...thanks."

    stop music fadeout 2.0
    show gunther normal at flip
    with dissolve
    Gunther "It's going to get busy on a hot day like this. Let's go ahead and get inside before there's a line."

    scene bg bathhousehall
    with s_dissolve
    play music "audio/Sir Gawain.ogg" volume 1.0 fadein 3.0
    "Inside the building, the air is a bit steamy."

    "Great doorways are cut into the stone walls and covered by a simple curtain."

    "Besides the doors is a large counter with small bottles of flowery and sweet smelling liquids and creams."

    "Behind the counter stands a tall and broad man."

    "The rhino man smiles and waves at you both as you enter."

    Gunther "Hey Marcus."

    "Gunther walks up to the purple guy wearing a toga."

    show marcus normal at top:
        zoom 1.5
    show bg bathhousehall_blur at truecenter:
        zoom 1.5
    with dissolve
    #focus and center image of Marcus start from top to bottom

    "He's not as tall as Terrance, but he looks like he's just as strong as the horse."

    show marcus normal at center1:
        zoom 1.5
    show bg bathhousehall_blur at truecenter:
        zoom 1.5
        ypos 400
    with ease
    "His purple hide appears soft and he smells like lilies growing in a freshwater spring."

    "He also has a rather thick and ridged..."
    
    show marcus normal at top:
        zoom 1.5
    show bg bathhousehall_blur at truecenter:
        zoom 1.5
    with move
    "...horn sprouting from his forehead."
    #cut back to Marcus's head at the ...
    
    #cut back to Fen and Gunther on left, Marcus on right

    show gunther normal at left2, flip behind marcus
    show marcus smile at right3:
        zoom 1
    show fen stern at left3
    show bg bathhousehall_blur at center:
        zoom 1
    with dissolve
    Marcus "Gunther! It's been ages. What can I do for you?"

    Gunther "Oh not much, I just need a few things and didn't feel like paying extra at the market stalls."

    show marcus shock at shock
    Marcus "Oh dear, that fur! Who's this scraggly looking fellow?"

    show gunther at flipback
    with dissolve
    Gunther "This is [name], my new employee."

    Marcus stern "Sweet child, take off those clothes and let me have at that fur!"

    show fen blush at shock
    Fen blush "W-What?!"

    show gunther at flip
    with dissolve
    Gunther "Ahm, speaking of children. How are the kids?"

    Marcus normal "Hardly children, they're all grown up and off on their own working. Leaving me here to run the place myself."

    Gunther "I see you've had some remodeling done."

    Marcus normal "Ah, it really has been a while for you!"

    Marcus "Please, you must check out the new pools."

    hide marcus
    hide gunther
    hide fen
    show bg bathhousehall
    with dissolve
    "The bathhouse is a square building, each main section separated into quadrants." 

    "Three pools and the front area make up these four quadrants of the bathhouse."

    scene bg bathhouse1
    with s_dissolve
    "The owner shows you over to the larger pool first."

    show marcus normal at center1
    show bg bathhouse1_blur
    with dissolve
    Marcus "Here's the Delphinium pool. Take a relaxing dip in the blue pool under the bright sun in this glass roof area."

    Marcus "This is where the masses come to kick up their feet and relax in the heated waters."

    Marcus "Please just be sure to rinse off using any of the fountains along the walls before entering any pool."

    Fen "Oh, it's pretty."

    Marcus "And from pretty, we have magnificent. For our premium clientele, please come see the Narcissus pool."

    scene bg bathhouse2 at flip
    show fog
    with s_dissolve
    "He leads you to a smaller pool. The side area is adorned with a more secluded alcove where steam billows out from constantly."

    show marcus normal at center1 behind fog
    show bg bathhouse2_blur
    with dissolve
    Marcus "Here at the luxury Narcissus section, you are treated to all the amenities of the Delphinium with a more private setting."

    Marcus "While relaxing here, treat yourself to some of the bathhouse's modest refreshments."

    Marcus "You may find some tasty treats as many of the patrons of this bath are merchants looking for an easy way to promote their goods with samples."

    Marcus grin "That is if they {b}withstand the steam here{/b}."

    Fen "Yeah... It's pretty warm here."

    Gunther "What's that section over there?"

    Marcus normal "Oh, that would be my private pool. I call her Belladonna."

    Marcus "Hmm, well since this place wouldn't have existed without you, Gunther. I suppose you two can have a quick look."

    scene bg bathhouse3 at flip
    with s_dissolve
    "Marcus leads you to his private pool in the bathhouse."

    "The area is smaller and more intimate than the other two pools."

    "A large padded table is on one side of the room and a separate soaking tub is across from it."

    show gunther normal at left2, flip
    show bg bathhouse3_blur
    with dissolve
    Gunther "That's a lovely bench."

    show marcus smile at right3
    with dissolve
    Marcus "Thanks, a couple of the boys made it during their guild apprenticeships."

    show fen stern at left3
    with dissolve
    Fen "What's that for?"

    Marcus normal "It's a massage table. Fits most people, big and small."

    Marcus smile "If you're lucky enough to find yourself on it, be prepared for me to rub away all your problems until you melt."

    Gunther grin "He does give a great massage."

    Fen blush "I see..."

    Marcus normal "Now, back to the front. I can't leave the counter unattended for too long."

    scene bg bathhousehall
    with s_dissolve
    "Marcus ushers you both back to the front of the bathhouse."

    show gunther normal at left2, flip
    show fen normal at left3
    show bg bathhousehall_blur
    with dissolve
    Gunther "Alright, not to hold up your business. I think we'll go ahead and take care of [name] here."

    show marcus normal at right3
    with dissolve
    Marcus "Of course, of course. I have some products that will sort this mess out in no time."

    Gunther "Thanks."

    #slide Marcus off screen
    hide marcus
    with dissolve
    "Marcus turns away, walks over to the shelves and starts picking out goods."

    show fen stern at flip
    with dissolve
    Fen "Umm, what's that over there?"

    Fen "There's a lot of steam coming out of there."

    show gunther smile2 at flipback
    with dissolve
    Gunther "Yep! It's a relic that I..."
    
    Gunther stern "...err that was brought back from the dungeon years ago."

    show fen at flipback
    with dissolve
    Fen "A relic?"

    Gunther normal "Relics and artifacts are magical items that can have wondrous effects." 

    Fen "Huh? So it's like an object that has an affinity?"

    Gunther stern "I guess you can think of it like that. I'm not as well versed in the details, but I know a crazy old bird who could tell you more."

    #dropping the Cal reference here
    #Show Marcus

    show marcus normal at right3
    show gunther at flip
    with dissolve
    Marcus "I'm back. Yes, there's a special crystal that produces endless hot water."

    Marcus "However the water completely disappears after a day, so it's not worth using it to drink or cook with."

    Fen normal "But it's perfect for a bathhouse."

    Marcus smile "He's a sharp pup."

    Gunther smile2 "Aye, that he is."

    Marcus "Alright, I have just the things for him ."

    show marcus normal at center1
    show gunther normal
    with dissolve
    "Marcus hands you a heavy duty brush and a couple of bottles."

    show marcus at right3
    with dissolve
    Marcus "So that's stuff pretty concentrated. You need only a few drops in a bucket of water."
    
    Marcus "The white fluid is the cleaner, and the clear fluid is the conditioner." 

    show fen smell
    with dissolve
    "You sniff the white bottle and to your surprise, there's no distinct smell."

    "When you take a whiff of the clear conditioner, you smell a faint hint of blossoming mountain flowers."

    Fen smile "Thanks."

    show gunther at flipback
    with dissolve
    Gunther "[name], you should stop by sometime. Like I said, he gives a really good massage."

    Marcus grin "If they're so good, why haven't you been around for one?"

    show gunther smile at flip
    with dissolve
    Gunther "This tiger stays pretty limber."

    Marcus "I could make that tail curl."

    Gunther blush2 "No doubt. So um, how's business?"

    Marcus smile "Well enough, I'm getting by well enough with some extra coin from some deals Murry secured through the market square."

    Marcus "It's allowed me to better run the downsized baths."

    Gunther normal "That's great."

    Marcus normal "Yep, and I get some more free time in the afternoons."

    Gunther "Oh? You should stop by the Flaming Flagon then."

    Marcus "I think I will, I heard you've got some good food now."

    Gunther stern "What do you mean 'now'?"

    Marcus sweat "I mean it's been a very long time, I just overheard some customers talking about some new food at your place."

    Marcus normal "And as you know, big guys like me enjoy eating."

    Gunther smile "That's the 'only' reason you're so big?"

    Marcus blush "If you gentlemen will excuse me, I have a massage appointment."

    show gunther normal at center1
    with dissolve
    play sound "audio/payment.ogg" volume 3.0
    Gunther normal "Here's payment for the bath and cleaners."

    Marcus normal "Of course, thank you and enjoy the Delphinium."

    "Marcus slides two baskets over to Gunther."

    show gunther wink at left2
    with dissolve
    Gunther wink "Catch ya later, Marcus."

    Fen normal "Thanks again."

    Marcus "You're welcome. It was nice to meet you, [name]."

    hide marcus
    with dissolve
    "Marcus disappears behind a curtained doorway."

    show gunther smile at flipback
    with dissolve
    Gunther "Alright, let's go rinse off and enjoy the pool for a bit."
    
    #scene bg bathhouse1

    scene bg bathhouse1
    with s_dissolve

    "There are shelves near the entrance for people to store their baskets."

    #show Gunther naked
    show gunther naked normal at right1
    show bg bathhouse1_blur
    with dissolve
    "Gunther strips and puts his clothes into the basket." 

    "You ogle the buff cat for a moment before disrobing yourself."

    show fen naked blush at left1
    with dissolve
    "Folding away your clothes and storing them in a free space, you start to feel more comfortable with all the nudity."

    Gunther "The spouts here constantly pour out warm water. There are buckets everywhere to mix soap or rinse off."

    Gunther naked smile2 "Would you like me to help wash your back?"

    Fen "S-sure."

    show gunther naked normal at right2:
        zoom 1.5
        ypos 1800
    show fen naked relax at left2, flip:
        zoom 1.5
        ypos 1800
    show bg bathhouse1_blur at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You both soak your fur in the relaxing warm water before you mix the soap according to instructions you were provided."

    "All the grime and dirty melt away from your fur and skin the moment the cleaning mixture soaks in."

    "Gunther rubs his strong paws along your back, giving it a good coating of soap."

    hide fen
    hide gunther
    hide ratio1
    show bg bathhouse1 at truecenter:
        zoom 1.5
    with dissolve
    "You then work the conditioner into your fur and let it sit for a few minutes before rinsing off the nice smelling lather."

    "He turns and gestures to his own back."

    show fen naked relax at left2:
        zoom 1.5
        ypos 1800
    show gunther naked normal at right1, flip:
        zoom 1.5
        ypos 1800
    show bg bathhouse1_blur at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You return the favor and splash soapy water onto his broad back. Your paws scrub in the cleaner and feel the strong muscles of the cat's shoulders."

    "Your fingers trace over a few scars hidden beneath his thick red fur, wondering where they came from."

    Gunther "Alright, I think we're clean enough for the pool."

    hide fen
    hide gunther
    hide ratio1
    show bg bathhouse1 at truecenter:
        zoom 1.5
    with dissolve
    "You rinse off one more time and follow Gunther into the pool. Other people leaned and sat along the side of the water chatting idly as they relaxed in the bubbling waters."

    "It really feels good to soak for a bit after all your hard work at the tavern."

    "Gunther seems to have less patiences for the waters than you as he is the first to exit the pool."

    show gunther naked normal at top:
        zoom 1.5
    show bg bathhouse1_blur at truecenter:
        zoom 1.5
    with dissolve
    Gunther "Alright, I don't want my skin to get all wrinkly. I'm going to go rinse off."

    hide gunther
    show bg bathhouse1 at truecenter:
        zoom 1
    with dissolve
    "You follow him out and find a clean bucket to wash the pool water off your fur."

    "Gunther looks around and just shoves his head under the wall spout to rinse off."

    "You go through a few more buckets of water before Gunther pats your fur dry by applying his affinity to his palms."

    "The conditioned fur allows the brush to easily slide through, optimizing your floofiness."

    show gunther naked smile2 at center1:
        zoom 1
    show bg bathhouse1_blur at truecenter:
        zoom 1
    with dissolve
    Gunther "Heh, you almost look like an orange cloud."

    hide gunther
    show bg bathhouse1 at truecenter:
        zoom 1
    with dissolve
    stop music fadeout 3.0
    "You redress feeling cleansed and return with Gunther to the Flaming Flagon for a quiet evening."

    call bondlvup0600 from _call_bondlvup0600
    $ marcus_bond_ui = True

    #show Fen with sparkle effects

    $ show_freeday_option('go to bathhouse')

    jump day_end

#Gunther bond event 2
label gunther_bond_02:
    scene bg tavern1
    with s_dissolve
    stop music fadeout 3.0
    "Another shift over at the Flaming Flagon. The night winds down as one by one, the tables empty."

    "The last guest stumbles home drunk and you finish stacking up the last stool onto the tables."

    show bg tavern1_blur
    show fen sweat at left1
    with dissolve
    Fen sweat "Phew."
    
    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    show gunther normal at right1
    with dissolve
    Gunther "Working hard out there, [name]."

    Fen normal "No busier than any other night."

    Gunther smile2 "Hey, come'ere. Let's have a drink."

    show fen stern at shock
    Fen "A drink with Gunther, how could I say no?"

    Gunther normal "Have a seat, you earned it."

    Fen normal "Thanks." 

    hide fen
    show bg tavern1_blur at top:
        zoom 1.5
    show gunther normal at top:
        zoom 1.5
    with s_dissolve
    play sound "audio/pour drink.ogg" volume 3.0
    "You watch curiously as Gunther gathers various bottles and pours it into a large metal cup filled with ice."

    "He shakes the mixture vigorously before pouring some into a couple of glasses."

    "You can smell how strong and sweet the concoction is as he slides the glass towards you."

    hide gunther
    show food drink3 at truecenter
    show ratio1
    with s_dissolve
    Gunther "Here ya go."

    Fen "Hmm, I don't think I've seen this before."

    Gunther "It's something new I came up with."

    play sound "audio/drink.ogg" volume 2.0
    "You take a sip of Gunther's new cocktail."

    hide food drink3
    hide ratio1
    show bg tavern1_blur at center:
        zoom 1
    show gunther normal at right1
    show fen stern at left1
    with dissolve
    Fen "Mmm!"

    Gunther smile2 "Pretty good, huh?"

    Fen lick "Kind of strong, but very tasty."

    Gunther "I had the same thoughts."

    Fen smile3 "It's been a while, but something about all this seems familiar."

    Gunther normal "Remember anything specific?"

    Fen stern "Not exactly. It just feels like I've done this all before?"

    Gunther stern "You feel like you've had amnesia before?"

    Fen "What? No, I mean all of this. Cooking, serving food and drinks."

    Gunther "You think you used to work at another tavern?"

    Fen "Not exactly."

    Gunther normal "I could always ask around to some of the other taverns across the kingdom, but I'd hate to lose my best employee to some competition."

    Fen "I don't think it would come to that, but I just wish I knew, ya know?"
    
    Fen "I also still feel like something I'm trying to remember is far away."

    Gunther "I hope you get your answers, [name]. Till then, you are welcome to live and work here as long as you'd like."

    play sound "audio/pour drink.ogg" volume 3.0
    "He pours another drink for both of you and lifts his glass."

    Gunther "Cheers."

    hide fen
    hide gunther
    show bg tavern1
    with dissolve
    play sound "audio/glass clink.ogg" volume 3.0
    "You tap your glass against his and you notice Gunther suddenly looks... sad?"

    show bg tavern1_blur
    show fen stern at left1
    show gunther stern at right1
    with dissolve
    Fen "Are you okay?"

    Gunther "Yeah... you just reminded me of someone I knew a long time ago."

    Fen smile2 "Did he have amnesia too?"

    Gunther grin "Ha! No, he didn't."

    Gunther normal "It's a sad story I'd rather not get into right now."

    show fen blush3 with dissolve
    Fen "Oh... what about a happy story then?"

    Gunther "Maybe you should get ready for bed."

    Fen blush "Noooo, too early. I want another drink."

    Gunther smile2 "Very well, you've definitely earned it."

    show fen blush4
    show gunther normal
    with dissolve
    play sound "audio/pour drink.ogg" volume 3.0
    "Gunther mixes another drink while your tail wags back and forth excitedly."

    "The force of your tail wagging causes you to sway side to side in your seat."

    Gunther smile "Heh, someone's excited. Here ya go."

    show fen at shock
    Fen "Thanks!"

    Gunther normal "Alright, I got a story for you."

    Gunther stern "Powerful relics draw adventurers to the dungeon of Felda."
    
    Gunther stern2 "Before the tavern, I was just another relic hunter, looking to make a fortune."

    Gunther stern "We would meet our party members from either the adventurer guild or meet in a tavern just like this one."

    "You nod and sip on your drink as Gunther continues."

    Gunther "We thought we were unstoppable."
    
    Gunther normal "We felled mighty monsters, transversed trapped filled labyrinths, and colossal horrors that could haunt you for the rest of your life."

    Gunther "On one such relic hunt, we ventured for a week until we came across a wishing well."

    show fen at shock
    Fen "Seriously?!"

    Gunther "That's what the sign said next to it. Toss in a coin and make a wish."

    Gunther "I figured it was some sort of trap. The rogue through it was a scheme and someone was waiting to collect your money at the bottom."

    Fen "I would have thrown a coin in."

    Gunther "That's what the third guy did."

    Fen "Did he make a wish?"

    Gunther stern "Well, he was about to when the well spat his coin out. Turns out I was right. It was a mimic."

    Fen "Mimic?"

    Gunther "It's a monster that disguises itself as objects and attacks when you get close enough."

    Fen "That's scary."

    Gunther sweat "Yeah, a little bit."

    Gunther smile2 "Then there was the time someone mistook my tail for a tentacle monster..."

    hide gunther
    hide fen
    show bg tavern1
    with s_dissolve
    "Gunther goes on into another story as you feel the room slowly sway left and right."

    show bg tavern1_blur
    with s_dissolve
    "The strength of the drinks hit you hard with sudden fatigue."
    
    "You can hear the big cat talking, but unable to make out any of his words as you slowly rest your head on the counter top."

    show bg tavern1_blur at top:
        zoom 1.5
    show gunther normal at top:
        zoom 1.5
    with s_dissolve
    Gunther "Am I boring you?"

    Fen "Zzz..."

    Gunther smile "Heh, lightweight."

    Fen "S-Shut up..."

    Gunther "Alright, let's get you to bed."

    hide gunther
    show bg tavern1_blur at center:
        zoom 1
    with s_dissolve
    "Gunther walks around the bar counter and scoops you into his arms."

    "Even with your head spinning, you remember this feeling."

    show bg tavern1_blur at top:
        zoom 1.5
    show gunther normal at top:
        zoom 1.75
        ypos -170
    show ratio1
    with s_dissolve
    "A pair of strong red arms pick you up, the familiar scent of the man carrying you through the darkness."

    "Your very first memory before you arrived in Felda replays in your head."

    "This is not a very pleasant memory and your body attempts to fight away the memory of your painful experience."

    menu:
        "You reach out for something..."

        "Chest":
            jump grope_chest

        "Arm":
            jump grope_arm

        "Neck":
            jump grope_neck

    label grope_chest:
        "You unconsciously reach out and grab something round, yet firm. Remembering that first moment when you woke up in a world filled with pain, you instinctively grip tightly to Gunther."

        Gunther "Why are you gripping my pec so hard?"

        "He chuckles as you mumble."

        jump gunther_bond2_cont

    label grope_arm:
        "You grab Gunther's arm. You wrap around his larger biceps and cling for dear life."

        Gunther "Whoa, it's okay buddy. You're going to rip my arm off squeezing it that hard."

        "You feel his hand stroke the top of your head."

        Gunther "It's alright, it's just me."

        jump gunther_bond2_cont

    label grope_neck:

        "You hug Guther's neck, letting your head drape over his muscular shoulder."

        Gunther "Airight buddy, you're definitely drunk."

        Fen "And you're hot."

        Gunther "Thanks, but I'm going to have to assume that's the alcohol talking."

        Fen "S-seriously t-though."

        Gunther "Settle down now, we'll get you to bed in just a moment."

        jump gunther_bond2_cont

    label gunther_bond2_cont:
        "You grumble and shift around in his arms."

        Gunther "You'll be in your bed soon, stop fidgeting or I might drop you."

        "Your fit comes to an end when you bury your face into the cat's chest, instinctually seeking a semblance of comfort and safety."

        "Whether you remember it in the morning or not, you acknowledge now that you always feel safe around Gunther."

        scene bg black
        with s_dissolve

        scene bg fenroom_night
        with s_dissolve
        "He takes you up to your room and gets you into your bed."

        Gunther "Alright, time to let go of me. Get some sleep."

        Fen "-Grumbles-"

        Gunther "Huh?"

        Fen "..."

        "With you safely back in your own bed, the tavern owner prepares to leave. He looks back from the door one more time."

        Gunther "-Sigh-"

        Gunther "Everything about you reminds me of him..."
        
        Gunther "I won't ever let that happen again."

        stop music fadeout 3.0
        "He closes the door quietly as you lay there falling asleep in your bed."

        scene bg black
        with s_dissolve

        pause

        call bondlvup0102 from _call_bondlvup0102

        jump day_start

label gunther_unlockcooking:

    scene bg kitchen
    with s_dissolve

    show fen normal at left1
    show bg kitchen_blur
    with dissolve
    Fen "Gunther."

    show gunther stern at right1
    with dissolve
    Gunther "Yes?"

    Fen "I've been wanting to ask you about the tavern's menu."

    Gunther normal "Oh, what about it?"

    Fen "I've got some ideas to expand our selections."

    Gunther smile "Really? The food has really started drawing more people over. That sounds like a grand idea."

    Fen smile "Great! I'll need to get some more ingredients in the kitchen, a place to test new recipes, and someone to help test out new recipes."

    #Gunther grinning
    Gunther grin "I'd be more than happy to assist you with tasting."

    Fen normal "Thanks, I'll need to spend more time in the kitchen."

    Gunther normal "That's fine, just don't burn yourself out."

    Fen "I can handle it, something about it feels so familiar."
    
    Fen "Even though my mind may not remember, it seems my muscles do."

    Gunther "If it can help your memory, I'm all for it."
    
    Gunther stern "Just be sure not to waste too many ingredients, we don't have a large starting budget."

    Fen smile "Understood."

    Fen normal "Let's start with something easy and tasty."

    Gunther normal "Yeah?"

    stop music fadeout 2.0
    show fen lick at shock
    Fen "Toast plate!"

    jump cooking_toast



label niall_intro:

    stop music fadeout 3.0
    scene bg tavern4
    with s_dissolve
    "After finishing up with cleaning a table for the next group of patrons, your eyes casually wander over towards a figure seated alone across the taproom."

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
    show bg tavern4_blur at truecenter:
        zoom 1.5
    show niall normal at center1, flip:
        zoom 1.5
        ypos 2000
    show ratio1
    with dissolve
    "He doesn't look anything like the burly, well-armed men and women you normally see coming in and out of the tavern."

    "Even though he's not doing anything that looks suspicious, you can't help but wonder how old he's gotta be to be visiting a place like this unattended."

    "He seems happily distracted, looking down at a small object he's turning over in his paw with a glint in his eye."

    hide ratio1
    show bg tavern4_blur:
        zoom 1
    show fen normal at left1
    show niall normal at right1:
        zoom 1
    with dissolve
    Fen "Hello there, sir. Welcome to the Flaming Flagon."

    #Niall jumps
    show niall shock at shock, flip
    "???" "O-Oh! Hello there!"

    "He quickly stows the object away, out of your sight."

    show niall normal at flipback
    "???" "Thank you so much for the warm welcome."

    "???" "I just got into Felda yesterday, and I hear that the local watering holes around here've got some great service."

    show niall smile at shock
    "???" "So, I just couldn't wait to try a place like this out!"

    Fen smile"Ah, so it's your first time in town, huh? Well, I hope you enjoy your stay."

    Fen normal "And just let me know whenever you're ready to order, okay?"

    Fen stern "{i}Hmm...I guess he's not acting like he's not supposed to be here... {/i}"

    show niall normal
    "???" "Actually, I'm ready to order now, if that's alright?"

    Fen smile "Hm? Oh, sure! What'll it be?"

    show niall stern
    "???" "Um...do you have anything virgin around here? And preferably sweet?"

    Fen stern "Virgin?"

    show niall sweat2
    "???" "Yeah. You see, I can't handle alcohol very well. A-haha..."

    Fen "Oh. Well, to be honest, I don't think I've had anyone ask that before."

    Fen sweat "And, uh... something gives me the strong impression that this isn't really a 'virgin' type of place."

    Fen normal "But, sure! I'd be happy to go and ask about something made special for you, if you'd like."

    hide fen
    hide niall
    show bg tavern4
    with dissolve
    "The young jackal nods appreciatively, and you step away behind the bar to ask Gunther if he knows how to make any non-alcoholic drinks."

    show ratio1
    show food drink2 at truecenter:
        ypos 500
    show bg tavern4_blur at truecenter:
        zoom 1.5
    with dissolve
    "A few minutes later, you come back holding a mug that's filled with a mixture of warmed milk, honey, lemon juice, and just a hint of ginger."

    hide food
    hide ratio1
    show fen normal at left1
    show niall normal at right1
    show bg tavern4_blur:
        zoom 1
    with dissolve
    Fen "Here you go! The boss says he calls this one 'The Creamy Dream.'"

    show niall smile
    "???" "Woah! That looks {b}so{/b} good."

    show niall lick
    play sound "audio/drink.ogg" volume 3.0
    "He throws it back eagerly in front of you, licking the tip of his wet nose after getting some of it splashed across his muzzle with each swig."

    play sound "audio/drink.ogg" volume 3.0
    "???" "{b}Uuurp!{/b} Yeah, I'm definitely coming back for more of this."

    Niall normal "My name's Niall, by the way. And, someday, I will be one of the greatest adventurers this land's ever seen."

    Fen "Oh, so you {b}are{/b} an adventurer, then."

    Niall "Well, duh. That's only the big reason why everyone's coming to this town in droves, you know."

    show niall smile at shock
    Niall "Besides, adventuring is just the life!"

    Niall smile "Uncovering long-lost treasures, fighting monsters, becoming instantly famous enough to have every guy either want to be you, or just plain want you..."

    Fen stern "Wow, I, uh...don't think I've ever thought of it quite like that."

    Niall normal "You should totally give it a try sometime; see how well it suits you."

    Niall "Oh! And hey, what was your name again?"

    Fen normal "It's [name]."

    Niall wink "[name]. Okay, got it. I'll be sure to keep an eye out for you on the Adventure Guild's renown board, just in case you ever happen to rise up in the ranks."

    Niall "You never know..."

    Fen stern "Hm? Adventure Guild?"

    Niall normal "Oh, you never heard of it? The branch in Felda has been around for quite a while now, I think."

    Niall smile "I joined the guild, myself, late last year. And ever since then, each day I set out on the road's been chock full of new wonders."

    $ bondexp04 += 1
    call bondexpup04 from _call_bondexpup04

    Niall "It's like, there's no telling what might be waiting for me just over the next hill, you know?"

    hide fen
    hide niall
    show bg tavern4
    with dissolve
    "You spend a short while more making idle talk like this with the young patron before going back to the other tables."

    "After you finish serving him the rest of his order, you realise that some of his excitement and good cheer must have been infectious."

    "A subtle, yet happy mood settles into you throughout the rest of your shift."

    "In fact, it kind of makes you want to try challenging yourself to see if you can serve the next dozen customers in half time!"

    stop music fadeout 3.0
    "And you succeed. Although, needless to say, Gunther isn't all that impressed that it took you messing up almost half the orders to do it..."

    $ niall_bond_ui = True
    call bondlvup0400 from _call_bondlvup0400

    $ show_workday_option('niall_work_option')
    $ hide_workday_option('niall_meet_option')

    $ ap -= 1

    jump work

label niall_serve_01:
    "You give Niall the food and drink he asked for."

    "The young adventurer never fails to ask you if there's anything special or different about it every time."

    "It makes you happy to see that no matter what you tell him, he always looks so satisfied with his meal once he starts digging in."

    $ bondexp04 += 1
    call bondexpup04 from _call_bondexpup04_1

    $ ap -= 1

    jump work

label niall_talk_01:
    stop music fadeout 3.0

    scene bg tavern4_blur
    show niall normal at center1
    with dissolve

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0

    "Niall instantly perks up and smiles at you with his eyes when you approach his table."

    menu:
        "He looks ready to talk with you about whatever you might like."

        "Check to see how Niall's doing" if bond04 == 2:
            jump about_Niall_check_in

        "Have you been inside any dungeons?":
            jump about_niall_dungeons

        "Do you really think I'd make a good adventurer?":
            jump about_fen_adventurer

        "Where do you come from?":
            jump about_niall_home

        "Are those spikes in your body!?":
            jump about_spikes

    label about_Niall_check_in:
        Niall smile "Hey, [name]! Can I have another fizzy pear juice, when you get the chance?"

        Fen smile "The pear soda? Sure, I'll get right on it!"

        Fen "It's great seeing you back to your old self around here again, by the way."

        show niall at shock
        Niall "Hehe! Yeah, and I guess I've got you to thank for it, don't I?"

        Niall normal "I'll be honest, I don't know how I would've kept going on without all these delicious snacks, if I decided to stay away."

        Fen "Right? And there'll be plenty more kinds to come soon, too. So, I hope your stomach's ready."

        Niall smile "Oh, yes~! That's what I'm talking about!"

        Niall normal "And you could look forward to great things in the future with me, too."

        Niall wink "I've already been putting in a heck of a lot more work toward my physical training, if you hadn't noticed."

        hide niall
        show bg tavern4 at truecenter:
            zoom 1
        show ratio1
        with dissolve
        "He tosses you a wink and flexes an arm up for you."

        "It definitely looks more defined than you would've expected, now that he's showing it off."

        show bg tavern4_blur:
            zoom 1
        hide ratio1
        show niall wink at center1
        with dissolve
        Niall wink "I'm gonna need a physic worthy of a real hero, if I'm gonna be able to actually do all the cool things I want to impress you with."

        Fen "Nice!"

        #If you chose to head pat Niall.
        if niall_bond_02_hug == False:
            Niall normal "Yeah, I can't have you needing to cheer me up like I'm some little kid every time I stumble and fall."

            Niall stern "The road upward's full of all kinds of unexpected twists and lows; it's that way no matter what it is you're trying to do."

            Niall normal "And for that, I need to be ready to face mine, whatever they are, and learn how to be confident enough to pick myself up again."

            Niall smile "That's the conclusion I came to after giving what happened before a whole lot of thought!"

            Fen "That's a pretty good mindset you got there, actually. Colour me impressed."

            Fen "Well, just know that I'm always open to hear whatever you might need me to, if you're ever feeling unsure about something again."

            $ bondexp04 += 1
            call bondexpup04 from _call_bondexpup04_8
            Niall normal "Thanks, [name]. You're a really awesome guy."

            show niall smile at shock
            Niall smile "I'm so grateful you're willing to be my inspiration. I swear I won't let you down!"

            $ ap -= 1

            jump work

        #If you chose to hug Niall.
        else:
            Niall stern "Hey, [name]..."

            Niall blush "Um, I was wondering if, before..."

            Fen "Yes?"

            Niall "Err...That hug from before, I wanted to ask: What exactly was it about?"

            Fen "About?"

            Niall "You know, like, uh...what did you mean by it, and all...?"

            menu:
                Fen "Oh!"

                "It was just something to cheer up a friend.":
                    jump about_Niall_hug_friends

                "I think you might really be my type!":
                    jump about_Niall_hug_type

                "Well, I'm not sure myself, honestly...":
                    jump about_Niall_hug_unsure

        label about_Niall_hug_friends:
            Niall stern "Oh..."

            Fen "What were you thinking it was about?"

            Niall sweat "Haha-ha! Who, me? Well...Of course, that's what I was thinking it was. Totally."

            show niall at shock
            Niall "I just wanted to ask you about it to make sure, though. You get it, yeah?"

            Fen "Oh. Yeah, definitely."

            Niall normal "Cool."

            Niall "But anyway, I don't plan on making you need to cheer me up like I'm some little kid like back there every time I stumble and fall."

            Niall stern "The road upward's full of all kinds of unexpected twists and lows; it's that way no matter what it is you're trying to do."

            Niall normal "And for that, I need to be ready to face mine, whatever they are, and learn how to be confident enough to pick myself up again."

            Niall smile "That's the conclusion I came to after giving what happened before a whole lot of thought!"

            Fen "That's a pretty good mindset you got there, actually. Colour me impressed."

            Fen "Well, just know that I'm always open to hear whatever you might need me to, if you're ever feeling unsure about something again."

            $ bondexp04 += 1
            call bondexpup04 from _call_bondexpup04_9
            Niall normal "Thanks, [name]. You're a really awesome guy."

            show niall smile at shock
            Niall "I'm so grateful you're willing to be my inspiration. I swear I won't let you down!"

            $ ap -= 1

            jump work

        label about_Niall_hug_type:
            #Niall Bond down.
            $ bondexp04 -= 1
            call bondexpdown04 from _call_bondexpdown04_1
            Niall shock "O-Oh...! Uh..."

            Niall stresse "Damn...I was afraid it might've been like that. I'm so sorry."

            Fen "Sorry? What for? You're a great guy!"
            
            Fen "Always so bright and charming, it's like I can't get enough."

            Fen "It even had me wondering, if..."
            
            Fen "Heh, We might, maybe end up something more than friends someday...?"

            Niall "Oh, no. Please, [name], please, just...don't for me."

            "He seems a little put off by your confession."

            "No, more than a little, actually. It's kind of hard to imagine why."

            "Was what you said really that bad?"

            Fen "Oh! Oh, no! Niall, I take it all back! I'm so sorry!"

            Niall "L-Look, it's not you who's at fault, I promise. But..."

            Niall "Let's please not go anywhere near there."
            
            Niall "I value us as friends, truly, and I'd want it to stay just like that, if it could."

            Fen "Yeah, yeah! Of course, anything you want. T-That was just a poor mistake of mine for not reading things correctly."

            Niall stern "Good. Thank you."

            Fen "({i} Phew... {/i})"

            hide niall
            show bg tavern4
            with dissolve
            "Oh, man. You feel like what you said just then could've really jeopardised your relationship if you weren't more careful."

            "With that out of the way, you think it's probably best if you kept it casual with Niall for the rest of the day."

            "Maybe giving the awkwardness a while to clear will put things more at ease between the two of you for next time."

            $ ap -= 1

            jump work

        label about_Niall_hug_unsure:
            #Niall Bond up.
            Niall stern "Don't know, huh?"

            Fen "Yeah, it's just...I don't think I could really tell you why I did it. Spur of the moment, maybe?"

            Fen blush "All I know is that it's what felt right for me to do at the time to show you you're not alone, you know?"

            Fen "And...I'm just really happy it worked, I guess. Heh-heh!"

            Niall blush "O-Oh!"

            Niall "Well, yeah, I guess I'm happy it worked, too..."

            Niall "And don't worry about not knowing the reason why either; it's totally fine."

            Niall "In fact, I think I may have read something once that said, 'Acts of the body shine, where thoughtful intentions fall to haze.'"

            Niall "So, maybe you doing that was just your heart being true to itself without the need to consult your mind, or something."

            Fen "Oh, really? Well, that'd be nice to figure, huh?"

            Niall smile "Instincts like those of a hero, yessir! That's what I'm gonna need to work on, myself, next."

            Niall normal "Speaking of which, my plan is to make it so you don't need to cheer me up every time I stumble and fall like you did back there."

            Niall wink "Not that I didn't appreciate the save, though."

            Niall stern "It's just that the road upward's full of all kinds of unexpected twists and lows; it's that way no matter what it is you might be trying to do."

            Niall normal "And for that, I need to be ready to face mine, whatever they are, and learn how to be confident enough to pick myself up again."

            Niall smile "That's the conclusion I came to after giving what happened before a whole lot of thought!"

            Fen "That's a pretty good mindset you got there, actually. Colour me impressed."

            Fen "Well, just know that I'm always open to hear whatever you might need me to, if you're ever feeling unsure about something again."

            $ bondexp04 += 2
            call bondexpup04 from _call_bondexpup04_10
            Niall normal "Thanks, [name]. You're a really awesome guy."

            show niall smile at shock
            Niall smile "I'm so grateful you're willing to be my inspiration. I swear I won't let you down!"

            $ ap -= 1

            jump work


    label about_niall_dungeons:
        Niall stern "Uh...well, no. I haven't really gotten the chance to go into any myself yet."

        Fen stern "But I thought you said you've been in the Adventure Guild for a while now, right?"

        Niall sweat"Y-Yeah. But...Uh, well..."

        Niall stern "They kept me busy doing other important things that needed my attention."
        
        Niall normal "Yeah, that's it. And I haven't been able to get around to exploring till now."

        Fen "Oh, really? Other important things like what, I wonder?"

        Niall "You know. Like...securing high quality goods vital to the guild's operation on a time-sensitive basis."

        Niall "Or spending weeks on end pouring over long-forgotten records, exchanges each worth a fortune in gold which took place throughout the four corners of the earth."

        show niall smile at shock
        Niall smile "Only by piecing together the details into a clear narrative could the truth of these secretive dealings become known! And I was the one to do it."

        Niall smile "So, yeah. Important stuff like that, obviously."

        "It takes you a moment to think about it, but easily enough, what he's describing eventually twigs for you."

        Fen sweat "Umm, 'obviously', huh? Are you sure about that?"

        Fen "Because the things you just described there sure sounded a lot like doing fetch quests and archival work to me..."

        show niall sweat2
        "Those words seem to instantly make his boastful act come crumbling down like a dropped biscuit."

        Niall angry2 "Rrrff...Okay, fine. I guess I haven't gotten to do much all that great at the guild just yet."

        Niall wink "But hey, I mean, every legend-past or future-comes from humble beginnings, amirite?"

        Niall smile "Even the all-powerful heroes and sorcerers who protect these lands now have had to clean out messenger hawk cages at some point in their careers, yeah?"

        Fen "I mean, that can be a good way to look at it, I guess."

        Fen sweat "It's pretty surprising to hear they've been making you be the one to clean the cages, though..."

        Niall sweat2 "A-haha...Maybe I should just be glad that the bards choose to leave such chapters of a hero's life out of their epic poems."

        $ bondexp04 += 1
        call bondexpup04 from _call_bondexpup04_2

        stop music fadeout 3.0

        Niall sweat "More often than not, anyway..."

        $ ap -= 1

        jump work

    label about_fen_adventurer:

        show niall smile at shock
        Niall "Yeah! Absolutely."

        Fen smile2 "Heh. Let me guess, it's the muscles that make you think that, isn't it?"

        Niall "Totally!"

        Niall wink "But it's not just that, though. You've also got this aura about you that just {b} screams {/b} wholesome curiosity and a passion for new kinds of thrills."

        Niall normal "Er...not that I mean to go all palm-reader on you, or anything, by saying that."

        Fen "Oh, It's completely fine. I kind of like hearing other people size me up every once in a while, actually."

        Fen "So long as they're not mean about it, that might actually help me gain some much-needed perspective."

        Niall "Oh, yeah? Is there something you might be looking to learn about yourself?"

        Fen stern2 "I'm...not sure, to be honest. I think there might be something important I forgot about at some point, but..."

        Fen "I just don't know."

        show niall smile at shock
        Niall "Oh! That's perfect, then."

        Niall normal "There's no better reason to go off on wanderlust than chasing things important to you that were lost and forgotten."

        Fen "Hmm...I suppose that makes sense...but still I don't know."

        Fen "I mean, isn't going into dungeons pretty dangerous?"

        Niall smile "Yeah, I guess maybe a little. But honestly, with a body like yours, I wouldn't be too afraid."

        show niall smile at center1:
            zoom 1.5
            ypos 1850
        with dissolve
        "Unthinkingly, his paw gravitates over towards your chest as if he's about to grope you, but then he stops himself suddenly at the last minute."

        show niall stern
        with dissolve
        "Niall seems to have realised the line he was about to cross, and now his paw is just hovering there, a sliver away from you."

        "He stares up at you intently; a silent and humble plea for your permission."

        Niall "..."

        menu:
            "Let him touch you a bit.":
                jump yes_niall_feel
        
            "Shake your head to decline.":
                jump no_niall_feel

        label yes_niall_feel:
            show niall normal
            with dissolve
            "The jackal tries poorly to hide his devious grin as he goes in to cop a feel."

            show niall smile
            with dissolve
            "He seems amazed by the pillowy firmness of your chest underneath your fur."

            "When his fingers trace over your nipple, you accidentally let out a soft moan, and realise it's time to pull away before you let things get too out of hand."

            $ bondexp04 += 1
            call bondexpup04 from _call_bondexpup04_3

            stop music fadeout 3.0
            hide niall
            hide fen
            show bg tavern4
            with dissolve
            "Niall winks at you appreciatively before turning back to his meal, letting the conversation end like that."

            $ ap -= 1

            jump work

        label no_niall_feel:
            "Flustered, you shake your head at him with serious eyes that leave no room to doubt your meaning."

            stop music fadeout 3.0
            hide niall
            hide fen
            show bg tavern4
            with dissolve
            "Looking a little let-down, he just turns back to his meal and lets the conversation drop there."

            "You figure he must be pretty embarrassed about that."

            stop music fadeout 3.0

            $ ap -= 1

            jump work

    label about_niall_home:
        show niall stern
        "The moment you ask him that, his whole body goes stiff as though the room just got much colder."

        Niall stresse "Uhhh...from nowhere. Nowhere at all."

        Fen "Really?"

        Niall sweat2 "Ye-up! Hahaha...!"

        "Something's off, clearly. For some reason, he looks almost...worried to tell you more?"

        menu:
            "Would it be a good idea for you to pursue the subject more?"
            
            "Are you sure there's nothing more you want to say?":
                jump niall_push_topic

            "Okay, I'll believe you, then.":
                jump niall_stop_topic

        label niall_push_topic:

            $ bondexp04 -= 1
            call bondexpdown04 from _call_bondexpdown04

            stop music fadeout 3.0

            show niall stresse
            "You swear you see the jackal's eyes flash briefly in annoyance as he looks at you, trying to come up with the right words to say."

            Niall "There isn't any place that I've ever really called my homeland. I..."

            show niall stern
            "He pauses again to quietly think to himself for a bit."

            Niall "I grew up a pauper you see, and an orphaned one at that. It was really hard learning how to strike out in the world on my own after everything."

            Fen stern "O-Oh, I see. I'm so sorry to hear that."

            Niall "It's not a time I really like thinking back on, so please, let's just leave it at that, [name]."

            Niall "Although, I can tell you without a whiff of doubt that I'm in a much better place right now than I've ever been in my life before. So, that's good."

            Niall "I'm grateful for it almost every day..."

            Fen "I totally understand. It's so great to hear you say that, Niall."

            Fen "I'm sorry if what I said brought up any bad memories. You have my word, I won't pry."

            "He falls silent again and spaces off through a nearby window out into the distance."

            Niall stern "Thanks. I appreciate it."
            # player loses one bond point with Niall

            "It seems like Niall isn't really in the mood to talk about other things right now..."
            $ ap -= 1

            jump work

        label niall_stop_topic:
            $ bondexp04 += 1
            call bondexpup04 from _call_bondexpup04_4
            show niall stern
            with dissolve
            "You can see him visibly start to relax again after hearing you say that."

            Niall stern "Thanks, [name]. I appreciate it."

            stop music fadeout 3.0

            "It seems like Niall isn't really in the mood to talk about other things right now..."

            $ ap -= 1

            jump work

    label about_spikes:
        show niall stern
        with dissolve
        Niall "Huh?"

        "He looks down at himself, as if just noticing them for the first time."

        Niall "Oh, yeah. I guess they are."

        Niall normal "It's perfectly okay, though. I was born with them in me, basically."

        Niall "From what I was told, they're a feature of my breed."
        
        Niall "Apparently, my ancestors were some kind of tribal warriors, highly adept at fighting."

        Niall "They probably lived in some pretty harsh environments with lots of things trying to kill them all the time, so they had to grow a bunch of these to survive."

        hide niall
        show bg tavern4
        with dissolve
        "Niall turns away from you and raises his fists. Without prompting, he begins shadowboxing the air in front of him from his seat."

        "Watching him, you notice that every now and again he's flailing his arms to the side between punches."

        "It's as if he's using the spikes on the back of his paws to parry invisible weapons coming at him from his whole frontal area."

        Niall "I've been told the enamel on the spikes makes them tough enough to pierce through iron if you're strong enough to put down the force."

        "He turns back to you and stops before spreading his arms out wide, like he's getting ready to hug the trunk of some enormous tree."

        show niall normal at center1
        show bg tavern4_blur
        with dissolve
        Niall "And the one on my chest was mostly likely used to impale grappled enemies who were dumb enough to try thrashing about in the warrior's intense grip!"

        Fen grin "Woah...That sounds so cool!"

        Fen "Do you get the chance to try it out in battle often, yourself?"

        Niall smile "Haha! Nah. I wouldn't go that crazy in the middle of a fight just to take down an opponent."

        Niall wink "Although I do prefer to rely on my fists and palms over the more typical heft of a sword to get the job done."

        show niall smile at shock
        Niall "There's just something about your body physically engaging with a force that's trying its hardest to go against you that's exhilarating like nothing else!"

        Fen "So, how would someone end up getting weapons to grow out of their body, though?"

        Niall normal "Who knows? Maybe through some old ritual magic or as a gift from a god?"

        Niall "'The aura in this land was capable of shaping the miracle that is us; it is more than likely capable of doing many things far beyond.'"

        Niall "That's something an old preacher I used to know would always say."

        stop music fadeout 3.0

        $ bondexp04 += 1
        call bondexpup04 from _call_bondexpup04_5

        hide niall
        show bg tavern4
        with dissolve
        Fen stern2 "Huh. Maybe there {b}is{/b} more to this than anyone can ever really know..."

        $ ap -= 1

        jump work

label niall_bond_01:
    scene bg tavern4
    with s_dissolve
    "You feel like you've finally taken notice of something that's been happening for a while whenever you look over at Niall's table."

    stop music fadeout 3.0
    "At least once a day, the young jackal adventurer appears to stare across the room at Gunther while his back is turned behind the bar."

    show bg tavern4_blur at truecenter:
        zoom 1.5
    show niall normal at center1:
        zoom 1.5
        ypos 2000
    show sparkle animation 01:
        zoom 0.5
        xpos 700
        ypos 350
    show ratio1
    with dissolve

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
    "You see Niall just smiles giddily with a twinkle in his eyes, sometimes for minutes at a time, before stopping once Gunther turns back to face the counter."

    "It's... pretty weird behaviour, honestly..."

    hide ratio1
    show fen stern at left1
    show bg tavern4_blur
    hide sparkle
    show niall normal at right1:
        zoom 1
    with dissolve
    Fen stern "Hey, Niall."

    show niall sweat at shock
    Niall sweat "Ah! Oh! Oh, [name]."

    Niall "I wasn't-Uh, I mean...Hey, how's it going?"

    Fen "So, I noticed you've been watching Gunther a lot while he works the bar, and I-"

    show niall shock at shock
    Niall "Gunther!"

    Niall smile "A-ha! I knew I was right about who he was. Yes!"

    Fen "O-Oh. That's...good for you, maybe?"

    Niall normal "Okay, so since you asked, I'll come clean about it: he's another reason why I chose this specific tavern as my first to visit in Felda."

    Niall "Back where I come from, there's barely a soul who's never heard the legend of Gunther the Grappler."

    Niall "He was once an incredibly skilled and talented adventurer, and a companion of the great Sword Hero."

    Niall "As a member of his party, he travelled all throughout the continent, slaying horrific monsters and mapping ancient magical ruins."

    Niall stern "Once, he single-handedly wrestled down a chimaera beast the size of a merchant wagon after it had knocked out the rest of his party in an ambush."

    show niall smile at shock
    Niall smile "That story has to be my favourite adventure of his, hands down."

    Niall "It shows just how much raw potential there is inside a man once he's willing to push beyond his limits for the sake of the people he wants to protect!"

    Fen normal "Wow...Are you sure that's really the same Guther? The one I work for seems way more mild-mannered than that."

    show fen at flip
    with dissolve
    Fen "At least in the time I've had to get to know him he does, anyway."

    hide niall
    hide fen
    show bg tavern1_blur at truecenter:
        zoom 1.5
    show gunther stresse at center1:
        zoom 1.5
        ypos 2150
    show ratio1
    with s_dissolve
    "You glance over at Gunther who looks like he's struggling to decide whether to put out salted peanuts or frosted pecans as snacks for the bar."

    show gunther normal with dissolve
    "Eventually, he gives up on the dilemma and just puts out bowls of both for the customers to enjoy, looking quite satisfied."

    hide gunther
    hide ratio1
    show bg tavern4
    with s_dissolve
    "An idea pops into your head."

    show fen normal at left1
    show niall smile at right1
    show bg tavern4_blur
    with dissolve
    Fen "Hey, would you like me to introduce you to Gunther, by any chance?"

    #show Niall image backing away
    show niall shock at shock
    Niall shock "W-W-What!?"

    Niall "Oh...N-No, I couldn't possibly."

    Niall sweat "I mean, it'd be a dream come true for me to go up and meet him, of course. But, like..."

    Niall "What would I even have to say to a great hero of legend that could possibly be worthy of his time?"

    Fen smile "Ha! Don't overthink it."

    Fen normal "Gunther runs a tavern. He's used to new people coming up to him and just spilling their guts out while he's there."

    Fen sweat "Sometimes, it takes a couple of them to get fully plastered first...in which case they do that literally..."

    Fen normal "But anyway, yeah, you shouldn't worry about it. In fact, something tells me he'll really like you."

    show niall smile at shock
    Niall "You mean it!? Oh, wow. Okay, yeah! In that case, I'll do it!"

    #show Niall image shaking nervously
    Niall stresse "...Just maybe not today, though."

    Niall sweat "As comfortable as he might be with me, I'm just not sure if I'm ready to face him yet."

    Niall "He's been, like, my biggest idol since I was six. I don't think you really get it..."

    Fen "Oh. Okay. Well then, just say the word anytime."

    stop music fadeout 3.0
    Niall normal "Thanks, [name]. I'll definitely let you know when the time's right for me."

    window hide
    hide fen
    hide niall
    show bg tavern4
    with dissolve

    $ ap -= 1

    call bondlvup0401 from _call_bondlvup0401

    jump work

label niall_bond_02pre:

    scene bg fenroom
    with s_dissolve

    play sound "audio/birds.ogg" volume 3.0
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0

    "You wake up to the warm sunlight gently illuminating your face, coaxing you from your sleep."

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
    "{color=#5252ff}???{/color}" "Ouch!"

    "Just as you're slipping on your clothes, a familiar sound catches your attention from the street below."

    scene bg tavernfront
    with s_dissolve
    "Curious, you head outside to investigate."

    show bg tavernfront_blur at truecenter:
        zoom 1.2 
    show ratio1
    with dissolve
    "There, in the early morning light, you spot Niall."

    "He's busy collecting dried leaves and dirt into a large sack, his movements energetic as always."

    menu:
        "Help him.":

            $ niall_bond_02pre_help = True

            "You lean over to help him gather the remaining leaves and dirt."

            "It's a bit of a struggle to get everything back into the sack, and by the time you're done, your hands are covered in dust and grime."
            
            "You'll definitely need to wash up after this."

        "Keep distance.":

            "Not wanting to get your hands dirty, you step back and watch as Niall finishes up the rest on his own."
    
    show bg tavernfront_blur:
        zoom 1
    show fen stern at left1
    hide ratio1
    with dissolve
    Fen "What's going on here?"

    show niall sweat at right1
    with dissolve
    Niall "Phew..."

    if niall_bond_02pre_help == True:
        call bondexpup04 from _call_bondexpup04_11
        $ bondexp04 += 1
        Niall smile "Thank you for the help, [name]!"

    else:
        pass

    Niall normal "I happened to trip and dropped this sack. Sorry it had to happen right in front of your place."

    show niall smile at shock
    Niall "But look, it's all cleaned up now! Not a single stray leaf left!"

    Fen normal "So... what's with the sack?"

    Niall normal "Oh, this? I'm just doing my quest! Helping haul this dirt outside the walls."

    Niall "The guild hands out these kinds of quests sometimes, and I'm happy to take them on."

    Fen "I see, I see. So even cleaning the town can be a quest. Interesting."

    Niall smile "Yep! Like I said before, I gotta start somewhere! Clearing these small quests will help me get access to tougher ones sooner!"

    Niall normal "Plus, keeping the town nice and clean keeps the adventurous spirit alive, don't you think?"

    Fen smile "Yeah, you're right."

    Fen normal "Well, keep up the good spirit. I'll see you tonight, right?"

    Niall normal "Yeah! See you tonight!"

    Niall wink "Niall, legend in the making, won't let you down!"

    stop music fadeout 3.0
    hide fen
    hide niall
    show bg tavernfront
    with dissolve
    "He waves enthusiastically and continues down the street, lugging the full sack behind him."

    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    "You can't help but feel uplifted just watching him go. His upbeat and kind energy is contagious."

    Fen "Now... I should get started on my work too."

    jump day_activity

label niall_bond_02:

    stop music fadeout 3.0
    scene bg tavern4
    with dissolve
    "While passing by his table, Niall goes and tugs on your shirt to grab your attention."

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
    show niall wink at right1
    show bg tavern4_blur
    with dissolve
    Niall wink "Psst! Hey, [name], guess what?"

    Niall normal "I feel like I'm ready. I think today might actually be the time!"

    show fen stern at left1
    with dissolve
    Fen stern "Hm? Time for what?"

    show niall stern at shock
    Niall stern "Oh, come on. Don't tell me you already forgot about what we talked about before."

    Niall "You setting me up on a one-to-one meeting with Gunther."

    show fen normal at shock
    Fen "Oh. Oh, right. That."

    Niall normal "I was finally able to gather up all my thoughts enough to know exactly what it is I wanna say."

    Niall "And if the heat of the moment does make me choke up, I've got a whole buncha questions for him written down."

    show niall smile at center1
    with dissolve
    Niall "See?"

    show niall at right1
    with dissolve
    "Niall slides over to you an open notebook. Both of the pages are absolutely scrawled with blotted ink."

    "The first question alone is enough to make you squint."

    Fen sweat "'How did your chest get so heroically big, and did it help you keep the bad guys distracted?'"

    show niall normal at shock
    Niall "Yeah, I'd really like to know if there's some kind of special advantage in a fight with having a body like his."

    Niall "It's just so... eye-catching in all the right places, you know?"

    Fen blush "Ehh~, I'm not so sure about it. Maybe try to come across as a bit less personal...?"

    show niall smile at shock
    Niall "Sure, thing! But it's still okay for me to meet him today, right?"

    Fen normal "Well, I still have to go ask if he can spare the time, but I don't see why not."

    Fen "Oh, but you'll probably need to hang around until after we close for it, if that's okay."

    show niall grin at shock
    Niall grin "Yeah, you bet!"

    Niall normal "[name], thanks so much! You've gotta be, like, the sweetest guy I know!"

    Fen blush4 "Ehehe! It's my pleasure."

    stop music fadeout 3.0
    hide fen
    hide niall
    show bg tavern4
    with dissolve
    "As you turn to move away, Niall goes back to his drink humming a jaunty tune."

    show bg tavern1 at top:
        zoom 1.5
    with dissolve
    "When you find the right moment for it, you slip behind the bar to talk to Gunther about what the two of you discussed."

    play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0
    show gunther normal at right1
    show bg tavern1_blur
    with dissolve
    Gunther "Whuzzat? You say he's got a whole booklet with questions he wants to ask me?"

    Gunther stresse "I mean, if the boy wants to treat it that much like an interview, he should really make it worth my while..."

    show fen stern at left1
    with dissolve
    Fen "He seems really eager to get the chance to talk to you, though."

    Fen normal "If we can agree to keep it to no more than a handful of questions, would that be alright?"

    Gunther stern "Hmm. Well, if that's how it is, then I guess it should be fine."

    Gunther "Okay, then. If he's gonna stick around till closing, I'll head on over to say hello."

    Fen smile "Great!"

    hide gunther
    hide fen
    show bg tavern2:
        zoom 1
    with dissolve
    "The rest of the shift goes by uneventfully, as you and Guther get ready for closing by locking up the tavern doors."

    "After washing out the last of the mugs, Gunther comes walking out to where Niall has remained sitting patiently for the past five hours."

    stop music fadeout 3.0
    "The young adventurer immediately lets out a gasp full of awe when he sees him coming."

    play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
    show gunther normal at right1
    show bg tavern2_blur
    with dissolve
    Gunther "Hey, there. I was told you wanted to sit down and have a little talk with me about something?"

    show niall blush at left1, flip
    with dissolve
    Niall blush "Yes, you're—Uh...Y-Yes, I...I'm..."

    "Once he realises his words are already failing, Niall quickly goes to reach for his notebook..."

    #things drop sound
    play sound "audio/drop.ogg" volume 3.0
    show niall at shock
    "But then fumbles to grab it; instead, knocking it over onto the floor."

    Niall blush2 "Oh, darn it..."

    Gunther sweat2 "Hey, hey. It's alright. There's no need to get so flushed over me."

    Gunther "I'm just a tavern owner, after all."

    show niall blush at shock
    Niall blush "Huh? B-But sir, that isn't true at all."

    show sparkle animation 01:
        zoom 0.25
        ypos 200
        xpos 570
    show sparkle animation 01 as sparkle01:
        zoom 0.2
        ypos 260
        xpos 420
    show sparkle animation 01 as sparkle02:
        zoom 0.3
        ypos 270
        xpos 600
    Niall star "You're Gunther the Grappler, Unstoppable Tiger of Flame!"

    Niall "The strongest brawler in the world, and one-time, undisputed champion of the royal arena!"

    Niall "You and your party explored the lair of the Bone Dragon and lived, freed countless victims from the curse of the Witching Stone, and found the—"

    Gunther sweat3 "And did all that in another life of mine, yeah."

    Gunther "I'm retired now, though. And I'm trying to put as much of that stuff as far behind me as I can, if I'm gonna be honest."

    show niall shock at shock
    hide sparkle animation 01
    hide sparkle01
    hide sparkle02
    Niall shock "What!?"

    Niall "B-B-But, sir! Why?"

    Gunther "Basically, I got tired. Sometimes stuff just happens, and people end up changing the trajectories of their lives. Sorry."

    Fen "You really used to go adventuring with a whole party, though?"

    show sparkle animation 01:
        zoom 0.25
        ypos 200
        xpos 570
    show sparkle animation 01 as sparkle01:
        zoom 0.2
        ypos 260
        xpos 420
    show sparkle animation 01 as sparkle02:
        zoom 0.3
        ypos 270
        xpos 600
    show niall star2 at shock
    Niall "Oh, not just any party, but that of the legendary heroes of Sword & Shield, themselves!"

    Niall "He of the unbreakable sword, and his brother, the impenetrable shield!"

    Niall "Then behind, there stood the grand wizard of the ivory tower with his staff in hand, calling for the most potent, mind-bending spells."

    Niall "And who can forget the most beautiful and glamorous healer—blessed star of the capital city—the radiant Lady of the Strands!"

    Fen grin "Really? Wow, you make them all sound so epic!"

    Gunther stresse "Oh, boy..."

    Niall "All the children in Felda and the realms beyond grow up learning their stories, holding the virtues behind them dear inside their hearts."

    Niall "A few of them are even inspired enough to go out and try to make new legends of their own, dreaming to do just as they would back in their heyday."

    Fen shock "That amazing!?"

    Fen "I mean, that's a pretty monumental thing, isn't it? I wonder how come I've never heard of that until now."

    #Gunther says in smaller text, to show he's whispering
    Gunther "{size=25}The boy's exaggerating a bit.{/size}"

    show niall stern
    hide sparkle animation 01
    hide sparkle01
    hide sparkle02
    Niall "Sir, I don't know what it is you may think of me, for I am but a no-name stranger in your magnificent presence..."

    show niall stern at shock
    Niall "But there's something I greatly want you to know!"

    hide niall
    hide gunther
    show bg tavern2
    with dissolve
    "You watch as Niall reaches down into his pocket and dramatically pulls something out to show to you and Gunther."

    #Show Orichalcum relic art
    show ratio1
    show orichalcum_relic at truecenter:
        zoom 2
    show bg tavern3_blur
    with dissolve
    "It looks like a small chunk of jagged crystal that sparkles bluish grey in the light."

    scene bg tavern2_blur
    show niall star at left1, flip
    show gunther stern at right1
    with dissolve
    Niall star "With this special Orichalcum relic, I plan on someday taking on a quest that will make me as mythic and brave as you."

    show niall at shock
    Niall "That is my one and only dream. I wanna go down in history!"

    Gunther stern "..."

    Fen grin "Oh, man. That's such a wild dream! But that's so exactly like you, Niall."

    Niall wink "Mhm. I know right. But hey, you gotta be willing to reach for the stars if you want people to start believing that's where you belong, right?"

    Fen "Heh, yeah, I guess."

    Fen normal "How about it, Gunther? You think Niall's showing what it takes to follow in your big footsteps?"

    Gunther stresse4 "..."

    Fen stern "Gunther?"

    Gunther stern "Yeah..."

    Gunther "Yeah, it all sounds really good, pup. I hope your dreams get you however far you want."

    Gunther "It's too bad I can't really help you out with any of it, though."

    Gunther stern2 "We're done here for tonight."

    stop music fadeout 1.0
    show niall shock at shock
    Niall shock "...!"

    Fen shock "What!?"

    Fen "Gunther, come on."

    Fen "I can't tell exactly how much of what he said about you was true, but you shouldn't be so dismissive."

    Gunther stern "Sorry, tavern's closed, and I've got some urgent business I just remembered I need to tend to."

    Gunther "If he wants to come back again when we reopen, he'll have excellent food and drink, served with a smile."

    show gunther stern2 at flip
    with dissolve
    Gunther "Until then..."

    #Gunther turns and moves slowly across the screen to leave

    show niall cry2 at shock
    Niall cry2 "But, sir, why...?"

    Niall "Is it...Is it that you think I won't amount to anything? That I'm wasting your time here, making myself look like an ass?"

    Fen shock "N-Niall!"

    Niall cry2 "Go on, then say it! It's okay. I've heard it all before and worse."

    Niall "It's not like this is going to be the most embarrassing night of my life or anything, not by a long shot!"

    #Zoom on Gunther with ratio
    Gunther "..."

    show gunther stern at flipback
    with dissolve
    Gunther "I'm not doubting that you can become an adventurer, pup. You'll get there just by doing what you're doing from the sounds of it."

    Gunther "Train hard, always keep alert, remember that danger can always be right there when you least expect it."

    Gunther "But that's all the advice on it I can give you. Figuring out the rest of it is something you're gonna have to do on your own."

    Gunther stern2 "I'm sorry... but at the end of the day, all these 'heroes' of yours are just foolish folks doing whatever they can to survive."

    Gunther "Nothing more."

    show niall shock at shock
    Niall shock "...!"

    Niall cry2 "Tch!"
    
    Niall "[name]...I want to leave."
    
    Fen sad "But Niall, you're crying. I can't just—"

    #Says this next part with the text shaking, like he's screaming with a shrill voice
    show niall cry2 at shock
    Niall cry2 "{sc=1.5}{b}{size=50}I said I want to leave!!!{/size}{/b}{sc}"

    stop music fadeout 3.0
    Fen "..."


    scene bg tavern3 at truecenter:
        zoom 1.5
    with dissolve

    play sound "audio/Door Open 2.ogg" volume 1.0
    "You move to unlock the front door for Niall, and not a second after, he goes bolting through."

    "As he sprints across the dark street towards the distance, it looks like he's keeping his head hung down at his feet..."

    scene bg tavern1
    with dissolve
    "And just like that, the tavern falls awkwardly quiet."

    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    show gunther stern2 at right1
    show bg tavern1_blur
    with dissolve
    "You see Gunther lingering with an arm propped against the bar counter, lost in thought."

    show fen stern at left1
    with dissolve
    Fen stern "What was that about? Why did you say all that?"

    Gunther stern "I don't think I said enough, honestly."
    
    Gunther "Should've told him to quit trying to be an adventurer while he was ahead."

    show fen shock at shock
    Fen shock "W-What!?"

    Gunther stern2 "But I couldn't bring myself to crush his poor, little dreams like that."

    Fen stern "Niall waited just for you all this time, though. I think the main reason why he came here in the first place was because of you."

    Fen "I remember you said adventuring isn't without its risks, but..."

    Fen "Niall's a good lad, you could..."

    Gunther stern "Just drop it, pup. It's for the best that stuff like this stays between me and the floorboards."

    Gunther "Just pretend like this whole thing was a dumb, little slip-up that you can forget as soon as you climb into bed."

    Gunther "I still care about you the same, and I'm sure your friend will, too, after he cools down."

    Gunther stern2 "I've seen guys of his type before; they don't give up on the people who help them out so easily..."

    Fen "So, what then? That's it?"

    Gunther stern "Yep. Oh, but don't worry about finishing the rest of closing for tonight. I'll get to it in a minute."

    show gunther at flip
    with dissolve
    Gunther "Just go on over to bed."

    Fen stern "..."

    Gunther stresse4 "...Ugh. Fine, then. Good night."

    show fen at flip
    with dissolve
    Fen "Good night..."

    hide fen with dissolve

    pause

    #Says in small whispering text once Gunther is alone
    stop music fadeout 3.0
    show gunther stern at flipback
    with dissolve
    Gunther "[name]..."

    scene bg tavernback_night
    with s_dissolve
    "But you don't go off to bed, though."

    play sound "audio/Door Close.ogg" volume 1.0
    "Instead, you sneak out the back door and make your way through the streets in the direction where Niall's scent lingers."

    scene bg tavernfront_night
    with dissolve
    "Thankfully, finding him isn't all that hard since he kept to the main thoroughfares the whole time."

    "You hear him crying first before you see him, huddled up against a wall by the lantern light."

    Fen "Niall!"

    "He jolts as soon as he hears you calling and then scrambles to his feet, looking like he might try to run away again." with vpunch

    Fen "Wait, please! I just want to talk with you."

    play music "audio/Winter Morning.ogg" volume 1.0 fadein 3.0
    show niall cry at top:
        zoom 1.5
    show bg tavernfront_night_blur:
        zoom 1.5
    with dissolve
    Niall cry "Talk about what? How bad you feel seeing me get shot down like a dunce in front of my hero?"

    Niall "About how much I wasted your time blathering on and on about dreams that'll never come true?"

    Fen sad "Niall, no. It's not like that."

    Fen "What Guther said back there...I don't know what to think of it, myself, I'll be honest."

    Fen "But he can't have possibly meant it to be as bad as you think."

    Niall "Yeah? And how would you know?"

    Niall "You don't know how much his legacy can mean to some people, but I do, and so does he."

    Niall "There's only a few like him out there: heroes who go and conquer the dungeons and then get to retire with fame and glory."

    Niall "Many ends up killed and eaten by monsters at some point, or use their wealth and power to become tyrants, or get corrupted by fame..."

    Niall cry2 "And he knew... Just from one look at me, he knew I'd never ever get to be as great as him."
    
    Fen "Niall—"

    Niall cry2 "Almost no one does! It just makes sense!" with vpunch

    Niall "It...It just makes stupid sense... An–And I couldn't see it!"

    Niall cry "I couldn't see it..."

    Fen "..."

    Fen "Niall, if being an adventurer just isn't the right calling for you. It's also ok."

    Fen "You can find lots of other things to put your passion towards."

    Niall cry2 "But whose call is it, then!?"

    Niall "What is it even supposed to take to be the right kind of person for going out and doing heroic works in the world?" with vpunch
    
    Fen shock "U-Uh..."

    Niall "Whose job is it to decide that? What are they doing with it, anyway?"

    Niall cry "Every day, I doubt myself—questioning the things I do and the choices I make..."

    Niall "I even find myself getting jealous of others..."

    Fen "That's..."

    Fen "So, that's how you really feel about it, huh?"

    hide niall
    show bg tavernfront_night:
        zoom 1
    with dissolve
    "He turns away to wipe some of the tears from his eyes and gives you a solemn nod, looking almost ashamed of it."

    show niall stresse at right1
    show bg tavernfront_night_blur
    with dissolve
    Niall "I know, it's not a very positive thing for me to feel, is it?"

    Niall sweat "So totally different from how I always try to be, because I know that people might hate me if they knew I actually thought like that."

    Niall stresse "You... You can hate me too now for it, if you want."

    show fen stern at left1
    with dissolve
    Fen stern "Niall."

    Niall "I don't care..."

    show fen angry at shock
    Fen angry "Niall, stop! I don't hate you!"

    Fen stern "I never will for something like this."
    
    Fen "And even if Gunther doesn't believe in you—thinks you'll never get to be an adventurer—that shouldn't matter, because..."
    
    Fen normal "Because I believe in you."

    show niall shock at shock
    Niall shock "!!!"

    Fen "All those kindness and dreams of yours couldn't have just been for nothing; not when you haven't even really tried."

    Fen "Who cares if the path looks dangerous? And who cares if it's against the odds?"

    show fen at shock
    Fen "No one else I've seen has got anywhere near the spirit for this as you do!"

    Fen "That alone is something that's gonna keep me cheering you on from the sidelines right till the end!"

    Fen smile "You could say that hearing all your stories ended up inspiring me in just that kind of way."

    Fen normal "And it wouldn't be very heroic of you to just turn your back on an admirer who's still waiting to hear all about your first great deed, now would it?"

    show niall normal with dissolve
    Niall "[name]..."

    "You see that he can't help but crack a brief smile after hearing you say that."

    Niall "[name], I..."

    show niall stern with dissolve
    Niall "But...But how can I possibly know you really mean that? Isn't it just mostly saying words to be nice? I mean..."

    Niall "How do I know that I can trust you...?"

    menu:
        "How does he know that he can trust you?"

        "Give him an encouraging pat on the head":
            jump about_Niall_pat
        "Bring him in for a tender hug":
            $ niall_bond_02_hug = True
            jump about_Niall_hug

    label about_Niall_pat:
        hide fen
        show niall at top:
            zoom 1.7
        show bg:
            zoom 1.7
        with dissolve
        "You stoop down and tussle the fur between his drooping ears."

        "They seem to perk back up as soon as your touch trails down across his scruff, and by the time you ease back, he's finished crying."

        Fen "Does that feel better at all?"

        Niall "({i} sniff {/i})...Uh-huh."

        "He stares up at you for a long minute afterward. You make sure that he can see the pride and relief in your eyes."

        Niall "You...really believe in me."

        Fen "I do, Niall. Don't ask me quite how, but I know you're destined to do great things some day."

        Fen "Maybe even great enough to give those heroes of legend a run for their money! Who knows?"

        show niall normal with dissolve
        Niall normal "Hehe..."

        stop music fadeout 3.0
        show niall at right1:
            zoom 1
        show fen normal at left1
        show bg tavernfront_night_blur
        with dissolve
        "You're so relieved to finally see the smile return to his face."

        play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
        Niall smile "Hahaha! Gee, you really think?"

        Niall normal "Well, damn. Maybe, eventually, I'll make it to the point where even Guther can't ignore me."

        show niall smile at shock
        Niall smile "Or maybe, next time, I'll be the one who gets to shoot {i} him {/i} down for an interview. How's about that? Haha!"

        Fen smile "Ahaha!"

        Niall normal "Thanks, [name]. It was stupid of me to think that I was all alone just because of this."

        Niall stern "And... I get it, Gunther was just worried about me. He know I'm still inexperienced."

        Niall "I shouldn't have reacted that way."

        Fen normal "Yeah, he can be a bit harsh with his words sometimes. Today seems to be one of those days."

        Niall wink "I should've known—it's in all the stories."

        Fen "Does that mean I'll get to see you at the tavern again, bright and early next time?"

        Niall smile "Mhm, for sure! You can count on it."

        Niall normal "After all, if you're gonna be so excited to hear tales of my valiant exploits once they're made..."

        Niall "I gotta make sure you get to hear it from the one and only trusty source there is!"

        show fen smile at shock
        Fen "Awesome! You know I can't wait!"

        show niall smile at shock
        Niall "Neither can I! And I'll make sure it's a good one just for you."

        Niall "My first and most coolest fan: '[name] the Dream-saver!' Heh-heh!"

        hide fen
        hide niall
        show bg tavernfront_night
        with s_dissolve
        "The two of you talk a little more, mostly so you can make sure Niall's okay going home tonight by himself."
        
        stop music fadeout 3.0
        "Once it looks like everything's been sorted out with this situation the best it could be, the two of you say your goodbyes."

        #Bond Level Up Music!
        call bondlvup0402 from _call_bondlvup0402

        scene bg tavernback_night
        with s_dissolve
        "It's been a long, difficult day that has left you feeling drained both physically and emotionally."

        "But despite that, it's strange and a little touching to think you might have come away from it all as a brand new hero in someone's eyes."

        $ work_day_count += 1
        $ day_count += 1
        $ ap += max_ap

        jump day_end
        
    label about_Niall_hug:
        hide fen
        show niall at top:
            zoom 1.7
        show bg:
            zoom 1.7
        with dissolve
        "You crouch down and pull him in for a big hug."

        "You're careful to do so in a way that keeps you from getting struck by that spike in his chest, but you think it's effective all the same."

        Niall "H-Huh?"

        "Suddenly, he starts trembling in your arms."

        show niall blush with dissolve
        Niall blush "Ahh~!"

        Fen shock "Ah! Are you okay?"

        Niall "Yes. I-It's just..."

        Niall "I don't think anyone's ever held me like this before...I'm sorry."

        Fen "Oh. Heh. I guess I may have gone a little too far, eh?"

        show niall at right1:
            zoom 1
        show fen normal at left1
        show bg tavernfront_night_blur
        with dissolve
        "You end the hug and take a step back, just in case he was getting uncomfortable."

        Fen "But, does that feel better at all?"
        
        Niall "({i} sniff {/i})...Uh-huh."

        "He stares up at you for a long minute afterward. You make sure that he can see the pride and relief in your eyes."

        Niall "You...really believe in me."

        Niall "Does this mean that you..."

        Fen "Hm?"

        Niall normal "N-No, nothing. It was just a stupid idea."

        Niall "But, uh...thank you still, for saying you believe in me."

        Fen smile "Of course, Niall." 

        Fen normal "Don't ask me quite how, but I know you're destined to do great things some day."

        Fen smile2 "Maybe even great enough to give those heroes of legend a run for their money! Who knows?"

        Niall "Hehe..."

        stop music fadeout 3.0
        show fen normal
        "You're so relieved to finally see the smile return to his face."

        play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
        Niall smile "Hahaha! Gee, you really think?"

        Niall normal "Well, damn. Maybe, eventually, I'll make it to the point where even Guther can't ignore me."

        show niall smile at shock
        Niall "Or maybe, next time, I'll be the one who gets to shoot {i} him {/i} down for an interview. How's about that? Haha!"

        Fen smile "Ahaha!"

        Niall normal "Thanks, [name]. It was stupid of me to think that I was all alone just because of this."

        Niall stern "And... I get it now, Gunther was just worried about me. He know I'm still inexperienced."

        Niall "I shouldn't have reacted that way."

        Fen normal "Yeah, he can be a bit harsh with his words sometimes. Today seems to be one of those days."

        Niall wink "I should've known—it's in all the stories."

        Fen "Does that mean I'll get to see you at the tavern again, bright and early next time?"

        Niall smile "Mhm, for sure! You can count on it."

        Niall normal "After all, if you're gonna be so excited to hear tales of my valiant exploits once they're made..."

        Niall "I gotta make sure you get to hear it from the one and only trusty source there is!"

        show fen smile at shock
        Fen "Awesome! You know I can't wait!"

        show niall smile at shock
        Niall "Neither can I! And I'll make sure it's a good one just for you."

        Niall "My first and most coolest fan: '[name] the Dream-saver!' Heh-heh! ❤"

        hide fen
        hide niall
        show bg tavernfront_night
        with s_dissolve
        "The two of you talk a little more, mostly so you can make sure Niall's okay going home tonight by himself."

        stop music fadeout 3.0
        "Once it looks like everything's been sorted out with this situation the best it could be, the two of you say your goodbyes."

        #Bond Level Up Music! 
        call bondlvup0402 from _call_bondlvup0402_1

        scene bg tavernback_night
        with s_dissolve
        "It's been a long, difficult day that has left you feeling drained both physically and emotionally."

        "But despite that, it's strange and a little touching to think you might have come away from it all as a brand new hero in someone's eyes."

        $ work_day_count += 1
        $ day_count += 1
        $ ap += max_ap

        jump day_end

label terrance_intro:

    stop music fadeout 3.0
    scene bg tavern4_blur
    with s_dissolve
    "Taking a nervous breath, you walk up to the massive draft horse, doing your best to not stare at him."

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0

    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Fen "Good afternoon Terrance, how's the day going?"

    "You hope that by keeping things simple and professional, you'll avoid embarrassing yourself."

    show terrance normal at right1
    with dissolve
    Terrance "Things are OK. Tired, pretty hungry and damn, I need a drink. Can ye fetch me a drink there lad?"

    Fen "Oh, of course, be right back."

    show bg tavern1
    hide fen
    hide terrance
    with dissolve
    "Rushing to the bar, you grab one of the larger tankards and glance back towards Terrance."
    
    show fen stern at center1, flip
    show bg tavern1_blur
    with dissolve
    "Realising you don't know exactly which drink he wanted, you pause."

    Fen "Dammit... didn't ask him what he wanted."

    show fen blush at flipback
    with dissolve
    "Frozen with indecision, you stand there for a few moments before looking back toward the horse who is giving you a questioning look."
    
    "Blushing, you gesture towards the various casks of liquids and are grateful to see Terrance point out one in particular."

    show fen at shock
    Fen "Right there!"

    hide fen
    show bg tavern4
    with dissolve
    "Quickly filling the tankard, you quickly rush back to the table and sheepishly place it down in front of the horse, who quickly drains it." 

    show terrance smile at right1
    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Terrance "Ah, that hit the spot. Thank ye kindly lad."

    show terrance normal
    "The horse looks you up and down and smiles."

    Terrance normal "Though, seems me tankard's empty, I'll be wanting another with me food."

    "He again looks you up and down and you can't help but think he is sizing you up in some way you can't understand."

    Terrance "Speaking of dinner, what's on the menu today?"

    show fen smile
    "You give the horse a proud smile."

    Fen "It's my homemade stew. It's fresh and we have some bread baked this morning to go with it."

    "Terrance nods and takes a deep breath."

    Terrance "I've heard about how ye improved the quality of the meals here. Gunther runs a good tavern, but let's be honest... he's no cook."
    
    Terrance "But bring me a bowl of that stew, it smells delicious and I'm definitely in the mood for a hearty meal after this workday."

    hide fen
    hide terrance
    show bg kitchen_night1
    with dissolve
    "You grab the empty tankard, turn and head towards the kitchen to fetch the order."
    
    "Heading to the cauldron, you lift the lid and note that it's still about half way and smells just as good, if not better than when the dinner rush started."

    "Getting one of the larger bowls you ladle a giant portion into the bowl and pause to slice off a thick slice of bread."
    
    show bg tavern1
    with dissolve
    "Placing it all on a tray, you pause at the bar to refill Terrance's tankard and quickly walk back to the waiting horse."

    show bg tavern4_blur
    show fen normal at left1
    show terrance normal at right1
    with dissolve
    Fen "Here you go. Hope you like it."

    show fen stern
    play sound "audio/drink.ogg" volume 3.0
    "You watch anxiously as Terrance raises the bowl to his mouth and takes a large gulp of the stew."
    
    "His eyes light up and he gives you a broad smile."

    Terrance smile "This is delicious!"

    $ bondexp02 += 1
    call bondexpup02 from _call_bondexpup02

    show fen normal
    "Terrance takes another sip from the bowl before grabbing the bread and tearing off a chunk."
    
    stop music fadeout 3.0

    hide fen 
    hide terrance
    show bg tavern4
    with dissolve
    "As he chews, you grin and begin to step away to tend to any other patrons."

    $ terrance_bond_ui = True
    call bondlvup0200 from _call_bondlvup0200

    $ show_workday_option('terrance_work_option')
    $ hide_workday_option('terrance_meet_option')

    $ ap -= 1

    jump work

label terrance_serve_01:
    "You bring Terrance his order of food and drink."

    "Hauling the heavy tray loaded up with dishes over to him involves some arm strength on your part."

    "It shouldn't really surprise you that keeping up a body as big and hard-working as his takes an extra meal or five above the norm."

    $ bondexp02 += 1
    call bondexpup02 from _call_bondexpup02_1

    "The horse raises his mug up to you with a wink as a show of thanks."

    $ ap -= 1

    jump work

label terrance_talk_01:
    stop music fadeout 3.0

    scene bg tavern4_blur
    show terrance normal at center1
    with s_dissolve

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    Terrance "Evening lad. Food's as good as ever. That ol tiger dunnae knows what he got going for him now."

    menu:
        "About you and Gunther...":
            jump about_terrance_gunther
                        
        "About your family...":
            jump about_terrance_family

        "About your work...":
            jump about_terrance_work

        #"About the future..." if terrance_worktalk_first == False:
            #jump about_terrance_future

    label about_terrance_gunther:
        Fen "Hey Terrance, how do you know Gunther anyways?"
        
        Fen "Like I know the basics but wondering if there was anything more."

        "The horse looks up from his food and smiles, glancing over to the tiger as he serves drinks."

        Terrance "We go a long ways back. We met in town before he opened the Flagon."
        
        Terrance "Honestly, not much to say really. He needed some help and Murry set it up so I could help him."

        "The horse snorts in what you think is exasperation and continues."

        Terrance stern "Stubborn old fool is a hard one to work with though. Always has to be right and in control. Bah."
        
        Terrance smile "But things have a funny way of working out and well, me and old furrball..."

        "The horse smiles again and gives the tiger another sideways glance."

        Terrance "Eh, I'll tell ya about that later lad."

        $ bondexp02 += 1
        call bondexpup02 from _call_bondexpup02_2
        $ ap -= 1

        jump work

    label about_terrance_family:
        Fen "Hey Terrance, ummm... can I ask you a question?"

        show terrance stern
        with dissolve
        "Terrance gives you a bit of a surprised look."

        Terrance normal "Of course lad? What do ye be wanting to know?"

        Fen "Just wondering about your family. Seems everyone I meet here are on their own."

        "You see the horse's eyes narrow slightly and you gulp, hoping you haven't offended him. He snorts before talking."

        Terrance "Not much to say. Me folks are both well, old though."
        
        Terrance "Names are Eomer and Eunice. They live about a week away from here, but with how they are now, they cannae make the trip."

        Terrance "I try to visit them once or twice a year. I do have a younger sister, Bernice. She lives with them and looks out for them with her husband, Jerrod."

        "The horse sighs and looks a bit downcast."

        Terrance "I love me family lad. More than anything. Most of me wages go to help them."

        Fen "Oh..."
        
        Terrance "Bernice cannae work and Jerrod dunnae make a lot. I have a simple life so I can send most of it to them."

        Terrance smile "All I can do, but I'm happy to do it."

        "He gives you a sad smile and returns to his dinner."
        
        "You can't help but feel for the gentle giant sitting in front of you and his story makes you wonder about your own family."

        "Getting up to get back to work, you thank Terrance and leave him to his thoughts, though you notice the smile never fades from his face."

        $ bondexp02 += 1
        call bondexpup02 from _call_bondexpup02_3
        $ ap -= 1

        jump work

    label about_terrance_work:
        Fen "So, do you only haul carts around the area?"

        Terrance "Nae lad, I do some other labour works as well when I can. Normally things for Gunther or Murry. But hauling be me normal job."

        "The horse takes a long drink and wipes his mouth before continuing."

        Terrance smile "I won't be lying to ye lad. It's a hard life. But I like it. I'm built for it as you can see."

        "You gulp as you stare the big equine up and down, eyes lingering on his broad chest and thick thighs."
        
        "You try to not linger to long on the loincloth that almost covers his privates... almost."

        Fen "I do... ummm... see."

        Fen "But you don't mind the hard work, everyday?"

        show terrance stern
        with dissolve
        "Terrance sighs and gives you a look you can't quite comprehend."

        Terrance "Lad, let me tell ye one thing. I'm not meant for anything but hauling carts, moving rocks or pulling out tree stumps."
        
        Terrance "Thinking isn't for me. I cannae do fiddly things with these giant hands."
        
        Terrance normal "When I'm hauling me goods around, I can just enjoy the honest hard work. It's all that I'm good at."

        Terrance "And for as long as I can haul and tote... I will."

        "You swear you hear a bit of sadness in his voice but he seems disinclined to talk further."
        
        "You decide to leave him to his thoughts."

        $ terrance_worktalk_first = True

        $ bondexp02 += 1
        call bondexpup02 from _call_bondexpup02_4
        $ ap -= 1

        jump work

label terrance_bond_01:
    stop music fadeout 3.0
    scene bg tavern4
    with s_dissolve

    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Fen "Ready for order?"

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    show terrance normal at right1
    with dissolve
    Terrance "Same as last time."

    hide fen
    hide terrance
    show bg tavern1
    with dissolve
    "You serve the giant horse drinks and soup as usual. This time you remembers to ask him what drink he want."

    show bg tavern4_blur
    show fen smile at left1
    show terrance normal at right1
    with dissolve
    Fen smile "Enjoy!"

    show fen normal at flip
    with dissolve
    "Just when you were about to leave, Terrance stopped you."

    Terrance "Wait a moment lad."

    show fen stern at flipback
    with dissolve
    "You pause and turn back to the draft horse."

    Terrance "Mind staying a while and chatting? Nice to have some conversation white eating."

    show terrance at flip
    with dissolve
    "His gestures around the room."

    show terrance at flipback
    with dissolve
    Terrance "And it's not that busy, ye can stay a few minutes I'm sure."

    Fen "I... umm... Sure? I don't mind... I just can't let Gunther get overwhelmed or anything."
    
    Fen normal "But you're right, not many here."

    Terrance "I know how he is. But not interested in Guther, I know all about that tiger."
    
    Terrance smile"I'm more interested in ye. Are ye feeling better? Gunther told me about ye situation."

    show fen stern
    "You feel yourself grow a bit flustered at the direct question but can stammer out a reply after a few moments."

    Fen stern "I mean I guess? I'm still a bit sore from the fall and just feel..."

    show terrance normal
    "The equine nods as he continues to eat, urging you to continue."

    Fen "I guess I'm just overwhelmed with everything. So much happened so fast and I'm not used to it."

    "You sigh sadly and look down forlornly at the floor."

    Fen stern2 "It can be frustrating. If it wasn't for Gunther helping me out, I don't know what I'd do."
    
    Fen sadsmile "He's been nothing but kind to me. Saving me, putting me up and giving me a job."

    Fen blush "I mean even with him walking in on me..."

    "You stop and feel your face blushing when you remember when Gunther walked in on you completely naked."

    show fen blush2    
    "You notice the horse looking at you quizzically and your gaze lowers."

    hide fen
    show terrance normal at center1:
        zoom 1.5
        ypos 1400
    show ratio1
    with dissolve
    "Even sitting behind the table, Terrance's lower body is easily visible and you can clearly see the loincloth barely covering the horse's privates."
    
    show terrance normal at center1:
        ypos 2200
    with move
    "Gulping, you force yourself to look back up and see Terrance giving you a sly smile."

    show fen blush at left1
    show terrance normal at right1:
        zoom 1
    hide ratio1
    with dissolve
    Fen "I mean... he..."

    "You feel yourself blushing even deeper."

    Terrance smile "Hah, you saw the old cat naked did ye? He tends to walk around like that sometimes."
    
    Terrance "I've seen him more than once while staying here for the night."

    "The horse notices your discomfort and pauses before giving you a reassuring smile."

    Terrance normal "Hey, don't worry about it. It's not uncommon around here for folk to be naked or close to it. Like me."

    "He pushes himself away from the table and stretches. You can't help but lower your eyes to try and sneak a quick peek but snap them back up when he continues to talk."

    Terrance "It's just a matter of comfort and safety. Hauling is hard work and I dunna need clothes to get me overheated or catching on something."
    
    Terrance "This loincloth is good enough for what is considered modesty in these parts."

    Fen "Hmm... I guess I'm just not used to that?"

    "You pause and think for a second."

    Fen stern "I wonder if that's why I'm having some issues adjusting? Maybe I'm from somewhere where nudity isn't as... umm... common?"

    show terrance smile
    "Terrance goes back to his stew and has a few more swallows. Chewing thoughtfully he considers what you said."

    Terrance normal "That could be. Might be something to ask people who know more about cultures around here than I do."
    
    Terrance "I'm just a simple hauler. Wouldnae know much outside where I normally work."

    Fen normal "I'll ask Gunther about that."

    show fen at flip
    with dissolve
    "Saying the name out loud, you pause and look around. You see the tiger standing by the bar, tankards in both hands and he's giving you a slightly amused look."
    
    "Glancing around, you see the bar has gotten busy and Gunther is beginning to get overwhelmed with orders."

    show fen shock at shock, flipback
    Fen "Dammit!! I'm sorry, I have to get back to work."

    Fen normal "Hope to talk more soon Terrance!"

    stop music fadeout 3.0
    hide terrance
    hide fen
    show bg tavern4
    with s_dissolve
    "You notice the appreciative nod and quiet whinny from Terrance as he watches you get back to work."

    call bondlvup0201 from _call_bondlvup0201

    $ ap -= 1

    jump work

label terrance_bond_02:
    # Add lines of Gunther ask Fen to give Terrance a shower.
    scene bg fenroom
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    play sound "audio/knock door.ogg" volume 1.0
    "As you cling to your pillow, you hear knocking sounds at your door."

    #knocking sound
    Gunther "Wake up, pup. It's past noon already."

    "Seems like you overslept today."

    play sound "audio/Door Open 2.ogg" volume 1.0
    "You quickly get up from the bed and put on your clothes and let Gunther in."

    show fen stresse at left1
    show bg fenroom_blur
    with dissolve
    Fen "Sorry! I'll get ready to help you!"

    show gunther normal at right1
    with dissolve
    Gunther "No need to. Terrance is at the backyard, go down and assist him with a quick shower."

    Gunther stern "It's usually my job, but I need to fix some bent chairs."

    Fen blush "Give Terrance a shower... I don't know if I'm up for the job."

    Gunther grin "Well, you have to try it sooner or later."

    Gunther smile "And I bet you'll love the work."

    stop music fadeout 3.0
    scene bg tavernback
    with s_dissolve
    "Walking down the stairs to the courtyard you stop and take in the view. You see the massive draft horse getting ready for his shower."
    
    "He is back on to you and you his loincloth is already neatly folded and laid off to the side."

    "Gulping slightly, you enter the courtyard and stand behind Terrance."
    
    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    show terrance naked normal at right1, flip
    show bg tavernback_blur
    with dissolve
    "He doesn't seem to be aware of your presence as he is busy filling a large wash basin with water from a pump."
    
    "A giant cauldron is boiling on a large bonfire nearby."

    show fen blush at left1
    with dissolve
    Fen "Cough... Ummm, Terrance? I'm here to give you your shower."
    
    Fen "I know Gunther normally does it but he's really busy and asked me to do it and I didn't umm... I didn't mind."

    show terrance at flipback
    with dissolve
    "The horse turns and looks at you, smiling slightly. He nods and continues to fill the bucket."
    
    "As you stand there, he walks over and picks up the cauldron by the side handles and easily pours the boiling water into the basin."

    Terrance naked smile "Just a minute there [name], lemme get the water set up and I'm good to go."

    show terrance at flip
    with dissolve
    "The water hisses and steams as boiling water hits the colder water and when finished, Terrance sticks a hand into the basin and swirls it around for a moment."

    Terrance naked normal "Perfect."

    show terrance at flipback
    with dissolve
    "He turns slightly to regard you once more. You can't help but swallow as you admire the muscles on his broad back and his firm rump."
    
    "His tail sways in the gentle breeze and you step forward, picking up a cloth from a ledge as well as a large bit of soap from a dish."

    Terrance "OK lad, start with my back. It's the one place I really cannae do myself."
    
    Terrance "Downside to being my size. Lemme sit down here so y'all don't have to stretch too much."

    stop music fadeout 3.0
    scene terrance cg1 01 at top
    with s_dissolve
    "Grabbing a stool that was nearby, the horse heavily sits down and you idly wonder if the stool can support his massive bulk."
    
    "It seems to bend slightly but holds and you walk up to Terrance."
    
    "Noticing some dust and dirt in his mane, you start brushing it off before dipping the cloth in the water."

    Fen "Sure, no worries. So... how was your day?"

    scene terrance cg1 02 at top
    with s_dissolve
    "You hear the horse snort and see his head shake slightly as you lather some soap on the cloth."
    
    play sound "audio/mopping.ogg" volume 1.0 loop fadein 2.0
    "Swallowing, you press the cloth against the back on his neck and slowly begin to clean it."

    scene terrance cg1 02 at top:
        zoom 1.3
    with s_dissolve
    "His fur is short so you can work the soap into it easily and as you slowly work your hand around his neck, you hear Terrance sigh in satisfaction."

    Terrance "Oh that's the spot. Ugh, same as ever. Hauling a heavy cart here, to get stuff to haul it all there."
    
    Terrance "It's hard but honest work."

    "As Terrance talks about his job, you zone out slightly and concentrate more on washing his back and shoulders."

    "You take your time, rubbing and kneading the muscles as you work the soap in, lathering the horse's entire back before grabbing a small cup and rinsing him off."
    
    "Seeing a few stubborn stains you redouble your efforts."

    Fen "There's a few stains I didn't get, lemme try again."

    Terrance "Dunnae worry about it, take all the time you need."
    
    Terrance "I ain't going anywhere till you're done. Dunnae hesitate to use those claws if you gotta. Gunther does all the time."

    "You pause and look at your claws, nervously you push them against the horse's back to try and scrape off the last few bits of stubborn dirt."
    
    "A contented whinny from Terrance makes it obvious he doesn't mind."

    Terrance "Dunnae be worried about hurting me, my hide's as thick as any leather ye could imagine."

    scene terrance cg1 03 at top:
        zoom 1.3
    with s_dissolve
    "The two of you engage in more idle banter as you give Terrance's back another wash and rinse."
    
    stop sound fadeout 3.0
    scene terrance cg1 03 at top:
        zoom 1
    with s_dissolve
    "Eventually, the job is done to your satisfaction and you step back to admire your work, and also find yourself admiring the muscular backside of the horse."

    scene terrance cg1 04 at top
    with s_dissolve
    Terrance "All done lad? Good, feels clean. Now do ye want to keep going?"
    
    Terrance "I can manage the rest on my own, but I admit, it's easier when someone else does it."

    scene terrance cg1 04 at center
    with ease
    "Before you can say anything, Terrance stands up and stretches."
    
    "Shaking himself, he casually continues to stretch either unaware or not caring that you are now getting a front row seat to see not only his toned rump..." with hpunch
    
    scene terrance cg1 04 at center:
        zoom 1.3
    with s_dissolve
    "...but seeing his balls and even his cock swaying between his legs."

    menu:
        "Do you agree to continue?"

        "No":
            jump terrance_bond_01_no1

        "Yes":
            jump terrance_bond_01_yes1

    label terrance_bond_01_no1:
        scene bg tavernback
        with s_dissolve
        "Gulping, you take a step back from the horse and place the cloth and soap back on the ledge."
        
        "While many emotions are running through you, you decide this might not be the best time or place to figure out exactly what you want from the massive equine."

        show fen blush at left1
        show bg tavernback_blur
        with dissolve
        Fen "I... I can't right now. I have to get back to work and help Gunther."
        
        Fen "Pretty sure I heard him calling me. You can handle everything else yourself right?"

        "You think you hear slight disappointment in the horse's voice, but are unsure."

        show terrance naked normal at right1
        with dissolve
        Terrance "Oh? Nae a problem, I can finish washing myself. Thanks for the help with my back through. I appreciate it."

        Fen "No worries, I'll be happy to help you again later if needed."

        Terrance naked smile "I'll remember that. Have a good dag lad."

        Fen "You too."

        stop music fadeout 2.0
        stop sound fadeout 2.0

        hide fen
        hide terrance
        show bg tavernback_blur
        with s_dissolve


        scene bg tavernback
        with s_dissolve

        $renpy.end_replay()

        #call bond level up and other stuff

        call bondlvup0202 from _call_bondlvup0202

        scene bg black
        with s_dissolve

        jump night_start

    label terrance_bond_01_yes1:
        scene terrance cg1 04 at center:
            zoom 1
        with s_dissolve
        "Gulping, you take a step back from the horse and nervously juggle the soap between your hands."
        
        "While many emotions are running through your mind and you're not quite sure if this is the time and place..."
        
        "You decide that it might help you figure out exactly what you are feeling towards the massive equine."

        Fen "I mean sure, not very sporting of me to only half wash your back. I'm sure if Gunther needs me, he'll call out."

        Terrance "If Gunther sent ye to help me shower..."

        "Terrance laughs for a moment before continuing."

        Terrance "He knows exactly how long it can take. He's helped me enough times. I doubt he'll rush you."

        "You don't know whether to feel relieved at that information as you wonder if there's anything to be read into it, or if it's just a plain statement of fact from Terrance."

        scene terrance cg1 04 at center:
            zoom 1.3
        with s_dissolve
        play sound "audio/bathtubsit.ogg" volume 0.5
        "Shrugging slightly, you dip the cloth into the still hot water and lather it with soap before pressing it against the horse's lower back."

        "Pausing for a moment, you can't help but stare at Terrance's rear."
        
        "It's just as large and muscled as the rest of him and a part of you is dying to just rub it, squeeze it and see just how firm it is." 

        "Taking a deep breath and ignoring the butterflies in your stomach you do exactly that."

        Fen "Umm, sorry, your behind is a bit dusty? I'll have to scrub a bit to clean it."

        Terrance "Are ye saying I have a dirty arse lad?"

        "Your face flushes with embarrassment and you try and stutter out an apology before Terrance laughter calms your nerves."

        Terrance "I know what ye mean lad. Dunnae get flustered. I tend to sit on some pretty dusty benches and stones over the day."

        "The horse pauses for a moment before speaking a bit softly."

        Terrance "I get it might be a bit too much so you can skip..."

        "You hurriedly interrupt him."

        Fen "No no... I don't mind, really. I mean it's just a butt right?"

        play sound "audio/mopping.ogg" volume 1.0 loop fadein 2.0
        "You press extra hard to prove the point and Terrance emits a slightly startled whinny, but it turns into a sigh of contentment as your hands begin to knead away."
        
        scene terrance cg1 05 at center:
            zoom 1.3
        with s_dissolve
        "The dirt is gone in no time but you continue to rub, squeeze and knead the horse's rump."

        Fen "Oh yeah... right..."

        "You quickly remember there is more to this than just Terrance's ass and you quickly move to his thighs and calves, paying them just as much attention."

        "You remember a certain tool Gunther mentioned, a pick to clean hooves and you quickly spot it and pick it up."

        Fen "Umm, can you let me clean your hooves now Terrance?"

        "Terrance's reply is a bit distracted sounding, almost like he was lost in thought."

        scene terrance cg1 05 at top:
            zoom 1
        with s_dissolve
        Terrance "What? Oh right. Aye, thanks [name]."

        "It takes a few minutes to clean the dirt and pebbles out of each of his hooves and once done, you grab a comb and briskly brush out his tail."
        
        "As you brush, you hear Terrance speak, his voice playful sounding."

        Terrance "Much obliged lad. The old tiger sometimes forgets my hooves and tail. I'll definitely be telling Gunther how thorough ye are."
        
        Terrance "But speaking on being thorough..."

        scene terrance cg1 05 at center:
            zoom 1.5
        with s_dissolve
        "His tail flicks away from your hand and he bends forward, placing one hoof on the stool."
        
        "You feel your cock tenting in your pants as you get an extremely close up view of everything the horse has to offer."
        
        "His tail even lifts, exposing his tailhole."

        Terrance "Still feels just a wee bit dirty lad, as I said too much dust and dirt in my line of work."
        
        Terrance "Could ye give my backside one more quick wash to make sure ye got it all?"

        Fen "I mean..."

        "You think for only a split second before answering."

        Fen "Yes."

        "Taking the cloth again, you start eagerly rubbing the horse's behind."
        
        "This time there isn't any cleaning, you are simply feeling up his ass and enjoying it."
        
        "The happy sighs and neighs coming from Terrance is a good indication he's enjoying it too."

        "You do though carefully run the cloth over his hole and while this causes a few slight shudders from Terrance."
        
        "You notice his balls twitch, and decide that doing anything else there might be overstepping things."
        
        stop sound fadeout 2.0
        "With one final, two handed squeeze, you step away."

        scene terrance cg1 05 at center:
            zoom 1
        with s_dissolve
        Fen "There. That's the cleanest butt I've seen in years."

        "Terrance runs his hands over his rump and you feel your cock throb again as he casually runs a finger over his tailhole, pushing gently against it."
        
        "You don't know if he's teasing you or just checking, but you appreciate the view."

        play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
        show terrance naked normal at top:
            zoom 1.5
            ypos -500
        show bg tavernback_blur behind terrance at center:
            zoom 1.1
        with s_dissolve
        "The horse turns and you can't help but stare as his cock is now slightly erect and twitches slightly as he talks."

        show terrance naked normal at top:
            zoom 1.5
        show bg tavernback_blur behind terrance at top:
            zoom 1.1
        with ease
        Terrance naked smile "Amazing job lad. Many thanks, ye have no idea how much I appreciate this."

        Fen "Ummm, no problem Terrance, glad to help."

        "You force yourself to look up to Terrance's face and you see he has another slight grin."
        
        show terrance naked normal
        with dissolve
        "Sitting down on the stool, you see his eyes dart down to your own bulge."
        
        "You feel your face turn a bit red under your fur and you quickly reposition yourself so your own erection isn't as noticeable."

        "When the horse speaks, there is a definite sly tone to it."

        Terrance "Well, if ye have the time, I'd be willing for ye to wash my front too."
        
        show terrance naked smile
        with dissolve
        Terrance "Yer doing such a good job and seem to be enjoying yerself as well. What you say [name]? Like to help this old horse wash his chest too?"

        Fen "I..."

        menu:
            "Got to go.":
                jump terrance_bond_01_no2

            "Let me help you out.":
                jump terrance_bond_01_yes2b

    label terrance_bond_01_no2:
        "While the hardness in your pants screams yes, you think that this might be going a bit too far for now."
        
        "You definitely have a strong interest in Terrance and you're beginning to think he might have some interest in you, but what exactly you can't say."

        show terrance naked smile at top:
            ease 0.5 zoom 1.6

        pause

        show terrance naked smile at top:
            ease 0.5 zoom 1.5
        "Reaching out, you gently lay one hand on his chest and hold it there for a moment before pulling your hand away."
        
        "You notice his ear flick as you do so."

        scene bg tavernback_blur
        show fen blush at left1
        show terrance naked normal at right1
        with s_dissolve
        Fen "Maybe next time? I'm getting worried about running late."
        
        Fen "But next time I give you a shower, I'll make sure I have enough time to wash your chest too."

        "You're positive you see a quick look of disappointment in the horse's eyes, but it's gone in mere moments, replaced with an easy going smile."

        Terrance naked smile "That's fine [name], I can finish up here. But... I'm going to hold ye to that now."

        hide fen
        with dissolve
        "The two of you exchange a grin and you head back into the inn."
        
        "Smiling, you call back over your shoulder."

        show fen smile at left3
        with dissolve
        Fen "Good! See you soon Terrance!"

        hide fen
        with dissolve

        pause

        Terrance naked normal "I wonder..."

        stop music fadeout 2.0
        stop sound fadeout 2.0

        scene bg tavernback
        with s_dissolve

        $renpy.end_replay()

        #call bond level up and other stuff

        call bondlvup0202 from _call_bondlvup0202_1

        scene bg black
        with s_dissolve

        pause

        jump night_start

    label terrance_bond_01_yes2b:

        "You stop to consider the offer."
        
        "The hardness in your pants is screaming yes and while this might be going a little too far, you admit you desperately want to rub the horse's chest."
        
        "Something about this gentle giant speaks to you and you want to see how far you can go."

        Fen "I mean, if you're OK with it, yeah, I'd like to help you more."

        Terrance "Wouldnae have offered if I wasnae ok with it."

        hide terrance
        show bg tavernback at center:
            zoom 1
        with dissolve
        "Nodding, you grab the cloth and begin to lather it up again."
        
        "As you reach out, Terrence stops you."

        show terrance naked normal at top:
            zoom 1.5
        show bg tavernback_blur at top:
            zoom 1.5
        with dissolve
        Terrance "One thing. I know yer a bit shy. So I'm just telling ye now, ye can do whatever ye want ok?"
        
        Terrance "I know a shower's all about getting clean and yer doing a great job there, but..."

        "He stops with a grin that says everything you need to know."
        
        "You gulp, but nod, stepping forward to get as close to the horse as you can."
        
        "Terrence raises his arms over his head and looks at you eagerly, waiting to see what you're about to do."

        "And what you do is manage to accidentally soak the front of your tunic with the washcloth."
        
        "Stepping back in dismay, you look at your now wet tunic and frown. Terrence for his part is snickering quietly."

        Terrance naked smile "Sorry lad, bit funny. But ye know, ye can spare the clothes from getting wet by just doing it naked."

        "Your ears burn as you hear the suggestion."
        
        "You never would have thought to have gotten naked and now that Terrence has mentioned it, you feel both a deep embarrassment and a burning desire about it."

        Fen "Oh... Umm... Gunther would kill me if he found out I did something like that!"

        show terrance naked normal
        "The horse looks at you incredulously for a moment before laughing."

        Terrance naked smile "The blazes he would! He's always naked when giving me a shower so why would he care if you were?"

        Fen "Wait? Really?"

        Terrance "Yes! For that exact reason, keeps his clothes from getting wet or dirty and a few other reasons..."

        "You pause to think about this information. Modesty says that you should remain clothed, regardless of what happens."
        
        "Everything else says that if Gunther does it..."

        Fen "You don't mind?"

        Terrance naked normal "Not at all, be lying if I said I wasnae curious to some degree myself."

        "With that you begin to strip."
        
        hide terrance
        show bg tavernback at center:
            zoom 1
        with dissolve
        "Your tunic and undershirt are a bit difficult to remove due to them now being wet but eventually they come off and you fold them and put them off to the side."

        #Fen Underwear
        show fen uw blush at center1
        show bg tavernback_blur
        with dissolve
        "Your trousers take no time and you pause, clad only in your undergarment, which you note with some embarrassment are straining to contain your erection."
        
        "Terrence notices and smiles gently."

        hide fen
        show terrance naked smile at top:
            zoom 1.5
        show bg tavernback_blur at top:
            zoom 1.5
        with dissolve
        Terrance naked smile "No worries lad, we're all men here right?"

        show terrance:
            ypos -700
        show bg tavernback_blur:
            ypos -500
        with ease
        "He reaches down and squeezes his own massive member as if to reassure you and taking a deep breath."
        
        hide terrance
        show fen hard blush at center1
        show bg tavernback_blur at center:
            zoom 1
        with dissolve
        "You remove that last bit of clothing and stand fully nude before the horse."
        
        "You hear a sharp intake of breath and you watch his eyes go over your body, pausing to obviously admire it."

        play sound "audio/mopping.ogg" volume 1.0 loop fadein 2.0
        stop music fadeout 3.0
        hide fen
        show bg tavernback
        with dissolve
        "Blushing furiously, you quickly grab the cloth and step close to Terrence and begin to scrub his chest, hoping that will distract him from you."

        show terrance naked normal at center1:
            zoom 2.5
            ypos 2800
        show bg tavernback_blur at top:
            zoom 2
        with dissolve
        "As you lather up his pecs, you strain a bit to get through the thick patch of hair on his chest..."
        
        "...But eventually you're pleased to notice that you're making headway."
        
        "You fail to notice that just as much soap is getting onto you as Terrence."

        "Pausing to admire your efforts, you realise that as you worked, you had leaned more into Terrence's massive leg and are now essentially sitting on his thigh..."
        
        "...And Terrence has one arm around your back to stabilise you."
        
        "Shrugging, you accept it for what it is and return to your job at hand."

        "Taking the time now to just enjoy yourself, you start to spend more time squeezing and kneading Terrence's pecs and abs than really doing any washing."
        
        "Sure, there's soap and water involved but it's definitely taking a secondary role."

        "You even feel brave enough to pay particularly close attention to his nipples, using your thumb to make both of them erect in turn."
        
        "which gets you a slight shudder and a happy sigh from the horse."

        show terrance naked smile at center1:
            zoom 2.5
            ypos 3300
        with ease
        Terrance "That's the spot. Yer doing well lad."
        
        Terrance "Wouldn't be lying if I said I'm enjoying the treatment yer giving me."

        show terrance naked normal at center1:
            zoom 2.5
            ypos 2800
        with ease
        "You give Terrence a shy look but say nothing, continuing to explore his massive upper body."

        stop sound fadeout 3.0
        Terrance "I mean I've heard the comments from the guys in the tavern. The crude comments, the lustful desires."

        "He stops and gives you a thoughtful look."
        
        play sound "audio/bathtubsit.ogg" volume 1.0
        "Reaching over to the basin, he grabs the ladle and uses the hand that was around your back to begin to rinse the water off each of you."
        
        "You wonder why he didn't use his other hand but when you look down, your eyes boggle at the sight."

        show terrance hard normal at center1:
            zoom 2.5
            ypos 2100
            xpos 1500
        with ease
        "You see that Terrence was using his other hand to hold back his now fully erect cock."
        
        "You try to estimate the length, but as the horse is sitting down and holding it off to the side, you can only guess 'a lot larger than yours'."

        #Terrance Blush
        show terrance naked blush at center1:
            zoom 1.5
            ypos 2050
        show bg tavernback_blur at top:
            zoom 1.5
        with dissolve
        "Terrence looks at you and for the first time, you see a flash of embarrassment cross his features before they settle back into the normal nonchalant look."

        Terrance naked normal "Erm, didn't think ye'd want to have that slapping into ye, so I just held it back."
        
        Terrance naked normal "I mean, ye do have a way with those paws of yers lad."
        
        Terrance "I mean, I can handle the rest here, ye dunnae need to wash my junk for me, I understand."
        
        Terrance naked blush3 "Heh, especially seeing ye kinda got me worked up a bit there, [name]. If ye washed me there..."

        "The embarrassed look flashes over his face again and this time he's unable to hide it."
        
        "You actually find the sight of the massive horse blushing rather charming."

        Terrance naked blush "Let's just say that I'll have a mess to clean up after the shower and ye might need one too."

        menu:
            "Do you agree to wash Terrence's privates?"

            "No":
                jump terrance_bond_01_no2b
            
            "Yes":
                jump terrance_bond_01_yes2

    label terrance_bond_01_no2b:
        
        hide terrance
        show bg tavernback at center:
            zoom 1
        with dissolve
        "You nod and quickly move off of the horse's thigh and back up."
        
        #Fen underwear
        show fen uw blush4 at left1
        show bg tavernback_blur
        with dissolve
        "Grabbing your clothes from the ledge you placed them on, you cover your own throbbing erection and give the horse a smile."
        
        Fen "Maybe you're right Terrence. But..."
        
        Fen "I really want to do this again sometime, maybe the next time you need a shower I can give it to you again?"
        
        Fen uw blush "Assuming Gunther doesn't mind."

        show terrance hard smile at right1
        with dissolve
        Terrance "Hah, if I ask for ye, the old cat will send you. Dunnae worry about that."

        "Terence stands and stretches and you feel your jaw hit the floor as the full majesty of his awesome body fills your vision."
        
        "Finally there is nothing blocking your vision and you are eternally grateful for that."

        "With a wink, Terrence casually grabs his cock and slowly strokes it a few times, maintaining eye contact with you."
        
        "All of the previous embarrassment he showed is now gone. With a sensual lick of his lips he speaks."

        Terrance "And ye can bet, I'll be asking for ye directly next time I need a shower, [name]."

        hide fen
        hide terrance
        show bg tavernback_blur
        with dissolve
        "With that, he turns and begins to scrub himself as you retreat back into the inn."
        
        "As you make it through the doorway, you hear the horse mutter to himself."

        Terrance "I wonder..."

        stop music fadeout 2.0
        stop sound fadeout 2.0

        scene bg tavernback
        with s_dissolve

        $renpy.end_replay()

        #call bond level up and other stuff

        call bondlvup0202 from _call_bondlvup0202_4

        scene bg black
        with s_dissolve

        pause

        jump night_start


    label terrance_bond_01_yes2:
        "You stop and consider what Terrance has just told you."
        
        show terrance hard smile at center1:
            ypos 1500
            zoom 1.6
        with dissolve
        
        "Without hesitation you reach down and place your hands over his and slowly pull it away from his cock."
        
        show terrance hard smile at top:
            zoom 1.6
        with ease
        "Placing his hand to his side, you smile at the horse and nod."

        "You can't help feeling incredibly embarrassed on one hand but you want this and you're not going to let anything get in the way."

        Fen "I'd love to."

        "He gives you a smile and closes his eyes."

        Terrance naked normal "OK then [name]... I'll let ye know when..."

        stop music fadeout 3.0
        "It only takes you a moment to understand what he meant by that and you nod."
        
        play sound "audio/mopping.ogg" volume 1.0 loop fadein 2.0
        show terrance hard smile at center1:
            ypos 1500
            zoom 1.6
        with ease
        "Taking the cloth, you lather it up one last time and decide to get the washing part out of the way as fast as possible as you have other plans for the horse."

        show terrance hard smile at center1:
            ypos 1700
            xpos 1300
            zoom 2
        with s_dissolve
        "It only takes a moment to wash the massive member and you toss the cloth into the basin."

        "The whole time you can feel his rod rising in your hands, growing heavier and heavier."

        stop sound fadeout 1.0
        Fen "Well, seems clean, but I guess I should be really thorough eh?"

        Terrance "I'm not complaining lad..."

        scene terrance cg1 08 at truecenter
        with s_dissolve
        "Grinning, you take the horse's cock in your hands and lay it up against your chest."
        
        "With you still mostly sitting on Terrance's thigh, his cock rests nicely against your chest, fitting snugly between your pecs."
        
        "Your own erection is throbbing and you allow it to rest against Terrance's cock."

        "Reaching down, you take Terrance's balls in your hand, marvelling at how large and heavy they are."
        
        "Bouncing them gently in your hands, you feel the thick tuft of fur that helps separate them and rolls them around a little before letting them drop back down..."
        
        "Where they end up resting on your thigh."

        scene terrance cg1 09 at truecenter
        with s_dissolve
        Fen "Awfully heavy there Terrance... when's the last time you emptied them?"

        "Terrance pauses a moment before answering."

        Terrance "Honestly lad? With all the hours I work, I havenae really had any time for personal pleasure in..."
        
        Terrance "I dunnae know how long. Been getting to me a bit let me tell ye."
        
        scene terrance cg1 10 at truecenter
        with s_dissolve
        play sound "audio/deep growls 1.ogg" volume 0.5 fadein 1.0 loop
        "Starting at the base, you slowly massage the horse's member. You slowly work your way up its length, making sure to gently caress every inch of it."
        
        "As you reach the ring, you can feel it twitch and throb beneath you and Terrance's breathing has gotten much shallower and faster."

        "You notice with some excitement that Terrance is almost mindlessly pushing his cock between your pecs, which was a sensation you definitely didn't expect to be feeling today."

        scene terrance cg1 11 at truecenter:
            zoom 1.2
        with s_dissolve
        play sound "audio/deep growls 1.ogg" volume 1.0 fadein 1.0 loop
        "You decide to go with this new avenue and allow him to pec fuck you harder, squeezing your own chest muscles to help pleasure him."
        
        "The very contented whinnys and snorts from the horse indicate that he is enjoying the feelings himself."

        Fen "Holding up there Terrance?"

        Terrance "Not much longer lad..."

        "The reply is strained and you give him a smirk and your hands reach near the now flaring head."

        Terrance "Bit more right there lad and lean back..."

        "Your hands rub around the fully flared head and you can feel the balls lifting off your thigh."
        
        "You feel Terrance's body beginning to shake and feel his hand dig into your side."

        "Quickly rubbing your hands up and down the entire length of his cock, you know the horse is about to cum, as thick spurts of pre are already jetting forth, soaking your chest fur."

        Terrance "[name], I'm...."

        menu:
            "Do you move away?"
            "No":
                jump terrance_bond_01_no3

            "Yes":
                jump terrance_bond_01_yes3

    label terrance_bond_01_no3:
        "Knowing full well what's about to happen, you decide that the best way to pleasure Terrance is to let him use you as a warm, muscular cum rag."
        
        "So when you know he's about to cum, you stand and lean into it, his flared head firmly pressed between your pectorals."

        play sound "audio/deep climax 1.ogg" volume 2.0
        scene terrance cg1 12 at truecenter:
            zoom 1.5
        with s_dissolve
        Terrance "HUNGHHH!!!"

        "Leaning to face Terrance, you pull him into you in an impromptu hug, which he returns eagerly."
        
        "While you were expecting a bit of a mess, the sheer amount of cum that shoots out surprises you."
        
        play sound "audio/deep climax 1.ogg" volume 1.0
        "Wave after wave blasts into your chest and under your muzzle."

        "While keeping his massive load contained between your bodies because of the hug, it also means both of you get thoroughly coated in a thick layer of jizz."

        scene terrance cg1 13 at truecenter:
            zoom 1.2
        with s_dissolve
        "After a moment the horse's cock gives one last spurt and stops, resting once again against your now sticky and drenched chest."

        scene terrance cg1 14 at truecenter:
            zoom 1
        with s_dissolve
        "Breaking away from the hug, Terrance looks at you with an expression you can't quite decipher."

        hide terrance
        show bg tavernback_blur at truecenter:
            zoom 1.5
        with s_dissolve
        "A smile breaks out on his face and he gently touches his forehead against yours."

        show terrance naked smile at top:
            zoom 2
        with dissolve
        Terrance "I needed that, thank ye [name]. Whew, bit dizzy. Let me get my bearings for a moment."

        hide terrance
        show bg tavernback at truecenter:
            zoom 1
        with dissolve
        "As he rests, you look around. While both of you are covered in a thick layer of cum, the courtyard itself is remarkably clean."
        
        play sound "audio/bathtubsit.ogg" volume 0.75
        "Standing up, You grab a cup from the now cool basin and begin to pour the water over the pair of you, washing away the mess."

        play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
        show terrance hard smile at top:
            zoom 1.5
        show bg tavernback_blur
        with dissolve
        Terrance "Say [name]..."

        "When the horse speaks, you turn to look at him. He's still sitting on the stool, but is watching you with a strange expression."

        Terrance hard normal "Ye know, I do want to thank ye for all this. Ye went above and beyond."

        "You feel yourself blushing slightly, as you know full well you were enjoying yourself just as much as the horse was, maybe even more in some ways."

        Terrance hard smile "So I was thinking... I normally help Gunther out after... So why not let me help ye out? I mean, I think ye can use it."

        hide terrance
        show fen hard hot2 at center1:
            zoom 1.5
        show ratio1
        with s_dissolve
        "He looks pointedly at your own still hard erection and you blush more when you realise he's offering to jerk you off."
        
        "Your dick gets even harder with the idea and you stand there thinking about what to say as he looks at you."

        jump terrance_bond_02_menu

    label terrance_bond_01_yes3:
        hide terrance
        show bg tavernback_blur at truecenter:
            zoom 1.5
        with s_dissolve
        "Remembering what the horse said, you quickly lean back and use your hands to aim his now erupting cock away from you."

        play sound "audio/deep climax 1.ogg" volume 2.0
        scene terrance cg1 15 at truecenter:
            zoom 1
        with s_dissolve
        "Great waves of his cum shoot forth and splatter against the wall of the courtyard."
        
        "His body shakes as he tries to hold you steady, but you have to stand to keep from tumbling off his thigh."

        play sound "audio/deep climax 1.ogg" volume 1.0
        Terrance "HUNGHHH!!!!" with vpunch

        "Continuing to hold his cock, you continue to jerk him off until he finally stops cumming, the last few small shots falling to the ground at your feet."
        
        hide terrance
        show bg tavernback_blur at truecenter:
            zoom 1.5
        with s_dissolve
        "Hearing Terrance emit a deep contented whinny, you look at him."

        show terrance hard smile at top:
            zoom 1.5
        show bg tavernback_blur
        with dissolve
        Terrance "I needed that, thank ye [name]. Whew, bit dizzy. Let me get my bearings for a moment."

        hide terrance
        show bg tavernback
        with dissolve
        "As he rests, you look around. While the courtyard needs a bit of a cleanup now, you were able to make sure that both you and Terrance stayed mostly clean."
        
        "A little of his cum on your foot and some of his pre soaking your chest fur is all that needs to be washed away and you do that while the horse recovers."

        play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
        show terrance hard normal at top:
            zoom 1.5
        show bg tavernback_blur
        with dissolve
        Terrance "Say [name]..."

        "When the horse speaks, you turn to look at him."
        
        "He's still sitting on the stool, but is watching you with a strange expression."

        Terrance hard normal "Ye know, I do want to thank ye for all this. Ye went above and beyond."

        "You feel yourself blushing slightly, as you know full well you were enjoying yourself just as much as the horse was, maybe even more in some ways."

        Terrance hard smile "So I was thinking... I normally help Gunther out after... So why not let me help ye out? I mean, I think ye can use it."

        hide terrance
        show fen hard hot2 at center1:
            zoom 1.5
        show ratio1
        with s_dissolve
        "He looks pointedly at your own still hard erection and you blush more when you realise he's offering to jerk you off."
        
        "Your dick gets even harder with the idea and you stand there thinking about what to say as he looks at you."

        jump terrance_bond_02_menu
    
    label terrance_bond_02_menu:

        menu:
            "Do you let Terrance jerk you off?"
            
            "No":
                jump terrance_bond_01_no4

            "Yes":
                jump terrance_bond_01_yes4

    label terrance_bond_01_no4:
        hide ratio1
        show fen hard hot3 at left1:
            zoom 1
        show terrance hard normal at right1
        show bg tavernback_blur at truecenter:
            zoom 1
        with dissolve
        "While you definitely want it, your brain is reeling from everything else that happened and you don't know if you could handle it right now."

        "Plus, now that you've had a bit of time to ponder things, you realise that while you're perfectly fine servicing the horse, you don't quite think you're comfortable with him returning the favour."
        
        "You don't know exactly why however."

        Fen hard hot2 "I... I... I really want to but I don't think I can handle that right now."
        
        Fen hard blush "This has been a lot for me Terrance."

        "You gaze down at the floor with a bit of shame."

        Fen "I'm sorry."

        "You hear the surprised snort from Terrance."

        Terrance hard smile "Sorry? What do ye have to be sorry for lad? If ye want it, I'm willing to give it, but if not."
        
        Terrance hard normal "Well that's yer choice to make, not mine. But the offer stands."

        "You look up at the horse who is smiling gently at you and you return the smile."

        Fen "I think next time... if yer still willing... I'd like to do that."

        Terrance hard smile "Oh, I would lad. No worries there."

        stop music fadeout 3.0
        scene bg tavernback
        with s_dissolve
        "With those encouraging words, you grab your clothes and head back to the tavern."

        "Pausing only once to wave goodbye to Terrance and admire his physique one last time."
        
        scene bg fenroom
        with s_dissolve
        "You know as soon as you get to your room, you're going to have to deal with your own erection, you wonder what the horse would have done."

        stop music fadeout 2.0
        stop sound fadeout 2.0

        scene bg tavernback
        with s_dissolve

        $renpy.end_replay()

        #call bond level up and other stuff

        call bondlvup0202 from _call_bondlvup0202_2

        scene bg black
        with s_dissolve

        pause

        jump night_start

    label terrance_bond_01_yes4:
        hide ratio1
        show fen hard hot2 at left1:
            zoom 1
        show terrance hard normal at right1
        show bg tavernback_blur at truecenter:
            zoom 1
        with dissolve
        "As you stand there, your mind reels with the potential."
        
        "You notice Terrance looking at you quizzically and you blush more before nodding yes."
        
        "Terrance smiles and stands up. You can't help but stare at his cock, which is still massive even though it's only semi erect now."

        Terrance "Trust me lad?"

        stop music fadeout 3.0
        "The question surprises you and you think for a moment before nodding yes."
        
        show fen hard hot2 at left2, flip:
            zoom 1.5
        show terrance hard smile at right2 behind fen:
            zoom 1.5
        show bg tavernback_blur at truecenter:
            zoom 1.5
        show ratio1
        with s_dissolve
        "When you do, Terrance stands up to you and turns you around before pulling you close to him."
        
        "You gasp as you feel his member lay against your back and you almost instinctively push against it."

        show fen hard hot2 at left2, flip:
            zoom 1.5
            ypos 1600
        show terrance hard smile at right2 behind fen:
            zoom 1.5
            ypos 1600
        with ease
        "As you wonder if the horse is going to try to fuck you, you feel one of his arms wrap around your chest and begin to rub your pecs..."
        
        "While the other slides down around your waist and rests in the thick patch of hair just above your cock."

        Terrance "Now dunnae get any ideas that I'm going to try anything. I have a feeling yer not up for taking me in that way... least not yet."

        play music "audio/stroking_slow_rhythmic_01.ogg" volume 1.0 fadein 3.0
        "You shudder at those words, thinking about the possibility but your thoughts are interrupted by Terrance's hand wrapping around your cock and squeezing it."

        "You feel like you're about to collapse and you grab onto Terrance's muscular arms for support as he slowly runs his thumb over the tip of your cock."

        play sound "audio/light moan 1.ogg" volume 1.0 fadein 3.0 loop
        "You gasp as you feel his rough hands rub over your nipples in turn, teasing them into becoming rock hard."
        
        "You whimper slightly and in response, he continues to flick his fingers over the sensitive nubs in turn."

        Terrance "Easy lad, I got ye. Ye just enjoy it OK?"

        Fen "I will but I'm not going to last long... I could cum right now I think."

        Terrance "Heh, I won't let ye lad..."

        show fen hard hot2 at left2, flip:
            zoom 2
            xpos 1200
            ypos 1600
        show terrance hard smile at right2 behind fen:
            zoom 2
            xpos 1750
            ypos 1600
        with dissolve
        "You feel the hand from your chest move down and grasp you under your balls, holding tightly and the other hand begins to stroke you."
        
        "At first light and gentle, Terrance slowly increases both the pressure and the tempo."

        "As the sensations mount you feel like you are about to cum, but can't and the feelings makes your entire body tremble."

        "You can't recall ever feeling this before and you continue to squirm under the ministations of Terrance."
        
        "You're vaguely aware that he's fully erect again and his cock is rubbing between your cheeks, just like it was against your pecs earlier."

        "You try to push against it but a rough whisper from the horse brings you up short."

        Terrance "No lad, this is about ye now, not me. I'll handle this after... but it's been a few minutes, are ye ready?"

        "You can barely focus but manage to say one word."

        Fen "Yes..."

        "With that, Terrance releases the grip on your balls and his hand quickly slides back up for chest, his fingers entwining in the thick hair there."
        
        stop music fadeout 3.0
        play sound "audio/light climax 1.ogg" volume 1.0
        show fen cum
        with dissolve
        "As this happens your entire body shudders and you feel the biggest orgasm of your life hit you." with hpunch

        "Your knees get weak and you grip the horse tightly for support as wave after wave of cum hits the ground, all the while the stroking continues."

        scene bg tavernback
        with dissolve
        "You feel like you're about to collapse as you finally stop cumming and you're grateful that the horse pulls you in tightly."

        play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
        Terrance "I got ye lad. Steady does it, just lean into me."

        "You feel Terrance's hands gently rubbing your chest and belly and you can't help but give a little whine as you enjoy his ministrations."
        
        "You particularly enjoy the belly rub and as his hand travels from your chest to your pubes, you moan a little."

        hide fen
        show terrance hard normal at top:
            zoom 2
        show bg tavernback_blur at truecenter:
            zoom 1.5
        with dissolve
        "After a few moments you feel steadier and you turn to face the horse."
        
        "You feel his throbbing dick slide against your body again but you ignore it somehow and hug the horse, you return the embrace."

        Fen "Oh god... That was incredible."

        Terrance hard smile "Honestly lad, it was damn fun for me too. Yer damn sexy and feeling ye react to me pleasuring ye was just..."

        "The horse stops and closes his eyes and you feel a shudder run through him."
        
        show terrance hard smile at top:
            ease 1 zoom 2.2
        "As he is about to re-opens his eyes, without even thinking, you reach up and caress the side of his face."
        
        show terrance hard normal at top:
            ease 1 zoom 2
        "His eyes open wide in surprise and you realise that you may have gone a bit too far."

        Fen "I... Oh god I'm sorry, I just..."

        Terrance hard smile "Oh hush lad."

        "Your stammering quiets down and the horse looks at you. He brushes the hair out of your face and smiles."

        Terrance "I dunnae mind, just wasnae expecting it."

        show fen naked blush at left1
        show terrance hard normal at right1:
            zoom 1
        show bg tavernback_blur:
            zoom 1
        with dissolve
        "His ears perk up and he pushes you away gently, much to your chagrin."

        Terrance "Wondering when he was gunna show up. Gunther, I heard him calling yer name."

        show fen naked shock at shock
        Fen "Oh crap... I gotta go!"

        hide fen
        with dissolve
        "You grab your clothes and race up the stairs but before entering the tavern you stop and look back at the horse who is looking at you."

        show fen naked blush at left1
        with dissolve
        Fen "Ummm, thanks for everything Terrance. Next time you're here can I give you another shower? Maybe find a better time or a more private space?"

        "Your ears burn as you know how blunt that sounded but you were pretty sure you knew how the horse was going to reply and you breathe a sigh of relief when he answers."

        Terrance hard smile "Yes, I'd like that a lot. I should be back in a few days."
        
        Terrance "Maybe I'll rent a room for the night and we can really take out time? See where things go?"

        hide fen
        show terrance hard at center1:
            zoom 1.5
            xpos 1300
        show ratio1
        show bg tavernback_blur:
            zoom 1.2
        with dissolve
        "You watch as the horse deliberately strokes his cock, quickly bringing himself to another orgasm, though this time much less cum."
        
        "You feel weak in the knees as you watch the little show Terrance did for you and you quickly dart to your room once he's done."

        scene bg tavernback
        with s_dissolve
        "The horse watches you go and grabs the cup to start cleaning himself before pouring the entire basin over the courtyard floor to clean up the latest mess."
        
        "Watching the water drain away he reaches up and touches the side of his face where you caressed him."

        Terrance "I wonder..."

        stop music fadeout 2.0
        stop sound fadeout 2.0

        scene bg tavernback
        with s_dissolve

        $renpy.end_replay()

        #call bond level up and other stuff

        call bondlvup0202 from _call_bondlvup0202_3

        scene bg black
        with s_dissolve

        call sxp_up from _call_sxp_up_2

        pause

        jump night_start

label terrance_bond_03pre:

    stop music 
    scene bg tavern4
    with dissolve

    "You place the standard meal in front of the big horse who smiles gently at you."

    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Fen "Evening Terrance. How are you tonight?"

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    show terrance smile at right1
    with dissolve
    Terrance "Fine lad. Just finished up me day's work and now just relaxing before I heads back to the farm."

    show fen smile with q_dissolve
    "You return the smile and pause while Terrance begins to eat his food. Your mind wanders to what he said, his farm."
    
    "You realise you don't actually know where he lives or anything his home life and your curiosity is aroused."

    Fen normal "Just wondering, do you live far away?"

    show terrance normal with q_dissolve
    "He pauses to look at you for a moment. Swallowing the mouthful of stew, he shakes his head."

    Terrance "Well, a few hours for me. I might walk faster than ye so take that with a grain o' salt lad. Why ya asking?"

    Fen stern "I just thought about it now. I've not really left the city since I've arrived and honestly..."

    "You pause, running your hand through your mane. Giving the horse a slightly sheepish smile you continue."

    Fen "I kinda want to see what's out there you know? But I don't need to get lost wandering around the countryside."
    
    Fen sweat "My luck I'd fall down a hole or something."

    Terrance "Hmm, well lad... ye could always come back to me farm for a night."
    
    Terrance grin "Give ya a chance to see at least the country I go through. I wouldnae mind the company to be honest."

    "Terrance grins at you and you see a twinkle in his eye. You smile broadly in return."

    show fen grin at shock
    Fen "Really? That's amazing! I'd love to visit your farm!"
    
    Fen normal "Umm, we can go on my day off I guess? I don't want to ask Gunther for any extra time off."

    show terrance at center1  behind fen
    with dissolve
    "The horse laughs and reaches out to tussle the top of your head."

    Terrance normal "I get ya lad. Ya dunnae need the ol' furball giving ya any guff."
    
    Terrance smile "Lemme know when yer next off and I'll come get ya before I head back to me farm. Does that sound good [name]?"

    show fen smile at shock
    Fen "That sounds great!"

    hide fen
    hide terrance
    show bg tavern4
    with dissolve
    "You hear a loud cough from Gunther and grimace. Bidding Terrance goodnight you turn to head off..."

    Terrance "One thing laddy, I only has the one bed..."

    $ terrance_bond_03pre_done = True

    $ ap -= 1

    jump work

label terrance_bond_03:

    play music "audio/etherealwasteland.ogg" volume 1.0 fadein 3.0
    scene bg ruin_pathway
    show image "gui/overlay/game_menu.png"
    show ratio1
    with vs_dissolve
    "You sprint down a crumbling pathway, following after a figure that's just barely within sight."
    
    "You don't know why you're chasing this figure, but you know it's important to catch him."
    
    "Losing sight of them, you begin to panic..."
    
    "You hear your name, someone is calling you."

    "{color=#f5693b}???{/color}" "[name]? [name]? [name]!!"

    show bg ruin_pathway at truecenter:
        zoom 1.5
    show ragnar normal at center1:
        matrixcolor TintMatrix("#000000")
    with dissolve
    "Running towards the voice, you once more see the mysterious figure."
    
    "Just as you're about to reach them, you suddenly collide with what feels like an invisible barrier." with hpunch
    
    hide ragnar
    show bg ruin_pathway:
        zoom 1
    with dissolve
    "You feel yourself shaking as the figure again walks out of view."

    stop music fadeout 3.0
    scene bg black
    with dissolve
    "{color=#f5693b}???{/color}" "[name]! Wake up lad!"

    scene bg fenroom_blur
    with dissolve

    scene bg black
    with dissolve

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    scene bg fenroom_blur at right:
        zoom 2
        ypos 2000
        xpos 2200
    show terrance stern at top:
        zoom 1.5
    with s_dissolve
    "With a start you awake, seeing the massive form of Terrance standing over you. The horse is looking at you with some concern."

    Terrance "Are ye OK lad? You seemed to be having a nightmare or something."

    show bg fenroom_blur:
        xpos 2150
    show terrance:
        xpos 800
    with move

    show bg fenroom_blur:
        xpos 2250
    show terrance:
        xpos 1000
    with move

    show bg fenroom_blur:
        xpos 2200
    show terrance:
        xalign 0.5
    with move
    "Shaking your head to help you gain your sense, you look past the horse to see the sun is just beginning to peek out over the horizon."
    
    "You look around in confusion, wondering why Terrance is in your room."

    show bg fenroom_blur at center:
        zoom 1
    show terrance normal at center1:
        zoom 1
    with dissolve
    Terrance "Sorry to wake ya, but you asked me to get ya on yer day off so you could come to me farm. I'm heading out soon so I thought I should get you."

    Fen "Damn, I kinda forgot... well not really forgot just you know, just waking up."
    
    Fen "Ugh, it's so early. Can't we leave later? The sun's not even up?"

    Terrance stern "Get up ya lazy git. Takes a while to get to me farm and I have some errands I have to run."

    hide terrance
    show bg black
    with dissolve
    "You lay back in bed and pull the covers over your head."
    
    show bg fenroom
    with dissolve
    "Suddenly you feel the covers being pulled off you and you see the horse grinning at you, holding your blankets." with hpunch

    show bg fenroom_blur at truecenter:
        zoom 1.5
    show terrance grin at top:
        zoom 1.5
    with dissolve
    Terrance "Younguns... always sleeping late. Now get dressed and let's go, I can't wait for ye all morning."

    hide terrance
    show bg fenroom:
        zoom 1
    with dissolve
    "Complaining all the while, you roll out of bed and pull on your clothes."
    
    scene bg kitchen
    with dissolve
    "Rubbing your eyes you stumble to the door and down the stairs as Terrance follows you."
    
    "You hear Gunther snoring as you pass his room."

    show fen 2 stern at right1, flip
    show bg kitchen_blur
    with dissolve
    Fen "Gunther has enough sense to stay in bed until after sunrise."

    show terrance normal at left1, flip
    with dissolve
    Terrance "Gunther isn't coming with me on a four hour walk now is he?"

    scene bg tavernback
    with dissolve
    "You don't really have an answer for that, so you just grumble as you make your way to the courtyard where Terrance's cart is."
    
    scene bg cart at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You shiver a bit in the cool morning air as you walk up to the cart. Peering inside, you see a small bundle of food and some jugs of drinks."

    "You also notice, even in your tired state, that the cart is clean and a fresh layer of hay is covering the inside of the cart with a few empty burlap sacks rolled up."
    
    hide ratio1
    show bg tavernback at truecenter:
        zoom 1
    with dissolve
    "Turning around, you are met with a pillow to the face. In your surprise you let it fall to the ground."

    Terrance "Catch! Or don't..."

    Fen "Whatthe?!?" with vpunch

    "You hear the horse laugh and as you pick up the pillow off the ground and dust it off, you see Terrance is holding one of your blankets as well."

    show bg tavernback_blur at truecenter:
        zoom 1.5
    show terrance normal at top:
        zoom 1.5
    with dissolve
    Terrance "I know it's really early lad. Yer not used to getting up at the crack of dawn."
    
    Terrance smile "So I thought ye could have a nap in me cart as I haul it to Mjolnik's. So get in and get comfy."

    scene bg cart
    with dissolve
    "You don't need any more convincing and slowly climb into the cart, stretching out in the hay."
    
    "Breathing deeply, you enjoy the smell of it and feel yourself drifting off as Terrance puts the blanket over you."   
    
    #cart sound
    "Soon, you feel the cart begin to move."

    Fen "So... Who's Mjolnik?"

    Terrance "A good young lad. Farmer who lives near me."
    
    Terrance "I promised to stop by and have a chat and lunch and thought ye wouldnae mind meeting him."

    show bg black
    with dissolve

    show bg cart
    with s_dissolve
    "Between the gentle movement of the cart, the smell of the fresh hay and the warmth of the blanket your eyes grow even heavier."
    
    show bg black
    with s_dissolve

    show bg cart
    with dissolve
    "You hear Terrance begin to sing a song, his voice low and rumbling, like an avalanche going down a mountainside."
    
    stop music fadeout 3.0
    show bg black
    with s_dissolve
    "You try to listen, but the words merge together as you slowly fall asleep again."

    #Transition
    pause 1.0

    pause 1.0

    pause 1.0

    scene bg cart
    with s_dissolve
    "You awaken with a start as you feel a jolt. You sit up, rubbing your eyes and brushing hay out of your fur and clothes."
    
    play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
    show bg village at truecenter:
        zoom 1.5
    show ratio1
    with s_dissolve
    "Stepping out of the cart, you feel the cool, fresh breeze gently brush against your face."

    show bg village at center:
        zoom 1
    hide ratio1
    with s_dissolve
    "You've arrived at a vast farm field. The weather is pleasant, and the wheat gleams beneath the sunlight."

    "You see Terrance walking around the corner of a small house and you roll out of the cart to follow him."

    show bg village at truecenter:
        zoom 1.5
        xpos 500
    with dissolve
    "Rounding the corner your eyes widen as you see who Terrance is talking with. You see a bull."
    
    show mjolnik grin at top:
        zoom 1.5
    show bg village_blur:
        zoom 2
    with dissolve
    "You see a young muscular bull."
    
    #show bulge
    show bg village_blur:
        ypos 500
    show mjolnik:
        ypos -500
    with move
    "You see a young, muscular naked bull!"

    show bg village_blur at truecenter:
        zoom 1.5
        xpos 500
    show terrance smile at left3, flip
    show fen 2 blush at left2
    show mjolnik smile at right1:
        zoom 1.0
    with dissolve
    "As you try to process this, Terrance pulls in close and puts an arm around your shoulder and turns you to directly face the grinning bull."

    Terrance "[name], this is Mjolnik, he's that farmer I told you about."
    
    Terrance "Mjolnik, this is [name]. I told you about him last time we chatted."

    menu:
        "The bull gives you a wide smile and holds out a hand. Do you..."

        "Ignore his nudity completely, it's the polite thing to do right?":

            $ mjolnik_meet = 'ignore'

            show fen 2 normal at center1
            with dissolve
            "Making sure to look Mjolnik straight in the eye, you shake his hand."
            
            "You wince as you feel the strength in his handshake and he then proceeds to pump your entire arm up and down effortlessly as he talks."

            Mjolnik normal "Well, I be right glad to meetcha there [name]! Any friend of Terrance must be a good egg."
            
            Mjolnik grin "Welcome to my farm, hope y'all can stay for lunch?"

            show mjolnik normal
            "Letting your hand go, he looks at you with wide expectant eyes and you nod at him."
            
            "His smile gets even larger and he turns to walk towards the farmhouse."

            Mjolnik smile "Well, c'mon in y'all, there's plenty o vittles ready for us!"

            hide fen
            hide terrance
            hide mjolnik
            show bg village at truecenter:
                zoom 1.5
                xpos 500
            with dissolve
            "As you and Terrance follow him into the house, you can't help but notice that Mjolnik has a very plump, but obviously muscular rump."

        "Discreetly check Mjolnik out, I mean it doesn't hurt to check him out?":

            $ mjolnik_meet = 'check'

            show fen at center1
            with dissolve
            "You shake his hand. You wince as you feel the strength in his handshake and he then proceeds to pump your entire arm up and down effortlessly as he talks."

            Mjolnik normal "Well, I be right glad to meetcha there [name]! Any friend of Terrance must be a good egg."
            
            Mjolnik grin "Welcome to my farm!"

            hide fen
            hide terrance
            show bg village_blur:
                zoom 2.5
            show mjolnik at center1:
                zoom 1.5
                ypos 2000
            with dissolve
            "As he's talking and inadvertently trying to tear your arm out of its socket, you can easily sneak a look at Mjolnik's body."
            
            show mjolnik:
                ypos 1500
            with move
            "Even soft, you can tell he has a large dick and it's paired with a set of rather large balls."

            "The combination of his hairy muscular frame, but boyish enthusiasm is actually quite charming."

            "Due to the vigorous greeting he is giving you, you can't help but notice his junk is swinging back and forth."

            show mjolnik normal:
                ypos 2000
            with move            
            "Suddenly the shaking stops and you quickly look back up into Mjolnik's earnest face. Not knowing what he just said, you simply nod."

            Mjolnik grin "Well that's great! C'mon in y'all, there's plenty o vittles ready for us!"

            hide mjolnik
            show bg village at truecenter:
                zoom 1.5
                xpos 500
            with dissolve
            "As you follow him into the house you sense Terrence is looking at you."
            
            "Turning to face him, you see he has a slight smile and he winks at you, and then gestures towards Mjolnik."
            
            "Turning to face the bull, you can't help but notice that Mjolnik has a very plump, but obviously muscular rump."

        "Look at this hunk o beef!":

            $ mjolnik_meet = 'beef'

            hide terrance
            hide fen
            show bg village_blur:
                zoom 2.5
            show mjolnik at center1:
                zoom 1.5
                ypos 1500
            with dissolve
            "You can't even look at anything else. That thick cock and those massive balls are calling to you."

            "You feel yourself begin to get a bit hard yourself and you manage to at least put your hand out, which Mjolnik takes, shaking it with enthusiasm."

            Mjolnik "Well, I be right glad to meetcha there [name]! Any friend of Terrance must be a good egg."
            
            Mjolnik smile "Welcome to my farm, hope y'all can stay for lunch?"
            
            Mjolnik "Don't be shy though [name], you kin look me in the face, Don't think I'm that ugly."

            Fen "!" with vpunch

            show mjolnik:
                ypos 2000
            with move
            Mjolnik normal "Besides, the ground ain't that interesting."

            show mjolnik smile at center1:
                zoom 1
            show bg village_blur at truecenter:
                zoom 1.5
                xpos 500
            with dissolve           
            "Letting your hand go, he looks at you with wide expectant eyes and you nod at him."
            
            "His smile gets even larger and he turns to walk towards the farmhouse."

            Mjolnik "Well, c'mon in y'all, there's plenty o vittles ready for us!"

            hide mjolnik
            show bg village at truecenter:
                zoom 1.5
                xpos 500
            with dissolve
            "As he turns to walk inside you can't help but stare at his rump."
            
            "It's big and plump but you know it's muscular too. You almost want to just grab it."
            
            "You feel Terrence behind you and hear the deep sigh."

            show terrance normal at left1, flip
            show fen 2 blush at right1
            show bg village_blur
            with dissolve
            Terrance "I get it, he's good looking. Dunnae be so damn obvious."
            
            Terrance smile "Mjolnik's a nice lad, but he's clueless about things regarding anything sexual."

            show fen at flip
            show terrance normal
            with dissolve
            "You turn around to protest but when you see Terrence staring pointedly at the bulge in your pants, you feel yourself blushing."

            Terrance stern "Just dunnae hurt the lad [name]."
            
            Terrance stern "If ye two happen to hit it off in a more... personal way... just be slow and kind? He deserves nothing more."

            "You see that Terrence is very serious and you nod your head."
            
            hide terrance
            hide fen
            show bg village at truecenter:
                zoom 1.5
                xpos 500
            with dissolve            
            "Seeing that he smiles and turns to walk into the farmhouse but whispers to you as he passes."

            Terrance "Aye, he does have a fine arse though."


    scene bg mjolnik_home
    with s_dissolve
    "Following Mjolnik into the farmhouse, you stop and look around."
    
    "The house is very tidy and homely. There's a soft rug covering a lot of the wood floor and some old tapestries on the walls."
    
    "A few chests and cabinets are pushed against the walls. Various bits of furniture fill out the large room."

    show bg mjolnik_kitchen
    with s_dissolve
    "Off to the side there's a small cooking area and it's piled high with fresh vegetables and other food. You also notice a pair of closed doors."

    "You sniff and notice the aroma of many herbs and spices in the air."
    
    "Looking for the source of the smell, you see a rack containing dozens of bottles of various sizes."

    show bg mjolnik_home_blur
    show mjolnik normal at center1
    with dissolve
    Mjolnik "Y'all take a load of yer feet."

    "He gestures to a few chairs around a table and you politely sit down."
    
    hide mjolnik
    show bg mjolnik_home
    with dissolve
    "The bull bustles around the kitchen. Soon he's bringing over plates of food and setting them down in front of you and Terrance."

    Mjolnik "No I ain't no fancy cook, so hope y'all enjoy it."

    #gut growls sound
    "Once you smell the food, your gut growls."
    
    "You remember you didn't have breakfast and that you are ravenous. You dig in with gusto."

    show bg mjolnik_home at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "As you're eating, you can't help but think about the quality of the food. It's done very well, but is plain."
    
    "Mostly cooked vegetables in various forms, homemade bread and bowls of fresh fruit, seeds and berries."
    
    "You can taste that Mjolnik has tried to add some herbs and spices but at best adds one per dish."

    "Regardless, it's very filling and very tasty. Though you can't help but wonder what you could do with it if you had access to the spices you keep smelling."

    show bg mjolnik_home_blur:
        zoom 1
    hide ratio1
    show terrance smile at left1, flip
    show mjolnik smile at right1
    with dissolve
    "After eating, Mjolnik and Terrance get into an intense discussion about the various crops and farming methods and oh god, it's boring..."
    
    "You get up and begin to wander around the room as the other two start arguing about what type of rutabaga would grow the best."
    
    "You roll your eyes and laugh to yourself."

    "You understand it's important, but you mostly are concerned with the food when it's in your kitchen, not when it's in the ground."

    "However, this gives you a wonderful chance to investigate the spice rack."
    
    scene bg mjolnik_kitchen
    with dissolve
    "You go over to it and are pleased to see a lot of the jars are open so you can inspect the contents easily."
    
    "You call out to Mjolnik."

    show fen 2 normal at center1
    show bg mjolnik_kitchen_blur
    with dissolve
    Fen "Sorry to bother, but can I have a look at these spices? They all smell so good."

    Mjolnik "Those? Sure thing. Feel free to sample em too if yer of the mind."
    
    Mjolnik "I grow em meself or get em from the old goat in the village. He's a herbalist. Real sharp one."

    hide fen
    show ratio1
    show bg mjolnik_kitchen at truecenter:
        zoom 1.5
    with dissolve
    "You happily spend the next hour going through every jar. You take samples of all the herbs and spices, even grabbing some food to experiment with."
    
    "While Mjolnik is a pretty basic cook, you're sure with these spices, you could really up your own cooking game. You make a note to find out more about this herbalist as well."
    
    "Suddenly you feel someone standing behind you and looking over your shoulder you see Mjolnik's smiling face."

    hide ratio1
    show bg mjolnik_kitchen_blur:
        zoom 2
    show mjolnik normal at top:
        zoom 1.5
    with dissolve
    Mjolnik "Whatcha doing [name]? Terrance stepped out for a moment to check on some things in the barn."

    "You feel the bull lay his head on your shoulder and you can feel the warmth of his body on your back."

    Fen "Umm... I was just seeing how these spices and herbs can be used in some of the food you made to give it some more flavour"

    Mjolnik smile "No foolin? Whatcha find out?"

    scene bg mjolnik_kitchen_blur
    show fen 2 normal at left1
    show mjolnik normal at right2:
        zoom 1
    with dissolve
    "You grab a spoon and dip it into the stew you've been experimenting with."

    show mjolnik smile at center1
    with dissolve
    #drink sound
    "Holding it out in front of Mjolnik's head, you feel him get even closer to you and he samples it."
    
    show fen 2 blush
    show mjolnik grin at left2 behind fen
    with dissolve
    "You hear a whistle from him and suddenly he hugs you tight."

    show fen 2 blush at shake
    Mjolnik "Ain't that the berries! That's amazing [name]. You must be something of a right proper cook."

    "You feel yourself blushing, but you're not sure if it's from the praise filling your ears, or the pressure against your lower back."
    
    "However you are content to let him keep hugging you, which he does until you hear Terrance call out in a teasing voice."

    show terrance smile at right3
    with dissolve
    Terrance "Let him go Mjolnik, ye gonnae crush the poor lad."

    show fen at flipback
    show mjolnik blush2 at center1
    with dissolve
    "You hear the bull make a slightly embarrassed cough as he lets you go and steps away."
    
    "Adjusting yourself before turning around, you see he has a sheepish expression on his face which to you looks rather adorable."

    show fen 2 normal
    show mjolnik normal at flip
    with dissolve
    Terrance "I shoulda warned ye [name]. Lad's a hugger. He'll squeeze ya to death if ya give him the chance."

    Terrance normal "But we've been here long enough. Should let Mjolnik get back to work and we need to get to my house before too long."
    
    Terrance "I'm going to get the cart ready, you two say goodbye and I'll meet ye outside [name]."

    scene bg mjolnik_kitchen
    with dissolve
    "You see Terrance give you a slight wink before he gives Mjolnik a quick hug and exits."
    
    "The bull turns to look at you."

    #If you ignored his nudity before.
    if mjolnik_meet == 'ignore':

        "Mjolnik, still with that sheepish grin, holds out his hand."

        show bg mjolnik_kitchen_blur at truecenter:
            zoom 1.5
        show mjolnik blush2 at top:
            zoom 1.5
        with dissolve
        Mjolnik "Sorry there [name]. I reckon I do have a habit of hugging folk. I hope y'all didn't mind."

        "You assure him quickly that you didn't and shake his hand goodbye."

        show mjolnik at top:
            ease 1 zoom 1.6
        "Pausing a moment, you pull him in and give him a quick hug yourself, just making sure to keep your lower body away from him."

        Mjolnik normal "Aw, shucks. Guess y'all don't mind. Hope I'll see y'all again [name]. You seem like a right nice sort."

        show mjolnik at top:
            ease 1 zoom 1.5
        "Letting go, you promise him you will visit again and an expression of pure happiness washes over it."
        
        "Seems Mjolnik is the type to wear his heart on his sleeve."

    #If you discretely checked him out.
    if mjolnik_meet == 'check':

        "Mjolnik, still with that sheepish grin, holds out his hand."

        show bg mjolnik_kitchen_blur at truecenter:
            zoom 1.5
        show mjolnik blush2 at top:
            zoom 1.5
        with dissolve
        Mjolnik "Sorry there [name]. I reckon I do have a habit of hugging folk. I hope y'all didn't mind."

        "You assure him quickly that you didn't and shake his hand goodbye."

        show mjolnik at top:
            ease 1 zoom 1.6        
        "Pausing a moment, you pull him in and give him a quick hug yourself. You feel his dick pressing up against you and hope the bull doesn't notice your growing erection."

        Mjolnik normal "Aw, shucks. Guess y'all don't mind. Hope I'll see y'all again [name]. You seem like a right nice sort."

        show mjolnik at top:
            ease 1 zoom 1.5
        "Letting go, you promise him you will visit again and an expression of pure happiness washes over it."
        
        "Seems Mjolnik is the type to wear his heart on his sleeve."
        
        "Thankfully he also seems to be a bit oblivious as he didn't seem to notice you were rock hard."

    #If you awooga'ed him
    if mjolnik_meet == 'beef':

        "Mjolnik, still with that sheepish grin, holds out his hand."

        show bg mjolnik_kitchen_blur at truecenter:
            zoom 1.5
        show mjolnik blush2 at top:
            zoom 1.5
        with dissolve
        Mjolnik "Sorry there [name]. I reckon I do have a habit of hugging folk. I hope y'all didn't mind."

        "You assure him quickly that you didn't and shake his hand goodbye."

        show mjolnik smile at top:
            ease 1 zoom 1.6        
        "Before you let go, he pulls you in for another hug."
        
        "His arms slide behind your back and you feel him rub your back up and down, even going down to rub your rump."

        show mjolnik at truecenter:
            ypos 300
        show ratio1
        with dissolve      
        "You can't help but get hard and you feel your erection pressing against Mjolnik's dick and you feel him starting to get hard himself."

        hide ratio1
        show mjolnik smile at top:
            zoom 1.6
        with dissolve
        Mjolnik "Aw, shucks. Guess y'all don't mind."

        show mjolnik stern with dissolve
        "He gives you a strange look and seems like he's confused about something."
        
        "After a few moments he speaks. You notice his tails are wagging back and forth rapidly, almost getting tangled up with themselves."

        show mjolnik blush2
        Mjolnik "[name], this might sound right strange..."
        
        Mjolnik "But you think we'll ever see each other again? I dunno why, but something about you I just can't figure out."
        
        Mjolnik "I just feel a bit weird but in a good way right? But I know I really do want to see y'all again."

        show mjolnik smile at top:
            ease 1 zoom 1.5
        "Letting go, you promise him you will visit again and an expression of pure happiness washes over it."
        
        "Seems Mjolnik is the type to wear his heart on his sleeve."
        
        "Thankfully he also seems to be a bit oblivious as he didn't seem to notice you were rock hard, even as his own cock is semi-hard."
    
    stop music fadeout 3.0
    scene bg village
    with s_dissolve
    "Wishing him farewell, you leave and meet Terrance by the cart."

    $ mjolnik_bond_ui = True
    call bondlvup1000 from _call_bondlvup1000
    
    #Transition

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    scene bg sky
    with s_dissolve
    "The two of you walk down the road from Mjolnik's, your blanket and pillow being carried by Terrance."
    
    "He informed you that he was leaving his cart at Mjolnik's, so the bull could load it with produce."
    
    "As your walking, Terrance starts to point out various features of the surrounding countryside."

    scene bg forest1
    with s_dissolve
    Terrance "Now, if ya looks over there, you can see the entry to Great Forest. Sure it has some fancy name, but that's all I knows it as."
    
    Terrance "The Herbalist, Eoghann, has a house of the far side of the woods. Nice sort, but a wee bit daft."

    "You pause to look at the woods. In your opinion, they seem a  bit dark and ominous, even from here you can see how thick the tree and underbrush is."
    
    scene bg village at left:
        zoom 3
        ypos 2300
        xpos -1000
    with s_dissolve
    "However as you look past the forest, you see something that catches your eye. Seems to be a large complex of ruins."

    Fen "Hey Terrance, what's that bunch of ruins past the forest there?"

    Terrance "That's the dungeon. I dunnae know what it's really called but all that's there is death and madness."

    "You think back to other folks talking about the dungeon and how a lot of the town seems to be centred around it."

    Fen "It can't be that bad. Seems a lot of folk go there to adventure."

    Terrance "Aye, there be a lot of stupid people in the world."

    scene bg sky
    with s_dissolve
    "You nod a few times and walk along in silence."
    
    "The horse seems a bit troubled and you wonder if what he said is at all true or just rumours and folk tales."

    scene bg terrance_house
    with s_dissolve
    "Soon enough a small farm comes into view and you notice Terrance beginning to smile again."
    
    "He gestures proudly at the farm and the surrounding fields and outbuildings."

    show terrance smile at center1
    show bg terrance_house_blur
    with dissolve
    Terrance "Welcome to me home lad!"
    
    Terrance "It's nae some grand castle or fancy tavern, but it's my home. Built it all myself over the past twenty or so years."

    hide terrance
    show bg terrance_house:
        zoom 2
        xpos 0
        ypos 1500
    with s_dissolve
    "Walking up to the main building, you glance around."
    
    "There seems to be a lot of root vegetables being grown in the fields but not much else."
    
    "You do see a large tangle of various wild berries and a few fruit trees off to the side but none of the leafy veggies or grains you saw at Mjolnik's."

    "You watch as Terrance unlatches the front door and hauls it open."
    
    #door open sounds transition
    scene bg terrance_home
    with s_dissolve
    "The house is just one room. There's a kitchen and dining area off to one side and there's a large table and some wooden chairs next to it."
    
    show bg terrance_home at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "A large comfortable looking chair is sitting by a small fireplace and there are a few chests against the wall."

    "At the back of the room there is a huge bed, covered with blankets and quilts, with a few large overstuffed pillows scattered about."
    
    "However, aside from the bed coverings, the house feels nearly bare and minimal."

    "You hear a slight cough from Terrance and turn to see him shuffling back and forth a bit uncomfortably."

    hide ratio1
    show bg terrance_home_blur:
        zoom 1
    show terrance stern at right1
    with dissolve
    Terrance "Actually, I'm sorry if the place is kinda plain. I'm a simple sort and dunnae need much."
    
    Terrance "Most of what I did have I sent off to me sisters when Ma and Pa moved in with her. They had a much bigger house so they could use the other bits of furniture."

    show fen 2 normal at left1
    with dissolve
    Fen "It's fine. The furnishings don't make the house. The owner does."

    show terrance normal with dissolve
    "You seem Terrance stare at you for a moment before a slight smile comes over his face."
    
    show fen 2 stern with dissolve
    "You do notice the lack of an obvious bathroom and nature is calling."

    Fen "Er... is there a bathroom?"

    show terrance smile
    "Terrance laughs and points out of a window."

    Terrance "Aye lad, there's an outhouse at the far end of the property. Nothing fancy like indoors crappers here."
    
    Terrance normal "And if yer gunna ask about showers, there's a stream that runs through me property. I use that to bathe."

    stop music fadeout 3.0
    "You look at him incredulously and he just smiles and shrugs."
    
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    scene bg sky
    with s_dissolve
    "You excuse yourself and go to find the outhouse, which you easily do."
    
    "You note while using it, that it's well built, clean and even has some carvings on the walls and door."
    
    "There's even a large jug of clean water and some soap which you can use to wash your hands."

    "Stepping outside the outhouse, you decide to explore a little."
    
    #Stream sound
    scene bg stream
    with s_dissolve
    "And you soon find the stream Terrance mentioned."
    
    "You bend down and run your hands through the water and shudder at how chilly it is, even in the midday heat."

    "You also see a place where Terrance has cut into the riverbank and built a stone embankment and steps to sit on while bathing."
    
    "A small wooden hut is there and a quick glance inside reveals towels, brushes, soap and other bathing supplies."

    scene bg flowerfield2
    with s_dissolve
    "You continue to explore and you stop, your jaw drops as you come across a field of flowers."
    
    "If there was a perfect pastoral image, this was it."
    
    "You can't even see the end of this field, just an endless sea of wildflowers of all shapes and colours."
    
    "Taking a few steps into the field, you are overwhelmed with the scents of all of them."

    "You want to stay there for a while longer but realise you've been gone for a long time and should get back to the house."

    scene bg terrance_house_sunset at right:
        zoom 3
        ypos 2200
    with s_dissolve
    "Making your way back to the house, you see smoke coming from the chimney and can hear Terrance singing again."
    
    "You make your way to the door and see the horse busily getting supplies for dinner while singing."
    
    stop music fadeout 3.0
    "You decide to remain quiet and just listen."

    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
    Terrance "🎶Mary Mack's mother's making Mary Mack marry me, My mother's making me marry Mary Mack.🎶"

    Terrance "🎶I'm gonna marry Mary so my Mary will take care O' me, We'll all be feeling merry when I marry Mary Mack.🎶"

    Terrance "🎶Now there's a nice wee lass and her name is Mary Mack, Make no mistake she's the girl I gonna take,🎶"

    Terrance "🎶And a lot of other fella's would get upon her track, but I'm thinkin' they'll have to get up early.🎶"

    "You can't help but be entranced by the horse's singing. His deep voice seems to reverberate off the walls of the house."
    
    "To you it sounds like the very stones of the house are singing."
    
    "He turns around, he notices you and immediately stops singing and you can see a blush forming on his face."

    scene bg terrance_home_night_blur at truecenter:
        zoom 1.5
    show terrance blush4 at top:
        zoom 1.5
    with dissolve
    Terrance "Oh, [name], didnae see ya there. Ummm..."

    Fen "That was amazing! I didn't know you were such an amazing singer!"

    show terrance blush3 with dissolve
    "Terrance runs his hand through his mane and coughs once in embarrassment. Though you see he is smiling."

    Terrance "Really lad? I just tend to sing to meself to help past the time while working or hauling. I didnae think I was any good."

    scene bg terrance_home_night
    with dissolve
    "Before you can answer, he hurriedly changes the topic." 
    
    "Gesturing to the pile of food on the table. It's piled high with vegetables, bread and even a haunch of some kind of meat."
    
    "Terrance reaches over to a shelf and grabs a few jars and places them on the table."

    show terrance normal at center1
    show bg terrance_home_night_blur
    with dissolve
    Terrance "I dunnae have the selection like Mjolnik, but I do have a few spices. Are ye up for making dinner lad? I cannae do half as good a job as ye."

    hide terrance
    show bg terrance_home_night
    with dissolve
    "You smile and nod, eager to see what you can come up with. Terrance goes and sits in the chair by the fireplace while you get to work."
    
    "Again, the fact you have so many spices to work with brings you great satisfaction and you make sure to use as many as you think are needed."

    show bg at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You make a thick and hearty vegetable stew for Terrance and spiced roast for yourself."
    
    "You then decide to make a side salad using all the various other vegetables and greens and top it off with a homemade dressing."

    hide ratio1
    show bg:
        zoom 1
    with dissolve
    "Setting up the table, you lay out all the food and Terrance is soon over, sniffing the air."

    show terrance grin at center1
    show bg terrance_home_night_blur
    with dissolve
    Terrance "That all smells right delicious lad. Heh, I need ye around more often, I eat much better!"

    "He smiles at you and sits at the table. You serve up the food and watch his reactions. To say the horse is enjoying the meal would be an understatement."
    
    "He easily polishes off the giant bowl of stew and even goes through most of the salad, leaving a small serving for you."

    hide terrance
    show bg terrance_home_night
    with dissolve
    "Patting his belly, Terrance leans back and closes his eyes, a contented look on his face."
    
    "You finish up your meal and quickly whisk away the dishes. Finding a basin for washing, you wash the dishes and put them out to dry."
    
    "By the time you're done, Terrance has opened his eyes and is watching you with a smile."

    show terrance normal at center1
    show bg terrance_home_night_blur
    with dissolve
    Terrance "Ya didnae need to do all the cleaning lad. I would have done that."
    
    Terrance "But thanks all the same. Ugh, I dunnae wanna get up, but the chores need to be done before bed."

    "You offer to help with the chores and Terrance laughs."

    Terrance grin "Ye can come for the conversation, but I dunnae think you'll be wanting to toss around the hay bales or be moving the giant rocks I have for the wall I'm building."

    scene bg terrance_house_sunset at right:
        zoom 3
        ypos 2300
    with s_dissolve
    "Going outside you spend the next few hours watching Terrance work."
    
    "You help by moving some of the smaller stones, but you admit the horse was right. You're not strong enough to move some of the larger ones."

    #shake and sounds
    "You watch in a mixture of awe, admiration and arousal as the giant horse easily picks up the larger stones and tosses them to where he wants them." with vpunch
    
    show bg terrance_house_sunset_blur
    show terrance naked smile at center1:
        zoom 1.5
    show ratio1
    with dissolve
    "His muscles straining and flexing as he does so."

    "The fact that Terrance has removed his loincloth during his chores isn't helping your blood pressure any however."
    
    show terrance:
        ypos 2200
    with move
    "Though soon, you can get used to his nakedness and appreciate the lack of shame the giant horse has while he works."
    
    "You idly wonder if Mjolnik might have picked up the habit from Terrance."

    scene bg terrance_house_sunset at right:
        zoom 3
        ypos 2300
    with dissolve 
    "You are broken from your reverie when Terrance calls out to you."

    show terrance naked smile at center1
    show bg terrance_house_sunset
    with dissolve
    Terrance "Ah, that's enough for tonight lad. I'm gunna wash up."
    
    Terrance naked normal "Would ye mind going in the house and finding something for a snack? I think I have some things around that would work."

    scene bg terrance_home_night
    with dissolve
    "You nod and head back to the house."
    
    "Looking around the kitchen, you don't find anything that would qualify as a snack."
    
    show ratio1
    show apple_01 at truecenter:
        zoom 1
    show bg terrance_home_night_blur
    with dissolve
    "You expand your search and by the bed you find a large basket. Inside there is a solitary apple. It seems fresh and is quite large."

    "Thinking about this for a moment, you take the apple and head back to the kitchen area where your mind races."
    
    scene bg terrance_home_night
    with dissolve
    "You think of a sweet sauce you can make from the various spices and suddenly have the idea of baking it."

    "Smiling, you quickly prepare the small stove and whip up the sauce."
    
    "Sampling it, you're pleased to find out it's quite sweet and should pair up nicely with the apple."
    
    "As you cover the apple in the sauce, you note you still have a lot of the sauce left over and make a mental note to try and use it later."

    "Popping it into the stove, you sit back and soon the delicious aroma of hot apple and spices permeates the house."
    
    "You keep an eye on it and when it begins to brown, you take it out and place it on the counter."

    show apple01_01 at truecenter
    show ratio1
    show bg terrance_home_night_blur
    with dissolve
    "You see a small sprig of mint and place it on the apple as garnish."
    
    "Stepping back to admire it, you hear from behind you."

    scene bg terrance_home_night_blur at center1:
        zoom 1.5
    show terrance naked normal at center1:
        zoom 1.5
        ypos 2200
    with dissolve
    Terrance "What the hell did ya make there [name]? It smells..."

    "The horse steps beside you and looks down at the baked apple and you watch as he kneels down to really stare at it for a moment."
    
    show terrance naked smile with dissolve
    "When he stands up and turns to you, he is beaming from ear to ear."

    Fen "I'm sorry, all I could find was this apple. I hope it's enough."

    Terrance naked grin "Well they are me favorite food lad. I try and keep a few around whenever I can."
    
    Terrance naked normal "And what did ye do it it? I cannae even describe how good it smells."

    "He looks at you anxiously and you know he's desperate to eat some."
    
    "Giving him a grin you pick up a knife and cut a large slice off and gingerly pick it up."
    
    "Holding it up in your fingers, you offer it to the horse."
    
    show terrance:
        ease 1 zoom 2 ypos 2700
    "Terrance gives you a raised eyebrow but leans forward and gently takes the slice from your fingers."

    show terrance naked grin
    show sparkle animation 01 as sparkle01:
        zoom 0.7
        xpos 500
        ypos 150
    show sparkle animation 01 as sparkle02:
        zoom 0.8
        xpos 1000
        ypos 50 
    show sparkle animation 01:
        zoom 0.5
        xpos 1150
        ypos 200
    with dissolve
    "You swear Terrance face's light up in absolute delight and the sounds coming from him make you smile."
    
    "You don't need words to know that the baked apple was a hit with the horse."
    
    hide sparkle01
    hide sparkle02
    hide sparkle
    show terrance naked normal
    with dissolve
    "After he swallows, he looks at you with a pleading expression."

    "You quickly slice off another piece and hold it out to him."
    
    show terrance naked smile with dissolve
    "He again takes the apple from your fingers but this time, his tongue licks along your fingers before he gently sucks one of them into his mouth." 

    "You gasp in surprise as he continues to suck on your finger, his eyes closed in absolute bliss."
    
    "You let him continue for a moment before gently pulling your finger loose. Cutting off another slice, you pick it up."

    Fen "Well, someone is definitely enjoying himself. Here's the next piece... Dammit."

    show sweet sauce at center1:
        zoom 2 ypos 2700
    with dissolve
    "You curse as the piece of apple squirts out of your grasp and lands between Terrance's pecs."
    
    show terrance naked normal with dissolve
    "He opens his eyes and looks at you before chuckling."

    Terrance "It's ok lad... but ye just gunna leave that there or...?"

    "The sultry tone in his voice catches you a bit by surprise and you feel yourself blushing."
    
    show sweet sauce at center1:
        ypos 1600
    show terrance at center1:
        ypos 1600
    show ratio1
    with dissolve
    "You glance down and notice that Terrance is already half erect and his cock is getting harder."
    
    "You know immediately what the horse is hinting at."

    #If you decline
    menu:

        "Decline.":
            scene bg terrance_home_night
            with s_dissolve
            "You're sorely tempted to do something. You think back to the shower you gave Terrance and you still don't know how you feel about him."
            
            "Thinking for a moment, you decide that maybe this wouldn't be the best idea and you simply pick up the piece of apple and offer it to Terrance."

            "His eyes open a bit in surprise and you think he is blushing a bit, but he accepts the apple and chews away on it."
            
            "Over the next little while, you feed him the rest of the apple, except for the last slice which he insists you eat."

            "You eat it and while it's barely warm, it's quite tasty and the sauce is perfect."
            
            "Sighing in contentment, you yawn and see Terrance looking at you with what you think is a bit of sadness."

            show terrance naked normal at center1
            show bg terrance_home_night_blur
            with dissolve
            Terrance "It's getting late lad. You take the bed. I'll sleep in me chair by the fire."
            
            Terrance naked smile "And I dunnae want to hear any arguing! I sleep in that old chair most nights anyways."

            hide terrance
            show bg terrance_home_night at truecenter:
                zoom 1.5
            show ratio1
            with s_dissolve
            "You nod sleepily and crawl into the bed, pausing only to remove your shirt and pants."
            
            "Laying down, you find the bed incredibly comfortable and it has a reassuring scent to it."
            
            show bg terrance_home_night_blur
            with dissolve
            "You're barely aware as Terrance pulls a blanket over you and as you drift off to sleep you hear him sing once more."

            #Texts become smaller and smaller
            Terrance "🎶Hush ye, my bairnie, Bonny wee dearie.🎶"

            Terrance"{size=28}🎶Sleep! Come and close the eyes, heavy and wearie.🎶{/size}"

            Terrance"{size=24}🎶Closed are the wearie eyes,rest ye are takin'🎶{/size}"
            
            Terrance"{size=20}🎶Sound be yer sleepin', And bright be yer wakin'🎶{/size}"

            stop music fadeout 3.0
            #Transition
            scene bg black
            with s_dissolve

            play music "audio/etherealwasteland.ogg" volume 1.0 fadein 3.0
            scene bg forest2_night
            with s_dissolve
            "You again find yourself chasing that figure. This time in the dark woods, where you can just see the figure walking ahead of you, always one step ahead."
            
            "No matter how fast you run, the figure remains just out of sight."

            show bg ruins_night
            with dissolve
            "You make a final effort to catch the figure, and break free from the treeline. You see a set of ruins and the figure moving towards them."
            
            show bg web
            with dissolve
            "You step out of the treeline, but get entangled in spider webs and fall to ground, helpless."

            show bg web at truecenter:
                zoom 1.5
            with dissolve            
            "You feel a presence over you and you know it's the spider in the web about to grab you..."

            stop music fadeout 1.0
            scene bg black
            with dissolve
            #Terrance upside down in your face
            Terrance "Get up lad! You went and fell out of the bed."

            play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
            scene bg terrance_home_blur at top:
                zoom 3
            show terrance naked smile at center1:
                xpos 1500
                zoom 2.5
                rotate 210
            with s_dissolve
            "Blinking in confusion you look around and see Terrance standing over you smiling."
            
            "You're on the floor beside his bed, with all his blankets wrapped up around you."

            scene bg terrance_home_blur
            show terrance naked smile at center1
            with s_dissolve
            Terrance "Yer making a habit of having bad dreams eh lad?"
            
            Terrance naked normal "If ye want to talk about them on the way back to Mjolnik's, feel free. Once there you can ride in the cart back to town."

            hide terrance
            show bg terrance_home:
                zoom 1
            with dissolve
            "You nod as you get dressed. Terrance pauses at the door to grab some bread and cheese, which he puts in a haversack and waits for you to follow him."
            
            stop music fadeout 3.0
            scene bg terrance_house
            with s_dissolve
            "Closing the door to his house, he turns and walks down the path and you follow him, deep in thought about the dream."

            call bondlvup0203 from _call_bondlvup0203
            #Maybe exchange this part with Fen traveling animation in future
            scene bg black
            with s_dissolve

            play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
            scene bg fenroom
            with s_dissolve
            "As you return to your room and get dressed for work, you're right on time to start the day."

            jump day_activity_menu

            #END

        "Accept.":

            stop music fadeout 3.0
            "You know what Terrance is hinting at and you're definitely interested."

            $ terrance_bond_03_sex_done = True
            
            label terrance_bond_03_sex:
                hide ratio1
                show bg terrance_home_night_blur at truecenter:
                    zoom 2
                show terrance at top:
                    ypos -300
                    zoom 2
                show sweet sauce at top:
                    ypos -300
                    zoom 2            
                with dissolve
                "You lean forward and pause for just a moment before eating the apple slice right off his chest."
                
                "You note that while the apple is indeed delicious, there is another treat you want to have now."

                play music "audio/Schlop.ogg" volume 1.0 fadein 1.0
                "Seeing some of the sauce running down his broad chest, you begin to lick it up."
                
                show terrance naked blush:
                    ease 1 zoom 2.5 ypos -500
                show sweet sauce:
                    ease 1 zoom 2.5 ypos -500
                "You soon end up moving to get closer to Terrance, who spreads his legs for you and you basically climb into his lap."
                
                "You slide your hands up his sides and nudge his arms up. Terrance obliges with a smile and raises his arms up over his head."

                Terrance "Now what are ye up to lad?"

                "You don't answer with words but with actions."
                
                "With his arms now over his head, the horse's chest is completely wide open to exploring and you do so with gusto."
                
                "Your tongue laps at every curve, your hands run over every muscle and through the thick mat of hair on his chest."
                
                hide sweet sauce with dissolve
                "Soon, you decide to pay attention to his nipples, licking, sucking and gentle nipping each in turn."

                Terrance "Ooo... that's good lad... remind me to return the favour when yer done..."

                "You duly note that request and get back to Terrance's body."
                
                stop music fadeout 3.0
                "Suddenly you remember the apple and smile as an idea comes across your mind."

                show terrance naked blush:
                    ease 1 zoom 2.5 ypos -200         
                "You lean over and slice off another thick chunk of apple. Holding it halfway in your mouth, you lean forward towards Terrance's face."
                
                "Your eyes lock with his and you press the tip of the apple against his muzzle. You give a needy whine and wait to see what he does."

                "You feel his arms lower as he pulls you in close and he opens his mouth to take the other end of the apple."
                
                show terrance naked blush3 with dissolve
                "Slowly he sucks the apple into his mouth, but as he does, pulls you in tighter."
                
                "As the last of the apple is swallowed, you find yourself kissing him."

                "As you continue to kiss Terrance, you feel his hands running up and down your back, before sliding under your shirt."
                
                "Leaning back you break the kiss so he can remove your shirt. As he does, he begins to lick your body, starting at your waist and slowly going up."

                "You shudder as his tongue washes over you, pausing to flick gently over each of your nipples in turn before he turns his attention to your neck."
                
                "You moan as he nibbles and nips at your neck and soon, you're passionately kissing him again."

                show terrance naked blush with dissolve
                Terrance "Told ye I'd return the favour... now shall we move to the bed lad and get comfortable?"

                scene bg terrance_home_night with dissolve
                "You agree and he easily picks you up and carries you to the bed."
                
                "As you pass by the table, you grab the bowl that has the rest of the sweet sauce in it."
                
                show bg terrance_home_night_blur at truecenter:
                    zoom 2.5
                show terrance hard normal at center1:
                    zoom 2
                    xpos 1500
                    ypos 1550
                with dissolve
                "He gently places you down on the bed and stands before you. His massive cock, now fully hard and throbbing, is level with your face."

                "You reach out to grab it and give it a squeeze, marvelling at its thickness."
                
                "You give Terrance a sly grin before grabbing the bowl. You see the horse giving you a puzzled look."

                Terrance "What ye planning there lad?"

                show sweet sauce2 at center1:
                    zoom 2
                    xpos 1500
                    ypos 1550
                with dissolve
                "You reply by carefully tipping a line of the sauce down the length of his cock."
                
                "As he watches you, you put the bowl off to the side and lick your lips. "

                Fen "I didn't get my treat for the night, so I'm going to have it now."

                play music "audio/Schlop.ogg" volume 1.0 fadein 1.0
                "With that you begin to lick Terrance's cock. Starting at the base of the shaft, you let your tongue explore every inch of his cock."
                
                "As you go, you lick off the sauce, savouring the combination of the sweet sauce and Terrance's natural musk."
                
                "In your mind, this is even better than the baked apple."
            
                play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
                "As you go towards the head, you hear Terrance moaning softly in pleasure."

                show terrance hard normal at center1:
                    zoom 2.5 xpos 1800 ypos 1800
                show sweet sauce2 at center1:
                    zoom 2.5 xpos 1800 ypos 1800
                with dissolve      
                "When you get to the very top, you open your mouth wide and manage to engulf the very tip of his dick in your mouth."
                
                "You try to go further, but the sheer size stops you and you feel Terrance rubbing the back of your head."

                Terrance "Don't get too ambitious lad."

                "You nod and concentrate on the now flaring head and the much louder moans from Terrance show you're doing a good job."
                
                stop music fadeout 3.0
                hide sweet sauce2
                show terrance hard blush5 at top:
                    zoom 1.5
                show bg terrance_home_night_blur at truecenter:
                    zoom 1.5
                with dissolve
                "After a few minutes Terrance pulls back and you look up at the now panting horse."

                stop nsfw1 fadeout 3.0
                Terrance "Feel like I'm about to blow lad... I dunnae want to just yet... but now I want another treat."

                hide terrance
                show bg terrance_home_night
                with dissolve
                "He gently pushes you back onto the bed and swiftly removes your pants and underwear."
    

    #CG starts from here
    # CG 00 base version, Fen looking at terrance
    scene terrance cg2 00 at truecenter
    with s_dissolve
    "Easily picking you up, he lays back on the bed and manoeuvres you so that you're directly facing his dick and he has full access to your rump."

    "You hear the horse chuckle and feel him bend over to grab something off the floor."

    #CG 01 zoom on horse cock, fen looking at cock
    scene terrance cg2 01 at right:
        zoom 1.7
        ypos 1800
    with s_dissolve   
    "While he does, you wrap your arm around his cock and nuzzle it against your face while reaching down to fondle his massive balls."

    "You're amazed by just how large Terrance's dick actually is."
        
    "You know you can't get more than an inch or two into your mouth, and just holding it in your hands, you feel the heat radiating from it as it throbs with intensity."

    scene terrance cg2 01 at right:
        zoom 1.7
        ypos 1100
    with move
    "His balls are just as impressive."
    
    "Rolling them around in your hand, you can feel how heavy they are and you've seen the size of the load the horse can shoot."

    #CG 02 fen lick, add sweat, hot ait and breath
    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
    play music "audio/Schlop.ogg" volume 1.0 fadein 1.0
    scene terrance cg2 02 at truecenter
    with s_dissolve
    "Continuing to kiss and lick his shaft you feel him lift up your tail and then a cold sticky substance begins to cover your hole."
        
    "A few seconds later you hear the sound of a bowl clattering on the floor and hear the horse chuckle."

    Terrance "Let's see if yer cake is as tasty as yer baked apple..."

    #Ass on face 1
    play sound "audio/light moan 2.ogg" volume 0.75 loop fadein 3.0
    scene terrance cg2 ass01 at truecenter
    with s_dissolve
    "It is now your turn to moan as you feel Terrance tongue lapping at your hole."
        
    "The sheer gusto to which Terrance is licking, makes you quiver and you find it difficult to do much of anything."

    #CG 03 Zoom on Fen face, pleasur
    scene terrance cg2 03 at right:
        zoom 1.7
        ypos 1700
    with s_dissolve
    Fen "Terrance... this is incredible... umpf..."

    "Your voice trails off as you feel his tongue pushing into you."
        
    "The feelings are some of the most intense you've ever felt. You moan again, louder this time."

    "Soon, you hear Terrance whinny in contentment."

    Terrance "This sauce does make it interesting. What ye say about going a bit further lad?"

    #Full CG 04, Fen licking
    scene terrance cg2 04 at truecenter
    with s_dissolve
    "You moan an assent as you start to against lather the throbbing cock in your hands with kisses and licks."
        
    "Soon, you feel something large prodding at your tight hole and you whimper in anticipation."

    Terrance "Dunnae worry lad, I'll go slow. One finger be enough fer now."

    "As the finger slowly pushes inwards, you feel yourself shuddering."
        
    "You can't help but to whimper and whine in pleasure as Terrance pushes deeper and deeper until you suddenly spasm uncontrollably."
    
    #Full CG 05, Fen licking, pleasur, sweat, hot air
    play sound "audio/light moan 1.ogg" volume 0.5 loop fadein 3.0
    scene terrance cg2 05 at truecenter
    with s_dissolve
    "You feel your thoughts scramble and can do nothing more but pant like you're in heat."

    Terrance "Seems I found something ye like lad. Let's see about teasing ye a wee bit more now."

    "The horse is good to his word. Whatever he's doing feels amazing and you are soon a quivering moaning wreck."
    
    "You feel like you are going to cum at any minute and you whine for release."

    # CG 05 Zoom on Fen face
    scene terrance cg2 05 at right:
        zoom 1.7
        ypos 1700
    with s_dissolve  
    "As you buck your hips, you barely realise that Terrance's mouth has now fully engulfed your rock hard dick."

    "You mindlessly thrust forwards into his warm mouth and then back against that finger and every time you do, another spams rocks your body."
        
    "You feel like you're about to explode and with a howl, you finally do."

    play sound "audio/light climax 1.ogg" volume 1.0
    # CG 06 still zoom Play cum sound
    scene terrance cg2 06 at right:
        zoom 1.7
        ypos 1700
    with s_dissolve
    Fen "Umpf...!" with hpunch

    "Your body shudders and shakes as you orgasm."
    
    "You feel yourself shooting a huge load right down Terrance's throat and you vaguely piece out the horse is himself moaning in pleasure as he swallows every drop."
    
    "As the post orgasm fog begins to lift you feel Terrance's body begin to shake and soon the cock you're still almost mindlessly caressing and licking begins to throb."

    #CG 06 full CG, Full CG, Fen licking, pleasur, sweat, hot air
    play sound "audio/light moan 1.ogg" volume 0.5 loop fadein 3.0
    scene terrance cg2 06 at truecenter
    with s_dissolve
    "Just as you begin to focus on pleasing Terrance, you suddenly feel something poking at your own hole and soon, you're filled again with one of Terrance's massive fingers."

    "Your head spins as you feel him push deep inside you and soon you start whining desperately as every push makes your cock twitch and throb."
        
    "You have no idea what the horse is doing but it's working."
        
    "Even though you just came, you feel another orgasm building up inside you."

    Terrance "Little trick I learned from Gunther, let's see how ye like having yer prostate tickled there lad."
        
    "You can only focus on two things... Terrace's cock in your hand and his finger massaging your insides."
        
    #both cum, cum sounds
    stop music fadeout 1.0
    stop nsfw1 fadeout 1.0
    play vocal1 "audio/deep climax 1.ogg" volume 1.0
    play sound "audio/light climax 1.ogg" volume 1.0
    scene terrance cg2 07 at truecenter
    with s_dissolve
    "With a whimper, you feel yourself unload again, this time all over Terrance."
    
    "You don't know how your able to cum twice in a row but here you are."

    "Through the brain fog, you hear Terrance grunt and you feel his cock jerk out of your hands."
    
    "It begins to shoot a thick load, every pulse sending a shot of his cum splattering on the floor."
        
    "You quickly grab ahold of it and frantically lick the shaft and caress the balls and Terrance unloads."
    
    # After cum
    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
    play sound "audio/light moan 1.ogg" volume 0.5 loop fadein 3.0
    scene terrance cg2 09 at truecenter
    with s_dissolve
    "Eventually he stops and you gently kiss the tip, licking a few stray drops of his cum up."
        
    "You note he has a very earthy taste, a bit odd but not unpleasant."

    $renpy.end_replay()

    #Endreplay here
    stop sound fadeout 2.0
    stop nsfw1 fadeout 2.0
    scene bg terrance_home_night at truecenter:
        zoom 1.5
    show ratio1
    with s_dissolve
    call sxp_up from _call_sxp_up_10
    #Transition
    "You crawl around until you're lying curled up in his arms and give him another kiss on the cheek."
    
    "This ends up being another passionate make out session which lasts for quite awhile."
    
    "Eventually though, Terrance pulls back and gives you a grin."

    play music "audio/Winter Morning.ogg" volume 1.0 fadein 3.0
    scene bg terrance_home_night_blur at left:
        zoom 3
    show terrance naked smile at top:
        zoom 2
    with dissolve
    Terrance "Damn lad. You seemed pent up. But I think we fixed that. Though I need to wipe me floor soon."

    scene bg terrance_home_night at truecenter
    with dissolve
    "You can't help but laugh and roll off the bed. Terrance points to a towel nearby and you grab it and swiftly clean up the rather large pool of cum together."
    
    "Your nose twitches as you smell his scent on the towel."

    Terrance "There's a basket outside, just toss it in that lad. I'll clean it with the rest of me laundry."

    scene bg terrance_home_night at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You quickly toss the towel into the basket and turn back to see Terrance stretching out and patting the bed next to him."
    
    "You happily get back into bed and cuddle into him. He pulls you close and you rest your head on his chest."

    scene bg terrance_home_night_blur at left:
        zoom 3
    show terrance naked smile at top:
        xpos 1300
        ypos -300
        zoom 2
    show fen naked blush2 at top:
        xpos 400
        zoom 2
    show ratio1
    with dissolve

    Fen "Guess you don't mind me sharing a bed with you eh?"

    Terrance "Nae lad, I quite rather ye did if I'm being honest."

    "You idly run your hand through the thick hair on his chest and think of something."

    Fen naked blush4 "You got... frisky awfully fast there. Any reason?"

    "You see a blush forming over the horse's face and you find it rather adorable. Terrance chuckles a bit before replying."

    Terrance "Well... let's just say I have two things that really get me going."
    
    Terrance "Being fed apples in one. I be half wondering if that old cat told you."

    show fen naked blush2 with dissolve
    "You shake your head and smile."

    Fen naked blush2 "Nope. Just kinda worked out. I'll remember that though. You said two. What's the second?"

    hide ratio1
    hide fen
    show terrance naked blush2 at top:
        zoom 2
    with dissolve
    "You see the blush deepen and he even turns his head away from you in embarrassment."

    Terrance "I havenae told anyone about that [name]. Not even Gunther knows. But I'll tell ya if ye really want to know..."

    menu:
        "Maybe another time...":

            show terrance naked blush with dissolve
            "Terance nods and you have the feeling he's actually grateful you didn't ask."
            
            stop music fadeout 3.0
            scene bg black
            with s_dissolve
            "As you slowly drift off to sleep, you wonder what kink he has that made him so embarrassed."

            #Transition

            play music "audio/etherealwasteland.ogg" volume 1.0 fadein 3.0
            scene bg forest2_night
            with s_dissolve
            "You again find yourself chasing that figure."
            
            "This time in the dark woods, where you can just see the figure walking ahead of you, always one step ahead."
            
            "No matter how fast you run, the figure remains just out of sight."

            scene bg ruins_night
            with dissolve
            "You make a final effort to catch the figure, and break free from the treeline. You see a set of ruins and the figure moving towards them."
            
            scene bg web
            with dissolve
            "You step out of the treeline, but get entangled in spider webs and fall to ground, helpless."

            show bg web at truecenter:
                zoom 1.5
            with dissolve            
            "You feel a presence over you and you know it's the spider in the web about to grab you..."

            stop music fadeout 1.0
            scene bg black
            with dissolve
            Terrance "Get up lad! You went and fell out of the bed."

            #Show terrance upside down
            play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
            scene bg terrance_home_blur at top:
                zoom 3
            show terrance naked smile at center1:
                xpos 1500
                zoom 2.5
                rotate 210
            with s_dissolve
            "Blinking in confusion you look around and see Terrance standing over you smiling."
            
            "You're on the floor beside his bed, with all his blankets wrapped up around you."

            scene bg terrance_home_blur
            show terrance naked smile at center1
            with s_dissolve
            Terrance "Yer making a habit of having bad dreams eh lad?"
            
            Terrance naked normal "If ye want to talk about them on the way back to Mjolnik's, feel free. Once there you can ride in the cart back to town."

            Terrance naked smile "All in all, I hope you enjoyed your stay and the 'fun' last night, lad."

            Fen "You bet I do."

            hide terrance
            show bg terrance_home:
                zoom 1
            with dissolve
            "You smiles to him as you get dressed. Terrance pauses at the door to grab some bread and cheese, which he puts in a haversack and waits for you to follow him."
            
            stop music fadeout 3.0
            scene bg terrance_house
            with s_dissolve            
            "Closing the door to his house, he turns and walks down the path and you follow him, deep in thought about the dream."

            call bondlvup0203 from _call_bondlvup0203_1
            #Maybe exchange this part with Fen traveling animation in future
            scene bg black
            with s_dissolve

            play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
            scene bg fenroom
            with s_dissolve
            "As you return to your room and get dressed for work, you're right on time to start the day."

            jump day_activity_menu

        "Tell me more.":

            "The horse sighs and looks at you. His face is the reddest you've ever seen it, but he starts talking."

            Terrance "As ye might know, me and Gunther are close friends who dunnae mind a roll in the hay when we can get away with it."
            
            Terrance naked blush "One night after a hard days work, Gunther was being a frisky kitty and wanted to have some fun but I was tired."

            Terrance "But I didnae want to ruin his night so I agreed. I let him have his way with me and he wanted to try a new position."
            
            Terrance "I lay on me stomach and he got on top and started pounding away at me."

            show terrance naked blush3 with dissolve
            "Terrance grins at you and you feel yourself blushing just a little. You continue to rub his chest while he talks."

            Terrance naked blush3 "I was so damn comfortable and exhausted that I ended up fell asleep."
            
            Terrance "Damn cat never even noticed and he was giving it to me for who knows how long."
            
            Terrance naked blush "Just as he was cumming, he grabbed me mane and that woke me up."

            show terrance naked blush4 with dissolve
            "He turns his head and coughs. You see his hesitation to finish and you pat his chest encouragingly."

            Fen "It's okay Terrance, I get it. So... what happened?"

            Terrance "As he was filling me with his load, I was shaking off the cobwebs but something clicked."
            
            Terrance naked blush3 "I loved the fact he was done all that while I was asleep. I..."
            
            Terrance "I came instantly too."

            "He gives an embarrassed chuckle."

            Terrance naked blush "Gunther thinks it was all his fault I came with nae help. He was right, but not fer the reason he thought."

            Terrance "Ever since then, I think a lot about that scenario but it's hard to do."
            
            Terrance "Most folk think it weird. I mentioned it to Gunther in passing and he was kinda weirded out by it."

            show terrance naked blush2 with dissolve
            "Terrance sighs and looks at you a bit forlornly."

            Terrance "I get it, tis a strange thing to get ya going, but I've managed to have a few more times, mostly with strangers I've nae seen again."
            
            Terrance naked blush "But yeah, that's me other big secret. I love having people use me when I'm asleep."

            "He sighs and gives you a strange look."

            Terrance "I hope ye don't think I'm a freak or something."
            
            Terrance "I dunnae why it turns me on so much. I wish I did so I could explain it but I just dunnae know."

            show terrance naked blush2 at top:
                zoom 2.2
            with dissolve
            "You prop yourself up and give him a quick kiss."
            
            show terrance naked blush at top:
                zoom 2
            with dissolve
            "He seemed a bit startled but seems grateful. You lay your head down on his chest again and think for a moment."

            Fen "I don't know how I feel about it, but I still really like you."
            
            Fen "I'm sure lots of people have kinks and likings I don't think about or even know of."
            
            Fen "I'm not going to judge. You're not hurting anyone."

            "You smile cheekily at him and stick out your tongue."

            Fen "So maybe one day I'll fuck you while you're napping. What would you say to that?"

            show terrance naked blush2 with dissolve
            pause
            show terrance naked blush3 with dissolve
            "He gives you a strange look before smiling."

            Terrance "I'd trust ye to do it lad and I wouldnae complain if ya did. But ye don't have to indulge my fantasies."

            "Terrance yawns and stretches. Seeing the horse yawn makes you realise how tired you are."

            Terrance naked blush "But we should get to bed lad. We can sleep in a bit for a change."
            
            Terrance naked blush3 "Ya dunane need to be at the Flagon till afternoon. If Guther complains, I'll set him straight."

            hide terrance
            show bg terrance_home_night at truecenter:
                zoom 1.5
            show ratio1
            with dissolve
            "He pulls a blanket over the pair of you and soon you hear his gentle snoring."
            
            stop music fadeout 3.0
            "Yawning again, you absently run your hand over his massive chest, pausing only to gentle tweak his nipples, which causes him to snort and whinny in his sleep."

            stop music
            scene bg black
            with s_dissolve
            "Thinking about what he said, you soon drift off to sleep yourself."

            #Transition
            play music "audio/etherealwasteland.ogg" volume 1.0 fadein 3.0
            scene bg forest2_night
            with s_dissolve
            "You again find yourself chasing that figure."
            
            "This time in the dark woods, where you can just see the figure walking ahead of you, always one step ahead."
            
            "No matter how fast you run, the figure remains just out of sight."

            scene bg ruins_night
            with dissolve
            "You make a final effort to catch the figure, and break free from the treeline. You see a set of ruins and the figure moving towards them."
            
            scene bg web
            with dissolve
            "You step out of the treeline, but get entangled in spider webs and fall to the ground, helpless."
            
            show bg web at truecenter:
                zoom 1.5
            with dissolve
            "You feel a presence over you and you know it's the spider in the web about to grab you..."

            play sound "audio/Punch.ogg" volume 1.0
            stop music fadeout 0.5
            show bg terrance_home_night2:
                zoom 1
            "You land out of the bed with a thump, tangled up in the blanket." with vpunch
            
            Fen "Damn... my head..."

            "You curse silently as you fumble to get out of the twisted up quilt and soon manage to get to your feet."
            
            "Tossing the blanket back on the bed, you stop and stare at the sight before you."

            show bg terrance_home_night2_blur at truecenter:
                zoom 1.5
            show ratio1
            with dissolve
            "Terrance is laying there, a peaceful look on his face, his head turned to the side."
            
            "What's gotten your attention is the fact his massive cock is fully erect and is laying against his abs, throbbing in time to his breathing."

            "Going by the look on his face, you imagine the horse is having an erotic dream and you wonder what he might be thinking off."
            
            "As you watch Terrance, you feel your own cock getting fully hard and you absently stroke yourself as you watch him."

            "You pause as you remember what he told you last evening before you went to sleep."
            
            "Your eyes travel down his body and rest on his twitching dick. You wonder if you want to do something to the slumbering giant."

            menu:
                "Let him be.":

                    "While Terrance said he didn't mind someone having sex with him while he was sleeping, you don't know how you feel about it."
                    
                    "You think about it for a while and ultimately, you decide that maybe in the future you'd indulge him, you won't today."

                    "You climb back in bed and cuddle up next to Terrance, who in his sleep pulls you into his side."
                    
                    scene bg black
                    with s_dissolve
                    "Pulling the blanket over you, you drift back to sleep, feeling secure in his arms."

                    pause

                    Terrance "Get up lad! Time to get going!"

                    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
                    show bg terrance_home_blur at top:
                        zoom 1.5
                    show terrance naked smile at top:
                        zoom 1.5
                    with s_dissolve
                    "Blinking in confusion you look around and see Terrance standing over you smiling."

                    scene bg terrance_home_blur
                    show terrance naked smile at center1
                    with s_dissolve
                    Terrance naked normal "Yer making a habit of sleeping late eh lad? I had some interesting dreams last night."
                    
                    Terrance naked smile "If ye want to talk about them on the way back to Mjolnik's, I'd love too. Once there you can ride in the cart back to town."

                    hide terrance
                    show bg terrance_home:
                        zoom 1
                    with dissolve
                    "You nod as you get dressed. Terrance pauses at the door to grab some bread and cheese, which he puts in a haversack and waits for you to follow him."
                    
                    stop music fadeout 3.0
                    scene bg terrance_house
                    with s_dissolve
                    "Closing the door to his house, he turns and walks down the path and you follow him, deep in thought about the dreams, both yours and whatever Terrance has dreamed about."

                    call bondlvup0203 from _call_bondlvup0203_2
                    #Maybe exchange this part with Fen traveling animation in future
                    scene bg black
                    with s_dissolve

                    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
                    scene bg fenroom
                    with s_dissolve
                    "As you return to your room and get dressed for work, you're right on time to start the day."

                    jump day_activity_menu
                    #END

                "Indulge him.":

                    "You look at the slumbering Terrance and think back to what he said to you last night."
                    
                    "Sure, it's a bit strange but he was extremely clear that he was not only OK with it, but that he trusted you if you wanted to do something."

                    "You reach down and stroke your dick, which is already hard."
                    
                    "You walk over to the side of the bed and gently run your hand down his chest and to his dick."
                    
                    "You wrap your hand around it and Terrance moans slightly, shifting to completely on his back, though you notice his head is still turned sideways, his muzzle level with your crotch."

                    "You feel his warm breath on your dick and move even closer to him, the tip of your cock now firmly pressed against his muzzle."
                    
                    play music "audio/Schlop.ogg" volume 1.0 fadein 1.0
                    "Grinning, you slowly push harder and watch your cock slide into Terrance's mouth, while you lean over and begin to lick the tip of his."

                    play sound "audio/light moan 3.ogg" volume 0.5 loop fadein 3.0
                    "At first, you thrust slowly, making sure you don't wake him, but soon realise that he's a fairly heavy sleeper."
                    
                    "And the feeling of his mouth is amazing."
                    
                    "You keep licking the tip of his now iron hard cock, enjoying the feeling of doing something 'wrong', but knowing that's it with his blessing."

                    "Soon, you feel his tongue curling around your dick and wrapping around it."
                    
                    play sound "audio/light moan 3.ogg" volume 1.0 loop fadein 3.0
                    "You leave Terrance dick alone as you thrust harder into his mouth."
                    
                    "Reaching around his head, you grab hold of his mane and use that to drive yourself even deeper into his warm maw."

                    "Soon you feel your orgasm coming on and you use both hands to pull his head as close to you as possible."
                    
                    stop music fadeout 2.0
                    play sound "audio/light climax 1.ogg" volume 1.0
                    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
                    "You heard a muffled, confused grunt from Terrance and as you cum, you see his eyes blink open." with hpunch
                    
                    "You continue to hold his head as you pump a sizable load into his throat and you see his eyes focus on you, and widen in surprise."

                    stop nsfw1 fadeout 3.0
                    play vocal1 "audio/deep climax 2.ogg" volume 0.5
                    "With a loud moan, he body jolts and you feel a blast of something warm against your side." with hpunch
                    
                    "Turning your head, you watch in amazement as Terrance's cock throbs, each pulse sending another wave of cum shooting forth, covering his chest and your side."

                    Fen "Damn..."

                    "Another few spurts and both of you finish."
                    
                    call sxp_up from _call_sxp_up_11

                    "As you pull your cock free of the horse's mouth, he wipes his face and gives you a happy grin."

                    Terrance "I didnae think ye'd ever do it lad. What a way to wake up."

                    Fen "I don't believe you came hands free? This really must do something for you."

                    "Terrance laughs and you see that blush return."

                    Terrance "Umm, aye... it really does lad. It really does."

                    "He pulls you down into a warm albeit sticky embrace and the two of you share a few kisses."
                    
                    "Soon though, Terrance heaves himself out of bed and gives you an 'angry' look."

                    Terrance "Damn yer hide lad, now we both messy. Guess before we get going to Mjolnik's, we'll have to get a bath in the stream."

                    play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
                    show bg terrance_home_blur
                    with s_dissolve
                    "He pulls open the curtain, and the morning sun floods the room."
                    
                    "Time must have flown by while the two of you were at it."

                    "You stick out your tongue at him and grin."

                    Fen "Oh no! How will we manage?"

                    "Terrance's reply is to simply pick you up and sling you over his shoulders like a bag of potatoes."
                    
                    scene bg stream
                    with s_dissolve
                    "Playfully protesting, he carries you to the bathing area as he goes over his plans for the day."
                    
                    stop music fadeout 3.0
                    "Giving him a few more kisses on the cheek, you look forward to the bath and walk home."
                    
                    call bondlvup0203 from _call_bondlvup0203_3
                    #Maybe exchange this part with Fen traveling animation in future
                    scene bg black
                    with s_dissolve

                    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
                    scene bg fenroom
                    with s_dissolve
                    "As you return to your room and get dressed for work, you're right on time to start the day."

                    jump day_activity_menu

label odachi_intro:
    stop music fadeout 3.0
    scene bg tavern4
    with s_dissolve
    "You move up to serve this man whom you saw stride into the tavern armed with a sword at his hip."
    
    show odachi normal at center1
    show bg tavern4_blur
    with s_dissolve
    play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
    "He's dressed in this style of loose-fitting clothing which you don't believe you've ever seen before."
    
    "His physique is incredibly well-defined, which makes him stand out to you even more."
    
    "Up until now, he was just looking absently around, seeming to just be getting a feel about the place."
    
    show odachi normal at center1:
        zoom 1.5
        ypos 2100
    show bg tavern4_blur at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "When you approach within a certain distance of his table, though, his piercing gaze locks eyes with you."
    
    "It makes you suddenly tense up a bit, though you don't know why."
    
    "He doesn't make any effort to start up a conversation with you, so you know you'll be the one who has to."

    hide ratio1
    show bg tavern4_blur:
        zoom 1
    show odachi normal at right1:
        zoom 1
    show fen normal at left1
    with dissolve
    Fen "Oh! Uh, welcome to the Flaming Flagon, sir. Can I help you with anything tonight?"

    "All that you hear is the sound of him exhaling through his nostrils before he twists his body around in the chair he's sitting in."

    "After almost a hard minute of silence between the two of you, he finally answers."

    "???" "Where road going that way?"

    "He waves over at one side of the tavern that you want to believe is East."

    Fen stern "Um, back out of Felda...? I think."

    "Come to think of it, you actually don't yet know the layout of the town you're in, much less the surrounding area."

    "You wouldn't even know if you're a local or from somewhere far away like this man is probably."

    "Despite your halfhearted answer, though, the stranger lets out a grunt in satisfaction."

    "He seems ready to give you his undivided attention, and pridefully points a thumb at himself."

    Odachi "Odachi! I samurai. You know? Sword fighter?"

    "He brings his well-defined arms together into a grip and makes a swinging gesture for you, as if practicing with an invisible blade."

    Fen normal "Nice to meet you, Odachi. My name's [name]. I just started working here recently."

    Fen "I'd love to hear more about just what being a samurai is about. Can I get you anything to drink in the meantime? A mug of beer, maybe?"

    Odachi "Um, Beer...?" 

    "You find it a bit cute how he tries to pronounce the word with two syllables and doesn't sound out the 'r'."

    "A small chuckle barely leaves your muzzle, and you hope he doesn't get the wrong idea like you're making fun of him."

    Odachi "That is drink, yes...?"

    Odachi smile "Okay. Yes, yes. I would like one beer."

    hide odachi
    hide fen
    show bg tavern4
    with dissolve
    "He gives you the coin out of his bag to pay for it, and you return with a chilled mug of the stuff."

    $ bondexp03 += 1
    call bondexpup03 from _call_bondexpup03

    stop music fadeout 3.0

    "Odachi graciously takes it from you using both his hands, giving a subtle bow of his head as he does so."

    $ odachi_bond_ui = True
    call bondlvup0300 from _call_bondlvup0300

    $ show_workday_option('odachi_work_option')
    $ hide_workday_option('odachi_meet_option')

    $ ap -= 1

    jump work

label odachi_serve_01:
    "You serve Odachi the food and drink he ordered."

    "It's always just 'whatever most popular today' plus a beer, so maybe he doesn't know how to ask for anything specific or maybe he just really doesn't mind."

    "When you set it down in front of him, the samurai puts his hands together and says something in another language that you feel are his words of gratitude."

    $ bondexp03 += 1
    call bondexpup03 from _call_bondexpup03_1

    $ ap -= 1

    jump work

label odachi_bond_01:
    stop music fadeout 3.0
    scene bg tavern4
    with dissolve
    "You pass by Odachi's table when he silently raises a hand for you, as though he's politely waiting to be called upon."

    play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
    show odachi normal at right1
    show bg tavern4_blur
    with dissolve
    Odachi "Hello [name], you know any who need work?"

    "You're beginning to notice that his manner of speech is very slow and methodical, like he has to think about everything he says before saying it."
    
    "And now he's asking around for work? Yeah, he definitely seems like he hasn't been around these parts for long."

    show fen stern at left1
    with dissolve
    Fen "Uh, I wouldn't really know. What kind of work are you looking for exactly?"
    
    Fen normal "If you could leave me with some ideas of what to look out for, then I can ask my boss if he has anything for you when he gets the chance."

    "The stranger immediately brightens up at you taking an invested interest in this for him."

    Odachi smile "Sword work! Or strong work! Work for people in need protection. I very good, so long as coins also good." 

    Fen smile "Okay, yeah. I can definitely look into that for you."

    scene bg tavern1
    with s_dissolve
    "You excuse yourself for a moment to go speak with Gunther about it after you wait for him to finish restocking the barrels behind the bar."

    scene bg tavern4_blur
    show fen normal at left1
    show odachi normal at right1
    with s_dissolve
    Fen "Oh, so I asked Gunther if he knew of any work for you."
    
    Fen "Turns out that around these parts, people like you are known as 'sell swords'; freelance muscle with no official insignias or oaths."
    
    Fen "Often travel alone and bounces around from employer to employer who needs to get stuff done and has the pay."
    
    Fen smile "That sounds like you, right?"

    Odachi "Yes. I work alone. Always...It is best life for myself."
    
    Odachi "I only judge there is of my way, of where I came from and what I do and do not do."
    
    Odachi "This very important, because my promise...strong like steel. Not give away easily; not broken easily, either."

    Fen stern "Wow... hmm..."
    
    Fen normal "So you're a romantic at heart, huh Odachi? I'm really glad to see someone like you hang out around this place."
    
    show fen smile at shock
    Fen "Oh! And Gunther also told me to let you know that while he wouldn't really have the kind of work you're looking for..."
    
    Fen "You're always welcome to chat up the other patrons of the tavern and ask them about it whenever it suits you."

    Odachi "Really?"

    Odachi smile "Okay, yes, yes!"
    
    Odachi "I do that soon as I can. Your boss very generous, and you very beautiful male under him. Thank you very much, friend."

    show fen sweat
    "You wonder if you should correct his phrasing to 'man working under him.'"
    
    hide odachi
    with dissolve
    "Before you can, he's already getting up from his table and making his way around the tavern."
    
    show bg tavern2
    hide fen
    with dissolve
    "At some point while continuing your shift, you notice him stride over to the table with three rowdy men to start up a conversation with them."
    
    "So far out of earshot, you can't really make out anything of what they're saying to each other, but not long after, they all get up and leave the Flaming Flagon together."
    
    stop music fadeout 3.0

    "You can't help but worry a little if Odachi will be okay being by himself in that kind of company..."

    call bondlvup0301 from _call_bondlvup0301

    $ ap -= 1

    jump work

label odachi_event_01:
    scene bg tavern3
    with s_dissolve
    stop music fadeout 3.0
    "You're busy cleaning up the mugs and plates after a meal rush, when you pick up on some kind of commotion happening at a table back near the back end of the tavern."
    
    show ratio1
    show bg tavern3 at truecenter:
        zoom 3
    with s_dissolve
    "There seems to be a gathering of rowdy men clad all in dirty, weatherworn, and mismatching clothes, as if they pulled together their outfits from articles they'd found that were left behind by others."
    
    "From what you could make out from as far away as you were, there were three of them. And all three of them sported bodies dominated by fur colored almost as black as pitch..."
    
    "Which gave you the illusion as though there was this fidgeting dark mass present in the room with you when you first spotted them out of the corner of your eye."

    scene bg tavern4_blur at truecenter:
        zoom 1.5
    show khaleb normal at center1:
        ypos 1900
        zoom 1.5
    show ratio1
    with s_dissolve
    play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0
    "Badger" "And then— And then I says to him, 'What the dicks you worried about me knocking up your daughters for?'"
    
    "Badger" "It's your sons you better learn to watch around me!"

    hide khaleb
    show arek smile2 at left1, flip behind ratio1:
        ypos 1750
        zoom 1.5
    show trei normal at right1 behind ratio1:
        ypos 1950
        zoom 1.5
    with s_dissolve
    "The other two break out in laughter loud enough to rattle the walls while passing around a bag of beef jerky that they probably snuck in from outside."

    show trei at shock
    "Hound" "Nah, nah. See, you missed a real golden opportunity for a comeback there, Khaleb."
    
    "Hound" "What you should have told him was, 'Throw me to the wolves and they'll come back pregnant!'"

    "Hyena" "Yeah, throw you to the wolves, and you'll come back a goddamn balloon, Trei."
    
    "Hyena" "Hey, speaking of which, you wanna come to my place sometime...?"

    "The laughter continues, and you decide that it was likely fine for you to let them be by themselves for now."
    
    scene bg tavern4
    with s_dissolve
    stop music fadeout 3.0
    "While they were pretty annoying, they were also the only people in the barroom right now aside from you and a few others."
    
    "You turn your back away from them but make a mental note to keep watch of them every now and then, though, just to see if they start making any trouble."

    show bg tavern4_blur
    show odachi normal at right1
    with dissolve
    play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
    Odachi "[name]."

    show fen normal at left1
    with dissolve
    Fen "Oh, Odachi. Sorry for keeping you waiting."
    
    Fen "What can I serve you?"

    Odachi smile "Beer, I will like."

    Fen "Alright, beer is on the way."

    hide odachi
    hide fen
    show bg tavern4
    with dissolve
    "After serving the beer, you and odachi chattes for a while. He seems to be in a good mood."

    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Fen "Did something good happen? You look really happy."

    play sound "audio/drink.ogg" volume 2.0
    "He drinks the beer in one gulp and looks at you with excitement in his eyes."

    show odachi smile at right1
    with dissolve
    Odachi "I now have work, that have good coins."
    
    Odachi "Now, get me more beer would you? This beer drink, is really good."

    Fen smile "That sounds great! I'll be right back with your orders."

    $ bondexp03 += 1
    call bondexpup03 from _call_bondexpup03_2

    stop music fadeout 3.0

    hide fen
    hide odachi
    show bg tavern4
    with dissolve
    "Things seem to be working out for Odachi, and it sounds like he will keep visiting here in the foreseeable future."

    $ ap -= 1

    jump work

label odachi_talk_01:

    #If else depends on Bond level
    #If else debends on Odachi had band or not

    stop music fadeout 3.0

    scene bg tavern4_blur
    show odachi normal at center1
    with s_dissolve

    play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
    Odachi "Hello, [name]. You working hard today? That very good for you, keeping busy."

    menu:
        "So, where are you from exactly?":
            jump about_odachi_home
                       
        "That sword of yours is so beautiful...":
            jump about_odachi_katana  

        "Don't you have any friends to come drinking with?":
            jump about_odachi_friends

    label about_odachi_home:
        show odachi smile
        with dissolve
        "Odachi smiles warmly when you ask him this, as though he's fallen back a little into reminiscing."

        Odachi "Place that must be like End of the world for people here. It a place by the sea."
                
        Odachi "Sea much warmer than here."
                
        Odachi "Water there is sparkling and clear, like one you serve me in glass."
                
        Odachi "I would be honored to show you one day, if can [name]."

        $ bondexp03 += 1
        call bondexpup03 from _call_bondexpup03_3

        Fen "By the sea... I like the idea of that."

        #Fen think
        stop music fadeout 3.0
        Fen "Before I can travel, I have to remember where my home is."

        $ ap -= 1

        jump work

    label about_odachi_katana:
        Odachi "Katana? Yes, thank you for notice."
        
        Odachi "Not easy to find best oil to maintain it in this land, but I do good for it with what I can find as replacement for that and powder."
        
        Fen "Oh, You take such good care of it. Is it a very important weapon?"

        Odachi "It kept me safe on many dangerous roads, fights inside other taverns much, much worse than here, and I could not trade for anything."

        Fen "Well, I'm glad it don't look like you're going to pull it out here."

        Fen "I mean... please don't do that."

        $ bondexp03 += 1
        call bondexpup03 from _call_bondexpup03_4

        stop music fadeout 3.0
        Odachi "Understood."

        $ ap -= 1

        jump work

    label about_odachi_friends:
        Odachi "Friends...? ...No. Not friends as you probably mean."

        Odachi "I have may good people I meet. Big-hearted people like you who show to me kindness."
            
        Odachi "But no, not true friends. Not people who walk same path in life next to me."

        Fen "Oh, man. That must feel really lonely for you at least sometimes, I'll bet."

        Odachi "Not really, no. I have my own way, and it needs for me be alone."
            
        Odachi "I am free to do with it what I wish. It is peaceful, when I am not fighting; it is focused."
            
        Odachi "There is no fear or dangers more than what concerns me."

        $ bondexp03 += 1
        call bondexpup03 from _call_bondexpup03_5
        
        stop music fadeout 3.0
        Odachi smile "I thank you for asking to me this question, [name]. It is very kind of you."
            
        Fen "..."

        Fen "Thank you too, Odachi."

        $ ap -= 1

        jump work
    
label odachi_bond_02:

    scene bg tavern3
    with s_dissolve
    stop music fadeout 3.0
    "While serving guests, you spot those three punks all get up from the table where they usually lurk."
    
    "They move up from the back of the tavern and start going over to where Odachi is sitting alone."
    
    "You grow worried by this, wondering if maybe he'd accidentally gotten himself into some kind of trouble with them since that one time you saw him leave the Flaming Flagon in their company."
    
    "You find a moment after you're done serving the other tables to go over to an empty one a bit closer to where they are and pretend to start cleaning it as you try to listen in."

    "It's not easy for you to eavesdrop on exactly what is they're whispering about to each other with the tavern being as bustling as it is right now."
    
    "But you do manage to make out a few snips of it every now and again"

    $ show_workday_option('khaleb_work_option')

label odachi_bond_02a:
    show bg tavern4_blur
    show khaleb normal at right1
    show odachi normal at left1, flip
    with s_dissolve
    play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0
    "Badger" "...Am I really supposed to believe you can outlast me, Fancy Pants...?"
    
    "Badger" "Well, maybe you better think on that again, cause you've got no idea how hard at it I can go once I get going..."

    Odachi smile "...Haha. Yes, I took on more and meaner than what you describe before, and still walk away no problem."
    
    Odachi "You need not fear of holding any back..."

    show trei normal at right3
    with dissolve
    "Hound" "...Damn, guys. I think he's serious. Ba-haha!"
    
    "Hound" "Poor bastard doesn't even know he's gonna end up face down on the ground, passed out, and soaked in a big, messy puddle of himself before I'm even done."
    
    "Hound" "Haha! Aw, I can't wait...!"

    hide trei
    hide odachi
    hide khaleb
    show bg tavern3
    with s_dissolve
    stop music fadeout 3.0
    "Overhearing this only makes your concern grow worse."
    
    "From what it sounds like to you, Odachi might have done something to anger those thugs, and now they're trying to goad him into a dangerous fight against all of them at once!"
    
    show bg tavern2
    with dissolve
    play music "audio/Stoneheart.ogg" volume 2.0 fadein 3.0
    "In a subtle panic, you turn your head around the barroom to look for Gunther to intervene, but he seems to be nowhere in sight right now."
    
    show bg tavern3
    with dissolve
    "As you're about to walk into the kitchen to go searching for him, you look back worriedly at Odachi's table one more time and see that all four of them are now gone."
    
    "Darting your eyes around, you only notice one thing: the hound's barbed, whip-like tail flicking before it leaves out the tavern's front door."
    
    "The panic setting in has now made your pulse rapid and your breathing unsteady."
    
    "There's no time to go get help, you realize. Your friend might need you beside him right now!"

    "You follow out into the town at a hurried pace."
    
    scene bg tavernfront_night
    with s_dissolve
    "You see nothing but the dark haze of the night broken up by a few lights from distant windows, and hear nothing aside from the clamor of the tavern behind you."
    
    "Left at a loss for what to do, you decide to just pick a random direction and start sprinting down it as far as you feel you should."
    
    scene bg townstreet_night
    with s_dissolve
    "You turn corners whenever it feels right in an attempt to make a one-canine sweep of the surrounding area, but eventually, you start to feel like what you're doing here might be aimless."

    "That is, until you hear someone's cry echo out of an unlit, narrow alley nearby."

    Odachi "Aaah-haaaah! Ohh! Ooooohh!"

    "That was Odachi's voice! You were almost sure of it. And it sounds like he might be in a great deal of pain."

    "As much as you want to run straight into the alley to reach him as fast as possible, you realize that might not be such a good idea."
    
    scene bg alley1_night
    with s_dissolve
    stop music fadeout 3.0
    "So instead, you elect to sneak your way through as best as you can, using the half-broken crates and rotting barrels discarded in the alley as cover."
    
    scene bg black
    with s_dissolve
    "Darkness fully envelopes you now, so much that you have to carefully feel your way forward past the debris to continue."
    
    "But the voices do grow louder the further you go."

    Odachi "Stop! Stop it, please! I-It is not right!"

    "Badger" "Oh, well. See, I knew you were all talk before, but this is just pathetic..."

    Odachi "You—you suppose to make wet it first!"

    "Badger" "Ugh...really? Ain't you guys with a water affinity supposed to make it happen whenever you want?"
    
    "Badger" "But yeah, fine, okay. I'll give you a hand, cuz I'm so nice."
    
    "Badger" "Yo, Trei! Mind setting up the mood lights so I can see what I'm doing here?"

    Trei "Oh! Yeah, yeah. Good idea Khaleb."
    
    Trei "I've been meaning to use those candles we swiped from that hotel on High Street whenever we got a chance."
    
    Trei "One sec..."

    scene bg alley2_night
    with s_dissolve
    "The hound snaps his fingers to ignite a bunch of bath candles with sharp, white flames one by one before placing them on some barrels nearby."
    
    "Their strangely intense glow floods that section of the alleyway, making clear to you every detail of what was going on up ahead."
    
    scene odachi cg1 01
    with s_dissolve
    "And once your eyes finished adjusting enough to register what you were seeing, it made you stunned to discover how wrong you were about the whole situation."

    "Odachi was bent over on his hands and knees with the exotic, loose-fitting pants you normally see him wear crumpled in a pile on the ground next to him."
    
    "He was baring his powerful, battle-hardened legs and plump ass, the view of which was always obstructed for you by his tail, now out for the large badger behind him."
    
    "His exposed cock was buried halfway into Odachi's rear while using two fingers to keep the back part of his fundoshi out of the way, pressed to the side up against his butt cheek."

    "You get the very strong impression that maybe you shouldn't be here..."

    menu:
        "What to do..."

        "Turn around and go back to the tavern.":
            
            scene bg alley2_night
            with s_dissolve
            "Now that you understand what a mistake you made reading into the situation, you figure it's probably for the best to respect their privacy."
            
            "If you stay like this, there's probably a good chance that one of them might catch you peeping."

            scene bg townstreet_night
            with s_dissolve
            "You manage to creep your way back out of the alley and start walking along the main roads to try and find your way back to the tavern."
            
            "Gunther would be expecting you to stand on shift very soon for when the night rush begins, and you wouldn't want to leave him all alone to deal with it."
            
            "Still, you just can't seem to get that whole thing you witnessed back there in the alley out of your head the entire journey back."
            
            "Maybe you should ask Odachi about it the next time you see him?"

            $renpy.end_replay()

            $ odachi_tailservice_seen = True
            $ odachi_bond_02_done = True
            #Flag Not seen odachi tail service

            $ ap -= 1

            jump work_end


        "Stay hidden and watch what happens.":

            #Flag seen Odachi tail service
            "Your curiosity wins over any other instinct, and you figure it might be alright to hang back and watch how this continues."
            
            "Though you feel only now like you're starting to understand who your friend was beyond just a regular at the tavern..."
            
            "You still couldn't have dreamt that you'd ever be seeing something like this from him..."

            Khaleb "Shit, Arek. I gotta leave it to you to find the dingiest place possible for us to have our little get-together..."

            Arek "Hey, bro. Don't blame me. You were the one who said to go find someplace real discreet, and I delivered."

            Khaleb "Meh...details."

            scene bg alley2_night
            with s_dissolve
            "You watch as Khaleb gently pulls out before throwing back his head."
            
            play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
            "He gathers up the saliva in his throat and comes forward, hocking up a loogie that dribbles down his lips and seeps right into Odachi's wide-open crack."
            
            "Your friend shudders visibly in disgust as he feels it, and even more so when Khaleb follows this by using a finger to push the spit even further up inside his anus."

            stop music fadeout 1.0
            Khaleb "Alrighty! Bitch looks like she's ready now. How 'bout it, Baby Girl? You ready to take on all three of us like you said...?"

            "Odachi's tone and posture seem nothing less than composed to you and maybe even a little determined, which you can't help but find baffling given the position he's in."

            Odachi "Y-Yes! I full ready now. All of you, give me your at on—Aaaagh!"

            #Thrust 1
            scene odachi cg1 02
            with s_dissolve
            "Without letting him finish his answer, Khaleb rams the full length of his cock back into Odachi's rear."
            
            #animation
            scene odachi cg1 03
            with s_dissolve
            play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
            play fuck "audio/fuck mid 1.ogg" volume 1.0
            play ball "audio/ball hits 1.ogg" volume 2.0
            "He starts thrusting into it with careless, buck wild abandon."
            
            "Meanwhile, the other two get to undressing themselves."
            
            #Change over to the other 2 character's naked spirit
            scene bg alley2_night_blur
            show arek hard grin at right1:
                zoom 1.5
            show trei hard normal at left1, flip:
                zoom 1.5
            show ratio1
            with s_dissolve
            "Now, bare naked from the waste down, they both approach the swordsman from the other end, each already sporting an erection."
            
            "They pause and linger there for a moment in front of him, staring at each other, as if unsure of how to decide who gets what."

            scene odachi cg1 03
            with s_dissolve
            Khaleb "Oh, for the luva—! Do I really gotta teach you two nimrods how to share jizz buckets, too!?!"
            
            Khaleb "Arek, you grab his throat. Trei, move over to the side and get that hand working."

            # see dick
            scene odachi cg1 04 at top:
                zoom 1.5
                xpos 500
            with s_dissolve
            "They both motion to do what he says, and you see Odachi adjust his position to accommodate them."
            
            # eat dick
            scene odachi cg1 05 at top:
                zoom 1.5
                xpos 500
            with s_dissolve
            play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
            play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
            play fuck "audio/fuck mid 1.ogg" volume 1.0
            play ball "audio/ball hits 1.ogg" volume 2.0
            "After giving it a few probing licks, he wraps the length of the hyena's rod around his lips and slowly sucks it down his throat."
            
            "At around the same time, he brings a hand up to grab the hound's long, red cock."
            
            "With thumb pressed against the underside of it where the shaft and glans connect, and begins stroking it."
            
            play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
            play fuck "audio/fuck fast 1.ogg" volume 1.0
            play ball "audio/ball hits 2.ogg" volume 2.0
            #with sweat with cock in mouth
            scene odachi cg1 06
            with s_dissolve
            "As they all work to establish a rhythm to their sexual act, you can see that the motions of it are being dominated by the badger, who is going to town on Odachi's freshy moistened ass."
            
            "His thrusts are so violent and so deep that you notice he's causing your friend's butt muscles to tense up every time he pushes in."
            
            "When flexing like that, his glute muscles look just as rock solid and tightly packed as the rest of him."
            
            "And you realize it's making you tent up in your pants quite a bit..."
            
            #transparent
            scene odachi cg1 07
            with s_dissolve
            Khaleb "Oooh! Bitch is tight! You guys won't believe how hard he's clamping on my dick down here when I pull back!"
            
            Khaleb "How're you two doing? Is it a vibe or a dive?"

            Arek "Ah, fuck, dude! It feels so tight up here, too! I-It's like he's gobbling me up like I'm a whole-ass meal. Aw, and he's huffing my crotch, too!"

            "Intermixed with the squelching sounds of Arek's member being pushed in and out of his throat..."
            
            "...you can indeed also make out what seems to be Odachi breathing in deep through his nose whenever his snout makes contact with the hyena's pubic fur."
            
            "Amazingly, he's not only keeping up with the task of dividing his attention enough to please three men at once..."
            
            "...but is also making sure to savor the experience himself with as many different senses as he can!"

            Trei "Yeah? W-Well—Umph!—Well, I'm not sure I'm satisfied with just this."

            "Even though he says that, it's plain to see that the hound is practically melting from the vigorous handjob he's getting."

            Trei "Yeah, that's right. I want something more...More like what he's keeping from us under there!"

            #zoom on bulge
            scene odachi cg1 08 at center:
                zoom 2
            with s_dissolve
            "He leans down and grabs at the heavy bulge formed in Odachi's fundoshi."

            Trei "What's the deal with that fancy underwear, huh? Looks like it's just getting in my way!"

            "With a devious smirk, Trei snaps his fingers again to create another white flame at his fingertips and holds it up to the fundoshi."
            
            #zoom fundoshi out
            scene odachi cg1 09 at center:
                zoom 2
            with s_dissolve
            "The side of the undergarment singes until the rest of it comes undone and falls to the ground."
            
            "With their confines broken, the samurai's balls are now free to hang low, while his dick rises up to greet the cool night air, exposed."

            "The hound wastes no time in getting himself down low enough to the ground to be face to face with Odachi's glossy, dark cockhead."
            
            #zoom cock in mouth
            scene odachi cg1 10a
            with s_dissolve
            "Then, tongue curled around the shaft, he slides it into his maw and starts giving fellatio."
            
            "He uses one hand to keep Odachi's cock and balls held in place where he wants them while also twisting his own nipple to self-stimulate with the other."

            #zoom out, animation
            scene odachi cg1 10
            with s_dissolve
            Arek "Greedy bastard. I wanted to be the one who unwraps the package..."

            Khaleb "Mmph! Mmph!! Aaahh!"
            
            Khaleb "Trei! Trei, ease up a little down there, would ya?"
            
            Khaleb "I think you're making him squeeze too hard around me."
            
            Khaleb "I-I think I'm already gonna—Mmmph! Mmmmmm...!"
            
            play vocal1 "audio/deep climax 1.ogg" volume 1.0
            stop nsfw1 fadeout 3.0
            stop fuck fadeout 3.0
            stop ball fadeout 3.0
            Khaleb "Hhooooooohh!!!"

            #Khaleb cum
            scene odachi cg1 11
            with s_dissolve
            "The badger's reckless excitement drives him unexpectedly into a point of overwhelm."
            
            "And now that he's hit that point, he just can't seem to stop his body from making him shoot all of his thick, pent-up load straight into Odachi's innards."
            
            "His futile attempt at resisting the orgasm is marked by spasms and him furiously slapping the samurai's ass."
            
            "Khaleb then starts to look a little fatigued coming down from it."

            #After Khaleb cum
            scene odachi cg1 12
            with s_dissolve
            Khaleb "Oh, shit...Oh, shit...Fuck, that was intense...Damn. I wanted to go for more, though. Eh, next time."
            
            Khaleb "Nice job, Blue Boy. You've earned your pay."

            stop music fadeout 3.0
            scene bg alley2_night
            with s_dissolve
            "With one final slap on the rear, he pulls out and gets back on his feet."

            show odachi hard normal at right1
            show bg alley2_night_blur
            with dissolve
            Odachi "One moment, sir."

            "Odachi stops what he's doing with the other two to speak."

            Odachi "If you finish, then what I should do with your friends? You said you pay for three to make happy, no?"

            show khaleb naked normal at left1, flip
            with dissolve
            "The badger smirks while his two lackeys exchange puzzled looks between each other."

            Khaleb "Heh. Oh, don't worry. I wasn't planning on leaving before I made sure you took good care of my bros."
            
            Khaleb naked smile "But how's about I make you an extra offer, Smart Guy?"
            
            Khaleb naked normal "Since you obviously care about doing good work and all."
            
            Khaleb "I want you to be the one to top each of my guys: one after the other, give 'em all you got to make 'em feel special."
            
            Khaleb "You got me? And for each one I hear howl up at the moon when cumming, I'll toss in an extra ten coins for your pay. Sound good?"

            Odachi "Yes, I do that."

            "What Odachi really thinks of the proposal remains a mystery to you, as his expression remains an unwavering mask of obedience."

            Khaleb "And what do you guys say? Up to find out what this guy's swordsmanship is firsthand?"

            hide odachi
            hide khaleb
            show bg alley2_night
            with dissolve
            "The hyena is quick and eager to respond."

            show bg alley2_night_blur
            show arek hard smile at center1
            with dissolve
            Arek "Yeah, yeah! Me first, though!"
            
            Arek hard grin "Come on, Sweet Lips, get on up. I ain't got all day."
            
            Arek "Hehe, don't think for a sec, though, that it's gonna be easy to make me beg..."

            show bg alley2_night
            hide arek
            with dissolve
            "Odachi silently rises to his feet."
            
            "He appears to loom stoically for a moment within Arek's personal space, locking eyes with him."
            
            "You can see that the hyena is growing a bit timid, having the samurai's piercing gaze aimed squarely at him."

            "Then suddenly, Odachi pulls a maneuver so lightning fast your brain barely registers it before it's over."
            
            "Before you know it, he's got Arek lifted off the ground by his legs." with vpunch
            
            "Not a second after the thug lets out a yelp in surprise, he's being moved over to one side of the alley where Odachi pins him against the wall by his back."
            
            show ratio1
            show bg alley2_night_blur at truecenter:
                zoom 1.5
            with s_dissolve
            "He takes advantage of his partner's maw hanging open in utter shock to bring him in for a long, messy kiss.  While his arms, keeping him suspended..."
            
            show odachi hard normal at center1, flip behind ratio1:
                zoom 2
                ypos 1700
            with s_dissolve
            "... work down below to position his cock at just the right angle in between Arek's spread apart legs."

            "With it leaking ample pre from the fucking he had gotten just before, Odachi's dick presses fairly easily into Arek's quivering hole."
            
            play fuck "audio/fuck fast 1.ogg" volume 1.0
            play ball "audio/ball hits 2.ogg" volume 2.0
            hide odachi
            show arek naked blush2 at top behind ratio1:
                zoom 2
            with s_dissolve
            "The hyena shuts his eyes in prideful defiance of the pleasure he feels when the thrusting starts."
            
            "Odachi knows just how to keep it interesting by alternating between slow, deep motions and shallow, rapid ones."
            
            "And all the while, their tongues grapple and massage one another."

            scene bg alley2_night_blur
            show khaleb hard smile at right1
            show trei hard normal at left1, flip
            with s_dissolve
            Khaleb "Woo! Yeah, get it, Arek! You look fucking hot like that!"
            
            Khaleb hard grin "Guess I know now just how I'm gonna knock you up one of these days. Hehe..."

            "The other two have gathered around this spectacle, absentmindedly continuing to stroke themselves as it unfolds."

            scene bg alley2_night_blur at truecenter:
                zoom 1.5
            show arek naked blush2 at top:
                zoom 2
            show ratio1
            with s_dissolve
            "Just as Arek seems to think he's found a way to shut out the sensations enough to not completely lose it..."
            
            "Odachi surprises him yet again by breaking the kiss to instead bury his snout right in the hyena's chest."
            
            "What begins as simply nuzzling and breathing in the musky scent of his partner's fluff quickly turns into a flurry of brief but firm kisses all across his pecs."
            
            "Odachi maintains the steady rhythm of fucking his ass throughout. And after a minute of all this sensation passes, Arek finally gives in to him."

            stop fuck fadeout 3.0
            stop ball fadeout 3.0
            show arek naked blush3
            Arek "Awoooooooohh!!" with vpunch

            "The hyena throws his burly arms around Odachi's neck and howls as he cums all over his own stomach."
            
            "At the same time, you only barely make out your friend letting out a short grunt as he fills his partner's needy asshole with his own seed."
            
            scene bg alley2_night
            with s_dissolve
            "And as he widens his stance to get all the ejaculate out, you can't help but notice that some of what's left over from the badger's half dried load is dripping out from the samurai's rear."

            show bg alley2_night_blur
            show odachi hard normal at left1, flip
            with dissolve
            Odachi "Hhm. That is half extra I get. And now for the other."

            "No sooner than Odachi lowers the thug down against the alley wall to bask in the afterglow of their session, does he turn around and move towards the other one."
            
            "Despite having just come, his dick still looks full hard, eagerly ready to go another round."

            show trei hard sweat at right1
            with dissolve
            Trei "Whoa, whoa, whoa! Hold on, buddy. You and I are gonna need to talk about this first."
            
            show odachi at center1
            with dissolve
            Trei "cuz I don't exactly fancy myself a givin'-in-the-reins kinda guy, ya feel me—"
            
            show odachi at right2
            with dissolve
            show trei at shock
            Trei "-Aaah!"

            hide odachi
            hide trei
            show ratio1
            show bg alley2_night at truecenter:
                zoom 1.5
            with dissolve
            "With that same deft maneuvering, Odachi throws the other thug to the ground on his side, letting himself fall with him, as he twists the hound's arm tight behind his back."
            
            play fuck "audio/fuck fast 1.ogg" volume 1.0
            play ball "audio/ball hits 2.ogg" volume 2.0
            show trei hard blush2 at top behind ratio1:
                zoom 2
            show bg alley2_night_blur
            with dissolve
            "His partner thrashes and squirms while he tries to get into the proper position, and eventually he finds just the right opening to slip in and start pounding away with the same methodical technique."
            
            "It looks not quite as easy to pull off from an almost lounging position while essentially restraining his partner..."
            
            "...but you can see from how stiffly Trei's rod is bobbing that it's still got to be doing something for him."

            scene bg alley2_night_blur
            show khaleb hard normal at center1
            with dissolve
            Khaleb "Fuck, Trei. Get a load of you! You're not even trying to save me some pocket change."
            
            Khaleb "I mean, the least you could do is not look so damn thrilled to be getting Arek's and my sloppy seconds..."

            Trei "F-F-Fuck, yooouu...He—He's in me so—sooohh..."

            "The hound lets his tongue roll out the side of his mouth as he gives in to the attentively dominating warrior forcing him to receive pleasure with even less resistance than the one before."

            Khaleb "Psst! Hey, Blue Boy! The horns! Get him by the horns; he loves it."

            hide khaleb
            show ratio1
            show bg alley2_night at truecenter:
                zoom 1.5
            with dissolve
            "Odachi follows this as though it were an instruction, rolls the hound over onto his belly, and grabs hold of his fierce, slender horns as if they were a pair of handlebars."
            
            "He then plunges his dick hard into his partner's ass while at the same time reeling him into a backbend."
            
            "For a good moment, the hound's body appears frozen like that, in the throes of pain and ecstasy. That is, until he starts feeling it about to come out."

            show trei hard blush2 at top behind ratio1:
                zoom 2
            show bg alley2_night_blur
            with dissolve
            Trei "Ah! Agh—Ahh! A-Awoooooooohhhh!!!"

            stop nsfw1 fadeout 3.0
            stop fuck fadeout 3.0
            stop ball fadeout 3.0
            hide trei
            show ratio1
            show bg alley2_night at truecenter:
                zoom 1.5
            with dissolve
            "Trei's cock oozes out cum in a puddle underneath him, each pulse of it happening in time with his breath."
            
            "A few seconds afterward, Odachi keeps on thrusting a bit more until he too finishes inside of him."
            
            "The samurai lowers his partner gently back down to the ground, and ends their coupling by giving the hound a back rub to ease any tension that the position might have caused."
            
            "His firm, practiced hands run across the other's silky black fur, kneading the muscles underneath."
            
            "You can hear the thug panting in elation as he accepts the massage."
            
            hide ratio1
            show odachi naked normal at center1
            show bg alley2_night_blur:
                zoom 1
            with s_dissolve
            Odachi "Okay. That is twenty coins more, please."

            hide odachi
            show bg alley2_night
            with dissolve
            "Odachi gets back up and starts retrieving his clothes from the alley."
            
            "If the samurai is tired at all from the fervent group sex he just took part in, he's not showing it."

            show odachi normal at top:
                zoom 1.5
            show ratio1
            show bg alley2_night_blur at truecenter:
                zoom 1.5
            with dissolve
            "As Odachi turns around to face Khaleb, he pauses midway, looking square in your direction."
            
            "You let out a soft gasp as you realize he's spotted you."
            
            show odachi smile
            with dissolve
            "Instead of saying anything, though, you just see him make what you think is a slight smile at you."

            hide ratio1
            hide odachi
            show bg alley2_night at truecenter:
                zoom 1
            with dissolve
            "He then continues to talk business with the thug."

            "You get a strong feeling that now is definitely the point where you've overstayed your welcome there, and so carefully you start backing up to withdraw from the alley."
            
            scene bg townstreet_night
            with s_dissolve
            "As you emerge back onto the street, you feel like a weight has been lifted off you just knowing that your friend wasn't in any danger."
            
            "At the same time, however, you grow aware of another, more oddly damp feeling down below.."
            
            "...it would seem that all your eavesdropping had left you with a pretty prominent wet spot in your pants around the crotch..."

            scene bg tavern4
            with s_dissolve
            "Navigating your way back to the Flaming Flagon, as you walk through the front door you notice that there's a lot more commotion going on inside the tavern than there was when you left it."
            
            play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0
            show bg tavern1
            with s_dissolve
            "...The night rush must have already started, you think while looking worriedly around at the many tables full of patrons who have yet to be served."

            call bondexpdown01 from _call_bondexpdown01
            $ bondexp01 -= 1
            Gunther "[name]!"

            "You look across the barroom to see Gunther hustling between tables as he struggles to keep up with having to take orders and serve food and drinks to so many guests."

            show bg tavern1_blur
            show fen sweat at left1
            with dissolve
            Fen "Aah, s-sorry Gunther! I—I was, uh..."

            show gunther stern at right1
            with dissolve
            Gunther "Get ready and start taking all these orders! I've got people queued up at the bar to get back to."
            
            hide gunther
            hide fen
            show bg tavern1
            with dissolve
            "Without any more delay, you run to go do as Gunther told you, picking up an apron along the way to tie around your waist and hide your embarrassing wet spot before going up to the patrons."
            
            stop music fadeout 3.0
            "The rest of the evening passes with you and Gunther constantly moving on your feet to grind down the backlog of hungry and impatient guests."

            $renpy.end_replay()
            
            $ odachi_tailservice_seen = True
            $ odachi_bond_02_done = True
            #$ odachi_tailservice_seen

            $ ap = 0

            jump work_end

label odachi_bond_02b:

    scene bg tavern4
    with s_dissolve
    "You go over to serve Odachi today feeling quite a bit more anxious about it than usual."

    "Mentally, you're putting in the effort to keep yourself looking at ease while bringing him his usual drink, just hoping he won't notice anything strange."

    "You're not really sure how to talk to him now, after seeing what he does in his spare time the other night."

    "Is that same money he's been using to pay for his drinks all this time? Crazy how no one really thinks about the way coins can change hands like that."

    "And what's this strange feeling you keep getting in your chest whenever you think back on how much he seemed to be enjoying being on his knees like that...?"

    show odachi normal at right1
    show bg tavern4_blur
    with dissolve
    Odachi "Hello? [name]?"
    
    show fen shock at left1
    with dissolve
    Fen shock "Huh? O-Oh! Ah, yes?"

    "Shoot! Were you spacing out in front of him just then?"

    Odachi smile "I will like house special of the day, and one beer, please."

    Fen sweat "Yup, yup! Right away, friend. One house beer and a special day, coming up. You got it!"

    Odachi normal "Uhhh...Are you alright?"

    Fen sweat "Ahahaha! W-Why wouldn't I be?"

    Odachi "Because your understanding of the language we speak even worse than me today, I think."

    "There's no use trying to play cool about it, is there? You're just not that good of an actor."

    "Guess it's time to fess up about it, then..."

    Fen stern "Ugh, okay. It's about something I saw you doing before with those three rowdy customers..."
    
    Fen stern "...who usually sit over there at the back of the tavern."

    show odachi smile
    "His face unexpectedly brightens with understanding as you point out the one table for him."

    Odachi smile "Ah! You mean adventurers I give myself for tail service, because they pay."

    Odachi "Yes, I sorry if it looked worrying for you that night. They was, uh...excited to share me all together, first time."

    Fen "Tail service? Is that what it's called?"

    Odachi "Yes. I hear."

    Odachi "Was very happy to discover it here, as well. We also have in my home country. It very big thing there."

    Odachi smile "Starting doing it was fun and easy, because it let me have way to appreciate Feldan males with more than just eyes."

    Fen blush "Oh, wow..."
    
    "You're simply beside yourself blushing, as thoughts of all the possibilities this opens up, now that you know of it, race through your head."

    "Odachi laughs amusedly at how strongly you're reacting."

    Odachi "I did not think it would be such a delicate topic for here, though."

    show fen at shock
    Fen "N-No, no. It's not that, it's..."
    
    Fen "Actually, I don't know. Maybe it is?"

    Odachi "Then, would you like to go somewhere more private, for us to discuss together more?"

    show fen at flip
    with dissolve
    "Suddenly, you become aware of some of the other patrons snickering amongst themselves at the next table over."

    "You realise they may have overheard what you were talking about and drew some of their own conclusions from the way you were acting."
    
    Fen sweat "Yeah, uh...that's probably a good idea, actually."

    show fen normal at flipback
    with dissolve
    Fen normal "Here, come with me. I know just the place."

    stop music fadeout 3.0
    scene bg tavernback_night
    with s_dissolve
    "With an enigmatic smirk, Odachi gets up and follows you out back behind the tavern."

    "You notice that it's a warm, humid night out today as soon as you step outside, the soft crunch of dew-dappled grass under your feet."

    "The area seems just as peaceful and secluded as ever, if not more so at this hour."

    show odachi smile at left1, flip
    show bg tavernback_night_blur
    with dissolve
    Odachi smile "Ah! I see you have hay bales to be use for squats. That is very good; want to keep rump in outstanding shape for clients."

    show fen stern at right1, flip
    with dissolve
    Fen "Huh?"

    Odachi normal "For tail service. Is that not why you ask to talk with me? To give advice for how you can do it, too?"

    show fen shock at shock
    Fen shock "Wha—What!?"

    Fen sweat "I..."

    "Actually, you're not quite sure how to answer him on that."
    
    "Until now, you thought you were only asking him about it out of a disturbed curiosity."

    "But were you really interested so much because you wanted to find out what the lifestyle was like for yourself...?"

    Fen stern "I don't know, honestly."

    Fen "You see, where I come from, we never had many people who go out and do what you do so happily, I don't think."

    Fen "From what I remember...I think."
    
    Fen "I'm sorry if I misled you, but I really did just want to talk because I was curious."
    
    Fen sweat "No offence, but I'm not interested in becoming a whore."

    Odachi "..."

    Fen sweat "Uh..."

    "A long, heavy silence sets in after you finish trying to explain yourself."

    "Odachi stands perfectly still in front of you with his arms crossed, eyebrows furrowing more and more underneath his bandana with each passing second."

    Odachi "'Whore'?"

    show fen stern
    "Your ears prick up alert at the twinge of steely cold insult in his voice."

    play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
    #maybe Odachi's theme starts playing here, or special emotional music we can have for bond event moments
    Odachi "I not know of such word."
    
    Odachi "The way you say... word about shame?"
    
    Odachi smile "In my homeland, there is no shame with having ways to love world with your body."

    Odachi smile2 "There, people who do this, it not just about having sex for money."

    Odachi "People learn how to sing and play music, speak wonderful stories, host card games, make tea and even dress like royalty sometimes for clients."

    Odachi smile "Many practise to work this like we do the blade."

    show fen shock at shock
    Fen shock "...!"

    Odachi normal "I not 'surrendering' anything from me to nobody. No one is here can control or judge me, but me, ever."

    Fen stern "But the way I saw you in that alleyway with those punks, it was like they owned you..."

    Odachi smile "And I proud to let them believe so."
    
    Odachi "I do good job for them and they pay, so I have no bad thing to say for them."

    Odachi "And more than that, it is great way to have connection with all people of this world."

    Fen blush "'Connection'. Is that really the point of what all this is about?"

    Odachi normal "Of course. Most everybody in the world wish for sex. What they want is true connection."

    Odachi "Some want to rid loneliness, some want to better their stress." 

    Odachi "Some want to see the true selves inside them grow with another..."
    
    Odachi "...and some just want to be close because you have something that they can only dream."

    Odachi smile "The gods gave us bodies because this reason, [name]."
    
    Odachi "It is so we know ourselves, show ourselves, love ourselves, and love each other in all ways we can."

    Odachi "I not ashame of how I do it. Is respectable as is my way with sword."

    Fen stern "..."

    Fen sad "...Odachi. I'm sorry. It was really stupid of me to judge what you do without remembering who you are."

    Odachi "It is alright. I not one who holds grudge."

    show odachi at flipback
    with dissolve
    Odachi "But excuse me, [name]. I should go getting back to my beer."

    show fen stern at center1
    with dissolve
    "You run up to grab his shoulder just as he turns away."

    Fen "Wait! Please, teach me how to start doing tail service. I'd love to learn from you."

    show odachi normal at flip
    with dissolve
    Odachi "Hm? But I thought you say you not want to."

    show fen blush2 at right1
    with dissolve
    Fen blush2 "I-I know. But I was just scared of what I thought it was."

    Fen blush "But all that stuff you just said about why people who like to do what you do exist...it was fascinating."

    Fen "And I know, deep down, that..."
    
    Fen stern "I'm someone who needs to make use of every opportunity I have..."
    
    Fen "...to discover myself and make new connections, no matter what kind."

    Fen normal "I need to learn more about this place, be it tail service or something else."

    show odachi smile at center1
    with dissolve
    "A firm, reassuring paw grabs hold of your own."

    "Odachi is smiling."

    "He seems almost proud of you for some reason, as though the two of you had just gotten to the end of some long and perilous quest together."

    Odachi "Of course I will help you, [name]."

    Odachi "Tail service or something else, beside you I will."

    hide odachi
    hide fen
    show ratio1
    show bg tavernback_night
    with s_dissolve
    "The two of you find a place to sit down together, and you listen."

    "You feel oddly at ease right now being here, all quiet, save for the bustling of the tavern, a gentle breeze, and Odachi's steady yet confident voice."

    "The way he helps you understand his methods is actually pretty easy to follow, despite him not always knowing the best words."

    "And he even manages to present a few tips in a way that's funny enough to get a good laugh out of you, which you appreciate."

    call sxp_up from _call_sxp_up_4
    Fen blush "He's not at all a bad teacher..."

    "You feel like you could just idle away the night listening to him talk about the art of love-making."

    stop music fadeout 3.0
    Gunther "[name]...?"

    #next line can be in big letters with a bit of a rumbling screen
    Gunther "{sc=1.5}{b}{size=50}[name]!!!{/size}{/b}{sc}" with vpunch

    hide ratio1
    with dissolve
    "Uh-oh. Sounds like you might've overextended your time for a break."

    "You quickly get up and excuse yourself to Odachi for suddenly needing to go, saying you'll be sure to make use of his advice and let him know how it goes."

    show odachi smile3 at center1
    show bg tavernback_night_blur
    with dissolve
    "He waves you off with a big, jolly laugh as you run back into the Flagon."

    Odachi smile "You are fabulous, my friend! Never doubt!"

    hide odachi
    show bg tavernback_night
    with s_dissolve

    pause

    call bondlvup0302 from _call_bondlvup0302

    jump work

label murry_talk_01:
    menu:
        "Ask about his artifact." if ask_murry_bath_done == True:
            jump murray_artifact_question

        "Ask him about the Baths." if bathhouse_murry_done == True : # this then unlocks the next option
            $ ask_murry_bath_done = True
            jump murray_bath_question

        "What do you sell?":
            jump Murry_sell_explaination

        "How long have you been in business with Gunther?":
            jump Murry_gunther_history

        "Back":
            jump market_murry_menu

    label Murry_sell_explaination:

        Fen "What do you sell exactly?"

        Murry smile "Why almost anything and everything!"

        Murry normal "I'm the chief market coordinator of Felda."

        Murry "I handle all the administration of the market square here."

        Murry "I issue permits to vendors in good standing."

        Murry "For a small fee, I will also help run stalls if the owner is busy or help craftsmen source raw materials for their work."

        show murry smile at shock
        Murry "So if you can name it, I can help find it!"

        Murry grin "For a small finder's fee of course."

        Fen "Anything huh?" 

        Fen "Good to know, thank you."

        Murry smile "Any time!"

        jump murry_talk_01

    label Murry_gunther_history:

        Fen "So how long has Gunther been a customer?"

        Murry smile "Oh Gunther and I go way back."

        Murry normal "Before he even opened the doors of Flaming Flagon to the public, he was standing right where you are."

        Murry "He needed furniture, ale, and decoration. And he needed it in a hurry."

        Fen "That makes sense."

        Murry smile "And I hear you're the reason for the extra dinerware."

        Fen "Gunther said it's really good for business."

        Murry normal "It must be for him to go ahead and order that much."

        Murry grin "I know it will, I have a sense for 'big' things."

        Fen "Thanks."

        jump murry_talk_01

    label murray_bath_question:
        Fen "It was, um nice to see you at the bathhouse."

        Murry smile "Ahhh, yes."

        Murry "I must thank you for the recommendation, it's just what I needed."

        Fen "You really seemed to be enjoying yourself."

        Murry blush "It's very relaxing. And with the enchanted water, there's hardly any cleanup."

        Fen "I was a bit surprised at how flexible you are."

        Murry smile "Well that's what this fella is for."

        hide murry
        show bg:
            zoom 1.5
        show stretch_relic at truecenter
        show ratio1
        with dissolve
        "He retrieves a green amulet from his pouch and holds it up for you to see."

        show murry normal at center1
        show bg:
            zoom 1
        hide stretch_relic
        hide ratio1
        with dissolve        
        Murry "A friend made me this relic as payment for some extensive services."

        Murry smile "And oh my it do wonders."

        jump murry_talk_01

    label murray_artifact_question:

        Fen "You said your friend 'made' this?"

        Murry smile "Yes, he specializes in magic and artifact crafting."

        Murry normal "This was originally an artifact that enhances the wearer's endurance and defense. A prized treasure for any dungeon adventurer."
        
        Murry "However, he found out that the effects did not cover a very large area."

        Murry "Due to my height, it fit perfectly for me. But I'm no adventurer."

        Fen "You may not be an adventurer, but you're adventurous."

        Murry hot "Ha, I certainly am. I definitely get good use from this."

        jump murry_talk_01 

label murry_help_01:
    scene bg stall
    with dissolve
    "You watch a couple of stalls for an hour, but there were not many customers."

    "After a busy day wandering around and handing out permits to some of the vendors at the square, your feet hurt."

    show murry normal at center1
    show bg stall_blur
    with dissolve
    Murry "Thanks for your assistance."

    Murry smile "You're such a good helper!"

    Fen "Aww, thanks."

    show murry normal at shock
    Murry "Here, take this for today."

    $ fen_coins += murry_payment
    play sound "audio/payment.ogg" volume 3.0
    "Murry hands you [murry_payment] coins."

    $ bondexp05 += 3
    call bondexpup05 from _call_bondexpup05_1
    Murry smile "It's good to have you around."

    stop music fadeout 3.0
    hide murry
    show bg stall
    with dissolve

    jump day_end

label murry_bond_01:
    "The market square is bustling with business everywhere. People walk up and down the aisles looking for anything that catches their eyes."

    stop music fadeout 3.0
    "As busy as the place seems, there is one thing that appears to be missing."

    show fen 2 stern at center1, flip, backandforth
    show bg stall_blur
    with dissolve
    Fen "Hmm, where's that little guy?"

    #flip Fen sprite to look left and right

    Fen "He's not at his usual spot."

    hide fen
    show bg stall at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "He's not standing on his usual box, nor is he anywhere to be found when you walk up to the counter."

    Fen "-Sniff-sniff-"

    "You detect the faint but familiar scent of cottonwood and musk."

    Fen "He's close, perhaps over here?"

    show bg stall at right:
        ypos 1500
        zoom 2
    with dissolve
    "You follow the trail that leads behind Murry's stall."

    "As you creep around the corner, the smell of musk grows stronger."

    "Your ears perk up as you pick up Murry's voice."

    "Among the stacks of crates and bundled goods, you spot the merchant surrounded by some rather large and intimidating looking men."

    play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0
    show bg stall_blur at right:
        ypos 2000
        zoom 3
    show murry hot at top, flip:
        zoom 2
        ypos -200
    hide ratio1
    with dissolve
    Murry "Mhmm. I can think of another way to sweeten the deal."

    "With a dreamy and dazed expression, Murry reaches out to grope the massive bulge in front of him."

    "Even from this distance, you can see the man's shaft throb visibly through the taught fabric."

    "The merchant continues to rub their bulges while they chatter about what sounds like numbers."

    "Eventually everyone starts to nod their heads and they each hand over a bag of coins to the little man."

    scene bg stall at right:
        zoom 2
        ypos 1500
    with dissolve
    "Murry accepts their bags of money, and the group leaves down the other end of the alley."

    show murry blush at right1
    show fen 2 stern at left1
    show bg stall_blur
    with dissolve
    "He turns and suddenly spots you at the other end of the alley."

    show murry shock at shock
    Murry "Oh! [name], how long have you been standing there?"

    Fen "I was just dropping by to say hi. I didn't see you at the front."

    Fen 2 sweat "When I found you in the back, I didn't want to, ah, interrupt anything."

    Murry "You're talking about all those beefy men earlier?"

    Fen "Yes. I was a bit worried seeing you surrounded like that."

    Murry sweat "Alright, there's something I must tell you."

    Murry "You see all those guys are... partners."

    Fen 2 blush "Oh?"

    Murry normal "Yes, yes. They're my {b}business{/b} partners."

    Fen 2 stern "Oh..."

    Fen 2 blush "Then what's with all of that, um, rubbing and groping?"

    Murry hot "Well they're also a bunch of horny guys that like to take turns rearranging my insides."

    show fen at shock
    Fen "Seriously?"

    Murry smile "Of course! Why would I fib about something like that?"

    Fen "Well...I guess I don't really know."

    Murry normal "[name], it's alright being shy. I used to be shy like that too."

    Fen 2 stern "Really? I mean you seemed really bold to casually grope a group of guys three times your size."

    Murry normal "Oh [name], you young innocent thing."

    Murry "Let me drop off these heavy bags and their orders and I'll be right with you."

    Fen 2 normal "Let me help you out there."

    Murry smile "Oh [name], you're too kind."

    scene bg stall
    with dissolve
    "You lean down and grab the stack of orders."

    "You follow the merchant back to the front of his stall and wait patiently for him to return."

    "Murry puts away his payments and notes all the orders in his logs, you're amazed at how fast the little guy can write."

    show murry normal at right1
    show bg stall_blur
    with dissolve
    Murry "Thanks for waiting."

    show fen 2 normal at left1
    with dissolve
    Fen "No problem."

    Murry stern "As you know, I'm a very busy guy."

    "You nod as he lets out a long sigh and slumps a bit."

    Fen 2 stern "Yeah."

    Murry sweat "It never ends, I tell ya."

    Fen "Do you ever take a break?"

    "Murry scratches his head in frustration and sighs."

    Murry "I've so little time, I often have to mix business with pleasure."

    Fen "Murry..."

    Murry "Well what can you do? The good people of this town are in constant need of my services, and the merchant guild won't dare try to replace me."

    Fen "Sounds like a tough job. I can understand the need to unwind."

    Fen 2 normal "Have you considered taking a trip to the bathhouse?"

    Murry stern "I have...not."

    Fen 2 smile "Really? You should. It's a great place to relax your sore body."

    Murry normal "Hmm. Perhaps a hot soak after a good stretching does sound nice."

    Fen 2 normal "Stretching? You can do that there."

    Murry "Oh wow...okay. I thought it was a bunch of fru fru health stuff. But it sounds like there might be some decent action there."

    Fen 2 smile "I always find the baths pretty relaxing on my off days."

    Murry smile "Thanks for the advice."

    Murry "I need to blow off steam, but my normal group hasn't been able to get together like we normally do."

    Fen 2 normal "Oh, a group of friends?"

    Murry blush "I guess you could call them that. They're more like fuck buddies."

    Fen 2 blush "Oh... um, sorry for the confusion."

    Murry smile "It's okay, I get it. They're really sweet guys, but at the end of the day they just want to get their rocks off."

    show murry stern
    with q_dissolve
    "You notice Murry's gaze nervously darts around all the papers on his desk."

    Fen 2 stern "Backed up on orders?"

    Murry normal "I'm backed up, but not on orders. These are mandates from the head of the merchant's guild and adjunct to the Royal Treasurer."

    Murry "Felda maintains various trade agreements with other towns around the kingdom. The royal treasurer is also in charge of trade agreements with neighboring powers."

    Murry "All merchant guild masters report to the treasurer, but my guild master actually works for her."

    Murry stern "And because of that, he wants his reports to look better than the other guild masters."

    Fen "He just wants to look good for his boss?"

    show murry angry at shock
    Murry "Yes, but I'm the one who has to do all the work!"

    Murry "Every day, I get a new message from him to shift goods around and that a new shipments would be dropped off at my market and I'm told to get rid of it quick."

    Murry stern "I can't vouch for all these vendors or the quality of the materials."
    
    Murry "It makes me uncomfortable to try to push off anything subpar to the people of Felda."

    Fen 2 normal "That's very admirable, Murry."

    Murry normal "Yeah, he's just going to make my life more difficult. I can't trust craftsmen I've never heard of before."

    Murry "The best part of my job is making new connections, making a new sale, doing 'whatever' I need to do to seal the deal."

    Murry blush "I've had some hard and rough negotiations. But by the end of it, everyone was satisfied."

    Fen 2 stern "And we're talking about..."

    show murry smile at shock
    Murry "New business deals of course!"

    Fen 2 sweat "Right, yes, do go on."

    scene bg stall
    with dissolve
    "As you grow accustomed to the causal nature of rampant sex that seems to be prevalent among the locals, Murry still seems..."
    
    stop music fadeout 3.0
    "...excessive compared to everyone else."

    call bondlvup0501 from _call_bondlvup0501

    scene bg stall
    with dissolve

    play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0

    show murry normal at center1
    show bg stall_blur
    with dissolve
    Murry "Well enough of my troubles. I really appreciate you letting me talk your ear off."
    
    Murry smile "What can I help you with today?"

    jump market_murry_menu

    #jump Murry menu


label marcus_bond_01:
    scene bg tavern4
    with s_dissolve
    stop music fadeout 3.0
    "You spot the bathhouse owner at one of the tables, he waves you over."

    show fen normal at left1
    show bg tavern4_blur
    with dissolve
    Fen "Good evening, Marcus."

    show marcus normal at right1
    with dissolve
    play music "audio/Sir Gawain.ogg" volume 1.0 fadein 3.0
    Marcus "[name]! Good to see you again. I see your fur is well kept."

    Fen blush "R-right. All thanks to you."

    Marcus grin "Glad to be of service."

    Fen wink "You're at the Flagon now, it is my turn to service {b}you{/b}."

    Marcus normal "Well I do think I see something appetizing..."

    Fen normal "What can I get for you?"

    Marcus "The food smells pretty good tonight. I'd like a meal and a flagon of ale."

    Fen smile "Coming right up."

    hide fen
    hide marcus
    show bg tavern4
    with dissolve 
    "You swiftly return with his order."

    show marcus smile at right1
    show bg tavern4_blur
    with dissolve
    Marcus "Mmmm! This is delicious!"

    show fen smile at left1
    with dissolve 
    Fen "Thanks."

    Marcus normal "It's amazing, the place seems very lively."

    Fen normal "It's as busy as usual for me, I'm sure you keep pretty busy yourself since you haven't dropped by till now."

    Marcus "Aye, that I am. But now that things have calmed down and I'm able to get away every once in a while."

    Fen "That's great. Is there anything else I could get for you?"

    Marcus smile "I'm good for now, gotta enjoy the meal."

    Fen smile "Call me if you need more."

    stop music fadeout 2.0
    hide marcus
    hide fen
    show bg tavern4
    with s_dissolve

    call bondlvup0601 from _call_bondlvup0601

    $ ap -= 1

    #bond up.

    jump work

label marcus_serve_01:
    "You serve Marcus the food and drink he ordered."

    "He seemed more interested in the food than the drinks, and ordered as many meals as usual."

    "You're not sure if you're seeing things, but you think his belly is getting a little bigger."

    $ bondexp06 += 1
    call bondexpup06 from _call_bondexpup06

    $ ap -= 1

    jump work

label marcus_event_01:
    Marcus "Hey...[name] was it?"

    Fen "Yep. That's me."

    Marcus smile "Good, I have a bit of a bad memory."

    Fen sweat "Yeah, tell me about it..."

    Marcus normal "Ah yes, at least we have each other's company then."

    Fen "I heard Gunther ask about your children, where are they?"

    Marcus smile "Oh they're all grown now and went off to start their own businesses and projects outside of Felda."

    Marcus normal "Sometimes I hate how large the kingdom is, but that's how life goes."
   
    Fen "Big family?"

    Marcus "Yep. I used to be an adventurer until I got news about my first child."

    Marcus stern "After he was born, I knew I wanted a big family. I couldn't keep risking my life dungeon diving, so I started up this place about a decade ago."

    Fen "Wow, that's wild."

    Marcus normal "Those were quite some times. Now weary adventures and townfolk come here to enjoy my bathhouse and relax."

    Fen "Bathhouses are very unfamiliar to me."

    Marcus "So this is your first time on your own, right?"
 
    Fen blush "Y-Yeah."

    Marcus grin "Don't worry, [name]. Let me give you a quick rundown again.."

    show marcus at center1:
        ease 1 zoom 1.1 ypos 1500
    "The purple rhino leans closer to you."

    Marcus normal "Here's how it works." 

    Marcus "Two main rules, no running and no clothing in the bath rooms."

    Marcus "There's the Delphinium pool. It's the largest pool and where most people go to rinse off and soak for a while."

    Marcus "Then we have the Narcissus pool. It's a smaller area, but we have refreshments and a sauna."

    Fen "Sauna?"

    Marcus "It's an enclosed area that is filled with steam. People like to gather there to sweat and chit chat."

    Fen "Sweat? I thought they came here to get clean."

    Marcus smile "Oh sweet youth. Sweating is one of the body's many ways of clearing out toxins." 

    Marcus "It's also beneficial to blood circulation. There are many therapeutic benefits."

    Fen "That's very fascinating."

    Marcus normal "And then there's my new private pool - Belladonna."
    
    Marcus "I've got myself a lovely tub and I use the space for massages as well."

    $ bondexp06 += 1
    call bondexpup06 from _call_bondexpup06_1

    Marcus smile "By the way, your fur looks a lot better. I see you've used the conditioner."

    Fen "Oh yes, that really made my fur feel soft. Thanks again."

    show marcus normal at center1:
        zoom 1
    with dissolve
    Marcus normal "It is my pleasure. Now..."

    jump bathhouse_menu

# talk at bathhouse
label marcus_talk_01:

    menu:
        "Could you use any help today?" if bath_work_unlock == True:
            
            Marcus smile "Thanks! Like said before, I could use a hand around here."

            if bath_work_time == 0:
                jump bathhouse_work2

            if bath_work_time == 1:
                jump bathhouse_work3

            else:
                jump bathhouse_work1

        "Back":
            jump bathhouse_menu

# talk at tavern
label marcus_talk_02:
    stop music fadeout 3.0

    scene bg tavern4_blur
    show marcus normal at center1
    with s_dissolve
    play music "audio/Sir Gawain.ogg" volume 1.0 fadein 3.0
    "Marcus smiles and invites you to chat for a bit."

    menu:
        "How are your children doing?":
            jump marcus_talk02_response1

        "Tell me about being an adventurer.":
            jump marcus_talk02_response2

        "What was the fruit I spotted the luxury bath.":
            jump marcus_talk02_response3

    label marcus_talk02_response1:

        Marcus smile "Which one? I have seven of them so far."

        Fen "Wow, big family."

        Marcus normal "Of course. I've always wanted a big family. I got my wish."

        Fen "So how old are they?"

        Marcus "They're all adults now. The youngest just turned twenty."

        Marcus "None of them wanted to stay and run the business with their old man, They'd rather be artists and tradesmen."

        Marcus "They moved back towards the kingdom so they could learn from a \"proper\" guild."

        Fen "Aww, you must miss them."

        Marcus stern2 "A bit. Really when they were little is what I miss the most. They grow up so fast."

        Fen "Cheer up, maybe they'll bless you with a grandbaby."

        $ bondexp06 += 1
        call bondexpup06 from _call_bondexpup06_2
        Marcus smile "I might be too old for another baby."

        Marcus stern "Hmm, then again, maybe not."

        Fen "...?"

        Marcus shock "Sorry, I'm just rambling now."

        stop music fadeout 3.0
        Fen "It's alright."

        $ ap -= 1

        jump work

    label marcus_talk02_response2:

        Marcus "That was quite some time ago, but quite an exciting one."

        Marcus grin "I was a poison specialist."

        Fen "Poison? Like an assassin?"

        Marcus sweat2 "Err, no. But you're not the first to also think the same."

        Fen "Oh, sorry."

        Marcus normal "No, I did nothing nefarious like that. I'm a researcher of poisons, venoms, and other toxic substances."

        Marcus "I identified, nullified, and treated party members who were poisoned as well as created new kinds for a variety of purposes."

        Fen "That's incredible."

        Marcus smile "Yes, the botanical and anatomical knowledge required is quite extensive."

        Fen "I'm going to pretend I know what that means."

        Marcus normal "It boils down to simple chemistry. Learning what different substances do to each other and to your body."

        Fen "Oh, is that how you know so much about skin and hair treatments?"

        Marcus "Actually, yes it is."

        Fen "I think that's really awesome. You took your skills and applied it to your business."

        Marcus smile "Yep, there's quite a few other retired adventurers who did the same."

        Fen "You'll have to share some more stories next time."

        stop music fadeout 3.0
        $ bondexp06 += 1
        call bondexpup06 from _call_bondexpup06_3
        Marcus normal "If you don't mind me rambling so much, sure."

        $ ap -= 1

        jump work
    
    label marcus_talk02_response3:

        Marcus "Oh those? They're called gem fruits."

        Fen "Now that you mention it, they do look pretty shiny."

        Marcus "Yes, one of the patrons donated a couple barrels of them to hand out."

        Marcus smile "They've been a hit, snacks have to survive the steamy and warm atmosphere around the pools."

        Fen "That makes sense. I have never seen fruit like this before."

        Marcus normal "Apparently it's only found growing in the dungeon."

        Fen "Sounds dangerous."

        Marcus "It is, but that's the charm of the dungeon. It contains things that are both marvelous and horrific."

        Fen "Hmm...food from the dungeon? Anyways, they were pretty tasty."

        stop music fadeout 3.0
        $ bondexp06 += 1
        call bondexpup06 from _call_bondexpup06_4
        Marcus smile "I'm glad you enjoyed them, the merchants are very fond of them as well."

        $ ap -= 1

        jump work

label bath_work_start:

    "You enter the bathhouse and spot the proprietor."

    show marcus stresse at center1, backandforth
    show bg bathhousehall_blur
    with dissolve
    "You see Marcus stumbling with his arm full of towels while also balancing a stack of buckets on his tail."

    show fen 2 stern at left1
    hide marcus
    with dissolve
    Fen "Umm, do you need some help?"

    show marcus sweat at right1
    with dissolve
    Marcus "Oh thank you, yes! Please set these buckets down on the counter."

    hide fen
    hide marcus
    show bg bathhousehall
    with dissolve
    "You help unburden his tail and he scrambles to the back room with his stacks of towels."

    "After a moment he returns with various bottles and soaps to fill the buckets with."

    show fen 2 stern at left1
    show bg bathhousehall_blur
    with dissolve
    Fen "I can come back later if you're busy."

    show marcus normal at right1
    with dissolve
    Marcus "Oh no, please wait. I can assist you. It's just sometimes I get a little backed up on tasks."

    Fen 2 normal "Oh, well I'd be happy to help you when I'm available."

    Marcus "Hmm... well business is picking up a little more than usual, even after the downsizing."
    
    Marcus grin "A part time worker can really help."

    "Marcus says that while staring at you, leaving no doubt about what he's implying."

    $ bath_work_unlock = True

    Fen 2 stern "Hmm, if it's on my day off..."

    Fen 2 smile "Sure, I'll come by when I have time to help."

    Marcus smile "Heh, that's good to hear. I reckon Gunther won't mind lending you to me once in a while."

    Marcus normal "So..."

    hide fen
    show marcus normal at center1
    with dissolve

    jump bathhouse_menu

#this can be the repeated task
label bathhouse_work1:
    Marcus normal "Could you help me restock all the tables with juice and fruit from the barrels in the store room?"

    Fen "Of course."

    scene bg bathhouse3
    with dissolve
    "This feels no different than working at the tavern."

    show fen naked normal at center1, flip, backandforth
    show bg bathhouse3_blur
    with dissolve 
    "A couple hours fly by as you run around the baths naked, filling the bowls with fresh snacks and pitchers with cold juice."

    "It's just like being a waiter, but naked!"

    "Most of the luxury bath's patrons commend you for your hard work."

    show fen naked blush at shock
    "Every once in a while, the patrons sneak in a pinch on your fuzzy rump."

    Fen "Yep, just like the tavern."

    hide fen
    show bg bathhouse3
    with dissolve
    "You even have a few bites here and there of the tasty bathhouse refreshments."

    scene bg bathhousehall_blur
    show marcus smile at center1
    with dissolve
    call bondexpup06 from _call_bondexpup06_6
    $ bondexp06 += 3
    Marcus smile "Thanks for your hard work. Here's payment."

    $ fen_coins += 15
    play sound "audio/payment.ogg" volume 3.0
    "Marcus hands you 15 coins for your work."

    $ bath_work_time += 1

    jump day_end

label bathhouse_work2:

    Marcus normal "Got something more dirty, today. I need all the dirty towels washed."

    "Your nose wrinkles at the thought."

    Fen "A-alright." 

    hide marcus
    show ratio1
    show bg bathhouse1 at center:
        zoom 1.5
    with s_dissolve
    "You collect the towel baskets from the side of pool."

    "Most of the cleansing scents in the air can mask more offensive odours, but not to your nose."

    scene bg black
    with s_dissolve
    "All the used towels are dumped into the wash basin located by the storage room."

    "The ingenious design provided a slot that pours out hot water into a large drain below."

    "The soiled cloths are to be placed into a large hollow barrel."

    "Loads of towels are placed beneath the flow of hot water."

    "As you open the slot to allow the cleaning water to flow out, the smells of people working all day disappear."

    "You use a large stick to agitate the towels as they rinse to knock off any dirt or debris." 

    "There's usually never too much since everyone must rinse before being allowed into the baths."

    "By the time your arms feel sore, you finish washing the last load."

    scene bg sky
    with s_dissolve
    "Now you spend a bit of time hanging them out to dry on the large drying racks located at the back of the bathhouse."

    "With the last wet towel hanging, you bring in the other rack full of clean towels and fold them."

    call bondexpup06 from _call_bondexpup06_7
    $ bondexp06 += 3   
    scene bg bathhousehall_blur
    show marcus smile at right1
    with dissolve
    Marcus "Great work! Feel free to use the pools."

    show fen 2 stern at left1
    with dissolve
    Fen "Hmm, it is getting a bit late."

    Marcus normal "It is, but we're closed so you'll have the place to yourself."

    show fen 2 smile at shock
    Fen 2 smile "Ah yes!"

    scene bg bathhouse1
    with dissolve
    "Thankfully you do have enough time to soak some of the soreness away."

    $ fen_coins += 15
    play sound "audio/payment.ogg" volume 3.0
    "Marcus pays you 15 coins for your hard work and you return to your room for the night."

    $ bath_work_time += 1

    jump day_end
    
label bathhouse_work3:

    Marcus normal "Could you run the counter while I take care of some things in the back?"

    Fen "Sure."

    hide marcus
    show ratio1
    show bg bathhousehall at center:
        zoom 1.5
    with dissolve
    "Working at the counter is perhaps the most boring job."

    "The majority of people come in and pay for a bath. You hand them the appropriate basket and offer any other soaps or oils you have on the counter."

    "Every once in a while, you come across a local who is surprised to see someone else at the counter other than Marcus."

    "Locals rarely stop to chit chat with you, preferring to do their talking around the baths or saunas."

    "You can hear Marcus giving someone a private massage and thinking about taking a peek."

    "However, customers keep arriving at a steady rate and you are unable to slip away."

    "Hours tick by between collecting payments and restocking some buckets and towels."

    scene bg bathhousehall
    show marcus normal at center1
    with dissolve
    call bondexpup06 from _call_bondexpup06_8
    $ bondexp06 += 3
    Marcus "Thanks [name], here's payment for today."

    $ fen_coins += 15
    play sound "audio/payment.ogg" volume 3.0
    "Marcus hands you 15 coins for your work."

    Marcus smile "Feel free to use the pool before closing up; you deserve a good rest."

    scene bg bathhouse1
    with dissolve
    "After resting a bit in the pool, you call it a day and head back."

    $ bath_work_time += 1

    jump day_end

label marcus_bond_02:

    Marcus smile "[name], good to see you. It's been really great having you around."

    Fen blush "Aw, thanks."

    Marcus normal "Seriously, it's given me extra time to research some new lotions and soaps scents."

    Fen "That's great. Speaking of lotions and soaps..."
    
    Fen "I was curious how you came up with so many wonderful scents for your products."

    Marcus "It's no different than my days as an adventure. Would you like to watch?"

    Fen excited "Really? I'd love to!"

    Marcus grin "Follow me."

    scene bg marcus workshop
    with s_dissolve
    "Marcus leads you down to his workshop attached to the bathhouse."

    "The spacious area allows the adequate ventilation for the various substances the former poisons specialists work with."

    "Vials and bottles of various herbs, powders, and oils sit out on a large wooden table."

    "A few notebooks accompanied the tools and behind them are shelves brimming with extra bottles and raw ingredients."

    "In the centre of the table is a large glass cauldron used to mix batches of various products."

    show fen 2 stern at left1
    show bg marcus workshop_blur
    with dissolve
    Fen "Woah."

    "You watch in amazement as he proceeds to work."

    "Marcus grabs a few bottles off the shelf to his right."

    show marcus normal at right1
    with dissolve
    Marcus "Just like working with toxins and poisons such as these, their chemical compounds that trigger different reactions."

    Marcus grin "Too much and it can kill you, just enough and it can tingle or numb pain."

    Marcus normal "A delicate equilibrium must be struck and we use our senses to navigate and balance everything out."

    Fen 2 normal "Huh, this sounds a lot like cooking."

    Marcus smile "I suppose you're correct, in many ways they are similar."

    Marcus normal "Hmm, maybe you might have a knack for this as you do cooking."

    Marcus "You prepare various ingredients to extract the specific qualities and then combine them to bring out a wondrous result."

    Fen "I think I understand, you also prepare ingredients and then fuse them together."

    show marcus smile at shock
    Marcus "Exactly! You catch on quick. There are many properties to different plants, minerals, and even animals like some snail shells can be used to manufacture potent poisons."

    Marcus normal "When diluted, you have a much more weakened effect and certain combinations can stimulate healing."

    show marcus at center1
    with dissolve
    "Marcus uncorks a bottle filled with a dried green powder and hands it to you."

    show marcus at right1
    with dissolve
    Marcus "Give this a careful whiff."

    hide fen
    hide marcus
    show ratio1
    show bg marcus workshop at truecenter:
        zoom 1.5
    with dissolve
    "As you hold the bottle close to your snoot, you immediately catch a strong minty smell."

    hide ratio1
    show fen 2 stern at left1
    show marcus normal at right1
    show bg marcus workshop_blur at center:
        zoom 1
    with dissolve
    Fen "Whew, that's strong."

    Marcus "Yep, this contains a compound that helps open up your sinuses and helps with breathing issues as well as nausea."

    Marcus smile "Combined with a soap base, it makes a wonderful scrub that leaves a tingly feeling."

    Fen 2 normal "How do you make soap?"

    Marcus normal "Oh it's quite easy. You take fat or oil and mix it with something alkaline, like lye."

    Fen 2 stern "Alkaline?"

    Marcus "Yes, as in the opposite of an acid. Alkaline substances will neutralise acidic substances."

    Marcus "But we're here to make something that helps keep fur soft and scales shiny. The scents all start in the oil."

    hide fen
    hide marcus
    show ratio1
    show bg marcus workshop at truecenter:
        zoom 1.5
    with dissolve
    "He takes a vial of sweet smelling oil and mixes it with some of the green powder. He grabs another large glass jug of some milky white liquid."

    Marcus "Now we just add some lye for our alkaline base, and bam." 

    "He pours everything into a large pot and places it in a bucket of hot water."

    "After a few stirs, he takes the mixture and pours it out into a large rectangular mould."

    hide ratio1
    show fen 2 stern at left1
    show marcus smile at right1
    show bg marcus workshop_blur at center:
        zoom 1
    with dissolve
    Marcus "And that's it. Once it dries and firm up, I cut it into bars."

    Fen 2 normal "Wow, that's pretty easy."

    Marcus "Want to try making an oil yourself sometime?"

    show fen 2 stern at shock
    Fen "Really?"

    Marcus normal "Of course, you've been such a great help."

    Marcus normal "Say, next time you order a massage, you're welcome to use the equipment here if you like."
    
    Marcus grin "We can use the oil you make during the massage. And don't worry about your fur, the oils I have here are fur-friendly."

    Fen 2 normal "Interesting, I'll consider that."

    Marcus smile "Who knows, maybe you'll come up with the next fragrance that will take Felda by storm."

    "You can't help but notice his ample belly jiggling when he laughs."

    stop music fadeout 3.0
    hide marcus
    hide fen
    show bg marcus workshop
    with dissolve
    "He sets the soap block down to dry on another shelf and accompanies you back to the front of the bathhouse."

    call bondlvup0602 from _call_bondlvup0602

    play music "audio/Sir Gawain.ogg" volume 1.0 fadein 3.0
    scene bg bathhousehall_blur
    show marcus normal at center1
    with dissolve
    jump bathhouse_menu

    #return bathhouse_menu and unlocks oil mixing option as part of the private bath

label oil_mix:
    Fen "I'd like to try mixing an oil."

    Marcus smile "Great, feel free to use the workbench. I think I still have everything set out from last time."

    Fen "Thanks."

    scene bg marcus workshop
    with s_dissolve
    "You head over into Marcus's workshop."

    #Cg Marcus_workshop

    "The place is neat and tidy with everything you need to craft a new oil base."

    "Marcus trusts you to work around the hazardous materials and that means donning the proper protective gear."

    "Now it's time to get cooking!"

    label oil_mix_menu:

        if oil_mix_counter >= 2:
            jump oil_mix_done

        else:
            pass

        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_blue:
            ypos 180
            xpos 700
            zoom 2
            rotate -30
        show olie_red:
            ypos 200
            xpos 50
            zoom 2
            rotate -10
        show olie_white:
            ypos 220
            xpos 1100
            zoom 2
            rotate 30
        show olie_yellow:
            ypos 150
            xpos 400
            zoom 2
            rotate 20
        show ratio1
        with dissolve

        menu:
            "Each oil has its own unique aroma, what combinations will you try mixing together?"

            "Check out red oil.":
                jump red_oil

            "Check out yellow oil.":
                jump yellow_oil

            "Check out blue oil.":
                jump blue_oil

            "Check out white oil.":
                jump white_oil

    # base oil descriptions (red{1], yellow[2], blue[3], and white[4])
    # Value red=1, yellow=2, blue=3, white=5
    # Mix Value combo1=3 combo2=4 combo3=6 combo4=5 combo5=7 combo6=8

    label red_oil:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_red at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "The crimson fluid has a spicy scent. Not exactly cinnamon or peppery, but somewhere in between."

    menu:
        "Use this oil?"

        "Use this one.":
            
            if oil_mix_value == 1:

                "You have already picked this one."

                jump oil_mix_menu
            
            else:
                "You added red oil into the mixture."
                $ oil_mix_value += 1
                $ oil_mix_counter += 1
                jump oil_mix_menu
            

        "Pick another.":
            jump oil_mix_menu


    #create options that the player selects an oil for use and output the corresponding combo text

    label yellow_oil:

        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_yellow at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "This reminds you of cooking oil, however it smells like a field of flowers. This fluid produces a mighty floral smell."

    menu:
        "Use this oil?"

        "Use this one.":
            
            if oil_mix_value == 2:

                "You have already picked this one."

                jump oil_mix_menu
            
            else:
                "You added yellow oil into the mixture."
                $ oil_mix_value += 2
                $ oil_mix_counter += 1
                jump oil_mix_menu
            

        "Pick another.":
            jump oil_mix_menu

    label blue_oil:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_blue at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "Brilliant and blue, this oil smells like a strong, but not overpowering cologne."

        "You can pick out hints of musk, hibiscus, sandalwood, and coconut, this oil is very complex."

    menu:
        "Use this oil?"

        "Use this one.":
            
            if oil_mix_value == 3:

                "You have already picked this one."

                jump oil_mix_menu
            
            else:
                "You added blue oil into the mixture."
                $ oil_mix_value += 3
                $ oil_mix_counter += 1
                jump oil_mix_menu
            

        "Pick another.":
            jump oil_mix_menu

    label white_oil:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_white at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "Smelling this one causes a shock to your senses! Your nose burns for a moment before you smell a sharp astringent scent."

        "Suddenly the sharp smell mellows out into something similar to butter. How odd."

    menu:
        "Use this oil?"

        "Use this one.":
            
            if oil_mix_value == 5:

                "You have already picked this one."

                jump oil_mix_menu
            
            else:
                "You added white oil into the mixture."
                $ oil_mix_value += 5
                $ oil_mix_counter += 1
                jump oil_mix_menu
            

        "Pick another.":
            jump oil_mix_menu

    label oil_mix_done:

        $ oil_mix_counter = 0
        
        if oil_mix_value == 3:
            jump combo1

        if oil_mix_value == 4:
            jump combo2

        if oil_mix_value == 6:
            jump combo3

        if oil_mix_value == 5:
            jump combo4

        if oil_mix_value == 7:
            jump combo5

        if oil_mix_value == 8:
            jump combo6

    label combo1:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_redyellow at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "You combine the red and yellow oils together. They start to blend into a lovely orange colour."

        Fen "Mmm, it has a spicy citrus note to it."

        "The mixture leaves a slightly warming sensation."

        scene bg bathhouse3
        with dissolve
        "You return to Marcus and hand him the freshly made oil."

        jump bathhouse_private_massage 

    label combo2:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_bluered at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "You mix the red and blue oils together into a single container."

        "Swirling the bottle gently, you watch the colours meld together into a brilliant violet hue."

        "It smells a bit fruity with a mild chilling sensation."

        scene bg bathhouse3
        with dissolve
        "You return to Marcus and hand him the freshly made oil."

        jump bathhouse_private_massage

    label combo3:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_redwhite at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "Taking the red and white vials, you combine them into a beautiful pink colour."

        "The new aroma carries a mix of rose and cherry blossom tempered with a mild smokey note."

        scene bg bathhouse3
        with dissolve
        "You return to Marcus and hand him the freshly made oil."

        jump bathhouse_private_massage

    label combo4:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_blueyellow at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "The yellow and blue oils fuse into a rich emerald green colour."

        "Wafting the bottle closer to your face, you are hit with a strong herbal scent."

        "It fades into a crisp minty aroma that leaves a tingling sensation in your nose."

        jump private_bath1

    label combo5:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_yellowwhite at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "Yellow and white blend together to make a golden honey-like substance."

        "You admire the shiny colour, the aroma is mild but sweet."

        scene bg bathhouse3
        with dissolve
        "You return to Marcus and hand him the freshly made oil."

        jump bathhouse_private_massage

    label combo6:
        scene bg marcus workshop_blur at truecenter:
            zoom 1.5
        show olie_bluewhite at truecenter:
            zoom 2
        show ratio1
        with dissolve
        "The white oil changes the rich blue colour into something that looks like a cloudless sky."

        "A rich and fresh scent reminds you of a beautiful spring day, flowers and grass covered in dew."

        "The floral notes blended with a soft pine scent is very relaxing."

        scene bg bathhouse3
        with dissolve
        "You return to Marcus and hand him the freshly made oil."

        jump bathhouse_private_massage


    #Below is the minor addition I'd suggest we add to Private Bath sex option with non-special mix

    #"Aside from the pleasant aroma, the oil does not appear to have any other effects." 

label private_bath1:

    #Mixing the right combo unlocks new CG
    scene bg bathhouse3
    with s_dissolve

    "You return to Marcus and hand him the freshly made oil."

    stop music fadeout 3.0
    play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0

    $ oil_mix_value = 0

    #If first time
    if private_bath1_done == False:

        $ private_bath1_done = True
        show marcus naked normal at right1
        show bg bathhouse3_blur
        with dissolve
        Marcus "Wow, this mixture is really something."

        show fen naked normal at left1
        with dissolve
        Fen "Mhmm, thanks again for letting me use your equipment."

        Marcus naked smile "Of course! Now let's get to it."

    else:
        #if not first time
        show marcus naked grin at right1
        show bg bathhouse3_blur
        with dissolve
        Marcus "Heh, it's that mix again, isn't it? This pup is craving it again, huh?"

        show fen naked blush at left1
        with dissolve
        Fen "Well, when you put it that way... yeah."

    play music "audio/bathtubambient.ogg" volume 0.2 fadein 3.0
    hide fen
    hide marcus
    show bg bathhouse3 at truecenter:
        zoom 1.5
    show ratio1
    with dissolve
    "You lay on the table and the bathhouse owner pours the potent mixture into his hand, letting some excess run down the small of your back."

    "Immediately the room is filled with its unique scent, and you can hear Marcus take in a deep whiff."

    Marcus "Mmm, I just love this smell."

    Fen "Me too."

    "The rotund man runs his oil slicked palms along your back, coating every curve."

    Marcus "I would have never thought of mixing those together. This makes my nose tingle!"

    Marcus "Mmm, there's something else to this mix. I can just sense it."

    "Your skin tingles as the concoction activates with your natural body heat."

    "A pleasurable sensation skitters across your back as Marcus begins his massage."

    Marcus "It's so warm."

    play sound "audio/light moan 2.ogg" volume 0.5 loop fadein 3.0
    "He keeps spreading the oil as he kneads your muscles until you feel your body start to go slack."

    "Your masseuse's skilled hands run up and down your back, stopping upon your ass to give your plump cheeks a little extra attention."

    "Every little motion relaxes you more until you feel like you're floating."

    "A gentle nudge to your shoulder brings you back to the massage table."

    hide ratio1
    show bg bathhouse3_blur at top:
        zoom 1.5
    show marcus naked grin at top:
        zoom 1.5
    with dissolve
    Marcus "Well you loosen up quick. Maybe you should sit up, so you don't pass out."

    Fen "Yeah..."

    stop sound fadeout 3.0
    #CG starts from here, zoom on Marcus holding you
    scene marcus cg1 01 at top:
        zoom 1.5
    with s_dissolve
    "As you sit yourself up on the massage table, Marcus moves behind you."

    play sound "audio/light moan 2.ogg" volume 0.5 loop fadein 3.0
    "His strong hands slide around your waist, his fingers stroke along your soft belly fur."

    "While his meaty fingers roam over your chest, gliding across your skin with ease."

    "His tantalising touch is combined with the warmth of his ample belly pressed against your back."

    "By now, the pleasant smell of your oil mix fills the room and coats you both."

    "The pleasure enhancing effects stirs a different sensation with you both."

    "You start to grow horny, and from what you can tell, so was Marcus."

    scene marcus cg1 01 at truecenter:
        zoom 1.5
    with dissolve
    "He continues to knead your muscles along pecs and down your sides, letting his fingers trail just a bit longer through your fur."

    "You can feel his breath above you as he half embraces you while still massaging down your arms."

    "His touch is soft. You can't help but lean back against his lovely belly."

    stop sound fadeout 3.0
    "You want to be closer to him as well, the growing desire to blend your bodies together becomes harder to resist with each passing moment."

    #zoom on their head
    scene marcus cg1 01 at top:
        zoom 1.5
    with dissolve
    "As if he could read your mind, Marcus nuzzles the top of your head and pulls you closer against him." 

    Marcus "[name], I can't stop touching you."

    "You sink into the bigger man and let his burly arms envelop you."

    Fen "Please, keep going."

    "Looking at the older man with pleading eyes, he smiles and leans his head down."

    #zoom on kiss

    scene marcus cg1 01 at truecenter:
        zoom 2
    show ratio1
    with dissolve
    "Your lips press together. You kiss Marcus deeply, letting your lips mesh and fit themselves together like holding hands."

    "You kiss the big guy and nibble along his lower lip, he returns the enthusiasm by licking back."

    "Not long after, your tongues tangle together while your lips continue to find different ways to fit together."

    "Sloppy but full of passion, you make out while his hands continue to rub and stroke your smaller body."

    #zoom on after kiss
    scene marcus cg1 03 at top:
        zoom 2
        xpos 1200
    show ratio1
    with dissolve
    "After a while, you finally part to catch your breath."
    
    "A bridge of spit connects your mouths for a moment as you pull away slowly and gaze longingly at one another."

    #change zoom/CG
    "Marcus smiles and follows up another smooch on your cheek."

    "He growls into your ear and strokes the inside of your thighs."

    "As Marcus's fingers trail along your soft fur, you feel the effects of your oil mixture."

    #Zoom on fen cock
    scene marcus cg1 03 at truecenter:
        zoom 2
        ypos 350
    with dissolve
    "The compounds course in your blood as your pulse quickens and your cock stands at full attention."

    "Every sensation of the man's touch sends shivering ripples of pleasure through your spine."

    Marcus "Let me help you with that."

    play sound "audio/light moan 2.ogg" volume 1.0 loop fadein 3.0
    scene marcus cg1 02 at truecenter:
        zoom 1
    with dissolve
    "The man reaches right between your legs and wraps his hand around your arousal."

    Marcus "You have a fine cock here, full of youthful vigor and energy."

    "He teases you with a light grip, just enough for your oiled flesh to drag slightly against his palm."

    scene marcus cg1 04a at truecenter:
        zoom 1
    with dissolve
    "Just a few strokes and your cock leaks like a fountain."

    Marcus "Fuck, that's hot."

    stop sound fadeout 2.0
    Fen "K-Keep going."

    play sound "audio/light moan 1.ogg" volume 0.5 loop fadein 3.0
    play fuck "audio/fuck mid 1.ogg" volume 1.0 fadein 1.0
    #Marcus jerk you animation
    scene marcus cg1 04 at truecenter:
        zoom 1
    with dissolve
    "Marcus obliges and grips your entire length in his hand."

    "Instantly another massive surge of pleasure wrecks your body as he merely squeezes your shaft."

    Fen "Ah!"

    Marcus "Whoa, that's hard!"

    "Your manhood is incredibly rigid as it throbs and gushes with pre at the slightest touch."

    "He teases your length, tracing his fingertips along the underside of your shaft, watching it bounce up and down his fingers as your heart beats."

    "As he slathers your cock in tingling oil, you moan and whimper from the sensual and gentle touch."

    Marcus "Just lean back and let me make you feel good."

    "You become aware that you're not the only one getting excited, Marcus's thickness begins to stir."

    #marcus erect cg, keeps jerking
    scene marcus cg1 05 at center:
        zoom 1.5
    with dissolve
    "His fat girth slaps against your leg as it fully awakens; you feel it throb against your thigh."

    "He notices you looking and gives your bits another teasing squeeze that makes you gasp."

    Marcus "Heh, can't help myself around you."

    scene marcus cg1 05 at truecenter:
        zoom 1
    with dissolve
    "Marcus's other hand continues to rub up and down your chest, teasing your nipples along each pass."

    "The hand around your length continues to stroke and squeeze your needy arousal."

    Fen "M-Marcus, a-ah."

    "You toss your head back, letting out a deep moan as the skilled man works your pole."

    Marcus "I can't hold back anymore."

    Fen "Fuck me."

    "Your pleading desires are answered as the big guy presses the fat purple head of his cock against your oiled hole."

    play sound "audio/light gasp 1.ogg" volume 1.0
    Fen "Oh!" 

    #marcus penetrates cg
    scene marcus cg1 06b at center:
        zoom 1.5
    with dissolve
    "The thick tool slides in after the tip, spreading open your tight tunnel."

    play sound "audio/light moan 1.ogg" volume 1.0 loop fadein 1.0
    "Your muscles squeeze the man's girth as his cock throbs violently inside you."

    play nsfw1 "audio/deep growls 1.ogg" volume 1.0 fadein 1.0
    "Marcus huffs and pants against the side of your head as the aphrodisiac mix enhances every sensation."

    "His hands shiver as you sink down upon him."

    "Slowly his whole length pushes forward, driving deeper inside you."

    "The pulsating tip presses right against your prostate, throbbing right next to the sensitive organ."

    Fen "Fu-ah-fuck yeah."

    play fuck "audio/fuck mid 1.ogg" volume 1.0
    play ball "audio/ball hits 1.ogg" volume 2.0
    # add sweat and breath, fuck animation
    scene marcus cg1 06 at truecenter:
        zoom 1
    with dissolve
    "You moan with Marcus as he grinds his hips right into your butt, driving the rest of his rod up your tail hole."

    "The slick oil coating his cock allows his thick pole to plough right through your guts."

    "You groan as you feel your insides shift to accommodate the man."

    "His grip on you tightens as he huffs and humps, his hand pumps away at your needy arousal."

    "You whine as you drown in the ocean of sensations, riding every wave of pleasure that crashes over your being."

    "Marcus seems lost in his motions, holding and caressing with the occasional thrust that forces another deep moan from the bottom of your lungs."

    "The bigger male licks the sweat from your cheek and moans loudly into your ear."

    Marcus "Such a sexy body, you feel like you're ready to blow."

    "Your mouth fails to form words as Marcus grabs your balls, squeezing gently and rolling them in his palms."

    Marcus "That's it, let it out."

    play sound "audio/light moan 1.ogg" volume 1.3 loop fadein 1.0
    play fuck "audio/fuck fast 1.ogg" volume 1.0
    play ball "audio/ball hits 2.ogg" volume 2.0
    #Fuck faster now
    scene marcus cg1 06f at truecenter:
        zoom 1
    with dissolve
    "He works your cock faster, twisting just a bit each time his hand passes the head."

    "Every tweak, thrust, stroke, and rub brings you closer and closer to that earth shattering moment."

    Marcus "F-fuck, your ass feels like it's sucking it down!"

    "As he keeps thrusting, Marcus switches between stroking and groping."

    "He marvels as the various spasms in your body ravage your senses."

    "He starts to thrust and stroke faster until you simply explode."

    "In the moment your mind is overwhelmed, senses shut down one by one as they are overloaded."

    
    #Fen cum
    play sound "audio/light climax 1.ogg" volume 1.0
    scene marcus cg1 07a at truecenter:
        zoom 1
    with dissolve
    Fen "Ah-hh... Ahhhh!"

    "The sounds of the room fade away from the deafening beat of your heart. Your vision blurs and cock busts all over Marcus's hand."

    "Your seed explodes across his table as you seize up and unleash your pent up load."

    Marcus "Damn that's hot. I'm going to blow too."

    "He pulls you down and thrusts at the same time, slamming his entirety into you."

    stop nsfw1 fadeout 0.5
    stop fuck fadeout 1.0
    stop ball fadeout 1.0
    play vocal1 "audio/deep climax 1.ogg" volume 1.0
    #Marcus cum
    scene marcus cg1 08a at truecenter:
        zoom 1
    with dissolve
    Marcus "Grrrrr!!"

    "After a few more pumps, the purple giant's cock erupts inside."

    play sound "audio/light moan 2.ogg" volume 1.0 loop fadein 1.0
    "His torrent of virility floods your insides as you continue to empty your own nuts."

    "Your hole milks the man's cock for every drop he has to give while his hand does the same to yours."

    Marcus "Yeah, that's it. Cum for me."

    "He keeps stroking, working out shot after shot until only a few beads of pearly white cream run down your length and along his fingers."

    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
    play sound "audio/light moan 2.ogg" volume 0.5 loop fadein 1.0
    scene marcus cg1 09 at truecenter:
        zoom 1
    with s_dissolve
    #After cum
    "The man keeps holding onto you tightly as he finishes emptying himself until the excess cream gushes out from beneath your tail."

    "At this point, your insides are completely filled with his warm seed."

    "Despite being spent, you instinctively cling to his rod with your hole, not allowing much more to spill out."

    "You both pant heavily, murring and cooing as you rub against each other until the tingling subsides."

    stop nsfw1 fadeout 3.0
    stop sound fadeout 3.0
    #CG end
    scene bg bathhouse3 at center:
        zoom 1
    with s_dissolve
    "By the time you catch your breath, Marcus helps you off his lap."

    "The big man's cock slides out from your loose hole with a wet pop and his cum leaks out in a small stream."

    "Marcus nuzzles your neck and kisses your cheek before handing you a towel to clean off."

    show marcus naked smile at right1
    show bg bathhouse3_blur
    with dissolve
    Marcus "Whew, I think we both needed that."

    # if first time

    if marcus_sxp_1 == False:
        $ marcus_sxp_1 = True
        call sxp_up from _call_sxp_up_9
        Marcus naked normal "That mix you made... it's definitely something."
    
        Marcus naked grin "It really gets me worked up."
    
    else:
        pass

    show fen naked hot2 at left1
    with dissolve
    Fen "I'd love to do that again some time."

    $ bondexp06 += 3
    call bondexpup06 from _call_bondexpup06_9
    Marcus naked smile "Me too, you know where to find me."

    hide fen
    hide marcus
    show bg bathhouse3
    with dissolve
    "After taking a bath in the private pool, you get dressed again and returns."

    $renpy.end_replay()

    jump day_end

label khaleb_event_01:

    stop music fadeout 3.0
    scene bg tavern3
    with s_dissolve
    "You're in the middle of wondering how you could already be out of clean platters to serve the food when your eyes fall toward the back of the taproom."

    "It's that badger and his friends again, up to making their usual noise, it looks like."

    "Only this time, you notice that there's a big pile of finished plates stacked on the table between them, rising almost to the height of one of the chairs."

    Fen "({i} Woah, those guys must've ordered a whole feast tonight, huh? I can't believe I didn't notice. {/i})"

    show bg tavern4
    with s_dissolve
    "As you're going over, ready to collect the plates for washing, though, something pops into your mind: a word of warning from Gunther."

    "He had told you to stay suspicious of any customers who got big meals and finished them in a short amount of time."

    "It was a possible sign that they were going to dine-and-dash, eating their fill before ducking out as soon as they saw an opportunity."

    hide music fadeout 3.0
    "And that kind of behaviour definitely wouldn't surprise you with these three from what you've seen of them so far."

    play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0
    show bg tavern4_blur
    show trei smile at right3
    with dissolve
    Trei "Ba-hahaha! Scrap metal, leaves, and some twine? Is that what you said that thing was actually made of?"

    Trei normal "Oh, man, Khaleb dude! It's just too smooth every time I see you pull one over on chumps like that."

    show arek normal at left3, flip
    with dissolve
    Arek "But how didja get the stone in the middle of it to glow, like it was the real deal?"
    
    Arek "I thought you said your affinity couldn't make light."

    show khaleb grin at center1
    with dissolve
    Khaleb "Ey, top marks! That's right, Buddy Boy, it can't."

    Khaleb normal "Nothing's to say, though, that I couldn't hire a guy to magic up some chunk of glass for me so that it shined just how you'd think a real relic would."

    Trei stresse "Man, and to think I was worried about what would happen if we came back empty handed to a client like that."

    show trei smile at shock
    Trei smile "That dungeon he sent us to really kicked our butts!"

    show khaleb stern at flip
    show trei stresse
    with dissolve
    "Khaleb reaches over to grab one of the hound's nipples, and twists it hard enough to make him whimper."

    Khaleb stern "You mean that dungeon really kicked {i} your {/i} butt when you were stupid enough to get caught in that damn shock cage trap, huh!?"

    show khaleb at flipback
    with dissolve
    Khaleb "I'd figure you two mutts oughta know enough by now to show a little more appreciation for the guy who keeps saving your crummy {i} lives {/i}."

    Arek smile2 "Hey, don't look at me, bro. I'm just happy to be getting to eat all this food offa the Baron's coin."

    Arek smile "Uurp! Fuck. I don't think I remember my gut feeling this stuffed since the last time I went home for mating season..."

    Fen sweat "Um, excuse me?"

    show arek normal
    show trei normal
    show khaleb normal
    with dissolve
    "As the three turn to look up at you, any and all traces of cheer have vanished from their faces."

    "They're really not sparing any effort to make you feel as though you didn't just intrude on them."

    Fen sweat "Uh...S-So, how was everything?"

    Fen "Would you mind terribly if I left you the bill, now?"

    "They exchange glances, and the hound even points at you with his thumb while snickering to the others."

    Khaleb grin "Yeah, sure. We don't mind nothing."

    "He takes out a pretty sizable blue velvet pouch, filled almost to burst with coins, and drops it on the table."

    play sound "audio/payment.ogg" volume 3.0
    "It lands heavily right next to where he'd left his utensils, sending a spoon and knife clattering onto the floor."

    Khaleb normal "Tell you what, though: I'll let you fish however much of a tip you want out of this, if only you'll get me one more thing."

    Fen "Oh, well, of course. What'll it be?"

    Khaleb smile "A pair of whatever undies you got on ya right now; gently used, if you don't mind."

    Fen blush "W-W-Wha!?" with vpunch

    show arek smile2
    show trei smile
    with dissolve
    "The other two break out again into laughter once they see how much of a rise that got out of you."

    Khaleb normal "Whatsa matter? I know you ain't going commando under there, or nothing."

    Khaleb "I've been seeing those pretty, delicate things poking up out of those shorts all night. Even now."

    "You immediately look down, and self-consciously go to pull up your pants. He was right..."

    Fen blush "W-Why do you want them?"

    Khaleb "Because, I got a weakness for adorable little pups like you, see?"

    show khaleb smile at left2 behind arek
    with dissolve
    "He throws one of his beefy arms over the hyena-wolf's shoulders, and then gently lowers his hand down across his back."

    show arek blush at shock
    "You look on in shock as he gropes a handful of ass right in front of you, making his friend visibly shudder under the force of his iron grip."

    Arek blush2 "Rrrrffh! B-Bro...!"

    Fen blush "Woah! Uhhh...I mean..."

    Fen stern "I don't know. I don't really think I know you that well at all to just let you go with a favour like that."

    show khaleb normal at center1
    show arek blush behind khaleb
    with dissolve
    Khaleb "Okay. In that case, let's get around to making friends, then."

    Khaleb "Go ahead and ask me anything you'd wanna know..."

    Fen "Uh..."

    label khaleb_event_01_ask:
        pass

    menu:
        "Ask him anything you'd want to know? What would you even have to say to a guy like him?"
    
        "Just who exactly are you three?":
            $ khaleb_event_01_asked = True
            jump about_khaleb_adventurers

        "Did I overhear you swindled somebody?":
            $ khaleb_event_01_asked = True
            jump about_khaleb_trick

        "Why are you all so noisy every night?":
            $ khaleb_event_01_asked = True
            jump about_khaleb_noise

        "Would you be interested in tail service?":
            $ khaleb_event_01_asked = True
            jump about_khaleb_tail_offer

        "No more questions." if khaleb_event_01_asked == True:
            jump khaleb_event_01_after

    label about_khaleb_adventurers:

        Khaleb "Us? We're an adventuring party. Duh."

        show trei angry at shock
        Trei angry "What didja think we are, huh? Some clowns from a travelling circus troupe?"

        Trei "Cuz I left the last guy what thought that gaspin' an' groaning somewhere off deep in the sewers, I'll tell ya what!"

        Khaleb "Can it, Trei. No one wants to hear about that one hobo you blew for a shiny pebble."

        Khaleb "Anyways, folks around these parts call us 'The Renegades'. Any type of gig you might want covered, we'll take on the job."

        Khaleb grin "Provided, of course, that you're willing to accept the special...conditions of how we work."

        Fen "Just some more adventurers, huh? Honestly, I never would've guessed."

        Fen "You guys sure don't look or act much like any other adventurers I've ever seen."

        Arek normal "Why's that, huh? Is it cuz we look more like a buncha bandits to you, or something?"

        Fen sweat "Uh, well..."

        Fen "({i} What's a good way for me to tell them they do, without making them mad? {/i})"

        show khaleb smile at shock
        Khaleb "Ha! Don't sweat it at all, kid. We're used to every other yutz making that call as soon as they see us."

        Khaleb normal "It's a fucked up, judgmental world out here; ain't nobody gotta act like they're perfect in it."

        Trei stern "Wouldn't kill 'em to go and try for our sakes a little more, though..."

        Arek grin "Since when do you care about what some randos think of ya?"

        show trei angry at shock
        Trei "Since they started calling me all these mean names whenever they'd catch me making off with their stuff!"

        Trei sweat "Oh, oops! I mean, ehh, me taking interest on my cut of the pay. Hehe..."

        jump khaleb_event_01_ask

    label about_khaleb_trick:
        show arek angry at shock
        Arek angry "Ey, buzz off, if all you're gonna do is pry inta our business!"

        Fen "But I just..."

        show arek angry at shock
        Arek angry "But you what, huh? Huh!?"

        Khaleb stern "It's cool, Arek, it's cool. Lemme explain."

        Khaleb normal "So, ya know how Felda's got this big, hotshot baron lordin' over it, yeah? Well, he hired us to do a small favour for him."

        Khaleb "'Small' was his word for it, anyway, but after dippin' one toe in that mess of a place he sent us to, I'd swear it was anything but."

        Khaleb stern "We barely lasted thirty minutes..."

        Khaleb "That dungeon sent us packing; we wasn't gonna die! Not for no amount of gold, or glory, or whatever else it is that usually gets us tickled."

        Khaleb angry "But it also wasn't fair just letting it all go like that. My boys almost got put in the ground cuz of it."

        show trei smile at shock
        Trei smile "Woo! Yeah, bro! We love ya, too, bro~!"

        Khaleb normal "So yeah...I figured I didn't wanna just let the baron get off scot free with his big damn lie."

        Khaleb grin "We went back to him, anyway, and played a li'l old trick that somehow still has chumps fallin' for it to this day."

        Fen "Wait, but..but it sounds like you just faked completing a job because you were mad about not being able to do it."

        show khaleb stern
        show arek normal
        show trei angry
        with dissolve
        "The whole table shoots you a bunch of vicious glares."

        Khaleb normal "Ey, clean the grease out of your ears, if ya hafta."

        Khaleb "I just said we figured out the baron lied to us about the mission first, and so we figured it was only fair to give him a lie back and still keep the money."

        Arek smile3 "One good turn deserves another, they say."

        Khaleb "Uh-huh. And now, we're paying that forward, celebrating a job done right by havin' a few good meals here at your place of business."

        Khaleb smile "You're welcome for that, by the way."

        Fen "Hmm..."

        "You haven't heard very much about Felda's baron before, so you can't claim to know anything about his character, yourself."

        "But could somebody in a position like that really be trying to take advantage of adventurers by sending them on dangerous missions?"

        "Shouldn't the town be valuing the adventurers, who are bringing it more wealth and fame, if anything?"

        Fen stern "I'm sorry. I'll drop the topic now. It was wrong of me to assume."

        jump khaleb_event_01_ask
    
    label about_khaleb_noise:

        show trei stern at shock
        Trei "Noisy!?"

        show trei angry at shock
        Trei angry "NOISY!!!??"

        Trei "Not as noisy as your dad the last time I pumped him fat fulla my load, I bet!"

        Fen shock "W-W-Wait...! Are you...?" with vpunch

        Fen "Are you saying you know my dad!?" with vpunch

        hide khaleb
        hide arek
        show trei sweat at top:
            zoom 1.5
        show bg tavern4_blur at truecenter:
            zoom 1.5
        with dissolve
        Trei "Huh?"

        show trei:
            zoom 1.6
        with vq_dissolve
        Fen "Oh my gosh, where is he now? What's he been doing?" with vpunch
        
        show trei:
            zoom 1.7
        with vq_dissolve
        Fen "Is he looking for me?" with vpunch
        
        show trei stresse:
            zoom 1.8
        with vq_dissolve
        Fen "Didhesomehowgethimselfhurtandthat'swhyhehasn'tcomeheretogetmeyet?" with vpunch

        Trei "Wha...What the {i} hell {/i} ?"

        show arek normal at left3, flip
        show trei stresse at right3:
            zoom 1
        show khaleb normal at center1
        show bg tavern4_blur:
            zoom 1
        with dissolve
        Khaleb "Kid, it was just an insult. Calm down."

        Arek "Yeah, like, for real."

        Fen sad "O-Oh..."

        Fen "Sorry about that. I guess I got the wrong idea."

        Khaleb smile "Anyway, about the noise, right? Was there anybody complaining to you about how loud we was being while having fun?"

        Fen "Huh? Oh, well, yes actually. A couple of the other patrons have complained to me about it before."

        Fen "Now seemed as good a time as any to say something about it, I thought."

        Khaleb normal "Uh-huh. Well, wouldja mind passin' on a response from me to these other patrons, when ya get a chance?"

        Fen "Oh, sure thing."

        Khaleb grin "'Fuck off and go get your whistle wet at home, if you don't like it.'" 

        Khaleb "I hate pansies who think anywhere that's public owes them crap." 

        Khaleb "No one's forcing 'em to be stuck here with us, just like no one's forcing us to be stuck here with them." 
        
        Khaleb smile "But you see us dealing just fine and dandy, right?"

        Fen stern "I mean, it's not at all very considerate of the people who come here to relax and find some peace after a long day."

        Khaleb normal "Answer's still 'too bad.' They can meet me outside and try to win me over with their fists, if they feel so much about it."

        show arek smile at shock
        Arek smile "I can give ya a tip, though: just keep the food comin' and then we'll maybe have no reason to be so loud as we would otherwise."

        show khaleb smile at shock
        Khaleb "Heh. Second to that!"

        jump khaleb_event_01_ask
    
    label about_khaleb_tail_offer:

        show khaleb normal
        show arek smile3
        show trei normal
        with dissolve
        "All of their eyes go wide and maws fall open after seeing that you really have the boldness to ask them that upfront."

        "They don't seem so much surprised at your offer as they are delighted by it, though, you think..."

        Khaleb smile "We-hell now, I had a feeling this place had other good things to offer besides new food and cheap drinks, but I wasn't really sure what it was."

        Khaleb "Alright then, Fluff Butt. Tell me what's your angle with it. I'm all ears."

        Fen "My...my angle?"

        Khaleb normal "Yeah, ya know. Like price, location, limits, who's bringing what...if there's gonna be a group discount."

        Khaleb "I thought it was standard stuff, really."

        Fen "Oh. Well, uh..."

        Khaleb stern "Wait, wait, wait. Don't tell me you was trying to hook us without knowing any of it!"
        
        Khaleb grin "Geez, what kinda clueless pup are you?"

        Fen sweat "Um..."

        Arek smile2 "Ya think he's actin' out a part for us, bro?"
        
        Arek "Like, only pretending to be some ditzy, stiff-ass waiter to show us how he likes to play?"

        Trei smile "Ooh! Yeah, yeah! That's actually super hot, now that I think about it."

        Trei normal "Just imagine: he's an honest, cute-as-heck kid with big dreams, but all he's ever known is his shitty, dead-end gig, working at a tavern..."

        Trei blush "That is, until curiosity gets the better of him, and he has a run in with us."

        Trei "And one night of sweet love makin' at a time, he becomes addicted to a whole new world of possibilities!"

        Trei "So much that he decides to leave his awful boss in the lurch, and then–"

        play sound "audio/Punch.ogg" volume 1.0
        show khaleb at right2
        with vq_dissolve
        "The badger reaches over and punches him in the crotch." with vpunch

        show trei stresse at shock
        Trei stresse "Aaaagh!"

        show khaleb at center1
        with dissolve
        Khaleb "Sounds like you've got us interested, kid. Alright, we'll give you a try."

        Khaleb "Just slip us the details whenever you get a chance, and we can plan for some fun."

        Fen sweat "O-Okay. Yeah, sure, definitely!"

        Fen "({i} What the heck just happened? I barely even got to say two words for myself... {/i})"

        jump khaleb_event_01_ask

    label khaleb_event_01_after:

        Khaleb smile "Well, how 'bout it, then? Feel like you know 'nuff about us to not get all shrinky over my proposition?"

        Fen "Oh, right. That..."

        "Truth be told, you were kind of hoping that these talks would get him to forget about asking you for your delicates."

        Fen blush "Well..."

        menu:
            "Do you give him the underwear?"
        
            "Yes.":
                jump about_khaleb_underwear
            "No.":
                jump about_khaleb_no_underwear

        label about_khaleb_underwear:
            Fen "Okay, sure. You've got a deal."

            scene bg tavernback_night_blur
            with s_dissolve
            "You briefly excuse yourself to the backyard, where you change out of your underwear."

            "For just the rest of tonight, you don't think you'd mind it that much if you went without any."

            scene bg tavern4_blur
            show arek smile3 at left3, flip
            show trei normal at right3
            show khaleb normal at center1
            with s_dissolve
            "You return with them neatly folded in your paws, and present them to the badger."

            Fen stern2 "Here. These are as freshly used as the come."

            $ bondexp07 += 2
            call bondexpup07 from _call_bondexpup07
            Khaleb "That so, eh? Well, I'll be damned. That's good service."

            hide trei
            hide arek
            show khaleb smile at center1:
                ypos 2000
                zoom 1.5
            show bg tavern4_blur at truecenter:
                zoom 1.5
            show ratio1
            with dissolve
            "He snatches them from you and then proceeds to press them up against his nose, drawing out a long, deep sniff right in front of you."

            "He doesn't seem to be even a little put off at the surprise on your face after seeing this kind of flippancy."

            #get a bond point with Khaleb
            scene bg tavern4
            with dissolve
            Trei "So, bro? How's he doing down there?"

            "The hound is already leaning in close, trying to catch a whiff of it too."

            "In response, Khaleb turns around, acting like he's about to graciously hand them over."

            "Instead, though, he goes at the last second to hook them over his friend's horns, letting the underwear snap tightly over the hound's eyes and muzzle."

            "He and the other one laugh again, as Trei struggles at first to pull them off before soon easing back down the more he breathes through them."

            "You watch him give a thumbs up and grunt his approval at your scent."

            show khaleb normal at center1
            show bg tavern4_blur
            with dissolve
            Khaleb "Nice. Guess it's definitely a vibe, then."

            $ fen_coins += 20
            play sound "audio/payment.ogg" volume 3.0
            "Khaleb ends up giving you a fistful of coins to pocket along with the payment for their meals."

            "You receive a 20 coins tip."

            stop music fadeout 3.0
            scene bg tavern4
            with dissolve
            "You're left wondering if maybe doing that was actually going to end up encouraging their bad behaviour into becoming something more."

            $ khaleb_bond_ui = True
            call bondlvup0700 from _call_bondlvup0700

            jump work

        label about_khaleb_no_underwear:
            Fen stern2 "I'm sorry, but those are just too personal for me to give."

            Arek normal "Pfft. Aw, great. Another prude..."

            Khaleb normal "Alrighty then, Fluff Butt. We respect ya."

            Khaleb "Nothing excitin' for us means nothing excitin' for you, though."

            Khaleb grin "Oh. And better not lemme catch you with those pretty panties poking out again, ya hear?"

            Khaleb smile "I just wouldn't know if I'd be able to help myself...Ah-Hehehe!"

            stop music fadeout 3.0
            scene bg tavern4
            with dissolve
            "Both his eyes and his laughter send a chill down your back, as you walk away to let them sort out their bill."

            "When you come to clean up the table later, you see that they left you nothing for a tip."

            "You figure that it must be just the way it is for choosing to go a higher road sometimes."

            $ khaleb_bond_ui = True
            call bondlvup0700 from _call_bondlvup0700_1

            jump work

label khaleb_bond_01:
    stop music fadeout 1.0
    scene bg tavern4
    with dissolve

    play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0 
    show khaleb normal at right1
    show bg tavern4_blur
    with dissolve
    Khaleb "Yo, kid! Come over here for a minute."

    show fen stern at left1
    with dissolve
    Fen "Hm?"

    "You turn around to see Khaleb casually waving you down from the back of the tavern."

    hide fen
    hide khaleb
    show bg tavern4 at right:
        zoom 1.5
    show ratio1
    with dissolve
    "He and his friends are gathered around some sort of board game they've set up with a bag of dice, and..."

    "Are those the salt and pepper shakers from the other tables as the pieces!?"

    show bg tavern4_blur at center:
        zoom 1
    hide ratio1
    show fen sweat at left3
    with dissolve
    Fen sweat "({i} Ugh, what the heck is it gonna be this time...? {/i})"

    Fen "Yes?"

    show khaleb normal at right1
    with dissolve
    Khaleb "How's a reed like a writin' desk?"

    Fen sweat "Uh...W-What?"

    Khaleb stern "How's a reed like a writin' desk?"

    Fen stern "No, no. I heard you the first time. It's just...what?"

    show arek normal at right3
    with dissolve
    Arek "See? I toldja he'd have no clue neither."

    show trei normal at center1, flip
    with dissolve
    Trei "Well, I still like my answer the best: 'It's cuz you can make a desk outa reeds if you got the skill enough for it.'"

    Arek "That's stupid, though. Everybody knows desks are made from wood and not a buncha flimsy grass."

    Arek grin "I mean, what kinda crap ass desks were they making you write on back in school?"

    show trei angry at shock
    Trei angry "Fuck, I dunno!" 

    Trei stresse "What makes ya think I even went to school, huh!?"

    Fen sweat "Oookay...Well then, what's—"

    hide trei
    show trei stresse at center1, flip behind khaleb
    with q_dissolve
    Khaleb normal "In case you're wondering, we're busy practisin' our 'refined intellectualism' skills what ways we can."

    Arek grin "If we can show those big money-type nobles how we're a cut above the rest of the bozos in this line of work, we'll be set!"

    Arek smile "They're gonna be so impressed by the smarts we learned that new jobs'll be flowing in like fine wine."

    Khaleb "Yeah, it's the reason for me askin' ya that weird question."

    Khaleb grin "Apparently, it's a real riot at tea parties and stuff whenever somebody asks it. Couldn't say why, though."

    show trei stern at flipback
    with q_dissolve
    Trei stern "I'll bet it's an in-joke somebody's sister-aunt thought up one day while she was drunk off her rocker."

    Trei angry "Grrr! I swear, those moneybags had better send their manservant's manservant out to hand deliver us jobs for this."

    Trei stresse "My head's in so much pain from being full of all this damn learning, it's about ta explode..."

    Arek grin "Wow. Some part of you's full enough to burst and it ain't your balls for once? Colour me amazed."

    Fen sweat "Alright then, sure. That part I get. But, uh..."

    Fen stern "Why did you need to take the salt and pepper from the other tables?"

    Khaleb stern "Eh? Oh, that."

    Khaleb normal "That's just for...whatchacallit? Improv!"

    Khaleb grin "See, we also caught word of this ritzy board game the rich galoots like to play. Helps 'em whittle away the hours between foot baths, I guess."

    Khaleb "Chess is what it's called, or something. And we was lucky enough to find an ol' pawn shop at the corner of Riverside and Third that had a set up for sale."

    Arek normal "But thing is, the big bozo who owned the joint would'a charged us an arm and a leg for everything. So we had to make due with just the board."

    Khaleb stern "Meh, he was a shyster, that dumb cat. I ain't never liked their types."

    Khaleb smile "Anyway, kid, ya wanna try a round out with us sometime. Test the muscles in that peabrain you got?"

    hide fen
    hide khaleb
    hide trei
    hide arek 
    show bg tavern4 at right:
        zoom 1.5
    show ratio1
    with dissolve    
    "You eye the game they've got going curiously for a moment."

    "Trei goes to drag a pepper shaker across the black-and-red chequered board and uses it to knock over a salt one before removing it from play."

    "You quickly realise you have no idea what they're doing, and, apparently, neither do they."

    hide ratio1
    show bg tavern4_blur at top:
        zoom 1.5
    show arek normal at top:
        zoom 1.5
    with dissolve
    Arek "Hey, uh, actually bro, I've been wondering..."

    Arek sweat "Ain't there supposed to be all different types a' pieces in chess?"

    Arek "Like, how am I suppos'ta know which of mine are the knights and which are the queens?"

    hide arek
    show khaleb stern at top, flip:
        zoom 1.5
    with dissolve
    "Khaleb opens his mouth to speak, but then pauses for a minute, scratching the underside of his chin as he tries to think."

    Khaleb "Huh...Ya know, that's actually a hella good question..."

    show khaleb normal at flipback
    with dissolve
    Khaleb "Hey kid, you wouldn't happen to have any coloured pieces of twine lyin' about we could use, would ya?"

    hide khaleb normal 
    show bg tavern4_blur at center:
        zoom 1
    show fen angry at left3
    show khaleb normal at right1
    with dissolve
    Fen angry "Put. The shakers. Back. Where they belong!"

    show khaleb shock at shock
    Khaleb shock "Geez! Alright, alright. No need to blow yer top over somethin' like this."

    Khaleb normal "We'll put everything back, nice an' orderly for you...right after one more game."

    show fen angry at shock
    Fen angry "What!? No. Right now."
    
    Fen "This is something that could seriously get me in trouble!"

    Khaleb grin "With who? That lumbering, grizzled palooka in a smock?"

    Khaleb "Is he forcing ya to work here under good behaviour cuz of some kinda debt, or something?"

    Fen stern "It's not like that."

    Khaleb normal "Oh, yeah? Well, then why do ya take months—if not years—out your life working for him?"

    Fen "I...Well, it's because..."

    "You don't need to explain anything of yourself to them."

    show fen angry at shock
    Fen angry "My reasons are my own, and I'd thank you very much not to pry!"

    Khaleb grin "Tch, figures you'd say that..."

    show trei normal at center1, flip behind khaleb
    with dissolve
    Trei "Damn, bro! I can't believe you're really gettin' him to show some fang. I'm swooning over here! Ahaha!"

    show arek smile3 at right3
    with dissolve
    Arek smile3 "It is pretty funny that now of all times is when he decides to keep his trap shut, huh?"

    Arek "Wonder what nerve it was ya hit."

    Fen angry "Ugh..."

    Fen "({i} These guys. Sometimes, I swear... {/i})"

    Khaleb normal "Alrighty, Busy Boy, looks like we're all wrapped up with our game now."

    Fen stern "So, what? That means you're done with the shakers, then, right?"

    Khaleb "Yeah, yeah. Take 'em and knock yourself out. We've got an art showing on the East side to crash about now, anyway."

    Trei stern "Aww, is some rando gonna come up and ask me what I think about ladies who make statues for peoples' lawns again?"

    Trei stern "I don't really give a gnat's ass..."

    Khaleb smile "Don't worry, Trei. This one's about makin' life-sized figures outta dried up sewage and twigs. If that happens again, it's weird."

    Arek smile2 "Yeah, just make extra sure not to light any fires this time around, or else our noses are gonna be hot in the stink along with our purses."

    hide arek
    hide trei
    hide fen
    hide khaleb
    show bg tavern4
    with dissolve
    "Good. It looks like they're leaving early tonight."

    "You're not sure you'll ever get used to the odd, negative air that seems to hover around them like a curse wherever they go."

    stop music fadeout 2.0
    "At least you managed to get the tables back in their proper display before anybody noticed."

    call bondlvup0701 from _call_bondlvup0701

    $ ap == 0

    jump work

label khaleb_serve_01:
    "You bring out The Renegade's meals after struggling to listen to them talk over each other while giving you their orders."

    "Every day, it seems that at least one of their dishes comes out wrong, even though you know you wouldn't make those kinds of mistakes so easily."

    "It would be fine, though... if they just didn't wait until they were already half done with the dish to let you know..."

    "At least they pay for what they don't send back, otherwise, you're getting Gunther involved."

    $ bondexp07 += 1
    call bondexpup07 from _call_bondexpup07_1

    $ ap -= 1

    jump work

label khaleb_talk_01:

    if khaleb_talk_01_done == False:

        $ khaleb_talk_01_done = True

        stop music fadeout 1.0
        scene bg tavern4
        with dissolve
        "You go to Khaleb's table after hearing him loudly call you over."

        play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0 
        show khaleb normal at center1
        show trei normal at right3
        show arek smile3 at left3, flip
        show bg tavern4_blur
        with dissolve
        Khaleb "Yo, kid, we need somethin' over here!"

        Fen "Yes, what is it?"

        "({i} Oh, please don't be trouble with another patron, again... {/i})"

        Khaleb grin "The boys and I are bored. Entertain us with somethin', will ya?"

        Fen shock "Huh!?"

        Fen "W-With what? It's not like I'm here as a performer?"

        Khaleb stern "I dunno. We got a request here, it's your job to try an' take care of it somehows, right?"

        Arek grin "Why don't ya think up some good ways to keep us talkin' for a bit?"

        Arek "You're always wastin' time yammering with all the other chumps here, anyway."

        Fen "Hmm...Well, I guess..."

        "Can you think of any questions you've been meaning to ask them?"
    
    else:
        stop music fadeout 1.0
        scene bg tavern4
        with dissolve
        "You find the time to approach the Renegades' table again."

        play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0 
        show khaleb stern at center1
        show trei stern at right3
        show arek normal at left3, flip
        show bg tavern4_blur
        with dissolve
        "They all make eyes at you coming towards them unprompted."

        "Was there something else you thought of to ask them?"
    
    menu:
        "Why are the three of you always together?":
            jump about_renegades_together
        
        "Why do you always seem to have issues with the food?":
            jump about_renegades_food_issue

        "What's it like always causing so much trouble?":
            jump about_renegades_troublemaking

    label about_renegades_together:

        Khaleb normal "Why wouldn't we be? I mean, we toldja we're a team and all."

        Fen "Yeah, but like, I don't think I've ever seen a friend group that spends so much time together like you three do."

        Arek normal "You thought we've been calling each other 'bro' so much just for the heck of it?"

        Arek grin "Nah, that's what being a Renegade means, ya see?"

        Khaleb smile "'Brothers by choice even stronger than blood, an' lovers with hearts more wicked than fate.'"

        Khaleb normal "That's sorta the motto we roll with to sum it up."

        Arek smile2 "It was Trei who thought it up, too—the name and the sayin'—if you can believe it."

        Arek smile "I can tell ya straight away, I still don't! Eheehee!"

        Fen "Oh? That's interesting. What inspired you to come up with that for your team?"

        Trei stresse "..."

        Fen stern "Hm?"

        Trei stresse "..."

        #In small text, like he's mumbling
        Trei sweat "{size=20}I-It came to me in a dream. And...I just thought it sounded real cool, ya know...?{/size}"

        "That may be the quietest you've ever heard him speak."

        Khaleb smile "But anyways, yeah. We, bein' the fearsome Renegades, like to think of ourselves as more than just your average band a' mercs."

        Khaleb "We're sworn for each other to help make it best we can in this shitpot world; thick as thieves, and that ain't always figurative neither."

        show arek smile2 at shock
        Arek smile2 "Awoo-woo! Hell yeah, bro! You the best out there! We love ya!!!"

        call bondexpup07 from _call_bondexpup07_7
        $ bondexp07 += 1
        Khaleb smile "That's right. And you'd do best to remember the name Renegades for as long as you can."

        Khaleb normal "Cuz our names are gonna be up there with the real legends someday, ya hear?"

        Fen sweat "Uh, yeah sure. I'll take care to keep that in mind..."

        "({i} How would it even be possible for me to forget their name when they keep shouting it all the time...?{/i})"

        $ ap -= 1

        jump work
    
    label about_renegades_food_issue:

        Khaleb stern "And what is that suppos'ta mean?"

        Fen "Well, you know..."

        Fen "It just feels as though every time you three order food here, at least one of you has some kind of complaint to make about it."

        Fen "'This pudding's too milky' or 'This bowl doesn't have enough soup in it'. Stuff like that."

        Khaleb "Tch. It's not our faults if your kitchen makes mistakes."

        Fen "Y-Yes, but every time? With {i} every {/i} dish?"

        Trei smile "Well, maybe if you guys ever made stuff better in-lined with our refined tastes, we'd have less reason to give yas complaints."

        Fen "Okayyy...Which would be...?"

        Khaleb normal "Oh-hoh? You're really open to takin' our requests on this?"

        Fen "Yup, uh-huh."

        "({i} Anything to keep them from calling me over so much, honestly... {/i})"

        show trei smile at shock
        Trei smile "Neat! I wanna see something that's real special and wows-all-around, ya know?"

        Trei normal "Stuff that got, eh...sliced truffles in it, the good stuff. Or what about some of those fish eggs ya hear about? The tiny black ones."

        show trei smile at shock
        Trei"Oh, oh! Or how about some real gold that you just take and shred all over the food 'til it sparkles?"

        Fen "({i}Are you kidding!? Those ingredients are gonna cost a fortune to find!{/i})" with vpunch

        Arek smile3 "Well, I dunno about the rest of yous, but lately I've been itchin' ta try a live animal like I hear some folks will eat on a dare."

        Arek "It's usually something like small tentacles, so I guess I'd be down."

        Arek smile2 "Especially if you serve it to me with a little sauce on the side to help it go easier."

        Fen shock "({i}No way am I putting something like that on the menu! Do you have any idea how dangerous that sounds!{/i})" with vpunch

        Khaleb smile "Damn. You boys got some good answers."

        Khaleb normal "Looks like I'm gonna have to be the chump who gives a borin' one, but hey, at least it's honest."

        Khaleb "Okay, kid, listen up good. After mullin' it over, I think what I'm famished about the most here is the lack of any real bite to the menu."

        Fen "Bite?"

        Khaleb grin "Yeah, bite. Punch, kick, whatever it is ya'd wanna have done to you..."

        Khaleb "Point is, the food's gotta be the kinda stuff that'll make you recoil in your seat after taking the first bite."

        Khaleb "Gettin' past that makes it all worth the experience."

        call bondexpup07 from _call_bondexpup07_8
        $ bondexp07 += 1
        Khaleb smile "And if you ask me, the best way to have that effect is by pickling or fermentin'. But I'm sure there's other ways, too."

        Fen"({i}Ingredients that are pickled or fermented to the point that they—{/i})"

        Fen sweat "({i}Yeah...I can't really imagine how you'd get anything from that besides food that's just straight up rotten.{/i})"

        Fen "Well, uh...You've all certainly given me a lot to think about, for sure."

        Fen "I'll definitely go have a talk with my boss about it later and see what we can do."

        show trei smile at shock
        Trei "Sweet! I'll be looking forward to guzzling down a whole bucket of saffron tea next time."

        Fen "({i}Crud...{/i})"

        $ ap -= 1

        jump work

    label about_renegades_troublemaking:

        show khaleb stern
        show trei stern
        show arek normal
        "The three of them noticeably tense up and pass around a few uncertain looks."

        Arek angry "You askin' us that cuz you wanna gloat or cuz ya heard the rumours?"

        Fen "What? No, I'm asking to be serious. What rumours?"

        Khaleb stern "It's hard, kid. Growin' up with the types of backgrounds we all got in common's hard."

        Khaleb normal "I mean, don't get me wrong, I wouldn't know what to trade in my lived experience for, if I could."

        Khaleb "But it's hard. Cuz of what some people'll think of us the first time they get a good whiff."
        
        Fen "Oh..."

        Fen "Well, I'm sorry if you three being who you are gets you looked down at by others."

        Fen "That must be terrible, but there has to be some way you could get everybody to relate."

        show khaleb smile
        "He laughs at that, sharply and cruel."

        Khaleb grin "So you're tellin' me you think you can ever know what it's like being me? Or any of us?"

        Khaleb "Kid, we're terrors in this world, and do you know what the word 'terror' means?"

        Khaleb "Cuz it ain't just what you think of feeling when you snuff out the lights before bed."

        Khaleb "It's the way that all things fall apart after takin' so long to get built; it's the things you and I don't know, but wanna ourselves otherwise."

        Khaleb stern "You can see it in a guy who's got an idea in his head that's just too scary brillant to pass on for anything. And I mean {i} anything {/i}."

        Khaleb stern "Or, ya can see it in a bad memory that doesn't wanna leave the earth: the pain and regrets of somebody or something that got lost way too soon."

        Khaleb "Imagine now, that you've got a piece of somethin' like that baked into ya when you're still young, like a cake made a' shit."

        Khaleb "Every day of your life's bound to be a struggle, pushing back against the one question that always comes poppin' inta your head: 'What if? What if...?'"

        Khaleb "That much mayhem and doubt find its way inta your blood, if not your very soul."

        Khaleb "But society, bein' what it is, still expects ya to try and act all 'normal' for it. Best you can, at least, up 'til it decides it's tired."

        Khaleb normal "So, that's just what me an' the boys here do. And I like to think we've been doin' pretty alright with it so far."

        Khaleb "Still sound like the kinda thing you'd wanna host a meet-and-greet about, though?"

        Fen "Oh, wow...I-I had no idea."

        Fen "Do you really have to live with so much bitterness over it, though?"

        Arek "..."

        Trei "..."

        Trei angry "You don't know what I'd think to do to ya right now, if it wasn't for this room fulla people here to judge me."

        Trei "Count your fuckin' blessings for it, pretty boy..."

        show khaleb stern at right2
        with dissolve
        show trei stresse at shock
        "Khaleb elbows Trei in the stomach, which is enough to get him to stop leering at you."

        show trei stern
        show khaleb normal at center1
        with dissolve
        Khaleb "But, yeah. Anyways, we've all gotta learn to cope with our pasts in our own ways. Some being more convincin' at it than others."

        Khaleb grin "Take that big boss man a' yours. I can tell he's been scarred by something real nasty before, plain as day."

        Fen "Wait...What!? Gunther!?"

        Fen "No way! He's the one of the kindest, most humble and supportive people."

        Fen "There's no way he'd have something so dark in common with you. You've gotta be wrong."

        Khaleb smile "Hey, believe whatever it is you want, kid. It's your right."

        Khaleb normal "But just remember, despair ain't something you can just learn to get rid of or ignore once you got it."

        Khaleb "It stays with you, rattlin' about, as it grows and grows..."

        Khaleb "Until the day comes when you just can't stop it all from coming out in some big, beautifully ugly sorta way..."

        Fen "..."

        Arek "..."

        Trei "..."

        Khaleb smile "I take it we're all done talkin' about this, then."

        $ ap -= 1

        jump work

#Mjolnik
label mjolnik_home:

    #manage visits to Mjolnik
    if mjolnik_visit_01_done == False:
        jump mjolnik_visit_01

    else:
        pass

    if mjolnik_visit_02_done == False:
        jump mjolnik_visit_02

    else:
        pass

    jump mjolnik_generic_visits

label mjolnik_visit_01:

    stop music fadeout 3.0

    scene bg kitchen
    with dissolve
    "As you're packing a snack to bring with you, you hear Gunther behind you."

    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    show gunther normal at right1
    show bg kitchen_blur
    with dissolve
    Gunther "Got plans for your day off?"

    show fen 2 normal at left1
    with dissolve
    Fen "Sure do, just hit me when I got up."
    
    show fen 2 smile at shock
    Fen "It's really early, so I'm going to go visit Mjolnik!"

    show gunther stern
    show fen 2 stern
    "The tiger gives you a surprised look. As he stares at you, you begin to fidget nervously, wondering if he's going to object."
    
    show gunther normal
    "Then he smiles."

    Gunther "That sounds like a good day. It's a pretty easy trip to his farm."
    
    Gunther "I mean it's a straight walk. Bit long but if you're up for the trek."

    show fen 2 smile
    "You nod, smiling broadly at this sort of unexpected support from Gunther."

    Fen 2 normal "I know, but it's really early. So if I leave soon, I'll be there before noon."
    
    Fen "I can spend the night there or at Terrance's and be back by early afternoon tomorrow to help with the cleaning up."

    "Gunther nods."

    Gunther normal "Sounds like you have it all planned out."
    
    Gunther normal "Just let the gate guard know where you're going and when you'll be back."
    
    Gunther smile "You have a good trip and I expect to see you back by clean up time tomorrow!"

    "He gives you one last smile before turning around and heading back up the stairs."

    Gunther normal "Now if you'll excuse me, I'm going back to bed. It's unhealthy to be up this early."

    hide fen
    hide gunther
    show bg kitchen
    with dissolve
    "Snickering a bit at that, you finish packing a snack for yourself."
    
    "Grabbing a small rucksack, you store your supplies and walk outside."
    stop music fadeout 3.0
    scene bg tavernfront
    with s_dissolve
    "Taking a deep breath, you start off on your journey."

    play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
    scene bg townstreet
    with s_dissolve
    "You nod politely and make some small talk with the few people you meet until you reach the gate."
    
    show guards stoic normal at left1
    show bg townstreet_blur
    with dissolve
    "One of the guards is there, standing at attention, halberd at the ready."

    show fen 2 normal at right1, flip
    with dissolve
    Fen "Morning Guardsmen. Great day today?"

    show guards at flip
    with dissolve
    "The guard turns and you know he is looking at you but he says nothing. Shuffling awkwardly you continue."

    Fen "Ummm, I'm going to visit a friend who lives on a farm outside of town. I'll be back probably tomorrow afternoon."

    hide fen
    hide guards
    show bg townstreet
    with dissolve
    "The guard still remains silent but you do see him nod his head. Giving him a smile you walk past him."

    #If you serviced the Stoic Guard before
    if sguards_sxp_1 == True:
        "As you pass by the silent guard, you jump as he slaps you hard on the rump."
        
        "His hand stays there for a moment, squeezing your ass and you hear his voice."

        show guards stoic grin at center1
        show bg townstreet_blur
        with dissolve
        SGuard "Good boy. I'll pass that on."

        hide guards
        show bg townstreet
        with dissolve
        "He lets your ass go and returns to his previous state of attention."
        
        "You look over your shoulder at him and notice his pants are bulging just a little more."
        
        "You lick your lips, determined to find the time to service the silent one again."

    else:
        pass

    stop music fadeout 3.0
    #travel music
    scene bg black
    with s_dissolve

    play music "audio/The-Fire-of-Druids.ogg" volume 1.0 fadein 3.0
    scene bg road1
    with vs_dissolve
    "Walking down the path, you try to keep a fast pace as you know the trip is a few hours at least."
    
    "You don't know how long exactly as you were asleep the last time you made it but Terrance seemed to indicate it would take him three to four hours."
    
    "You're sure you'll make it faster because you're not hauling a heavy cart."

    scene bg sky
    with s_dissolve
    "About an hour later you pause to take a rest."
    
    "Looking around you, you realise that Felda is completely out of view and you can see nothing but fields and woods all around you, with some isolated buildings here and there."

    "You're struck by how scenic it is but also how desolate it seems. You scan the road and surrounding fields but fail to see anyone at all."
    
    "You knew that most people in this area live in Felda or in the surrounding villages but you expected to see at least one or two travellers."

    "You realise how lonely it must get for Terrance, as he spends most of his days walking back and forth along this route."

    "Shrugging your shoulders, you grab some of the food from your rucksack and eat it while continuing your trip."
    
    "As you walk, you begin to notice a few landmarks that Terrance had pointed out when you both had walked back from his house."

    "An old bridge to nowhere, half collapsed over a stream."

    scene bg forest1
    with s_dissolve
    "A grove of trees where Terrance said he'd sneak a nap if tired on his route."
    
    "You detour to check, but the grove is empty."
    
    scene bg sky
    with s_dissolve
    "You've been walking for a while now, and it feels like you're getting close."

    "Finally you see a broken old cart, one of the last things you'd pass to Mjolnik's farm and you slow down, making sure you don't miss the turn off."

    stop music fadeout 3.0
    #Scene show farm
    scene bg village
    with s_dissolve
    "Seeing the dusty path, you turn and walk down it and soon Mjolnik's farm comes into view."

    play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
    show mjolnik smile at top:
        zoom 1.5
    show bg village_blur at left:
        zoom 3
        ypos 2000
    show ratio1
    with s_dissolve
    "You smile as you see the young bull in the fields on his knees, you assuming weeding the crops."
    
    show mjolnik smile at top:
        zoom 1.5
        ypos -750
    show bg village_blur at left:
        zoom 3
        ypos 1900
    with move
    "You also notice like last time, he's fully naked."
    
    scene bg village
    with dissolve
    "Cupping your hands to your mouth, you call out."

    Fen "MJOLNIK!!! It's me [name]! I've come to visit you like I promised!"

    "You watch the bull glance up in surprise as he hears his name and even from this distance you can see the enormous grin on his face."

    show bg village at truecenter:
        zoom 1.5
    with dissolve    
    "He gets up and dashes towards you, so fast you're worried he's going to knock you clean off your feet, but instead he grabs you in a bearhug and twirls you both around." with vpunch

    $ bondexp10 += 5
    call bondexpup10 from _call_bondexpup10
    Mjolnik "Well butter my biscuits! Y'all did come to visit!"

    "He stops twirling the pair of you but continues to hug you close even as your feet hit the ground again."
    
    "Remembering what Terrance said, you simply return the embrace. Eventually he lets you go and beams at you."

    show bg village_blur:
        zoom 1
    show mjolnik smile at center1
    with dissolve
    Mjolnik "Sure does make this a special day now dunnit?"
    
    Mjolnik normal "Let's get y'all inside and grab some vittles. Y'all must be hungrier than a newborn critter." 

    hide mjolnik
    show bg village
    with dissolve
    "Turning, he walks quickly to his house and you almost have to run to keep up with him."
    
    scene bg mjolnik_home
    with s_dissolve
    play sound "audio/Door Open 2.ogg" volume 1.0
    "As you step inside the farmhouse, you are again struck by not only how cosy it feels, but by the wonderful aroma of all the various herbs and spices Mjolnik has."
    
    "Grabbing a chair he offers it to you."

    show bg mjolnik_home_blur
    show mjolnik smile at center1
    with dissolve
    Mjolnik "Plant yer arse down [name]! I'll grab us some drinks n' food and we can chat for a while. Sure do appreciate y'all visiting!"

    hide mjolnik
    show bg mjolnik_home
    with dissolve
    "The bull hustles in the kitchen area, swiftly ladling up some bowls of stew and a few mugs of water, placing them on the table and sitting down."
    
    "You notice he's beaming ear to ear."

    show mjolnik normal at right1
    show bg mjolnik_home_blur
    with dissolve
    Mjolnik "So what brought y'all to my neck of the woods? Just to visit?"

    show fen 2 smile at left1
    with dissolve
    "You nod and smile back at him."

    Fen 2 normal "Pretty much that. I said I would and I try to keep my promises."
    
    Fen 2 smile "Plus it was a beautiful day and I got up really early."

    show mjolnik smile
    "Mjolnik beams at you and begins to eat."
    
    hide mjolnik
    hide fen
    show bg mjolnik_home
    with dissolve
    "You also start eating and you notice the stew, while simple, is quite tasty and seems to be spiced even better than the last time you were here."
    
    "As you savour the meal, you see the bull is staring at you quite intensely."

    show bg mjolnik_home_blur at truecenter:
        zoom 1.5
    show mjolnik smile at top:
        zoom 1.5
    with dissolve
    Mjolnik "After y'all were here last time, I got to thinking about all the spices."
    
    Mjolnik normal "So I tried adding more. I went a bit crazy with it. Crazy as a shithouse rat."

    "You can't help but chuckle at that and sample the food again, this time really trying to taste the flavours."
    
    "While you would have done a few things different, like less salt, it's a very well done soup and you tell Mjolnik as much."

    Fen "You did a great job. This is delicious!"

    Mjolnik blush2 "Aw shucks. Y'all making me blush."

    "You notice the bull is indeed blushing, and you find that adorable."
    
    show mjolnik normal with q_dissolve
    "The pair of you finish the meal and while relaxing, you decide to ask Mjolnik about a few things."

    jump mjolnik_visit_talk

label mjolnik_visit_02:
    scene bg fenroom
    with s_dissolve
    "You go back up to your room and plop down on your bed and think about your options."
    
    "Thinking of the promise you made to one young innocent bull with an adorable smile, you decide to visit Mjolnik again."
    
    stop music fadeout 3.0
    scene bg kitchen
    with s_dissolve
    "Quickly getting ready, you bound downstairs to get some snacks for the road and are surprised to see Guther in the kitchen, having breakfast."

    show gunther normal at left1, flip
    show bg kitchen_blur
    with dissolve
    play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
    Gunther "Morning [name]."

    "He sees your surprised look and rolls his eyes."

    Gunther stern "Yes, I know I'm up early, woke up and couldn't get back to sleep. What are you up to today?"

    show fen 2 normal at right1, flip
    with dissolve
    Fen "I'm going out to visit Mjolnik again."

    "Gunther pauses and looks at you with a raised eyebrow."

    Gunther "Out to see him again? You must like him if you're willing to go all that way to see him."

    Fen 2 blush "Now hold on, it's not that..."

    Gunther normal "Granted, I don't know much about him. Just who he vaguely is and where he lives."
    
    Gunther "Terrance has mentioned him a few times. I've never met him. I don't even know if he's ever been to town."

    show fen 2 normal at right2
    with dissolve
    "You grab some fruit, slices of bread, a thick slice of beef and a few bottles of water and put them in a rucksack."
    
    show gunther stern with q_dissolve
    "You see Gunther giving you a bit of a stinkeye."

    show fen 2 stern at right1
    with dissolve
    Fen 2 "It's not that much for a trip. Sheesh."
    
    Fen 2 normal "But yeah, Mjolnik says he doesn't like the town much. He did say he'd come in with me someday though."

    "Gunther nods. Getting up to head back upstairs, he pauses and speaks."

    Gunther normal "Well, you have a fun time. You know what I expect from you."
    
    Gunther normal "But if you do bring him to visit, make sure to bring him here."
    
    Gunther wink "I'd like to meet him. And see if he's willing to give me deals on fresh produce."

    hide fen
    hide gunther
    show bg kitchen
    with dissolve
    "He winks at you before vanishing from view."
    
    stop music fadeout 3.0
    "You laugh to yourself about his mercenary tendencies and head out to start your trip."

    scene bg townstreet
    with s_dissolve
    play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
    "You again say hello to the various folk you meet and when you reach the guard gate, you notice that the guards are busy doing a changeover."
    
    "There's a new guard there you notice. He seems to be ordering the other guards around and is carrying a large shield and an ornate halberd."

    "One of them notices you and calls out to where you're going and when you'll be back."

    stop music fadeout 3.0
    "You reply and the guard waves you on through. You wave back and head on your way, though you do wonder about the new guard."

    scene bg road1
    with s_dissolve
    play music "audio/The-Fire-of-Druids.ogg" volume 1.0 fadein 3.0
    "The trip is much the same as the last. You remember a few more of the various landmarks and housing and even see someone heading towards Felda."
    
    "You say hello to them in passing, but they simply nod, smile and keep going."

                    #**********

    #If your SXP is greater than X
    if FenSXP >= 10:
        play sound "audio/bondexpup.ogg" volume 2.0
        "{color=#16f58d}{i}SXP Check 10 - Success{/i}{/color}"

        "As you're walking down the road, you get the faintest whiff of something."
        
        show bg:
            zoom 1.5
        show ratio1
        with dissolve
        "You stop in puzzlement as you try and identify the scent."
        
        "You know you should recognize it and you realise that you're suddenly getting an erection."

        "That puzzles you even more as there's no reason for that to be happening."
        
        "As you begin to walk further down the road, the smell grows a bit stronger."
        
        "A familiar scent of musk and earth and you look over to your left and see a grove of trees and suddenly you know exactly what the smell is."

        stop music fadeout 3.0
        scene bg forest1
        with s_dissolve
        "Walking slowly over to the grove, your ears perk up as you hear the unmistakable sounds of someone pleasuring themselves and you know exactly who it is..."
       
        "Terrance."

        "This is the grove he told you he'll sometimes sneak a nap in if he gets tired during his daily routes and it appears he uses the privacy of the grove for something more."

        show bg:
            zoom 1.2
        with dissolve        
        "You quietly creep closer and eventually come to the treeline and can see inside the grove."

        show bg forest1_blur:
            zoom 2
        show terrance naked blush3 at top:
            zoom 2
            ypos 100
        show ratio1 
        with dissolve
        "Sure enough you see Terrance, sitting on a log, cock in hand."
        
        play fuck "audio/fuck mid 1.ogg" volume 2.0 fadein 1.0
        "He is leaning back and his eyes are closed and there is a blissful expression on his face."
        
        "You feel a bit guilty spying on him and wonder if you should leave him to his private time."

        menu:
            "Leave him be.":
                stop fuck fadeout 3.0
                scene bg road1
                with s_dissolve
                "You smile and take one last look at the horse before sneaking quietly back to the road."
                
                play music "audio/The-Fire-of-Druids.ogg" volume 1.0 fadein 3.0
                "While it might have been fun to spy on him, and you're almost sure he wouldn't actually mind, something about it seems wrong."

                "Besides, if you want to get your claws on the massive horse, you're sure you can easily enough."
                
                "Smiling at that thought you continue on your way to Mjolnik's."

            "Enjoy the show.":

                #Maybe a flag here
                $ terrance_jerk_seen = True
                "Leaning against a tree, you slide your hand into your own pants and begin to stroke yourself."
                
                show terrance hard normal:
                    ypos -1100
                    xpos 1400
                show bg:
                    ypos 1000
                with dissolve
                "You get fully hard, your eyes are drawn to Terrance's massive cock."
                
                "As he pumps his hand up and down the shaft, you lick your lips at the sight."

                scene bg forest1
                with dissolve
                "Knowing you're safely concealed in the tree and Terrance is fully engrossed in his activity, you pause to strip naked yourself."
                
                "You slide off the rutsack and quickly peel off your shirt, tossing both on the ground."
                
                "Soon your pants join them and you stand there, hidden in the trees in just your underwear, which is tenting pretty nicely."

                "But soon you peel them off and kick them aside."
                
                show bg forest1_blur:
                    zoom 1.2
                show fen hard hot2 at top:
                    zoom 1.5
                    ypos -250
                with dissolve
                "You stand there fully nude, watching the horse jerk off and you start to match your own motions to his."
                
                "The fact that you are watching him and being naked in public is a potent aphrodisiac and you begin to rub your body."

                "Running your hands over your chest, you gently tug and squeeze your nipples and whine softly to yourself as they get hard."
                
                "Flicking your fingers over the sensitive nubs, makes you wish that the horse was licking them, but you decide that you do not want to risk revealing yourself."

                hide fen
                show bg forest1 at truecenter:
                    zoom 1
                with dissolve
                "The pair of you stand there, your movements synchronised in a strange dance of desire, as Terrance gets closer to climax, you hear him speak."

                #If you have not had sex with Terrance before
                if terrance_bond_03_sex_done == False:
                    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked blush3 at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    Terrance "Ooo, Gunther lad... just like that... pull me tail lad. Pull it extra hard, ye know how that gets me going."

                    show terrance hard normal:
                        ypos -1100
                        xpos 1400
                    show bg:
                        ypos 1000
                    with dissolve
                    "You watch the horse lick his lips as he says that and he begins to stroke himself faster and faster."
                    
                    "Even from the distance you're at, you can see his balls beginning to tighten against his body and you know the show is about to reach its climax."

                    stop nsfw1 fadeout 3.0
                    stop fuck fadeout 3.0
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked blush4 at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    Terrance "Fuck yer pretty pony! Fuck me hard Gunther!"
                    
                    play vocal1 "audio/deep climax 1.ogg" volume 1.0
                    Terrance "Ah... even harder lad, I can take it... Oooo.... Gunther!!!" with hpunch

                    "With that final utterance, Terrence orgasms."
                    
                    hide terrance
                    hide ratio1
                    show bg forest1 at center:
                        zoom 1
                    with dissolve
                    "His whinny is loud but it does cover your own grunt as you also cum."
            
                    "As the pair of you pant in the afterglow, your mind finally reacts to what Terrance said."

                    "Seems the horse likes it a little rough, and especially likes having his tail pulled while being fucked."
                    
                    "As you try and quietly get dressed, you file that tidbit of information away."
                    
                    "You stop just before putting your shirt back on and quietly mutter to yourself."

                    Fen "Pretty pony?"

                    "You giggle slightly as you guess that must be some kind of love talk between the two."
                    
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked smile at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    "Glancing back, you see that Terrance is now sitting on the ground, his eyes still closed but you hear snoring coming from the horse."
                    
                    "Seems after blowing his load, he decided to take a nap."

                    "While a nap does sound good, you have somewhere to be."
                    
                    scene bg road1
                    with s_dissolve
                    play music "audio/The-Fire-of-Druids.ogg" volume 1.0 fadein 3.0
                    "Picking up the rucksack, you quietly leave the grove and walk back to the main road, peering in both directions to make sure no one sees you leaving the grove."

                    "Seeing no one, you get back on the road."
                    
                    "You grin to yourself about what just happened."
                    
                    "And the mental images of Terrance's massive body shuddering as he cums, his thick cock spraying his seed all over the grove fills your mind as you continue to Mjolnik's."

                #If you have had sex with Terrance before
                else:
                    play nsfw1 "audio/deep moan 1.ogg" volume 0.5 fadein 1.0
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked blush3 at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    Terrance "Ooo, [name] lad, get that arse up in the air and let me have a go at it!"

                    hide terrance
                    hide ratio1
                    show bg forest1 at truecenter:
                        zoom 1
                    with vpunch
                    "You almost fall over as you hear the horse mention your name."
                    
                    "You actually stop masturbating for a moment to make sure you heard him right."
                    
                    "And you did. Your heart skips a beat and you start to panic as you're sure Terrance has caught you."

                    "Why else would he mention you by name, unless he knows you're there and is letting you know it."
                    
                    "Your ears perk up and your face gets red as you hear all kinds of dirty things the horse wants to do to you."

                    "You then realise that Terrance hasn't in fact seen you."
                    
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked blush3 at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    "The horse is talking about all the things he wants to do to you in the future."
                    
                    "And from what he's saying, he really wants to bend you over and fuck you until you can't walk."

                    "And that makes you jerk off even harder."

                    show terrance hard normal:
                        ypos -1100
                        xpos 1400
                    show bg:
                        ypos 1000
                    with dissolve
                    "You picture yourself under the horse, on your hands and knees, ass high in the air."
                    
                    "You can almost feel the massive flared head pushing into your tailhole, seeking access."
                    
                    "You can feel your tight hole slowly giving way and then..."

                    stop nsfw1 fadeout 3.0
                    stop fuck fadeout 3.0
                    show bg forest1_blur:
                        zoom 2
                    show terrance naked blush4 at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    Terrance "Take it!"
                    
                    play vocal1 "audio/deep climax 1.ogg" volume 1.0
                    Terrance "Take me whole fucking cock, [name] ya gorgeous flaming bitch!" with vpunch
                    
                    scene bg forest1
                    with dissolve
                    "With that final bit of dirty talk, you erupt, spewing your seed everyone."
                    
                    "You struggle to not howl, but can't stop some moans. However those moans are drowned out by a thunderous whinny from Terrance as he cums."
                    
                    "As intense as your orgasm was, you know it pales to the one Terrance is feeling."

                    "You watch in amazement as multiple jets of cum fly over his broad shoulders, before a few lesser ones hit his chest."
                    
                    "The horse whinnies again in contentment and slides to the ground. As you clean up and get dressed you think about what just happened."

                    "Seems not only is Terrance more interested in you than you might have guessed, he seems to really want to bang you."
                    
                    "The thought makes your cheeks flush as you think you might want that as well. You curse how that is most improbable."

                    show bg forest1_blur:
                        zoom 2
                    show terrance naked smile at top:
                        zoom 2
                        ypos 100
                    show ratio1 
                    with dissolve
                    "Glancing back, you see that Terrance is still sitting on the ground, his eyes now closed and you hear snoring coming from the horse."
                    
                    "Seems after blowing his load, he decided to take a nap."

                    "While a nap does sound good, you have somewhere to be."
                
                    scene bg road1
                    with s_dissolve
                    play music "audio/The-Fire-of-Druids.ogg" volume 1.0 fadein 3.0
                    "Picking up the rucksack, you quietly leave the grove and walk back to the main road, peering in both directions to make sure no one sees you leaving the grove."

                    "Seeing no one, you get back on the road."
                    
                    "You grin to yourself about what just happened."
                    
                    "And the mental images of Terrance's massive body shuddering as he cums, his thick cock spraying his seed all over the grove fills your mind as you continue to Mjolnik's."

    else:
        play sound "audio/bondexpdown.ogg" volume 2.0
        "{color=#16f58d}{i}SXP Check 10 - Failure{/i}{/color}"

        pass

    #scene transition
    scene bg sky
    with s_dissolve
    "After some more uneventful travel, you're at the path that leads to Mjolnik's."
    
    "Sighing happily at the near end of your journey, you walk down the path, keeping an eye out for the bull."
    
    scene bg village
    with s_dissolve
    stop music fadeout 3.0
    "As his farmhouse comes into view, you look around, but don't see him anywhere."

    Fen "Crap... I hope he's not gone out. Not like he knew I was coming today."

    show bg:
        zoom 2
        xpos 0
        ypos 1500
    with dissolve
    "You walk up to the front door and pause."
    
    "You almost just walk in but realise that even if Mjolnik is easy going, that might be rude.cSo you simply knock loudly."
    
    "You heard a startled grunt from inside."

    Mjolnik "What in blazes?"

    play sound "audio/Door Open 2.ogg" volume 1.0
    show bg village_blur
    show mjolnik shock at center1
    with dissolve
    "The door swings open and you're greeted by a very confused Mjolnik, who just appears to have gotten out of bed."
    
    play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
    show mjolnik smile with q_dissolve
    "The bull rubs his eyes and his face breaks out into a huge smile as he recognizes you."

    $ bondexp10 += 5
    call bondexpup10 from _call_bondexpup10_1
    show mjolnik grin at shock
    Mjolnik "[name]! Well don't this just beat all?"
    
    Mjolnik normal "I was just thinking to meself, what could make this day even better and y'all just fall out of the sky!"

    "He goes to hug you but stops midway."
    
    show mjolnik blush3 with dissolve
    "He stands there a bit awkwardly with his arms half out-stretched."

    Mjolnik "Done forgot, Terrance said I gotta stop hugging people without asking. Seems I have a bad habit of that."

    show mjolnik at top:
        zoom 1.2
        ypos -100
    with dissolve
    "You shake your head and simply hug the bull."
    
    show mjolnik smile with dissolve
    "He makes a happy mooing sound and returns the embrace and you spend a good few minutes just standing there in each other's arms."
    
    "The fact you can lay your head directly on his chest is a bonus."

    show mjolnik normal at center1:
        zoom 1
    with dissolve
    "Eventually it's Mjolnik who breaks the hug and gestures inside."

    Mjolnik smile "Where's my manners, c'mon in, make yerself at home!"

    scene bg mjolnik_home
    with s_dissolve
    Fen "Thanks Mjolnik. Odd I didn't see you out in the fields?"

    "The bull laughs and plops down in a chair, before putting his hooves on the table."
    
    "Leaning back in his chair he grins at you."

    show mjolnik grin at top:
        zoom 1.5
    show bg mjolnik_home_blur at truecenter:
        zoom 1.5
    with dissolve
    Mjolnik "Oh, that's easy. I just took a day off."
    
    Mjolnik normal "I worked extra hard the past two days to get everything done. Reckon that'll give me the morning off at least."
    
    Mjolnik "I only got a few small chores to do later."

    "The two of you spend the next few hours just making casual small talk and enjoying a few snacks."
    
    show mjolnik smile with q_dissolve
    "You find that Mjolnik is extremely good at small talk, able to weave elaborate stories about the smallest incident."
    
    "He spends a good half hour telling a yarn about a mouse he saw a few days ago and you find it fascinating to listen to."

    "However, stories about mice aside, you do want to ask him about some other, more in depth topics."
    
    "So when there's a bit of a lull in the conversation, you do so."

    jump mjolnik_visit_talk

label mjolnik_visit_talk:
    
    menu:

        "About farming..." if mjolnik_talk_about_farming == False:

            $ mjolnik_talk_about_farming = True

            Fen "How do you like farming? Seems like hard work."

            show mjolnik smile
            "Mjolnik smiles and nods. He leans back and puts his hands behind his head."

            Mjolnik "Y'all have no idea how hard it can get. But I like it."
            
            Mjolnik grin "I'm good at it. Terrance says so and he knows so much. Granted he mostly grows root veggies."

            Mjolnik normal "His mitts are just too big to handle more delicate things, so he sticks to the hardy stuff."
            
            Mjolnik smile "But the turnips he can grow. Mhmm, delicious!"

            Mjolnik normal "But me? I handle grains and greens. Plus I grow some stuff for Eoghann."
            
            Mjolnik "Over the years he's taught me a few tricks to grow herbs. I'm right grateful to him."

            "You nod. Looking over the relaxed bull, you admire his musculature."

            Fen "Plus I guess it's a lot of hard physical work? You're pretty muscular. Looks really good."

            Mjolnik blush2 "Oh y'all could sweet talk the birds from the trees [name]!"
            
            Mjolnik blush "But yeah, all the labour makes me big n strong."

            Mjolnik grin "Almost as big as Terrance. Well, I reckon when I'm as old as him, I'll be just as big!"

            Mjolnik normal "But enough about that, I know farming isn't as interesting as most things. It's important, everyone likes a full belly."
            
            Mjolnik "Just not the most exciting. Unless y'all really like taters."

            show bg mjolnik_home_blur at truecenter:
                zoom 1
            show mjolnik smile at center1:
                zoom 1
            with dissolve
            "Mjolnik gets up and stretches, completely oblivious to the fact that he's naked and full on showing you his body."
            
            "He scratches his chest and smiles at you."

            jump mjolnik_visit_activity

        "About Terrance..." if mjolnik_talk_about_terrance == False:
            
            $ mjolnik_talk_about_farming = True

            Fen "So, how do you know Terrance anyways?"

            Mjolnik grin "I know that big ol 'hoss since I was a kid. He's a friend of the family."
            
            Mjolnik normal "He's always been around, helping to do things and he totes my produce to market."

            Mjolnik smile "Honestly, he's like a second pa to me. I reckon without everything he's shown me I would have burned this place to the ground five times over by now."
            
            Mjolnik normal "I owe him so much. I'd do anything for him."

            show mjolnik stern with q_dissolve
            "His face grows thoughtful for a moment."
            
            show mjolnik normal with q_dissolve
            "You see a split second of apprehension or doubt cross his features before it returns to his normal easy going smile."

            Mjolnik "I'm lucky, if I say so myself. I got so many good folk to help."
            
            Mjolnik "My ma and pa. My brothers. Terrance and ol' Eoghann."
            
            Mjolnik smile "Eoghann's like the papaw I never had."

            Mjolnik stern "..."

            Mjolnik "Sad thing is, I think his mind's getting a bit bad. He's old so I reckon that's normal."
            
            Mjolnik "I do worry about him, living alone in those woods. Maybe he should move here."
            
            Mjolnik smile "Oh well. He's a right stubborn ol' goat, so that'll never happen."

            show bg mjolnik_home_blur at truecenter:
                zoom 1
            show mjolnik smile at center1:
                zoom 1
            with dissolve
            "Mjolnik gets up and stretches, completely oblivious to the fact that he's naked and full on showing you his body."
            
            "He scratches his chest and smiles at you."

            jump mjolnik_visit_activity

        "About your family..." if mjolnik_talk_about_family == False:

            $ mjolnik_talk_about_family = True

            Fen "So, how about your family? I haven't seen them, so just wondering where they are?"

            show mjolnik stern with q_dissolve
            "Mjolnik gives you a slightly surprised look as if he wasn't expecting the question. He pauses for a moment before replying."

            Mjolnik normal "Well, they live in the city, so you wouldn't be seeing em here! My ma and pa are there and so are my two brothers."

            "You nod, wondering if you may have seen or even served his family at the Flagon and not even known. But your thoughts are interrupted by Mjolnik."

            Mjolnik smile "Yep. They love it in the city, all of em."
            
            Mjolnik normal "Not for me though, I don't like the city. Too busy. I rather the country."
            
            Mjolnik "But my pa, Snorri and my ma, Beltyn, wanted to retire there, so left me the farm, packed up my brothers and left. "

            Mjolnik "I miss em but I got to keep working the farm and make em proud."
            
            Mjolnik grin "Pa always said that as the oldest son, I'd get the farm and make him proud."

            "He gives you a broad smile, but you sense a hint of sadness. It's obvious he misses his family."

            Mjolnik smile "And I reckon I'll make em both right proud!"

            show bg mjolnik_home_blur at truecenter:
                zoom 1
            show mjolnik smile at center1:
                zoom 1
            with dissolve
            "Mjolnik gets up and stretches, completely oblivious to the fact that he's naked and full on showing you his body."
            
            "He scratches his chest and smiles at you."

            jump mjolnik_visit_activity

label mjolnik_visit_activity:

    if mjolnik_visit_01_done == True:

        Mjolnik "I need to go get those last few chores done."
        
        Mjolnik "Y'all welcome to come help a bit or watch. I sure don't mind."

        play sound "audio/Door Open 2.ogg" volume 1.0
        scene bg village
        with s_dissolve
        "Nodding you get up and follow the bull outside." 

        show bg village at left:
            zoom 3
            ypos 2000
        with s_dissolve
        "This time he goes over to one of the actual fields."
        
        "There's a large sack with a strap sitting there and when Mjolnik gets there, he puts it on and steps into the field."

        show mjolnik normal at center1
        show bg village_blur
        with dissolve
        Mjolnik "I needs to get a bit more seeding done. It's boring, but well, if y'all don't put the seeds in the dirt, y'all don't get no crops."

        Mjolnik "I only have the one seedbag so y'all ain't able to help here."
        
        Mjolnik "But if yer of the mind to lend a hand, I never did get to finishing off putting the hay in the barn."

        "With that, he begins to walk up and down the field, pausing every foot or so to plant a seed before moving on."
        
        "You think about what to do."

        jump mjolnik_visit_activity_menu


    else:
        pass

    Mjolnik normal "Enough jaw-jacking for now. I gots chores to do."
    
    Mjolnik smile "Y'all welcome to come help a bit or watch. I sure don't mind the company."

    "Nodding you get up and follow the bull outside."

    scene bg village
    with dissolve
    "Walking around the front of the farmhouse, you follow Mjolnik. He suddenly stops and points to a large garden filled with herbs."

    show mjolnik normal at center1
    show bg village_blur
    with dissolve
    Mjolnik "Well I was planning to weed and tend to the herbs before you came and to start on the hay. But I'll only be able to do one now."
            
    Mjolnik smile "Y'all showing up ate a bit of time. I reckon it was plum worth it, but.."

    hide mjolnik
    show bg village at left:
        zoom 3
        ypos 2000
    show ratio1
    with dissolve
    "He beams at you before going to the garden and getting on his hands and knees."

    "You'd swear the bull was teasing you, with how his ass was pointed directly at you, but you know from what Terrance told you, he's pretty innocent."

    "Still, nice view..."

    "You call out to Mjolnik who looks over his shoulder at you."

    hide ratio1
    show bg village_blur
    show fen 2 blush at left1
    with dissolve
    Fen "So anything I can do while you work?"

    show mjolnik normal at right1
    with dissolve
    Mjolnik "Hmm, reckon y'all can just watch me tend the herbs if that tickles yer fancy."
        
    Mjolnik grin "Or if y'all want to really be a dear, you can start on the hay for me."

    label mjolnik_visit_activity_menu:
        menu:
            "Watch the bull work." if watch_the_bull_work_done == False:
                $ watch_the_bull_work_done = True
                jump watch_the_bull_work

            "Help the bull with chores." if help_the_bull_with_chores_done == False:
                $ help_the_bull_with_chores_done = True
                jump help_the_bull_with_chores

    #menuWatch the bull work-

label watch_the_bull_work:
    scene bg village at left:
        zoom 3
        ypos 2000
    show ratio1
    with dissolve

    if mjolnik_visit_01_done == True:
        "You wince as you remember how sore you felt after tangling with that haystack and decide this time, you'll just relax."
        
        "Mjolnik doesn't seem to mind, so you get comfortable on a thick patch of grass."
        
        "You watch Mjolnik for a while and eventually you begin to forget he's even naked and watch how he works."
        
        "For such a large bull,  he's extremely delicate in what he does. He can work around the most fragile of plants without even breaking a leaf off."

        "But soon enough, the gardening loses your attention and you can't help but stare at the bull."
    
    else:
        "You watch Mjolnik for a while and eventually you begin to forget he's even naked and just watch how he tends the plants."
            
        "For such a large bull, he's extremely delicate in what he does. He can work around the most fragile of plants without even breaking a leaf off."

        "But soon enough, the weeds and herbs lose your attention and you can't help but stare at the bull."

    show bg village_blur
    show mjolnik smile at top:
        zoom 1.5
    hide ratio1
    show ratio1
    with dissolve        
    "The first thing you notice is the serene look on his face."
        
    "Mjolnik seems to be extremely content tending to his gardens."
        
    "Every so often, he'll stop to wipe some sweat from his brow or to replace the blade of grass he habitually chews on, but otherwise he's totally focused on his task."

    show mjolnik smile at top:
        zoom 1.5
        ypos -400
    with move
    "However, you finally just shrug and really look at his body."
    
    "He's completely oblivious so you don't even feel the need to be subtle."

    show mjolnik smile at top:
        zoom 1.5
        ypos -750
    with move
    "What really gets your attention is just how well endowed he is."
        
    "While you think he's not as big as Terrance, you're pretty sure that even soft, Mjolnik is bigger than a lot of guys who you've been with or seen."
        
    "You really are curious to how big he is fully erect."

    hide mjolnik
    show bg village
    with dissolve
    "But soon, even ogling the bull gets a bit tiresome and your mind wanders."

    stop music fadeout 3.0    
    "You know that when Mjolnik is done, he's going to be hungry. You decide to give him a treat and go back to the kitchen."

    scene bg mjolnik_kitchen
    with s_dissolve
    play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
    "You look around the kitchen to see what you could possibly make to surprise him."
    
    "One thing that catches your eye is a basket of freshly picked peas."

    show bg mjolnik_kitchen_blur
    show bean_01 at truecenter
    show ratio1
    with dissolve   
    "Picking one up, you sniff it before opening the pod to taste the peas."

    "They are crunchy, sweet and very tasty."
    
    hide ratio1
    hide bean_01
    show bg mjolnik_kitchen
    with dissolve
    "You look at the various spices and decide that maybe a pea soup would be nice."
        
    "Looking around more, you see a few bottles of milk and decide that a cream of pea soup would be best."

    "You sniff the milk to make sure it's not sour and it smells fine. You sample it and are blown away by how delicious it is."
        
    "You've had plenty of milk but something about this milk really catches your attention."
        
    "It almost seems like it's mildly spiced somehow and that adds to the flavour."

    "Happy with this discovery, you get to work."
        
    "You hum to yourself happily as you prepare the peas, shelling them and discarding any bad one, plus the odd unwelcome bug."
        
    "Once that's done, you grab a pot and fill it with water. Putting it on the fire to boil, you add the peas and wait for them to cook."

    "When done, you grab a mortar and pestle and ground them up."
        
    "Putting the paste back into the pot, you add a bottle of the milk and some spices and slowly simmer the soup."

    show bg mjolnik_kitchen_blur
    show soup04_10 at truecenter
    show ratio1
    with dissolve    
    "Multiple small tastes later, you think you have it just perfect and let it simmer and wait for Mjolnik."

    scene bg mjolnik_kitchen
    with dissolve
    "Your mind wanders and soon you're daydreaming, only keeping enough awareness to stir the soup so it doesn't burn."
    
    "You're shaken from your reverie by a loud voice, that of a very surprised Mjolnik."

    show mjolnik normal at center1
    show bg mjolnik_kitchen_blur
    with dissolve
    Mjolnik "What in tarnation smells so good? [name], were you cooking while I was working?"

    hide mjolnik
    show bg mjolnik_kitchen
    with dissolve
    "He doesn't wait for a reply as he walks up to the soup and bends over it to smell it."
        
    "As you're sitting next to the soup, the view is interesting to say the least."

    show bg mjolnik_kitchen at truecenter:
        zoom 1.5
    show ratio1
    with dissolve 
    "You also notice, being so close to the bull, that while he is sweaty from working outside, he doesnt smell bad at all."

    "Inhaling deeply, you get a little bit of musk, but it's mostly grass and fresh earth."
    
    hide ratio1
    show bg mjolnik_kitchen_blur
    show mjolnik smile at top:
        zoom 1.5
    with dissolve
    "Before you can dwell on that further, you squeak as the bull hauls you off your chair into another of his crushing bearhugs." with hpunch

    Mjolnik grin "[name], this is amazing! How'd y'all know sweet peas are my favourite food? I could just kiss you right now!"

    scene bg mjolnik_home
    with dissolve
    "As he lets you down and turns back to the soup."
        
    "But soon enough, the pair of you are at the table eating."
        
    "You only have a small bowl but Mjolnik polishes off the rest. When's he's done, the look of pure happiness on his face warms your heart."

    show mjolnik smile at top:
        zoom 1.5
    show bg mjolnik_home_blur at truecenter:
        zoom 1.5
    with dissolve
    Mjolnik "[name] this is the best thing to happen to me in so long. I can't thank y'all enough."
    
    Mjolnik normal "If there's anything I can do for y'all, just ask."

    "You smile back at him and simply nod, though you definitely can think of a few things off the top of your head."
        
    "But knowing how Mjolnik is, you decide to behave tonight."

    scene bg mjolnik_home
    with dissolve
    "The two of you spend the rest of the day making idle small talk, but you quickly find out that there are a few topics Mjolnik doesn't seem to be comfortable talking about."
        
    "He's quick to change the topic whenever his family is brought up, and knowing he's depressed about their absence, you don't prod too much."

    "He also is reluctant to talk much about Eoghann or Terrance, aside from stories of their shared past."
        
    "You quickly realise he idolises both of them and doesn't seem to want to dwell on anything negative about them."

    "But there's more than enough to chat about."

    show mjolnik smile at top:
        zoom 1.5
    show bg mjolnik_home_blur at truecenter:
        zoom 1.5
    with dissolve  
    "He seems especially fascinated with your talks of the Flaming Flagon, Gunther and the various people who frequent the tavern."

    Mjolnik normal "Surely, I'm not too keen on going to town. But if I went with y'all... maybe one day I'd go. Just to see."

    Fen "I'd happily take you there and show you the sights."

    show mjolnik blush with q_dissolve
    "Mjolink gives you a shy smile, but you notice his tails are wagging about frantically."
        
    "A sure sign the bull is excited."
    
    show bg:
        zoom 1
    show mjolnik smile at center1:
        zoom 1
    with dissolve
    "Suddenly he yawns and stretches."

    Mjolnik normal "When, I'm plum tuckered out. I'm going to hit the hay. You can stay in the room my parents used to use."

    "Mjolnik gestures to one of the closed doors on the far wall, before walking to the other. Opening it he pauses for a moment."

    Mjolnik "I'm right happy y'all came by [name]. I dunno why, but just being around you makes me feel all giddy."
        
    Mjolnik smile "You sleep tight. I reckon I'm gonna be up and working by the time you get out of bed, being a big city boy."
        
    Mjolnik normal "I know you have to get back there, so just head on out."

    show bg:
        zoom 1.5
    show mjolnik blush2 at top:
        ypos -500
        zoom 2
    with dissolve 
    "You get up and hug the bull."
    
    "You feel him tense up and chuckle about how he seems unsure how to act when he's the one being hugged."
    
    #show mjolnik blush with q_dissolve
    "Soon enough he relaxes and he returns the embrace, though this time you notice, he's a lot more gentle."

    stop music fadeout 3.0
    show mjolnik blush2 at top:
        ypos -200
        zoom 2
    with move
    "When you look up at his face, you see that he looks conflicted, like he's trying to figure out if he wants to do something and you notice he's leaning in towards you."

    menu:
        "Wish him goodnight.":

            show mjolnik at center1:
                zoom 1
            show bg:
                zoom 1
            with dissolve
            "Not wanting to potentially confuse him, you gently break the embrace and step back."
            
            show mjolnik blush with q_dissolve
            "You see him blush slightly but he still has the same happy grin."
            
            play sound "audio/Door Open 2.ogg" volume 1.0
            "Without a word, he steps into his room and closes the door and you walk to the other door, pausing for a moment before opening it."

        "See what he does":

            $ mjolnik_kiss = True

            "You think you know what the bull is up to, but you decide to let him make the move."
            
            show mjolnik blush3 with q_dissolve
            "He pauses and looks at you, and the confusion in his face is even greater."

            show mjolnik blush2:
                zoom 2.2
            with dissolve    
            "After a moment, he closes his eyes and kisses you."

            hide mjolnik
            show bg mjolnik_home
            show ratio1
            with dissolve
            "As he does, he slides his hands behind your head and you feel his fingers entwining in your mane."
            
            "You decide to follow his lead and run your own fingers through his hair."

            "You feel him trembling as he continues to kiss you and it's obvious this is something he is not used to doing."
                
            "You help him along, using vocalisations and your own body to guide him."

            hide ratio1
            stop music fadeout 3.0
            show bg mjolnik_home_blur
            show mjolnik blush3 at top:
                ypos -200
                zoom 2
            with dissolve
            "He breaks off the kiss and opens his eyes. You see that he is blushing furiously and is beginning to stammer in embarrassment."

            show mjolnik blush2:
                zoom 2.2
            with dissolve                  
            "You gently guide his face back down to yours and with a simple whine, convince him to kiss you again."

            "This time he's more confident and even begins to explore your muzzle with his tongue."

            "With a happy whimper, you open your mouth and let his tongue inside to press against yours."

            hide ratio1
            stop music fadeout 3.0
            show bg mjolnik_home_blur
            show mjolnik blush3 at top:
                ypos -200
                zoom 2
            with dissolve
            "Soon though, he breaks off the kiss and steps away. He grabs the door frame for support and gives you a worried look."

            Mjolnik blush3 "Umm, I... I hope I didn't just put my hoof in it. Y'all ain't mad or anything?..."

            "You reach up and gently rub the side of his face."

            Fen "Not at all. I rather enjoyed it."

            show mjolnik blush with q_dissolve
            "He lets loose a huge sigh of relief and the happy look returns."
            
            scene bg mjolnik_home
            with dissolve
            "Without a word, he steps into his room and closes the door and you walk to the other door."

            "Not bad for what you are pretty sure was his first time kissing someone."
            
            "You grin to yourself and pause for a moment before opening it."

    scene bg black
    with s_dissolve
    "The room is extremely plain with only a bed and a small table beside it."

    "You strip down and crawl into the bed, finding it quite comfortable."
    
    play sound "audio/Transition1.ogg" volume 1.0
    "Soon you nod off to sleep."

    pause

    jump mjolnik_visit_next_day

label mjolnik_visit_next_day:
    scene bg mjolnik_home
    with s_dissolve
    play sound "audio/birds.ogg" volume 3.0
    play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
    "Waking up the next morning, you stretch and get dressed."

    if mjolnik_visit_01_done == True:

        $ mjolnik_visit_02_done = True

        "As you leave the room, you can hear Mjolnik snoring in the other bedroom. You smile and decide to make him some breakfast before you go."

        show bg mjolnik_kitchen
        with dissolve
        "You find his baking supplies and make a loaf of fresh bread and put it in the oven to bake."
        
        "Soon the smell of fresh bread is filling the house."

        "You can still hear the snoring and shake your head at how sound Mjolnik seems to sleep." 
    
        "But you're glad he can sleep in. The bull is one of the hardest workers you know and deserves it."

        show bg mjolnik_home
        with dissolve
        "Once the bread is done, you place the loaf on the table and then look for more."
        
        "You find a basket of various fresh fruits and berries and quickly make a fruit salad from those and place it next to the bread."

        scene bg village
        with s_dissolve
        "Grinning to yourself, you gather up for things and quietly head out to start your walk back to town."
        
        stop music fadeout 3.0
        "As you do, you think about what happened on your visit and look forward to seeing the bull again soon."

        call bondlvup1001 from _call_bondlvup1001

        scene bg fenroom
        with s_dissolve

        "You return just in time to begin your workday."

        jump day_activity

    else:
        $ mjolnik_visit_01_done = True

        pass
    
    "Looking around the farmhouse, you see that Mjolnik is gone and there's a few bits of food left for you on the table."
                
    "You help yourself to them and when done, pack the leftovers to take with you on the trip back to Felda."

    scene bg village
    with s_dissolve
    "You spend a few minutes tidying up and when done, leave the farmhouse and set out down the path leading to the main road."
                
    "You fail to see Mjolnik anywhere as you walk and when you reach the main road you look down towards the village."

    "You're positive you see Mjolnik way down the road, but it could be your mind playing tricks on you."

    "Hitching up your rucksack, you start the long walk home, thinking about all the things that transpired on the trip."

    scene bg fenroom
    with s_dissolve

    "You return just in time to begin your workday."

    jump day_activity

label help_the_bull_with_chores:

    if mjolnik_visit_01_done == True:
        "You didn't help with the chores the last time you were here and feel a bit guilty about not helping out again."
        
        "You decide to help out with whatever needs doing. How hard could it be?"
    
    else:
        pass

    Fen "I could use a bit of exercise. What would you like me to do?"

    Mjolnik grin "That's mighty fine of y'all."
        
    Mjolnik normal "What I need today is the hay tossed into that ol' barn. There's a pitchfork there so just heave as much as y'all can into the barn."

    scene bg village at right1:
        zoom 3
        xpos 500
        ypos 1800
    show ratio1
    with dissolve
    "He gestures to a large barn off to the side of the farm."
        
    "You nod and walk over there."
    
    scene bg sky
    with s_dissolve
    "Around the far side are the barn doors, wide open with a pile of hay taller than the barn right in front of it."

    "You gawk at the massive mound of dried grass and see a single pitchfork stuck into the ground by the door."
        
    "Picking it up, you gaze solemnly at the pile before getting to work."

    scene bg village_blur at right1:
        zoom 3
        xpos 500
        ypos 1800
    show fen uw blush at top:
        ypos -300
        zoom 1.5
    show ratio1
    with dissolve
    "After an hour or so, you've stripped down to your undergarments due to the heat, exertion and the fact the hay was getting all inside your clothes and making you itch like crazy."
        
    "Though you're pleased to note that you've made a dent in the pile. Albeit a small one."

    scene bg sky
    with dissolve
    "Sighing you get back to work. Time blurs as you just focus on throwing as much hay into the barn as possible."
        
    "You eventually hit your stride and soon the pile begins to actually shrink."
        
    "More and more ends up stuffed into the barn and soon you have to use the pitchfork to ram the hay compactly into it."

    stop music fadeout 3.0
    show bg sky_blur
    show ratio1
    with dissolve
    "However, there is a toll."
    
    "Your muscles are screaming in pain with each heave and you find yourself panting for breath."

    scene bg black
    with dissolve
    "You force yourself to keep going, but eventually, you collapse into the now much much smaller pile and just lay there panting and wheezing." with vpunch

    Mjolnik "[name]!"

    show bg sky_blur
    show mjolnik shock at truecenter:
        zoom 2
        rotate 160
        ypos -500
        xpos 650
    with dissolve
    "You open one eye and see the bull crouched in front of you, a look of concern on his face."
  
    hide mjolnik
    show bg sky
    with dissolve
    "Without a word, he scoops you up into his arms and walks to the farmhouse."

    show mjolnik shock at top:
        ypos -500
        zoom 2
    show bg village_blur:
        zoom 2
    show ratio1
    with dissolve  
    Mjolnik "Dumb idjit! Y'all trying to kill yourself?"
    
    Mjolnik "Y'all just a city boy, y'all ain't used to doing this kinda farmwork!"

    "You whimper in response as you feel your entire body screaming in pain."
        
    "Mjolnik continues to chide you, but you know he's concerned."

    scene bg mjolnik_home
    with dissolve
    play sound "audio/Door Open 2.ogg" volume 1.0        
    "Arriving at the farmhouse, he simply kicks the front door open and rushes inside, before repeating the tactic on one of the two closed doors."

    show bg mjolnik_room
    with dissolve
    "Placing you down on the bed, he frowns."
    
    show mjolnik stern at center1
    show bg mjolnik_room_blur
    with dissolve
    Mjolnik "Don't y'all go anywhere, I'm gonna go get that salve and get you fixed right up!"

    hide mjolnik
    show bg mjolnik_room
    with dissolve
    "You actually chuckle a bit at that, as you're pretty sure you can't move, let alone go anywhere."
        
    "Soon, the bull returns holding a stone jug with a lid and some towels."
        
    "Setting the jug and towels down on the table, he sits on the bed beside you and begins to pick straw out of your fur."

    show bg mjolnik_room_blur at top:
        zoom 1.5
    show mjolnik normal at top:
        zoom 1.5
    with dissolve
    Mjolnik "Well, the pile's decently smaller, so there's that."
    
    Mjolnik grin "But y'all working so hard? That was as dumb as a three-legged goat entering a footrace."

    "He grins at you as he shakes his head."

    Mjolnik normal "Color me impressed [name]. But now I gotta fix y'all up and it's gonna suck."

    hide mjolnik
    show bg mjolnik_room at center
    show ratio1
    with dissolve
    "He opens the jug and you are instantly hit with a foul pungent odour that makes your eyes water."
        
    "You see that Mjolnik is reacting in much the same way."

    show mjolnik stern at top:
        zoom 1.5
    show bg mjolnik_room_blur at top
    hide ratio1
    with dissolve
    Mjolnik "This here is some kind of salve that will fix ya right up. But it stings like a swarm of angry bees."
    
    Mjolnik "And I gotta rub it over all y'all."

    hide mjolnik
    show bg mjolnik_room at center
    show ratio1
    with dissolve
    "Without a word, Mjolnik turns you over so you're lying on your stomach and he hauls off your underwear."
        
    "You'd normally say something but right now, all you can think about is the pain."
        
    "The pain that sharply increases as Mjolnik takes a handful of the slave and starts to smear it over your body and rub it in."

    Fen "ARGH!... Oooo... owww...." with hpunch

    Mjolnik "I said it was gonna hurt. But it'll help right fast, just wait. I just gotta get it past yer fur."

    "The bull continues to massage your upper back and shoulders and soon enough the pain does begin to vanish."
    
    "As he works his way down, you marvel at how the pain quickly dissipates as the salve is rubbed into your skin."

    "The smell is horrible though and you hope you can get a bath after."
        
    "Though you stop thinking about the smell as Mjolnik reaches your ass."
        
    "You assumed that he'd just skip over it, but the bull is through and soon you can help but moan as he massages your rump."

    "He even pushes just a little into your tailhole, which causes some interesting sensations with the salve and you feel yourself getting hard as he even rubs your taint."
        
    "However he soon moves on to your legs and feet."

    show mjolnik normal at top:
        zoom 1.5
    show bg mjolnik_room_blur at top
    hide ratio1
    with dissolve    
    Mjolnik "Can ya turn over [name]? Or do y'all need me to do it?"

    hide mjolnik
    show bg mjolnik_room at center
    show ratio1
    with dissolve
    "You struggle to flip over, but just flounder around."
        
    "Mjolnik laughs and helps you turn over."
    
    show bg mjolnik_room_blur
    show fen hard blush at top:
        zoom 2.5
        rotate -45
        ypos -1500
    hide ratio1
    show ratio1
    with dissolve
    "Your face is burning as you realise that you're still fully erect, but the bull doesn't seem to even notice as he goes to work on your arms and chest."

    "As he does, you can't help but moan in pleasure which makes Mjolnik pause."

    hide fen
    show mjolnik normal at top:
        zoom 1.5
    show bg mjolnik_room_blur at top
    hide ratio1
    with dissolve  
    Mjolnik "I'm right sorry [name], I know it hurts, I just gotta do yer belly and leg and around yer junk and I'm all done."

    hide mjolnik
    show bg mjolnik_room at center
    show ratio1
    with dissolve
    "As he works lower, you realise that Mjolnik thinks that he's hurting you and not arousing you."
        
    "Soon, he's working on your legs and the only part of you that is still stinging is around your crotch."
        
    "You feel his hands beginning to move there."

    scene bg black
    with dissolve
    "You close your eyes and just enjoy the feeling as he rubs his finger through your pubes and your inside thighs."
        
    "He pauses and asks a question, some concern in his voice."

    Mjolnik "Ain't no pain in yer actual junk is there? I'm not sure how y'all might have done something there but y'all moan a lot when I'm poking around there."
        
    Mjolnik "I can rub that too, but the salve might really sting."

    #If your SXP is equal to X

    $ config.menu_include_disabled = True

    menu:
        "Maybe just a little bit of the salve? (SXP 10)" if FenSXP >= 10:
            #Check SXP >= 10
            $ config.menu_include_disabled = False
            Fen "Well... it does hurt a little. Maybe just a little bit of the salve?"

            show mjolnik normal at top:
                zoom 1.5
            show bg mjolnik_room_blur at top
            hide ratio1
            with dissolve            
            Mjolnik "Ok [name], but if it gets too much tell me ok?"

            hide mjolnik
            show bg mjolnik_room at center
            show ratio1
            with dissolve
            "He wipes his hands off and dips one finger into the pot, taking out a small amount of the salve."
            
            show bg mjolnik_room_blur
            show fen hard blush at top:
                zoom 2.5
                rotate -45
                ypos -1500
            hide ratio1
            show ratio1
            with dissolve
            "Spreading it over his hands, he tentatively reaches over and wraps his hand around your erection."

            play vocal1 "audio/light gasp 1.ogg" volume 0.5
            "You gasp in both pain and pleasure as you instantly feel the effects of the salve."
            
            play music "audio/Schlop.ogg" volume 1.0 fadein 1.0
            "It burns slightly, but soon gives way to a pleasant warm sensation."
            
            "As Mjolnik begins to massage your throbbing dick between his hands, you can't help but whimper in happiness."

            hide fen
            show mjolnik stern at top:
                zoom 1.5
            show bg mjolnik_room_blur at top
            hide ratio1
            with dissolve  
            "You notice Mjolnik is staring intently at your cock, a look of concentration on his face."
            
            show mjolnik stern at top:
                ypos -800
                zoom 1.5
            show bg mjolnik_room_blur at top:
                ypos -500
            show ratio1
            with dissolve            
            "You glance down at his cock and are surprised to see it is completely flaccid."
            
            "The bull is obviously so oblivious to how you really feel, it's adorable and you decide to not clue him in."

            hide mjolnik
            show bg mjolnik_room_blur
            show fen hard hot2 at top:
                zoom 2.75
                rotate -45
                ypos -1900
                xpos 500
            hide ratio1
            show ratio1
            with dissolve
            "Soon enough, you feel an orgasm building and you squirm."
            
            "As you do, Mjolnik begins to jerk you off with one hand while also spreading the salve on your balls with the other."
            
            play vocal1 "audio/light gasp 1.ogg" volume 0.5
            "You gasp and partially sit up." with hpunch

            hide fen
            show mjolnik stresse at top:
                zoom 1.5
            show bg mjolnik_room_blur at top
            hide ratio1
            with dissolve  
            Mjolnik "I ain't hurting ya am I? Should I stop?"

            Fen "No, this feels amazing, just... Can you squeeze a little harder and rub the very tip a bit?"

            hide mjolnik
            show bg mjolnik_room_blur
            show fen hard hot2 at top:
                zoom 2.75
                rotate -45
                ypos -1900
                xpos 500
            hide ratio1
            show ratio1
            with dissolve
            "The bull simply nods and does as requested."
            
            "You begin to thrust in time with him and soon you know you're going to cum."
            
            stop music fadeout 3.0
            "You don't know what to do, so you simply let it play out."

            play sound "audio/light climax 1.ogg" volume 1.0
            show fen cum at top:
                zoom 3
                rotate -45
                ypos -1900
                xpos 200
            with q_dissolve
            "With a whine, you feel yourself cum and you shoot a thick load all over your chest and face, with a small amount getting on a surprised Mjolnik." with hpunch

            "The bull looks at you first in surprise and then a huge grin breaks out on his face."

            hide fen
            show mjolnik grin at top:
                zoom 1.5
            show bg mjolnik_room_blur at top
            hide ratio1
            with dissolve            
            Mjolnik "Tarnation! That must have worked!"

            play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0            
            Mjolnik smile "I know when I get all tense down there, I use a little bit of the salve and rub myself and then that happens and everythings all better."

            Fen "Whew... yeah, that felt amazing... sorry about the mess."
            
            scene bg mjolnik_room with dissolve
            "Mjolnik laughs and grabs one of the towels and quickly cleans you off."

            show mjolnik grin at center1
            show bg mjolnik_room_blur
            with dissolve
            Mjolnik "Schucks, I make a much bigger mess, so y'all don't worry that pretty little head about it. I'm just glad y'all feeling better."

            Mjolnik normal "Also, don't worry about the smell. That'll vanish in a few hours."
            
            Mjolnik "I saw yer nose wrinkle a few times. It's a right ripe stink ain't it?"

            "You nod and grin back at him."

            Fen "You can say that again, but it worked."
            
            Fen "Thanks for everything Mjolnik, I had a good time, even with the pain. I'm going to visit you again real soon OK?"

            Mjolnik smile "Y'all serious [name]? Shucks, I'm already thinking about when y'all gonna come back."
            
            stop music fadeout 3.0
            Mjolnik "I really like hanging out with ya."

            hide mjolnik
            show bg mjolnik_room
            with dissolve
            "With that, he leaves, closing the door behind you."

            scene bg black
            with s_dissolve            
            play sound "audio/Transition1.ogg" volume 1.0
            "And soon you're asleep."

            pause

            jump mjolnik_visit_next_day
    
        "I'm fine.":

            #If your SXP is less than X
            $ config.menu_include_disabled = False

            scene bg mjolnik_room with dissolve
            "You honestly think about taking advantage of the situation, but you're tired, still overall sore and just want to go to bed."
            
            "You let Mjolnik know you're ok and he grins at you happily."

            show mjolnik grin at center1
            show bg mjolnik_room_blur
            with dissolve
            Mjolnik "That's great [name]! I'm right glad y'all feeling better! I'll letcha get some shut eye and y'all have a good night."
            
            Mjolnik normal "I'll be up extra early to do some errands and chores, so just let yerself out and don't worry none about saying goodbye."

            Mjolnik smile "Also, don't worry about the smell. That'll vanish in a few hours."
            
            Mjolnik normal "I saw yer nose wrinkle a few times. It's a right ripe stink ain't it?"

            "You nod and grin back at him."

            Fen "You can say that again, but it worked."
            
            Fen "Thanks for everything Mjolnik, I had a good time, even with the pain. I'm going to visit you again real soon OK?"

            Mjolnik smile "Y'all serious [name]? Shucks, I'm already thinking about when y'all gonna come back."
            
            Mjolnik "I really like hanging out with ya."

            hide mjolnik
            show bg mjolnik_room
            with dissolve
            "With that, he leaves, closing the door behind you."
            
            play sound "audio/Transition1.ogg" volume 1.0
            scene bg black
            with s_dissolve
            "And soon you're asleep."

            pause

            jump mjolnik_visit_next_day
            

label mjolnik_generic_visits:

    hide fen
    show bg kitchen
    with dissolve
    "You decide to visit Mjolnik today. It's been awhile and you just want to see him again."

    stop music fadeout 3.0
    "Quickly packing a few snacks for the road, you set out."
    
    play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
    scene bg village
    with s_dissolve
    "The trip is uneventful and soon you're turning down the path to Mjolnik's farm."

    "You see the bull working in the field and call out to him."
    
    "He stops and waves, his normal broad smile visible even from a distance."

    call bondexpup10 from _call_bondexpup10_2
    $ bondexp10 += 3 
    show bg village_blur:
        zoom 1.2
    show mjolnik normal at center1
    with dissolve
    Mjolnik grin "Well ain't this just a right nice surprise!"
    
    Mjolnik normal "What brings y'all here today?"

    Fen "Just coming to say hello."

    $ config.menu_include_disabled = True

    menu:
        "What to do today?":
            $ config.menu_include_disabled = False
            $ mjolnik_visit_random = renpy.random.randint(1, 100)

            if mjolnik_visit_random <= 25:

                #"test option 1-25"
                jump mjolnik_generic_chores

            if mjolnik_visit_random <= 50:

                #"test option1 26-50"
                jump mjolnik_generic_cooking
            
            if mjolnik_visit_random <= 75:

                #"test option1 51-75"
                jump mjolnik_generic_massage

            if mjolnik_visit_random <= 85:

                #"test option1 76-85"
                jump mjolnik_haystack_2

            if mjolnik_visit_random <= 95:

                #"test option1 86-95"
                jump mjolnik_massage_front

            if mjolnik_visit_random <= 100:

                #"test option1 96-100"
                jump mjolnik_gold_in_field

            else:
                pass

        "About this fruit... (Need Ember Fruit)" if ember_fruit >= 1 and mjolnik_cooking_fruit_done == False:
            $ config.menu_include_disabled = False
            jump mjolnik_cooking_fruit

    #Generic Chores - 25% chance of happening
    label mjolnik_generic_chores:
        show mjolnik smile with q_dissolve
        "Mjolnik beams at you and gestures around the farm."

        Mjolnik normal "Well I reckon might be a bit of a boring visit."
        
        Mjolnik normal "I have a lot of chores I have to do, so y'all might wanna lend a hand if y'all of a mind."
        
        Mjolnik smile "Sooner I gets it all done, sooner we can relax."

        hide mjolnik
        show bg village
        with dissolve
        "You nod and ask what needs to be done. Mjolnik gives you a list of a bunch of small tasks that need doing. Most are trivial but time consuming."
        
        "As you start, you notice the similarities with all the minor tasks you and Gunther have to do to keep the Flaming Flagon running."

        "But you don't mind helping Mjolnik out. The chores he's asked you to do aren't overly hard, just tedious."
        
        "Some painting, some moving and some simple gardening."

        scene bg village at right1:
            zoom 3
            xpos 500
            ypos 1800
        show ratio1
        with dissolve        
        "However as you go behind the farmhouse you groan as you see that damnable pile of hay is still there."
        
        scene bg sky
        with dissolve
        "You stare at it balefully for a while and wonder if it's grown since the last time you had to deal with it."

        "Leaving that wretched pile of grass behind, you get back to the tasks at hand."
        
        "Soon you have all the painting done and move on to gardening."

        "Many weeds are slain by your hand and many garden pests were vanquished."

        scene bg village
        with s_dissolve
        "You're busy building a small rock wall when you hear Mjolnik calling out for you."
        
        "Leaving the rocks, you head to him and he greets you with one of his bearhugs."
        
        "By now you're rather used to them and enjoy them so gladly return the embrace. "

        show mjolnik smile at center1
        show bg village_blur:
            zoom 1.2
        with dissolve
        Mjolnik "Thanks so much! Y'all saved me so much time. Let's go eat and chat and just have a nice ol' night."

        scene bg mjolnik_kitchen
        with s_dissolve
        "And that's what you do. You offer to do some cooking and Mjolnik gratefully accepts."
        
        "The meal is simple but a success, with Mjolnik praising your cooking profusely."
        
        scene bg mjolnik_home_blur
        show mjolnik smile at center1
        with dissolve
        "After cleaning up, you spend some time talking about nothing."

        "It's mostly just you listening to Mjolnik tell stories about whatever he thinks about or remembers."
        
        "He is a good storyteller, so you don't mind, even when it's a mundane topic."

        stop music fadeout 3.0
        scene bg black
        with s_dissolve
        "After a few hours, the pair of you turn in for the night."
        
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly."
        
        pause

        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        scene bg mjolnik_home
        with s_dissolve
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."

        scene bg village
        with dissolve        
        "Once done, you bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        $ mjolnik_generic_chores_done = True

        scene bg fenroom
        with s_dissolve

        "You return just in time to begin your workday."

        jump day_activity

    #Generic Cooking - 25% chance of happening
    label mjolnik_generic_cooking:
        show mjolnik smile with q_dissolve
        "Mjolnik blinks at you as your stomach growls."
        
        scene bg mjolnik_home
        with dissolve
        "Giving you a slight grin he ushers you into his house."

        show mjolnik grin at right1
        show bg mjolnik_home_blur
        with dissolve
        Mjolnik "I mean I have some chores to do, but that stomach is making more racket than a bag of hammers being tossed down the stairs."

        show fen 2 normal at left1
        with dissolve
        "You nod."

        Fen "I actually am kinda hungry. I didn't eat much before I came down."

        Mjolnik normal "Well, y'all a much better cook than I am. Do y'all wanna do the cooking? Maybe show me some tips and tricks?"

        Fen 2 smile "Sure, love to."

        "And that's what you do."
        
        scene bg mjolnik_kitchen
        with dissolve
        "After taking an inventory of all the available ingredients, you discuss with Mjolnik what he thinks you should make."
        
        "Most of his suggestions are plain, but with a bit of subtle prompting, you get him to think of some fancier things."

        "Soon you're whipping up a tasty dish, explaining carefully to Mjolnik each step and why you're making it a certain way."
        
        "The bull is listening with rapt attention to your every word and you have to admit you really enjoy teaching him a little of what you know."

        show bg mjolnik_home
        with dissolve
        "Soon enough the meal is complete and you both sit down to eat."
        
        show bg mjolnik_home_blur at top:
            zoom 1.5
        show mjolnik smile at top:
            zoom 1.5
        with dissolve
        "Mjolnik is profuse with his praise, but you're quick to point out that it was his ideas for the food."
        
        show mjolnik blush with q_dissolve
        "He blushes at that but the smile on his face is heartwarming."

        stop music fadeout 3.0
        scene bg mjolnik_home
        with dissolve
        "Mjolnik insists on cleaning up and while he does, you start up a large fire as it's beginning to get chilly."
        
        play music "audio/fireplace.ogg" volume 2.0 fadein 2.0
        show bg mjolnik_home at truecenter:
            zoom 1.5
        show ratio1
        with dissolve
        "You then sit by the fire and stare into the flames."
        
        "There's always something entracing about them to you and you barely notice when Mjolnik joins you."

        show bg mjolnik_home_blur
        show fen 2 normal at left1:
            zoom 1.5
        show mjolnik normal at right1:
            zoom 1.5
        hide ratio1
        show ratio1
        with dissolve
        "He places an arm around you and pulls in you close."
        
        "The two of you wordlessly sit for hours just watching the flickering dancing flames until they die into gently glowing embers."
        
        stop music fadeout 3.0
        "When that happens, you both decide that's a good time to turn in for the night."
        
        scene bg black
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly."
        
        pause

        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        scene bg mjolnik_home
        with s_dissolve
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."

        scene bg village
        with dissolve        
        "Once done, you bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        $ mjolnik_generic_cooking_done = True

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        jump day_activity

    #Generic massage 25% chance of happening
    label mjolnik_generic_massage:
        show mjolnik stresse with q_dissolve
        Mjolnik "..."

        "You notice the bull seems to be in some distress."
        
        "He's frowning and whenever he moves in certain ways, he winces."

        Fen "Umm, are you doing okay? You seem to be in a bit of distress."

        Mjolnik shock "Huh, that obvious eh?"
        
        Mjolnik sweat "I went and did something to right mess up my back."
        
        Mjolnik "It's killing me and I can't seem to get it to want to work."
        
        Mjolnik "Plus, I can't even get Eoghann's salve onto it, cause it's the dead centre of my back. Just don't bend that way."

        "He gives a pained chuckle."
        
        "You think back to how effective that salve was when Mjolnik used it on you, so this is a fine time to return the favour."

        Fen "Give me the salve. I'll rub it in for you."

        Mjolnik normal "Really? Y'all be willing to do that for little ol' me?"

        Fen "Nothing little about you Mjolnik... in any way."

        "The innuendo goes straight over the bull's head, but you expected it to anyway."
        
        scene bg mjolnik_home
        with s_dissolve
        "You follow him into the house and he goes to his room, pausing at the door."

        show bg mjolnik_home_blur
        show mjolnik normal at center1
        with dissolve
        Mjolnik "Y'all mind if we use my room? I'm probably not gonna wanna move after so rather be already tucked in bed."

        play sound "audio/Door Open 2.ogg" volume 1.0
        "You nod and he opens the door."
        
        scene bg mjolnik_room
        with s_dissolve
        "You follow him inside and look around the room while Mjolnik slowly crawls onto the bed."
        
        "The room is rather plain, but there is a large shelving unit on the far wall that is packed full of various things."

        show mjolnik normal at center1
        show bg mjolnik_room_blur
        with dissolve
        Mjolnik "The salve's on that shelf on the far wall."

        "You nod and go to retrieve the jug."
        
        hide mjolnik
        show bg mjolnik_room
        with dissolve
        "There's a few jugs and jars on the shelf, but your nose quickly picks out the right one. You remember the pungent odour quite well."
        
        "The shelf is also filled with a lot of small knick-knacks of various types and somewhat unexpectedly, quite a few books."

        "You glance at the covers as you grab the jar and they all seem to be about herbalism, gardening and potions."
        
        "Your eyebrow raises as that last book was not something you expected to see."

        stop music fadeout 3.0
        show bg mjolnik_room at truecenter:
            zoom 1.5
        show ratio1
        with dissolve
        "Going back to Mjolnik, you can't help but admire his body."
        
        "He's face down on the bed, his head hanging over the end, most likely so his horns don't impale the bed."
        
        "His legs are just spread enough you can see his balls and you gulp at the size of them."

        "Shaking your head to dispel any erotic thoughts, you get to work."
        
        "Opening up the jug, you cough as the smell hits your nose."
        
        "You have no idea what Eoghann puts in this stuff, but does it ever make your eyes water."

        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "You also know first hand it works. Taking a decent handful, you begin to rub it into the bulls back."
        
        "At first you hear a few whimpers from him but soon, the whimpers turn to quiet sighs of contentment and even some gentle moo'ings of pleasure."

        "The fact Mjolnik actually moo'ed, made you chuckle a bit and you try to get him to do it again."
        
        "Firmly running your hands along the muscles, you gently knead each in turn. Which does indeed cause Mjolnik to make some more moo'ing noises."

        "You eventually get down to his lower back and can't help but stare at his rump."
        
        "His three tails are swishing back and forth, which only highlights his firm but rather plump behind."
        
        "You really want to just grab his cheeks and squeeze, but know it's not the time or place."

        "Going back up to his shoulders, you work some more salve into his shoulders and neck, finding it a bit difficult to get through the thick fur there, but eventually you do."
        
        "You expect more noises from Mjolnik but there's nothing but silence."

        stop music fadeout 1.0
        hide ratio1
        show bg mjolnik_room:
            zoom 1
        with dissolve
        "You kean over to look at his face and you see that his eyes are closed and he appears to have fallen asleep."
        
        "Shaking your head in amusement, you get up and return the jug to its original place."

        "Looking around the room, you grab a blanket that was tossed over a chair and spread it over the slumbering bull."
        
        "You quietly leave the room, giving the sleeping bull one last glance. He looks incredibly serene."

        stop music fadeout 3.0
        scene bg black
        with s_dissolve
        "Going to the other room, you get ready for bed yourself."
        
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly."
        
        pause

        scene bg mjolnik_home
        with s_dissolve
        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."
        
        "He does comment that his back feels amazing and he thanks you for helping him."
        
        scene bg village
        with dissolve
        "Once done, you bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        $ mjolnik_generic_massage_done = True

        jump day_activity

    #The Haystack Round 2 - 10% chance of happening
    label mjolnik_haystack_2:
        show mjolnik smile with q_dissolve
        "Mjolnik beams at you and gestures around the farm."

        Mjolnik "Well, I'm just about done here and I only have one last chore to do. I really need to finish moving that haypile into the barn. Wanna help?"

        "You grimace at the thought of that miserable stack of grass but sigh and nod your head."
        
        "At least with Mjolnik helping, it should go a lot faster."

        scene bg sky
        with s_dissolve
        "The pair of you go around the back of the farm to the barn and you stop in horror."
        
        "The pile has definitely been added too. It looks about the same size as the first time you tried to fill the barn."

        scene bg barn
        with dissolve
        "You peer into the barn and are surprised to see it's mostly empty... you look around in confusion." 
        
        "You know you filled this whole barn. Then you see a single piece of hay float down in front of you."
        
        "You watch it land at your feet and then you look up."

        "There's an entire second floor you didn't even know existed that is full of straw."
        
        "You assume Mjolnik must have transferred everything up over."
        
        "Sighing you pick up the single piece of straw and look at it forlornly."

        "Returning to Mjolnik, you offer him the straw and smiling, he takes it and sticks it in his mouth and begins to chew on it."

        show mjolnik smile at center1
        show bg barn_blur
        with dissolve       
        "He offers you a pitchfork and the two of you get to work."

        Fen "Sigh..."

        Mjolnik smile "Aw buck up [name]. We'll have this done faster than most people eating a fresh apple."

        hide mjolnik
        show bg barn at truecenter:
            zoom 1.5
        show ratio1
        with dissolve
        "You snort and get to work. Soon you get into a rhythm and the pile starts to shrink."
        
        "The fact Mjolnik is shovelling massive loads with each toss, is helping as well."
        
        "You begin to zone out as the time passes. Eventually you put the pitchfork in the ground by the barn to catch your breath."

        show fen 3 normal at top:
            zoom 1.5
            ypos -200
        show bg barn_blur
        hide ratio1
        show ratio1
        with dissolve
        "You peel off your shirt and toss it aside, picking bits of hay out of your fur."
        
        "As you do so you hear Mjolnik call out."

        Mjolnik "Hey [name]! Think fast!"

        show bg barn:
            zoom 1.7 
            rotate 20
        hide fen
        hide ratio1
        "You most certainly do not think fast as Mjolnik barrels you over right into the pile, driving both of you deep inside it." with vpunch
        
        "You yelp in surprise and try to scramble loose, but the bull hauls you back into the pile each time."

        "So, Mjolnik wants a war? Well, he's getting one!"

        show bg barn:
            zoom 1.7 
            rotate -20
        "You pounce on the bull and soon the two of you are rolling around in the pile, tossing hay at each other and laughing." with vpunch
        
        scene bg barn_blur at top:
            zoom 2
        show mjolnik smile at top:
            zoom 2
            ypos -200
        with dissolve
        "After a while, Mjolnik pins you to the ground, with your hands over your head and he straddles you."

        Mjolnik "Y'all sure are a slippery little cuss, but give it up [name], I got y'all beat!"

        "You try to struggle free, but have to admit the bull is far too strong and you simply nod."
        
        show mjolnik grin with q_dissolve
        "Mjolnik grins at you."
        
        show bg barn_blur at top:
            zoom 2
            ypos -400
        show mjolnik smile at top:
            zoom 2
            ypos -1200
        show ratio1
        with dissolve
        "As he does, you become very aware that his cock is laying directly on your stomach."

        "It's weighty enough you can feel it as you breathe."

        show bg barn_blur at top:
            zoom 2
        show mjolnik blush3 at top:
            zoom 2
            ypos -200
        hide ratio1
        with dissolve        
        "You try to avoid thinking about it and look back up to Mjolnik who has leaned in extra close and has a conflicted expression."
        
        scene bg barn
        with dissolve
        "You're sure he's going to kiss you but instead he leans further down and sniffs around your chest and underarms for a moment before quickly rolling off you."

        show mjolnik blush3 at center1
        show bg barn_blur
        with dissolve
        "He blushes and stands up, hay cascading off of him and covering you."

        Mjolnik blush2 "Sorry [name], just y'all smell so nice. Kinda like a fire y'all threw spices on."
        
        Mjolnik "Maybe we should get back to work."

        hide mjolnik
        show bg barn
        with dissolve
        "He turns and does so."
        
        "The two of you shovel about half of what's left into the barn before Mjoolnik calls it a day."

        show mjolnik smile at center1
        show bg barn_blur
        with dissolve
        Mjolnik "Thanks so much! Y'all saved me so much time."
        
        Mjolnik normal "Let's go eat and chat and just have a nice ol' night."

        scene bg mjolnik_home
        with s_dissolve
        "And that's what you do. You offer to do some cooking and Mjolnik gratefully accepts."
        
        "The meal is simple but a success, with Mjolnik praising your cooking profusely."
        
        "After cleaning up, you spend some time talking about nothing."

        "It's mostly just you listening to Mjolnik tell stories about whatever he thinks about or remembers."
        
        "He is a good storyteller, so you don't mind, even when it's a mundane topic."

        stop music fadeout 3.0
        "After a few hours, the pair of you turn in for the night."
        
        scene bg black
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly."

        pause
        
        scene bg mjolnik_home
        with s_dissolve
        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."
        
        "You haven't even bothered to get dressed, coming out in just your underwear."

        "You note during breakfast he is trying to sneak some peeks at you, especially if you stretch or lift your arms."
        
        "He's not good at hiding it though."

        "Once done, you quickly get dressed and get ready to head out."
        
        scene bg village
        with dissolve
        "You bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        $ mjolnik_haystack_2_done = True

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        jump day_activity

    #Cooking with passion(fruit) chance of happening (Maybe when you actually have the fruit.)
    #Buy from Murry, hints Mjolnik 
    label mjolnik_cooking_fruit:
        Fen "Say, can we go get something to eat?"
        
        Fen "I didn't have much to eat before I came down. Plus I wanna try something."

        hide mjolnik
        show dragonfruit_01 at truecenter
        show bg village
        show ratio1
        with dissolve
        "You reach into your rucksack and pull out that new fruit you bought from Murry."
        
        "You show it to the bull and he cocks his head as he looks at it."

        hide dragonfruit_01
        hide ratio1
        show bg village_blur
        show mjolnik normal at center1
        with dissolve
        Mjolnik "Ain't never seen no fruit that looks like that before."

        "Mjolnik blinks at you as your stomach growls."
        
        scene bg mjolnik_home
        with s_dissolve
        "Giving you a slight grin he ushers you into his house."

        show mjolnik normal at right1
        show bg mjolnik_home_blur
        with dissolve
        Mjolnik "I mean I have some chores to do, but that stomach is making more racket than a bag of hammers being tossed down the stairs."

        Mjolnik "Well, y'all a much better cook than I am. And something new? Reckon with that newfangled fruit you brought?"
        
        Mjolnik smile "Sure thing [name]. Maybe show me some tips and tricks?"

        show fen 2 smile at left1
        with dissolve
        Fen "Sure, love to."

        stop music fadeout 3.0
        show mjolnik grin at shock
        Mjolnik "That sure sounds exciting! What y'all planning"

        play music "audio/cookingbgm.ogg" volume 1.0 fadein 3.0
        scene bg mjolnik_kitchen
        with dissolve
        "You have to admit that you have no idea. But the first step is cutting them up."
        
        "You know Murry said they needed to be cut up and the seeds removed. The flesh could be eaten raw or cooked."

        "So that's where you start."
        
        $ ember_fruit -= 1
        show bg mjolnik_kitchen_blur at truecenter:
            zoom 1.5
        show mjolnik normal at right2:
            zoom 1.5
        show fen 2 normal at left2, flip:
            zoom 1.5
        show ratio1
        with dissolve
        "As you're cutting away, you feel Mjolnik behind you and soon enough, his arms wrap around your waist and he rests his head on your shoulder and he watches you intently."

        "You try to ignore him but he is holding you close and as usual, he is naked and his dick is big."
        
        "You feel it pressed up against your rump and you can't help but feel your own cock getting harder."

        "Shaking your head to dispel the thought you prepare the fruit."
        
        scene bg mjolnik_kitchen
        with dissolve
        "After only a few minutes you have a pile of the fruit ready to go and you pick up a piece and offer it to the bull who accepts eagerly."

        "As he's eating it, you try a piece yourself."
        
        "The fruit is quite sweet and has a bit of a spicy aftertaste you find enjoyable."
        
        "If the noises in your ear are correct, so does Mjolnik."
        
        show bg mjolnik_kitchen_blur at truecenter:
            zoom 1.5
        show mjolnik normal at right2:
            zoom 1.5
        show fen 2 normal at left2, flip:
            zoom 1.5
        show ratio1
        with dissolve
        "He shifts behind you and as he repositions himself, his cock ends up firmly resting between your cheeks."

        Mjolnik "Gosh darn, that's a sweet treat. Bit of a kick to it too. Can y'all feel the heat [name]?"

        "You indeed can. If you even had a tiny indication the bull wanted something, you'd be begging for him to take you right here and now."
        
        "But you can tell that Mjolnik is still flaccid and completely oblivious to the reactions he's eliciting."
        
        scene bg mjolnik_home
        with dissolve
        "You're both relieved and dismayed when he steps away to take a seat at the table."

        "Discreetly adjusting yourself, you grab some other fresh fruits Mjolnik has and make a fruit salad for the pair of you to eat."
        
        "By the time you're done, your erection has at least gone down and you bring the salad over to the table."

        "And it's a success! Both you and Mjolnik agree that the new fruit really adds to it and soon the whole bowl is gone."

        show bg mjolnik_home_blur:
            zoom 1.5
        show mjolnik smile at top:
            zoom 1.5
        with dissolve
        Mjolnik "Well after that delicious snack, I reckon I'm not gonna do any more work."
        
        Mjolnik normal "Let's just sit by the fire again [name]. That was right relaxing."

        stop music fadeout 3.0
        hide mjolnik
        show bg mjolnik_home:
            zoom 1.5
        with dissolve
        "Mjolnik insists on cleaning up and while he does, you start up a large fire."
        
        play music "audio/fireplace.ogg" volume 2.0 fadein 2.0
        "You then sit by the fire and stare into the flames."
        
        "There's always something entracing about them to you and you barely notice when Mjolnik joins you."

        show bg mjolnik_home at truecenter:
            zoom 1.5
        show ratio1
        with dissolve
        "This time he sits behind you and pulls you into him."
        
        "Without saying anything, he tugs at your shirt and you raise your arms and let him remove it."

        show bg mjolnik_home_blur at truecenter:
            zoom 2
        show mjolnik normal at left2, flip:
            zoom 2
            ypos 1900
        show fen 3 normal at right2:
            zoom 2
            ypos 1900
        hide ratio1
        show ratio1
        with dissolve      
        "Once bare chested, he pulls you flush against him and begins to just idly rub your chest."

        "Again, if you thought he wanted something sexual, you'd agree in a heartbeat, but Mjolnik seems more interested in just gently playing with the fur on your chest and stomach."
        
        "The heat from both the fire and the bull is relaxing and you enter an almost trance like state."
      
        scene bg mjolnik_home at truecenter:
            zoom 2
        hide mjolnik
        hide fen
        show ratio1
        with dissolve
        "As time passes, Mjolnik hands explore more of your torso, eventually ending up lightly scratching the thick hair above your waistband."
        
        "Without even thinking, you undo your pants and pull them down slightly."

        "With your pubes exposed, Mjolnik's finger entwines into them and gently caresses and tugs at the thick fur."
        
        "It's incredibly erotic but innocent at the same time and this time you don't even get aroused."
        
        "You just let him proceed and enjoy the sensations."

        show bg mjolnik_home_blur
        show image "gui/overlay/game_menu.png"
        with dissolve
        "More time passes and the fire dies down to embers. As the flames flicker out, Mjolniks hand goes back up to your chest and he hugs you for a few minutes."

        stop music fadeout 3.0
        "When he breaks the embrace and gets up, he offers you a hand and helps you to your feet."
        
        scene bg black
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
        "You feel completely relaxed and ready for bed."

        pause

        scene bg mjolnik_home
        with s_dissolve
        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        "You sleep extremely soundly and wake up refreshed."
        
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."

        scene bg village
        with dissolve        
        "Once done, you bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        $ mjolnik_cooking_fruit_done = True

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        jump day_activity

    #Massage the front - 10% chance of happening
    label mjolnik_massage_front:
        hide mjolnik
        show bg village:
            zoom 1
        with dissolve
        "You notice that Mjolnik seems to be in a bit of pain."
        
        "While he's trying to smile, he keeps rubbing his chest and every time he does so, a quick expression of pain flashes across his face."

        show fen 2 stern at left1
        show bg village_blur
        with dissolve
        Fen "Are you okay? Did you hurt your chest?"

        show mjolnik sweat at right1
        with dissolve
        Mjolnik "That obvious? Yeah, I was doing some chores and I guess I just twisted the wrong way."
        
        Mjolnik "Now it hurts to move in certain ways and everytime I try to massage it or put on Eoghann's salve, I just can't. Stings to much."

        Fen 2 normal "Maybe I can help put it on?"

        Mjolnik normal "Would y'all do that for me?"

        Fen 2 smile "Of course. Let go and get that salve and get you all patched up."

        scene bg mjolnik_home
        with s_dissolve
        "The pair of you go inside, Mjolnik goes into his room and returns with the jug of salve."
        
        show mjolnik normal at top:
            zoom 1.5
        show bg mjolnik_home_blur at center:
            zoom 1.5
        with dissolve
        "He hands it over to you and you motion for him to sit on the floor. He does so and you sit down behind him."

        "Opening the jug, your nose immediately wrinkles from the smell and you hear Mjolnik snort."

        Mjolnik grin "Smells awful, but sure does work."

        "You nod as you remember how effective it was on you."
        
        stop music fadeout 3.0
        hide mjolnik
        show bg mjolnik_home
        show ratio1
        with dissolve
        "Take a decent amount in your hand, you reach around and begin to rub it into the bull's chest."
        
        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "Mjolnik tries to stay silent but you do hear a few quiet whimpers as you work the salve through his fur."

        "As your hands go over his chest you brush over one of his nipples and you hear a sharp intake of breath and a pained yelp from Mjolnik."

        stop music fadeout 1.0
        scene bg mjolnik_home_blur at center:
            zoom 1.5
        show mjolnik blush2 at top:
            zoom 1.5
        with dissolve                
        "Pulling your hand away in concern who ask what was wrong."

        Mjolnik "Ah, didn't think it would be a problem, but guess with the salve and the pain... umm... "
        
        Mjolnik "I got another thing going on, nothing to do with the chest pain."
        
        Mjolnik "I'll tell y'all about it some other time. Just..."
        
        Mjolnik "[name], can y'all just avoid touching around my nipples for now?"

        "You wonder why the bull seems extra sensitive there but shrug."

        show mjolnik at top:
            zoom 2
            ypos -400
        show ratio1
        with dissolve
        "You simply move around to the front, so you can see exactly where you're rubbing and Mjolnik sighs in relief."

        Mjolnik "Thanks [name]. I'll tell y'all later."

        "While you are curious about what the bull might say, you do have a job and you set about doing it."
        
        play music "audio/Schlop.ogg" volume 2.0 fadein 1.0
        "Now that you can see his chest, it's easy to avoid the extra tender spots and work the salve in everywhere else."

        "You have to admit that you are enjoying this."

        "As you trace your hands over every contours of the bulls chest and abs, you can feel the muscles tense and relax under your fingers."
        
        "You even use the very tips of your claws on some points which causes the bull to gasp in pleasure."

        Mjolnik "Golly [name], I dunno what y'all doing but it feels good. Making me feel right funny though."

        "You notice that as you continue, Mjolnik closes his eyes and seems to be concentrating on something."
        
        show mjolnik hard normal:
            ypos -1000
            xpos 1200
        with dissolve
        "Glancing down, you see that for a change, the bull is actually erect and you do a double take."

        show mjolnik hard normal:
            zoom 2.2
            ypos -1300
        with dissolve        
        "You knew he was large, but now seeing him hard, you upgrade him to massive."
        
        "Though you're not trying to actually get him fully hard so you ease off a bit."

        stop music fadeout 1.0
        scene bg mjolnik_home
        with dissolve
        "Soon enough you finish and back away from Mjolnik, who gingerly touches his chest."
        
        "He then pokes it a few times before slapping it once."
        
        play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
        show mjolnik smile at center1
        show bg mjolnik_home_blur
        with dissolve
        "Smiling broadly he gets up. You're thankful on one hand that he's fully flaccid again."

        Mjolnik grin "Well don't that beat all. Everything is perfect! I feel like I could go throw a boulder in the creek!"

        show mjolnik normal with q_dissolve
        "He sees your expression and quickly shakes his head."

        Mjolnik "Now I ain't gonna do anything silly. I'm planning on having some supper and having an early night."

        hide mjolnik
        show bg mjolnik_kitchen
        with dissolve
        "And that's what you do. You offer to do some cooking and Mjolnik gratefully accepts."

        show bg mjolnik_home
        with dissolve        
        "The meal is simple but a success, with Mjolnik praising your cooking profusely."
        
        "After cleaning up, you spend some time talking about nothing."

        "It's mostly just you listening to Mjolnik tell stories about growing up with Terrance and Eoghann."
        
        "You find it odd that his family doesn't come up much, but you guess after moving to Felda, they don't come around often."
        
        "Though you find it odd they moved there when Mjolnik was still young, leaving him in the care of a few neighbours."

        stop music fadeout 3.0
        "After a few hours, the pair of you turn in for the night."
        
        scene bg black
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly."

        pause

        scene bg mjolnik_home
        with s_dissolve
        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."

        scene bg village
        with dissolve
        "Once done, you bid the bull farwell and begin your trip back to town, back to the Flaming Flagon."

        $ mjolnik_massage_front_done = True

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        jump day_activity

    #There's gold in that field - 5% chance of happening
    #Perhaps only once
    label mjolnik_gold_in_field:
        if mjolnik_gold_in_field_done == True:

            jump mjolnik_massage_front
        
        else:
            pass

        $ mjolnik_gold_in_field_done = True
        "You notice that Mjolnik has a pile of tools leaned up against the farmhouse."
        
        "A shovel, pickaxe, axe and a billhook. You inspect the tools and Mjolnik speaks up."

        Mjolnik smile "Ah, see y'all wondering about the tools?"
        
        Mjolnik normal "Welo today I was planning on finally clearing out a small patch of land on the far side of my farm."
        
        Mjolnik smile "Y'all wanna come with?"

        Fen "Sure."

        hide mjolnik
        show bg village
        with dissolve
        "You grab a few of the tools and Mjolnik grabs the rest along with a basket of food."
        
        scene bg forest3
        with s_dissolve
        "The pair of you walk to small patch of woods at very back of Mjolnik's farm, where a large tangle of bushes awaits."
        
        "As Mjolnik begins to get ready, you notice something in the middle of the bushes."

        show bg forest3 at truecenter:
            zoom 1.5
        with dissolve
        "You stare hard into the thicket and you swear you see something square. Wondering what it could be you call out to Mjolnik."

        Fen "Hold on... I see something."

        Mjolnik "Whatcha see?"

        Fen "Lemme see... if I go under the bushes..."

        show bg forest3:
            zoom 2
        show ratio1
        with dissolve
        "Getting on all fours, you crawl under the outer bushes."
        
        "To your surprise, the thicket isn't solid all the way through, in fact it's more of a grove than a thicket."

        show bg forest3_blur
        show berry2_01 at truecenter
        show berry2_01 as berry2 at truecenter:
            xpos 1300
            ypos 500
            rotate 30
        show berry2_01 as berry3 at truecenter, flip:
            xpos 500
            ypos 475
            rotate -10
        with dissolve
        "You see two things. One is that the inside of the thicket is covered in blackberries and they are unusually large and juicy looking."
        
        hide berry2_01
        hide berry2
        hide berry3
        show treasure04 02 at truecenter:
            zoom 2
        hide ratio1
        show ratio1
        with dissolve
        "But the other thing is a small wooden chest sitting right in the middle of the thicket."

        "You grab the chest and drag it backwards."
        
        scene bg forest3
        with dissolve
        "Exiting the thicket, you place the chest in front of the surprised Mjolnik."

        show mjolnik shock at right1
        show bg forest3_blur
        with dissolve
        Mjolnik "Well I'll be darned. Who'd think there be something like that in this ol' thicket."

        show fen 2 smile at left1
        with dissolve
        Fen "Not just that, there's a lot of blackberries in there. Really big ones."

        hide fen
        hide mjolnik
        show bg forest3:
            zoom 1.5
        show ratio1
        with dissolve
        "Mjolnik harrumphs and turns to stare at the thicket."
        
        play sound "audio/Wood Break 6.ogg" volume 2.0
        "Grabbing the billhook, with a mighty swing his slices downward through the entire thicket wall and easily peels a section off to the side, exposing the hollow centre." with hpunch

        scene bg forest3_blur
        show mjolnik grin at center1
        with dissolve
        Mjolnik "Well, don't that beat all. Guess I got myself a blackberry patch."
        
        Mjolnik smile "I reckon I'll leave this alone then. No sense wasting those berries."
        
        Mjolnik normal "Now what's this chest all about?"

        hide mjolnik
        show bg:
            zoom 1.5
        show treasure04 02 at truecenter:
            zoom 2
        with dissolve
        "The two of you inspect the chest."
        
        "It's very well built, with thick wooden sides bound in iron."
        
        "A lock keeps the contents securely sealed. Of course, the key is nowhere to be found."

        scene bg forest3_blur
        show fen 2 stern at left1
        with dissolve        
        Fen "Great, it's locked."

        show mjolnik normal at right1
        with dissolve
        Mjolnik "Not for long..."

        hide fen
        hide mjolnik
        show bg:
            zoom 1.5
        show treasure04 02 at truecenter:
            zoom 2
        with dissolve
        "Grabbing the pickaxe, Mjolnik sizes up the chest and carefully swings the pickaxe."
        
        #Sound here maybe
        play sound "audio/Metal hard 2.ogg" volume 2.0
        "One direct hit and a shower of sparks later, the lock is loose." with vpunch
        
        scene bg forest3_blur
        show mjolnik grin at center1
        with dissolve        
        "Mjolnik grins at you."

        Mjolnik "That's that. Open it up [name] and let's see what's inside."
        
        Mjolnik normal "Hopefully it ain't empty, otherwise I just destroyed a perfectly good lock for nothing."

        stop music fadeout 1.0
        hide mjolnik
        show bg:
            zoom 1.5
        show treasure04 02 at truecenter:
            zoom 2
        with dissolve

        pause

        #Open sound
        play sound "audio/cooking/ding.ogg" volume 2.0
        show treasure04 04 at truecenter:
            zoom 2
        show ray at truecenter
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
        
        play music "audio/Of-Trees-and-Poets.ogg" volume 1.0 fadein 3.0
        "You open the box and the pair of you gasp in shock."
        
        "The chest is full of coins. Hundreds of them."
        
        "You turn to each other and grin widely."
        
        scene bg mjolnik_home
        with s_dissolve
        "Closing the lid, you grab the tool and Mjolnik grabs the chest and you hurry back to his farmhouse."

        "Once inside you dump the coins on the table and start counting."
        
        "There's thousands worth of coins there. A huge sum."

        show bg mjolnik_home_blur
        show mjolnik shock at right1
        with dissolve
        Mjolnik "Well... damn. Just damn."
        
        Mjolnik "What y'all reckon we do with it [name]?"

        show fen 2 sweat at left1
        with dissolve
        Fen "I mean it's yours. It was on your property."

        show mjolnik stern2 with q_dissolve
        "Mjolnik shakes his head."

        Mjolnik smile "Y'all the one who found it."
        
        Mjolnik grin "So I say we split it. Half half. That's as fair as fair can be."

        menu:
            "For real!? Awesome!":
                show fen 2 normal at shock
                Fen "For real!? Awesome!"

                Fen 2 smile "To think that a chest like this had been lost here, likely for quite some time. Good thing we discovered it."

                Mjolnik smile "Aye, what a lucky day, eh?"

                $ gold_in_field = 2000
                
                scene bg mjolnik_home
                with dissolve
                "you split the coins into two piles."

            "We can take those!?":

                $ gold_in_field = 1000

                show fen 2 shock at shock
                Fen "We can take those!?"

                Fen "No... I mean... that's too much."
                
                Fen 2 stern "You would have found the chest if I hadn't visited today."
                
                Fen 2 sweat "It's all yours, but if you really wanna insist... you keep three quarters."

                $ bondexp10 += 5
                call bondexpup10 from _call_bondexpup10_3
                scene bg mjolnik_home
                with dissolve
                "Mjolnik reluctantly agrees and you split the coins into two piles."
        
        "Mjolnik asks if he can keep the chest and you agree, not wanting to have to lug it back to town."
        
        "You stuff your rucksack full. It's heavy and you're not sure if you want to carry it all the way back to town."

        show mjolnik normal at center1
        show bg mjolnik_home_blur
        with dissolve
        Mjolnik "Well... y'all could leave it here and I can ask Terrance to tote it back to town for ya."
        
        Mjolnik smile "Won't bug him any. Just give him a few coins for his trouble."

        "Thinking it over, you agree that's a good idea and you count out some coins and ask Mjolnik to give that to Terrance as a payment."

        $ fen_coins += gold_in_field
        play sound "audio/payment.ogg" volume 3.0
        "{color=#16f58d}{i}You receive [gold_in_field] coins.{/i}{/color}"

        scene bg mjolnik_home
        with dissolve        
        "The pair of you are too excited to even eat anything aside from leftovers."
        
        "You spend the rest of the night talking about what you're going to do with your money."
        
        "Mjolnik plans to buy a bunch of farming tools and new equipment and stock for his farm."

        "When he asks you what you plan on spending your money on, you honestly don't know."
        
        "You know you'll think of something."

        stop music fadeout 3.0
        "After a few hours, the pair of you turn in for the night."

        scene bg black
        with s_dissolve
        play sound "audio/Transition1.ogg" volume 1.0
        "You sleep soundly and have dreams of wealth and opulence."

        pause

        scene bg mjolnik_home
        with s_dissolve
        play sound "audio/birds.ogg" volume 3.0
        play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0        
        "Upon awakening, you hear Mjolnik is already up making some breakfast and you join him."

        scene bg village
        with dissolve        
        "Once done, you bid the bull farwell and begin your trip back."

        $ mjolnik_gold_in_field_done = True

        scene bg fenroom
        with s_dissolve
        
        "You return just in time to begin your workday."

        jump day_activity

label bathhouse_common:
    $ fen_coins -= 5
    play sound "audio/payment.ogg" volume 3.0

    "Marcus hands you a basket with a towel."

    Marcus "There's a rack for the baskets. Be sure to rinse off before entering the pool."

    Fen "Yes, of course."

    #show Fen naked
    hide marcus
    show bg bathhousehall
    with dissolve
    stop music fadeout 3.0
    "You strip and place your clothing into the basket and head into the bath."

    play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
    scene bg bathhouse1
    with s_dissolve

    play sound "audio/bathtubsit.ogg" volume 1.0
    "You rinse off and take a dip in the soothing waters."

    show fen naked relax at top:
        zoom 1.5
    show bg bathhouse1_blur at truecenter:
        zoom 1.5
    with dissolve
    "The heat melts away the tension in your body and you feel relaxed."

    #Add random encounters here!!!
    #'common', 'common', 'odachi',
    $ commonpool_event = renpy.random.choice(['common', 'odachi','niall','khaleb'])

    if commonpool_event == 'common':
        label bathhouse_common_common:
            "Various adventurers chatter among themselves, but you fail to hear anything interesting as you soak."

            "After a while your skin starts to prune. It's time to go."

            "Feeling refreshed, you leave feeling refreshed and avoid dirtying yourself the rest of the day."

            hide fen
            show bg bathhouse1
            with s_dissolve

            jump bathhouse_common_end
    
    if commonpool_event == 'odachi':
        if odachi_bond_ui == False:
            jump bathhouse_common_common

        else:
            pass

        if odachi_bathhouse_first == False:

            $ odachi_bathhouse_first = True

            hide fen
            show bg bathhouse1 at truecenter:
                zoom 1.5
            with dissolve
            "Lounging back, arms spread across the tiled edge, you take note of the other bathers all the way on the opposite side of the pool from you."

            "They were about a half-dozen random citizens of Felda, chatting amongst themselves and playing."

            Fen "Must've picked a good day to come out for a soak, I guess."

            "Even though the wide-open space was echoing every word and splash that they made, it still didn't stop you from enjoying your time."

            show bg bathhouse1_blur
            with s_dissolve
            "The soothing effect of the hot water on your aching nerves and muscles was quickly pulling you into a blissfully relaxed state."

            show bg black
            with s_dissolve
            "Your eyes flutter shut, and with mind emptied of almost all thoughts, you begin to nod off into a tranquil daze."

            "That is at least, until your ears perk up at the sound of something new and strange fastly approaching."

            show bg bathhouse1 at truecenter:
                zoom 1.5
            with dissolve
            "You open your eyes and look down at the water before you to see that a roiling stream of bubbles is surging up to the surface."

            "And whatever it is that's making them is making its way towards you at an alarming rate!"

            stop music fadeout 3.0
            "You're about to act on instinct; scream like a little girl and leap out of the water, until-"

            #Odachi jumps up onto the screen with a splashing sound

            play sound "audio/big splash.ogg" volume 1.0
            show bg bathhouse1_blur
            with dissolve
            show odachi naked smile3 at center1
            with easeinbottom
            Odachi naked smile3 "Ahh~!"

            "The familiar blue otter rises up from the pool, hoisting both arm high in a long, gratifying stretch."

            play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
            Odachi naked smile "New record! Nice."

            Fen "O-Odachi!?"

            Odachi naked smile "Ah, [name]. I thought seeing fur colour, it was you. How you doing today?"

            Fen "Uh, well, uh..."

            show bg bathhouse1_blur at center:
                zoom 2
            show odachi:
                zoom 1.5
            show ratio1
            with dissolve
            "As he keeps that pose, your eyes naturally wander down the tensed, sculpted curves of his body and spot the semi-erect cock raised just above the water."

            show bg bathhouse1_blur at truecenter:
                zoom 1.5
            show odachi:
                zoom 1
            hide ratio1
            with dissolve
            Fen blush "F-Fine. I'm doing fine. Just wanted to step out for some rest."

            Fen "Today's my day off, so..."

            Odachi naked smile3 "Really? You not working today? That's great! It means that two of us can talk for long time as friends, without interruption."

            show bg bathhouse1_blur at center:
                zoom 2
                ypos 1500
            show odachi naked smile at top:
                zoom 1.5
            with dissolve
            "He walks over towards you and lowers himself back down to sit against the edge with you, mimicking your relaxed posture."

            "It seems like he's trying to play it casual with you."

            Odachi naked smile2 "This place is very nice, yes? Just like hot spring we have back home."

            Fen blush "Uh...Y-Yeah, definitely."

            "You try your best to look away when answering him, afraid that he might catch you ogling if you don't."

            Fen "So...What exactly were you doing just now below the water?"

            Odachi naked smile "Oh. I just was practising my holding breath."
            
            Odachi "Was able to do it for nine whole minutes today. Longest since I left home country."

            Fen "Oh, wow. Is that something you like to do for sport there?"

            Odachi naked smile3 "Sport? No, not if not also racing. I do it for fun."

            Odachi naked smile "I trying to have fun while in Felda like ways its native people do."
            
            Odachi "I was ask around for places to have clean fun and was told about here."

            Odachi naked smile3 "I am very glad to see you here also. New places always much better with friends."

            "It sounds like Odachi would really appreciate some good company whenever he's here."

            jump odachi_bathmenu_01
        
        else:
            hide fen
            show bg bathhouse1
            with dissolve
            "You spot Odachi practising his swimming and breath control."

            play music "audio/Winter Sakura.ogg" volume 1.0 fadein 3.0
            show bg bathhouse1_blur at center:
                zoom 2
                ypos 1500
            show odachi naked smile at top:
                zoom 1.5
            with dissolve
            "You head right on over to say hi and get settled in by the poolside with him."

            jump odachi_bathmenu_01
        
        label odachi_bathmenu_01:
            "Maybe you can think of some ways to keep him entertained today?"

            menu:
                "So you really like this bathhouse, huh?":
                    jump about_odachi_bathhouse
                "Isn't it impressive how hygienic this place is?":
                    jump about_odachi_hygiene
                "Hot springs? You mean the natural ones?":
                    jump about_odachi_onsen
                "You're still wearing that headband...":
                    jump about_odachi_headband
        
        label about_odachi_bathhouse:

            Odachi naked smile "Oh, yes! I have only be coming here...maybe one or two week now, but already, I very much in love with owner and all people here."

            Odachi naked normal "Marcus, I think his name. He notice I come from people with probably water affinity, and he wanted give me three free days of bathing my first times."

            Odachi naked smile3 "Free! Only needed to come at time when he also takes bath, and I could invite clients from tail service to join, too."

            Odachi "Sounds much like a most generous man and great business owner, no?"

            Fen "That...actually sounds like a pretty fishy deal to you."

            if bond03 <= 1:
                Fen "{i}And what's this tail service he's talking about?{/i}"
                
            else:
                pass

            Fen sweat "Uh-huh. And did he say that these clients of yours could also get in free?"

            Odachi naked normal "No. They had to pay."

            Odachi "Marcus said he could not give for free entrance to people without water affinity. That it was policy, and would be too crazy if it could go to just anyone."

            Fen sweat "Oh...So, only you got in for free and also brought him more business, huh?"

            Odachi naked smile "No. I also paid."

            Fen "Hm? But you said-"

            Odachi naked normal "I could not say yes to Marcus offer for free entrance knowing how much care he puts into good business and the way of the policy."

            Odachi "It would not be honourable for me."

            "Damn. Did Odachi's code of honour really make him need to be {b}this{/b} humble and considerate?"

            "He couldn't even accept a free bath day if the owner offered him one? It's kinda hard to imagine..."

            jump bathhouse_odachi_end

        label about_odachi_hygiene:

            Odachi naked smile3 "Haha! Yes, truly is."

            Odachi naked smile "Small artefacts underneath pool, makes sure water never stays dirty for long. And lots of fresh towels every day."
            
            Odachi naked smile3 "Plus olive oil soap—my favourite!"

            Fen "What would you say the most important place on the body to keep clean is?"

            Odachi naked normal "Hmm..."

            Odachi naked smile3 "Butt! Must always have looking fresh after each use, for next time."

            "You almost can't believe how unabashedly he just said that..."

            Odachi naked smile "What about you?"

            Fen "Me? Oh, I think it's important to make sure you always wash behind the ears."

            Odachi naked normal "Ears?"

            Fen "Yep. Under, inside, and behind. Lots of people tend to forget it, so it helps you feel exceptional if you're someone who actually remembers."

            if fen_remembers_father == False:
                Fen "That's actually a funny little life lesson I learned growing up from...from..."

                scene bg white
                with dissolve
                scene bg bathhouse1_blur at center:
                    zoom 2
                    ypos 1500
                show odachi naked normal at top:
                    zoom 1.5
                with dissolve
                #Screen briefly flashes or blurs to show that Fen is struggling to remember

                "All of a sudden, you realise that you're not quite sure what you were about to say."

                "Why did you even offer that information in the first place?"

                Fen "Uh...from somebody who's pretty silly, I'm sure."
            
            else:
                Fen "That's actually a funny little life lesson I learned growing up from my father."

            Odachi naked smile "Ha! I would bet."

            Odachi naked normal "'Always wash behind the ears...'"
            
            Odachi naked smile3 "...Sure, I guess. But only if don't mind always being wet behind them, too! Ha-hah!"

            jump bathhouse_odachi_end

        label about_odachi_onsen:

            Odachi naked smile "{b}Onsen!{/b} They traditional way of taking bath in my home country."

            Odachi naked smile2 "Many towns built around one hot spring when someone finds it. This because entire community comes to use it."

            Odachi "Much of culture is made this way, with people coming together and feel better around each other."

            Odachi naked smile "Even gods were given jobs for bath time and {b}onsen{/b}, because it was to be gift from the mother earth, and to protect against accidents and disease."

            Fen grin "Oh, wow...Man, why does this place sound more and more like a dream everytime I hear about it?"

            Odachi naked smile3 "Ha! It not always so perfect as I make sound. I just very good, uh...storyteller, like people often say me."

            Odachi naked normal "One time, when I was pup in {b}onsen{/b}, this very mean imp-thing in bath next to me stole an orange I was eating right out my hands."

            Odachi naked stresse "And then, he went and peed all over my clothes I had left outside!"

            Fen "Wait. There was a monster {b}inside{/b} the bath with you?"

            Odachi naked normal "Oh, yes. {b}Onsen{/b} most are open air; open for all nature to join."

            Odachi naked smile2 "There were imps taking baths with whole of their families next to us. Huge crickets making fall leaves from bushes on the rocks above."

            Odachi naked smile "And trained yellow goblins. Could even use lightning affinity when wanted to. They trained to serve us fruit to eat on wooden bowls, pushed in the water."

            Odachi naked smile3 "Very, very cute. I always want one of my own. Hehe."

            Fen "Oh. Well, I guess as long as you guys found a way to keep it safe and hygienic, I still think that sounds pretty great."

            jump bathhouse_odachi_end
            
        label about_odachi_headband:

            Odachi naked stresse "Uh...yes. Yes, I know."

            Odachi "It is just something hard to take off..."

            Fen stern "Hard? I mean, it doesn't look like it's stuck to you."

            Odachi "No, no. Not hard, like, I cannot. Hard, like, uh..."

            Odachi naked sweat "I sorry. I do not know what to say."

            Fen "Well, I just would think you wouldn't want it getting drenched in the water, is all."

            Odachi naked stresse "Yes. I know, [name]. I am sorry."
            
            Odachi "I know you are good male for think of me, but...Is not something I can just do with people here."

            "You notice that the subject must've made him pretty uncomfortable."

            "He's blushing and there's more sweat running down his face now than a second ago from just the steam."

            "You realise that it's probably best if you just apologise for the question now and just drop it."

            Fen "It's okay, I understand. I'm sorry if me asking made you feel embarrassed about it."

            Odachi naked smile "Thank you. Perhaps, one day, I will be happy with show you, if we are close enough."

            Fen "Oh, that's alright. I don't care if I-"

            Odachi naked blush "But I hope you do. You seem like male who deserve to see every part of me."

            Fen blush "O-Oh...!"

            jump bathhouse_odachi_end

        label bathhouse_odachi_end:

            hide odachi
            show bg bathhouse1 at truecenter:
                zoom 1
            with dissolve
            "You chatted in the pool for a while, enjoying the nice soak."

            $ bondexp03 += 3
            call bondexpup03 from _call_bondexpup03_6

            show odachi naked smile at center1
            show bg bathhouse1_blur
            with dissolve
            Odachi "Thank you, [name]. I had very nice day here today because of you."

            Odachi "Until next time."

            stop music fadeout 3.0
            hide odachi
            show bg bathhouse1
            with dissolve
            "With that, Odachi lifts himself out of the bath and makes for the common room to collect his clothing."

            "Since you know that overheating isn't as much a risk for you as it would be for others, you stay inside for a while longer before heading out yourself."

            "You feel all fresh and rejuvenated for whatever may come your way tomorrow!"

            $ bathhouse_odachi_done = True

            jump bathhouse_common_end
    
    if commonpool_event == 'niall':

        if niall_bond_ui == False:
            jump bathhouse_common_common

        else:
            pass

        if niall_bathhouse_first == False:

            $ niall_bathhouse_first = True

            hide fen
            show bg bathhouse1 at truecenter:
                zoom 1.5
            with dissolve
            "Lounging back, arms spread across the tiled edge, you take note of the vast emptiness of the room and realise that you've got it all to yourself."

            "Considering how much traffic this place often sees on the daily as one of Felda's biggest attractions, this solitude is quite the treat!"

            Fen "Must've picked a good day to come out for a soak, I guess."

            "Because of the wide-open, liminal space that echoes every musical hum and splash you make, it feels really easy for you to just enjoy your time."

            show bg bathhouse1_blur
            with s_dissolve
            "The soothing effect of the hot water on your aching nerves and muscles was quickly pulling you into a blissfully relaxed state."

            stop music fadeout 3.0
            show bg black
            with s_dissolve
            "Your eyes flutter shut, and with mind emptied of almost all thoughts, you begin to nod off into a tranquil daze."

            "That is at least, until your ears perk up at the sound of paws clacking on the tiled floor behind you, getting louder fast."

            Niall grin "{size=80}Cannonball!{/size}"
            #Niall runs across the screen before making a heavy splashing sound.


            show bg bathhouse1
            with dissolve
            show bg black
            with dissolve
            show bg bathhouse1
            with dissolve
            show niall naked normal at center1:
                xpos -600
            with easeinright
            "You blink open your eyes just in time to see the young, blue jackal dive into the water in front of you with his knees tucked in..."
            
            play sound "audio/big splash.ogg" volume 2.0
            "...making a big splash." with hpunch
    
            "After a moment, Niall's head pops back up above the surface, and he turns to you with a big playful smile showing all across his face."

            play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
            show niall naked smile at center1
            show bg bathhouse1_blur
            with dissolve
            Niall naked smile "Woo! That worked out great."

            Niall "I was worried the pool was gonna be too shallow for a second."

            Fen naked normal "Oh, Niall. Fancy running into you here."

            Niall naked normal "Hey, [name]. What's up? I thought it was you I saw taking a dip when I walked in."

            Niall naked smile "So, since it looked like there was nobody else here, I figured I'd make myself known in the best way possible."

            Fen sweat "By...By shouting real loud and making ripples in the bath?"

            show niall at shock
            Niall "Heck yeah! Impressions don't mean anything unless you're always making big waves, so I might as well always be trying, right?"

            Niall naked stern "Or, uh...that's how I gotta act at the guild if I don't want to be passed up on all the good quests, at least."

            Fen stern "Life at the guild is that competitive, huh?"

            show niall naked sweat at shock
            Niall "Oh, and how! I've barely even got the time to kick back and relax at all these days."

            Niall naked smile "Hey, speaking of which, mind if I keep you company for your soak today?"

            Fen "Oh, sure. Be my guest."

            show bg bathhouse1_blur at center:
                zoom 2
                ypos 1500
            show niall naked normal at top:
                zoom 1.5
            with dissolve
            "Staying low under the surface, he paddles over to where you are at the shallow end of the pool and reclines next to you."

            "You fully expect him to start gabbing about whatever must be burning at the front of his mind for him to want to be in your company this much right now."

            "But after a long minute of nothing but silence, you realise that he genuinely just wants to enjoy the bath peacefully with you."

            "Though an unexpected thing to see from someone like him, it's not an unwelcome change."

            jump niall_bathmenu_01

        else:
            stop music fadeout 3.0
            hide fen
            show bg bathhouse1
            with dissolve
            "you spot Niall shadowboxing some of the mist alone by the poolside."

            play music "audio/Excalibur.ogg" volume 1.0 fadein 3.0
            show bg bathhouse1_blur at center:
                zoom 2
                ypos 1500
            show niall naked normal at top:
                zoom 1.5
            with dissolve
            "You head right on over to say hi and get settled into the water with him."

            jump niall_bathmenu_01

        label niall_bathmenu_01:
            "Maybe you can think of some ways to keep him entertained today?"

            menu:
                "So what do you think about this bathhouse?":
                    jump about_niall_bathhouse
                "How do you usually like to keep clean?":
                    jump about_niall_hygiene
                "Do you often come here alone?":
                    jump about_niall_bath_company
        
        label about_niall_bathhouse:
            show niall naked smile
            Niall "It's great! I don't think I've been to a place that's felt this classy in years. And Marcus, the owner here is just so nice."

            Niall naked normal "While he was in the middle of giving me the tour, I asked him what the best way for someone to relax here after a long day of being on your feet."

            Niall naked smile "Turns out, Marcus offers deep tissue foot massages to customers in the know. And then, he gave me a free voucher for my first session!"

            Fen "Wow, that does sound pretty sweet. And he gives you the massage himself?"

            Niall naked stern "Mm-Hm. And that's so unlike most managers I've ever known who run a place this big."

            Niall naked smile "It takes a special kind of love and passion for what you do to say you want to put yourself in the place of the average worker, you know?"

            Fen "Well, yeah. That's definitely true."

            Fen sweat "{i}But still, I can't help but wonder if these secret services are only meant for customers he thinks would need his 'physical' therapy... {/i}"

            Niall naked stern "You doing okay there, [name]? You look a little lost in thought all of a sudden."

            Fen "Huh? O-Oh, yeah. I'm fine. Just wondering about what else Marcus does, is all."

            Niall "Come to think of it, your feet must be killing you, having to be on them all day working in a tavern from dawn till dusk, huh?"

            Niall naked smile "Would you like to have my free voucher for Marcus's foot massage. I'm totally alright with you going instead of me."

            Fen "R-Really? Oh, I dunno. Not sure I really need something like that, and even so, I'm not sure what it's gonna do for me."

            Niall naked normal "True, but you can't know for sure unless you give it a try, right?"

            Fen "Uh...You know, I'll think about it. And if I feel really interested in the near future, I'll let you know."

            Fen "But don't feel like you have to keep it for me until then or anything, yeah?"

            Niall naked smile "Okay!"

            jump bathhouse_niall_end

        label about_niall_hygiene:
            Niall "Me? Well, I know I give special attention to my spikes when I wash."

            Fen "Oh, really?"

            Niall "Yeah. You wouldn't believe how much gunk can build up around the ones on my paws after a long day of punching monsters."

            Niall"And even when they're pretty clean, I usually still like to give them a good buffing to make sure they keep that lustrous shine."

            Niall naked smile "I gotta treat them like the fine weapons they are, even if they do come out of my body."

            "As if to demonstrate, he holds up one of his paws and turns it over in the light pouring in from above."

            "You're a little impressed by the shine he's able to make on it, not unlike the radiance of a pearl."

            Fen grin "That's so cool! I wish there was a part of my body that I could make glisten like that."

            Niall "Hehe. Well, don't go selling yourself short now."

            #He says the next line in a whisper, probably with smaller text than usual

            Niall naked blush "{size=18}I'm sure you've got something down there that glistens beautifully in the right light...{/size}"

            Fen "What was that?"

            Niall naked wink "Nothing!"

            jump bathhouse_niall_end

        label about_niall_bath_company:
            Niall naked stern "Uh...yeah, more or less."

            Niall "I mean, I invited some of the other guys from the guild to come join once or twice, but..."

            Fen stern "But?"

            Niall naked blush2 "They, uh...They said they'd only come if we could do naughty stuff together here."

            Fen stern "And you weren't okay with that?"

            Niall "No, of course not."

            Niall "Well, I mean, not with them anyway. I'm sure they're all okay guys, but I feel like I just don't know them that well."

            Niall naked stern "There's no telling what exactly they wanted to do with me, or how our relationship would be when it's over."

            Niall "Like, I know that a lot of people are pretty casual about the way they give up their bodies, but...I just don't think that's me, [name]."

            Fen "Well, you could always try and ask some other people who've been with them like that how they are."

            Fen "That way, you could at least learn some good ways to get closer first."

            Niall "I dunno."

            Niall naked blush2 "I'd still want someone I know I can {b}really{/b} trust to take that step with me."

            Niall naked stern "Otherwise, I'd just end up feeling so...powerless, I guess."

            Niall "...Does that make me weird?"

            "You don't think you've ever seen him look at you with eyes this serious."

            Fen sad "Oh, Niall..."

            Fen "Of course, not. No one's ever weird for just avoiding what might make them uncomfortable."

            Fen "And I think you're really strong for knowing your own limits like that. Not many people can say they truly do."

            Niall naked blush "R-Really?"

            Niall "Well, uh...thanks, [name]."

            jump bathhouse_niall_end

        label bathhouse_niall_end:

            hide niall
            show bg bathhouse1 at truecenter:
                zoom 1
            with dissolve
            "You chatted in the pool for a while, enjoying the nice soak."

            $ bondexp04 += 3
            call bondexpup04 from _call_bondexpup04_6

            show niall naked normal at center1
            show bg bathhouse1_blur
            with dissolve
            Niall "Glad I got to spend the day with you like this, but I gotta go now."

            Niall naked smile "Hope to catch you next time!"

            stop music fadeout 3.0
            hide niall
            show bg bathhouse1
            with dissolve
            "With that, Niall lifts himself out of the bath and makes for the common room to collect his clothing."

            "Since you know that overheating isn't as much a risk for you as it would be for others, you stay inside for a while longer before heading out yourself."

            "You feel all fresh and rejuvenated for whatever may come your way tomorrow!"

            $ bathhouse_niall_done = True

            jump bathhouse_common_end

    if commonpool_event == 'khaleb':

        if khaleb_bond_ui == False:
            jump bathhouse_common_common

        else:
            pass

        if khaleb_bathhouse_first == False:

            "After dozing off for a while, you snap back alert to the sound of some kind of commotion."
            
            stop music fadeout 3.0
            hide fen
            show bg bathhouse1 at center:
                zoom 1
            with dissolve
            "You see a couple of the other patrons moving past to get out of the water and leave in a hurry."
            
            "It leaves you wondering for just a second before you see the reason why splashing about in the water across from you."
            
            "That group of thugs from the tavern is here..."
            
            show arek naked sweat at left1, flip
            show trei naked sweat at right1
            show bg bathhouse1_blur
            with dissolve
            "Those two black furred dogs are being rowdy, wrestling each other in the pool and causing big splashes whenever one of them falls down in the water."
            
            hide arek
            hide trei
            show khaleb naked normal at center1
            with dissolve
            "Meanwhile, that badger is watching them go at it from on top of the marble steps to the side."
            
            hide khaleb
            show bg bathhouse1
            with dissolve
            "He's lounging fully naked on a towel with a hand against his chin, like some emperor spectating a savage game in his honour."
            
            "You stand there dumbfounded for a minute, unsure of what to do."
            
            show bg bathhouse1_blur at truecenter:
                zoom 1.5
            show arek naked sweat at left1, flip:
                zoom 1.5
            show trei naked sweat at right1:
                zoom 1.5
            show ratio1
            with dissolve
            "The hound uses his superior height to try and force the hyena-wolf down to his knees from behind."
            
            "But then, Arek sucks in a bit of water through his mouth and turns up to spray it right into the hound's eyes, making him jump back, blinded." with vpunch
            
            "As Trei rubs his eyes to get the mixture of scented bath oil and spit out, he blinks a couple of times before realising he's looking right over at you."
            
            "He can see the full hard-on you're sporting right now..."
            
            hide arek
            hide ratio1
            show bg bathhouse1_blur at top
            show trei naked angry at top
            with dissolve
            Trei naked angry "Yo! You buy tickets to see the show, or what!?" with vpunch
            
            hide ratio1
            show bg bathhouse1_blur at center:
                zoom 1
            show fen naked shock at left3
            show trei naked angry at right2:
                zoom 1
            with dissolve
            Fen "Huh?"

            show arek naked smile2 at left2
            with dissolve
            Arek "Oh, hellooo abs~! ❤"

            Fen naked blush "Uh, I...I-I'm sorry. I just, uh..."

            "You're about to back out of the room and leave, but then Khaleb gets up from his spot and swaggers on over to you."

            show khaleb naked smile at right3
            with dissolve 
            Khaleb "Ey! Wait, wait, wait on a sec. What's the hurry there, Fluff Butt?"

            Khaleb naked normal "We ain't strangers or nothin' to ya, right?"

            Fen "N-No. It's...It's that I saw some other people leave just now, so I figured that might mean you guys want to be left alone."

            show trei naked stern at shock
            Trei naked stern "How'dja figure that, huh? This bath's public, ya dumb matchstick." 

            Trei "What right do you think we got to tell people the water ain't fine?"

            Fen "But there were people leaving when I came in. They looked scared about something."

            Arek naked normal "Pft. Ain't that just the rub. They were squares; none of the moxie it takes to be around us."

            Khaleb "Yeah, that wasn't nothing. Only my bros livening up the joint with a bit a' good ol' fashion wet brawling."

            show arek naked smile2 at shock
            Arek "And winner gets a special 'surprise treat' from big bro!"

            Khaleb "Sounds interesting don't it?"

            Khaleb naked smile "You're more than welcome, if you want in. Trei's looking like he needs someone more close to his skill level, anyway."

            show trei naked stern at flip, shock
            Trei "Heyyyy!"

            jump khaleb_bathmenu_01

        else:
            jump bathhouse_khaleb_2nd

        label khaleb_bathmenu_01:
            menu:
                Fen "Well, I dunno. Uh, I mean..."
            
                "Say you'll agree to wrestle Trei":
                    jump about_trei_wrestle

                "Say you want to wrestle Arek instead":
                    jump about_arek_wrestle

                #"Ask if you can wrestle Khaleb":
                    #jump about_khaleb_wrestle

                "Refuse and walk out":
                    jump about_no_one_wrestle

        label about_trei_wrestle:
            show fen naked grin at shock
            Fen "Alright then, you're on!"

            Fen "Just let me know what the rules are, and I'm set."

            Khaleb naked smile "Rules? You think we thought up rules for this shit?"

            Khaleb naked normal "Yeah, uh...Just make sure nobody dies. Or breaks something that's gonna cost me more than, like, five gold to fix. There's your rules for ya."

            Khaleb "Now Trei, looks like we got you a redemption match set up."

            Khaleb "So you climb on back inta that drink and make yourself look extra frisky for me, ya hear? One of your big bros 'grand prizes' is on the line."

            show trei naked angry at flipback, shock
            Trei "Grrr! I'm gonna get it for sure this time!"

            Fen naked normal "So, what do I get exactly, if I win?"

            Khaleb "'{i}When{/i} I win', kid. That's the kinda mentality you gotta have."

            Khaleb "And to help paint a picture for ya, the reward's different every time, but it's something that comes right from me, so you know it's gonna be good, yeah?"

            Khaleb "Could be a free dinner this time, could be a swanky new accessory that'll bring out the shine in your eyes..."

            show khaleb hard grin
            with dissolve
            Khaleb hard grin "Could even be a little favour I owe you down the road. Anything you want."

            Fen naked blush "A-Anything...?"

            hide fen
            hide arek
            hide trei
            show khaleb hard normal at center1:
                zoom 1.5
            show bg bathhouse1_blur at center:
                zoom 1.5
            show ratio1
            with dissolve
            "Just then, you notice his dick get fully erect while looking down at yours. He twitches it for you while nodding along to your question."

            hide ratio1
            hide khaleb
            show bg bathhouse1 at truecenter:
                zoom 1
            with dissolve
            "While you're distracted, Khaleb snaps his fingers, and in no time, he and Arek are grabbing you by the arms and legs."

            show bg bathhouse1 at truecenter:
                zoom 1.5
                rotate -11.8
            with vpunch
            "They're lifting you over towards the pool!" 

            Khaleb "Yup! Now get in there and break a leg, scamp. Not literally, of course."

            Khaleb "Heave-fuckin'-ho!"

            play sound "audio/big splash.ogg" volume 2.0
            show bg bathhouse1 at truecenter:
                zoom 3
                rotate -300
            with vpunch
            "Like a stone, they toss you into the center of the pool where Trei was waiting expectantly for just this moment."

            label about_trei_wrestle_2:

                show bg bathhouse1_blur at truecenter:
                    zoom 3
                    rotate 0
                show trei naked angry at center1:
                    zoom 1.5
                show ratio1
                with dissolve
                "No sooner than you come up gasping for air is he already on top of you, trying to push you back down again."

                show trei naked sweat at right1:
                    zoom 1.5
                show fen naked normal at left1 behind ratio1:
                    zoom 1.5
                with dissolve
                "The two of you lock arms in a desperate struggle. Seeing your resistance only seems to make him even more riled up."

                show fen at left2
                show trei at right2
                with dissolve
                "You can tell he's trying to use his height to his advantage like before to overwhelm you." with hpunch

                "And now, he's started barking frantically in your face, trying to make you flinch and throw you off." with hpunch

                hide fen
                hide trei
                show bg bathhouse1
                with dissolve
                "But that might be just the kind of slip up you need."

            if FenSTR <= 6:

                "{color=#16f58d}{i}Strength Check 6 - Failure{/i}{/color}"

                show bg bathhouse1_blur
                show trei naked angry at top:
                    zoom 1.5
                hide ratio1
                with dissolve
                "You try to use his lack of focus on his own form to topple him, but sadly, you're not strong enough to shift the weight where you need it."
                
                show trei naked sweat:
                    zoom 2
                with vq_dissolve
                "Trei seizes the moment you messed up and uses it to knock your arms away."
                
                play sound "audio/big splash.ogg" volume 1.0
                hide trei
                show bg bathhouse1 at truecenter:
                    zoom 3
                    rotate -300
                with vpunch
                "He then knees you so hard in the sternum that you go flying back and crash down into the water limply with an enormous splash."
                
                #(+1 bond point with Khaleb)

                #Sound of some claps from Khaleb and Arek

                play sound "audio/clapping.ogg" volume 1.0
                $ bondexp07 += 3
                call bondexpup07 from _call_bondexpup07_2
                show bg bathhouse1_blur at truecenter:
                    rotate 0
                    zoom 1
                show arek naked smile2 at left3, flip
                show khaleb naked smile at right3
                with dissolve
                Khaleb "That's it folks! We have a winner!!!"
                
                Khaleb naked normal "Nice job, Trei. Come on over here and get what's yours."
                
                show trei naked normal at center1, flip
                with dissolve
                Trei "Oh, boy! What'd I win, what'd I win?"
                
                stop music fadeout 1.0
                play sound "audio/Schlop.ogg" volume 2.0 fadein 1.0 loop
                show khaleb at right2
                with dissolve
                Khaleb "Open wide..."
                
                hide arek
                show trei naked normal at left2:
                    zoom 1.5
                show khaleb naked normal at right2:
                    zoom 1.5
                show ratio1
                with dissolve
                Trei "N-Nngghh!!"

                if khaleb_bathhouse_first == False:

                    $ khaleb_bathhouse_first = True

                    "You resurface only to immediately blush at the sight of Khaleb's long, snake-like tongue disappearing into Trei's open, waiting mouth."
                    
                    "The two of them then interlock muzzles in a big, sloppy kiss that feels like it lasts forever."
                    
                    show trei hard normal
                    with dissolve
                    "The mystery of just what that tongue is doing in his throat leaves you transfixed, as you watch the pup absolutely melt in his friend's attentive arms."

                    jump bathhouse_khaleb_end

                else:

                    "You blush even harder than you already are at the sight of Khaleb's long, snake-like tongue disappearing into Trei's open, waiting mouth."
                    
                    "The two of them then interlock muzzles in a big, sloppy kiss that feels like it lasts forever."
                    
                    "Imagining everything that tongue could be doing in his throat leaves you transfixed, as you watch the pup absolutely melt in his friend's attentive arms."
                    
                    Fen hot "Oh, woah...!"

                    stop sound fadeout 1.0
                    "Eventually, the kiss ends once you see Trei turn blue in the face, and he falls over coughing and gasping for air."
                    
                    "You also notice that he's just as rock hard erect as you are despite that, though."

                    jump bathhouse_khaleb_end

            else:
                #(STR check passed.)

                "{color=#16f58d}{i}Strength Check 5 - Success{/i}{/color}"

                show trei naked angry at top:
                    zoom 1.5
                hide ratio1
                with dissolve
                "You deftly use his lack of focus on his own stability against him."

                show trei naked angry at top:
                    zoom 2
                with vq_dissolve
                "The force between the two of you shifts away from his centre of balance, and you bring him toppling under his own weight." with vpunch

                play sound "audio/big splash.ogg" volume 2.0
                hide ratio1
                hide trei
                show bg bathhouse1
                with dissolve
                "The hound yelps, flailing wildly for anything he can grab, as his footing slips and he comes crashing down with a tremendous splash."

                #Sound of some claps from Khaleb and Arek
                play sound "audio/clapping.ogg" volume 1.0
                $ bondexp07 += 3
                call bondexpup07 from _call_bondexpup07_3
                show bg bathhouse1_blur at truecenter:
                    rotate 0
                    zoom 1
                show arek naked smile2 at left3, flip
                show khaleb naked smile at right3
                with dissolve
                Khaleb naked smile "That's it folks! We have a winner!!!"

                Khaleb naked normal "Not too shabby, kid. Now come on over so I can give ya something real nice."

                show fen naked smile2 at center1
                with dissolve
                Fen naked smile2 "Ahahaha! Thanks. But it was nothing, really."

                Fen naked normal "So, what did I just win?"

                label bathhouse_khaleb_kiss_you:

                    if khaleb_bathhouse_first == False:

                        $ khaleb_bathhouse_first = True

                        hide fen
                        hide arek
                        hide trei
                        show bg bathhouse1_blur at truecenter:
                            zoom 2
                        show khaleb naked normal at top:
                            zoom 2
                        with dissolve
                        Khaleb "Open wide..."

                        Fen "Huh?"                        

                        stop music fadeout 1.0
                        play sound "audio/Schlop.ogg" volume 2.0 fadein 1.0 loop
                        show khaleb naked normal at top:
                            zoom 3
                            ypos -400
                        show ratio1
                        with dissolve
                        "Before you're able to process what's going on, Khaleb's long, snake-like tongue presses itself past your lips and starts invading your mouth."

                        "You blush hard, so surprised that you try to push him away on instinct. But his big, brutish arms are wrapped around you, holding you in place tight."

                        "All you can do is let out a suppressed moan while his tongue brushes up against your soft palate before worming its way down your throat."

                        "You feel it swirling around like an auger, tickling every nerve in your epiglottis, pushing to go ever deeper."

                        "Tears well up in your eyes, and you realise you're choking. But Khaleb only watches you convulse with a hungry gleam."

                        "At first, you're doing everything you can to break free, but then an almost insane thought enters your mind as you start to go lightheaded."

                        "This doesn't feel so bad anymore...In fact, it almost feels good in a way that you can't really compare to anything else."

                        "The danger is making you achingly hard. Hard enough that you think you just might—"

                        "{color=#b641b2}???{/color}" "What's going on in there?"
                        
                        hide ratio1
                        hide khaleb
                        show bg bathhouse1
                        with dissolve
                        "Khaleb then pulls away from you abruptly, leaving you to cough up a lung."

                        jump bathhouse_khaleb_end

                    else:

                        hide fen
                        hide arek
                        hide trei
                        show bg bathhouse1_blur at truecenter:
                            zoom 2
                        show khaleb naked normal at top:
                            zoom 2
                        with dissolve                            
                        Khaleb "Open wide..."
                            
                        Fen hot "Nngffh!"

                        stop music fadeout 1.0
                        play sound "audio/Schlop.ogg" volume 2.0 fadein 1.0 loop
                        show khaleb naked normal at top:
                            zoom 3
                            ypos -400
                        show ratio1
                        with dissolve                        
                        "You're barely able to contain your anticipation, as Khaleb's long, snake-like tongue presses itself past your lips and invades your mouth."
                            
                        "You blush hard, so skittish at first that you try to push him away. But his big, brutish arms are wrapped around you, holding you in place tight."
                            
                        "All you can do is let out a suppressed moan while his tongue brushes up against your soft palate before worming its way down your throat."
                            
                        "You feel it swirling around like an auger, tickling every nerve in your epiglottis, pushing to go ever deeper."
                            
                        "Tears well up in your eyes, and you realise you're choking. But Khaleb only watches you convulse with a hungry gleam."
                                                    
                        "At first, you're doing everything you can to break free, but then an almost insane thought enters your mind as you start to go lightheaded."
                            
                        "This doesn't feel so bad anymore...In fact, it almost feels good in a way that you can't really compare to anything else."
                            
                        "The danger is making you achingly hard. Hard enough that you think you just might—"

                        stop sound fadeout 1.0
                        play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0    
                        show bg bathhouse1_blur at truecenter:
                            zoom 2
                        show khaleb naked normal at top:
                            zoom 2
                        hide ratio1
                        with dissolve
                        "But then, just as suddenly, it all stops. Khaleb pulls himself out of you, leaving you to gasp desperately for air."
                        
                        Khaleb "Phew! I'd say that's enough for now, huh?"
                            
                        Khaleb naked smile "Wouldn't want you getting to work up about it and making a mess around the place, would we?"
                            
                        Khaleb naked normal "So, what'd ya think of that, kid? Was it to your satisfaction?"

                        jump bathhouse_khaleb_end

        label about_arek_wrestle:

            Fen naked grin "How about I take on the other guy, instead?"

            show arek naked normal at shock
            Arek naked normal "Eh? You got a losing kink, or something?"

            Khaleb naked smile "Ooh! A surprise challenge from our little peeper, then, is it? That's pretty bold of ya. I like it."

            show trei naked angry at shock
            Trei "Hey! You thinking I'm some kinda joke to you? Is that it?"

            Fen naked stern "N-No, no. It's just, uh..."

            Khaleb naked normal "He's feeling like a taste of the ol' chub today. I totally get it."

            Khaleb "So, Arek, you game to go another round?"

            show arek naked smile2 at flip, shock
            Arek "Fuck yeah, bro!"

            Khaleb naked smile "Great. Then, head on back in and make sure you look extra frisky for me."

            Fen "So, what do I get exactly, if I win?"

            Khaleb naked normal "'{i}When{/i} I win', kid. That's the kinda mentality you gotta have."

            Khaleb "And to help paint a picture for ya, the reward's different every time, but it's something that comes right from me, so you know it's gonna be good, yeah?"

            Khaleb "Could be a free dinner this time, could be a swanky new accessory that'll bring out the shine in your eyes..."

            show khaleb hard grin with dissolve
            Khaleb "Could even be a little favour I owe you down the road. Anything you want."

            show khaleb hard grin
            with dissolve
            Fen naked blush "A-Anything...?"

            hide fen
            hide arek
            hide trei
            show khaleb hard normal at center1:
                zoom 1.5
            show bg bathhouse1_blur at center:
                zoom 1.5
            show ratio1
            with dissolve
            "Just then, you notice his dick get fully erect while looking down at yours. He twitches it for you while nodding along to your question."

            hide ratio1
            hide khaleb
            show bg bathhouse1 at truecenter:
                zoom 1
            with dissolve
            "While you're distracted, Khaleb snaps his fingers, and in no time, he and Trei are grabbing you by the arms and legs."

            show bg bathhouse1 at truecenter:
                zoom 1.5
                rotate -11.8
            with vpunch
            "They're lifting you over towards the pool!"

            Khaleb "Yup! Now get in there and break a leg, scamp. Not literally, of course." 

            Khaleb "Heave-fuckin'-ho!"

            play sound "audio/big splash.ogg" volume 2.0
            show bg bathhouse1 at truecenter:
                zoom 3
                rotate -300
            with vpunch
            "Like a stone, they toss you into the center of the pool where Arek was waiting expectantly for just this moment."

            label about_arek_wrestle_2:

                show bg bathhouse1_blur at truecenter:
                    zoom 3
                    rotate 0
                show arek naked normal at right1:
                    zoom 1.5
                show ratio1
                with dissolve
                "No sooner than you come up gasping for air is he already rushing at you, crouched down in the water."

                show arek naked normal at center1:
                    zoom 1.5
                show fen naked normal at left3 behind ratio1:
                    zoom 1.5
                with dissolve
                "He tackles you right in the stomach, shoving you back with enough force to almost topple you had you not grabbed onto his clumpy fur to stop it."

                "He growls, positioning his arms under your pits to then try and lift you up off the ground." with vpunch

                show fen at left2
                show arek at right2
                with vq_dissolve
                "It's obvious to you that he's trying to bring you helplessly into the air, where he can then go toss you however he likes."

                "You're only hope now is to muscle your way out of his lock. Maybe you can even turn it around on him."

            if FenSTR <=9:

                "{color=#16f58d}{i}Strength Check 10 - Failure{/i}{/color}"

                "You try to part his arms away from you by pulling at them from the sides, but sadly, you're not strong enough to do it." with hpunch

                "Arek seizes the moment you messed up and uses it to hoist you up above the water like a prize catch." with vpunch

                play sound "audio/big splash.ogg" volume 1.0
                show bg bathhouse1 at truecenter:
                    zoom 3
                    rotate -300
                hide fen
                hide arek
                hide ratio1
                with vpunch
                "He then hurls you with so much enraged strength that you go flying across the pool and crash down into the water with an enormous splash."

                #(+1 bond point with Khaleb)

                #Sound of some claps from Khaleb and Trei
                play sound "audio/clapping.ogg" volume 1.0
                $ bondexp07 += 3
                call bondexpup07 from _call_bondexpup07_4
                show bg bathhouse1_blur at truecenter:
                    rotate 0
                    zoom 1
                show trei naked normal at left3, flip
                show khaleb naked smile at right3
                with dissolve
                Khaleb "That's it folks! We have a winner!!!"

                "Nice job, Arek. Come on over here and get what's yours."

                show arek naked smile2 at center1, flip
                with dissolve
                Arek "Hehe! You don't need to tell me that twice, bro."

                stop music fadeout 1.0
                play sound "audio/Schlop.ogg" volume 2.0 fadein 1.0 loop
                show khaleb naked normal at right2
                with dissolve
                Khaleb "Open wide..."

                hide trei
                show arek naked normal at left2:
                    zoom 1.5
                show khaleb naked normal at right2:
                    zoom 1.5
                show ratio1
                with dissolve
                Arek "Mm-Mmmph!!"

                if khaleb_bathhouse_first == False:

                    $ khaleb_bathhouse_first = True

                    "You resurface only to immediately blush at the sight of Khaleb's long, snake-like tongue disappearing into Arek's open, waiting mouth."

                    "The two of them then interlock muzzles in a big, sloppy kiss that feels like it lasts forever."

                    show arek hard normal
                    with dissolve
                    "The mystery of just what that tongue is doing in his throat leaves you transfixed, as you watch the pup absolutely melt in his friend's attentive arms."

                    #(Ending where Marcus bursts in)

                    jump bathhouse_khaleb_end

                else:

                    "You blush even harder than you already are at the sight of Khaleb's long, snake-like tongue disappearing into Arek's open, waiting mouth."
                    
                    "The two of them then interlock muzzles in a big, sloppy kiss that feels like it lasts forever."
                    
                    show arek hard normal
                    with dissolve
                    "Imagining everything that tongue could be doing in his throat leaves you transfixed, as you watch the pup absolutely melt in his friend's attentive arms."
                    
                    Fen hot "Oh, woah...!"
                    
                    stop sound fadeout 1.0
                    "Eventually, the kiss ends once you see Arek turn blue in the face, and he falls over coughing and gasping for air."
                    
                    "You also notice that he's just as rock hard erect as you are despite that, though."

                    jump bathhouse_khaleb_end
            
            else:

                "{color=#16f58d}{i}Strength Check 10 - Success{/i}{/color}"

                "You're able to exert enough power in your arms to gradually pry yourself free from his clawing grip." with hpunch

                "While he's busy cursing you out, you're able to twist his arms back enough to make him finch." with hpunch

                hide fen
                hide arek
                hide ratio1
                show bg bathhouse1 at truecenter:
                    zoom 1
                with vq_dissolve
                "That gives you enough time to spin him around and pin his paws behind his back into a grapple of your own."

                "As the hyena barks and thrashes desperately, you make a sweep at his legs to knock him off balance."
                
                play sound "audio/big splash.ogg" volume 2.0
                "And he comes falling face-first into the water with a tremendous splash." with vpunch

                #Sound of some claps from Khaleb and Arek
                play sound "audio/clapping.ogg" volume 1.0
                $ bondexp07 += 3
                call bondexpup07 from _call_bondexpup07_5
                show bg bathhouse1_blur at truecenter:
                    rotate 0
                    zoom 1
                show trei naked normal at left3, flip
                show khaleb naked smile at right3
                with dissolve
                Khaleb naked smile "That's it folks! We have a winner!!!"

                Khaleb naked normal "Not too shabby, kid. Now come on over so I can give ya something real nice."

                show fen naked smile2 at center1
                with dissolve
                Fen "Ahahaha! Thanks. But it was nothing, really."

                jump bathhouse_khaleb_kiss_you

        label about_no_one_wrestle:

            Fen naked stern "Sorry but you all look like you're causing a scene in here."

            Fen "I don't want to be a part of it when you end up getting caught."

            show khaleb naked normal at right1
            hide arek
            hide trei
            with dissolve
            Khaleb "Aw, come on. Who're people gonna go complain to? That lard bag geezer what owns the joint?"

            Khaleb naked smile "I'll bet he's already gone so deaf, he'll barely be able to catch two words they tell him."

            Khaleb naked normal "And even if he does find out, I'll betcha anything we could outpace those stubby rhino legs of his with a fast walk outta here before he sees us."
           
            Fen naked sweat "Uh, I'm not sure if you know Marcus anywhere near as well as you—"
            
            hide fen
            hide khaleb
            show trei naked normal at left2, flip
            show arek naked normal at right2
            with dissolve
            Trei "Haha! Right on, Khaleb, man! Wrestle party foreva!!!"
            
            show arek naked sweat at shock
            Arek "Ey, ey! What are ya—Whoa!"
            
            play sound "audio/big splash.ogg" volume 1.0
            #water sound
            hide trei
            hide arek
            show bg bathhouse1
            with vpunch
            "In a burst of spontaneous energy, the hound picks up his shorter friend by his scruff and chucks him back into the water like a potato sack."
            
            "He goes in screaming and causes a big splash that reverberates all throughout the room."
            
            "{color=#b641b2}???{/color}" "What's going on in there?"
            
            show khaleb naked sweat at center1
            show bg bathhouse1_blur
            with dissolve 
            Khaleb "Ooh...Yeah, that definitely might've overdone it a tad..."

            jump bathhouse_khaleb_end

        label bathhouse_khaleb_end:
            stop sound fadeout 1.0
            stop music fadeout 1.0
            play sound "audio/Door Open 2.ogg" volume 2.0
            show bg bathhouse1 at truecenter:
                zoom 1
            hide ratio1
            hide trei
            hide arek
            hide khaleb
            hide fen
            with hpunch
            "Suddenly, the doors to the bathroom burst open, making the lusty mood vanish instantly as a cold draft pours in."

            show marcus angry at right1
            show bg bathhouse1_blur
            with dissolve
            Marcus angry "Ah-ha! So this is who's been causing all those complaints."

            show fen naked shock at left1
            with dissolve
            Fen "Wha–? No, no, wait! You've got it wrong. I'm not–"

            call bondexpdown06 from _call_bondexpdown06
            $ bondexp06 -= 3
            show marcus angry
            Marcus angry "{sc=1.5}{b}{size=50}Save it!{/size}{/b}{sc}" with vpunch
            
            Marcus "All of you are getting your butts out of here right now before I call the guards to come and kick them out!" with vpunch

            hide marcus
            hide fen
            show khaleb naked sweat at center1
            with dissolve
            Khaleb "Eh, so it goes."

            Khaleb naked normal "Thanks for hanging with us, kid. It's been real. We oughta do this again sometime soon."

            hide khaleb
            show bg bathhouse1
            with dissolve
            "You are definitely{i} not {/i}doing anything like this again with them any time soon."

            "You just hope that, with any luck, you'll be able to explain things better to Marcus later."

            $ bathhouse_khaleb_done = True

            jump day_end

        label bathhouse_khaleb_2nd:
            hide fen
            show bg bathhouse1 at center:
                zoom 1
            with dissolve
            "You luxuriate for a while here in a space that is completely empty..."
            
            play music "audio/Khaleb_theme.ogg" volume 2.0 fadein 3.0
            show khaleb naked normal at center1
            show bg bathhouse1_blur
            with dissolve
            "All except for Khaleb and his crew, who are making noise and play fighting again."

        label khaleb_bathmenu_02:
        
        "After what happened the first time, you probably shouldn't approach them."
        
        "But maybe there's a reason to?"
        
        menu:
            "No, just keep to yourself":
                jump about_khaleb_bath_no
                
            
            "Ask if you can challenge Trei":
                
                Khaleb "Hold up now, you wanna what?"
                
                Fen "Ask if I could wrestle Arek like you guys were doing before."
                
                Fen "You, uh...made it look really fun the other time, so I was wondering. Hehe..."
                
                Khaleb "And you'd wanna go at it with the pepper strip mutt? Want me to offer the same prize as last time, too?"
                
                Fen "Y-Yes, please."
                
                Khaleb naked smile "Well, damn. If that's how it is, then sure."
                
                Fen "Really?"
                
                Khaleb naked normal "You caught me in a generous mood today, kid, so why the heck not? Consider your wish granted."
                
                show khaleb at shock
                Khaleb "Yo, Trei! Come over here for a sec?"
                
                show trei naked normal at right1
                with dissolve
                Trei "Oh hey, bro, how's it hangin'? We having fun with the busboy again?"
                
                Khaleb "Orange Zesty over here wants to challenge you to a match in the water. You game?"
                
                show trei at shock
                Trei "Are ya kiddin'? I'm always down for a good brawl!"
                  
                Khaleb "Great, then let's get the both of yaz into position."

                Khaleb naked smile "Heave-fuckin'-ho!"

                play sound "audio/big splash.ogg" volume 2.0
                hide khaleb
                hide arek
                hide trei
                show bg bathhouse1 at truecenter:
                    zoom 3
                    rotate -300
                with vpunch
                "Like a stone, Khaleb and Arek toss you into the centre of the pool where Arek waits expectantly for just this moment."

                jump about_trei_wrestle_2

            "Ask if you can challenge Arek":

                Khaleb "Hold up now, you wanna what?"
                
                Fen "Ask if I could wrestle Arek like you guys were doing before."
                
                Fen "You, uh...made it look really fun the other time, so I was wondering. Hehe..."
                
                Khaleb "And you'd wanna go at it with the dough ball mutt? Want me to offer the same prize as last time, too?"
                
                Fen "Y-Yes, please."
                
                Khaleb naked smile "Well, damn. If that's how it is, then sure."
                
                Fen "Really?"
                
                Khaleb "You caught me in a generous mood today, kid, so why the heck not? Consider your wish granted."
                
                show khaleb at shock
                Khaleb "Yo, Arek! Come over here for a sec?"
                
                show arek naked normal at left1, flip
                with dissolve
                Arek "Yeah, bro? Ya needed something?"
                
                Khaleb "Orange Zesty over here wants to challenge you to a match in the water. You game?"
                
                show arek naked smile2 at shock
                Arek "Heck yeah, I am!"
                
                Khaleb "Great, then let's get the both of yaz into position."
                
                Khaleb naked smile "Heave-fuckin'-ho!"
                
                play sound "audio/big splash.ogg" volume 2.0
                hide khaleb
                hide arek
                hide trei
                show bg bathhouse1 at truecenter:
                    zoom 3
                    rotate -300
                with vpunch
                "Like a stone, Khaleb and Trei toss you into the centre of the pool where Arek waits expectantly for just this moment."

                jump about_arek_wrestle_2

    label about_khaleb_bath_no:

        hide khaleb
        hide arek
        hide trei
        show bg bathhouse1
        with dissolve
        "You know well enough to warn them that you're going to tell Marcus, if they start acting too rowdy or try getting you involved in it again."

        "You'd rather not risk looking like a troublemaker."

        stop music fadeout 3.0
        "With that established, you find a nice corner to soak in by yourself and get what little rest you can before heading off."

        jump bathhouse_common_end

    label bathhouse_common_end:

        stop music fadeout 3.0

        if cha_from_commonpool < 3:
            $ cha_from_commonpool += 1
            call cha_up from _call_cha_up
            "Your charm increases as a result of the bath!"

        else:
            "It seems like you can't gain any more charm from this pool."
            pass

        jump day_end

label bathhouse_luxury:
    $ fen_coins -= 10
    play sound "audio/payment.ogg" volume 3.0

    #Add random encounters here!!!
    #'common', 'common', '???',
    $ luxurypool_event = renpy.random.choice(['common', 'murry'])

    if luxurypool_event == 'common':
        jump bathhouse_luxury_common

    if luxurypool_event == 'murry':
        jump bathhouse_luxury_murry

    label bathhouse_luxury_common:
        "Marcus hands you a wooden box with a plush towel."
        
        #show Fen naked
        stop music fadeout 3.0
        hide marcus
        show bg bathhousehall
        with dissolve
        "You place your clothes into the box and store it on the shelf."

        play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
        scene bg bathhouse2
        show fog
        with s_dissolve
        "The pool is much smaller than the public bath. A mixture of floral aromas fills the air here."

        #Add random event here
        "Some of the faces you vaguely recognize as merchants and a couple of adventurers lounging on marble benches around plumes of steam."

        show fen naked relax at center1 behind fog
        show bg bathhouse2_blur
        with dissolve
        "You find a quiet spot to rinse off and enjoy the heat of the sauna."

        hide fen
        show bg bathhouse2_blur:
            zoom 1.5
        show material gemfruit at truecenter:
            zoom 2
        show ratio1
        with dissolve    
        "There are small tables with bowls filled with shinny fruits and some with pitchers and cups."

        hide ratio1
        hide material gemfruit
        show fen naked lick at center1, flip
        show bg bathhouse2_blur:
            zoom 1
        with dissolve
        "You help yourself to a few delicious berries."

        "The heat of the sauna makes you want something sweet and cold to drink."

        "The pitchers are filled with what smells like fruit juice. The condensation running down the side of the container indicates the contents are chilled."

        hide fen
        show bg bathhouse2
        with dissolve
        "The cool juice hits the spot as you soak your worries away in the Narcissus pool."

        "Eventually you start to feel a bit dizzy from the abundant heat and humidity."

        "Refreshed and relaxed from your premium bath, you redress and go back home."

        "You let the rest of the day pass by lazily after treating yourself to something nice."

        jump bathhouse_luxury_end

    label bathhouse_luxury_murry:
        if bond05 == 0:
            jump bathhouse_luxury_common
        
        else:
            pass
        #Triggers after selecting Luxury bath option 

        Marcus grin "By the way, you might want to be careful around the pools today."

        Fen "Why's that?"

        Marcus smile "It tends to get messy when Murry visits."

        Fen "Oh, Murry's here?"

        Marcus grin "Yep. Little guy seems to really be enjoying himself, as well as some of the other guests lately."

        Fen "I'm glad to see him relaxing."

        Marcus smile "You could call it that, it brings in good money without too much extra work."

        hide marcus
        show bg bathhousehall
        with dissolve
        "Marcus hands you your bath bucket and you head towards the steamy pools."

        #scene change
        play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
        scene bg bathhouse2
        show fog
        with s_dissolve
        "As you enter the pool, you can hear loud slapping and moaning."

        if bathhouse_murry_done == False:
            "Sounds and Smells like... Murry?"
        else:
            "You know that the source could be no other than Murry getting fucked."

        show fen naked blush at center1
        show bg bathhouse2_blur
        with dissolve
        "Slowly creeping towards the noise and through the steam, you spot the little merchant."

        jump continue_Murry_2

        label continue_Murry_2:

            menu:
                "What to do..."

                "Shy away.":
                    jump Murry_sex_reserved

                "Get closer.":
                    jump murry_sex_intro

        label Murry_sex_reserved:
            hide fen
            show bg bathhouse2
            with dissolve
            "You turn away and distance yourself from the sounds of the debauchery unfolding behind you."

            "Setting that aside, you take a moment to unwind, enjoying the soothing warmth of the pool and sauna."
            
            #jump to normal luxury bathhouse scene
            jump bathhouse_luxury_end

        label murry_sex_intro:

            $ murry_partner = renpy.random.choice(['saur', 'gatr'])
            #Show cg of feralgatr or venusaur 
        
            if murry_partner == 'gatr':
                jump murry_partner_gatr_start

            if murry_partner == 'saur':
                jump murry_partner_saur_start
            
            else:
                pass

            #Feralgatr \ blue guy
            label murry_partner_gatr_start:
                play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0
                $ murry_partner = 'gatr'
                scene murrycg1 b 00
                with s_dissolve
                "Murry is together with a huge blue gator. His companion seems completely ready to stuff his huge cock into the much smaller male."

                "The blue hulk sports an enormous shaft, easily the size of one of Murry's legs."

                scene murrycg1 b 01
                with s_dissolve
                "He holds Murry with ease, spreading the merchant's plump cheeks apart."

                scene murrycg1 b 01a at truecenter
                with s_dissolve
                "As he reveals the smaller male's hole to everyone at the bathhouse, your eyes are unable to look away from the gator's growing erection."

                "The massive blue rod rises to full attention till the throbbing tip of that blue monster grinds against Murry's smaller bits."

                jump Murry_sex_menu1

            #Venusaur \ green guy
            label murry_partner_saur_start:
                play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0
                $ murry_partner = 'saur'
                scene murrycg1 a 00
                with s_dissolve
                "You spot Murry sitting on a massive green cock. The amphibian-like cohort is gently humping his length against the tiny merchant."

                "The big spotted man sports an impressive belly on which the smaller male rest upon."

                scene murrycg1 a 01
                with s_dissolve
                "He easily lifts Murry into prime fucking position, letting spreading his ass to reveal his perky little hole between those plump cheeks."

                scene murrycg1 a 01a at truecenter
                with s_dissolve
                "You watch in wonder as the massive cock comes to life and rises between Murry's legs."

                "The thick green shaft pulses with anticipation to be pureed into Murry."

                "Pre leaks down his tip and Murry's cock as the Merchant looks longingly at the green beast below."

                "Their clear fluids mix as the man starts to grind gently, Murry is ready to be split in half."

                jump Murry_sex_menu1

        label Murry_sex_menu1:

            $ config.menu_include_disabled = True
            menu:
                "What do you do?"

                "Stay a respectful distance.":
                    $ config.menu_include_disabled = False
                    jump Murry_sex_open

                "Grab yourself a front row seat!" if FenSXP >= 10: #sxp lock
                    $ config.menu_include_disabled = False
                    jump Murry_sex_front_row

        label Murry_sex_open:
            $ bondexp05 += 1
            call bondexpup05 from _call_bondexpup05_2
            "You lean in a bit closer to give yourself a nice view of the action."

            if murry_partner == 'gatr':
                scene murrycg1 b 01a at top:
                    zoom 1.5
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 01a at top:
                    zoom 1.5
                with s_dissolve

            else:
                pass    
            "Murry notices you and leans up from his partner's pillowy chest."

            Murry "Oh [name], fancy meeting you here."

            Fen "H-Hey Murry."

            stop music fadeout 3.0
            "He gives you a wink as his partner hoists him into position."

            jump murry_sex_cont

        label Murry_sex_front_row:
            $ bondexp05 += 2
            call bondexpup05 from _call_bondexpup05_3
            "You step right up to Murry and his partner for a front row seat to the show."

            if murry_partner == 'gatr':
                scene murrycg1 b 01a at top:
                    zoom 1.5
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 01a at top:
                    zoom 1.5
                with s_dissolve

            else:
                pass
            "Murry notices you and leans up from his partner's pillowy chest."

            Murry "O-Oh, a-ah, hey [name]."

            "You see his cock throb in anticipation of being impaled."

            Murry "Enjoying the show?"

            Murry "Not so shy anymore, huh?"

            Fen "Well you just looked so inviting."

            stop music fadeout 3.0
            Murry "Well of course I do!"

            jump murry_sex_cont

        label murry_sex_cont:
            play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
            if murry_partner == 'gatr':
                scene murrycg1 b 01a at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 01a at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            "Murry smiles and leans back into the big belly of his hulking companion."

            "His legs are spread wide apart, offering everyone in the steamy room an unfettered view of his cock and balls."

            "Below Murry, his partner's massive cock stands at full attention with a heavy set of orbs full of pent up seed."

            play sound "audio/Body Flesh 2.ogg" volume 2.0
            if murry_partner == 'gatr':
                scene murrycg1 b 02 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 02 at truecenter:
                    zoom 1
                with dissolve

            else:
                pass 
            "Without hesitation, it rammed in."

            "You can't help but stare in wonder at how the tiny guy takes that entire massive thick meat log."

            if murry_partner == 'gatr':
                scene murrycg1 b 03 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 03 at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            play fuck "audio/fuck mid 1.ogg" volume 3.0 fadein 1.0
            play ball "audio/ball hits 1.ogg" volume 3.0 fadein 1.0
            play nsfw1 "audio/deep moan 1.ogg" volume 1.0 fadein 1.0
            "And just like that, the show began."

            "With each thrust, a distinct bulge appears on the raccoon's stomach, marking the intensity of the motion."

            "The charm bouncing off shines with a brilliant green light as Murry's innards are rearranged before you."

            "Imagining taking such a huge piece of meat causes your own arousal to stir."

            "Wet slapping noises echo with various grunts in the steamy bath, alerting you to the larger audience."

            "Murry groans as his partner pulls his body back down on their hips, burying their entire shaft into him."

            "You can clearly make out the bulge in Murry's belly throb."

            "Murry's escapades draws in a crowd of patrons that watch with excitement."

            "There is more than one type of excitement observed as you spot a couple of older merchants stroking each other as they watch the little guy bounce up and down."

            "The massive cock forces itself all the way into the raccoon, making the jiggling belly bulge obscenely." 

            "To Murry, there is no discomfort, only bliss from the thick pipe lodged inside him plows away into his body like a comical fuck sleeve."

            "The sloshing bounce of Murry's belly is mesmerizing watching his body stretch to accommodate the sheer mass of the much larger male."

            "You stroke yourself, watching the little man display his perverted act to all around."

            if murry_partner == 'gatr':
                scene murrycg1 b 04 at truecenter:
                    zoom 1.2
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 04 at truecenter:
                    zoom 1.2
                with s_dissolve

            else:
                pass
            Murry "O-Oh fuck!"

            "The merchant groans as the bulge pushes out like an arm punching from beneath his fur."

            "Murry's cock flops against the bulge protruding above his belly."

            "Every thrust forces the blunt tip of his companion's cock push right above his belly button."

            "This in turn pushes out the air from Murry's lungs, causing his moans to end in sharp peaks."

            "The merchant's body takes the abuse without any signs of discomfort."

            "In fact, Murry looks like he's having the time of his life being split in half by a hulking man with a cock half the length of the raccoon."

            "More patrons have gathered to bear witness to the head merchant letting loose in the upscale bathhouse."

            "Grunts and moans among the audience built along with the speed of Murry's partner."

            play fuck "audio/fuck fast 1.ogg" volume 3.0 fadein 1.0
            play ball "audio/ball hits 2.ogg" volume 3.0 fadein 1.0
            play nsfw1 "audio/deep growls 1.ogg" volume 1.0 fadein 1.0
            if murry_partner == 'gatr':
                scene murrycg1 b 05 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 05 at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            "Things are getting hot and steamy, and not because of the hot water."

            "The crowd is focused on the action, openly jerking it to the display. You included."

            "The man's fat balls slapped into the tiny rump while he pulled Murry down against his thrust, forcing his cock deeper into the stretchy raccoon."

            "He groans as his girthy shaft disappears all the way into Murry, almost poking into the smaller man's chest."

            "Everyone can tell the guy's about to erupt."

            "His balls pull up and his hands grip Murry's little thighs, yanking him down onto his throbbing cock."

            stop fuck fadeout 2.0
            stop ball fadeout 2.0
            stop nsfw1 fadeout 2.0
            play vocal1 "audio/deep climax 1.ogg" volume 1.0
            if murry_partner == 'gatr':
                scene murrycg1 b 06 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 06 at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            play sound "audio/Schlop.ogg" volume 3.0 loop fadein 1.0
            "With the bulbous tip pushing out from Murry's belly, everyone can see the orgasmic explosion unfold."

            "He unleashes a bellowing roar as hot cum spews inside Murry with such force, you can see it stretching his belly beneath his fur."

            if murry_partner == 'gatr':
                scene murrycg1 b 07 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 07 at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            "Murry is completely lost in the sensation of being filled."

            "You can make out every throb of the man's cock as it pulses inside the merchant."

            if murry_partner == 'gatr':
                scene murrycg1 b 08 at truecenter:
                    zoom 1.2
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 08 at truecenter:
                    zoom 1.2
                with s_dissolve

            else:
                pass
            "Each jet of virile seed gushes into Murry, filling him slowly like a balloon."

            "You can imagine every gush coming from that massive thing lodged with Murry is crushing his prostate into new shapes."

            "Your cock throbs harder as you think about what that would feel like if it were you."

            "Soon the clear outline of the man's tip poking out from his stomach fades, leaving only a slowly growing belly."

            "The man's thrusting gradually slows until his shaft no longer moved."

            "Only the continuous torrent of cum spilling out from the enormous cock lodged within Murry kept his bulbous belly bouncing."

            "Murry trembles from the immaculate pressure building inside him culminating into a burst of pleasure."

            "The racoon's smaller cock explodes and he releases his own orgasm all over himself."

            "With a long groan, he starts to pull out from Murry's stretched hole."

            if murry_partner == 'gatr':
                scene murrycg1 b 09 at center:
                    zoom 1.3
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 09 at center:
                    zoom 1.3
                with s_dissolve

            else:
                pass
            "{size=50}POP!{/size}"

            "Like a cork in the neck of a bottle, the man's fat dong plops out from Murry's ass."

            "Buckets of creamy cum leak out from Murry's still tight hole."

            if murry_partner == 'gatr':
                scene bg white at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene bg white at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            "You let out an audible groan as you finally let loose as well."

            if murry_partner == 'gatr':
                scene murrycg1 b 10 at truecenter:
                    zoom 1
                with s_dissolve

            if murry_partner == 'saur':
                scene murrycg1 a 10 at truecenter:
                    zoom 1
                with s_dissolve

            else:
                pass
            "His heavy breathing causes that giant belly to slosh gently as he catches his breath."

            "Excess cum splatters loudly against the floor of the bath. Thankfully there's a nearby drain for it to wash away into, leaving little mess behind."

            "Murry settles against the big man as creamy white seed drips from his used hole."

            if murry_sxp_1 == False:
                $ murry_sxp_1 = True

                call sxp_up from _call_sxp_up_18
            
            else:
                pass
            "It looks like some of the other occupants in the bahthouse have also spilled a bit of their own excitement on Marcus's floors."

            stop sound fadeout 3.0
            scene bg bathhouse2
            with s_dissolve
            "Now that the show's over, most of the crowd dispersed and the big guy helped Murry get cleaned up."

            "You quickly get back to finishing your own bath while quietly waiting for your still very much stiff erection to die down."

            $renpy.end_replay()

            $ bathhouse_murry_done = True

            stop music fadeout 3.0

            if cha_from_luxurypool < 3:
                $ cha_from_luxurypool += 1
                call cha_up from _call_cha_up_5
                "Your charm increases as a result of the... sauna?"

            else:
                "It seems like you can't gain any more charm from... sauna?"

                pass

            jump day_end

    label bathhouse_luxury_end:
        
        stop music fadeout 3.0

        if cha_from_luxurypool < 3:
            $ cha_from_luxurypool += 1
            call cha_up from _call_cha_up_1
            "Your charm increases as a result of the sauna!"

        else:
            "It seems like you can't gain any more charm from sauna."
            pass

    jump day_end

label bathhouse_private_menu:

    Marcus grin "Here for a massage, aren't you? I've been looking forward to serving you."

    Marcus normal "So, would you like to blend some oil to your preference?"

    menu:

        "Yes, I'd like that.":
            jump oil_mix
        
        "No, let's get started.":

            Marcus smile "Can't wait any longer, huh? Well then, follow me."

            scene bg bathhouse3
            with s_dissolve
            stop music fadeout 3.0
            "You follow Marcus to his private room."

            play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
            "In addition to the pool and massage table, the room is decorated with various large leaves and potted flowers."
            
            jump bathhouse_private_massage

label bathhouse_private:
    $ fen_coins -= 30
    play sound "audio/payment.ogg" volume 3.0

    if bond06 >= 2:
        jump bathhouse_private_menu
    
    else:
        pass

    "Marcus eyes you up and down."

    Marcus grin "Did you know that you're pretty cute?"

    Fen grin "You're not bad looking yourself."

    Marcus smile "I'd like to know what that fur really feels like."

    Fen "How about a massage?"

    Marcus grin "Follow me to the private bath."

    stop music fadeout 3.0
    scene bg bathhouse3
    with s_dissolve
    "You enter the big guy's private room."

    play music "audio/bathtubambient.ogg" volume 1.0 fadein 3.0
    "On one side is a large tub filled with steaming water. On the other side is a large table covered in padded boards."

    label bathhouse_private_massage:
        pass
    
    show marcus grin at right1
    show bg bathhouse3_blur
    with dissolve
    Marcus grin "You know the rules."

    show fen 2 blush at left1
    with dissolve
    Fen "Of course."

    show fen naked blush
    with dissolve
    "You strip naked."

    Marcus normal "Come here and lay down."

    show fen at shock
    Fen "Hey, don't the rules apply to you as well?"

    Marcus grin "Heh, well let me just slip into something more comfortable."

    hide fen
    show marcus normal at center1:
        zoom 1.5
    show bg bathhouse3_blur at truecenter:
        zoom 1.5
    show ratio1
    with s_dissolve
    "He slides his thumb beneath the sling of his toga."

    show marcus pants grin
    with s_dissolve
    "He gently tugs it off his bulging shoulder and lets it slide off his muscular bicep."

    show marcus uw grin
    with s_dissolve
    "He spins around and shakes his rump to kick off the white cloth."

    "His ample ass cheeks jiggle as he swings his hips left and right like a pendulum."

    "Teasing your eyes with a few more shakes of his hips, Marcus slides his underwear off."

    show marcus naked grin
    with s_dissolve
    "The proprietor reveals his smooth purple hide in its entirety."

    "He continues to sway side to side, letting his impressive meat slap the sides of his thighs each time." 

    "Your eyes follow his cock as it smacks left and right with each sway of his hips."

    hide ratio1
    hide marcus
    show bg bathhouse3 at truecenter:
        zoom 1
    with s_dissolve
    "The hypnotic display is broken when he pats the table and licks his lips."

    show marcus naked grin at right1
    show fen naked hot2 at left1
    show bg bathhouse3_blur
    with dissolve
    Marcus "Better?"

    show fen at shock
    Fen naked hot2 "Yeah!"

    hide marcus
    hide fen
    show ratio1
    show bg bathhouse3 at truecenter:
        zoom 1.5
    with s_dissolve
    "You hop onto the table and lay on your belly. There's a groove for your head to fit comfortably in."

    "You feel the larger man's hands start to roam along your back." 

    "Your tail wags as his fingers squeeze and knead your muscles gently while stroking your fur."

    # If you made oil mix
    if oil_mix_value >= 1:
        "You feel Marcus apply the oil mixture on you, starting with your back and then moving to your limbs."

        "The warm oil provides a gentle sensation on your fur and skin, and the scent grows stronger as it evaporates into the air."

        if oil_mix_value == 3:

            Marcus "Oh this has a pleasant tingle. It kind of reminds me of Gunther."

        if oil_mix_value == 4:
            
            Marcus "Oh this is cool to the touch with a little bit of sweetness. I love the colours on this."

        if oil_mix_value == 6:
            
            Marcus "This has a lovely smell and color, I can see this being popular with couples."

            Marcus "This would also go great in a soap."

        if oil_mix_value == 7:
            
            Marcus "Wow, just look at how this sparkles in the light. I think it will be a hit at the Narcissus pool."

        if oil_mix_value == 8:
            
            Marcus "This is a really soothing mix. It reminds me of a green field of flowers."

            Marcus "It's a very sweet and calming aroma, much like you."

        else:
            pass

        "Aside from the pleasant aroma, the oil does not appear to have any other effects."

    else:
        pass


    $ oil_mix_value = 0
    
    Marcus "Heh, someone's feeling good."

    Fen "Y-yeah."

    "You let Marcus dig his strong hands into your back."

    "All the tension from working melts away from the pressure of a man four times your size digging along your shoulder blades and down your spine."

    "He pushes up and down along your lower back, melting away the knots in your muscles."

    "You feel his massive paws smack upon your fuzzy rump."

    play sound "audio/light moan 2.ogg" volume 1.0 loop fadein 3.0
    Fen "Ah-aahhh~"

    "Marcus kneads each globe of your asscheek, kneading and squeezing along your glutes and thighs."

    "He then flips you over onto your back with ease."

    Fen "Eep."

    "Marcus digs his fingers into the sides of your neck."

    "The firm pressure almost hurts but as he moves shoulders and upper arm"

    "His massive hands squeeze your arms until they feel like putty."

    "The masseur slides his hands upon your chest, give your pecs a good grope."

    Fen "Mrr~"

    Marcus "Heh."

    "He continues to work down to your thighs and legs."

    "You feel his fingers trace along your cock, but he appears to keep everything professional." 

    hide ratio1
    show bg bathhouse3:
        zoom 1
    with s_dissolve
    "Time melts away with your stress as Marcus works his magic on your sore bones."

    play sound "audio/Slap 1.ogg" volume 2.0
    "As you feel like about to pass out by the end of it until a light smack on your cheek brings you back to the waking world."

    show marcus naked normal at right1
    show bg bathhouse3_blur
    with dissolve
    Marcus "Alright, I can't be gone too long. I hope you enjoyed your massage."

    show fen naked relax2 at left1
    with dissolve
    Fen "Hnggg..."

    $ bondexp06 += 3
    call bondexpup06 from _call_bondexpup06_5
    Marcus naked smile "I'll take that as a yes."

    $ show_workday_option('marcus_work_option')

    hide fen
    hide marcus
    show bg bathhouse3
    with dissolve
    "After spending more time in the warm pool, You stumble out from the bathhouse feeling radiant and stress free."

    if cha_from_privatepool < 4:
        $ cha_from_privatepool += 1
        call cha_up from _call_cha_up_2
        "Your charm increases as a result of the massage!"

    else:
        "It seems like you can't gain any more charm from massage."
        pass

    jump day_end

label lunch_service:

    if lunch_service_first == False:

        $ lunch_service_first = True

        scene bg kitchen
        with s_dissolve

        show fen stern at left1
        show bg kitchen_blur
        with dissolve
        Fen "You wanted to talk with me about something new to do for the tavern, boss?"
            
        show gunther normal at right1
        with dissolve
        Gunther "Ah, [name]. Yeah, I had this idea about what else you could do for the daytime hours before we open, if you want."

        Gunther stern "I noticed we often have more raw ingredients left over at the end of the day after meal prep than we need."

        Gunther normal "So, what do you think about just making all of them into food in the morning and selling some as lunch out in front of the Flagon?"

        Fen normal "Oh, you mean we'd do something like a merchant stall they have out at the market?"

        Gunther "Yeah, kind of like that. I'd be a thing you could do instead of helping me tidy up the place before opening."

        Gunther wink "And I'll let you keep a certain percentage of what we make off the meals depending on how well we do on a given day."

        Fen "Alright, sure. I'm willing to give it a try."
            
        Fen smile "And who knows? We might be able to get some new regulars that way, too."

        show fen normal
        Gunther grin "Haha! That's the spirit!"

        Gunther normal "Remind me later to get a good table set aside for it and go buy some extra wooden bowls. I'll help you make the sign for it, too."

        Gunther "Just lemme know when you plan on doing it first thing before we get started with the work day."

        show fen smile2 at shock
        Fen "Yes, boss! Hehe~"
        
    else:
        pass

        stop music fadeout 3.0
    
    #IF ELSE by recipie number 0-4 5-9 10-19
    if get_success_recipe_count() <= 4:
        jump lunch_service_01

    if get_success_recipe_count() <= 9:
        jump lunch_service_02

    if get_success_recipe_count() <= 19:
        jump lunch_service_03

    else:
        pass

    label lunch_service_01:
        play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
        scene bg tavernfront
        with s_dissolve
        "You go outside to work the lunch stall this afternoon with a big, steaming cauldron of hearty soup and a basket full of yeast rolls to sell."

        "The soup, itself, is a slight variation on the classic pottage stew."

        "It's diluted a bit to make sure there's enough to go around, but it's still chock full of assorted veggies."
            
        $ lunchservice_event = renpy.random.choice(['few','few','lots'])

        jump lunch_service_end

    label lunch_service_02:
        play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
        scene bg tavernfront
        with s_dissolve
        "You head out and set up the lunch stall, arranging everything neatly."

        "Along with the usual soup and bread, there are a few new dishes freshly added to the menu, ready to entice customers."

        $ lunchservice_event = renpy.random.choice(['few','lots','lots'])

        jump lunch_service_end

    label lunch_service_03:
        play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0
        scene bg tavernfront
        with s_dissolve
        "You head out and set up the lunch stall."

        "With the newly expanded menu, there are now a variety of dishes on display, and everything looks fantastic, ready to impress your hungry customers."

        $ lunchservice_event = renpy.random.choice(['many','lots'])

        jump lunch_service_end

    #label lunch_service_04:
        #jump lunch_service_end

    label lunch_service_end:

        if lunchservice_event == 'few':

            "A while passes, and you only manage to sell about a handful of servings before you realise that you need to start packing it up."

            "Unfortunately, the street wasn't all that busy today, and your dish wasn't interesting enough to attract more customers on its own."

            "Looks like you'll just have to hope the rest of the food sells during regular hours, or else it's gonna have to get donated to someone, if not thrown away..."

            $ fen_coins += 2
            play sound "audio/payment.ogg" volume 3.0
            "You got 2 coins from the lunch service."

            stop music fadeout 3.0

            jump night_start

        if lunchservice_event == 'lots':

            "Before you know it, you're almost all sold out of the food you made!"

            "It seemed like the street was busy today with lots of townsfolk and travellers passing through, many of whom seemed eager to come look at your stall."

            "You're not sure if it was the meal you picked or just pure luck, but you made quite some extra coin today by filling the hungry tummies of the common folk."

            $ fen_coins += 5
            play sound "audio/payment.ogg" volume 3.0
            "Nice! You got 5 coins from the lunch service."

            stop music fadeout 3.0

            jump night_start

        if lunchservice_event == 'many':

            "The lunch business is booming today. It's clear that the new dishes are drawing in more guests."
            
            "You can tell many are stopping by just to sample the latest additions to the menu, eager to taste something fresh and exciting."

            $ fen_coins += 8
            play sound "audio/payment.ogg" volume 3.0
            "Great! You got 8 coins from the lunch service."

            stop music fadeout 3.0

            jump night_start


        else:
            pass

        jump night_start
