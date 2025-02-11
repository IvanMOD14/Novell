# The script of the game goes in this file.

#init python:

    #renpy.music.register_channel(name='beeps', mixer='voice')

    #def gunther_callback(event, interact=True, **kwargs):
        #if event == "show":
            #renpy.sound.play("audio/gunther_voice.ogg", channel="beeps", loop=True)
        #elif event == "slow_done":
            #renpy.sound.queue("audio/silence.ogg", channel="beeps", loop=False)

#define Gunther = Character("Gunther", image="gunther", color="#a30326", callback=gunther_callback)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Menu related flags

default disable_back = False

#Characters
define Gunther = Character(_("Gunther"), image="gunther", color="#a30326")

define Fen = Character("[name]", image="fen", who_color="#eb6f10")

define Terrance = Character(_("Terrance"), image="terrance", who_color="#f5693b")

define Murry = Character(_("Murry"), image="murry", who_color="#07bd84") 

define Odachi = Character(_("Odachi"), image="odachi", who_color="#14b4dc") 

define Niall = Character(_("Niall"), image="niall", who_color="#5252ff") 

define Marcus = Character(_("Marcus"), image="marcus", who_color="#b641b2") 

define Khaleb = Character(_("Khaleb"), image="khaleb", who_color="#bcbcbc")

define Trei = Character(_("Trei"), image="trei", who_color="#a52f00")

define Arek = Character(_("Arek"), image="arek", who_color="#06756e")

define Mjolnik = Character(_("Mjolnik"), image="mjolnik", who_color="#a8a8a8")

define FGuard = Character(_("Guard"), image="guards", who_color="#005690")

define CGuard = Character(_("Guard"), image="guards", who_color="#005690")

define EGuard = Character(_("Guard"), image="guards", who_color="#005690")

define SGuard = Character(_("Guard"), image="guards", who_color="#005690")

define RedBunny = Character(_("Red Bunny"), image="guards", who_color="#d43602")

define BlueBunny = Character(_("Blue Bunny"), image="guards", who_color="#02a3d4")

define Oran = Character(_("Oran"), image="guards", who_color="#00e5ed")

define Shadow1 = Character("???", image="shadow1", who_color="#ffffff")

define Shadow2 = Character("???", image="shadow2", who_color="#ffffff")

define Patron1 = Character(_("Patron A"), image="patron1", who_color="#ffffff")

define Patron2 = Character(_("Patron B"), image="patron2", who_color="#ffffff")

define Patron3 = Character(_("Patron C"), image="patron3", who_color="#ffffff")

define Patron4 = Character(_("Patron D"), image="patron4", who_color="#ffffff")

#Fen's Stats

default FenCHA = 5

default FenCON = 5

default FenSTR = 5

default FenINT = 5

default FenDEX = 5

default FenSXP = 0

#Fen's Stats Growth Cap

#max 5
default str_from_workout = 0

#max 3
default cha_from_commonpool = 0

#max 3
default cha_from_luxurypool = 0

#max 4
default cha_from_privatepool = 0

#Fen's Stats Growth Call

label cha_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenCHA += 1
    $ renpy.notify ("CHA UP!")
    return

label con_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenCON += 1
    $ renpy.notify ("CON UP!")
    return

label str_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenSTR += 1
    $ renpy.notify ("STR UP!")
    return

label int_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenINT += 1
    $ renpy.notify ("INT UP!")
    return

label dex_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenDEX += 1
    $ renpy.notify ("DEX UP!")
    return

label sxp_up:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ FenSXP += 1
    $ renpy.notify ("SXP UP!")
    return


#Bond Levels
#Gunther
default bond01 = 0
#Terrance
default bond02 = 0
#Odachi
default bond03 = 0
#Niall
default bond04 = 0
#Murry
default bond05 = 0
#Marcus
default bond06 = 0
#Khaleb
default bond07 = 0
#Guards
default bond08 = 0
#Guards Captain
default bond09 = 0
#Mjolnik
default bond10 = 0

default bond11 = 0

default bond12 = 0

default bond13 = 0

default bond14 = 0

default bond15 = 0

default bond16 = 0

default bond17 = 0

default bond18 = 0

default bond19 = 0

default bond20 = 0

default bond21 = 0

default bond22 = 0

default bond23 = 0

default bond24 = 0

default bond25 = 0

default bond26 = 0

default bond27 = 0

default bond28 = 0

default bond29 = 0

default bond30 = 0

default bond31 = 0

default bond32 = 0

default bond33 = 0

default bond34 = 0

default bond35 = 0

default bond36 = 0

default bond37 = 0

default bond38 = 0

default bond39 = 0

default bond40 = 0

default bond41 = 0

default bond42 = 0

default bond43 = 0

default bond44 = 0

default bond45 = 0

default bond46 = 0

default bond47 = 0

default bond48 = 0

default bond49 = 0

default bond50 = 0

