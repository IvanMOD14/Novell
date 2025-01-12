##오버레이(overlay) 이미지

image flash_blue :
    "images/overlay/bluelight.png"
    zoom 0.6

image flash_red :
    "images/overlay/redlight.png"
    zoom 0.6

image flash_orange :
    "images/overlay/orangelight.png"
    zoom 0.6

image fire_magic :
    "images/overlay/orangelight2.png"
    zoom 0.6

image chapter_back :
    "images/overlay/chapter_back.png"
    zoom 0.6

image sword_slash:
    "images/overlay/sword_slash.png"
    zoom 0.5

image sword_slash2:
    "images/overlay/sword_slash2.png"
    zoom 0.5

image sword_slash3:
    "images/overlay/sword_slash3.png"
    zoom 0.5

image arrow:
    "images/overlay/arrow.png"
    zoom 0.5

image arrow2:
    "images/overlay/arrow2.png"
    zoom 0.4

image chap:
    "images/overlay/chap.png"
    zoom 0.5

image ter:
    "images/overlay/ter.png"
    zoom 0.5

image one:
    "images/overlay/one.png"
    zoom 0.5

image two:
    "images/overlay/two.png"
    zoom 0.5

image three:
    "images/overlay/three.png"
    zoom 0.5

image four:
    "images/overlay/four.png"
    zoom 0.5

image five:
    "images/overlay/five.png"
    zoom 0.5

image magic_circle:
    "images/overlay/magic.png"
    zoom 0.5

image click:
    "gui/logo/click.png"
    xcenter 0.5
    ycenter 0.35

image cloud1:
    "images/overlay/cloud1.png"
    zoom 0.5

image cloud2:
    "images/overlay/cloud2.png"
    zoom 0.5

image cloud3:
    "images/overlay/cloud3.png"
    zoom 0.5

image light_emit1:
    "images/overlay/light_emit1.png"
    zoom 0.7
    yoffset 100
   
image light_emit2:
    "images/overlay/light_emit2.png"
    zoom 0.7
    yoffset 100

image light_emit3:
    "images/overlay/light_emit3.png"
    zoom 0.7
    yoffset 100

image light_emit4:
    "images/overlay/light_emit4.png"
    zoom 0.7
    yoffset 100

image light_emit5:
    "images/overlay/light_emit5.png"
    zoom 0.7
    yoffset 100

image light_emit6:
    "images/overlay/light_emit6.png"
    zoom 0.7

image charm1:
    "images/overlay/charm1.png"
    zoom 0.7

image charm1:
    "images/overlay/charm1.png"
    zoom 0.5

image charm2:
    "images/overlay/charm2.png"
    zoom 0.5

image charm3:
    "images/overlay/charm3.png"
    zoom 0.5

image sigh:
    "images/overlay/sigh.png"
    zoom 0.5

image question:
    "images/overlay/question.png"
    zoom 0.5

image exclamation:
    "images/overlay/exclamation.png"
    zoom 0.5

image exclamation2:
    "images/overlay/exclamation.png"
    zoom 0.5

image ddam:
    "images/overlay/ddam.png"
    zoom 0.4

image black_back:
    "images/overlay/black.png"
    zoom 0.8

image fire_dust1:
    parallel :
        Transform("images/overlay/fire_dust1.png", zoom=0.15)
        ease 8 rotate (random_rotate_angle)
        ease 8 rotate 0
        repeat

    parallel :
        ease 2 xoffset 50
        ease 2 xoffset -50
        repeat

    parallel :
        ease 4 alpha 0.1
        ease 4 alpha 0.8
        repeat


image fire_dust2:
    parallel :
        Transform("images/overlay/fire_dust2.png", zoom=0.2)
        ease 8 rotate (random_rotate_angle)
        ease 8 rotate 0
        repeat

    parallel :
        ease 2 xoffset 50
        ease 2 xoffset -50
        repeat

    parallel :
        ease 4 alpha 0.2
        ease 4 alpha 0.9
        repeat

init python:
    import random
    # 랜덤 회전 각도 생성, 예를 들어 0도에서 360도 사이
    random_rotate_angle = random.randint(0, 360)

image ember1 = Fixed(SnowBlossom("fire_dust1", 30, xspeed=(-20, -50), yspeed=(-70, -120), start=10))

image ember2 = Fixed(SnowBlossom("fire_dust2", 15, xspeed=(20, 50), yspeed=(-40, -900), start=6))


image cloud_gold1:
    "images/overlay/cloud_gold1.png"
    zoom 0.5

    parallel:
        ease 0.7 yoffset 5
        ease 0.7 yoffset -5
        repeat

image cloud_gold2:
    "images/overlay/cloud_gold2.png"
    zoom 0.5

    parallel:
        ease 0.7 yoffset 5
        ease 0.7 yoffset -5
        repeat

image cloud_gold3:
    "images/overlay/cloud_gold3.png"
    zoom 0.5

    parallel:
        ease 0.75 yoffset 5
        ease 0.75 yoffset -5
        repeat

image cloud_gold4:
    "images/overlay/cloud_gold4.png"
    zoom 0.5

    parallel:
        ease 0.75 yoffset 5
        ease 0.75 yoffset -5
        repeat   


image dizzy:
    "images/overlay/dizzy.webp"


image freezing:
    "images/overlay/freezing.webp"
    align (0.5, 0.5)
    zoom 0.5
    alpha 0
    ease 2 alpha 0.45
    ease 1 alpha 0

image freezing_alpha:
    "images/overlay/freezing_alpha.png"
    align (0.5, 0.5)
    zoom 0.5

init:
    $ ice_effect = ImageDissolve("freezing_alpha", 2.0, 8)

image spark_eye:
    "images/overlay/spark_eye.png"
    align (0.5, 0.5)
    zoom 0.12
    alpha 0
    xpos 0.23
    ypos 0.13
    ease 0.25 alpha 0.9
    ease 0.15 alpha 0


image spark_eye_alpha:
    "images/overlay/spark_eye_alpha.png"
    align (0.5, 0.5)
    zoom 0.5

init:
    $ spark_eye_effect = ImageDissolve("spark_eye_alpha", 0.4, 8)

image hit:
    "images/overlay/hit.webp"
    align (0.5, 0.5)
    zoom 0.5

image hit2:
    "images/overlay/hit2.webp"
    align (0.5, 0.5)
    zoom 0.5

image dissolve_pattern:
    "images/overlay/dissolve_pattern.png"
    align (0.5, 0.5)
    zoom 0.5

init:
    $ dissolve_effect = ImageDissolve("dissolve_pattern", 0.8, 8)