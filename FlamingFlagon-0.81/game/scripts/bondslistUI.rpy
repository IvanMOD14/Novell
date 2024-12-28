transform rotate_text:
    rotate -11.8
    ypos -200

transform rotate_text2:
    rotate -11.8
    ypos -150



default gunther_bond_ui = False
default terrance_bond_ui = False
default odachi_bond_ui = False
default niall_bond_ui = False
default murry_bond_ui = False
default marcus_bond_ui = False
default khaleb_bond_ui = False
default guards_bond_ui = False
default mjolnik_bond_ui = False

screen bondslist:
    image "gui/overlay/game_menu.png"
    image "ratio2.png"
    text "{color=#262626}{size=220}{font=GlowSans-Bold.otf}BONDS{/font}{/size}{/color}" at rotate_text

    frame:
        background None
        side ("c r"):
            area (200,250,1620,650)
            viewport id "bond_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                grid 2 6:
                    xalign 0.5
                    yalign 0.5
                    spacing 70

                    if gunther_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if gunther_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_gunther_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            textbutton _("{color=#a30326}{size=60}{font=GlowSans-Bold.otf}Gunther{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond01]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond01')

                    if terrance_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if terrance_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_terrance_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#f5693b}{size=60}{font=GlowSans-Bold.otf}Terrance{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond02]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond02')

                    if odachi_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if odachi_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_odachi_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            textbutton _("{color=#14b4dc}{size=60}{font=GlowSans-Bold.otf}Odachi{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond03]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond03')

                    if niall_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if niall_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_niall_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#5252ff}{size=60}{font=GlowSans-Bold.otf}Niall{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond04]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond04')

                    if murry_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if murry_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_murry_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#07bd84}{size=60}{font=GlowSans-Bold.otf}Murry{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond05]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond05')

                    if marcus_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if marcus_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_marcus_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#b641b2}{size=60}{font=GlowSans-Bold.otf}Marcus{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond06]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond06')

                    if khaleb_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if khaleb_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_khaleb_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#bcbcbc}{size=60}{font=GlowSans-Bold.otf}Khaleb{/font}{/size}{size=30}{font=GlowSans-Bold.otf}& Co{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond07]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond07')

                    if guards_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if guards_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_guards_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#bcbcbc}{size=60}{font=GlowSans-Bold.otf}Guards{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond08]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond08')

                    if mjolnik_bond_ui == False:
                        frame:
                            background "images/workday/choice_box_s.png"
                            xsize 750
                            ysize 168
                            xpadding 302
                            ypadding 0
                            xalign 0
                            yalign 0.5
                            text "{color=#9c9c9c}{size=110}{font=GlowSans-Bold.otf}???{/font}{/size}{/color}":
                                xpos 10

                    if mjolnik_bond_ui == True:
                        frame:
                            background "images/workday/chara_box_mjolnik_s.png"
                            xsize 750
                            ysize 168
                            xpadding 250
                            ypadding 0
                            xalign 0.5
                            yalign 0.5
                            textbutton _("{color=#a8a8a8}{size=60}{font=GlowSans-Bold.otf}Mjolnik{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size}   [bond10]"):
                                xalign 0
                                yalign 0.5
                                xpos -180
                                action ShowMenu('bond10')                  

            vbar value YScrollValue("bond_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    null height 20 #just a height set.


    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Return()







screen bond01:

    image "bg tavern2.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "gunther normal",
        "gunther blush",
        "gunther blush2",
        "gunther blush3",
        "gunther grin",
        "gunther shock",
        "gunther smile",
        "gunther smile2",
        "gunther stern",
        "gunther stern2",
        "gunther stresse",
        "gunther stresse2",
        "gunther stresse3",
        "gunther stresse4",
        "gunther sweat",
        "gunther sweat2",
        "gunther sweat3",
        "gunther wink",
        "gunther uw normal",
        "gunther uw blush3",
        "gunther uw smile2",
        "gunther uw stern",
        "gunther uw wink",
        "gunther naked normal",
        "gunther naked smile2",
        "gunther naked stern",
    ], npcstats_transform)

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond01]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp01]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  2{/size}") ypos 400 xpos 150

    text _("{color=#a30326}{size=110}{font=GlowSans-Bold.otf}Gunther{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Flaming Flagon Owner{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond01", dissolve)

screen bond02:

    image "bg tavernback.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "terrance normal",
        "terrance blush3",
        "terrance blush4",
        "terrance smile",
        "terrance stern",
        "terrance sweat normal",
        "terrance sweat smile",
        "terrance sweat stern",
        "terrance naked normal",
        "terrance naked smile",
        "terrance naked blush",
        "terrance naked blush2",
        "terrance naked blush3",
        "terrance hard normal",
        "terrance hard smile",
    ], npcstats_transform)

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond02]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp02]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  3{/size}") ypos 400 xpos 150

    text _("{color=#f5693b}{size=110}{font=GlowSans-Bold.otf}Terrance{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Cart Puller{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond02", dissolve)

screen bond03:

    image "bg townstreet_night.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "odachi normal",
        "odachi angry",
        "odachi blush",
        "odachi shock",
        "odachi smile",
        "odachi smile2",
        "odachi smile3",
        "odachi stern",
        "odachi stresse",
        "odachi sweat",
        "odachi naked normal",
        "odachi naked blush",
        "odachi naked smile",
        "odachi naked smile2",
        "odachi naked smile3",
        "odachi naked stresse",
        "odachi naked sweat",
        "odachi hard normal",
        "odachi hard smile",
    ], npcstats_transform)
    
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond03]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp03]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  2{/size}") ypos 400 xpos 150

    text _("{color=#14b4dc}{size=110}{font=GlowSans-Bold.otf}Odachi{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Lone Sellsword{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond03", dissolve)

