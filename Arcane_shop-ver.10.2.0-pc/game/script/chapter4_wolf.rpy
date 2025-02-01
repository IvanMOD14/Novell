label c4w_start:

    $ cleanup_memory()
    $ _skipping = False
    scene bg shop
    show chapter_back
    with Fade(0.8, 0.8, 0.8)
    
    pause 0.4
    play channel1 "effect/fresh_snap.mp3" volume 0.7
    pause 0.1
    show chap
    pause 0.5
    show ter
    pause 1.0
    play channel2 "effect/finger_snap.mp3" volume 0.8
    pause 0.1
    show four
    pause 1.0
    
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35
    
    hide chapter_back
    hide chap
    hide ter
    hide four
    with Dissolve (1.5)

    $ _skipping = True
    $ wolf_route = True
    
    show screen book_icon with dissolve
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c04_w_0000
    
    show wolf am_d
    with dissolve

    "\"...\"" id c04_w_0001
    
    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 40)
    show wolf bigeye at surprise_move

    "가게로 돌아온 가헬은 엎드려 자는 [pl_name][josa_eul_reul] 보고 살짝 움찔했다." id c04_w_0002
    
    "이렇게 무방비한 모습을 볼 기회는 별로 없었다." id c04_w_0003

    hide exclamation
    show wolf base
    with dissolve

    "가헬은 잠시 [pl_name]의 얼굴을 보며 추억에 잠겼다." id c04_w_0004
    
    "어린 시절의 가헬이 보기에도 [pl_name][josa_eun_neun] 잘생겼다." id c04_w_0005
    
    w "(이렇게 멋있는 수컷은 흔치 않지.)" id c04_w_0006
    
    show wolf shy
    with dissolve

    "가헬은 [pl_name][josa_eul_reul] 끌어안고 같이 낮잠을 자면 얼마나 좋을지 상상했다." id c04_w_0007
    
    show wolf shy2
    with dissolve

    "마음속이 간질거리는 기분이었다. 가헬은 새삼 [pl_name]에게 반해서 두근거리는 걸 자각했다." id c04_w_0008
    
    "아침 훈련을 하느라 숨차게 뛰었던 때보다, 지금이 더 심장박동을 잘 느낄 수 있었다." id c04_w_0009
    
    show wolf shy3
    with dissolve

    "가헬은 잠시 창밖을 보며 마음을 진정시키고 [pl_name][josa_eul_reul] 깨웠다." id c04_w_0010
    
    show wolf talk
    with dissolve

    w "\"[pl_name], [pl_name]?\"" id c04_w_0011
    
    show wolf base
    with dissolve

    c sleep "\"으, 어?\"" id c04_w_0012
    
    "퍼뜩 깨어난 [pl_name][josa_eun_neun] 얼빠진 표정으로 가헬을 바라보았다." id c04_w_0013
    
    "[pl_name][josa_eun_neun] 잠에서 다 깨지 못하고 멍하니 앉아 있었다." id c04_w_0014
    
    show wolf talk am_u
    with dissolve
    
    w "\"많이 피곤한가?\"" id c04_w_0015
    
    show wolf base am_d
    with dissolve

    c base "\"음... 아니, 그냥 좀 졸려서. 괜찮아.\"" id c04_w_0016
    
    "[pl_name][josa_eun_neun] 크게 하품하고 자리에서 벌떡 일어났다." id c04_w_0017
    
    "쭉쭉 기지개를 켜고 마른세수를 한 [pl_name][josa_eun_neun] 주변을 둘러봤다." id c04_w_0018
    
    c ddam2 "\"헉! 벌써 11시야? 진작에 깨우지 그랬어.\"" id c04_w_0019
    
    show wolf talk am_u
    with dissolve
    
    w "\"메모를 남겨두고 나갔는데...?\"" id c04_w_0020
    
    c question2 "\"메모?\"" id c04_w_0021
    
    show wolf base am_d at walk (-1500, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.85
    pause(3.0)
    show wolf at mirror
    show wolf at walk (0, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.85
    pause(0.5)

    "가헬은 카운터 위에 올려진 메모를 집어 왔다." id c04_w_0022

    show wolf talk am_u at mirror2
    with dissolve

    w "\"... 안 읽었군.\"" id c04_w_0023
    
    w "\"오늘은 아침 훈련을 다녀왔다.\"" id c04_w_0024
    
    show wolf base am_d
    with dissolve

    c ddam2 "(그것도 모르고 쿨쿨 잤네...)" id c04_w_0025
    
    "조금 부끄러워진 [pl_name][josa_eun_neun] 혹시 침을 흘리거나 하진 않았나 거울을 확인했다." id c04_w_0026

    c question2 "\"손님이 왔다가 그냥 간 건 아니겠지?\"" id c04_w_0027

    show wolf talk am_u
    with dissolve

    w "\"... 도둑 걱정이 먼저 아닌가?\"" id c04_w_0028

    show wolf base am_d
    with dissolve

    "[pl_name][josa_eun_neun] 깜짝 놀라서 금고를 열어봤다가 머쓱하게 닫았다." id c04_w_0029
    
    c ddam "(금고는 어차피 보안 마법이 걸려있으니 걱정할 필요가 없지...)" id c04_w_0030
    
    c sigh "\"으, 잠이 덜 깼나봐.\"" id c04_w_0031

    show wolf talk
    with dissolve

    w "\"괜찮나? 피곤하면 오늘은 쉬는 게 어떤가.\"" id c04_w_0032

    show wolf base
    with dissolve

    c talk "\"아냐. 이제 정신 차리고 일해야지.\"" id c04_w_0033
    
    "가헬은 자꾸 하품하는 [pl_name][josa_eul_reul] 보고 말했다." id c04_w_0034

    show wolf talk
    with dissolve

    w "\"그럼 간단한 집안일 정도는 내가 대신 하지.\"" id c04_w_0035
    
    show wolf base
    with dissolve

    c "\"앗, 그렇게까지 할 필요는-\""  id c04_w_0036
    
    "[pl_name][josa_eun_neun] 말하는 도중에 생각이 바뀌었다." id c04_w_0037
    
    "어차피 평소에도 알게 모르게 챙겨주는 가헬이라 마음이 느슨해졌다." id c04_w_0038
    
    c laugh "\"뭐, 도와준다니 고마워.\"" id c04_w_0039
    
    "[pl_name][josa_eun_neun] 뻔뻔하게 웃으며 할 일을 떠넘겼다." id c04_w_0040
    
    "가헬은 고개를 끄덕이고는 2층으로 올라갔다." id c04_w_0041

    show wolf at mirror
    with dissolve
    pause(0.5)
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 2.8, 5)
    pause(1.0)

    # [가헬 방으로 장면전환]
    scene bg home with Fade(0.8, 0.8, 0.8)

    show wolf base
    with dissolve

    "검과 갑옷을 정리한 가헬은 땀에 젖은 옷을 꺼냈다." id c04_w_0042
    
    "안 좋은 냄새가 나기 전에 빨래할 생각이었다." id c04_w_0043

    w "(하는 김에 [pl_name]의 옷도 다 세탁해야겠군.)" id c04_w_0044

    stop music fadeout 2.5
    
    # [2층복도? 화장실? 로 장면전환]
    scene bg shop2f with Fade(0.8, 0.8, 0.8)

    show wolf smile
    with dissolve

    "가헬은 미소를 지으며 바구니에 담긴 옷을 꺼냈다." id c04_w_0045
    
    "[pl_name][josa_i_ga] 입던 옷에서 나는 희미한 체취가 느껴진다." id c04_w_0046
    
    "[pl_name][josa_wa_gwa] 함께 살면서 좋은 점이 여러 가지 있지만, 역시 일상을 공유하는 관계가 된 것이 가장 좋았다." id c04_w_0047
    
    
    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 40)
    show wolf happy at surprise_move

    w "\"... !!\"" id c04_w_0048

    show underwear :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "가헬은 옷더미에서 [pl_name]의 속옷을 발견하고 흠칫 놀랐다." id c04_w_0049

    hide exclamation
    hide underwear
    with dissolve

    play sound "effect/swallowing.mp3" volume 0.85
        
    "왠지 침이 꿀꺽 넘어갔다." id c04_w_0050
    
    "평소엔 몰랐지만 한 번 의식하고 나니 갑자기 엄청나게 야한 물건으로 보였다." id c04_w_0051
    
    show wolf shy3
    with dissolve

    w "(무슨 생각을...)" id c04_w_0052

    show wolf shy2
    with dissolve

    w "(아니, 그렇지만...)" id c04_w_0053
    
    "속으로 다짐해 봐도 자꾸만 눈길이 간다." id c04_w_0054

    play channel1 "effect/heart_beat.mp3" volume 0.75
    
    "괜히 입이 바싹바싹 마르고 심장이 두근거리는 게 느껴진다." id c04_w_0055
    
    show wolf am_u
    with dissolve

    "가헬은 결국 그것에 손을 뻗었다." id c04_w_0056
    
    "손에 감기는 부드러운 천의 감촉에 털이 곤두섰다." id c04_w_0057
    
    "가헬은 [pl_name]의 속옷을 집어 얼굴에 가져다 댔다." id c04_w_0058
    
    show wolf horny3
    with dissolve

    w "\"......\"" id c04_w_0059

    play sound "effect/inhale.mp3" volume 0.9
    
    "가헬은 깊게 숨을 들이쉬며 [pl_name]의 체향을 폐에 가득 채웠다." id c04_w_0060
    
    "살냄새와 함께 향긋한 풀 내음과 포근한 이불 같은 냄새가 뒤섞인 느낌이었다." id c04_w_0061
    
    play sound "effect/exhale.mp3" volume 0.95
    show wolf horny
    with dissolve

    w "\"하아...\"" id c04_w_0062
    
    "가헬은 황홀한 표정으로 여운을 즐겼다." id c04_w_0063
    
    "죄책감 따위는 사르르 녹아 사라졌다. 조금만 더 즐기고 싶은 욕심이 차오르기 시작했다." id c04_w_0064
    
    show wolf shy2
    with dissolve

    w "(하지만 [pl_name][josa_i_ga] 눈치채면 어떡하지?)" id c04_w_0065
    
    "가헬은 고민에 빠졌다." id c04_w_0066
    
    menu :
        "속옷을 몰래 챙긴다." :
            $ underwear += 1
            show wolf shy2 am_d
            show underwear :
                xcenter 0.5
                ycenter 0.5
            with dissolve
            
            "가헬은 재빠르게 속옷을 주머니에 숨겼다." id c04_w_0067

            hide underwear
            show wolf shy3
            with dissolve

            w "(빨리 쓰고 다른 빨래와 같이 놓으면 모르겠지?)" id c04_w_0068
    
            "가헬은 두근거리는 심장을 진정시키며 다른 옷들을 꺼냈다." id c04_w_0069

            stop channel1 fadeout 2.5
            
        "그냥 평범하게 세탁한다." :
            show wolf shy am_d
            with dissolve
            stop channel1 fadeout 2.5

            "가헬은 고개를 좌우로 저었다." id c04_w_0070

            show wolf shy2
            with dissolve

            w "(참자... 들키면 변명할 거리도 없어.)" id c04_w_0071
    
            "가헬은 [pl_name]의 속옷도 그냥 다른 옷더미에 던져넣었다." id c04_w_0072
    
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40 
    scene bg shop with Fade(0.8, 0.8, 0.8)
    "{i}잠시 후{/i}" id c04_w_0073
    
    show cara base
    with dissolve

    "[pl_name][josa_eun_neun] 회복 물약을 만들면서 잡생각을 하고 있었다." id c04_w_0074
    
    "저녁으로 무엇을 먹을지부터, 돈을 쓸어 담을 수 있는 혁신적인 신제품의 아이디어까지 온갖 생각에 빠져있었다." id c04_w_0075
   
    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (890, 0)
    show cara consider
    with dissolve

    c "(용병뿐만 아니라 대부분의 사람들이 사고 싶어 할 물건 없을까?)" id c04_w_0076
    
    c "(식사를 대신하는 물약 같은 거라도 만들어볼까? 아니면 근육을 키워주는 연고 같은...)" id c04_w_0077
    
    hide question
    show exclamation at exclamation_move (1050, 40)
    show cara ddam2
    with vpunch

    c "\"앗 뜨거!\"" id c04_w_0078

    hide exclamation
    with dissolve
    
    "허황된 망상에 빠져있던 [pl_name][josa_eun_neun] 연금솥에서 끓이던 물약에 손가락을 집어넣을 뻔했다." id c04_w_0079

    # 레스크 한숨
    show cara sigh
    with dissolve

    "지켜보는 사람도 없는데 괜히 부끄러워졌다." id c04_w_0080
    
    show cara base
    with dissolve

    c "(빨리 마무리하고 병에 담아야지.)" id c04_w_0081

    "[pl_name][josa_eun_neun] 마법 불꽃을 끄고 연금솥을 냉각시켰다." id c04_w_0082
    
    "솥의 손잡이 끝에 손을 대고 마력을 불어넣었다." id c04_w_0083

    show cara consider
    with dissolve

    c "(내장된 특수 합금이 자동으로 최적 온도를... 뭐라고 했더라?)" id c04_w_0084
    
    show cara base
    with dissolve

    c "(아무튼 비싼 값을 하고 좋네.)" id c04_w_0085
    
    c "(아, 이런 아이디어가 있어야 부자가 될 텐데.)" id c04_w_0086

    "[pl_name][josa_eun_neun] 유리병을 꺼내서 물약을 하나씩 담았다." id c04_w_0087
    
    play sound "effect/water.mp3" volume 0.5
    show potion :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "맑은 초록빛이 상쾌해 보인다." id c04_w_0088
    
    hide potion
    with dissolve

    show cara am_u
    with dissolve

    "연금솥에 든 액체를 전부 병에 담은 [pl_name][josa_eun_neun] 약간 뻐근해진 어깨를 주물렀다." id c04_w_0089
    
    hide cara with dissolve
    pause(0.5)
    show wolf at change(1, 1500, 0)
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (0, 2.8, 5)

    "마침 가헬이 아래층으로 내려왔다." id c04_w_0090

    show wolf talk am_u
    with dissolve

    w "\"뭐 도울 일이라도 있나?\"" id c04_w_0091

    show wolf base am_d
    with dissolve

    c "\"아니, 다 했어. 그냥 어깨가 좀 뻐근해서...\"" id c04_w_0092

    "[pl_name][josa_eun_neun] 뒤를 돌아서 궤짝에 회복 물약을 채워넣기 시작했다." id c04_w_0093
    
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at fwalk

    "그 모습을 지켜보던 가헬은 [pl_name]의 뒤에 가까이 다가섰다." id c04_w_0094
    
    show wolf am_u
    with dissolve

    "[pl_name][josa_i_ga] 궤짝을 닫자마자 가헬은 [pl_name]의 어깨에 손을 얹었다." id c04_w_0095

    c "\"휴, 진짜 다 했-\"" id c04_w_0096

    #레스크 깜짝
    with vpunch
    c ddam2 "\"으악!\"" id c04_w_0097

    "가헬은 [pl_name]의 뒤에서 어깨를 꾹꾹 주무르며 말했다." id c04_w_0098
    
    show wolf talk
    with dissolve

    w "\"어깨가 엄청나게 굳었는데, 스트레칭은 잘하고 있나?\"" id c04_w_0099

    show wolf base
    with dissolve

    c ddam "\"윽, 잠깐! 아! 흐읍...\"" id c04_w_0100

    # 레스크 horny4 에서 홍조 빼서 hurt 표정 만들기. 끄아아아악 함
    with vpunch

    c hurt "\"거긴 좀, 아픈!... 끄으으으...\"" id c04_w_0101

    "가헬은 강력한 힘으로 자비 없이 마사지했다." id c04_w_0102
    
    "돌처럼 굳은 어깨를 주무르며 [pl_name][josa_i_ga] 쭈뼛거리는 걸 감상했다." id c04_w_0103
    
    "마사지를 당하는 [pl_name][josa_eun_neun] 저릿저릿한 느낌에 거의 눈물을 찔끔 흘릴 뻔했다." id c04_w_0104

    show wolf shy3
    with dissolve

    w "(뒤에서 이러고 있으니 왠지 기분이 이상한데...)" id c04_w_0105

    play sound "effect/footstep.mp3" volume 0.85
    show wolf base am_d at bwalk
    
    "가헬은 엄한 생각이 들기 전에 손을 뗐다." id c04_w_0106
    
    "[pl_name][josa_eun_neun] 어깨가 너덜너덜해진 상태로 말했다." id c04_w_0107

    c ddam2 "\"고마워. 덕분에 많이 나아진 것 같아.\"" id c04_w_0108

    show wolf talk
    with dissolve

    w "\"이 궤짝은 창고에 둘 생각인가?\"" id c04_w_0109

    show wolf base at change(1, 0, 100)
    with ease
    pause(0.3)
    show wolf at change(1, 0, 0)
    with ease
    pause(0.3)
    show wolf at mirror
    pause(0.1)
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 2.8, 5)

    "[pl_name][josa_i_ga] 말할 틈도 없이 가헬이 물약 상자를 들고 갔다." id c04_w_0110

    c consider "(훈련도 하고 왔으면서, 무리하는 거 아닌가?)" id c04_w_0111

    "[pl_name][josa_eun_neun] 가헬의 뒷모습을 보고 생각난 게 있었다." id c04_w_0112
    
    "가헬에게 줘야 할 아티팩트를 아직 전달하지 않았다." id c04_w_0113
    
    "[pl_name][josa_eun_neun] 가헬을 따라서 창고로 들어갔다." id c04_w_0114

    scene bg warehouse  with Fade(0.8, 0.8, 0.8)
    
    show wolf am_u
    with dissolve

    "[pl_name][josa_i_ga] 창고에 오자마자 가헬은 손을 털고 말했다." id c04_w_0115

    show wolf talk
    with dissolve
    
    w "\"[pl_name], 창고 청소를 좀 해야 할 것 같다.\"" id c04_w_0116

    show wolf base am_d
    with dissolve

    c question2 "\"어? 최근에 정리했는데.\"" id c04_w_0117

    show wolf at mirror
    with dissolve
    pause(0.5)
    show wolf at mirror2
    with dissolve
    
    "가헬은 창고 내부를 슥 둘러보고는 다시 말했다." id c04_w_0118

    show wolf talk am_u
    with dissolve

    w "\"아무래도 \'청소\'는 안 한 것 같은데.\"" id c04_w_0119

    show wolf base am_d
    with dissolve

    c ddam2 "\"앗, 그건 그렇지...\"" id c04_w_0120

    "[pl_name][josa_eun_neun] 당황해서 우물쭈물하다가 일단 금고부터 열기로 했다." id c04_w_0121

    c talk "\"청소는 나중에 할 테니까, 잠깐만...\"" id c04_w_0122

    "금고를 열자 보이는 번쩍이는 금화들이 [pl_name]에게 흐뭇한 미소를 선사한다." id c04_w_0123
    
    show ring_red :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "가장 위에는 류호가 만든 아티팩트 반지가 놓여있다." id c04_w_0124
    
    "[pl_name][josa_eun_neun] 순간 다른 생각이 떠올랐다." id c04_w_0125

    c base "(스승님이 만든 아티팩트니까 값어치는 보통이 아닐 텐데.)" id c04_w_0126
    
    c question2 "(못해도 계약금의 3배는 되지 않을까?)" id c04_w_0127
    
    c consider "(차라리 팔고 계약금을 더 얹어주는 게 서로 이득일지도...)" id c04_w_0128
    
    hide ring_red
    with dissolve

    "[pl_name]의 머릿속에서 저울이 움직인다." id c04_w_0129
    
    "계약을 온전히 지키는 것과 이익을 챙기는 것 사이에서 [pl_name][josa_eun_neun] 갈등했다." id c04_w_0130
    
    menu :
        "가헬에게 아티팩트를 준다." :

            # 마법방어아티팩트 변수 획득
            $ magicitem = 1
            
            "개인의 양심이 이겼다. [pl_name][josa_eun_neun] 금화 위에 있는 반지를 꺼냈다." id c04_w_0131
            
            "[pl_name][josa_eun_neun] 어리둥절한 표정의 가헬에게 말했다." id c04_w_0132

            c talk "\"손 내밀어봐.\"" id c04_w_0133

            show wolf base am_u
            with dissolve

            show ring_red :
                xcenter 0.5
                ycenter 0.5
            with dissolve
            
            "얌전히 손을 내민 가헬의 손바닥 위로 반지가 떨어졌다." id c04_w_0134
            
            hide ring_red
            with dissolve

            play sound "effect/ping.mp3" volume 0.75
            show exclamation at exclamation_move (1050, 40)
            show wolf bigeye at surprise_move

            "가헬은 순간적으로 깜짝 놀랐다." id c04_w_0135
            
            "[pl_name]에게 반지를 주면서 고백할까 하는 망상을 했었던 탓에 다른 의미로 생각할 뻔했다." id c04_w_0136

            c "\"약속했던 아티팩트야. 조금 더 고급이 되어버렸지만...\"" id c04_w_0137

            hide exclamation
            show wolf talk
            with dissolve

            w "\"아아... 고맙다. 가치를 감정받아서 차액을-\"" id c04_w_0138

            c smile "\"차액은 됐어. 늦은 만큼 이자가 붙은 걸로 생각해.\"" id c04_w_0139

            show wolf shy am_d
            with dissolve

            "가헬은 아티팩트를 손에 끼고 싶은 욕구를 참고 주머니에 넣었다." id c04_w_0140

            c talk "\"사실 이 아티팩트, 스승님이 만든 거야.\"" id c04_w_0141
            
            show wolf talk
            with dissolve

            w "\"네 스승님?\"" id c04_w_0142
            
            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 고개를 끄덕였다." id c04_w_0143
            
            $ unlock_info_tag(2, "7")
            $ display_text = _("정보 : 마법 보호막")
            show screen affection_indicator

            c "\"응. 실험해 보진 않았지만, {color=#ee3939}'마법 보호막'{/color} 효과가 있을 거야.\"" id c04_w_0144
            
            show wolf talk am_u
            with dissolve

            w "\"보통 아티팩트가 아니군... 잘 쓰도록 하겠다.\"" id c04_w_0145
            
            show wolf base am_d
            with dissolve

            c "\"아, 직접 쓰게? 하긴 용병이니 위험한 일도 많겠지.\"" id c04_w_0146

            "전속 계약이 끝나더라도 가헬의 용병 생활에 도움이 될 것이다." id c04_w_0147
            
            "[pl_name][josa_eun_neun] 내심 뿌듯함을 느꼈다." id c04_w_0148

                    
        "가헬에게 금화를 준다." :

            "상인의 금전욕이 이겼다. [pl_name][josa_eun_neun] 반지를 슬쩍 안으로 밀어 넣고 금화를 꺼냈다." id c04_w_0149
            
            "[pl_name][josa_eun_neun] 어리둥절한 표정의 가헬에게 말했다." id c04_w_0150

            c talk "\"약속했던 아티팩트...를 못 구해서 말이야.\"" id c04_w_0151
            
            c "\"대신이라고 하기 뭐 하지만 추가금을 얹어서 줄게.\"" id c04_w_0152

            show wolf talk am_u
            with dissolve

            w "\"아아... 알았다. 고맙게 받지.\"" id c04_w_0153

            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 가헬에게 묵직한 금화 주머니를 건넸다. 꽤 많은 금액이지만 전혀 아깝지 않았다." id c04_w_0154

            c "\"아티팩트를 주기로 했는데 못 지켜서 미안해.\"" id c04_w_0155

            "[pl_name][josa_eun_neun] 뻔뻔하게 표정 하나 바꾸지 않고 거짓말을 했다." id c04_w_0156
            
            "오히려 가헬이 미안한 표정으로 말했다." id c04_w_0157
            
            show wolf sad3_am am_d
            with dissolve

            w "\"아니다. 괜히 번거롭게 했군.\"" id c04_w_0158

            "[pl_name][josa_eun_neun] 양심의 가책을 느끼기 시작했지만 웃으며 대답했다." id c04_w_0159

            c laugh "\"가헬 덕분에 가게도 잘 되는걸.\"" id c04_w_0160
            
            show wolf smile
            with dissolve

            "아무것도 모르는 가헬은 그저 미소로 대답할 뿐이었다." id c04_w_0161
        
    # 가게 저녁으로 배경전환
    scene bg shop2 with Fade(0.8, 0.8, 0.8)

    "노을빛이 따스하게 가게 안을 채우는 시간이 되자 [pl_name][josa_eun_neun] 영업을 마칠 준비를 했다." id c04_w_0162
    
    "오전에 푹 자버린 탓인지 모르겠지만, 오늘 수익은 약간 아쉬웠다." id c04_w_0163

    show wolf talk
    with dissolve

    w "\"정리 중인가?\"" id c04_w_0164

    show wolf base
    with dissolve

    c talk "\"응, 거의 다 했어.\"" id c04_w_0165

    "가헬은 조금 머뭇거리다가 말을 꺼냈다." id c04_w_0166

    show wolf talk am_u
    with dissolve

    w "\"내일... 일이 끝나면 술집에 같이 갔으면 한다.\"" id c04_w_0167

    show wolf base am_d
    with dissolve

    c base "(아 맞다. 며칠 전에 얘기했었지...)" id c04_w_0168

    c "그때는 대충 둘러대면서 \'다음에 꼭 가자\'고 했던 게 기억났다." id c04_w_0169
    
    c "술은 별로 즐기지 않는 편이지만 이번에는 거절할 수 없을 것 같다." id c04_w_0170

    c talk "\"그, 그래...\"" id c04_w_0171

    "선전포고에 가까운 가헬의 말에 [pl_name][josa_eun_neun] 고개를 끄덕일 수밖에 없었다." id c04_w_0172

    c "\"일단 오늘 저녁은 스튜로 할까? 많이 끓여두고 내일도 먹게...\"" id c04_w_0173

    show wolf talk am_u
    with dissolve

    w "\"알았다.\"" id c04_w_0174

    hide wolf
    with dissolve

    "[pl_name][josa_eun_neun] 따끈한 스튜와 함께 평온한 하루를 마무리했다." id c04_w_0175

    c consider "최근 들어 자꾸 요란한 날과 평범한 날이 교차하는 기분인데..." id c04_w_0176
    
    c "설마 내일은 요란한 날이 되려나? 술집, 왠지 걱정되네..." id c04_w_0177

    stop music fadeout 2.5

