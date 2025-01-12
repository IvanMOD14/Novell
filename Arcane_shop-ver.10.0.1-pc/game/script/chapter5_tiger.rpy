label c5t_start:

    $ cleanup_memory()
    $ _skipping = False
    scene bg back_alley
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
    
    # 여기에 음악
    play music "audio/chill-abstract-intention-12099.mp3" volume 0.7 fadein 2.5

    hide chapter_back
    hide chap
    hide ter
    hide five
    with Dissolve (1.5)

    $ _skipping = True
    
    show screen book_icon with dissolve

    "{i}다음 날{/i}" id c05_t_0000

    show tiger out_d base_am
    with dissolve

    "엘레드는 아침부터 뒷골목을 서성거리고 있었다." id c05_t_0001

    show tiger at walk (500, 3.0, 4)

    "좀 더 앞으로 가면 [pl_name]의 가게지만, 오늘은 왠지 가봤자 후회만 할 것 같았다." id c05_t_0002

    show tiger at mirror
    with dissolve
    show tiger at walk (0, 3.0, 5)
    
    "이러지도 저러지도 못한 채, 엘레드는 같은 자리만 맴돌았다." id c05_t_0003
    
    show tiger sad3_am at mirror2
    with dissolve

    "엘레드의 인생에서 이렇게까지 오래 고민하는 일은 많지 않았다." id c05_t_0004

    show tiger sad2_am
    with dissolve

    t "(도대체 어디가 약점인지...)" id c05_t_0005

    show tiger base_am
    with dissolve

    "엘레드에게 [pl_name][josa_eun_neun] 마치 거대한 요새와도 같았다." id c05_t_0006
    "뻔뻔하게 [pl_name][josa_wa_gwa] 얼굴을 마주하는 정도는 쉽지만, 그 안에 들어가기는 너무나도 어려웠다." id c05_t_0007
    "어떻게든 간신히 벽을 넘었나 싶었지만, 그 안에는 더 높고 견고한 성벽이 기다리고 있었다." id c05_t_0008

    show tiger out_u sad3_am
    with dissolve

    t "(처음엔 이럴 생각이 아니었는데...)" id c05_t_0009
    t "(아니, 정말 '처음'에는 이럴 생각이긴 했지만...)" id c05_t_0010
    
    "이렇게 '가볍게 즐기는 사이'로 끝내고 싶지 않았다." id c05_t_0011
    
    show tiger out_d sad2_am
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (120, -200)

    "엘레드는 한숨을 푹 쉬고 기억을 되짚어 보았다. 생각할수록 죄다 후회되는 것뿐이었다." id c05_t_0012

    # 과거 가게 배경으로
    scene bg shop_past with Fade(0.8, 0.8, 0.8)
    
    "엘레드가 [pl_name][josa_eul_reul] 처음 봤을 때는 지금으로부터 약 4달 전이었다." id c05_t_0013
    "뒷골목에 마법 상점이 생기는 일도 흔치 않은데, 마탑의 공증을 받았다는 얘기가 신경 쓰였다." id c05_t_0014
    "엘레드는 정찰 삼아 한번 둘러볼 생각이었다." id c05_t_0015

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c05_t_0016

    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger am_d base_am :
        xoffset -1500
    show tiger at walk (0, 2.8, 6)

    c talk "\"어서 오세요. 찾는 물건이 있으신가요?\"" id c05_t_0017

    show tiger am_u talk_am
    with dissolve

    t "\"... 자네...\"" id c05_t_0018
    
    show tiger base_am
    with dissolve

    c talk "\"네?\"" id c05_t_0019
    
    show tiger wink_am
    with dissolve

    t "\"자네를 찾으러 왔네.\"" id c05_t_0020
    
    show tiger am_d base_am
    with dissolve

    c question2 "\"... 네??\"" id c05_t_0021

    show tiger shy_am
    with dissolve

    "엘레드는 [pl_name][josa_eul_reul] 보자마자 반해버렸다." id c05_t_0022
    "신비로운 느낌의 오드아이도, 묶어놓은 기다란 꽁지머리도, 옷 틈새로 보일 듯 말 듯한 얇은 허리도, 모든 것이 엘레드의 마음에 쏙 들었다." id c05_t_0023
    "엘레드는 멋진 미소와 함께 인사했다." id c05_t_0024

    show tiger am_u smile_am
    with dissolve

    t "\"어험! 나는 반슈타인 기사단의 단장, 엘레드라고 하네.\"" id c05_t_0025

    show tiger am_d base_am
    with dissolve

    c talk "\"아, 안녕하십니까. 마법 상점을 찾아주셔서 감사합니다.\"" id c05_t_0026

    "[pl_name][josa_eun_neun] 엄청난 귀족 앞에서 예법을 차려 인사했다." id c05_t_0027
    "시장에서 엘레드의 '악명'을 몇 번 들었으나, 실물을 보는 것은 처음이었다." id c05_t_0028

    c consider "(갑옷을 무슨 용병처럼 입었네...)" id c05_t_0029
    
    show tiger am_u talk_am
    with dissolve

    t "\"그 정도로 격식 차릴 필요 없네. 내게 필요한 건, 자네의 이름이라네.\"" id c05_t_0030
    
    show tiger am_d base_am
    with dissolve

    c talk "\"네? 저, 제 이름은 [pl_name]입니다.\"" id c05_t_0031
    
    "[pl_name][josa_eun_neun] 조금 긴장하며 대답했다. 기사단에서 자신을 찾아올 이유가 있는지 고민했다." id c05_t_0032

    show tiger am_u talk_am
    with dissolve

    t "\"[pl_name]... 그렇군. 이곳에서는 무엇을 파나?\"" id c05_t_0033
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드를 손님으로 판단하고, 준비했던 영업 대사를 읊었다." id c05_t_0034
    
    c talk "\"제가 직접 연금술로 만든 상품들이 준비되어 있습니다.\"" id c05_t_0035
    
    c "\"마탑에서 공증받은 회복 물약은 물론이고, 이쪽에는 연고나 광택제 같은 다양한 생활용품도 있습니다.\"" id c05_t_0036
    
    "[pl_name][josa_i_ga] 열심히 소개했지만, 엘레드는 내용을 거의 듣지 않았다." id c05_t_0037
    
    "엘레드는 상품보단 열심히 말하는 [pl_name]에게 관심이 있었다. 엘레드는 가게를 잠깐 둘러보고는 다시 말했다." id c05_t_0038
    
    show tiger embarrass_am
    with dissolve
    pause(0.7)
    show tiger talk_am
    with dissolve

    t "\"사랑의 묘약 같은 것은 없나?\"" id c05_t_0039
    
    c question2 "\"예? 그, 그런 건 당연히 없습니다만...\"" id c05_t_0040
    
    "[pl_name][josa_eun_neun] 당황한 표정으로 엘레드를 보았다. 그러나 이어진 말은 [pl_name][josa_eul_reul] 더욱 크게 당황하게 했다." id c05_t_0041
    
    show tiger am_u horny_am
    with dissolve

    t "\"이상하군. 나는 이미 자네에게 매혹당한 것 같은데.\"" id c05_t_0042
    
    show tiger am_d smile_am
    with dissolve

    "[pl_name][josa_eun_neun] 그제야 엘레드에 대한 소문이 무슨 뜻인지 제대로 이해했다. 엘레드의 첫인상이 정해진 순간이었다." id c05_t_0043
    
    c ddam2 "\"아, 하, 하...\"" id c05_t_0044
    
    "[pl_name][josa_eun_neun] 누가 봐도 어색한 미소를 지었다." id c05_t_0045
    
    c ddam "(이런 말이나 하려고 가게에 온 건가? 뭐라고 대답해야 하지?)" id c05_t_0046
    
    "미묘한 침묵 속에서, 엘레드는 이곳에 온 원래 목적을 떠올렸다. 마탑과 무슨 관련인지 알아볼 생각이었다." id c05_t_0047
    
    show tiger am_u talk_am
    with dissolve

    t "\"자네는 마탑 출신인가? 굉장히... 유능한 것 같군.\"" id c05_t_0048
    
    show tiger base_am
    with dissolve

    c talk "\"아, 아닙니다. 그런 곳에서 배울 만큼 돈이 많지는 않아서요.\"" id c05_t_0049
    
    show tiger am_d
    with dissolve

    t "(특이하군... 마탑 출신도 아니면서 연금술을 배웠다고?)" id c05_t_0050
    
    "엘레드는 아직 [pl_name][josa_eul_reul] 완전히 믿을 수는 없었다. 하지만 [pl_name]의 호감을 얻기 위해서라도, 너무 캐묻는 것은 자제하기로 했다." id c05_t_0051
    
    show tiger am_u talk_am
    with dissolve

    t "\"독학으로 가게를 차리는 건 쉽지 않은 일이지. 자네가 더욱 맘에 드는군.\"" id c05_t_0052
    
    show tiger am_d base_am
    with dissolve

    c smile "\"영광입니다.\"" id c05_t_0053
    
    # 캐릭터들 숨기기
    hide tiger
    with dissolve

    "그날 이후로, 엘레드는 '단골손님'이 되었다." id c05_t_0054
    "[pl_name][josa_i_ga] 마탑과 직접적인 관련이 없다는 것을 확인했지만, 엘레드는 계속 가게를 찾아갔다." id c05_t_0055
    "[pl_name][josa_i_ga] 엘레드의 플러팅을 거절할수록, 엘레드는 오히려 점점 더 [pl_name]에게 빠져들었다." id c05_t_0056
    
    # 회상 끝 뒷골목 엘레드로
    
    scene bg back_alley with Fade(0.8, 0.8, 0.8)

    show tiger out_d sad2_am
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (120, -200)

    "엘레드는 크게 한숨을 쉬었다." id c05_t_0057
    "그냥 이 정도 관계로 만족한다면, 큰 문제가 생기진 않을 것이다." id c05_t_0058
    "지금까지 그래왔던 것처럼, 가문에서 [pl_name]에게 직접 손대지는 않을 것이다." id c05_t_0059
    
    show tiger sad3_am
    with dissolve

    t "(하지만...)" id c05_t_0060

    "엘레드는 더 많은 것을 원했다. [pl_name][josa_wa_gwa] 좀 더 진지한 관계가 되고 싶었다." id c05_t_0061
    "그러나 그것은 엘레드의 욕심일 뿐이었다. [pl_name][josa_i_ga] 엘레드와 같은 마음일 리가 없었다." id c05_t_0062
    "만에 하나 둘이 연인이 되더라도, 현실적인 문제가 잔뜩 기다리고 있었다. " id c05_t_0063
    
    t "(신분, 작위, 후계자, 결혼...)" id c05_t_0064
    
    show tiger out_d sad2_am
    with dissolve

    t "(하아...)" id c05_t_0065
    
    "생각할수록 엘레드의 마음만 괴로워질 뿐이었다." id c05_t_0066
    "엘레드는 결국 발걸음을 돌렸다. 이런 상태로 얼굴을 마주하는 건 별로 좋은 생각이 아니었다." id c05_t_0067


    stop music fadeout 2.5

label c5t_market:
    scene bg market with Fade(0.8, 0.8, 0.8)
    play music "audio/spirit-of-adventure-130563.mp3" volume 0.9 fadein 1.0  
    
    # 시장 낮 배경

    "한편, [pl_name][josa_eun_neun] 시장을 돌아다니고 있었다." id c05_t_0068
    "어제 장사가 너무 잘 되는 바람에 몇 가지 재료가 똑 떨어졌다." id c05_t_0069
    "사는 김에 식재료나 다른 것들도 사다 보니, 생각보다 시간이 많이 흘렀다." id c05_t_0070
    
    c "(빨리 가게로 돌아가야지. 가헬이 알아서 잘하고 있겠지만, 엘레드랑 마주치면 또 무슨 일이 생길지 모르니까...)" id c05_t_0071

    "가방을 정리하고 돌아서는 [pl_name]의 뒤로, 누군가 따라붙었다." id c05_t_0072

    show mob boar at left
    with dissolve
    show mob2 cat at right
    with dissolve

    show mob at talk_move
    mob "\"아~ 형씨, 드디어 찾았네.\"" id c05_t_0073
    
    "한 명이 아니었다. 딱 용병 같은 차림새의 수인 둘이 [pl_name]의 좌우로 다가왔다." id c05_t_0074
    
    "[pl_name][josa_i_ga] 아는 얼굴은 아니었다." id c05_t_0075
    
    c consider "\"... 누구세요?\"" id c05_t_0076

    "[pl_name][josa_eun_neun] 둘을 약간 경계하며 대답했다." id c05_t_0077
    
    "말을 건 쪽은 어깨가 떡 벌어진 멧돼지 수인이고, 옆으로 다가온 수인은 얍삽한 인상의 고양이 수인이었다." id c05_t_0078

    show mob2 at talk_move
    mob2 "\"별일은 아니고, 고용주께서 댁을 보고 싶어 하시거든.\"" id c05_t_0079
    
    "가게에 직접 찾아오거나 편지를 보내거나 하지도 않고, 다짜고짜 용병을 통해 얘기하는 건 뭔가 이상했다." id c05_t_0080
    "당연히 그 '고용주'가 뭔가 떳떳하지 못한 구석이 있다는 것을 의미했다." id c05_t_0081
    "[pl_name][josa_eun_neun] 자신의 떳떳하지 못한 거래들을 떠올렸다. 하지만 요즘은 암시장에 자주 가지도 않았고, 가장 최근 거래도 문제없이 끝났다." id c05_t_0082
    
    c "\"왜요?\"" id c05_t_0083
    
    "[pl_name][josa_eun_neun] 일단 발뺌하며 눈치를 봤다. 애초에 어떻게 자신을 찾아서 말을 거는지 의심스러웠다." id c05_t_0084
    "[pl_name][josa_eun_neun] 외모를 숨기고 암시장에 가기 때문에, 이렇게 간단히 찾아낼 수 있을 리가 없었다." id c05_t_0085
    
    show mob at talk_move
    mob "\"나야 모르지.\"" id c05_t_0086
    
    show mob2 at talk_move
    mob2 "\"넌 입 좀 다물어.\"" id c05_t_0087
    mob2 "\"에헴, 확인차 물어보겠는데 이 동네 마법 상점의 주인 맞지?\"" id c05_t_0088
    
    "마법 상점을 수소문해서 [pl_name][josa_eul_reul] 찾았다면 말이 안 되는 건 아니었다." id c05_t_0089
    "하지만 굳이 길거리에서 말을 거는 것도 이상했다. [pl_name][josa_eun_neun] 이 용병들이 더욱 의심스러워졌다." id c05_t_0090
    "빠르게 둘을 위아래로 훑어보고, 딱히 높은 등급의 용병은 아니라고 판단했다." id c05_t_0091
    
    c "(몸에 흉터가 있긴 하지만, 그렇다고 경력이 많아 보이지는 않네.)" id c05_t_0092
    c "(가헬의 브로치처럼 소속을 증명하는 것도 없고. 복장도 이 동네 용병들이랑 다른데?)" id c05_t_0093
    
    "[pl_name][josa_eun_neun] 일단 살짝 떠보기로 했다." id c05_t_0094
    
    c talk "\"제 상점에는 구체적으로 무슨 용건인가요?\"" id c05_t_0095
    
    "용병은 서로 시선을 교환하더니, 고양이 수인 쪽이 입을 열었다." id c05_t_0096

    show mob2 at talk_move
    mob2"\"그래. 솔직히 우리도 잘 몰라. 하지만 너도 큰돈 만지고 싶지 않아?\"" id c05_t_0097
    
    "큰돈이라는 말에 조금 솔깃했지만, 대뜸 이런 식으로 말하는 것을 믿을 수는 없었다." id c05_t_0098
    
    c "(뒷세계에서 또 뭔가 심상치 않은 일이 생기고 있나?... 하지만 물어본다고 대답을 해줄 것 같진 않군.)" id c05_t_0099

    "더 들어봤자 쓸모없는 일이라고 판단한 [pl_name][josa_eun_neun] 고개를 저었다." id c05_t_0100

    c "\"말은 고맙지만, 잘 모르는 일에 참여할 수는 없어서요. 그럼 이만.\"" id c05_t_0101
    
    "[pl_name][josa_eun_neun] 가게로 돌아갈 생각으로 몸을 돌렸다." id c05_t_0102
    "골목 틈새로 들어가려고 하자, 용병이 재빠르게 앞을 막았다." id c05_t_0103
    
    show mob at talk_move
    mob "\"어허~ 그냥 가면 우리가 돈을 못 받지.\"" id c05_t_0104
    
    show mob2 at talk_move
    mob2 "\"얘기만 해도 끝나는 일이니까 얌전히 가자고. 응?\"" id c05_t_0105
    
    "살짝 찡그린 표정으로 위협하는 태도가 꽤 불량했다. [pl_name][josa_eun_neun] 이 상황에서 어떻게 해야 할지 고민했다." id c05_t_0106
    
    c consider "(뭐지? 이런 걸로 겁을 먹을 거라고 생각했나? 하긴 효과가 있었으니 이러는거겠지...)" id c05_t_0107
    
    "[pl_name][josa_eun_neun] 조금 타협하면 상대방도 한발 물러서리라 생각했다." id c05_t_0108
    
    c talk "\"얘기를 듣고 싶어도, 지금 당장은 좀 곤란한데요. 내일 가게로 오세요.\"" id c05_t_0109
    
    "어차피 가게에 오더라도 가헬을 이길 수는 없을 것이다." id c05_t_0110

    play channel1 "effect/footstep.mp3" volume 0.85
    show mob at fwalk
    pause 2

    "[pl_name][josa_eun_neun] 살짝 옆으로 비켜섰지만, 멧돼지 용병은 툴툴거리며 조금 더 위협적으로 [pl_name]에게 다가왔다." id c05_t_0111
    
    show mob at talk_frontmove
    mob "\"이 고생을 했는데 하루 더 기다리라고?\"" id c05_t_0112
    
    show mob2 at talk_move
    mob2 "\"아우, 진짜. 말은 내가 할 테니까, 너는 조용히 좀 해!\"" id c05_t_0113
    
    "고양이 용병은 또다시 동료를 타박하며 말을 이었다." id c05_t_0114
    
    show mob2 at talk_move
    mob2 "\"우리가 좀 급하거든? 지금 같이 댁의 상점으로 갈까?\"" id c05_t_0115
    
    c ddam2 "(어쩌지? 가게에 진짜 가기만 하면 가헬도 있으니 상관 없겠지만...)" id c05_t_0116
    c "(이 태도를 보면, 가게에 가기도 전에 어딘가 끌고 갈지도 몰라. 어떻게 하지?)" id c05_t_0117
    
    "[pl_name][josa_eun_neun] 빠르게 가방 속에 손을 넣었다." id c05_t_0118
    "위에 들어있는 건 물약을 담기 위한 빈 유리병들이었다. 그 아래에는 감자와 버섯 몇 개가 굴러다니고 있었다." id c05_t_0119
    
    c consider "(유리병을 던져버리면 시선을 돌릴 수 있을까? 너무 동그래서 쉽게 깨지진 않을 텐데.)" id c05_t_0120
    c "(차라리 마법을 쓰면 당황할까? 무슨 마법을 써야 하지? 아니, 그냥 경비병을 부르면...)" id c05_t_0121
    
    "[pl_name][josa_eun_neun] 아주 짧은 틈에 수많은 생각을 했다." id c05_t_0122
    "빠르게 주변을 둘러봤지만, 순찰하는 경비병은 보이지 않았다." id c05_t_0123

    $ unlock_info_tag(4, "3")
    $ display_text = _("정보 : 발광 마법")
    show screen affection_indicator

    c ddam "(윽, 그래도 경비병을 부르는 척하면 당황하겠지? 잠깐 시선을 돌리면 그 틈에 발광 마법으로 눈을...)" id c05_t_0124

    c ddam2 "\"겨, 경비병!!! 여기-\"" id c05_t_0125
    c ddam "\"윽-!!\"" id c05_t_0126

    # 인물 이미지 옆으로 휙 날려버리기
    
    play sound "effect/drop2.mp3" volume 1
    show mob :
        parallel :
            ease 0.4 zoom 2 

        parallel :
            ease 0.4 alpha 0 xoffset 50

    pause 0.2
    
    with vpunch

    
    "[pl_name][josa_i_ga] 돌발행동을 하자, 예상과는 정반대의 일이 벌어졌다." id c05_t_0127
    "깜짝 놀란 멧돼지 용병이 [pl_name][josa_eul_reul] 끌고 뒷골목 쪽으로 달렸다." id c05_t_0128
    
    show mob2 at talk_move
    mob2 "\"아니, 이런 미친!\"" id c05_t_0129
    
    # 고양이 호다닥
    play sound "audio/effect/walk.mp3" volume 0.95
    show mob2 :
        parallel :
            ease 0.4 zoom 2 

        parallel :
            ease 0.4 alpha 0 xoffset 200

    "고양이 용병도 재빠르게 그 뒤를 따라갔다." id c05_t_0130
    "길거리를 지나가던 수인 몇 명이 그 소리를 듣기는 했으나, 이미 그 자리에는 먼지만 날리고 있었다." id c05_t_0131

    stop music fadeout 2.5

