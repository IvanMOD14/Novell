label chapter2:
    
    $ cleanup_memory()
    $ _skipping = False
    scene bg dungeon_1 at scene_hmove (0, -230, -230)
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
    show two
    pause 1.0

    play music "background-trap-154361.mp3" fadein 2.8 volume 0.35
    
    hide chapter_back
    hide chap
    hide ter
    hide two
    with Dissolve (1.5)

    $ _skipping = True

    show screen book_icon with dissolve
    show cara out_d
    with dissolve

    c base out_d "던전은 서로 다른 공간을 강제로 이어 붙인 것처럼 기묘한 조화를 이루는 공간이다." id c02_0000

    c "벽에는 각양각색의 곰팡이가 얼룩덜룩하게 피어있고, 마나를 머금고 희미하게 빛나는 이끼가 불규칙한 패턴으로 성장하고 있었다." id c02_0001

    c "마물의 흔적이나 다른 사람의 야영 흔적 같은 것도 가끔씩 남아있다. 던전이 그냥 동굴과 다른 점은 마력에 따라 움직이는 것이다." id c02_0002

    c "던전 그 자체가 살아 숨 쉬고 있다. 매 순간 공간이 조금씩 변화하고, 벽의 일부는 마치 살아서 꿈틀거리는 듯했다." id c02_0003

    hide cara
    with dissolve

    scene bg dungeon_1 at scene_hmove (1.7, -230, -40)
    pause 1.7
    scene bg dungeon_1 at scene_hmove (2.5, -40, -410)
    pause 2.5
    scene bg dungeon_1 at scene_hmove (1.7, -410, -230)
    pause 1.7

    
    c out_d "나와 가헬은 조심스럽게 걸어가며, 이 기괴한 풍경을 조용히 감상했다." id c02_0004

    c talk "\"항상 느끼는 거지만, 던전 내부는 정말 기묘해... 마치 여러 조직을 이어 붙인 생물의 내장에 들어온 느낌이야.\"" id c02_0005

    "가헬은 [pl_name]의 말에 대해 잠시 생각에 잠긴 듯하더니, 무겁게 대답했다." id c02_0006

    show wolf out_d
    with dissolve
    show wolf out_u talk
    with dissolve

    w "\"내장이라... 끔찍한 비유지만, 부정할 수는 없겠군.\"" id c02_0007

    show wolf out_d base
    with dissolve

    c base "우리는 마나 허브를 찾기 위해 발걸음을 재촉했다." id c02_0008
   
    c "가능한 넓은 범위를 탐지하기 위해 던전의 중간쯤까지 가야 했다. 지도를 따라 공터에 도달하자, 나는 공간탐지 마법을 준비했다." id c02_0009

    "[pl_name]의 몸에서 서서히 피어오르는 푸른 빛무리가 어둠을 밀어내며 신비로운 광채를 발산했다." id c02_0010
    
    play sound "effect/flash.mp3" volume 0.2    
    show flash_blue at flash
    pause 2.5
    hide flash_blue at flash

    c "이 마력은 내 발끝에서 시작해 물줄기를 타고 흐르는 나뭇잎처럼 하늘거리며, 끊임없이 변화하는 던전의 깊숙한 곳까지 스며들었다." id c02_0011

    c "주변을 경계하는 가헬과 주문을 사용하는 내 숨소리 외에는 숨죽은 듯 고요했지만, 빛나는 마력의 실을 통해 느껴지는 던전은 꽉 찬 술집처럼 시끄러웠다." id c02_0012

    c "나는 손에 든 지도와 탐지 마법을 통해 느껴지는 던전을 비교하며 가헬에게 말했다." id c02_0013

    c talk "\"음, 일단 문제 없어. 지도와 거의 다르지 않네. 동쪽에 샘, 서쪽에 마물로 막힌 통로도 그대로야. 마나 허브는... 북서쪽에 있어.\"" id c02_0014

    c base "말을 마치자마자, 나는 던전의 지도를 접어 주머니에 넣었다. 가헬은 말없이 주변을 경계하던 중, 고개를 끄덕였다." id c02_0015

    c "고요한 던전 길을 따라 걷다가 가헬이 입을 열었다. 아까 사용한 탐지 마법이 궁금한 것 같았다." id c02_0016

    show wolf out_u talk
    with dissolve

    w "\"탐지 마법으로 다양한 정보를 추적할 수 있는 마법사는 드문 걸로 알고 있는데, 대단하군.\"" id c02_0017

    show wolf base
    with dissolve

    c talk "\"전에 던전 탐사 때도 보여줬잖아. 새삼스럽게 왜?\"" id c02_0018

    show wolf out_d talk
    with dissolve

    w "\"그때는 단순한 표면을 추적하는 마법으로만 생각했지.\"" id c02_0019
    
    w "\"대부분 마법사들은 공간 전체를 파악하려면 너무 많은 정보에 압도되기 때문에, 특정 대상만 추적하는 편이라고 들었다.\"" id c02_0020

    show wolf base
    with dissolve

    "그가 신기하다는 듯 이어 말했다." id c02_0021

    show wolf out_u talk
    with dissolve

    w "\"너도 그렇게 마나 허브를 추적하는 줄 알았는데, 던전에서 탐지 마법으로 정확히 공간 정보를 읽어내다니. 흔한 마법사와는 다르군.\"" id c02_0022

    show wolf out_d base
    with dissolve

    "[pl_name][josa_eun_neun] 살짝 민망한 웃음을 지으며 대답했다." id c02_0023

    c smile "\"하하, 용병 마법사면 아무래도 전투용 원소 마법이 특기일 테니까.\"" id c02_0024
    
    c talk "\"마탑의 정식 마법사에게 이런 건 아무것도 아닐 거야. 성도 반대편에서 잃어버린 동전도 찾을 수 있을걸?\"" id c02_0025

    "가헬은 여전히 [pl_name][josa_eul_reul] 대단하다고 생각하는 듯 빛나는 눈이었다." id c02_0026

    show wolf out_u talk
    with dissolve

    w "\"회복 물약에 마탑 공증을 받은 것도 그렇고, 혹시 마탑에서 교육을 받았어?\"" id c02_0027

    show wolf out_d base
    with dissolve

    c talk "\"그랬으면 계약할 때 신분 증명이 상인이 아니라 마법사였을걸?\"" id c02_0028
 
    c "\"마탑에 들어가려면 엄청난 경쟁률을 자랑하는 시험에 합격부터 해야 하고, 거기서 정식 마법사가 되기까지 어마어마한 돈이 든다고.\"" id c02_0029
 
    c "\"난 그렇게 재능이 있지도, 돈이 많지도 않아서... 회복 물약은 마탑의 지인을 통해 인증받은 거야.\"" id c02_0030

    "[pl_name]의 대답에 가헬은 의문을 표했다." id c02_0031

    show wolf out_u talk
    with dissolve

    w "\"그럼, 마법은 어떻게 배운 거야?\"" id c02_0032

    show wolf base
    with dissolve

    c talk "\"어릴 때 스승님이 있었거든. 특이한 용 수인이었어.\"" id c02_0033

    "가헬은 잠시 놀라서 [pl_name][josa_eul_reul] 바라봤다." id c02_0034

    w "(단 한 명의 스승에게?... 스승이 뛰어난 건가, 아니면...)" id c02_0035

    show wolf out_d talk
    with dissolve

    w "\"...그럼 마탑의 지인은?\"" id c02_0036

    show wolf base
    with dissolve

    c talk "\"아, 음. '바토'라고 있어. 걔한테 배운 건 아냐. 상점을 차렸을 때쯤에 처음 만났거든.\"" id c02_0037

    c base "나는 가헬과 '바토'라는 곰 수인에 대해 얘기하며 걸어갔다." id c02_0038
    
    c "원래 그는 마탑에서 허가받지 않은 {color=#ee3939}'금지된 마법'{/color} 같은 행위를 단속하는 업무를 하는데, 내 상점이 새로 생길 때도 검사를 하기 위해 찾아왔다." id c02_0039
    
    c "당연히 내 가게에는 문제가 없었지만, 바토가 쓰러지는 소동이 있었고 그때 도와준 인연으로 마탑 공증 문서까지 받게 되었다." id c02_0040

    stop music fadeout 2.5

label manaherb_colony:

    scene bg dungeon_2 with Fade(0.8, 0.8, 0.8)
    play music "sonic-void-157268.mp3" fadein 2.5 volume 0.7

    c out_d "한가로운 수다 시간은 오래가지 않았다. 배회하는 하급 마물 몇을 쓰러뜨리고 마나 허브 군락에 도착했다." id c02_0041
    
    c "빽빽하게 자라난 초록 수풀은 물약으로 만들어 팔 생각에 침이 꿀꺽 넘어갈 수준으로 가득 자라나 있었다." id c02_0042
    
    c "물론 전부 채집해 가면 나중에 내가 다시 왔을 때도 자라나지 않을 수 있으니, 적당히 반 정도만 가져가야 한다." id c02_0043
    
    c "나는 전용 주머니를 꺼내 허브를 채집할 준비를 했다." id c02_0044

    menu:
        "허브 채집을 함께하자고 한다.":

            $ wolf_understanding += 1 # 가헬 이해도 변화
            $ display_text = _("가헬 이해도 변화") 
            show screen affection_indicator

            c talk "\"가헬도 한번 채집해 볼래? 생각보다 쉬워.\"" id c02_0045

            show wolf out_d
            with dissolve
            show wolf out_u talk
            with dissolve

            w "\"어떻게 하는 건가?\"" id c02_0046

            show wolf out_d base
            with dissolve

            c base "나를 도와주려는 가헬의 앞에서 직접 시범을 보였다." id c02_0047

            c talk "\"시들지 않게 뿌리 끝을 마나로 감싸고 줄기가 끊어지지 않게 뽑는 거야. 마력보단 손재주가 중요할걸?\"" id c02_0048

            show wolf out_d sad_am
            with dissolve
            
            w "\"그건... 나는 마력을 조작형으로 사용할 수 없다. 시술을 받아서...\"" id c02_0049

            c talk "\"응? 아... 그렇구나.\"" id c02_0050

            show wolf base
            with dissolve

            c base "힘이 전부인 용병의 세상에서 몸에 술식을 새겨넣는 일은 흔하다." id c02_0051
  
            c "재능이 있다면 훈련을 통해 검기를 발생시킨다거나 받는 충격을 흘려낸다거나 하는 마법이 가능하지만, 용병이라면 쉽고 빠르게 시술로 해결하는 게 이득일 것이다." id c02_0052
 
            c "물론 시술은 만능이 아니다. 아무래도 가헬은 마나를 흡수해서 근육을 강화하는 술식밖에 사용할 수 없는 것 같다." id c02_0053
                        
            show wolf out_u talk
            with dissolve

            w "\"시간이 꽤 걸릴 테니, 그동안 주변을 지켜보도록 하지.\"" id c02_0054
            
            $ unlock_character_image("wolf", "wolf b_no sword_d")
            $ display_text = _("이미지 : 가헬(검)")
            show screen affection_indicator
            show wolf sword_d base
            with dissolve


        "경비를 부탁한다.":

            c talk "\"채집하는 동안 주변을 지켜줄 수 있을까?\"" id c02_0055

            show wolf out_d
            with dissolve
            show wolf out_u talk
            with dissolve

            w "\"알겠다.\"" id c02_0056
            
            $ unlock_character_image("wolf", "wolf b_no sword_d")
            $ display_text = _("이미지 : 가헬(검)")
            show screen affection_indicator
            show wolf sword_d base
            with dissolve

            "조용한 던전 안에서 대화마저 끊기니 숨 막히는 침묵이 이어졌다." id c02_0057

            c consider "(차라리 같이 채집하자고 할 걸 그랬나...)" id c02_0058

            c base "나는 어떻게든 수닷거리라도 꺼내볼까 하다가 그냥 채집에 집중했다." id c02_0059
            
            c "(빨리 끝내는 편이 낫겠다.)" id c02_0060

    # 선택지 끝
    
    # 시간흐름을 의미하는 화면 암전 효과

    scene bg dungeon_2 with Fade(0.8, 0.8, 0.8)

    c out_d "\"휴. 이 정도면 충분하겠지?\"" id c02_0061

    show herb :
        xcenter 0.5
        ycenter 0.5
    with dissolve
        
    "[pl_name][josa_i_ga] 세심하게 허브를 뜯어 주머니를 가득 채우는 동안, 가헬은 [pl_name][josa_eul_reul] 지켜보다가 가까이 온 박쥐 마물을 베어버리거나 했다." id c02_0062

    hide herb
    with dissolve
    
    "[pl_name][josa_eun_neun] 스트레칭을 하며 굳은 몸을 풀었다." id c02_0063

    stop music fadeout 2.5

    c talk "\"이제 나가자.\"" id c02_0064

    show wolf sword_d
    with dissolve

    w "\"...\""    

    ## 긴박한 BGM
    play music "cool-determine-hip-hop-trap-crime-dramatic-sports-music-21122.mp3" volume 0.65 fadein 2.5

    show wolf sword_u talk
    with dissolve

    w "\"잠깐... 뭔가 심상치 않다.\"" id c02_0065

    show wolf base
    with dissolve

    "가헬은 멀리 있는 마물을 유심히 바라보았다. 아직 마물이 가까이 오지 않았지만, 마물이 있는 방향에 주목해서 관찰하다가 하나의 결론을 냈다." id c02_0066

    show wolf talk
    with dissolve

    w "\"없던 통로가 생겼다.\"" id c02_0067

    show wolf sword_d base
    with dissolve

    c talk "\"던전이 움직였다는 뜻이네. 잠깐 탐지해 봐야겠어.\"" id c02_0068

    c base "나는 던전에 들어올 때보다 간단하게 가까운 곳만 탐지 마법을 사용했다." id c02_0069

    play sound "effect/flash_fast.mp3" volume 0.25    
    show flash_blue at flash_fast
    pause 0.95
    hide flash_blue at flash_fast

    c talk "\"막힌 벽이 뚫렸나 봐. 아니, 마물이, 너무 많은데?\"" id c02_0070

    c base "탐지할 수 없는 고립된 방에 마물이 가득 있었다가 지금 연결된 것 같다. 빨리 도망가야..." id c02_0071

    with vpunch

    n "{i}캬오오!!{/i}" id c02_0072

    c ddam2 "\"헉!\"" id c02_0073

    c "짐승형 마물이 위협적인 소리를 내며 이쪽으로 뛰어온다. 그 소리에 다른 마물들도 반응하는 듯했다." id c02_0074
   
    c "나와 가헬은 다른 통로로 뛰어서 도망쳤다. 그러나 그쪽에도 마물이 남아있었다." id c02_0075

    show wolf sword_u fight
    with dissolve

    w "\"흡!\"" id c02_0076

    play sound "effect/sword_slice.mp3" volume 0.7
    show sword_slash at slash2
    pause 0.2
    hide sword_slash at slash2

    pause 0.5

    play sound "effect/sword_slice2.mp3" volume 0.7
    show sword_slash2 at slash
    pause 0.2
    hide sword_slash2 at slash
    pause 0.5

    "가헬은 뿔을 앞세워 돌진하는 짐승형 마물을 날렵한 동작으로 조각내며 앞서 나아갔다." id c02_0077

    "[pl_name][josa_eun_neun] 가헬의 뒤를 정신없이 따라가다가 뒤돌아보니, 어둠 속에서 마물들이 득실거리는 것을 발견했다." id c02_0078