label c4w_guild:
    #[길거리 배경]
    
    scene bg street with Fade(0.8, 0.8, 0.8)
    play music "audio/chill-abstract-intention-12099.mp3" volume 0.7 fadein 2.5

    "{i}다음 날 아침{/i}" id c04_w_0178

    "가헬은 이른 아침부터 용병 길드로 걸어갔다." id c04_w_0179
    
    "가헬은 전에 던전에서 마력 폭주를 일으킨 뒤로 개인적인 조사를 하고 있었다." id c04_w_0180
    
    "사실 가헬이 마력 폭주를 겪은 것은 이번이 처음이 아니었다." id c04_w_0181
    
    "가헬은 자신을 망령처럼 따라다니는 이 증상을 해결하고 싶었다." id c04_w_0182
    
    "용병으로서도 위험 요소지만, [pl_name][josa_wa_gwa] 함께하는 지금은 더욱 위험했다." id c04_w_0183

    w sad_am "(이대로는 호위 실격이다.)" id c04_w_0184

    "'마력 폭주'는 마법 사용이 미숙하거나 무리해서 사용할 때 나타나는 것으로 알려져 있다." id c04_w_0185
    
    "처음에는 가헬도 같은 이유인 줄 알았다." id c04_w_0186
    
    "그러나 마력 폭주가 반복될수록 이상한 점이 생겼다." id c04_w_0187
    
    "최근 던전에서처럼, 알 수 없는 이유로 마력 폭주를 일으키게 된 것이다." id c04_w_0188
    
    "가헬은 다양한 원인을 찾다가 최근에 한 가지 단서를 잡았다." id c04_w_0189

    "그것은 가헬이 받은 '시술'이었다." id c04_w_0190

    w sad2_am "(수상한 시술을 받는 게 아니었는데...)" id c04_w_0191

    "가헬은 자기 허벅지 위를 보고 작게 한숨을 쉬었다." id c04_w_0192

    "{color=#ee3939}'트로나'{/color} 왕국의 용병이라면 과반수는 시술을 받았을 것이다." id c04_w_0193
    
    "가헬이 받은 시술도 평범한 근육 강화인 줄 알았다." id c04_w_0194
    
    "하지만 지금은 이게 마력 폭주의 가장 유력한 원인이다." id c04_w_0195
    
    "가헬은 비슷한 사례가 있는지 조사하기 위해 길드에 의뢰를 넣어놨다." id c04_w_0196
    
    "오늘은 그 결과를 들으러 가는 길이었다." id c04_w_0197

    play sound "effect/footstep.mp3" volume 0.85

    # 용병 길드 배경
    scene bg guild with Fade(0.8, 0.8, 0.8)

    "아침의 용병 길드는 역시나 한산했다." id c04_w_0198
    
    show lucas base
    with dissolve

    "루카스는 길드로 들어오는 가헬을 보고 반사적으로 인사를 했다." id c04_w_0199

    show lucas talk am_u
    with dissolve

    l "\"안녕하십니까, 가헬님...\"" id c04_w_0200

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 80)
    show lucas embarrass2 am_d at surprise_move
    
    l "\"!!...\"" id c04_w_0201

    "가헬을 보고 술집에서 자신의 추태가 기억난 루카스는 얼굴이 붉어졌다." id c04_w_0202

    hide exclamation
    show lucas embarrass am_d
    with dissolve

    l "\"그, 저번에 술집에서는 감사했습니다.\"" id c04_w_0203
    
    show lucas embarrass2 am_d
    with dissolve

    w talk "\"괜찮습니다.\"" id c04_w_0204

    "가헬은 \'그 정도는 별일 아니다.\'라고 말하려다 그만뒀다." id c04_w_0205
    
    "괜히 뭐라고 말할수록 괜히 비꼬는 것처럼 들릴지도 모른다." id c04_w_0206
    
    "가헬은 그냥 주제를 바꾸기로 했다." id c04_w_0207

    w "\"오늘은 조사 의뢰의 결과를 받으러 왔습니다.\"" id c04_w_0208

    show lucas base page_d
    with dissolve

    "루카스는 뒤쪽의 서류 더미를 뒤적거리다가 종이 몇 장을 꺼냈다." id c04_w_0209
    
    "가헬의 의뢰에 대한 보고서였다." id c04_w_0210

    show lucas talk page_u
    with dissolve

    l "\"에헴! 마력 폭주에 대한 조사군요.\"" id c04_w_0211
    
    l "\"최근에 용병이 마력 폭주를 일으킨 사례는 총 4건입니다.\"" id c04_w_0212
    
    l "\"가헬님을 제외한 3건은 모두 용병 등급이 낮았습니다. 신뢰도도 평균 이하군요.\"" id c04_w_0213

    show lucas base page_d
    with dissolve

    "가헬은 보고서 개요를 듣고 생각에 빠졌다." id c04_w_0214
    
    "흔히들 말하는 \'질 나쁜 용병\'의 특징이었다. 그들도 자신과 같은 시술을 받은 것인지 궁금했다." id c04_w_0215

    show lucas talk am_u
    with dissolve

    l "\"자세한 정보는 다음 페이지에 있습니다.\"" id c04_w_0216

    show lucas base am_d
    with dissolve

    w "\"감사합니다. 추가 의뢰가 있을지는 조금 더 자세히 봐야겠군요.\"" id c04_w_0217

    hide lucas
    with dissolve

    "가헬은 루카스가 건넨 문서를 들고 의자에 앉았다." id c04_w_0218
    
    "다른 용병의 사례를 하나씩 읽어봐도 시원하게 해결되는 건 없었다." id c04_w_0219
    
    "하나는 암시장에서 날뛰다가 체포된 사건이었고, 다른 두 개는 분수에 맞지 않는 의뢰에 무리하다가 생긴 사건이었다." id c04_w_0220

    w base "(직접 만나기도 어렵겠군...)" id c04_w_0221

    "세 용병의 주 활동 지역이 서로 제각각이었다." id c04_w_0222
    
    "게다가 가헬 본인 사례로 미루어보건대, 이들도 시술받은 지 몇 년 이상 지났을 것이다." id c04_w_0223
    
    "그래도 이런 용병이 고급 시술을 받았을 것 같지는 않다." id c04_w_0224

    w "(나와 같은 시술을 받았을 가능성이 높다.)" id c04_w_0225

    "가헬은 역시 시술이 원인이라고 판단했다." id c04_w_0226
    
    "확실한 증거는 잡지 못했지만, 앞으로 할 일은 정해졌다." id c04_w_0227
    
    "가장 큰 목표는 시술을 제거하는 것이고, 그러기 위해서 뭘 해야 할지 차분히 생각했다." id c04_w_0228
    
    "우선 자신의 시술이 제거할 수 있는 상태인지 알아봐야 하고, 상태에 따라 해결책을 마련해야 한다." id c04_w_0229
    
    "그리고 폭주를 억제할 수 있는 임시방편도 마련하면 좋을 것이다." id c04_w_0230
    
    "가헬은 자연스럽게 [pl_name][josa_wa_gwa] 상담해 볼지 생각하다가 고개를 저었다." id c04_w_0231
    
    "마력 폭주 때문에 계약을 해지당하면 모든 게 끝이다." id c04_w_0232

    "가헬은 다른 마법적 지식이 있는 사람을 궁리하다가 \'바토\'가 떠올랐다." id c04_w_0233
    
    "[pl_name][josa_wa_gwa] 친해 보이는 데다, 한 번 만나봤으니 가볍게 물어볼 수는 있을 것이다." id c04_w_0234
    
    "술집에서의 대화가 떠오른 가헬은 루카스에게 바토의 연락처를 물어보기로 했다." id c04_w_0235

    show lucas base am_d
    with dissolve

    w talk "\"루카스 씨, 혹시 바토 씨의 연락처를 알 수 있습니까?\"" id c04_w_0236

    show lucas talk page_u
    with dissolve

    l "\"물론이죠. 편지는 여기로 보내시면 됩니다.\"" id c04_w_0237

    show lucas base am_d
    with dissolve

    "루카스는 쪽지에 바토의 연락처를 적어서 건네줬다. 건물 주소뿐만 아니라 암호처럼 숫자가 잔뜩 붙어있었다." id c04_w_0238

    w base "(마탑은 연락처도 길고 복잡하게 쓰는군...)" id c04_w_0239

    w talk "\"감사합니다. 추가의뢰는 나중에 할 것 같습니다.\"" id c04_w_0240
    
    show lucas talk
    with dissolve

    l "\"알겠습니다.\"" id c04_w_0241

    show lucas base
    with dissolve
    
    "가헬은 루카스에게 작별 인사를 남기고 용병 길드에서 나왔다." id c04_w_0242

    # [길거리 배경]
    scene bg street with Fade(0.8, 0.8, 0.8)

    "가헬은 바토에게 만나자는 취지의 전보를 보냈다." id c04_w_0243
    
    "답변을 기다리는 며칠 동안 가헬은 던전에 다시 가볼 생각이었다." id c04_w_0244
    
    "기사단이 토벌을 마쳐서 마물은 거의 없겠지만, 당시 상황을 다시 확인해서 나쁠 건 없다." id c04_w_0245

    w "(아직은 계획뿐이지만...)" id c04_w_0246

    "확실한 건 아무것도 없지만 나름의 진전이 있었다." id c04_w_0247
    
    "오늘만큼은 조금 쉬어도 좋을 것 같다." id c04_w_0248
    
    "[pl_name][josa_wa_gwa] 술집에 갈 생각에 가헬의 기분이 조금 들뜨기 시작했다." id c04_w_0249

    stop music fadeout 2.5