label c5t_backalley:
    scene bg back_alley
    # show back_alley
    with Fade(0.8, 0.8, 0.8)

    

    # 음악 바꾸기
    play music "sahara-143269.mp3" volume 0.55 fadein 1.0
    
    show tiger out_d base_am
    with dissolve

    "엘레드는 뒷골목을 통해 중앙 광장 쪽으로 가고 있었다." id c05_t_0132

    play channel1 "effect/footstep.mp3" volume 0.95
    show tiger at walk (0, 5.0, 6)

    "아침부터 [pl_name]의 가게 앞에서 고민하다가 생각보다 많은 시간을 썼다." id c05_t_0133
    "창문으로 얼굴이라도 볼지 생각했지만, 자기 자신이 너무 한심해져서 결국 그만두었다." id c05_t_0134
    
    t "(그래도 일하러 가는데 늦지는 않겠군.)" id c05_t_0135

    play channel1 "effect/footstep.mp3" volume 0.95
    show tiger at walk (0, 5.0, 6)

    "마차가 있는 곳까지 빨리 가기 위해 엘레드는 발걸음을 재촉했다." id c05_t_0136
    "[pl_name]의 가게에 자주 가다 보니 뒷골목도 나름 익숙해졌다." id c05_t_0137
    "엘레드가 골목을 오른쪽으로 돌자, 어디선가 익숙한 목소리가 들렸다." id c05_t_0138
    
    c "\"누구 없- ...\"" id c05_t_0139
    c "\"도와주- ...\"" id c05_t_0140
    
    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (900, 0)

    t "([pl_name]? 멀리에서 뭔가 소리 지른 것 같은데...)" id c05_t_0141
    
    hide question

    "빠르게 스쳐 지나간 소리라서, 엘레드는 [pl_name]의 말을 제대로 듣지 못했다." id c05_t_0142
    "무슨 소리가 더 나는지 듣기 위해 엘레드는 감각을 곤두세웠다." id c05_t_0143

    play sound "audio/effect/walk.mp3" volume 1

    "[pl_name]의 목소리가 더 들리지는 않았지만, 다급하게 뛰어가는 발소리가 났다." id c05_t_0144
    "엘레드는 [pl_name][josa_i_ga] 뭔가로부터 도망친다고 생각했다. 곧바로 소리가 나는 곳을 뒤쫓았다." id c05_t_0145
    
    t "(이쪽인가?)" id c05_t_0146

    play channel1 "effect/cloth.mp3" volume 0.7

    "구불구불한 골목길을 지나가자, 저 멀리에서 누군가에게 끌려가는 [pl_name][josa_i_ga] 보였다." id c05_t_0147
    
    show tiger angry_am
    with dissolve
    
    "엘레드는 심장 속에서부터 피가 끓어오르는 느낌이 들었다." id c05_t_0148

    play sound "audio/effect/walk.mp3" volume 1
    show tiger at walk (2500, 2, 6)

    "곧바로 뛰기 시작하면서, 엘레드는 크게 소리쳤다." id c05_t_0149

    show tiger fight2_am
    with vpunch
    
    t "\"거기 서라!!\"" id c05_t_0150

    hide tiger
    show tiger out_u fight2_am at left
    with dissolve

    show mob boar at mirror, right
    with dissolve

    show mob at mirror, talk_move

    mob "\"누, 누구야?\"" id c05_t_0151

    play channel1 "effect/cloth.mp3" volume 0.8
    show mob at mirror :
        ease 0.2 xoffset 460
    show mob2 cat :
        xoffset 700
    with dissolve

    "상황 파악이 덜 된 동료의 등을 떠밀면서, 고양이 용병은 [pl_name][josa_i_ga] 도망치지 못하도록 팔까지 붙잡았다." id c05_t_0152

    show mob2 at talk_move

    mob2 "\"뒷골목에 무슨 기사가 있어?! 일단 뛰어!\"" id c05_t_0153

    ############################### 뒤로 돌고 뛰어가는거
    show mob at mirror2
    show mob2 at mirror
    with dissolve
    
    play sound "audio/effect/walk.mp3" volume 1
    show mob at walk (2500, 2, 6)
    show mob2 at walk (2500, 2, 6)
    pause 0.5
    
    c ddam2 "(엘레드?)" id c05_t_0154

    play sound "audio/effect/walk.mp3" volume 1
    show tiger at walk (2500, 2, 6)
    
    "엘레드는 뒷골목을 이리저리 뛰어다니며 용병들을 뒤쫓았다." id c05_t_0155

    with Fade(0.8, 0.8, 0.8)

    camera :
        
        ease 0.5 ypos 8
        ease 0.2 ypos -8
        repeat
    
    play sound "audio/effect/walk.mp3" volume 1
    show mob at mirror, walk (-650, 2.2, 6)
    show mob2 at mirror, walk (-450, 2.2, 6)
    pause 0.8
    
    show tiger fight_am at mirror, walk (500, 2, 6)
    pause 0.5
    
    "[pl_name][josa_eun_neun] 용병들이 당황한 사이 탈출을 시도했으나 역부족이었다." id c05_t_0156

    play channel1 "effect/cloth.mp3" volume 0.7
    show mob at mirror, talk_move
    show mob2 at mirror, talk_move

    "오히려 [pl_name][josa_i_ga] 버둥거리는 걸 막으려고 더 강하게 붙잡았다." id c05_t_0157
    
    c ddam "(으윽, 이러다 목 졸리겠어. 차라리 얌전히 있자...)" id c05_t_0158
    
    "[pl_name][josa_eun_neun] 흉흉한 기세로 쫓아오는 엘레드를 믿기로 했다." id c05_t_0159
    
    c ddam2 "(점점 가까이 오네. 금방 따라잡겠는데?)" id c05_t_0160
    c "(이 녀석들이 엘레드한테 정신이 팔려서 빈틈이 생기면, 마법을 써 봐야겠어.)" id c05_t_0161
    
    "엘레드는 굵직한 목소리로 용병들에게 말했다." id c05_t_0162

    show tiger fight2_am at mirror, talk_move 
    
    t "\"경고한다! 지금 투항하면, 감형해 주겠다.\"" id c05_t_0163
    
    show mob2 at talk_move

    mob2 "\"에잇, 젠장! 왜 그랬어!\"" id c05_t_0164

    show mob at talk_move
    
    mob "\"이럴 줄 알았으면 안 했지!!\"" id c05_t_0165
    
    show mob at mirror
    show mob2 at mirror2
    with dissolve
    
    play sound "audio/effect/walk.mp3" volume 1
    show mob at walk (-2200, 2, 6)
    show mob2 at walk (-2200, 2, 6)
    pause 0.5
    show tiger at mirror, walk (-2500, 2, 6)
    pause 1.5

    "용병들은 숨을 헐떡거리며 계속 도망치기에 바빴다. [pl_name][josa_eun_neun] 그 틈을 타 마법을 쓸 궁리를 했다." id c05_t_0166
    
    c "(발광 마법을 눈에 쏴보자. 엘레드의 시야를 방해하지 않게, 약간 옆에서...)" id c05_t_0167

    play sound "audio/effect/walk.mp3" volume 1
    show mob at mirror, walk (0, 2.2, 6)
    show mob2 at mirror, walk (150, 2.2, 6)
    pause 2.2
    
    "[pl_name][josa_eun_neun] 마력을 조절하며 신중하게 마법을 사용했다." id c05_t_0168

    # 발광 마법 번쩍!

    play sound "effect/flash_fast.mp3" volume 0.25    
    show flash_blue at flash_fast
    pause 0.95
    hide flash_blue
    
    with hpunch

    show mob at mirror, talk_move
    mob "\"윽! 뭐지?\"" id c05_t_0169
    
    show mob2 at mirror, talk_move
    mob2 "\"뭐해!? 왼쪽이야!\"" id c05_t_0170
    
    "그러나 너무 각도를 신경 쓰다가, 용병 하나 밖에 맞추지 못했다." id c05_t_0171
    "그마저도 잠깐 눈을 감게 만들었을 뿐, 발을 묶기에는 모자랐다." id c05_t_0172
    "[pl_name][josa_eun_neun] 최대한 빨리 다른 방법을 궁리했다." id c05_t_0173
    
    c consider "(역시 평소 쓰던 화염구를...)" id c05_t_0174
    c "(아니, 이렇게 가까이서 터트리면 나도 위험하지. 다른 방법을 생각하자.)" id c05_t_0175
    c "(직접 공격하지 않아도 방법은 있을 거야.)" id c05_t_0176
    
    "[pl_name][josa_eun_neun] 끌려가면서도 주변 상황을 둘러보았다." id c05_t_0177
    "뒷골목은 언제나처럼 잡동사니가 굴러다니고 있었다. 밟을 수 있는 길은 그렇게 넓지 않았다." id c05_t_0178
    
    c "(아무거나 움직여서 발에 걸리게 할까? 아니, 그냥 뛰어넘을 가능성이 있어.)" id c05_t_0179
    c "(조금 더 확실하게... 그래. 미끄러지게 얼음을 깔아보자. 어차피 몇초면 사라질 테니 정확하게 써야 해...)" id c05_t_0180
    
    "[pl_name][josa_eun_neun] 머릿속으로 술식을 그리며 적절한 때를 노렸다." id c05_t_0181
    "얼음 마법을 자주 쓰지 않아서 조금 불안했지만, 아무것도 안 하는 것보다는 나을 것이다." id c05_t_0182
    
    c talk "(지금!)" id c05_t_0183
    
    # (마법 이펙트)

    play sound "effect/freezing.mp3" volume 0.85
    show mob at mirror :
        pause 1.5
        ease 1 xoffset 500

    show mob2 at mirror :
        pause 1.5
        ease 1 xoffset 650

    show freezing with ice_effect
    pause 0.8
    hide freezing

    "[pl_name][josa_eun_neun] 바닥에 얇게 얼음을 깔았다. 용병들이 얼음판을 밟자마자 쭈욱 미끄러졌다." id c05_t_0184
    
    
    play sound "effect/crash.mp3" volume 0.62
    show mob :
        ease 0.1 yoffset 100
        ease 0.1 yoffset 90
        ease 0.1 yoffset 100
    pause 0.15
    camera :
        ease 0.5 ypos 0
    with vpunch

    mob "\"으악!\"" id c05_t_0185

    play sound "effect/crash.mp3" volume 0.62
    show mob2 :
        ease 0.1 yoffset 100
        ease 0.1 yoffset 90
        ease 0.1 yoffset 100
    pause 0.15
    with vpunch

    mob2 "\"뭐야!\"" id c05_t_0186

    c hurt "\"으윽...\"" id c05_t_0187

    "균형을 잃고 쓰러진 용병 때문에, [pl_name]도 바닥에 쓰러지고 말았다." id c05_t_0188
    "탈출하지는 못했지만, 시간을 꽤 많이 끌었다." id c05_t_0189

    show mob :
        pause 0.2
        ease 0.2 yoffset 0
    show mob2 :
        ease 0.25 yoffset 0
    
    play sound "audio/effect/walk.mp3" volume 1

    show tiger fight_am at walk (-500, 1.8, 6)
    pause 1.8
        
    "용병들은 [pl_name][josa_eul_reul] 들어 올려 다시 뛰려고 했으나, 엘레드는 그들을 꽤 가까이 따라잡았다." id c05_t_0190

    show tiger fight2_am at talk_move

    t "\"최후통첩이다! 인질을 놓지 않으면, 즉시 집행하겠다!\"" id c05_t_0191
    
    "엘레드의 쩌렁쩌렁한 목소리가 뒷골목에 울려 퍼졌다." id c05_t_0192

    show mob2 at talk_move
    
    mob2 "\"놓고 째자.\"" id c05_t_0193

    show mob at talk_move
    
    mob "\"알았어...\"" id c05_t_0194
    
    "용병들은 갈라지는 목소리로 빠르고 조용하게 얘기했다." id c05_t_0195

    with vpunch
    
    c "\"악!\"" id c05_t_0196
    
    "용병들이 [pl_name][josa_eul_reul] 집어 던지듯 내팽개쳤다. [pl_name][josa_eun_neun] 길바닥을 구르며 흙먼지를 뒤집어썼다." id c05_t_0197
    
    show tiger vangry_am at talk_move

    t "\"용서하지 않겠다!!\"" id c05_t_0198
    
    "[pl_name][josa_eul_reul] 버리고 도망가는 용병들의 뒤에 대고, 엘레드는 크게 소리쳤다." id c05_t_0199
    "일그러진 콧잔등과 드러낸 송곳니는 엘레드가 얼마나 분노하고 있는지 보여줬다." id c05_t_0200

    show tiger at talk_move

    "엘레드는 망치를 고쳐 쥐고 자세를 잡았다." id c05_t_0201
    
    play sound "effect/spark_eye.mp3" volume 0.6
    show spark_eye with spark_eye_effect
    "아주 찰나의 순간에, [pl_name][josa_eun_neun] 엘레드의 눈이 번쩍하고 빛나는 걸 보았다." id c05_t_0202
    
    # 호랑이 울음소리 넣기?
    play sound "effect/roar_tiger.mp3" volume 0.85
    show tiger fight2_am
    with vpunch
    "{i}크허엉-!!!{i}" id c05_t_0203
    
    "바닥에 거의 눕듯이 쓰러져있던 [pl_name][josa_eun_neun] 심장이 멈추는 것 같은 기분이 들었다." id c05_t_0204
    "듣기만 해도 무시무시한 울음소리였다. 용병들은 엘레드의 포효에 몸이 굳어버렸다." id c05_t_0205
    
    # 망치 퍽퍽 이펙트)
    show tiger :
        ease 0.2 xoffset 0

    play channel1 "effect/swing.mp3" volume 0.8
    pause 0.5
    play sound "effect/hit_hammer.mp3" volume 0.85
    show hit
    pause 0.2
    show mob :
        ease 0.2 xoffset 1400
    hide hit with Dissolve (0.2)
    with vpunch

    

    play channel1 "effect/swing2.mp3" volume 0.8
    pause 0.5
    play sound "effect/hit_hammer.mp3" volume 0.85
    show hit2
    pause 0.2
    show mob2 :
        ease 0.2 xoffset 1500
    hide hit2 with Dissolve (0.2)
    with vpunch    

    "엘레드가 엄청난 속도로 달려들어 망치를 휘둘렀다." id c05_t_0206

    play sound "effect/crash.mp3" volume 0.62
    with vpunch  
    mob "\"크어억!\"" id c05_t_0207

    play sound "effect/crash2.mp3" volume 0.6
    with vpunch    
    mob2 "\"으아악!\"" id c05_t_0208
    
    "눈 깜짝할 사이에 용병들은 망치에 얻어맞았고, 벽에 처박히듯 날아가 버렸다." id c05_t_0209

    "긴장이 풀려서 온몸에 힘이 빠진 [pl_name][josa_eun_neun] 벽에 기대어 앉았다." id c05_t_0210

    show tiger fight3_am out_d
    with dissolve

    t "\"자네, 괜찮나?\"" id c05_t_0211

    show tiger at fwalk
    pause 2
    show tiger sleep_am out_u
    with dissolve
    
    "엘레드는 멍하게 있는 [pl_name][josa_eul_reul] 와락 끌어안았다. 워낙 순식간에 일어난 일이라 [pl_name][josa_eun_neun] 얼떨떨한 상태로 대답했다." id c05_t_0212

    c talk "\"잘... 모르겠네요.\"" id c05_t_0213

    show tiger talk_am
    with dissolve

    t "\"일단 잠깐만 앉아있게.\"" id c05_t_0214

    hide tiger
    hide mob
    hide mob2
    with dissolve

    show tiger fight_am out_d at left
    show mob boar at mirror, right
    show mob2 cat :
        xoffset 650
    with dissolve
    

    "엘레드는 [pl_name][josa_eul_reul] 놓아주고, 기절한 것 같은 용병들에게 다가갔다." id c05_t_0215

    show tiger fight2_am out_u
    with dissolve

    t "\"시민의 안전을 위협하고, 명령을 듣지 않은 죄로 재판에 회부하겠다.\"" id c05_t_0216

    show tiger fight_am out_d
    with dissolve

    play sound "effect/flash_fast.mp3" volume 0.25    
    show flash_blue at flash_fast
    pause 0.95
    hide flash_blue
    pause 0.2
    camera :
        ease 0.1 xpos -10
        ease 0.2 xpos 10
        ease 0.1 xpos 0
    
    "당연히 대답은 없었다. 엘레드는 아티팩트를 사용해서 용병들의 팔다리를 묶었다." id c05_t_0217

    stop music fadeout 2.5

    scene bg back_alley with Fade(0.8, 0.8, 0.8)

    play music "audio/chill-abstract-intention-12099.mp3" volume 0.7 fadein 2.5    

    "[pl_name][josa_eun_neun] 어디 다치지 않았는지 확인하며 몸을 움직여봤다." id c05_t_0218
    
    c sigh "(으, 무릎에 멍들겠네... 아침부터 길거리에서 이런 일을 당할 줄은 몰랐다.)" id c05_t_0219
    
    "예전에 던전에서 목숨을 잃을 뻔한 경험 다음으로 무서운 사건이었다." id c05_t_0220
        
    "몸은 비교적 멀쩡했지만, 혼이 쏙 빠져나간 기분이었다." id c05_t_0221

    camera :
        ease 0.3 ypos -15
        ease 0.4 ypos 15
        ease 0.3 ypos 0
    
    "[pl_name][josa_eun_neun] 천천히 자리에서 일어났다." id c05_t_0222

    show tiger base_am out_d
    with dissolve
    pause 0.2
    show tiger talk_am out_u
    with dissolve
    
    t "\"순찰 중인 경비대를 불렀으니 잠시만 기다려주게. 인계가 끝나면, 내가 가게까지 호위하도록 하지.\"" id c05_t_0223

    show tiger base_am out_d
    with dissolve
    
    "[pl_name][josa_eun_neun] 엘레드의 말을 듣고도 멍하니 있었다." id c05_t_0224

    show tiger talk_am out_u
    with dissolve
    
    t "\"[pl_name]?\"" id c05_t_0225

    show tiger base_am
    with dissolve
    
    c talk "\"아, 어, 네.\"" id c05_t_0226

    show tiger sad3_am
    with dissolve
    
    "얼빠진 [pl_name]의 반응에 엘레드는 착잡한 표정을 지었다." id c05_t_0227

    show tiger talk_am out_u
    with dissolve

    t "\"무슨 일이 있었던 건가?\"" id c05_t_0228

    show tiger base_am out_d
    with dissolve
    
    "[pl_name][josa_eun_neun] 어떻게 말해야 할지 잠깐 고민했다." id c05_t_0229

    c "\"시장에서 저 용병들이 먼저 말을 걸면서 누군가를 보러 가자고 했어요.\"" id c05_t_0230

    c "\"저를 데려가는 대가로 돈을 받는 것 같은데, 뭔가 수상해서 거절했더니 갑자기...\"" id c05_t_0231

    show tiger talk_am out_u
    with dissolve
    
    t "\"알겠네. 더 자세한 건 저들을 조사해 봐야겠군.\"" id c05_t_0232

    show tiger base_am out_d
    with dissolve
    
    "[pl_name][josa_eun_neun] 고개를 끄덕이고는, 떨어진 가방을 주웠다. 겉의 흙먼지를 툭툭 털고 속을 들여다봤다." id c05_t_0233
    
    c sigh "(아... 빈 병은 안 깨졌는데, 감자에 흠집이 생겼네.)" id c05_t_0234
    
    "뒤늦게 찾아온 스트레스에 [pl_name][josa_eun_neun] 머리가 아파졌다. 엘레드가 구해주지 못했다면, 정말로 납치를 당할 뻔했다." id c05_t_0235
    
    c talk "\"하필이면 가헬에게 가게를 맡기고 나온 때에 이런 일이... 당분간은 가헬이랑 붙어 다니면서 조심해야겠어요.\"" id c05_t_0236
    
    c base "(그리고... 혹시 모르니 괜찮은 호신 도구를 가지고 다녀야겠어.)" id c05_t_0237
    
    "던전도 아닌 곳에서 위험한 일을 겪었더니, [pl_name][josa_eun_neun] 불안감이 커졌다. 일회용이라도 효과가 확실한 둔화 아티팩트를 구비할 생각을 했다." id c05_t_0238

    "엘레드는 미묘하게 슬픈 표정으로 대답했다." id c05_t_0239

    show tiger sad2_am out_u
    with dissolve

    t "\"애초에 이런 일이 발생하지 않도록 해야 했으니... 경비대의 순찰을 강화하도록 지시하겠네.\"" id c05_t_0240
    t "\"델로스의 치안은 궁극적으로는 내 책임이지. 나를 탓하게나.\"" id c05_t_0241

    show tiger sad3_am out_d
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드의 표정에 약간 당황했다." id c05_t_0242

    c talk "\"아, 아닙니다. 엘레드 님이 아니었으면 더 큰 일이 날 뻔했는데, 제가 어떻게 엘레드 님을 탓하겠어요.\"" id c05_t_0243

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (140, -190)
    show tiger sigh_am
    with dissolve
    
    "엘레드는 작게 한숨을 쉬고는 대답했다." id c05_t_0244

    show tiger sad2_am out_u
    with dissolve

    t "\"하... 이렇게라도 자네를 구할 수 있어서 다행이군.\"" id c05_t_0245

    t "\"음, 정말로 다친 곳은 없나? 함께 치유사를 보러 가는 게 좋지 않겠나?\"" id c05_t_0246

    show tiger sad3_am out_d
    with dissolve

    c ddam2 "(나 그렇게까지 상태가 안 좋아 보이나? 피도 안 나는데...)" id c05_t_0247

    "[pl_name][josa_eun_neun] 엘레드가 자신을 과하게 걱정하는 것 같아서 살짝 머쓱해졌다." id c05_t_0248

    c talk "\"괜찮습니다.\"" id c05_t_0249

    show tiger at nod

    "엘레드는 작게 고개를 끄덕였다." id c05_t_0250

    show tiger talk_am out_u
    with dissolve

    t "\"저 자들은 엄중한 벌을 받게 될걸세. 자네가 안심하고 다닐 수 있도록 내가 최선을 다하겠네.\"" id c05_t_0251

    show tiger base_am
    with dissolve
    pause 0.2
    show tiger fight_am out_d
    with dissolve

    "엘레드의 말은 평소와 다르게 무게감이 있었다. 엘레드는 심각한 표정으로 경비대의 순찰과 범죄자 조사에 대해 생각했다." id c05_t_0252
    "[pl_name][josa_eun_neun] 엘레드의 어른스러운 모습이 낯설게 느껴졌다." id c05_t_0253

    c base "(노골적인 추파만 너무 많이 봐서 그런가? 이런 진지한 모습... 처음 보는 것 같네.)" id c05_t_0254

    "[pl_name][josa_eun_neun] 엘레드가 단숨에 용병들을 제압한 것을 떠올리며, 한 가지 질문을 꺼냈다." id c05_t_0255

    show tiger base_am
    with dissolve

    menu :
        "마법에 관해 물어본다." :

            $ display_text = _("엘레드 이해도 변화")
            show screen affection_indicator

            "[pl_name][josa_eun_neun] 엘레드가 쓴 마법이 궁금했다." id c05_t_0256

            c talk "\"조금 전에 망치를 휘두를 때, 어떤 마법을 쓰셨나요?\"" id c05_t_0257

            play sound "effect/boing.mp3" volume 0.9
            show question at question_move (900, -20)
            show tiger talk_am out_u
            with dissolve

            t "\"흠? 특이한 걸 물어보는군. 자네도 훈련해 볼 생각인가?\"" id c05_t_0258
            
            hide question
            show tiger base_am out_d
            with dissolve

            c "\"아, 아니요. 그냥 궁금해서...\"" id c05_t_0259

            "[pl_name][josa_eun_neun] 살짝 민망하게 웃었다. 궁금한 게 생겨서 그냥 물어봤는데, 엘레드의 대답은 예상과 조금 달랐다." id c05_t_0260

            show tiger smile_am out_u
            with dissolve
            
            t "\"어디까지 알고 싶나?\"" id c05_t_0261

            show tiger out_d
            with dissolve
            
            "의도를 확인하는 질문에, [pl_name][josa_eun_neun] 자신이 무슨 말을 했는지 깨달았다." id c05_t_0262
            "평소에 엘레드가 아무리 격식 없이 대해도, 너무 정보를 캐묻는 짓이었다." id c05_t_0263
            "[pl_name]같은 기사단 외부인에게 알려줄 리가 없었다." id c05_t_0264
            
            c ddam2 "\"그, 아닙니다.\"" id c05_t_0265

            show tiger wink_am out_u
            with dissolve

            t "\"자네가 가문의 일원이라면, 내가 직접 전수해 줄 텐데 말이지.\"" id c05_t_0266
            
            "엘레드는 윙크하며 [pl_name]의 어깨에 손을 얹었다." id c05_t_0267
            "'부부가 되면 알려주겠다'고 말한 뒤에 [pl_name]의 반응을 보고 싶었지만, 엘레드는 자신의 마음을 자제했다." id c05_t_0268
            
            c "\"죄송합니다.\"" id c05_t_0269
            
            "[pl_name]에게는 '자네가 아니었으면 봐주지 않겠다'는 뜻으로 들렸다." id c05_t_0270
            "[pl_name][josa_eun_neun] 호기심이 앞서서 괜한 말을 했다는 것을 깨닫고 민망해졌다." id c05_t_0271
            
            show tiger out_d
            with dissolve

            t "\"너무 신경 쓰지 말게.\"" id c05_t_0272

            show tiger happy2_am out_u
            with dissolve
            show tiger at talk_move
            
            "엘레드는 [pl_name]의 등을 가볍게 두드리며 웃어 보였다." id c05_t_0273


        "무기에 관해 물어본다." :
            
            # 이해도 +1
            $ tiger_understanding += 1 
            $ display_text = _("엘레드 이해도 변화")
            show screen affection_indicator

            c talk "\"엘레드 님은 망치를 쓰시는군요. 기사단장 전용 무기인가요?\"" id c05_t_0274
            
            "엘레드가 쓰는 망치는 겉보기에도 엄청나게 무거워서, 아무나 쓸 수 있는 무기는 아닌 것 같았다." id c05_t_0275
            
            show tiger talk_am out_u
            with dissolve

            t "\"음? 제식 무기가 아니긴 한데, 그렇게 대단한 물건은 아니라네.\"" id c05_t_0276

            show tiger base_am out_d
            with dissolve

            c "\"아... 저는 당연히 엘레드 님도 검이나 창을 쓰는 줄 알았어요.\"" id c05_t_0277
            
            show tiger talk_am out_u
            with dissolve

            t "\"뭐, 대부분의 기사는 그렇지. 나도 검과 창이 없는 건 아니지만...\"" id c05_t_0278
            
            show ddam at ddam_move (804,20)
            show tiger happy2_am out_d
            with dissolve

            "엘레드는 무언가 생각하다가 씁쓸한 웃음을 지었다." id c05_t_0279
            
            hide ddam
            show tiger talk_am out_u
            with dissolve
            
            t "\"만약 아버지의 인정을 받았다면, 물려받은 무구들을 사용했을걸세.\"" id c05_t_0280

            show tiger base_am out_d
            with dissolve
            
            "[pl_name][josa_eun_neun] 엘레드가 직접 가족에 대해 얘기하는 것을 처음 들었다." id c05_t_0281
            
            c "\"아버지라면, 백작님 말씀이죠?\"" id c05_t_0282
            
            "[pl_name][josa_eun_neun] 이전에 아진에게 들었던 소문을 떠올렸다. 직접 본 적은 없지만, 백작이 독한 술을 마시는 모습이 저절로 그려졌다." id c05_t_0283
            
            show tiger sad2_am out_u
            with dissolve

            t "\"그래. 나 같은 방탕한 아들과는 많이 다른... 분이라네.\"" id c05_t_0284
            
            show tiger sad3_am out_d
            with dissolve

            c base "(엘레드가 자기를 '방탕하다'고 표현하는 건 처음 봤다.)" id c05_t_0285
            c "(무슨 일이 있었던 것 같지만... 표정도 복잡해 보이고, 괜히 더 캐묻지 말자...)" id c05_t_0286
    
    show tiger base_am out_d
    with dissolve

    c question2 "\"근데 어쩌다 뒷골목에?...\"" id c05_t_0287
    
    "[pl_name][josa_eun_neun] 조금 어색하게 화제를 돌렸다." id c05_t_0288

    show tiger talk_am out_u
    with dissolve

    t "\"당연히, 오늘도 자네 가게를 찾아가는 길이었지. 이런 일이 생겨서 좀 늦어버렸지만...\"" id c05_t_0289

    show tiger base_am out_d
    with dissolve
    
    c talk "\"아, 네...\"" id c05_t_0290
    
    "엘레드는 물 흐르듯 자연스럽게 거짓말을 했다. 조금 전까지 [pl_name]의 가게 앞에서 한참 고민했다는 사실을 말해줄 수 없었다." id c05_t_0291
    "때마침 경비대가 와서, 엘레드는 범죄자를 넘겨주고 [pl_name][josa_wa_gwa] 함께 가게로 갈 수 있었다." id c05_t_0292

    stop music fadeout 2.5

