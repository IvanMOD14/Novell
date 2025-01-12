# 이미지 잠금 변수 설정

##늑대 ##################################
default persistent.wolf_unlocked = [False]*20

##호랑이 ################################
default persistent.tiger_unlocked = [False]*20

##곰 ################################
default persistent.bear_unlocked = [False]*20

##용 ################################
default persistent.dragon_unlocked = [False]*20

define config.enter_replay_transition  = Fade (0.6, 0.6, 0.6)
define config.exit_replay_transition = Fade (0.6, 0.6, 0.6)
default gallery_index = 0

######################################################################
# 이미지들 ############################################################
######################################################################

image real_black_alpha :
    Solid("#000000ff")
    alpha 0.7

image backcol_alpha :
    "images/bg/backcol.png"
    alpha 0.9 

image main_menu:
    "gui/main_menu.jpg"
    anchor (0.5, 0.5)
    pos (0.502, 0.501)
    zoom 0.772

image cg_frame :
    "images/gallery/cg_frame.png"
    zoom 0.492

image wolf_sel :
    "images/gallery/wolf_sel.png"
    zoom 0.492

image wolf_unsel :
    "images/gallery/wolf_unsel.png"
    zoom 0.492

image tiger_sel :
    "images/gallery/tiger_sel.png"
    zoom 0.492

image tiger_unsel :
    "images/gallery/tiger_unsel.png"
    zoom 0.492

image bear_sel :
    "images/gallery/bear_sel.png"
    zoom 0.492

image bear_unsel :
    "images/gallery/bear_unsel.png"
    zoom 0.492

image dragon_sel :
    "images/gallery/dragon_sel.png"
    zoom 0.492

image dragon_unsel :
    "images/gallery/dragon_unsel.png"
    zoom 0.492


###########################################################
## 여기 이후 수정 필요한 부분 ################################ 
###########################################################

## 썸내일 이미지 ###############################################

## 늑대 ####################################################

image wolf_cg1_thumb =AlphaMask(
    Transform("bg wolf_s1_01", crop=(550, 0, 356, 1100)),
    mask="cg_frame")

image wolf_cg2_thumb =AlphaMask(
    Transform("wolf_cg2", crop=(720, 0, 356, 1100)),
    mask="cg_frame")

image wolf_cg3_thumb =AlphaMask(
    Transform("wolf_cg3", crop=(800, 0, 356, 1100)),
    mask="cg_frame")

image wolf_cg4_thumb =AlphaMask(
    Transform("wolf_cg4", crop=(960, 190, 356, 1100)),
    mask="cg_frame")

image wolf_cg5_thumb =AlphaMask(
    Transform("wolf_cg5g", crop=(680, 190, 356, 1100)),
    mask="cg_frame")

## 호랑이 ####################################################

image tiger_cg1_thumb :
    "images/thumb/tiger_01.png"
    zoom 0.492

image tiger_cg2_thumb :
    "images/thumb/tiger_02.png"
    zoom 0.492

image tiger_cg3_thumb :
    "images/thumb/tiger_03.png"
    zoom 0.492

image tiger_cg4_thumb :
    "images/thumb/tiger_04.png"
    zoom 0.492

## 곰 ####################################################

image bear_cg1_thumb =AlphaMask(
    Transform("bg bear_s1_01", crop=(690, 0, 356, 1100)),
    mask="cg_frame")

## 용 ####################################################

image dragon_cg1_thumb =AlphaMask(
    Transform("dragon_cg1", crop=(760, 0, 356, 1100)),
    mask="cg_frame")


init python:
    import time

    def time_image_loading(image_name):
        start_time = time.time()
        renpy.load_image(image_name)
        end_time = time.time()
        print(f"Loading time for {image_name}: {end_time - start_time:.4f} seconds")



## 썸네일 레이어드 이미지 #################################

