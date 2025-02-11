default unlocked_recipe = 0

# 菜谱状态
# unlock: 已解锁
# success: 已成功
# 其他情况：未解锁
default recipe_state_map = {}

init python:
    # 解锁一个菜谱
    def set_recipe_unlock(id):
        global recipe_list, recipe_state_map
        if id not in list(map(lambda i: i['id'], recipe_list)):
            print('菜谱', id, "不是有效id")
            return
        if recipe_state_map.get(id) == None:
            recipe_state_map[id] = 'unlock'
    
    # 试做成功一个菜谱
    def set_recipe_success(id):
        global recipe_list, recipe_state_map
        if id not in list(map(lambda i: i['id'], recipe_list)):
            print('菜谱', id, "不是有效id")
            return
        if recipe_state_map.get(id) == 'unlock':
            recipe_state_map[id] = 'success'
    
    # 获取已解锁菜谱数量
    def get_unlocked_recipe_count():
        count = 0
        for id in recipe_state_map:
            if recipe_state_map[id] == 'unlock' or recipe_state_map[id] == 'success':
                count += 1
        return count

    # 获取已成功菜谱数量
    def get_success_recipe_count():
        count = 0
        for id in recipe_state_map:
            if recipe_state_map[id] == 'success':
                count += 1
        return count

# 菜谱界面：展示未解锁、已解锁、已完成的菜品
screen recipelist:
    image "gui/overlay/game_menu.png"
    image "ratio2.png"

    text "RECIPES":
        color "#262626"
        size 220
        font "GlowSans-Bold.otf"
        at transform:
            rotate -11.8
            ypos -250
    
    $ total_recipe_count = len(recipe_list)
    $ unlock_recipe_count = get_success_recipe_count()
    text "DEVELOPED [unlock_recipe_count] / [total_recipe_count]":
        color "#828282"
        font "GlowSans-Bold.otf"
        size 80
        xpos 1850
        ypos 920
        xanchor 1.0

    frame:
        background None
        side ("c r"):
            area (200,250,1620,650)

            viewport id "recipe_scroller":
                draggable True
                mousewheel True
                
                $ row_count = 4
                $ column_count = 1 + (len(recipe_list) - 1) / 4
                grid row_count column_count:
                    xalign 0.5
                    yalign 0.5
                    spacing 5

                    for recipe in recipe_list:
                        frame:
                            background "images/menu_smallpage.png"
                            xsize 384
                            ysize 216
                            xpadding 0
                            ypadding 0
                            xalign 0.5
                            yalign 0.5

                            $ recipe_state = recipe_state_map.get(recipe['id'])
                            
                            if recipe_state == None:
                                text "???" align (0.5, 0.5) color "#000"
                                # 开发按钮
                                if recipe_dev:
                                    textbutton "强制解锁" text_size 16 action Function(set_recipe_unlock, recipe['id'])
                            else:
                                imagebutton:
                                    xalign 0.5
                                    yalign 0.3
                                    idle recipe['img']
                                    at transform:
                                        zoom 0.35
                                    # 仅解锁还没成功时置灰
                                    if recipe_state == 'unlock':
                                        at transform:
                                            matrixcolor BrightnessMatrix(-1.0)
                                            alpha 0.5
                                    # 成功后才能点击查看介绍
                                    else:
                                        activate_sound "audio/cooking/recipe_open.ogg"
                                        action Show('recipe_detail', dissolve, recipe)
                                # 开发按钮
                                if recipe_dev:
                                    if recipe_state == 'unlock':
                                        textbutton "强制成功" text_size 16 action Function(set_recipe_success, recipe['id'])
            vbar value YScrollValue("recipe_scroller")

    textbutton _("Return"):
        pos (50, 955)
        text_size 40
        text_font "GlowSans-Bold.otf"
        activate_sound "audio/cooking/recipe_close.ogg"
        action Return()

# 菜谱详情：菜品的介绍和图示
screen recipe_detail(recipe):
    image "bg kitchen.png"
    image "gui/overlay/game_menu.png"
    image "menu_overpage.png"

    image recipe['img']:
        ypos 100
        xalign 0.5

    text recipe['name']:
        size 50
        color "#753309"
        xalign 0.5
        xanchor 0.5
        ypos 630
 
    text recipe['desc']:
        size 40
        color "#753309"
        xalign 0.5
        xanchor 0.5
        ypos 730

    textbutton _("Return"):
        ypos 955 xpos 50
        text_size 40
        text_font "GlowSans-Bold.otf"
        activate_sound "audio/cooking/recipe_close.ogg"
        action Hide("recipe_detail", dissolve)