label monster_chase :

    scene bg dungeon_3 with Fade(0.2, 0.0, 0.5, color = '#fff')

    show wolf sword_u fight2
    with dissolve

    w "\"[pl_name], 피해!!\"" id c02_0079

    show wolf sword_u fight
    with dissolve

    c ddam2 out_d "\"으악!\"" id c02_0080

    play sound "effect/wind.mp3" volume 1.0

    show arrow at slide_right
    with vpunch
    pause 0.25
    show arrow2 at slide_right2
    with hpunch
    pause 0.5  

    c ddam "본능적으로 몸을 낮추고 구르며, 내 머리를 향해 날아오는 날카로운 독침을 간발의 차이로 피했다." id c02_0081

    c ddam2 "머리털 사이로 느껴지는 공기의 진동은 나를 소름이 끼치게 했다." id c02_0082

    play sound "effect/sword_slice2.mp3" volume 0.7
    show sword_slash2 at slash, mirror
    pause 0.2
    hide sword_slash2 at slash
    
    c base "가헬은 흉측한 모양의 덩어리를 두 동강 내고, 근육이 팽팽하게 조여진 다리로 빠르게 내게 질주했다." id c02_0083

    show wolf sword_u fight2
    with dissolve

    w "\"수가 너무 많아. 한 곳을 뚫고 도주할까?\"" id c02_0084

    show wolf sword_d fight
    with dissolve

    c talk "\"제길... 그래야겠어.\"" id c02_0085

    c base "이런 위험도 '하'의 던전에서 이토록 강력한 마물이 대거 나타나는 것은 이례적인 일이었다." id c02_0086
    
    c "추리할 여유는 없었다. 살아남기 위해 신속히 대응해야 했다." id c02_0087

    c talk "\"눈이 없는 마물도 있으니, 연막은 의미 없을 거야. 최대한 안전하게 길을 뚫으려면 최대한 마물을 반대로 유인해야 해. 그러려면...\"" id c02_0088

    play sound "effect/slashcut.mp3" volume 0.65
    show redlight at slash
    pause 0.2
    hide redlight at slash

    c base "빠른 판단을 마치고 나는 가헬의 검에 손을 댔다. 날카로운 칼날에 베인 손끝 위에 핏방울이 맺힌다." id c02_0089

    w "뭐 하는!..." id c02_0090

    c talk "\"왼쪽으로, 먼저 달려! 바로 따라갈게.\"" id c02_0091

    "가헬은 잠시 당황했지만, 곧 이해하고 마물들을 향해 날카로운 눈길을 던졌다." id c02_0092

    with vpunch

    c talk "\"지금!\"" id c02_0093
    
    play sound "effect/magic.mp3" volume 0.7
    show bluelight at magic
    pause 0.2
    hide bluelight
    pause 0.5

    "[pl_name][josa_i_ga] 소리치자, 가헬은 왼쪽으로 번개처럼 돌진했다. 동시에 [pl_name][josa_eun_neun] 피에 마나를 담아 허공에 뿌렸다." id c02_0094

    c base "마나를 추적하는 마물 몇몇은 여기에 이끌려 움직일 것이다. 나는 전력을 다해 가헬의 뒤를 따라 뛰었다." id c02_0095

    w "\"앞에서 오른쪽!\"" id c02_0096

    "가헬은 마물을 베어내는 동시에 중간중간 [pl_name][josa_i_ga] 잘 따라오고 있는지 확인했다." id c02_0097
    
    c ddam2 "오른쪽으로 급회전하자 쫓아오는 마물의 수가 확연히 줄었다. 하지만 내 숨은 점점 가빠졌고, 체력의 한계를 느꼈다." id c02_0098
    
    c ddam "숨을 고르기 위해, 잠시라도 숨을 곳을 찾아야 했다. 정말 잠깐이라도 마물에게서 몸을 숨기고 한숨 돌릴 곳이..." id c02_0099

    ##흔들림 효과
    with hpunch

    w "\"[pl_name]!!\"" id c02_0100

    c talk "\"어?\"" id c02_0101
    
    "가헬이 [pl_name][josa_eul_reul] 옆으로 밀쳤다." id c02_0102
    
    with vpunch
    play sound "effect/knife_stab.mp3" volume 0.9
    show redlight at slash
    pause 0.2
    hide redlight at slash

    show wolf hurt
    with dissolve

    w "\"크윽...!\"" id c02_0103
    
    c talk "\"가헬!\"" id c02_0104

    "가헬의 팔에서 짙은 피가 뚝뚝 떨어졌다. 마물이 쏜 가시가 근육 깊숙이 파고 들어가, 격렬한 고통에 가헬은 얼굴을 찡그렸다." id c02_0105
    
    "빠르게 퍼지는 독 때문에 팔뚝의 피부가 보랏빛으로 변하고, 상처에서는 피가 거품을 이루며 솟구쳤다." id c02_0106

    show wolf fight
    with dissolve
    
    "그러나 가헬은 아픔을 무시한 채, 근접한 마물 하나를 강하게 내려 베고, 그 시체를 발로 차서 쫓아오는 마물들을 방해했다." id c02_0107
    
    "이 틈을 타 [pl_name][josa_eun_neun] 가방을 뒤져 회복 물약을 찾았다." id c02_0108

    if high_potion == 1 :
        c base "(맞아. 이게 있었지.)" id c02_0109
        
        show high_potion :  
            xcenter 0.5
            ycenter 0.5
        with dissolve
        
        play sound "effect/water.mp3" volume 0.5

        c "나는 특제 회복 물약을 꺼내 바로 상처에 들이부었다." id c02_0110
        
        c "마법의 힘이 담긴 붉은 액체가 상처를 덮고, 순식간에 그를 완전히 치유한다." id c02_0111

        hide high_potion
        with dissolve

        c "그의 상처가 마치 시간이 되감기듯 사라져 갔다. 나는 이걸 챙겨서 정말 다행이라고 생각했다." id c02_0112

        $ wolf_love += 1 
        $ display_text = _("가헬 호감도 변화")
        show screen affection_indicator
        show wolf base
        with dissolve

        c "가헬은 한결 편안해진 표정으로 팔을 움직이며 상태를 점검해 본다." id c02_0113

        show wolf sword_u talk
        with dissolve

        w "\"허... 통증이 전혀 없어. 굉장한 성능의 물약이네.\"" id c02_0114

        show wolf sword_d base
        with dissolve       

    else :
        c base "(일단 응급 처치라도 해야 해.)" id c02_0115
        
        show potion :
            xcenter 0.5
            ycenter 0.5
        with dissolve

        c "나는 물약 두 개를 꺼내 하나는 바로 상처에 들이붓고 하나는 가헬에게 마시게 했다." id c02_0116
        
        c "아직 마물 떼와 거리가 있으니, 회복만 한다면 도망칠 수 있을 것이다." id c02_0117
        
        hide potion
        with dissolve

        c "보라색이던 피부가 점점 돌아오고, 콸콸 흐르던 피가 서서히 멈추는 게 보인다." id c02_0118
        
        c "하지만 고통만은 어쩔 수 없는지 가헬의 표정은 썩 좋지 않다." id c02_0119
        

    with hpunch

    # 마력 진동 이펙트?
    "!!!" id c02_0120
    
    c question2 "(응?... 뭐지? 방금 마력 진동이 터진 거 같은데.)" id c02_0121

    c base "자연스러운 흐름에 거스르는 마력이 털을 곤두서게 만든다." id c02_0122
    
    c "일단 가헬이 일어서는 동안 마물이 가까이 오지 못하도록 마력탄을 몇 개 던졌다." id c02_0123
    
    c "마물에게 제대로 된 피해는 못 주겠지만 마구잡이로 흩뿌려서 발을 묶을 생각이었다." id c02_0124

    show wolf sword_u hurt2
    with dissolve
    with vpunch

    w "\"커흑...!\"" id c02_0125

    "갑자기 가헬이 고통스러운 신음을 내뱉었다." id c02_0126

    w "\"으으윽... 빨리, 나가!\"" id c02_0127

    c question2 "\"뭐? 무슨 소리야?\"" id c02_0128

    w "\"나에게서, 떨어져! 먼저 여기서 나가! 빨리!! 크으윽...\"" id c02_0129

    # 여기서부터 가헬 역안

    $ unlock_character_image("wolf", "wolf b2 black_eye2 out_d aura")
    $ display_text = _("이미지 : 가헬(아우라)")
    show screen affection_indicator
    show wolf b2 sword_d black_eye2 aura
    with Dissolve (1.2)

    c base "가헬은 방금 나를 밀친 것과 비교할 수 없을 정도로 강하게 나를 밀어냈다. 등이 거의 얻어맞은 것처럼 욱신거린다." id c02_0130

    c "바닥에 나자빠진 내 눈에 보인 것은 알 수 없는 이유로 괴로워하는 가헬이었다." id c02_0131

    c "가헬 주변의 마력이 일그러지면서 가헬의 안으로 빨려 들어가는 게 느껴졌다. 게다가 가헬의 눈도 이상한 색으로 변하고 있었다." id c02_0132

    $ unlock_info_tag(1, "1")
    $ display_text2 = _("정보 : 마력 폭주")
    show screen affection_indicator2

    c consider "(설마... {color=#ee3939}'마력이 폭주'{/color}하는 건가?)" id c02_0133

    c base "가헬도 마력을 다룰 수 있으니까 무리해서 사용하면 저런 증상이 발생할 수 있다. 하지만 가헬같은 용병이 그 정도로 무리했다면 체력도 바닥나는 게 정상이다." id c02_0134
    
    c "방금까지만 해도 가헬은 숙련된 검사다운 통제된 호흡을 하고 있었다. 뭔가 다른 원인으로 마력 폭주가 발생하는 것 같다." id c02_0135
    
    c "가헬의 온몸 근육이 제멋대로 꿈틀거리는 게 보인다. 마력으로 근육을 강화하는 마법을 사용한다면 마력 폭주는 저런 형태로 나타날 것이다." id c02_0136

    c "(아마도 힘이 넘쳐흐르는 대신, 단 한 순간도 멈추지 못하겠지.)" id c02_0137

    c "모든 게 내 잘못 같았다. 죄책감이 몸을 무겁게 짓누른다." id c02_0138

    show wolf sword_u
    with dissolve

    c "가헬은 쌍검을 부러질 기세로 꽉 쥐고, 검붉은 색으로 변해버린 눈을 부릅뜨고 마물 떼를 바라본다." id c02_0139
    
    c "나와 함께 나가려다가 나를 베어버릴 가능성이 있으니, 차라리 마물을 전부 해치울 생각인 것 같다." id c02_0140
    
    c "아무리 가헬이 강해도 저런 상태로 멀쩡히 싸울 수 있단 말인가?" id c02_0141
    
    # 가헬 키워드 4 마력 폭주 획득

    show wolf black_eye
    with dissolve
    
    w "\"반드시, 돌아갈 테니까...\"" id c02_0142

    c "그의 목소리에는 굳은 결의가 담겨 있었다. 그 말을 남긴 가헬은 순간적으로 움직임을 가속하며, 마치 빛과 같은 속도로 마물에게 돌진했다." id c02_0143

    hide wolf with dissolve

    c "점점 멀어지는 가헬을 뒤로하고 나는 가헬의 뜻대로 밖으로 나갈 길을 찾았다." id c02_0144

    stop music fadeout 2.5

    scene bg dungeon_1 with Fade(0.8, 0.8, 0.8)

    play music "background-trap-154361.mp3" fadein 2.5 volume 0.35

    c sad_am out_d "던전 입구에서 가헬을 기다리면서도 걱정과 괴로움에 고개를 들지 못했다." id c02_0145
    
    c "던전 호위 용병은 이런 목숨값까지 고려해서 고용하는 것이지만, 가헬과는 정이 들었기도 하고." id c02_0146
    
    c "그리고 이상하게도 비슷한 일을 겪었던 기분이 들면서 그게 무슨 일이었는지 기억나지 않아서 더 괴로웠다." id c02_0147

    c "(...시체라도 찾아야 하지 않을까?)" id c02_0148

    c base "그런 생각을 하며 던전에 다시 들어가려는 순간, 눈앞에 가헬이 걸어 나오는 게 보인다." id c02_0149
    
    # 가헬 등장

    show wolf sword_d hurt
    with dissolve

    c "가헬은 심하게 지쳐 보이지만 놀랍게도 피 한 방울 흘리지 않은 것 같다." id c02_0150

    c talk "\"가헬!\"" id c02_0151

    show wolf sword_u talk
    with dissolve

    w "[pl_name]..." id c02_0152


    play sound "audio/effect/body_drop.mp3"  volume 0.8
    show wolf sword_d hurt2 at down
    with hpunch
    pause 0.6
    show wolf smile
    with dissolve

    c base "가헬은 옅은 미소를 지으며 안도감을 느낀 건지 바닥에 쓰러졌다. 허겁지겁 다가가자 다행히 기절하지 않은 가헬이 내 손을 잡는다." id c02_0153
    
    c talk "\"빨리 가게로 가자.\"" id c02_0154
    
    show wolf sword_d talk
    with dissolve

    w "\" ... 그래.\"" id c02_0155

    show wolf base
    with dissolve
    
    $ unlock_info_tag(1, "2")
    $ display_text = _("정보 : 전송 마법진")
    show screen affection_indicator

    c base "나는 힘겹게 가헬을 부축해서 {color=#ee3939}'전송 마법진'{/color}으로 갔다. 치유사를 찾을 시간에 차라리 빨리 가게에서 특제 회복 물약을 쓰는 게 나을 것이다." id c02_0156

    stop music fadeout 2.5