label c5t_shop:
    #가게 낮 배경
    
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    # 화면에 가헬
    show wolf am_d base
    with dissolve

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c05_t_0293
    
    show wolf at surprise_move

    "가헬은 문을 열고 들어오는 [pl_name][josa_eul_reul] 보고 말을 꺼내려다가, 뒤따라 들어온 엘레드에 움찔했다." id c05_t_0294
    
    # 엘레드랑 가헬 2인화면)
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at walk (500, 1.6 , 3)
    pause 0.7
    play sound "effect/footstep.mp3" volume 0.85
    show tiger out_d base_am :
        xoffset -1500
    show tiger at walk (-500, 2.8, 6)
    pause 0.7
    
    c talk "\"좀 오래 걸렸지? 미안해.\"" id c05_t_0295
    
    show wolf am_u talk
    with dissolve

    w "\"... 무슨 일 있었나?\"" id c05_t_0296
    
    show wolf am_u base
    with dissolve

    "[pl_name][josa_i_ga] 입을 열기도 전에 엘레드가 선수를 쳤다." id c05_t_0297
    
    show tiger out_u talk_am
    with dissolve

    t "\"뒷골목에서 위험한 일이 있었지. 파렴치한 것들이 납치를 시도한 것 같네.\"" id c05_t_0298
    
    show tiger out_d base_am

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1600, 40)
    show wolf am_u bigeye
    with dissolve

    w "\"!!...\"" id c05_t_0299
    
    hide exclamation

    "가헬은 매우 놀란 듯 헛숨을 삼켰다. 엘레드와 [pl_name][josa_eul_reul] 번갈아 보고는 다급하게 말했다." id c05_t_0300
    
    show wolf talk
    with dissolve

    w "\"[pl_name], 어디 다친 곳은 없나? 어떤 놈들이지?\"" id c05_t_0301
    
    show wolf angry
    with dissolve

    c talk "\"일단 진정해. 엘레드 님 덕분에 큰 일이 되기 전에 끝났어.\"" id c05_t_0302
    
    show wolf am_d sad_am at surprise_move
    with dissolve

    "가헬은 귀가 축 처진 채로 안절부절못했다." id c05_t_0303
    
    show wolf sad2_am
    with dissolve

    w "\"그, 그런 일이... 나는... 호위 실격이다.\"" id c05_t_0304
    
    show wolf sad_am
    with dissolve

    c sigh "\"아니야. 내가 가게를 봐달라고 부탁했잖아. 이런 일이 생길 줄은 몰랐으니 어쩔 수 없지.\"" id c05_t_0305

    show tiger at nod
    
    "엘레드는 작게 고개를 끄덕이며 말했다." id c05_t_0306
    
    show tiger out_u talk_am
    with dissolve

    t "\"이미 벌어진 일은 어쩔 수 없지만, 지금부터 가게와 [pl_name][josa_eul_reul] 지키는 건 자네의 몫 아닌가.\"" id c05_t_0307
    
    show tiger out_d base_am
    with dissolve

    "가헬은 심호흡한 뒤에야 진정했다." id c05_t_0308
    
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (350, -200)
    show wolf sigh
    with dissolve
    pause(1)
    show wolf am_u talk
    with dissolve

    w "\"... 알겠습니다.\"" id c05_t_0309
    
    hide sigh
    show wolf base
    show tiger out_u talk_am
    with dissolve

    t "\"그 무뢰배들의 조사는 나에게 맡겨주게. 자네들이 안심할 수 있도록 최대한 빠르게 끝낼 터이니.\"" id c05_t_0310
    
    show tiger out_u wink_am
    with dissolve

    "엘레드는 평소처럼 자신만만하게 말하고 [pl_name]에게 윙크했다." id c05_t_0311
    
    show tiger out_d base_am
    with dissolve

    c talk "\"부탁드립니다.\"" id c05_t_0312
    
    "[pl_name][josa_i_ga] 고개를 숙이자, 엘레드는 웃으며 말했다." id c05_t_0313
    
    show tiger laugh_am    
    with dissolve

    t "\"당연히 해야 할 일이니, 고개 숙이지 말게나.\"" id c05_t_0314

    show tiger talk_am
    with dissolve

    t "\"그럼, 이른 시일 내로 돌아오도록 하지.\"" id c05_t_0315
    
    show tiger out_d base_am at mirror
    with dissolve
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk (-1500, 3.0, 5)
    pause(2.0)
    play sound "audio/effect/bell.mp3" volume 0.685

    "엘레드가 나가고 가게의 분위기는 무겁게 가라앉았다." id c05_t_0316

    hide wolf
    show wolf am_d base
    with dissolve

    "가헬은 큰 한숨을 쉬었다." id c05_t_0317
    
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-120, -200)
    show wolf sigh 

    w "\"하아... 오늘부터 불침번을 서야겠군.\"" id c05_t_0318
    
    c question2 "\"잠을 안 자고 버틴다고? 보안 마법이 시끄럽게 깨울 테니까 너무 무리하지 않아도 돼.\"" id c05_t_0319
    
    show wolf am_u talk
    with dissolve

    w "\"보안 마법이 잘 작동하는지 확인해 보겠다. 창문마다 빠짐없이 걸려있겠지?\"" id c05_t_0320
    
    show wolf am_d base
    with dissolve

    c consider "\"응. 그래도 잠은 제대로 자는 게 좋아. 낮에 졸리면 밤새우는 게 의미가 없으니까...\"" id c05_t_0321
    
    "가헬은 고민하다가 대답했다." id c05_t_0322
    
    show wolf am_u talk at surprise_move

    w "\"음... 복도에 앉아서 얕은 잠을 자도 충분하다.\"" id c05_t_0323
    
    show wolf am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 가헬의 강한 의지에 결국 고개를 끄덕였다." id c05_t_0324
    
    c talk "\"그래... 그러면, 당분간은 부탁할게.\"" id c05_t_0325
    
    scene bg shop with Fade(0.8, 0.8, 0.8)

    "{i}며칠 뒤{/i}" id c05_t_0326
    
    "걱정과 다르게, 별다른 일 없이 하루하루가 지나갔다." id c05_t_0327
    "가헬은 항상 신경을 곤두세우고 경계하느라 말수가 더 줄어들었다." id c05_t_0328
    "[pl_name]의 긴장이 아주 조금 느슨해질 때쯤, 엘레드가 가게를 찾아왔다." id c05_t_0329
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c05_t_0330

    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger am_d base_am :
        xoffset -1500
    show tiger at walk (0, 2.8, 6)
    pause(2.8)
    
    show tiger am_u talk_am
    with dissolve

    t "\"좋은 소식과 나쁜 소식이 있네.\"" id c05_t_0331

    t "\"좋은 소식은 이제 자네가 안심해도 좋다는 것이고...\"" id c05_t_0332

    show tiger sad2_am
    with dissolve

    t "\"나쁜 소식은 이 사건을 완전히 뿌리 뽑지 못했다는 것이라네.\"" id c05_t_0333
    
    show tiger am_d base_am
    with dissolve

    c talk "\"그래도 조사해 주셔서 감사합니다.\"" id c05_t_0334
    
    "엘레드는 목을 가다듬고 가져온 문서를 읽으며 말했다." id c05_t_0335
    
    show tiger am_u talk_am
    with dissolve

    $ unlock_info_tag(4, "4")
    $ display_text = _("정보 : 강철손 상회2")
    show screen affection_indicator
    
    t "\"그놈들은 {color=#ee3939}'강철손 상회'{/color}에서 고용한 용병이었네.\"" id c05_t_0336
    t "\"자네처럼 연금술이나 다른 기술이 있는 자를 납치해서 제공하고 돈을 받았다고 하는군.\"" id c05_t_0337
    t "\"상회 위치도 금방 자백한 덕분에, 바로 급습 작전을 시작했지.\"" id c05_t_0338
    
    show tiger am_d base_am
    with dissolve

    c question2 "\"네? 벌써 그 정도까지 진행됐나요?\"" id c05_t_0339
    
    "[pl_name][josa_eun_neun] 살짝 놀라며 말했다. 생각보다 훨씬 빠르게 일이 진행되고 있었다." id c05_t_0340

    show tiger at nod

    "엘레드는 작게 고개를 끄덕였다." id c05_t_0341
    
    show tiger am_u talk_am
    with dissolve

    t "\"이미 끝났다고 볼 수 있지.\"" id c05_t_0342
    t "\"하지만 방금 말했듯이, 완벽하게 마무리 짓지는 못했다네. 어느 정도 습격에 대비하고 있었던 모양이야.\"" id c05_t_0343
    t "\"건물에 갇혀있던 장인들은 모두 구출했으나, 간부로 보이는 놈 하나는 결국 탈출해 버렸네.\"" id c05_t_0344
    
    show tiger am_d base_am
    with dissolve

    c ddam2 "\"그래도 다들 무사하다니 다행이네요.\"" id c05_t_0345
    
    "[pl_name][josa_eun_neun] 침을 꿀꺽 삼켰다. 붙잡혔던 장인들은 말 그대로 노예처럼 생활했을 것이다." id c05_t_0346
    "자신도 비슷한 처지가 되었을지도 모른다고 생각하니 등골이 서늘했다." id c05_t_0347
    
    c consider "\"그렇게 장인을 모아서 무엇을 했던 건가요?\"" id c05_t_0348
    
    show tiger am_u sad3_am at surprise_move

    "엘레드는 조금 곤란한 표정으로 어깨를 으쓱했다." id c05_t_0349
    
    show tiger talk_am
    with dissolve

    t "\"뭔가 금지된 마법에 대해 연구했던 것 같다네. 중단시켜서 다행인 일이지.\"" id c05_t_0350
    
    t "\"마탑에서도 이 조직을 주시하던 모양인데... 기사단이 선수 쳐서 자료를 뺏어갔다고 생각하더군.\"" id c05_t_0351
    
    show tiger am_d base_am
    with dissolve

    c consider "(금지된 마법? 굳이 장인을 모았다는 건, 뭔가를 만들었다는 건데...)" id c05_t_0352
    
    c "(금지된... 무기 같은 걸까? 조금 궁금하네.)" id c05_t_0353
    
    "[pl_name][josa_eun_neun] 그 자료를 한번 읽어보고 싶었지만, 당연히 입 밖으로 꺼낼 수는 없었다. " id c05_t_0354
    
    show tiger am_u talk_am
    with dissolve

    t "\"마탑을 상대하는 건 나보다는 대공님이 전문가이시니, 그쪽으로 자료를 넘겨드렸네.\"" id c05_t_0355
    
    show tiger am_d base_am
    with dissolve

    "[pl_name]도 몇 번 들었던 얘기지만, 귀족과 마탑 사이에는 깊은 갈등이 있었다. 아무리 엘레드라도 혼자서는 어떻게 할 수 없는 영역이었다." id c05_t_0356
    
    c talk "\"그랬군요. 여러모로 신경 써주셔서 정말 감사합니다.\"" id c05_t_0357
    
    "[pl_name][josa_i_ga] 고개를 꾸벅 숙이자, 엘레드는 언제나처럼 크게 웃었다." id c05_t_0358
    
    show tiger am_d laugh_am at surprise_move

    t "\"크하하하! 이 정도는 당연한 일이지.\"" id c05_t_0359
    
    show tiger am_u talk_am
    with dissolve

    t "\"뭐, 우중충한 얘기는 여기까지라네.\"" id c05_t_0360


    hide tiger
    with dissolve
    show tiger am_d base_am at left
    show wolf out_d base at right
    with dissolve
        
    "그동안 잠자코 이야기를 듣고 있던 가헬도 엘레드에게 고개를 숙였다." id c05_t_0361
    
    show wolf out_u talk
    with dissolve

    w "\"감사합니다.\"" id c05_t_0362
    
    show wolf out_d base
    show tiger am_u talk_am
    with dissolve

    t "\"그래. 자네도 고생했네.\"" id c05_t_0363
    
    show tiger am_d base_am
    with dissolve

    "며칠 동안 계속 날을 세우고 있어서 그런지, 가헬의 표정은 평소보다도 딱딱하게 굳어있었다." id c05_t_0364
    
    c smile "\"이제 마음 놓고 잘 수 있겠네.\"" id c05_t_0365
    
    show wolf talk
    with dissolve

    w "\"그래...\"" id c05_t_0366
    
    show wolf base
    with dissolve

    c consider "(내색하지 않았지만, 가헬도 엄청 힘들었겠지.)" id c05_t_0367
    
    c talk "\"그러면 내일은 가게를 쉴까? 휴일이랑 이어서 이틀 푹 쉬자.\"" id c05_t_0368
    
    c "\"너도 술집에 간다거나, 뭐 아무튼 제대로 쉬고 와.\"" id c05_t_0369
    
    show wolf out_u talk
    with dissolve

    w "\"알았다.\"" id c05_t_0370
    
    # 가헬 2층으로)
    show wolf out_d base at mirror
    with dissolve
    pause(0.5)
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 2.8 , 5)

    "가헬은 우선 옷부터 갈아입기 위해 2층으로 올라갔다." id c05_t_0371

    hide wolf
    show tiger am_u talk_am
    with dissolve

    t "\"나도 슬슬 가야겠군.\"" id c05_t_0372
    
    show tiger base_am
    with dissolve

    "엘레드는 가게에서 나가려다가 갑자기 생각난 게 있었다." id c05_t_0373
    
    show tiger am_u talk_am at talk_move
    
    t "\"참, 전에 말했던 물약 구매 건을 기억하나?\"" id c05_t_0374
    
    show tiger base_am
    with dissolve

    c talk "\"아, 네.\"" id c05_t_0375
    
    show tiger talk_am
    with dissolve

    t "\"자네만 괜찮으면 진행하고 싶지만, 지금 당장은 쉬어야 하지 않겠나?\"" id c05_t_0376
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 잠깐 고민하다가 대답했다." id c05_t_0377
    
    c consider "\"음... 재료도 구해야 하니, 시간이 필요하긴 합니다. 어느 정도 규모인지 알 수 있을까요?\"" id c05_t_0378
    
    show tiger am_u talk_am
    with dissolve

    t "\"회복 물약은 물론이고, 상비약으로 쓸 연고나 강장제도 필요하지.\"" id c05_t_0379

    show tiger wink_am
    with dissolve

    t "\"자네가 만들 수 있다면 다른 것도 주문하고 싶군.\"" id c05_t_0380
    
    show tiger am_d base_am
    with dissolve

    c talk "\"그러면 잠시만요...\"" id c05_t_0381
    
    "[pl_name][josa_eun_neun] 빈 종이를 꺼내서 품목과 수량을 받아적기 시작했다." id c05_t_0382
    
    c talk "\"강화약은 효과가 큰 것과 오래 지속되는 것, 두 종류가 있습니다.\"" id c05_t_0383
    
    show tiger am_u talk_am
    with dissolve

    t "\"지속시간이 긴 걸로 하지.\"" id c05_t_0384
    
    show tiger am_d base_am
    with dissolve
    pause(0.5)

    # 가헬 기본복장 다시 걸어오기)
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf am_d base :
        xoffset 1500
    show wolf at walk (500, 2.8, 6)
    
    "가헬은 열심히 대화하는 [pl_name][josa_wa_gwa] 엘레드를 보고 멈칫했다. " id c05_t_0385
    
    show wolf at surprise_move

    w "(일하는데 방해가 되지 않게 조용히 있어야겠군...)" id c05_t_0386
    
    scene bg shop with Fade(0.8, 0.8, 0.8)

    "{i}잠시 후{/i}" id c05_t_0387

    show tiger am_u talk_am
    with dissolve

    t "\"이 정도면 충분한 것 같네. 다 만드는 데 얼마나 걸릴 것 같나?\"" id c05_t_0388
    
    show tiger am_d base_am
    with dissolve

    c consider "(오늘내일 쉬고, 던전에 갔다가, 재료 손질하고, 제작하면...)" id c05_t_0389
    
    "[pl_name][josa_eun_neun] 손가락을 하나씩 접으며 일정을 예상했다." id c05_t_0390
    
    c talk "\"7, 8일 정도 걸릴 겁니다. 급하게 필요하시다면 하루 정도는 앞당길 수 있는데-\"" id c05_t_0391
    
    show tiger am_u talk_am
    with dissolve

    t "\"아니, 그 정도면 충분히 빠르군.\"" id c05_t_0392
    
    show tiger base_am
    with dissolve

    "엘레드는 가볍게 손을 저으며 [pl_name][josa_eul_reul] 만류했다." id c05_t_0393
    
    show tiger talk_am
    with dissolve

    t "\"음... 상품은 궤짝에 보관하나?\"" id c05_t_0394
    
    show tiger am_d base_am
    with dissolve

    c talk "\"네. 이 정도면 상자 4개 정도 분량입니다.\"" id c05_t_0395
    
    "엘레드는 귀를 팔랑거리며 무언가를 고민하다가 말했다." id c05_t_0396
    
    show tiger am_u smile_am at surprise_move

    t "\"그럼 기사단에서 마차를 보내주겠네. 상품과 함께 본부로 와 주겠나?\"" id c05_t_0397
    
    c smile "\"네, 알겠습니다.\"" id c05_t_0398
    
    "[pl_name][josa_eun_neun] 가볍게 고개를 끄덕이며, 큰 거래가 성사된 것에 미소를 지었다." id c05_t_0399

    stop music fadeout 2.5

