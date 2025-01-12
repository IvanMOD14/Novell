label c5w_start:

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
    show five
    pause 1.0
    
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35
    
    hide chapter_back
    hide chap
    hide ter
    hide five
    with Dissolve (1.5)
    
    $ _skipping = True
            
    show wolf am_d
    with dissolve

    "[pl_name][josa_eun_neun] 1층에서 가게를 청소하고 있는 가헬과 눈이 마주쳤다." id c05_w_0000
    "평소와 같은 아침이지만, \'연인\' 가헬과 함께하는 첫 아침이었다." id c05_w_0001
    "[pl_name][josa_eun_neun] 살짝 어색한 인사를 했다." id c05_w_0002

    c talk "\"안녕.\"" id c05_w_0003

    show wolf talk am_u
    with dissolve

    w "\"잘 잤나.\"" id c05_w_0004

    show wolf base am_d
    with dissolve
    
    c shy2 "\"응...\"" id c05_w_0005

    show wolf shy2
    with dissolve

    "비슷한 생각을 했는지 가헬도 조금 어색하게 얼굴을 붉혔다." id c05_w_0006

    show wolf at fwalk
    play sound "effect/footstep.mp3" volume 0.9
    pause 1.9

    show wolf shy am_u
    with dissolve

    show wolf :
        ease (0.25) xoffset 20
        ease (0.25) xoffset 0

    play sound "effect/short_kiss.mp3" volume 0.5
    "[pl_name]에게 가까이 다가온 가헬은 [pl_name]의 뺨에 가벼운 키스를 했다." id c05_w_0007

    show wolf shy5 
    with dissolve

    w "\"오늘도 잘생겼군.\"" id c05_w_0008

    show wolf happy am_d 
    with dissolve

    c laugh "\"하하...\"" id c05_w_0009

    "[pl_name][josa_eun_neun] 새삼 가헬과 연인이라는 게 신기했다." id c05_w_0010
    "계약한 용병과 사랑에 빠지는 일은 많이 들어봤지만, 자신의 얘기일 줄은 몰랐다." id c05_w_0011
    
    c talk "\"나머지는 내가 할게.\"" id c05_w_0012
    
    "[pl_name][josa_eun_neun] 상품을 진열하다가 연금술 재료가 모자란 게 생각났다." id c05_w_0013
    "원래는 휴일에 잠깐 시장을 갈 생각이었지만, 휴일에는 가헬과 느긋하게 쉬고 싶었다." id c05_w_0014
    "일정을 어떻게 할지 고민하는 사이에 가헬이 먼저 말을 꺼냈다." id c05_w_0015
    
    show wolf talk am_u 
    with dissolve

    w "\"오늘은 잠깐 던전에 갔다 오겠다.\"" id c05_w_0016

    show wolf base am_d 
    with dissolve
    
    c "\"그래.\"" id c05_w_0017
    
    c consider "(음...?)" id c05_w_0018
    
    "[pl_name][josa_eun_neun] 아무 생각 없이 대답했다가 뭔가 위화감을 느꼈다." id c05_w_0019
    "가헬이 개인 활동을 하지 말란 법은 없지만, 가헬은 일단 전속 계약한 용병이다." id c05_w_0020
    "[pl_name][josa_eun_neun] 가헬이 던전에 가는 이유가 궁금해졌다." id c05_w_0021
    
    menu :
        "그냥 넘어간다." :

            c base "(이중계약을 하진 않았겠지. 뭐...)" id c05_w_0022
            "[pl_name]에게 비밀이 있는 것처럼, 가헬도 뭔가 숨기고 싶은 게 있을 것이다." id c05_w_0023
            
            "[pl_name][josa_eun_neun] 가헬이 던전에 가는 이유를 캐묻지 않았다." id c05_w_0024
            
            c talk "\"그럼 오후에 돌아와?\"" id c05_w_0025
            
            "둘러댈 말을 고르고 있던 가헬은 예상치 못한 질문에 말을 더듬었다." id c05_w_0026

            show ddam at ddam_move (930,40)
            show wolf embarrass am_u
            with dissolve
            hide ddam
            with dissolve

            w "\"아, 아니. 그렇게까지 늦지 않을 거다. 정오가 되기 전에 돌아오도록 하지.\"" id c05_w_0027

            show wolf base am_d
            with dissolve

            "[pl_name][josa_eun_neun] 고개를 끄덕이고 상품 진열을 계속했다. 점심에는 함께 식사할 수 있을 것 같다." id c05_w_0028
            
        "이유를 물어본다." :
            
            c talk "\"던전에는 무슨 일로?\"" id c05_w_0029

            show wolf embarrass am_u
            with dissolve
            
            w "\"그게...\"" id c05_w_0030

            show wolf base am_u
            with dissolve
            
            "가헬은 잠시 말을 고르다가 대답했다." id c05_w_0031

            show wolf talk
            with dissolve

            w "\"조사할 게 있다. 그렇게 오래 걸리지 않을 거다.\"" id c05_w_0032
            w "\"돌아와서 같이 점심을 먹도록 하지.\"" id c05_w_0033

            show wolf base am_d
            with dissolve
            
            "[pl_name][josa_eun_neun] 저번에 봤던 \'이상한 돌\'이 생각났다." id c05_w_0034

            c question2 "(그때 결국 아무것도 밝혀내지 못한 게 가헬도 신경 쓰이나?)" id c05_w_0035

            "[pl_name][josa_eun_neun] 제멋대로 결론을 내리고 대답했다." id c05_w_0036

            c talk "\"알았어. 잘 다녀와. 참, 토벌 작전 이후로 마물이 다시 생겼을지 모르니 몸조심하고.\"" id c05_w_0037

            show wolf smile am_u
            with dissolve

            w "\"응. 이해해 줘서 고맙다.\"" id c05_w_0038

            show wolf am_d
            with dissolve

            "가헬은 미소 지으며 대답했다." id c05_w_0039

            show wolf base
            with dissolve

    pause 0.2
    hide wolf
    show wolf base
    with dissolve
    show wolf at walk (-1500, 2.8, 5)
    play sound "effect/footstep.mp3" volume 0.9
    pause 1.5
    play channel1 "audio/effect/bell.mp3" volume 0.6
    
    "가헬은 [pl_name][josa_i_ga] 챙겨준 회복 물약과 함께 가게를 나섰다." id c05_w_0040

    show cara consider
    with dissolve

    c "\"음...\"" id c05_w_0041

    play sound "audio/effect/sigh.mp3" volume 0.23
    show cara sigh am_u
    with dissolve

    c "\"휴, 드디어 끝났다.\"" id c05_w_0042

    show cara base am_d
    with dissolve
    
    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (-500, 1.6, 3)

    "상품들을 전부 진열한 [pl_name][josa_eun_neun] 빠진 게 없나 한번 둘러보았다." id c05_w_0043

    show cara at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (0, 1.6, 3)
    
    "[pl_name][josa_eun_neun] 영업 시작을 알리는 안내판을 뒤집으려다가 우뚝 멈춰 섰다." id c05_w_0044

    show cara consider
    with dissolve
    
    c "(어차피 가헬도 없으니, 오전 영업을 쉬고 시장에 다녀올까?)" id c05_w_0045
    c "(음, 가헬이 가기 전에 미리 말할 걸 그랬나?)" id c05_w_0046

    show cara base
    with dissolve
    
    "이런저런 생각이 머릿속을 빠르게 스쳐 지나간다." id c05_w_0047
    "판단을 마친 [pl_name][josa_eun_neun] 가방을 찾아 시장에 갈 준비를 했다." id c05_w_0048
    
    stop music fadeout 2.5

label c5w_dungeon:
    # 던전 배경
    scene bg dungeon_1 with Fade(0.8, 0.8, 0.8)
    play music "background-trap-154361.mp3" fadein 2.5 volume 0.35

    # 가헬 등장

    show wolf sword_d
    with dissolve

    "가헬은 마력 폭주의 원인을 조사하러 다시 던전에 왔다." id c05_w_0049
    
    "던전의 구조가 크게 바뀌지 않아 탐색하기 쉬웠다." id c05_w_0050
    
    "물론 가헬은 긴장을 풀지 않았다." id c05_w_0051

    # 검이 번쩍
    show wolf sword_u fight
    with dissolve

    play sound "effect/sword_slice.mp3" volume 0.7
    show sword_slash at slash2
    pause 0.2
    hide sword_slash

    w "\"핫!\"" id c05_w_0052
    
    "가헬은 재빠르게 검을 휘둘러 마물을 조각냈다." id c05_w_0053
    
    "확실히 던전 안은 토벌 작전 덕분에 꽤 평화로웠다." id c05_w_0054
    
    "마물이 전혀 없는 것은 아니지만, 이 정도면 초보 용병도 마음 놓고 다닐 정도였다." id c05_w_0055

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-110, -220)
    show wolf sword_d sigh
    with dissolve

    hide sigh
    with dissolve

    w "\"휴...\"" id c05_w_0056

    show wolf out_d base
    with dissolve
    
    "가헬은 자세를 추스르고 한숨을 쉬었다." id c05_w_0057
    
    "이미 던전의 거의 모든 장소를 돌아봤다. 딱히 몸이 이질적으로 반응하는 느낌은 없었다." id c05_w_0058
    
    "마물 무리와 싸웠던 장소에서 근육 강화를 써보았지만 전혀 문제없었다." id c05_w_0059

    w "(증거가 될 물건도 없고, 역시 허탕이군.)" id c05_w_0060

    show wolf sad_am out_u
    with dissolve

    "가헬은 슬픈 표정을 하며 주먹을 쥐었다." id c05_w_0061
    
    "그 순간을 떠올리면 지금도 아찔했다. 근육이 제멋대로 움직이는 느낌은 정말로 끔찍했다." id c05_w_0062
    
    "자칫 잘못하면 [pl_name][josa_eul_reul] 베어버릴 수도 있었다. 그런 일은 두 번 다시 일어나서는 안 된다." id c05_w_0063
    
    "생각할수록 죄책감에 파묻히는 기분이었다." id c05_w_0064

    show wolf sad2_am out_u
    with dissolve

    w "(정신 차리자.)" id c05_w_0065

    show wolf base out_d
    with dissolve

    "일단 할 수 있는 조사를 하고 있지만, 사실 던전에 뭐가 있으리라 기대하지는 않았다." id c05_w_0066
    
    "마력 폭주를 일으킬 수 있는 물건이 있다면 기사단이 진즉에 회수했을 것이다."    
    
    w "(그러고 보니 그 이상한 돌은... 그때는 분명히 없었던 물건이다.)" id c05_w_0067

    "엘레드가 보여준 \'이상한 돌\'이 원인이었다면, 술집에서 또 마력 폭주를 일으켰을 것이다." id c05_w_0068
    
    "자신보다는 마물과 관련이 있을 것 같지만, 그마저도 확실한 건 아니었다." id c05_w_0069

    show wolf fight3 out_u
    with dissolve
    
    w "(결국 기대할 만한 건 \'바토\' 씨 뿐인가...)" id c05_w_0070
    
    "가헬은 바토의 답장을 다시 떠올렸다." id c05_w_0071
    
    "다행히 바토는 흔쾌히 가헬의 상태를 봐주겠다고 했다." id c05_w_0072

    show wolf base out_d
    with dissolve
    
    "만날 장소는 우선 용병 길드로 정했다. 주점은 듣는 귀가 너무 많았다." id c05_w_0073

    w "(아예 훈련장에서 보자고 해야 하나...)" id c05_w_0074


    play sound "effect/footstep.mp3" volume 0.9
    show wolf at walk (0, 1.6, 3)
    
    pause 1.7
    show wolf talk
    with dissolve
    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 80)
    
    "가헬은 던전을 걸어 다니다가 번뜩 무언가가 생각났다." id c05_w_0075
    
    show wolf base
    hide exclamation
    with dissolve

    "그날 던전에는 마력 진동이 있었다." id c05_w_0076
    "보통 수인은 마력 진동에 강하게 영향을 받아봤자 잠깐 어지러운 느낌이 드는 게 끝이다." id c05_w_0077
    "간혹 마법 공격의 방향이 꺾인다거나 하는 일이 있어서 위험한 것은 맞지만, 신체에 직접 영향을 주는 일은 없었다." id c05_w_0078
    "원래 체내의 마나 흐름은 외부 영향을 잘 받지 않는다." id c05_w_0079
    "하지만 가헬의 상태는 조금 다르다." id c05_w_0080
    "시술에 뭔가 문제가 있다는 게 사실이라면, 그것 때문에 마나 흐름에 문제가 생기는 건 당연한 일이다." id c05_w_0081
    "외부 마력에 영향을 쉽게 받을 수도 있다." id c05_w_0082
    
    show wolf fight3 out_u
    with dissolve

    w "\"흠...\"" id c05_w_0083

    show wolf base out_d
    with dissolve

    "확실한 건 아직 아무것도 없지만, 가헬은 아주 작은 실마리를 잡은 기분이 들었다." id c05_w_0084
    "역시 바토를 만나보면 좀 더 많은 것을 알 수 있을 것 같다." id c05_w_0085
    "가헬은 더 늦기 전에 던전에서 나왔다." id c05_w_0086

    stop music fadeout 2.5

