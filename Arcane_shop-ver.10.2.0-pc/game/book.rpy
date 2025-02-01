init offset = -1


###### 언락들 ##########

####케릭터####
# $ unlock_character("cara")

####이미지####
# 하나
# $ unlock_character_image("wolf", "wolf b_no inn_d")

# 여러개
# $ unlock_multiple_images("wolf", [
#     "wolf b_no inn_d",
#     "wolf b_no nake0_d",
#     "wolf b_no nake_d"
# ])

####정보####
# 첫 번째 책의 3번 태그 언락
#    $ unlock_info_tag(0, "3")
    
# 두 번째 책의 여러 태그 한번에 언락
#    $ unlock_multiple_info_tags(1, ["4", "5", "6"])


###################################################################
### 책 UI 이미지들 #############################################
###################################################################
image book :
    "gui/book/book.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image book_page :
    "gui/book/book_page.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image book_page2 :
    "gui/book/book_page2.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image book_tip :
    "gui/book/book_tip.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image new :
    "gui/book/new.png"
    zoom 0.6

image name_frame :
    "gui/book/name_frame.png"
    zoom 0.64

image name_frame2 :
    "gui/book/name_frame2.png"
    zoom 0.64

image name_frame_locked :
    "gui/book/name_frame_locked.png"
    zoom 0.64

image newname_frame :
    "gui/book/newname_frame.png"
    zoom 0.64

image newname_frame2 :
    "gui/book/newname_frame2.png"
    zoom 0.64
    
image info_frame :
    "gui/book/info_frame.png"
    zoom 0.56

image info_frame_hover :
    "gui/book/info_frame_hover.png"
    zoom 0.56

image newinfo_frame :
    "gui/book/newinfo_frame.png"
    zoom 0.56

image newinfo_frame_hover :
    "gui/book/newinfo_frame_hover.png"
    zoom 0.56

image close :
    "gui/book/close.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image close_area :
    "gui/book/close_area.png"
    xcenter 0.465
    ycenter 0.45
    zoom 0.64
    alpha 0

image returnb :
    "gui/book/return.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image returnb_down :
    "gui/book/return.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    ease 0.3 yoffset 100

init python:
    def check_new_character():
        for char_dict in [persistent.characters_tag, persistent.characters_tag2]:
            for char_tag, details in char_dict.items():
                if details["unlocked"]:  # 해당 캐릭터가 해금된 경우에만 확인
                    if (details["viewed"] == False or 
                        (char_tag in persistent.characters_details and 
                        persistent.characters_details[char_tag]["all_viewed"] == False) or
                        (char_tag in persistent.characters_details_2p and 
                        persistent.characters_details_2p[char_tag]["viewed"] == False) or
                        (char_tag in persistent.characters and 
                        is_any_image_unviewed(persistent.characters[char_tag]) == True)):
                        return True
        return False


