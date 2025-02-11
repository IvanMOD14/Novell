
init python:
    # 说明：
    # id：必填，该选项 id，会作为选择后的返回值
    # title：必填，可以为空字符串，显示标题的问题
    # title_size：可选，标题的字号大小
    # background：可选，选项背景图片的路径
    # show：必填，该选项的初始显示状态，后续可以通过接口修改

    # 所有选项
    total_freeday_option_list = [
        {
            "id": 'example1',
            "title": 'Village',
            "background": "freeday/choice_box_village.png",
            "title_size": 80,
            "show": False,
        },
        {
            "id": 'example2',
            "title": 'Market',
            "background": "freeday/choice_box_market.png",
            "title_size": 80,
            "show": False,
        },
        {
            "id": 'example3',
            "title": 'My Room',
            "background": "freeday/choice_box_myroom.png",
            "title_size": 80,
            "show": False,
        },
        {
            "id": 'example3-1',
            "title": 'Clean tavern front',
            "show": False,
        },
        {
            "id": 'example3-2',
            "title": 'Rest in room',
            "show": False,
        },
        {
            "id": 'go to village',
            "title": _('Village'),
            "background": "freeday/choice_box_village.png",
            "show": False,
        },
        {
            "id": 'go to tailservice',
            "title": _('Tail Service'),
            "background": "freeday/choice_box_tailservice.png",
            "show": False,
        },
        {
            "id": 'go to bathhouse',
            "title": _('Bathhouse'),
            "background": "freeday/choice_box_bathhouse.png",
            "show": False,
        },
        {
            "id": 'go to market',
            "title": _('Market'),
            "background": "freeday/choice_box_market.png",
            "show": True,
        },
        {
            "id": 'go to backyard',
            "title": _('Backyard'),
            "background": "freeday/choice_box_backyard.png",
            "show": True,
        },
        {
            "id": 'go to church',
            "title": _('Church'),
            "background": "freeday/choice_box_church.png",
            "show": False,
        },
        {
            "id": 'go to room',
            "title": _('My Room'),
            "background": "freeday/choice_box_myroom.png",
            "show": True,
        },
    ]

    # 后续发布中动态增加的 freeday 选项，会添加到以前存档的 freeday 选项记录中
    # 后续删除的 freeday 选项，以前的存档中也会消失
    def update_freeday_option_list():
        global freeday_option_list, total_freeday_option_list
        new_freeday_option_list = []
        for total_option in total_freeday_option_list:
            has_exist = False
            # 当前存档中存在该选项，继续存在
            for curr_option in freeday_option_list:
                if total_option['id'] == curr_option['id']:
                    has_exist = True
                    new_freeday_option_list.append(curr_option)
                    break
            # 当前存档中不存在该选项，新增
            if has_exist == False:
                new_freeday_option_list.append(total_option)
        freeday_option_list = new_freeday_option_list
    
    # 显示选项
    def show_freeday_option(id):
        update_freeday_option_list()
        option = find_freeday_option(id)
        option['show'] = True

    # 隐藏选项
    def hide_freeday_option(id):
        update_freeday_option_list()
        option = find_freeday_option(id)
        option['show'] = False
    
    def find_freeday_option(id):
        global freeday_option_list
        for option in freeday_option_list:
            if option['id'] == id:
                return option
        return None

    def find_total_freeday_option(id):
        global total_freeday_option_list
        for option in total_freeday_option_list:
            if option['id'] == id:
                return option
        return None

# 当前存档中的选项
default freeday_option_list = {}

label freeday_entry(text):
    $ _text = text
    $ update_freeday_option_list()
    call screen freeday(text)
    return _return

screen freeday(text = None):
    if text:
        use say(None, text)
        $ renpy.get_widget('freeday', 'what').style = style.get('say_thought')

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
            for slot_option in freeday_option_list:
                $ option = find_total_freeday_option(slot_option['id'])
                if slot_option['show'] and option:
                    fixed:
                        fit_first True
                        # 选项底框
                        add 'freeday/choice_box.png'
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
                            idle At('freeday/choice_box_hover.png', Transform(alpha = 0))
                            hover 'freeday/choice_box_hover.png'
                            action Return(option['id'])