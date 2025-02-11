
init python:
    # 说明：
    # id：必填，该选项 id，会作为选择后的返回值
    # title：必填，可以为空字符串，显示标题的问题
    # title_size：可选，标题的字号大小
    # background：可选，选项背景图片的路径
    # show：必填，该选项的初始显示状态，后续可以通过接口修改

    # 所有选项
    total_workday_option_list = [
        {
            "id": 'example1',
            "title": 'Terrance',
            "title_size": 80,
            "background": "workday/chara_box_terrance.png",
            "show": False,
        },
        {
            "id": 'example2',
            "title": 'Odachi',
            "title_size": 80,
            "background": "workday/chara_box_odachi.png",
            "show": False,
        },
        {
            "id": 'example3',
            "title": 'Niall',
            "title_size": 80,
            "background": "workday/chara_box_niall.png",
            "show": False,
        },
        {
            "id": 'example3-1',
            "title": '',
            "show": False,
        },
        {
            "id": 'example3-2',
            "title": '',
            "show": False,
        },
        {
            "id": 'khaleb_work_option',
            "title": 'Khaleb',
            "background": "workday/chara_box_khaleb.png",
            "show": False,
        },
        {
            "id": 'marcus_work_option',
            "title": 'Marcus',
            "background": "workday/chara_box_marcus.png",
            "show": False,
        },
        {
            "id": 'terrance_meet_option',
            "title": 'Terrance',
            "background": "workday/chara_box_terrance.png",
            "show": True,
        },
        {
            "id": 'terrance_work_option',
            "title": 'Terrance',
            "background": "workday/chara_box_terrance.png",
            "show": False,
        },
        {
            "id": 'odachi_meet_option',
            "title": '???',
            "background": "workday/chara_box_odachi2.png",
            "show": True,
        },
        {
            "id": 'odachi_work_option',
            "title": 'Odachi',
            "background": "workday/chara_box_odachi.png",
            "show": False,
        },
        {
            "id": 'niall_meet_option',
            "title": '???',
            "background": "workday/chara_box_niall2.png",
            "show": True,
        },
        {
            "id": 'niall_work_option',
            "title": 'Niall',
            "background": "workday/chara_box_niall.png",
            "show": False,
        },
    ]

    # 后续发布中动态增加的 workday 选项，会添加到以前存档的 workday 选项记录中
    # 后续删除的 workday 选项，以前的存档中也会消失
    def update_workday_option_list():
        global workday_option_list, total_workday_option_list
        new_workday_option_list = []
        for total_option in total_workday_option_list:
            has_exist = False
            # 当前存档中存在该选项，继续存在
            for curr_option in workday_option_list:
                if total_option['id'] == curr_option['id']:
                    has_exist = True
                    new_workday_option_list.append(curr_option)
                    break
            # 当前存档中不存在该选项，新增
            if has_exist == False:
                new_workday_option_list.append(total_option)
        workday_option_list = new_workday_option_list
    
    # 显示选项
    def show_workday_option(id):
        global workday_option_list
        option = find_workday_option(id)
        option['show'] = True

    # 隐藏选项
    def hide_workday_option(id):
        global workday_option_list
        option = find_workday_option(id)
        option['show'] = False
    
    def find_workday_option(id):
        global workday_option_list
        for option in workday_option_list:
            if option['id'] == id:
                return option
        return None

    def find_total_workday_option(id):
        global total_workday_option_list
        for option in total_workday_option_list:
            if option['id'] == id:
                return option
        return None

# 当前存档中的选项

default workday_option_list = {}

label workday_entry(text):
    $ _text = text
    $ update_workday_option_list()
    call screen workday(text)
    return _return

screen workday(text = None):
    if text:
        use say(None, text)
        $ renpy.get_widget('workday', 'what').style = style.get('say_thought')

    default spacing = 20
    default item_ysize = 225
    default page_size = 3
    viewport:
        pos (860, 30)
        xysize (1030, item_ysize * page_size + spacing * (page_size - 1))
        mousewheel True
        scrollbars "vertical"
        draggable True
        vbox:
            spacing 20
            for slot_option in workday_option_list:
                $ option = find_total_workday_option(slot_option['id'])
                if slot_option['show'] and option:
                    fixed:
                        fit_first True
                        # 选项底框
                        add 'workday/choice_box.png'
                        # 选项背景
                        if option.get('background'):
                            add option.get('background')
                        # 文字
                        text option['title']:
                            xpos 100
                            yalign 0.5
                            size option.get("title_size", 80)
                            font "GlowSans-ExtraBold.otf"
                        # 选项 hover 花纹
                        imagebutton:
                            idle At('workday/choice_box_hover.png', Transform(alpha = 0))
                            hover 'workday/choice_box_hover.png'
                            action Return(option['id'])