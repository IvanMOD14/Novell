# Murry's stock
default murry_stock_01 = 1
#Golden Apple
default murry_stock_06 = 3
#Vigorous Fungi
default murry_stock_07 = 1
#Ember Fruit
default murry_stock_08 = 10

# Buy Item

label murry_buy_01:

    $ murry_stock_01 -= 1
    $ fen_coins -= 30
    $ cha_candy += 1

    play sound "audio/buy and sell.ogg" volume 3.0
    "Thank you for your purchase!"

    call screen murry_shop

label murry_buy_06:

    $ murry_stock_06 -= 1
    $ fen_coins -= 50
    $ gold_apple += 1

    play sound "audio/buy and sell.ogg" volume 3.0
    show murry smile
    Murry "Thank you for your purchase!"

    call screen murry_shop

label murry_buy_07:

    $ murry_stock_07 -= 1
    $ fen_coins -= 200
    $ vigorous_fungi += 1

    play sound "audio/buy and sell.ogg" volume 3.0
    show murry smile
    Murry "Thank you for your purchase!"

    Murry hot "Hehe, I bet this one will be VERY useful to you."

    call screen murry_shop

label murry_buy_08:

    $ murry_stock_08 -= 1
    $ fen_coins -= 10
    $ ember_fruit += 1

    play sound "audio/buy and sell.ogg" volume 3.0
    show murry smile
    Murry "Thank you for your purchase!"

    Murry normal "Interested in this one, huh? Best to remove the seeds before eating."

    call screen murry_shop

screen murry_shop:
    #image "gui/overlay/game_menu.png"
    image "ratio2.png"
    text "{color=#262626}{size=220}{font=GlowSans-Bold.otf}SHOP{/font}{/size}{/color}" at rotate_text2

    frame:
        background None
        side ("c r"):
            area (200,250,1620,650)
            viewport id "murryshop_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                grid 2 6:
                    xalign 0.5
                    yalign 0.5
                    spacing 70
                
                    if murry_stock_06 >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/item 06.png" at itemui_size
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Golden Apple{/font}{/size}{/color}":
                                xalign 0
                                yalign 0
                                xpos 200
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}Stock Left  [murry_stock_06]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                ypos 70
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}50 coins{/size}":
                                xalign 0
                                yalign 0
                                xpos 430
                                ypos 70
                            if fen_coins >= 50:
                                textbutton "{size=50}BUY{/size}":
                                    xalign 0
                                    yalign 0
                                    xpos 580
                                    ypos 80
                                    action Call("murry_buy_06")

                    if murry_stock_07 >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/item 07.png" at itemui_size
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Vigorous Fungi{/font}{/size}{/color}":
                                xalign 0
                                yalign 0
                                xpos 200
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}Stock Left  [murry_stock_07]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                ypos 70
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}200 coins{/size}":
                                xalign 0
                                yalign 0
                                xpos 430
                                ypos 70
                            if fen_coins >= 200:
                                textbutton "{size=50}BUY{/size}":
                                    xalign 0
                                    yalign 0
                                    xpos 580
                                    ypos 80
                                    action Call("murry_buy_07")

                    if murry_stock_08 >= 1:
                        frame:
                            background "images/workday/choice_box_s.png"
                            image "images/ingredients/dragonfruit_01.png" at itemui_size2
                            xsize 750
                            ysize 168
                            xpadding 20
                            xalign 0
                            yalign 0.5
                            textbutton "{color=#ffffff}{size=50}{font=GlowSans-Bold.otf}Ember Fruit{/font}{/size}{/color}":
                                xalign 0
                                yalign 0
                                xpos 200
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}Stock Left  [murry_stock_08]{/size}":
                                xalign 0
                                yalign 0
                                xpos 200
                                ypos 70
                            text "{color=#d6d6d6}{size=28}{font=GlowSans-Regular.otf} {/font}{/size}{/color}\n{size=28}10 coins{/size}":
                                xalign 0
                                yalign 0
                                xpos 430
                                ypos 70
                            if fen_coins >= 10:
                                textbutton "{size=50}BUY{/size}":
                                    xalign 0
                                    yalign 0
                                    xpos 580
                                    ypos 80
                                    action Call("murry_buy_08")

            vbar value YScrollValue("murryshop_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    null height 20 #just a height set.


    textbutton _("{size=50}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Jump("market_murry_menu")