label c5w_blackmarket:
    # 길거리 배경
    scene bg street with Fade(0.8, 0.8, 0.8)
    play music "audio/spirit-of-adventure-130563.mp3" volume 0.9 fadein 1.0

    "가헬이 던전에 간 사이, [pl_name][josa_eun_neun] 가게 문을 닫고 시장에 갔다." id c05_w_0087

    show cara out_d
    with dissolve

    "상점에서 정제된 기름, 합성수지, 수은과 몇 가지 약초들을 사고 다른 가게들을 천천히 둘러봤다." id c05_w_0088
    
    show cara at mirror
    with dissolve

    "향긋한 꽃냄새에 이끌려 고개를 돌려보니 미용 상품 전문점이 있었다." id c05_w_0089
    "[pl_name][josa_eun_neun] 거기서 비누를 살지 말지 고민했다." id c05_w_0090

    show cara consider
    with dissolve

    c "(직접 만들 수 있지만 너무 귀찮단 말이지...)" id c05_w_0091

    "비누는 굳히고 자르는 과정이 가장 귀찮다. 팔 물건도 아닌데 작게 나누는 짓을 하고 싶지 않았다." id c05_w_0092
    "세탁용 세제 같은 건 큰 통에 담아둘 수 있어서 그래도 괜찮은 편이다." id c05_w_0093

    show cara base
    with dissolve

    "[pl_name][josa_eun_neun] 결국 고민 끝에 비누를 하나 골랐다." id c05_w_0094

    show soap :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (890, 0)
    show cara talk
    with dissolve

    c "(가헬이 저번에 좋다고 했던 게 이런 향이었나?)" id c05_w_0095

    hide soap
    hide question
    show cara base
    with dissolve

    play sound "effect/inhale.mp3" volume 0.7

    "[pl_name][josa_eun_neun] 코를 킁킁거리며 비누에서 나는 풀 냄새를 맡아보았다." id c05_w_0096
    "몇 가지 허브가 섞인 상쾌한 느낌이었다." id c05_w_0097
    "가헬은 자주 씻지도 않으면서, 왠지 꽃향기가 나는 비누보다 이런 비누만 쓰려고 했다." id c05_w_0098

    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (1500, 2.8, 5)

    "가헬의 취향에 맞는 비누를 구매한 [pl_name][josa_eun_neun] 다른 상점을 향해 걸어갔다." id c05_w_0099

    stop music fadeout 2.5
    scene bg back_alley
    with Fade(0.8, 0.8, 0.8)
    play music "audio/chill-abstract-intention-12099.mp3" volume 0.7 fadein 2.5

    # 뒷골목 배경

    "[pl_name][josa_eun_neun] 상점가에서 가게로 돌아가는 길에 뒷골목으로 빠졌다." id c05_w_0100

    show cara out_d consider
    with dissolve

    c "(아무도 없지?)" id c05_w_0101
    
    # 레스크 후드
    show cara base_hood hood
    with dissolve

    $ unlock_character_image("cara", "cara b_no hood")
    $ display_text = _("이미지 : [pl_name](후드)")
    show screen affection_indicator

    "주변을 둘러본 [pl_name][josa_eun_neun] 후드를 눌러썼다." id c05_w_0102
    "길쭉한 귀가 구멍 위로 튀어나왔다." id c05_w_0103
    "[pl_name][josa_eun_neun] 다시 한번 보는 사람이 없나 경계하고는 조심스레 움직였다." id c05_w_0104

    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (-500, 1.6, 3)
    pause 1.7
    show cara at vshake (0.08, 0, -10)

    "[pl_name][josa_eun_neun] 벽면을 손으로 더듬다가 걸리는 위치를 잡고 당겼다." id c05_w_0105

    play sound "effect/stone_grind.mp3" volume 0.9
    with vpunch
    #벽 열리는 효과음

    "벽이 문처럼 밀리면서 새로운 길이 열렸다." id c05_w_0106

    stop music fadeout 2.5
    scene bg black_market
    with Fade(0.8, 0.8, 0.8)
    play music "night-detective-226857.mp3" volume 0.6 fadein 2.5

    # 암시장1 배경
    
    $ unlock_info_tag(3, "2")
    $ display_text = _("정보 : 암시장")
    show screen affection_indicator

    "이곳이 바로 {color=#ee3939}'암시장'{/color}이다." id c05_w_0107

    show cara base_hood hood
    with dissolve

    "일반적인 시장과 크게 다를 것은 없지만, 여기서는 무엇이든 자유롭게 거래한다." id c05_w_0108
    "평범한 물건을 세금 없이 팔기도 하고, 수인이라면 당연히 꺼림칙하게 느껴질 물건을 거래하기도 한다." id c05_w_0109
    "[pl_name][josa_eun_neun] 여기서 \'어떤 물건\'을 거래하러 왔다." id c05_w_0110

    show cara at mirror
    with dissolve
    pause 0.5
    hide cara
    show cara base_hood hood
    with dissolve

    "주변을 둘러보자, 몇몇 수인들이 [pl_name][josa_eul_reul] 지나쳐 걸어갔다." id c05_w_0111

    show cara consider_hood
    with dissolve

    c "(너무 일찍 왔나?)" id c05_w_0112

    show cara base_hood
    with dissolve

    "암시장이라고 해도 무슨 입장 암호나 회원 전용 같은 건 없다." id c05_w_0113
    "여기의 규칙은 '서로 신분을 숨길 것'이다." id c05_w_0114
    "암시장 안에선 밖의 신분을 적당히 모르는 척해주는 것이 예의다." id c05_w_0115
    "물론 규칙이라는 게 절대적이지 않아서, 암시장에서 분쟁과 폭력 사건은 꽤 흔한 일이다." id c05_w_0116
    "[pl_name][josa_eun_neun] 괜한 일에 휘말리고 싶지 않아서 후드가 잘 씌워져 있는지 신경 썼다." id c05_w_0117
    "이 후드도 나름 괜찮은 아티팩트다. 마법으로 [pl_name]의 얼굴이 다른 수인처럼 보이도록 하는 효과가 있다." id c05_w_0118

    c "(원래라면 여기에서의 호위까지 가헬에게 맡겨야 하겠지만...)" id c05_w_0119

    "가헬과의 계약에서 굳이 던전 밖까지 호위를 맡긴 건 이런 이유도 있었다." id c05_w_0120
    "하지만 지금은 가헬에게 자신의 거래 현장을 보여주고 싶지 않았다." id c05_w_0121
    "[pl_name][josa_eun_neun] 빠른 걸음으로 다른 수인들을 지나쳐갔다." id c05_w_0122

    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (-1500, 2.3, 4)
    
    pause 2.5

    scene bg black_market2
    with Fade(0.8, 0.8, 0.8)

    # 뚜벅뚜벅 연출하고 암시장2

    "이상할 정도로 저렴한 상품과 무섭게 생긴 수인들을 지나쳐, [pl_name][josa_eun_neun] 어떤 건물 앞에 도착했다." id c05_w_0123
    
    show cara base_hood hood
    with dissolve

    "코를 막고 싶은 비린내가 슬금슬금 새어 나오는 곳이었다." id c05_w_0124

    show cara talk_hood hood
    with dissolve
    
    c "\"거래하러 왔습니다.\"" id c05_w_0125

    show cara base_hood
    with dissolve
    
    play sound "effect/door_knock.mp3" volume 0.62
    show cara :
        ease 0.22 xoffset 35
        ease 0.1 xoffset -10
        ease 0.05 xoffset 0
        repeat 2
    
    "[pl_name][josa_eun_neun] 만지기도 꺼림칙한 문을 발로 노크했다." id c05_w_0126

    "안에서 나온 수인은 [pl_name]보다도 꽁꽁 싸매고 있었다." id c05_w_0127
    "종조차 알아볼 수 없는 그 남자는 [pl_name][josa_eul_reul] 보고 복면 속에서 씨익 웃었다." id c05_w_0128
    "적어도 [pl_name][josa_eun_neun] 그렇게 느꼈다." id c05_w_0129

    n "\"오늘도 고급 회복 물약인가?\"" id c05_w_0130

    show cara talk_hood hood_up
    with dissolve

    c "\"네.\"" id c05_w_0131

    show cara base_hood 
    with dissolve

    n "\"그리고 신선한 \'그것\'도?\"" id c05_w_0132

    show cara talk_hood
    with dissolve

    c "\"... 네.\"" id c05_w_0133

    show cara base_hood hood
    with dissolve

    "[pl_name][josa_eun_neun] 시선을 살짝 피하며 말했다." id c05_w_0134
    "성노예를 훈련하고 거래하는 상인이라 그런지 아무 수인이나 쉽게 깔보는 경향이 있었다." id c05_w_0135
    "자꾸 짜증 나게 굴지만 적절한 재료를 구할 곳이 여기뿐이라 그냥 참았다." id c05_w_0136

    n "\"좀 기다려봐.\"" id c05_w_0137
    
    "[pl_name][josa_eun_neun] 다시 안으로 들어간 상인을 조용히 기다렸다." id c05_w_0138
    "다른 수인들은 어떤지 모르겠으나, [pl_name][josa_i_ga] 거래하는 물건은 정말로 들키면 보통 위험한 게 아니었다." id c05_w_0139
    "암시장에 올 때마다 내적 갈등은 깊어져만 갔다." id c05_w_0140

    show cara consider_hood
    with dissolve

    c "(슬슬 그만둬야 하나... 가게 매출도 좀 오른 거 같고...)" id c05_w_0141

    show cara base_hood
    with dissolve
    
    "[pl_name][josa_eun_neun] 가끔 특제 회복 물약을 팔아서 돈을 벌고 있다." id c05_w_0142
    "마탑의 연금술사들이 만든 고급 물약은 정말 엄청난 부자가 아니면 쓸 수 없다." id c05_w_0143
    "[pl_name][josa_eun_neun] 그런 물건을 굉장히 저렴한 가격에 파는 셈이다." id c05_w_0144
    
    c "(만약 바토에게 이걸 들켰다면 정말로... 모두 끝났겠지.)" id c05_w_0145

    "소문에 따르면 마탑은 시간과 공간 마법을 이용해 영원한 고문을 할 수 있다고 한다." id c05_w_0146
    "그게 허풍이라고 해도 최소한 온갖 실험에 사용당하게 될 것이다." id c05_w_0147
    "그런 위험 부담을 지고 계속 이런 거래를 해야 할지 고민이 됐다." id c05_w_0148

    $ unlock_info_tag(3, "3")
    $ display_text = _("정보 : 특제 물약2")
    show screen affection_indicator

    "무엇보다도 [pl_name]의 {color=#ee3939}'특제 물약'{/color}은 재료를 구하기가 어렵다." id c05_w_0149
    "마탑에서는 어떻게 만드는지 모르겠으나, [pl_name][josa_eun_neun] 주술을 사용해서 만들고 있다." id c05_w_0150
    "그리고 그 재료는 바로 \'수인의 피\'였다." id c05_w_0151

    n "\"아주 신선한 걸로 한 병. 맞지?\"" id c05_w_0152

    show red_bottle :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "다시 나타난 암시장 상인은 피가 가득 든 유리병을 내밀었다." id c05_w_0153

    hide red_bottle
    with dissolve

    "어떤 노예가 강제로 피를 뽑혔을 것이다." id c05_w_0154

    show high_potion :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "[pl_name][josa_eun_neun] 그것을 빠르게 가방에 숨기고 특제 물약을 건네줬다." id c05_w_0155

    hide high_potion
    with dissolve

    show cara talk_hood hood_up
    with dissolve

    c "\"돈은 어딨죠?\"" id c05_w_0156

    show cara base_hood hood
    with dissolve
    
    n "\"왜 이렇게 급해?\"" id c05_w_0157
    
    "그는 주머니에서 뭔가의 종이를 꺼냈다." id c05_w_0158
    "금화를 보관하는 증서였다." id c05_w_0159
    "액수를 확인한 [pl_name][josa_eun_neun] 그것도 가방에 넣었다." id c05_w_0160
    "매번 거래할 때마다 돈을 턱턱 내는 것도 약간 꺼림칙했다." id c05_w_0161

    n "\"요즘 재밌는 소식이 있는데.\"" id c05_w_0162
    
    "[pl_name][josa_eun_neun] 쓸데없는 말에 대답하고 싶지 않았다." id c05_w_0163

    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (-300, 1.5, 3)

    "무시하고 가려는 [pl_name][josa_eul_reul] 보고 상인은 다시 말을 꺼냈다." id c05_w_0164

    n "\"\'강철손 상회\'가 무섭게 세를 불리고 있어. 조만간 무슨 일이든 생길 거야.\"" id c05_w_0165
    
    "[pl_name][josa_eun_neun] 그게 뭔지 모르겠지만, 일단 뒷세계의 조직인 건 확실하다고 판단했다." id c05_w_0166
    "그런건 되도록 안 얽히는 게 최선이다." id c05_w_0167

    show cara at mirror
    with dissolve
    show cara talk_hood hood_up
    with dissolve
    
    c "\"관심 없습니다.\"" id c05_w_0168

    show cara base_hood hood
    with dissolve
    
    "[pl_name]의 까칠한 대답에 상인은 이상한 웃음소리를 냈다." id c05_w_0169
    
    n "\"계속 암시장에 다닐 거면 관심 가지는 게 좋을걸?\"" id c05_w_0170

    n "\"뭐, 인생 망가지면 내가 조련할 가능성이 높아지니 상관없나? 큭큭큭...\"" id c05_w_0171
    
    "상인은 [pl_name][josa_wa_gwa] \'상품\'을 겹쳐보고 있었다." id c05_w_0172

    show cara angry_hood
    with dissolve

    # 레스크 분노

    "노골적인 성희롱에 [pl_name][josa_eun_neun] 분노가 솟구쳤다. 피가 차갑게 식는 느낌이었다." id c05_w_0173
    
    c "(...)" id c05_w_0174
    c "(흠... 죽여버릴까?)" id c05_w_0175
    c "(아니지... 번거롭게 죽이지 말고 산 채로 제물로 쓰면...)" id c05_w_0176
    
    "[pl_name][josa_eun_neun] 눈앞의 남자가 불타오르는 상상을 했다." id c05_w_0177

    $ unlock_info_tag(3, "4")
    $ display_text = _("정보 : 산 제물")
    show screen affection_indicator

    "{color=#ee3939}'목숨을 제물'{/color}로 바치는 건 궁극의 주술이자 절대 금기다." id c05_w_0178
    "그것은 아주 먼 옛날에 전쟁의 원인이 되어, 대부분의 주술사가 사라지게 되는 결과를 낳았다." id c05_w_0179
    
    c "(아니다... 오늘은 뒤처리 할 시간이 없지.)" id c05_w_0180
    
    "[pl_name][josa_eun_neun] \'금지\' 따위 신경 쓰지 않았지만, 일을 저지른 뒤의 상황은 신경 쓰였다." id c05_w_0181
    "암시장에서 괜히 문제 일으켜서 좋을 것 하나 없었다." id c05_w_0182
    "흔적을 잡히기라도 하면 보통 피곤한 일이 아닐 것이다." id c05_w_0183

    show cara angry2_hood
    with dissolve
    
    c "\"제 몸은 제가 알아서 잘 할테니 신경 쓰지 마시죠.\"" id c05_w_0184

    show cara angry_hood
    with dissolve
    
    "[pl_name][josa_eun_neun] 그냥 빠르게 자리를 뜨고 다음에 생각하기로 했다." id c05_w_0185
    

    show cara at mirror2
    with dissolve

    pause 0.2
    play sound "effect/footstep.mp3" volume 0.9
    show cara at walk (-1500, 2.2 , 4)

    "상인이 낄낄거리는 소리가 점점 멀어져갔다." id c05_w_0186

    stop music fadeout 2.5
    

    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    #가게 배경

    show cara base_hood hood
    with dissolve
    
    "가게까지 오는 길이 유난히 길게 느껴졌다." id c05_w_0187

    show cara base am_d
    with dissolve
    pause 0.2

    show red_bottle :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "후드를 벗은 [pl_name][josa_eun_neun] 가방에서 피가 든 유리병부터 꺼냈다." id c05_w_0188

    hide red_bottle
    with dissolve
    pause 0.2

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-100, -160)
    show cara sigh
    with dissolve

    c "\"휴...\"" id c05_w_0189

    show cara base
    with dissolve
    pause 0.2

    play sound "effect/flash_fast.mp3" volume 0.25    
    show flash_blue at flash_fast
    pause 0.95
    hide flash_blue at flash_fast

    show clear_bottle :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "주술로 피에서 생명력의 정수를 뽑아내자, 탁했던 붉은 액체가 맑게 변한다." id c05_w_0190

    hide clear_bottle
    with dissolve

    "이대로 사용할 수는 없고, 일반 회복 물약과 적절한 비율로 섞어야 \'특제\' 물약이 된다." id c05_w_0191

    c "(곧 가헬이 올 시간이네. 빨리 처리해야지...)" id c05_w_0192

    "[pl_name][josa_eun_neun] 가방의 내용물을 정리하기로 했다." id c05_w_0193

    scene bg warehouse with Fade(0.8, 0.8, 0.8)   
    # 창고 배경

    show cara
    with dissolve

    "창고는 가헬이 한 번 청소했는지 먼지 없이 깔끔했다." id c05_w_0194
    "[pl_name][josa_eun_neun] 남에게 보여줄 수 없는 물건들을 잘 숨겨놨다." id c05_w_0195
    "가헬이 또 청소하더라도 간단하게 들키지는 않을 것이다." id c05_w_0196

    c "(물약은 내일 만들고, 금화는 다음 주에 가져와도 되겠지.)" id c05_w_0197

    "간단한 계획을 세운 [pl_name][josa_eun_neun] 가헬이 오기 전에 가게 영업을 시작했다." id c05_w_0198

    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    # 가게 저녁 배경

    c sigh "\"하암~\"" id c05_w_0199
    
    "점심이 지나고 나른한 오후 시간이 되자 [pl_name][josa_eun_neun] 조금 지루해졌다." id c05_w_0200
    "긴장이 풀린 탓도 있었다." id c05_w_0201
    "손님이 가고 나니 정말 할 일이 없어져서 괜히 책상 위를 정리했다." id c05_w_0202

    show wolf talk am_u
    with dissolve

    w "\"[pl_name], 내일 바쁜가?\"" id c05_w_0203

    show wolf base am_d
    with dissolve

    "가헬은 조금 쭈뼛거리며 [pl_name]에게 말을 걸었다." id c05_w_0204
    
    c question2 "\"아니? 휴일이잖아.\"" id c05_w_0205
    
    "[pl_name][josa_eun_neun] 당연하다는 듯 말했다가 뒤늦게 가헬의 의도를 알아챘다." id c05_w_0206
    "연인으로서 맞이하는 첫 휴일에 첫 데이트를 기대하는 표정이었다." id c05_w_0207
    
    c laugh "\"하하. 데이트 신청하는 거야?\"" id c05_w_0208

    show wolf shy2
    with dissolve
    pause 0.2
    show wolf :
        ease 0.25 yoffset 10
        ease 0.15 yoffset 0
    
    "가헬은 부끄러운지 살짝 붉어진 얼굴로 고개를 끄덕였다." id c05_w_0209

    show wolf shy5 am_u
    with dissolve
    
    w "\"사실 좀 더 일찍 물어봤어야 했는데...\"" id c05_w_0210
    w "\"아직 멋진 계획을 세우지 못했다.\"" id c05_w_0211

    show wolf base am_d
    with dissolve
    
    "가헬은 [pl_name][josa_wa_gwa] 첫 데이트로 어디부터 가야 할지 고민했다." id c05_w_0212
    "유명한 식당부터 대륙 끝의 해변이나, 화려한 축제를 찾아가도 좋을 것이다." id c05_w_0213
    
    c talk "\"그러면 나 하고 싶은 거 있어.\"" id c05_w_0214
    
    "가헬의 상상은 이어지는 [pl_name]의 말에 와장창 깨져버렸다." id c05_w_0215
    
    c "\"용병이 훈련하는 거 구경해보고 싶어.\"" id c05_w_0216

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (890, 0)
    show wolf talk am_u
    with dissolve
    
    w "\"... 그걸, 왜?\"" id c05_w_0217

    hide question
    show wolf embarrass
    with dissolve
    
    "가헬은 조금 당황했다." id c05_w_0218

    show wolf base am_d
    with dissolve

    "그걸 굳이 시간 내서 봐야 할 모습이라고는 상상도 하지 못했다." id c05_w_0219
    
    c question2 "\"음, 정확히는 가헬이 훈련하는 모습?\"" id c05_w_0220
    c consider "\"유명 용병단은 뭐가 다른지 궁금하기도 하고...\"" id c05_w_0221
    c talk "\"가헬이 어떻게 그렇게 강한지도 궁금해서.\"" id c05_w_0222

    show ddam at ddam_move (930,40)
    show wolf embarrass
    with dissolve
    
    "가헬은 [pl_name]의 대답에 기뻐해야 할지 혼란스러웠다." id c05_w_0223

    hide ddam
    with dissolve

    "서로를 알아가는 건 중요한 일이지만, 낭만적인 데이트는 아닌 것 같았다." id c05_w_0224
    
    show wolf base
    with dissolve

    "가헬은 고민 끝에 승낙했다." id c05_w_0225

    show wolf talk am_u
    with dissolve
    
    w "\"특별한 것은 없다. 체력 단련은 보기에 지루할 테니, 검술 연습을 해야겠군.\"" id c05_w_0226

    show wolf base am_d
    with dissolve
    
    "가헬은 [pl_name]에게 멋진 모습을 보여줄 생각이었다." id c05_w_0227
    
    c "\"그리고 기왕 놀러 가는 거 점심도 가져가야겠어.\"" id c05_w_0228
    
    w "(이것도 나름 데이트같군...)" id c05_w_0229
    
    "[pl_name][josa_eun_neun] 무슨 음식을 챙겨갈지 고민하며 영업을 정리했다." id c05_w_0230

    stop music fadeout 2.5