label dungeon_end : 

    scene bg shop with Fade(0.8, 0.8, 0.8)
    
    show wolf out_d hurt
    with dissolve

    "가게에 도착한 [pl_name][josa_eun_neun] 낑낑대며 가헬의 몸을 계단으로 이끌었다." id c02_0157
    
    c ddam2 out_d "(무거워!...)" id c02_0158

    stop music fadeout 2.5  
    
    scene bg home with Fade(0.8, 0.8, 0.8)

    show wolf out_d hurt
    with dissolve

    "[pl_name][josa_eun_neun] 자신의 방 침대에 가헬을 눕혔다. 겉으로 보이는 핏자국은 없지만, 어디를 어떻게 다쳤는지 확인할 필요가 있었다." id c02_0159
    
    "[pl_name][josa_eun_neun] 가헬의 옷을 벗기기 시작했다." id c02_0160

    play sound "audio/effect/puton.mp3" volume 0.5
    
    show wolf am_d hurt
    with dissolve

    w "\"!!...\"" id c02_0161
    
    show wolf am_u talk
    with dissolve

    w "\"이, 이정도는 직접…!\"" id c02_0162

    menu:

        "강제로 벗긴다." :

                show wolf am_d base
                with dissolve

                "가헬은 [pl_name]의 손을 막으려고 했으나 근육이 말을 듣지 않았다." id c02_0163


    $ unlock_character_image("wolf", "wolf b_no inn_d")
    $ display_text = _("이미지 : 가헬(속옷)")
    show screen affection_indicator
    play sound "audio/effect/body_drop.mp3" volume 0.6
    show wolf inn_u hurt2
    with dissolve

    w "\"거기는!...\"" id c02_0164

    $ unlock_character_image("wolf", "wolf b_no nake0_d")
    $ display_text2 = _("이미지 : 가헬(알몸)")
    show screen affection_indicator2
    play sound "audio/effect/takeoff.mp3" volume 0.55
    show wolf nake0_d talk
    with dissolve
    pause 0.5
    show wolf shy
    with dissolve

    "결국 [pl_name]의 손에 속옷까지 빼앗긴 가헬은 수치스러워서 눈을 감았다." id c02_0165

    w "\"으...\"" id c02_0166

    show high_potion :  
            xcenter 0.5
            ycenter 0.5
    with dissolve

    "[pl_name][josa_eun_neun] 침대 밑에 숨겨둔 특제 회복 물약을 꺼냈다." id c02_0167
    
    c talk "\"못 움직이는거 보니 역시 근육을 혹사시킨 것 같네. 근육이 물약을 흡수하려면...\"" id c02_0168
    
    play sound "effect/water.mp3" volume 0.5

    c base "나는 생각 끝에 물약을 가헬의 몸 위에 들이부었다. 근육을 주무르면서 직접 몸 안으로 흡수시키면 될 것이다." id c02_0169

    hide high_potion
    with dissolve

    c "축축한 손으로 가헬의 팔을 잡고 마사지하자 효과가 보이기 시작했다." id c02_0170

    
    play sound "audio/effect/slow_breath.mp3" volume 0.7 fadein 1.5
    show wolf horny3
    with dissolve
    
    "[pl_name][josa_i_ga] 양 손으로 가헬의 가슴을 주무르자 가헬의 숨소리가 거칠어졌다." id c02_0171

    "정작 [pl_name][josa_eun_neun] 가헬의 몸 구석구석을 만지며 근육이 멀쩡한지 신경쓰느라 바빴다." id c02_0172
    
    c "(생각보다 더 단단한데?)" id c02_0173
    
    "한편 가헬은 [pl_name] 때문에 미칠 것 같았다." id c02_0174

    show wolf shy3
    with dissolve

    "눈을 감고 있었더니 감각이 더 예민해진 것 같아서 차라리 눈을 떴다." id c02_0175
    "가슴부터 배, 옆구리, 허벅지까지 서서히 내려가는 [pl_name]의 손길에 정신을 차릴 수 없었다." id c02_0176
    "조금이라도 긴장을 풀었다가는 [pl_name]의 앞에서 발기해버릴 것이다." id c02_0177
    
    show wolf shy2
    with dissolve

    w "조금만 살살..." id c02_0178
    
    c question2 "아파? 어디... 여기?" id c02_0179
    
    "[pl_name][josa_eun_neun] 가헬의 반응을 오해하고 혈관에 문제가 있나 의심했다." id c02_0180
    
    "[pl_name]의 손이 가헬의 허벅지 안쪽을 붙잡는 순간, 가헬의 남근은 벌떡 일어났다." id c02_0181
    
    $ unlock_character_image("wolf", "wolf b_no nake_d")
    $ display_text = _("이미지 : 가헬(발기)")
    show screen affection_indicator
    show wolf nake_d horny2
    with Dissolve (1.0)
    with vpunch

    w "\"!!!\"" id c02_0182
    
    show wolf horny3
    with dissolve

    w "... 이, 이제 괜찮다." id c02_0183
    
    show wolf shy2
    with dissolve

    play sound "effect/footstep.mp3" volume 0.8 fadeout 0.7
    show wolf shy2 at walk (-500, 0.8, 2)
    
    pause(1.1)
    show wolf at down
    with ease
    show wolf at scene_vmove(0.5, 100, 0)
    pause 0.8
    show wolf at vshake (0.08, 0, -10)
    
    "가헬은 바닥에 떨어진 속옷을 주워서 입으려다가 포기했다." id c02_0184

    show wolf nake_u horny2
    with dissolve

    "도저히 가릴 수 없는 크기의 물건이 힘차게 자기주장을 하고 있었다." id c02_0185
    
    "가헬은 그냥 알몸 그대로 방을 나갔다." id c02_0186

    play sound "audio/effect/walk.mp3" volume 0.75
    show wolf at walk (-1500, 0.8, 3)

    # 화면 밖으로 나가기

    if wolf_see >= 1 :
        
        c talk "\"가헬!\"" id c02_0187

        c base "가헬은 아무래도 자신의 방에 들어간 것 같다." id c02_0188

        c "부끄러운건 이해하지만 아직 다 낫지도 않았는데 막 움직이면 근육이 망가질 수 있다." id c02_0189
        
        scene bg shop2f with Fade(0.8, 0.8, 0.8)

        play sound "audio/effect/body_fall.mp3" volume 0.8

        c "나는 바닥에 놓인 갑옷과 검을 챙겨서 가헬의 방 문 앞에 내려놓았다." id c02_0190
        
        c "(따지고보면 처음 본 것도 아니긴 한데...)" id c02_0191
        
        "가헬이 알면 수치심에 죽을지도 모르는 사실을 숨기며 [pl_name][josa_eun_neun] 아래층으로 내려갔다." id c02_0192

    else :
        
        c consider "(내가 뭘 본거지.)" id c02_0193

        c base "조금 당황스럽지만 자신보다 더 당황했을 가헬을 생각하니 미안해졌다." id c02_0194

        c "가헬은 아무래도 자신의 방에 들어간 것 같다." id c02_0195

        scene bg shop2f with Fade(0.8, 0.8, 0.8)

        play sound "audio/effect/body_fall.mp3" volume 0.8

        c "나는 바닥에 놓인 갑옷과 검을 챙겨서 가헬의 방 문 앞에 내려놓았다." id c02_0196
        
        c "(그냥 모르는 척 해줘야겠다.)" id c02_0197

        "머릿속에서 방금 본 것을 쫓아내며 [pl_name][josa_eun_neun] 아래층으로 내려갔다." id c02_0198

    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40
    

    #가헬 풀 복장
    show wolf am_d shy2
    with dissolve

    "잠시 후, 조금 부끄러운 듯한 모습의 가헬이 내려왔다." id c02_0199

    show wolf
    with dissolve

    c talk "\"오늘은 더 쉬는 게 좋지 않을까?\"" id c02_0200

    show wolf am_u shy3
    with dissolve

    w "\"걱정해 줘서 고맙다. 하지만 던전의 상태를 빨리 알려야 해.\"" id c02_0201

    show wolf am_d base
    with dissolve
    
    "가헬의 추측에 따르면, {color=#ee3939}‘마물 콜로니’{/color}에서 도망간 마물들이 던전으로 숨어들어 간 것 같다고 한다." id c02_0202

    "검증이 필요하겠지만 아마도 마물이 마력 진동을 느끼고 그곳으로 이끌려간 것으로 추측 중이다." id c02_0203

    "이런 정보를 빨리 용병 길드에 전달해야 위험도가 갱신될 것이다." id c02_0204

    c "\"나 혼자 가도 되는데.\"" id c02_0205

    show wolf am_u talk
    with dissolve
    
    w "\"던전 깊은 곳의 마물이... 내 증언이 필요하다.\"" id c02_0206

    show wolf am_d base
    with dissolve
    
    c base "가헬의 주장을 굽히지 못해서 결국 우리는 함께 용병 길드로 갔다." id c02_0207

    scene bg guild with Fade(0.8, 0.8, 0.8)
    c "시끌벅적한 용병 길드는 가헬의 등장으로 약간 조용해졌다. '칼루리엔' 소속 용병이니 이목이 쏠릴 법하다. 뒤에 선 나는 가헬의 덩치에 가려져서 다행이라고 생각했다." id c02_0208
    
    show lucas base at left, mirror
    with dissolve

    show wolf at right
    with dissolve

    show lucas talk
    with dissolve

    l "\"안녕하십니까 가헬님.\"" id c02_0209
    
    show lucas base
    with dissolve

    "길드 접수원 루카스는 예의 바른 인사를 건넸다. 가헬은 곧바로 본론으로 들어가 {color=#ee3939}‘타시아’{/color} 던전에 가득한 마물에 관해 이야기했다." id c02_0210

    show lucas talk am_u
    with dissolve

    l "\"... 보고서가 필요하겠군요.\"" id c02_0211
    
    show lucas base page_u
    with dissolve

    "[pl_name]의 증언은 사전 설명에 불과했다. 가헬의 증언에 따라 마물의 종류와 대략적인 수, 던전의 변화 등등이 기록된다." id c02_0212
   
    "생각보다 더 엄청난 양의 마물과 전투했다는 걸 알게 되자 [pl_name]의 표정은 점점 경악으로 변했다." id c02_0213

    show wolf am_u talk
    with dissolve

    w "\"콜로니의 마물이 던전에 유입된 것 같다. 그것도 꽤 많은 수가.\"" id c02_0214

    show wolf am_d base
    with dissolve
    
    show lucas talk
    with dissolve

    l "\"자세한 증언 감사합니다. 이 사건은 반슈타인 기사단에도 공유해야겠군요.\"" id c02_0215
    
    show lucas base page_d
    with dissolve

    "심하면 던전에서 마물 콜로니가 새로 생길 수도 있다. 물론 그렇게 되면 기사단이 처리하겠지만, 위험한 일은 하나라도 적은 편이 좋다." id c02_0216
    
    scene bg street with Fade(0.8, 0.8, 0.8)

    "가헬과 증언을 마치고 가게로 돌아오는 길에 고기를 크게 한 덩이 샀다. 육체의 부상은 치료했으나 정신적인 휴식이 필요할 것이다." id c02_0217
    
    c talk "\"오늘은 든든하게 먹고, 내일 영업도 혼자 할 테니 푹 쉬어.\"" id c02_0218

    show wolf
    with dissolve
    
    "가헬은 [pl_name][josa_eul_reul] 물끄러미 바라보다가 활짝 웃었다." id c02_0219

    show wolf vhappy
    with dissolve    

    w "\"고마워.\"" id c02_0220
    
    c laugh "가헬의 순수한 미소는 처음 보는 것 같다. 나는 마주 웃어주었다." id c02_0221


