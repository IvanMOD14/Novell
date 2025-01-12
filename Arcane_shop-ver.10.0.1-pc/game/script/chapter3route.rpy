label routechoice:
    scene bg home with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40
    show cara sleep inn_d
    with dissolve
    
    $ unlock_character_image("cara", "cara b_no inn_d")
    $ display_text = _("이미지 : [pl_name](알몸)")
    show screen affection_indicator

    c "\"으음...\"" id c03r_0000

    "창을 통해 들어오는 밝은 햇살이 [pl_name]의 잠을 깨운다." id c03r_0001
    
    show cara base
    with dissolve
    pause(0.5)

    show cara sleep
    with dissolve
    
    "[pl_name][josa_eun_neun] 침대에서 꾸물거리다 다시 눈을 감았다." id c03r_0002
    
    c "(피곤한데... 조금만 더 잘까? 진짜 조금만...)" id c03r_0003

    "오늘따라 침대가 포근하게 느껴진다." id c03r_0004

    show cara base
    with dissolve

    "[pl_name][josa_eun_neun] 그대로 몇 분간 몽롱하게 있다가 간신히 눈을 떴다." id c03r_0005
    
    show cara sigh
    with dissolve

    c "(으, 그래도 일은 해야지.)" id c03r_0006
    
    scene bg shop with Fade(0.8, 0.8, 0.8)
    
    "[pl_name][josa_eun_neun] 졸린 몸을 이끌고 영업준비를 했다." id c03r_0007
    
    show cara sigh
    with dissolve

    "[pl_name][josa_eun_neun] 하품을 쩍쩍하며 안내판을 영업중으로 바꾸었다." id c03r_0008
    
    show question :
        xalign 0.57
        yalign 0.1
    show cara consider
    with dissolve

    c "(오늘 왜 이렇게 졸리지?)" id c03r_0009
    
    hide question
    
    #의자앉는 내리기
    show cara sleep at change(1, 0, 50)
    with dissolve

    "잠깐 의자에 앉은 [pl_name][josa_eun_neun] 따스한 햇살에 잠깐 눈을 감았다." id c03r_0010
    
    "손님도 없고 조용하니 졸음이 파도처럼 몰려왔다." id c03r_0011

    show cara sleep at change(1, 0, 100)
    with dissolve

    "[pl_name]의 의지와 상관없이 고개가 저절로 떨어진다." id c03r_0012
    
    c "(손님 오기 전까지 조금만 자자...)" id c03r_0013
    
    show cara sleep at change(1, 0, 150)
    with dissolve

    "결국 마음을 굳힌 [pl_name][josa_eun_neun] 테이블 위에 엎드렸다." id c03r_0014
    
    c "(이 모습을 가헬이 보면 잔소리 할텐데... 근데 오늘 가헬이 안 보이네.)" id c03r_0015
    
    "가헬이 깨우리라 판단한 [pl_name][josa_eun_neun] 그냥 잠들기를 선택했다." id c03r_0016
    
    c "(엘레드도 올 때가 지났는데, 음...)" id c03r_0017

    hide cara
    with dissolve

    "[pl_name][josa_eun_neun] 잡다한 생각을 하다가 잠에 빠져들었다." id c03r_0018

    "고요한 상점에 [pl_name]의 숨소리만 조용하게 흐른다." id c03r_0019

    stop music fadeout 2.5
    scene bg backcol with Fade(0.8, 0.8, 0.8)

    n "\"...\"" id c03r_0020

    n "\"[pl_name]...\"" id c03r_0021

    "누군가가 [pl_name][josa_eul_reul] 부르고 있었다." id c03r_0022

    c sleep "(누구지?...)" id c03r_0023
    
    "잠에 푹 빠져있던 [pl_name][josa_eun_neun] 몽롱한 정신으로 고개를 들었다. 하지만 상대방의 모습은 보이지 않았다." id c03r_0024

    "꿈 속이라는 걸 자각하지 못한 [pl_name][josa_eun_neun] 주위를 둘러보았다." id c03r_0025

    n "\"[pl_name]?\"" id c03r_0026

    "[pl_name][josa_eun_neun] 자신을 부르는 쪽으로 고개를 돌렸다." id c03r_0027

    "[pl_name]의 눈 앞에 있는 수인은..." id c03r_0028

    #~캐릭터 선택 화면~ 만들어야 함
    menu :
        "가헬" :

            show wolf base am_d
            with dissolve

            "\"...\"" id c03r_0029

            jump c4w_start

        "엘레드" :

            show tiger base_am am_d
            with dissolve

            "\"...\"" id c03r_0030

            jump c4t_start