init python:
    # cooking 界面每帧刷新
    config.per_frame_screens.append('cooking')

    # 构造字典方便使用
    cooking_material_map = {}
    for material in cooking_material_list:
        cooking_material_map[material['id']] = material

    # 用于烹饪的 Class，每次开始烹饪初始化一个
    class Cooking():
        def __init__(self):
            # 待选择的食材
            self.to_select_material = [None, None, None, None, None, None, None, None]
            # 已选择的食材
            self.selected_material = [None, None, None, None, None]
            # 固定食材的数量
            self.fixed_material_count = 0
            # 是否可交互
            self.interactable = False
        
        # 获取指定次序的待选食材
        def get_to_select_material(self, idx):
            return cooking_material_map.get(self.to_select_material[idx])

        # 获取指定次序的已选食材
        def get_selected_material(self, idx):
            return cooking_material_map.get(self.selected_material[idx])
        
        # 添加一个食材
        def add_material(self, idx):
            # 添加已选食材
            for i, id in enumerate(self.selected_material):
                if id == None:
                    self.selected_material[i] = self.to_select_material[idx]
                    # 移除待选食材
                    self.to_select_material[idx] = None

        # 移除一个食材
        def remove_material(self, idx):
            # 待选食材还原
            for i, id in enumerate(self.to_select_material):
                if id == None:
                    self.to_select_material[i] = self.selected_material[idx]
                    # 清空已选食材
                    self.selected_material[idx] = None
                    return

        # 计算已选择的食材的分数
        def get_material_score(self):
            score = 0
            for id in self.selected_material:
                if id != None:
                    score += cooking_material_map[id]['score']
            return score

# material_list: 待选食材列表，最多八个
# fixed_material_list: 固定食材列表，最多五个
label show_cooking(
    material_list,
    fixed_material_list = [],
    start_button_img = None,
):
    python:
        _start_button_img = start_button_img
        cooking = Cooking()
        # 填充待选食材列表
        for idx, material in enumerate(material_list):
            cooking.to_select_material[idx] = material
        # 填充已选食材列表
        for idx, material in enumerate(fixed_material_list):
            cooking.selected_material[idx] = material
            cooking.fixed_material_count = len(fixed_material_list)

    show screen cooking(_start_button_img)
    return

label start_cooking():
    hide cooking()
    $ cooking.interactable = True
    call screen cooking(_start_button_img)
    return _return


# 烹饪界面
screen cooking(start_button_img = None):
    # 开始按钮
    fixed:
        fit_first True
        align (0.5, 0)
        add (start_button_img if start_button_img else "dishes/bread09_03.png"):
            matrixcolor BrightnessMatrix(-1.0)
            alpha 0.8
        textbutton "COOK":
            align (0.5, 0.6)
            text_size 100
            text_font "GlowSans-Bold.otf"
            text_kerning 10
            if cooking.interactable:
                action Return(cooking.get_material_score())

    # 已选食材：点击后移除食材
    hbox:
        align (0.45, 0.688)
        spacing 40
        for i in range(0, 5):
            $ material = cooking.get_selected_material(i)
            # 固定食材无法移除
            $ action = Function(cooking.remove_material, i) if i >= cooking.fixed_material_count else None
            use cooking_material_item(material, action, True)
    
    # 待选食材：点击后添加食材
    grid 2 4:
        spacing 10
        align (0.98, 0.1)
        for i in range(0, 8):
            $ material = cooking.get_to_select_material(i)
            $ action = Function(cooking.add_material, i) if cooking.interactable else None
            use cooking_material_item(material, action)

    # 对话

# 一个食材选项
# material：食材对象
# action：点击后的动作
screen cooking_material_item(material, action, shake = False):
    default is_hovering = False
    fixed:
        fit_first True
        imagebutton:
            xysize (185, 185)
            background "cooking/menu_cooking_box.png"
            idle Solid('#0000')
            hovered SetLocalVariable("is_hovering", True)
            unhovered SetLocalVariable("is_hovering", False)
            if material and action:
                hover "cooking/menu_cooking_box.png"
                if material.get('audio'):
                    activate_sound material.get('audio')
                action action
                # 选中的食材摇一下
                if shake:
                    at transform:
                        yoffset 0
                        linear 0.05 yoffset 15
                        linear 0.1 yoffset -15
                        linear 0.05 yoffset 0
            # 没有食材时不能设置 NullAction，否则对话阶段鼠标悬浮会阻塞
            else:
                action NullAction()
        python:
            # 没有食材时将 hover 复位，避免没有 NullAction 导致 unhovered 失效的问题
            if not material:
                is_hovering = False
        # 当前栏位存在食材
        if material:
            add material['img'] zoom 0.25 align (0.5, 0.5)
            # 调试模式显示食材分数
            if recipe_dev:
                text "分数：" + str(material['score']) size 28
            # hover 显示食材名称
            if is_hovering:
                frame:
                    anchor (1.0, 1.0)
                    pos (40, 40)
                    xpadding 20
                    background Frame("gui/cooking/name_frame.png", 30, 30, 30, 30)
                    text material['name'] size 40 layout "nobreak" 