screen bond04:
    image "bg guild.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "niall normal",
        "niall angry",
        "niall angry2",
        "niall blush",
        "niall blush2",
        "niall cry",
        "niall cry2",
        "niall hot",
        "niall lick",
        "niall shock",
        "niall smile",
        "niall stern",
        "niall stresse",
        "niall sweat",
        "niall sweat2",
        "niall wink",
        "niall naked normal",
        "niall naked blush",
        "niall naked blush2",
        "niall naked smile",
        "niall naked stern",
        "niall naked sweat",
        "niall naked wink",
    ], npcstats_transform)
    
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond04]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp04]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  1{/size}") ypos 400 xpos 150

    text _("{color=#5252ff}{size=110}{font=GlowSans-Bold.otf}Niall{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Aspiring Adventurer{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond04", dissolve)

screen bond05:

    image "bg stall.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "murry normal",
        "murry angry",
        "murry blush",
        "murry grin",
        "murry hot",
        "murry shock",
        "murry smile",
        "murry stern",
        "murry stresse",
        "murry sweat",
    ], npcstats_transform)
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond05]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp05]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  0{/size}") ypos 400 xpos 150

    text _("{color=#07bd84}{size=110}{font=GlowSans-Bold.otf}Murry{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Merchant on a Box{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond05", dissolve)

screen bond06:

    image "bg bathhousehall.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "marcus normal",
        "marcus angry",
        "marcus blush",
        "marcus blush2",
        "marcus grin",
        "marcus hot",
        "marcus shock",
        "marcus smile",
        "marcus stern",
        "marcus stern2",
        "marcus stresse",
        "marcus sweat",
        "marcus sweat2",
        "marcus pants grin",
        "marcus uw grin",
        "marcus naked normal",
        "marcus naked grin",
        "marcus naked smile",
    ], npcstats_transform)
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond06]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp06]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  2{/size}") ypos 400 xpos 150

    text _("{color=#b641b2}{size=110}{font=GlowSans-Bold.otf}Marcus{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Bathhouse Owner{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond06", dissolve)

screen bond07:

    image "bg alley2_night.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "khaleb normal",
        "khaleb angry",
        "khaleb grin",
        "khaleb shock",
        "khaleb smile",
        "khaleb smile2",
        "khaleb stern",
        "khaleb sweat",
        "khaleb naked normal",
        "khaleb naked grin",
        "khaleb naked smile",
        "khaleb hard normal",
        "khaleb hard grin",
        "khaleb hard smile",
        "arek normal",
        "arek angry",
        "arek blush",
        "arek blush2",
        "arek grin",
        "arek shock",
        "arek smile",
        "arek smile2",
        "arek smile3",
        "arek sweat",
        "arek naked normal",
        "arek naked blush",
        "arek naked blush2",
        "arek naked blush3",
        "arek naked smile2",
        "arek naked sweat",
        "arek hard normal",
        "arek hard grin",
        "arek hard smile",
        "trei normal",
        "trei angry",
        "trei blush",
        "trei smile",
        "trei stern",
        "trei stresse",
        "trei sweat",
        "trei naked normal",
        "trei naked angry",
        "trei naked stern",
        "trei naked sweat",
        "trei hard normal",
        "trei hard blush",
        "trei hard blush2",
        "trei hard shock",
        "trei hard sweat",
    ], npcstats_transform)
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond07]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp07]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  1{/size}") ypos 400 xpos 150

    text _("{color=#bcbcbc}{size=110}{font=GlowSans-Bold.otf}Khaleb{/font}{/size}{size=50}{font=GlowSans-Bold.otf} & Co{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Trouble Maker{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond07", dissolve)


screen bond08:

    image "bg townstreet.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "guards fussy normal",
        "guards fussy hot",
        "guards fussy hot2",
        "guards fussy hot3",
        "guards fussy smile",
        "guards fussy naked normal",
        "guards fussy hard blush",
        "guards carefree normal",
        "guards carefree eat",
        "guards carefree grin",
        "guards carefree naked",
        "guards carefree hard",
        "guards carefree hard pre",
        "guards energetic normal",
        "guards energetic grin",
        "guards energetic hot",
        "guards energetic hot2",
        "guards energetic hot3",
        "guards energetic tongue",
        "guards energetic naked",
        "guards energetic hard",
        "guards stoic normal",
        "guards stoic grin",
        "guards stoic smile",
        "guards stoic naked",
        "guards stoic hard",

    ], npcstats_transform)
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond08]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp08]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  0{/size}") ypos 400 xpos 150

    text _("{color=#bcbcbc}{size=110}{font=GlowSans-Bold.otf}Guards{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Town Guards{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond08", dissolve)


screen bond10:

    image "bg village.png"

    image "gui/overlay/game_menu.png"

    use character_stats([
        "mjolnik normal",
        "mjolnik blush",
        "mjolnik blush2",
        "mjolnik grin",
        "mjolnik shock",
        "mjolnik smile",
        "mjolnik stern",
        "mjolnik stern2",
        "mjolnik stresse",
        "mjolnik sweat",

    ], npcstats_transform)
    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level{/font}  [bond10]{/size}") ypos 200 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}  [bondexp10]{/size}") ypos 300 xpos 150

    text _("{size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}  0{/size}") ypos 400 xpos 150

    text _("{color=#bcbcbc}{size=110}{font=GlowSans-Bold.otf}Mjolnik{/font}{/size}{/color}") ypos 810 xpos 1800 xanchor 1.0

    text _("{size=40}{font=GlowSans-Bold.otf}Young Farmer{/font}{/size}") ypos 950 xpos 1800 xanchor 1.0

    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Hide("bond10", dissolve)