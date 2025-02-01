image bg dragon_s1_back :
    "images/bg/dragon/01/d_back.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_01 :
    "images/bg/dragon/01/d_1.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_02 :
    "images/bg/dragon/01/d_2.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_03 :
    "images/bg/dragon/01/d_3.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_04 :
    "images/bg/dragon/01/d_4.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_05 :
    "images/bg/dragon/01/d_5.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_05_1 :
    "images/bg/dragon/01/d_5_1.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_06 :
    "images/bg/dragon/01/d_6.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0


image dragon_s1_06_1 :
    "images/bg/dragon/01/d_6_1.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_07 :
    "images/bg/dragon/01/d_7.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_08 :
    "images/bg/dragon/01/d_8.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_09 :
    "images/bg/dragon/01/d_9.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_10 :
    "images/bg/dragon/01/d_10.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_finger :
    "images/bg/dragon/01/d_finger.png"
    zoom 0.5
    xalign 1.0
    yalign 0.5

image dragon_s1_finger2 :
    "images/bg/dragon/01/d_finger2.png"
    zoom 0.5
    xalign 1.0
    yalign 0.5

image dragon_s1_slit :
    "images/bg/dragon/01/d_slit.png"
    zoom 0.61
    xalign 0.5
    yalign 1.0

image dragon_s1_arm :
    "images/bg/dragon/01/d_arm.png"
    zoom 0.5
    xalign 1.0
    yalign 0.5

image dragon_s1_arm2 :
    "images/bg/dragon/01/d_arm2.png"
    zoom 0.5
    xalign 1.0
    yalign 0.5

image dragon_s1_ball :
    "images/bg/dragon/01/d_ball.png"
    zoom 0.61
    alpha 0.95
    xalign 0.5
    yalign 1.0

image dragon_s1_ball2 :
    "images/bg/dragon/01/d_ball2.png"
    zoom 0.61
    alpha 0.95
    xalign 0.5
    yalign 1.0


layeredimage dragon_cg1:
   
    group background:
    
        attribute background default:
            "bg dragon_s1_back"
    
    group base:
    
        attribute base default:
            "dragon_s1_01"
        attribute base2 :
            "dragon_s1_08"
    
    group add:
    
        attribute hand :
            "dragon_s1_03"
        attribute hand2 :
            "dragon_s1_05"
        attribute milk :
            "dragon_s1_09"
        attribute milk2 :
            "dragon_s1_10"
    
    group add2:
    
        attribute inner :
            "dragon_s1_06_1"
        attribute ball :
            "dragon_s1_ball2"

