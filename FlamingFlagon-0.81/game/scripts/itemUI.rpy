transform itemui_size:
    zoom 0.6

#Use Item

label use_cha_candy:

    $ cha_candy -= 1

    call cha_up from _call_cha_up_3

    "You eat the candy!"

    return

label use_gold_apple:

    $ gold_apple -= 1

    call cha_up from _call_cha_up_4

    "You take a bite of the apple! It's not as delicious as you imagined, but you can feel your fur shining more after eating it."

    return

label use_vigorous_fungi:

    $ vigorous_fungi -= 1

    call str_up from _call_str_up_2

    "You take a bite of the fungi! It's actually not that bad, and you can feel your muscles grows a little bit after eating it."

    return

screen itemslist:
    image "gui/overlay/game_menu.png"
    image "ratio2.png"
    text "{color=#262626}{size=220}{font=GlowSans-Bold.otf}ITEMS{/font}{/size}{/color}" at rotate_text2

    frame:
        background None
        side ("c r"):
            area (200,250,1620,650)
            viewport id "item_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                grid 2 6:
                    xalign 0.5
                    yalign 0.5
                    spacing 70
                
                    if fen_coins >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/item 00.png" at itemui_size
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Coins{/font}{/size}{/color}":
                                xalign 0
                                yalign 0
                                xpos 200
                                action ShowMenu('item00')
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}Amount Left  [fen_coins]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                ypos 70

                    if gold_apple >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/item 06.png" at itemui_size
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Golden Apple{/font}{/size}{/color}\n{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf}+1 Charisma{/font}{/size}{/color}\n{size=28}Amount Left  [gold_apple]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                action ShowMenu('item06')
                            textbutton "{size=50}USE{/size}":
                                xalign 0
                                yalign 0
                                xpos 580
                                ypos 80
                                action Call("use_gold_apple")

                    if vigorous_fungi >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/item 07.png" at itemui_size
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Vigorous Fungi{/font}{/size}{/color}\n{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf}+1 Strength{/font}{/size}{/color}\n{size=28}Amount Left  [vigorous_fungi]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                action ShowMenu('item07')
                            textbutton "{size=50}USE{/size}":
                                xalign 0
                                yalign 0
                                xpos 580
                                ypos 80
                                action Call("use_vigorous_fungi")

            vbar value YScrollValue("item_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    null height 20 #just a height set.


    textbutton _("{size=50}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Return()




screen item00:

    image "bg market.png"

    image "gui/overlay/game_menu.png"

    image "gui/overlay/game_menu.png"

    image "item 00":
        ypos 200
        xalign 0.5

    text _("{size=40}{font=GlowSans-Regular.otf}The currency circulating in Felda. Coins of various value.\n\nThis money is not familiar to you. Where exactly did you come from...?{/font}{/size}") ypos 500 xalign 0.5

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("item00", dissolve)

#golden apple
screen item06:

    image "bg forest2.png"

    image "gui/overlay/game_menu.png"

    image "gui/overlay/game_menu.png"

    image "item 06":
        ypos 200
        xalign 0.5

    text _("{size=40}{font=GlowSans-Regular.otf}A special variety that exclusively grows in dungeons,\ndistinguished by their unique metallic sheen on the surface.\n\nLegend has it that consuming one will enhance your beauty.{/font}{/size}") ypos 500 xalign 0.5

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("item06", dissolve)

#Vigorous Fungi
screen item07:

    image "bg forest2.png"

    image "gui/overlay/game_menu.png"

    image "gui/overlay/game_menu.png"

    image "item 07":
        ypos 200
        xalign 0.5

    text _("{size=40}{font=GlowSans-Regular.otf}A special variety that exclusively grows in dungeons.\n\nLegend has it that consuming one will enhance your strength, \nbut must be eaten while still raw.{/font}{/size}") ypos 500 xalign 0.5

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("item07", dissolve)