label c5w_date1:
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40 
    
    "{i}~다음 날 아침~{/i}" id c05_w_0231
    
    # 레스크 화면에 등장

    show cara
    with dissolve

    "[pl_name][josa_eun_neun] 휴일에도 일찍 일어나서 무언가를 만들고 있었다." id c05_w_0232
    
    "특제 회복 물약은 이미 다 만들었고, 연금솥은 깔끔하게 비워두었다." id c05_w_0233

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-100, -160)
    show cara sigh am_u
    with dissolve

    c "(이게 아닌데. 이거랑은 조금 다른 느낌이었으면...)" id c05_w_0234

    show cara base am_d
    with dissolve

    "[pl_name][josa_eun_neun] \'다른 용도\'로 쓰기 위한 허브 오일을 조합 중이었다." id c05_w_0235
    "조그만 그릇에 이런저런 재료를 넣어 섞어보면서 결과물을 분석했다." id c05_w_0236

    show cara consider
    with dissolve

    c "(기본 용매부터 바꿔야 하나?)" id c05_w_0237

    "쓸만한 다른 재료가 있을지 고민했다." id c05_w_0238
    "적당히 미끈거리고 끈적하면서 굳지 않으며 몸에 쉽게 흡수되지 않는 방법을 생각하느라, 머리가 아파지기 시작했다." id c05_w_0239

    show cara sad_am
    with dissolve

    c "(으으, 이런 건 최신 논문 없나? 이미 누군가는 생각했을 법한데...)" id c05_w_0240

    "마탑에서 이미 관련 상품까지 판매하고 있지만, [pl_name][josa_i_ga] 쉽게 알 수 있는 정보는 아니었다." id c05_w_0241
    
    show cara base
    with dissolve
    
    "[pl_name][josa_eun_neun] 그릇을 비우고 다시 새로운 조합을 시도해 보기로 했다." id c05_w_0242
    
    #특제 오일 재료선택 / 올바르게 골라야 씬2 조건부 
    
    c "(우선 베이스로 쓸 용액부터 골라보자.)" id c05_w_0243

    # 1번 선택지
    menu :
        "코코넛 기름" :
            # 러브젤점수+2
            $ oil_making += 2
            "[pl_name][josa_eun_neun] 코코넛 기름을 조심스레 부었다. 달달하고 고소한 향기가 났다." id c05_w_0244
        
        "정제수" :
            # 러브젤점수+0
            $ oil_making += 0
            "[pl_name][josa_eun_neun] 연금용 정제수를 꺼냈다. 평소처럼 조금씩 그릇에 부었다." id c05_w_0245

        "나무 수액" :
            # 러브젤점수+1
            $ oil_making += 1
            "[pl_name][josa_eun_neun] 나무 수액이 담긴 병을 열었다. 특유의 오묘한 냄새가 났다." id c05_w_0246

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (890, 0)
    with dissolve
    
    c "(그리고 무슨 허브를 넣을까?)" id c05_w_0247

    hide question
    with dissolve

    # 2번 선택지
    menu :
        "보라색 로즈마리" :
            # 러브젤점수+2
            $ oil_making += 2
        
        "빨간 세이지" :
            # 러브젤점수+1
            $ oil_making += 1
            
        "에메랄드 민트" :
            # 러브젤점수+0
            $ oil_making += 0
            
    "허브를 추출하자 씁쓸한 풀냄새가 가득 퍼진다." id c05_w_0248
    "[pl_name][josa_eun_neun] 딱 한 방울을 덜어서 그릇에 넣었다." id c05_w_0249

    show cara consider
    with dissolve
    
    c "(핵심 재료는 뭘 쓸까...)" id c05_w_0250

    # 3번 선택지
    menu :
        "크리스탈 나무에서 채집한 수지" :
            # 러브젤점수+0
            $ oil_making += 0
        
        "달빛을 받은 이슬의 농축액" :
            # 러브젤점수+2
            $ oil_making += 2
            
        "마물에서 추출한 점액질" :
            # 러브젤점수+1
            $ oil_making += 1

    "[pl_name][josa_eun_neun] 재료들을 잘 섞은 뒤에 살짝 만져봤다." id c05_w_0251

    show cara base
    with dissolve

    c "(나쁘지 않은데?)" id c05_w_0252

    "[pl_name][josa_eun_neun] 첨가제를 넣거나 비율을 조금씩 바꿔가며 여러 개의 샘플을 만들어보았다." id c05_w_0253
    "그중에 가장 괜찮은 것을 찾을 생각이었다." id c05_w_0254

    c "(이거보단 저게 더 나은 것 같기도 하고...)" id c05_w_0255

    # 점수 결과물

    if oil_making >= 4 :
        #(4~6점) 10개
        $ display_text = _("{color=#bd1b28}'부드러운 꽃향기'{/color}가 나는 오일 획득") 
        show screen affection_indicator
        show oil2 :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        "마침내 [pl_name][josa_eun_neun] {color=#ee3939}'부드러운 꽃향기'{/color}가 나는 오일을 한 병 만들었다." id c05_w_0256
    elif oil_making == 3 :
        #(3 점) 7 개
        $ display_text = _("{color=#bd1b28}'싱그러운 풀냄새'{/color}가 나는 오일 획득") 
        show screen affection_indicator
        $ oil_complete = True
        show oil2 :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        "마침내 [pl_name][josa_eun_neun] {color=#ee3939}'싱그러운 풀냄새'{/color}가 나는 오일을 한 병 만들었다." id c05_w_0257
    elif oil_making <= 2:
        #(0~2점) 10개
        $ display_text = _("{color=#bd1b28}'은은한 과일 향'{/color}이 나는 오일 획득") 
        show screen affection_indicator
        show oil2 :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        "마침내 [pl_name][josa_eun_neun] {color=#ee3939}'은은한 과일 향'{/color}이 나는 오일을 한 병 만들었다." id c05_w_0258

    show cara consider
    with dissolve
    
    c "\"가헬도 이걸 좋아하려나?\"" id c05_w_0259

    hide oil2
    show cara base
    with dissolve
    
    "[pl_name][josa_eun_neun] 특제 오일의 향을 맡아보고 뚜껑을 닫았다."    

    "팔 물건이 아니니까 카운터 안쪽에 두었다." id c05_w_0260

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-100, -160)
    show cara sigh am_u
    with dissolve
    
    c "\"휴...\"" id c05_w_0261
    
    "[pl_name][josa_eun_neun] 한숨을 푹 내쉬었다." id c05_w_0262

    show cara base am_d
    with dissolve

    "[pl_name][josa_i_ga] 특제 오일을 만든 것은 오늘 밤을 대비하기 위해서였다." id c05_w_0263
    "저번에는 피곤하다는 이유로 어떻게든 피했지만, 이제 정말 가헬과의 밤을 더 미룰 수 없었다." id c05_w_0264
    "기대 반 걱정 반으로 마음이 혼란스러웠다. 당장 할 수 있는 준비부터 할 수밖에 없었다." id c05_w_0265

    hide cara
    with dissolve
    pause 0.3
    show wolf talk
    with dissolve
    
    # 화면에 가헬 등장

    w "\"[pl_name]? 일찍 일어났군.\"" id c05_w_0266

    show wolf base
    with dissolve
    
    c talk "\"응... 미리 만들어둘 게 있어서.\"" id c05_w_0267
    
    "1층으로 내려온 가헬은 [pl_name][josa_i_ga] 주섬주섬 재료를 치우는 걸 보았다." id c05_w_0268
    
    if oil_complete == True :
        "[pl_name]의 몸에서 나던 향기가 가게 안에 가득했다." id c05_w_0269
    else :
        "연금술 재료의 다양한 향기가 가게 안에 가득했다." id c05_w_0270

    show wolf shy
    with dissolve
    
    show wolf:
        ease (0.25) yoffset -20
        ease (0.15) yoffset 0
        repeat 2
    
    "가헬은 코를 킁킁거렸다." id c05_w_0271
    
    "그리고 급히 정신 차리고 말을 꺼냈다." id c05_w_0272

    show wolf shy5 am_u
    with dissolve

    w "\"점심으로 뭘 준비할까?\"" id c05_w_0273

    show wolf shy2 am_d
    with dissolve
    
    c talk "\"아참, 어제 결국 못 정했지. 재료는 많이 있는데...\"" id c05_w_0274

    show wolf base
    with dissolve
    
    "[pl_name][josa_eun_neun] 식재료를 가득 채워놓은 선반에서 뭐부터 꺼내야 할지 고민했다." id c05_w_0275
    "보존 마법이 있으니 어지간한 요리는 가져갈 수 있지만, 무게나 공간은 어쩔 수 없었다." id c05_w_0276
    "가장 쉬운 수프는 이미 후보에서 탈락했다." id c05_w_0277

    c "\"먹을 때 간편한 거 없을까? 요리는 지금 해두면 되는데.\"" id c05_w_0278

    show wolf talk am_u
    with dissolve
    
    w "\"그럼, 글렌브루크식 베개 빵으로 하지.\"" id c05_w_0279

    show wolf base am_d
    with dissolve
    
    c question2 "\"베개... 빵?\"" id c05_w_0280
    
    "처음 들어보는 단어에 [pl_name][josa_eun_neun] 갸우뚱했다." id c05_w_0281
    "베개라고 하니 자연스럽게 \'잔뜩 부풀려서 폭신폭신해진 빵\'이 떠올랐다." id c05_w_0282

    show wolf talk am_u
    with dissolve

    w "\"빵 속을 동그랗게 파서 재료를 넣는 음식이다.\"" id c05_w_0283
    w "\"동부에서 점심으로 흔히 먹던데, 나도 몇 번 사 먹어봤다.\"" id c05_w_0284

    show wolf base
    with dissolve
    
    c talk "\"만들 수도 있어?\"" id c05_w_0285

    show wolf talk
    with dissolve
    
    w "\"그렇게 어렵지 않다.\"" id c05_w_0286

    show wolf base am_d
    with dissolve
    
    "가헬은 빵부터 가져가서 썰기 시작했다." id c05_w_0287
    
    c "\"속 재료는 어떻게 할까?\"" id c05_w_0288

    show wolf talk am_u
    with dissolve
    
    w "\"먹고 싶은 게 있으면 아무거나 넣어도 된다. 어차피 현지에서도 가게마다 제멋대로더군.\""  id c05_w_0289
    w "\"아, 살라미는 내가 썰겠다.\"" id c05_w_0290

    show wolf base am_d
    with dissolve
    
    "[pl_name][josa_wa_gwa] 가헬은 한동안 음식을 만드느라 분주하게 움직였다.   " id c05_w_0291
    "가헬이 집안일을 대신 하게 된 뒤로, [pl_name][josa_eun_neun] 가헬의 뛰어난 요리 실력을 알게 되었다." id c05_w_0292
    "칼질부터 불 조절까지 전문 요리사 못지않았다." id c05_w_0293

    c base "(나도 나름 잘 한다고 생각했는데...)" id c05_w_0294

    "가헬은 썰어놓은 속 재료를 한 곳에 모아두고, 몇 가지 소스를 뿌려서 섞었다." id c05_w_0295
    "맛있는 냄새가 가게를 채우기 시작했다." id c05_w_0296

    show roll_bread:
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "빵이 완성되었다." id c05_w_0297

    hide roll_bread
    with dissolve

    "휴일에 같이 먹을 음식을 만드는 건, 따지고 보면 평소와 크게 다르지 않은 일상이었다." id c05_w_0298


    c consider "(데이트... 남들이 하는 것도 좀 따라 해봐야 할까?)" id c05_w_0299

    "[pl_name][josa_eun_neun] 갑자기 엘레드가 떠올랐다." id c05_w_0300
    "엘레드라면 역시 경험도 많을 테고, 왜 그런 데이트를 하는지도 잘 알 것이다." id c05_w_0301

    c "(하지만 만나서 물어보기는 좀 그렇네...)" id c05_w_0302

    "엘레드도 [pl_name][josa_wa_gwa] 연인이 되기를 원했다." id c05_w_0303
    "그게 얼마나 진심인지 잘 모르겠지만, [pl_name][josa_eun_neun] 이제 엘레드의 마음을 거절할 수밖에 없다." id c05_w_0304
    "그래 놓고서 데이트에 대해 상담하는 건 [pl_name][josa_i_ga] 생각해도 이상했다." id c05_w_0305

    c sleep "(으, 모르겠다. 나중에 생각하자.)" id c05_w_0306
    "[pl_name][josa_eun_neun] 잡생각을 치우고 요리를 가방에 넣었다." id c05_w_0307

    stop music fadeout 2.5

    # 용병단 훈련장 배경으로
    scene bg practice_range with Fade(0.8, 0.8, 0.8)
    play music "documentary-116953.mp3" fadein 2.5 volume 0.55
    "{i}~잠시 후~{/i}" id c05_w_0308

    show wolf out_d base
    with dissolve

    c talk "\"이제 다 온 거지? 생각보다 멀리 있네...\"" id c05_w_0309
    "[pl_name][josa_eun_neun] 가헬과 함께 걸어서 용병단의 거점에 도착했다." id c05_w_0310
    "가헬의 용병단 브로치가 열쇠처럼 작동하는 보안 장치는 꽤 신기했다." id c05_w_0311

    show wolf out_u talk
    with dissolve

    w "\"전송 마법진을 쓸 걸 그랬나?\"" id c05_w_0312
    
    show wolf out_d base
    with dissolve

    c ddam2 "\"그, 그렇게까지 비싼 돈 내고 갈 거리는 아니야.\"" id c05_w_0313
    
    "[pl_name][josa_i_ga] 손사래를 치자 가헬은 순순히 고개를 끄덕였다." id c05_w_0314

    show wolf out_u talk
    with dissolve

    w "\"여기가 \'칼루리엔\'의 야영지 겸 훈련장이다.\"" id c05_w_0315

    show wolf shy5
    with dissolve

    w "\"평소에는 훈련까지 포함해서 뛰어오는 편이지만, 오늘은 데이트하러 온 거니까...\"" id c05_w_0316
    
    show wolf shy2
    with dissolve

    "가헬은 \'데이트\'를 말하며 좋은 건지 부끄러운 건지 모를 홍조를 띄웠다." id c05_w_0317

    show wolf out_d base
    with dissolve

    c ddam "\"뛰어서? 걷기만 해도 힘든 것 같은데...\"" id c05_w_0318
    
    "[pl_name][josa_eun_neun] 주변을 둘러보며 시설을 구경하다가 조금 어색하게 말했다." id c05_w_0319

    c talk "\"으음, 생각보다는 평범하네.\"" id c05_w_0320
    
    "보안 장치처럼 안에도 뭔가 마법적인 물건이 많을 줄 알았다." id c05_w_0321
    "하지만 텐트와 훈련용 나무 기둥은 더할 나위 없이 평범해 보였다." id c05_w_0322
    "오히려 용병단의 명성에 비하면 부실한 것 아닌가 하는 생각이 들었다." id c05_w_0323
    
    show wolf out_u talk
    with dissolve
    
    w "\"아무래도 여기는 나 말고 쓰는 수인이 없어서...\"" id c05_w_0324
    w "\"기본적인 것을 빼면 대부분 본부로 돌려보냈다.\"" id c05_w_0325

    show wolf out_d base
    with dissolve

    c "\"본부가 따로 있어? 하긴 당연한 얘기인가...\"" id c05_w_0326
    
    show wolf :
        ease 0.25 yoffset 10
        ease 0.15 yoffset 0

    "가헬은 고개를 끄덕이고는 대답했다." id c05_w_0327
    
    show wolf out_u talk
    with dissolve

    w "\"우리는 대륙 전역에서 각자 활동하는 편이다. 다른 유명 용병단에 비하면 인원수는 적은 편이지.\"" id c05_w_0328
    
    show wolf out_d base
    with dissolve

    "[pl_name][josa_eun_neun] \'칼루리엔\'이 조금 특이하다고 생각하며 한가지 질문을 꺼냈다." id c05_w_0329

    menu:
        "용병의 강함에 관해 물어본다." :
            c talk "\"그럼 용병단원은 전부 엄청나게 강하겠네? 용병 길드에서 평가가 그렇게까지 좋으려면...\"" id c05_w_0330
            
            "[pl_name][josa_eun_neun] 용병 길드 게시판에서 항상 \'칼루리엔\'을 볼 수 있었다." id c05_w_0331
            "소수의 인원으로 그 정도 점수를 받으려면, 그냥 \'실력이 좋다\'로는 부족할 것이다." id c05_w_0332

            c question2 "\"왕국에서 손꼽는 강자만 모인 거 아냐?\"" id c05_w_0333
            
            "생각보다 더 엄청난 용병과 계약하고, 연애까지 하게 된 [pl_name][josa_eun_neun] 놀라움에 눈을 반짝였다." id c05_w_0334
            "[pl_name]의 말에 가헬은 조금 난감한 듯 웃었다." id c05_w_0335
            
            show wolf out_u smile
            with dissolve
            
            w "\"다들 강한 건 사실이지만...\"" id c05_w_0336
            
            $ unlock_info_tag(3, "5")
            $ display_text = _("정보 : 용병왕")
            show screen affection_indicator

            c "\"{color=#ee3939}'용병왕'{/color}의 전설처럼 막 순위대로 번호를 부여받고 그러는 거야?\"" id c05_w_0337
            
            show ddam at ddam_move (930,40)
            show wolf talk
            with dissolve
            hide ddam
            with dissolve

            w "\"그, 그건 전설이다. 요즘 용병에게 그런 순위는 없다.\"" id c05_w_0338

            show wolf out_d base
            with dissolve
            
            "[pl_name][josa_eun_neun] 상식이 깨진 표정으로 되물었다." id c05_w_0339

            c talk "\"하지만 용병왕은 실존했던 수인이잖아? 그리고 길드에 있던 순위는...\"" id c05_w_0340
            
            show wolf talk
            with dissolve

            w "\"그 후손이 살아있는 건 사실이지만... 아무튼 용병의 순위는 강한 순서가 아니다. 실적 등으로 매겨지는 평가점수에 불과하다.\"" id c05_w_0341
            
            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 조금 실망스러운 표정을 했다. 용병에 대한 환상이 약간 깨지긴 했지만, [pl_name][josa_eun_neun] 다른 질문을 꺼냈다." id c05_w_0342
            
            c question2 "\"그럼 가헬은 용병단에서 어느 정도 강해?\"" id c05_w_0343
            
            show wolf out_u talk
            with dissolve

            w "\"으음, 단순히 힘으로 따지면 중간 정도? 각자 장점이 다르기 때문에 단언하기 힘들군. 나는 마물 토벌에 강한 편이다.\"" id c05_w_0344
            
            show wolf out_d base
            with dissolve

            c talk "\"아 맞아. 몇 달 전에 마물 토벌 작전이 있었지...\"" id c05_w_0345
            
            "백작의 명령으로 기사단이 나설 정도의 일이었다." id c05_w_0346
            "그리고 그 일의 여파로 [pl_name][josa_wa_gwa] 가헬은 하마터면 던전에서 목숨을 잃을 뻔했다." id c05_w_0347

            c base "(지금 생각하니 엄청 위험했지, 그 날...)" id c05_w_0348
            
            "[pl_name][josa_eun_neun] 새삼 가헬이 뛰어난 용병이라서 다행이라고 생각했다." id c05_w_0349

        "용병의 일상에 관해 물어본다." :
            c question2 "\"가헬이나 단원들은 평소에 뭐 해? 그러니까, 쉴 때라던가 말이야.\"" id c05_w_0350

            show wolf out_u talk
            with dissolve

            w "\"... 회의를 위해 모일 때를 제외하면, 종종 같이 술을 마실 때는 있다.\"" id c05_w_0351

            show wolf out_d base
            with dissolve

            c talk "\"그건 조금... 예상할 수 있는 모습이네.\"" id c05_w_0352

            "용병들이 술집에 모여있는 건 아주 흔한 일이다." id c05_w_0353
            "조금 맥이 빠진 [pl_name][josa_eun_neun] 다른 질문을 꺼냈다." id c05_w_0354

            c "\"그럼 뭔가 취미로 하는 거 있어?\"" id c05_w_0355
            
            show wolf talk
            with dissolve

            w "\"... 지금은 없다.\"" id c05_w_0356
            
            show wolf base
            with dissolve

            c consider "(지금은?...)" id c05_w_0357
            
            "가헬의 미묘한 대답에 [pl_name][josa_eun_neun] 가헬이 취미 생활을 못 하게 된 이유를 생각했다." id c05_w_0358
            
            c talk "\"나 대신 가게 일을 하느라 시간이 모자란 거 아냐?\"" id c05_w_0359

            show wolf out_u talk
            with dissolve

            w "\"그런 건 아니다. 그냥... 시간이 남을 땐 훈련을 하고 있다.\"" id c05_w_0360
            
            show wolf out_d base
            with dissolve

            c "\"쉬는 때가 없는 것 같네...\"" id c05_w_0361
            
            "[pl_name][josa_eun_neun] 가헬이 가게 일을 도와주는 것에 자꾸만 익숙해지고 있었다." id c05_w_0362
            "이제 연인이니 더욱 마음이 느슨해진 것도 있다." id c05_w_0363

            c consider "(이러다가 가헬 없으면 아무것도 못 하는 거 아냐?)" id c05_w_0364
            
            with vpunch
            c ddam "(.... 헉!)" id c05_w_0365
            
            "진실(?)을 깨달은 [pl_name][josa_eun_neun] 식은땀을 흘렸다." id c05_w_0366

            "너무 가헬에게 의존하다가는 하루 종일 애벌레처럼 꾸물거리기만 할지도 모른다." id c05_w_0367

            show wolf talk
            with dissolve

            w "\"[pl_name][josa_eun_neun] 어떤가?\"" id c05_w_0368
            
            show wolf base
            with dissolve

            c talk "\"나? 나는 남는 시간에 연금술 서적을 읽어. 독학이라 그런지 아직 배울 게 많더라고.\"" id c05_w_0369

            show wolf happy
            with dissolve

            "가헬은 [pl_name][josa_i_ga] 책에 집중하는 모습이 생각났다. 멋진 외모에 어울리는 취미라고 생각했다." id c05_w_0370

        "용병의 자금에 관해 물어본다." :
            c question2 "\"단체로 활동하지 않으면, 돈도 각자 사용하겠네?\"" id c05_w_0371
            
            show wolf out_u talk
            with dissolve

            w "\"그렇다. 공용 자금이 없는 건 아니지만, 대형 용병단에 비하면 적은 편이다.\"" id c05_w_0372
            
            show wolf out_d base
            with dissolve

            c consider "(하긴 가헬도 단독계약이었지...)" id c05_w_0373
            
            "[pl_name][josa_eun_neun] 예전에 어떤 용병과 계약할 때, 계약서에 \'예비 용병 비용\'이 있었던 게 기억났다." id c05_w_0374
            "가헬은 소속 용병단이 있지만 그런 내용이 없었다." id c05_w_0375
            "[pl_name][josa_i_ga] 과거에 있었던 일을 얘기하자 가헬이 설명을 시작했다." id c05_w_0376
            
            show wolf out_u talk
            with dissolve

            w "\"대형 용병단은 대부분 그렇게 계약하는 편이다.\"" id c05_w_0377
            w "\"임무 도중 용병이 다쳤을 때, 대리인으로 임무를 계속하는 것이다.\"" id c05_w_0378
            w "\"평소에는 후방 지원을 맡기거나 한다.\"" id c05_w_0379
            
            show wolf out_d base
            with dissolve

            c talk "\"계약금을 비싸게 받으려는 속임수는 아니었구나...\"" id c05_w_0380
            
            "가헬은 조금 씁쓸한 표정으로 대답했다." id c05_w_0381
            
            show wolf out_u sigh
            with dissolve

            w "\"그런 목적이 아예 없다고는 할 수 없겠군. 머릿수가 많으면 지출도 늘어나기 마련이니...\"" id c05_w_0382
            
            show wolf out_d base
            with dissolve

            c sigh "\"으음, 장사 하는 입장에서 이해가 가.\"" id c05_w_0383
            
            "[pl_name][josa_eun_neun] 어깨를 으쓱했다." id c05_w_0384

        "아무것도 묻지 않는다." :

            c consider "(음... 용병단에 대한 건 그냥 물어보지 말까?)" id c05_w_0385
            
            "[pl_name][josa_eun_neun] 가헬의 말에 그냥 고개를 끄덕였다." id c05_w_0386

    show wolf out_u talk
    with dissolve

    w "\"그러고 보니 훈련하는 모습을 보여줘야겠군.\"" id c05_w_0387

    w "\"위험하니 이쪽에 앉아서 구경해라.\"" id c05_w_0388

    show wolf out_d base
    with dissolve

    "[pl_name][josa_eun_neun] 가헬이 가져다준 작은 의자에 앉았다." id c05_w_0389

    show wolf sword_d base
    with dissolve

    "가헬은 나무 기둥 앞에서 검을 꺼내 들고 [pl_name][josa_eul_reul] 보며 말했다." id c05_w_0390
    
    show wolf sword_u talk
    with dissolve

    w "\"원래 검술 훈련은 실전과 유사해야 하지만, 오늘은 좀 기본적인 것부터 보여주겠다.\"" id c05_w_0391
    
    show wolf base
    with dissolve

    play sound "effect/sword_slice.mp3" volume 0.7
    show sword_slash at slash2
    pause 0.2
    hide sword_slash

    pause 0.3

    play sound "effect/sword_slice2.mp3" volume 0.7
    show sword_slash2 at slash
    pause 0.2
    hide sword_slash2
    pause 0.5

    "가헬은 검을 쥐고 허공을 빠르게 베어냈다." id c05_w_0392
    
    show wolf talk
    with dissolve

    w "\"이렇게 기본적인 베기 동작부터 시작해서...\"" id c05_w_0393

    show wolf base
    with dissolve

    play sound "effect/sword_slice.mp3" volume 0.7
    show sword_slash at slash2
    pause 0.13
    hide sword_slash

    pause 0.23

    play channel1 "effect/sword_slice.mp3" volume 0.7
    show sword_slash2 at slash
    pause 0.13
    hide sword_slash2
    
    pause 0.25

    play sound "effect/sword_slice2.mp3" volume 0.7
    show sword_slash3 at slash2
    pause 0.2
    hide sword_slash3
    pause 0.5

    # 가헬의 연속공격!

    "가헬은 춤추듯 움직이며 연속으로 검을 휘둘렀다." id c05_w_0394
    
    "보여주기 위한 움직임이라 그런지 실전보다는 느린 느낌이었다." id c05_w_0395
    
    show wolf talk
    with dissolve

    w "\"이건 상대를 몰아치는 방식이다.\"" id c05_w_0396
    
    w "\"사실 평소에 이런 동작을 할 기회는 별로 없다. 주로 대련에서 보여주기용으로나 쓰는 편이지.\"" id c05_w_0397
    
    show wolf out_d base
    with dissolve

    "가헬은 검을 검집에 넣고 동작을 마무리 했다." id c05_w_0398

    c talk "\"그래도 확실히 멋있네.\"" id c05_w_0399

    show wolf happy
    with dissolve

    "가헬은 조금 뿌듯한지 수줍은 미소를 지었다." id c05_w_0400

    show wolf talk
    with dissolve

    w "\"실전에서는 더 변칙적인 움직임으로 허점을 찔러야 한다. 마물을 상대할 때는 속도도 중요하고...\"" id c05_w_0401

    show wolf base
    with dissolve

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 50)

    "가헬은 마치 검술 교사처럼 조곤조곤 말하다가 갑자기 다른 생각이 떠올랐다." id c05_w_0402

    hide exclamation
    show wolf out_u talk
    with dissolve

    w "\"[pl_name]도 무기를 익혀보는 게 어떤가?\"" id c05_w_0403

    c question2 "\"무기? 내가?\"" id c05_w_0404

    w "\"호신용이 아니어도 좋다. 취미로 배울 수 있는 것도 많으니까.\"" id c05_w_0405

    show wolf out_d base
    with dissolve

    "[pl_name][josa_eun_neun] 어떤 무기를 사용해야 할지 고민했다." id c05_w_0406

    menu:
        
        "투척 무기 사용법을 배우면 실용적이지 않을까?" :
            $ display_text = _("가헬 호감도 변화")
            show screen affection_indicator 

            c question2 "\"던지기도 배울 수 있을까?\"" id c05_w_0407
            
            c talk "\"미리 마법을 담아두고 던져서 사용하는 무기도 많으니까, 던전에서 유용하게 쓸 수 있을 거 같아.\"" id c05_w_0408
            
            show wolf out_u talk
            with dissolve
            
            w "\"전문 분야는 아니지만 간단한 훈련이라면 도와줄 수 있다.\"" id c05_w_0409

            show wolf out_d base
            with dissolve

            "가헬은 구석에 놓여있던 자루의 끈을 풀고 무언가를 꺼냈다." id c05_w_0410

            c question2 "\"이게 뭐야?\"" id c05_w_0411
            
            show wolf out_u talk
            with dissolve

            w "\"그냥 돌멩이다. 자루째로 들어 올려서 근육 훈련에 쓰지만, 지금은 이 돌멩이를 던지는 데 쓰도록 하지.\"" id c05_w_0412
            
            show wolf out_d base
            with dissolve

            c ddam2 "\"마땅히 던질 게 없나보네...\"" id c05_w_0413

            "[pl_name]의 말에 가헬은 조금 시무룩한 표정으로 대답했다." id c05_w_0414
            
            show wolf out_u sad2_am
            with dissolve

            w "\"그, 그렇다...\"" id c05_w_0415

            show wolf talk
            with dissolve

            w "\"그리고 날카로운 물건은 잘못 던지면 튕겨 나와서 다칠 수 있다.\"" id c05_w_0416
            
            show wolf out_d base
            with dissolve

            "멋지게 단검을 던지는 걸 상상했던 [pl_name][josa_eun_neun] 아쉬움을 삼키고 돌멩이를 집어 들었다." id c05_w_0417
            
            c talk "\"이 정도 무게면 폭탄보다 살짝 가볍네.\"" id c05_w_0418
            
            play sound "effect/boing.mp3" volume 0.9
            show question at question_move (890, 0)
            show wolf talk
            with dissolve

            w "\"마법 폭탄은 화약이 없지 않나? 그렇게까지 무거울 것 같지 않은데...\"" id c05_w_0419
            
            hide question
            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 던전에 갈 때 사용하던 연막 폭탄을 생각하며 대답했다." id c05_w_0420
            
            c "\"그런 건 소모품이라서 좋은 재료는 못 쓰거든.\"" id c05_w_0421
            c consider "\"보석을 소모품처럼 쓸 수 있으면 상관없겠지만... 그 정도로 돈을 펑펑 쓸 거면 용병을 잔뜩 고용하겠지.\"" id c05_w_0422
            
            show wolf out_u talk
            with dissolve
            
            w "\"그렇군...\"" id c05_w_0423
            
            show wolf out_d base at walk (0, 2.5, 4)
            play sound "effect/footstep.mp3" volume 0.9
            pause 2.0

            "가헬은 나무 기둥에서 꽤 멀찍이 떨어져서 거리를 가늠했다." id c05_w_0424
            
            show wolf out_u talk
            with dissolve

            w "\"급소를 노리거나 할 필요는 없을 테니, 맞추는 것부터 목표로 하지.\"" id c05_w_0425
            
            show wolf out_d base
            with dissolve

            "그렇게 [pl_name][josa_eun_neun] 한동안 돌을 던져서 나무 기둥을 맞추는 연습을 했다." id c05_w_0426
            "생각보다 맞추기 어려워서 [pl_name][josa_eun_neun] 자루가 텅 빌 때까지 돌을 던졌다." id c05_w_0427
        
        "마력을 담아서 사슬이나 채찍을 쓸까?" :
            # 호감도1 섭1
            $ wolf_love +=1
            $ wolf_sub +=1
            $ display_text = _("가헬 호감도 변화")
            show screen affection_indicator 
            
            c talk "\"기왕 배우는 거 호신용이 좋지 않을까?\"" id c05_w_0428

            show wolf out_u talk
            with dissolve

            w "\"그렇다면 단봉이 어떤가? 배우기도 쉽고 가벼워서 쓰기 편하다.\"" id c05_w_0429
            
            show wolf out_d base
            with dissolve

            "[pl_name][josa_eun_neun] 고개를 저었다." id c05_w_0430

            c "\"사슬이나 채찍 같은 걸로 휘감으면 간단하게 제압할 수 있지 않겠어?\"" id c05_w_0431
            
            show ddam at ddam_move (930,40)
            show wolf out_u talk
            with dissolve
            hide ddam
            with dissolve

            w "\"그, 그렇긴 하다만... 그렇게 제압하려면 힘이 꽤 필요하다.\"" id c05_w_0432
            
            show wolf out_d base
            with dissolve

            "가헬은 [pl_name]의 무기 선택에 약간 당황했다." id c05_w_0433
            "도구면 모를까 무기로 채찍을 쓰는 경우는 그렇게 많지 않다." id c05_w_0434

            show wolf happy
            with dissolve

            w "(하지만 채찍을 쓰는 [pl_name]의 모습이라...)" id c05_w_0435

            show wolf shy2
            with dissolve

            w "(생각해보니 그것도 꽤 매력적일 것 같군...)" id c05_w_0436

            show wolf base
            with dissolve

            c consider "\"마법으로 할 수 있을 것 같은데...\"" id c05_w_0437

            c talk "\"재질만 괜찮으면 아티팩트가 아니어도 되지 않을까?\"" id c05_w_0438

            show wolf out_u talk
            with dissolve

            w "\"우선 어디를 어떻게 묶어야 하는지부터 배워야겠군...\"" id c05_w_0439
            
            show wolf out_d base at mirror
            with dissolve
            pause 0.5
            show wolf at walk (1500, 2.8, 5)
            play sound "effect/footstep.mp3" volume 0.9
            pause 3.0
            show wolf at mirror2
            show wolf at walk (0, 2.8, 5)
            play sound "effect/footstep.mp3" volume 0.9
            pause 1.5

            "가헬은 미묘한 표정으로 밧줄을 꺼내왔다." id c05_w_0440

            show wolf shy
            with dissolve

            "무기가 아니라 다른 방법으로 사용하는 상황이 저절로 생각났다." ##추가
            "가헬에게 그런 취향은 없었지만, 해보기 전에는 모를 일이었다." id c05_w_0441

            c question2 "\"가헬?\"" id c05_w_0442

            show wolf base at surprise_move

            w "아, 여기. 이걸 잡아라." id c05_w_0443

            "가헬은 부끄러운 상상에서 깨어나, 묶는 법을 보여주는 것에 집중했다." ##추가
            "[pl_name]에게 밧줄 뭉치를 건네주고 가헬은 한쪽 끝을 잡았다." id c05_w_0444
            
            show wolf out_u talk
            with dissolve

            w "\"당연한 얘기지만, 가능하면 손부터 제압하는 게 좋다.\"" id c05_w_0445
            w "\"두 손의 거리를 통제하기만 해도 승부가 결정되는 셈이지.\"" id c05_w_0446
            
            show wolf out_d base
            with dissolve

            "가헬이 설명과 함께 밧줄로 엉성하게 양손을 감았다." id c05_w_0447
            
            show wolf talk
            with dissolve

            w "\"흔히 죄수를 묶는 것처럼 이렇게 하면-\"" id c05_w_0448
            
            c question2 "\"이렇게?\"" id c05_w_0449
            
            play sound "effect/magic.mp3" volume 0.7
            show bluelight at magic
            pause 0.2
            hide bluelight at magic
            pause 0.5

            "[pl_name][josa_eun_neun] 밧줄에 마력을 불어넣어 가헬의 손목을 강하게 조였다." id c05_w_0450
            
            play sound "effect/ping.mp3" volume 0.75
            show exclamation at exclamation_move (1050, 40)
            show wolf bigeye at surprise_move

            "갑작스레 손이 묶인 가헬은 크게 당황했다." id c05_w_0451

            show wolf shy
            with dissolve

            "가헬은 자꾸만 폭주하려는 망상을 간신히 참으며 말을 이었다"  ##추가        
            
            hide exclamation
            show wolf shy5
            with dissolve

            w "\"그... 렇다.\"" id c05_w_0452
            
            show wolf talk
            with dissolve

            w "\"힘으로 풀리지 않게 매듭을 하는 것도 중요하다.\"" id c05_w_0453
            
            show ddam at ddam_move (930,40)
            show wolf embarrass
            with dissolve
            hide ddam
            with dissolve

            "가헬은 생각보다 강하게 묶인 밧줄에 식은땀을 흘렸다." id c05_w_0454
                
            show wolf base :
                ease 0.15 xoffset 10
                ease 0.10 xoffset 0
                ease 0.15 xoffset 10
                ease 0.10 xoffset 0

            "다행히 [pl_name][josa_i_ga] 이상하게 생각하기 전에 팔을 빼낼 수 있었다." id c05_w_0455
            
            show wolf out_u talk
            with dissolve

            w "\"생각보다 실용성이 있겠군...\"" id c05_w_0456
            
            show wolf out_d base
            with dissolve

            c question2 "\"그래? 좀 더 진지하게 묶는 법을 배워야 하나?\"" id c05_w_0457
            
            "가헬은 [pl_name]에게 묶여있는 자기 모습을 상상했다." id c05_w_0458
            
            show wolf shy3 at surprise_move
            
            "다시 머릿속에서 그려진 음란한 상황 때문에, 얼굴에 열이 확 오르고 부끄러워졌다." ##추가
            
            show wolf out_u shy5
            with dissolve

            w "\"나는 그런 쪽은 전문가가 아니라서... 내가 가르쳐주기는 어렵군.\"" id c05_w_0459
            
            show wolf out_d base
            with dissolve

            c talk "\"그건 아쉽네. 이건 허점을 찌르는 비장의 수단으로 써야겠어.\"" id c05_w_0460
            
            show wolf out_u talk
            with dissolve

            w "\"좋은 생각이다. 지금은 우선 간단한 검술을 배우는 게 어떤가?\"" id c05_w_0461
            
            w "\"직접 검을 써도 좋고, 상대의 행동을 예측하는 데도 도움이 될 거다.\"" id c05_w_0462
            
            show wolf out_d base
            with dissolve

            "가헬은 어떻게든 [pl_name]의 관심을 돌리기 위해 검술 얘기를 꺼냈다." id c05_w_0463
            "다행히 [pl_name][josa_i_ga] 속아 넘어간 덕분에, 둘은 한동안 검술 연습을 할 수 있었다." id c05_w_0464
        
        "취미라면 역시 가장 평범한 검을 배워볼까?" :
            # 호감도 1
            $ wolf_love +=1
            $ wolf_dom +=1
            $ display_text = _("가헬 호감도 변화")
            show screen affection_indicator 

            c talk "\"가볍게 몸을 움직이는 정도라면, 나도 검술을 배워볼까?\"" id c05_w_0465

            show wolf happy
            with dissolve

            "가헬은 [pl_name]에게 검술을 가르쳐 줄 생각에 기분이 좋아졌다." ##추가

            show wolf shy3
            with dissolve

            w "(이걸 빌미로 자연스럽게 몸도 만지게 될테고...)" id c05_w_0466

            show wolf at mirror
            with dissolve
            pause 0.5
            show wolf at walk (1500, 2.8, 5)
            play sound "effect/footstep.mp3" volume 0.9
            pause 3.0
            show wolf base at mirror2
            show wolf at walk (0, 2.8, 5)
            play sound "effect/footstep.mp3" volume 0.9
            pause 1.5

            "가헬은 기다렸다는 듯, 연습용 목검을 들고 왔다." id c05_w_0467
            
            show wolf out_u talk
            with dissolve

            w "\"우선은 쥐는 법부터 가르쳐주겠다. 검의 이 부분을 잡고...\"" id c05_w_0468
            
            show wolf base
            with dissolve
            
            "[pl_name][josa_eun_neun] 가헬의 손 모양을 따라 목검을 쥐어보았다." id c05_w_0469
            
            with vpunch

            c ddam2 "\"이거 보기보다 무거운데. 나무 맞아?\"" id c05_w_0470
            
            show wolf talk
            with dissolve
            
            w "\"마법으로 가공해서 무게를 늘린 물건이긴 하다. 이 정도면 시작하기에 나쁘지 않은 정도인데...\"" id c05_w_0471
            
            show wolf base
            with dissolve
            
            c question2 "\"그러면 진짜 검은 이것보다 훨씬 무겁겠네?\"" id c05_w_0472
            
            show wolf :
                ease 0.25 yoffset 10
                ease 0.15 yoffset 0
                
            "가헬은 고개를 끄덕였다." id c05_w_0473
            
            show wolf talk
            with dissolve
            
            w "\"단검 같은 걸 제외하면 보통 5배 정도 무겁다.\"" id c05_w_0474
            
            show wolf base
            with dissolve
            
            "[pl_name][josa_eun_neun] 놀란 표정으로 대답했다." id c05_w_0475

            c ddam2 "\"그게 보통이라고? 휘두르면 몸이 휘청이는 거 아냐?\"" id c05_w_0476

            show wolf talk
            with dissolve
            
            w "\"맞다. 그러지 않기 위해 연습부터 철저히 해야 한다.\"" id c05_w_0477

            show wolf base
            with dissolve
            
            "[pl_name][josa_eun_neun] 몸을 움직일 생각에 벌써 귀찮아졌다. 그래도 곧바로 포기해 버릴 생각은 아니었다." id c05_w_0478
            
            c talk "\"이제 다음은 베는 법인가?\"" id c05_w_0479

            show wolf talk
            with dissolve
            
            w "\"그것도 맞지만, 발걸음도 함께 신경 써야 한다.\"" id c05_w_0480
            
            show wolf base at fwalk
            play sound "effect/footstep.mp3" volume 0.9
            pause 1.9

            show wolf :
                ease (1.3) yoffset 235
            pause 1.3
            show wolf talk
            with dissolve

            w "\"여기를 이쪽으로...\"" id c05_w_0481
            
            "가헬은 쭈그려 앉아 [pl_name]의 종아리를 잡았다." id c05_w_0482
            
            w "\"다리를 조금만 벌리고 허리를 낮춰서...\"" id c05_w_0483

            show wolf happy
            with dissolve

            "가헬은 자세를 잡아주며 은글슬쩍 [pl_name]의 허벅지 안쪽을 만졌다." ##추가

            c consider "... 이, 이렇게?" id c05_w_0484
            
            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 조금 이상하다고 생각했지만, 가헬의 지시대로 자세를 잡았다." id c05_w_0485
            "가헬에게 배우니 뭔가 본격적으로 훈련을 하는 느낌이었다." id c05_w_0486
            
            show wolf :
                ease (1.00) yoffset 153
            pause 1.0
            show wolf talk
            with dissolve

            w "\"한 걸음 나아가면서 동시에 베면 된다.\"" id c05_w_0487
            
            show wolf base
            with vpunch

            "갑자기 일어난 가헬이 [pl_name]의 귓가에 말해서 살짝 소름이 돋았다." id c05_w_0488
            "기분이 약간 이상했지만 일단 시키는 대로 했다." id c05_w_0489

            play sound "effect/weakslash.mp3" volume 0.9
            pause 0.3

            "나무 막대기가 허공을 가르며 작은 바람 소리를 냈다." id c05_w_0490
            
            show wolf talk
            with dissolve

            w "\"힘이 너무 많이 들어갔다. 정말로 뭔가를 베는 것보단 휘두르는 느낌으로 다시 해보자.\"" id c05_w_0491
            
            show wolf base
            with dissolve
            
            play sound "effect/weakslash.mp3" volume 0.85
            pause 0.5

            "[pl_name][josa_i_ga] 다시 한번 가볍게 움직이자 똑같은 소리가 났다." id c05_w_0492
            
            "뭐가 다른지 모르겠지만 가헬은 차이를 느낀 것 같다." id c05_w_0493
            
            show wolf talk
            with dissolve

            w "\"곧바로 좋아졌군. 어깨는 살짝 긴장을 풀고 팔과 손목이 너무 꺾이지 않게, 이런 자세로...\"" id c05_w_0494
            
            show wolf base
            with dissolve

            "가헬은 [pl_name]의 뒤에 딱 붙어서 [pl_name]의 자세를 바로잡았다." id c05_w_0495

            with hpunch
            "[pl_name][josa_eun_neun] 등에 닿는 가헬의 가슴 근육에 움찔했다." id c05_w_0496
            
            show wolf out_u shy5
            with dissolve

            w "\"힘을 빼라니까. 너무 긴장하지 말고...\"" id c05_w_0497
            
            show wolf happy
            with dissolve

            c ddam "(이젠 가헬의 말까지 좀 이상하게 들리는 기분인데...)" id c05_w_0498

            show wolf base
            with dissolve

            "[pl_name][josa_eun_neun] 마음을 다잡고 다시 자세를 잡았다." id c05_w_0499
            
            show wolf out_d at bwalk
            with Dissolve (0.2)
            play sound "effect/footstep.mp3" volume 0.9
            pause 1.5
            show wolf talk
            with dissolve

            w "\"좋다. 이번에는 아까와 수직이 되도록 베어보자.\"" id c05_w_0500
            
            show wolf base
            with dissolve

            "가헬이 몇 걸음 물러서자 드디어 [pl_name][josa_eun_neun] 안심하고 목검을 휘두를 수 있었다." id c05_w_0501
            "그렇게 [pl_name][josa_eun_neun] 한동안 가헬의 시범을 따라 목검을 휘둘렀다." id c05_w_0502

    stop music fadeout 2.5

    scene bg practice_range with Fade(0.8, 0.8, 0.8)
        
    "{i}~잠시 후~{/i}" id c05_w_0503

    c ddam "\"힘들어!\"" id c05_w_0504

    "[pl_name][josa_eun_neun] 지쳐서 훈련장에 그대로 주저앉아 버렸다." ##추가

    "가헬은 지쳐서 헥헥대는 [pl_name][josa_eul_reul] 보더니 말했다." id c05_w_0505

    show wolf out_u talk
    with dissolve

    w "그럼 잠깐 쉬도록 할까." id c05_w_0506

    show wolf out_d base
    with dissolve

    c ddam2 "\"그래...\"" id c05_w_0507
    
    "꽤 오랜 시간 몸을 움직인 탓에 [pl_name][josa_eun_neun] 더 이상 훈련을 하고 싶지 않았다." id c05_w_0508
    
    show wolf out_u talk
    with dissolve

    w "물도 마시고, 가져온 음식을 먹도록 하지." id c05_w_0509
    
    show wolf out_d smile
    with dissolve

    "[pl_name][josa_eun_neun] 그저 고개를 끄덕일 뿐이었다." id c05_w_0510

    "가헬은 [pl_name]의 모습에 미소를 짓고, 휴식할 장소를 물색했다." id c05_w_0511

    show wolf out_u talk
    with dissolve

    w "어디에서 먹을까?" id c05_w_0512

    menu :

        "커다란 나무 아래" :

            stop music fadeout 2.5
            jump under_tree

            

        "텐트 안" :
            
            stop music fadeout 2.5
            jump c5w_date2