image character :
    ConditionSwitch(
        "check_new_character()", "gui/book/character_new.png",
        "True", "gui/book/character.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image character_area :
    ConditionSwitch(
        "check_new_character()", "gui/book/character_area_new.png",
        "True", "gui/book/character_area.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    alpha 1

image character_hover :
    ConditionSwitch(
        "check_new_character()", "gui/book/character_new.png",
        "True", "gui/book/character.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    ease 0.3 xoffset 18

image character_selected :
    ConditionSwitch(
        "check_new_character()", "gui/book/character_new.png",
        "True", "gui/book/character.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    xoffset 18

init python:
    def check_new_info():
        for page in persistent.info_tags:
            for item in page.values():
                if item["unlocked"] and not item["viewed"]:
                    return True
        return False

image info :
    ConditionSwitch(
        "check_new_info()", "gui/book/info_new.png",
        "True", "gui/book/info.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image info_area :
    ConditionSwitch(
        "check_new_info()", "gui/book/info_area_new.png",
        "True", "gui/book/info_area.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    alpha 1

image info_hover :
    ConditionSwitch(
        "check_new_info()", "gui/book/info_new.png",
        "True", "gui/book/info.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    ease 0.3 xoffset 18

image info_selected :
    ConditionSwitch(
        "check_new_info()", "gui/book/info_new.png",
        "True", "gui/book/info.png"
    )
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    xoffset 18

image achievements :
    "gui/book/achievements.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64

image achievements_area :
    "gui/book/achievements_area.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    alpha 1

image achievements_hover :
    "gui/book/achievements.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    ease 0.3 xoffset 17

image achievements_selected :
    "gui/book/achievements.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.64
    xoffset 17

image right_small :
    "gui/book/right_small.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.39

image right_small_hover :
    "gui/book/right_small_hover.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.39

image left_small :
    "gui/book/left_small.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.39

image left_small_hover :
    "gui/book/left_small_hover.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.39

image right :
    "gui/book/right.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.47

image right_hover :
    "gui/book/right_hover.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.47

image left :
    "gui/book/left.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.47

image left_hover :
    "gui/book/left_hover.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.47

image fate_stone_blue:
    "gui/book/fate_stone_wolf.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image fate_stone_green:
    "gui/book/fate_stone_tiger.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image fate_stone_red:
    "gui/book/fate_stone_bear.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image fate_stone_yellow:
    "gui/book/fate_stone_dragon.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image fate_stone_black:
    "gui/book/fate_stone_black.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image fate_stone_wolf:
    yoffset -5
    animation
    "fate_stone_black"  # 첫 번째 이미지
    "fate_stone_blue" with Dissolve(1.2)
    pause 1.2
    pause 0.5
    "fate_stone_black" with Dissolve(1.2)
    pause 1.2
    pause 0.5
    repeat

image fate_stone_tiger:
    yoffset -5
    animation
    "fate_stone_black"  # 첫 번째 이미지
    "fate_stone_green" with Dissolve(1.3)
    pause 1.3
    pause 0.4
    "fate_stone_black" with Dissolve(1.3)
    pause 1.3
    pause 0.4
    repeat

image fate_stone_bear:
    yoffset -5
    animation
    "fate_stone_black"  # 첫 번째 이미지
    "fate_stone_red" with Dissolve(1.4)
    pause 1.4
    pause 0.3
    "fate_stone_black" with Dissolve(1.4)
    pause 1.4
    pause 0.3
    repeat

image fate_stone_dragon:
    yoffset -5
    animation
    "fate_stone_black"  # 첫 번째 이미지
    "fate_stone_yellow" with Dissolve(1.5)
    pause 1.5
    pause 0.2
    "fate_stone_black" with Dissolve(1.5)
    pause 1.5
    pause 0.2
    repeat

init python:
    def heart_change_offset():
        if renpy.game.preferences.language == None :
            return 4      
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional" :
            return 10  
        else:
            return 5   


image heart_change:
    yoffset heart_change_offset()
    animation
    "heart_base"  # 첫 번째 이미지
    "heart_stone2" with Dissolve(1.1)  # 첫 번째 이미지에서 두 번째 이미지로 1.5초 동안 부드럽게 전환
    pause 1.1  # 두 번째 이미지가 표시되는 시간 (0.5초)
    "heart_stone3" with Dissolve(1.2)
    pause 1.2
    "heart_stone4" with Dissolve(1.2)
    pause 1.2
    "heart_base" with Dissolve(1.2)
    pause 1.2
    repeat  # 애니메이션 반복


image heart_base:
    "gui/book/heart_stone.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

init python:
    def heart_stone_offset():
        if renpy.game.preferences.language == None :
            return 1      
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional" :
            return 5  
        else:
            return 2 

image heart_stone:
    yoffset heart_stone_offset()
    "heart_base"

image heart_stone2:
    "gui/book/heart_stone2.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image heart_stone3:
    "gui/book/heart_stone3.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

image heart_stone4:
    "gui/book/heart_stone4.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.045

transform book_slide_up:
    on show:    
        ypos 1500  # 시작 위치 (아래쪽)
        ease 0.5 ypos 545
    # on hide:
    #     ypos 545
    #     ease 0.5 ypos 1500

transform bookmark_slide_up:
    on show:
        ypos 1600  # 책갈피 시작 위치 (아래쪽, 책보다 조금 더 아래)
        ease 0.65 ypos 545  # 책갈피가 최종적으로 도달할 위치

    # on hide:
    #     ypos 545
    #     ease 0.35 ypos 1500

transform bookmark_slide_up_moblie:
    zoom 1.11
    yoffset 25
    on show:
        ypos 1600  # 책갈피 시작 위치 (아래쪽, 책보다 조금 더 아래)
        ease 0.65 ypos 545  # 책갈피가 최종적으로 도달할 위치

transform name_frame_slide_up:
    on show:
        xpos 520 ypos 1500
        ease 0.5 ypos 170
        

    # on hide:
    #     ypos 170
    #     ease 0.5 ypos 1500

transform name_frame_up:
    on show:
        xpos 520 ypos 170


transform bookside_slide_up:
    on show:
        xpos 140 ypos 1500
        ease 0.49 ypos -30


###################################################################
### 게임 설정집 아이콘  #############################################
###################################################################

init python:
    def is_data_changed():
        
        # persistent.info_tags 확인
        for tag_set in persistent.info_tags:
            for tag, data in tag_set.items():
                if data["unlocked"] and not data["viewed"]:
                    return True
        
        # persistent.characters_tag 확인
        for char_tag in [persistent.characters_tag, persistent.characters_tag2, persistent.characters_tag3]:
            for char, data in char_tag.items():
                if data["unlocked"]:  # 해당 캐릭터가 해금된 경우에만 확인
                    # 캐릭터 기본 정보가 확인되지 않은 경우
                    if not data["viewed"]:
                        return True
                    
                    # 캐릭터 상세 정보가 확인되지 않은 경우
                    if (char in persistent.characters_details and 
                        persistent.characters_details[char]["all_viewed"] == False):
                        return True
                    
                    # 캐릭터 추가 정보가 확인되지 않은 경우
                    if (char in persistent.characters_details_2p and 
                        persistent.characters_details_2p[char]["viewed"] == False):
                        return True
                    
                    # 캐릭터 이미지가 확인되지 않은 경우
                    if char in persistent.characters:
                        char_data = persistent.characters[char]
                        for img in char_data["images"]:
                            if (char_data["unlocks"][img] and  # 이미지가 언락되었고
                                not char_data["viewed"][img]):  # 아직 확인하지 않은 경우
                                return True
        
        return False


define gui.bookui_frame_borders = Borders(300, 20, 10, 300)

image icon :
    "gui/book/icon.png"
    zoom 0.25

image icon2 :
    "gui/book/icon2.png"
    zoom 0.25

image icon_new :
    "gui/book/icon_new.png"
    zoom 0.25

image icon2_new :
    "gui/book/icon2_new.png"
    zoom 0.25

transform zoom_icon:
    zoom 1.2

transform zoom_icon2:
    xalign 0.5
    yalign 0.5
    zoom 1.11
    yoffset 25


screen book_icon():
    

    frame : 
        background Frame("gui/book/icon_back.png", gui.bookui_frame_borders, tile=gui.frame_tile)  # 사각형 크기와 색상 설정
        xalign 1.018  # 화면의 오른쪽에 위치
        yalign 0.00  # 화면의 위쪽에 위치
        if renpy.variant("mobile") :
            at zoom_icon

        imagebutton :
            idle ("icon_new" if is_data_changed() else "icon")
            hover ("icon2_new" if is_data_changed() else "icon2")
            action ShowMenu("book_ui")
            focus_mask True


###################################################################
### 책 UI 스크린 #############################################
################################################################### 

screen book_ui():
    zorder 100
    modal True
  
    frame at bookmark_slide_up:
        background None
        xalign 0.5
        yalign 0.5
        if renpy.variant("mobile") :
            at bookmark_slide_up_moblie
        add "close" 
        add "book" 
        add "character_selected" 

        use character_tag
        use character_tag2
        use book_info
        use book_achievements
        add "book_tip"
        frame :
            background None
            xoffset -12 yoffset -13
            use book_close
    

screen book_close():
    key "K_ESCAPE" action [Function(reset_all_indexes), Return()]
    
    imagebutton:
        xpos 1438 ypos 36
        idle "close_area"
        action [Function(reset_all_indexes), Return("book_ui")]
    on "hide" action Function(reset_all_indexes)

screen book_return():

    imagebutton :
        xpos 1331 ypos 36
        idle "close_area"
        action [Function(hide_multiple_screens_with_transition)]

init python:
    def hide_multiple_screens_with_transition():
        renpy.transition(Dissolve(0.3))
        for char_tag, details in persistent.characters_tag.items():
            renpy.hide_screen(details["screen"])
        for char_tag, details in persistent.characters_tag2.items():
            renpy.hide_screen(details["screen"])
        reset_all_indexes()



screen book_character():

    imagebutton :
        xpos 140 ypos -30
        idle "character_area"
        hover "character_hover"
        selected_idle "character_selected"
        selected_hover "character_selected"
        action [Hide("information", transition=Dissolve(0.3)), Function(reset_all_indexes)]
        focus_mask True


screen book_info():

    imagebutton :
        xpos 134 ypos -41
        idle "info_area"
        hover "info_hover"
        selected_idle "info_selected"
        selected_hover "info_selected"
        action [ShowMenu("information"), Function(hide_multiple_screens_with_transition)]
        focus_mask True

screen book_achievements():

    imagebutton :
        xpos 134 ypos -41
        idle "achievements_area"
        hover "achievements_hover"
        selected_idle "achievements_selected"
        selected_hover "achievements_selected"
        action NullAction()
        # action [ShowMenu("information"), Function(hide_multiple_screens_with_transition)]
        focus_mask True

screen book_info2():

    imagebutton :
        xpos 134 ypos -46
        idle "info_area"
        hover "info_hover"
        selected_idle "info_selected"
        selected_hover "info_selected"
        action [ShowMenu("information"), Function(hide_multiple_screens_with_transition)]
        focus_mask True

screen book_achievements2():

    imagebutton :
        xpos 134 ypos -46
        idle "achievements_area"
        hover "achievements_hover"
        selected_idle "achievements_selected"
        selected_hover "achievements_selected"
        action NullAction()
        # action [ShowMenu("information"), Function(hide_multiple_screens_with_transition)]
        focus_mask True

###################################################################
### 케릭터 이름표  #############################################
###################################################################


init python:
    if not persistent.characters_tag:
        persistent.characters_tag = {
            "cara": {"unlocked": True, "screen": "mc_character_info", "char_name": "cara", "name": "[pl_name]", "viewed": False},
            "wolf": {"unlocked": False, "screen": "wolf_character_info", "char_name": "wolf", "name": "가헬", "viewed": False},
            "tiger": {"unlocked": False, "screen": "tiger_character_info", "char_name": "tiger", "name": "엘레드", "viewed": False},
            "bear": {"unlocked": False, "screen": "bear_character_info", "char_name": "bear", "name": "바토", "viewed": False},
            "dragon": {"unlocked": False, "screen": "dragon_character_info", "char_name": "dragon", "name": "류호", "viewed": False}
    }
    if not persistent.characters_tag2:
        persistent.characters_tag2 = {
            "lucas": {"unlocked": False, "screen": "lucas_character_info", "char_name": "lucas", "name": "루카스", "viewed": False},
            "ahjin": {"unlocked": False, "screen": "ahjin_character_info", "char_name": "ahjin", "name": "아진", "viewed": False},
            "??": {"unlocked": False, "screen": "?_character_info", "char_name": "??", "name": "??", "viewed": False},
            "???": {"unlocked": False, "screen": "?_character_info", "char_name": "???", "name": "???", "viewed": False},
            "????": {"unlocked": False, "screen": "?_character_info", "char_name": "????", "name": "????", "viewed": False}
    }
    if not persistent.characters_tag3:
        persistent.characters_tag3 = {
            "?????": {"unlocked": False, "screen": "?_character_info", "char_name": "?????", "name": "??", "viewed": False},
            "?": {"unlocked": False, "screen": "?_character_info", "char_name": "?", "name": "?", "viewed": False},
            "??": {"unlocked": False, "screen": "?_character_info", "char_name": "??", "name": "??", "viewed": False},
            "???": {"unlocked": False, "screen": "?_character_info", "char_name": "???", "name": "???", "viewed": False},
            "????": {"unlocked": False, "screen": "?_character_info", "char_name": "????", "name": "????", "viewed": False}
    }

## 케릭터 언락
## 사용 예시
# $ unlock_character("cara")

init python:
    def unlock_character(char_id):
        """
        모든 characters_tag에서 캐릭터를 찾아 언락합니다.
        """
        tag_dicts = [
            persistent.characters_tag,
            persistent.characters_tag2,
            persistent.characters_tag3
        ]
        
        for tag_dict in tag_dicts:
            if char_id in tag_dict:
                tag_dict[char_id]["unlocked"] = True
                renpy.save_persistent()
                return True

        return False


screen character_tag():
    zorder 110


    frame :
        background Solid ("#43652c00")
        minimum (450, 700)
        maximum (450, 700)
        xoffset 455 yoffset 152

        
        if renpy.game.preferences.language == None :
            style_prefix "krbook"
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
            style_prefix "cnbook"
        else :
            style_prefix "enbook"
        vbox:
                           
            for char_details in persistent.characters_tag.values():
                if char_details["unlocked"]:  # 캐릭터가 해금된 경우
                    frame : 
                        text char_details["name"]  # 캐릭터 이름 표시
                else :
                    frame :
                        text ""



    frame at name_frame_slide_up :
        xalign 0.5 yalign 0.5
        minimum (1000, 50)
        maximum (1000, 50)
        background Solid ("#ffffff00")

        hbox :
            xalign 0.5
            yalign 0.5
            
            if len(persistent.characters_tag3) >= 1 :
                imagebutton:
                    xoffset 535 yoffset -40 
                    idle "right"
                    hover "right_hover"
                    action [Show("character_tag3"), With(Dissolve(0.3))]


    
    frame at name_frame_slide_up:
        background Solid ("#2523ba00")
        minimum (450, 700)
        maximum (450, 700)
        xoffset 455 yoffset 152
        style_prefix "nametag"

        vbox:

            for char_tag, details in persistent.characters_tag.items():
                if details["unlocked"]:  # 해당 캐릭터가 해금된 경우에만 버튼 표시
                    frame : 
                        if (details["viewed"] == False or
                            persistent.characters_details[char_tag]["all_viewed"] == False or
                            persistent.characters_details_2p[char_tag]["viewed"] == False or
                            is_any_image_unviewed(persistent.characters[char_tag]) == True) :
                            imagebutton:
                                align (0.5, 0.5)
                                idle "newname_frame"
                                hover "newname_frame2"
                                action [SetDict(persistent.characters_tag[char_tag], key="viewed", value=True),
                                        SetDict(persistent.characters_details[char_tag], key="all_viewed", value=True),
                                        SetDict(persistent.characters[char_tag]["viewed"], key=persistent.characters[char_tag]["images"][0], value=True),
                                        ShowMenu(details["screen"]),
                                        Hide("character_tag")]
                        else :
                            imagebutton:
                                align (0.5, 0.5)
                                idle "name_frame"
                                hover "name_frame2"
                                action [ShowMenu(details["screen"]), Hide("character_tag")]
                
                
                else:  # 해당 캐릭터가 해금되지 않은 경우
                    frame:
                        imagebutton:
                            align (0.5, 0.5)
                            idle "name_frame_locked"  # 자물쇠 이미지
                            hover "name_frame_locked"  # 자물쇠 이미지
                            action None  # 비활성화된 상태





screen character_tag2():
    zorder 110
    
    frame at name_frame_slide_up:
        background Solid ("#68f00d00")
        minimum (450, 700)
        maximum (450, 700)
        xoffset 1030 yoffset 152
        
        if renpy.game.preferences.language == None :
            style_prefix "krbook"
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
            style_prefix "cnbook"
        else :
            style_prefix "enbook"
        vbox:
            for char_show in persistent.characters_tag2.values():
                if char_show["unlocked"]:  # 캐릭터가 해금된 경우
                    frame: 
                        text char_show["name"]  # 캐릭터 이름 표시
                else:
                    frame:
                        text ""

    frame at name_frame_slide_up:
        background Solid ("#2523ba00")
        minimum (450, 700)
        maximum (450, 700)
        xoffset 1030 yoffset 152
        style_prefix "nametag"

        vbox:
            for char_tag, details in persistent.characters_tag2.items():
                if details["unlocked"]:  # 해당 캐릭터가 해금된 경우에만 버튼 표시
                    frame:
                        if (details["viewed"] == False or
                            persistent.characters_details[char_tag]["all_viewed"] == False or
                            persistent.characters_details_2p[char_tag]["viewed"] == False or
                            is_any_image_unviewed(persistent.characters[char_tag]) == True) :
                            imagebutton:
                                align (0.5, 0.5)
                                idle "newname_frame"
                                hover "newname_frame2"
                                action [
                                    SetDict(persistent.characters_tag2[char_tag], key="viewed", value=True),
                                    SetDict(persistent.characters_details[char_tag], key="all_viewed", value=True),
                                    SetDict(persistent.characters[char_tag]["viewed"], key=persistent.characters[char_tag]["images"][0], value=True),
                                    ShowMenu(details["screen"]),
                                    Hide("character_tag")
                                ]
                        else:
                            imagebutton:
                                align (0.5, 0.5)
                                idle "name_frame"
                                hover "name_frame2"
                                action [ShowMenu(details["screen"]), Hide("character_tag")]
                else:  # 해당 캐릭터가 해금되지 않은 경우
                    frame:
                        imagebutton:
                            align (0.5, 0.5)
                            idle "name_frame_locked"  # 자물쇠 이미지
                            hover "name_frame_locked"  # 자물쇠 이미지
                            action None  # 비활성화된 상태






screen character_tag3():
    zorder 110
    
    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        add "book" yoffset 5
        add "character_selected" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "book_tip" yoffset 5    

        frame :
            xpos 520 ypos 166
            background Solid ("#68f00d00")        
            minimum (450, 700)
            maximum (450, 700)
            xoffset -65 yoffset -10
            
            if renpy.game.preferences.language == None :
                style_prefix "krbook"
            elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                style_prefix "cnbook"
            else :
                style_prefix "enbook"
            vbox:
                for char_show in persistent.characters_tag3.values():
                    if char_show["unlocked"]:  # 캐릭터가 해금된 경우
                        frame: 
                            text char_show["name"]  # 캐릭터 이름 표시
                    else:
                        frame:
                            text ""

        frame :
            xalign 0.5 yalign 0.5
            minimum (1000, 70)
            maximum (1000, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton:
                    xoffset -505 yoffset -40
                    idle "left"
                    hover "left_hover"
                    action [Hide("character_tag3"), With(Dissolve(0.3))]
            

        frame :
            xpos 520 ypos 166
            background Solid ("#2523ba00")
            minimum (450, 700)
            maximum (450, 700)
            xoffset -65 yoffset -10
            style_prefix "nametag"

            vbox:
                for char_tag, details in persistent.characters_tag3.items():
                    if details["unlocked"]:  # 해당 캐릭터가 해금된 경우에만 버튼 표시
                        frame:
                            if (details["viewed"] == False or
                                persistent.characters_details[char_tag]["all_viewed"] == False or
                                persistent.characters_details_2p[char_tag]["viewed"] == False or
                                is_any_image_unviewed(persistent.characters[char_tag]) == True) :
                                imagebutton:
                                    align (0.5, 0.5)
                                    idle "newname_frame"
                                    hover "newname_frame2"
                                    action [
                                        SetDict(persistent.characters_tag3[char_tag], key="viewed", value=True),
                                        SetDict(persistent.characters_details[char_tag], key="all_viewed", value=True),
                                        SetDict(persistent.characters[char_tag]["viewed"], key=persistent.characters[char_tag]["images"][0], value=True),
                                        ShowMenu(details["screen"]),
                                        Hide("character_tag")
                                    ]
                            else:
                                imagebutton:
                                    align (0.5, 0.5)
                                    idle "name_frame"
                                    hover "name_frame2"
                                    action [ShowMenu(details["screen"]), Hide("character_tag")]
                    else:  # 해당 캐릭터가 해금되지 않은 경우
                        frame:
                            imagebutton:
                                align (0.5, 0.5)
                                idle "name_frame_locked"  # 자물쇠 이미지
                                hover "name_frame_locked"  # 자물쇠 이미지
                                action None  # 비활성화된 상태

        frame :
                    background None
                    xoffset -12 yoffset -8
                    use book_close

style nametag_vbox is krbook_vbox

style nametag_frame is krbook_frame

style krbook_frame :
    background Solid ("#ffffff00")
    minimum (400, 87)
    maximum (400, 87)
    ypadding 16

style krbook_vbox :
    xalign 0.5
    spacing 53

style krbook_text :
    align (0.5, 0.5)
    size 45
    color "#583425"
    font "DNFForgedBlade-Medium.ttf"


style enbook_frame is krbook_frame

style enbook_vbox is krbook_vbox

style enbook_text :
    align (0.485, 1)
    size 50
    color "#583425"
    font "blackchancery.regular.ttf"

style cnbook_frame is krbook_frame

style cnbook_vbox is krbook_vbox

style cnbook_text :
    align (0.5, 0.75)
    yoffset -1
    size 44
    color "#583425"
    font "NotoSerifTC-Bold.ttf"



###################################################################
### 케릭터 상세정보  #############################################
###################################################################

transform bookmark2_slide_up:
    xalign 0.5
    yalign 0.5
    on show:
        ypos 610  # 책갈피 시작 위치 (아래쪽, 책보다 조금 더 아래)
        ease 0.3 ypos 545  # 책갈피가 최종적으로 도달할 위치

transform bookmark2_slide_up_mobile:
    xalign 0.5
    yalign 0.5
    zoom 1.11
    yoffset 25
    on show:
        ypos 610  # 책갈피 시작 위치 (아래쪽, 책보다 조금 더 아래)
        ease 0.3 ypos 545  # 책갈피가 최종적으로 도달할 위치


init python:
    if not persistent.characters:
        persistent.characters = {
            "cara": {
                "images": ["cara b_no out_d", "cara b_no hood", "cara b_no", "cara b_no inn_d", "cara b_no nake0_d", "cara b_no nake_d"],
                "unlocks": {
                    "cara b_no out_d": True,
                    "cara b_no hood": False,
                    "cara b_no": True,
                    "cara b_no inn_d": False, 
                    "cara b_no nake0_d": False, 
                    "cara b_no nake_d": False, 
                    
                },
                "viewed": {
                    "cara b_no out_d": False,
                    "cara b_no hood": True,
                    "cara b_no": False,
                    "cara b_no inn_d": True,
                    "cara b_no nake0_d": True,
                    "cara b_no nake_d": True,                    
                },
                "index": 0,
                "locked_image": "c_locked"
                
            },
            "wolf": {
                "images": ["wolf b_no out_d", "wolf b_no sword_d", "wolf b2 black_eye2 out_d aura", "wolf b_no", "wolf b_no inn_d", "wolf b_no bulge_d", "wolf b_no nake0_d", "wolf b_no nake_d"],
                "unlocks": {
                    "wolf b_no out_d": True, 
                    "wolf b_no sword_d" : False,
                    "wolf b2 black_eye2 out_d aura" : False,
                    "wolf b_no": True, 
                    "wolf b_no inn_d": False,
                    "wolf b_no bulge_d": False,
                    "wolf b_no nake0_d": False,
                    "wolf b_no nake_d": False,
                    
                },
                "viewed": {
                    "wolf b_no out_d": False,
                    "wolf b_no sword_d" : True,
                    "wolf b2 black_eye2 out_d aura" : True,
                    "wolf b_no": False,
                    "wolf b_no inn_d": True,
                    "wolf b_no bulge_d": True,
                    "wolf b_no nake0_d": True,
                    "wolf b_no nake_d": True,
                },
                "index": 0,
                "locked_image": "w_locked"
            },
            "tiger": {
                "images": ["tiger b_no out_d", "tiger b_no", "tiger b_no base inn_d", "tiger b_no base bulge_d", "tiger b_no base nake0_d", "tiger b_no base nake_d"],
                "unlocks": {
                    "tiger b_no out_d": True, 
                    "tiger b_no": True, 
                    "tiger b_no base inn_d": False,
                    "tiger b_no base bulge_d": False,
                    "tiger b_no base nake0_d": False,
                    "tiger b_no base nake_d" : False
                },
                "viewed": {
                    "tiger b_no out_d": False, 
                    "tiger b_no": False, 
                    "tiger b_no base inn_d": True,
                    "tiger b_no base bulge_d": True,
                    "tiger b_no base nake0_d": True,
                    "tiger b_no base nake_d" : True
                },
                "index": 0,
                "locked_image": "t_locked"
            },
            "bear": {
                "images": ["bear b_no out_d staff_d", "bear b_no out_d knuckle staff2_d", "bear b_no", "bear b_no inn_d", "bear b_no nake0_d", "bear b_no nake_d"],
                "unlocks": {
                    "bear b_no out_d staff_d": True, 
                    "bear b_no out_d knuckle staff2_d": False, 
                    "bear b_no": True,
                    "bear b_no inn_d": False,
                    "bear b_no nake0_d" : False,
                    "bear b_no nake_d" : False
                },
                "viewed": {
                    "bear b_no out_d staff_d": False, 
                    "bear b_no out_d knuckle staff2_d": True, 
                    "bear b_no": False,
                    "bear b_no inn_d": True,
                    "bear b_no nake0_d" : True,
                    "bear b_no nake_d" : True
                },
                "index": 0,
                "locked_image": "b_locked"
            },
            "dragon": {
                "images": ["dragon b_no base_out out_d", "dragon b_no", "dragon b_no nake0_d", "dragon b_no nake_d"],
                "unlocks": {
                    "dragon b_no base_out out_d": True, 
                    "dragon b_no": True, 
                    "dragon b_no nake0_d": False,
                    "dragon b_no nake_d": False   
                },
                "viewed": {
                    "dragon b_no base_out out_d": False, 
                    "dragon b_no": False, 
                    "dragon b_no nake0_d": True,
                    "dragon b_no nake_d": True   
                },
                "index": 0,
                "locked_image": "d_locked"
            },
            "lucas": {
                "images": ["lucas b_no page_d", "lucas b_no am_d"],
                "unlocks": {
                    "lucas b_no page_d": True, 
                    "lucas b_no am_d": True, 
                },
                "viewed": {
                    "lucas b_no page_d": False,
                    "lucas b_no am_d": False, 
                },
                "index": 0,
                "locked_image": "l_locked"
            },
            "ahjin": {
                "images": ["ahjin b_no am_d"],
                "unlocks": {
                    "ahjin b_no am_d": True, 
                },
                "viewed": {
                    "ahjin b_no am_d": False,
                },
                "index": 0,
                "locked_image": "l_locked"
            },
}

## 이미지 언락
## 사용 예시
#하나
# $ unlock_character_image("wolf", "wolf b_no inn_d")

#여러개
# $ unlock_multiple_images("wolf", [
#     "wolf b_no inn_d",
#     "wolf b_no nake0_d",
#     "wolf b_no nake_d"
# ])

init python:
    store.character_unlocks = {}
    
    def unlock_character_image(char_id, image_id):
        key = f"{char_id}_{image_id}"
        if key in store.character_unlocks:
            return store.character_unlocks[key]
            
        if char_id in persistent.characters:
            if image_id in persistent.characters[char_id]["unlocks"]:
                persistent.characters[char_id]["unlocks"][image_id] = True
                persistent.characters[char_id]["viewed"][image_id] = False
                renpy.save_persistent()
                store.character_unlocks[key] = True
                return True
        store.character_unlocks[key] = False
        return False


init python:
    # 이미지를 가져오는 범용 함수
    def get_character_image(char_name):
        char_data = persistent.characters[char_name]
        image_key = char_data["images"][char_data["index"]]
        return image_key if char_data["unlocks"][image_key] else char_data["locked_image"]

    # 다음 이미지로 전환하는 범용 함수
    def next_image(char_name):
        char_data = persistent.characters[char_name]
        char_data["index"] = (char_data["index"] + 1) % len(char_data["images"])
        update_viewed(char_name)
        renpy.save_persistent()
        renpy.transition(Dissolve(0.3))

    # 이전 이미지로 전환하는 범용 함수
    def previous_image(char_name):
        char_data = persistent.characters[char_name]
        char_data["index"] = (char_data["index"] - 1) % len(char_data["images"])
        update_viewed(char_name)
        renpy.save_persistent()
        renpy.transition(Dissolve(0.3))

    def update_viewed(char_name):
        char_data = persistent.characters[char_name]
        image_key = char_data["images"][char_data["index"]]
        char_data["viewed"][image_key] = True
        renpy.save_persistent()

    def is_any_image_unviewed(char_data):
        return any(not viewed for viewed in char_data["viewed"].values())
    
    #인덱스 초기화
    def reset_all_indexes():
        for char_name in persistent.characters:
            persistent.characters[char_name]['index'] = 0
        global page_number
        page_number = 1
        global current_info
        current_info = ""
        global current_page_index
        current_page_index = 0
        change_characters_details_2p_status()
        update_changed_status()
        change_characters_details_viewstatus()


init python:
    if not persistent.characters_details:
        persistent.characters_details = {
            "cara": {
                    "info": {
                        "이름": "[pl_name]",
                        "나이": _("24"),
                        "종족": _("카라칼, 늑대 혼혈"),
                        "직업": _("상인"),
                        "신장": _("2m 3cm"),
                        "몸무게": _("105kg"),
                        "별자리": _("물병자리"),
                        "생일": _("2월 1일"),
                        "좋아하는것": _("금기서적"),
                        "싫어하는것": _("강한냄새"),
                        "운명": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": False,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "운명": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "운명": True
                    },
                    "all_viewed": False,  
                    "changed": True
                },
                "wolf": {
                    "info": {
                        "이름": _("가헬"),
                        "나이": _("23"),
                        "종족": _("늑대"),
                        "직업": _("용병"),
                        "신장": _("2m 15cm"),
                        "몸무게": _("146kg"),
                        "별자리": _("사수자리"),
                        "생일": _("12월 13일"),
                        "좋아하는것": _("훈련"),
                        "싫어하는것": _("목욕 및 샤워"),
                        "호감도": "",
                        "이해도": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": False,
                        "이해도": False
                    },
                    "all_viewed": False,
                    "changed": True  
                },
                "tiger": {
                    "info": {
                        "이름": _("엘레드 말레우스 판테라"),
                        "나이": _("38"),
                        "종족": _("호랑이"),
                        "직업": _("기사단장"),
                        "신장": _("2m 31cm"),
                        "몸무게": _("183kg"),
                        "별자리": _("처녀자리"),
                        "생일": _("9월 12일"),
                        "좋아하는것": _("잘생긴 외모, 캣닙"),
                        "싫어하는것": _("벌레"),
                        "호감도": "",
                        "이해도": ""

                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": True,
                        "이해도": True
                    },
                    "all_viewed": False,
                    "changed": True  
                },
                "bear": {
                    "info": {
                        "이름": _("바토 바스툼 울사"),
                        "나이": _("21"),
                        "종족": _("곰"),
                        "직업": _("마법사"),
                        "신장": _("1m 92cm"),
                        "몸무게": _("217kg"),
                        "별자리": _("양자리"),
                        "생일": _("4월 4일"),
                        "좋아하는것": _("달콤한 음식"),
                        "싫어하는것": _("더러운것"),
                        "호감도": "",
                        "이해도": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": True,
                        "이해도": True
                    },
                    "all_viewed": False,
                    "changed": True  
                },
                "dragon": {
                    "info": {
                        "이름": _("류호"),
                        "나이": _("380 이상"),
                        "종족": _("용"),
                        "직업": _("주술사"),
                        "신장": _("2m 11cm"),
                        "몸무게": _("196kg"),
                        "별자리": _("천칭자리"),
                        "생일": _("9월 26일"),
                        "좋아하는것": _("술, 음식, 여행"),
                        "싫어하는것": _("말대꾸"),
                        "호감도": "",
                        "이해도": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": True,
                        "이해도": True
                    },
                    "all_viewed": False,
                    "changed": True
                },
                "lucas": {
                    "info": {
                        "이름": _("루카스"),
                        "나이": _("32"),
                        "종족": _("치타"),
                        "직업": _("용병길드 접수원"),
                        "신장": _("2m 5cm"),
                        "몸무게": _("138kg"),
                        "별자리": _("물고기자리"),
                        "생일": _("2월 29일"),
                        "좋아하는것": _("케이크, 크림"),
                        "싫어하는것": _("해산물"),
                        "호감도": "",
                        "이해도": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": True,
                        "이해도": True
                    },
                    "all_viewed": False,
                    "changed": True
                },
                "ahjin": {
                    "info": {
                        "이름": _("아진"),
                        "나이": _("250 이상"),
                        "종족": _("여우"),
                        "직업": _("동방 무역상인"),
                        "신장": _("1m 98cm"),
                        "몸무게": _("94kg"),
                        "별자리": _("쌍둥이자리"),
                        "생일": _("5월 29일"),
                        "좋아하는것": _("새콤한 과일, 해산물"),
                        "싫어하는것": _("???"),
                        "호감도": "",
                        "이해도": ""
                    },
                    "unlocks": {
                        "이름": True,
                        "나이": True,
                        "종족": True,
                        "직업": True,
                        "신장": True,
                        "몸무게": True,
                        "별자리": True,
                        "생일": True,
                        "좋아하는것": True,
                        "싫어하는것": True,
                        "호감도": True,
                        "이해도": True
                    },
                    "viewed": {
                        "이름": False,
                        "나이": False,
                        "종족": False,
                        "직업": False,
                        "신장": False,
                        "몸무게": False,
                        "별자리": False,
                        "생일": False,
                        "좋아하는것": False,
                        "싫어하는것": False,
                        "호감도": True,
                        "이해도": True
                    },
                    "all_viewed": False,
                    "changed": True
                },
}



init python:
    if not persistent.characters_details_2p:
        persistent.characters_details_2p = {

            "cara": {"text": cara_description, "viewed": False, "changed": True},
            "wolf": {"text": wolf_description, "viewed": False, "changed": True},
            "tiger": {"text": tiger_description, "viewed": False, "changed": True},
            "bear": {"text": bear_description, "viewed": False, "changed": True},
            "dragon": {"text": dragon_description, "viewed": False, "changed": True},
            "lucas": {"text": lucas_description, "viewed": False, "changed": True},
            "ahjin": {"text": ahjin_description, "viewed": False, "changed": True},
}
    


default char_name = ""

init python:
    def change_page(direction):
        global page_number
        if 1 <= page_number + direction <= 2:  # 페이지 범위 유지
            page_number += direction
        renpy.transition(Dissolve(0.3))
        change_characters_details_viewstatus()
        update_changed_status()
    
    def change_characters_details_2p_status(): 
        for character, details in persistent.characters_details_2p.items():
            if details["viewed"]: # viewed가 True라면
                details["changed"] = False # changed 항목을 False로 설정
    
    def change_characters_details_viewstatus():
        for char_name, char_data in persistent.characters_details.items():
            if char_data.get("all_viewed", False):  # all_viewed가 True라면
                for key in char_data["viewed"]:  # 모든 viewed 항목을 순회
                    char_data["viewed"][key] = True  # 각 viewed 항목을 True로 설정
      
    def update_changed_status():
        for char_name, char_data in persistent.characters_details.items():
            if char_data.get("all_viewed", False):  # all_viewed가 True라면
                char_data["changed"] = False  # changed 항목을 False로 설정

init python:
    def get_heart_images(value, threshold, max_hearts):
        if value >= threshold:
            return ["heart_change"] * max_hearts
        else:
            return ["heart_stone" if value >= i else None for i in range(1, max_hearts * 3, 3)]

    def get_character_stat(char_name, stat_name):
        if stat_name == "호감도":
            return globals().get(f"{char_name}_love", 0)
        elif stat_name == "이해도":
            return globals().get(f"{char_name}_understanding", 0)
        else:
            return persistent.characters_details[char_name]["info"][stat_name]

default page_number = 1



screen mc_character_info(char_name = "cara"):
    zorder 110
    modal True

    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
            
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
                
                    

            
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)

        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:  
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                

                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "운명":
                                        if persistent.fate_wolf == True :
                                            add "fate_stone_wolf"
                                        if persistent.fate_tiger == True :
                                            add "fate_stone_tiger"
                                        if persistent.fate_bear == True :
                                            add "fate_stone_bear"
                                        if persistent.fate_dragon == True :
                                            add "fate_stone_dragon"                           
                                    
                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new" #느낌표 이미지
                                    else :
                                        text _(value)
                                else:
                                    text _("???")
        
        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()





screen wolf_character_info(char_name = "wolf"):
    zorder 110
    modal True

    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart

                                    elif persistent.characters_details[char_name]["viewed"][key] == False: 
                                        text _(value)
                                        add "new"
                                    else:
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()




                    

screen tiger_character_info(char_name = "tiger"):
    zorder 110
    modal True

    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart

                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new"
                                    else :
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()






screen bear_character_info(char_name = "bear"):
    zorder 110
    modal True
    
    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart

                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new"
                                    else :
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()






screen dragon_character_info(char_name = "dragon"):
    zorder 110
    modal True
    
    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                            
                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new"
                                    else :
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()




screen lucas_character_info(char_name = "lucas"):
    zorder 110
    modal True

    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart

                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new"
                                    else :
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()

screen ahjin_character_info(char_name = "ahjin"):
    zorder 110
    modal True

    frame at bookmark2_slide_up:
        background None
        if renpy.variant("mobile") :
            at bookmark2_slide_up_mobile
        add "returnb"

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2
        
        frame :
            background None
            xoffset -12 yoffset -10
            use book_return
            use book_close
        add "book" yoffset 5
        frame :
            background None
            xoffset -6 yoffset -1
            use book_info
            use book_achievements
        add "character_selected" yoffset 5
        add "book_tip" yoffset 5
        
        vbox :
            add get_character_image(char_name) zoom 0.47 xpos 680 ypos 500

            if is_any_image_unviewed(persistent.characters[char_name]):
                add "new" zoom 1.2 xpos 500 ypos -560

        vbox:
            align (0.232, 0.213)  # 스크린 중앙에 vbox 정렬
            spacing 5
            for i, img in enumerate(persistent.characters[char_name]["images"]):
                frame:
                    minimum (15, 15)
                    maximum (15, 15)
                    if persistent.characters[char_name]["index"] == i:
                        background Solid ("#C8133D")

                    elif persistent.characters[char_name]["unlocks"][img]:
                        background Solid ("#390000")

                        if persistent.characters[char_name]["viewed"][img] == False:
                            background Solid ("#d59006")

                    else:
                        background Solid ("#39000067")
        
        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset -195
                    idle "left"
                    hover "left_hover"
                    action Function(previous_image, char_name)
                
                imagebutton :
                    xoffset 190
                    idle "right"
                    hover "right_hover"
                    action Function(next_image, char_name)
        
        frame :
            xalign 0.705 yalign 0.77
            minimum (420, 50)
            maximum (420, 50)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                imagebutton :
                    xoffset 5
                    yoffset -3
                    idle "left_small"
                    hover "left_small_hover"
                    action [Function(change_page, -1), Function(change_characters_details_2p_status)]
                    sensitive page_number > 1  # 첫 페이지에서는 비활성화

                if page_number ==1 :
                    text "  1 / 2  " style "number_text" yoffset 21
                else :
                    text "  2 / 2  " style "number_text" yoffset 21

                
                imagebutton :
                    xoffset -5
                    yoffset -3
                    idle "right_small"
                    hover "right_small_hover"
                    action [SetDict(persistent.characters_details_2p[char_name], key="viewed", value=True), Function(change_page, 1)]
                    sensitive page_number < 2  # 마지막 페이지에서는 비활성화

        if page_number == 1:   
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
            
                    for key, value in persistent.characters_details[char_name]["info"].items():
                        frame:
                            hbox:
                                text "{key} : ".format(key=key)
                                if persistent.characters_details[char_name]["unlocks"][key]:
                                    if key == "호감도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_love"], 17, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart
                                    elif key == "이해도":
                                        $ hearts = get_heart_images(globals()[f"{char_name}_understanding"], 12, 6)
                                        for heart in hearts:
                                            if heart:
                                                add heart

                                    if persistent.characters_details[char_name]["viewed"][key] == False : 
                                        text _(value)
                                        add "new"
                                    else :
                                        text _(value)
                                else:
                                    text _("???")

        elif page_number == 2:
            frame :
                xalign 0.705 yalign 0.41
                minimum (420, 670)
                maximum (420, 670)
                background Solid ("#ffffff00")
                if renpy.game.preferences.language == None:
                    style_prefix "inbook"
                elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                    style_prefix "cn_inbook"
                elif renpy.game.preferences.language == "english" :
                    style_prefix "en_inbook"
                else :
                    style_prefix "else_inbook"
                
                vbox:
                    hbox :
                        text _("정보") style select_text_style()
                        if persistent.characters_details_2p[char_name]["viewed"] == False or persistent.characters_details_2p[char_name]["changed"] == True :
                            add "new"
                    add "bar"
                    text persistent.characters_details_2p[char_name]["text"] style select_text_style2()


style number_text :
    xalign 0
    yalign 0
    size 33
    color "#583425"
    font "OpenSans-Bold.ttf"

style inbook_frame :
    minimum (407, 51)
    maximum (407, 51)
    background Solid ("#1b629200")

style inbook_hbox :
    align(0 , 0)

style inbook_vbox :
    spacing 0

style inbook_text :
    xalign 0 yalign 0
    size 27
    color "#583425"
    font "DNFForgedBlade-Medium.ttf"


style en_inbook_frame is inbook_frame

style en_inbook_hbox is inbook_hbox

style en_inbook_vbox is inbook_vbox

style en_inbook_text :
    xalign 0 yalign 0
    size 30
    color "#583425"
    font "blackchancery.regular.ttf" 


style else_inbook_frame is inbook_frame

style else_inbook_hbox is inbook_hbox

style else_inbook_vbox is inbook_vbox

style else_inbook_text :
    xalign 0 yalign 0
    size 24
    color "#583425"
    font "NotoSansKR-Medium.otf" 

style cn_inbook_frame is inbook_frame

style cn_inbook_hbox is inbook_hbox

style cn_inbook_vbox is inbook_vbox

style cn_inbook_text :
    xalign 0 yalign 0
    size 27
    color "#583425"
    font "NotoSerifTC-Bold.ttf"
    

      

###################################################################
### 인게임 정보택  #############################################
###################################################################

init python:
    # persistent 데이터가 없을 경우를 위한 초기 데이터
    if not persistent.info_tags:
        persistent.info_tags = [
            {
                "1": {"unlocked": True, "name": title_1, "viewed": False},
                "2": {"unlocked": False, "name": title_2, "viewed": False},
                "3": {"unlocked": False, "name": title_3, "viewed": False},
                "4": {"unlocked": False, "name": title_4, "viewed": False},
                "5": {"unlocked": False, "name": title_5, "viewed": False},
                "6": {"unlocked": False, "name": title_6, "viewed": False},
                "7": {"unlocked": False, "name": title_7, "viewed": False}
            },
            {
                "1": {"unlocked": False, "name": title_8, "viewed": False},
                "2": {"unlocked": False, "name": title_9, "viewed": False},
                "3": {"unlocked": False, "name": title_10, "viewed": False},
                "4": {"unlocked": False, "name": title_11, "viewed": False},
                "5": {"unlocked": False, "name": title_12, "viewed": False},
                "6": {"unlocked": False, "name": title_13, "viewed": False},
                "7": {"unlocked": False, "name": title_14, "viewed": False}
            },
            {
                "1": {"unlocked": False, "name": title_15, "viewed": False},
                "2": {"unlocked": False, "name": title_16, "viewed": False},
                "3": {"unlocked": False, "name": title_17, "viewed": False},
                "4": {"unlocked": False, "name": title_18, "viewed": False},
                "5": {"unlocked": False, "name": title_19, "viewed": False},
                "6": {"unlocked": False, "name": title_20, "viewed": False},
                "7": {"unlocked": False, "name": title_21, "viewed": False}
            },
            {
                "1": {"unlocked": False, "name": title_22, "viewed": False},
                "2": {"unlocked": False, "name": title_23, "viewed": False},
                "3": {"unlocked": False, "name": title_24, "viewed": False},
                "4": {"unlocked": False, "name": title_25, "viewed": False},
                "5": {"unlocked": False, "name": title_26, "viewed": False},
                "6": {"unlocked": False, "name": title_27, "viewed": False},
                "7": {"unlocked": False, "name": title_28, "viewed": False}
            },
            {
                "1": {"unlocked": False, "name": title_29, "viewed": False},
                "2": {"unlocked": False, "name": title_30, "viewed": False},
                "3": {"unlocked": False, "name": title_31, "viewed": False},
                "4": {"unlocked": False, "name": title_32, "viewed": False},
                "5": {"unlocked": False, "name": title_33, "viewed": False},
                "6": {"unlocked": False, "name": title_34, "viewed": False},
                "7": {"unlocked": False, "name": title_35, "viewed": False}
            },
        ]

    if not persistent.info_pages:
        persistent.info_pages = [
            {
                "1": {info_1_key: info_1_content},
                "2": {info_2_key: info_2_content},
                "3": {info_3_key: info_3_content},
                "4": {info_4_key: info_4_content},
                "5": {info_5_key: info_5_content},
                "6": {info_6_key: info_6_content},
                "7": {info_7_key: info_7_content}
            },
            {
                "1": {info_8_key: info_8_content},
                "2": {info_9_key: info_9_content},
                "3": {info_10_key: info_10_content},
                "4": {info_11_key: info_11_content},
                "5": {info_12_key: info_12_content},
                "6": {info_13_key: info_13_content},
                "7": {info_14_key: info_14_content}
            },
            {
                "1": {info_15_key: info_15_content},
                "2": {info_16_key: info_16_content},
                "3": {info_17_key: info_17_content},
                "4": {info_18_key: info_18_content},
                "5": {info_19_key: info_19_content},
                "6": {info_20_key: info_20_content},
                "7": {info_21_key: info_21_content}
            },
            {
                "1": {info_22_key: info_22_content},
                "2": {info_23_key: info_23_content},
                "3": {info_24_key: info_24_content},
                "4": {info_25_key: info_25_content},
                "5": {info_26_key: info_26_content},
                "6": {info_27_key: info_27_content},
                "7": {info_28_key: info_28_content}
            },
            {
                "1": {info_29_key: info_29_content},
                "2": {info_30_key: info_30_content},
                "3": {info_31_key: info_31_content},
                "4": {info_32_key: info_32_content},
                "5": {info_33_key: info_33_content},
                "6": {info_34_key: info_34_content},
                "7": {info_35_key: info_35_content}
            },            
        ]

## 정보 언락
## 사용 예시
# 첫 번째 책의 3번 태그 언락
#    $ unlock_info_tag(0, "3")
    
# 두 번째 책의 여러 태그 한번에 언락
#    $ unlock_multiple_info_tags(1, ["4", "5", "6"])

init python:
    def unlock_info_tag(book_index, tag_number):
        """
        특정 책의 특정 태그를 언락합니다.
        
        Args:
            book_index (int): 책 인덱스 (0부터 시작)
            tag_number (str): 태그 번호 ("1", "2" 등)
        """
        if 0 <= book_index < len(persistent.info_tags):
            if tag_number in persistent.info_tags[book_index]:
                persistent.info_tags[book_index][tag_number]["unlocked"] = True
                renpy.save_persistent()
                return True
        return False

    def unlock_multiple_info_tags(book_index, tag_numbers):
        """
        여러 태그를 한번에 언락합니다.
        
        Args:
            book_index (int): 책 인덱스
            tag_numbers (list): 언락할 태그 번호 리스트
        """
        for tag_number in tag_numbers:
            unlock_info_tag(book_index, str(tag_number))



init python:
    def show_next_page():
        global current_page_index
        if current_page_index < len(persistent.info_pages) - 1:
            current_page_index += 1
        update_info_display()

    def show_previous_page():
        global current_page_index
        if current_page_index > 0:
            current_page_index -= 1
        update_info_display()

    def update_info_display():
        global current_info
        current_info = {}
        
    def reset_info():
        global current_page_index
        current_page_index = 0
        current_info = {}

    def reset_changed_status():
        for page in persistent.info_tags:
            for details in page.values():
                if details["viewed"]:
                    details["changed"] = False

    def has_unlocked_items(page_index):
    # 존재하는 페이지인지 확인
        return page_index < len(persistent.info_tags)

default current_page_index = 0  # 현재 페이지 인덱스 초기화

default current_info = {}



init python:
    def prepare_translated_info(info):
        translated_info = {}
        for key, value in info.items():
            translated_key = _(key)  # 키 번역
            translated_value = _(value)  # 값 번역
            translated_info[translated_key] = translated_value
        return translated_info



screen information():
    zorder 110
    modal True   

    frame :
        background None
        if renpy.variant("mobile") :
            at zoom_icon2

        add "book" yoffset 5
        add "info_selected" yoffset 5
        use book_close
        frame :
            background None
            xoffset -12 yoffset -12
            use book_character
        frame :
            background None
            xoffset -6 yoffset -1
            use book_achievements
        add "book_tip" yoffset 5

    

        frame :
            xalign 0.31 yalign 0.46
            minimum (460, 70)
            maximum (460, 70)
            background Solid ("#ffffff00")

            hbox :
                xalign 0.5
                yalign 0.5

                if current_page_index > 0:
                    imagebutton:
                        xoffset -233
                        idle "left"
                        hover "left_hover"
                        action [Function(show_previous_page), With(Dissolve(0.3))]
            
            hbox :
                xalign 0.5
                yalign 0.5


                # 오른쪽 화살표 표시
                if current_page_index < len(persistent.info_tags) - 1 and has_unlocked_items(current_page_index + 1):
                    imagebutton:
                        xoffset 230
                        idle "right"
                        hover "right_hover"
                        action [Function(show_next_page), With(Dissolve(0.3))]
    

        frame at name_frame_up:
            background Solid ("#68f00d00")
            minimum (450, 700)
            maximum (450, 700)
            xalign 0.5 yalign 0.5
            xoffset -275 yoffset -33
            
            if renpy.game.preferences.language == None:
                style_prefix "krinfo"
            elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional":
                style_prefix "cninfo"
            elif renpy.game.preferences.language == "english" :
                style_prefix "eninfo"
            else:
                style_prefix "elseinfo"
            vbox:
                for tag, details in persistent.info_tags[current_page_index].items():
                    frame:
                        $ display_text = "???" if not details["unlocked"] else details["name"]
                        text display_text

        
        frame at name_frame_up:
            background Solid ("#2523ba00")
            minimum (450, 700)
            maximum (450, 700)
            xalign 0.5 yalign 0.5
            xoffset -275 yoffset -33
            style_prefix "infotag"

            vbox:
                for tag, details in persistent.info_tags[current_page_index].items():
                    frame:
                        if details["unlocked"]:
                            # 기존 코드 (unlocked된 항목에 대한 처리)
                            if details["viewed"] == False:
                                imagebutton:
                                    align (0.5,0.5)
                                    idle "newinfo_frame"
                                    hover "newinfo_frame_hover"
                                    selected_idle "newinfo_frame_hover"
                                    selected_hover "newinfo_frame_hover"
                                    action [SetDict(persistent.info_tags[current_page_index][tag], "viewed", True),
                                        SetVariable("current_info", persistent.info_pages[current_page_index][tag]),
                                        With(Dissolve(0.3))]
                            else:
                                imagebutton:
                                    align (0.5,0.5)
                                    idle "info_frame"
                                    hover "info_frame_hover"
                                    selected_idle "info_frame_hover"
                                    selected_hover "info_frame_hover"
                                    action [SetVariable("current_info", persistent.info_pages[current_page_index][tag]),
                                        With(Dissolve(0.3))]
                        else:
                            # unlocked되지 않은 항목에 대한 처리
                            imagebutton:
                                    align (0.5,0.5)
                                    idle "info_frame"  # 클릭 불가능한 상태로 표시


        frame id "info_content":
            xalign 0.705 yalign 0.41
            minimum (420, 670)
            maximum (420, 670)
            background Solid ("#ffffff00")
            if renpy.game.preferences.language == None:
                style_prefix "infobook"
            elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
                style_prefix "cn_infobook"
            elif renpy.game.preferences.language == "english"  :
                style_prefix "en_infobook"
            else :
                style_prefix "else_infobook"
            
            
            frame:
                vbox:
                    if current_info:
                        for key, value in current_info.items():
                            text _([key]) style select_text_style()
                            add "bar"
                            text _([value]) style select_text_style2()
                            text ""

image bar :
    "gui/book/bar.png"
    zoom 0.3

style infotag_vbox:
    xalign 0.5
    spacing 7

style infotag_frame is krbook_frame

################################

style krinfo_frame :
    background Solid ("#ffffff00")
    minimum (400, 87)
    maximum (400, 87)
    ypadding 16

style krinfo_vbox is infotag_vbox

style krinfo_text :
    align (0.5, 0.5)
    size 37
    color "#583425"    
    font "DNFForgedBlade-Medium.ttf"

style eninfo_frame is krinfo_frame

style eninfo_vbox is krinfo_vbox

style eninfo_text :
    align (0.48, 1)
    size 40
    color "#583425"
    font "blackchancery.regular.ttf"

style elseinfo_frame is krinfo_frame

style elseinfo_vbox is krinfo_vbox

style elseinfo_text :
    align (0.48, 1)
    size 31
    color "#583425"
    font "NotoSansKR-Medium.otf"

style cninfo_frame is krinfo_frame

style cninfo_vbox is krinfo_vbox

style cninfo_text :
    align (0.485, 1)
    yoffset -2
    size 38
    color "#583425"    
    font "NotoSerifTC-Bold.ttf"


###############################

style infobook_frame is inbook_frame

style infobook_hbox is inbook_hbox

style infobook_vbox :
    spacing 8

style infobook_text is inbook_text

style en_infobook_frame is infobook_frame

style en_infobook_hbox is infobook_hbox

style en_infobook_vbox is infobook_vbox

style en_infobook_text is en_inbook_text


style else_infobook_frame is infobook_frame

style else_infobook_hbox is infobook_hbox

style else_infobook_vbox is infobook_vbox

style else_infobook_text is else_inbook_text


style cn_infobook_frame is infobook_frame

style cn_infobook_hbox is infobook_hbox

style cn_infobook_vbox is infobook_vbox

style cn_infobook_text is cn_inbook_text

##############################

init python:
    # 텍스트 스타일을 결정하는 함수
    def select_text_style():
        if renpy.game.preferences.language == None:
            return "add"
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
            return "cnadd"
        elif renpy.game.preferences.language == "english" :
            return "enadd"
        else:
            return "elseadd"
    def select_text_style2():
        if renpy.game.preferences.language == None:
            return "add2"
        elif renpy.game.preferences.language == "chinese_simple" or renpy.game.preferences.language == "chinese_traditional"  :
            return "cnadd2"
        elif renpy.game.preferences.language == "english" :
            return "enadd2"
        else:
            return "elseadd2"

## add 는 정보탭 안의 정보 텍스트
style add is inbook_text :
    align (0, 0.5)
    size 32

## add2 는 캐릭터 인물 페이지 2장 안의 정보 텍스트
style add2 is inbook_text :
    align (0, 0.5)
    size 25

style enadd is en_inbook_text :
    align (0, 0.5)
    size 36

style enadd2 is en_inbook_text :
    align (0, 0.5)
    size 29

style elseadd is else_inbook_text :
    align (0, 0.5)
    size 29

style elseadd2 is else_inbook_text :
    align (0, 0.5)
    size 22

style cnadd is cn_inbook_text :
    align (0, 0.5)
    size 32

style cnadd2 is cn_inbook_text :
    align (0, 0.5)
    size 25




init python:
    naming = {
            "1": {
                    "info": {
                        _("이름 : "): "",
                        _("나이 : "): "",
                        _("종족 : "): "",
                        _("직업 : "): "",
                        _("신장 : "): "",
                        _("몸무게 : "): "",
                        _("별자리 : "): "",
                        _("생일 : "): "",
                        _("좋아하는것 : "): "",
                        _("싫어하는것 : "): "",
                        _("호감도 : "): "",
                        _("이해도 : "): "",
                        _("운명 : "): ""
                    }
            }
    }