label bondlvup0101:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show gunther normal as gunther00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show gunther normal as gunther01 at right1:
        zoom 1
    with easeinleft

    $ bond01 = 1
    $ bondexp01 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    #show text "{size=80}BOND LEVEL 0 → {atl=bounce_text~10}{size=80}1{/size}{/size}":
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0102:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show gunther normal as gunther00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show gunther normal as gunther01 at right1:
        zoom 1
    with easeinleft

    $ bond01 = 2
    $ bondexp01 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 1 → {size=80}2{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0200:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show terrance normal as terrance00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show terrance normal as terrance01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0201:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show terrance normal as terrance00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show terrance normal as terrance01 at right1:
        zoom 1
    with easeinleft


    $ bond02 = 1
    $ bondexp02 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0202:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show terrance naked normal as terrance00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show terrance naked normal as terrance01 at right1:
        zoom 1
    with easeinleft


    $ bond02 = 2
    $ bondexp02 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 1 → {size=80}2{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0203:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show terrance smile as terrance00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show terrance smile as terrance01 at right1:
        zoom 1
    with easeinleft


    $ bond02 = 3
    $ bondexp02 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 2 → {size=80}3{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0300:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show odachilogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show odachi normal as odachi00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show odachi normal as odachi01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0301:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show odachilogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show odachi normal as odachi00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show odachi normal as odachi01 at right1:
        zoom 1
    with easeinleft

    $ bond03 = 1
    $ bondexp03 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0302:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show odachilogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show odachi normal as odachi00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show odachi smile3 as odachi01 at right1:
        zoom 1
    with easeinleft

    $ bond03 = 2
    $ bondexp03 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 1 → {size=80}2{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0400:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show niall normal as naill00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show niall normal as niall01 at right1:
        zoom 1
    with easeinleft

    $ bond04 = 1
    $ bondexp04 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0401:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show niall normal as naill00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show niall normal as niall01 at right1:
        zoom 1
    with easeinleft

    $ bond04 = 1
    $ bondexp04 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0402:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show niall smile as naill00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show niall smile as niall01 at right1:
        zoom 1
    with easeinleft

    $ bond04 = 2
    $ bondexp04 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 1 → {size=80}2{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0500:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show murry normal as murry00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show murry normal as murry01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0501:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show murry normal as murry00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show murry normal as murry01 at right1:
        zoom 1
    with easeinleft

    $ bond05 = 1
    $ bondexp05 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0600:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show marcus normal as marcus00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show marcus normal as marcus01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0601:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show marcus normal as marcus00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show marcus normal as marcus01 at right1:
        zoom 1
    with easeinleft

    $ bond06 = 1
    $ bondexp06 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0602:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show marcus smile as marcus00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show marcus smile as marcus01 at right1:
        zoom 1
    with easeinleft

    $ bond06 = 2
    $ bondexp06 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 1 → {size=80}2{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0700:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show odachilogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show khaleb normal as odachi00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show khaleb normal as odachi01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0701:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show odachilogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show khaleb normal as odachi00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show khaleb normal as odachi01 at right1:
        zoom 1
    with easeinleft

    $ bond07 = 1
    $ bondexp07 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup0800:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show guards fussy normal as guards00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show guards fussy normal as guards01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup1000:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show mjolnik normal as mjolnik00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show mjolnik normal as mjolnik01 at right1:
        zoom 1
    with easeinleft

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND UNLOCK{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return

label bondlvup1001:

    $_dismiss_pause = False

    window hide
    show image "gui/overlay/game_menu.png"
    show ratio2
    show treelogo:
        ypos -100
        xpos 880
        zoom 1
    with dissolve
    play sound "audio/bondlevelup.ogg" volume 3.0
    show mjolnik smile as mjolnik00 at right1:
        matrixcolor TintMatrix("#000000")
        xpos 1480
        alpha 0.75
        zoom 1
    show mjolnik smile as mjolnik01 at right1:
        zoom 1
    with easeinleft

    $ bond10 = 1
    $ bondexp10 = 0

    show sparkle animation 01 as sparkle01:
        zoom 0.4
        xpos 730
        ypos 330

    show sparkle animation 01 as sparkle02:
        zoom 0.3
        xpos 800
        ypos 400
    
    show sparkle animation 01:
        zoom 0.2
        xpos 720
        ypos 520
    
    show text "{size=80}BOND LEVEL 0 → {size=80}1{/size}{/size}":
        ypos 540
        xpos 450
        rotate -13
    with dissolve

    pause(5.0)

    $_dismiss_pause = True
    pause

    return




#Bond EXP
#Gunther
default bondexp01 = 0
#Terrance
default bondexp02 = 0
#Odachi
default bondexp03 = 0
#Niall
default bondexp04 = 0
#Murry
default bondexp05 = 0
#Marcus
default bondexp06 = 0
#Khaleb
default bondexp07 = 0
#Guards
default bondexp08 = 0
#Guards Captain
default bondexp09 = 0
#Mjolnik
default bondexp10 = 0

default bondexp11 = 0

default bondexp12 = 0

default bondexp13 = 0

default bondexp14 = 0

default bondexp15 = 0

default bondexp16 = 0

default bondexp17 = 0

default bondexp18 = 0

default bondexp19 = 0

default bondexp20 = 0

default bondexp21 = 0

default bondexp22 = 0

default bondexp23 = 0

default bondexp24 = 0

default bondexp25 = 0

default bondexp26 = 0

default bondexp27 = 0

default bondexp28 = 0

default bondexp29 = 0

default bondexp30 = 0

default bondexp31 = 0

default bondexp32 = 0

default bondexp33 = 0

default bondexp34 = 0

default bondexp35 = 0

default bondexp36 = 0

default bondexp37 = 0

default bondexp38 = 0

default bondexp39 = 0

default bondexp40 = 0

default bondexp41 = 0

default bondexp42 = 0

default bondexp43 = 0

default bondexp44 = 0

default bondexp45 = 0

default bondexp46 = 0

default bondexp47 = 0

default bondexp48 = 0

default bondexp49 = 0

default bondexp50 = 0

#BondEXPLEVEL

label bondexpup01:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ gunther_bond_ui = True
    $  renpy.notify ("Gunther Bond UP!")
    return

label bondexpdown01:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Gunther Bond DOWN!")
    return

label bondexpup02:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ terrance_bond_ui = True
    $  renpy.notify ("Terrance Bond UP!")
    return

label bondexpdown02:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Terrance Bond DOWN!")
    return

label bondexpup03:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ odachi_bond_ui = True
    $  renpy.notify ("Odachi Bond UP!")
    return

label bondexpdown03:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Odachi Bond DOWN!")
    return

label bondexpup04:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ niall_bond_ui = True
    $  renpy.notify ("Niall Bond UP!")
    return

label bondexpdown04:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Niall Bond DOWN!")
    return

label bondexpup05:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ murry_bond_ui = True
    $  renpy.notify ("Murry Bond UP!")
    return

label bondexpdown05:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Murry Bond DOWN!")
    return

label bondexpup06:
    play sound "audio/bondexpup.ogg" volume 2.0
    $ marcus_bond_ui = True
    $  renpy.notify ("Marcus Bond UP!")
    return

label bondexpdown06:
    play sound "audio/bondexpdown.ogg" volume 2.0 volume 2.0
    $  renpy.notify ("Marcus Bond DOWN!")
    return

label bondexpup07:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("Khaleb Bond UP!")
    return

label bondexpdown07:
    play sound "audio/bondexpdown.ogg" volume 2.0 volume 2.0
    $  renpy.notify ("Khaleb Bond DOWN!")
    return

label bondexpup08:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("Guards Bond UP!")
    return

label bondexpdown08:
    play sound "audio/bondexpdown.ogg" volume 2.0 volume 2.0
    $  renpy.notify ("Guards Bond DOWN!")
    return

label bondexpup09:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup10:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("Mjolnik Bond UP!")
    return

label bondexpdown10:
    play sound "audio/bondexpdown.ogg" volume 2.0
    $  renpy.notify ("Mjolnik Bond DOWN!")
    return

label bondexpup11:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup12:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup13:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup14:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup15:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup16:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup17:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup18:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup19:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup20:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup21:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup22:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup23:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup24:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup25:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup26:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup27:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup28:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup29:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup30:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup31:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup32:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup33:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup34:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup35:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup36:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup37:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup38:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup39:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup40:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup41:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup42:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup43:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup44:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup45:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup46:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup47:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup48:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup49:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return

label bondexpup50:
    play sound "audio/bondexpup.ogg" volume 2.0
    $  renpy.notify ("XXX Bond UP!")
    return


#Cooking

default RecipePoint = 0

#Action Points when working

# transforms

define vq_dissolve = Dissolve(0.2)
define q_dissolve = Dissolve(0.5)
define s_dissolve = Dissolve(1.5)
define vs_dissolve = Dissolve(2.5)
define vvs_dissolve = Dissolve(4)

transform center1:
    xanchor 0.5
    xpos 980
    yalign 0.96
    ypos 1350

transform left1:
    xanchor 0.5
    xpos 480
    yalign 0.96
    ypos 1350

transform right1:
    xanchor 0.5
    xpos 1440
    yalign 0.96
    ypos 1350

transform left2:
    xanchor 0.5
    xpos 720
    yalign 0.96
    ypos 1350

transform right2:
    xanchor 0.5
    xpos 1200
    yalign 0.96
    ypos 1350

transform left3:
    xanchor 0.5
    xpos 240
    yalign 0.96
    ypos 1350

transform right3:
    xanchor 0.5
    xpos 1680
    yalign 0.96
    ypos 1350

transform left1flip:
    xanchor 0.5
    xpos 480
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform right1flip:
    xanchor 0.5
    xpos 1440
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform left2flip:
    xanchor 0.5
    xpos 720
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform right2flip:
    xanchor 0.5
    xpos 1200
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform left3flip:
    xanchor 0.5
    xpos 240
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform right3flip:
    xanchor 0.5
    xpos 1680
    yalign 0.96
    xzoom -1.0
    ypos 1350

transform backgroundshow:
    xanchor 0.5
    xpos 1680
    yalign 0.96
    xzoom -1.0

transform shock:
    parallel:
        yoffset 0.5
        linear 0.1 yoffset 0.52
        linear 0.1 yoffset 0.48
        linear 0.1 yoffset 0.5
    parallel:
        linear 0.1 yzoom 1.1
        linear 0.1 yzoom 1

transform flip:
    xzoom -1.0

transform flipback:
    xzoom 1.0

transform shake:
    linear 0.1 xoffset -2
    linear 0.1 xoffset 3
    linear 0.1 xoffset 2
    linear 0.1 xoffset -3
    linear 0.1 xoffset 0
    repeat

transform backandforth:
    linear 1 xoffset -50
    pause 1.2
    xzoom -1.0
    pause 0.5
    linear 2 xoffset 100
    pause 1.2
    xzoom 1.0
    pause 0.5
    linear 2 xoffset -100
    pause 1.2
    xzoom -1.0
    pause 0.5
    linear 2 xoffset 100
    pause 1.2
    xzoom 1.0
    pause 0.5
    repeat

transform backandforth2:
    linear 1 xoffset -25
    pause 0.5
    linear 2 xoffset 50
    pause 0.5
    linear 2 xoffset -50
    pause 0.5
    linear 2 xoffset 25
    pause 0.5
    repeat

#Alpha Mask images
image fen black = AlphaMask("bg black.png", "fen normal.png")


#animations

image main_menu animation:
    "images/main_menu 01.png"
    pause 0.1
    "images/main_menu 02.png"
    pause 0.1
    "images/main_menu 03.png"
    pause 0.1
    repeat

image sparkle animation 01:
    "images/sparkle 01.png"
    pause 0.1
    "images/sparkle 02.png"
    pause 0.1
    "images/sparkle 03.png"
    pause 0.1
    "images/sparkle 04.png"
    pause 0.1
    "images/sparkle 05.png"
    pause 0.1
    "images/sparkle 06.png"
    pause 0.1
    repeat


image bg road1_rain_blur = im.Blur("bg road1_rain.png", 5.5)

image bg fenroom_blur = im.Blur("bg fenroom.png", 5.5)

image bg fenroom_night_blur = im.Blur("bg fenroom_night.png", 5.5)

image bg fenroom_night2_blur = im.Blur("bg fenroom_night2.png", 5.5)

image bg fireplace1_blur = im.Blur("bg fireplace1.png", 5.5)

image bg fireplace2_blur = im.Blur("bg fireplace2.png", 5.5)

image bg flowerfield_blur = im.Blur("bg flowerfield.png", 5.5)

image bg guntherroom_blur = im.Blur("bg guntherroom.png", 5.5)

image bg kitchen_blur = im.Blur("bg kitchen.png", 5.5)

image bg kitchen_night1_blur = im.Blur("bg kitchen_night1.png", 5.5)

image bg kitchen_night2_blur = im.Blur("bg kitchen_night2.png", 5.5)

image bg kitchen_nofire_blur = im.Blur("bg kitchen_nofire.png", 5.5)

image bg kitchen2_blur = im.Blur("bg kitchen2.png", 5.5)

image bg road1_blur = im.Blur("bg road1.png", 5.5)

image bg road1_rain_blur = im.Blur("bg road1_rain.png", 5.5)

image bg tavern1_blur = im.Blur("bg tavern1.png", 5.5)

image bg tavern2_blur = im.Blur("bg tavern2.png", 5.5)

image bg tavern3_blur = im.Blur("bg tavern3.png", 5.5)

image bg tavern4_blur = im.Blur("bg tavern4.png", 5.5)

image bg tavernback_blur = im.Blur("bg tavernback.png", 5.5)

image bg tavernback_night_blur = im.Blur("bg tavernback_night.png", 5.5)

image bg tavernfront_blur = im.Blur("bg tavernfront.png", 5.5)

image bg tavernfront_night_blur = im.Blur("bg tavernfront_night.png", 5.5)

image gunther close worry2_blur = im.Blur("images/Gunther/gunther stresse2.png", 2)

image ragnar normal_blur = im.Blur("images/Ragnar/ragnar normal.png", 2)

image bg townstreet_blur = im.Blur("bg townstreet.png", 5.5)

image bg townstreet_night_blur = im.Blur("bg townstreet_night.png", 5.5)

image bg market_blur = im.Blur("bg market.png", 5.5)

image bg stall_blur = im.Blur("bg stall.png", 5.5)

image bg bathhouse1_blur = im.Blur("bg bathhouse1.png", 5.5)

image bg bathhouse2_blur = im.Blur("bg bathhouse2.png", 5.5)

image bg bathhouse3_blur = im.Blur("bg bathhouse3.png", 5.5)

image bg bathhousehall_blur = im.Blur("bg bathhousehall.png", 5.5)

image bg alley1_night_blur = im.Blur("bg alley1_night.png", 5.5)

image bg alley2_night_blur = im.Blur("bg alley2_night.png", 5.5)

image bg alley2_night_blur = im.Blur("bg alley2_night.png", 5.5)

image bg alley2_blur = im.Blur("bg alley2.png", 5.5)

image bg marcus workshop_blur = im.Blur("bg marcus workshop.png", 5.5)

image bg village_blur = im.Blur("bg village.png", 5.5)

image bg mjolnik_home_blur = im.Blur("bg mjolnik_home.png", 5.5)

image bg mjolnik_kitchen_blur = im.Blur("bg mjolnik_kitchen.png", 5.5)

image bg terrance_house_blur = im.Blur("bg terrance_house.png", 5.5)

image bg terrance_house_sunset_blur = im.Blur("bg terrance_house_sunset.png", 5.5)

image bg terrance_house_night_blur = im.Blur("bg terrance_house_night.png", 5.5)

image bg terrance_home_blur = im.Blur("bg terrance_home.png", 5.5)

image bg terrance_home_night_blur = im.Blur("bg terrance_home_night.png", 5.5)

image bg terrance_home_night2_blur = im.Blur("bg terrance_home_night2.png", 5.5)

image bg room3_blur = im.Blur("bg room3.jpg", 5.5)

image bg forest1_blur = im.Blur("bg forest1.png", 5.5)

image bg forest2_blur = im.Blur("bg forest2.png", 5.5)

image bg forest3_blur = im.Blur("bg forest3.png", 5.5)

image bg sky_blur = im.Blur("bg sky.png", 5.5)

image bg mjolnik_room_blur = im.Blur("bg mjolnik_room.png", 5.5)

image bg barn_blur = im.Blur("bg barn.png", 5.5)
# The game starts here.

label start:
    #"Your adventure begins."
    ## Setup a scenario that leads to combat
    #"Suddenly, you encounter a wild Goblin!"
    #$ combat_background = "bg townstreet_night_blur"
    #$ current_player_characters = [hero]
    #$ current_enemies = [goblinA, goblinB, goblinC]
    #call combat_start("regular")
    #with dissolve
   
    #call end_combat

    #"After combat, the story continues..."

    #"A new party member Mage have joined you!"

    #"Here goes combat No.2"

    ## Call the combat system with the current setup
    #$ combat_background = "bg flowerfield_blur"
    #$ current_player_characters = [hero, mage]
    #$ current_enemies = [goblinA, slimeA, goblinB]
    #call combat_start("regular")
    #with dissolve

    #call end_combat

    stop music fadeout 3.0
    scene bg black
    with s_dissolve

    scene bg black
    with s_dissolve
    play music "audio/Thunder Storm 2.ogg" volume 1.0 fadein 3.0
    "Every part of your body throbs with pain."

    scene bg road1_rain
    show ratio1
    with vs_dissolve

#Play thunderstorm noises and flash white like lightning

"The sound of thunder rolls across the grey skies."

"You can feel something wet drip down your nose."

"As it runs across your bruised lips, you pick out the metallic taste of your blood mixed with rain."

"Something loud crashes above you, showering splitters of wood all over you."

"The rain grows heavier, each drop beating against your matted fur."

"The warmth begins to drain from your limbs, washed away by a creeping chill."

show bg road1_rain_blur
with s_dissolve
"Numbness is setting in. The cold wind soaks away your aches."

"You prepare yourself to welcome the embrace of unconsciousness, yet your lungs demand one last complaint."

"{color=#eb6f10}???{/color}" "-Groan-"

#a30326
"{color=#a30326}Deep voice{/color}" "W-Who's there?!"

"Something shuffles nearby. Your swollen eyes make it difficult to see."

"{color=#a30326}Deep voice{/color}" "A kid?!"

"A hand shakes you gently."

show gunther close worry2_blur behind ratio1 at center1:
    zoom 1.5
    ypos 2000
with s_dissolve
"You see something red above you."

"{color=#a30326}Deep voice{/color}" "Are you okay?"

"{color=#eb6f10}???{/color}" "... "

"{color=#a30326}Deep voice{/color}" "What the hell? There's no other footprints."

"{color=#a30326}Deep voice{/color}" "Did you fall from the tree?"

#small text 
"{color=#a30326}Deep voice{/color}" "{size=25}There's no way... it's dead. He couldn't have climbed up there without breaking... {/size}"

"{color=#eb6f10}???{/color}" "-Cough-"

"{color=#a30326}Deep voice{/color}" "Damn, he's barely breathing... "

show gunther close worry2_blur:
    zoom 1.75
    ypos 2000
with dissolve
"{color=#a30326}Deep voice{/color}" "Hold on, you're going to be okay."

"The remnants of the stranger's warmth envelopes you."

"It feels like he's hugging you as he wraps his cloak around your naked form."

"The world jostles as your limp body rises off the cold hard ground."

"{color=#a30326}Deep voice{/color}" "You barely weigh anything even soaking wet... "

scene bg black
with s_dissolve
"Your eyes swell shut all the way."

stop music fadeout 3.0
"Unconsciousness takes you quietly into the darkness... "

"... and the world around you fades away."

scene bg black
with s_dissolve

scene bg fenroom_blur
with dissolve

scene bg black
with dissolve

"Your eyes open and you immediately shut them as you feel an overwhelming pain in your skull."

scene bg fenroom_blur
with s_dissolve

show bg fenroom
with s_dissolve
"With blurry vision, you rub your eyes and try to focus away from the splitting headache."

show fen stern at center1, flip
show bg fenroom_blur
with dissolve
"You find yourself clothed and in an unfamiliar bed."

"Actually nothing seems familiar at all."

show fen stern at flipback
with dissolve
"As you look around, you spot a large red tiger standing at the doorway of this room."

show fen stresse at shock
"{color=#eb6f10}???{/color}" "!?"
#bounce MC like he's surprised

show fen at left1, flipback
with dissolve

show gunther normal at right1
with dissolve
play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
"Tiger" "Easy there, cub."

"{color=#eb6f10}???{/color}" "W-Where am I?!"

show gunther smile
"Tiger" "Yer at the one and only, Flaming Flagon. The finest tavern in the town of Felda."

play sound "audio/bondexpup.ogg" volume 2.0
$ gunther_bond_ui = True
$  renpy.notify ("Gunther Bond unlock!")
Gunther normal "I am Gunther, the owner."

Gunther "I found you at death's door on the outskirts of town. Do you remember anything?"

show fen stern2
with dissolve
$ name = renpy.input(_("Umm, I..I think my name is... ?"))
$ name = name.strip()
if name == "":
    $ name= (_("Fen"))

Fen stern "[name]. My name is [name], I think."

Fen stern2 "I don't really remember anything else. Except... I was on the ground."

Fen "Everything hurts."

Gunther stern "It looked like you fell out of a tree."

Gunther "Whacha doin' out there? The wilderness is no place for a cub like you."

show fen sad
with dissolve
Fen sad "I'm sorry, I don't know."

Gunther normal "Alright, no need to get upset."

Fen "How did I get here?"

Gunther "I carried you all the way back."

Gunther "You were naked, so I've put you in some of my old clothes."

Fen "T-thank you."

Gunther "You've been sleeping for two days since I brought you back. Can you stand?"

show fen stern
with dissolve
"You push yourself up from the bed and try your legs."

"As soon as you set yourself upon them, your limbs betray you and you stumble forward."

#move Gunther closer to Fen
show gunther stern at center1 behind fen
with dissolve
Gunther "Whoa there, I gotcha."

"The tiger's strong arms guide you back onto the bed."

show fen stern2
show gunther normal at right1
with dissolve
"Everything still hurt, apparently your full strength has yet to return."

Gunther "Do you know where you live? Or if you have any family?"

show fen sad
with dissolve
Fen "I... umm."

"The puzzled look on your face tells Gunther his answer."

show fen cry
with dissolve
"Tears begin to well up on your eyes. The more you try to remember, the more confused and frustrated you become."

Gunther stresse "-Sigh-"

Gunther "I can't just abandon someone with amnesia out on the streets... "

Gunther normal "Listen, I'll let you stay here. But you're gonna have to earn your keep. I run a tavern, not a charity."

"The promise of somewhere to be and Gunther's generosity causes your tears to fade."

show fen sadsmile
with dissolve
Fen "T-Thank you, Gunther."

Gunther "Doesn't look like you can walk yet. Rest here for a bit. Let me know if you remember anything."

Fen "Okay, I will."

Gunther "I'll check on you later."

#gunther turns to leave

Fen "Gunther... "

#gunther turns back to look at MC

Gunther "Hmm?"

show fen smile
with dissolve
Fen "Thanks again... for saving my life."

Gunther blush4 "Oh-er, be careful, you might not feel the same after I put you to work."

hide gunther
with dissolve
"Without another word, Gunther slinks outside and closes the door behind him."

hide fen
hide gunther
show bg fenroom
with dissolve
"Your body still aches, but at least you can feel your arms and legs."

stop music fadeout 3.0
"Trying to remember makes your head hurt pretty bad."

show bg black
with vs_dissolve
"Laying back down with your eyes closed, you drift off to sleep."

#fade to evening scene
show bg fenroom_night
with s_dissolve
play music "audio/Winter Morning.ogg" volume 1.0 fadein 3.0
"Some time later, you look at the window and see it's now dark outside."

"Your head still pounded with dull ache, filled with hazy and disjointed memories."

"No idea of who you were, where you came from, nothing."

"You close your eyes and try to clear your mind."

"The sounds of glasses clinking paired with rambunctious and robust voices cheering kept you from falling back asleep."

"Over your thin blanket is an old worn cloak, it smells faintly of burnt wood and cinnamon, a scent that seems familiar..."

"Holding it close, the article of clothing provided you a sense of comfort in the sea of commotion."

scene bg black
with s_dissolve
stop music fadeout 3.0
"You soon doze off again, imagining as if you were somewhere else."

Gunther "{size=25}... yeah, he's still sleeping.{/size}"

"You hear Gunther close the door and footsteps fade into the loud crowd below."

scene bg black
with s_dissolve
centered "-Next day-"
with s_dissolve

scene bg fenroom
with dissolve
play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
"The morning sun beams through the window and strikes your face."

"You are able to stand today, though your body still aches."

"Overall, you feel a lot better this morning."

show gunther naked normal at center1
show bg fenroom_blur
with dissolve
"As you turn from making the bed, you find a naked Gunther staring at you."

Gunther naked smile2 "Good morning!"

with vpunch
Fen "Ack!"

Gunther naked stern "What's wrong?"

Fen "Y-You're naked!"

Gunther naked normal "Yes, I'm on my way to wash up. What's wrong with that?"

Fen "Sorry, I don't know why I reacted that way."

Gunther "Maybe something related to your memory loss?"

Gunther "Anyways, I'm going to get dressed and make us some breakfast."

#stomach sounds

"As if your stomach has its own ears, it growls at the last word."

Gunther naked smile2 "Ha, I bet you're starvin'. The kitchen is right down the stairs."

Gunther naked normal "I'm glad you're back up on your feet."

Gunther "Get the fire started, I'll be down in just a few minutes."

Fen "Okay."

hide gunther
show bg fenroom
with dissolve
"You watch the burly feline walk away to his room before you head down the stairs."

scene bg kitchen_nofire
with s_dissolve
"Right down the steps, you find a sizable kitchen."

"A great long table sits in the middle. Ingredients and utensils lined the walls."

show bg fireplace1
with dissolve
"The fireplace on the other side of the table offers a view into the main tavern."

"You find a stack of firewood next to the hearth. Throwing a few logs in, you stuff some tinder at the bottom."

"Cupping your hands and leaning in close, you howl softly and feel the heat burst past your muzzle."

Fen "{b}Awoooo~{/b}"

show bg fireplace2
with dissolve
"A small flame streams out of your muzzle and the wood catches fire."

show fen normal at left1, flip
show gunther normal at right1
show bg kitchen_blur
with dissolve
Gunther "Ah, I see you have an affinity."

show fen stresse at shock, flipback
Fen "Ack!"

Gunther "Sorry, didn't mean to scare you."

Fen stern "What's an affinity?"

Gunther stresse2 "Really? I'm surprised you're able to talk and not know about affinities."

Gunther normal "Many of us have an affinity, like you, I have an affinity for fire."

#maybe a mini CG with making the fire

"The feline snaps his fingers and a tiny jet of flame bursts out with a wisp of smoke."

Gunther "How did you know how to make fire like that?"

Fen "I don't know. It just felt natural."

Fen normal "Also, you didn't seem to have any matches or flint to get a fire started with."

Gunther stresse3 "Oh... yeah. I supposed I always started the fire with my affinity as well."

hide fen
hide gunther
show bg kitchen
with dissolve
"The tiny fire had grown into a smoldering roar."

"Gunther starts to cook breakfast, and soon the kitchen is filled with delicious smells."

show fen stern at left1
show gunther normal at right1
show bg kitchen_blur
with dissolve
Gunther "Alright cub, eat up."

Fen "I may not remember much, but I am an adult."

Gunther smile2 "Good, I'd hate to think I would put a child through so much manual labor."

Fen "Manual labor?"

Gunther normal "Yes [name]. If you want to stay here, you'll have to earn your keep."

Gunther "So get some fuel into yer belly."

Gunther "Today we will receive a shipment of ale and wine that will need to be unloaded."

Gunther "After that, you'll help me prepare to open the bar."

Fen normal "Okay, I'll do my best."

Gunther "Great. Let's eat, food's getting cold."

hide fen
hide gunther
show bg kitchen
with dissolve
"You woof down the plate of breakfast. You didn't realize how hungry you had been."

"Gunther chuckles as he quickly finishes his own meal."

show fen lick at left1
show bg kitchen_blur
with dissolve
Fen "That was delicious."

show gunther blush3 at right1
with dissolve
Gunther "You're just saying that because you haven't eaten anything in a couple of days."

Fen normal "Well, it's still tasty to me."

Gunther normal "The patrons don't really come to the Flaming Flagon for my food, but it keeps them satisfied."

Gunther "Here, have the rest of my toast."

"The barkeep tosses another square of crispy bread onto your plate and you eat it in just two bites."

Fen eat "So, what will you have me do today?"

Gunther "You'll be giving me a hand with pretty much what I normally do all by myself."

Fen eat "You run this bar by yourself?"

Gunther "Pretty much since I first opened it some years ago."

Gunther "I had a couple of previous employees, but they ran off for the adventure life despite my warnings."

Fen normal "Is adventuring really that great?"

Gunther stern "It depends. Some people who have made a name for themselves usually acquire some decent treasure to exchange for fortunes."

Gunther normal "But the truth is, a lot of them don't survive their first years."

Fen stern "That many of them die?"

Gunther "Yes and no, some find quickly that they're not cut out for it. Some are killed, but some others suffer fates worse than death."

Fen stresse "Worse than dying?"

Gunther "Yes, some end up horrifically cursed or disfigured."

Gunther smile2 "For all we know, maybe you were a fledgling adventurer who got knocked upside the head."

show fen sad
with dissolve
Fen "Maybe... Who knows?"

"Though that is a very plausible explanation, you don't feel that's what happened to you."

Gunther normal "It's just dangerous, but high risk comes with decent rewards."

show fen stern
with dissolve
Fen "I understand, safety is the issue."

Gunther "Very much so. All I have to worry about is the occasional food and drink critic, or fixing busted up furniture."

Fen smile "Well for a bartender, you still saved my life. Looks like anyone can be a hero."

Gunther blush "I guess so."

Gunther stern "Oh, we should get going. Terrance should be here any moment with our delivery."

Fen "Terrance?"

Gunther normal "Yes, he delivers goods around town. He's a really nice guy, I think you'll like him."

scene bg tavernback
with s_dissolve
stop music fadeout 3.0
"After cleaning your plates off, you follow Gunther out the backdoor."

"The back of the tavern connected with two alleys and a short path to the main road."

"You hear the sound of heavy hoof falls clopping closer."

"A large figure stops towards you from the road, hauling an enormous wagon behind it."

play music "audio/The Tale.ogg" volume 1.0 fadein 3.0
show gunther normal at left1, flip
show bg tavernback_blur
with dissolve
Gunther "Terrance! Just in time."

show terrance sweat normal at right1
with dissolve
Terrance "Hey Gunther. Large order today huh?"

Gunther "Yep, I've been busy renegotiating with all the suppliers."

Terrance "I hear business is doing good."

Gunther "Sure is. You need to stop by and have a drink sometime. I haven't seen you in a while."

Terrance "I've been pretty busy myself. Oh! Who's this?"

"The massive horse stares at you."

Gunther "Let me introduce you to my new employee, [name]."

show gunther at left3
show fen blush2 at left2
with dissolve
"He pushes you out in front of him. You stumble forward and almost crash into Terrance."

"You slow yourself enough to stop a fingerbreadth away from his massive chest."

"Being so close to the horse, you can feel the heat radiating from his sweat soaked fur."

"Terrance's musky scent floods your nose as you take a close whiff."

"He smells of dirt, sweat, hay, and the faintest bit of leather."

Gunther smile2 "Forgive him, this is his first day."

Fen "N-Nice to meet you."

Terrance sweat smile "You too, why's your face all red?"

Fen blush "B-big... I mean, sorry. I'm just a little shy."

Terrance "Aww, cute little fella. Don't feel nervous, I'm only so big from hauling this heavy cart all day."

Gunther normal "Yep, Terrance is a gentle giant, don't let his massive muscles scare you."

show fen blush2
with dissolve
"{i}That's not the massive thing that scares me.{/i}"

"You think as you stare at the prominent bulge from beneath the horse's loincloth."

Gunther "Give me a hand with the barrels. We can't hold Terrance up on his other deliveries."

show fen blush at shock, flip
Fen "Right away."

hide fen
hide terrance
hide gunther
show bg tavernback
with dissolve
"You both begin unloading half a dozen barrels of ale and spirits as well as a few crates of vegetables."

"It took a few minutes to move your items off the horse's cart."

show gunther normal at left1, flip
show bg tavernback_blur
with dissolve
Gunther "Okay, looks like that's everything. Would you like a {b}tip{/b} today?"

show terrance sweat normal at right1
with dissolve
Terrance "As much as I'd like that, I got to get to the other side of town soon. Perhaps next time, maybe [name] could help."

Gunther wink "Sure. Something tells me that he'd like that very much."

Terrance "It was good to meet you, [name]. I'll see you all next time."

hide gunther
hide terrance
with dissolve
stop music fadeout 3.0
"The horse picked up his heavy cart and headed to his next stop."

show gunther normal at right1, flipback
with dissolve
play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
Gunther "Fancy that giant?"

show fen blush at left1
with dissolve
Fen "W-What?"

Gunther smile2 "No need to be coy. I've seen that look before."

Fen "I-I don't know what you mean."

Gunther normal "You have much to learn. Let's start with rolling the barrels into the cellar. Set the boxes on the kitchen table."

Fen stresse "These barrels are heavy."

Gunther "Heavy for a fit lad like yourself?"

Gunther "You have a decent build, with this work I'm sure you're only going to get bigger and stronger."

Fen sweat "Alright."

hide gunther
hide fen
with dissolve
"Gunther helps you tip the barrel onto its side and gently rolls it down the ramp to the storage room."

scene bg kitchen
with s_dissolve

show bg kitchen_blur
show gunther normal at right1
with dissolve
Gunther "Okay, here's where all the unopened barrels of drinks are. Here we fill the large flagons and casks to serve at the bar."

Gunther "Wine is on the left, ale on the right."

show fen normal at left1
with dissolve
Fen "That's easy enough to remember."

Gunther "Good, let's finish moving the rest of the barrels in here."

"After hauling in the barrels, two crates of vegetables sit on the large kitchen table."

Gunther "Alright, like I said, I'm not a great cook. I usually just cut all this up and throw it into a soup."

Gunther "There should be bread in the cupboard. Anyone that wants a meal will get a bowl of soup and a hunk of bread in it."

Fen "That doesn't sound too bad."

Gunther "Alright, there's a well back behind. We can get water from there for cooking and cleaning."

Gunther "I'll draw some water. You can start cutting up everything. There's a knife on the counter."

Fen smile "Got it."

hide fen
hide gunther
show bg kitchen
with dissolve
"You start on preparing the ingredients while Gunther leaves to draw water."

"Even though you cannot recall the details of your past, preparing food feels familiar to your hands."

"Guided by intuition, you start to peel and chop the various vegetables."

"Your muscles appear to remember how to handle a knife without cutting yourself."

show bg kitchen_blur
show fen normal at left1, flip
with dissolve
"Each item has its own unique scent, and your nose is able to pick out each and every one of them before they are even cut."

show gunther normal at right1, flip
with dissolve
"Gunther begins to fill a rather large cauldron with water."

show fen sweat
with dissolve
"Your hands and arms quickly begin to tire as you only finish preparing the first crate of produce."

show gunther at flipback
with dissolve
Gunther "You keep cutting them up this small, you'll never be finished by the time we open."

show fen stern at flipback
with dissolve
Fen "How large do you normally cut them?"

Gunther "Like this."

"The tavern owner takes a potato and cuts it in half, then slides it over to pile."

show fen stresse at shock
Fen "What?! You can't eat that in a single bite."

Gunther "What's wrong with that?"

Fen "How are they going to get a little bit of everything when they have to shove a whole potato in their mouth."

show gunther sweat at shock
Gunther "I cut it in half!"

show fen stern at flip
with dissolve
Fen "I'll get this finished before the tavern is open."

Gunther stresse "Fine, go ahead and finish up the soup. Leave it near the fire, it's supposed to last the rest of the night."

Fen "Yes, I can do this."

Gunther normal "Don't wear yourself out. You still have to serve the patrons tonight."

show fen normal at flipback
with dissolve
Fen "Understood."

#gunther leaves the scene
hide gunther
hide fen
show bg kitchen
with dissolve
"Gunther leaves you to cook while he sets the chairs and cleans the bar top."

"The looming questions about your forgotten past seem so far away as you focus on your work for Gunther."

"As you cut into an odd colored root, a bitter stench wrinkles your nose."

show bg kitchen_blur
show fen stern at center1, flip
with dissolve
Fen "Ew, this is rotten. Better toss it."

"You throw it away and continue cutting the remaining ingredients."

show fen normal
with dissolve
"By now the water is just starting to boil, just in time to dump everything into the pot."

"You give the entire thing a stir, but something still feels like it's missing."

"Sniffing the air, the smell of the soup seems bland. Your nose picks up on something spicy in the cabinet."

"Opening the cupboards, you find some dried herbs and a few peppers. Grabbing a handful of each, you toss them into the bubbling liquid."

show fen lick
with dissolve
"Another stir and you can tell there's more flavor than just a moment ago."

"Using a metal rod, you adjust the coals beneath the soup so that the liquid simmers."

show fen normal
with dissolve
"You hear someone calling you from the front."

Gunther "[name], have you finished up back there? I need a hand filling some flagons."

stop music fadeout 3.0
Fen "Coming!"

scene bg tavern2
with s_dissolve

show gunther normal at center1
show bg tavern2_blur
with dissolve
play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0
Gunther "Good, take this. Use it to tap one of the ale barrels here and fill these flagons."

Fen "Alright."

"Gunther hands you a hollow metal spike with a ring. The tool is pretty straightforward to use."

hide gunther
show bg tavern2
with dissolve
"You notice the other barrels have a cork stuffed into a hole on their lids."

show fen stern at left1, flip
show bg tavern2_blur
with dissolve
"Stabbing the tool into one of the unopened barrels, you hear a hiss of air blow out."

"Bitter smelling ale begins to pour out from the tap and splatter on the ground."

show fen stresse at shock
Fen "Crap."

show fen stern
with dissolve
"You quickly grab one of the flagons and catch the pouring brew."

"By the time you finish filling each flagon, the barrel is nearly empty."

show gunther normal at right1
with dissolve
Gunther "Great, you managed not to make a mess."

show fen normal at flipback
with dissolve
Fen "It looks like I'm a fast learner."

Gunther grin "Or maybe it's because I'm the best teacher ever."

Fen smile "Whatever you say, boss."

Gunther stern "Hmm, I guess I am your boss. But you don't have to call me that."

Fen normal "Okay, what's next?"

Gunther normal "Well the afternoon crowd should be coming any moment now. Patrons will bark their orders at the bar."

Gunther "You'll eventually help take the orders and serve the tables. I can handle anyone sitting at the bar myself."

Fen "Okay, sounds simple enough."

Gunther "A mug of ale, a bowl of food, or a glass of wine all costs a coin. An entire flagon is five coins."

Fen "That's pretty easy to remember."

Gunther "Yep, let's have a quick taste of your soup."

hide fen
hide gunther
show bg tavern2
with dissolve
"The chains that held the cauldron above the fire are mounted to a hinged arm inside the fireplace."

"This allowed one to easily move the pot from the kitchen onto the side of the fireplace facing the main tavern."

show food soup1 at truecenter
show bg tavern2_blur
with dissolve
"You grab a bowl from a nearby table and scoop a large ladle full of hot soup into it."

play sound "audio/drink.ogg" volume 3.0
"Your boss takes bite... "

hide food
show fen normal at left1
show gunther stern at right1
show bg tavern2_blur
with dissolve

show gunther stern at shock
Gunther "You cooked this?!"

Fen stresse "What's wrong with it?"

Gunther stresse2 "This is really good! This could be bad news."

Fen "Bad? Why?"

Gunther stresse4 "If the patrons find it tasty, there's not going to be enough to last the night!"

Fen stern "Do you normally sell all of {b}your{/b} soup?"

Gunther stern "Well... no. But I hate the thought of someone going hungry."

Fen smile "I could always make more."

Gunther normal "You just may have to."

"The tiger devours the rest, even giving the empty bowl a few licks before he returns behind the bar."

Gunther "Alright, it sounds like the crowd is here."

hide gunther
hide fen
show bg tavern2
with dissolve
"Your ears perk up just before the doors swing open and a flood of people enter the tavern."

Patron1 "Oh, what smells so good?"

Patron2 "Gunther, I need my usual flagon!"

Patron3 "Who's that cute guy?"

Patron4 "Does Gunther have a young boyfriend?!"

show gunther normal at center1
show bg tavern2_blur
stop music
with dissolve
with vpunch
Gunther "{sc=1.5}{b}{size=50}Everyone, quiet down!{/size}{/b}{sc}"

#show name surprised
with dissolve
"Gunther's voice blasted over the crowd and everyone quickly fell silent."

play music "audio/The Rangers Tavern.ogg" volume 1.0 fadein 3.0
Gunther smile2 "I've hired some help. Get used to seeing him around here."

Gunther stern "And if I hear anyone picking on him, you'll have to deal with me, got it?!"

hide gunther
show fen blush at center1
with dissolve
Fen "Umm... Hi everyone."

Patron1 "He's so cute!"

Patron3 "Looks like there's a new attraction."

Patron2 "Where's my ale?!"

Gunther "Coming right up!"

Gunther wink "Alright [name], just hang out in the kitchen and see if there's enough to make another pot of soup."

scene bg kitchen_night1
with s_dissolve
"You quickly dart back into the kitchen, thankful to be out of the spotlight."

"The crowd gathers on and you see Gunther at work."

"The big cat easily handles three flagons in each hand while working the spout with his tail."

"Meanwhile, more people slowly fill every table and seat at the bar."

show fen normal at center1, flip
show bg kitchen_night1_blur
with s_dissolve
"As you gather all the ingredients onto the table, you continue to study Gunther."

"You smile as you continue with your prep work."

"Every once in a while, you hear the clang of the pot as Gunther scoops out a bowl of stew."

"One bowl quickly becomes three and four... "

hide fen
show bg kitchen_night1
with dissolve
"By the time you have the next pot filled, Gunther pops into the kitchen with an armful of dirty dishes."

show gunther sweat3 at left1, flip
show bg kitchen_night1_blur
with dissolve
Gunther "I was afraid this would happen. [name], please wash up the bowls and utensils."

Gunther sweat "We'll have to go buy some more tomorrow. How's the next pot coming along?"

show fen normal at right1, flip
with dissolve
Fen "It's almost ready to go on the fire."

Gunther smile "Perfect, you're a natural!"

hide gunther
with dissolve
"Your boss returns to the front."

Fen stern "Something about all this seems... familiar."

hide fen
show bg kitchen_night1
with dissolve
"With the next pot cooking, you start on cleaning up all the dirty dishes."

"The night blazes by, and most of the place is empty after Gunther announces last call."

scene bg tavern2
with s_dissolve
"As you clean out the cauldrons, Gunther stacks all the chairs on the tables and sweeps the floors."

show gunther sweat at left1, flip
show bg tavern2_blur
with dissolve
Gunther "Whew, they really loved the stew."

show fen smile2 at right1, flip
with dissolve
Fen "Yeah, there was hardly anything to clean out of these cauldrons."

Gunther normal "Since we have to go shopping for some more bowls and dishes tomorrow, how about we get you some new clothes too?"

Fen normal "Gunther, you're too generous."

Gunther "Even though there isn't a dress code, consider it your work uniform."

Fen "Thanks." 

Fen "-Yawn-"

Gunther "Ready for bed?"

Fen smile "Yeah, I suppose I am."

Gunther "Get some rest then, you've earned it."

Fen normal "You should too."

Gunther grin "I'll be going to bed soon, I just need to count the earnings and do some budgeting."

Fen "Okay, good night."

Gunther normal "You as well."

#scene bg Fens_room
scene bg fenroom_night
with s_dissolve
stop music fadeout 3.0
"You head up to your room and flop onto your bed."

scene bg black
with s_dissolve
play music "audio/Winter Morning.ogg" volume 1.0 fadein 3.0
"As your eyes grow heavy and you drift off to sleep, you think about Gunther."

"Watching him work tonight, expertly taking every order down and serving multiple groups reminds you of something... "

#flash shadow of Fen's dad
scene bg kitchen2_blur
show ratio1
with s_dissolve
"You remember something about a house."

hide ratio1
show ragnar normal_blur at center1, flip
show ratio1
with s_dissolve
"It was where you worked, in the 'back of the house' while {b}he{/b} worked in the 'front of the house'."

"He was an older canine, you both worked in a small restaurant."

"He wasn't just any old dog."

scene bg black
with s_dissolve
centered "he was..."

centered "he is... "
#flash light

scene bg fenroom
with s_dissolve
stop music fadeout 3.0
"And just like that, you wake up to the morning light beaming through your window."

"There's a knock at your door and Gunther peeks inside."

show gunther normal at right1
show bg fenroom_blur
with dissolve
play music "audio/Irish Sea.ogg" volume 1.0 fadein 3.0
Gunther "Oh good, you're awake. And dressed."

show fen normal at left1
with dissolve
Fen "Oh, yeah. I passed out right as soon as I laid down."

Gunther "It certainly looks like it, you're still wearing the stains of last night."

Fen stresse "Oh, I should go get changed."

Gunther normal "Into what?"

Fen sweat "Oh, that's right. We're going to buy clothes today."

Gunther smile2 "You've got the memory loss bad!"

Gunther normal "But yeah, we'll be sure you'll have clean work clothes once we find you some regular threads."

#move Gunther closer
show gunther stern at right2
with dissolve
Gunther "-Sniff-sniff-"

Gunther normal "Would you like me to give you a bath?"

show fen blush at shock
Fen blush "W-What?"

Gunther "A bath. You know, to clean yourself with water and soap?"

Fen "I know what a bath is, just not used to someone asking to assist."

Gunther "Really? It's a pretty normal thing. Hell, I help bathe Terrance every once in a while."

Gunther stresse4 "Hmm, but I suppose someone his size really could use the help."

Fen "T-Thanks, but I think I can manage."

Gunther normal "You sure? More hands make less work."

"Feeling your cheeks burn more from your boss's offer, you try to tastefully dodge the rising awkwardness."

Fen sweat "You know what, taking a bath could take a while."

Fen "It will be busy if we leave too late."

show gunther at right1
with dissolve
Gunther "If you say so. I'll be waiting downstairs then."

Fen normal "Sure, I'll be down in just a moment."

hide gunther
with s_dissolve
"The tiger left the room, leaving you standing there."
#gunther slides off screen

Fen stern "Phew."

Fen blush2 "His hands on my naked body... "

"You shake your head vigorously."

Fen blush "If I keep this up, I {b}will{/b} need a cold bath."

hide fen
show bg fenroom
with s_dissolve
stop music fadeout 3.0
"You collect yourself and quickly pull out a few tangles from your fur with your claws."

#scene change outside with Gunther
scene bg tavernfront
with s_dissolve
play music "audio/Green Wolf Inn.ogg" volume 1.0 fadein 3.0

show gunther normal at right1
show bg tavernfront_blur
with dissolve
Gunther "Ready to check out Felda?"

show fen normal at left1
with dissolve
Fen "Sure."

Gunther "Alright, it's a pretty decent sized town. There's lots to remember."

hide gunther
hide fen
show bg tavernfront
with dissolve
"From the road in front of the tavern, you can see the tops of many different buildings of the town."

"The bright and warm morning's sun is unhindered by any cloud. It is a beautiful day."

scene bg townstreet
with s_dissolve
"Other people start to appear to open their shops and start their day of commerce."

"You hear something clanking down the street."

"Looking over, you spot someone dressed in a full suit of armour walking next to another guy wearing a big pointy hat."

show fen stern at left1
show bg townstreet_blur
with dissolve
Fen "What's with those outfits?"

show gunther normal at right1
with dissolve
Gunther "Who, those two?"

Fen "Yeah."

Gunther stern "They're probably adventurers heading to the dungeon."

Fen "Oh... "

"You have no idea what he's talking about."

"Maybe you should ask Gunther more about Felda."

default ask_about_market = False

label ask_gunther1:

menu:
    "Would you like to ask more about Felda?"
    
    "Where are we going today?":
        jump about_market

    "What's that stone building over there?":
        jump about_church

    "What's the dungeon?":
        jump about_dungeon

    "What's that place with the colourful sign?":
        jump about_bars

    "Let's go shopping." if ask_about_market == True:
        jump shopping

label about_market:
    show fen normal
    Gunther normal "We're going to the market square."

    Fen normal "Does Terrance work there?"

    Gunther "He's contracted by the merchants to deliver goods and sometimes he's there to pick up deliveries."

    Gunther "A lot of craftsmen have some stalls and shops there. You can make some business deals."

    Gunther smile "But when it comes to produce, I prefer to go to the farmer themselves."

Fen smile "That makes sense. I can't wait to see what they have there."

$ ask_about_market = True

jump ask_gunther1

label about_church:
    show fen stern
    Gunther normal "That building is the church."

Fen "A church?"

Gunther stern "Yes, I'm not really religious myself. So I've never really been."

Gunther "I couldn't really tell you more about their beliefs, but the priests seem friendly."

Gunther normal "They also act as a hospital. In fact, it's technically the first place you ever visited."

Fen stern "Huh?"

Gunther "You looked like you were about to die, they helped bandage and clean your wounds."

Gunther grin "It only took them a couple of hours before they said I could take you back to the tavern."

Fen normal "I must thank them then."

Fen stern "Hmm. I don't take it that they visit the tavern much."

Gunther normal "They do not, they spend most of their time healing and praying."

Gunther smile "Though one of the priests is known to be a bit of a slacker. He does visit more often than the others."

Gunther normal "Perhaps you might catch him at the tavern sometime."

jump ask_gunther1

label about_dungeon:
    show fen stern
    Gunther "It's the main attraction of Felda."

Gunther normal "Adventures from all over come here to venture into it."

Fen stern "What's in there?"

Gunther stern "All sorts of dangers, but also wondrous treasures."

Gunther "The dungeon offers fame, fortune, and more to those brave enough to delve into its depths."

Fen stresse "Ah, but the trick is being able to return."

Gunther normal "Indeed it is. And let me tell you, a lot of people don't make it back out."

jump ask_gunther1

label about_bars:
    show fen stern
    Gunther normal "That place? Just some trashy bar."

Fen stern "Another bar in Felda?"

Gunther "Yep!"

Gunther "Because we attract a lot of travellers and adventures, there's lots of places to eat and drink in Felda."

Gunther smile2 "But rest assured, the Flaming Flagon has the best drinks at the best prices in all the town!"

Fen smile "So what's the bar in that cool looking building?"

Gunther stresse3 "Eh... A rather pretentious place."

Gunther stresse "They call themselves 'Club Zero'."

Gunther grin "Stupid place if you ask me. How is it a club if it's open to everyone?"

Fen smile2 "I mean, Flaming Flagon isn't exactly on fire either."

Gunther shock "Eh...!" 

"Gunther opens his mouth to argue, but his words deteriorate into an unintelligible grumble."

#Show fen sweat

jump ask_gunther1

label shopping:
    Fen normal "Alright, let's go shopping."

Gunther normal "It's past the main square."

scene bg market
with s_dissolve
"The market is busy as vendors open their stalls to start their day."

scene bg stall
with s_dissolve
stop music fadeout 3.0
"Gunther takes you over to the stall hanging a sign showing a spool of thread and a needle."

show bg stall_blur at truecenter:
    zoom 2
show murry normal at center:
    zoom 2
    ypos 2900
show ratio1
with s_dissolve
play music "audio/maou_bgm_ethnic02.ogg" volume 1.0 fadein 3.0
"You spot a pair of pointy ears pop up from behind the counter."

"A short middle aged man shuffles out and looks up at the big cat."

show murry at center with easeintop:
    ypos 1900
"He climbs up onto a nearby crate to get eye level with Gunther."

"You get a sniff of the short man."

"He smells like cottonwood with an undertone of something musky."

show bg stall_blur at center:
    zoom 1
show murry normal at right3:
    zoom 1
show gunther normal at center1, flip behind murry
show fen normal at left3
hide ratio1
with s_dissolve
Gunther "Good morning, Murry."

#flip Gunther to face MC

show gunther at flipback
with dissolve
Gunther "This is Murry, the merchant. For a small fee, he'll promote and sell your goods here at the market."

#flip gunther back to face Murry

Murry "Are you here to sell this fine gentleman?"

show fen shock at shock
Fen "What?!"

show gunther stern at flip
with dissolve
Gunther "No, Murry. I am not."

Fen stresse "They sell people here?"

Gunther normal "No, they don't. Indentured servitude has been outlawed for centuries."

Murry smile "I am only teasing him."

Gunther sweat3 "Sure, 'only'."

Murry normal "Ah-hem, what do I owe the pleasure of not one, but two strapping young men at such an early hour?"

Gunther normal "Just looking for some new clothes for [name] here."

Murry hot "Oh ho ho! Something tantalising for your eyes only? I didn't know you liked that sort of thing, Gunther."

Gunther blush4 "No, Murry. [name] is my newest employee at the Flagon."

Murry stresse "W-What? You've hired help? That's why he's in such horrible rags?"

Gunther stern "I don't like how you describe our work uniforms... "

Murry blush "You poor thing, please let me find you something clean and comfortable."

Gunther sweat3 "Just pick something appropriate please."

Gunther stern "And keep your hands to yourself, Murry!"

#slide Murry off the screen and then back on

hide murry
with dissolve
"The small merchant hops off his box and darts into the back of his stall."

"A moment later, he returns with an armful of clothes."

show bg stall_blur at truecenter:
    zoom 2
show ratio1
hide fen
hide gunther
with s_dissolve
Murry "Here, these just came in. It's all the rage in Felda!"

Gunther "... "

Gunther "These are just normal clothes."

"You pick through the various articles of clothing, there's quite a few options."

"You narrow your choices down to two different shirts, until the softer fabric of one wins you over."

"Finally, you settle on a set of clothes that feel comfortable and look like they should fit."

show murry normal at right3:
    zoom 1
show gunther normal at center1, flip behind murry
show fen normal at left3
show bg stall_blur:
    zoom 1
hide ratio1
with s_dissolve
Fen "I like these, but I wonder if they fit."

Gunther "Can he try it on?"

Murry hot "Of course, and I'll give you a discount if you strip right here."

Gunther stern "... How much of a discount?"

Murry normal "Twenty?"

Gunther normal "Twenty five."

Murry smile "Deal."

Fen stresse "Hold on a minute... "

Fen "Don't I get a say?"

show gunther at flipback
with dissolve
Gunther "Well of course! You're welcome to haggle."

Fen sweat "I meant about undressing... "

Gunther "Oh... well I suppose."

"As things stand, nudity doesn't seem like a shameful thing to do here. But... "

menu:
    "Strip for the discount?"

    "Yes":
        jump accept_strip

    "No":
        jump decline_strip

label accept_strip:
    Fen blush "Fine, I'll do it... "

show fen at shock
Fen "For thirty!"

show gunther normal at shock
show murry shock at shock
Gunther "!"
#shock Murry and Gunther

Murry "My my, the lad can drive a hard bargain..."

$ bondexp05 += 1
call bondexpup05 from _call_bondexpup05
Murry smile "Deal!"

#be cool if Gunther had a thumbs up spritem, I'd use it here

call bondexpup01 from _call_bondexpup01
$ bondexp01 += 1
Gunther smile "Nice! Good job [name]!"

scene bg stall at truecenter:
    zoom 2.0
with s_dissolve
"You step inside Murry's stall, out of view of the entire market square."

#show fen naked
show fen naked blush at top:
    zoom 1.5
show bg stall_blur
with s_dissolve
"As you glance around, you see both Murry and Gunther eyes dart away once you look at them."

#name blush
"You quickly shrug off your dirty clothes and don your new threads."

#show fen dressed in new clothes

scene bg stall_blur
show gunther normal at center1
show fen 2 normal at left3
show murry normal at right3
with s_dissolve
Fen "Oh these fit perfectly."

show gunther at flip
with dissolve
Gunther "It looks great, we'll take them."

jump complete_clothes_purchase

label decline_strip:
    Fen "I think I'll just try these on over here... "

Gunther "If you wish."

Murry normal "Full price it is."

show gunther stern2 at flip
with dissolve
Gunther "-Sigh-"

Fen stern "Err... I'll be right back."

#slide fen off screen

scene bg stall at right:
    zoom 2.0
with s_dissolve
"You look around for a more private place to change."

"Most of the area is pretty open, but you manage to find a narrow space between two stacks of barrels on the other side of Muarry's stall."

"The enclosed corner provides you adequate cover to disrobe."

"A few seconds later, you walk back around the corner in your new outfit."

#show fen new outfit
scene bg stall_blur
show gunther normal at center1
show fen 2 normal at left3
show murry normal at right3
with s_dissolve
Fen "How does it look?"

Murry hot "You look ravishing!"

Murry "It looks good on you."

Fen 2 smile "They're very comfortable, I like it."

show gunther at flip
with dissolve
Gunther "Very well then."

jump complete_clothes_purchase

label complete_clothes_purchase:
    "Gunther pays Murry for your new clothes."

Murry smile "Thank you as always for your business. Come see me again if you need anything else."

Fen 2 normal "Thanks Murry."

Gunther "Actually, I'm also looking to purchase some dining ware, mainly bowls, plates, maybe some utensils."

Murry "Of course, the carpenter guild is having a sale, I can get all of that for you. I just need to write up a quick purchase order."

"The merchant scribbles down a note and hands it to Gunther."

Gunther "And here you go."

"Gunther hands Murry a small bag of coins."

Murry "That should cover everything. I should be able to have Terrance deliver it today."

Gunther grin "You're the best Murry, till next time."

stop music fadeout 2.0
scene bg market
with s_dissolve
"The small merchant gives you both a wink and rushes to set up Gunther's delivery."

$ murry_bond_ui = True
call bondlvup0500 from _call_bondlvup0500

#Tutorial of Bond Level
#"Meeting new characters unlocks new bonds."

#"You can view your unlocked bonds in the 'Bond' menu. Clicking on a character's icon will reveal more details."

scene bg market
with dissolve
"The market is starting to get lively as you complete your shopping."

show gunther normal at right1
show bg market_blur
with dissolve
Gunther "I have a few things to take care of back at the tavern before Terrance arrives."

show fen 2 normal at left1
with dissolve
Fen "Anything I can help with?"

Gunther "I believe I have everything under control, but you should probably go ahead and wash your work clothes so that they have enough time to dry before we open."

Fen 2 smile "Okay!"

#scene bg behind_tavern
scene bg tavernback
with s_dissolve
stop music fadeout 3.0
"You return to The Flaming Flagon."

play music "audio/Vargr.ogg" volume 1.0 fadein 3.0
"Gunther heads inside while you draw some water to wash your dirty clothes."

show bg tavernback_blur
show fen 2 stern2 at center1:
        zoom 1.5
        ypos 2000
show ratio1
with dissolve
"As you scrub the stains from your clothes, you get a strange sense of deja vu."
#zoom in on Fen centred

"Your hands feel like you've done this so many times before... "

#suddenly zoom out and show Gunther

Gunther "Hey, you're going to put a hole in that if you keep scrubbing the same spot."

scene bg tavernback_blur
show fen 2 stern2 at left1
show gunther normal at right1
with s_dissolve
"You suddenly realise you've been rubbing the same spot for the last several minutes."

Fen 2 stern "Oh... um, it was a really stubborn spot."

Gunther "Well it looks like you got it out."

"-clop-clop-clop-"

show gunther stern at flip
with dissolve
Gunther "Crap, he's early. Hurry up and get them dry."

Fen "That's going to take a while... "

show gunther normal at flipback
with dissolve
Gunther "Stand back."

show fen at left3
show gunther at right2
with dissolve
"You step back and Gunther leans over your wet clothes."

"The cat takes a deep breath and blows gently over the soaked fabric."

#maybe a sprite effect for fire magic

"Hot air billows out from his lungs and dries your work clothes in seconds."

Gunther smile "Now get dressed, we've got to start getting ready to open."

show fen 2 smile at shock
Fen "Got it!"

jump work_start



return