label under_tree :
    
    scene bg practice_range :
        zoom 1.2
    with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    show wolf out_d base
    with dissolve

    c sigh "\"휴... 숨 좀 돌려야지.\"" id c05_w_0513

    "나무 그늘은 [pl_name][josa_wa_gwa] 가헬이 모두 들어갈 만큼 컸다." id c05_w_0514
    "[pl_name][josa_eun_neun] 나무에 기대앉고 푹 늘어졌다." id c05_w_0515

    show wolf out_u talk
    with dissolve

    w "\"수고 많았다.\"" id c05_w_0516

    show wolf out_d base
    with dissolve

    "가헬은 [pl_name]의 곁에 앉아서 미리 준비해 둔 음식을 꺼냈다." id c05_w_0517

    show roll_bread :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    c talk "\"고생한 보람이 있는 맛이어야 할텐데.\"" id c05_w_0518

    "\'베개 빵\'을 받아 든 [pl_name][josa_eun_neun] 그것을 크게 베어 물었다." id c05_w_0519

    hide roll_bread
    with dissolve

    "빵 속에 채소와 고기를 버무려 넣어서, 한입에 다양한 식감이 느껴진다." id c05_w_0520

    show wolf talk
    with dissolve

    w "\"맛은 어떤가?\"" id c05_w_0521

    show wolf base
    with dissolve

    c laugh "\"맛있어. 배고파서 그런 게 아니라 진짜로.\"" id c05_w_0522

    "가헬도 빵을 한입 물었다." id c05_w_0523

    show wolf out_u sad_am
    with dissolve

    w "\"고기를 조금 더 넣을 걸 그랬군...\"" id c05_w_0524

    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] 가헬의 음식 취향을 떠올리며 가볍게 웃었다." id c05_w_0525
    "반 정도 먹어 치우고 나니, 왜 점심으로 인기 있는지 알 것 같았다." id c05_w_0526
    "식사하는 데 걸리는 시간이 짧아지는 요리였다." id c05_w_0527

    c talk "\"먹기 편해서 지역 명물인가봐? 나 같아도 자주 사 먹을 것 같아.\"" id c05_w_0528

    c consider "\"근데 만들기는 약간 귀찮은 걸...\"" id c05_w_0529
    
    show wolf talk
    with dissolve

    w "\"글쎄. 대량으로 만들어 팔 정도면, 편한 방법이 있을지도 모르겠군.\"" id c05_w_0530

    show wolf out_d base
    with dissolve

    "[pl_name][josa_eun_neun] \'나중에 동부에 직접 가볼까\' 같은 생각을 하며 식사를 마무리했다." id c05_w_0531

    # stop music fadeout 2.5
    jump c5w_date_end

label c5w_date2:
    # 용병단 텐트 안쪽 배경
    scene bg tent with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    play sound "audio/effect/sigh.mp3" volume 0.23

    c sigh "\"휴... 드디어!\"" id c05_w_0532

    "텐트 안에 작은 침상이 있어서 다행이었다." id c05_w_0533
    "[pl_name][josa_eun_neun] 곧바로 침상에 걸터앉아 푹 늘어졌다." id c05_w_0534

    show wolf out_u talk
    with dissolve

    w "\"수고 많았다.\"" id c05_w_0535

    show wolf out_d base
    with dissolve

    "가헬은 [pl_name]의 옆에 앉아서 미리 준비해 둔 음식을 꺼냈다." id c05_w_0536

    show roll_bread :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    c talk "\"아, 고마워.\"" id c05_w_0537

    "\'베개 빵\'을 받아 든 [pl_name][josa_eun_neun] 그것을 크게 베어 물었다." id c05_w_0538

    hide roll_bread
    with dissolve

    "빵 속에 채소와 고기를 버무려 넣어서, 한입에 다양한 식감이 느껴진다." id c05_w_0539

    show wolf talk
    with dissolve

    w "\"맛은 어떤가?\"" id c05_w_0540

    show wolf base
    with dissolve

    c laugh "\"좋아. 가헬이 만든 건데 당연히 맛있지.\"" id c05_w_0541

    "가헬도 빵을 한입 물었다." id c05_w_0542

    show wolf out_u sad_am
    with dissolve

    w "\"고기를 조금 더 넣을 걸 그랬군...\"" id c05_w_0543

    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] 가헬의 음식 취향을 떠올리며 가볍게 웃었다." id c05_w_0544
    "반 정도 먹어 치우고 나니, 왜 점심으로 인기 있는지 알 것 같았다." id c05_w_0545
    "식사하는 데 걸리는 시간이 짧아지는 요리였다." id c05_w_0546

    c talk "\"먹기는 편한데 만들기는 조금 번거롭네. 빵 속을 파내기가 귀찮은 거 같아.\"" id c05_w_0547
    c consider "\"빵을 구울 때 미리 모양을 만들 수 없나?...\"" id c05_w_0548
    
    show wolf talk
    with dissolve

    w "\"글쎄. 대량으로 만들어 팔 정도면, 편한 방법이 있을지도 모르겠군.\"" id c05_w_0549

    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] \'나중에 동부에 직접 가볼까\' 같은 생각을 하며 식사를 마무리했다." id c05_w_0550

    # stop music fadeout 2.5
    jump c5w_cg3

