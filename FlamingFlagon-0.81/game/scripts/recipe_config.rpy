init python:
    # 开发者模式，会开放一些便于调试的按钮，功能开发准备发布则设置为 False
    recipe_dev = False

    # 所有菜谱的字典
    # id: 唯一 id，用于判断解锁等
    # img：显示的图片路径
    # name：菜谱名称
    # desc：菜谱描述
    # 顺序 汤 面包类主食类 甜品类 蔬菜类 纯肉类
    recipe_list = [
        {
            "id": "vegetablesoup",
            "img": "dishes/soup04_07.png",
            "name": _("Vegetable Soup"),
            "desc": _("This is the first dish you've made here.\nAlthough it's very ordinary, it holds special significance for you."),
        },
        {
            "id": "toast",
            "img": "dishes/bread09_03.png",
            "name": _("Toast"),
            "desc": _("dishes/bread09_03.png"),
        },
        {
            "id": "toastbutter",
            "img": "dishes/bread09_02.png",
            "name": _("Butter Toast"),
            "desc": _("dishes/bread09_02.png"),
        },
        {
            "id": "toastegg",
            "img": "dishes/bread09_01.png",
            "name": _("Sunny Toast"),
            "desc": _("dishes/bread09_01.png"),
        },
        {
            "id": "baconsandwich",
            "img": "dishes/sandwich01_01.png",
            "name": _("Bacon Sandwich"),
            "desc": _("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"),
        },
        {
            "id": "shrimpsandwich",
            "img": "dishes/sandwich01_02.png",
            "name": _("Shrimp Sandwich"),
            "desc": _("dishes/sandwich01_02.png"),
        },
        {
            "id": "bakedapple",
            "img": "dishes/apple01_01.png",
            "name": _("Baked Apple"),
            "desc": _("A sweet dish that is easy to make. \nA warm treat for a chilly night."),
        },
        {
            "id": "bakedapplecream",
            "img": "dishes/apple01_02.png",
            "name": _("Baked Apple & Cream"),
            "desc": _("Delicious warm baked apple with the addition of fresh cream. \nThe cream reminds you of the night you baked your first apple."),
        },
        #{
            #"id": "applepie",
            #"img": "dishes/applepie01_01.png",
            #"name": _("Apple Pie"),
            #"desc": _("dishes/applepie01_01.png"),
        #},
        {
            "id": "bakedpotato",
            "img": "dishes/potato01_01.png",
            "name": _("Baked Potato"),
            "desc": _("dishes/applepie01_01.png"),
        },
        {
            "id": "steak",
            "img": "dishes/steak04_01.png",
            "name": _("Steak"),
            "desc": _("dishes/applepie01_01.png"),
        },
    ]
    
    # 所有食材的字典
    cooking_material_list = [
        {
            "id": "soup",
            "img": "dishes/soup04_07.png",
            "name": _("Soup"),
            "audio": "audio/cooking/liquid.ogg",
            "score": 1,
        },
        {
            "id": "apple",
            "img": "dishes/apple01_01.png",
            "name": _("Apple"),
            "audio": "audio/cooking/pop.ogg",
            "score": 10,
        },
        {
            "id": "toast_bread",
            "img": "ingredients/bread2.png",
            "name": _("Bread"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "toast_tomato",
            "img": "ingredients/tomato.png",
            "name": _("Tomato"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "toast_lettuce",
            "img": "ingredients/cabbage.png",
            "name": _("Lettuce"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "toast_egg",
            "img": "ingredients/egg1_01.png",
            "name": _("Egg"),
            "audio": "audio/cooking/pop2.ogg",
            "score": 0,
        },
        {
            "id": "toast_butter",
            "img": "ingredients/supplies01_01.png",
            "name": _("Butter"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "sandwich_bread",
            "img": "ingredients/bread2.png",
            "name": _("Bread"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "sandwich_tomato",
            "img": "ingredients/tomato.png",
            "name": _("Tomato"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "sandwich_cheese",
            "img": "ingredients/cheese.png",
            "name": _("Cheese"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "sandwich_shrimp",
            "img": "ingredients/ingredients_shrimp01_01.png",
            "name": _("Shrimp"),
            "audio": "audio/cooking/pop3.ogg",
            "score": 20,
        },
        {
            "id": "sandwich_bacon",
            "img": "ingredients/supplies01_01.png",
            "name": _("Bacon"),
            "audio": "audio/cooking/pop3.ogg",
            "score": 30,
        },
        {
            "id": "sandwich_avocado",
            "img": "ingredients/ingredients_avocado01_01.png",
            "name": _("Avocado"),
            "audio": "audio/cooking/pop.ogg",
            "score": 20,
        },
        {
            "id": "bakedapple_apple",
            "img": "ingredients/apple_01.png",
            "name": _("Apple"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "bakedapple_honey",
            "img": "ingredients/ingredients_honey01_01.png",
            "name": _("Honey"),
            "audio": "audio/cooking/pop2.ogg",
            "score": 1,
        },
        {
            "id": "bakedapple_mint",
            "img": "ingredients/herb6_01.png",
            "name": _("Mint"),
            "audio": "audio/cooking/pop.ogg",
            "score": 3,
        },
        {
            "id": "bakedapple_cinnamon",
            "img": "ingredients/pouch.png",
            "name": _("Cinnamon"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "bakedapple_hotpepper",
            "img": "ingredients/pepper_01.png",
            "name": _("Hot Pepper"),
            "audio": "audio/cooking/pop3.ogg",
            "score": -999,
        },
        {
            "id": "bakedapple_cream",
            "img": "ingredients/milk.png",
            "name": _("Cream"),
            "audio": "audio/cooking/liquid.ogg",
            "score": 10,
        },
        {
            "id": "bakedpotato_potato",
            "img": "ingredients/potato.png",
            "name": _("Potato"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "bakedpotato_butter",
            "img": "ingredients/supplies01_01.png",
            "name": _("Butter"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "bakedpotato_salt",
            "img": "ingredients/seasoning_02.png",
            "name": _("Salt"),
            "audio": "audio/cooking/pop3.ogg",
            "score": 1,
        },
        {
            "id": "steak_meat",
            "img": "ingredients/meat2.png",
            "name": _("Fresh Meat"),
            "audio": "audio/cooking/pop.ogg",
            "score": 0,
        },
        {
            "id": "steak_saltpepper",
            "img": "ingredients/seasoning_02.png",
            "name": _("Salt & Pepper"),
            "audio": "audio/cooking/pop.ogg",
            "score": 10,
        },
        {
            "id": "steak_rosemary",
            "img": "ingredients/herb2_01.png",
            "name": _("Rosemary"),
            "audio": "audio/cooking/pop2.ogg",
            "score": 1,
        },
        {
            "id": "steak_garlic",
            "img": "ingredients/garlic.png",
            "name": _("Garlic"),
            "audio": "audio/cooking/pop.ogg",
            "score": 1,
        },
        {
            "id": "steak_hotpepper",
            "img": "ingredients/pepper_01.png",
            "name": _("Hot Pepper"),
            "audio": "audio/cooking/pop3.ogg",
            "score": -999,
        },
        {
            "id": "steak_ginger",
            "img": "ingredients/ginger.png",
            "name": _("Ginger"),
            "audio": "audio/cooking/pop2.ogg",
            "score": -999,
        },
    ]