label c5t_order:

    scene bg shop with Fade(0.8, 0.8, 0.8)

    "{i}일주일 뒤{/i}" id c05_t_0400

    "목표가 생기자, 시간은 빠르게 흘러갔다." id c05_t_0401
    "가헬과 던전에 가서 재료를 모으고, 가게 영업도 하면서 물약을 만드느라 정신없이 보냈다." id c05_t_0402
    "평범한 일상이 소중하다는 걸 다시금 깨닫는 시간이었다." id c05_t_0403

    # 기사단 본부 배경

    scene bg knights_templar with Fade(0.8, 0.8, 0.8)
    play music "audio/the-long-way-home-259747.mp3" volume 0.6 fadein 1.0

    "상품을 실은 마차와 함께, [pl_name][josa_eun_neun] 기사단의 본부에 도착했다." id c05_t_0404
    "기사단 본부는 슬쩍 봐도 굉장히 세련된 건축물이었다. 한눈에 다 들어오지 않을 정도로 넓고 높았다." id c05_t_0405
    "[pl_name][josa_eun_neun] 마차에서 내리려고 일어섰다." id c05_t_0406
    
    play sound "effect/putdown.mp3" volume 0.9
    "{i}달칵!{/i}" id c05_t_0407
    
    show cara out_u talk
    with dissolve

    c "\"아, 감사합니다.\"" id c05_t_0408
    
    show cara out_d base
    with dissolve

    "한발 먼저 마차 문을 열어주는 기사 때문에 [pl_name][josa_eun_neun] 약간 놀랐다. 이런 대접을 받는 것은 처음이었다." id c05_t_0409
    
    show cara consider
    with dissolve

    c "(규율이 원래 이런가? 기사단의 품격을 보여주는 건가?)" id c05_t_0410
    
    show cara base
    with dissolve

    "엘레드를 제외하면 기사를 볼 일이 많지 않았기에, [pl_name][josa_eun_neun] 기사들의 질서 잡힌 모습을 그저 바라만 보았다." id c05_t_0411
    
    "머리로 아는 것과 실제로 보는 것은 역시 차이가 있었다." id c05_t_0412

    knight "\"보급품은 저희가 들겠습니다.\"" id c05_t_0413

    show cara talk at talk_move
    
    c "\"감사합니다.\"" id c05_t_0414
    
    show cara base
    with dissolve

    "기사의 말에 [pl_name][josa_eun_neun] 다시 고개를 숙였다. 기사들이 무거운 궤짝을 하나씩 들고 떠났다." id c05_t_0415
    
    knight2 "\"단장님이 기다리고 계십니다. 따라오시죠.\"" id c05_t_0416
    
    show cara talk
    with dissolve

    c "\"네.\"" id c05_t_0417
    
    show cara base
    with dissolve

    "[pl_name][josa_eun_neun] 기사의 안내에 따라 건물 안으로 들어갔다." id c05_t_0418

    # 엘레드 집무실 배경
    scene bg office with Fade(0.8, 0.8, 0.8)
    
    play sound "effect/door_knock_weak.mp3" volume 0.9
    "{i}똑똑{/i}" id c05_t_0419
    
    knight2 "\"단장님, 손님을 모셔 왔습니다.\"" id c05_t_0420
    
    t talk_am "\"들어오게.\"" id c05_t_0421
    
    "[pl_name][josa_i_ga] 집무실 안으로 들어가자, 의자에 앉아 있던 엘레드는 자리에서 벌떡 일어났다." id c05_t_0422

    show tiger am_u talk_am
    with dissolve

    t "\"[pl_name], 드디어 왔군.\"" id c05_t_0423
    
    show tiger am_d base_am
    with dissolve

    "따뜻한 햇빛이 들어오는 엘레드의 집무실은 이런저런 장식물과 가구로 조화롭게 보였다." id c05_t_0424
    "엘레드의 자리는 큰 책상과 좋은 재질의 의자가 있었고, 손님용 소파와 작은 책상이 옆에 준비되어 있었다." id c05_t_0425
    "기사단을 상징하는 깃발과 세련된 조각상은 고풍스럽게 보이고, 전시용 무구는 새것처럼 광이 났다." id c05_t_0426
    
    c talk "\"안녕하세요.\"" id c05_t_0427
    
    show tiger am_u talk_am
    with dissolve

    t "\"자네는 차를 가져오게.\"" id c05_t_0428
    
    show tiger am_d base_am
    with dissolve

    knight2 "\"넵.\"" id c05_t_0429
    
    "[pl_name][josa_eul_reul] 안내한 기사는 엘레드에게 경례하고 방에서 나갔다." id c05_t_0430
    "문이 닫히자, [pl_name][josa_eun_neun] 조금 어색하게 입을 열었다." id c05_t_0431
    
    c talk "\"주문하신 상품은 모두 전달했습니다.\"" id c05_t_0432

    show tiger am_u smile_am
    with dissolve

    t "\"그래, 그래. 일단 여기 앉게.\"" id c05_t_0433
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 손님용 소파에 앉아 주변을 살짝 둘러봤다." id c05_t_0434
    "평범한 '기사단장의 방' 그대로라서 오히려 조금 신기했다. 엘레드라면 조금 특이한 점이 있을 것으로 생각했었다." id c05_t_0435
    
    show tiger am_u talk_am
    with dissolve

    t "\"크흠, 대금은 여기 있네.\"" id c05_t_0436

    show tiger am_d base_am
    with dissolve

    c smile "\"감사합니다.\"" id c05_t_0437
    
    "[pl_name][josa_eun_neun] 엘레드가 건네준 묵직한 주머니를 받아서 확인했다." id c05_t_0438
    "반짝거리는 금화는 보기만 해도 마음을 풍족하게 만들었다. [pl_name][josa_eun_neun] 금화 주머니를 가방에 소중하게 넣어놓았다." id c05_t_0439
    
    show tiger am_u talk_am
    with dissolve

    t "\"자네 덕분에 보급 걱정을 덜었군. 정말로 고맙네.\"" id c05_t_0440
    
    show tiger am_d base_am
    with dissolve

    c talk "\"아, 아닙니다.\"" id c05_t_0441
    
    "엘레드는 살짝 긴장한 [pl_name][josa_eul_reul] 보고 평소처럼 능글맞은 윙크를 날렸다." id c05_t_0442
    
    show tiger wink_am
    with dissolve

    t "\"지금은 차 한잔하면서, 느긋하게 얘기라도 하지.\"" id c05_t_0443
    
    c ddam "(... 평소랑 완전 똑같잖아?)" id c05_t_0444
    
    "[pl_name][josa_eun_neun] 조금 황당했지만, 오히려 마음이 약간 편해졌다." id c05_t_0445
    
    show tiger base_am
    with dissolve

    play sound "effect/door_knock_weak.mp3" volume 0.9
    "{i}똑똑{/i}" id c05_t_0446
    
    "문이 열리면서 향긋한 차의 냄새가 공기 중에 퍼졌다." id c05_t_0447

    # 테오 등장
    hide tiger
    with dissolve
    show tiger at left
    show theo at right
    with dissolve

    "찻잔을 들고 방에 들어온 기사는 검은 털의 개 수인이었다." id c05_t_0448

    show tea
    with dissolve
    play sound "effect/putdown.mp3" volume 0.8

    "기사는 엘레드와 [pl_name] 앞에 차를 내려놓고 말했다." id c05_t_0449

    hide tea
    show theo talk am_u
    with dissolve     
    
    th "\"반슈타인 기사단에 오신 것을 환영합니다.\"" id c05_t_0450

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (400, -45)
    show tiger am_u talk_am
    show theo base am_d
    with dissolve

    t "\"테오? 어쩌다 자네가 왔나?\"" id c05_t_0451
    
    hide question
    show tiger am_d base_am
    with dissolve
    show theo at talk_move

    "테오라고 불린 기사는 작게 어깨를 으쓱했다." id c05_t_0452

    show theo talk am_u
    with dissolve 

    th "\"다들 서로 가겠다는 걸 말리고 왔습니다.\"" id c05_t_0453

    show tiger am_u talk_am
    show theo base am_d
    with dissolve
    
    t "\"녀석들도 참, 부단장이 나서게 만들다니...\"" id c05_t_0454
    
    show tiger am_d base_am
    with dissolve

    c ddam2 "(부단장?!)" id c05_t_0455
    
    "[pl_name][josa_eun_neun] 찻잔을 잡으려다가 눈치를 봤다. 한가롭게 차나 마실 상황이 아니었다." id c05_t_0456
    
    show theo talk am_u
    with dissolve

    th "\"견습 기사면 아직 그럴 나이 아니겠습니까?\"" id c05_t_0457
    th "\"... '손님'이 궁금한 건 저도 마찬가지고.\"" id c05_t_0458

    show theo smile
    with dissolve
    
    "테오는 [pl_name] 쪽을 보며 살짝 미소를 지었다." id c05_t_0459
    
    show tiger am_u talk_am
    show theo base
    with dissolve

    t "\"소개가 늦었군. 이쪽은 이번에 계약한 상인, [pl_name][josa_ida_da].\"" id c05_t_0460
    t "\"[pl_name], 우리 기사단의 부단장 테오도르 바토르칸이라네.\"" id c05_t_0461

    show tiger am_d base_am
    with dissolve

    play channel1 "effect/cloth.mp3" volume 0.6
    pause 0.7

    camera :
        ease 0.35 ypos 30
        ease 0.35 ypos 0
    pause 0.7

    "[pl_name][josa_eun_neun] 자리에서 일어나 예법을 차려 인사했다." id c05_t_0462
    
    c talk "\"처음 뵙겠습니다.\"" id c05_t_0463

    show theo smile am_u
    with dissolve
    
    th "\"안녕하십니까. 편히 계십시오.\"" id c05_t_0464

    show theo am_d
    with dissolve
    show theo :
        ease 0.35 yoffset 30
        ease 0.35 yoffset 0
    pause 0.7
    
    "테오는 부드럽게 웃으며 [pl_name]에게 마주 인사했다." id c05_t_0465

    "그리고 갑자기 표정을 바꾸며, 엘레드를 못마땅하게 바라봤다." id c05_t_0466

    show theo disapprove am_u
    with dissolve
    
    th "\"단장님, 보급 계획에 사심이 반영된 것 같습니다만?\"" id c05_t_0467

    show theo am_d
    with dissolve
    
    "엘레드는 능글맞은 웃음으로 받아쳤다." id c05_t_0468
    
    show tiger am_u smile_am
    with dissolve

    t "\"무슨 말인지 모르겠군. [pl_name][josa_eun_neun] 실력이 확실한 연금술사라네.\"" id c05_t_0469
    
    show tiger am_d base_am
    with dissolve

    c consider "(원래는 다른 계획이 있었나? 나 때문에 엘레드가 무슨 짓을 했나?...)" id c05_t_0470
    
    "[pl_name][josa_eun_neun] 둘의 눈치를 보느라 차에는 손도 대지 못하고 가만히 있었다." id c05_t_0471
    
    show theo disapprove am_u
    with dissolve

    th "\"... 그런 거로 알겠습니다.\"" id c05_t_0472

    show theo base am_d
    with dissolve
    show theo at surprise_move
    show theo at mirror
    with dissolve
    show theo at walk (1500, 2.8, 4)
    pause 2.8
    
    "테오는 그 말을 끝으로 경례와 함께 방에서 나갔다." id c05_t_0473

    play sound "effect/putdown.mp3" volume 0.8

    "그제야 [pl_name][josa_eun_neun] 찻잔을 들어 올릴 수 있었다." id c05_t_0474
    "아주 조금 마셔봤지만, 너무 뜨거워서 무슨 맛인지 잘 알 수 없었다." id c05_t_0475
    
    c talk "\"저, 방금 부단장님이 하신 말은...\"" id c05_t_0476

    show tiger at walk (0, 2, 3)
    pause 2
    show tiger am_u talk_am
    with dissolve

    t "\"너무 신경 쓰지 말게.\"" id c05_t_0477
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드를 바라보았다." id c05_t_0478
    "아까와 똑같이 뻔뻔한 얼굴이지만, 엘레드는 결국 [pl_name]의 시선을 피했다." id c05_t_0479
    
    show tiger am_u embarrass_am
    with dissolve

    t "\"뭐, 자네와 친분이 반영된 것은 어느 정도 사실이긴 하지만...\"" id c05_t_0480

    show tiger am_u talk_am
    with dissolve

    t "\"그래도 합리적인 결정이었네. 마탑 소속 연금술사와 협상으로 시간을 보내는 것보다 훨씬 현명한 선택이지.\"" id c05_t_0481
    
    show tiger am_d base_am
    with dissolve

    c question2 "\"마탑과도 거래하시나요?\"" id c05_t_0482
    
    "엘레드는 차를 한 모금 마시고 대답했다." id c05_t_0483
    
    show tiger am_u talk_am
    with dissolve

    t "\"절대 안 할 수는 없지. 하지만 가능하면 안 하고 싶다네.\"" id c05_t_0484
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 귀족과 마탑 사이 갈등의 원인이 궁금해졌다. 꽤 오래된 갈등일 테니 간단한 이유는 아닐 것이다." id c05_t_0485
    
    c consider "\"마탑... 음.\"" id c05_t_0486
    
    "[pl_name][josa_eun_neun] 섣불리 질문을 꺼내지 못하고 고민했다. 귀족도 마탑도 잘 알지 못하는 입장에서 뭐라고 말하기 어려웠다." id c05_t_0487
    
    show tiger am_u talk_am
    with dissolve

    t "\"지금이라 할 수 있는 얘기지만, 처음에는 자네도 마탑 소속이 아닌지 의심했다네.\"" id c05_t_0488

    show tiger am_d base_am
    with dissolve
    
    c talk "\"아... 소속은 아니지만, 마탑의 공증을 받았죠.\"" id c05_t_0489
    
    "[pl_name][josa_eun_neun] 바토를 떠올리며 고개를 끄덕였다." id c05_t_0490
    
    show tiger am_u talk_am
    with dissolve

    t "\"그래. 자네의 '친구' 덕분이겠지.\"" id c05_t_0491
    
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 살짝 놀라서 되물었다." id c05_t_0492

    c exclamation "\"!... 바토를 아세요?\"" id c05_t_0493
        
    show tiger am_u talk_am
    with dissolve

    t "\"흠... 그 도련님과 이렇다 할 친분이 있는 사이는 아니라네.\"" id c05_t_0494
    t "\"자네의 가게가 마탑과 관련이 있나 궁금해서 알아본 것이지.\"" id c05_t_0495

    show tiger am_d base_am
    with dissolve
    
    c talk "\"그랬군요.\"" id c05_t_0496
    
    c consider "(맨날 나한테 플러팅하려고 가게에 온 게 아니었나? 엘레드의 원래 의도는 달랐던 모양이네...)" id c05_t_0497
    
    "[pl_name][josa_eun_neun] 적당히 식은 차를 한 모금 마셨다." id c05_t_0498
    "꿀을 넣었는지 아주 은은한 단맛이 느껴졌다. 고급 차에 대해서 잘 모르지만, 일반적으로 마시는 차는 아닌 것 같았다." id c05_t_0499
    
    play sound "effect/putdown.mp3" volume 0.9
    camera :
        ease 0.2 ypos 15
        ease 0.3 ypos -15
        ease 0.2 ypos 0
    pause 0.5

    c question2 "\"음?\"" id c05_t_0500
    
    "신발 밑에 뭔가 밟히는 게 있었다." id c05_t_0501
    "아래를 슬쩍 내려다보자 반짝거리는 돌멩이 같은 것이 있었다." id c05_t_0502
    "[pl_name][josa_eun_neun] 그것을 주워서 살펴보았다. 보석 같긴 한데 뭐라고 표현하기 힘든 기묘한 색이었다." id c05_t_0503

    show rainbowstone :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    c talk "\"이건...\"" id c05_t_0504
    
    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1090, 20)
    show tiger am_u talk_am

    t "\"그, 그건 어디서 찾았나?\"" id c05_t_0505

    "엘레드는 [pl_name][josa_i_ga] 들고 있는 것을 보고 움찔했다." id c05_t_0506

    hide exclamation
    with dissolve
    
    c talk "\"여기 바닥에 떨어져 있었습니다.\"" id c05_t_0507
    
    hide rainbowstone
    with dissolve
    
    "엘레드는 바닥을 내려다봤다가 갑옷 속에 손을 넣어보고는 크게 당황했다." id c05_t_0508

    show tiger am_d embarrass_am at surprise_move
    pause(0.5)
    show tiger am_u talk_am
    with dissolve

    t "\"어?! 아, 그, 그렇군. 내가 흘린 물건이라네.\"" id c05_t_0509

    show tiger am_d base_am
    with dissolve

    c talk "\"그렇군요. 여기...\"" id c05_t_0510

    if persistent.rainbowstone_wolf == True or persistent.rainbowstone_bear == True or persistent.rainbowstone_dragon == True :
        
        "[pl_name][josa_eun_neun] 그 보석 비슷한 것을 엘레드에게 건네주려다, 갑자기 이상한 느낌이 들었다." id c05_t_0511

        c consider "(기시감... 최근에 이런 알록달록한 걸 본 적이 있었나?)" id c05_t_0512
        
        "이 정도로 특이하게 생긴 물건이면 기억에 남을 법했다. 하지만 딱히 생각나는 게 없었다." id c05_t_0513
        "[pl_name][josa_eun_neun] 엘레드의 손에 그것을 건네주면서 말했다." id c05_t_0514

        c question2 "\"근데 이건 대체 뭔가요? 왠지 익숙한 느낌인데...\"" id c05_t_0515
        
        show tiger am_u talk_am
        with dissolve
        
        t "\"이걸 본 적이 있나? 언제, 어디서?\"" id c05_t_0516
        
        show tiger am_d base_am
        with dissolve
        
        "엘레드의 진지한 질문에 [pl_name][josa_eun_neun] 식은땀을 흘렸다." id c05_t_0517
        
        c ddam2 "\"아니, 본 적은 없고... 그냥 특이해서요. 딱히 기억나는 건 없습니다.\"" id c05_t_0518
        
        show tiger sad3_am
        with dissolve
        
        t "\"아, 그런가... 으음...\"" id c05_t_0519
        
        "엘레드는 살짝 실망한 듯 맥 빠진 표정을 했다." id c05_t_0520
    else :
        
        "[pl_name][josa_eun_neun] 그 보석 비슷한 것을 엘레드에게 건네주었다." id c05_t_0521

        c question2 "\"색이 꽤 특이하네요. 무슨 보석인가요?\"" id c05_t_0522
        
        show tiger am_u talk_am
        with dissolve

        t "\"아... 보석은 아니라네.\"" id c05_t_0523

    show tiger am_d base_am
    with dissolve

    "엘레드는 잠시 고민하다가 조용히 말을 꺼냈다." id c05_t_0524
    
    show tiger am_u talk_am
    with dissolve

    t "\"이건 이전에 토벌 작전을 수행하다가 발견한 것이라네.\"" id c05_t_0525
    t "\"처음에는 꽤 흥미롭게 생겨서 이런저런 조사를 해봤지만, 결국 정체를 밝혀내지 못했다네.\"" id c05_t_0526
    
    show tiger am_d base_am
    with dissolve

    c consider "(밝혀내지 못했다고? 무슨 물질이길래...)" id c05_t_0527
    
    show tiger am_u talk_am
    with dissolve

    t "\"보고서에 따르면 부숴도 보고, 끓여도 보고, 아무튼 이것저것 많이 해봤다네. 하지만 전부 소용없었지.\"" id c05_t_0528
    t "\"아무 소득이 없으니, 조사는 잠정 중단되었다네.\"" id c05_t_0529
    
    show tiger am_d base_am
    with dissolve
    
    c talk "\"으음, 그런 일이 있었군요.\"" id c05_t_0530
    
    "엘레드는 돌조각을 잠시 바라보다가 [pl_name][josa_eul_reul] 향해 시선을 돌렸다." id c05_t_0531
    
    show tiger am_u talk_am
    with dissolve

    t "\"자네도 이게 궁금한가?\"" id c05_t_0532

    show tiger am_d base_am
    with dissolve

    c talk "\"네? 어...\"" id c05_t_0533
    
    menu :

        "흥미롭긴 한데, 별로 쓸모는 없어 보인다." :
           
            c consider "(생긴 게 조금 흥미롭기는 하지만... 기사단에서도 포기할 정도면, 별거 아니겠지...)" id c05_t_0534

            c talk "\"이미 충분히 조사하셨다고 하니, 더 궁금한 점은 없습니다.\"" id c05_t_0535
            
            show tiger at nod_big
            pause 0.4

            "엘레드는 잠시 턱을 쓰다듬으며 생각했다." id c05_t_0536

            show tiger am_u talk_am
            with dissolve

            t "\"흐음... 그럼 추가 조사는 포기해야겠군.\"" id c05_t_0537

            show tiger am_d base_am
            with dissolve
            hide tiger
            with dissolve
            play sound "effect/putdown.mp3" volume 0.8
            pause 0.5
            show tiger am_d base_am
            with dissolve
            
            "엘레드는 자리에서 일어나서, 조그만 상자에 돌조각을 집어넣고 돌아왔다." id c05_t_0538
        
        "역시 신경 쓰인다. 정보를 더 들어보고 싶다." :
            
            # 엘레드 돌 on
            $ persistent.rainbowstone_tiger = True

            c consider "(굳이 나한테 물어보는 건, 뭔가 말해주겠다는 뜻인가?)" id c05_t_0539

            c talk "\"조금 궁금하긴 합니다.\"" id c05_t_0540

            show tiger am_u talk_am
            with dissolve
            
            t "\"그럼 자네가 직접 살펴보겠나?\"" id c05_t_0541

            show tiger am_d base_am
            with dissolve
            
            c talk "\"아, 그래도 될까요?\"" id c05_t_0542

            show tiger am_u
            with dissolve
            
            "엘레드는 대답 대신 손을 내밀었다." id c05_t_0543

            show tiger am_d
            with dissolve
            
            "[pl_name][josa_eun_neun] 냉큼 돌조각을 받아서 들었다. 햇빛을 받아서 여러 가지 색으로 빛나는 게 꽤 신비로웠다." id c05_t_0544
            
            "[pl_name][josa_eun_neun] 돌을 이리저리 둘러보며 말했다." id c05_t_0545

            c question2 "\"당연하겠지만, 마력에 반응은 없었죠?\"" id c05_t_0546
            
            show tiger am_u talk_am
            with dissolve

            t "\"그렇다네.\"" id c05_t_0547

            show tiger am_d base_am
            with dissolve
            
            "[pl_name][josa_eun_neun] 가볍게 마나를 불어넣어 보았다." id c05_t_0548

            c consider "(반응은커녕, 마나가 잔류하는 느낌도 없네. 그냥 돌멩이 같은데...)" id c05_t_0549

            "[pl_name][josa_eun_neun] 다른 질문을 꺼내려고 했으나, 엘레드가 움찔하며 먼저 말했다." id c05_t_0550
            
            play sound "effect/ping.mp3" volume 0.75
            show exclamation at exclamation_move (1090, 20)
            show tiger am_u talk_am at surprise_move

            t "\"자, 자네! 그거, 녹아내리고 있다네!\"" id c05_t_0551
            
            hide exclamation
            show tiger fight_am am_d
            with vpunch

            c ddam2 "\"에? 어? 우왓?!\"" id c05_t_0552
            
            "[pl_name]의 손안에서 돌이 녹아내리고 있었다. 기묘한 얼룩으로 변한 그것은, 온갖 색의 잉크를 섞어서 뿌린 것처럼 흘러내렸다." id c05_t_0553
            
            c ddam2 "\"이, 이게 무슨 일이지?\"" id c05_t_0554
            
            "[pl_name][josa_eun_neun] 서둘러 찻잔에라도 액체를 담으려고 했으나, 정작 돌-액체는 [pl_name]의 털 속으로 파고들었다." id c05_t_0555
            "몸에 흡수되는 것 처럼 돌조각은 순식간에 사라졌다. 예상치 못한 상황에 [pl_name][josa_eun_neun] 크게 당황해서 굳어버렸다." id c05_t_0556
            
            show tiger fight2_am am_u at surprise_move

            t "\"[pl_name]? 자네, 괜찮나?\"" id c05_t_0557

            show tiger fight_am am_u
            with dissolve
            
            c talk "\"어... 괜찮은 것 같아요. 어디가 아프거나 하진 않은데...\"" id c05_t_0558
            c sigh "\"근데 어떻게 갑자기 녹아내렸는지, 잘 모르겠네요. 그냥 마력 반응이 없다는 걸 재확인했을 뿐인데...\"" id c05_t_0559
            
            show tiger at fwalk
            pause 2

            "엘레드는 [pl_name]의 팔을 붙잡고 확인했다. 평소와 전혀 다르지 않은 연한 털색의 팔이었다." id c05_t_0560
            
            show tiger consider_am
            with dissolve 

            t "\"으음... 겉으로 보기에는 이상이 없군.\"" id c05_t_0561

            show tiger consider2_am am_d
            with dissolve

            c consider "\"제가 마나를 불어넣어서 그런 걸까요?\"" id c05_t_0562

            show tiger :
                ease 0.2 xoffset 15
                ease 0.3 xoffset -15
                ease 0.2 xoffset 0
            
            "엘레드는 고개를 저었다." id c05_t_0563

            show tiger consider_am am_u
            with dissolve 

            t "\"그 정도로 큰 변화가 있었다면, 보고서에 반드시 쓰여 있었겠지.\"" id c05_t_0564
            t "\"흠, 원인을 파악할 수 없지만, 이렇게 갑자기 사라져 버리는 것은 기록해야겠군.\"" id c05_t_0565
            
            show tiger consider2_am
            with dissolve
            show tiger :
                ease 0.2 yoffset 135+15
                ease 0.2 yoffset 135
            pause 0.4

            "엘레드는 잠시 턱을 쓰다듬으며 생각했다." id c05_t_0566

            show tiger consider_am am_d
            with dissolve
            
            t "\"그리고, 몸에 이상이 생기면 반드시 나에게 연락하게. 내가 어떻게든 책임지겠네.\"" id c05_t_0567
            
            show tiger consider2_am am_d
            with dissolve

            c talk "\"네, 알겠습니다.\"" id c05_t_0568

            show tiger at bwalk
            pause 2
            
            play sound "audio/effect/sigh.mp3" volume 0.23
            show sigh at mirror, sigh_move2 (120, -200)
            show tiger sigh_am am_d
            with dissolve
            
            "엘레드는 한숨을 푹 내쉬었다." id c05_t_0569

    show tiger talk_am am_u
    with dissolve
    
    t "\"이것에 대해서는 함구해 주겠나? 엄중한 최고 기밀 사항은 아니지만, 정보가 새어 나갈 가능성은 차단하고 싶네.\"" id c05_t_0570
    
    show tiger base_am am_d
    with dissolve

    "엘레드의 진지한 부탁에 [pl_name][josa_eun_neun] 고개를 끄덕였다." id c05_t_0571
    
    c talk "\"네, 알겠습니다.\"" id c05_t_0572
    
    c consider "(... 개인적인 친분이 있으니까 이렇게 친절하게 부탁하는 거겠지?)" id c05_t_0573
    
    "조금 어색해진 분위기에, [pl_name][josa_eun_neun] 뭔가 다른 화제가 없을지 고민했다." id c05_t_0574
    
    "[pl_name][josa_eun_neun] 괜히 찻잔을 만지작거리다가 갑자기 생각난 것처럼 말했다." id c05_t_0575
    
    c talk "\"차 맛이 정말 좋네요.\"" id c05_t_0576

    show tiger talk_am am_u
    with dissolve
    
    t "\"입맛에 맞나? 조금이지만 캣닢이 들어가서, 쓴맛이 느껴질 수도 있는데.\"" id c05_t_0577

    show tiger base_am am_d
    with dissolve
    
    c talk "\"아, 그래서 꿀이 약간 들어갔군요. 쓴맛이 잘 숨겨진 느낌입니다.\"" id c05_t_0578
    
    "엘레드는 찻잔을 내려다보며 말했다." id c05_t_0579

    show tiger smile_am am_u
    with dissolve
    
    t "\"테오가 손님을 배려했나 보군. 그 녀석, 성격이 아주 꼼꼼해서 별명이 지옥견이라네.\"" id c05_t_0580
    
    show tiger am_d
    with dissolve

    c ddam2 "(무슨 별명이...)" id c05_t_0581
    
    "황당하다는 [pl_name]의 표정에, 엘레드는 큭큭거리며 말을 이었다." id c05_t_0582

    show tiger happy2_am am_u
    with dissolve
    
    t "\"테오는 아주 어릴 때부터 나랑 친구라서, 기사단장이라고 봐주는 법이 없지. 기사단 내의 일은 대부분 테오의 손을 거치고 있다네.\"" id c05_t_0583
    
    show tiger am_d
    with dissolve

    c consider "\"그런 분이 차 심부름까지 하신다니...\"" id c05_t_0584

    show tiger am_u
    with dissolve
    
    t "\"원래는 견습 기사들이 하는 일이지만... 아까도 말하지 않았나? 서로 하겠다는 걸 말리고 왔다고 했지.\"" id c05_t_0585

    show tiger laugh_am am_u
    with dissolve

    t "\"크하하! 그 성격에 말리기는 무슨. 말없이 째려보기만 해도 모든 기사가 입을 다물 텐데.\"" id c05_t_0586
    
    c smile "\"하하, 누구랑 성격이 비슷하네요.\"" id c05_t_0587

    show tiger smile_am am_d
    with dissolve
    
    "[pl_name]의 웃음에 엘레드도 따라서 씨익 웃었다." id c05_t_0588