label magic_shop_bear:

    scene bg shop with Fade(0.8, 0.8, 0.8)

    "정말 다사다난했던 어제 이후로 평화로운 가게 영업을 하니 기분이 나른해졌다. 이틀 연속 휴업을 한 탓인지 손님도 몇 없어서 재료 손질에 시간을 쓸 수 있었다." id c02_0222
   
    "늘어지는 마음을 다잡기 위해 청소라도 하던 도중에 문이 열린다." id c02_0223

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c02_0224


    $ unlock_character("bear")
    $ display_text = _("캐릭터 : 바토")
    show screen affection_indicator
    show bear out_d
    show staff_d
    with dissolve

    "상점에 들어온 건 흰색 곰이었다. 로브를 두르고 스태프를 든 모습이 전형적인 마법사의 복장이다. 익숙한 얼굴에 [pl_name][josa_eun_neun] 바로 인사를 건넸다." id c02_0225

    c talk "\"어서 와. 한적할 때 잘 왔어.\"" id c02_0226

    c base "이 곰, 바토는 복장부터 알 수 있듯이 마법사다. 그것도 마탑의 정규 교육을 받은 엘리트 마법사." id c02_0227

    c "그를 처음 본다면 첫인상과 덩치에 조금 겁먹을 수 있지만 알고 보면 생각보다 말랑말랑한 곰이다." id c02_0228

    c "보기보다 수줍음도 많고 부끄럼도 타지만 마법 실력만큼은 일류라고 할 수 있다." id c02_0229

    show bear talk
    show staff_d
    with dissolve

    b "\"안녕하세요, 형...\"" id c02_0230

    show bear base
    show staff_d
    with dissolve

    c "그는 나보다 어리다. 마탑의 교육은 기사 수련과 달리 시험을 통과할 때까지 몇 년이고 계속되는데, 그 과정을 빠르게 졸업하고 벌써 몇 년째 실전에서 뛴다는 건 바토의 천재성을 증명하는 것이다." id c02_0231

    c talk "\"오늘은 무슨 일로 왔어?\"" id c02_0232

    hide staff_d
    show bear out_u embrass3
    show staff_u
    with dissolve
    
    b "\"그, 그게, 별건 아니고, 그냥... 확인하러 왔어요.\"" id c02_0233

    hide staff_u
    show bear out_d base
    show staff_d
    with dissolve

    c "\"음, 차라도 한 잔 내올게.\"" id c02_0234

    c base "바토가 말하는 '확인'은 여러 가지 의미가 있다. 이 가게가 멀쩡히 있는지, 나는 어디 잡혀가진 않았는지, 그리고 바토 본인의 상태까지 확인하러 온 것이다." id c02_0235

    c "그는 내 위험한 사업에 대해 어느 정도 알고 있고 그것을 단속해야 하는 입장이지만, 동시에 나에게 목숨을 빚지고 나에게 협력하는 중이다." id c02_0236

    $ unlock_info_tag(1, "3")
    $ display_text = _("정보 : 마력 누수")
    show screen affection_indicator

    c "바토는 언제부턴가 심각한 {color=#ee3939}'마력 누수'{/color} 문제를 겪고 있다." id c02_0237
    
    c "마법을 사용할 때 마나가 조금 새는 정도는 흔한 일이지만, 바토는 평균 수준에 한참 못 미치는 효율이 나올 정도로 마나가 줄줄 새고 있었다." id c02_0238

    c "출력이 약해지는 건 당연한 일, 남들과 같은 수준의 마법을 쓰려면 밑 빠진 독에 물을 붓는 것처럼 마나를 퍼부어야 한다. 그리고 그렇게 마력을 쓰다간 목숨이 위험해진다." id c02_0239
    
    # 바토 키워드 1 마력누수 획득

    hide staff_d
    show bear out_u talk
    show staff_u
    with dissolve

    b "\"여기 오면 왠지 마음이 편해요. 그렇게 자주 온 건 아니지만...\"" id c02_0240

    show bear base
    with dissolve
    
    "바토는 차를 홀짝이며 우물쭈물 말했다. 생김새와 동떨어진 성격에는 왠지 그를 동생처럼 여기게 만드는 묘한 힘이 있다." id c02_0241
    
    c "나는 바토를 가게 안쪽으로 이끌었다." id c02_0242
    
    c talk "\"잠깐 앉아볼래?\"" id c02_0243

    show bear talk
    with dissolve
 
    b "\"ㄴ, 네...\"" id c02_0244
    
    hide staff_u
    show bear out_d base
    show staff_d
    with dissolve
 
    c base "나는 치유사가 진찰하는 것처럼 의자에 앉은 바토를 만졌다. 흰 털에 뒤덮인 살과 근육이 긴장한 듯 움찔거린다." id c02_0245
    
    c "가헬이나 엘레드처럼 전문적인 훈련을 한 몸매는 아니어도 무시무시한 힘을 낼 수 있는 근육이 느껴진다." id c02_0246
 
    c "흔해빠진 용병 나부랭이보단 바토가 더 주먹질을 잘할 것이다. 싸우는 모습을 내가 직접 보진 못했지만, 바토에게 맞고 곤죽이 된 암시장 상인의 얼굴은 본 적이 있다." id c02_0247

    hide staff_d
    show bear out_u embrass
    show staff_u
    with dissolve

    with vpunch
    b "\"...힉!\"" id c02_0248
    
    c question2 "\"응? 왜 그래?\"" id c02_0249

    show bear embrass3
    with dissolve
    
    b "\"아, 아니, 아니에요.\"" id c02_0250

    c base "아까보다 더 긴장했는지 바토의 털이 쭈뼛쭈뼛 서 있다. 폭신 말랑한 촉감이 중독적이라 더 만지고 싶지만 해야 할 일은 끝났으니 손을 뗐다." id c02_0251

    show bear base
    with dissolve

    c talk "\"각인은 아무 문제 없어. 새어나간 마나도 잘 회수되고 있지?\"" id c02_0252

    show bear talk
    with dissolve

    b "\"네. 고마워요, 형.\"" id c02_0253

    hide staff_u
    show bear out_d base
    show staff_d
    with dissolve
    
    c "\"혹시 모르니 평소에 가장 자주 쓰는 마법 한번 써봐.\"" id c02_0254

    show bear embrass3
    with dissolve
    pause 0.5
    show bear embrass4
    with dissolve
    
    b "\"......\""  id c02_0255
    
    "바토는 잠깐 고민하더니 들고 다니던 스태프의 마력 구체를 똑 뗐다." id c02_0256

    hide staff_d
    show bear out_u base
    show staff2_u
    with dissolve
    
    c base "(저게 저렇게 떨어지는 물건이었구나...)" id c02_0257
    
    "바토는 금속 재질처럼 보이는 구체에 손을 집어넣었다. 동그란 덩어리는 생김새와 다르게 액체처럼 물컹거리면서 바토의 손가락을 바로 집어삼켰다." id c02_0258
    
    $ unlock_character_image("bear", "bear b_no out_d knuckle staff2_d")
    $ display_text = _("이미지 : 바토(너클)")
    show screen affection_indicator
    show bear knuckle
    show weapon :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "순식간에 형태를 변환하는 구체는 전투용 너클로 쓰는 것 같았다. 바토는 마력을 불어넣어 여러 종류의 강화 마법을 한 번에 사용했다." id c02_0259
    
    hide weapon
    with dissolve

    show bear talk
    with dissolve

    b "\"... 멀쩡해요.\"" id c02_0260

    hide staff2_u
    show bear out_d base
    show staff2_d
    with dissolve

    play sound "effect/swing.mp3" volume 0.7
    pause 0.4
    with vpunch
    pause 0.5
    
    play sound "effect/swing2.mp3" volume 0.7
    pause 0.4
    with vpunch
    pause 0.5   
    
       
    "바토가 허공에 주먹질을 몇 번 하자 공기가 찢어지며 위협적인 바람 소리가 난다. 무시무시한 소리에 자연스럽게 [pl_name]의 털이 바짝 일어선다." id c02_0261
    
    c ddam2 "(저 정도면 한 방에 죽고도 남겠는데... 사람한테는 살살 하나 보다.)" id c02_0262

    c base "암시장 상인의 뭉개진 얼굴이 떠오르며 바토의 강함을 새삼 느꼈다." id c02_0263
    
    c "육체적인 힘도 강하지만 그걸 보조해 주는 다양한 강화 마법들을 동시에 사용하는 것도 대단한 능력이다." id c02_0264
    
    c "무기를 단단하게 만들고 육체를 빠르게 만들면서 받는 충격을 분산하는 완벽한 전투용 마법 조합이다." id c02_0265

    c talk "\"체감은 어때? 무리해서 마력을 쓰는 거 아냐?\"" id c02_0266

    hide bear
    hide staff2_u
    show bear out_d
    show staff_d
    with dissolve

    "바토는 전투용 너클을 다시 스태프의 마력 구체로 돌려놓았다." id c02_0267

    hide staff2_d
    hide staff_d
    show bear out_u talk
    show staff_u
    with dissolve

    b "\"괜찮아요. 이 정도면 160 도데카 정도...\"" id c02_0268

    show bear base
    with dissolve

    menu:
        "그게 뭔지 물어본다.":

            $ bear_understanding += 1 # 바토 이해도 변화
            $ display_text = _("바토 이해도 변화")

            show screen affection_indicator

            c question2 "\"160 도데카? 그게 뭐야?\"" id c02_0269
            
            c base "마탑의 교육을 받지 못한 나는 그 용어가 일종의 단위인 것은 눈치챘지만 정확한 의미는 알지 못했다. 바토는 내 반응을 보고 설명을 시작했다." id c02_0270

            show bear talk
            with dissolve
            
            b "\"표준 마력 단위에요. 자주 쓰는 말은 아니고, 논문에서나 쓰는 거라...\"" id c02_0271
            
            b "\"마력의 12가지 발현 이론에서 생긴 용어인데, 아니 그게 중요한 게 아니지... 이건 기준점이 되는 표준 수정 구슬이 있으면 편한데.\"" id c02_0272
            
            b "\"아, 아예 직접 체감해 볼래요?\"" id c02_0273

            play sound "effect/footstep.mp3" volume 0.85
            hide staff_u
            show bear out_d base at fwalk
            show staff_d at fwalk
            with Dissolve (0.2)
            pause 1

            "바토는 마법에 관련된 얘기라 그런지 평소보다 활기차게 말을 이었다. 그는 자연스럽게 [pl_name]의 손을 덥석 잡고는 미세한 마력을 흘려 넣었다." id c02_0274
            
            #마력 불어넣는 이펙트 짧게
            play sound "effect/flash_fast.mp3" volume 0.25    
            show flash_blue at flash_fast
            pause 0.95
            hide flash_blue at flash_fast

            c "(역시 손이 크네.)" id c02_0275
            
            hide staff_d
            show bear out_u talk
            show staff_u at change(1.22, 0, 135)
            with dissolve

            b "\"이게 1 도데카에요. 아, 아닌가... 나는 두 배로 써야 정상으로 나오려나? 아무튼 아주 작은 단위라서 기초 마법도 5 도데카 이상은 쓰고 그래요.\"" id c02_0276
            
            b "\"술식에 따라 다르지만 보통... 앗!\"" id c02_0277

            hide staff_u
            show staff_d at change(1.22, 0, 135)
            show bear out_d shy
            with dissolve
            play sound "effect/footstep.mp3" volume 0.85
            show bear at bwalk
            show staff_d at bwalk

            c "바토는 내 손을 꽉 잡고 있다가 자신이 뭘 하고 있는지 뒤늦게 알아차리고 후다닥 손을 뗐다. 하얀 얼굴에 홍조가 보이는 것 같다." id c02_0278

            c talk "\"하하, 알려줘서 고마워. 그래도 {color=#ee3939}'마력 누수'{/color} 자체는 그대로니까 시술을 맹신하면 안 돼.\"" id c02_0279

            show bear base
            with dissolve


        "대충 아는 척 넘어간다.":

            c talk "\"뭐, 괜찮다니 다행이네.\"" id c02_0280

            c base "마탑의 교육을 받지 못한 나는 그 용어가 일종의 단위인 것은 눈치챘지만 더 궁금해하지 않았다. 바토는 내 말에 수줍게 고개를 끄덕였다." id c02_0281

            hide bear
            hide staff_u
            show bear out_d shy
            show staff_d
            with dissolve

            c talk "\"그래도 {color=#ee3939}'마력 누수'{/color}는 여전하니까 시술을 맹신하면 안 돼.\"" id c02_0282

    c base "나는 바토에게 혹시 모를 상황을 위한 마나 물약을 하나 쥐여줬다." id c02_0283

    show mana_potion :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    c "마법사라면 쓸 필요가 없는 수준의 물건이지만 바토의 상태가 상태다 보니 일종의 비상식량 같은 개념으로 챙기게 했다." id c02_0284

    hide mana_potion
    with dissolve
    pause 0.5
    hide staff_d
    show bear out_u talk
    show staff_u
    with dissolve
    
    b "\"정말, 고마워요. 형...\"" id c02_0285

    hide staff_u
    show bear out_d base
    show staff_d
    with dissolve
    
    c talk "\"이 정도는 별거 아닌걸. 오늘 휴일일 텐데 푹 쉬어.\"" id c02_0286
    
    hide bear
    hide staff_d
    with dissolve

    c base "나는 바토의 어깨를 가볍게 두드리며 배웅했다. 지금은 동생 같은 수인이지만, 언제 무엇이 달라질지 모르는 우리의 관계에 조금 걱정되기도 한다." id c02_0287
    
    c "처음부터 의도치 않게 비밀을 공유한 관계란 아직 열어보지 않은 상자 같은 것이다." id c02_0288

    c "바토와 처음 만난 날, 바로 내 가게에서 바토는 마력이 고갈되어 쓰러졌다. 그때를 떠올리면 지금도 정신이 아찔해진다." id c02_0289