label c5w_cg3 :
    # 용병단 텐트 안쪽 배경
    scene bg tent with Fade(0.8, 0.8, 0.8)
    $ persistent.wolf_unlocked[2]= True

    show wolf out_d
    with dissolve

    c consider "\"훈련도 했고, 점심도 먹었고. 음?...\"" id c05_w_0551

    "[pl_name][josa_eun_neun] 궤짝 위에 쌓여있는 잡동사니를 발견했다." id c05_w_0552
    "가헬의 성격답게 깔끔하게 정리해 놓았지만, 뭔가 눈에 띄는 물건이 있었다." id c05_w_0553

    play sound "effect/paper_up.mp3" volume 0.85

    "[pl_name][josa_eun_neun] 그것을 집어 들었다." id c05_w_0554

    c question2 "\"이게 뭐야?\"" id c05_w_0555

    "그것은 일반적인 책의 크기 정도에 종이처럼 얇았다." id c05_w_0556
    "접히지 않을 정도로 단단한 재질로 만들어져있고, 겉에는 가헬의 모습이 그려져 있었다." id c05_w_0557
    "가헬은 흠칫 놀라며 말했다." id c05_w_0558

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 40)
    show wolf embarrass at surprise_move

    w "\"그, 그건 예전에...\"" id c05_w_0559

    hide exclamation
    show wolf pit
    with dissolve
    pause 0.2

    show wolf_s3_01
    with Fade(0.8, 0.8, 0.8) 

    "과거의 가헬은 뭔가 신기한 복장을 하고 있었다." id c05_w_0560
    "가헬은 본 적 없는 스타일의 바지를 입고 상의는 벗은 채로 근육을 과시하는 자세를 하고 있었다." id c05_w_0561
    "핏줄이 보일 정도로 아주 자세한 그림이었다." id c05_w_0562
    "현실을 보이는 그대로 담아내서 초정밀 그림으로 만들어내는 도구를 사용한 것 같다." id c05_w_0563

    c "\"이건 무슨 그림이야? 굉장히 고급 아티팩트로 만든 것 같은데...\"" id c05_w_0564
    
    "가헬은 별로 떠올리고 싶지 않은 과거의 사건이 생각나 버렸다." id c05_w_0565
    "어떻게 말해야 할지 고민하는 기색이 역력했다." id c05_w_0566

    w out_u sad2_am "\"음... 과거에 홍보용으로 썼던 그림이다.\"" id c05_w_0567
    w "\"수컷의 매력을 극대화하는 복장이라고 하던데...\"" id c05_w_0568

    c base "(어느 나라의 문화인지는 몰라도 확실히 매력적인 느낌이 있네.)" id c05_w_0569
    
    c question2 "\"이 기다란 건 뭐야? 밧줄치고는 너무 굵은데.\"" id c05_w_0570

    w sad3_am "\"나도 잘 모르겠군... 시키는 대로 입은 거라 설명은 듣지 못했다.\"" id c05_w_0571

    "가헬은 이 얘기를 더 이어가고 싶지 않았지만, [pl_name][josa_eun_neun] 전혀 눈치채지 못했다." id c05_w_0572
    
    c consider "\"뭔가... 분위기가 다르네.\"" id c05_w_0573

    "그림 속 가헬과 지금의 가헬은 키나 근육이 크게 달라 보이지 않았다." id c05_w_0574
    "하지만 몇몇 흉터가 없고 표정도 미묘하게 달랐다." id c05_w_0575
    "뭐라고 콕 찍어 말할 수 없었지만, [pl_name][josa_eun_neun] 그것이 용병의 경력 차이라고 생각했다." id c05_w_0576

    c talk "\"용병은 이런 일도 하는구나.\"" id c05_w_0577
    
    w embarrass "\"크흠! 뭐... 초보 용병일 땐 일을 가릴 처지가 아니니까.\"" id c05_w_0578

    hide wolf_s3_01
    with Fade(0.8, 0.8, 0.8)

    "사실 그때 가헬은 반쯤 속은 채로 계약했다." id c05_w_0579

    "한 푼이 아쉬운 시기에 무리한 요구를 거절하지 못했다." id c05_w_0580
    
    show wolf shy2
    with dissolve

    w shy2 "(그러다가 결국 \'그런\' 모습까지...)" id c05_w_0581
    
    show wolf shy3
    with dissolve

    "가헬은 정말 부끄러운 일이 생각나서 얼굴이 붉게 달아올랐다." id c05_w_0582
    "주제를 돌리고 싶었지만, [pl_name][josa_i_ga] 한발 빨랐다." id c05_w_0583
    
    c question2 "\"그럼 이건 기념품으로 하나 준 거야?\"" id c05_w_0584
    
    show wolf out_u shy5
    with dissolve

    w "\"음... 그렇다.\"" id c05_w_0585
    
    show wolf out_d shy2
    with dissolve

    c talk "\"꽤 비싼 물건을 줬네. 이건 투영 기능이 있는 아티팩트야.\"" id c05_w_0586
    
    "[pl_name][josa_eun_neun] 그림 속 가헬의 위에 손을 올리고 마나를 불어넣었다." id c05_w_0587

    show wolf_s3_01
    with Fade(0.8, 0.8, 0.8)

    play sound "effect/magic.mp3" volume 0.7
    show bluelight at magic
    pause 0.2
    hide bluelight at magic
    pause 0.5
    
    # 가헬 19금 cg

    c "\"이렇게 하면 미리 투영된 다른 그림이...\"" id c05_w_0588

    show wolf_cg3 horny
    with dissolve
    
    # cg 숨기기

    play sound "effect/ping.mp3" volume 0.75
    pause 0.2

    c ddam2 "\"어?\"" id c05_w_0589

    hide wolf_s3_01
    hide wolf_cg3
    play sound "effect/weakslash.mp3" volume 0.9
    with vpunch
    
    
    hide exclamation
    show wolf out_u shy2
    with dissolve

    "가헬은 번개처럼 빠르게 [pl_name]의 손에서 그림을 낚아챘다." id c05_w_0590

    show wolf shy4
    with dissolve

    w "\"이, 이, 이, 이런 기능이 있는 줄은 몰랐다.\"" id c05_w_0591

    c base "(... 그런 그림이었구나.)" id c05_w_0592
    
    show wolf out_d shy3
    with dissolve

    "크게 당황한 가헬은 그림을 숨겼다. [pl_name][josa_eun_neun] 부끄러워하는 가헬에게 말했다." id c05_w_0593
    
    c talk "\"... 다른 얘기 할까?\"" id c05_w_0594

    show wolf shy
    with dissolve

    w "\"...\"" id c05_w_0595

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-110, -220)
    show wolf shy4
    with dissolve
    hide sigh
    with dissolve

    w "\"...\"" id c05_w_0596
    
    show wolf out_u shy5
    with dissolve

    w "\"... 고맙다.\"" id c05_w_0597

    show wolf out_d base
    with dissolve

    $ renpy.end_replay()

label c5w_date_end:

    "[pl_name][josa_i_ga] 다른 대화 주제를 꺼냈다." id c05_w_0598

    c question2 "\"가헬은 왜 용병이 되기로 했어? 역시 어릴 때부터 재능이 있었나?\"" id c05_w_0599
    
    show wolf out_u
    with dissolve

    "가헬은 살짝 멈칫했다. [pl_name][josa_eun_neun] 정말로 과거의 가헬을 기억하지 못하는 모양이다." id c05_w_0600

    show wolf talk
    with dissolve

    w "\"비슷하지만 조금 다르다. 어릴 때부터 가족이 없어서, 당장 먹고살기에 급했거든.\"" id c05_w_0601
    
    w "\"어쩌면 농부나 광부가 되었을지도 모르지.\"" id c05_w_0602

    show wolf out_d base
    with dissolve

    c talk "\"그랬구나. 나는... 비교적 상황이 좋았네.\"" id c05_w_0603
    
    "[pl_name][josa_eun_neun] 류호를 떠올리며 기억을 되짚었다." id c05_w_0604

    c "\"한 12년 정도 전에 스승님을 만나서 지낼 곳이 생겼지.\"" id c05_w_0605
    
    c sad_am "\"아무튼 스승님은 거의 항상 여행 중이라서... 혼자였던 날이 훨씬 많았지만.\"" id c05_w_0606
    
    "가헬은 처음 듣는 [pl_name]의 과거 얘기에 귀를 기울였다." id c05_w_0607

    c talk "\"스승님한테 배운 것으로 뭘 할 수 있을까 생각하다가, 마법 상점을 차리게 된 거야.\"" id c05_w_0608
    
    show wolf talk
    with dissolve

    w "\"... 스승님을 만나기 전에는?\"" id c05_w_0609
    
    show wolf base
    with dissolve

    "가헬의 질문에 [pl_name][josa_eun_neun] 잠시 생각에 빠졌다." id c05_w_0610

    c question2 "\"그 전에?...\"" id c05_w_0611
    c talk "\"글쎄, 기억이 잘 안 나는데.\"" id c05_w_0612
    
    "열심히 생각해 보려고 해도 머릿속에 떠오르는 게 거의 없었다." id c05_w_0613
    "아주 단편적인 순간만이 남아있었다." id c05_w_0614

    show wolf out_u talk
    with dissolve

    w "\"뭔가 더 어릴 때의 기억은 없나?\"" id c05_w_0615
    
    show wolf out_d base
    with dissolve

    c consider "\"어릴 때는 들판에서 뛰어다니고... 수영도 하고...\"" id c05_w_0616
    
    "가헬은 [pl_name]에게 보육원에 대해 말해야 할지 고민했다." id c05_w_0617
    "함께 놀았던 어린 시절을 [pl_name][josa_i_ga] 기억하지 못하는 게 너무 아쉬웠다." id c05_w_0618
    "하지만 괜히 안 좋은 기억까지 건드리고 싶지는 않았다." id c05_w_0619
    
    show wolf pit
    with dissolve

    w "(조심스럽게 물어볼까...)" id c05_w_0620
    
    show wolf out_u talk
    with dissolve

    w "\"보육원에서 지내던 시절은... 기억나지 않나?\"" id c05_w_0621
    
    show wolf out_d base
    with dissolve

    stop music fadeout 2.5

    c question2 "\"보육원?...\"" id c05_w_0622

    c talk "\"그, 그렇네? 나는 아버지들이 없으니까, 보육원에서 컸는데.\"" id c05_w_0623

    play sound "effect/dizzy.mp3" volume 0.65 fadein 1

    camera:
        perspective True
        parallel:
        
            ease 2 rotate 7
            ease 2 rotate -7

            repeat
        parallel:
        
            ease 2 zpos -220

    show wolf :
        
        xoffset 1

        parallel:
            
            ease 2 rotate 5
            ease 2 rotate -5
            repeat

        parallel:
            
            ease 2 zpos 40 yoffset 20
            repeat

    show dizzy :
        alpha 0 xalign 0.5 yalign 0.5
        

        parallel:     
            ease 2  rotate 3
            ease 2  rotate -3
            repeat

        parallel:
            
            ease 2 alpha 0.4


    c consider "\"왜... 잘 기억이 안 나지?\"" id c05_w_0624
    
    "분명 보육원에서 지내던 기억이 있는데, 자세히 떠올리려고 노력할수록 그 어떤 것도 기억나지 않았다." id c05_w_0625
    "물건을 같이 쓰는 게 싫었는데, 어떤 물건을 누구와 같이 썼는지 모르겠다." id c05_w_0626
    "[pl_name][josa_eun_neun] 텅 비어버린 기억에 기묘한 느낌이 들었다." id c05_w_0627
    
    c "(마치 책 위에 잉크를 엎은 것 같은... 아니, 페이지가 찢어진 책 같은...)" id c05_w_0628

    
    
    camera:
        perspective True
        parallel:
            ease 1.5 rotate 0
        parallel:
            ease 1.5 zpos 0
    show wolf :
        parallel:
            ease 1.5 rotate 0
        parallel:
            ease 1.5 zpos 0 yoffset 0
    show dizzy :
        ease 1.5 alpha 0
    

    pause 1.6
    

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 40)
    show wolf out_u talk at surprise_move

    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    w "\"[pl_name]? [pl_name]! 괜찮나? 무리해서 생각할 필요 없다.\"" id c05_w_0629
    
    hide exclamation
    hide wolf
    show wolf out_d fight3
    with dissolve  

    "가헬은 [pl_name][josa_i_ga] 보육원의 사고를 떠올리고 충격을 받은 건 아닌지 걱정했다." id c05_w_0630
    
    c talk "\"응? 난 괜찮아.\"" id c05_w_0631
    
    "[pl_name][josa_eun_neun] 왜 가헬의 표정이 심각한지 이해하지 못했다." id c05_w_0632
    
    show wolf out_u sad2_am
    with dissolve

    w "\"... 잊어버렸다면 상관없다.\"" id c05_w_0633
    
    show wolf out_d sad3_am
    with dissolve

    "[pl_name][josa_eun_neun] 가헬의 반응이 신경 쓰였다." id c05_w_0634
    "아쉬움과 안도감이 뒤섞인 복잡한 표정 때문에 [pl_name]도 생각이 많아졌다." id c05_w_0635
    
    c laugh "\"어디 크게 다친 적 없는 거 같으니, 잘 지낸 거겠지?\"" id c05_w_0636
    
    show wolf base
    with dissolve

    "[pl_name][josa_eun_neun] 아무렇지 않게 말했지만, 속으로는 다른 생각을 했다." id c05_w_0637
    
    c base "(가헬은 뭔가 알고 있어. 지금 당장은 숨기고 싶어 하지만...)" id c05_w_0638
    
    show wolf out_u talk
    with dissolve

    w "\"훈련하느라 피곤했을 텐데, 괜한 소리를 했군.\"" id c05_w_0639
    
    show wolf out_d base
    with dissolve

    c talk "\"아니야. 별로 안 피곤해.\"" id c05_w_0640
    c ddam2 "\"아... 설마 가게까지 뛰어갈 생각은 아니지?\"" id c05_w_0641
    
    "[pl_name][josa_eun_neun] 더 이상 훈련을 하고 싶지 않았다." id c05_w_0642
    "하지만 가헬의 대답은 예상하던 것과 전혀 달랐다." id c05_w_0643
    
    show wolf out_u shy5
    with dissolve

    w "\"피곤하지 않으면... 오늘 밤은 기대해도 되나?\"" id c05_w_0644
    
    show wolf out_d shy2
    with dissolve
    
    with vpunch
    c ddam "\"!!...\"" id c05_w_0645
    
    "[pl_name][josa_eun_neun] 훈련하느라 완전히 잊고 있었던 게 생각났다." id c05_w_0646
    "오늘을 위해 특제 오일까지 준비했지만, 그게 과연 실전에서 효과가 있을지는 모를 일이다." id c05_w_0647
    
    c ddam2 "\"그래... 오늘 밤에는 해야지.\"" id c05_w_0648
    
    show wolf happy
    with dissolve
    
    "[pl_name][josa_eun_neun] 사뭇 비장하게 대답했다." id c05_w_0649
    "그렇게 가헬과 [pl_name][josa_eun_neun] 미묘한 긴장감을 유지한 채 가게로 돌아갔다." id c05_w_0650

    stop music fadeout 2.5

label c5w_cg4_part1:
    # 가헬의 방 밤 배경
    scene bg gahel_room_night with Fade(0.8, 0.8, 0.8)
        
    "{i}~그날 밤~{/i}" id c05_w_0651

    show wolf happy
    with dissolve
    
    play sound "audio/effect/sigh.mp3" volume 0.23

    c inn_d sigh "\"휴...\"" id c05_w_0652
    
    "[pl_name][josa_eun_neun] 깊은숨을 내쉬며 긴장을 풀었다." id c05_w_0653
    "몸의 준비는 마쳤으나 마음의 준비는 여전히 힘들었다. 밤이 될 때까지 정말 오만가지 생각을 했다." id c05_w_0654
    
    c consider "(괜찮겠지?...)" id c05_w_0655
    
    "[pl_name]도 경험이 없는 건 아니지만, 많다고 할 수도 없었다." id c05_w_0656
    "가헬의 크기를 감당할 수 있는지 걱정이 드는 건 당연한 일이었다." id c05_w_0657
    
    show wolf am_u shy5
    with dissolve

    w "\"[pl_name]?\"" id c05_w_0658
    
    show wolf am_d happy
    with dissolve

    c talk "\"아, 어. 난 준비됐어.\"" id c05_w_0659
    
    "[pl_name][josa_eun_neun] 짐짓 아무렇지도 않은 척 대답했다. 가헬도 꽤 긴장했는지 얼굴이 붉었다." id c05_w_0660
    
    w "\"......\"" id c05_w_0661
    
    "가헬은 말없이 [pl_name]에게 조금 다가갔다." id c05_w_0662
    "[pl_name]의 예상보다 더 많이 긴장한 것 같다." id c05_w_0663
    
    show wolf shy2
    with dissolve

    w "(처음도 아닌데 왜 이렇게 떨리지?)" id c05_w_0664
    
    "가헬도 다 큰 수인이니만큼 어느 정도 경험이 있긴 했다." id c05_w_0665
    "만약 [pl_name][josa_i_ga] 살아있다는 걸 진작에 알았더라면, 몇몇 경험은 굳이 하지 않았을 것이다." id c05_w_0666
    "가헬은 자신의 첫 경험이 [pl_name][josa_i_ga] 아니라는 게 아쉬워졌다." id c05_w_0667
    
    show wolf shy
    with dissolve

    w "(이제 와서 후회해도 소용없는 일이지만...)" id c05_w_0668
    
    show wolf happy
    with dissolve

    "가헬은 차라리 [pl_name]에게 능숙한 모습을 보여주리라 다짐했다." id c05_w_0669
    
    c "\"많이 긴장한 것 같네.\"" id c05_w_0670
    
    show wolf am_u shy5
    with dissolve

    w "\"조, 조금?...\"" id c05_w_0671
    
    show wolf am_d happy
    with dissolve

    "[pl_name][josa_eun_neun] 가헬의 벨트 버클을 풀었다. 가헬은 저번처럼 무력하게 벗겨질 뻔했다." id c05_w_0672
    
    show wolf am_u shy5
    with dissolve

    w "\"굳이 안 벗겨줘도 된다.\"" id c05_w_0673
    
    show wolf happy
    with dissolve

    "가헬이 [pl_name]의 팔을 붙잡았지만, [pl_name][josa_i_ga] 조금 빨랐다." id c05_w_0674
    
    c "\"벗겨주는 것도 나름 재밌는데?\"" id c05_w_0675
    
    "[pl_name][josa_eun_neun] 거의 다 벗겨진 가헬의 바지를 내리고 미소 지었다." id c05_w_0676

    show wolf bulge_d shy3
    with dissolve

    $ unlock_character_image("wolf", "wolf b_no bulge_d")
    $ display_text = _("이미지 : 가헬(속옷발기)")
    show screen affection_indicator

    "가헬은 결국 [pl_name]의 손에 바지가 벗겨지고 말았다." id c05_w_0677

    "흥분을 감추지 못한 가헬의 아랫도리가 불룩 튀어나와 있었다." id c05_w_0678
    
    
    if underwear == 1 :
        
        c "\"응?\"" id c05_w_0679
        
        "가헬의 바지 주머니에서 뭔가 만져지는 게 있었다." id c05_w_0680
        "가헬이 말릴 새도 없이 그것을 꺼내본 [pl_name][josa_eun_neun] 조금 당황했다." id c05_w_0681
        
        # 속옷 이미지
        show underwear :
            xcenter 0.5
            ycenter 0.5
        with dissolve

        play sound "effect/ping.mp3" volume 0.75
        show exclamation at exclamation_move (1050, 40)
        show wolf shy5 at surprise_move
        

        w "\"그, 그건!...\"" id c05_w_0682

        hide exclamation
        with dissolve
        
        "가헬은 [pl_name]의 속옷을 챙겼다는 사실을 잊고 있었다." id c05_w_0683
        "아직 \'사용\'하지 않아서 뒤처리할 생각도 하지 못한 탓이었다." id c05_w_0684
        
        "[pl_name][josa_eun_neun] 왜 자신의 속옷이 가헬의 주머니에 들어있는지 잠시 고민했다." id c05_w_0685
        
        hide underwear
        with dissolve

        c "\"가헬?\"" id c05_w_0686

        show wolf bulge_u shy2 at surprise_move
        
        w "\"으윽...\"" id c05_w_0687
        
        "가헬은 변명의 여지가 없어서 새빨개진 얼굴로 침묵했다." id c05_w_0688

        show wolf shy
        with dissolve
        
        c "\"이런 게 필요하면... 말하지 그랬어.\"" id c05_w_0689
      
        "가헬은 퍼뜩 놀라며 고개를 저었다." id c05_w_0690

        show wolf bulge_d shy5
        with dissolve
        
        show wolf :
            ease 0.15 xoffset 10
            ease 0.10 xoffset 0
            
        w "\"아, 아니다. 이제 필요 없다.\"" id c05_w_0691
        
        c consider "(\'이제\' 라고? 흐음...)" id c05_w_0692
        
        "가헬은 뭐라고 설명해야 할지 고민했다." id c05_w_0693

        show wolf bulge_u shy3
        with dissolve
        
        w "\"내가, 음, 후각이 좀 예민해서...\"" id c05_w_0694
        w "\"그러니까, \'그런 거\'에 쉽게 흥분하는 편이라...\"" id c05_w_0695

        show wolf bulge_d shy2
        with dissolve
        
        "가헬은 말할수록 더 부끄러워졌다." id c05_w_0696
        "사실 이런 페티시 자체는 부끄러워할 만한 부분이 아니었다." id c05_w_0697
        "수인 사회에서는 외모나 근육만큼이나 체취도 중요하게 생각하는 수인이 많다." id c05_w_0698
        "[pl_name][josa_eun_neun] 가헬이 속옷으로 뭘 하려고 했는지 알 것 같았다." id c05_w_0699
        
        #가헬 이해도+1
        $ wolf_understanding += 1 
        $ display_text = _("가헬 이해도 변화")
        show screen affection_indicator

        c talk "\"일단 지금은 급한 것부터 하자.\"" id c05_w_0700

        show wolf bulge_u shy4
        with dissolve
        
        w "\"그래...\"" id c05_w_0701

        show wolf shy
        with dissolve
        
    "가헬은 흥분과 부끄러움이 뒤섞인 얼굴로 말했다." id c05_w_0702

    show wolf bulge_d shy5
    with dissolve
    
    w "\"... 이 정도는 내가 벗겠다.\"" id c05_w_0703
    
    show wolf nake_d shy2
    with dissolve

    "가헬이 속옷 끈을 풀자 길쭉한 기둥이 튀어나왔다." id c05_w_0704
    "[pl_name][josa_eun_neun] 저절로 침을 꿀꺽 삼켰다." id c05_w_0705
    
    c "(정말... 엄청나게 크네.)" id c05_w_0706
    
    "가까이서 보니 더 커 보이는 느낌이었다." id c05_w_0707

    show wolf :
        ease 0.25 xoffset 50
        ease 0.15 xoffset 30

    "[pl_name][josa_eun_neun] 가헬을 살짝 뒤로 밀면서 말했다." id c05_w_0708

    c "\"침대에 누워볼래?\"" id c05_w_0709