label c4w_tavern:
    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40 

    "{i}그날 저녁{/i}" id c04_w_0250
    
    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] 오늘 하루의 가게 영업을 마무리하고 장부를 작성하고 있었다." id c04_w_0251

    c laugh "\"와, 오늘이 역대 최대 매출이야. 처음 온 손님이 꽤 많네.\"" id c04_w_0252

    c base "평소에는 잘 안 팔리던 연고나 허브 오일까지 꽤 많이 팔았다." id c04_w_0253
    
    c consider "용병이 아닌 것 같은 손님들도 있었다. 앞으로도 이렇게만 팔면 좋을 것 같은데..." id c04_w_0254

    show wolf talk am_u
    with dissolve

    w "\"상품이 부족하진 않은가?\"" id c04_w_0255
    
    play sound "effect/footstep.mp3" volume 0.85
    show wolf base am_d at fwalk

    "바닥 청소를 마친 가헬은 [pl_name]에게 가까이 다가왔다." id c04_w_0256
    
    c talk "\"지금 당장은 괜찮아. 휴일에 연금술 재료를 조금 사면 될 것 같아.\"" id c04_w_0257
    
    "장부 정리를 마친 [pl_name][josa_eun_neun] 오늘 술집에 가기로 한 게 떠올랐다." id c04_w_0258
      
    menu :
        "그냥 모르는 척하자." :
            
            $ c4w_kiss_trigger1 = False
            c consider "(아무 말도 안 하면 그냥 넘어가려나?)" id c04_w_0259
            
            show wolf talk
            with dissolve

            w "\"그럼, 이제 술집에 갈까?\"" id c04_w_0260
            
            show wolf base
            with dissolve
            
            c ddam2 "\"그, 그래...\"" id c04_w_0261
            
            c sigh "(괜한 생각이었네.)" id c04_w_0262
            
            "[pl_name][josa_eun_neun] 묘하게 들뜬 것 같은 가헬과 함께 가게를 정리했다." id c04_w_0263
                
        "술집에 가자고 하자." :

            $ c4w_kiss_trigger1 = True
            c talk "\"일도 끝났고 슬슬 나갈까?\"" id c04_w_0264
            
            show wolf talk
            with dissolve

            w "\"술집에 갈 생각이지?\"" id c04_w_0265

            play sound "effect/sparkle.mp3" volume 0.5
            show wolf sparkle
            with dissolve

            "가헬은 왠지 반짝이는 표정으로 [pl_name][josa_eul_reul] 바라보았다." id c04_w_0266
            
            c "\"으, 응...\"" id c04_w_0267
            
            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 묘하게 들뜬 것 같은 가헬과 함께 가게를 정리했다." id c04_w_0268

    # 술집 밤 배경
    scene bg pub2 with Fade(0.8, 0.8, 0.8)
    play music "medieval-fantasy-142837.mp3" volume 0.5  fadein 2.5

    "[pl_name][josa_eun_neun] 가헬과 함께 술집에 들어섰다." id c04_w_0269
    
    show wolf
    with dissolve

    "저녁 시간대의 술집은 점점 손님이 들어오는지 하나씩 자리가 채워지고 있었다." id c04_w_0270
    
    "떠들썩한 분위기와 굉장히 다양한 냄새가 압도적으로 느껴진다." id c04_w_0271

    c talk "\"손님이 많네...\"" id c04_w_0272

    show wolf talk am_u
    with dissolve

    w "\"밤이 되면 더 많아질 거다.\"" id c04_w_0273

    show wolf base am_d
    with dissolve
    
    c sigh "(그럼 꽉 찬다는 거 아냐? 동네에 수인이 이렇게 많았나?)" id c04_w_0274

    "상상만 했는데 피곤해진 [pl_name][josa_eun_neun] 일단 자리에 앉았다." id c04_w_0275

    show wolf talk am_u
    with dissolve
    
    w "\"식사도 해야 하니 저녁 특선을 주문해야겠군. 연어? 소시지? 덜 기름진 거라면 구운 버섯도 있다.\"" id c04_w_0276

    show wolf base am_d
    with dissolve
    
    c talk "\"으음, 소시지로 할게.\"" id c04_w_0277

    hide wolf
    with dissolve
    
    "가헬은 점원에게 주문하러 일어섰다." id c04_w_0278
    
    "가헬이 아주 잠깐 자리를 비운 사이, 예상치 못한 수인이 [pl_name] 앞에 나타났다." id c04_w_0279

    #엘레드 등장
    show tiger base_am am_d
    with dissolve

    show tiger wink_am am_u
    with dissolve

    t "\"하하! 여기서 다 만나는군. 자네도 한잔하러 왔나?\"" id c04_w_0280

    show tiger base_am am_d
    with dissolve

    "테이블에 마시던 술잔을 내려놓은 엘레드는 자연스럽게 [pl_name]의 곁에 다가왔다." id c04_w_0281
    
    "꽤 독한 술을 마시는지, 자극적인 냄새가 났다." id c04_w_0282

    c ddam2 "\"앗, 네. 근데 오늘은...\"" id c04_w_0283

    show tiger at mirror, right
    with dissolve

    show wolf fight3 at mirror, left
    with dissolve
    play sound "effect/putdown.mp3" volume 0.9
    
    "가헬과 함께 왔다고 얘기하려는 순간, 가헬이 두 사람 사이에 나타나서 에일 두 잔을 테이블 위에 탁 내려놓았다." id c04_w_0284
    
    "가헬은 아무 말 없이 차가운 눈빛으로 엘레드를 바라보았다." id c04_w_0285

    show tiger smile_am 
    with dissolve

    "엘레드는 직감으로 가헬과 [pl_name] 사이에 진전이 없다는 걸 눈치챘다." id c04_w_0286

    show tiger wink_am am_u
    with dissolve

    t "\"흐음... 역시 자네들도 일 끝나고 한잔하는 모양이군?\"" id c04_w_0287

    hide tiger and wolf
    with dissolve
    show wolf base at right
    with dissolve
    show tiger smile_am am_d at left
    with dissolve

    "엘레드는 씨익 웃으며 가헬 반대편으로 자리를 옮겼다." id c04_w_0288
    
    "가헬과 엘레드 사이에 낀 [pl_name][josa_eun_neun] 불길한 예감이 들었다." id c04_w_0289

    c ddam "(익숙한 상황... 오늘도 싸우려나?)" id c04_w_0290

    "[pl_name][josa_eun_neun] 둘 사이를 최대한 떨어뜨려 놓기로 생각하며 말을 꺼냈다." id c04_w_0291

    c talk "\"엘레드님도 술집에 자주 오시나 봐요?\"" id c04_w_0292


    show ddam at ddam_move (320,0)
    show tiger talk_am am_u
    with dissolve

    t "\"하, 하하. 뭐 그런 셈이지.\"" id c04_w_0293

    hide ddam
    show tiger base_am am_d
    with dissolve

    "엘레드는 속으로 당황을 숨기며 대답했다." id c04_w_0294

    $ unlock_info_tag(3, "1")
    $ display_text = _("정보 : 남자 사냥")
    show screen affection_indicator

    "엘레드는 주로 {color=#ee3939}'남자 사냥'{/color}을 하러 술집에 오는 편이다. 적당한 남자를 꾀어서 뜨거운 하룻밤을 보내곤 했다." id c04_w_0295
    
    "오늘도 그런 목적으로 술집에 왔지만, [pl_name][josa_eul_reul] 만날 줄은 몰랐다." id c04_w_0296

    show wolf talk am_u
    with dissolve

    w "\"기사단장님은 다른 귀족들과 고상하게 파티라도 하는 줄 알았는데-\"" id c04_w_0297

    show tiger vangry_am am_u
    with dissolve

    t "\"하! 그런 역겨운 장소에 한 번이라도 가보면 생각이 바뀔걸세.\"" id c04_w_0298
    
    show wolf base am_d
    with dissolve

    t "\"술은커녕 물도 제대로 못 마실 테니.\"" id c04_w_0299

    show tiger angry_am am_d
    with dissolve

    "엘레드는 조금 짜증이 난 듯 술을 쭉 들이켜고는 말을 이었다." id c04_w_0300

    show tiger talk_am am_u
    with dissolve

    t "\"뭐 자네들도 나름대로 힘든 점이 있겠지.\"" id c04_w_0301
    
    t "\"이런 고리타분한 얘기 말고 흥미진진한 얘기를 할까?\"" id c04_w_0302

    show tiger base_am am_d
    with dissolve
    pause(0.2)
    show tiger am_u
    with dissolve
    
    "엘레드는 조그마한 원석 같은 것을 꺼내 들었다." id c04_w_0303
    
    show rainbowstone :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "모양은 꽤 보석같았지만 색이 워낙 난잡해서 뭐라 말하기 힘든 돌조각이었다." id c04_w_0304

    show tiger talk_am
    with dissolve

    t "\"이번에 대대적인 토벌 작전에서 찾은 거라네. 던전 안에서 꽤 여러 개 발견했지.\"" id c04_w_0305
    
    show tiger wink_am
    with dissolve

    t "\"처음엔 그냥 마나 결정 비슷한 것인 줄 알았는데, 내 본능이 중요하다고 하길래 싹 쓸어왔지.\"" id c04_w_0306
    
    show tiger base_am am_d
    with dissolve

    "엘레드가 테이블 위에 올려둔 돌조각은 꽤 작은 편이라 색깔만 아니었으면 그냥 지나쳤을 법했다." id c04_w_0307
    
    "[pl_name]에게는 그냥 이상한 색의 보석처럼 보였다." id c04_w_0308

    #이상한무지개돌 이미지 숨기기
    hide rainbowstone
    with dissolve

    c question2 "\"그럼 위험한 물건일 가능성도 있다는 건가요?\"" id c04_w_0309

    show tiger laugh_am
    with dissolve

    t "\"뭐 그냥 돌인 것 같긴 하네. 하하하! 부수거나 끓이거나 이것저것 해봤지만, 별다른 점은 없었다네. 마력이 들어있지도 않고 말이야.\"" id c04_w_0310

    c "(근데 돌을 대체 어디서 꺼낸 거지?)" id c04_w_0311

    show tiger base_am
    with dissolve
    
    "[pl_name][josa_eun_neun] 저번부터 엘레드의 물건 수납 방법이 신경 쓰였지만, 입 밖으로 꺼내지는 않았다." id c04_w_0312

    show wolf talk am_u
    with dissolve

    w "\"마탑에서 분석하지는 않았습니까?\"" id c04_w_0313

    show wolf base am_d
    show tiger talk_am
    with dissolve

    t "\"흠... 마탑이랑은 굳이 얽히고 싶지 않아서 말이지. 기사단 측에서는 이미 분석이 끝나기도 했고...\"" id c04_w_0314
    
    show tiger base_am
    with dissolve

    "[pl_name][josa_eun_neun] 이전에 엘레드가 말한 귀족과 마탑의 관계가 기억났다." id c04_w_0315
    
    "단순히 사이가 안 좋은 정도를 넘어서 꽤 적극적으로 견제하는 것 같다." id c04_w_0316

    show tiger talk_am am_u
    with dissolve

    t "\"마탑에 맡기면 쓸데없이 비용을 잔뜩 청구할걸세.\"" id c04_w_0317

    show tiger base_am am_d
    with dissolve

    c "\"음, 정말로 그냥 색만 알록달록한 돌인가 봐요?\"" id c04_w_0318

    show tiger sad2_am am_u
    with dissolve

    t "\"흐음... 자네도 그렇게 생각하나? 이번에는 내 본능이 틀렸을지도 모르겠군.\"" id c04_w_0319

    show tiger base_am am_d
    with dissolve

    # 이상한 무지개돌 이미지
    show rainbowstone :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    

    "[pl_name][josa_eun_neun] 이상한 돌조각을 집어 들었다." id c04_w_0320
    
    "색이 심하게 이상할 뿐, 그냥 흔히 볼 수 있는 원석 같았다." id c04_w_0321
    
    "마나를 살짝 흘려 넣어봤지만 엘레드의 말대로 딱히 아무런 반응도 없었다." id c04_w_0322

    # 이미지 숨기기
    hide rainbowstone
    with dissolve

    show tiger talk_am am_u
    with dissolve

    t "\"자네가 조사해 보겠다면 그거 하나는 빌려주겠네.\"" id c04_w_0323
    
    t "\"기사단에서 정식으로 의뢰할 수는 없고, 내 개인적인 부탁이라고 생각해 주게.\"" id c04_w_0324

    show tiger base_am am_d
    with dissolve

    menu :
        "잘 모르겠으니 거절하자." :

            "[pl_name][josa_eun_neun] 돌의 무늬에 집중하다가 속이 울렁거리는 기분이 들었다." id c04_w_0325
            
            "조금 꺼림칙한 느낌이라 조사는 거절하기로 했다." id c04_w_0326

            c talk "\"저도 잘 모르겠네요. 제 능력으로는 부족한 것 같습니다.\"" id c04_w_0327

            show tiger talk_am am_u
            with dissolve
            
            t "\"아쉽군. 뭐, 어쩔 수 없지.\"" id c04_w_0328

            show tiger base_am
            with dissolve

            "엘레드는 [pl_name]에게서 돌조각을 돌려받았다." id c04_w_0329
            
            show tiger am_d
            with dissolve

            "자연스럽게 주머니에 넣는 것처럼 엘레드의 손이 내려간다." id c04_w_0330

            c ddam2 "(진짜 고간에 공간이 있다고?!)" id c04_w_0331

            "[pl_name][josa_eun_neun] 조금 충격적인 진실을 뇌에서 쫓아냈다." id c04_w_0332
            
            "세상에는 모르는 게 나은 것들도 있는 법이다." id c04_w_0333
            
        "정체가 궁금하니 조사해 보자." :

            # 이상한 돌 변수 +1 <있어야 이득
            $ persistent.rainbowstone_wolf = True

            c talk "\"그러면 감사히 받겠습니다. 뭔가 알아낸 게 있으면 꼭 알려드리죠.\"" id c04_w_0334

            "[pl_name][josa_eun_neun] 돌조각을 주머니에 집어넣으려고 했다." id c04_w_0335
            
            "그러나 돌조각은 갑자기 흐물흐물 녹아내렸다." id c04_w_0336

            c question2 "\"어? 이거 왜 이러지?\"" id c04_w_0337

            "얼음이 녹는 것처럼 돌조각은 물처럼 [pl_name]의 팔을 타고 흘러내렸다." id c04_w_0338
            
            "다른 손으로 액체를 닦아내려고 했으나 그마저도 만지는 순간 사라져 버렸다." id c04_w_0339

            c ddam2 "\"엥?\"" id c04_w_0340

            "원래부터 없던 것처럼 흔적도 없이 사라진 돌조각에 [pl_name][josa_eun_neun] 조금 당황했다." id c04_w_0341

            play sound "effect/ping.mp3" volume 0.75
            show exclamation at exclamation_move (1550, 40)
            show exclamation2 at exclamation_move (550, 40)            
            show wolf fight2 am_u
            show tiger fight_am am_u
            with dissolve

            w "\"괜찮나? 몸에 흡수된 것으로 보이는데...\"" id c04_w_0342

            hide exclamation
            hide exclamation2
            with dissolve
            
            w "\"피부가 간지럽지 않나? 이상한 향이 느껴진다거나, 시야가 노랗게 변한다거나?\"" id c04_w_0343

            show wolf fight am_d
            with dissolve
            
            "가헬은 [pl_name]보다 크게 놀란 듯 이것저것 물어봤다." id c04_w_0344

            show wolf fight3 am_d
            with dissolve
            
            "동시에 이 사태의 원인인 엘레드를 매섭게 째려봤다." id c04_w_0345

            show tiger sad2_am am_d
            with dissolve

            "사태의 심각성을 눈치챈 엘레드가 시무룩해졌다." id c04_w_0346

            c talk "\"딱히 이상한 느낌은 없어. 마나 결정처럼 증발한 건가?\"" id c04_w_0347

            "[pl_name][josa_eun_neun] 자기 팔을 앞뒤로 훑어보며 고민했다." id c04_w_0348
            
            "돌이 녹아서 흡수될 정도면 뭔가 원인이 있을 텐데, [pl_name]의 고민은 더욱 깊어졌다." id c04_w_0349

            play sound "audio/effect/sigh.mp3" volume 0.23
            show sigh at mirror, sigh_move2 (-370, -230)
            show tiger sad2_am am_u
            with dissolve

            t "\"내가 괜한 부탁을 했군. 전적으로 내 책임일세. 다른 조각은 주의해서 보관하도록 하지.\"" id c04_w_0350

            play sound "effect/footstep.mp3" volume 0.85
            show tiger base_am at fwalk
            with Dissolve (0.15)

            "엘레드는 갑자기 가까이 다가와서 [pl_name]의 손을 덥석 잡고는 말했다." id c04_w_0351
            
            show tiger talk_am
            with dissolve

            t "\"그리고 조금이라도 이상한 느낌이 들면 반드시 나에게 연락하게. 이렇게 되어서 정말 미안하군.\"" id c04_w_0352

            show tiger base_am
            with dissolve

            "엘레드는 갑자기 진지한 표정으로 [pl_name][josa_eul_reul] 바라봤다." id c04_w_0353
            
            "[pl_name][josa_eun_neun] 엘레드가 전에 가게에 찾아온 날이 생각나서 조금 기분이 이상해졌다." id c04_w_0354

            c ddam2 "\"아, 예...\"" id c04_w_0355
            
            play sound "effect/footstep.mp3" volume 0.85
            show tiger base_am at bwalk
            

            "그때처럼 엘레드가 부담스럽게 느껴져서 [pl_name][josa_eun_neun] 떨떠름한 표정으로 슬쩍 손을 뺐다." id c04_w_0356
            
            show wolf base
            with dissolve

            "가헬의 매서운 시선도 그제야 사라졌다." id c04_w_0357

    
    "꽤 흥미롭지만, 아무런 결론도 나지 않은 대화가 끝났다." id c04_w_0358
    
    "마침 적절한 때에 종업원이 식사를 테이블에 내려놓는다." id c04_w_0359

    "빵, 수프, 샐러드, 그리고 감자와 소시지구이가 차례차례 테이블에 올라왔다." id c04_w_0360
    
    "먹음직스러운 냄새에 [pl_name]의 식욕이 돌아왔다." id c04_w_0361

    show tiger talk_am am_u
    with dissolve

    t "\"이런, 나도 식사를 주문해야겠군.\"" id c04_w_0362
    
    t "\"\'소시지\'도 좋지만, 오늘은 \'미트볼\'이 좋겠어.\"" id c04_w_0363

    "엘레드는 [pl_name][josa_eul_reul] 향해 윙크하며 의미심장한 말을 했다." id c04_w_0364
    
    show tiger wink_am
    with dissolve

    t "\"크고, 두툼하고, 육즙이 가득한 걸로 말일세.\"" id c04_w_0365
    
    hide tiger
    show wolf vangry
    with dissolve

    "가헬의 으르렁거리는 표정을 뒤로하고, 엘레드는 주문하러 가버렸다." id c04_w_0366

    c ddam "(이거 성희롱이지?...)" id c04_w_0367

    "[pl_name][josa_eun_neun] 작게 한숨을 쉬고는 가헬을 달래기로 했다." id c04_w_0368

    c sigh "\"미안해. 제대로 쉬지도 못하고.\"" id c04_w_0369

    show wolf am_u
    with dissolve

    w "\"아니다. 아예 오늘 결판을 내야겠군.\"" id c04_w_0370

    show wolf angry am_d
    with dissolve

    c question2 "\"뭐? 뭘 하려고...\"" id c04_w_0371

    show wolf base
    with dissolve

    "가헬은 대답 없이 전투적으로 빵을 씹었다." id c04_w_0372
    
    "[pl_name]도 걱정을 뒤로하고 일단 식사를 시작했다." id c04_w_0373

    show tiger at left
    with dissolve

    show wine :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "엘레드는 새 술잔과 함께 돌아왔다." id c04_w_0374
    
    "[pl_name]도 고급 와인의 부드러운 향을 느낄 수 있었다." id c04_w_0375

    hide wine
    with dissolve

    c consider "(저건 한 잔에 얼마나 할까?)" id c04_w_0376

    show beer :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "[pl_name][josa_eun_neun] 쓸데없는 상상을 하며 에일을 한 모금 들이켰다." id c04_w_0377
    
    "생각보다 나쁘지 않은 곡물 향이 느껴졌다." id c04_w_0378

    hide beer
    with dissolve

    show tiger talk_am am_u
    with dissolve

    t "\"자네는 술 잘 마시나?\"" id c04_w_0379

    show tiger base_am am_d
    with dissolve

    c talk "\"잘 모르겠네요. 만취한 적은 없고, 에일은 5잔 정도...\"" id c04_w_0380

    "[pl_name][josa_eun_neun] 자신의 한계가 조금 궁금하긴 했다." id c04_w_0381
    
    "하지만 굳이 실험해 볼 생각은 없었다. 만취해서 어떤 추태를 부릴지 걱정되기 때문이었다." id c04_w_0382

    show wolf fight2 am_u
    with dissolve

    w "\"취하게 만들어서 어떻게 해볼 생각이라면 포기하십시오.\"" id c04_w_0383

    show wolf fight am_d
    with dissolve

    "가헬의 날카로운 시선에도 엘레드는 능글거리는 웃음을 거두지 않았다." id c04_w_0384

    show tiger smile_am am_u
    with dissolve

    t "\"글쎄. 가헬 자네는 어떤가? [pl_name][josa_eul_reul] 지킬 수 있을 만큼은 마시겠지?\"" id c04_w_0385

    show tiger am_d
    show wolf vangry am_u
    with dissolve

    w "\"... 그건 대결 신청인가?\"" id c04_w_0386

    "가헬의 말투가 험악해졌다." id c04_w_0387
    
    show tiger base_am
    show wolf angry am_d
    with dissolve

    "두 수인 사이에 불똥이 튀는 것 같은 기분이 들어서, [pl_name][josa_eun_neun] 둘을 중재하려고 했다." id c04_w_0388

    c talk "\"그런 걸로 싸우지 말고...\"" id c04_w_0389

    show tiger laugh_am am_u at surprise_move

    t "\"하하! 저번 승부도 결과가 나지 않았던 것 같다만.\"" id c04_w_0390

    show tiger base_am am_d
    with dissolve

    c ddam "내 말에 끼어드는 엘레드 때문에 골치가 아팠다." id c04_w_0391
    
    c sigh "그곳의 크기로 승부를 보려 하다니, 대체 수인 사회는 뭐가 문제란 말인가." id c04_w_0392

    show wolf vangry am_u
    with dissolve

    w "\"그때도 말했지만, 크기는 나도 지지 않는다.\"" id c04_w_0393

    show wolf angry am_d
    with dissolve

    "가헬의 으르렁거리는 말투에 엘레드는 다른 무기를 꺼냈다." id c04_w_0394

    show tiger smile_am am_u
    with dissolve

    t "\"자신 있어 보이는군. 하지만 {color=#ee3939}\'뒤쪽\'{/color}은 자신 있나?\"" id c04_w_0395

    show tiger base_am am_d
    with dissolve

    c ddam2 "(뒤쪽?!)" id c04_w_0396

    "엘레드는 당황한 표정의 [pl_name][josa_eul_reul] 향해 윙크하며 말했다." id c04_w_0397

    show tiger wink_am am_u
    with dissolve

    t "\"어느 쪽이든 한 번 맛보면 잊을 수 없을걸세.\"" id c04_w_0398

    show tiger base_am am_d
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드의 탐스러운 엉덩이가 눈에 들어왔다." id c04_w_0399
    
    "저런 말을 들으니 엄청나게 신경 쓰이기 시작했다." id c04_w_0400
    
    show wolf vangry at surprise_move
    
    "가헬은 반박하지 못하고 그저 이를 갈았다." id c04_w_0401

    c ddam2 "\"그, 그런 승부는 자제하시죠. 좀 건전하고 정정당당한 스포츠를 하는 게 어떨까요?\"" id c04_w_0402

    "그리고 [pl_name][josa_eun_neun] 곧 자기 말을 후회하게 된다." id c04_w_0403

    stop music fadeout 2.5

    # 술집 배경 2? 아님 그냥 그대로 배경?
    scene bg pub2 with Fade(0.8, 0.8, 0.8)

    "{i}잠시 후{/i}" id c04_w_0404

    "[pl_name][josa_eun_neun] 얼떨떨한 표정으로 두 수인을 바라봤다." id c04_w_0405

    play sound "effect/crowd.mp3" volume 0.85    
    show wolf base inn_d at right
    show tiger base inn_d at left
    with dissolve

    $ unlock_character_image("tiger", "tiger b_no base inn_d")
    $ display_text = _("이미지 : 엘레드(속옷)")
    show screen affection_indicator

    "속옷만 입은 근육질 수인 둘이 가까이 붙어있는 모습을 수많은 인파가 둘러싸고 있었다." id c04_w_0406

    c sigh "(대체 어쩌다 이런 일이 된거야...)" id c04_w_0407

    play music "stomp-117637.mp3" fadein 2.5 volume 0.3

    "가헬과 엘레드는 레슬링으로 결판을 내기로 했다."    
    
    "우승 상품은 없지만, 패배를 용납할 수 없는 두 수인의 결투가 열렸다." id c04_w_0408
    
    "심판을 맡은 [pl_name][josa_eun_neun] 관심이 집중되는 이 상황이 당황스러웠다." id c04_w_0409
    
    "앞뒤 사정을 모르는 관중들은 그저 흥미롭게 둘을 바라보고 있었다." id c04_w_0410

    show wolf talk inn_u
    with dissolve

    w "\"반드시 꺾어주지.\"" id c04_w_0411

    show tiger laugh inn_u
    with dissolve

    t "\"하하! 어디 한번 덤벼보게.\"" id c04_w_0412

    show wolf base inn_d at change(1, 300, 0)
    show tiger base inn_d at change(1, -300, 0)
    with ease
    show wolf base inn_d at change(1, 320, 0)
    show tiger base inn_d at change(1, -320, 0)
    with ease
    show wolf base inn_d at change(1, 280, 0)
    show tiger base inn_d at change(1, -280, 0)
    with ease 

    "[pl_name]의 신호로 경기가 시작됐다. 관중의 기대감으로 술집의 분위기는 뜨겁게 달아오르기 시작했다." id c04_w_0413

    "가헬이 빠르게 엘레드의 팔을 잡고 당겼다." id c04_w_0414

    show wolf hurt at surprise_move

    w "(젠장. 엄청 무겁군.)" id c04_w_0415

    show wolf base
    with dissolve

    "체급의 차이가 있어서 그런지 엘레드를 쉽게 흔들 수는 없었다." id c04_w_0416
    
    "엘레드도 가헬의 힘이 보통은 아니라는 걸 느낄 수 있었다." id c04_w_0417
    
    show tiger at surprise_move

    "엘레드는 가헬을 약간 밀어내려고 힘을 줬다." id c04_w_0418

    show tiger smile
    with dissolve

    t "(허, 이것봐라?)" id c04_w_0419

    "엘레드는 가헬의 팔근육이 눈에 띄게 팽팽해지는 걸 봤다." id c04_w_0420
    
    show tiger base
    with dissolve

    "흔하디흔한 근육 강화지만 효과는 강력했다. 엘레드는 순간 넘어질 뻔 했지만, 곧바로 반격했다." id c04_w_0421

    show wolf hurt
    show tiger fight3
    with vpunch

    w "\"큭!\"" id c04_w_0422

    show wolf fight
    with dissolve

    "엘레드도 근육 강화를 사용하자 힘의 균형이 다시 뒤집혔다." id c04_w_0423
    
    show wolf at change(1, 360, 0)
    show tiger inn_u at change(1, -240, 0)
    with ease
    pause(0.5)
    show wolf inn_u at change(1, 230, 0)
    show tiger inn_d at change(1, -350, 0)
    with ease
    pause(0.5)
    show wolf inn_d at change(1, 280, 0)
    show tiger at change(1, -280, 0)
    with ease

    "가헬은 다리에 힘을 줘서 버티고 있었다. 서로 견제와 방어를 주고받으며 접전을 이어갔다." id c04_w_0424

    c base "(둘 다 근육이 무시무시한데...)" id c04_w_0425

    play sound "effect/crowd2.mp3" volume 0.85

    "관중들은 승부보다 근육 구경에 더 열광하는 것 같았다. 각자 자신이 응원하는 쪽을 외치고 있었다." id c04_w_0426


    menu :
        "가헬을 응원한다." :

            $ wolf_love += 1
            $ tiger_love += -1
            $ display_text = _("가헬, 엘레드 호감도 변화")
            show screen affection_indicator 
            $ cheer_Gahel = True
            
            c talk "\"가헬, 힘내!\"" id c04_w_0427

            show wolf smile
            with dissolve

            "가헬은 [pl_name]의 응원에 시선을 돌리지 않고 미소로만 대답했다." id c04_w_0428
            
            "눈앞의 엘레드를 꺾는 것으로 보답할 생각이었다." id c04_w_0429
            
        "엘레드를 응원한다." :

            $ tiger_love += 1
            $ wolf_love += -1 
            $ display_text = _("가헬, 엘레드 호감도 변화")
            show screen affection_indicator 
            $ cheer_Elred = True
            
            c talk "\"엘레드님, 힘내요!\"" id c04_w_0430

            show tiger wink
            with dissolve

            "엘레드는 [pl_name]의 응원에 시선을 돌려서 윙크했다." id c04_w_0431

            show wolf at surprise_move
            
            "가헬은 그 틈을 노려서 공격했지만, 엘레드는 능숙하게 방어했다." id c04_w_0432

        "조용히 구경한다." :

            "[pl_name][josa_eun_neun] 괜히 둘의 신경을 건드리지 않게 입을 다물었다." id c04_w_0433
            
            "가헬과 엘레드는 오로지 승부에 집중하고 있었다." id c04_w_0434
    
    show wolf fight inn_d
    show tiger fight3 inn_d
    with dissolve

    "가헬의 검붉은 빛 근육과 엘레드의 주황 무늬 근육이 굉장한 기세로 싸우고 있었다." id c04_w_0435

    with vpunch
    pause (0.5)
    with hpunch
    
    "[pl_name][josa_eun_neun] 침을 꿀꺽 삼키고 근육의 격돌을 구경했다." id c04_w_0436
    
    "거의 알몸이나 다름없는 상태로 서로의 몸을 맞대고 있는 두 수인이 헐떡대는 게 조금 엄한 생각을 불러일으켰다." id c04_w_0437
    
    "관객들도 다 비슷한 생각인지 얼굴이 붉어 보였다." id c04_w_0438

    "강하게 부풀어 오른 가헬의 허벅지 근육은 엘레드와 비교해도 작아 보이지 않았다." id c04_w_0439
    
    "땀에 젖어서 오늘따라 섹시하게 반짝였다. 근육이 꿈틀거리는 게 눈에 보일 정도였다." id c04_w_0440

    c shy "(만져봤을 땐 엄청 단단했지...)" id c04_w_0441

    "[pl_name][josa_eun_neun] 조금 야한 상상을 했다가 얼굴이 빨개졌다." id c04_w_0442

    "엘레드 쪽도 만만치 않았다." id c04_w_0443
    
    "엘레드의 이두근은 핏줄까지 솟아서 위압감이 엄청났다." id c04_w_0444
    
    "그리고 엘레드의 엉덩이는 굉장히 탱탱해 보였다." id c04_w_0445
    
    "[pl_name][josa_eun_neun] 저 엉덩이를 손으로 주무르면 어떤 느낌일지 상상했다." id c04_w_0446
    
    "조금 전에 엘레드의 발언이 자꾸만 생각났다." id c04_w_0447

    c horny "(잊을 수 없는 맛이라니...)" id c04_w_0448

    "[pl_name]도 다른 관객들처럼 승부보다 근육에 집중했다." id c04_w_0449
    
    "좋은 구경거리라는 것을 인정할 수밖에 없었다." id c04_w_0450
    
    show tiger fight2
    with dissolve
    
    t "\"언제까지 미적지근하게 굴 셈인가?\"" id c04_w_0451

    show tiger fight3
    with dissolve
    
    "엘레드는 가헬만 들릴 정도로 작게 얘기했다." id c04_w_0452
    
    "레슬링 시합에 대한 얘기지만, [pl_name][josa_wa_gwa]의 관계에 대한 도발이기도 했다." id c04_w_0453
    
    "가헬은 땀을 뻘뻘 흘리면서도 반격의 기회를 노렸다." id c04_w_0454

    show wolf fight2
    with dissolve
    
    w "\"쓸데없이 엉덩이가 가볍군.\"" id c04_w_0455

    show wolf fight at surprise_move

    "가헬은 재빠르게 손을 움직여 엘레드의 힘을 옆으로 흘려냈다." id c04_w_0456
    
    "엘레드가 살짝 휘청대는 틈을 놓치지 않고 그대로 허리를 밀어 넘어트리려고 했다." id c04_w_0457

    show tiger fight3 at surprise_move
    
    "그러나 엘레드도 순순히 당해줄 생각은 없었다. 엘레드는 가헬의 팔을 잡아당겼다." id c04_w_0458

    
    play sound "audio/effect/crash2.mp3" volume 0.4
    pause (0.35)
    hide wolf
    hide tiger
    with vpunch
    pause (0.2)
    with hpunch

    "{i}우당탕!!{/i}" id c04_w_0459

    c ddam2 "\"앗!\"" id c04_w_0460

    play sound "audio/effect/body_drop.mp3"  volume 0.8
    with vpunch

    "둘의 거대한 육체가 거의 동시에 바닥으로 쓰러졌다." id c04_w_0461

    if cheer_Elred == True :
            
        "그러나 엘레드가 조금 더 빨랐다. 가헬의 어깨가 먼저 바닥에 닿았다." id c04_w_0462
        
        show wolf base inn_d at right
        show tiger base inn_d at left
        with dissolve

        stop music fadeout 2.5

        c talk "\"승자는, 엘레드!\"" id c04_w_0463

        play sound "effect/crowd3.mp3" volume 0.85
        show tiger laugh at surprise_move

        "관중들의 환호성 속에서 엘레드는 호탕하게 웃었다." id c04_w_0464
        
        show wolf sad
        with dissolve

        "가헬의 귀는 축 처졌다." id c04_w_0465

        show tiger talk
        with dissolve

        t "\"그래도 만만치 않은 상대였네.\"" id c04_w_0466
    else :
   
        "그러나 가헬이 조금 더 빨랐다. 엘레드의 등이 먼저 바닥에 닿았다." id c04_w_0467
        
        show wolf base inn_d at right
        show tiger base inn_d at left
        with dissolve

        stop music fadeout 2.5
        
        c talk "\"승자는, 가헬!\"" id c04_w_0468

        play sound "effect/crowd3.mp3" volume 0.85
        show wolf wink
        with dissolve

        "관중들의 환호성 속에서 가헬은 [pl_name]에게 윙크했다." id c04_w_0469

        play channel1 "audio/effect/sigh.mp3" volume 0.23
        show sigh at mirror, sigh_move2 (-370, -230)
        show tiger sad2
        with dissolve

        "엘레드는 조금 아쉬웠는지 한숨을 쉬었다." id c04_w_0470

        show wolf talk
        with dissolve

        w "\"힘은 몰라도 기회를 잡는 실력은 내가 이긴 것 같군.\"" id c04_w_0471
    
    scene bg pub with Fade(0.8, 0.8, 0.8)
    play music "medieval-fantasy-142837.mp3" volume 0.5  fadein 2.5

    "{i}잠시 후{/i}" id c04_w_0472

    show wolf base am_d at right
    show tiger base_am am_d at left
    with dissolve
    "평소의 복장으로 돌아온 가헬과 엘레드는 점원이 가져온 시원한 술을 들이켰다." id c04_w_0473
    
    "둘의 승부 덕분에 손님들의 주문이 늘었다는 감사의 표시였다." id c04_w_0474

    show tiger wink_am
    with dissolve

    t "\"하하, 땀 흘리고 난 뒤에 마시니 좋군. 가헬 자네도 꽤 맘에 들었어.\"" id c04_w_0475

    show tiger base_am
    with dissolve

    w "\"......\"" id c04_w_0476
    
    show wolf talk
    with dissolve

    w "\"감사합니다.\"" id c04_w_0477

    show wolf base
    with dissolve

    "엘레드는 또 가헬에게 일방적으로 친한 척을 했으나, 가헬의 표정은 떨떠름했다." id c04_w_0478
    
    "[pl_name][josa_eun_neun] 둘의 관계가 좋아진 건지 나빠진 건지 헷갈렸다." id c04_w_0479

    c consider "(아무튼 서로 주먹질은 안 했으니 다행인가?)" id c04_w_0480

    show tiger talk_am am_u
    with dissolve

    t "\"흠, 벌써 시간이 이렇게 됐군. 아쉽지만 오늘은 먼저 가보도록 하겠네.\"" id c04_w_0481

    show tiger base_am am_d
    with dissolve

    "엘레드는 원래 계획을 취소하고 돌아가기로 했다." id c04_w_0482
    
    "예상치 못한 일로 늦어지기도 했고, 아무리 엘레드라도 [pl_name][josa_i_ga] 보는 앞에서 대놓고 \'남자 사냥\'을 할 수는 없었다." id c04_w_0483

    show tiger talk_am am_u
    with dissolve

    t "\"그럼, 다음에 또 보게나.\"" id c04_w_0484
    
    show tiger base_am am_d at mirror
    with dissolve
    pause(0.5)
    show tiger at walk (-1500, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.85

    c talk "\"안녕히 가십시오, 엘레드님.\"" id c04_w_0485

    "[pl_name][josa_eun_neun] 엘레드에게 인사하고 나서 의자에 늘어졌다." id c04_w_0486
    
    "예상하던 것보다도 엄청 정신없는 하루였다." id c04_w_0487
    
    show wolf talk am_u
    with dissolve

    w "\"피곤하면 슬슬 돌아갈까?\"" id c04_w_0488

    show wolf base am_d
    with dissolve

    c "\"그래... 잠깐, 이거 좀 먹고.\"" id c04_w_0489

    "긴장이 풀린 [pl_name][josa_eun_neun] 남은 수프를 쭉 들이켰다." id c04_w_0490
    
    "왜 다른 손님들의 주문이 늘었는지 이해할 수 있었다." id c04_w_0491

    if cheer_Gahel == True :

        show wolf vhappy am_u
        with dissolve

        w "\"그래도 오늘 함께 술집에 와서 좋았다.\"" id c04_w_0492
    
    else :

        show wolf talk am_u
        with dissolve

        w "\"... 그래도 오늘 함께 술집에 와서 좋았다.\"" id c04_w_0493

        show wolf base am_d
        with dissolve

    c laugh "\"맞아. 재밌었어. 생각하던 거랑 다르지만...\"" id c04_w_0494

    "[pl_name][josa_eun_neun] 작게 하품하며 자리에서 일어났다." id c04_w_0495

    stop music fadeout 2.5

label c4w_kiss:

    # 길거리 밤 배경
    scene bg street3 with Fade(0.8, 0.8, 0.8)
    play music "i-think-about-159746.mp3" volume 0.6 fadein 2.5

    "술집에서의 한바탕 소동이 끝난 후, [pl_name][josa_wa_gwa] 가헬은 길거리로 나왔다." id c04_w_0496
    
    show wolf base am_d
    with dissolve

    "해가 완전히 저물었지만, 길거리는 밤치고는 꽤 밝은 편이었다." id c04_w_0497
    
    "밝은 달빛이 길가를 환하게 비추고, 여기저기서 작은 불빛이 새어 나오고 있었다." id c04_w_0498

    c consider "(뒷골목이 아니라서 그런가?)" id c04_w_0499

    "술집에 올 때는 몰랐는데, 상점에서 왔던 길은 조금 어둑해 보였다." id c04_w_0500
    
    "[pl_name][josa_eun_neun] 어느 쪽 길로 갈지 조금 둘러봤다." id c04_w_0501
    
    "조금 더 걷더라도 밝은 큰길로 갈지, 그냥 왔던 길을 다시 돌아갈지 고민했다." id c04_w_0502

    menu :
        "밝은 데로 가자." :
            $ c4w_kiss_trigger2 = True
            c talk "\"이쪽으로 가자.\"" id c04_w_0503
            
            show wolf talk am_u
            with dissolve

            w "\"아래쪽 광장을 지나가면, 약간 돌아서 가게 될텐데?\"" id c04_w_0504
            
            show wolf base am_d
            with dissolve

            c "\"조금 더 걷지 뭐.\"" id c04_w_0505

            "[pl_name][josa_eun_neun] 대수롭지 않게 말했다. 밤의 길거리는 조심해서 나쁠 것 없었다." id c04_w_0506

            show wolf happy am_d
            with dissolve

            w "([pl_name][josa_wa_gwa] 함께 걷는 것도 좋지...)" id c04_w_0507

            "가헬은 행복한 생각을 하며 [pl_name][josa_eul_reul] 따라갔다." id c04_w_0508
            
        "가까운 데로 가자." :
            c talk "\"이쪽으로 가자.\"" id c04_w_0509

            show wolf base am_d
            with dissolve

            w "\"알았다.\"" id c04_w_0510

            show wolf base am_d
            with dissolve

            c "\"조금 어둡긴 해도 별일 없을거야.\"" id c04_w_0511

            "[pl_name][josa_eun_neun] 대수롭지 않게 말했다. 그저 빨리 가게로 돌아가고 싶었다." id c04_w_0512

    show wolf at walk (-1500, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.85
    pause(0.5)

    scene bg street3 with Fade(0.8, 0.8, 0.8)
    show wolf base
    with dissolve

    "술집에서 멀어질수록 사람들의 떠들썩한 목소리도 멀어져간다." id c04_w_0513
    
    "풀벌레 우는 소리와 발걸음 소리만이 조용하게 길거리를 채우고 있었다." id c04_w_0514

    with hpunch
    
    "[pl_name][josa_eun_neun] 서늘한 밤공기에 살짝 몸을 떨었다."    

    c sigh "\"으, 낮에는 따뜻했는데.\"" id c04_w_0515

    show wolf talk am_u
    with dissolve

    w "\"추운가? 망토라도 가져올 걸 그랬군.\"" id c04_w_0516

    show wolf base am_d
    with dissolve

    "정말로 아쉬워하는 가헬 때문에 [pl_name][josa_eun_neun] 손사래를 쳤다." id c04_w_0517

    c talk "\"아, 아냐. 이 정도는 참을 만해. 나보다 가헬이 더 추울 것 같은데?\"" id c04_w_0518

    "객관적으로 봐도 가헬과 [pl_name]의 복장 차이는 극명했다." id c04_w_0519
    
    "[pl_name][josa_eun_neun] 오히려 자기 겉옷을 벗어줄지 잠깐 고민했다." id c04_w_0520

    show wolf talk am_u
    with dissolve

    w "\"나는 안 춥다.\"" id c04_w_0521

    show wolf base
    with dissolve

    c question2 "\"그럼 다행이고. 응?\"" id c04_w_0522

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at fwalk2

    "가헬은 가까이 다가오더니 [pl_name]의 어깨에 팔을 걸쳤다." id c04_w_0523
    
    "어깨동무보다는 끌어안은 것에 가깝지만, 가헬은 짐짓 아무렇지도 않은 척했다." id c04_w_0524

    c base "(가헬... 팔 근육도 엄청나네.)" id c04_w_0525

    c "눈으로는 많이 봤지만, 이렇게 촉감으로 가헬의 근육을 느낀 적은 별로 없었다." id c04_w_0526
    
    c consider "던전에서 돌아온 가헬을 치료할 때 정도?" id c04_w_0527
    
    c base "그때도 느꼈지만 가헬의 근육은 굉장히 단단하면서 쫄깃한 느낌이 있다." id c04_w_0528
    
    c "쫄깃하다는 표현이 적절한지 모르겠지만, 아무튼 만지는 느낌이 좋았다." id c04_w_0529

    "[pl_name][josa_i_ga] 가헬의 근육에 대해 생각하는 동안, 가헬은 엄청나게 긴장하고 있었다." id c04_w_0530

    show wolf shy3
    with dissolve

    w "(이렇게라도 조금 더 가까이...)" id c04_w_0531

    show wolf shy2
    with dissolve

    "가헬은 희미하게 느껴지는 [pl_name]의 체향에 집중했다." id c04_w_0532
    
    "[pl_name]에게 들키지 않을까 걱정 될 정도로 심장이 쿵쿵 뛰었다." id c04_w_0533
    
    "[pl_name]의 걷는 속도에 맞추느라 가헬의 걸음걸이는 삐걱거렸다." id c04_w_0534
    
    "[pl_name][josa_eul_reul] 보고 있지 않아도 모든 신경이 [pl_name]에게 쏠려있었다." id c04_w_0535
    
    "가헬의 손은 [pl_name]의 가슴 앞 허공에서 갈 곳을 잃고 방황했다." id c04_w_0536

    c talk "\"저기...\"" id c04_w_0537

    show wolf talk am_d
    with vpunch

    w "\"ㅇ, 왜?\"" id c04_w_0538

    show wolf base
    with dissolve

    "가헬은 하마터면 혀를 씹을 뻔했지만, [pl_name][josa_eun_neun] 아무것도 모른 채 말했다." id c04_w_0539

    c question2 "\"가헬은 엘레드가 싫어?\"" id c04_w_0540

    "가헬은 우뚝 멈춰 섰다." id c04_w_0541
    
    "[pl_name]의 의도를 알 수 없어서 뭐라고 대답해야 할지 고민했다." id c04_w_0542
    
    "덩달아 길에서 멈춰 선 [pl_name]도 가헬의 망설임을 느꼈는지 다시 말했다." id c04_w_0543

    c talk "\"서로 진심으로 싸우고 싶어 한다거나 그런 게 아니라는 건 알고 있지만...\"" id c04_w_0544
    
    c "\"사실 저번에 엘레드가 가게에 오고 나서, 가헬의 상태가 조금 신경 쓰였거든.\"" id c04_w_0545
    
    c consider "\"그리고 오늘도 티격태격 하는 게 조금... 엘레드랑 뭔가 있나 싶어서 말이야.\"" id c04_w_0546

    with vpunch

    "가헬은 침을 꿀꺽 삼켰다." id c04_w_0547
    
    "본능적으로 지금이 중요한 순간이라는 걸 알 수 있었다. 바짝 긴장한 가헬은 말을 더듬었다." id c04_w_0548

    show wolf talk
    with dissolve

    w "\"그건, 그러니까...\"" id c04_w_0549

    show wolf base am_u at change(1.59, 0, 275)
    with dissolve

label wolf_cg2_start :

    scene bg street3
    show wolf base am_u at change(1.59, 0, 275)

    "가헬은 큰 결심을 하고 [pl_name]의 양어깨를 붙잡았다." id c04_w_0550
    
    "서로의 눈이 서로를 바라보는 순간이었다." id c04_w_0551
    
    show wolf talk 
    with dissolve

    w "\"나는, 엘레드보다 네가 더 중요하다. 오직 너 때문에 엘레드와 싸운 것뿐이다.\"" id c04_w_0552

    show wolf base
    with dissolve

    "예상하지 못한 대답에 [pl_name][josa_eun_neun] 조금 당황했다." id c04_w_0553

    with vpunch

    c talk "\"뭐? 왜?\"" id c04_w_0554

    if c4w_kiss_trigger1 == True and cheer_Gahel == True and c4w_kiss_trigger2 == True and wolf_love >= 4 : 
        jump c4w_see
   
    else :
            
        "가헬은 침을 꿀꺽 삼키고 입을 열었다. 심장이 입 밖으로 튀어나올 것 같은 기분이었다." id c04_w_0555

        show wolf shy2
        with dissolve

        w "\"나도, 너와 사귀고 싶으니까...\"" id c04_w_0556
        
        show wolf shy3
        with dissolve

        "가헬은 부끄러움에 시선을 돌렸다." id c04_w_0557
        
        "[pl_name][josa_eun_neun] 뒤늦게 놀란 표정을 지었다." id c04_w_0558

        c ddam2 "\"나랑?!\"" id c04_w_0559

        c ddam "나는 혼란스러웠다. 약간 수줍어하는 가헬이 낯설게 느껴졌다." id c04_w_0560
        
        c consider "가헬도 엘레드처럼 내 진심이 궁금했을까? 뭐라고 말해줘야 할지 고민했다." id c04_w_0561

        c ddam2 "\"그, 그랬구나... 고마...워?\"" id c04_w_0562

        show wolf sad_am
        with dissolve

        "[pl_name][josa_eun_neun] 자신의 말을 즉시 후회했다." id c04_w_0563
        
        "기대하던 대답이 아니었는지 가헬의 표정이 썩 밝아 보이지 않았다." id c04_w_0564

        c talk "\"거절하려는 건 아니야. 약간... 갑작스러워서.\"" id c04_w_0565

        "가헬은 우물쭈물하다가 대답했다." id c04_w_0566

        show wolf sad2_am
        with dissolve

        w "\"... 기다릴 수 있다.\"" id c04_w_0567

        show wolf sad_am
        with dissolve

        "가헬은 이미 오랜 시간을 기다려왔다." id c04_w_0568
        
        "[pl_name][josa_eun_neun] 가헬의 말에 고개를 저었다." id c04_w_0569

        c wink "\"오늘부터 \'연인\' 하면 되지.\"" id c04_w_0570

        show wolf happy
        with vpunch

        w "\"!!...\"" id c04_w_0571

        show wolf shy3
        with dissolve

        w "\"그래.\"" id c04_w_0572

        "가헬은 새삼 부끄러운지 [pl_name][josa_eul_reul] 제대로 바라보지 못하고 대답했다." id c04_w_0573

        c talk "\"일단 가게로 돌아가자.\"" id c04_w_0574

        hide wolf
        with dissolve

        "서로 아무 말도 하지 않았지만 자연스럽게 손을 잡았다." id c04_w_0575
        
        "가헬과 [pl_name][josa_eun_neun] 밤의 길거리를 함께 걸었다." id c04_w_0576
    
        jump c4w_end

   
label c4w_see:
    
    $ persistent.wolf_unlocked[1]= True
    show wolf base am_u at change(1.68, 0, 325)
    with dissolve

    "가헬은 [pl_name]에게 조금 더 다가섰다." id c04_w_0577
    
    "한 손으로 팔을 감싸고 다른 손을 목덜미에 올리며 거의 맞닿을 정도로 가까워졌다." id c04_w_0578
    
    show wolf shy4
    with dissolve

    w "\"너를 좋아하니까. 너를, 사랑하니까.\"" id c04_w_0579

    show wolf shy
    with dissolve

    c ddam2 "나는 말문이 막혔다. 그 어느 때보다 진지하게 말하는 가헬이 낯설게 느껴졌다." id c04_w_0580
    
    c ddam "뭐라고 대답할지 전혀 생각이 나지 않았다." id c04_w_0581
    
    c base "서로의 호흡이 느껴질 정도로 가까워서 기분도 이상했다." id c04_w_0582
    
    c "머리가 텅 빈 것 같기도 하고, 너무 꽉 찬 것 같기도 하고..." id c04_w_0583

    show wolf shy2
    with dissolve

    w "\"처음 봤을 때부터, 계속, 계속...\"" id c04_w_0584

    c talk "\"처음부터? 그렇게까지...\"" id c04_w_0585

    "가헬과 [pl_name]의 \'처음\'은 서로 다른 때를 가리키고 있지만, 누구도 눈치채지 못했다." id c04_w_0586
    
    "[pl_name][josa_eun_neun] 가헬의 눈동자 속에 자신의 얼굴이 보일 정도로 가깝다는 걸 알아챘다." id c04_w_0587

    show wolf shy5
    with dissolve

    w "\"그래서 너와 연애하고 싶었다.\"" id c04_w_0588
    
    w "\"다른 연인들처럼, 진심으로 사랑하는 사이가 되고 싶었는데...\"" id c04_w_0589
    
    show wolf sad2_am
    with dissolve

    w "\"전혀 눈치채지 못하더군.\"" id c04_w_0590

    show wolf sad3_am
    with dissolve

    c ddam2 "\"그, 그랬구나... 미안해.\"" id c04_w_0591

    "[pl_name][josa_eun_neun] 자신이 왜 사과하는지도 모른 채 횡설수설했다." id c04_w_0592

    c talk "\"어쩐지 엘레드랑 으르렁거리던게...\"" id c04_w_0593

    show wolf angry
    with dissolve

    "가헬은 눈에서 불꽃이 튈 기세로 [pl_name][josa_eul_reul] 바라보았다." id c04_w_0594

    show wolf talk
    with dissolve

    w "\"그 남자 얘기는 그만하자.\"" id c04_w_0595

    show wolf base
    with dissolve

    c "\"... !!\"" id c04_w_0596


    # 여기서부터 cg

    scene bg wolf_s2_sky
    show wolf_s2_cloud
    show wolf_s2_house
    show wolf_s2_01
    show wolf_s2_leaf
    with Fade(0.8, 0.8, 0.8)    
    
    "가헬은 [pl_name][josa_eul_reul] 끌어당겼다." id c04_w_0597

    show wolf_s2_02
    with dissolve
    
    "둘 사이에 거리는 이제 없다. 가헬은 어느 때보다 깊은 목소리로 말했다." id c04_w_0598

    w shy5 "\"키스해도 될까.\"" id c04_w_0599

    c shy2 "(이래도 되나? 가헬이랑?)" id c04_w_0600
   
    c "(그렇지만 못할 건 없잖아.)" id c04_w_0601
    
    c "(어쩌지? 모르겠다.)" id c04_w_0602

    "[pl_name][josa_eun_neun] 고민 끝에 작게 고개를 끄덕였다." id c04_w_0603
    
    "허락을 받아낸 가헬은 [pl_name]의 눈을 보며 조심스럽게 다가갔다." id c04_w_0604

    show bg wolf_s2_sky :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.01
    show wolf_s2_cloud :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.04
    show wolf_s2_house :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.08
    show wolf_s2_01 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.12
    show wolf_s2_02 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.12
    show wolf_s2_leaf :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 1.8 zoom 1.4

    
    "가헬이 고개를 살짝 기울여 [pl_name]의 코에 닿는 순간, 둘은 서로의 떨림을 느낄 수 있었다." id c04_w_0605
    
    "[pl_name][josa_eun_neun] 지금 상황을 어떻게 해야 할지 고민했다." id c04_w_0606

    c "(가헬, 엄청나게 긴장한 것 같은데...)" id c04_w_0607

    menu :
        "가헬이 하고 싶은 대로 하게 둔다." :
            
            #가헬호감도+2
            $ wolf_dom += 1
            $ wolf_love +=2
            $ display_text = _("가헬 호감도 변화")
            show screen affection_indicator 
        
            hide wolf_s2_02
            show wolf_s2_03_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.12
            with dissolve      
            
            c "(그, 그래도 가헬이 나보단 잘하겠지?)" id c04_w_0608

            show bg wolf_s2_sky :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.06
            show wolf_s2_cloud :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.2
            show wolf_s2_house :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.3
            show wolf_s2_01 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.41
            show wolf_s2_03_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.41
            show wolf_s2_leaf :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 2.2

            pause (2.0)
            hide wolf_s2_01
            hide wolf_s2_03_w
            show wolf_s2_04_w:
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            "[pl_name][josa_eun_neun] 그냥 눈을 꾹 감았다. 가헬의 혀가 맞닿아 오는 게 느껴졌다." id c04_w_0609
            
            "[pl_name][josa_i_ga] 입을 살짝 벌리자 기다렸다는 듯 가헬의 혀가 들어온다." id c04_w_0610
            
            "말캉한 혀끼리 부딪치며 뜨거운 감정을 교환했다. 질척한 소리가 새어나온다." id c04_w_0611

            c shy "\"읏!!...\"" id c04_w_0612

            "가헬은 조금 더 고개를 숙여 [pl_name]의 입안 구석구석을 탐했다." id c04_w_0613
            
            "약간 거칠어진 가헬의 움직임에 [pl_name][josa_eun_neun] 숨이 가빠졌다." id c04_w_0614
            
            "가헬은 [pl_name][josa_eul_reul] 더 세게 끌어안으며 쉴 틈을 주지 않았다." id c04_w_0615
            
            "[pl_name]도 주춤거리다 가헬의 허리쯤에 손을 얹었다." id c04_w_0616

            "로맨틱한 것과 별개로, 가헬의 키스는 조금 과격한 것 같았다." id c04_w_0617

            with hpunch
            
            c "(자, 잠깐. 이 느낌은...)" id c04_w_0618

            "[pl_name][josa_eun_neun] 아랫배쯤에 닿는 묵직한 느낌에 흠칫 놀랐다." id c04_w_0619
            
            "가헬의 고간이 조금씩 존재감을 키우고 있었다." id c04_w_0620
            
            "가헬 본인은 그 사실을 아는지 모르는지 키스에 열중했다." id c04_w_0621
            
            show wolf_s2_04_w at surprise_move2
            
            "[pl_name][josa_eun_neun] 결국 가헬의 몸을 가볍게 두드렸다." id c04_w_0622

            show wolf_s2_05_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            w "\"... 왜 그래?\"" id c04_w_0623

            c "\"허억... 허억... 아, 아니 잠깐 숨 좀 쉬게...\"" id c04_w_0624

            hide wolf_s2_04_w
            hide wolf_s2_05_w
            show wolf_s2_06_1 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            show wolf_s2_06_2 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            "[pl_name][josa_eun_neun] 자신을 집요하게 바라보는 가헬의 시선을 살짝 피했다." id c04_w_0625
            
            "정말로 잡아먹히는 거 아닌가 싶은 생각이 들었다." id c04_w_0626

            w "\"......\"" id c04_w_0627

            show wolf_s2_06_1 :
                linear 0.16 xoffset 15
                linear 0.16 xoffset 0
                linear 0.13 xoffset 5
            
            show wolf_s2_heart :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
                    
                parallel:
                    easein 1.2 alpha 0

                parallel:
                    easein 1.2 xoffset 10 yoffset -45
                        
            "그 모습을 보던 가헬은 코로 [pl_name][josa_eul_reul] 툭 치며 무언의 압박을 보냈다." id c04_w_0628

            c shy2 "(다시 하자는 건가?)" id c04_w_0629

            "가헬이 강아지처럼 보채는 것 같아서 조금 귀엽게 보였다." id c04_w_0630

            hide wolf_s2_06_1
            hide wolf_s2_06_2
            show wolf_s2_04_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            show wolf_s2_07_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve
            
            "[pl_name][josa_eun_neun] 약간의 웃음기와 함께 다시 입을 맞췄다." id c04_w_0631

            "한층 더 질척한 소리가 고요한 길거리를 채운다." id c04_w_0632

            "[pl_name][josa_eun_neun] 조금 여유롭게 가헬의 템포에 맞춰줄 수 있었다." id c04_w_0633

            show wolf_s2_05_w :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve
            
            "가헬은 살짝 눈을 떠서 [pl_name]의 반응을 감상했다." id c04_w_0634

            w "(꿈이 아니야... [pl_name][josa_wa_gwa] 키스 하고있어...)" id c04_w_0635

            "가헬의 모든 감각이 [pl_name][josa_eul_reul] 향해 바짝 곤두섰다." id c04_w_0636
            
            "[pl_name][josa_i_ga] 조금 웃는 것도 느낄 수 있었다." id c04_w_0637

            w "(이 순간이 영원했으면...)" id c04_w_0638

        "내가 적극적으로 가헬을 이끈다." :
            
            #가헬호감도+2 / 특수엔딩용 트리거+1
            $ wolf_sub += 1
            $ wolf_love += 2
            $ display_text = _("가헬 호감도 변화")
            show screen affection_indicator 
            
            hide wolf_s2_02
            show wolf_s2_03_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.12
            with dissolve   

            c "(가헬도 부끄러운 것 같으니까...)" id c04_w_0639

            "[pl_name][josa_eun_neun] 자신이 먼저 가헬을 이끌기로 마음먹었다." id c04_w_0640

            show bg wolf_s2_sky :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.06
            show wolf_s2_cloud :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.2
            show wolf_s2_house :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.3
            show wolf_s2_01 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.41
            show wolf_s2_03_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 1.41
            show wolf_s2_leaf :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                ease 2 zoom 2.2

            pause (2.0)
            hide wolf_s2_01
            hide wolf_s2_03_mc
            show wolf_s2_04_mc:
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            "[pl_name][josa_eun_neun] 손을 뻗어 가헬의 허리를 잡았다." id c04_w_0641

            "[pl_name][josa_i_ga] 다가가자 가헬은 조심스럽게 눈을 감았다." id c04_w_0642
           
            "가헬이 조금 당황해서 굳은 사이 [pl_name][josa_eun_neun] 더 공격적으로 덤벼들었다." id c04_w_0643
            
            show wolf_s2_05_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve
            
            "[pl_name][josa_eun_neun] 살짝 눈을 떠서 가헬의 반응을 지켜봤다." id c04_w_0644
            
            "호흡에 맞추어 자연스럽게 가헬의 입을 침범했다." id c04_w_0645

            with hpunch

            w "\"!!...\"" id c04_w_0646

            "가헬은 입안으로 들어오는 [pl_name]의 혀에 약간 놀랐다." id c04_w_0647

            w shy "(이렇게 적극적일 줄은 몰랐는데...)" id c04_w_0648

            transform slow_move :

                ease 0.25 xoffset -10
                ease 0.25 xoffset 10
                ease 0.2 xoffset 0
            
            show wolf_s2_04_mc at slow_move
            show wolf_s2_05_mc at slow_move

            "[pl_name][josa_eun_neun] 손에 힘을 주고 부드럽게 끌어당겼다." id c04_w_0649
            
            "자연스럽게 고개를 조금 더 숙인 가헬은 [pl_name]의 혓바닥을 반갑게 맞이했다." id c04_w_0650
            
            "말캉한 혀끼리 부딪치며 뜨거운 감정을 교환했다." id c04_w_0651

            c "(서투르진 않네.)"  id c04_w_0652

            hide wolf_s2_05_mc
            with dissolve          

            "[pl_name][josa_eun_neun] 가헬의 입안 구석구석을 탐했다." id c04_w_0653
            
            "조금 거칠게 가헬을 공략하는 [pl_name]의 움직임에 가헬은 숨이 가빠졌다." id c04_w_0654
            
            "[pl_name][josa_eun_neun] 가헬의 등을 꽉 쥐고 쉴 틈을 주지 않았다." id c04_w_0655
            
            "가헬도 자연스럽게 [pl_name]의 허리를 잡은 손에 힘을 줬다." id c04_w_0656

            show wolf_s2_04_mc at surprise_move2

            c shy "(음? 이 느낌은...)" id c04_w_0657

            show wolf_s2_05_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            "[pl_name][josa_eun_neun] 아랫배쯤에 닿는 묵직한 느낌에 살며시 눈을 떴다." id c04_w_0658
            
            "가헬의 고간이 조금씩 존재감을 키우고 있었다." id c04_w_0659
            
            "가헬 본인은 그 사실을 아는지 모르는지 [pl_name]에게 휘둘리고 있었다." id c04_w_0660
            
            "[pl_name][josa_eun_neun] 속으로 웃으며 입을 잠깐 뗐다." id c04_w_0661

            hide wolf_s2_04_mc
            hide wolf_s2_05_mc
            show wolf_s2_01 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            show wolf_s2_06 :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve


            w shy5 "\"하아... 하아...\"" id c04_w_0662

            "[pl_name][josa_eun_neun] 숨을 고르는 가헬에게 작게 속삭였다." id c04_w_0663

            c shy2 "\"혀 내밀어봐.\"" id c04_w_0664

            show wolf_s2_06_1a :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve

            "가헬은 [pl_name]의 명령대로 혀를 내밀었다." id c04_w_0665

            hide wolf_s2_01
            hide wolf_s2_06
            hide wolf_s2_06_1a
            show wolf_s2_04_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            show wolf_s2_07_mc :
                align (0.5, 0.32)
                anchor (0.5, 0.32)
                zoom 1.41
            with dissolve
            
            "[pl_name][josa_eun_neun] 가헬의 혀를 아주 가볍게 깨물고 나서 강하게 핥아 올렸다." id c04_w_0666
            
            "질척한 타액의 소리가 마치 남자의 아랫도리를 빠는 것 같았다." id c04_w_0667
            
            "가헬은 정말로 [pl_name]에게 잡아먹히는 거 아닌가 싶은 느낌이 들었다." id c04_w_0668

            w shy "(꿈이 아니야... [pl_name][josa_wa_gwa] 키스 하고있어...)" id c04_w_0669

            "가헬은 이 상황이 비현실적으로 느껴졌다." id c04_w_0670
            
            "키스도 상상하지 못했지만, 이렇게 적극적으로 덤벼오는 [pl_name][josa_eun_neun] 더욱 상상하지 못했다." id c04_w_0671

            c shy "(여기는 솔직하네.)" id c04_w_0672

            "[pl_name][josa_eun_neun] 가헬의 고간이 더 부풀어 오르는걸 옷 위로 느꼈다." id c04_w_0673
            
            "[pl_name][josa_i_ga] 허리를 살짝 튕겨 문지르자, 가헬은 벼락이라도 맞은 듯 움찔거렸다." id c04_w_0674
  
    hide wolf_s2_04_w
    hide wolf_s2_05_w
    hide wolf_s2_07_w
    hide wolf_s2_04_mc
    hide wolf_s2_07_mc
    show wolf_s2_01 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        zoom 1.41
    show wolf_s2_08 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        zoom 1.41
    with dissolve
    
    "[pl_name][josa_eun_neun] 가헬을 가볍게 밀어내며 말했다." id c04_w_0675

    c shy2 "\"후아... 이 이상은 길거리에서 하면 안 될 것 같아.\"" id c04_w_0676

    show wolf_s2_01 at surprise_move2
    show wolf_s2_08 at surprise_move2

    "[pl_name][josa_i_ga] 가헬의 아랫도리를 손가락으로 쿡 찌르자, 가헬은 시뻘게진 얼굴로 움찔했다." id c04_w_0677

    show wolf_s2_09 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        zoom 1.41
    with dissolve
    
    w "\"그, 그래...\"" id c04_w_0678

    hide wolf_s2_09
    with dissolve

    show bg wolf_s2_sky :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00
    show wolf_s2_cloud :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00
    show wolf_s2_house :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00
    show wolf_s2_01 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00
    show wolf_s2_08 :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00
    show wolf_s2_leaf :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        ease 2.7 zoom 1.00

    "[pl_name][josa_wa_gwa] 가헬은 한동안 조용히 서로를 바라봤다." id c04_w_0679

    w shy2 "\"...\"" id c04_w_0680

    c "\"...\"" id c04_w_0681
    
    "둘 사이에 침묵이 흐른다." id c04_w_0682

    # 가게앞 밤 배경으로
    scene bg shop_outside2 with Fade(0.8, 0.8, 0.8)
    show wolf
    with dissolve

    "뒷골목의 상점까지 도착하자 [pl_name][josa_i_ga] 말을 꺼냈다." id c04_w_0683

    c vhappy "\"그럼, 오늘부터 \'연인\'인가?\"" id c04_w_0684

    show wolf shy3
    with dissolve

    w "\"... 그래.\"" id c04_w_0685

    "가헬은 새삼 부끄러운지 [pl_name][josa_eul_reul] 제대로 바라보지 못하고 대답했다." id c04_w_0686

    show wolf am_u
    with dissolve
    
    "하지만 [pl_name]의 손을 잡는 태도는 꽤 자연스러웠다." id c04_w_0687

    stop music fadeout 2.5

    $ renpy.end_replay()

label c4w_end:

    #레스크 방 밤 버전
    scene bg home3 with Fade(0.8, 0.8, 0.8)
    show wolf
    with dissolve

    c talk"\"... 가헬?\"" id c04_w_0688

    show wolf talk
    with dissolve

    w "\"응.\"" id c04_w_0689

    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] 자신의 방까지 따라온 가헬에게 뭐라고 말해야 할지 고민했다." id c04_w_0690
    
    "지금의 분위기 흐름은 당연히 함께 침대로 들어가서 뜨거운 밤을 보내는 것이다." id c04_w_0691
    
    "하지만 [pl_name][josa_eun_neun] 술집에서 나올 때부터 약간의 졸음을 참고 있었다." id c04_w_0692
    
    "무리해서 하면 못 할 것도 아니지만, 예상되는 \'격렬한 행위\'는 오래 하지 못할 것 같았다." id c04_w_0693

    c talk "\"음, 뭘 기대하는지 알아서 미안한데... 지금 당장은 좀 힘들 거 같아.\"" id c04_w_0694

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (890, 0)
    show wolf talk
    with dissolve

    w "\"그게 무슨, 뜻인가?\"" id c04_w_0695

    hide question
    show wolf base
    with dissolve

    "가헬은 얼빠진 표정으로 [pl_name][josa_eul_reul] 바라보았다." id c04_w_0696
    
    "[pl_name][josa_eun_neun] 작게 하품하고 대답했다." id c04_w_0697

    c "\"오늘은 너무 늦어서...\"" id c04_w_0698
    
    c consider "\"이미 잘 시간도 넘었는데 준비에 뒤처리까지 하려면 오래 걸리잖아.\"" id c04_w_0699
    
    c "\"하다가 잠들어버리고 싶진 않아서...\"" id c04_w_0700

    "그리고 [pl_name]에게는 거절하고 싶은 중대한 이유가 하나 더 있었다." id c04_w_0701
    
    "[pl_name][josa_i_ga] 직접 봤던 가헬의 크기는 굉장했다." id c04_w_0702
    
    "그런 걸 받아내기 위한 몸과 마음의 준비가 필요했다." id c04_w_0703

    c ddam "(내가 가능하긴 할지 약간 두렵기도 하고...)" id c04_w_0704

    show wolf sad_am
    with dissolve

    "가헬의 귀가 순식간에 축 처졌다." id c04_w_0705
    
    "불쌍한 얼굴에 [pl_name][josa_eun_neun] 다른 방안을 제시했다." id c04_w_0706

    c talk "\"그, 같이 잘래? 자기 전에 빠르게 \'손장난\' 정도는 할 수 있어.\"" id c04_w_0707

    "가헬의 표정은 전혀 바뀌지 않았다." id c04_w_0708

    show wolf sad2_am
    with dissolve

    w "\"아니다. 붙어있으면 도저히 못 참을 것 같다.\"" id c04_w_0709

    show wolf sad3_am
    with dissolve

    c ddam2 "\"그래, 다음에 하자. 다음...\"" id c04_w_0710

    "자꾸 일을 미루는 것 같아서 [pl_name][josa_eun_neun] 약간 죄책감이 들었다." id c04_w_0711
    
    "[pl_name][josa_eun_neun] 가헬을 위로할 방법을 생각했다." id c04_w_0712

    menu :
        "가헬에게 굿나잇 키스를 한다." :

            play sound "effect/short_kiss.mp3" volume 0.5
            "[pl_name][josa_eun_neun] 살짝 발돋움해서 가헬의 뺨에 입을 맞췄다." id c04_w_0713
    
    show wolf shy
    with dissolve

    "쪽 하는 귀여운 소리를 남기고 [pl_name][josa_eun_neun] 한걸음 뒤로 물러났다." id c04_w_0714

    c talk "\"잘 자.\"" id c04_w_0715

    show wolf vhappy
    with dissolve

    w "\"... 그래.\"" id c04_w_0716

    "가헬은 기분이 풀린 듯 밝게 미소 지었다." id c04_w_0717
    
    "[pl_name][josa_eun_neun] 자연스럽게 가헬의 머리에 손을 올릴 뻔했다." id c04_w_0718
    
    "왠지 그런 행동을 예전에도 했었던 것 같은 기분이 들었다." id c04_w_0719

    c consider "(뭐지 이 ... 기시감?)" id c04_w_0720

    "예전에 바토의 머리를 쓰다듬은 적이 있지만, 뭔가 그것과는 다른 느낌이었다." id c04_w_0721
    
    "왜 이런 느낌이 드는지 알 수 없지만, 지금 더 고민해 봤자 소용없는 일이었다." id c04_w_0722
    
    show wolf shy2 at walk(-1500, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.85
    pause(0.5)

    "[pl_name][josa_eun_neun] 방을 나가는 가헬에게 손을 흔들어주었다." id c04_w_0723

    hide wolf
    
    "입은 옷을 정리하고 [pl_name][josa_eun_neun] 침대에 누웠다." id c04_w_0724

    # 레스크 속옷버전
    play sound "audio/effect/puton.mp3" volume 0.5
    show cara sigh inn_d
    with dissolve

    c "\"흐아암...\"" id c04_w_0725
    
    show cara sleep
    with dissolve

    "[pl_name][josa_eun_neun] 머리에 베개가 닿자마자 빠르게 골아떨어졌다." id c04_w_0726

    jump chapter4_dream