label bear_past:
    
    scene bg shop_past with Fade(0.8, 0.8, 0.8)

    show bear out_d
    show staff_d
    with dissolve

    $ unlock_info_tag(1, "4")
    $ display_text = _("정보 : 마탑")
    show screen affection_indicator

    "그날 {color=#ee3939}'마탑'{/color}에서 마법사가 와서 가게를 검사한다는 건 알고 있었다. 당연히 문제가 될 물건들은 전부 치워두었으니, 아무 문제도 없었다." id c02_0290

    play sound "audio/effect/body_drop.mp3"  volume 0.8
    show bear pain at down
    show staff_d at down
    with hpunch

    "진짜 문제는 가게를 검사하던 바토가 갑자기 쓰러져버린 것이다."  id c02_0291

    scene bg home_past with Fade(0.8, 0.8, 0.8)

    # 주인공 방
    "[pl_name][josa_eun_neun] 바토를 부축해서 방에 눕혔으나 상태는 계속 나빠지기만 했다. 딱히 보이는 상처가 없어서 [pl_name][josa_i_ga] 고민하는 순간 바토가 말했다." id c02_0292

    show bear out_u pain at down
    show staff_u at down
    with dissolve
    
    b "\"마력을 다 써서, 조금만 쉬면, 나아질 겁니다...\"" id c02_0293
    
    c talk "\"아니 쓰러질 때까지 마법을 쓰는 마법사가 어디 있어요!\"" id c02_0294
    
    c base "어이가 없어서 나는 거의 화를 내듯 소리쳤다." id c02_0295
    
    show bear embrass3
    with dissolve

    "[pl_name][josa_i_ga] 바토의 가슴에 손을 턱 얹자 당황한 바토는 어버버거리며 이상한 소리를 냈다." id c02_0296
    
    "[pl_name][josa_eun_neun] 그대로 바토의 심장을 향해 마나를 쏟아부었다." id c02_0297

    #마나 주입하는 이펙트 길게

    play sound "effect/flash.mp3" volume 0.2    
    show flash_blue at flash
    pause 2.5
    hide flash_blue at flash

    show bear embrass
    with vpunch
    b "\"헉!!\"" id c02_0298
    
    "바토가 물에서 나온 물고기처럼 펄떡거렸지만 [pl_name][josa_eun_neun] 그냥 무시했다. 어느 정도 마나를 불어넣고 손을 떼자, 바토는 벌떡 일어나서 [pl_name]에게 다가왔다." id c02_0299

    show bear embrass2 at normal
    show staff_u at normal
    with dissolve 
    
    b "\"이, 이건 절대 비밀입니다. 현장에서 쓰러진 것까지 들키면!...\"" id c02_0300
    
    c talk "\"일단 진정해요. 방금 쓰러졌던 사람이...\"" id c02_0301


    play sound "audio/effect/body_drop.mp3"  volume 0.8
    hide staff_u
    show bear out_d at down
    show staff_d at down
    with hpunch
    pause 0.5
    show bear sigh
    with dissolve
    
    "바토는 침대 위에 털썩 앉아 침울한 얼굴을 했다." id c02_0302
    
    c "\"처음 봤을 때부터 생각했지만 저랑 비슷한 나이대죠? 마탑 소속으로 일하는 정도면 졸업도 했을 테고.\"" id c02_0303

    show bear base
    with dissolve
    
    "바토는 [pl_name][josa_eul_reul] 올려보다가 작게 고개를 끄덕였다." id c02_0304

    hide staff_d
    show bear out_u talk
    show staff_u at down
    with dissolve
    
    b "\"21살입니다. 졸업은 3년 전에...\"" id c02_0305

    show bear base
    with dissolve
    
    c ddam2 "\"뭐?\"" id c02_0306
    
    c base "바토가 내 생각보다 더 어려서 깜짝 놀랐다. 젊은 나이에 마탑을 졸업한 엘리트라고 생각하긴 했지만, 그래도 갓 졸업한 신참 정도로 생각하고 있었다." id c02_0307
    
    c "(오히려 경력으로 따지면 나보다 선배잖아... 물론 선후배 따질 관계는 아니지만.)" id c02_0308

    show bear embrass4
    with dissolve
    
    c "내 놀란 표정에 쑥스러웠는지 바토는 고개를 숙여버렸다. 나는 어색한 분위기를 깰 겸 짐짓 친근한 척을 했다." id c02_0309
    
    c laugh "\"아, 동생일 줄은 예상하지 못해서. 하하... 나는 24살인데, 그냥 편하게 불러.\"" id c02_0310

    hide staff_u
    show bear out_d talk
    show staff_d at down
    with dissolve
    
    b "\"그, 그럼, 저... '형'이라고 불러도 될까요?\"" id c02_0311

    show bear base
    with dissolve
    
    c base "바토의 올려다보는 눈망울이 왠지 초롱초롱하게 느껴진다. 귀여운 동생 같아서 하마터면 자연스럽게 머리를 쓰다듬을 뻔했다." id c02_0312
    
    c "나는 정신을 차리고 바토를 진정시키기로 했다." id c02_0313
    
    c talk "\"그래. 바토라고 했지? 뭔가 숨기고 싶은 게 있나 본데, 어차피 난 마탑에 아는 사람 없으니 너무 걱정하지 마.\"" id c02_0314

    hide staff_d
    show bear out_u talk
    show staff_u at down
    with dissolve
    
    b "\"에? 그럼, 마법적 지식은 어떻게...\"" id c02_0315

    hide staff_u
    show bear out_d base
    show staff_d at down
    with dissolve

    c "\"스승님이 있어. 좀 특이하지만, 스승으로는 아주 좋은 분이야.\"" id c02_0316

    show bear embrass4
    with dissolve

    "바토는 잠깐 고민하다가 입을 열었다." id c02_0317

    hide staff_d
    show bear out_u talk
    show staff_u at down
    with dissolve

    b "\"형이라면... 왠지 말할 수 있을 것 같아요.\"" id c02_0318

    scene bg home_past with Fade(0.8, 0.8, 0.8)

    "바토는 9살에 마탑의 시험에 합격했다. 당연히 천재라는 소리가 따라붙었지만, 언제부턴가 마법을 쓰면 제대로 된 위력이 나오지 않게 되었다." id c02_0319
    
    "술식과 시전에 문제가 없는데도 마나가 자꾸 새어나가는 문제에 그는 '마력 누수'라는 이름을 붙였다." id c02_0320
   
    "처음에는 그냥 마력을 더 많이 써서 해결했지만, 당연히 그런 방식에는 한계가 찾아오기 마련이다." id c02_0321
    
    "바토의 별명은 마탑의 엘리트에서 반쪽짜리 마법사까지 점점 추락했다." id c02_0322
   
    "결과만 중요하게 여기는 마탑에서 좋은 취급을 받기 위해, 바토는 전문 분야까지 바꾸며 빨리 졸업했다." id c02_0323
    
    "졸업 후에도 다른 마법사들이 하기 싫어하는 일을 도맡아 하며 성과는 인정받았지만, 그럴수록 바토는 마력에 허덕였다." id c02_0324

    show bear out_u base
    show staff_u
    with dissolve
    pause 0.5
    show bear sigh
    with dissolve

    b "\"그래도 잘 버텼다고 생각했는데...\"" id c02_0325

    show bear base
    with dissolve

    c talk "\"이 정도로 마나가 부족하면 회복도 느릴 수밖에 없어.\"" id c02_0326

    c consider "나는 한 가지 생각이 떠올랐다. 누수 자체를 고칠 순 없겠지만, 새어나간 마나를 곧바로 흡수할 수 있게 만드는 방법이 있을 것이다." id c02_0327
    
    c base "머릿속에서 술식을 떠올리며 나는 말을 꺼냈다." id c02_0328
    
    $ unlock_info_tag(1, "5")
    $ display_text = _("정보 : 시술")
    show screen affection_indicator

    c talk "\"마력 {color=#ee3939}'시술'{/color}로 회복을 빠르게 만들면 어떨까? 각인을 새기는 방식으로...\"" id c02_0329

    show bear talk
    with dissolve

    b "\"그, 시술... 이요?\"" id c02_0330

    hide staff_u
    show bear out_d base
    show staff_d
    with dissolve

    c talk "\"응. 마법사가 하기엔 좀 그런가?\"" id c02_0331

    c base "몸에 술식을 새기는 것은 특정 마법을 쉽고 빠르게 반복 사용하기 위한 지름길이다." id c02_0332
    
    c "세련된 마법 기술을 연구하는 마탑 소속 마법사라면, 이런 시술은 저급한 수단으로 생각할 수 있다." id c02_0333
    
    "[pl_name][josa_eun_neun] 간단하게 원리를 설명했다." id c02_0334
    
    c talk "\"마력 누수가 발생하는 즉시 새어나간 마나를 붙잡아서 심장으로 돌려보내는 거야.\"" id c02_0335
    
    $ unlock_info_tag(1, "6")
    $ display_text = _("정보 : 아티팩트")
    show screen affection_indicator

    c "\"외부에서 마나를 강탈할 필요도 없고 {color=#ee3939}'아티팩트'{/color}같은 물건도 필요 없이 자기 마나로 해결할 수 있어.\"" id c02_0336
    
    c "\"물론 누수 자체를 해결하진 못하겠지만...\"" id c02_0337

    show bear embrass3
    with dissolve
    pause 0.5
    show bear embrass4
    with dissolve
    
    "바토는 뭔가 고민하는 표정이었다." id c02_0338

    c consider "(역시 마법사 체면에 좀 그런가?)" id c02_0339

    hide staff_d
    show bear out_u talk
    show staff_u
    with dissolve

    b "\"할게요. 시술.\"" id c02_0340

    show bear base
    with dissolve

    "무언가 굳게 결심한 바토의 표정은 [pl_name]의 대답에 곧바로 무너졌다." id c02_0341

    c talk "\"그럼 옷 좀 벗어볼래?\"" id c02_0342

    hide staff_u
    show bear out_d embrass
    show staff_d
    with hpunch
    b "\"버, 벗어요?!\"" id c02_0343
    
    c "\"응! 아... 로브만.\"" id c02_0344

    show bear shy 
    with dissolve
    pause 0.5
    show bear at down
    show staff_d at down  
    with ease

    "[pl_name][josa_eun_neun] 얼굴이 시뻘게진 바토를 의자 위에 앉게 했다." id c02_0345
    
    "바토는 우물쭈물하다가 로브의 매듭을 풀었다." id c02_0346

    play sound "audio/effect/takeoff.mp3" volume 0.65
    hide staff_d
    show bear upnake_d
    with dissolve
    
    c base "로브를 벗자 드러난 바토의 몸은 묵직한 돌덩이 같았다. 목에 난 검은 갈기털 아래에는 대리석 같은 흰 털이 가득했다." id c02_0347
    
    c "바토의 어깨와 팔은 숙련된 용병들 못지않은 근육으로 울퉁불퉁했다." id c02_0348
   
    c "반면 가슴과 배는 동그랗고 말랑해 보인다. 바토는 벗은 로브를 가지런하게 정리해서 무릎 위에 올려놨다." id c02_0349
   
    c "내가 바토의 뒤에 서서 등에 손을 대자, 바토는 흠칫 놀라며 숨을 들이켰다." id c02_0350

    show bear upnake_u embrass
    with vpunch

    b "\"히익!...\"" id c02_0351
   
    c consider "(왜 내가 나쁜 짓을 하는 것 같지...)" id c02_0352
   
    show bear upnake_d embrass4
    with dissolve

    c base "커다란 덩치가 무색하게 바토는 곧 잡아먹힐 동물처럼 긴장했다. 바토의 넓은 등은 탄탄한 근육이 느껴지면서도 부드럽고 폭신했다." id c02_0353
    
    c "짧은 털의 촉감이 너무 좋아서 손을 뗄 수가 없다." id c02_0354
    
    c "마치 사람만큼 커다란 곰 인형을 쓰다듬고 있는 것 같았다. 뒤에서 보이는 동그란 귀가 왠지 귀엽게 느껴졌다." id c02_0355
    
    c "다른 곳의 감촉은 어떨까 궁금했지만, 나는 뒤늦게 정신을 차리고 말했다." id c02_0356
   
    c talk "\"마력이 어떻게 새어 나오는지 측정해 볼게. 가벼운 마법 아무거나 써볼래?\"" id c02_0357
   
    show bear upnake_u base
    with dissolve

    "바토는 쭈뼛대다가 탐지 마법을 펼쳤다." id c02_0358

    hide bear
    play sound "effect/flash.mp3" volume 0.2
    show magic_circle at magic_up
    show bear upnake_u at down   
    show flash_blue at flash
    pause 2.5
    hide flash_blue at flash
    
    "바토를 중심으로 바닥에 푸른 마법진이 생기더니 곧바로 마법진째 녹아내려 빛 덩어리가 되었다." id c02_0359
    
    "그 빛은 순식간에 푸른 파도처럼 일렁이다가 방 밖으로 사라졌다." id c02_0360
    
    "차원이 다른 사용법에 [pl_name]의 입이 딱 벌어졌지만, 지금은 집중해야 할 일이 있다." id c02_0361
   
    c consider "\"음, 좌우로 퍼지는구나. 예상대로 금방 사라지네. 흠...\"" id c02_0362
   
    "결과를 머릿속에서 정리하는 동안 바토는 물끄러미 [pl_name][josa_eul_reul] 바라보았다." id c02_0363
   
    c talk "\"좋아. 어떻게 각인할지 떠올랐어.\"" id c02_0364
   
    "[pl_name][josa_eun_neun] 창고에서 시술에 쓸 재료들을 가져왔다." id c02_0365
    
    "일반적인 문신과 다르게 마력 각인은 마나가 잘 통하는 재료를 쓰는 게 중요하다. 보석 가루, 연금용 정제수, 촉매로 쓸 마석과 액화 미스릴로 마법 잉크를 즉석 제조했다." id c02_0366
    
    "방에서 기다리던 바토는 왠지 덩칫값 못하는 자세로 쭈그린 채 [pl_name][josa_i_ga] 재료들을 섞는 걸 구경했다." id c02_0367

    show bear talk
    with dissolve
   
    b "\"잘, 부탁드려요...\"" id c02_0368

    show bear upnake_d base
    with dissolve
   
    c base "나는 바토의 하얀 털 위에 그림 그리듯 잉크를 칠했다." id c02_0369
    
    show bear upnake_u embrass
    with dissolve

    c "손가락이 닿을 때마다 바짝 긴장한 바토가 움직이지 않으려고 하는 게 느껴진다." id c02_0370
    
    c "사실 내가 하는 마법 시술은 보통의 마법진처럼 오차 없이 정교할 필요가 없다. 바토가 불쌍하니 최대한 빨리 끝내기로 했다." id c02_0371
   
    c talk "\"이제 마력으로 각인하면 끝!\"" id c02_0372

    play sound "effect/magic.mp3" volume 0.7
    show bluelight at magic
    pause 0.2
    hide bluelight
    pause 0.5
   
    c base "마력을 살포시 불어넣자, 마법 잉크는 바토의 몸속으로 사라졌다. 눈에 보이지 않지만, 존재는 확실히 느낄 수 있었다." id c02_0373

    c talk "\"어때?\"" id c02_0374

    show bear out_u
    show staff_u at down
    with dissolve
    pause 0.5
    hide staff_u
    show bear out_d embrass4 at down
    show staff_d at down
    with dissolve
    pause 0.8
    show bear at normal
    show staff_d at normal
    with ease
  
    c base "바토는 다시 로브를 걸치고 손을 꼼지락거렸다. 몸에 술식이 새겨진 느낌은 좀 특이한 감각일 것이다." id c02_0375

    hide staff_d
    show bear out_u talk
    show staff_u
    with dissolve
  
    b "\"아... 이런 느낌이구나.\"" id c02_0376

    show bear base
    with dissolve

    "바토는 손 위에 마력을 모았다가 거대한 마법진으로 변형시켰다. 마법진은 곧바로 사라졌으나 주변이 쥐 죽은 듯 고요해졌다." id c02_0377
  
    hide bear
    hide staff_u
    play sound "effect/flash.mp3" volume 0.2
    show magic_circle at magic_up
    show bear out_u
    show staff_u
    show flash_blue at flash
    pause 2.5
    hide flash_blue at flash

    #장면 전환
    scene bg home2 
    show bear out_u
    show staff_u
    with Fade(0.2, 0.0, 0.5, color = '#fff')
    stop music fadeout 2.5    

    c ddam2 "\"뭐, 뭐야?\"" id c02_0378

    show bear talk
    with dissolve
  
    b "\"혹시 몰라서 결계를 쳤어요. 형... 형이 그 {color=#ee3939}'불법 시술'{/color}을 하는 사람이죠?\"" id c02_0379

    show bear base
    with dissolve
  
    c base "정곡을 찔렸다. 하지만 나는 반사적으로 모른 체를 했다." id c02_0380
   
    c talk "\"불법이라니, 방금 새긴 게 어떤 원리인지는 네가 더 잘 알텐데?\"" id c02_0381

    hide staff_u 
    show bear out_d talk
    show staff_d
    with dissolve 
  
    b "\"맞아요. 그래서 눈치챘어요. 술식은 전부 평범하지만, 근본적으로 이거 '마법'이 아니죠?\"" id c02_0382

    show bear base
    with dissolve
  
    c ddam "두 번이나 비밀을 들켜서 심장이 철렁했다. 식은땀이 삐질삐질 나지만 최대한 뻔뻔하게 굴었다." id c02_0383
   
    c ddam2 "\"그렇긴 한데, 딱히 금지된 것도 아니잖아? 그냥 마나를 쓰는 방법이 특이해서...\"" id c02_0384

    hide staff_d
    show bear out_u talk
    show staff_u 
    with dissolve
   
    b "\"특이하긴 하죠. 마나를 제물로 {color=#ee3939}'주술'{/color}을 사용하는 사람이...\"" id c02_0385

    show bear base
    with dissolve
   
    ## 긴박한 BGM
    play music "cool-determine-hip-hop-trap-crime-dramatic-sports-music-21122.mp3" volume 0.65 fadein 2.5

    c consider "결국 나는 말문이 막혔다. 대체 어디까지 알고 있는 거지?" id c02_0386
    
    $ unlock_info_tag(1, "7")
    $ display_text = _("정보 : 주술")
    show screen affection_indicator

    c base "내가 스승님에게 배운 것은 마법 뿐만이 아니라 {color=#ee3939}'주술'{/color}도 있었다. '주술'은 마법 이전부터 존재하던 고대의 기술로, 이제는 사용할 줄 아는 사람이 거의 없다." id c02_0387
    
    c "제물을 사용하면 강력한 효과를 얻을 수 있기에, 나는 중요한 일에 주술을 이용하곤 했다." id c02_0388
  
    b "\"그리고 방금 탐지 마법으로 마을 밖에 궤짝을 놓고 온 것도 알아냈어요. 내용물까진 모르겠지만... 들키면 안 되니 숨긴 거죠?\"" id c02_0389
  
    with vpunch
    c ddam2 "(헉!!)" id c02_0390

    c ddam "식은땀이 아니라 진땀이 줄줄 흘렀다. 숨겨놓은 특제 회복 물약까지 들키면 정말로 끝장이다." id c02_0391
    
    c "꼬리가 길면 밟힌다더니 결국 마탑에 잡혀가는구나... 눈앞이 캄캄해지고 다리에 힘이 풀려 쓰러질 것 같았다." id c02_0392

    play sound "effect/footstep.mp3" volume 0.85
    show bear at fwalk
    show staff_u at fwalk
    with Dissolve (0.2)
    
    c "갑자기 바토가 내 손을 덥석 잡아서 이대로 즉시 연행되는 건가 생각했다." id c02_0393

    stop music fadeout 2.5
    pause 1.2
    hide staff_u
    show bear out_d talk
    show staff_d at change(1.22, 0, 135)
    with dissolve
    
    # BGM 복귀
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40
    b "\"차라리 형이라서 다행이에요. 어차피 한 배를 탄 사이니까, 마탑에는 비밀로 할게요.\"" id c02_0394

    show bear base
    with dissolve
  
    c base "전혀 예상하지 못한 말에 나는 얼빠진 대답을 했다." id c02_0395
  
    c talk "\"어? 그, 그래...\"" id c02_0396


    hide staff_d 
    show bear out_u talk
    show staff_u at change(1.22, 0, 135)
    with dissolve
  
    b "\"너무 걱정하지 마요. 마탑 측에서 이런 일을 추적하는 건 저밖에 없으니까.\"" id c02_0397

    show bear base
    with dissolve
  
    c "\"고생이 많네...\"" id c02_0398
    
    c base "나는 아무 말이나 반사적으로 내뱉었다. 짧은 시간에 너무 많은 감정이 휘몰아쳐서 오히려 멍청해진 기분이었다." id c02_0399
    
    c "나는 혼이 쏙 빠진 채로 멍하니 있다가 바토가 꽉 쥔 손이 저려서 정신을 차렸다." id c02_0400
    
    c talk "\"아, 고마워. 정말, 어떻게 되는 줄 알았어...\"" id c02_0401

    show bear talk
    with dissolve
    
    b "\"그건 제가 할 말이에요. 형은 목숨의 은인이나 마찬가지인걸요.\"" id c02_0402

    hide staff_u
    show bear out_d base
    show staff_d at change(1.22, 0, 135)
    with dissolve
    
    c base "바토는 또다시 동생 같은 눈빛으로 나를 바라보았다. 정신 조작 계열 마법이 아닌가 의심될 정도로 강력한 귀여움에 나는 결국 패배했다." id c02_0403
    
    c happy "자연스럽게 바토의 머리를 쓰다듬고 나서야 풀려날 수 있었다. 오늘 처음 만난 사이에 좀 과한 스킨쉽 아닌가 싶지만 아무렴 어때." id c02_0404

    hide staff_d 
    show bear out_u happy
    show staff_u at change(1.22, 0, 135) 
    with dissolve
    
    b "\"그럼... 다음에 또 올게요.\"" id c02_0405
    
    "바토는 행복한 미소를 지으며 돌아갔다." id c02_0406
    
    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    
    c base "그렇게 바토와 만난 첫날은 폭풍과 같이 지나갔다. 그 뒤로 바토는 가끔씩 가게에 찾아와서 각인을 점검받거나 소소한 수다를 떨거나 했다." id c02_0407
    
    c "처음엔 혹시 나를 방심시키려는 계획이 아닐까 했는데, 바토는 정말로 나를 동료나 친구로 생각하는 것 같았다." id c02_0408
    
    c "나는 기회를 놓치지 않고 바토를 구슬려 마탑의 {color=#ee3939}'물약 공증문서'{/color}까지 받아냈다. 덕분에 가게는 지금까지 아주 잘 나가는 중이다." id c02_0409
    
    # (바토 키워드2 : 공범?)

    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    
    c consider "(음... 가헬도 없으니, 오늘은 일찍 닫을까?)" id c02_0410
    
    c base "잡생각이 너무 많았는지 괜히 한 것도 없는데 피곤한 기분이었다. 나는 평화로운 하루에 감사하며 가게를 정리했다." id c02_0411

    stop music fadeout 2.5