label tiger_cg3_start :

    "엘레드는 식어버린 차를 단숨에 마셔버리고 조용하게 말했다." id c05_t_0589

    show tiger talk_am am_u
    with dissolve

    t "\"아참, 저번에 차마 묻지 못했던 건데... 자네 '그날' 이후에 몸 상태는 괜찮나?\"" id c05_t_0590
    
    show tiger base_am am_d
    with dissolve

    "[pl_name][josa_eun_neun] '그날'의 뜻을 눈치채고 움찔했다. 술집에서 엄청나게 취한 뒤에 화끈한 밤을 보냈던 걸 말하는 게 틀림없었다." id c05_t_0591

    c ddam2 "\"그, 근육통이 좀 있었지만, 지금은 괜찮습니다.\"" id c05_t_0592

    show tiger smile_am am_u
    with dissolve
    
    t "\"찢어지진 않았나 걱정이 돼서 그렇다네. 자네는 자꾸 괜찮다고만 해서 말이지.\"" id c05_t_0593
    
    show tiger am_d
    with dissolve

    c consider "(걱정 하는 거 맞지?...)" id c05_t_0594
    
    "[pl_name]의 의심하는 눈빛에 엘레드는 오히려 더 뻔뻔하게 미소 지었다." id c05_t_0595

    show tiger smile2_am am_u
    with dissolve
    
    t "\"흠, 정말로 괜찮다면 다행이군.\"" id c05_t_0596
    
    show tiger smile_am am_d
    with dissolve
    
    play sound "effect/putdown.mp3" volume 0.8
    pause 0.2
    show tiger at fwalk
    pause 2

    "엘레드는 찻잔을 내려놓고 [pl_name]에게 다가왔다." id c05_t_0597
    
    c ddam2 "(뭐지? 어, 어디까지 다가오는 거야?)" id c05_t_0598
    
    c "\"잠깐, 뭐 하려는- 설마, 하자고요? 여기서요?!\"" id c05_t_0599
    
    c "(굳이 본부로 초대한 것도... 애초에 이럴 계획이었던 거야?)" id c05_t_0600
    
    "[pl_name][josa_eun_neun] 엘레드의 함정에 빠졌다는 걸 뒤늦게 알아챘다." id c05_t_0601

    show tiger smile2_am am_d
    with dissolve
    
    t "\"당연하지 않나? 자네도 알다시피, 침대는 없어도 방법은 많다네.\"" id c05_t_0602
    
    show tiger smile_am red am_u
    with dissolve

    "엘레드는 [pl_name]의 어깨에 손을 올렸다." id c05_t_0603
    "이미 엘레드의 얼굴은 붉게 달아올라 있었다. [pl_name][josa_wa_gwa] 가까이 있는 것만으로도 자꾸 욕망이 샘솟았다." id c05_t_0604
    
    c "\"그, 그게 문제가 아니라... 다른 기사님이 보기라도 하면 큰일이잖아요?\"" id c05_t_0605
    
    "[pl_name][josa_eun_neun] 상상만 해도 아찔한 상황에 식은땀을 흘렸다." id c05_t_0606

    show tiger smile2_am am_u
    with dissolve
    
    t "\"흐음... 책상 밑에 숨으면 아무도 모를 것 같지 않나? 언제 누가 오더라도 문제없다네.\"" id c05_t_0607
    
    show tiger smile_am am_d
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드의 집무실 중앙에 있는 큰 책상을 보았다." id c05_t_0608
    
    c "\"숨는 건 가능하겠지만, 그... 음...\"" id c05_t_0609
    
    "[pl_name]도 욕망이 없는 것은 아니었다. 이런 방식만 아니었다면 찬성했을 수도 있었다." id c05_t_0610

    "엘레드와 보냈던 밤은 좋긴 했다. 쾌락 하나만큼은 정말 엄청나게 환상적이었다." id c05_t_0611

    c "(다음에 또 하는 걸 기대하지 않았다면 거짓말이지만... 지금 여기서 해도 괜찮을까?)" id c05_t_0612
    
    "[pl_name][josa_i_ga] 잠깐 고민하는 사이 엘레드는 [pl_name]의 손을 붙잡았다." id c05_t_0613
    
    show tiger smile2_am am_u
    with dissolve

    t "\"자네도 하고 싶은 게 있지 않나?\"" id c05_t_0614
    
    "엘레드는 [pl_name]의 손을 잡아당겨 자신의 배에 얹었다. 손에 닿는 짧은 털과 두툼한 근육이 느껴졌다." id c05_t_0615
    
    t "\"자네가 욕망에 조금만 더 솔직하면 좋을 텐데 말이지.\"" id c05_t_0616

    show tiger smile_am am_d
    with dissolve
    
    show tiger :
        ease 0.2 yoffset 135+15
        ease 0.2 yoffset 135
    pause 0.4

    "[pl_name][josa_eun_neun] 반사적으로 침을 꿀꺽 삼켰다. 엘레드의 복근을 만지면서 얼굴을 붉혔다." id c05_t_0617
    
    c ddam "(내가 이런 유혹에 넘어갈 거라고 생각한 적이 없었는데...)" id c05_t_0618
    
    "한번 경험해 본 탓인지, 엘레드의 유혹이 예전과는 다르게 느껴졌다." id c05_t_0619
    "[pl_name][josa_eun_neun] 엘레드의 육체를 좀 더 다양하게 경험해 보고 싶었다. [pl_name][josa_eun_neun] 자신의 욕망이 조금씩 꿈틀거리는 것을 느꼈다." id c05_t_0620
    "[pl_name]의 마음은 아까와 정반대로 기울었다. 조금 불안하긴 하지만, 어쨌든 기회처럼 느껴졌다." id c05_t_0621
    
    c talk "\"그럼 오늘은 제가 원하는 것도... 마음대로 해도 되나요?\"" id c05_t_0622
    
    "엘레드는 드디어 (술에 취하지 않은) [pl_name][josa_eul_reul] 유혹하는 데 성공했다." id c05_t_0623
    
    show tiger laugh_am am_u red_laugh
    with dissolve

    t "\"크하하! 그래. 내 육체는 전부 자네의 것이라네. 자, 이쪽으로 오게.\"" id c05_t_0624

    show tiger smile_am am_d red
    with dissolve

    stop music fadeout 2.5

    scene bg black with dissolve_effect
    
    "엘레드는 [pl_name][josa_eul_reul] 책상으로 이끌었다." id c05_t_0625
    "책상 아래 공간은 확실히 누구 하나 숨어있어도 모를 것 같다." id c05_t_0626
    
    c talk "\"여기... 들어가면 될까요?\"" id c05_t_0627
    
    "엘레드는 고개를 끄덕이며 의자에 앉았다." id c05_t_0628
    
    t smile2_am red "\"급해서 미안하군. 아까부터 참기 힘들었다네.\"" id c05_t_0629
    
    "[pl_name][josa_eun_neun] 조심스레 엘레드의 앞에 무릎 꿇었다. 책상에 귀가 눌리는 느낌이 들었다." id c05_t_0630

label c5t_cg3:
    
    # 배경 바꾸기
    if renpy. mobile :
        $ cleanup_memory()
    scene tiger_cg3 :
        zpos 0
        xpos 0
        ypos 0
    with Fade(0.8, 0.8, 0.8)
   
    $ persistent.tiger_unlocked[2]= True


    camera:
        perspective True
        gl_depth True

    # 여기서부터 CG
    #1)

    "..." id c05_t_0631

    play sound "audio/effect/takeoff.mp3" volume 0.6
    show tiger_cg3 at vshake (0.08, 0, -10)
    

    "엘레드는 허리 갑옷을 벗어 던지고 가득 부풀어 오른 고간을 내밀었다." id c05_t_0632

    "[pl_name][josa_eun_neun] 눈앞에 훅 다가온 붉은 속옷에 살짝 놀랐다. [pl_name][josa_eun_neun] 조심스레 손을 뻗으며 엘레드를 올려다봤다." id c05_t_0633

    #1-1)
    play sound "effect/heart_beat.mp3" volume 0.75
    show tiger_cg3 im_01_1
    with dissolve

    t talk_am "\"여기서 보는 자네 얼굴도 엄청... 야하군.\"" id c05_t_0634
    
    c ddam "(여기서는 보이는 게 거의 없는데...)" id c05_t_0635
    
    "[pl_name][josa_eun_neun] 손가락으로 엘레드의 귀두 끝을 문질렀다. 프리컴으로 살짝 젖어있는 게 느껴졌다." id c05_t_0636

    c talk "\"벗길게요?\"" id c05_t_0637
    
    t "\"허락받을 필요 없네...\"" id c05_t_0638

    play channel1 "effect/cloth.mp3" volume 0.6
    
    "[pl_name][josa_eun_neun] 간단하게 속옷의 매듭을 풀었다. 쓱 당기자 붉은 천이 쉽게 벗겨졌다." id c05_t_0639
    
    #2)
    show tiger_cg3 im_01_1 :
        ease 1 zpos 130 xpos -20 ypos -20
        
    pause 1

    show tiger_cg3 im_02
    with dissolve
    
    "빳빳하게 서 있는 자지가 [pl_name][josa_eul_reul] 향해 고개를 들고 있었다." id c05_t_0640
    #3, tongue)
    show tiger_cg3 im_03
    with dissolve
    pause 0.4
    play channel2 "effect/sticky2.mp3" volume 0.7
    show tiger_s3_tongue :
        zpos 130 xpos 1130 ypos 630 
    with dissolve
    pause 1
    hide tiger_s3_tongue
    with dissolve

    "[pl_name][josa_eun_neun] 조심스레 혀를 내밀어 엘레드의 귀두 끝부터 핥았다. 진한 수컷의 향과 프리컴의 맛이 느껴졌다." id c05_t_0641

    play channel1 "effect/sigh_tiger.mp3" volume 0.7

    t "\"후우...\"" id c05_t_0642
    
    #4)
    show tiger_cg3 im_03 :
        ease 1 xpos -40 ypos -50
    pause 1
    play sound "effect/sticky3.mp3" volume 0.7
    show tiger_cg3 im_04 
    with dissolve

    "[pl_name][josa_i_ga] 조금 더 자지를 삼키자, 엘레드는 뜨거운 숨을 내쉬었다." id c05_t_0643
    "귀두까지는 쉽게 가능했지만, 기둥은 굵기가 엄청나서 조금 겁이 났다." id c05_t_0644

    c ddam2 "(으, 입을 얼마나 벌려야 하는 거지?)" id c05_t_0645

    #5, tongue)
    show tiger_cg3 im_05 
    with dissolve

    play channel2 "effect/sticky2.mp3" volume 0.7
    show tiger_s3_tongue :
        zpos 130 xpos 1050 ypos 640 
    with dissolve
    pause 1
    hide tiger_s3_tongue
    with dissolve
    
    "[pl_name][josa_eun_neun] 굵기를 가늠하기 위해 살짝 물러나서 옆면부터 핥았다." id c05_t_0646

    c talk "(이건 진짜 각오해야겠는데.)" id c05_t_0647
    
    #6)
    play channel1 "effect/sticky3.mp3" volume 0.65
    show tiger_cg3 im_06 
    with dissolve

    "기합을 넣은 [pl_name][josa_eun_neun] 턱이 빠질 것처럼 입을 벌리고 자지를 삼켰다." id c05_t_0648

    "뒤로 받았을 때보다는 낫지만, 입안이 꽉 차는 느낌에 본능적으로 공포를 느꼈다." id c05_t_0649

    with hpunch

    c ddam "\"읍!!...\"" id c05_t_0650
    
    "[pl_name][josa_eun_neun] 심호흡하며 마음을 가라앉혔다. 굉장히 힘들지만, 아예 못 움직일 정도는 아니었다." id c05_t_0651

    #7)
    play channel2 "effect/sticky.mp3" volume 0.65
    show tiger_cg3 im_07 
    with dissolve

    "[pl_name][josa_eun_neun] 침으로 젖은 자지를 조금씩 빨아올렸다." id c05_t_0652

    play channel1 "effect/sigh_tiger.mp3" volume 0.7
    
    t "\"하...\"" id c05_t_0653

    #6,7)
    play channel2 "effect/sticky2.mp3" volume 0.7
    show tiger_cg3 im_06 
    with dissolve
    show tiger_cg3 im_07 
    with dissolve
    show tiger_cg3 im_06 
    with dissolve
    show tiger_cg3 im_07 
    with dissolve
    "엘레드는 만족스러운 미소를 지었다." id c05_t_0654

    "[pl_name]의 실력은 그다지 좋은 편이 아니었지만, 엘레드는 이 상황에 정신적으로 아주 흥분했다." id c05_t_0655
    
    "갑작스러운 소리만 아니었다면 크게 신음을 낼 뻔했다." id c05_t_0656

    play sound "effect/door_knock_weak.mp3" volume 0.9    

    "{i}똑똑{/i}" id c05_t_0657
    
    t "\"읏, 어흠!\"" id c05_t_0658
    
    #8)
    play channel1 "effect/sticky4.mp3" volume 0.7
    show tiger_cg3 im_08
    with dissolve
    show tiger_cg3 im_08 :
        ease 1 zpos 120 xpos -20 ypos 0

    "[pl_name][josa_eun_neun] 노크 소리에 털이 곤두섰다. 엘레드도 목을 가다듬고는 아무 일도 없던 척 자세를 바로잡았다." id c05_t_0659
    
    play sound "effect/door.mp3" volume 0.8
    
    "문이 열리는 소리에 [pl_name][josa_eun_neun] 조용히 몸을 구겼다. " id c05_t_0660

    th talk "\"단장님, 보급 계획서... 음?\"" id c05_t_0661

    play channel1 "effect/footstep.mp3" volume 0.85
    
    "뚜벅뚜벅 다가오는 발소리에 [pl_name][josa_eun_neun] 그야말로 죽은 것처럼 숨을 참았다." id c05_t_0662
    
    "테오는 치우지 않은 찻잔을 보고 속으로 한숨을 쉬었다. 보고서를 책상 위에 내려놓으며 엘레드에게 잔소리했다." id c05_t_0663
    
    th "\"직접 치우는 건 바라지도 않으니, 손님이 갔으면 갔다고 말이라도 하십쇼.\"" id c05_t_0664
    
    #8-1,8)
    show tiger_cg3 im_08_1 
    with Dissolve (0.15)
    show tiger_cg3 im_08
    with Dissolve (0.15)
    t embarrass_am "\"그, 크흠, 안 그래도 그러려고 했네.\"" id c05_t_0665
    
    "엘레드는 테오의 눈치를 보며 가만히 있었다." id c05_t_0666

    play channel2 "effect/ceramic.mp3" volume 0.9

    "테오는 찻잔을 잡으며 말했다." id c05_t_0667
    
    th "\"그 '손님' 말인데... 아니, 됐습니다.\"" id c05_t_0668
    
    t talk_am "\"왜 그러나?\"" id c05_t_0669
    
    th "\"어차피 잔소리해 봤자 귓등으로도 안 듣잖습니까.\"" id c05_t_0670

    "[pl_name][josa_eun_neun] 대화가 길어지자 조용히 호흡했다." id c05_t_0671
    "다행히 테오는 [pl_name]의 존재를 전혀 눈치채지 못한 것 같았다." id c05_t_0672
    "눈앞에 번들거리는 엘레드의 자지가 보였다." id c05_t_0673
    
    c ddam2 "(나는 몸 구기고 있느라 힘든데, 적당히 말 돌려서 빨리 좀 쫓아내지...)" id c05_t_0674

    menu :
        "허벅지를 찔러서 신호를 준다." :
           
            c consider "(지금 무슨 상황인지 잊어버린 건 아니겠지?)" id c05_t_0675
           
            # 8-2,8)
            show tiger_cg3 im_11
            show tiger_s3_hand :
                zpos 130 xpos 922 ypos 752
            with dissolve
            
            show tiger_cg3 im_11 :
                ease 1 xpos -40 ypos -50
            show tiger_s3_hand :
                ease 1 zpos 130 xpos 810 ypos 710

            "[pl_name][josa_eun_neun] 조심스레 손을 들었다." id c05_t_0676

            show tiger_s3_hand :
                ease 0.5 ypos 730
                ease 0.2 ypos 710
                ease 0.5 ypos 730
                ease 0.2 ypos 710
            pause 2

            with vpunch 

            "엘레드의 허벅지를 톡톡 건드리자, 엘레드가 움찔하는 게 보였다." id c05_t_0677

            hide tiger_s3_hand
            with dissolve
            
            t "\"아! 그, 지금이 몇 시지?\"" id c05_t_0678

            th "\"4시 조금 넘었습니다.\"" id c05_t_0679
            
            t talk_am red "\"그래... 저녁 전까지는 쉬도록 하게.\"" id c05_t_0680
            
            c sigh "(그래... 제발 빨리 나가줬으면...)" id c05_t_0681

            play channel2 "effect/ceramic.mp3" volume 0.9
            
            "테오는 찻잔 두 개를 챙겨가며 말했다." id c05_t_0682
            
            th "\"무슨 소립니까. 제가 쉬면 기사단이 안 굴러가는데.\"" id c05_t_0683
            
            "콧김을 흥 하고는 걸어가는 발소리가 들렸다." id c05_t_0684

            play sound "audio/effect/sigh.mp3" volume 0.23
            show sigh at sigh_move (180, 240) :
                zpos 130

            "[pl_name][josa_eun_neun] 문이 닫히자마자 푹 한숨을 내쉬었다." id c05_t_0685

            hide sigh
            
            # 조건없이 씬 진행
            jump c5t_cg3_result_next

        "성감대를 일부러 자극해서 엘레드를 괴롭힌다." :
            
            show tiger_cg3 im_08 :
                ease 1 xpos -40 ypos -50
            pause 1
            c talk "(다급해지면 어떻게든 알아서 하겠지?)" id c05_t_0686

            "[pl_name][josa_eun_neun] 엘레드를 어떻게 괴롭힐지 고민했다." id c05_t_0687
            
            # 루프로
            jump c5t_cg3_touch


