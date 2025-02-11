default name = "■■■"

init python:
    # 获取列表中显示过的图片，如果都没显示过则显示第一张
    def get_seen_image_list(image_list):
        result = []
        for image in image_list:
            if renpy.seen_image(image):
                result.append(image)
        if len(result) == 0:
            result.append(image_list[0])
        print(result)
        return result

screen character_stats(image_list, image_transform):
    default image_index = 0
    default unlock_image_list = get_seen_image_list(image_list)

    image unlock_image_list[image_index]:
        at image_transform
        matrixcolor TintMatrix("#000000")
        alpha 0.5
    
    imagebutton:
        at image_transform
        idle unlock_image_list[image_index]
        focus_mask True
        action SetLocalVariable("image_index", (image_index + 1) % len(unlock_image_list))

transform fenstats_transform():
    xzoom -1
    ypos 1 xalign 0.5 zoom 0.7

transform npcstats_transform():
    xzoom 1
    yalign 0.5 xalign 0.5 zoom 0.7

screen fenstats:
    image "gui/overlay/game_menu.png"
    
    use character_stats([
        "fen normal",
        "fen angry",
        "fen blush",
        "fen blush2",
        "fen blush3",
        "fen cry",
        "fen eat",
        "fen eat2",
        "fen grin",
        "fen hot",
        "fen lick",
        "fen normal",
        "fen sad",
        "fen sadsmile",
        "fen shock",
        "fen smell",
        "fen smile",
        "fen smile2",
        "fen smile3",
        "fen stern",
        "fen stern2",
        "fen stern3",
        "fen stresse",
        "fen sweat",
        "fen wink",
        "fen 2 normal",
        "fen 2 blush",
        "fen 2 smile",
        "fen 2 stern",
        "fen 2 stern2",
        "fen 3 normal",
        "fen 3 blush",
        "fen 3 stern",
        "fen 3 stresse2",
        "fen uw normal",
        "fen uw blush",
        "fen uw blush4",
        "fen naked blush",
        "fen naked hot2",
        "fen naked lick",
        "fen naked relax",
        "fen naked relax2",
        "fen naked shock",
        "fen hard blush",
        "fen hard hot1",
        "fen hard hot2",
        "fen hard hot3",
        "fen cum",
    ], fenstats_transform)
        
    image "gui/stats_lines.png"

    text "{size=80}{font=GlowSans-Bold.otf}[name]{/font}{/size}" ypos 900 xalign 0.5

    #text "{size=80}{font=GlowSans-Bold.otf}Your Name{/font}{/size}" ypos 900 xalign 0.5

    text _("{size=40}{font=GlowSans-Bold.otf}Money{/font}  [fen_coins]{/size}") ypos 910 xpos 300

    text _("{size=40}{font=GlowSans-Bold.otf}Days Passed{/font}  [day_count]{/size}") ypos 960 xpos 300

    text _("{size=40}{font=GlowSans-Bold.otf}CHA{/font} [FenCHA]{/size}") ypos 145 xpos 440

    text _("{size=40}{font=GlowSans-Bold.otf}INT{/font} [FenINT]{/size}") ypos 40 xpos 1200

    text _("{size=40}{font=GlowSans-Bold.otf}STR{/font} [FenSTR]{/size}") ypos 245 xpos 1330

    text _("{size=40}{font=GlowSans-Bold.otf}SXP{/font} [FenSXP]{/size}") ypos 492 xpos 510

    text _("{size=40}{font=GlowSans-Bold.otf}CON{/font} [FenCON]{/size}") ypos 615 xpos 1480

    text _("{size=40}{font=GlowSans-Bold.otf}DEX{/font} [FenDEX]{/size}") ypos 740 xpos 445
    
    textbutton _("{size=40}{font=GlowSans-Bold.otf}Return{/font}{/size}") ypos 955 xpos 50 action Return()