label bear_lab:

    # 개인실 배경
    scene bg magic_lab with Fade(0.8, 0.8, 0.8)
    play music "science-documentary-169621.mp3" fadein 2.5 volume 0.5

    "바토는 [pl_name]의 가게에서 나온 뒤, 곧바로 마탑에 있는 자신의 연구실로 향했다." id c02_0412
   
    "사실 대부분의 마법사들은 자신의 방에 처박혀서 절대 나오지 않거나, 정반대로 완전히 방치하고 잡동사니 창고로 쓰거나 했다." id c02_0413
  
    "이렇게 화려하게 꾸며놓은 마법사는 바토밖에 없을 것이다." id c02_0414

    show bear out_u
    show staff_u
    with dissolve
    pause 0.5
    play sound "audio/effect/takeoff.mp3" volume 0.65
    hide staff_u
    show bear am_d talk
    with dissolve

    b "\"휴...\"" id c02_0415

    show bear base
    with dissolve
    pause 0.5
    show bear at down
    with ease
        
    "바토는 한숨을 쉬며 침대 위에 걸터앉았다. 오늘은 [pl_name]의 말대로 푹 쉴 생각이었다." id c02_0416
    
    "모든 마탑의 마법사들이 그러하듯 바토의 연구실은 자신의 취향에 맞게 개조되어 있다." id c02_0417
    
    "바토가 살던 고향의 저택처럼 고급 가구들로 채워놓은 방은 여느 귀족의 서재 못지않게 화려해 보였다." id c02_0418
    
    "바닥에 깔린 카펫은 왕국 인기 재단사의 최신 작품이고, 소파는 다른 귀족들도 탐낼 최고급 물건이다. 바토의 집안이 얼마나 유복한지 엿볼 수 있는 부분이다." id c02_0419
    
    b "(우선 씻고 낮잠이라도 잘까...)" id c02_0420
    
    scene bg bathroom with Fade(0.8, 0.8, 0.8)
    
    "바토는 알몸으로 거울 앞에 서서 자기 모습을 바라봤다." id c02_0421
    
    "남들보다 두툼한 팔근육과 달리 미묘하게 작은 키는 바토의 콤플렉스다. 다른 수인들 옆에 서면 살짝 낮은 눈높이 때문에 다들 바토를 내려다보게 된다." id c02_0422

    $ unlock_character_image("bear", "bear b_no nake0_d")
    $ display_text = _("이미지 : 바토(알몸)")
    show screen affection_indicator
    show bear nake0_d
    with dissolve
  
    b "(키는 더 안 크려나...)" id c02_0423
 
    "머릿속으로 키가 훌쩍 커진 자기 모습을 상상하자 왠지 체형도 다른 느낌으로 바뀌었다." id c02_0424
    
    "기사단의 수인들처럼 열심히 훈련한 미래의 자신은 배가 둥글게 나오지도 않았고 키도 훤칠하니 누구에게나 인기 있을 느낌의 청년이었다." id c02_0425

    show bear nake0_u sigh 
    with dissolve
    
    "그러나 거울 속에 보이는 자신의 모습을 보자 곧바로 한숨부터 나왔다. 애초에 외모가 바뀐다고 상황이 바뀔 것 같진 않았다." id c02_0426

    b "(잘생겼다고 마탑주가 되는 건 아니니까.)" id c02_0427

    show bear nake0_d base
    with dissolve

    "마탑에서는 더 많은 이득을 가져가기 위해 학파 간의 영향력 싸움이 치열하다. 마치 왕정에서 귀족들의 세력 싸움과도 비슷한 느낌이다." id c02_0428
    
    "아니, 마법사 사회는 귀족보다 더 끔찍했다. 마법을 쓰지 못하면 귀족이라도 하찮게 여기고, 마법 연구를 위해서라면 수단과 방법을 가리지 않았다." id c02_0429
    
    "보통 사람들은 마탑이 마법을 가르치는 곳으로 알지만, 마탑의 정규교육은 사실 주요 돈벌이 수단이다." id c02_0430
    
    "동시에 재능있는 마법사를 걸러내 자기 학파에 영입하기 위한 수단이기도 하다." id c02_0431

    "바토가 열심히 일하는 것도 개인의 지위는 물론이고 자신의 학파를 위한 행동이었다." id c02_0432
    
    "무허가 마법 조사관은 '다들 하기 싫어하지만, 누군가는 해야 하는 일'이다." id c02_0433
    
    "그것을 바토가 맡음으로서 바토의 학파가 마탑에서 더 큰 발언권을 가지게 된다." id c02_0434
    
    "모두가 다른 사람을 장기 말로 여기는 사회에서 바토는 간신히 외톨이 신세를 면하고 있었다." id c02_0435

    show bear sigh
    with dissolve
    
    "바토는 우울한 생각에 또다시 한숨을 내쉬었다." id c02_0436
    
    "이러다 하루 종일 한숨만 쉴 것 같아서 얼른 씻기로 했다." id c02_0437

    show bear base
    with dissolve

    "바토의 욕실은 최신 마법 공학으로 만든 실험적인 가구들로 채워져 있다. 마력으로 물을 불러오는 욕조라던가 온도 조절 장치 같은 것은 마탑에서나 볼 수 있는 물건이다." id c02_0438
    
    "바토는 욕조에 앉아 따뜻한 물에 몸을 담그고 잠깐 눈을 감았다. 조금은 마음이 진정되는 기분이었다." id c02_0439

    b "\"좋게 생각하자...\"" id c02_0440

    "어쨌든, 마법사라면 마탑에 소속되는 게 이득이다. 마탑의 대외적인 권위는 물론이고, 무슨 일을 하더라도 마법사는 좋은 대우를 받는 편이다." id c02_0441

    "마법을 쓸 줄 아는 용병이 없는 건 아니지만, '마탑 소속 마법사'와는 취급이 하늘과 땅 차이다." id c02_0442

    "왕실이나 귀족 사회에서도 마탑은 무시할 수 없는 집단이다. 물론 이 미치광이 집단이 언제 어떤 사고를 칠 지 몰라서 견제하는 것이긴 하다." id c02_0443

    "마탑이 족쇄처럼 느껴지긴 해도 마탑에 소속되면 연구하기 좋은 건 사실이다." id c02_0444
    
    "마탑 장서관의 방대한 자료는 다른 곳에서 찾아볼 수 없는, 정말 온갖 정보가 모이는 곳이라 유용하다." id c02_0445
  
    "바토는 최근에 본 '마나 융합 기법을 적용한 형상 변환 마법의 최적화' 논문에 대해 생각하다가 떠오른 게 있었다." id c02_0446
  
    "논문 끝에 형상 변환을 사용한 {color=#ee3939}'자위 도구 제작'{/color}에 대한 공식이 붙어있었는데, 거기에 참고 자료로 첨부된 수인들의 적나라한 교미 장면이 생각났다." id c02_0447

    "바토의 머릿속은 곧바로 그런 이미지로 가득 찼다." id c02_0448

    show bear nake0_d shy
    with dissolve  

    "그런 생각을 하자 곧 그의 자지가 바로 반응하기 시작했다." id c02_0449

    b "(... 자기 전에 한 번 할까?)" id c02_0450