# 루프 선택지
label c5t_cg3_touch :
      
    if c5t_touch_count == 3 :
        jump c5t_cg3_result


    #[루프 선택지]
    menu:
        
        "귀두를 살짝 깨문다." :

            jump c5t_cg3_glans
        
        "회음부를 자극한다." :

            jump c5t_cg3_crotch

        "허벅지 안쪽을 핥는다." :

            jump c5t_cg3_thighs
       
label c5t_cg3_glans :
    
    if c5t_touch_glans == False :
        $ c5t_touch_count += 1
        if c5t_touch_count == 3 :
            $ c5t_touch_true += 1
        $ c5t_touch_glans = True

        "[pl_name][josa_eun_neun] 침을 꿀꺽 삼키고 고개를 움직였다." id c05_t_0688

        #6)
        play sound "effect/sticky3.mp3" volume 0.7
        show tiger_cg3 im_06
        with dissolve
        
        "엘레드의 귀두가 입술에 닿자 조심스레 입을 벌렸다." id c05_t_0689

        th "\"아참, 술집에서 또 뭔 짓을 했습니까?\"" id c05_t_0690
        
        #9)
        show tiger_cg3 im_09
        with vpunch
        show tiger_cg3 im_06
        with dissolve

        "[pl_name][josa_eun_neun] 앞니로 귀두를 가볍게 깨물었다." id c05_t_0691

        t horny3_am red_no "\"다!! 당연히!... 별다른 일 없었네.\"" id c05_t_0692
        
        "엘레드는 간신히 의자에서 튀어 오르는 걸 참았다. 쾌감과 고통이 동시에 느껴져서 눈물이 찔끔 났다." id c05_t_0693

        th "\"평소에 워낙 악명이 자자해서 어지간한 일로는 얘기도 안 나올 텐데...\"" id c05_t_0694
        th "\"남들 보는 앞에서 무슨 짓을 한 겁니까? 아예 벌거벗고 춤이라도 췄습니까?\"" id c05_t_0695

        #10)
        show tiger_cg3 im_10
        with dissolve

        "[pl_name][josa_eun_neun] 하마터면 이상한 소리를 내며 웃을 뻔했다. " id c05_t_0696
        
        c laugh "(뭐야, 이미 다 맞췄는데?)" id c05_t_0697

        show tiger_cg3 im_11
        with dissolve

        "웃음을 억누르며 [pl_name][josa_eun_neun] 다음에 어떻게 할지 고민했다." id c05_t_0698

        jump c5t_cg3_touch

    else :

        c base "(이건 이미 했고...)" id c05_t_0699
        jump c5t_cg3_touch
        
label c5t_cg3_crotch :

    if c5t_touch_crotch == False :
        $ c5t_touch_count += 1
        if c5t_touch_count == 2 :
            $ c5t_touch_true += 1
        $ c5t_touch_crotch = True

        #11, hand)
        show tiger_cg3 im_11
        with dissolve
        pause 0.4
        show tiger_s3_hand :
            zpos 130 xpos 922 ypos 752
        with dissolve
    
        "[pl_name][josa_eun_neun] 엘레드의 불알을 감싸 쥐었다. 크고 튼실한 게 손안을 꽉 채웠다." id c05_t_0700

        show tiger_s3_hand :
            ease 0.3 yoffset 30
            ease 0.3 yoffset 0
            repeat 2

        "자신의 것과 약간 다른 촉감이 신기했다. [pl_name][josa_eun_neun] 그것을 가볍게 주물럭거렸다." id c05_t_0701
        
        hide tiger_s3_hand
        with dissolve

        "그러나 목표는 여기가 아니었다." id c05_t_0702

        t shy_am red_no "\"어흠!\"" id c05_t_0703

        "엘레드가 괜히 헛기침하는 사이, [pl_name][josa_eun_neun] 잠깐의 손장난을 마쳤다." id c05_t_0704
        
        #11-1,11-2)
        play channel2 "effect/sticky.mp3" volume 0.65
        show tiger_cg3 im_11_1
        with dissolve
        show tiger_cg3 im_11_2
        with dissolve
        show tiger_cg3 im_11_1
        with dissolve

        "목표 지점은 불알 아래, 회음부였다." id c05_t_0705

        with vpunch

        "손가락으로 꾹 누르자 엘레드의 몸이 파르르 떨리는 것이 느껴졌다." id c05_t_0706

        t talk_am red "\"흐, 흠!! 오늘은 특이 사항 없었나?\"" id c05_t_0707

        "뭉친 근육을 풀어주듯 꾹꾹 문지르자, 엘레드의 남근이 힘차게 불끈거렸다." id c05_t_0708

        th "\"없습니다. 평소에 보고서나 잘 읽으십시오.\"" id c05_t_0709

        "테오는 잔소리를 더 늘어놓으려다가, 아무도 손대지 않은 과자를 하나 집어 먹었다." id c05_t_0710
        
        show tiger_cg3 im_11
        with dissolve

        c consider "(음, 다른 방법을 써야 하나...)" id c05_t_0711

        jump c5t_cg3_touch
    
    else :

        c base "(이건 이미 했고...)" id c05_t_0712
        jump c5t_cg3_touch

label c5t_cg3_thighs :

    if c5t_touch_thighs == False :
        $ c5t_touch_count += 1
        if c5t_touch_count == 1 :
            $ c5t_touch_true += 1
        $ c5t_touch_thighs = True
        
        "[pl_name][josa_eun_neun] 엘레드의 허벅지 쪽으로 고개를 돌렸다." id c05_t_0713

        #12,12-1)
        show tiger_cg3 im_12_1
        with Dissolve (1.0)
        pause 0.4
        show tiger_cg3 im_12
        with Dissolve (0.3)
        show tiger_cg3 im_12_1
        with Dissolve (0.3)

        "코로 허벅지 안쪽을 쿡 누르자 긴장한 근육을 느낄 수 있었다." id c05_t_0714
        #tongue)
        play sound "effect/sticky3.mp3" volume 0.7
        show tiger_s3_tongue :
            zpos 130 xpos 912 ypos 778 
        with dissolve
        pause 1
        hide tiger_s3_tongue
        with dissolve
        
        "[pl_name][josa_eun_neun] 그대로 혀를 내밀었다." id c05_t_0715

        with hpunch

        t talk_am red "\"으- 그, 그러고 보니 내일 일정이 어떻게 되지?\"" id c05_t_0716

        "[pl_name]의 질척한 혓바닥에 엘레드는 크게 움찔했지만, 어떻게든 아무 일도 없는 척했다." id c05_t_0717
        
        th "\"...? 특별한 건 없습니다.\"" id c05_t_0718

        "테오는 다음 주에 있을 회의를 얘기했다. 당연히 엘레드는 전혀 집중하지 못했다." id c05_t_0719

        #11)
        show tiger_cg3 im_11
        with dissolve

        c consider "(이 정도로는 부족한가?)" id c05_t_0720
        jump c5t_cg3_touch

    else :

        c base "(이건 이미 했고...)" id c05_t_0721
        jump c5t_cg3_touch

label c5t_cg3_result :

    if c5t_touch_true == 3  :
            
        $ c5t_cg3_success = True

        "엘레드의 반응이 미묘해서, [pl_name][josa_eun_neun] 좀 더 자극적인 걸 하기로 마음먹었다." id c05_t_0722

        "엘레드도 참을 수 없을 정도면 어떻게든 테오를 내보낼 것이다." id c05_t_0723
        
        c laugh "(해보니까 왠지 재밌기도 하고...)" id c05_t_0724

        #14)
        play channel2 "effect/sticky2.mp3" volume 0.7
        show tiger_cg3 im_14
        with dissolve

        "[pl_name][josa_eun_neun] 엘레드의 귀두를 입에 물었다. 그러나 이 정도로 멈출 생각은 아니었다." id c05_t_0725

        t horny3_am red_no "\"아무튼, 보고서느으-...\"" id c05_t_0726

        #15)
        play channel1 "effect/sticky4.mp3" volume 0.7
        show tiger_cg3 im_15
        with vpunch

        "[pl_name][josa_i_ga] 조금씩 깊게 삼킬수록, 엘레드의 떨림도 커졌다." id c05_t_0727

        t  "\"잘, 읽어볼 테니, 음...\"" id c05_t_0728

        "엘레드는 표정을 유지하기가 힘들었다." id c05_t_0729

        "조금이라도 긴장을 놓으면 무슨 일이든 터질 것 같았다." id c05_t_0730

        th "\"어디 아프십니까?\"" id c05_t_0731

        "테오는 오늘따라 엘레드의 상태가 좀 이상하다고 생각했다." id c05_t_0732

        t embarrass_am red "\"아, 아니.\"" id c05_t_0733

        #16)
        play channel2 "effect/sticky.mp3" volume 0.65
        show tiger_cg3 im_16
        with dissolve

        "[pl_name][josa_eun_neun] 천천히 혀를 굴리며 조금 더 깊게 삼켰다." id c05_t_0734
        "기둥의 가장 굵은 지점을 넘어가자, 생각 외로 쑤욱 들어갔다." id c05_t_0735

        c ddam "(윽, 잘못하면 질식하겠는데...)" id c05_t_0736

        "[pl_name][josa_eun_neun] 코로 뜨거운 숨을 내뿜었다. 엘레드의 털이 코에 닿을 정도로 깊이 삼켰다는 게 신기했다." id c05_t_0737

        #16-1)
        show tiger_cg3 im_16_1
        with dissolve

        "[pl_name][josa_i_ga] 흐르는 침을 삼키자, 갑자기 좁아진 목구멍이 엘레드의 자지를 꽉 조였다." id c05_t_0738

        with vpunch

        t horny_am red_no "\"아흣!!...\"" id c05_t_0739

        c ddam2 "(.... 망했다.)" id c05_t_0740

        #17)
        show tiger_cg3 im_17
        with dissolve

        "신음소리를 낸 엘레드를 보고 테오는 순식간에 눈매가 변했다." id c05_t_0741

        ## 위아래 카메라 움직이기
        show tiger_cg3 im_17 :
            ease 0.7 ypos 52
            pause 0.3
            ease 0.9 ypos -62
            pause 0.3
            ease 0.6 ypos 10
        pause 2.6
        
        "엘레드를 위아래로 훑으며 상황을 파악했다." id c05_t_0742

        ## 홍차
        show tea :
            zoom 0.98 zpos 130
        with dissolve

        th "\"너. 지금... 설마, 찻잔이 남은 것도...\"" id c05_t_0743

        hide tea
        with dissolve

        th "\"이 새끼...\"" id c05_t_0744

        "테오는 말투부터 눈빛까지 엘레드에게 경멸을 보냈다." id c05_t_0745

        #8)
        play channel1 "effect/sticky4.mp3" volume 0.7
        show tiger_cg3 im_10
        with dissolve


        "[pl_name][josa_eun_neun] 아무것도 보이지 않았지만, 진땀을 흘리며 가만히 있었다." id c05_t_0746
        
        t embarrass_am red "\"어흠! 그, 그렇게 됐다네.\"" id c05_t_0747
        
        "테오는 스트레스로 인한 갑작스러운 두통에 머리를 짚었다." id c05_t_0748
        
        th "\"이런 것도 상관이라고, 하아... 30분 안에 끝내.\"" id c05_t_0749

        t talk_am "\"하, 한 시간...\"" id c05_t_0750
        
        "테오는 이런 상황에서도 협상하는 엘레드 때문에 어이가 없었다. 책상 밑의 [pl_name]도 비슷한 심정이었다." id c05_t_0751

        th "\"무슨 한 시간씩이나 필요해? 아, 맘대로 해. 만약 오후 훈련이 끝날 때까지 안 끝내면...\"" id c05_t_0752
        
        play channel2 "effect/ceramic.mp3" volume 0.9

        "테오는 뒷말을 생략하고 찻잔 두 개를 챙겼다." id c05_t_0753

        #18)
        play sound "effect/footstep.mp3" volume 0.85
        pause 2
        play channel1 "effect/door.mp3" volume 0.8
        pause 3.7
        show tiger_cg3 im_18
        with dissolve
        
        play sound "audio/effect/sigh.mp3" volume 0.23
        show sigh at sigh_move (180, 250) :
            zpos 130
        
        "문이 닫히는 소리가 나자, 마침내 [pl_name][josa_eun_neun] 숨을 푹 내쉬었다." id c05_t_0754
        
        hide sigh

        c angry "\"전에도 비슷한 일이 있었나요?\"" id c05_t_0755
        
        "은은한 비난이 담긴 [pl_name]의 말에 엘레드는 당황하며 대답했다." id c05_t_0756

        t embarrass_am red "\"아... 아니! 자네가 처음이라네.\"" id c05_t_0757
        
        c "(진짜인가? 아니, 지금 의심해 봤자 소용없겠지...)" id c05_t_0758
        
        "[pl_name][josa_eun_neun] 굳이 엘레드를 더 추궁하지 않았다." id c05_t_0759
        
        jump c5t_cg3_result_next

    else :

        "[pl_name][josa_eun_neun] 뭘 할지 잠깐 고민했다." id c05_t_0760

        #10)
        show tiger_cg3 im_10
        with dissolve

        "[pl_name][josa_i_ga] 엘레드의 자지를 다시 쥐자, 그는 식은땀을 흘리며 입을 열었다." id c05_t_0761

        t talk_am red "\"아무튼, 보고서는 읽어볼 테니 이만 가보게.\"" id c05_t_0762
        
        "오늘따라 엘레드의 태도가 이상했지만, 테오는 그냥 엘레드가 일하기 싫어서 그런 거로 생각했다." id c05_t_0763
        
        play sound "effect/footstep.mp3" volume 0.85

        th "\"예예, 충견은 일이나 하러 갑니다.\"" id c05_t_0764
        
        c shy2 "(드디어!...)" id c05_t_0765

        play channel1 "effect/door.mp3" volume 0.8
        
        "문이 닫히는 소리가 나자, 마침내 [pl_name][josa_eun_neun] 숨을 푹 내쉬었다." id c05_t_0766

        jump c5t_cg3_result_next

    
label c5t_cg3_result_next :
    
    #19)
    show tiger_cg3 im_19
    with dissolve

    c talk "\"그럼, 빨리 끝내죠.\"" id c05_t_0767
    
    #20)
    play channel2 "effect/sticky2.mp3" volume 0.7
    show tiger_cg3 im_20
    with dissolve
    
    "[pl_name][josa_eun_neun] 다시 한번 각오를 다지고 입을 벌렸다. 엘레드의 자지는 이미 흥건하게 젖어있었다." id c05_t_0768

    play channel1 "effect/sigh_tiger.mp3" volume 0.7

    t horny2_am red_no"\"하아...\"" id c05_t_0769
    
    #21)
    play channel2 "effect/sticky.mp3" volume 0.65
    show tiger_cg3 im_21
    with dissolve
    
    "엘레드는 [pl_name]의 혓바닥이 기둥을 쓸어내리는 느낌에 신음을 흘렸다." id c05_t_0770
    "너무 오래 참아서 당장이라도 터질 것 같았다. 하지만 조금이라도 더 [pl_name][josa_i_ga] 주는 자극을 느끼고 싶었다." id c05_t_0771

    c horny "\"크읍!...\"" id c05_t_0772

    #20,21,22)
    play channel2 "effect/sticky3.mp3" volume 0.7
    show tiger_cg3 im_20
    with dissolve
    show tiger_cg3 im_21
    with dissolve
    show tiger_cg3 im_22
    with Dissolve (0.25)
    
    "반면, 마음이 급해진 [pl_name][josa_eun_neun] 빨리 엘레드를 싸게 만들고 싶었다." id c05_t_0773
    "자지 표면을 혀로 자극하면서 왕복하다가, 조금 더 깊게 고개를 집어넣었다." id c05_t_0774

    c "(윽! 진짜 너무 굵은데...)" id c05_t_0775

    #20,21,22)
    play channel1 "effect/sticky3.mp3" volume 0.7
    show tiger_cg3 im_20
    with dissolve
    show tiger_cg3 im_21
    with dissolve
    show tiger_cg3 im_22
    with Dissolve (0.25)
    
    "엘레드는 평소처럼 상대방의 머리를 붙잡고 깊게 넣고 싶었지만, [pl_name]의 심기를 거스르지 않기 위해 꾹 참았다." id c05_t_0776
    "애꿎은 주먹만 꽉 쥐고 허리를 들썩거렸다." id c05_t_0777
    "[pl_name][josa_eun_neun] 조금 더 속도를 높였다. 거리낄 것 없이 질척한 소리를 내며 엘레드의 기둥을 빨아들였다." id c05_t_0778

    t horny3_am "\"자, 잠깐! 그렇게 하다간, 금방 싸버릴 것 같네...\"" id c05_t_0779
    
    #20,21,22)
    play channel2 "effect/sticky2.mp3" volume 0.7
    show tiger_cg3 im_20
    with dissolve
    show tiger_cg3 im_21
    with dissolve
    show tiger_cg3 im_22
    with Dissolve (0.25)
    play channel1 "effect/sticky3.mp3" volume 0.7
    show tiger_cg3 im_20
    with dissolve
    show tiger_cg3 im_21
    with dissolve
    show tiger_cg3 im_22
    with Dissolve (0.25)
    
    "[pl_name][josa_eun_neun] 입안에 흥건한 프리컴으로 이미 알 수 있었다." id c05_t_0780
    "[pl_name][josa_eun_neun] 엘레드의 발목을 붙잡고 머리를 움직였다. 엘레드는 결국 참지 못하고 모든 것을 내려놓았다." id c05_t_0781

    t "\"젠장, 크윽!...\"" id c05_t_0782

    with vpunch
    
    "엘레드는 더 이상 참지 않았다. 절정이 온몸을 부르르 떨게 했다." id c05_t_0783

    #23)
    show tiger_cg3 im_22 :
        ease 1 zpos 150 xpos -45 ypos -70
    pause 1.0
    play sound "audio/effect/sqz1.mp3" volume 0.7
    pause 0.5
    show tiger_cg3 im_23
    with vpunch

    "자지가 꿈틀거릴 때마다 엄청난 양의 정액이 흘러나왔다." id c05_t_0784

    with hpunch

    c "\"읍!!\"" id c05_t_0785
    
    "[pl_name]의 목구멍 안쪽으로 걸쭉한 액이 가득 찼다." id c05_t_0786

    "어느 정도는 삼키긴 했지만, 너무 많은 양이라서 전부 마실 수는 없었다." id c05_t_0787

    #23-1)
    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.4
    show tiger_cg3 im_23_1
    with vpunch

    t "\"크르르르르...\"" id c05_t_0788
    
    "엘레드는 절정을 느끼면서 짐승의 소리를 냈다. 폭포처럼 쏟아지는 정액은 [pl_name]의 입 밖까지 흘러넘쳤다." id c05_t_0789

    #24)
    show tiger_cg3 im_24
    with dissolve

    "결국 [pl_name][josa_eun_neun] 더 이상 버티지 못하고 입에서 자지를 뺐다. 얼굴에도 정액이 튀어서 [pl_name][josa_eun_neun] 당황했다." id c05_t_0790
    
    #25)
    play sound "audio/effect/cough.mp3" volume 0.7
    show tiger_cg3 im_25
    with dissolve
    
    c "\"콜록콜록!\"" id c05_t_0791

    #26)
    show tiger_cg3 im_26
    with dissolve
    pause 0.4

    show tiger_cg3 im_26 :
        ease 1 zpos 0 xpos -15 ypos 0
    
    "마침내 끝난 사정에 [pl_name][josa_eun_neun] 겨우 정신을 차렸다." id c05_t_0792
    "어떤 의미로든 굉장한 경험이었다. [pl_name][josa_eun_neun] 정액 범벅이 된 얼굴로 엘레드를 올려다봤다." id c05_t_0793

    t talk_am red "\"미, 미안하네. 도저히 참을 수가 없어서...\"" id c05_t_0794
    
    c horny2 "\"각오하긴 했어요. 이 정도일 줄은 몰랐지만.\"" id c05_t_0795
    
    "[pl_name][josa_eun_neun] 입가에 묻은 정액을 핥으며 말했다." id c05_t_0796

    c talk "\"그럼 이제 제 차례 맞죠?\"" id c05_t_0797
    
    t "\"그, 그렇지. 뭘 원하나?\"" id c05_t_0798
    
    c shy2 "\"뒤로 돌아서 엉덩이 벌려봐요.\"" id c05_t_0799
    
    t "\"어?\"" id c05_t_0800
    
    "엘레드는 뭔가 상황이 이상하게 돌아간다고 느꼈다." id c05_t_0801

    stop music fadeout 2.5

    $ renpy.end_replay()

    if c5t_cg3_success == True :
        jump c5t_cg4
    else :
        jump c5t_after
    