label c5w_cg4:

    scene wolf_s4_01 with Fade(0.8, 0.8, 0.8)
    play sound "effect/heart_beat.mp3" volume 0.75
    $ persistent.wolf_unlocked[3]= True
    
    # (씬1 시작)
    
    w nake_d base "이렇게?..." id c05_w_0710

    "가헬은 그대로 [pl_name]에게 떠밀려 침대 위에 누웠다." id c05_w_0711
    "은은한 달빛을 받아 가헬의 검은 털이 매혹적으로 빛난다." id c05_w_0712
    "[pl_name][josa_eun_neun] 가헬의 알몸을 보며 새삼 흉터가 많다는 걸 깨달았다." id c05_w_0713
    "본인은 어떻게 생각하는지 모르겠지만 [pl_name]에게는 흉터도 섹시하게 보였다." id c05_w_0714
    
    c inn_d base "(본격적으로 하기 전에 잠깐 전희를...)" id c05_w_0715
    
label c5w_cg4_touch :

    if c5w_cg4_touch_thigh + c5w_cg4_touch_abs + c5w_cg4_touch_chest == 1 :
        
        show wolf_cg4 w_2
        with dissolve
        pause 0.7
 
    elif c5w_cg4_touch_thigh + c5w_cg4_touch_abs + c5w_cg4_touch_chest == 2 :
        
        play channel1 "effect/breath.mp3" volume 0.4 fadeout 2.5
        show wolf_cg4 w_3
        with dissolve
        pause 0.7
    
    elif c5w_cg4_touch_thigh + c5w_cg4_touch_abs + c5w_cg4_touch_chest == 3 :
        
        show wolf_cg4 w_4
        with dissolve
        pause 0.7
 
    #[루프 선택지]
    menu:
        
        "자지를 만진다." :

            $ c5w_cg4_touch_penis = True 

            jump c5w_cg4_next
        
        "허벅지를 만진다." :
            
            jump c5w_cg4_touch_thigh

        "가슴을 만진다." :

            jump c5w_cg4_touch_chest
        
        "복근을 만진다." :

            jump c5w_cg4_touch_abs

        

########################
### 루프 선택지 #########
########################

label c5w_cg4_touch_thigh :
    
    if c5w_cg4_touch_thigh == False :
       
        $ c5w_cg4_touch_thigh = True 

        show wolf_s4_hand :
            zoom 0.95
            xoffset 940
            yoffset 700
        with dissolve
        
        "[pl_name][josa_eun_neun] 가헬의 허벅지 안쪽에 손을 얹었다." id c05_w_0716
        "짧고 부드러운 털과 팽팽한 근육이 느껴졌다." id c05_w_0717
        "[pl_name]의 손길에 가헬은 살짝 움찔했다." id c05_w_0718
        "아주 민감한 정도는 아니지만, 작은 자극도 크게 느껴질 상황이었다." id c05_w_0719
        "[pl_name][josa_eun_neun] 가헬이 뜨거운 숨을 내쉴 때까지 은근하게 어루만졌다." id c05_w_0720

        hide wolf_s4_hand
        with dissolve

        jump c5w_cg4_touch

    else :

        jump c5w_cg4_touch_mistake

label c5w_cg4_touch_chest :

    if c5w_cg4_touch_chest == False :

        $ c5w_cg4_touch_chest = True 

        show wolf_s4_hand :
            zoom 0.75
            xoffset 1080
            yoffset 300
        with dissolve

        "[pl_name][josa_eun_neun] 큰 흉터가 남은 가헬의 가슴에 손을 얹었다." id c05_w_0721
        "탱글탱글한 대흉근이 손 안에 꽉 차는 느낌이었다." id c05_w_0722
        "[pl_name][josa_i_ga] 장난스럽게 주무르자, 가헬도 작게 웃으며 근육에 힘을 줬다." id c05_w_0723
        "힘이 들어간 근육은 돌처럼 딱딱해졌다." id c05_w_0724
        "[pl_name][josa_eun_neun] 새로운 감촉을 즐기다가, 돌기를 붙잡았다." id c05_w_0725
        
        w shy "\"흣!...\"" id c05_w_0726

        "[pl_name][josa_i_ga] 유두를 괴롭히자, 가헬은 이를 꽉 물었다." id c05_w_0727
        "좋은지 싫은지 알 수 없는 감각이 찌릿하게 느껴졌다." id c05_w_0728
        "가헬은 [pl_name][josa_i_ga] 주는 자극을 참으며 움찔거렸다." id c05_w_0729

        hide wolf_s4_hand
        with dissolve

        jump c5w_cg4_touch

    else :

        jump c5w_cg4_touch_mistake

label c5w_cg4_touch_abs :

    if c5w_cg4_touch_abs == False :

        $ c5w_cg4_touch_abs = True

        show wolf_s4_hand :
            zoom 0.8
            xoffset 930
            yoffset 420
        with dissolve

        "선명하게 갈라진 근육이 [pl_name][josa_eul_reul] 유혹하고 있었다." id c05_w_0730
        "[pl_name][josa_eun_neun] 가헬의 복근 위에 손을 얹었다." id c05_w_0731
        "손가락 사이로 느껴지는 감촉이 중독적이었다. [pl_name][josa_eun_neun] 옆구리에 길쭉하게 난 흉터를 살짝 만져보았다." id c05_w_0732

        c "(이 상처는 좀 위험했을 거 같은데.)" id c05_w_0733

        w "\"거기는 조금... 간지럽다.\"" id c05_w_0734

        "[pl_name][josa_eun_neun] 간지럼 타는 가헬이 궁금했지만, 지금의 분위기를 망치고 싶지는 않았다." id c05_w_0735

        hide wolf_s4_hand
        with dissolve

        jump c5w_cg4_touch
    
    else :

        jump c5w_cg4_touch_mistake

label c5w_cg4_touch_mistake :

    "[pl_name][josa_i_ga] 손을 뻗는 순간, 가헬이 [pl_name]의 팔을 덥석 붙잡았다." id c05_w_0736

    w shy5 "\"더 참기 힘들다...\"" id c05_w_0737

    "가헬은 [pl_name]의 손을 아래로 이끌었다." id c05_w_0738
    "[pl_name][josa_eun_neun] 뜨거운 열기를 뿜어내는 자지로 시선을 돌렸다." id c05_w_0739

    jump c5w_cg4_next

    # 같은거 2회 누르면 함정으로 강제진행. 자지 바로 만지면 그냥 루프종료. 한번씩 다 보고 자지 눌러야 조건 제대로 충족.
    
label c5w_cg4_next : 

    show wolf_s4_hand :
            zoom 0.95
            xoffset 600
            yoffset 650
    with dissolve


    "[pl_name][josa_eun_neun] 흥분으로 고개를 끄덕이고 있는 가헬의 남근을 잡았다." id c05_w_0740

    hide wolf_s4_hand
    with dissolve

    play channel1 "audio/effect/heavy_breath.mp3" volume 0.7

    if c5w_cg4_touch_penis == True and c5w_cg4_touch_chest == True and c5w_cg4_touch_abs ==True and  c5w_cg4_touch_thigh == True :

        #프리컴 홍수 이미지
        show wolf_cg4 w_5
        with dissolve
        pause 0.7

        "가헬의 자지는 엄청난 양의 프리컴을 뿜어내고 있었다." id c05_w_0741
        "흘러내린 물줄기가 바닥에 뚝뚝 떨어졌지만, 그것보다 더 많은 양이 샘솟았다." id c05_w_0742

        $ c5w_touch_complete = True

    else :

        show wolf_cg4 w_4
        with dissolve

        "이슬처럼 맺힌 프리컴이 흘러내리려고 했다." id c05_w_0743

    play sound "effect/sticky3.mp3" volume 0.7

    show wolf_s4_tongue :
        xoffset 450
        yoffset 570
    with dissolve
    pause 1
    hide wolf_s4_tongue
    with dissolve
    
    "[pl_name][josa_eun_neun] 가헬과 눈을 마주치며 귀두부터 살짝 혀로 핥았다." id c05_w_0744
    
    "짙은 수컷의 맛과 냄새가 가득 느껴졌다." id c05_w_0745

    w horny "\"하아...\"" id c05_w_0746

    
    "가헬의 자지는 굵기도 무시할 수 없었다. 본격적으로 하기 전에 우선 탐색전을 했다." id c05_w_0747

    stop channel1 fadeout 3
    play channel2 "effect/sticky2.mp3" volume 0.7

    show wolf_s4_tongue :
        xoffset 650
        yoffset 600
    with dissolve

    pause 1

    hide wolf_s4_tongue
    with dissolve
    
    "[pl_name][josa_eun_neun] 귀두를 전체적으로 핥고 나서, 기둥 표면을 천천히 자극했다." id c05_w_0748
    
    "굵은 혈관과 닿은 혀를 통해 맥박이 느껴졌다. [pl_name][josa_eun_neun] 꿀꺽 침을 삼키고 입을 벌렸다." id c05_w_0749

    play channel2 "effect/sticky.mp3" volume 0.65
    
    show wolf_cg4 w_6
    with dissolve

    show wolf_cg4 :
        ease 1.5 yoffset -90
    
    c ddam2 "(윽, 턱 빠지겠는데...)" id c05_w_0750
    
    "[pl_name][josa_eun_neun] 간신히 입안에 귀두를 집어넣을 수 있었다. 고개를 내려 조금 더 삼키려고 했다." id c05_w_0751

    play sound "effect/sticky2.mp3" volume 0.7
    
    show wolf_cg4 w_7
    with dissolve
    
    with hpunch

    c sigh "\"읍!...\"" id c05_w_0752
    
    "[pl_name][josa_eun_neun] 절반도 채 삼키지 못하고 멈췄다. 기둥은 생각보다도 더 길쭉했다." id c05_w_0753
    
    "[pl_name][josa_eun_neun] 심호흡으로 마음의 준비를 하고 다시 도전했다." id c05_w_0754
    
    "최대한 밀어 넣어봤지만, 절반도 채 삼키지 못했다." id c05_w_0755
    
    w "\"무리하지 않아도 된다.\"" id c05_w_0756

    play sound "effect/sticky3.mp3" volume 0.7

    show wolf_cg4 w_8
    with dissolve
    pause 0.5
       
    "[pl_name][josa_eun_neun] 조심스럽게 고개를 뒤로 뺐다." id c05_w_0757

    play channel1 "audio/effect/sigh.mp3" volume 0.23

    scene wolf_cg4 w_2 w_3 w_4 w_5 w_5_add :
        yoffset -430 xoffset -4
    with dissolve
    
    c nake_d talk "\".... 하아. 쉽지 않네.\"" id c05_w_0758
    
    "[pl_name][josa_eun_neun] 기대 반 걱정 반으로 말했다." id c05_w_0759
    "길이는 감을 잡았으니, 가헬의 약점을 공략할 차례였다." id c05_w_0760

    play channel2 "effect/sticky2.mp3" volume 0.7
    
    show wolf_cg4 w_6 w_8
    with dissolve
    
    "[pl_name][josa_eun_neun] 다시 가헬의 자지를 입에 물었다." id c05_w_0761

    play sound "effect/sticky3.mp3" volume 0.7

    show wolf_s4_07
    with dissolve

    hide wolf_s4_07
    with dissolve

    show wolf_s4_07
    with dissolve

    hide wolf_s4_07
    with dissolve

    "천천히 혓바닥으로 표면을 자극하며 위아래로 움직이기 시작했다." id c05_w_0762

    with vpunch
    
    w nake_d shy "\"읏...\"" id c05_w_0763
    
    "가헬은 [pl_name][josa_i_ga] 주는 자극에 잘게 떨었다." id c05_w_0764
    "침대 시트를 꽉 잡으며 더 깊이 넣고 싶은 마음을 참았다." id c05_w_0765
    "[pl_name][josa_i_ga] 움직이는 박자에 따라서 허리를 들썩이는 정도가 한계였다." id c05_w_0766
    
    c nake_d sigh "(이렇게 큰걸, 가능할까?...)" id c05_w_0767
    
    "[pl_name][josa_eun_neun] 입안을 묵직하게 채우는 감각에 흥분하면서도 조금 두려워졌다." id c05_w_0768
    "마음을 굳게 먹어도 떨리는 건 어쩔 수 없었다." id c05_w_0769

    play sound "effect/sticky4.mp3" volume 0.6

    hide wolf_cg4
    show wolf_cg4 w_2 w_3 w_4 w_5 w_5_add :
        yoffset -430 xoffset -4
    with dissolve
    
    c talk "\"후아...\"" id c05_w_0770
    
    "[pl_name][josa_i_ga] 입을 떼자 드러난 가헬의 자지는 아까보다 더 흉포해 보였다." id c05_w_0771
    "굵은 핏줄이 도드라진 기둥은 맥박이 눈에 보일 정도였다." id c05_w_0772
    "침에 젖은 붉은 귀두는 과장 좀 보태서 주먹만 한 크기였다." id c05_w_0773

    show oil2 :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    # 특제 오일 이미지

    "[pl_name][josa_eun_neun] 미리 준비한 특제 오일을 꺼냈다." id c05_w_0774

    hide oil2
    with dissolve

    "기존 허브 오일보다 잘 마르지 않고 끈적거리게 만들어서 지금 같은 상황에 잘 어울릴 것이다." id c05_w_0775

    play channel2 "effect/sticky2.mp3" volume 0.7

    hide wolf_cg4
    show wolf_cg4 w_2 w_3 w_4 w_5 w_5_add w_9 :
        yoffset -430 xoffset -4
    with dissolve

    "가헬의 남근 위에 듬뿍 뿌리자 번들거리는 게 더욱 음란하게 보인다." id c05_w_0776

    show wolf_cg4 w_10
    with dissolve

    show wolf_cg4 :
        ease 2 yoffset -300
    
    "[pl_name][josa_eun_neun] 속옷을 벗어던지고 가헬의 위에 올라탔다." id c05_w_0777
    
    c horny2 "\"나는 준비됐어.\"" id c05_w_0778

    with vpunch
    
    w horny2 "\"!!...\"" id c05_w_0779
    
    "자지에 닿는 맨살의 감촉에 가헬은 정신이 아찔했다." id c05_w_0780
    "[pl_name][josa_eun_neun] 한 손으로 가헬의 기둥을 붙잡고 자세를 잡았다." id c05_w_0781
    "입구에 닿는 귀두가 뜨겁게 느껴졌다." id c05_w_0782

    show wolf_cg4 :
        ease 1 yoffset -370

    pause 1

    play channel1 "effect/sticky2.mp3" volume 0.7

    show wolf_cg4 w_11
    with dissolve

    show wolf_cg4 :
        ease 1 yoffset -310

 
    "더 이상 도망갈 수 없다. [pl_name][josa_eun_neun] 천천히 허리를 내렸다." id c05_w_0783

    with vpunch
    
    c horny "\"으윽!\"" id c05_w_0784
    
    w "\"크흡!\"" id c05_w_0785
    
    "충분한 준비 덕분에 삽입 자체는 쉬웠다." id c05_w_0786
    
    "그러나 [pl_name]도 가헬도 벼락을 맞은 듯 벌벌 떨었다." id c05_w_0787
    "[pl_name][josa_eun_neun] 거대한 물건을 받아들이느라 뒤가 활짝 벌려지는 감각에 놀랐다." id c05_w_0788
    "굵기는 어느 정도 각오를 했으나, 길이는 역시 적응할 수 없었다." id c05_w_0789
    
    c ddam2 "\"어, 얼마나 들어간 거지?\"" id c05_w_0790
    
    w horny "\"40\% 정도...\"" id c05_w_0791
    
    c "(뭐? 고작 그 정도 넣었는데, 이렇게 깊게 들어온다고?)" id c05_w_0792
    
    "[pl_name][josa_eun_neun] 정신이 아득해졌다." id c05_w_0793
    
    w "\"아까도 말했지만, 무리하지 말고 천천히...\"" id c05_w_0794
    
    w "\"어차피 전부 다 안 들어간다.\"" id c05_w_0795
    
    c "\"그건 좀... 무섭네.\"" id c05_w_0796
    
    "[pl_name][josa_eun_neun] 식은땀을 흘리며 대답했다." id c05_w_0797

    play sound "effect/breath.mp3" volume 0.4

    show wolf_cg4 :
        ease 1 yoffset -250
    
    "심호흡하면서 긴장을 풀자 조금씩 더 깊이 들어오는 \'침입자\'를 느낄 수 있었다." id c05_w_0798
    
    c horny "\"흐으으으으...\"" id c05_w_0799
    
    c "(여기까지 들어올 줄은 몰랐는데...)" id c05_w_0800
    
    "[pl_name][josa_eun_neun] 아랫배가 묵직하게 차오르는 느낌이 들었다." id c05_w_0801
    "가헬도 쾌감에 들뜬 표정을 숨길 수 없었다." id c05_w_0802
    "당장이라도 격렬하게 움직이고 싶지만, 간신히 참고 있었다." id c05_w_0803
    
    c horny4 "\"읏! 이 이상은 진짜 무리야...\"" id c05_w_0804
    
    c horny3 "\"잠시만, 기다려 봐. 후우....\"" id c05_w_0805

    play channel2 "effect/sticky.mp3" volume 0.65

    show wolf_cg4 :
        ease 1 yoffset -310
    
    "어떻게든 가헬의 크기에 익숙해진 [pl_name][josa_eun_neun] 가헬의 어깨를 잡고 천천히 움직였다." id c05_w_0806
    "밑에서부터 꿰뚫리는 감각이 아찔했다." id c05_w_0807
    "아프기보다는 오싹오싹한 무서운 느낌이었다." id c05_w_0808
    "[pl_name][josa_eun_neun] 공포와 흥분이 뒤섞여 심장이 거세게 뛰는 걸 느낄 수 있었다." id c05_w_0809

    play sound "effect/sticky3.mp3" volume 0.7
    play channel1 "audio/effect/heavy_breath.mp3" volume 0.7

    show wolf_cg4 :
        ease 1 yoffset -250
        ease 1 yoffset -330
        ease 0.5 yoffset -310

    "둘 사이엔 질척거리는 소리와 뜨거운 호흡만 오갔다." id c05_w_0810
    
    w "\"하아, [pl_name]... 내가 움직여도 될까?\"" id c05_w_0811
    
    "가헬의 푸른 눈은 이미 욕망으로 활활 불타고 있었다." id c05_w_0812

    show wolf_cg4 w_11_add
    with dissolve

    "말로는 허락을 구하고 있었지만, 이미 가헬의 손은 [pl_name]의 허리를 붙잡았다." id c05_w_0813
    "[pl_name][josa_eun_neun] 차마 이제 와서 거절할 수 없었다. [pl_name][josa_eun_neun] 고개를 위아래로 끄덕였다." id c05_w_0814
    
    stop channel1 fadeout 3

    w "\"미안하다. 더 이상 못 참겠군...\"" id c05_w_0815
    
    "가헬의 손아귀가 [pl_name][josa_eul_reul] 강하게 움켜쥔다. [pl_name][josa_eun_neun] 손자국이 남는 거 아닐지 걱정했다." id c05_w_0816
    "하지만 그런 걱정 따위 가볍게 날려버리는 커다란 충격이 [pl_name][josa_eul_reul] 강타했다." id c05_w_0817

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    
    show wolf_cg4 w_12
    with vpunch

    c "\"하윽!! 자, 잠깐!!\"" id c05_w_0818
 
    "가헬이 허리를 올려 치자 자지가 한층 더 깊은 곳까지 쑥 들어오는 게 느껴졌다." id c05_w_0819

    show wolf_cg4 w_11_add
    with dissolve

    "들어오는 감각만큼이나 빠져나가는 감각도 아찔했다." id c05_w_0820
    "귀두가 구멍 안쪽을 전부 훑고 지나가는 감각에 [pl_name]의 다리가 덜덜 떨렸다." id c05_w_0821
    
    c "(대체 어디까지 들어오는 거야!?)" id c05_w_0822

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    
    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.3)

    c "\"가헬, 윽! 천천히...\"" id c05_w_0823

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.3)

    play channel1 "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.25)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch
    
    "[pl_name][josa_eun_neun] 배 속이 가득 차는 느낌에 경악했다." id c05_w_0824

    show wolf_cg4 w_11_add
    with Dissolve (0.35)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    
    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.5)

    "이걸 버텨내는 자신의 몸이 놀라울 지경이었다." id c05_w_0825

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.3)

    play channel1 "audio/effect/CI-I - (20).mp3" volume 1
    
    show wolf_cg4 w_12
    with vpunch
    
    "가헬은 이미 이성을 잃어서 [pl_name][josa_i_ga] 뭐라고 말하는지 듣지 못했다." id c05_w_0826

    show wolf_cg4 w_11_add
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.22)

    play channel2 "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_11_add
    with Dissolve (0.22)

    play channel1 "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    "[pl_name][josa_i_ga] 움직이던 것보다 훨씬 빠른 박자로 가헬은 허리를 들썩거렸다." id c05_w_0827

    show wolf_cg4 w_11_add
    with Dissolve (0.22)

    play channel2 "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    "살이 부딪히며 철썩거리는 소리를 낸다." id c05_w_0828

    show wolf_cg4 w_11_add
    with Dissolve (0.22)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch
    
    w "\"[pl_name], [pl_name]...\"" id c05_w_0829

    show wolf_cg4 w_13
    with Dissolve (0.25)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_13
    with Dissolve (0.2)

    play channel1 "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_13
    with Dissolve (0.16)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_13
    with Dissolve (0.15)

    play channel1 "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_13
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    show wolf_cg4 w_13
    with Dissolve (0.15)

    play channel1 "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch


    "점점 더 빨라지는 가헬의 움직임에 [pl_name][josa_eun_neun] 간신히 억누르던 신음을 터트렸다." id c05_w_0830

    show wolf_cg4 w_13
    with Dissolve (0.2)
    
    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch
    
    c "\"읏, 아흑!\"" id c05_w_0831
    
    show wolf_cg4 w_13
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch

    c "\"가헬, 잠깐. 으응!\"" id c05_w_0832

    show wolf_cg4 w_13
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch
    
    c "\"하아, 하으으으읏!!\"" id c05_w_0833
    
    "[pl_name][josa_eun_neun] 순간적으로 뭔가 막혀있던 곳이 뚫리는 느낌이 들었다." id c05_w_0834

    show wolf_cg4 w_13
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg4 w_12
    with vpunch
    
    "가헬의 자지가 뿌리 끝까지 깊숙이 박혔다." id c05_w_0835
    "[pl_name][josa_i_ga] 몸을 부르르 떨자, 땀방울이 가헬의 배에 떨어졌다." id c05_w_0836
    "곧이어 뜨거운 것이 몸속에서 느껴졌다." id c05_w_0837
    
    c "(이 느낌은...!)" id c05_w_0838

    show wolf_cg4 w_14
    with dissolve

    play channel1 "audio/effect/heavy_breath.mp3" volume 0.7
    
    "가헬이 아주 작게 강아지처럼 낑낑대는 소리를 냈다." id c05_w_0839

    play sound "audio/effect/sqz1.mp3" volume 0.7
    pause 0.5

    show wolf_cg4 w_15
    with vpunch    

    "[pl_name][josa_eun_neun] 깊은 곳에서 왈칵왈칵 쏟아지는 정액이 느껴졌다." id c05_w_0840

    "몸속으로 끓는 물을 들이붓는 기분이었다." id c05_w_0841

    play sound "audio/effect/sqz3.mp3" volume 0.7
    pause 0.4

    show wolf_cg4 w_16
    with vpunch

    w horny2 "\"그르르르르...\"" id c05_w_0842

    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.5

    show wolf_cg4 w_17
    with vpunch
    
    c horny4 "(어, 언제 끝나는 거야?!)" id c05_w_0843

    pause 0.5

    play channel2 "effect/sticky3.mp3" volume 0.7
    
    hide wolf_cg4
    show wolf_cg4 w_4 w_5_add w_9 w_10 w_11 w_11_add w_18
    with dissolve    
    
    "데일 것처럼 뜨거운 느낌이 끝나고, 뭉근하게 따뜻한 느낌이 들었다." id c05_w_0844
    "격렬한 분출은 끝난 듯했지만, 내장을 뒤덮은 정액이 흘러내리는 기분은 정말 이상했다." id c05_w_0845
    "[pl_name] 자신의 몸도 양초처럼 줄줄 녹아서 흐를 것만 같았다." id c05_w_0846
    
    play sound "audio/effect/sigh.mp3" volume 0.23

    c shy2 "\"후... 엄청, 격렬했어.\"" id c05_w_0847

    play channel1 "effect/breath.mp3" volume 0.4 fadeout 2.5
    
    "겨우 정신을 차린 [pl_name][josa_eun_neun] 잠시 숨을 골랐다. 폭풍이 휩쓸고 지나간 뒤처럼 정신이 멍했다." id c05_w_0848
    
    w shy3 "\"미, 미안... 너무 빨리 싸버렸다.\"" id c05_w_0849
    
    "가헬은 부끄러워하며 조용히 사과했다." id c05_w_0850
    
    # 적절한 젤 + 씬에서 터치 조건 만족하면 씬2로 점프)
    
    if oil_complete == True and c5w_touch_complete == True:
        jump c5w_cg5

    else :
        jump c5w_cg4_end