label bear_01:

    menu:
        "아니다. 오늘은 그냥 쉬자.":

            show bear sigh
            with dissolve
            pause 0.5
            show bear nake0_u
            with dissolve
  
            "바토는 그런 생각을 했다는 사실이 부끄러워졌다." id c02_0451
  
            "너무 자주 하는 것도 좋은 생각은 아니겠지. 바토는 괜히 몸 위에 물을 끼얹으며 다른 생각을 했다." id c02_0452
  
            "술식의 최적화를 통해 얼마나 마나를 아낄 수 있는지 암산하다가 목욕을 마쳤다." id c02_0453
            
            scene bg magic_lab with Fade(0.8, 0.8, 0.8)

            "바토는 침대에 누워서 잡생각에 빠져들었다. 권투 같은 육체 훈련을 해야 할지 아니면 마법 연구로 마나를 절약하는 데 집중할지 고민하다가 잠이 들었다." id c02_0454
  
            "바토의 휴일은 그렇게 흘러갔다." id c02_0455

            jump chapter2_end

        "지금이 아니면 언제 하겠어?":
            $ persistent.bear_unlocked[0]= True
            
            jump bear_see_01


label bear_see_01:
    
    $ bear_see += 1
    scene bg bathroom
    show bear nake0_d
    
    show bear nake0_u
    with dissolve


    "바토는 유두로 자위하는 방법을 생각하며 가슴에 손을 가져갔다." id c02_0456
    
    "가볍게 스치는 정도로는 만족할 수 없다. 바토는 자신의 유두를 꼬집고 긁으면서 짜릿한 감각에 빠져들었다." id c02_0457

    show bear nake0_u horny
    with dissolve     
 
    b "\"하아...\"" id c02_0458
    
    $ unlock_character_image("bear", "bear b_no nake_d")
    $ display_text = _("이미지 : 바토(발기)")
    show screen affection_indicator
    show bear nake_u horny
    with Dissolve (1.5)  
 
    "금세 힘이 들어가서 불끈거리는 자지가 물 위로 고개를 내밀었다." id c02_0459
    
    "옅은 분홍빛 귀두는 유난히 통통하게 보였다." id c02_0460
   
    "바토는 손을 뻗어 그것을 잡으려다가 다른 생각이 떠올랐다. 전부터 궁금했던 그것을 해볼 기회였다." id c02_0461

    stop music fadeout 2.5
 
    #여기부터 cg?
    scene bg bear_s1_01 with Fade(0.8, 0.8, 0.8)
    play channel1 "effect/heart_beat.mp3" volume 0.75
    
    "바토는 아직 다른 수인과 몸을 섞어본 적은 없지만, 방법만큼은 잘 알았다. 마탑의 장서관에서 읽은 수많은 정보 덕분에 이론만큼은 누구보다 충실했다." id c02_0462
    
    #알약이미지?

    show bear_s1_pill
    with dissolve

    "깨끗하게 씻고 나온 바토는 미리 준비해 온 특별한 알약을 꺼냈다." id c02_0463

    show bear_s1_02
    show bear_s1_pill
    with dissolve
 
    b nake_d horny2 "\"으응... 읏!\"" id c02_0464

    scene bg bear_s1_01 at scene_vmove(2, 0, -170)
    show bear_s1_02 at scene_vmove(2, 0, -170)
    show bear_s1_pill
    pause 2.5
    play sound "effect/sticky2.mp3" volume 0.7

    "바토는 바닥에 누운 자세로 다리를 벌려 자신의 뒷구멍에 손가락을 넣었다." id c02_0465
    
    hide bear_s1_pill
    with dissolve

    "안쪽 깊은 곳까지 알약을 밀어 넣자, 알약이 부드럽게 녹아내리기 시작했다." id c02_0466

    play sound "effect/sticky.mp3" volume 0.65

    "연금술로 만든 젤이 바토의 속을 질척하게 채운다. 미끌미끌하게 변한 분홍빛 구멍은 손가락 두 개쯤은 쉽게 받아들였다." id c02_0467


    play channel1 "effect/breath.mp3" volume 0.4
    with hpunch
 
    b nake_d horny2 "\"하으읏!...\"" id c02_0468

    play channel2 "effect/sticky3.mp3" volume 0.65
    
    "손가락을 움직일 때마다 찔꺽거리는 소리와 함께 젤이 새어 나온다." id c02_0469
    
    "바토의 구멍은 자신의 두꺼운 손가락도 버거워했다. 이곳에 뭘 넣어 본 경험이 부족한 탓이었다." id c02_0470
 
    b nake_d shy "(여기쯤에 있을 텐데...)" id c02_0471
 
    "바토는 낑낑대며 자신의 구멍 안쪽을 열심히 탐험했다. 전립선을 자극하는 방법은 알지만, 전립선이 자기 몸의 어디에 있는지는 몰랐다." id c02_0472
    
    "이곳저곳을 눌러보다가 가장 그럴듯한 곳을 문지르니 조금 이상한 기분이 들었다." id c02_0473
    
    "상상하던 짜릿한 쾌감과는 좀 거리가 있어서 실망스럽지만, 여기서 멈출 생각은 없었다." id c02_0474

    "바토는 이전에 봤던 논문에 나왔던 {color=#ee3939}'자위 도구 제작'{/color} 공식을 떠올리며 마력 구체를 끌어당겨 마력을 부여 했다." id c02_0475

    play sound "effect/magic.mp3" volume 0.7
    show bluelight at magic
    pause 0.2
    hide bluelight at magic
    pause 0.8
        
    "간단한 남근 모양의 기둥을 만들어낸 바토는 거기에 감각 공유 마법을 걸었다." id c02_0476
    
    "원래는 잘린 팔다리를 대신하는 도구에 사용하는 마법이지만, 방법에 따라 고문이나 성적인 용도로 사용할 수 있다." id c02_0477

    "손에 잡힌 구체는 강철처럼 단단하지만, 바토가 마나를 불어넣자 액체처럼 흐물거리며 모양을 바꿨다." id c02_0478

    "바토는 자위 도구를 보면서 침을 꿀꺽 삼켰다." id c02_0479

    b "...넣어볼까?" id c02_0480

    menu: 

        "자위 도구를 넣는다." :   

            play sound "effect/sticky2.mp3" volume 0.65
            show bear_s1_03 at scene_vmove(0, 0, -170)
            with dissolve
            pause 0.8
            show bear_s1_dilldo
            with dissolve
            pause 0.8
            play sound "audio/effect/heavy_breath.mp3" volume 0.7
    
            "바토가 직접 만든 어른의 장난감을 뒷구멍에 넣자, 약간의 고통과 처음 겪는 쾌락이 동시에 찾아왔다."            


    with vpunch 
 
    b nake_d horny2 "\"허억!!... 후, 흐으읏!\"" id c02_0481
 
    "뚫으면서 동시에 뚫리는 감각은 말로 표현하기 힘든 충격적인 경험이었다. 쾌감이 어느 정도 고통을 상쇄해 줘서 그나마 집어넣을 수 있었다." id c02_0482
    
    "가짜긴 해도 처음으로 뒤에 넣어지는 것은 쉽지 않았다. 바토는 손가락으로 할 때와 차원이 다른 감각에 헐떡였다." id c02_0483

    stop sound fadeout 1.5
    
    "겨우 숨을 가다듬고 나서 본격적으로 움직이기 시작하자, 저릿저릿한 느낌에 숨소리조차 내기 힘들었다." id c02_0484
 
    b nake_d horny "(조금만 더 깊이...)" id c02_0485
 
    "장난감을 잡고 움직일 때마다 안쪽을 무자비하게 침범당하는 감각과 동시에, 감각 공유 마법을 통해 전해진 자기 구멍의 조임이 바토의 좆을 마구 쥐어짰다." id c02_0486

    play sound "effect/sticky2.mp3" volume 0.65
    play channel1 "effect/fast_breath.mp3" volume 0.45 fadein 1.5
    
    "구멍의 질척거리는 소리와 바토의 허덕이는 숨소리만이 방 안에 울려 퍼진다." id c02_0487
    
    "감당하기 벅찬 느낌에 가쁜 숨을 내쉬면서도, 바토는 본능적으로 더 강한 쾌감을 찾아 헤맸다." id c02_0488
    
    "살짝 더 안쪽의 어딘가를 강하게 누르면 이 답답함이 해소될 것 같다. 바토는 움직임을 잠깐 멈추고 다른 방법을 고민했다." id c02_0489

    hide bear_s1_dilldo
    with dissolve
 
    b nake_d shy "\"... 이것보다 더 커야 하나?\"" id c02_0490
 
    "바토는 자신이 만든 장난감이 너무 작은 건 아닌지 진지하게 고민했다." id c02_0491
    
    "분명히 책에서 말한 '초심자 추천' 크기에 맞춰서 만든 것 같은데, 무의식중에 겁이 나서 크기를 줄였을지도 모른다." id c02_0492


    show bear_s1_dilldo
    with dissolve
    pause 0.8 
    show bear_s1_04 at scene_vmove(0, 0, -170)
    hide bear_s1_dilldo
    play channel2 "effect/sticky3.mp3" volume 0.65
    show bear_s1_dilldo
    with dissolve
    pause 0.8
    show bear_s1_dilldo2
    with dissolve


    "바토는 장난감에 손을 대고 다시 마나를 써서 형태를 바꾸기로 했다. 이번에는 좀 더 크고 길쭉한 걸로, 모양도 신경 써서 더 '진짜' 같이 만들었다." id c02_0493
    
    "바토가 한 가지 간과한 것은, 장난감을 뒷구멍에서 빼지 않고 그대로 마법을 사용한 것이다." id c02_0494
    
    "다시 말해 장난감이 자신의 뒷구멍 속에서 마구 커지는 것과 동시에, 감각 공유로 자지까지 무시무시한 자극을 당하는 것이다." id c02_0495

    hide bear_s1_dilldo
    hide bear_s1_dilldo2
    play sound "audio/effect/sqz2.mp3" volume 0.7
    show bear_s1_05 at scene_vmove(0, 0, -170)
    with dissolve
    pause 0.2
    with vpunch
 
    b nake_d horny3 "\"크읏, 아, 아흐으으으으윽!!... 그어어어어!!\"" id c02_0496

    scene bg bear_s1_01 at scene_vmove(2, -170, 0)
    show bear_s1_05 at scene_vmove(2, -170, 0)
    pause 2.5
 
    "말로 표현하기 힘든 폭력적인 감각에 바토는 신음을 흘리다가 아예 짐승의 소리를 냈다." id c02_0497
    
    "좋고 싫음을 구분할 수 없는 강렬한 자극에 몸을 덜덜 떨었다. 눈물도 찔끔 흘린 것 같지만 그것보다 사정의 쾌감이 짜릿하게 느껴졌다." id c02_0498
    
    "정작 바토의 남근에선 정액이 나오지 않았다." id c02_0499

    play sound "audio/effect/sqz1.mp3" volume 0.7
    pause 0.5
    with hpunch
    pause(0.8)
    
    "계속되는 절정의 감각에 휩쓸려 정액을 싸는 기분이 들었지만, 바토의 분홍빛 자지는 투명한 전립선액을 뱉을 뿐이었다." id c02_0500
    
    "처음 경험하는 전립선 오르가즘은 정말 이상하면서도 중독적인 느낌이었다." id c02_0501

    play channel1 "effect/breath.mp3" volume 0.4
 
    b nake_d horny2 "\"허억... 후우, 하윽!\"" id c02_0502
 
    "육체는 이미 쾌락에 휩쓸려 절정을 시작했지만, 정신은 이제부터가 진짜 시작이라는 듯 불이 붙었다. 과거에 했던 자위는 그냥 잠깐의 손장난에 불과했다." id c02_0503
    
    "황홀한 감각에 녹아내리던 바토는 지금 자신의 뒤를 꽉 채운 물건이 진짜였으면 하는 마음이 들었다." id c02_0504
    
    "자료로 본 수인들의 교미 장면에서, 힘차게 자지를 박아 넣는 말 수인과 쾌감에 울부짖는 사자 수인의 모습이 생각났다." id c02_0505
 
    b "(괜히 우는 게 아니었구나...)" id c02_0506
 
    "참고 싶어도 참을 수 없는 체험을 해보니 이제 이해가 간다. 오히려 그렇게 짐승처럼 울부짖고 싶은 욕구가 심장을 뜨겁게 달군다." id c02_0507
    
    "욕망에 이끌린 바토는 장난감에 다른 마법을 걸었다. 난폭하게 구멍을 유린당하는 기분을 느끼고 싶어서 장난감이 자동으로 움직이게 했다." id c02_0508

    play channel2 "effect/sticky.mp3" volume 0.65
    show bear_s1_dilldo2
    with dissolve
    show bear_s1_dilldo
    with dissolve
    hide bear_s1_dilldo2
    show bear_s1_dilldo2
    with dissolve
    hide bear_s1_dilldo
    play channel1 "effect/sticky3.mp3" volume 0.65
    show bear_s1_dilldo
    with dissolve
    hide bear_s1_dilldo2
    show bear_s1_dilldo2
    with dissolve
    pause 0.5
    play sound "audio/effect/heavy_breath.mp3" volume 0.75

    "그리고 바토는 그 결정을 곧바로 후회했다." id c02_0509

    with hpunch
 
    b nake_d horny3 "\"윽, 앗! 하으, 잠깐. 으아악! 하응! 크으, 안 돼!\"" id c02_0510
 
    "생각한 대로 뒷구멍이 마구 쑤셔지는 쾌감은 정말 좋았다. 하지만 감각 공유를 해제하는 걸 깜빡한 나머지, 방금 사정한 자지가 강제로 쥐어짜이기 시작했다." id c02_0511
    
    "그것은 바토의 엉덩이가 장난감을 마구 쥐어짠다는 뜻이다." id c02_0512
    
    "굵직한 (가짜) 자지에 꿰뚫린 구멍은 움직임에 맞춰 한껏 벌려졌다가 오므리기를 반복했다." id c02_0513
    
    "바토에게는 조금 과한 크기인지 바토의 엉덩이는 움직이는 장난감을 꽉 물고 놓아주지 않았다." id c02_0514
    
    "쾌락에 충실한 육체는 벌벌 떨면서도 그 모든 감각을 생생하게 받아들였다." id c02_0515
    
    scene bg bear_s1_01
    show bear_s1_06
    play sound "audio/effect/sqz1.mp3" volume 0.7
    with dissolve
    with vpunch
    pause 0.8

    b nake_d horny3 "\"싸...싼다아아앗...!!\"" id c02_0516

    play sound "audio/effect/sqz4.mp3" volume 0.6
    with vpunch
    pause 0.8
     
    "한 차원 높은 절정을 경험한 바토는 얼굴에 튈 정도로 강하게 정액을 분출했다." id c02_0517
    
    "그러나 절정은 모든 정액을 쏟아낼 때까지 끝나지 않았고, 바토의 좆은 투명한 전립선액까지 뿜어댔다." id c02_0518
    
    "바토는 양손으로 자신의 유두를 꼬집으며 황홀경에 빠져들었다." id c02_0519
 
    b "(너무, 너무 좋아!)" id c02_0520

    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.6
    with vpunch
    pause 0.8
 
    "바토는 더 이상 아무것도 나오지 않을 때까지 절정을 계속했다." id c02_0521

    "바닥에 흘러내리는 액체라던가 축축하게 적셔진 털이 뭉치는 것 따위는 신경 쓰지 않고 온전히 자신의 감각에만 집중했다." id c02_0522

    play sound "audio/effect/sqz3.mp3" volume 0.7
    pause 0.4
    with hpunch
    play channel1 "audio/effect/sqz1.mp3" volume 0.7
    pause 0.5 
    with vpunch
    pause 0.4

    b "\"흐으으... 하아아아아아아...\"" id c02_0523

    scene bg bear_s1_01
    show bear_s1_07
    with dissolve
    play sound "audio/effect/slow_breath.mp3" volume 0.6
 
    "겨우 이성을 조금 되찾은 바토는 자신의 뒤에 꽂혀있던 장난감을 뽑아냈다." id c02_0524
    
    "제멋대로 움직이는 거대한 자지가 약간 징그럽게 느껴지면서도, 이런 게 자신의 속에서 꿈틀거렸다는 사실이 약간 뿌듯하기도 했다." id c02_0525

    show bg bear_s1_01 at scene_vmove(2, 0, -235)
    show bear_s1_07 at scene_vmove(2, 0, -235)
    
    "텅 빈 뒷구멍이 벌름거리는 것을 스스로 느낄 수 있었다. 마음 한구석에서 다시 쾌락을 경험하고 싶은 욕구가 스멀스멀 새어 나왔지만 바토는 이성의 끈을 꽉 붙잡았다." id c02_0526
    
    "바토는 장난감을 원래의 마법 구체로 되돌리고 바닥에 내려놓았다. 이제서야 자신의 털이 엉망으로 뭉쳐진 것을 깨달았다." id c02_0527
 
    b nake_d shy "(이런, 다시 씻어야겠네.)" id c02_0528
 
    "희뿌연 액체로 엉망이 된 바닥까지 전부 청소하려면 꽤 시간이 걸릴 것이다." id c02_0529
    
    "푹 쉬려던 원래의 계획은 전부 엉망이 됐지만, 그 어느 때보다 만족스러운 하루를 즐길 수 있었다." id c02_0530
    
    "바토는 힘이 풀려 후들거리는 다리로 간신히 일어나 화장실로 향했다." id c02_0531
 
    "바토의 휴일은 그렇게 흘러갔다." id c02_0532

    $ renpy.end_replay()