label c5t_cg4:

    if renpy.mobile :
        $ cleanup_memory()
    scene tiger_cg4_background :
        zpos -958  
    show tiger_cg4_back_shelf :
        zpos -500
        
    show tiger_cg4

    show tiger_cg4_front
    show tiger_cg4_front2 :
        alpha 0.15
    with Fade(0.8, 0.8, 0.8)

    camera:
        perspective True
        gl_depth True

    # 씬 보면 호감도 +1
    $ tiger_love +=1
    $ display_text = _("엘레드 호감도 변화")
    $ persistent.tiger_unlocked[3]= True


    t nake_d talk "\"바로 하려는 건가?\"" id c05_t_0802

    "엘레드는 유리창에 얼핏 비치는 [pl_name][josa_eul_reul] 보며 불안해했다. 뭔가 평소의 [pl_name][josa_wa_gwa]는 기세가 달랐다." id c05_t_0803

    c nake_d talk "\"이제 와서 꼬리를 빼는 건 아니죠?\"" id c05_t_0804

    t "\"그건 아니지만, 책상에서 하는 편이...\"" id c05_t_0805

    #front2)

    play channel1 "effect/heart_beat.mp3" volume 0.75

    camera :
        ease 1.8 zpos -55

    show tiger_cg4_front :
        pause 0.4
        ease 1.6 alpha 0
    show tiger_cg4_front2 :
        pause 0.3
        linear 1.6 alpha 1

    "엘레드는 창문에 기대어 [pl_name] 쪽으로 엉덩이를 내민 자세를 유지했다." id c05_t_0806

    c "\"밖에서 보일까 봐 그러시나요? 이미 다 들켰잖아요.\"" id c05_t_0807

    "엘레드는 '박히는 것' 정도는 전혀 두렵지 않았다. 굳이 말하자면 꽤 즐기는 편이었다." id c05_t_0808
    "그러나 상의를 집어 던지고 이제 바지를 내리는 [pl_name]의 눈빛은 조금 두려웠다." id c05_t_0809
    "평소에는 아름답게만 보이던 오드아이가, 지금은 이상하게 무저갱처럼 깊어 보였다." id c05_t_0810

    t "(뭔가 다른 면모가 있다고는 예상했지만... 이 정도였나?)" id c05_t_0811

    play channel1 "effect/cloth.mp3" volume 0.6

    "[pl_name][josa_eun_neun] 마지막으로 속옷을 벗으며 말했다." id c05_t_0812

    c "\"전에 썼던 허브 오일, 가지고 있죠?\"" id c05_t_0813

    show oil :
        zpos 651
        zoom 0.41
    with dissolve

    t "\"아... 그건, 여기 있네.\"" id c05_t_0814

    hide oil
    with dissolve    

    "엘레드는 바닥에 벗어둔 갑옷에서 작은 유리병을 꺼냈다. [pl_name][josa_eun_neun] 엘레드의 손에서 유리병을 낚아챘다." id c05_t_0815
    
    #2)
    show tiger_cg4 im_02
    with dissolve

    "손가락과 기둥에 오일을 듬뿍 뿌리고 엘레드의 뒤로 다가갔다." id c05_t_0816

    c consider "(흠, 이런 용도로 쓸 거면 좀 더 끈적하게 만들어야 하나?)" id c05_t_0817

    play sound "effect/sticky3.mp3" volume 0.7

    "엘레드는 구멍을 찌르는 [pl_name]의 손가락에 살짝 흠칫했다. 당연히 손가락부터 들어올 거라고 예상했지만, 그게 3개일 줄은 예상하지 못했다." id c05_t_0818

    #3, tigerbeat)
    show tiger_cg4 im_03 tigerbeat
    with hpunch

    t horny2 "\"흐윽!... 자네, 내 구멍을 과대평가하는 것 아닌가?\"" id c05_t_0819

    c sneer "\"무슨 뜻인지 잘 모르겠네요.\"" id c05_t_0820

    play channel2 "effect/sticky2.mp3" volume 0.7

    "[pl_name][josa_eun_neun] 그저 빨리 박아 넣을 생각뿐이었다. 미끈한 손가락이 엘레드의 구멍 안을 휘저었다." id c05_t_0821

    c "\"제가 지금 많이 급해서요.\"" id c05_t_0822

    "[pl_name][josa_eun_neun] 조금 전에 엘레드가 했던 말을 그대로 돌려주었다." id c05_t_0823

    #surprise)
    show tiger_cg4 im_03 surprise
    with hpunch

    t horny "\"아직 시간은 많이 있다네. 성급해하지 말고- 읏!\"" id c05_t_0824

    play channel1 "effect/sticky4.mp3" volume 0.7
    with vpunch

    "[pl_name][josa_i_ga] 갑자기 손가락을 빼자, 엘레드는 찌릿한 감각에 몸을 떨었다. 쾌감보다는 조금 위험한 느낌이었다." id c05_t_0825

    #tigerbeat hide)

    show tiger_cg4 tigerbeat_no surprise_no
    with dissolve

    c "\"그럼, 넣을게요.\"" id c05_t_0826

    #4, tigerbeat)
    play channel2 "effect/sticky4.mp3" volume 0.7
    show tiger_cg4 im_04 tigerbeat
    with hpunch

    "[pl_name][josa_eun_neun] 귀두로 엘레드의 구멍을 쿡 찔렀다. 입을 오물거리는 것처럼 움직이는 항문이 느껴졌다." id c05_t_0827

    t horny3 "\"잠깐, 조금만 천천히- 크으윽!!!\"" id c05_t_0828

    play channel1 "effect/sticky.mp3" volume 0.65

    "엘레드의 생각보다 훨씬 빠르게, 뜨겁고 굵은 것이 안으로 들어오고 있었다." id c05_t_0829
    "엘레드는 이를 꽉 깨물고 부들부들 떨었다. 이런 종류의 고통은 오랜만에 겪어보는 것이었다." id c05_t_0830

    #tigerebeat hide)
    play channel2 "effect/exhale.mp3" volume 0.7
    show tiger_cg4 tigerbeat_no
    with dissolve

    c horny3 "\"하아...\"" id c05_t_0831

    "자지를 감싸는 내벽의 느낌에 [pl_name][josa_eun_neun] 반사적인 한숨을 내쉬었다." id c05_t_0832

    play channel1 "effect/sticky3.mp3" volume 0.7

    "엘레드의 몸을 붙잡고 욕심대로 더 깊게 밀어 넣었다. 엘레드는 강제로 내부가 열리는 느낌에 몸을 떨었다." id c05_t_0833

    t "\"으윽!... 그래. 끝까지 밀어 넣게.\"" id c05_t_0834

    "엘레드는 고통에 몸을 떨면서도 여유를 잃지 않고 말했다. [pl_name][josa_i_ga] 조금 미숙하더라도 괜찮았다." id c05_t_0835
    "오히려 이게 [pl_name]의 처음이었으면 좋겠다고 생각했다." id c05_t_0836

    play sound "audio/effect/breath.mp3" volume 0.4

    "자지를 끝까지 밀어 넣은 [pl_name][josa_eun_neun] 잠시 뜨거운 숨을 뱉다가 말했다." id c05_t_0837

    c "\"그러면 움직일게요.\"" id c05_t_0838

    stop sound fadeout 4

    t talk red "\"하, 핫, 기대되는군!\"" id c05_t_0839

    #5, 5_1+spike+ring, frame1,2)
    play channel1 "audio/effect/dickout.mp3" volume 0.7
    show tiger_cg4 im_05_2
    show tiger_cg4_frame  
    with Dissolve (0.4)

    play channel2 "audio/effect/slap.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_s4_ring_move    
    show tiger_cg4 im_05 spike
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    

    "[pl_name][josa_eun_neun] 천천히 허리를 뒤로 뺐다가 다시 밀어 넣었다. 전혀 풀어지지 않은 구멍은 엄청나게 좁게 느껴졌다." id c05_t_0840
    "엘레드도 속을 제멋대로 휘저어버리는 기둥에 진땀을 흘렸다." id c05_t_0841

    c horny "\"윽...\"" id c05_t_0842

    #5, 5_1+spike+ring, frame1,2)
    play channel1 "audio/effect/dickout2.mp3" volume 0.7
    hide tiger_cg4_frame
    hide tiger_s4_ring_move
    show tiger_cg4 im_05_2 spike_no
    show tiger_cg4_frame
    with Dissolve (0.4)

    play channel2 "audio/effect/slap2.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_05 spike
    show tiger_s4_ring_move
    show tiger_cg4_front2    
    show tiger_cg4_frame fr_02
    with vpunch

    t horny2 red_no "\"너무, 무리하지 말고, 후우... 조금 더 아래를 노려서, 흣! 그래, 그렇게...\"" id c05_t_0843

    "엘레드는 헐떡거리면서도 [pl_name][josa_eul_reul] 리드했다. 당연한 얘기지만, 초보자를 능숙하게 이끄는 것은 엘레드의 전문 분야였다." id c05_t_0844
    "주도권을 되찾은 엘레드는 비장의 기술을 선보였다." id c05_t_0845

    with hpunch

    c "\"흐앗?!\"" id c05_t_0846

    "갑자기 조여오는 구멍 때문에 [pl_name][josa_eun_neun] 깜짝 놀랐다." id c05_t_0847
    "아까와는 느낌이 완전히 달랐다. 단순히 조이는 것이 아니라, 꿈틀거리면서 삼키는 듯한 움직임이 느껴졌다." id c05_t_0848
    "이곳을 손가락처럼 섬세하게 움직일 수 있다는 사실이 놀라웠다." id c05_t_0849

    t "\"왜 그러나? 빨리 굶주린 구멍에 자지를 더 먹여주게...\"" id c05_t_0850

    "엘레드의 노골적인 말에 [pl_name][josa_eun_neun] 괜히 부끄러워졌다." id c05_t_0851

    #5_1)
    play channel1 "audio/effect/dickout3.mp3" volume 0.7
    show tiger_cg4 im_05_1 spike_no
    show tiger_cg4_frame fr_01
    hide tiger_s4_ring_move
    with dissolve

    "하지만 동시에, 이런 상황에서 너무 초짜같이 굴고 싶지 않았다. [pl_name][josa_eun_neun] 엘레드의 자지를 꽉 움켜쥐고 말했다." id c05_t_0852

    c horny2 "\"그렇게나 원하신다면...\"" id c05_t_0853

    #5, 5_2+spike+ring, frame1,2)
    play channel2 "audio/effect/slap3.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_05 spike
    show tiger_s4_ring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    "[pl_name][josa_eun_neun] 조금 더 강하게 허리를 꽂아 넣었다. 엘레드의 구멍은 정말로 굶주린 것처럼 자지를 놓아주지 않았다." id c05_t_0854
    
    "내벽은 말랑하면서도 단단한, 모순적인 느낌으로 [pl_name][josa_eul_reul] 집어삼켰다." id c05_t_0855
    "[pl_name][josa_eun_neun] 조금씩 쾌락에 젖어 더 격하게 움직였다. 엘레드의 가슴에 달린 피어싱이 박자에 따라 흔들렸다." id c05_t_0856
    
    #5, 5_2+spike+ring, frame1,2)
    play channel1 "audio/effect/dickout.mp3" volume 0.7
    hide tiger_s4_ring_move
    show tiger_cg4 im_05_1 spike_no
    show tiger_cg4_frame fr_01    
    with dissolve

    t "\"하윽!... 거기, 거기를 더!\"" id c05_t_0857

    #5, 5_2+spike+ring, frame1,2)
    play channel2 "audio/effect/slap.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_05 spike
    show tiger_s4_ring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch
    pause 0.4

    c "\"여기?\"" id c05_t_0858

    "[pl_name][josa_eun_neun] 내벽에서 살짝 튀어나온 듯한 부분을 노려서 귀두로 꾹 눌렀다. 엘레드는 짜릿한 느낌에 저절로 신음을 뱉었다." id c05_t_0859

    t "\"으흣! 그래, 거기를 짓뭉개서, 나를 절정 시켜주게. 빨리...\"" id c05_t_0860

    c "(포지션이 바뀌었다고 이렇게까지 반응이 달라지다니... 아니, 오히려 정말로 한결같이 음탕한 건가?)" id c05_t_0861

    #5, 5_2+spike+ring, frame1,2_1)
    play channel1 "audio/effect/dickout2.mp3" volume 0.7
    hide tiger_s4_ring_move
    show tiger_cg4 im_05_1 spike_no
    show tiger_cg4_frame fr_01    
    with dissolve
    
    play channel2 "audio/effect/slap2.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_05 spike
    show tiger_s4_ring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    "[pl_name][josa_eun_neun] 엘레드가 원하는 대로 전립선을 눌러주었다." id c05_t_0862

    #6)
    play sound "audio/effect/SPS - (8).mp3" volume 0.6
    hide tiger_s4_ring_move
    show tiger_cg4_frame fr_02_1
    show tiger_cg4 im_06 spike
    with hpunch
    
    "엘레드의 자지에서 투명한 액이 왈칵 흘러나왔다. [pl_name]의 손이 축축해질 정도로 멈추지 않고 새어 나왔다." id c05_t_0863

    #6_1)
    show tiger_cg4_frame fr_02
    show tiger_cg4 im_06_1 spike_no
    with dissolve

    c "(그러고 보니, 여기도 좋아했었지?)" id c05_t_0864

    menu :

        "피어싱을 잡아 당긴다." :

            #7, tigerbeat)
            show tiger_cg4 im_07 tigerbeat
            with hpunch    

            "[pl_name][josa_eun_neun] 다른 손을 더듬어 금색 고리를 붙잡았다." id c05_t_0865

    play sound "audio/effect/moaning_tiger.mp3" volume 0.8
    t horny3 "\"응하아읏!!\"" id c05_t_0866

    "[pl_name][josa_i_ga] 피어싱을 가볍게 당길 때마다, 엘레드는 위아래로 찾아오는 짜릿한 감각에 뜨거운 숨을 뱉었다. 창문이 입김으로 뿌옇게 변했다." id c05_t_0867

    #7_1)
    show tiger_cg4 im_07_1 tigerbeat_no
    with dissolve

    t horny2 "\"하... 자네, 흐응! 역시 기대를, 저버리지 않는군.\"" id c05_t_0868

    "엘레드는 황홀한 표정으로 쾌락에 녹아내리고 있었다. 줄줄 새는 전립선액으로 바닥이 더러워지는 것도 신경 쓰지 않았다. [pl_name]도 헐떡거리며 간신히 사정을 참았다." id c05_t_0869

    c "(자칫하면 바로 쌀 것 같은데...)" id c05_t_0870

    #8)
    play channel1 "audio/effect/dickout3.mp3" volume 0.7
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_08
    with dissolve

    "[pl_name][josa_i_ga] 살짝 뒤로 물러서서 자지를 빼내자, 활짝 벌려진 구멍이 아쉬운 듯 오물거렸다." id c05_t_0871

    t "\"음?\"" id c05_t_0872

    c horny3 "\"후... 이대로 싸면 아쉽잖아요.\"" id c05_t_0873

    hide tiger_cg4_frame
    with dissolve

    "엘레드는 쾌락에 잠식된 상태로 웃으며 말했다." id c05_t_0874

    t "\"흐음, 아쉽지 않을 만큼 채워주겠다는 예고인가?\"" id c05_t_0875

    "[pl_name][josa_eun_neun] 아직 엘레드의 말을 감당할 수 없었다. 평소에도 숨 쉬듯 플러팅을 한다고 생각했는데, 지금은 아예 수준이 달랐다." id c05_t_0876
    
    #(짝! 손자국)
    #9, tiger beat)
    play channel2 "audio/effect/hand_clap2.mp3" volume 0.7
    show tiger_cg4 im_09 tigerbeat
    with vpunch

    "[pl_name][josa_eun_neun] 대답 대신 엘레드의 엉덩이를 찰싹 때렸다." id c05_t_0877

    t horny3 "\"으흥!\"" id c05_t_0878

    "엘레드의 엉덩이 털에 살짝 눌린 자국이 났다. 부르르 떠는 꼬리는 아무래도 좋다는 의미인 것 같았다." id c05_t_0879

    show tiger_cg4 tigerbeat_no
    with dissolve

    c "(진짜 이런 것도 좋아하는구나...)" id c05_t_0880

    #10, spike, ring)
    play channel2 "audio/effect/slap3.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_10 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    "과한 흥분을 가라앉힌 [pl_name][josa_eun_neun] 다시 구멍을 노려서 허리를 움직였다. 아까와는 달리, 아무런 저항도 없이 쑥 들어갔다." id c05_t_0881

    #11,10+spike+ring)
    #12, tigerbeat)
    play channel1 "audio/effect/dickout.mp3" volume 0.7
    hide tiger_s4_hring_move
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_11 spike_no
    with dissolve
    
    play channel2 "audio/effect/slap.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_10 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch
    pause 0.5

    t horny2 "\"흐아아앗!!...\"" id c05_t_0882
    
    play sound "audio/effect/SPS - (9).mp3" volume 0.6
    show tiger_cg4 im_12 tigerbeat
    with hpunch    

    "전립선을 강하게 찔린 엘레드는 희뿌연 액을 싸버렸다. 정액인지 아닌지 구분할 수 없는 액체가 후두둑 떨어졌다." id c05_t_0883

    #13,14)
    play channel1 "audio/effect/dickout2.mp3" volume 0.7
    hide tiger_s4_hring_move
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_14 spike_no tigerbeat_no
    with dissolve
    
    play channel2 "audio/effect/slap2.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_13 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    "[pl_name][josa_i_ga] 찌를 때마다 계속 흘러나와서, 바닥에는 조그만 웅덩이가 생겼다. [pl_name][josa_eun_neun] 아래를 힐긋 보고는 말했다." id c05_t_0884

    play channel1 "audio/effect/dickout3.mp3" volume 0.7
    hide tiger_s4_hring_move
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_14 spike_no tigerbeat_no
    with dissolve

    c horny2 "\"사정한 거에요?\"" id c05_t_0885

    t "\"하으... 자네가, 찌를 때마다, 계속... 계속 싸는 것 같다네.\"" id c05_t_0886

    #13+spike+ring, 14)
    play channel2 "audio/effect/slap3.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_13 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch

    "공기 중에 가득한 땀 냄새와 정액 냄새, 빛을 받아 반짝이는 엘레드의 털과 근육, 헐떡거리는 엘레드의 표정까지, 모든 상황이 믿을 수 없을 만큼 음란했다." id c05_t_0887
    "[pl_name][josa_eun_neun] 결국 마지막 인내심을 버렸다. 당장 엘레드의 안에 정액을 쏟아부을 각오로 움직였다." id c05_t_0888

    #13+spike+ring, 14)
    #13+spike+ring, 14)
    #13+spike+ring)
    play channel1 "audio/effect/dickout.mp3" volume 0.7
    hide tiger_s4_hring_move
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_14 spike_no tigerbeat_no
    with Dissolve (0.35)
    
    play channel2 "audio/effect/slap.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_13 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch
    pause 0.5
    
    play channel1 "audio/effect/dickout2.mp3" volume 0.7
    hide tiger_s4_hring_move
    show tiger_cg4_frame fr_01
    show tiger_cg4 im_14 spike_no tigerbeat_no
    with Dissolve (0.25)

    play channel2 "audio/effect/slap2.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_13 spike
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_02
    with vpunch
    pause 0.5

    t "\"그, 으으읏!!... 갑자기, 그러면... 아읏! 하으윽!!\"" id c05_t_0889

    #15+tigerbeat+surprise)
    play channel1 "audio/effect/sqz1.mp3" volume 0.7
    pause 0.2
    hide tiger_s4_hring_move
    show tiger_cg4 im_15 spike_no tigerbeat surprise
    with vpunch

    "바닥으로 흩뿌려지는 정액은 도저히 멈출 것 같지 않았다. 엘레드의 허벅지는 지나친 쾌감에 덜덜 떨고 있었다." id c05_t_0890

    #16+tigerbeat)
    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.45
    show tiger_cg4 im_16 tigerbeat
    with vpunch

    "절정이 가까워진 [pl_name]도 상태는 비슷했다. 엘레드는 신음을 뱉으면서도 [pl_name][josa_eul_reul] 재촉했다." id c05_t_0891

    t horny3 "\"좋아! 빨리, 빨리 안에, 채워주게. 흐응! 나를, 자네의 것으로, 흐아으으읏-!!\"" id c05_t_0892

    #(mc 불컥불컥 싸는 컷인)
    #mcbeat)
    
    play channel1 "audio/effect/sqz3.mp3" volume 0.7
    show tiger_cg4_frame fr_03
    show tiger_cg4 im_16 mcbeat
    with vpunch

    c horny4 "\"크윽!\"" id c05_t_0893
    
    play channel2 "audio/effect/sqz4.mp3" volume 0.7
    show tiger_cg4_frame fr_03_1
    with vpunch

    "[pl_name][josa_eun_neun] 가장 깊숙이 꽂아 넣은 채로 절정했다. 힘차게 터져 나온 정액은 엘레드를 가득 채울 기세로 흘러나왔다." id c05_t_0894

    #17)
    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.45
    show tiger_cg4 im_17
    with vpunch
    pause 0.4
    with hpunch

    "엘레드 역시 진득한 정액을 분출했다. 창문까지 튀어서 흰 얼룩이 생기고 있었지만, 아무도 신경 쓰지 않았다." id c05_t_0895

    play sound "audio/effect/moaning_tiger2.mp3" volume 0.7
    t "\"그르르르...\"" id c05_t_0896

    play channel1 "effect/exhale.mp3" volume 0.7

    c "\"하아아...\"" id c05_t_0897

    #18)
    play channel1 "audio/effect/dickout2.mp3" volume 0.7
    hide tiger_cg4_frame
    show tiger_cg4_frame fr_04
    show tiger_cg4 im_18 surprise_no mcbeat_no tigerbeat_no
    with dissolve
    
    play sound "audio/effect/breath.mp3" volume 0.4
    
    "두 짐승은 숨을 고르며 사정 후의 여운에 빠져들었다." id c05_t_0898

    c horny3 "\"정말... 잊을 수 없는 맛이 맞네요.\"" id c05_t_0899

    t horny2 "\"당연하지. 크하하-...\"" id c05_t_0900
    
    stop sound fadeout 2.0

    #19, surprise)
    play channel2 "audio/effect/slap2.mp3" volume 0.8
    hide tiger_cg4_front2
    hide tiger_cg4_frame
    show tiger_cg4 im_19 spike tigerbeat
    show tiger_s4_hring_move
    show tiger_cg4_front2
    show tiger_cg4_frame fr_03_1
    with vpunch
    pause 0.5

    t horny3 "\"윽!...\"" id c05_t_0901

    "엘레드는 평소처럼 호탕하게 웃다가, 속에서부터 느껴지는 감각에 움찔했다." id c05_t_0902
    "[pl_name]의 자지는 아직도 빳빳하게 고개를 들고 있었다." id c05_t_0903

    c horny2 "\"아직 시간 있죠? 책상 위에 누워봐요.\"" id c05_t_0904

    t horny "\"하, 하하하! 이건 예상하지 못했는데...\"" id c05_t_0905

    hide tiger_cg4_frame
    with dissolve

    camera :
        ease 1.8 zpos 0

    pause 1.8

    $ renpy.end_replay()