layeredimage gallery_frame:
   
    group images:
    
        attribute w_cg1 :
            "wolf_cg1_thumb"
        attribute w_cg2 :
            "wolf_cg2_thumb"
        attribute w_cg3 :
            "wolf_cg3_thumb"
        attribute w_cg4 :
            "wolf_cg4_thumb"
        attribute w_cg5 :
            "wolf_cg5_thumb"

        attribute t_cg1 :
            "tiger_cg1_thumb"
        attribute t_cg2 :
            "tiger_cg2_thumb"
        attribute t_cg3 :
            "tiger_cg3_thumb"
        attribute t_cg4 :
            "tiger_cg4_thumb"

        attribute b_cg1 :
            "bear_cg1_thumb"

        attribute d_cg1 :
            "dragon_cg1_thumb"

    
    group frames:
    
        attribute unsel :
            "images/gallery/frame_overlay_unsel.png"
            zoom 0.492
        attribute sel :
            "images/gallery/frame_overlay_sel.png"
            zoom 0.492
  
    group texts:

        attribute text_unsel :
            "images/gallery/frame_text_unsel.png"
            zoom 0.492
        attribute text_sel :
            "images/gallery/frame_text_sel.png"
            zoom 0.492
    
    group extra:

        attribute locked :
            "images/gallery/locked.png"
            zoom 0.492

        attribute none :
            "images/gallery/none.png"
            zoom 0.492


#############################################################################
# 갤러리 네비게이션 ##########################################################
#############################################################################


## 메뉴 #######################################################################
screen gallery_base() :
    add "main_menu"
    add "backcol_alpha"

screen gallery_navigation() :
    tag menu
    use gallery_base
    use gallery_return

    key "K_ESCAPE" action [Function(cleanup_memory), Return()]
    key "mouseup_3" action [Function(cleanup_memory), Return()]

    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60

        for animal in ["wolf", "tiger", "bear", "dragon"]:
            imagebutton:
                idle f"{animal}_unsel"
                hover f"{animal}_sel"
                action ShowMenu(f"gallery_{animal[0]}")
                focus_mask True

screen gallery_return() :

    vbox:
        style_prefix "gallery"      
        pos (0.91, 0.92)
        vbox:
            align (0.5, 0.5)
            if renpy.variant("mobile"):
                textbutton "돌아가기":
                    style "return_button"
                    xoffset -110
                    action [Function(cleanup_memory), Return()]

            else :
                textbutton "돌아가기":
                    action [Function(cleanup_memory), Return()]


screen gallery_return_navi() :

    vbox:
        style_prefix "gallery"      
        pos (0.91, 0.92)
        vbox:
            align (0.5, 0.5)
            if renpy.variant("mobile"):
                textbutton "돌아가기":
                    style "return_button"
                    xoffset -110
                    action ShowMenu("gallery_navigation")

            else :
                textbutton "돌아가기":
                    action ShowMenu("gallery_navigation")



## 늑대 네비게이션###################################################################
screen gallery_w() :
    tag menu
    use gallery_base
    use gallery_return_navi
    $ renpy.sound.stop()

    $ wolf_gallery_count = sum(1 for name, value in globals().items() if name.startswith("wolf_cg") and name.endswith("_gallery_images"))

    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60
        
        for i in range(wolf_gallery_count):
            if i < len(persistent.wolf_unlocked) and persistent.wolf_unlocked[i]:
                imagebutton:
                    idle "gallery_frame w_cg{} unsel".format(i+1)
                    hover "gallery_frame w_cg{} sel".format(i+1)
                    action ShowMenu("gallery_w_cg", cg_set=i+1)
                    focus_mask True
            else:
                add "gallery_frame locked"
    

    ## replay 기능##
    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60

        $ replay_actions = [
            Replay("wolf_01"),
            Replay("wolf_cg2_start", scope={"c4w_kiss_trigger1": True, "cheer_Gahel": True, "c4w_kiss_trigger2": True, "wolf_love": 4}),
            Replay("c5w_cg3"),
            Replay("c5w_cg4", scope={"wolf_dom": 1}),
            Replay("c5w_cg5_start")
            ## 리플레이 라벨과 리플레이시 넣어야할 변수들 넣기.
        ]

        for i in range(len(replay_actions)):
            if persistent.wolf_unlocked[i]:
                imagebutton:
                    idle "gallery_frame text_unsel"
                    hover "gallery_frame text_sel"
                    action replay_actions[i]
                    focus_mask True
            else:
                add "gallery_frame none"

    key "K_ESCAPE" action ShowMenu("gallery_navigation")
    key "mouseup_3" action ShowMenu("gallery_navigation")