label chapter2_end:
    
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    show wolf am_d
    with dissolve

    "던전에서 겪은 사건 이후로 충분한 휴식을 취한 가헬은 다시 [pl_name]의 상점 일을 돕기 시작했다." id c02_0533
    
    "상품은 적당히 잘 팔렸고 금화는 창고에 차곡차곡 쌓였다. [pl_name][josa_eun_neun] 저축한 돈으로 아티팩트를 하나 구하려고 했지만..." id c02_0534
    
    show wolf am_u talk
    with dissolve

    w "\"더 나중에 줘도 괜찮다.\"" id c02_0535

    show wolf am_d base
    with dissolve
 
    c talk "\"하지만 이미 한 달 미뤘잖아. 상인으로서 내 자존심이...\"" id c02_0536
 
    "가헬에게 계약금으로 지불할 아티팩트를 구해야 하는데, 시중에서 살 수 있는 물건이 없었다." id c02_0537
    
    "물론 돈으로 줄 수도 있지만, 그냥 [pl_name]의 마음에 걸리는 것이었다." id c02_0538
    
    "계약이 항상 완벽하게 지켜지는 것은 아니지만, 어쨌든 계약은 계약이니까 지키려고 노력하는 게 마땅했다." id c02_0539
    
    show wolf am_d talk
    with dissolve

    w "\"무리하지 말고, 어차피 당장 필요한 물건이 아니니까.\"" id c02_0540
    
    show wolf am_d base
    with dissolve

    c talk "\"그래... 조금만 더 기다려볼게.\"" id c02_0541
 
    "[pl_name][josa_eun_neun] 가헬의 말에 결국 현실과 타협하고 말았다." id c02_0542
    
    "사실 아무 아티팩트나 괜찮았다면 당장이라도 하나 구할 수 있었다. 가헬같은 용병과 1년 계약을 할 정도로 '비싼' 아티팩트를 구하지 못해서 문제인 것이다." id c02_0543
 
    "'아티팩트'는 본디 고대의 기술과 마법으로 만들어 강력한 힘을 가진 유물을 지칭하는 말이다." id c02_0544

    "하지만 점차 고대에 만들어지지 않은 물건에도 아티팩트라는 단어가 붙기 시작했다." id c02_0545
    
    "결국 아티팩트의 기능에 따라 등급이 매겨지고 그에 따라 가격이 매겨졌다." id c02_0546

    "비싼 아티팩트는 지금 내 상황처럼 거래 대금으로 활용하기도 하고, 부자들이 과시용으로 구매하기도 한다." id c02_0547
 
    c consider "(그냥 내가 직접 만들어볼까? 아, 아니다...)" id c02_0548
 
    c base "스승님이라면 모를까, 내 실력으로는 그렇게까지 가치 있는 아티팩트를 만들 수 없을 것이다." id c02_0549
    
    c "애초에 내 전문 분야가 아니라서 뭘 어떻게 해야 할지 감이 잡히지 않았다." id c02_0550
 
    c talk "\"스승님이 계시면...\"" id c02_0551
 
    c base "스승님은 강력한 마력을 타고난 용 수인이며 동시에 주술을 자유자재로 사용할 수 있는 숙련된 주술사였다." id c02_0552
    
    c "아티팩트 하나쯤 간단하게 뚝딱 만들어낼 수 있는 사람이지만, 만나고 싶다고 아무 때나 만날 수 없는 게 문제다." id c02_0553
    
    c "아마 지금도 마음대로 전 세계를 떠돌며 사람들을 도와주거나 무언가를 잔뜩 먹고 있을 것이다." id c02_0554
 
    show wolf am_u talk
    with dissolve

    w "\"그보다, 오늘 영업 끝나면 같이 술집에 가는 거 어때. 가볍게 술도 한잔 하고.\"" id c02_0555
 
    c question2 "\"술집?... 굳이?\"" id c02_0556
    
    show wolf am_d sad_am
    with dissolve

    "[pl_name][josa_eun_neun] 술을 자주 마시는 편이 아니라서 가볍게 대답했지만, 가헬은 [pl_name]의 말에 큰 충격을 받은 것 같았다." id c02_0557
    
    "마치 비 맞은 강아지 같은 표정이 된 가헬을 보자 [pl_name][josa_eun_neun] 죄책감이 들기 시작했다." id c02_0558
 
    c consider "(가헬이 데이트 신청한 것도 아닌데... 너무 단칼에 거절했나?)" id c02_0559
    
    show wolf am_d sad2_am
    with dissolve
    
    w "\"가끔은 놀러가는 것도 좋지 않나?...\"" #히잉 표정 유지

    show wolf sad_am
    with dissolve
 
    c ddam2 "\"다, 다음에 가자. 하하...\"" id c02_0560
 
    show wolf am_u sad2_am
    with dissolve

    w "\"... 알았다.\"" id c02_0561

    show wolf am_d sad_am
    with dissolve
 
    c base "내 언행에 익숙한 가헬이라면 내가 대충 둘러댄 것을 알아차릴 것이다. 그러나 가헬은 더 이상 추궁하지 않고 고개를 끄덕였다." id c02_0562
    
    c consider "(아무래도 다음에는 꼭 같이 가야만 할 것 같다...)" id c02_0563
 
    c base "평범하게 흘러가는 하루에 감사함보다 지루함을 느끼기 시작할 때쯤, 또 다른 '사건'이 일어났다." id c02_0564
    
    c "바로 내 스승님이 마법 상점을 찾아온 것이다." id c02_0565

    hide screen book_icon with dissolve
    stop music fadeout 2.5

    jump chapter3