label c5t_after:

    #음악
    #기사단 집무실
    scene bg office with Fade(0.8, 0.8, 0.8)
    play music "audio/the-long-way-home-259747.mp3" volume 0.6 fadein 1.0 

    "{i}잠시 후{/i}" id c05_t_0906

    show tiger smile_am
    with dissolve

    "엘레드는 평소보다 반짝반짝 빛나는 얼굴로 갑옷을 챙겨 입었다." id c05_t_0907
    
    "아까까지 쾌락에 허덕이던 얼굴이 생기가 넘치는 게 조금 짜증 날 지경이었다." id c05_t_0908
    
    c nake_d ddam2 "(이상하다... 저번에는 그렇다 치고, 왜 이번에도 나만 고생한 것 같지?)" id c05_t_0909

    play channel1 "effect/cloth.mp3" volume 0.6

    "[pl_name][josa_eun_neun] 엘레드가 건네준 망토로 끈적한 정액을 닦아냈다. 기사의 망토로 이래도 되나 싶지만, 적당한 물건이 없었다." id c05_t_0910
    
    show tiger talk_am am_u
    with dissolve
    
    t talk_am am_u "\"마음 같아선 직접 배웅해 주고 싶다만, 시간이 촉박하군.\"" id c05_t_0911

    show tiger base_am am_d
    with dissolve
    
    c out_d "\"그, 그건 제 탓이니까요. 하하...\"" id c05_t_0912

    play sound "audio/effect/puton.mp3" volume 0.5
    
    "[pl_name][josa_eun_neun] 민망한 웃음을 지으며 서둘러 옷을 입었다. 옷을 단정하게 입어도 제멋대로 뻗친 털을 숨길 수는 없었다." id c05_t_0913
    
    c sigh "(집에 돌아가면 제대로 씻어야겠다.)" id c05_t_0914

    show tiger talk_am am_u
    with dissolve
    
    t "\"테오와 마주치면 전부 눈치챌 것 같군... 자네도 잔소리에 폭격당하지 않게 조심하게.\"" id c05_t_0915

    show tiger base_am am_d
    with dissolve
    
    "엘레드는 [pl_name]에게 건물을 빙 둘러서 나가는 법을 가르쳐주었다." id c05_t_0916

    c consider "(이거 완전 경험자의 비법이잖아? 부단장을 피해 본 경험이 많았나본데...)" id c05_t_0917
    
    "[pl_name][josa_eun_neun] 마지막으로 가방을 챙기고 엘레드를 마주 보았다." id c05_t_0918

    c talk "\"그럼 다음에 또 뵙겠습니다.\"" id c05_t_0919

    show tiger happy_am am_u
    with dissolve
    
    t "\"그래. 오늘 아주 즐거웠다네.\"" id c05_t_0920
    
    "엘레드는 정말로 행복해 보이는 미소를 지었다." id c05_t_0921

    stop music fadeout 2.5

    # 기사단 본부 배경)
    
    scene bg knights_templar with Fade(0.8, 0.8, 0.8)
    play music "audio/the-legend-of-a-dance-212000.mp3" volume 0.5 fadein 2
    
    play sound "effect/footstep.mp3" volume 0.85

    "[pl_name][josa_eun_neun] 엘레드가 알려준 대로 뒷문을 찾아 걸어갔다." id c05_t_0922

    show cara out_d
    with dissolve

    c "(좀 전에는 안내가 있어서 괜찮았는데, 건물이 다 똑같이 생겨서 구분이 안 된다.)" id c05_t_0923

    show cara consider
    with dissolve

    c "(엘레드의 설명을 아예 지도로 그려둘 걸 그랬나?)" id c05_t_0924

    show cara base
    with dissolve

    "[pl_name][josa_eun_neun] 같은 길을 두 번 왕복하고 나서야 올바른 길을 찾았다. 해가 조금씩 낮아지고 있었다." id c05_t_0925
    
    show cara :
        ease 0.5 yoffset 30
    
    "중간에 기사를 한 명 마주쳤다가 어색하게 고개를 숙이고 빠르게 지나갔다." id c05_t_0926

    show cara :
        ease 0.5 yoffset 0

    c "(부단장이 아니라서 다행이지만, 조금 조심해야겠어...)" id c05_t_0927

    play sound "effect/footsteps.mp3" volume 0.9
    pause 2.5
    play channel1 "effect/cloth.mp3" volume 0.6
    hide cara
    with dissolve
    
    "[pl_name][josa_eun_neun] 기사들의 발걸음 소리가 들려서, 옆의 화단 뒤로 숨었다." id c05_t_0928
    "조경용 나무가 풍성해서 쉽게 들키진 않을 것 같았다." id c05_t_0929

    #기사들 한묶음으로 나오게
    
    show mob knights
    with dissolve

    knight "\"오늘 저녁 메뉴가 뭐지?\"" id c05_t_0929_1

    knight2 "\"뭔지 모르겠지만, 세 그릇은 먹을 수 있어.\"" id c05_t_0930

    knight3 "\"너네는 그 '손님' 덕분에 오늘 훈련 늦게 왔잖아.\"" id c05_t_0931
    
    knight2 "\"고작 15분 가지고 생색은...\"" id c05_t_0932

    c consider "(내 얘기잖아?)" id c05_t_0933
    
    "[pl_name][josa_eun_neun] 기사들의 얘기에 귀를 기울였다." id c05_t_0934

    knight3 "\"그래서 어떻게 생겼어?\"" id c05_t_0935
    
    knight2 "\"뭐... 단장님 취향대로 늘씬하게 생긴 늑대였는데.\"" id c05_t_0936
    
    c question2 "(엘레드 취향이 어떻길래...)" id c05_t_0937

    play sound "audio/effect/laugh.mp3" volume 0.65
    show mob at vshake (0.08, 0, -10)

    "너무 담백한 평가에 다른 기사가 웃음을 터트렸다." id c05_t_0938
    
    knight "\"너무 잘생겨서 제대로 표현을 못 하는 거 아냐?\"" id c05_t_0939
    
    knight3 "\"흠, 어떻게 생겼길래 그러는 거야?\"" id c05_t_0940
    
    "숨어있던 [pl_name][josa_eun_neun] 기사들의 대화가 끝나지 않아서 초조해졌다." id c05_t_0941
    "대화 내용도 신경 쓰이고, 숨어있다가 들키진 않을까 걱정했다." id c05_t_0942
    
    knight "\"분위기부터 보통이 아니라고.\"" id c05_t_0943
    
    knight "\"처음 봤을 땐 상인이 아니라 유명 음유시인인 줄 알았어. 갈색과 보라색 오드아이가 얼마나 신비로운지...\"" id c05_t_0944
    
    knight3 "\"또 얼굴만 보고 푹 빠졌군.\"" id c05_t_0945
    knight "\"아니, 너도 봤어야 해. 땀내 나는 기사들 틈에서 한 송이 꽃처럼 아름다운 모습을.\"" id c05_t_0946

    c ddam "(저렇게까지 말하니 좀 민망하네...)" id c05_t_0947
    
    knight3 "\"그렇게 예찬해 봤자 무슨 의미가 있나? 어차피 단장님 애인이겠지.\"" id c05_t_0948
    
    c exclamation "(!!...)" id c05_t_0949
    
    "[pl_name][josa_eun_neun] 애인이란 단어에 움찔했다." id c05_t_0950
    
    c consider "(내가 엘레드의 애인이라고? 그 정도 사이는 아닌데...)" id c05_t_0951
    
    knight "\"이번 애인은 얼마나 오래갈까?\"" id c05_t_0952
    
    knight2 "\"단장님 취향에 맞으면 한 달은 가겠지.\"" id c05_t_0953
    
    knight3 "\"에이, 잘 생겨도 한 달은 좀...\"" id c05_t_0954
    
    c "(무슨 애인이 한 달도 못 가고 바뀌어?)" id c05_t_0955
    c "(... 설마 나 같은 관계를 애인이라고 하는 건가? 하긴, 엘레드라면 그럴 수도 있지...)" id c05_t_0956
    
    "[pl_name][josa_eun_neun] 스스로 납득하며 기사들이 움직이길 기다렸다. 그러나 대화는 끝날 기미가 보이지 않았다." id c05_t_0957
    
    knight "\"그 정도 미모면 한 달 가능하지 않을까? 내기할래?\"" id c05_t_0958
    
    # (갑자기 엘레드 테오 등장)

    show mob :
        parallel :
            ease 1 alpha 0.75
        
        parallel :
            ease 1 zoom 0.95


    show theo at right
    with dissolve
    show tiger talk_am am_u at left
    with dissolve
    
    t "\"재밌겠군. 나는 한 달 넘는 것에 걸겠네.\"" id c05_t_0959

    show tiger base_am am_d
    with dissolve
    
    "갑자기 나타난 엘레드에 기사들은 자세를 바로잡았다." id c05_t_0960
    
    show mob at surprise_move
    knights "\"다, 단장님!...\"" id c05_t_0961
    
    "엘레드의 발언 내용에 테오는 뭐라 말하려다가 그만두었다. 대신 얼어있는 기사들에게 한마디 했다." id c05_t_0962

    show theo talk am_u
    with dissolve

    th "\"저녁 식사에 너무 늦지 않도록 해라.\"" id c05_t_0963

    show theo base am_d
    with dissolve
    
    knights "\"넵, 알겠습니다!\"" id c05_t_0964

    show tiger talk_am am_u
    with dissolve
    
    t "\"테오, 자네도 내기하지 않겠나?\"" id c05_t_0965

    show tiger base_am
    with dissolve
    show theo :
        ease 0.2 yoffset -20
        ease 0.2 yoffset 0
    
    "테오는 어이없다는 듯 어깨를 으쓱했다." id c05_t_0966

    show theo talk am_u
    with dissolve
    
    th "\"안 합니다.\"" id c05_t_0967

    show theo base am_d
    with dissolve
    
    "이미 엘레드에게 잔소리를 퍼부은 뒤라서, 테오는 짧게 할 말만 했다." id c05_t_0968

    show tiger talk_am
    with dissolve
    
    t "\"싱겁기는. 자네들은 빨리 식사하러 가게. 훈련하느라 고생했네.\"" id c05_t_0969

    show tiger base_am am_d
    with dissolve
    
    knights "\"넵, 감사합니다!\"" id c05_t_0970

    play sound "effect/footsteps.mp3" volume 0.9
    hide mob
    with dissolve
    
    "기사들은 절도 있는 자세로 저벅저벅 걸어갔다." id c05_t_0971
    "[pl_name][josa_eun_neun] 엘레드와 테오가 지나가기를 기다리고 있었다." id c05_t_0972

    show theo talk am_u
    with dissolve
    
    th "\"진심이야?\"" id c05_t_0973

    show theo base
    show tiger talk_am am_u
    with dissolve
    
    t "\"무슨 뜻이지?\"" id c05_t_0974

    show tiger base_am
    with dissolve
    
    "둘 사이에는 미묘한 침묵이 흘렀다. [pl_name][josa_eun_neun] 괜히 침을 꿀꺽 삼켰다." id c05_t_0975

    show theo talk
    with dissolve
    
    th "\"네가 '애인'이랑 오래 가는 걸 본 적이 없는데. 이번에는 다를 자신이 있어?\"" id c05_t_0976

    show theo base am_d
    with dissolve
    show tiger :
        ease 0.3 yoffset 15
        ease 0.3 yoffset 0
    
    "오랜 친구만이 할 수 있는 말에, 엘레드는 천천히 고개를 끄덕였다." id c05_t_0977

    show tiger talk_am am_u
    with dissolve
    
    t "\"... 그래.\"" id c05_t_0978

    show tiger base_am am_d
    with dissolve
    show theo at surprise_move        

    "테오는 흥미롭다는 듯 눈을 조금 크게 떴다." id c05_t_0979

    show theo talk am_u
    with dissolve

    th "\"드디어 애인 갈아치우는 건 그만둘 생각인가 봐?\"" id c05_t_0980

    show theo base am_d
    with dissolve
    show tiger talk_am am_u
    with dissolve

    t "\"그런 게 아니다. 나는...\"" id c05_t_0981

    show tiger sad2_am
    with dissolve

    t "\"내 마음조차 어떻게 해야 할지 모르겠어. [pl_name][josa_eul_reul] 생각할수록 자꾸 후회할 행동만 하고 있다고.\"" id c05_t_0982

    show theo talk am_u
    show tiger sad3_am
    with dissolve

    th "\"무슨 말을 하는 거야? 연애 처음 하는 애송이처럼...\"" id c05_t_0983

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (-330, -210)
    show tiger sad2_am
    with dissolve
    show theo base am_d
    with dissolve

    "테오의 어리둥절한 표정에 엘레드는 한숨을 푹 쉬었다." id c05_t_0984

    show tiger sad2_am am_u
    with dissolve

    t "\"그래, 어쩌면 이게 내 진정한 첫사랑일지도 몰라. 내 삶에서 이렇게 누군가를 원해본 적이 없었는데...\"" id c05_t_0985
    t "\"나는, 그를 진심으로 사랑해... 괴로울 정도로...\"" id c05_t_0986

    show tiger sad_am am_d
    with dissolve
    show theo talk am_u
    with dissolve

    th "\"무슨...\"" id c05_t_0987

    show theo base
    with dissolve

    camera :
        ease 0.1 ypos 10
        ease 0.1 ypos -10
        ease 0.1 ypos 0
    
    c exclamation "(뭐!?...)" id c05_t_0988
    
    "[pl_name][josa_eun_neun] 하마터면 테오와 동시에 입 밖으로 소리를 낼 뻔했다." id c05_t_0989
    
    c consider "(그냥 흔한 애인이 아니라, 진지하게 나를 사랑했다고?)" id c05_t_0990
    c "(그러면 그동안 나에게 했던 플러팅은 뭐였지? 엘레드의 진심은 대체...)" id c05_t_0991
    
    "[pl_name][josa_eun_neun] 머릿속이 복잡해졌다. 지금까지 엘레드와 있었던 일들이 엉망진창으로 섞여서 떠올랐다." id c05_t_0992
    
    c "(그런 방법밖에 몰랐던 걸까? 아니면 가벼운 마음으로 시작해서 점점 깊어진 걸까? 나를 사랑한다고?...)" id c05_t_0993
    
    "[pl_name][josa_eun_neun] 왠지 심장이 두근거리기 시작했다. 주변을 둘러보는 테오에게 심장 소리를 들키는 줄 알았다." id c05_t_0994
    
    show theo talk
    with dissolve

    th "\"하... 그러면 어쩔 생각인데? 첩으로 들이려고?\"" id c05_t_0995

    show theo base am_d
    show tiger fight_am
    with dissolve
    
    "엘레드는 화난 듯 얼굴을 찡그렸다가 억지로 표정을 폈다. 지금 엘레드는 화를 낼 입장이 아니었다." id c05_t_0996
    
    show tiger sad2_am am_u
    with dissolve

    t "\"[pl_name][josa_eun_neun]... 우리는 아직 그럴 수 있는 관계가 아니다.\"" id c05_t_0997

    show theo talk am_u
    with dissolve
    
    th "\"그러니까 지금 너 혼자 매달리고 있다는 거야? 허, 그동안 너에게 차인 수많은 남자가 들으면 아주 재밌어하겠군.\"" id c05_t_0998
    
    show theo base am_d
    with dissolve

    "테오는 약간의 비아냥을 담아서 웃었다. 그 엘레드가 사랑 때문에 마음고생한다는 사실이 놀라웠다." id c05_t_0999
    
    show tiger talk_am am_u
    with dissolve

    t "\"여러 번 고민했지만, 포기하고 싶지는 않다. 어떻게든 내 곁에 두고 싶다. 자꾸 농담인 척, 혼인하자고 말하고 싶고...\"" id c05_t_1000
    
    show tiger base_am
    with dissolve

    c exclamation "(... 혼인? 결혼하겠다고? 나랑?)" id c05_t_1001
    
    "혼인이라는 단어가 [pl_name]의 마음속에 푹 꽂혔다." id c05_t_1002
    
    c "(엘레드가 나와 진지하게 혼인하고 싶다고? 정말로?...)" id c05_t_1003

    "[pl_name][josa_eun_neun] 대화 내용을 따라가지 못할 정도로 생각이 많아졌다." id c05_t_1004

    "[pl_name][josa_i_ga] 혼자서 생각을 곱씹는 동안, 엘레드와 테오는 심각한 얘기를 했다." id c05_t_1005

    show theo talk am_u
    with dissolve

    th "\"하... 그렇게 진심이라면, 백작님을 설득할 생각은 있는 거지?\"" id c05_t_1006

    show theo base
    show tiger talk_am
    with dissolve

    t "\"해야지. 방법은 전혀 모르겠지만.\"" id c05_t_1007

    show tiger base_am am_d
    with dissolve

    "테오는 엘레드가 이렇게 자신 없는 말을 하는 것 자체가 이상하게 느껴졌다. 도저히 평소의 엘레드와 같은 호랑이가 아닌 것 같았다." id c05_t_1008
    
    show theo talk am_u
    with dissolve

    th "\"하... 네 아버지 성격이면 진짜 검부터 들 것 같아서 무섭다.\"" id c05_t_1009
    th "\"그때가 되면 네 목숨은 어떻게든 지켜줄 테니까, 지금은 그 애인한테나 잘해.\"" id c05_t_1010

    show theo base am_d
    show tiger sad2_am am_u
    with dissolve
    
    t "\"그래... 고맙다.\"" id c05_t_1011

    show tiger sad3_am am_u
    with dissolve
    show tiger :
        ease 0.3 yoffset 15
        ease 0.3 yoffset 0
    
    "엘레드는 귀가 축 처진 채 작게 고개를 끄덕였다." id c05_t_1012

    show theo talk am_u
    with dissolve
    
    th "\"그리고 네가 정말 진심이라면, 저번의 혼담도 제대로 거절해. 아버지 보기 껄끄러운 건 알겠지만...\"" id c05_t_1013
    
    show tiger sad2_am am_u
    show theo base am_d
    with dissolve

    t "\"알았다...\"" id c05_t_1014

    show tiger sad3_am am_d
    show theo talk am_u
    with dissolve
    
    th "\"얘기가 너무 길어졌군. 조금 뒤에 보자.\"" id c05_t_1015

    show theo base am_d at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85
    show theo at walk (1500, 2.8, 4)
    
    "테오는 슬퍼 보이는 엘레드를 두고 먼저 자리를 떠났다." id c05_t_1016
    
    c ddam "(혼담? 엘레드가 결혼할 상대가 있었단 말이야? 하긴 엘레드 나이면 이미 결혼 했을 법한데...)" id c05_t_1017
    c "(엘레드는 원래 그쪽이랑 결혼하려고 했던 걸까? 나는... '첩'이고? 으, 모르겠어.)" id c05_t_1018
    
    "[pl_name][josa_eun_neun] 현실적인 이야기에 심장이 차갑게 식는 느낌이 들었다. 정답 없는 생각을 계속할수록 스스로가 바보처럼 느껴졌다." id c05_t_1019
    
    # (엘레드 천천히 퇴장)

    show tiger at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85
    show tiger at walk (-1500, 2.8, 5)
    
    "멀어져가는 엘레드의 뒷모습에서 눈을 뗄 수 없었다." id c05_t_1020
    "엘레드가 무슨 생각을 하는지 너무나 궁금했지만, 동시에 진실을 알게 되면 실망할 것 같았다. [pl_name][josa_eun_neun] 빨리 집에 가고 싶어졌다." id c05_t_1021

    stop music fadeout 2.5

label c5t_end:

    # 가게 오후 배경
    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    "[pl_name][josa_i_ga] 가게에 돌아왔을 때는 이미 해가 뉘엿뉘엿 지고 있었다." id c05_t_1022

    show cara out_d
    with dissolve
    pause 1
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-100, -160)
    show cara sigh
    with dissolve

    "익숙한 공간에 돌아오자 마침내 긴장이 풀렸다. [pl_name][josa_eun_neun] 안도의 한숨을 내쉬며 축 늘어졌다." id c05_t_1023
    
    c out_d "(오늘따라 가방이 무겁네. 아, 금화가 들어있었지... 이것만 넣어두고 빨리 씻어야겠다.)" id c05_t_1024

    hide cara
    with dissolve
    
    "..." id c05_t_1025

    # (화면에 가헬)
    show wolf
    with dissolve
    with vpunch
    
    "창고에 잠깐 갔다 온 [pl_name][josa_eun_neun] 눈앞의 가헬을 보고 화들짝 놀랐다." id c05_t_1026
    
    c exclamation "\"!...\"" id c05_t_1027
    c ddam2 "\"아, 안녕. 저녁은 먹었어?\"" id c05_t_1028

    show wolf talk am_u
    with dissolve
    
    w "\"그래. 생각보다 늦게 돌아왔군. 기사단에서 무슨 일 있었나?\"" id c05_t_1029

    show wolf base am_d
    with dissolve
    
    "[pl_name][josa_eun_neun] 오늘 있었던 일이 떠올라서 당황했다." id c05_t_1030
    
    c "\"아니? 그냥, 견학을 좀 하느라...\"" id c05_t_1031
    
    "반사적으로 거짓말을 해버린 [pl_name][josa_eun_neun] 화제를 돌릴 궁리를 했다." id c05_t_1032
    
    c "\"많이 걸어서 그런가? 좀 피곤하네. 오늘은 일찍 잘게.\"" id c05_t_1033
    
    "[pl_name][josa_eun_neun] 가헬이 뭐라고 대답하기 전에 선수를 쳤다." id c05_t_1034
    "가헬은 허둥지둥 움직이는 [pl_name]의 모습에서 뭔가 위화감을 느꼈다." id c05_t_1035

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (1050, 50)
    show wolf fight3 am_u
    with dissolve
    
    w "\"...... !!\"" id c05_t_1036

    hide exclamation
    with dissolve
    
    "익숙하면서도 낯선 냄새가 희미하게 가헬의 코 끝을 스쳤다." id c05_t_1037
    "아주 희미해서 알아채기 힘들었지만, 비릿하고 짙은 수컷의 냄새 같았다." id c05_t_1038

    show wolf fight
    with dissolve
    
    w "(설마 엘레드랑...)" id c05_t_1039

    show wolf fight3
    with dissolve
    pause 0.2
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at fwalk

    pause 2.0
    play sound "effect/sniff.mp3" volume 0.4
    
    "가헬은 [pl_name]의 뒤에 가까이 붙어서 냄새를 맡았다." id c05_t_1040
    
    w "\"[pl_name]....\"" id c05_t_1041

    camera :
        ease 0.1 ypos 10
        ease 0.1 ypos -10
        ease 0.1 ypos 0

    
    "바로 뒤에서 들리는 가헬의 목소리에 [pl_name][josa_eun_neun] 조금 움찔했다." id c05_t_1042
    
    c "\"왜?\"" id c05_t_1043
    
    "가헬은 차마 엘레드와 무슨 일이 있었냐고 물어볼 수 없었다." id c05_t_1044
    "[pl_name]의 입으로 사실을 듣고 싶지 않았다." id c05_t_1045
    "가헬은 속으로만 끙끙대다가 결국 가게를 뛰쳐나갔다." id c05_t_1046
    
    # (가헬퇴장)
    show wolf am_d
    with dissolve
    pause 0.2

    play sound "effect/walk.mp3" volume 0.85
    show wolf at walk2 (-1600, 1.8, 5)
    
    c "\"가헬?\"" id c05_t_1047
    
    c "\"가헬! 어디 가?\"" id c05_t_1048
    
    c sigh "(갑자기 왜 저러지?)" id c05_t_1049
    
    "[pl_name][josa_eun_neun] 자꾸만 알 수 없는 상황이 생기는 게 답답했다." id c05_t_1050
    
    c ddam "(말도 없이 늦게 와서 화났나? 내가 뭐 잘못한 게 있나? 무슨 일인지 말이라도 하지...)" id c05_t_1051
    
    "각자 복잡한 마음을 안고 서로에게 등을 돌렸다. 무거운 감정에 발목이 잡힌 채, [pl_name][josa_eun_neun] 씻고 잠들 준비를 했다." id c05_t_1052

    # 챕터끝났다
    jump patreon_end