## 늑대 CG 이미지 ########
define wolf_cg1_gallery_images = [
    "bg wolf_s1_01",
    "bg wolf_s1_03",
    "bg wolf_s1_04",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define wolf_cg2_gallery_images = [
    "wolf_cg2",
    "wolf_cg2 im_02 im_02 im_mc heart",
    "wolf_cg2 sky2 cloud2 house2 im_zoom im_03 leaf2",
    "wolf_cg2 im_mouth",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define wolf_cg3_gallery_images = [
    "wolf_cg3",
    "wolf_cg3 horny",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define wolf_cg4_gallery_images = [
    "wolf_cg4g",
    "wolf_cg4g w_2 w_3 w_4 w_5",
    "wolf_cg4g w_2 w_3 w_4 w_5 w_6",
    "wolf_cg4g w_2 w_3 w_4 w_5 w_6 w_7",
    "wolf_cg4g w_2 w_3 w_4 w_5 w_9 w_10 w_11 w_11_add",
    "wolf_cg4g w_2 w_3 w_4 w_5 w_9 w_10 w_11 w_12",
    "wolf_cg4g w_2 w_3 w_4 w_5 w_9 w_10 w_11 w_12 w_15 w_16 w_17",
    "wolf_cg4g w_4 w_5_add w_9 w_19",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define wolf_cg5_gallery_images = [
    "wolf_cg5g",
    "wolf_cg5g body2 arm2 cara_belly2 mouth2 eyehalf2 red2 breath2 sweat2 bite belly_line",
    "wolf_cg5g body2 arm2 cara_belly2 mouth2 eyehalf2 red2 breath2 sweat2 bite belly_line penisdw cara_belly2_tran",
    "wolf_cg5g body2 arm2 cara_belly2 mouth2 eyehalf2 red2 breath2 sweat2 bite belly_line2 seed seedleft3 seedleft4",
    "wolf_cg5g body2 arm2 cara_belly2 mouth2 eyehalf2 red2 breath2 sweat2 bite belly_line2 cara_seed seedleft3 seedleft4 seedleft5 seed3",
    "wolf_cg5g mouth eyehalf red breath sweat bite cara_seed seedleft3_1 seedleft4_1 seedleft5_1 seedleft seedleft2 penisup",
    "wolf_cg5g mouth eyehalf red breath sweat bite cara_seed seedleft3_1 seedleft4_1 seedleft5_1 seedleft seedleft2 penisup seed5 cara_seed2 cara_seed3 screenseed screenseed2 ",
    "wolf_cg5g mouth eyehalf red breath sweat bite cara_seed seedleft3_1 seedleft4_1 seedleft5_1 seedleft seedleft2 penisup cara_seed2 cara_seed3 ",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]



## 늑대 CG 이미지 나오는 스크린 ###############################

screen gallery_w_cg(cg_set):
    tag menu
    
    $ cg_gallery_images = globals()[f"wolf_cg{cg_set}_gallery_images"]
    
    key "K_ESCAPE" action [SetVariable("gallery_index", 0), ShowMenu("gallery_w")]
    key "mouseup_3" action [SetVariable("gallery_index", 0), ShowMenu("gallery_w")]
    
    if gallery_index < len(cg_gallery_images) - 1:
        imagebutton idle cg_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", gallery_index + 1), With(dissolve)]
    else:
        imagebutton idle cg_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", 0), ShowMenu("gallery_w")]


## 호랑이 네비게이션###################################################################
screen gallery_t() :
    tag menu
    use gallery_base
    use gallery_return_navi
    $ renpy.sound.stop()

    $ tiger_gallery_count = sum(1 for name, value in globals().items() if name.startswith("tiger_cg") and name.endswith("_gallery_images"))

    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60
        
        for i in range(tiger_gallery_count):
            if i < len(persistent.tiger_unlocked) and persistent.tiger_unlocked[i]:
                imagebutton:
                    idle "gallery_frame t_cg{} unsel".format(i+1)
                    hover "gallery_frame t_cg{} sel".format(i+1)
                    action ShowMenu("gallery_t_cg", cg_set=i+1)
                    focus_mask True
            else:
                add "gallery_frame locked"

    

    ## replay 기능##
    hbox:
        anchor (0.5, 0) xpos(0.5)
        spacing -60
        
        $ replay_actions = [
            Replay("tiger_see_01", scope={"oil": 1}),
            Replay("c4t_see"),
            Replay("c5t_cg3"),
            Replay("c5t_cg4"),
            ## 리플레이 라벨과 리플레이시 넣어야할 변수들 넣기.
        ]

        for i in range(len(replay_actions)):
            if persistent.tiger_unlocked[i]:
                imagebutton:
                    idle "gallery_frame text_unsel"
                    hover "gallery_frame text_sel"
                    action replay_actions[i]
                    focus_mask True
            else:
                add "gallery_frame none"
        



    key "K_ESCAPE" action ShowMenu("gallery_navigation")
    key "mouseup_3" action ShowMenu("gallery_navigation")


## 호랑이 CG 이미지 ########
define tiger_cg1_gallery_images = [
    "bg tiger_s1_01",
    "bg tiger_s1_04",
    "bg tiger_s1_05",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define tiger_cg2_gallery_images = [
    "tiger_cg2",
    "tiger_cg2 im_02 fm_01",
    "tiger_cg2 im_03 fm_02 spike ln_01",
    "tiger_cg2 im_06 fm_01",
    "tiger_cg2 im_09 fm_04 spike ln_01 ln_02",
    "tiger_cg2 im_10 fm_05 ln_02",
    "tiger_cg2 im_11 fm_04 spike ln_01 ln_02",
    "tiger_cg2 im_12 fm_04 ",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define tiger_cg3_gallery_images = [
    "tiger_s3_01",
    "tiger_s3_02",
    "tiger_s3_03",
    "tiger_s3_06",
    "tiger_s3_16_1",
    "tiger_s3_23",
    "tiger_s3_23_1",
    "tiger_s3_25",
    "tiger_s3_26",    
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

define tiger_cg4_gallery_images = [
    "tiger_cg4g front_01",
    "tiger_cg4g im_02 fr_01",
    "tiger_cg4g im_03 fr_02_1",
    "tiger_cg4g im_04",
    "tiger_cg4g im_05",
    "tiger_cg4g im_06 fr_03",
    "tiger_cg4g im_07 fr_03_1",
    "tiger_cg4g im_08 fr_04",
       
    # 추가 이미지를 여기다 정의할 수 있습니다.
]

## 호랑이 CG 이미지 나오는 스크린 ###############################


screen gallery_t_cg(cg_set):
    tag menu
    
    $ cg_gallery_images = globals()[f"tiger_cg{cg_set}_gallery_images"]
    
    key "K_ESCAPE" action [SetVariable("gallery_index", 0), ShowMenu("gallery_t")]
    key "mouseup_3" action [SetVariable("gallery_index", 0), ShowMenu("gallery_t")]
    
    if gallery_index < len(cg_gallery_images) - 1:
        imagebutton idle cg_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", gallery_index + 1), With(dissolve)]
    else:
        imagebutton idle cg_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", 0), ShowMenu("gallery_t")]


## 곰 네비게이션###################################################################
screen gallery_b() :
    tag menu
    use gallery_base
    use gallery_return_navi
    $ renpy.sound.stop()

    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60
        
        if persistent.bear_unlocked[0] == True :
            imagebutton :
                idle "gallery_frame b_cg1 unsel"
                hover "gallery_frame b_cg1 sel"
                action [ShowMenu("gallery_b_cg1")]
                focus_mask True
        else :
            add "gallery_frame locked"

    

    ## replay 기능##
    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60

        if persistent.bear_unlocked[0] == True :    
            imagebutton :
                idle "gallery_frame text_unsel"
                hover "gallery_frame text_sel"
                action Replay("bear_see_01")
                focus_mask True
        else :
            add "gallery_frame none"
        



    key "K_ESCAPE" action ShowMenu("gallery_navigation")
    key "mouseup_3" action ShowMenu("gallery_navigation")


## CG 이미지 ########
define bear_cg1_gallery_images = [
    "bear_cg1",
    "bear_cg1 dilldo",
    "bear_cg1 water",
    "bear_cg1 milk",
    "bear_cg1 last",
    # 추가 이미지를 여기다 정의할 수 있습니다.
]


## CG 이미지 나오는 스크린 ###############################

screen gallery_b_cg1() :
    tag menu
    key "K_ESCAPE" action [SetVariable("gallery_index", 0), ShowMenu("gallery_b")]
    key "mouseup_3" action [SetVariable("gallery_index", 0), ShowMenu("gallery_b")]

    if gallery_index < len(bear_cg1_gallery_images) - 1:
        imagebutton idle bear_cg1_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", gallery_index + 1), With(dissolve)]

    else:
        imagebutton idle bear_cg1_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", 0), ShowMenu("gallery_b")]


## 용 네비게이션###################################################################
screen gallery_d() :
    tag menu
    use gallery_base
    use gallery_return_navi
    $ renpy.sound.stop()

    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60
        
        if persistent.dragon_unlocked[0] == True :
            imagebutton :
                idle "gallery_frame d_cg1 unsel"
                hover "gallery_frame d_cg1 sel"
                action [ShowMenu("gallery_d_cg1")]
                focus_mask True
        else :
            add "gallery_frame locked"

    

    ## replay 기능##
    hbox :
        anchor (0.5, 0) xpos(0.5)
        spacing -60

        if persistent.dragon_unlocked[0] == True :    
            imagebutton :
                idle "gallery_frame text_unsel"
                hover "gallery_frame text_sel"
                action Replay("dragon_cg1_start")
                focus_mask True
        else :
            add "gallery_frame none"
        



    key "K_ESCAPE" action ShowMenu("gallery_navigation")
    key "mouseup_3" action ShowMenu("gallery_navigation")


## CG 이미지 ########
define dragon_cg1_gallery_images = [
    "dragon_cg1",
    "dragon_cg1 hand",
    "dragon_cg1 hand2 inner",
    "dragon_cg1 base2 milk ball"
    # 추가 이미지를 여기다 정의할 수 있습니다.
]


## CG 이미지 나오는 스크린 ###############################

screen gallery_d_cg1() :
    tag menu
    key "K_ESCAPE" action [SetVariable("gallery_index", 0), ShowMenu("gallery_d")]
    key "mouseup_3" action [SetVariable("gallery_index", 0), ShowMenu("gallery_d")]

    if gallery_index < len(dragon_cg1_gallery_images) - 1:
        imagebutton idle dragon_cg1_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", gallery_index + 1), With(dissolve)]

    else:
        imagebutton idle dragon_cg1_gallery_images[gallery_index]:
            action [SetVariable("gallery_index", 0), ShowMenu("gallery_d")]





# 갤러리 버튼 스타일########################################################################

style gallery_button is default
style gallery_button_text is button_text

style gallery_button:
    properties gui.button_properties("gallery_button")

style gallery_button_text:
    color "#888888"
    hover_color "#ee0a4b"
    selected_color "#ee0a4b7e"
    size 30