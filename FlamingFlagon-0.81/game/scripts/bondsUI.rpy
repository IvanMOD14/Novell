screen bonds:
    image "gui/overlay/game_menu.png"

    frame:
        background None
        side ("c r"):
            area (400,200,1120,680)
            viewport id "bond_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 50

                    frame:
                        xpadding 60
                        ypadding 25
                        xalign 0.5
                        yalign 0.5
                        text "{color=#a30326}{size=50}{font=GlowSans-Bold.otf}Gunther{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}{/size} [bondexp01]        {size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size} [bond01]        {size=40}{font=GlowSans-Bold.otf}Bond Level Cap{/font}{/size} 1"

                    frame:
                        xpadding 60
                        ypadding 25
                        xalign 0.5
                        yalign 0.5
                        text "{color=#f5693b}{size=50}{font=GlowSans-Bold.otf}Terrance{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}{/size} [bondexp02]        {size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size} [bond02]        {size=40}{font=GlowSans-Bold.otf}Bond Level Cap{/font}{/size} 1"

                    frame:
                        xpadding 60
                        ypadding 25
                        xalign 0.5
                        yalign 0.5
                        text "{color=#14b4dc}{size=50}{font=GlowSans-Bold.otf}Odachi{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}{/size} [bondexp03]        {size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size} [bond03]        {size=40}{font=GlowSans-Bold.otf}Bond Level Cap{/font}{/size} 1"

                    frame:
                        xpadding 60
                        ypadding 25
                        xalign 0.5
                        yalign 0.5
                        text "{color=#5252ff}{size=50}{font=GlowSans-Bold.otf}Niall{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}{/size} [bondexp04]        {size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size} [bond04]        {size=40}{font=GlowSans-Bold.otf}Bond Level Cap{/font}{/size} 1"

                    frame:
                        xpadding 60
                        ypadding 25
                        xalign 0.5
                        yalign 0.5
                        text "{color=#07bd84}{size=50}{font=GlowSans-Bold.otf}Murry{/font}{/size}{/color}\n{size=40}{font=GlowSans-Bold.otf}Bond Points{/font}{/size} [bondexp05]        {size=40}{font=GlowSans-Bold.otf}Bond Level{/font}{/size} [bond05]        {size=40}{font=GlowSans-Bold.otf}Bond Level Cap {/font}{/size} 0"
            vbar value YScrollValue("bond_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    null height 20 #just a height set.

    
    textbutton "{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}" ypos 955 xpos 50 action Return()