label c5w_cg4_end :
    
    c horny "\"괜찮아. 나는 약간, 피곤한걸...\"" id c05_w_0851
    
    "[pl_name][josa_eun_neun] 뻐근한 팔다리를 움직여서 겨우 일어났다." id c05_w_0852

    play channel2 "effect/sticky.mp3" volume 0.65

    hide wolf_cg4
    show wolf_cg4 w_4 w_5_add w_9 w_19
    with dissolve 

    "뒤에 꽂혀있던 거대한 기둥이 빠져나가자, 뻥 뚫린 구멍에서 정액이 후두둑 떨어졌다." id c05_w_0853
    
    show wolf_cg4 :
        ease 1.5 yoffset -80

    "가헬의 정액 냄새가 진하게 퍼졌다." id c05_w_0854
    
    c ddam "\"윽, 이렇게 힘든 거였구나...\"" id c05_w_0855
    
    "뒤늦게 느껴지는 구멍의 통증에 [pl_name][josa_eun_neun] 침대에 기대어 헐떡였다." id c05_w_0856
    
    "충분히 준비했다고 생각했는데 가헬의 크기를 감당하기엔 모자란 듯했다." id c05_w_0857
    
    w "\"괜찮나?\"" id c05_w_0858
    
    # 여기부터 스탠딩

    "가헬은 [pl_name]의 몸을 침대 위로 끌어 올렸다." id c05_w_0859
    
    c "\"응... 조금만 쉬고 씻어야겠어.\"" id c05_w_0860
    
    "[pl_name][josa_eun_neun] 편안하게 누워서 눈을 감자마자 그대로 잠들었다." id c05_w_0861
    "가헬은 차마 [pl_name][josa_eul_reul] 깨우지 못했다. [pl_name]의 작은 숨소리에 집중할 뿐이었다." id c05_w_0862

    stop music fadeout 2.5

    $ renpy.end_replay()

    jump c5w_end

label c5w_cg5:
    
    c happy "\"괜찮아. 그렇게 빠르지 않았는데-\"" id c05_w_0863
    
    c horny "\"으악!\"" id c05_w_0864

    play sound "audio/effect/puton.mp3" volume 0.5

    show wolf_cg4 :
        ease 0.25 yoffset -40
        ease 0.5 yoffset 80
    
    # 카메라 위로 확 올리기?
    pause 1

    "가헬은 [pl_name][josa_eul_reul] 끌어안고 일어섰다." id c05_w_0865

    
    transform s5_zoomback:
        
        zoom 0.93 xoffset -10 yoffset -60

    transform s5_zoomin:
        
        zoom 0.965 xoffset -5 yoffset -30


label c5w_cg5_start:

    scene wolf_s5_back 
    show wolf_s5_body
    show wolf_s5_cara
    show wolf_s5_arm 

    with Fade(0.8, 0.8, 0.8)

    $ persistent.wolf_unlocked[4]= True

    # 여기부터 cg5

    "그대로 뒤로 돌아 침대 위에 [pl_name][josa_eul_reul] 눕힌 가헬은 씨익 웃었다." id c05_w_0866
    
    "다리 사이에 자리 잡은 가헬이 조금 무섭게 보였다." id c05_w_0867

    play channel1 "effect/heart_beat.mp3" volume 0.75
    
    w nake_d shy5 "\"[pl_name], 계속할 수 있지?\"" id c05_w_0868
    
    "가헬의 자지는 전혀 작아지지 않은 채로 [pl_name]의 안에 박혀 있었다." id c05_w_0869
    
    "오히려 조금 더 커진 것인지, 가헬의 맥박이 뒤로 느껴질 정도였다." id c05_w_0870
    "[pl_name][josa_eun_neun] 잠깐 쉬자고 말할지 생각했지만, 가헬이 한 수 더 빨랐다." id c05_w_0871

    w "\"너는 아직 충분히 즐기지 못한 것 같은데...\"" id c05_w_0872

    c nake_d horny "\"그건... 아읏! 맞지만...\"" id c05_w_0873

    if wolf_see == 1 :
        
        "가헬이 자위할 때 한 번 싸고도 계속 이어서 했던 게 생각났다." id c05_w_0874
        "[pl_name][josa_eun_neun] 가헬의 한계가 어디까지인지 걱정되기 시작했다." id c05_w_0875

    
    hide wolf_s5_arm
    show wolf_cg5_wolfarm mouth eyehalf red breath
    with dissolve

    "가헬은 [pl_name][josa_eul_reul] 내려다보며 황홀한 표정을 지었다." id c05_w_0876

    w horny "\"계속 궁금했다. 너는 어디가 약한지, 무슨 자세를 좋아하는지, 어떤 표정으로 절정하는지...\"" id c05_w_0877
    
    "평소에는 부끄러워서 하지 못할 얘기를 거침없이 하는 가헬이 낯설었다." id c05_w_0878

    c shy2 "\"그, 그랬구나.\"" id c05_w_0879
    
    "[pl_name][josa_eun_neun] 너무 민망해서 아무 말이나 내뱉어버렸다." id c05_w_0880

    w horny "\"이제 하나씩 알아갈 수 있겠군.\"" id c05_w_0881

    play sound "audio/effect/SPS - (1).mp3" volume 0.9

    show wolf_s5_body at s5_zoomback
    show wolf_cg5_wolfarm at s5_zoomback
    with dissolve
    
    "가헬은 살살 허리를 뒤로 뺐다." id c05_w_0882
    
    "[pl_name][josa_eun_neun] 깊게 박힌 말뚝이 빠져나가는 느낌에 소름이 돋았다." id c05_w_0883
    
    "대체 얼마나 깊숙이 박혀있던 건지, 몸이 텅 비어버리는 기분이었다." id c05_w_0884

    play channel2 "effect/sticky4.mp3" volume 0.65

    show wolf_s5_body at s5_zoomin
    show wolf_cg5_wolfarm at s5_zoomin       
    show wolf_s5_belly
    with Dissolve (0.8)
    
    "가헬은 다시 느릿하게 자지를 넣으면서 내벽 이곳저곳을 자극했다." id c05_w_0885

    play channel1 "audio/effect/heavy_breath.mp3" volume 0.7
    show wolf_cg5_wolfarm sweat
    with dissolve 

    "속이 휘저어진 [pl_name][josa_eun_neun] 저절로 신음을 내뱉었다." id c05_w_0886

    with hpunch
    
    c horny "\"으앗!... 응!\"" id c05_w_0887

    transform s5_move :
        ease 0.5 xoffset 20 yoffset -15
        ease 0.5 xoffset -5 yoffset -30
        repeat 2

    transform s5_move2 :
        ease 0.5 xoffset 10 
        ease 0.5 xoffset 0
        repeat 2
        
    
    play channel2 "effect/sticky3.mp3" volume 0.65

    show wolf_s5_body at s5_move
    show wolf_cg5_wolfarm at s5_move
    show wolf_s5_cara at s5_move2
    show wolf_s5_belly at s5_move2
    
    "가헬은 [pl_name]의 안쪽을 마음껏 탐험했다." id c05_w_0888
    "[pl_name][josa_i_ga] 쾌감을 느끼는 지점을 찾기 위해 모든 부분을 자극했다." id c05_w_0889

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    with vpunch
    
    "살짝 튀어나온 부분을 가헬이 귀두로 문지르자, [pl_name][josa_eun_neun] 저릿한 느낌에 덜덜 떨었다." id c05_w_0890
    
    play sound "effect/breath.mp3" volume 0.4

    if wolf_dom >= 1 :
        
        "가헬은 위험한 미소를 지으며 [pl_name]의 발목 붙잡았다." id c05_w_0891

        w "\"[pl_name]...\"" id c05_w_0892

        
        show wolf_s5_body :
            yoffset 0
        show wolf_cg5_wolfarm :
            yoffset 0
        with dissolve

        show wolf_s5_body :
            yoffset 0
        show wolf_cg5_wolfarm :
            yoffset 0
        show wolf_s5_bite
        with Fade (0.6, 0.6, 0.6) 
        
        "가헬은 [pl_name]의 다리를 가볍게 깨물고는 낼름 핥으며 [pl_name][josa_eul_reul] 내려다보았다." id c05_w_0893

        show wolf_s5_body :
            yoffset -30
        show wolf_cg5_wolfarm :
            yoffset -30
        with dissolve

        "목덜미를 깨물고 싶은 욕구가 가득했지만, 간신히 참고 있었다." id c05_w_0894
        
        c horny3 "(정말 잡아먹히는 기분인데...)" id c05_w_0895
        
        "[pl_name][josa_eun_neun] 쾌락에 사로잡혀 똑바로 생각할 수 없었다." id c05_w_0896
        "가헬이라면 잡아먹혀도 괜찮을 것 같았다." id c05_w_0897
        
    elif wolf_sub >= 2 :
            
        "가헬은 강아지 같은 눈으로 [pl_name][josa_eul_reul] 바라보았다." id c05_w_0898
        
        w "\"여기가 좋은가? 아니면 조금 더 아래?\"" id c05_w_0899
        
        "[pl_name][josa_eun_neun] 멍한 정신으로 가헬이 무슨 말을 했는지 곱씹었다." id c05_w_0900
        "자신이 잘하고 있는지 확인받고 싶어 하는 것 같았다." id c05_w_0901
        
        c horny3 "\"다 좋으니까 빨리...\"" id c05_w_0902

        show wolf_s5_body :
            yoffset 0
        show wolf_cg5_wolfarm :
            yoffset 0
        with dissolve
        
        "[pl_name][josa_eun_neun] 다리로 가헬의 허리를 감아 끌어당겼다." id c05_w_0903

        show wolf_s5_body :
            yoffset -30
        show wolf_cg5_wolfarm :
            yoffset -30
        with dissolve

        "가헬은 [pl_name]의 행동에 살짝 당황했는지 붉어진 얼굴로 대답했다." id c05_w_0904
        
        w "\"아, 알았다.\""  

    transform s5_movedw :
        ease 1.5 yoffset -20
    
    transform s5_movedw2 :
        ease 1.5 yoffset -30
    
    transform s5_zoomin2 :
        zoom 1.03 yoffset 20
    

    show wolf_s5_body at s5_zoomin2
    show wolf_cg5_wolfarm at s5_zoomin2
    show wolf_s5_belly2
    show wolf_s5_penisdw : 
        zoom 1.03 yoffset -142 xoffset -38
    show wolf_s5_belly2_tran
    show wolf_s5_water_cara
    with Dissolve (0.8)

   
    show wolf_s5_back at s5_movedw
    show wolf_s5_body at s5_movedw
    show wolf_cg5_wolfarm at s5_movedw
    show wolf_s5_belly at s5_movedw2
    show wolf_s5_belly2 at s5_movedw2
    show wolf_s5_cara at s5_movedw2
    show wolf_s5_water_cara at s5_movedw2
    show wolf_s5_penisdw :
        ease 1.5 yoffset -175
    show wolf_s5_belly2_tran at s5_movedw2
    if wolf_dom >= 1 :
        show wolf_s5_bite at s5_movedw2

    pause 1.7

    show wolf_s5_belly2_tran :
        ease 1.2 alpha 0.45
    
    pause 1.4
    
    play sound "effect/breath.mp3" volume 0.4
    play channel1 "audio/effect/wet_slap.mp3" volume 0.6

    "가헬은 속도를 높여 [pl_name][josa_i_ga] 느끼는 지점을 집중적으로 눌렀다." id c05_w_0905
    "[pl_name][josa_eun_neun] 침대 시트가 찢어질 정도로 꽉 움켜쥐고 쾌락에 덜덜 떨었다." id c05_w_0906

    show wolf_s5_belly2_tran :
        ease 1 alpha 1
    
    pause 1.2

    "\'이성이 녹아내리는 기분\'이 뭔지 알 수 있었다."    

    stop channel1 fadeout 3

    transform s5_zoomback2 :
        zoom 0.97 yoffset -60
    
    transform s5_zoomin3 :
        zoom 1.05 yoffset 0
    
    transform s5_fit :
        yoffset -147 xoffset -4

    hide wolf_s5_penisdw
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_tran
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch


    c "\"하윽! 응, 흐아...\"" id c05_w_0907

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    c "\"가헬, 너무 좋아...\"" id c05_w_0908
    
    "가헬은 [pl_name]의 표정을 보고 새삼스럽게 심장이 두근거렸다." id c05_w_0909
    "자꾸만 [pl_name][josa_eul_reul] 독점하고 싶어지는 마음을 참을 수가 없었다." id c05_w_0910

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch
    
    w "\"그르르르...\"" id c05_w_0911
    
    "가헬은 자신도 모르게 으르렁거리는 소리를 내기 시작했다." id c05_w_0912
    "속에서부터 울리는 늑대의 울음소리는 [pl_name]의 등골을 오싹하게 만들었다." id c05_w_0913

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    "가헬은 [pl_name]의 허벅지를 잡고 조금 더 깊게 꽂아 넣기를 반복했다." id c05_w_0914


    show wolf_cg5_wolfarm seedleft4
    with vpunch
    play sound "effect/sticky4.mp3" volume 0.7

    "질퍽거리는 소리와 함께 휘저어진 정액은 하얀 거품이 되어 새어 나왔다." id c05_w_0915
    
    "방 안의 공기에서도 진득한 정액 냄새를 맡을 수 있었다." id c05_w_0916

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    c "\"흐억! 으, 거긴!\"" id c05_w_0917
    
    "점점 깊게 들어오는 가헬의 자지에 [pl_name][josa_eun_neun] 반사적으로 몸을 떨었다." id c05_w_0918
    "한 번 열린 곳은 아까보다 수월하게 가헬을 받아들였다." id c05_w_0919
    "[pl_name][josa_eun_neun] 땀에 젖은 가헬의 허벅지가 닿아오는 게 느껴졌다." id c05_w_0920
    "자신의 속에 자리 잡은 기둥의 핏줄 하나하나 세밀하게 느껴지는 기분이었다." id c05_w_0921
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch
    
    w "\"[pl_name], 여기 엄청 좁다.\"" id c05_w_0922
    
    "가헬은 귀두부터 뿌리까지 자지 전체를 터질 것처럼 조여오는 내벽에 정신이 아찔했다." id c05_w_0923
    "가헬이 움직이는 대로 [pl_name]의 복근이 살짝 솟아오르고 꺼지기를 반복한다." id c05_w_0924
    "[pl_name][josa_eun_neun] 자신의 배가 이렇게까지 튀어나올 수 있다는 사실에 깜짝 놀랐다." id c05_w_0925
    "사실상 가헬에게 몸이 꿰뚫린 것과 다름없었다." id c05_w_0926

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    c "\"으응!... 너무 깊어.\"" id c05_w_0927

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    c "\"흑! 조금만 살살... 하읏!\"" id c05_w_0928

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch
    
    w "\"이렇게 꽉 조이면서, 그런 말 해도...\"" id c05_w_0929
    
    "[pl_name]의 부탁이라면 뭐든 들어주던 친절한 가헬은 잠시 사라졌다." id c05_w_0930
    "오직 짐승의 본능에 충실한 늑대 한 마리가 [pl_name][josa_eul_reul] 탐하고 있었다." id c05_w_0931

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    "가헬은 아까보다 더 격렬하게 움직이며 [pl_name][josa_eul_reul] 밀어붙였다." id c05_w_0932
    "과한 자극에 [pl_name][josa_eun_neun] 머릿속이 하얗게 비어버리는 기분이었다." id c05_w_0933

    play channel1 "audio/effect/wet_slap.mp3" volume 0.8

    "허벅지와 허벅지가 맞부딪치며 철벅철벅 소리를 냈다." id c05_w_0934

    "[pl_name][josa_eun_neun] 자기 내장이 가헬의 모양에 맞춰 변하는 것 같은 이상한 기분이 들었다." id c05_w_0935

    stop channel1 fadeout 3

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line at s5_fit
    with vpunch

    "가헬이 찌를 때마다 심장을 때리는 것처럼 충격이 온몸에 전해졌다." id c05_w_0936
    "순간 [pl_name]의 등줄기를 타고 짜릿한 감각이 스쳐 지나갔다." id c05_w_0937

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line
    with Dissolve (0.2)

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch
    
    play sound "audio/effect/CI-I - (4).mp3" volume 1

    c "\"잠깐, 나, 나올 것 같! 윽!! 흐으으응!...\"" id c05_w_0938

    play sound "audio/effect/sqz4.mp3" volume 0.6

    hide wolf_s5_belly2_line
    hide wolf_s5_water_cara
    show wolf_s5_belly2_line_add at s5_fit
    show wolf_s5_seed2 at s5_fit
    with vpunch
    
    "[pl_name][josa_eun_neun] 제대로 말을 잇지 못하고 사정해 버렸다." id c05_w_0939

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_cg5_wolfarm seedleft3
    with hpunch     
    
    "강하게 튀어 오른 희뿌연 액이 가헬의 얼굴에 묻었다." id c05_w_0940

    hide wolf_s5_seed2
    show wolf_s5_seed_cara at s5_fit
    with dissolve
    
    w "\"!!...\"" id c05_w_0941
    
    "가헬은 입가에 묻은 정액을 핥았다. 기분 탓인지는 몰라도 \'맛있다\'고 생각했다." id c05_w_0942
    
    "절정에 움찔거리는 [pl_name]의 모습을 눈에 담았다." id c05_w_0943
    "모든 상황이 가헬의 머릿속을 흥분으로 가득 채웠다." id c05_w_0944

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "가헬은 아까보다도 더욱 속도를 높였다." id c05_w_0945
    "[pl_name]의 허벅지에 손톱이 박힐 정도로 꽉 잡고 본능대로 움직였다." id c05_w_0946

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    w "\"하아... 사랑해, [pl_name]...\"" id c05_w_0947

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "가헬이 깊은 곳을 찌를 때마다 [pl_name]의 머릿속은 쾌감으로 번쩍거렸다." id c05_w_0948
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "더 이상 나올 게 없을 때까지 꽉 쥐어짜인 기분이었다." id c05_w_0949
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "그러나 절정은 끝나지 않았다." id c05_w_0950
    
    c horny4 "\"더는, 흐억! 무리...\"" id c05_w_0951

    with hpunch
    
    "[pl_name][josa_eun_neun] 처음 경험하는 지나친 쾌감에 다리를 덜덜 떨었다. 나오는 것은 없지만 계속 사정하는 기분이 들었다." id c05_w_0952
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "가헬은 [pl_name][josa_i_ga] 헐떡대는 모습을 눈에 새겼다." id c05_w_0953
    "동시에 [pl_name]의 이런 모습을 남들이 몰랐으면 하는 마음이 생겼다." id c05_w_0954

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "몸도 마음도 불이 붙은 가헬은 땀을 뚝뚝 흘리면서 행위에 집중했다." id c05_w_0955

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    
    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    w horny2 "\"크윽! 조금만 더...\"" id c05_w_0956
    
    "가헬도 슬슬 한계가 왔는지 표정이 일그러졌다." id c05_w_0957

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    
    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "땀에 젖어 빛나는 근육은 어느 때보다도 팽팽하게 보였다. 고환이 올라붙어서 절정이 가까웠음을 알렸다." id c05_w_0958

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    
    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.18)

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (6).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    with Dissolve (0.1)

    play sound "audio/effect/CI-I - (4).mp3" volume 1

    show wolf_s5_body at s5_zoomin3
    show wolf_cg5_wolfarm at s5_zoomin3
    show wolf_s5_belly2 at s5_fit
    show wolf_s5_belly2_line_add at s5_fit
    with vpunch

    "가헬은 퍽퍽 소리가 날 정도로 강하게 움직이며 두 번째 절정을 시작했다." id c05_w_0959

    play sound "audio/effect/sqz3.mp3" volume 0.7
    show wolf_s5_seed3 at s5_fit
    with vpunch
    
    w "\"아우우우!...\"" id c05_w_0960

    play sound "audio/effect/sqz2.mp3" volume 0.7
    hide wolf_s5_seed3
    show wolf_s5_seed4 at s5_fit
    show wolf_cg5_wolfarm seedleft5
    with vpunch
    
    "[pl_name][josa_eun_neun] 뜨거운 정액이 꿀럭꿀럭 들어오는 것을 느낄 수 있었다." id c05_w_0961
    "아까보다 훨씬 많은 양이 들어오는 것 같았다." id c05_w_0962
    "뱃속이 두 번이나 꽉 차는 기분은 이상했다. 몸속으로 용암의 강이 흐르는 느낌이었다." id c05_w_0963
    
    c "(이러다가 입으로 토하는 거 아냐?)" id c05_w_0964

    play sound "audio/effect/SPS - (8).mp3" volume 0.6
    
    show wolf_s5_body at s5_zoomback2
    show wolf_cg5_wolfarm at s5_zoomback2
    hide wolf_s5_belly
    hide wolf_s5_belly2
    hide wolf_s5_belly2_line_add
    hide wolf_s5_seed4
    with Dissolve (0.8)
    
    "몇 번이고 계속되는 격류에 조금 무서워지기 시작할 때쯤, 가헬은 천천히 뒤로 물러났다." id c05_w_0965
    "깊은 곳에 박혀있던 굵은 자지가 쑥 빠져나가면서 민감한 내벽을 긁고 지나갔다." id c05_w_0966

    with hpunch
    
    c "\"으헉!\"" id c05_w_0967
    
    "준비되지 않은 자극에 [pl_name][josa_eun_neun] 벼락을 맞은 것처럼 떨었다." id c05_w_0968
    "가헬은 뻥 뚫린 구멍에서 조금씩 새어 나오는 정액을 보고 다시 흥분했다." id c05_w_0969

    play sound "effect/sticky2.mp3" volume 0.65

    show wolf_s5_penisup at s5_fit
    show wolf_s5_seedleft_wolf at s5_fit
    show wolf_s5_seedleft2_wolf at s5_fit
    with dissolve

    "가헬의 좆은 두 번의 분출로도 모자란 지 여전히 고개를 들고 있었다." id c05_w_0970
    "크림처럼 휘저어진 정액과 방금 싼 꾸덕꾸덕한 정액이 달라붙은 기둥은 굉장히 음란한 모습이었다." id c05_w_0971

    transform s5_movelr :
        ease 1.2 xoffset -15
        ease 1.2 xoffset 0
        repeat 2

    transform s5_movelr2 :
        ease 1.2 xoffset -22
        ease 1.2 xoffset 0
        repeat 2

    transform s5_movelr5 :
        ease 1.25 xoffset -13
        ease 1.25 xoffset 0
        repeat 2

    play sound "audio/effect/SPS - (1).mp3" volume 0.7

    show wolf_s5_penisup at s5_movelr
    show wolf_s5_seedleft_wolf at s5_movelr
    show wolf_s5_seedleft2_wolf at s5_movelr
    show wolf_s5_body at s5_movelr2
    show wolf_cg5_wolfarm at s5_movelr2

    show wolf_s5_cara at s5_movelr5
    if wolf_dom >= 1 :
        show wolf_s5_bite at s5_movelr5
    show wolf_s5_seed_cara at s5_movelr5

    pause 4.0

    "가헬은 3라운드를 시작할 기세로 자지를 살살 문질렀다." id c05_w_0972
    
    w horny "\"[pl_name]...\"" id c05_w_0973
    
    c ddam2 "\"뭐?! 또 하려고? 아, 안돼. 더는 못해...\"" id c05_w_0974
    
    "[pl_name][josa_eun_neun] 가헬의 정력이 정말로 무서워졌다." id c05_w_0975
    "기겁하고 손사래 치는 [pl_name]의 모습에 가헬은 조금이나마 이성이 돌아왔다." id c05_w_0976
    "물론 잔뜩 흥분한 좆은 그대로였다." id c05_w_0977
    
    
    w "\"그럼... 마지막으로 위에 싸기만 하겠다.\"" id c05_w_0978
    
    "[pl_name][josa_eun_neun] 가헬의 말을 듣고도 제대로 이해하지 못했다." id c05_w_0979
    "너무 피곤해서 팔다리가 축축 늘어지는 기분이었다." id c05_w_0980
    "[pl_name][josa_eun_neun] 반쯤 감긴 눈으로 가헬의 행동을 지켜봤다." id c05_w_0981

    transform s5_movelr3 :
        ease 0.3 xoffset -13
        ease 0.3 xoffset 0
        repeat 3

    transform s5_movelr4 :
        ease 0.3 xoffset -20
        ease 0.3 xoffset 0
        repeat 3

    transform s5_movelr6 :
        ease 0.305 xoffset -16
        ease 0.305 xoffset 0
        repeat 3
    
    play sound "effect/sticky.mp3" volume 0.65

    show wolf_s5_penisup at s5_movelr3
    show wolf_s5_seedleft_wolf at s5_movelr3
    show wolf_s5_seedleft2_wolf at s5_movelr3
    show wolf_s5_body at s5_movelr4
    show wolf_cg5_wolfarm at s5_movelr4

    show wolf_s5_cara at s5_movelr6
    if wolf_dom >= 1 :
        show wolf_s5_bite at s5_movelr6
    show wolf_s5_seed_cara at s5_movelr6

    pause 1.8

    "가헬은 그대로 [pl_name]의 몸 위에서 빠르게 움직였다." id c05_w_0982
    "찔꺽거리는 소리가 유난히 크게 들린다." id c05_w_0983
    "그동안의 격렬한 행위에 가헬의 자지도 꽤 민감해졌는지 붉게 달아올랐다." id c05_w_0984

    play sound "effect/sticky3.mp3" volume 0.65

    show wolf_s5_penisup at s5_movelr3
    show wolf_s5_seedleft_wolf at s5_movelr3
    show wolf_s5_seedleft2_wolf at s5_movelr3
    show wolf_s5_body at s5_movelr4
    show wolf_cg5_wolfarm at s5_movelr4

    show wolf_s5_cara at s5_movelr6
    if wolf_dom >= 1 :
        show wolf_s5_bite at s5_movelr6
    show wolf_s5_seed_cara at s5_movelr6

    pause 1.8
    
    w "\"크르르르르...\"" id c05_w_0985
    
    "사정한지 얼마 안 됐는데도 금방 절정이 가까워졌다." id c05_w_0986
    "어떻게 보면 잠깐 멈췄던 사정을 다시 시작하는 것과 다름없었다." id c05_w_0987
    "가헬은 순간 우뚝 멈추더니, 세 번째 분출을 시작했다." id c05_w_0988
    
    # 가헬 화면으로 왈칵 분출

    play sound "audio/effect/sqz1.mp3" volume 0.7
    show wolf_s5_seed at s5_fit
    show wolf_s5_seedleft2_cara at s5_fit
    with vpunch
    
    "왈칵왈칵 쏟아져나오는 정액은 전보다 꽤 묽어졌지만, 양은 전혀 줄지 않았다." id c05_w_0989

    play sound "audio/effect/sqz2.mp3" volume 0.7

    hide wolf_s5_seed
    show wolf_s5_seedleft3_cara at s5_fit
    show wolf_s5_seed5 at s5_fit
    with vpunch

    "허공에 날아오른 물줄기는 [pl_name]의 몸 위로 떨어졌다." id c05_w_0990
    "따뜻함을 넘어서 뜨겁게 느껴지는 정액이 [pl_name][josa_eul_reul] 푹 적시기 시작했다." id c05_w_0991
    
    play sound "audio/effect/sqz4.mp3" volume 0.7

    show wolf_s5_screenseed at s5_fit
    with vpunch

    show wolf_s5_screenseed :
        ease 2.5 yzoom 2 yoffset 600 alpha 0
    pause 0.5

    show wolf_s5_screenseed2 at s5_fit
    with vpunch

    show wolf_s5_screenseed2 :
        ease 2 yzoom 2 yoffset 700 alpha 0

    pause 1.8

    c horny4 "\"윽!\"" id c05_w_0992
        
    "엄청난 기세로 분출된 정액은 [pl_name]의 얼굴까지 튀었다." id c05_w_0993
    
    hide wolf_s5_seed5
    with dissolve

    "[pl_name][josa_eun_neun] 반사적으로 그걸 핥아버렸다." id c05_w_0994

    c "(맛, 이상해...)" id c05_w_0995
    
    "가헬의 페로몬이 듬뿍 담겨서 그런지, 형용하기 힘든 이상한 맛이 났다." id c05_w_0996
    "하지만 딱히 뱉을 생각은 안 들었다." id c05_w_0997
    "따뜻한 물에 푹 담가진 기분이라 점점 졸리기만 했다." id c05_w_0998
    
    w "\"하아, 후우...\"" id c05_w_0999
    
    "긴 절정 끝에 가헬은 깊은숨을 내쉬며 여운을 즐겼다." id c05_w_1000
    "뭘 먹지 않고도 배부른 기분이 들었다. [pl_name][josa_wa_gwa] 끝내주는 밤을 보냈다는 게 너무나도 행복했다." id c05_w_1001

    transform s5_movedw3 :
        ease 1.5 yoffset -125
    
    transform s5_movedw4 :
        ease 1.5 yoffset -15

    show wolf_s5_penisup at s5_movedw3
    show wolf_s5_seedleft_wolf at s5_movedw3
    show wolf_s5_seedleft2_wolf at s5_movedw3
    show wolf_s5_body at s5_movedw4
    show wolf_cg5_wolfarm at s5_movedw4
    scene bg black with Fade (0.8,0.8,0.8)
    
    "가헬은 [pl_name][josa_eul_reul] 끌어안았다."    
    "[pl_name][josa_eun_neun] 눈을 감고 가헬의 체온을 느끼며 서서히 잠에 빠져들었다." id c05_w_1002
    "손가락 하나 까딱하기 싫을 정도로 피곤했다." id c05_w_1003

    scene bg gahel_room_night with Fade (0.8,0.8,0.8)

    show wolf nake_d shy5
    with dissolve
    
    w "\"[pl_name]?\"" id c05_w_1004

    show wolf nake_d happy
    with dissolve

    c nake_d sigh "\"으응... 조금만 쉬고, 씻을게...\"" id c05_w_1005
    
    "[pl_name][josa_eun_neun] 그 말을 끝으로 거의 기절하듯 잠들었다." id c05_w_1006

    stop music fadeout 2.5

    $ renpy.end_replay()

label c5w_end:

    # 가헬 방 낮 배경
    scene bg gahel_room with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35
    
    show wolf nake0_d happy
    with dissolve

    "{i}~다음 날 아침~{/i}" id c05_w_1007

    c nake0_d ddam2 "\"헉!!\"" id c05_w_1008
    
    "[pl_name][josa_eun_neun] 번쩍 잠에서 깼다." id c05_w_1009
    "언제나처럼 평화로운 아침의 풍경이 [pl_name][josa_eul_reul] 반겨준다." id c05_w_1010

    show wolf nake0_u shy5
    with dissolve

    w "\"일어났나.\"" id c05_w_1011

    show wolf nake0_d happy
    with dissolve
    
    c "\"가헬?\"" id c05_w_1012

    show wolf shy
    with dissolve

    show wolf :
        ease 0.5 yoffset 20
        ease 0.5 yoffset 0
    
    
    "침대 옆자리에는 알몸의 가헬이 누워있었다. 가헬은 [pl_name][josa_eul_reul] 껴안은 채로 가볍게 코를 비볐다." id c05_w_1013

    show wolf happy
    with dissolve

    c shy "(아, 맞다. 어제...)" id c05_w_1014

    "[pl_name][josa_eun_neun] 어젯밤 화끈한 정사의 흔적으로 얼룩진 침대 시트를 보고 약간 민망해졌다." id c05_w_1015
    "뒤늦게 온몸이 쑤시는 게 느껴졌다. 근육통으로 뻣뻣하게 굳어버린 팔다리를 움직이기가 너무 힘들었다." id c05_w_1016
    "[pl_name][josa_eun_neun] 어제 일어난 일을 천천히 되짚어봤다." id c05_w_1017

    c shy2 "(나 뭔가 부끄럽게 헐떡거리다가... 설마 기절했나?)" id c05_w_1018

    "너무 큰 쾌락을 느낀 뒤로 기억이 흐릿했다." id c05_w_1019

    c consider "(뭔가 무서운 일도 있었던 거 같은데...)" id c05_w_1020

    show wolf nake0_u shy5
    with dissolve

    w "\"아직 피곤할 텐데, 조금 더 누워있지 그래.\"" id c05_w_1021

    show wolf nake0_d happy
    with dissolve

    show wolf at change(1.2, 0, 100)
    with Dissolve (0.8)

    show wolf shy :
        ease 1 yoffset 150
        ease 0.35 yoffset 160
        ease 0.35 yoffset 150
    with Dissolve (0.15)

    pause 1.8

    "가헬은 [pl_name][josa_eul_reul] 더 꼭 끌어안고 목덜미에 얼굴을 파묻었다." id c05_w_1022
    "격렬한 운동으로 땀을 흘린 덕분에 [pl_name]의 체취도 짙어졌고, 가헬의 냄새 역시 잔뜩 묻어있었다." id c05_w_1023
    "그게 맘에 든 가헬은 [pl_name][josa_eul_reul] 놓아주고 싶지 않았다. 함께 침대에서 늦잠을 자고 싶은 욕구가 마구 생겨났다." id c05_w_1024

    c shy2 "\"그러고 싶지만...\"" id c05_w_1025

    hide wolf
    show wolf nake0_d shy
    with dissolve

    show wolf nake_d
    with Dissolve (0.8)

    with vpunch

    "[pl_name][josa_eun_neun] 크게 기지개를 켰다가 뭔가 허리를 쿡 찌르는 느낌에 흠칫했다." id c05_w_1026
    "익숙한 무게감과 온도에 식은땀이 났다." id c05_w_1027

    c ddam2 "\"설마 또 하려고?...\"" id c05_w_1028

    show wolf nake_u shy3
    with dissolve
    
    w "\"아, 아니다! 이건 그냥 아침이라서...\"" id c05_w_1029

    show wolf nake_d shy2
    with dissolve
    
    "가헬이 당황한 사이, [pl_name][josa_eun_neun] 무거운 몸을 이끌고 침대에서 일어났다." id c05_w_1030
    "근육통에 비명을 지를 뻔했지만, 어떻게든 자리에서 일어설 수 있었다." id c05_w_1031

    c sigh "\"으으... 일단 씻어야겠어.\"" id c05_w_1032
    
    "[pl_name][josa_eun_neun] 털에 말라붙은 정액을 씻어내고 싶었다. 가헬은 조금 아쉬웠지만 차마 [pl_name][josa_i_ga] 씻는 걸 말릴 수는 없었다." id c05_w_1033

    show wolf nake_u shy4
    with dissolve
    
    w "\"방 정리는 내가 하겠다.\"" id c05_w_1034

    show wolf nake_d happy
    with dissolve
    
    "[pl_name][josa_eun_neun] 고개를 끄덕이고 후들거리는 다리로 씻으러 갔다." id c05_w_1035
    
    scene bg gahel_room with Fade(0.8, 0.8, 0.8)
    
    "평소보다 오래 걸렸지만 [pl_name][josa_eun_neun] 구석구석 깔끔하게 씻고 돌아왔다." id c05_w_1036

    show wolf inn_d
    with dissolve

    "놀라울 정도로 말끔하게 치워진 방에서 가헬이 속옷을 입고 있었다." id c05_w_1037
    
    c inn_d talk "\"어, 벌써 씻고 왔어?\"" id c05_w_1038
    
    show wolf inn_u embarrass
    with dissolve

    w "\"... 응. 우물에서 씻었다.\"" id c05_w_1039

    show wolf inn_d base
    with dissolve
    
    "조금 미심쩍은 침묵이 있었지만, 물기를 닦아내는 가헬이 거짓말을 하는 것 같진 않았다." id c05_w_1040
    "[pl_name][josa_eun_neun] 팔을 스트레칭하며 말했다." id c05_w_1041
    
    c "\"끄응... 더 늦기 전에 가게 문을 열어야겠어.\"" id c05_w_1042

    show wolf inn_u talk
    with dissolve
    
    w "\"피곤하진 않은가?\"" id c05_w_1043

    show wolf base
    with dissolve
    
    c "\"뭐... 다리가 후들후들 떨리긴 하지만 기분은 상쾌한데?\"" id c05_w_1044

    show wolf talk
    with dissolve
    
    w "\"역시 쉬는 게...\"" id c05_w_1045

    show wolf inn_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 한 치의 거짓말도 없이 자신의 상태를 말했다." id c05_w_1046
    "극단적인 경험을 하고 나니 오히려 개운한 기분이었다." id c05_w_1047
    "[pl_name][josa_eun_neun] 옷을 챙겨입고 천천히 1층으로 내려갔다." id c05_w_1048

    stop music fadeout 2.5
    
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40 
    
    "걱정만 하던 일이 다 지나가고 난 뒤, [pl_name][josa_eun_neun] 홀가분한 기분으로 영업 준비를 했다." id c05_w_1049
    "가헬이 청소하는 동안, [pl_name][josa_eun_neun] 상품 진열을 마치고 표지판을 뒤집어놓았다." id c05_w_1050
    
    c talk "\"이렇게까지 상쾌한 아침은 오랜만이야.\"" id c05_w_1051
    
    "가헬이 보기엔 좀 이상할 정도로 반짝반짝 빛나는 상태였다." id c05_w_1052

    show wolf am_u talk
    with dissolve
    
    w "\"다리가 아프다고 하지 않았나? 오늘은 좀 앉아 있는 게 좋겠군.\"" id c05_w_1053

    show wolf am_d base
    with dissolve
    
    c "\"음, 그건 그렇네.\"" id c05_w_1054
    
    "[pl_name][josa_eun_neun] 의자에 앉아서 허벅지를 주물렀다. 아직도 힘이 잘 들어가지 않았다." id c05_w_1055
    "[pl_name][josa_eun_neun] 첫 손님이 언제쯤 올까 생각하다가 엘레드가 떠올랐다." id c05_w_1056
    
    c consider "(술집에서 만난 이후로 얼굴을 못 봤네.)" id c05_w_1057
    
    "엘레드에게는 매정한 일이지만, 이제는 정말로 엘레드를 거절할 일만 남았다." id c05_w_1058
    
    c question2 "(더 이상 가게에 안 오려나?)" id c05_w_1059
    
    "상상해 보니 왠지 아쉬워졌다." id c05_w_1060
    "엘레드를 \'친구\'라고 할 수는 없지만, 아무튼 단골손님이고 어느 정도 친해진 사이였다." id c05_w_1061
    
    c consider "(그렇다고 예전과 같은 사이로 남을 수는...)" id c05_w_1062
    
    c sigh "(어휴. 그만 걱정하자. 엘레드를 만나면 어떻게든 되겠지.)" id c05_w_1063
    
    "[pl_name][josa_eun_neun] 습관적인 걱정을 그만두고 장부를 펼쳤다. 남는 시간에 장부 정리나 할 생각이었다." id c05_w_1064
    
    "어느 정도 시간이 흐르고, 손님을 몇 명 상대하고 나니 평소의 일상으로 돌아온 기분이었다." id c05_w_1065
    "[pl_name][josa_eun_neun] 슬슬 앉아 있는 것에 질려서 조심스레 일어섰다." id c05_w_1066

    show wolf am_u talk
    with dissolve
    
    w "\"뭐 필요한 거 있나? 내가 대신 하겠다.\"" id c05_w_1067

    show wolf am_d base
    with dissolve
    
    c ddam2 "\"아, 아니... 그렇게까지 힘들지 않아.\"" id c05_w_1068
    
    "[pl_name][josa_i_ga] 가헬의 과보호에 익숙해지려면 조금 더 시간이 필요할 것 같다." id c05_w_1069
    
    scene bg home with Fade(0.8, 0.8, 0.8)
    
    "[pl_name]의 일상은 가헬과의 연애 이후로 더 행복해졌다." id c05_w_1070
    "크게 달라진 것은 없지만, 눈만 마주쳐도 괜히 웃음이 났다." id c05_w_1071
    "마냥 행복할 것 같았던 일상은, 어떤 사건으로 크게 흔들리게 된다." id c05_w_1072
    "[pl_name][josa_i_ga] 생각하지 못한 방향으로..." id c05_w_1073

    jump patreon_end



