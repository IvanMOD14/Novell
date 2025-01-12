label c4t_start:

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
    $ tiger_route = True
    
    show screen book_icon with dissolve

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c04_t_0000

    show tiger am_d base_am
    with dissolve

    c talk "\"헛!...\"" id c04_t_0001

    "문이 열리는 소리에 [pl_name][josa_eun_neun] 퍼뜩 잠에서 깼다. 가게로 들어오는 엘레드가 보였다." id c04_t_0002

    show tiger am_u talk_am
    with dissolve

    t "\"안녕하신가!\"" id c04_t_0003

    show tiger am_d base_am
    with dissolve

    c "\"아, 안녕하십니까. 으음...\"" id c04_t_0004

    "[pl_name][josa_eun_neun] 벌떡 일어나서 눈을 비비며 잠기운을 털어냈다." id c04_t_0005

    c "\"(지금 몇 시지? 헉, 2시간이나 잤다고?)\"" id c04_t_0006
    c "\"(가헬이 깨웠을 법한데... 으, 일단 빨리 정신 차리자.)\"" id c04_t_0007

    "엘레드는 졸다가 깬 [pl_name][josa_eul_reul] 보고 귀엽다고 생각했다." id c04_t_0008
    "지금 엘레드는 [pl_name][josa_i_ga] 뭘 해도 좋게만 보일 것이다." id c04_t_0009

    show tiger am_u talk_am
    with dissolve

    t "\"하하, 자네의 자는 모습도 구경하고 싶군.\"" id c04_t_0010

    show tiger am_d base_am
    with dissolve

    "엘레드는 \'같은 침대에서\'라는 말을 붙이려다 말았다. 너무 직설적으로 말할수록 [pl_name][josa_i_ga] 더 도망가는 기분이었다." id c04_t_0011

    c "\"그, 그건 잘, 모르겠네요.\"" id c04_t_0012

    "잠이 덜 깬 [pl_name][josa_eun_neun] 엘레드의 속뜻을 알아차리지 못하고 엉뚱하게 대답했다." id c04_t_0013
    "얼굴 털이 눌리지는 않았는지 확인하다가 눈에 걸리는 게 있었다. 책상 위에 뭔가 쪽지가 올려져 있었다." id c04_t_0014

    c base "\"(아침 훈련하러 간다고?... 가헬이 남긴 쪽지구나. 어쩐지 안 깨운다 싶었는데...)\"" id c04_t_0015

    "[pl_name][josa_eun_neun] 머리를 쓸어넘기고 평소의 모습으로 엘레드에게 말했다." id c04_t_0016

    c talk "\"크흠! 평소보다 늦으셨네요, 엘레드 님. 오늘은 무슨 일로 오셨습니까?\"" id c04_t_0017

    show tiger sad3_am
    with dissolve

    "엘레드는 평소의 능글맞은 미소 대신, 미묘하게 슬픈 것 같은 표정을 지었다." id c04_t_0018

    show tiger am_u sad2_am
    with dissolve

    t "\"그렇게까지 격식 차릴 필요 없네...\"" id c04_t_0019

    show tiger am_d sad3_am
    with dissolve

    "엘레드는 [pl_name][josa_i_ga] 여전히 거리를 두는 것 같아 아쉬웠다. 첫 만남부터 본능적으로 유혹을 한 게 오히려 역효과였을지도 모른다." id c04_t_0020

    show tiger am_u talk_am
    with dissolve

    t "\"내가 너무 성급했던 것 같군. 자네와 친구부터 돼야 했던 건 아닐지, 후회하고 있다네. \"" id c04_t_0021

    show tiger am_d base_am
    with dissolve

    c consider "\"(친구? 엘레드랑? 기사단장씩이나 되는 귀족과 친해지면 좋은 일이지만, 글쎄...)\"" id c04_t_0022

    c "\"(\'개방적인 수인 사회\'라고 해도 귀족과 평민의 차이는 확실히 존재했다.)\"" id c04_t_0023

    c "\"(여러 가지 권리가 평민에게도 주어졌지만, 귀족들은 여전히 돈과 권력을 쥐고 있는 상위 계층이다.)\"" id c04_t_0024

    c "\"(정말로 격식 없는 사이가 될 수 있을지 모르겠다.)\"" id c04_t_0025

    "[pl_name][josa_eun_neun] 뭐라고 대답해야 할지 고민하다가 적당히 둘러대기로 했다." id c04_t_0026

    c talk "\"용건 없이 찾아올 정도면 이미 친구라고 할 수 있지 않을까요?\"" id c04_t_0027

    "엘레드는 씁쓸한 미소를 지으며 대답했다." id c04_t_0028

    show tiger am_u sad2_am
    with dissolve

    t "\"그것도 좋지만... 나는 이제 친구로 만족할 수 없네. 이미 자네에게 마음을 빼앗겨버렸거든.\"" id c04_t_0029

    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드의 진지한 표정에 다시 마음이 복잡해졌다." id c04_t_0030
    
    "어제는 아무런 결론도 내지 못했다. 오늘도 이렇다 할 대답이 있는 건 아니었다." id c04_t_0031

    c consider "\"(그런데 진짜로 엘레드와 연인이 될 수 있을까?)\"" id c04_t_0032

    "엘레드의 남편이 되는 상상을 하자 골치 아픈 일만 생각났다." id c04_t_0033
    "귀족과 평민의 결혼이 법으로 인정된 지 꽤 오래 지났지만, 엘레드의 가문에서 절대로 결혼을 허락할 것 같지 않았다." id c04_t_0034

    c "\"(엘레드의 가족이라... 유명한 기사 집안이라는 거 말고는 잘 모르겠네.)\"" id c04_t_0035
    c "\"(나 의외로 엘레드에 대해 아는 게 거의 없구나...)\"" id c04_t_0036

    "[pl_name][josa_eun_neun] 거절을 좀 더 예의 있게 말하기로 했다." id c04_t_0037

    c talk "\"원하는 대답을 드리지 못해서 죄송합니다. 저는 아직 마음의 준비가 안 됐습니다.\"" id c04_t_0038

    show tiger sad3_am
    with dissolve

    "[pl_name]의 대답에 엘레드는 곧바로 귀가 축 내려갔다. 슬픈 표정을 보고 [pl_name][josa_eun_neun] 아주 조금 양심의 가책을 느꼈다." id c04_t_0039

    show tiger am_u sad2_am
    with dissolve

    t "\"그, 그렇군. 알겠네...\"" id c04_t_0040

    show tiger am_d sad3_am
    with dissolve

    "엘레드의 말을 끝으로 죽음 같은 침묵이 이어졌다. 1초가 1시간 같은 순간이었다." id c04_t_0041

    c ddam2 "\"(윽, 딱히 꺼낼 화제도 없는데. 매몰차게 나가라고 할 수도 없고...)\"" id c04_t_0042

    "무거워진 분위기를 깨고 엘레드가 조용히 말했다." id c04_t_0043

    show tiger am_u sad2_am
    with dissolve

    t "\"... 혹시라도 자네의 마음을 돌릴 수 있다면, 무엇이든 하겠네.\"" id c04_t_0044

    show tiger am_d sad3_am
    with dissolve

    c consider "\"(무엇이든?)\"" id c04_t_0045

    "연애 소설에 나올 법한 말이긴 한데, [pl_name][josa_eun_neun] 엘레드가 정말로 \'무엇이든\' 할 거라고는 생각하지 않았다." id c04_t_0046
    
    "소설 속 목숨을 건 사랑 이야기는 소설일 뿐이다." id c04_t_0047

    c "\"(뭔가 노력하는 모습을 보인다면 생각이 바뀔지도 모를 일이지만... 글쎄...)\"" id c04_t_0048

    c talk "\"말씀만으로도 감사합니다.\"" id c04_t_0049

    "[pl_name]의 말에 엘레드는 거의 체념한 듯 평소 같은 웃음을 지었다." id c04_t_0050

    show tiger am_u happy2_am
    with dissolve

    t "\"지금은 친구라도 된 것에 만족해야겠군.\"" id c04_t_0051
    
    t "\"흠... 친구라면 이름 정도는 좀 더 편하게 불러야 하지 않겠나?\"" id c04_t_0052

    show tiger am_d base_am
    with dissolve

    c ddam2 "\"네? 제가, 엘레드 님을요?\"" id c04_t_0053

    "[pl_name][josa_eun_neun] 설마 하는 표정을 지었다." id c04_t_0054
    "아무 귀족 나부랭이도 아니고 이 지역의 기사단장인데, 엘레드 본인이 괜찮다고 해도 남들은 이상하게 볼 것 같았다." id c04_t_0055

    show tiger am_u smile_am
    with dissolve

    t "\"당연하지 않은가? 적어도 둘이 있을 땐 \'님\'을 붙이지 않아도 좋네.\"" id c04_t_0056

    c ddam2 "\"그, 그건 조금... 으음...\"" id c04_t_0057

    "고민하는 [pl_name]에게 엘레드는 쐐기를 박았다." id c04_t_0058

    t "\"빈말로 친구라고 하는 건 아닐 테지?\"" id c04_t_0059

    show tiger am_d base_am
    with dissolve

    "정곡을 찔린 [pl_name][josa_eun_neun] 일단 한발 물러서기로 했다." id c04_t_0060

    c "\"알겠습니다, 엘레드-\"" id c04_t_0061

    "[pl_name][josa_eun_neun] 자연스럽게 \'님\'을 붙일 뻔했다." id c04_t_0062

    c ddam "\"(어색해! 진짜 이래도 되나?)\"" id c04_t_0063

    show tiger am_u laugh_am
    with dissolve

    t "\"하핫! 금방 익숙해질걸세.\"" id c04_t_0064

    "아직 갈 길이 멀지만, 엘레드는 이제라도 둘 사이의 관계에 어떤 진전이 있다고 생각했다." id c04_t_0065

    t "\"그러면 오늘은-\"" id c04_t_0066
    
    show tiger am_d base_am
    with dissolve

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c04_t_0067

    # 가헬이 왼쪽에서 등장
    show tiger at mirror, right
    with dissolve 
    pause 0.5
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at mirror
    show wolf at change(1, -2000, 0)
    show wolf am_d base at walk (-500, 2.8, 5)

    w "\"...\"" id c04_t_0068

    "엘레드의 말은 가헬의 등장으로 갑자기 끊겼다. 찰나의 순간에 수인 셋이 서로 시선을 교환했다." id c04_t_0069
    "[pl_name][josa_eun_neun] 둘의 눈치를 보다가 입을 열었다." id c04_t_0070

    c ddam2 "\"아, 안녕. 훈련은 끝났나 보네?\"" id c04_t_0071

    show wolf talk
    with dissolve

    w "\"... 그렇다.\"" id c04_t_0072
    
    show wolf base
    with dissolve

    "가헬은 엘레드를 쳐다보고 가볍게 인사했다." id c04_t_0073

    show wolf am_u talk
    with dissolve

    w "\"어서 오십시오.\"" id c04_t_0074

    show wolf am_d base
    with dissolve

    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 3.4, 6)

    "그 말을 끝으로 가헬은 엘레드가 없는 것처럼 2층으로 올라갔다." id c04_t_0075

    "[pl_name][josa_eun_neun] 둘이 또 싸울까 봐 긴장했다가 마침내 숨을 푹 내쉬었다." id c04_t_0076

    hide wolf
    hide tiger
    show tiger
    with dissolve
    pause 0.5
    show tiger am_u talk_am
    with dissolve

    t "\"흠! 아무튼 오늘은 이것만 사고 가겠네.\"" id c04_t_0077

    show tiger base_am
    with dissolve

    "엘레드는 작은 허브 오일을 한 병 집어 들었다." id c04_t_0078

    # 오일 주고 씬 봤으면
    if oil==1 and tiger_see == 1 :

        show tiger talk_am
        with dissolve

        t "\"이게 꽤 괜찮더군. 내 취향에도 잘 맞고.\"" id c04_t_0079

        show tiger am_d base_am
        with dissolve

        c ddam2 "\"아, 하하... 그러시군요. 선물이 맘에 들었다니 다행입니다.\"" id c04_t_0080

        "[pl_name][josa_eun_neun] 엘레드가 허브 오일을 쓴 방법이 생각나서 조금 당황했다." id c04_t_0081
        "대화만 들으면 \'그런 용도\'라고 생각하지는 못할 것이다." id c04_t_0082

        c consider "\"(혹시 일부러 돌려 말한 건가?...)\"" id c04_t_0083

        "[pl_name][josa_eun_neun] 조금 고민하다가 괜히 신경 쓰지 않기로 했다. 동전이나 챙겨서 궤짝에 넣어뒀다." id c04_t_0084

    else :

        "엘레드는 가볍게 향을 맡아보고 말했다." id c04_t_0085

        show tiger talk_am
        with dissolve

        t "\"향이 깔끔해서 좋군. 어떤 허브가 들어갔나?\"" id c04_t_0086

        show tiger am_d base_am
        with dissolve

        c talk "\"라벤더와 로즈마리를 기본으로 타임을 약간 섞었습니다.\"" id c04_t_0087

        show tiger am_u talk_am
        with dissolve

        t "\"흐음... 끈적하진 않겠군?\"" id c04_t_0088

        show tiger am_d base_am
        with dissolve

        c consider "\"그렇... 죠? 첨가물을 넣으면 끈적하게 만들 수는 있지만-\"" id c04_t_0089

        "엘레드는 크게 웃으며 말했다." id c04_t_0090

        show tiger am_u laugh_am
        with dissolve

        t "\"크하하하! 그럴 필요는 없다네. 나는 미끈미끈한 게 조금 더 취향이라서 말이지.\"" id c04_t_0091

        "[pl_name][josa_eun_neun] 엘레드가 건네는 동전을 받으며 식은땀을 흘렸다." id c04_t_0092

        c ddam2 "\"(이것도 성희롱인가?... 아니, 됐다. 신경 쓰지 말자.)\"" id c04_t_0093
    
    show tiger am_u talk_am
    with dissolve

    t "\"다음에는 느긋하게 대화할 시간을 내서 오도록 하지.\"" id c04_t_0094

    show tiger am_d wink_am
    with dissolve

    "엘레드는 평소의 능글맞은 윙크를 했다." id c04_t_0095
    
    "[pl_name][josa_eun_neun] 자연스럽게 예법 차린 인사를 하려다가 멈칫했다." id c04_t_0096

    c consider "\"(적당히 가벼운 느낌은 어떻게 해야 하지...)\"" id c04_t_0097

    c talk "\"다음에 또 오세요.\"" id c04_t_0098

    "[pl_name][josa_eun_neun] 약간 어색하게 손을 흔들었다. 엘레드는 웃으면서 가게를 나갔다." id c04_t_0099

    show tiger smile_am at mirror
    with dissolve
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk (-1500, 2.8, 5)
    pause 2.5

    # 엘레드 나가고 문소리 딸랑
    play sound "audio/effect/bell.mp3" volume 0.6
    pause 1
    
    "[pl_name][josa_eun_neun] 크게 기지개를 켜면서 굳은 몸을 풀었다." id c04_t_0100
    "불편한 자세로 졸아서 그런지 별로 개운하지 않았다." id c04_t_0101

    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at change (1, 1800, 0)    
    show wolf at walk (0, 3.6, 6)

    "2층에서 가헬이 다시 내려오는 게 보였다." id c04_t_0102

    show wolf am_u talk
    with dissolve

    w "\"... 엘레드 경은 갔나 보군.\"" id c04_t_0103

    show wolf am_d base
    with dissolve

    "가헬은 [pl_name]의 옆에 붙어있는 호랑이가 사라져서 다행이라고 생각했다." id c04_t_0104

    c "\"응.\"" id c04_t_0105

    c base "\"(오늘은 둘이 안 싸워서 다행이다. 아니지? 둘이 지금보다 친하게 지낼 방법은 없을까?)\"" id c04_t_0106

    "[pl_name][josa_eun_neun] 가헬이 알게 되면 놀라서 펄쩍 뛸 생각을 했다." id c04_t_0107
    "아무것도 모르는 가헬은 가게가 깨끗한지, 상품이 잘 진열되어 있는지 신경 썼다." id c04_t_0108
    "가게 일을 도와주던 가헬은 묘하게 멍해 보이는 [pl_name][josa_i_ga] 신경 쓰였다." id c04_t_0109

    show wolf am_u talk
    with dissolve

    w "\"... 엘레드와 무슨 일 있었나?\"" id c04_t_0110

    show wolf am_d base
    with dissolve

    c ddam2 "\"아, 아니?\"" id c04_t_0111

    "별다른 일은 없었지만, [pl_name][josa_eun_neun] 흠칫 놀랐다. 괜히 몰래 뭔가 하다가 들킨 기분이었다." id c04_t_0112

    w "\"...\"" id c04_t_0113

    # 가헬 귀 추욱
    show wolf sad_am
    with dissolve

    w "\"......\"" id c04_t_0114

    "가헬은 뭐라도 말하려다가 그만뒀다." id c04_t_0115

    show wolf sad3_am
    with dissolve

    w "\"(내가 그럴 자격이 있나?)\"" id c04_t_0116

    "[pl_name][josa_eun_neun] 손님이 없는 틈에 재료를 손질했다. 가게에는 한동안 [pl_name]의 칼질 소리만이 감돌았다." id c04_t_0117

    # 가헬 다시 베이스 표정
    show wolf base
    with dissolve    

    c talk "\"아참. 내일은 시장에 갈 생각인데, 뭐 필요한 거 있어?\"" id c04_t_0118

    show wolf am_u talk
    with dissolve

    w "\"... 딱히 없다. 식재료만 보충하면 되겠군.\"" id c04_t_0119

    show wolf am_d base
    with dissolve

    c "\"그래...\"" id c04_t_0120

    c "\"(평소라면 같이 가자고 할 법도 한데? 어제부터 가헬 상태가 조금 이상하네. 좀 더 쉬게 해줘야 하나...)\"" id c04_t_0121

    "내일은 시장에 갈 예정이고, 그다음 날은 가게를 쉬는 날이다." id c04_t_0122
    "[pl_name][josa_eun_neun] 휴일에 뭘 할지 고민하며 재료 손질을 계속했다." id c04_t_0123

    stop music fadeout 2.5

label c4t_market:
    scene bg market with Fade(0.8, 0.8, 0.8)
    play music "audio/spirit-of-adventure-130563.mp3" volume 0.9 fadein 1.0  
    
    # 시장 낮 배경

    "{i}다음 날{/i}" id c04_t_0124

    show cara b_no am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 쪽지를 들고 시장을 돌아다녔다." id c04_t_0125

    c "\"(연금술 재료는 충분히 샀고, 식재료를 사려면 저쪽으로 가야겠군.)\"" id c04_t_0126

    "길거리를 걷는 와중에 [pl_name]의 옆으로 꽤 많은 수인이 우르르 지나갔다." id c04_t_0127

    play channel1 "effect/footstep.mp3" volume 0.85
    show cara at walk (500, 1.6, 3)
    
    "[pl_name][josa_eun_neun] 살짝 옆으로 피해서 수인들이 지나가기를 기다렸다." id c04_t_0128

    c "\"(뭐지? 저쪽에 뭐가 있나?)\"" id c04_t_0129

    "[pl_name][josa_eun_neun] 따라가 볼지 잠시 고민하다가 고개를 저었다." id c04_t_0130
    "눈치를 보아하니 다들 이미 뭔가를 사고 뿔뿔이 흩어지는 것 같았다. [pl_name][josa_eun_neun] 그대로 가던 길을 걸어갔다." id c04_t_0131

    play channel1 "effect/footstep.mp3" volume 0.85
    show cara at walk (0, 1.6, 3)    

    "중앙 교차로까지 가기도 전에, [pl_name][josa_eun_neun] 수인들이 몰려들었던 원인을 마주쳤다." id c04_t_0132

    # 아진 등장
    hide cara
    with dissolve
    pause 0.5     
    show ahjin b_no
    with dissolve

    $ unlock_character("ahjin")
    $ display_text = _("캐릭터 : 아진")
    show screen affection_indicator

    "노점상들 사이에, 눈에 띄게 특이한 상자들이 있었다. 그리고 그 앞에는 동방풍 옷을 입은 여우 수인이 서 있었다." id c04_t_0133
    "눈을 감고 있는 건지 시선을 알아채기 어려웠지만, 상대방이 [pl_name]의 시선을 알아채고 말을 걸었다." id c04_t_0134

    show ahjin am_u talk
    with dissolve
    
    n "\"어서 오세요. 마침 좋은 때에 오셨습니다. 곧 영업 종료에요.\"" id c04_t_0135

    show ahjin am_d base
    with dissolve
    
    "상인은 몇 가지 상품을 더 꺼내서 늘어놓았다. 뭐가 들었는지 알 수 없는 병과 특이하게 생긴 열매들이 눈길을 사로잡았다." id c04_t_0136
    
    c "\"어? 이건...\"" id c04_t_0137
    
    # 드래곤 고추
    show red_pepper :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    

    "[pl_name][josa_i_ga] 새빨간 열매를 알아보자마자, 상인은 곧바로 말을 이어 붙였다." id c04_t_0138

    show ahjin am_u talk
    with dissolve
    
    $ unlock_info_tag(3, "6")
    $ display_text = _("정보 : 드래곤고추")
    show screen affection_indicator
    n "\"오~ {color=#ee3939}'드래곤고추'{/color}를 좋아하시나요? 올해는 아주 잘 익어서 빛깔이 곱습니다.\"" id c04_t_0139

    show ahjin am_d base
    with dissolve

    c "\"(엄청 적극적으로 영업하네. 구경만 할까 했는데...)\"" id c04_t_0140

    # 고추 숨김
    hide red_pepper
    with dissolve  
    
    "[pl_name][josa_eun_neun] 살짝 긴장하며 대답했다."
    
    c talk "\"아, 아니요. 옛날에 딱 한 번 먹어봤던 게 생각나서요.\""
    
    c base "\"(스승님이 긴 방랑을 마치고 집으로 돌아올 때, 이것저것 신기한 것들을 가져오기도 했다.)\"" id c04_t_0141
    c "\"(그중에 이 향신료는 엄청나게 매워서 기억에 남아있다.)\"" id c04_t_0142
    c "\"(스승님은 과일 먹듯 씹어 먹었지만, 나는 조금만 맛봤을 뿐인데 혀가 불타버리는 느낌이었다.)\""  id c04_t_0143

    "[pl_name][josa_eun_neun] 류호가 떠올라서 조금 추억에 잠겼다. 아무래도 상인이 파는 상품은 대부분 동방에서 가져온 물건인 것 같았다." id c04_t_0144

    show ahjin am_u talk
    with dissolve
    
    n "\"이런, 동방 출신이 아니셨군요. 고향이 같은 줄 알고 넘겨짚고 말았네요~\"" id c04_t_0145
    
    "상인은 능청맞게 사과하고는 목을 가다듬었다." id c04_t_0146
    
    a "\"어흠! 제 소개부터 하지요. 제 이름은 \'아진\'입니다.\"" id c04_t_0147
    a "\"바다를 건너는 무역 상단 {color=#ee3939}\'진주 나침반\'{/color}의 주인이지요. 여기서는 주로 술과 향신료를 팔고 있습니다.\""
    
    show ahjin am_d base
    with dissolve

    "아진은 나긋나긋하게 움직이며 자기소개를 했다." id c04_t_0148
    "키는 [pl_name][josa_wa_gwa] 엇비슷해 보이지만, 체형 때문인지 전체적으로 길쭉해 보였다." id c04_t_0149
    "아진의 복장은 류호처럼 한 벌을 절묘하게 걸친 스타일이었다. 하지만 끈이나 문양이 류호의 것과는 사뭇 달랐다." id c04_t_0150
    
    c "\"(스승님이랑은 문화가 좀 다른가보다.)\"" id c04_t_0151

    "흰 털은 은빛으로 반짝거리며 윤기가 흐르고 있었다. 정교하게 세공된 단안경과 커다란 부채는 꽤 고급품으로 보였다. 무역상답게 돈을 잘 버는 듯했다." id c04_t_0152
    
    show ahjin am_u talk
    with dissolve

    a "\"궁금한 게 있다면 무엇이든 물어보세요. 용도별로 미리 조합된 향신료도 소량 남아있답니다.\"" id c04_t_0153

    show ahjin am_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 상품들을 둘러보며 살만한 게 있는지 고민했다." id c04_t_0154
    
    c "\"(어차피 식재료도 살 거니까, 향신료로 고기를 양념해서 구워볼까? 음, 동방의 술은 한 번도 안 마셔봐서 궁금하긴 한데... 으으, 고민된다. 차라리 추천을 받아볼까?)\"" id c04_t_0155
     
    menu :
        "요리에 쓸 향신료를 사자." :
            
            c talk "\"고기 구울 때 쓸 향신료 조합으로 주세요.\"" id c04_t_0156

            show ahjin am_u talk
            with dissolve

            a "\"그럼 \'임페리얼 드래곤\'으로 드리겠습니다. 동방풍 하면 떠오르는 익숙한 맛일 거에요.\"" id c04_t_0157

            show ahjin am_u base
            with dissolve
            
            "아진은 큰 주머니에서 유리병을 꺼냈다. 말려서 가루로 만든 향신료가 꽉 차 있었다." id c04_t_0158

            show ahjin am_u talk
            with dissolve

            a "\"앗? 이건 5병밖에 안 남았네요.\"" id c04_t_0159

            show ahjin am_d base
            with dissolve
            
            c "\"괜찮아요. 하나만 주세요.\"" id c04_t_0160

            "[pl_name][josa_eun_neun] 동전을 몇 개 건네고 유리병을 받았다." id c04_t_0161
            "아진의 말대로, 유리병에서는 먹어본 적 있는 요리의 향이 났다. 정확하게 기억나지는 않지만, 류호와 유명한 식당에 갔을 때 먹은 메뉴일 것이다." id c04_t_0162
            "트로나 왕국 수인들에게 가장 익숙한 동방의 맛일 테니, 아무래도 다들 많이 사 간 것 같다." id c04_t_0163

            show ahjin am_u talk
            with dissolve
            
            a "\"매운맛은 어떠신가요? \'홍옥 구름\'을 넣어 얼큰하게 끓인 국물이 해장용으로 아주 좋습니다.\"" id c04_t_0164

            show ahjin am_d base
            with dissolve
            
            c question2 "\"(매운맛의 수프라면, 스승님이랑 먹었던 그건가?)\"" id c04_t_0165
            
            "류호와 같이 지낼 때, 말린 생선과 야채로 끓인 맑은 수프를 먹은 적이 있다." id c04_t_0166
            "그때 류호는 본인 몫의 그릇에 자꾸만 향신료를 팍팍 넣어서 시뻘겋게 만들었던 게 기억났다." id c04_t_0167
            
            c base "\"(조금만 넣으면 괜찮겠지, 뭐.)\"" id c04_t_0168
            
            c talk "\"그럼 그것도 하나 주세요.\"" id c04_t_0169

            "[pl_name][josa_eun_neun] 향신료들을 가방에 챙겼다." id c04_t_0170

        "기분도 전환할 겸, 술을 사볼까?" :

            c talk "\"술은 무슨 종류가 있나요?\"" id c04_t_0171
            
            "아진은 술병 몇 개를 살짝 움직여서 두 종류로 구분했다." id c04_t_0172

            show ahjin am_u talk
            with dissolve
            
            a "\"이쪽이 곡주, 반대쪽이 과실주입니다. 이건 칸즈미로 만들어서 부드러운 단맛이 특징이죠. 좀 더 독한 걸 원하시면 하쿠린이 들어간 복숭아술도 있어요.\"" id c04_t_0173
            
            show ahjin am_u base
            with dissolve

            c ddam2 "\"(그, 그게 다 뭐지?)\"" id c04_t_0174

            "[pl_name][josa_eun_neun] 전혀 이해할 수 없는 재료에 조금 당황했다. 맛을 중점으로 골라야 할 것 같다." id c04_t_0175

            c talk "\"음, 새콤달콤한 것도 있나요? 쓴맛이 적어서 쉽게 마실 수 있는 걸로 사고 싶은데.\"" id c04_t_0176

            show ahjin am_u talk
            with dissolve
            
            a "\"그렇다면 역시 황금 이슬을 추천합니다. 으깬 매실을 발효시키고 꿀을 추가한, 아주 달콤한 술이죠.\"" id c04_t_0177

            show ahjin am_d base
            with dissolve
            
            "[pl_name][josa_eun_neun] 아진이 건네는 병을 받아서 들었다. 병 자체에도 뭔가 그림이 그려져 있었다." id c04_t_0178
            
            c ddam2 "\"(헉, 고급술인가? 괜히 사치 부리는 거 아닌지 모르겠네...)\"" id c04_t_0179
            
            "[pl_name]의 표정을 읽은 아진은 바로 말을 덧붙였다." id c04_t_0180

            show ahjin am_u talk
            with dissolve
            
            a "\"그렇게 비싼 술은 아닙니다. 비싼 술은 이미 다 팔았죠. 하핫.\"" id c04_t_0181

            show ahjin am_d base
            with dissolve
            
            "[pl_name][josa_eun_neun] 고민 끝에 술을 사기로 했다." id c04_t_0182
            
            c base "\"(여유가 있을 때 이런 것도 즐겨봐야지.)\"" id c04_t_0183

        "잘 팔리는 상품을 물어보자." :
            
            c talk "\"뭐가 제일 잘 팔리나요? 아까 다들 뭔가 사서 가던데.\"" id c04_t_0184

            show ahjin am_u talk
            with dissolve
            
            $ unlock_info_tag(3, "7")
            $ display_text = _("정보 : 용린과")
            show screen affection_indicator
    
            a "\"아, 이거 말입니까? {color=#ee3939}'용린과'{/color}라고 하는 건데...\"" id c04_t_0185

            # 용린과
            show dragon_fruit :
                xcenter 0.5
                ycenter 0.5
            with dissolve

            show ahjin am_u base
            with dissolve
            
            "아진은 주먹만 한 과일을 꺼내 보였다. 빼곡한 가시가 표면을 뒤덮은 모양새가 특이했다." id c04_t_0186

            show ahjin am_u talk
            with dissolve
            
            a "\"어째선지 여기서는 다들 \'천국의 과일\'이라고 하더군요.\"" id c04_t_0187

            hide dragon_fruit
            show ahjin am_d base
            with dissolve
            
            c "\"천국의 과일이면 설마, 그 전설의...?\"" id c04_t_0188
            
            "아진은 어깨를 살짝 으쓱하고는 대답했다." id c04_t_0189
            
            show ahjin am_u talk
            with dissolve
            
            a "\"네. 이 대륙의 용병왕이라는 자가 즐겨 먹었다고 하죠. 어디까지나 전설입니다만...\"" id c04_t_0190

            show ahjin am_d base
            with dissolve
            
            c base "\"(용병왕이 하룻밤에 10명의 남편을 모두 만족시킬 수 있었던 건, 천국의 과일을 먹어서라고 했는데.)\"" id c04_t_0191
            c consider "\"(에이, 아니겠지... 그게 진짜였으면 이미 너도나도 이것만 먹었겠지?)\"" id c04_t_0192
            
            "생각이 많아진 [pl_name]의 귀가 작게 팔랑거렸다." id c04_t_0193

            show ahjin am_u talk
            with dissolve
            
            a "\"표정을 보아하니 저랑 같은 생각이군요. 용린과는 영양분이 풍부해서 어느 정도 효과가 있을 수도 있겠지만, 무슨 마법의 과일은 아니니까요.\"" id c04_t_0194
            
            "아진은 고개를 가볍게 저으며 웃어 보였다." id c04_t_0195
            
            a "\"뭐, 그래도 전설 덕분에 잘 팔리긴 했습니다. 손님도 하나 어떠신가요?\"" id c04_t_0196

            show ahjin am_d base
            with dissolve
            
            c base "\"(사과 2개 가겪 밖에 안하잖아? 무슨 맛인지 궁금하니 사볼까?)\"" id c04_t_0197
            
            "[pl_name][josa_eun_neun] 동전을 주고 용린과를 받았다. 향이 나쁘지 않다고 생각하며 가방에 넣어두었다." id c04_t_0198
          
    "[pl_name][josa_eun_neun] 다른 상품들을 가볍게 둘러봤다." id c04_t_0199

    c base "\"(딱히 더 살 거 없겠지? 슬슬 식료품을 사러 가볼까.)\"" id c04_t_0200

    "그 순간, [pl_name]의 뒤에서 누군가가 불쑥 나타났다." id c04_t_0201

    show ahjin at left
    with dissolve
    show dragon b_no out_d base_out at right
    with dissolve
    pause 0.5

    show ahjin am_u talk
    with dissolve

    a "\"류호 씨 아니십니까?\"" id c04_t_0202

    show ahjin am_d base
    with dissolve

    c talk "\"어, 스승님?!\"" id c04_t_0203
    
    "예상치 못한 류호의 등장에 [pl_name][josa_eun_neun] 깜짝 놀랐다." id c04_t_0204
    "기약 없이 훌쩍 떠나버린 스승님을 이렇게 빨리 만나게 될 줄은 몰랐다." id c04_t_0205
    
    c base "\"(못해도 한 달 정도는 걸릴 줄 알았는데...)\"" id c04_t_0206
    
    "류호는 [pl_name][josa_eul_reul] 스윽 보고는 말했다." id c04_t_0207

    show dragon out_u talk_out
    with dissolve
    
    d "\"자네도 살 물건이 있소?\"" id c04_t_0208

    show dragon out_u base_out
    with dissolve
    
    c talk "\"아니요. 이미 샀습니다.\"" id c04_t_0209

    show dragon out_u talk_out
    with dissolve
    
    d "\"다행이군. 그럼 남은 술은 전부 내가 사겠네.\"" id c04_t_0210

    show dragon out_d base_out
    with dissolve
    
    show dragon at vshake (0.08, 0, -10)

    "류호는 아진이 진열해 놓은 술을 한 병씩 살펴보았다. 그리고 차례차례 소매 속으로 집어넣었다." id c04_t_0211

    "[pl_name][josa_eun_neun] 그것이 순간이동 마법이라는 걸 알아챘다. 류호에게는 숨 쉬는 것처럼 자연스러운 마법 사용이었다." id c04_t_0212

    show ahjin am_u talk
    with dissolve

    a "\"고향에 가시면 이것보다 더 좋은 술도 많을 텐데요.\"" id c04_t_0213

    show dragon out_u talk_out
    with dissolve

    d "\"뭐 그렇긴 하지. 자네가 들여온 좋은 술은 이미 귀족들이 다 사 갔을 테니.\"" id c04_t_0214

    show dragon out_d base_out
    with dissolve
    
    a "\"그건... 굳이 창고 정리 날에만 찾아오시는 류호 씨 탓 아닐까요?\"" id c04_t_0215

    show ahjin am_d base
    with dissolve
    
    c question2 "\"(귀족? 창고 정리?)\"" id c04_t_0216
    
    c talk "\"평소에는 귀족들 대상으로 거래하시나요?\"" id c04_t_0217
    
    "[pl_name]의 질문에 아진은 살짝 능청스럽게 대답했다." id c04_t_0218

    show ahjin am_u talk
    with dissolve
    
    a "\"네. 비싼 상품은 아무래도 돈이 많은 분께 팔고 있죠. 무역하는 값은 벌어야 하니까요.\"" id c04_t_0219

    show ahjin am_d base
    with dissolve
    
    c "\"(지금 파는 건 재고 처리에 가깝겠군. 당연한 일이지만...)\"" id c04_t_0220
    
    "속았다는 생각은 들지 않았다. 오히려 장사꾼의 수완이 큰 게 부럽다고 생각했다." id c04_t_0221
    
    c "\"(귀족 대상 상품이 있으면 돈을 잘 벌겠지?)\"" id c04_t_0222
    
    "무슨 상품을 만들지 고민하던 [pl_name][josa_eun_neun] 정작 귀족 사회에 대해 거의 모른다는 걸 다시 깨달았다." id c04_t_0223
    "눈앞에 있는 선배 장사꾼에게 살짝 떠보기로 마음먹었다." id c04_t_0224
    
    c "\"귀족분들을 많이 만난다면 요즘 귀족 사이 소문 같은 것도 잘 아시겠네요?\"" id c04_t_0225

    show ahjin am_u talk
    with dissolve
    
    $ unlock_info_tag(4, "1")
    $ display_text = _("정보 : 정보 길드")
    show screen affection_indicator
    
    a "\"아핫! 손님, {color=#ee3939}'정보 길드'{/color} 소속은 아니지요?\"" id c04_t_0226

    show ahjin am_u base
    with dissolve
    
    c ddam2 "\"네?\"" id c04_t_0227

    show ahjin am_d
    with dissolve
    show ahjin am_u
    with dissolve

    "아진은 접은 부채를 까딱거리며 웃었다. 뜬금없는 대답에 당황한 [pl_name][josa_eul_reul] 보며 아진은 말을 이었다." id c04_t_0228

    show ahjin am_u talk
    with dissolve

    a "\"으흠, 아닙니다. 좀 더 직설적으로 말씀하시지요. 귀족과 관련해서 무엇이 궁금하십니까?\"" id c04_t_0229

    show ahjin am_d base
    with dissolve
    
    "아진이 \'어설픈 정보 캐기\'에 웃음이 터졌다는 걸 눈치챈 [pl_name][josa_eun_neun] 살짝 부끄러워졌다." id c04_t_0230

    "그래도 아진이 주는 기회를 붙잡을 생각이었다." id c04_t_0231

    c consider "\"(귀족의 문화 전반에 관해 물어봤자 대답하기 어려울 테고. 귀족, 귀족이라...)\"" id c04_t_0232

    "[pl_name][josa_eun_neun] 순간 어제의 엘레드가 떠올랐다." id c04_t_0233

    c talk "\"이 지역 백작님 휘하... 반슈타인 기사단의 단장을 아시나요?\"" id c04_t_0234

    show ahjin am_u talk
    with dissolve

    a "\"기사단장이라면, 그 바람둥이로 유명한 호랑이 말이군요. 혹시 손님은...\"" id c04_t_0235

    show ahjin am_u base
    with dissolve
    
    c ddam2 "\"아, 아니요!\"" id c04_t_0236
    
    "[pl_name][josa_eun_neun] 아진의 말을 단칼에 끊으며 대답했다." id c04_t_0237
    
    c talk "\"그, 엘레드 경의 가문에 대해 정보가 있나 해서요.\"" id c04_t_0238

    show ahjin am_u consider
    with dissolve
    
    a "\"판테라? 흐음... 거기 하인 말로는 가주가 후계자 문제로 골머리를 썩인다고 했습니다.\"" id c04_t_0239
    a "\"신경질이라도 부리는지 하인 얼굴이 핼쑥했지요. 음, 주로 독한 술을 사 가더군요.\"" id c04_t_0240

    show ahjin am_d base
    with dissolve
    
    "[pl_name]의 머릿속에는 독한 술에 취해서 성질부리는 가상의 호랑이가 그려졌다. 골칫덩이 아들과 분노한 아버지의 관계가 자연스레 완성됐다." id c04_t_0241
    "추측일 뿐이지만, 엘레드의 소문을 고려하면 충분히 가능한 일이었다." id c04_t_0242
    
    c talk "\"말해주셔서 감사합니다.\"" id c04_t_0243

    show ahjin am_u talk
    with dissolve
    
    a "\"이 정도 얘기는 아까 구매하신 상품에 덤으로 드리지요. 하하.\"" id c04_t_0244

    show ahjin am_d base
    with dissolve
    show dragon at vshake (0.08, 0, -10)
    
    "아진이 넉살 좋게 대답하는 동안, 류호는 모든 술을 소매 속으로 쓸어 담았다." id c04_t_0245
    "아진은 그 타이밍에 맞춰 류호에게 말을 꺼냈다." id c04_t_0246

    show ahjin am_u talk
    with dissolve
    
    a "\"그래서 이번에는 또 무슨 보물로 값을 치르실 건가요?\"" id c04_t_0247

    show ahjin am_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 류호가 보석이나 다른 보물들을 돈 대신 쓰던 게 생각났다. 아진에겐 아예 익숙한 일인 듯했다." id c04_t_0248
    
    c ddam2 "\"(대부분의 상점에선 안 받아주니까 제발 금화를 쓰라고 말했었는데...)\"" id c04_t_0249

    show dragon out_u talk_out
    with dissolve

    d "\"오늘은 금화가 있다네. 아까 식당에서 자꾸 귀찮게 굴어서 말이지.\"" id c04_t_0250

    show dragon out_d base_out
    with dissolve

    "[pl_name][josa_eun_neun] 무슨 일이 있었는지 대충 상상할 수 있었다. 아진도 비슷한지 금화를 받으면서 작게 웃었다." id c04_t_0251

    c consider "\"(둘이 되게 친한 사이인가 보네.)\"" id c04_t_0252
    
    "[pl_name][josa_eun_neun] 류호가 떠나가기 전에 빨리 질문하기로 했다." id c04_t_0253

    c talk "\"스승님은 아진 씨와 아주 친하신가봐요?\"" id c04_t_0254

    show dragon out_u talk_out
    with dissolve
    
    d "\"뭐, 그런 셈이오.\"" id c04_t_0255

    show dragon out_d base_out
    with dissolve
    show ahjin am_u talk
    with dissolve
    
    a "\"대답이 너무하지 않으십니까. 격식 없는 사이는 아니지만, 친구라고 할 정도로 오래 보긴 했지요.\"" id c04_t_0256

    show ahjin am_u base
    with dissolve
    
    c question2 "\"(핀잔을 줄 정도면 정말 친한가본데? 옛날부터 알던 사이면 얼마나 오래된 걸까?)\"" id c04_t_0257
    c "\"(설마... 저분도 스승님처럼 막 몇백 살인가?)\"" id c04_t_0258
    
    "[pl_name][josa_eun_neun] 짧은 시간에 둘의 관계를 상상하다가 갑자기 자신의 처지가 떠올랐다." id c04_t_0259
    "스승님에게 자신은 거의 얼굴만 아는 사이가 아닌가 하는 생각이 들었다." id c04_t_0260
    "제자라는 사실을 인정받은 것과 별개로, 친하다고 할 수 있는 관계는 아니었다." id c04_t_0261

    show ahjin am_u talk
    with dissolve
    
    a "\"손님도 류호 씨를 잘 알고 계시는 것 같은데요.\"" id c04_t_0262

    show ahjin am_d base
    with dissolve
    
    c talk "\"아, 저는, 제자 [pl_name]입니다.\"" id c04_t_0263
    
    "[pl_name][josa_eun_neun] 약간 어색하게 고개를 숙였다." id c04_t_0264
    
    c base "\"(스승님의 친구라면 최소한의 예의는 차려야지...)\"" id c04_t_0265
    
    "[pl_name][josa_eun_neun] 류호의 기억 봉인을 생각하자 다시 마음이 복잡해졌다." id c04_t_0266
    "지금 생각하니 류호의 말투도 미묘하게 거리감이 생긴 것 같았다." id c04_t_0267

    show ahjin am_u talk
    with dissolve
    
    a "\"정말로 제자를 들이셨군요.\"" id c04_t_0268

    show ahjin am_d base
    show dragon out_u talk_out
    with dissolve
    
    d "\"이제는 잘 성장하여 자네처럼 상인을 하고 있지.\"" id c04_t_0269

    show dragon out_d base_out
    with dissolve
    
    "아진이 흥미롭다는 듯 고개를 기울이자, [pl_name][josa_eun_neun] 손사래를 쳤다." id c04_t_0270
    
    c talk "\"상단 같은 건 아니고, 저쪽 뒷골목 3번째 줄에 작은 마법 상점을 하고 있어요.\"" id c04_t_0271

    show ahjin am_u talk
    with dissolve
    
    a "\"그것도 충분히 멋진 일이네요.\"" id c04_t_0272

    show ahjin am_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 조금 머쓱한 기분에 어색하게 웃으며 귀를 팔랑거렸다." id c04_t_0273
    
    c question2 "\"(잠깐, 아진 씨는 과거의 제자들을 알고 있나?)\"" id c04_t_0274
    
    "[pl_name][josa_eun_neun] 류호의 옛 제자에 대한 얘기가 떠올랐다." id c04_t_0275

    "그때 류호의 표정이 좋지 않아서 물어보지 못했다. 지금 꺼낼만한 얘기도 아니었다." id c04_t_0276

    c consider "\"(기억 봉인 때문에 앞으로도 물어보긴 어렵겠네...)\"" id c04_t_0277

    "[pl_name][josa_eun_neun] 속으로 결론을 내렸다. 궁금해도 별수 없는 일이었다." id c04_t_0278

    show dragon out_u talk_out
    with dissolve

    d "\"아무튼, 볼일이 끝났으니 나는 이만 가보겠네.\"" id c04_t_0279

    show dragon out_d base_out
    with dissolve

    show cloud1 at right, cloud_rise
    with dissolve
    show cloud2 at right, cloud_rise2
    with dissolve
    show cloud3 at right, cloud_rise3
    with dissolve

    pause 1.5
    
    hide dragon
    with dissolve

    hide cloud1
    hide cloud2
    hide cloud3
    with dissolve
    
    "류호는 간단한 작별 인사를 남기고 사라졌다." id c04_t_0280

    "[pl_name][josa_eun_neun] 순식간에 사라져 버린 류호에게 인사도 하지 못했다." id c04_t_0281

    hide ahjin
    with dissolve
    show ahjin b_no am_u consider
    with dissolve

    a "\"이것 참, 맨날 바람처럼 왔다가 가는군요.\"" id c04_t_0282

    show ahjin am_d base
    with dissolve
    
    c talk "\"제 가게에 올 때도 창고 안에 뿅 나타나셨어요.\"" id c04_t_0283
    
    "[pl_name][josa_eun_neun] 어깨를 으쓱하고는 고개를 저었다. 아진은 작게 웃다가 말했다." id c04_t_0284

    show ahjin am_u talk
    with dissolve
    
    a "\"아, 수다 떨다가 시간이 이렇게 흘렀는지도 몰랐네요.\"" id c04_t_0285

    show ahjin am_d base
    with dissolve
    
    c "\"맞다. 곧 영업 종료라고 했었죠. 그러면 저도 이만 가보겠습니다.\"" id c04_t_0286
    
    "[pl_name][josa_i_ga] 작게 고개를 숙이자, 아진도 마주 고개를 숙였다." id c04_t_0287

    show ahjin am_u talk
    with dissolve
    
    a "\"덕분에 즐거웠습니다. 안녕히 가세요.\"" id c04_t_0288
    
    "[pl_name][josa_eun_neun] 매대를 정리하는 아진을 뒤로하고, 원래 사려던 식재료를 사러 걸어갔다." id c04_t_0289

    stop music fadeout 2.5

    show backcol :
        alpha 0.7
    hide ahjin
    show ahjin am_u base
    with Dissolve(1.0)
    
    a "\"흠...\"" id c04_t_0290

    #아진 눈 번쩍!
    play sound "effect/magic.mp3" volume 0.65
    pause 0.4
    show ahjin am_u eye_bright
    with dissolve    
    
    "아진이 눈을 뜨자 가려져있던 그의 눈동자가 드러났다." id c04_t_0291
    "잘 세공된 아쿠아마린처럼 눈부시게 빛나는 하늘색 눈동자였다. 날카로운 눈매는 아진의 인상을 크게 바꾸었다." id c04_t_0292
    "아진은 멀리 사라지는 [pl_name]의 뒷모습을 보고 혼잣말했다." id c04_t_0293

    show ahjin am_u talk2
    with dissolve
    
    a "\"스승과 제자에게 똑같은 문제가 있다니, 흥미로운 일이야...\"" id c04_t_0294
    
    "아진이 무엇을 보았는지 [pl_name][josa_i_ga] 알 방법은 없었다." id c04_t_0295


label c4t_shop:
    #가게 낮 배경
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40
    scene bg shop
    with Fade(0.8, 0.8, 0.8)

    "{i}다음 날 오후{/i}" id c04_t_0296

    show cara
    with dissolve

    "휴일의 아침을 늦잠으로 보낸 [pl_name][josa_eun_neun], 나른한 오후를 독서로 보내고 있었다." id c04_t_0297
    
    "나중에 읽을 생각으로 사뒀던 마법 관련 서적을 붙들고 있었다." id c04_t_0298

    show cara consider
    with dissolve
    
    c "\"(\'공격 마법 입문서\'라면서 뭐 이렇게 복잡하게 설명하지?)\"" id c04_t_0299
    
    "서장에는 세계의 원리와 마법의 경이로움 같은 관심 없는 내용만 있어서 넘겨버렸다." id c04_t_0300

    show cara base
    with dissolve
    
    "이미 알고 있는 마나 사용법은 복습 삼아 대충 읽었다." id c04_t_0301
    
    "앞쪽의 쓸데없는 소리를 제외하고, 타격계는 뾰족하게 만들고 속성계는 둥글게 만들라는 내용이 핵심이었다." id c04_t_0302
    
    c "\"(입문용 공간 마법 같은 건 없나보다.)\"" id c04_t_0303
    
    "[pl_name][josa_eun_neun] 목차를 펼쳐 봤다가 책을 빠르게 휘리릭 넘겨보고, 다시 보던 곳으로 돌아왔다." id c04_t_0304
    
    "불 마법의 주의 사항 부분은 의외로 읽을 만했다. \'시전자가 데이지 않는 화염구 만들기\'의 역사가 간략하게 적혀있었다." id c04_t_0305
    
    "하지만 [pl_name][josa_i_ga] 원하던 내용은 별로 없었다." id c04_t_0306
    
    "예시로 들어간 마법 술식 그림이 많지 않았고, \'위력과 마나 소모량의 적절한 타협점\' 같은 건 아예 언급도 없었다." id c04_t_0307

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-110, -160)
    show cara am_u sigh
    with dissolve

    c "\"(어휴, 이런 것까지 논문을 구매해야 하나?...)\"" id c04_t_0308
    
    "마탑에서는 최신 정보를 풀지도 않고, 어느 정도 기간이 지난 논문만 외부로 판매하고 있었다." id c04_t_0309

    show cara am_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 연금술 관련 자료는 조금 구매했지만, 다른 분야는 큰돈을 쓸 정도로 급하진 않았다." id c04_t_0310
    
    "[pl_name][josa_eun_neun] 일단 책을 더 읽어보기로 마음먹었다." id c04_t_0311

    hide cara
    with dissolve
    
    "..." id c04_t_0312

    play sound "audio/effect/bell.mp3" volume 0.6
    pause 0.2
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at mirror
    show wolf at change (1, -1800, 0)
    show wolf at walk (0, 3.6, 6)

    "{i}딸랑~{/i}"  

    "글자에 푹 빠진 [pl_name][josa_eun_neun] 가헬이 가게로 돌아온 것도 눈치채지 못하고 있었다." id c04_t_0313
    
    "가헬은 집중한 [pl_name]의 모습을 보고 있다가 조용히 말했다." id c04_t_0314

    show wolf am_u talk
    with dissolve
    
    w "\"... [pl_name]?\"" id c04_t_0315

    show wolf am_d base
    with dissolve
    
    c ddam2 "\"어, 언제 왔어?\"" id c04_t_0316
    
    "[pl_name][josa_i_ga] 고개를 들자, 책 위로 가헬의 모습이 보였다." id c04_t_0317

    show wolf am_u talk
    with dissolve
    
    w "\"방금 돌아왔다.\"" id c04_t_0318

    show wolf am_u base
    with dissolve
    
    c talk "\"쉬는 날에도 훈련이라니, 너무 몸을 혹사하는 거 아냐?\"" id c04_t_0319

    show wolf am_u talk
    with dissolve
    
    w "\"괜찮다.\"" id c04_t_0320

    show wolf am_d base
    with dissolve
    pause 0.5
    show wolf am_d embarrass
    with dissolve
    pause 1
    show wolf am_d base
    with dissolve  

    "가헬은 뭔가 더 말하려는 듯하다가 우물쭈물했다. 미묘하게 시선을 피했다가 다시 마주하는 가헬이 이상했다." id c04_t_0321
    
    "[pl_name][josa_eun_neun] 책을 다시 읽으려다가 말고 가헬에게 질문했다." id c04_t_0322

    c question2 "\"왜 그래?\"" id c04_t_0323

    show wolf am_u talk
    with dissolve
    
    w "\"... 오늘은 같이 술집에 갔으면 한다.\"" id c04_t_0324

    show wolf am_d base
    with dissolve
    
    c consider "\"(아 맞다. 며칠 전에도 얘기했었지. 왜 저렇게 긴장하면서 말하지?...)\"" id c04_t_0325
    
    c talk "\"그래. 알았-\"" id c04_t_0326

    play sound "effect/door_knock_weak.mp3" volume 0.9
    "{i}똑똑{/i}" id c04_t_0327
    
    "[pl_name][josa_i_ga] 대답하는 것과 동시에, 누군가 가게의 문을 두드렸다." id c04_t_0328

    "[pl_name][josa_eun_neun] 읽던 책을 덮어놓으며 고개를 갸웃했다." id c04_t_0329

    c question2 "\"누구지? 쉬는 날에 무슨 일로...\"" id c04_t_0330

    "[pl_name][josa_i_ga] 자리에서 일어났지만, 가헬이 한발 먼저 문으로 향했다." id c04_t_0331

    play sound "audio/effect/bell.mp3" volume 0.6
    
    "가헬이 문을 열자 거대한 체구와 그보다 큰 목소리가 가게 앞에 나타났다." id c04_t_0332
    
    # 엘레드 화면 왼쪽에 등장
    hide wolf
    with dissolve
    show wolf
    with dissolve
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger am_u laugh_am at change (1, -1600, 0)
    show tiger at walk (-750, 2.8 , 5)
    with dissolve

    t "\"[pl_name]! 휴일에 찾아와서 미안하- ...\"" id c04_t_0333
    
    show tiger am_d base_am
    with dissolve

    w "\"...\"" id c04_t_0334
    
    "덩치 큰 수인 둘이 좁은 문을 꽉 채우고 서로 시선을 교환했다. 찰나의 순간에 수많은 생각과 날카로운 눈빛이 둘 사이를 오갔다." id c04_t_0335
    "가헬은 이대로 확 문을 닫아버리고 싶은 마음을 억누르며 말했다." id c04_t_0336

    show wolf am_u talk
    with dissolve

    w "\"그래서, 무슨 용건입니까.\"" id c04_t_0337

    show wolf am_d base
    show tiger am_u talk_am
    with dissolve
    
    t "\"흠? 자네에게는 용건 없네.\"" id c04_t_0338

    show tiger am_d base_am
    with dissolve
    
    "말 한번 주고받았을 뿐인데 분위기가 험악해졌다. 둘 사이에 천둥번개라도 치는 것 같았다." id c04_t_0339
    
    c sigh "\"(아이고... 또 시작이네.)\"" id c04_t_0340
    
    "[pl_name][josa_eun_neun] 골치가 아파지기 시작했다. 둘이 으르렁거리기 전에 일단 떼어놓기로 했다." id c04_t_0341

    c base "\"(빨리 용건만 듣고 나가야지...)\"" id c04_t_0342
    c talk "\"일단 들어오세요, 엘레드 님.\"" id c04_t_0343
    
    # 가헬과 엘레드 위치 평범하게 좌우로
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at walk (500, 1.6 , 3)
    pause 0.7
    show tiger smile_am
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85
    show tiger at walk (-500, 1.2 , 2)
    pause 0.5       

    "가헬이 조금 비켜서자 엘레드가 가게 안으로 들어올 수 있었다. 엘레드는 전쟁에서 이긴 장군처럼 의기양양하게 들어왔다." id c04_t_0344

    show tiger am_u talk_am
    with dissolve
    
    t "\"휴일에 찾아와서 미안하네. 하지만 휴일이라서 온 것이지. 오늘, 같이 술집에 가지 않겠나?\"" id c04_t_0345

    show tiger am_u base_am
    with dissolve

    c "\"네?!\"" id c04_t_0346

    show tiger :
        ease 0.2 yoffset -10 
        ease 0.2 yoffset 0 
    
    "우연의 일치겠지만, 술집 얘기가 또 나와서 [pl_name][josa_eun_neun] 깜짝 놀랐다." id c04_t_0347

    "너무 크게 외쳐버린 [pl_name] 때문에 엘레드도 덩달아 흠칫했다. 가헬도 입 밖으로 소리를 내진 않았지만 약간 놀랐다." id c04_t_0348

    "방금까지의 태도는 어디로 갔는지, 엘레드는 조금 주춤하며 말을 덧붙였다." id c04_t_0349

    show tiger am_d talk_am
    with dissolve
    
    t "\"아, 술집은 싫은가? 다른 곳도 상관없다만...\"" id c04_t_0350

    show tiger am_d base_am
    with dissolve
        
    "가헬은 아까의 엘레드와 비슷한 \'승리자의 표정\'으로 말에 끼어들었다." id c04_t_0351

    show wolf am_u smile
    with dissolve
    
    w "\"이미 저와 술집에 가기로 했습니다. 오늘, 지금.\"" id c04_t_0352

    show wolf am_d smile
    with dissolve

    show tiger am_d sad3_am
    with dissolve
    
    "가헬의 말에 엘레드는 말문이 막혔다. 맑은 하늘에 갑자기 먹구름이 낀 듯, 엘레드의 표정은 급격히 어두워졌다." id c04_t_0353
    "[pl_name][josa_i_ga] 보기에도 처량할 지경이었다." id c04_t_0354
    
    c question2 "\"(근데 왜 술집이지? 오늘 술집에 뭔가 있나?)\"" id c04_t_0355
    
    "[pl_name][josa_i_ga] 잘못된 추측에 빠진 사이, 가헬은 엘레드를 가볍게 비웃으며 말했다." id c04_t_0356

    show wolf am_u talk
    with dissolve
    
    w "\"그러니 엘레드 경은 이만 돌아가 주십시오.\"" id c04_t_0357

    show wolf am_d base
    with dissolve

    show tiger am_u sad2_am
    with dissolve
    
    t "\"으음... 선약이라면 어쩔 수 없군.\"" id c04_t_0358

    show tiger am_d sad3_am
    with dissolve
    
    "엘레드는 가헬의 강경한 태도에 한발 물러서는 듯했다." id c04_t_0359

    show tiger am_u sad2_am
    with dissolve
    
    t "\"그러면 먼저 가 있겠네. 술집에서 만나도록 하지.\"" id c04_t_0360

    show tiger am_d sad3_am
    with dissolve
    
    "갑자기 태도를 바꾸며 윙크하는 엘레드 때문에 [pl_name]도 가헬도 황당하다는 표정을 지었다." id c04_t_0361

    c consider "\"(이건 절박한 거야, 능글맞은 거야? 평소에는 이런 느낌이 아니었는데...)\"" id c04_t_0362
    
    "엘레드의 상태가 이상하다고 생각하며, [pl_name][josa_eun_neun] 엘레드의 의도를 추측했다." id c04_t_0363
    
    c talk "\"중요한 얘기라면 여기서 하는 게 낫지 않을까요? 술집은 듣는 귀도 많고...\"" id c04_t_0364

    show tiger am_u sad2_am
    with dissolve
    
    t "\"아니, 그저 친구와 같이 휴일을 보내고 싶을 뿐이라네.\"" id c04_t_0365

    show tiger am_d sad3_am
    with dissolve
    
    "엘레드는 평범하게 진실을 말했으나, [pl_name][josa_eun_neun] 엘레드가 뭔가 숨기고 있는 건 아닌지 고민했다." id c04_t_0366
    "가헬도 엘레드의 발언을 의심스럽게 생각했다." id c04_t_0367
    
    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (1420, 0)
    show wolf am_u talk
    with dissolve
    
    w "\"친구?\"" id c04_t_0368

    hide question
    show wolf am_d base
    with dissolve

    show tiger am_d smile_am
    with dissolve

    t "\"아, 자네는 모르는가?\"" id c04_t_0369

    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at fwalk
    pause 1.6
    show tiger am_u
    with dissolve

    "엘레드는 씨익 웃으며 [pl_name]에게 다가가 어깨에 손을 올렸다." id c04_t_0370

    show tiger am_u happy2_am
    with dissolve

    t "\"나는 [pl_name][josa_wa_gwa] 친구라네. 친구면 같이 술도 마실 수 있지 않나?\"" id c04_t_0371

    "엘레드는 은근히 [pl_name][josa_eul_reul] 자신의 품으로 당겼다. 엘레드의 노골적인 친한 척은 마치 어린아이의 행동 같았다." id c04_t_0372
    
    # 손 쳐내는 탁! 소리
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at fwalk
    pause 2.1
    play sound "effect/putdown.mp3" volume 0.8
    show tiger am_d base_am
    with dissolve

    "[pl_name][josa_eun_neun] 적당히 웃으며 엘레드의 손을 떼어내려 했으나, 가헬이 한 수 더 빨랐다." id c04_t_0373

    show wolf vangry
    with dissolve 

    w "\"만취하게 만들어서 뭘 할 생각이지?\"" id c04_t_0374

    show tiger smile_am
    with dissolve 
    
    "가헬은 엘레드의 손을 쳐내고는 엘레드를 뚫어져라 쳐다봤다." id c04_t_0375
    "으르렁거리는 소리를 내도 이상하지 않을 정도로 표정이 험악했다. 그러나 엘레드는 미소를 거두지 않았다." id c04_t_0376

    with vpunch
    
    c ddam2 "\"(윽, 잠깐?!)\"" id c04_t_0377
    
    "[pl_name][josa_eun_neun] 예상치 못한 압박감에 식은땀을 흘렸다." id c04_t_0378
    "거대한 근육질 수인 둘(의 가슴) 사이에 끼이는 건 의외로 목숨이 위험한 일이었다." id c04_t_0379
    
    with hpunch

    c sigh "\"그만!!\"" id c04_t_0380

    show tiger base_am
    show wolf base
    with dissolve
    play sound "effect/putdown.mp3" volume 0.8
    hide tiger
    hide wolf
    show tiger at left
    show wolf at right
    with dissolve

    "[pl_name][josa_eun_neun] 숨이 막히기 전에 소리치며 둘을 밀어냈다." id c04_t_0381

    c "\"후우... 하루 종일 싸우다가 밤 되겠네. 그냥 셋이서 가요.\"" id c04_t_0382

    show tiger :
        ease 0.2 yoffset 10
        ease 0.2 yoffset 0
    pause 0.4

    "[pl_name][josa_i_ga] 내린 결론에 엘레드는 고개를 끄덕였다." id c04_t_0383

    show wolf am_u sad2_am
    with dissolve

    w "\"하지만...\"" id c04_t_0384

    show wolf am_d sad3_am
    with dissolve

    c "\"옆 마을 술집을 가도 따라올걸?\"" id c04_t_0385

    "[pl_name][josa_eun_neun] 농담으로 꺼낸 말이었지만, 말하고 나니까 엘레드가 정말로 그럴 것 같아서 조금 어이없었다." id c04_t_0386

    show wolf am_u sigh
    with dissolve

    "가헬도 비슷한 생각이 들었는지 결국 포기했다." id c04_t_0387

    stop music fadeout 2.5

label c4t_tavern:
    
    #술집 낮 배경
    scene bg pub:
        align (0.5, 0.58)
        zoom 1.26 
    with Fade(0.8, 0.8, 0.8)
    play music "medieval-fantasy-142837.mp3" volume 0.5  fadein 2.5
    
    "출발할 때부터 시작된 조용한 신경전은 술집에 도착해서도 끝나지 않았다." id c04_t_0388
    
    # 확대한 가헬 엘레드 등장
    show tiger at left, change(1.22, 30, 135)
    with dissolve
    show wolf at right, change(1.22, 0, 135)
    with dissolve

    "동그란 탁자 앞에 [pl_name][josa_i_ga] 앉자마자 좌우로 엘레드와 가헬이 앉았다. 작은 원탁의 한쪽에 셋이 몰려있는 모습이 되었다." id c04_t_0389
    
    c ddam "\"(너무 가까운 거 아냐? 왜 또 내가 중간에...)\"" id c04_t_0390
    
    "왠지 다른 손님들이 이쪽을 힐끔힐끔 보는 기분이었다. 그들이 무슨 얘기를 하는지 모르겠으나, 구경거리가 된 느낌은 좋지 않았다." id c04_t_0391
    "[pl_name][josa_eun_neun] 둘이 조금 떨어져서 앉았으면 했다." id c04_t_0392
    
    c ddam2 "\"... 진짜 굳이 이렇게 앉아야 하나요?\"" id c04_t_0393

    camera:
        perspective True
        parallel:
        
            ease 1.5 xoffset -240
            pause 0.4
            ease 2 xoffset 250
            pause 0.4
            ease 1 xoffset 0
    
    show wolf at right:
        ease 1.5 xoffset 150
        pause 0.4
        ease 2 xoffset -150
        pause 0.4
        ease 1 xoffset 0

    hide tiger
    show tiger at left, change(1.22, 30, 135):
        
        ease 1.5 xoffset 150
        pause 0.4
        ease 2 xoffset -150
        pause 0.4
        ease 1 xoffset 0

    pause 4.5

    "[pl_name][josa_eun_neun] 엘레드와 가헬을 번갈아 보며 말했다." id c04_t_0394
    "동시에 [pl_name][josa_eun_neun] 아까처럼 또 숨 막히는 경험을 할 것 같아서 약간 불안해졌다." id c04_t_0395

    show tiger am_u laugh_am
    with dissolve
    
    t "\"하하, 자네의 매력에 나도 모르게 이끌리고 말았군.\"" id c04_t_0396

    show wolf am_u fight3
    with dissolve
    
    w "\"...\"" id c04_t_0397
    
    "가헬은 아무 말도 하지 않았으나, [pl_name][josa_i_ga] 보기엔 당장이라도 검을 꺼낼 것 같은 눈빛이었다. 정말로 검을 가지고 오진 않아서 다행이었다." id c04_t_0398
    
    c "\"알았으니까 조금만 떨어져 앉아주세요. 가헬, 너도\"" id c04_t_0399
    
    "[pl_name][josa_eun_neun] 큰맘 먹고 엘레드의 옆구리를 가볍게 콕콕 찔렀다." id c04_t_0400
    "귀족에게 무례한 짓을 하는 것이지만, 엘레드의 성격을 생각하면 괜찮을 거라는 생각이 들었다." id c04_t_0401

    show tiger am_d talk_am
    with dissolve
    pause 0.5
    show wolf am_d base
    with dissolve
    
    t "\"크흠, 알겠네...\"" id c04_t_0402

    show tiger am_d base_am
    with dissolve
    
    # 둘 다 평범 좌우 스탠딩 위치로
    hide tiger
    hide wolf
    show tiger at left
    show wolf at right
    with dissolve

    "엘레드는 마지못해 의자를 살짝 옮겼다. 가헬은 그 모습을 보고 나서 한 박자 뒤에 움직였다." id c04_t_0403
    
    c consider "\"(오늘따라 가헬도 좀 이상하게 구는데...)\"" id c04_t_0404
    
    "끝나지 않는 신경전 때문에 [pl_name][josa_eun_neun] 여전히 골치가 아팠다"
    "가능하면 둘이 싸우지 않았으면 하지만, 사소한 일로 다투는 걸 말리기도 귀찮고 피곤해졌다." id c04_t_0405
    
    c sleep "\"(술집에 괜히 왔나?)\"" id c04_t_0406
    
    "[pl_name][josa_eun_neun] 이 자리를 박차고 나가서 집에 가는 상상을 했다." id c04_t_0407
    "물론 현실성이 없었다. 가헬과 약속해서 온 것이기도 하고, 엘레드에게도 예의가 아니었다. " id c04_t_0408
    
    c sigh "\"휴... 일단 식사 메뉴를 주문할게요.\"" id c04_t_0409

    show tiger am_u talk_am
    with dissolve
    
    t "\"그건 내가 하겠네.\"" id c04_t_0410

    show wolf am_u talk
    with dissolve
    
    w "\"아니, 내가 하겠다.\"" id c04_t_0411

    show tiger am_d fight_am
    show wolf am_d fight3
    with dissolve

    "경쟁적으로 대답하는 엘레드와 가헬 때문에 [pl_name][josa_eun_neun] 살짝 멈칫했다." id c04_t_0412

    menu :
        "그냥 내가 간다." :
            # 씬 보는 트리거
            $ c4t_resque_pick = True
            
            "[pl_name][josa_eun_neun] 둘의 의견을 무시하고 자리에서 벌떡 일어섰다. 잠깐이라도 이 상황에서 벗어나고 싶었다." id c04_t_0413

            show tiger am_d base_am
            show wolf am_d base
            with dissolve
            
            c talk "\"그리고 에일도 세 잔 주문할게요.\"" id c04_t_0414
            
            "[pl_name][josa_eun_neun] 마치 아무 말도 듣지 못했다는 듯 가버렸다. 엘레드와 가헬은 할 말을 잃고 그 뒷모습을 바라보았다." id c04_t_0415
            
            "잠깐의 침묵 끝에 엘레드가 입을 열었다." id c04_t_0416
            
            show tiger am_u smile_am
            with dissolve

            t "\"뭐... 가끔은 저런 의외의 모습도 매력이 있지.\"" id c04_t_0417

            show wolf am_u talk
            with dissolve

            w "\"... 취향 참 독특하십니다.\"" id c04_t_0418

            show wolf am_d base
            with dissolve
            show tiger am_d base_am
            with dissolve

            "가헬은 확 \'변태\'라고 말하고 싶은 것을 은근히 돌려 말했다. 엘레드는 그것을 눈치챘는지 큭큭대며 웃음을 흘렸다." id c04_t_0419

            show tiger am_u horny2_am
            with dissolve

            t "\"모를 일이지. [pl_name]에게 수컷을 지배하는 재능이 있을지도...\"" id c04_t_0420

            show tiger am_u horny2_am
            with dissolve
            
            "엘레드는 무언가를 생각하면서 입술을 핥았다." id c04_t_0421

            show tiger am_d base_am
            with dissolve

            "[pl_name]에 대한 성희롱이라는 걸 이해하자마자, 가헬은 눈을 번뜩이며 나직하게 말했다." id c04_t_0422

            show wolf am_u fight2
            with dissolve 
            
            w "\"입조심해라.\"" id c04_t_0423

            show tiger am_u fight3_am
            with dissolve 
            
            "가헬은 거의 반사적으로 엘레드를 위협했다."       
            "엘레드도 가헬이 왜 저렇게 공격적으로 말하는지 이해할 수는 있었다. 그렇다고 자신의 발언을 취소할 생각은 없었다." id c04_t_0424
            "[pl_name][josa_i_ga] 가헬과 엘레드는 눈빛만으로 격렬한 승부를 펼쳤다. 왁자지껄한 술집 속에서 유일하게 고요한 테이블이었다." id c04_t_0425

            show wolf am_d base
            show tiger am_d base_am
            with dissolve 

            "둘은 [pl_name][josa_i_ga] 돌아오는 걸 보고 아무 일도 없었던 척했다." id c04_t_0426
            "[pl_name][josa_eun_neun] 술잔을 내려놓으며 둘의 눈치를 보았다." id c04_t_0427
            
            c sigh "\"(나 없는 사이에 말다툼하진 않았나보다. 에휴... 내가 왜 이런 걱정을 해야 하지?)\""            

        "가헬에게 맡긴다." :
            $ c4t_gahel_pick = True

            c talk "\"그러면 부탁할게. 아참, 가능하면 술도 같이 부탁해.\"" id c04_t_0428

            show tiger am_d base_am
            show wolf am_d base
            with dissolve
            
            "평소에 자주 와 본 가헬이라면 괜찮은 메뉴도 잘 알고 있을 것이다." id c04_t_0429

            show wolf am_u talk
            with dissolve 
            
            w "\"알았다.\"" id c04_t_0430

            show wolf am_d smile
            with dissolve 
            
            "가헬은 작은 미소를 지으며 자리에서 일어났다." id c04_t_0431

            hide wolf
            with dissolve

            "[pl_name][josa_eun_neun] 엘레드가 또 달라붙으려고 하지 않을까 걱정했지만, 예상외로 엘레드는 가만히 있었다." id c04_t_0432
            "정확히는 몸만 가만히 있었다." id c04_t_0433

            show tiger am_u wink_am
            with dissolve 
            
            t "\"둘만 있으니 좋군. 원래는 이런 분위기를 즐기고 싶었는데 말이지.\"" id c04_t_0434
            
            "엘레드의 음흉한 미소 때문에 [pl_name][josa_eun_neun] 어이가 없었다." id c04_t_0435
            
            c consider "\"(역시 술집에 오려고 했던 건, 단 둘이 데이트하는 기분을 내려는 꿍꿍이였나...)\"" id c04_t_0436
            
            "[pl_name][josa_eun_neun] 욕망이 흘러넘치는 듯한 엘레드의 표정을 보고도 모른 척 다른 얘기를 꺼냈다." id c04_t_0437
            
            c talk "\"그러고 보니 평범한 술도 괜찮으신가요? 아무래도 고급품은 아닐텐데...\"" id c04_t_0438

            show tiger am_d talk_am
            with dissolve
            
            t "\"아아, 그건 괜찮네. 첫 잔을 상쾌하게 시작하는 것도 좋지.\"" id c04_t_0439

            show tiger am_d base_am
            with dissolve
            
            "[pl_name][josa_eun_neun] 당연히 엘레드가 고급술만 마실 거라고 생각했다. 그러나 엘레드는 여기보다 훨씬 허름한 술집에도 많이 가본 수인이다." id c04_t_0440
            "물론 그런 곳에 가는 목적은 뜨거운 하룻밤을 보낼 남자를 \'사냥\'하기 위해서였지만, 엘레드는 굳이 그런 사실을 얘기하진 않았다." id c04_t_0441
            
            show tiger am_u smile_am
            with dissolve 
            
            t "\"내 취향에 맞지 않을까 봐 걱정해 주는 건가? 역시 자네는 마음씨도 아름답군...\"" id c04_t_0442

            
            show wolf at right
            with dissolve
            play sound "effect/putdown.mp3" volume 0.8
            pause 0.5
            
            "가헬은 술잔을 탁 소리가 나게 내려놓았다. [pl_name][josa_eun_neun] 가헬이 엘레드의 말을 끊은 것처럼 느꼈다." id c04_t_0443

            show tiger am_d base_am
            with dissolve
            show wolf am_u talk
            with dissolve 
            
            w "\"식사는 저녁 특선 메뉴로 주문했다.\"" id c04_t_0444
            
            c talk "\"고마워.\"" id c04_t_0445

        "엘레드에게 맡긴다." :
            $ c4t_elred_pick = True

            c talk "\"그러면 부탁드립니다.\"" id c04_t_0446

            show tiger am_d base_am
            show wolf am_d base
            with dissolve

            "[pl_name][josa_eun_neun] 엘레드라면 비싼 메뉴도 쉽게 주문할 것 같다고 생각했다." id c04_t_0447
            "속물적인 생각이긴 하지만, 엘레드는 귀족이니까 이 정도는 몇 푼도 안 될 것이다." id c04_t_0448

            show tiger am_u talk_am
            with dissolve
            
            t "\"빨리 갔다 오겠네.\"" id c04_t_0449

            show tiger am_d wink_am
            with dissolve
            
            "엘레드는 특징적인 윙크를 날리고 주문하러 갔다." id c04_t_0450

            hide tiger
            with dissolve

            "가헬은 그 모습을 슬쩍 보다가 다시 [pl_name]에게 눈을 돌렸다." id c04_t_0451

            show wolf am_u fight2
            with dissolve
            
            w "\"혹시라도 저 자식이 허튼짓하지 않는지 감시하겠다.\"" id c04_t_0452

            show wolf am_d fight3
            with dissolve
            
            c ddam2 "\"아니, 여기가 던전도 아니고 그렇게까지 호위할 필요는 없어. 휴일에 쉬러 온 건데 긴장한 채로 있으면 어떡해.\"" id c04_t_0453

            show wolf am_d sad_am
            with dissolve
            
            "[pl_name][josa_eun_neun] 가헬이 왜 이렇게 엘레드를 경계하는지 이해할 수 없었다." id c04_t_0454
            
            "가헬은 귀가 처진 채 대답했다." id c04_t_0455

            show wolf am_u sad2_am
            with dissolve
            
            w "\"알겠다...\"" id c04_t_0456
            
            show wolf am_d sad3_am
            with dissolve

            c consider "\"(둘이 뭔가 껄끄러운 과거라도 있나? 지금 물어볼 분위기는 아닌 것 같고...)\"" id c04_t_0457

            "[pl_name][josa_eun_neun] 둘이 과거에 다툴만한 사건이 있었나 생각해 보았다." id c04_t_0458
            "마물 토벌 과정에서 만났을 가능성도 있지만, 지금 확실한 것은 없었다." id c04_t_0459

            show wolf base
            show tiger am_u smile_am at left
            with dissolve
            
            t "\"여기도 꽤 괜찮은 와인을 팔더군. 이거 받게.\"" id c04_t_0460
            
            show tiger am_d
            with dissolve
            
            "엘레드는 미소를 지으며 좋은 향이 나는 와인 한 잔을 [pl_name]의 앞에 두었다." id c04_t_0461

            show tiger am_d base_am
            with dissolve

            "가헬 몫의 와인을 줄 때는 미소가 싹 없어졌다." id c04_t_0462
            
            c talk "\"감사합니다.\""
 
    show tiger am_u smile_am
    with dissolve

    "[pl_name][josa_i_ga] 잔을 잡자마자 엘레드도 잔을 들어 올렸다." id c04_t_0463

    t "\"첫 잔인데 건배는 해야 하지 않겠나?\"" id c04_t_0464

    show wolf am_u
    with dissolve
    
    "[pl_name][josa_i_ga] 뭐라고 대답하기도 전에, 가헬도 따라서 잔을 들어 올렸다." id c04_t_0465
    
    "얼떨결에 건배를 해버린 [pl_name][josa_eun_neun] 촌극의 주인공이 된 기분이 들었다." id c04_t_0466
    
    c sigh "\"(이게 뭐 하는 짓인지 모르겠네... 마시기나 하자.)\"" id c04_t_0467

    show tiger base_am
    with dissolve
    
    "[pl_name][josa_eun_neun] 술을 한 모금만 마시려고 했다. 그러나 맛을 보자마자 쭈욱 들이켰다." id c04_t_0468
    
    "오랜만에 마시는 술이라 그런지 쭉쭉 들어갔다." id c04_t_0469

    show wolf am_d talk
    with dissolve
    
    w "\"빈속에 너무 빨리 마시는 거 아닌가.\"" id c04_t_0470

    show wolf am_d base
    with dissolve
    
    c talk "\"이 정도는 괜찮아.\"" id c04_t_0471
    
    "[pl_name][josa_i_ga] 잔을 내려놓자 엘레드는 그때를 노린 듯 질문했다." id c04_t_0472

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (400, -30)
    show tiger am_d talk_am
    with dissolve
    
    t "\"자네는 술을 잘 마시는 편인가?\"" id c04_t_0473

    hide question
    show tiger am_d base_am
    with dissolve
    
    c consider "\"음, 잘 모르겠네요. 자주 마시는 편은 아니라서...\"" id c04_t_0474
    
    "남들이 얼마나 마시는지 모르니, 자기 자신을 객관적으로 평가할 수가 없었다. [pl_name][josa_eun_neun] 막연히 자기 주량이 평범하다고 생각했다." id c04_t_0475
    
    show tiger am_u smile_am
    with dissolve

    t "\"흐음...\"" id c04_t_0476

    show tiger am_d smile_am
    with dissolve
    
    "엘레드는 의미심장한 미소를 지을 뿐이었다. 때마침 종업원이 나타나서 식사를 테이블에 내려놓는다." id c04_t_0477

    show tiger base_am
    with dissolve
    
    if c4t_resque_pick==True :
        
        show salmon_steak :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        
        "버섯 수프, 향신료가 강한 꼬치구이, 옥수수 감자샐러드와 메인이 되는 연어구이가 테이블을 채운다." id c04_t_0478

        "다채로운 향기가 [pl_name]의 식욕을 자극했다." id c04_t_0479

        hide salmon_steak
        with dissolve
        
        c base "\"(음, 다양하게 주문하길 잘했다.)\"" id c04_t_0480

    elif c4t_gahel_pick==True :

        show bbq :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        
        "김이 모락모락 나는 바베큐가 테이블 위에 올라왔다." id c04_t_0481
        
        "수프나 빵 같은 것도 있었지만, 뼈가 붙은 채로 구운 고기는 테이블 위에서 압도적인 존재감을 뽐냈다." id c04_t_0482

        hide bbq
        with dissolve
        
        c base "\"(가헬이 주문해서 그런가. 고기 비중이 높네...)\"" id c04_t_0483

    elif c4t_elred_pick==True :

        show steak :
            xcenter 0.5
            ycenter 0.5
        with dissolve
        
        "말린 토마토를 넣어 구운 빵과 치즈를 듬뿍 넣은 고기 스튜부터 시작해서, 평소 먹던 것과 다른 화려한 샐러드까지 음식 하나하나가 비싸 보였다." id c04_t_0484
        
        "마지막으로 중앙에 놓인 스테이크는 화려함의 정점이었다." id c04_t_0485

        hide steak
        with dissolve
        
        c ddam2 "\"(이게 다 얼마야? 이 술집에서 이런 것도 팔았구나...)\"" id c04_t_0486
   
    "[pl_name][josa_eun_neun] 식사하면서도 둘의 눈치를 보느라 머뭇거렸다." id c04_t_0487

    c consider "\"(어린애도 아니고 먹는 거로 싸우진 않겠지?)\"" id c04_t_0488

    "그러나 [pl_name][josa_i_ga] 걱정해야 할 것은 그런 게 아니었다." id c04_t_0489

    hide wolf
    show wolf at right :
        ease 0.2 xoffset -12 
        ease 0.2 xoffset 0 
    
    "가헬은 접시 하나를 [pl_name] 쪽으로 살짝 밀어주며 말했다." id c04_t_0490

    show wolf am_u talk
    with dissolve

    w "\"오늘 입맛이 없나? 평소보다 먹는 속도가 느린데.\"" id c04_t_0491

    show wolf am_u base
    with dissolve
    
    c ddam2 "\"아, 아니?\"" id c04_t_0492

    show wolf am_d talk
    with dissolve
    
    w "\"근육을 키우려면 고기도 챙겨 먹어야 한다.\"" id c04_t_0493

    show wolf am_d base
    with dissolve

    show tiger am_u smile_am
    with dissolve
    pause 0.5
    show tiger at left, change(1.22, 30, 135)
    with dissolve
    
    "둘의 대화를 듣고 있던 엘레드는 씩 웃으며 뭔가를 [pl_name]에게 들이밀었다." id c04_t_0494

    "포크로 고기를 찍어 [pl_name]의 입가에 가져온 것이다. 어린아이에게 음식을 먹일 때와 비슷했다." id c04_t_0495

    t "\"자, 아~ 해보게.\"" id c04_t_0496
    
    c "\"아니, 그, 저는 4살이 아닙니다만...\"" id c04_t_0497

    show wolf at right, change(1.22, 0, 135)
    with dissolve
    
    "[pl_name][josa_eun_neun] 고개를 살짝 뒤로 뺐다. 그러나 이번엔 가헬이 비슷하게 빵을 들이밀었다." id c04_t_0498

    show wolf am_u talk
    with dissolve
    
    w "\"식사는 균형도 중요하다.\"" id c04_t_0499

    show wolf am_u base
    with dissolve
    
    "[pl_name][josa_eun_neun] 무슨 이상한 장난에 휘말린 기분이었다." id c04_t_0500
    
    c "\"(가헬까지 왜 이래? 진심으로 나 먹으라고 이러는 거 맞아?)\"" id c04_t_0501
    
    "그렇다고 가헬과 엘레드가 합심해서 자신을 놀릴 것 같지는 않았다." id c04_t_0502
    "[pl_name][josa_eun_neun] 얼떨떨한 표정으로 입을 벌렸다. 다 큰 어른이 되어서 남이 주는 음식을 받아먹는 건 정말 이상한 기분이었다." id c04_t_0503
    "고기와 빵을 삼키고 나서 [pl_name][josa_eun_neun] 술을 쭉 들이켰다. 어느새 한 잔을 다 비웠다." id c04_t_0504
    
    c sigh "\"(인생이 쓰면 술이 달다던데...)\"" id c04_t_0505

    "한 번 마시기 시작하니 더 마시고 싶어진 [pl_name][josa_eun_neun] 갑자기 자리에서 벌떡 일어났다." id c04_t_0506

    play sound "audio/effect/chair_drag.mp3" volume 0.6
    
    # 의자 끽!소리 넣을까?
    "의자가 거칠게 뒤로 밀려나면서 끼익 소리를 냈다." id c04_t_0507

    play sound "effect/ping.mp3" volume 0.75
    show exclamation at exclamation_move (650, 40)
    show exclamation2 at exclamation_move (1640, 40)
    hide wolf
    hide tiger
    show wolf am_d base at right, change(1.22, 0, 135), surprise_move
    show tiger am_d base_am at left, change(1.22, 30, 135), surprise_move
    with Dissolve (0.2)

    "갑작스러운 [pl_name]의 행동에 두 쌍의 놀란 시선이 따라붙었다." id c04_t_0508

    hide exclamation
    hide exclamation2
    show wolf sad3_am
    show tiger sad3_am
    with dissolve

    w "\"(화난 건가? 화났겠지... 승부욕에 미쳐서 괜한 짓을 했군.)\"" id c04_t_0509

    t "\"([pl_name]에게는 조금 과했나?)\"" id c04_t_0510

    "둘의 걱정과 다르게 [pl_name][josa_eun_neun] 새 잔을 들고 평범하게 자리에 앉았다." id c04_t_0511

    show wolf base
    show tiger base_am
    with dissolve
    
    $ unlock_info_tag(4, "2")
    $ display_text = _("정보 : 증류주")
    show screen affection_indicator
    
    c talk "\"여기서 {color=#ee3939}'증류주'{/color}도 판다고 하더라. 한번 마셔볼지 잠깐 고민했어.\"" id c04_t_0512

    hide wolf
    show wolf am_d base at right, change(1.22, 0, 135) :
        ease 0.5 xoffset -40
        pause 0.5
        ease 0.5 xoffset 0
    pause 1.5    

    "가헬은 [pl_name][josa_i_ga] 들고 있는 게 에일인지 확인하고는 말했다." id c04_t_0513

    show wolf am_u talk
    with dissolve
    
    w "\"말리지는 않겠지만, 너무 취하지 않게 조심해라.\"" id c04_t_0514

    show wolf am_d base
    with dissolve
    
    "[pl_name][josa_eun_neun] 괜히 반항심이 들었다. 에일을 쭉 들이켜자 향긋한 곡물 향이 느껴졌다." id c04_t_0515
    "[pl_name][josa_eun_neun] 방금 가져온 잔을 바로 절반까지 비워버렸다." id c04_t_0516
    
    c consider "\"(아직 취기가 올라오지도 않았는데, 너무 애 취급하는 거 아냐?)\"" id c04_t_0517

    show tiger am_u laugh_am
    with dissolve
    
    t "\"크하하! 그래, 그렇게 통쾌하게 마시는 날도 있어야지.\"" id c04_t_0518
    
    "엘레드는 [pl_name]의 마음을 눈치챘는지 크게 웃으며 말했다." id c04_t_0519

    show tiger am_u wink_am
    with dissolve
    
    t "\"내가 살 테니까 마음껏 마시게.\"" id c04_t_0520
    
    c smile "\"앗, 감사합니다.\"" id c04_t_0521

    show tiger am_d base_am
    with dissolve
    
    "공짜라면 주저할 이유가 없었다. [pl_name][josa_eun_neun] 기쁜 표정으로 대답했다." id c04_t_0522
    "반면에 가헬의 표정은 좋지 않았다." id c04_t_0523

    show wolf angry
    with dissolve

    w "\"......\"" id c04_t_0524

    show tiger am_u talk_am
    with dissolve
    
    t "\"흠, 자네는 술이 별로인가? 용병답지 않군.\"" id c04_t_0525

    show tiger am_d base_am
    with dissolve

    w "\"...\"" id c04_t_0526

    show wolf am_u talk
    with dissolve

    w "\"... 감사합니다.\"" id c04_t_0527

    show wolf am_d base
    with dissolve
    
    "가헬은 마지못해 엘레드에게 예의를 차렸다." id c04_t_0528
    


    # 술집 밤 배경으로 변경
    scene bg pub2 with Fade(0.8, 0.8, 0.8)

    "..." id c04_t_0529
    
    "시답잖은 대화를 하며 술을 마시다 보니, [pl_name][josa_eun_neun] 살짝 몽롱해졌다." id c04_t_0530
    "적당한 취기가 몸을 따뜻하게 만들고, 기분을 들뜨게 했다. 떠들썩한 술집의 분위기에 섞여 들어가는 느낌은 생각 외로 괜찮았다." id c04_t_0531

    show tiger am_d base_am red at left
    show wolf am_d base red at right
    with dissolve
    
    c talk "\"음, 술집에 오길 잘한 것 같아.\"" id c04_t_0532

    show tiger am_u laugh_am red_laugh
    with dissolve
    
    t "\"하핫! 역시 그렇게 생각할 줄 알았다네.\"" id c04_t_0533

    show tiger am_d base_am red
    with dissolve

    "겉보기에는 평소랑 다르지 않지만, [pl_name][josa_eun_neun] 판단력이 살짝 흐려져 있었다." id c04_t_0534
    "자기 스스로 얼마나 취했는지 모른 채, 새 잔을 받아왔다." id c04_t_0535
    
    c base "\"(술맛이 꽤 괜찮은데? 나, 생각보다 많이 마실 수 있군.)\"" id c04_t_0536

    show wolf am_u talk
    with dissolve
    
    w "\"[pl_name], 이제 충분히 마시지 않았나?\"" id c04_t_0537

    show wolf am_d base
    with dissolve
    
    c talk "\"어? 그렇게 많이 안 마셨어. 한, 5잔 정도?\"" id c04_t_0538
    
    "[pl_name][josa_eun_neun] 점원이 빈 잔을 몇 개 가져갔다는 사실을 잊은 채, 눈앞의 잔 개수를 세었다." id c04_t_0539
    "가헬도 비슷하게 취했는지 그 사실에 반박하지 못했다. 하지만 가헬은 취했어도 가헬의 눈빛만큼은 날카롭게 살아있었다." id c04_t_0540

    show tiger am_u smile_am
    with dissolve
    
    t "\"술집에서 취할 걱정을 하나? 역시 비리비리한 용병이라 그런지 술에도 약한가 보군.\"" id c04_t_0541
    
    show tiger am_d smile_am
    with dissolve
    
    "엘레드의 직설적인 도발에 가헬은 표정을 구겼다." id c04_t_0542

    show wolf am_u fight2
    with dissolve
    
    w "\"그래서 술로 승부를 볼 셈인가?\"" id c04_t_0543

    show wolf am_d fight3
    with dissolve
    
    "말은 그렇게 했으나, 사실 가헬은 술 승부에는 그다지 자신이 없었다." id c04_t_0544
    "엘레드는 귀족이니 독한 술에도 익숙하겠지만, 자신은 용병들 사이에서 평범한 정도였다." id c04_t_0545
    "하지만 여기서 꼬리를 내릴 수는 없었다." id c04_t_0546

    show tiger am_u talk_am
    with dissolve
    
    t "\"흐음, 결투라면 좀 더 재밌는 걸로 하지.\"" id c04_t_0547

    show tiger am_d base_am
    with dissolve
    
    c ddam2 "\"결투요? 술집에서 주먹질은 안 되는데...\"" id c04_t_0548

    "[pl_name][josa_eun_neun] 둘이 또 싸울까 봐 걱정했으나, 엘레드는 가헬을 놀릴 생각이었다." id c04_t_0549

    show tiger am_u smile_am
    with dissolve
    
    t "\"레슬링으로 결판을 내는 건 어떤가?\"" id c04_t_0550
    
    show wolf am_u fight2
    with dissolve
    
    w "\"하! 체구가 크다고 반드시 유리한 건 아니다.\"" id c04_t_0551

    show wolf am_u fight3
    with dissolve
    
    "가헬은 엘레드의 도발에 꽤 무례하게 받아쳤다." id c04_t_0552
    "평소의 [pl_name][josa_ra_ira]면 가헬이 무례하게 구는 걸 말렸겠지만, 지금은 주먹질이 아닌 것에 다행이라고 생각했다." id c04_t_0553
    "그냥 둘이 싸우지 않았으면 하는 마음으로 상황을 지켜보고 있었다." id c04_t_0554

    show wolf am_d fight2
    with dissolve
    
    w "\"소문에 따르면 엉덩이가 가볍던데, 쉽게 쓰러지는 건 아닌지 모르겠군.\"" id c04_t_0555

    show wolf am_d fight3
    with dissolve
    show tiger at surprise_move
    
    "가헬의 반격에 엘레드는 큭큭대며 웃었다. 가헬이 발끈하며 지지 않으려는 모습을 볼 수록 놀리는 재미가 있었다." id c04_t_0556

    show tiger am_d smile_am
    with dissolve
    
    t "\"뭐... 침대에서 내 엉덩이를 노리는 건 쉬울지도 모르지만, 전장에서는 쉽지 않을걸세.\"" id c04_t_0557

    show tiger am_d smile_am
    with dissolve
    
    c ddam2 "\"(엉덩이가 쉬워?! 호색한이라더니 정말 앞뒤 가리지 않나 보다...)\"" id c04_t_0558
    
    "[pl_name][josa_eun_neun] 엘레드의 엉덩이를 생각하자 얼굴이 붉어졌다. 지금도 시원하게 드러내놓은 엉덩이를 옆에서 볼 수 있었다." id c04_t_0559
    "괜히 목이 타는 느낌이라 [pl_name][josa_eun_neun] 시선을 돌리고 조용히 잔을 기울였다." id c04_t_0560

    show wolf am_u fight2
    with dissolve
    
    w "\"호색한이라더니... 사실 앞에 자신이 없어서 뒤를 쓰는 것 아닌가?\"" id c04_t_0561

    show wolf am_u fight3
    with dissolve
    show tiger am_u fight2_am
    with dissolve

    t "\"... 그 발언은 용납할 수 없군. 나는 상대를 배려해 주는 것뿐이라네.\"" id c04_t_0562

    show tiger am_u fight_am
    with dissolve
    
    "엘레드도 더 이상 능글맞은 표정을 하는 건 그만두었다." id c04_t_0563
    "처음엔 조금 놀릴 생각이었지만, 점점 진지하게 가헬과 결판을 내고야 말겠다는 생각이 들기 시작했다." id c04_t_0564

    show wolf am_d fight2
    with dissolve
    
    w "\"그러면 \'크기\'로 승부를 내지.\"" id c04_t_0565

    show wolf am_d fight3
    with dissolve
    
    "가헬은 이것만큼은 자신이 있었다. 특히 \'길이\'는 절대 지지 않을 거라고 자신 있게 말할 수 있었다." id c04_t_0566
    "엘레드는 본능적으로 가헬의 태도 변화를 느끼고 한발 물러서기로 했다." id c04_t_0567

    show tiger am_d fight2_am
    with dissolve
    
    t "\"전에도 그랬지만 자네는 그 승부에서 이길 거라는 확신이 있군. 그 자랑스러운 \'무기\'가 내 것보다 강력할 거라는 확신이...\"" id c04_t_0568

    show tiger am_d fight_am
    with dissolve
    
    c ddam2 "\"(여기가 술집이니까 굳이 돌려서 말하는 거... 맞지?)\"" id c04_t_0569
    
    "[pl_name][josa_eun_neun] 둘 사이에 끼어있는 게 부담스러울 지경이 되자, 의자를 살짝 뒤로 밀었다." id c04_t_0570
    "지금 이 순간은 엘레드와 가헬 둘만의 세계였다." id c04_t_0571

    show tiger am_u horny2_am
    with dissolve
    
    t "\"흐음... 그 정도로 자신만만하면 조금 궁금해지는군.\"" id c04_t_0572

    show tiger am_u smile_am
    with dissolve
    
    "거대한 것을 상상한 엘레드가 거의 반사적으로 입술을 핥자, 가헬은 짜증이 났다." id c04_t_0573

    show wolf am_u fight
    with dissolve
    
    w "\"([pl_name] 앞에서 무슨 행동을 하는 거지?)\"" id c04_t_0574
    

    "불행인지 다행인지, [pl_name][josa_eun_neun] 제발 둘의 싸움이 언쟁에서 끝나기를 기대하며 조용히 있었다." id c04_t_0575

    show wolf am_d fight2
    with dissolve

    w "\"그래서 승부를 받아들일 텐가?\"" id c04_t_0576

    show wolf am_d fight3
    with dissolve
    show tiger am_d talk_am
    with dissolve

    t "\"기세가 대단하군... 좋다. 어디 한번 붙어보도록 하지. 그 자랑스러운 대검을 보여주게.\"" id c04_t_0577
    
    show tiger am_d base_am
    with dissolve
    show wolf am_d talk at surprise_move
    with Dissolve (0.2)

    "가헬은 엘레드의 말에 순간적으로 당황했다." id c04_t_0578

    show wolf am_d base
    with dissolve 

    "대결을 하려면 당연히 보여줘야 하지만, 엘레드가 말하니 뭔가 성욕이 묻어나오는 기분이었다." id c04_t_0579
    "[pl_name]도 엘레드의 끈적함이 느껴져서 황급하게 말했다." id c04_t_0580

    c ddam2 "\"설마 지금 여기서 할 건 아니죠? 그런 대결을 할거면...\"" id c04_t_0581

    menu :
        "뒷골목에서 하는 게..." :

            c ddam2"\"최소한 뒷골목에 숨어서 하는 게...\"" id c04_t_0582

            show tiger am_u talk_am
            with dissolve

            t "\"몰래 하는 것도 스릴이 있지. 하지만 굳이 따지면 관객이 있는 편이 좋지 않나?\"" id c04_t_0583

            show tiger am_d base_am
            with dissolve

            "엘레드의 말에 [pl_name][josa_eun_neun] 머리를 짚었다." id c04_t_0584
            
            c ddam "\"(정말 보통 변태가 아니구나...)\"" id c04_t_0585
            
            "가헬도 엘레드의 발언이 어이없다는 듯 말했다." id c04_t_0586

            show ddam at ddam_move (1430,40)
            show wolf am_u talk
            with dissolve
            
            w "\"나는 관객이 필요 없다. 그런 취미가 있는 수인이 더 드물지 않나?\"" id c04_t_0587

            hide ddam
            show wolf am_d base
            with dissolve
            show tiger am_u talk_am
            with dissolve
            
            t "\"뭐, 각자 자신만의 취향이 있는 법이지. 자네도...\"" id c04_t_0588

            show tiger am_d base_am
            with dissolve
            
            "엘레드는 가헬을 위아래로 훑어봤다." id c04_t_0589

            show tiger am_u talk_am
            with dissolve
            
            t "\"자네를 감당할 만한 \'상대\'를 찾다 보면 취향이 까다로울 텐데?\"" id c04_t_0590

            show tiger am_u smile_am
            with dissolve
            show tiger at left, hshake (0.06, 0, -10)
            pause 0.8
            show wolf am_u fight3
            with dissolve
            
            "엘레드는 손으로 고리 모양을 만들고 다른 손가락을 집어넣었다. 굉장히 노골적인 암시였다." id c04_t_0591

        "방을 빌려서 하는 게..." :
           
            c ddam2 "\"방을 하나 빌려서 하는 게...\"" id c04_t_0592

            show tiger am_u talk_am
            with dissolve

            t "\"셋이 한 방에 들어갈 셈인가? 그것도 좋지.\"" id c04_t_0593

            show tiger am_d base_am
            with dissolve
            
            c "\"저, 저도요?\"" id c04_t_0594
            
            "[pl_name][josa_eun_neun] 조금 놀랐으나 엘레드는 당연하다는 듯 말했다." id c04_t_0595

            show tiger am_u talk_am
            with dissolve
            
            t "\"당연히 심판이 필요하지 않나. 뭐, 자네가 참가하는 것도 좋지. 둘보다는 셋이 재미있거든.\"" id c04_t_0596

            show tiger am_d smile_am
            with dissolve
            
            "가헬은 엘레드의 말을 곱씹었다. 승부에 [pl_name][josa_i_ga] 참가하는 건 이상했다. 그 사실을 지적하기 전에 엘레드는 말을 이었다." id c04_t_0597

            show tiger am_u smile_am
            with dissolve
            
            t "\"셋이면 훨씬 다양한 걸 할 수 있지. 나는 앞뒤를 동시에 쓰는 게 가장 좋다네.\"" id c04_t_0598

            show tiger am_d smile_am
            with dissolve
            
            "엘레드의 표정은 이미 그런 상황을 즐기는 중이었다." id c04_t_0599
            "[pl_name][josa_eun_neun] 엘레드가 말한 상황이 자연스럽게 머릿속에 떠올라서 헛숨을 삼켰다." id c04_t_0600

            show wolf am_u fight2
            with dissolve
            
            w "\"승부랑 상관없는 얘기 아닌가?\"" id c04_t_0601

            show wolf am_u fight3
            with dissolve
            show tiger :
                ease 0.2 yoffset 13
                ease 0.2 yoffset 0
            pause 0.4
            
            "가헬의 지적에 엘레드는 고개를 끄덕이면서도, 전혀 상관없는 얘기를 계속했다." id c04_t_0602

            show tiger am_u wink_am
            with dissolve
            
            t "\"자네도 기회가 되면 꼭 해보게. 평소보다 5배는 더 좋을 테니.\"" id c04_t_0603

            show tiger am_u smile_am
            with dissolve
            
            c ddam2 "\"(앞뒤를 동시에...)\"" id c04_t_0604
            
            #엘레드 이해도+1
            $ tiger_understanding += 1 
            $ display_text = _("엘레드 이해도 변화")
            show screen affection_indicator

            "딱히 궁금했던 건 아니지만, [pl_name][josa_eun_neun] 엘레드의 성향을 조금 더 구체적으로 알게 되었다." id c04_t_0605

            t "\"뭐... 자네의 외모와 물건으로 유혹하면 다들 좋다고 달려들걸세.\"" id c04_t_0606

        "역시 그만두는 게..." :

            c ddam2 "\"역시 그만두는 게... 좋지 않을까요?\"" id c04_t_0607
            
            "[pl_name][josa_eun_neun] 식은땀을 흘리며 둘의 결투를 말리려고 했다." id c04_t_0608

            show tiger am_u wink_am
            with dissolve

            t "\"기사단장 정도 되면, 도전을 거부하는 게 패배보다 부끄럽다네.\"" id c04_t_0609
            
            show tiger am_d base_am
            with dissolve

            "[pl_name][josa_eun_neun] 엘레드의 말에 조금 당황했다." id c04_t_0610

            c consider "\"(이건 그거랑 다르지 않나?...)\"" id c04_t_0611

            c ddam2 "\"그, 아무튼, 보는 눈도 많은데 그런 승부는 자제하시죠.\"" id c04_t_0612
            
            show tiger shy_am
            with dissolve

            "엘레드는 무언가 조금 고민하더니, 능글맞은 웃음을 지었다." id c04_t_0613
            
            show tiger am_u smile_am
            with dissolve

            t "\"관객이 많으니 꼭 해야 하지 않겠나?\"" id c04_t_0614

            show tiger laugh_am red_laugh
            with dissolve

            "[pl_name][josa_eun_neun] 괜한 말을 했다는 것을 즉시 깨달았다. 엘레드는 이런 것에서 수치심은커녕 흥분해 버리는 변태였다." id c04_t_0615
            
            show tiger am_d base_am red
            with dissolve

            "가헬은 [pl_name]에게 승부를 말릴 필요가 없다는 것을 간접적으로 말했다." id c04_t_0616
            
            show wolf am_u talk
            with dissolve

            w "\"어차피 엘레드 경은 패배해도 잃을 명성이 없으니, 너무 신경 쓰지 마라.\"" id c04_t_0617
            
            show wolf am_d base
            with dissolve

            "가헬이 은근히 비꼬자, 엘레드는 오히려 큭큭대며 말했다." id c04_t_0618
            
            show tiger am_u smile_am
            with dissolve

            t "\"만약 자네가 승리한다면, 그 \'무기\'에 대한 소문이 퍼지겠군. 기사단장도 무릎 꿇린 대검이라...\"" id c04_t_0619
            
            t "\"다들 자네의 검만 바라보게 되어도, 내 탓을 하지는 말게.\"" id c04_t_0620


    "평소의 엘레드였다면 [pl_name] 앞에서 이 정도로 심하게 성적인 언행을 하지 않았을 것이다." id c04_t_0621
    "하지만 지금 엘레드의 이성은 육욕에 조금씩 잡아먹히고 있었다." id c04_t_0622
    "가헬은 엘레드의 욕망이 담긴 시선에 기분이 급격하게 나빠졌다." id c04_t_0623

    show wolf am_d fight2
    with dissolve
    
    w "\"으...\"" id c04_t_0624

    show wolf am_d fight3
    with dissolve
    show tiger am_d base_am
    with dissolve

    "가헬이 경멸 어린 눈빛으로 바라보자 엘레드는 아주 조금 제정신이 돌아왔다." id c04_t_0625
    "그러나 머릿속에 맴도는 욕망은 사라지지 않고 술기운과 섞여서 엘레드의 판단력을 뒤죽박죽으로 만들고 있었다." id c04_t_0626

    show tiger am_u talk_am
    with dissolve
    
    t "\"거절할 셈인가? 그렇다면 대결은 다른 방식으로 진행하지.\"" id c04_t_0627

    show tiger am_d base_am
    with dissolve
    show wolf am_d base
    with dissolve
    
    "엘레드의 머릿속에 좋은 (혹은 안 좋은) 생각이 떠올랐다. 나중에 후회할 선택이지만, 지금 하는 것을 참을 수 없었다." id c04_t_0628
    "그리고 엘레드가 제시한 방법은 술집 전체를 뒤집어엎을 정도로 강력한 것이었다." id c04_t_0629

    stop music fadeout 2.5

label c4t_tavern_battle:

    # 술집 밤 배경
    scene bg pub2 with Fade(0.8, 0.8, 0.8)
    # 음악
    play music "stomp-117637.mp3" fadein 1.5 volume 0.3
        
    # 속옷상태로 등장한 엘레드 가헬
    show tiger inn_d base red at left
    with dissolve

    $ unlock_character_image("tiger", "tiger b_no base inn_d")
    $ display_text = _("이미지 : 엘레드(속옷)")
    show screen affection_indicator

    show wolf inn_d red at right
    with dissolve

    $ unlock_character_image("wolfr", "wolf b_no inn_d")
    $ display_text = _("이미지 : 가헬(속옷)")
    show screen affection_indicator

    "엘레드와 가헬은 속옷 차림으로 서 있었다. 술을 마시던 손님들은 웅성거리며 무슨 일인지 궁금해했다." id c04_t_0630

    play sound "effect/crowd.mp3" volume 0.85   

    "엘레드가 제시한 승부 내용은 \'누가 더 매력적인 수컷인가?\'였다. 술집에 모인 손님들의 선택으로 승자를 정할 계획이었다." id c04_t_0631

    "가헬은 모르는 수인들 앞에서 이렇게까지 해야 하나 고민했지만, 이제 와서 발뺌하기엔 너무 늦었다." id c04_t_0632
    
    "엘레드는 큰 목소리로 외쳤다." id c04_t_0633

    show tiger inn_u talk
    with dissolve

    t "\"주목! 곧 승부를 시작하겠다. 나, 기사 엘레드는 용병 가헬에게 결투를 신청한다!\"" id c04_t_0634

    show tiger inn_d base
    with dissolve

    "손님들은 자연스럽게 엘레드의 선언에 집중했다." id c04_t_0635
    
    "단순히 엘레드의 목소리가 커서 가능한 일이 아니었다. 기사단장의 카리스마와 노련함은 군중을 휘어잡는 힘이 있었다." id c04_t_0636

    show tiger inn_u talk
    with dissolve
    
    t "\"기준은 오직 \'수컷의 매력\' 뿐이다. 누가 더 매력적인지 잘 보고 선택하도록.\"" id c04_t_0637
    
    t "\"제군들은 이 승부의 증인이자 심판으로서 각자 자신의 마음에 정직하길 바란다.\"" id c04_t_0638

    show tiger inn_d base
    with dissolve
    
    "술에 취해서 속옷 차림으로 말해도 무시할 수 없는 위압감이 있었다. [pl_name][josa_eun_neun] 엘레드의 이런 모습이 신기했다." id c04_t_0639
    
    c "\"(그냥 변태 아저씨인 줄 알았는데, 기사단장은 뭔가 다르긴 다르네...)\"" id c04_t_0640

    "엘레드의 명령에 따라 테이블이 옮겨지고, 둘의 승부를 위한 무형의 무대가 생겼다. 술집 손님들은 둥글게 모여서 앞으로 벌어질 일을 기대했다." id c04_t_0641
    
    c consider "\"(근데 뭘 하려고 속옷만 입은 거지?)\"" id c04_t_0642

    "구체적으로 무엇을 할지는 모르겠지만, [pl_name][josa_eun_neun] 관중 속에 섞여 조용히 둘을 바라보았다." id c04_t_0643

    # 여기서부터 사람들 와글와글

    "승부가 시작되자 엘레드는 기선제압을 위해 먼저 자세를 잡았다." id c04_t_0644

    show tiger inn_u smile
    with dissolve
    
    "팔을 들어 올려서 근육에 힘을 주자 핏줄이 불거졌다. 남의 시선에 익숙한 엘레드는 주먹을 꽉 쥐며 이두박근을 자랑했다." id c04_t_0645
    
    "지금은 능글맞은 미소가 정말 완벽하게 어울렸다." id c04_t_0646

    show wolf inn_u base
    with dissolve
    
    "가헬도 질세라 자세를 취했다." id c04_t_0647
    "처음엔 조금 어색해 보였으나, 엘레드를 슬쩍 보고 다른 자세를 취하며 차이점을 어필했다." id c04_t_0648
    "희고 검은 털색의 대비가 아름답게 갈라진 허벅지 근육을 더욱 강조했다." id c04_t_0649

    play sound "effect/crowd.mp3" volume 0.85

    n "\"저 용병도 굉장한데...\"" id c04_t_0650
    
    n "\"하지만 그 유명한 엘레드 경이잖아...\"" id c04_t_0651

    show tiger inn_u base
    with dissolve

    "관중들은 각자의 취향에 따라 조금씩 자리를 옮겼다. 그래도 어느 한쪽을 포기할 수 없는지, 중간쯤에 가장 많이 모였다." id c04_t_0652
    
    "어쩌다 보니 [pl_name][josa_eun_neun] 가장 앞줄에 서 있게 되었다." id c04_t_0653
    
    "가헬은 [pl_name][josa_wa_gwa] 시선을 마주치고 약간 부끄러워서 얼굴을 붉혔다. 그러나 승부에서 지는 것이 더 부끄러운 일이었다." id c04_t_0654

    show wolf fight at surprise_move
    
    w "\"흡!...\"" id c04_t_0655
    
    "가헬은 숨을 내쉬면서 몸을 굽혔다." id c04_t_0656
    "선명하게 갈라진 가헬의 복근은 잔뜩 힘이 들어가서 터질 것 같았다. 흉터가 가헬의 야성적인 매력을 강조했다." id c04_t_0657

    show tiger fight3 at surprise_move

    "둘이 자세를 바꿀 때마다 관중들은 환호성을 지르며 감탄했다." id c04_t_0658
    "이때를 노린 것인지, 점원은 관중 속을 돌아다니며 술을 팔고 있었다." id c04_t_0659

    play sound "effect/crowd2.mp3" volume 0.85
    
    n "\"이걸 어떻게 선택해?\"" id c04_t_0660
    
    n "\"오늘 죽어도 좋아!\"" id c04_t_0661
    
    "엘레드는 몇몇 수인의 반응을 보며 만족스러운 웃음을 지었다. 거의 타고난 재능이었다." id c04_t_0662
    "반면 가헬은 엘레드에게 지지 않으려고 최대한 노력하고 있었다." id c04_t_0663
    "조금 뻣뻣하지만, 오히려 차가운 눈빛으로 침묵하는 게 가헬에게 어울렸다." id c04_t_0664
    "뜨거운 분위기 속에서 힘을 쓰느라 그런지, 둘은 조금씩 땀을 흘리고 있었다. 그것은 관중을 더 열광시키게 했다." id c04_t_0665

    "[pl_name]도 후끈한 분위기에 휩쓸려 둘을 지켜봤다." id c04_t_0666
    
    show tiger wink at surprise_move
    with Dissolve (0.2)

    "[pl_name]의 시선을 느낀 엘레드는 윙크하며 가슴에 힘을 줬다." id c04_t_0667
    "근육을 튕겨서 가슴이 꿀렁거리자, 금색 피어싱도 따라서 흔들렸다." id c04_t_0668
    
    c ddam2 "\"(저런 기술은 어떻게 생각해 낸 거야?!)\"" id c04_t_0669

    hide tiger
    show tiger inn_u wink red at left, surprise_move2
    pause 0.8
    show tiger wink at left, surprise_move2
    pause 0.5 

    "아주 정확하게 좌우를 번갈아 움직이는 게 한두 번 해본 솜씨가 아니었다." id c04_t_0670

    show tiger laugh red_laugh at left, surprise_move
    with Dissolve (0.2)

    "엘레드는 크게 웃으면서 가슴을 활짝 폈다. 장난스러운 표정과 음란한 육체가 역설적인 조화를 이루었다." id c04_t_0671
    "관중의 시선이 가슴에 쏠리자 엘레드는 고양감을 느꼈다." id c04_t_0672
    "그 순간, 엘레드의 본능이 엘레드에게 \'승부를 결정지을 방법\'을 속삭였다." id c04_t_0673

    play channel1 "effect/footstep.mp3" volume 0.85
    hide wolf
    show wolf inn_u fight3 red at right
    show tiger smile red at left, walk (500, 1.6 , 3)
    with Dissolve (0.2)
    pause 1.8
    
    # 엘레드가 가헬에게 가까이 
    hide tiger
    show tiger inn_u smile red at surprise_move2
    hide wolf
    show wolf inn_u fight3 red at right
    
    "엘레드는 가헬의 옆에 달라붙었다. 그리고 두툼한 꼬리를 살랑거렸다." id c04_t_0674

    show wolf embarrass
    with dissolve
    
    w "\"무슨, 잠깐!...\"" id c04_t_0675
    
    "엘레드의 꼬리가 가헬의 다리 사이로 들어갔다." id c04_t_0676

    show tiger at surprise_move

    "그것으로 그치지 않고, 끝이 살짝 올라가며 가헬의 고간에 감기듯 붙었다." id c04_t_0677

    show wolf hurt at surprise_move
    with Dissolve (0.2)
    
    # 사람들 으ㅏ어ㅏ으ㅓㅏㅓㅏㅓ아ㅏㅇ~~~ 한번 하기
    play sound "effect/crowd3.mp3" volume 0.85
    
    "관중은 환호성을 질렀다." id c04_t_0678
        
    "가헬이 당황해서 잠깐 굳은 사이, 엘레드가 가헬에게 속삭였다." id c04_t_0679

    show tiger inn_d
    with dissolve
    
    t "\"관객이 이렇게까지 기대하는데, 공연에서 내뺄 생각은 아니겠지?\"" id c04_t_0680

    show wolf inn_d fight2
    with dissolve
    
    w "\"무슨 공연?\"" id c04_t_0681

    show wolf inn_d fight3
    with dissolve
    show tiger inn_u
    with dissolve

    t "\"당연히 이런 것이지.\"" id c04_t_0682
    
    # 엘레드 다시 원위치
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk (-500, 1.6 , 3)
    pause 0.5
    
    "엘레드는 다시 가헬과 거리를 벌리면서 꼬리를 풀었다." id c04_t_0683

    show tiger inn_u at surprise_move
    with Dissolve (0.2)
    pause 0.5
    show tiger at surprise_move
    pause 0.5
    
    "다리를 살짝 벌리면서 자세를 낮추고는 허리를 튕겼다. 리듬을 타듯 몇 번 튕기다가 부드럽게 흔들었다." id c04_t_0684
    
    "엘레드의 가슴도 엉덩이도 묵직하게 흔들렸다. 숨을 멎게 할 정도로 외설적인 움직임이었다." id c04_t_0685
    
    show wolf inn_u fight2
    with dissolve

    w "\"대체 무슨 짓을-\"" id c04_t_0686

    show wolf inn_d fight3
    with dissolve
    show tiger inn_d horny2
    with dissolve

    t "\"자신 없으면 나에게 맡기게. 내가 잘 가르쳐줄 테니.\"" id c04_t_0687

    # 엘레드 가헬 최대한 가까이
    play channel1 "effect/footstep.mp3" volume 0.85
    hide tiger
    hide wolf
    show tiger inn_d horny2 red at left, walk (600, 1.6 , 3)
    show wolf inn_d fight3 red at right
    pause 1.8
    show wolf inn_u fight
    with dissolve
    
    
    
    "그러고는 가헬에게 찰싹 달라붙었다. 가슴과 가슴이 서로 짓눌려서 터질 것 같았다." id c04_t_0688
    "엘레드는 가헬을 도발하면서 동시에 유혹하는 도박을 저질렀다." id c04_t_0689
    "평소라면 절대 하지 않았겠지만, 모두 술에 취한 상태라서 가능한 짓이었다." id c04_t_0690

    # 사람들 으ㅏ어ㅏ으ㅓㅏㅓㅏㅓ아ㅏㅇ~~~ 한번 하기
    play sound "effect/crowd3.mp3" volume 0.85 
       
    "관중은 또다시 우렁찬 환호성을 질렀다." id c04_t_0691
    
    n "\"저 틈에 끼고 싶어...\"" id c04_t_0692
    
    "[pl_name]의 옆에서 누군가 숨넘어가는 소리를 내며 말했다." id c04_t_0693
    "[pl_name]도 그 심정이 이해가 갔다. 보기만 해도 너무 자극적인 모습이었다." id c04_t_0694

    c shy2 "\"(진짜 끼이면 숨이 막혀 죽을지도 모르지만... 양쪽에 가슴이라니...)\"" id c04_t_0695
    
    "[pl_name][josa_eun_neun] 오늘 숨이 막힌 경험이 떠올랐지만, 지금은 그것도 좋게만 느껴졌다." id c04_t_0696
    
    menu :
        "남들과 함께 응원한다." :
            # (씬 조건) (엘레드 호감도는 씬 봐야 지급)
            $ c4t_elred_win = True

            "[pl_name][josa_eun_neun] 다른 관중처럼 소리를 질렀다." id c04_t_0697

            play sound "effect/crowd3.mp3" volume 0.85

            with vpunch
            
            c talk "\"와아아!\"" id c04_t_0698
            
            "[pl_name]의 목소리에 가헬은 당황하면서 [pl_name] 쪽을 바라보았다. 술에 취한 [pl_name][josa_eun_neun] 상기된 표정으로 손을 흔들었다." id c04_t_0699

            "가헬이 한눈판 사이 엘레드는 한 손으로 가헬의 허리를 감싸고 말했다." id c04_t_0700

            show tiger inn_u
            with dissolve

            t "\"잘 보고 배우게.\"" id c04_t_0701

            show tiger :
                xoffset 100
                ease 0.8 yoffset -15
                ease 0.8 yoffset 0
            pause 1.6

            "엘레드가 천천히 온몸을 위아래로 움직였다." id c04_t_0702

            "단순히 자기 몸을 흔드는 게 아니라, 가헬의 몸과 맞대는 것을 의도한 움직임이었다." id c04_t_0703
            
            "엘레드의 피어싱이 가헬의 가슴을 건드렸다. 가슴뿐만 아니라, 복근과 복근이, 그리고 고간과 고간이 비벼지고 있었다." id c04_t_0704

            show wolf hurt at surprise_move
            with Dissolve (0.2)

            w "\"읏!!...\"" id c04_t_0705
            
            # 엘레드 bulge

            show tiger bulge_u
            with dissolve

            $ unlock_character_image("tiger", "tiger b_no base bulge_d")
            $ display_text = _("이미지 : 엘레드(속옷발기)")
            show screen affection_indicator
            
            show wolf fight2 at surprise_move
            with Dissolve (0.2)

            "가헬은 자신을 쿡 찌르는 뜨거운 것에 움찔했다." id c04_t_0706

            "도저히 흥분을 감추지 못하고 발기해 버린 엘레드는, 그것을 둔기처럼 가헬에게 휘둘렀다." id c04_t_0707
            
            show tiger at surprise_move2 :
                xoffset 100 

            "묵직한 충격이 정확하게 가헬의 속옷 위를 때렸다." id c04_t_0708
            
            "엘레드는 맞닿은 가헬의 남근도 불끈거리는 걸 알 수 있었다." id c04_t_0709
            
            # 가헬 bulge
            show wolf bulge_u hurt
            with dissolve

            $ unlock_character_image("wolf", "wolf b_no bulge_d")
            $ display_text = _("이미지 : 가헬(속옷발기)")
            show screen affection_indicator

            pause 0.5
            show tiger laugh red_laugh
            with dissolve
            
            t "\"크하하! 아까의 자신감은 어디로 갔지? 이 거대한 칼은 장식용인가?\"" id c04_t_0710

            show tiger smile red
            with dissolve
            
            "엘레드의 공세에 가헬은 속수무책으로 휘둘렸다. 육체의 흥분과 정신의 수치심이 뒤죽박죽으로 섞여서 제대로 반응할 수 없었다." id c04_t_0711
            "[pl_name][josa_i_ga] 지켜보고 있는데, 여기서 패배를 인정하고 도망갈 수도 없었다." id c04_t_0712

            show tiger bulge_d
            with dissolve
            
            t "\"흠...\"" id c04_t_0713
            
            # 둘 다 알몸 이미지)
            show tiger at surprise_move2 :
                xoffset 100
            show wolf nake_d fight2
            with Dissolve (0.5)
            
            "누가 말릴 새도 없이, 엘레드는 가헬의 속옷 매듭을 잡고 확 당겼다." id c04_t_0714

            show tiger nake_d
            with dissolve

            "동시에 다른 손으로 자신의 속옷도 벗어버렸다." id c04_t_0715
            
            "엄청난 길이와 두께의 남근들이 모두의 시선을 사로잡았다." id c04_t_0716
            "다들 함성을 지르지 못하고 오히려 헛숨을 삼키거나 조용히 감탄을 내뱉었다." id c04_t_0717

            show tiger nake_u horny2
            with dissolve
            
            t "\"하! 이렇게 훌륭한 무기를 숨기고 있었다니. 하지만 기술은 어떨까?\"" id c04_t_0718

            play channel1 "effect/footstep.mp3" volume 0.85
            show tiger at walk (-500, 1.6, 3)
            pause 1.8
            show wolf nake_u hurt
            with dissolve
            
            # 둘이 거리 멀어짐) (가헬눈감기)
            
            "엘레드는 가헬을 두고 혼자서 춤을 추기 시작했다." id c04_t_0719
            show tiger at walk (-300, 1.2, 2)
            pause 1.2
            show tiger at mirror
            with dissolve
            show tiger at walk (-150, 1.2, 2)
            pause 1.2
            show tiger at walk (-500, 1.2, 2)
            pause 1.2
            show tiger at mirror2
            with dissolve
            pause 0.5

            show tiger smile at vshake (0.08, 0, -10) :
                xoffset -500
            with Dissolve (0.2)
            pause 0.5
            show wolf fight2
            with dissolve
    
            "천천히 박자를 타며 아까 근육을 자랑할 때처럼 자세를 잡다가, 가슴의 피어싱을 가볍게 튕기고는 허리를 흔들었다." id c04_t_0720
            "모두 최면에 걸린 듯 엘레드만 바라보았다." id c04_t_0721
            
            "[pl_name]도 말없이 조용하게 관능적인 춤을 보고 있다가, 뭔가 자신의 얼굴에 확 날아와서 비명을 질렀다." id c04_t_0722
            
            # 화면 와장창
            with vpunch

            c ddam2 "\"으악!!\"" id c04_t_0723
        
            "엘레드가 쥐고 있던 속옷 두 개를 [pl_name]에게 던진 것이었다." id c04_t_0724

            show black
            with dissolve
            
            "그러나 [pl_name]의 품을 노리고 던진 것이, 하필이면 정확하게 눈 위로 착지해서 [pl_name]의 얼굴을 뒤덮었다." id c04_t_0725
            
            # (가헬 엘레드 놀람)

            play sound "audio/effect/crash2.mp3" volume 0.4
            with vpunch
            
            "[pl_name][josa_eun_neun] 제자리에서 우당탕 주저앉았다." id c04_t_0726

            show tiger talk
            
            t "\"[pl_name]?\"" id c04_t_0727

            show wolf talk
            
            w "\"[pl_name]!\"" id c04_t_0728
            
            # (둘 고간 가까이)
            camera:
                perspective True
                parallel:
                    zpos -200
                    ypos 90
            
            show tiger :
                zpos 200
                yoffset -130
                xoffset -350
            show wolf :
                zpos 200
                yoffset -130
                xoffset 400

            hide black
            with Dissolve (1)     
            
            "[pl_name][josa_i_ga] 얼굴에서 속옷을 치우자 보인 것은 눈앞에 있는 두 개의 거대한 기둥이었다." id c04_t_0729

            "멀리서 지켜보기만 해도 숨 막히는 크기의 남근이 바로 앞에서 맥박치고 있었다." id c04_t_0730

            "너무 가까워서 핏줄까지 보이는 건 물론이고, 두 수컷의 향기가 느껴지는 것 같았다." id c04_t_0731
       
            "폭력적인 음란함에 [pl_name][josa_eun_neun] 또 비명을 지를 뻔했지만, 꾹 참았다." id c04_t_0732
            
            c "\"나, 저, 괜, 괜찮으니까, 그게...\"" id c04_t_0733
            
            "모두의 이목이 이쪽으로 쏠리자, [pl_name][josa_eun_neun] 제대로 말을 잇지 못했다." id c04_t_0734

            "급격하게 머릿속이 빙글빙글 도는 기분이었다." id c04_t_0735
            
            t "\"후... 미안하네. 일단 여기서 멈추도록 하지.\"" id c04_t_0736

            stop music fadeout 2.5
            

        "둘이 무엇을 하는지 지켜본다." :
            
            $ c4t_gahel_win = True
           
            "[pl_name][josa_eun_neun] 무슨 일이 벌어질지 상상하며 둘을 지켜봤다." id c04_t_0737
            
            "가헬은 갑자기 [pl_name][josa_i_ga] 이 모습을 보고 뭐라고 생각할지 신경 쓰였다." id c04_t_0738
            
            "가헬이 엘레드를 밀어내려는 찰나, 엘레드가 먼저 가헬에게 속삭였다." id c04_t_0739
            
            show tiger smile red
            with dissolve

            t "\"[pl_name]도 기대하는 것 같은데?\"" id c04_t_0740

            show tiger horny2
            show wolf inn_d fight3 red
            with dissolve

            "가헬은 곁눈질로 [pl_name] 쪽을 바라보았다." id c04_t_0741
            "술에 취한 [pl_name][josa_eun_neun] 가슴에 대한 망상에 빠져 얼굴이 붉었다. 엘레드에게는 기대하는 표정으로 보일 법 했다." id c04_t_0742

            show wolf fight
            with dissolve

            "가헬은 그 표정을 보고 다시 승부욕에 불타기 시작했다. 이 대결에 이겨서 [pl_name]에게 멋진 인상을 남길 생각이었다." id c04_t_0743
            
            show wolf fight2
            with dissolve

            w "\"흥, 누가 \'진짜 수컷\'인지 보여주겠다.\"" id c04_t_0744
            
            show wolf inn_u fight
            with dissolve

            "가헬은 엘레드를 밀어내는 대신, 가슴의 피어싱을 붙잡았다." id c04_t_0745
            
            show tiger horny3 red at surprise_move :
                xpos 960

            t "\"으흣!\"" id c04_t_0746
            
            "세게 잡아당기지도 않았는데 엘레드는 자극에 몸을 떨었다." id c04_t_0747

            show wolf inn_d fight
            with dissolve
            
            "가헬은 엘레드의 자세가 무너진 틈을 타서 꼬리를 세게 붙잡았다. 방금 전의 도발에 대한 복수였다." id c04_t_0748
            
            hide tiger
            show tiger inn_d fight2 red at surprise_move2 :
                xoffset 100
            hide wolf
            show wolf inn_d fight at right
            
            t "\"윽, 이건 레슬링이 아니라네.\"" id c04_t_0749
            
            show tiger fight
            show wolf fight2
            with dissolve

            w "\"알고 있다. 엘레드 경이 좋아하는 레슬링은 \'이런 거\' 아니었나?\"" id c04_t_0750

            play sound "audio/effect/hand_clap.mp3" volume 0.6
            show wolf fight at surprise_move

            "가헬은 꼬리를 붙잡은 손을 놓고, 곧바로 엘레드의 엉덩이를 가볍게 때렸다." id c04_t_0751
            
            show tiger horny3 at surprise_move

            "시원하게 드러난 엉덩이에 찰싹 소리와 함께 미세한 손자국이 남았다." id c04_t_0752

            show tiger horny
            with dissolve

            "엘레드는 \'이런 거\'를 좋아한다는 사실을 부정할 수 없었다. 엉덩이를 맞은 순간 몸이 찌릿하게 떨렸기 때문이다." id c04_t_0753
            
            show tiger fight3
            with dissolve

            t "\"그... 정도로는 나를 만족시킬 수 없네.\"" id c04_t_0754
            
            # 엘레드 멀어짐
            play channel1 "effect/footstep.mp3" volume 0.85
            show tiger at walk (0, 1.0, 2)

            "엘레드는 살짝 뒤로 물러서서 말했다. 아직은 여유롭게 말할 수 있지만, 자칫하면 신음을 낼 뻔했다." id c04_t_0755
            "엘레드는 성욕이 터져 나오지 않게 간신히 참고 있었다." id c04_t_0756

            # 가헬이 엘레드 뒤에 붙음

            hide tiger
            show tiger inn_d fight3 red
            show wolf fight3 at mirror :
                xpos 100
            with dissolve
             
            "드디어 주도권을 잡은 가헬은 재빠르게 엘레드의 뒤로 움직였다." id c04_t_0757

            show wolf inn_u
            show tiger inn_u horny3
            with dissolve

            "가헬이 손을 뻗어 엘레드의 가슴을 잡자 엘레드는 당황 했다. 손가락 틈새에 유두와 피어싱이 잡혔다." id c04_t_0758
            
            show wolf fight2 
            with dissolve

            w "\"여기가 약점인가?\"" id c04_t_0759
            
            show wolf fight3
            show tiger horny
            with dissolve

            t "\"자, 잠깐! 윽, 하읏...\"" id c04_t_0760
            
            show wolf at surprise_move2 :
                xpos 100

            "가헬은 손아귀에 힘을 주어 가슴을 주물렀다. 빵 반죽처럼 마구 주무르는 손길에 엘레드는 결국 신음을 뱉고 말았다." id c04_t_0761

            show tiger horny2 at surprise_move

            "엉덩이에 닿은 가헬의 속옷도 엘레드에겐 자극이었다. 엘레드는 가쁜 숨을 들이쉬며 가헬에게 농락당했다." id c04_t_0762
            
            "힘을 주어 탈출할 수도 있었지만, 이 상황을 더 즐기고 싶은 욕망이 너무 컸다." id c04_t_0763
            
            # 엘레드 bulge 불끈! 잠깐쉬고 엘레드 위치 변경
            
            show tiger bulge_u horny3 red with vpunch
            pause 1.0
            play channel1 "effect/footstep.mp3" volume 0.85
            show tiger at walk(300, 1.6, 3)

            t "\"그만! 그만!!\"" id c04_t_0764
            
            show tiger bulge_d horny3 at mirror
            with dissolve

            "엘레드의 속옷이 힘차게 솟아오름과 동시에 엘레드가 가헬을 뿌리쳤다." id c04_t_0765
            
            "엘레드는 벌겋게 달아오른 얼굴로 말했다." id c04_t_0766

            show tiger bulge_u vangry red
            with dissolve

            t "\"제길. 알겠네. 자네도 꽤 강하군. 일단 여기서 멈추도록 하지.\"" id c04_t_0767
            
            stop music fadeout 2.5

    scene bg pub2
    camera:
        perspective True
        parallel:
            zpos 0
            ypos 0
    with Fade(0.8, 0.8, 0.8)
       
    "{i}잠시 후{/i}" id c04_t_0768

    # 평범 가헬 엘레드 스탠딩
    show tiger am_d base_am red at left
    with dissolve
    show wolf am_d base red at right
    with dissolve

    "술집 안의 어수선한 분위기 속에서 엘레드와 가헬은 다시 평소의 복장으로 돌아왔다." id c04_t_0769
    "손님들은 조금 전에 본 것에 대해 속삭이며 엘레드의 눈치를 봤다." id c04_t_0770
    
    t "\"어흠! 불미스러운 일로 중단하였으나, 매력을 보여주기에는 충분한 시간이었다고 생각한다.\"" id c04_t_0771

    play sound "effect/crowd.mp3" volume 0.85   

    "투표가 시작되자 손님들은 각자의 잔을 들고 모였다. 어느 쪽에 잔을 놓을지 고민하는 손님이 대부분이었다." id c04_t_0772
    "그러나 승부는 결국 끝날 수밖에 없었다." id c04_t_0773
    
    if c4t_elred_win==True :

        "엘레드 쪽에 놓인 잔이 더 많았다. 굳이 세어보지 않아도 알 수 있었다." id c04_t_0774
        "점원이 잔 개수를 세어보고 말하자 엘레드는 공식적으로 발표했다." id c04_t_0775

        show tiger am_u talk_am
        with dissolve
        
        t "\"이 결투는 나, 엘레드의 승리로 끝났다. 모두 정직하게 참여해 주어 고맙다.\"" id c04_t_0776

        play sound "effect/crowd_clap.mp3" volume 0.75   
        show tiger am_d base_am
        with dissolve
        
        "아까의 열기가 식어서 그런지는 몰라도, 다들 얌전하게 손뼉을 치며 축하했다." id c04_t_0777
        
        c ddam "\"(엘레드의 음란한... 춤이 결정적이긴 했지.)\"" id c04_t_0778
        
        "그리 오래 본 것도 아닌데, 거의 최면에 걸린 것처럼 자꾸만 떠올랐다." id c04_t_0779

    elif c4t_gahel_win==True :

        "가헬 앞에 놓인 잔이 더 많았다. 생각보다 격차가 많이 벌어진 승부였다." id c04_t_0780
        "점원이 잔 개수를 세어보고 말하자 엘레드는 공식적으로 발표했다." id c04_t_0781

        show tiger am_u talk_am
        with dissolve
    
        t "\"이 결투는 가헬의 승리로 끝났다. 모두 정직하게 참여해 주어 고맙다.\"" id c04_t_0782

        play sound "effect/crowd_clap.mp3" volume 0.75   
        show tiger am_d base_am
        with dissolve
        
        "아까의 열기가 식어서 그런지는 몰라도, 다들 얌전하게 손뼉을 치며 축하했다." id c04_t_0783
        
        c base "\"(다들 가헬의 반격이 더 좋았나 보다.)\"" id c04_t_0784
        
        "조금 과격하긴 했지만, 불리한 싸움을 뒤집고 상대를 지배하는 모습이 인상 깊었다." id c04_t_0785
    
    play music "medieval-fantasy-142837.mp3" volume 0.5  fadein 2.5  

    "테이블이 제자리로 돌아가고 손님들이 흩어지자, 방금까지의 승부는 꿈처럼 느껴졌다. 열광적인 시작에 비해 미지근한 끝이었다." id c04_t_0786

    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at fwalk
    show wolf at fwalk
    pause 0.6

    "[pl_name][josa_eun_neun] 딱히 한 것도 없지만 피곤해졌다. 의자에 늘어져 있는 [pl_name]의 옆에 엘레드와 가헬이 다가왔다." id c04_t_0787
    
    show wine :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    show tiger am_u talk_am
    with dissolve

    t "\"자네도 한 잔 받게.\"" id c04_t_0788

    hide wine
    show tiger am_u base_am
    with dissolve

    c "\"아, 감사합니다. 근데 이걸 왜...\"" id c04_t_0789
    
    "엘레드는 [pl_name][josa_i_ga] 뭐라고 할지 알고 있는 것처럼 말을 덧붙였다." id c04_t_0790
    
    # (엘레드 윙크)
    show tiger am_d wink_am
    with dissolve
    
    t "\"방금 전의 \'특별 행사\' 기념으로 받았다네.\"" id c04_t_0791
    t "\"자네도 피곤해 보이니 이것만 마시고 오늘은 이만 헤어져야겠군.\"" id c04_t_0792

    show tiger am_d base_am
    with dissolve
    
    "엘레드는 정말로 아쉬운 듯 말했다." id c04_t_0793
    
    "가헬은 자기 몫의 잔을 들고 있다가 갑자기 단숨에 들이켰다." id c04_t_0794
    
    show wolf hurt at surprise_move :
        yoffset 135

    pause 1.0
    show wolf am_u fight2
    with dissolve
    
    w "\"크윽... 다 마시면 가자.\"" id c04_t_0795
    
    show wolf am_d fight3
    with dissolve

    "가헬은 정말 단 1초라도 더 머물고 싶지 않아 보였다." id c04_t_0796
    
    c sigh "\"(하긴... 주변 손님들이 다 이쪽을 보는 거 같은 기분이 든다.)\"" id c04_t_0797

    c talk "\"알았어.\"" id c04_t_0798

    "[pl_name][josa_eun_neun] 술에 입을 대자마자 혀가 불타는 것 같았다. 냄새는 향긋한 과일이나 꽃 같은데, 사실은 굉장한 도수의 증류주였다." id c04_t_0799
    "술이 스쳐 지나간 목구멍이 전부 따끈하게 느껴졌다. 내쉬는 숨에도 술의 향기가 나는 기분이었다." id c04_t_0800
    
    c ddam "\"(아니, 이런 걸 한 번에 마셨단 말이야?)\"" id c04_t_0801

    "당연히 가헬의 속은 완전히 엉망진창이 되었다. 표정도 그다지 좋지 않았다." id c04_t_0802
    
    show wolf hurt
    with dissolve

    c ddam2 "\"가헬, 괜찮아?\"" id c04_t_0803

    show wolf am_u hurt2
    with dissolve

    w "\"나는, 괜찮, 다...\"" id c04_t_0804
    
    show wolf hurt
    with dissolve

    "가헬은 지끈거리는 머리를 부여잡고 간신히 말했다. 엘레드에게도 가헬의 상태가 별로 좋아 보이지 않았다." id c04_t_0805
    
    show tiger am_u talk_am
    with dissolve

    t "\"자네는 쓰러지기 전에 물 한 잔 마시게. 걸을 수는 있겠나?\"" id c04_t_0806
    
    show tiger am_d base_am
    with dissolve

    show wolf :
        ease 1.0 yoffset 235 
    
    "가헬은 뭐라고 웅얼거리긴 했으나 제대로 된 대답을 하지 못하고 테이블 위에 고개를 숙였다." id c04_t_0807
    
    c ddam2 "\"가헬?!\"" id c04_t_0808
    
    show tiger am_u talk_am
    with dissolve

    t "\"일단 눕혀야겠네. 빨리 가서 방 하나 예약하게.\"" id c04_t_0809

    show tiger base_am
    with dissolve

    "엘레드의 지시대로 [pl_name][josa_eun_neun] 허둥지둥 움직였다." id c04_t_0810
    
    scene bg backcol with Fade(0.8, 0.8, 0.8)
 
    "엘레드가 가헬을 질질 끌어서 침대에 올려놓기까지 순식간에 이루어졌다. 만취해서 쓰러진 수인을 다뤄본 경험이 많은 것 같았다." id c04_t_0811

    c talk "\"괜찮을까요?\"" id c04_t_0812
    
    t "\"호흡이 멀쩡하니 문제없을걸세. 흠, 혹시 모르니 점원에게 부탁도 해놓아야겠군.\"" id c04_t_0813

    scene bg pub2 with Fade(0.8, 0.8, 0.8)
    
    "엘레드는 술값을 계산하면서 금화 두 개를 더 건넸다. 새벽 동안 가헬을 확인하는 추가 노동의 값으로는 굉장히 후하게 쳐준 것이었다." id c04_t_0814
    "[pl_name][josa_eun_neun] 조금이나마 걱정을 덜어냈다." id c04_t_0815

    stop music fadeout 2.5

label tiger_cg2_start :

    # 밤 길거리
    scene bg street3 with Fade(0.8, 0.8, 0.8)
    play music "tense-and-depressed-142983.mp3" fadein 2.5 volume 0.4

    show tiger am_d base_am red
    with dissolve

    "술집에서 나오니 적당히 서늘한 바람이 불었다. [pl_name][josa_eun_neun] 상쾌한 밤공기를 크게 들이마셨다." id c04_t_0816
    
    c ddam2 "\"(으으, 너무 많이 마셨나? 술이 깨기는커녕 더 어지러운데.)\"" id c04_t_0817
    
    "엘레드는 [pl_name]의 옆에서 크게 웃었다." id c04_t_0818

    show tiger am_u laugh_am red_laugh
    with dissolve
    
    t "\"하하하! 오늘 아주 즐거웠다네. 마무리는 조금 엉망이었지만...\"" id c04_t_0819

    show tiger am_d base_am red
    with dissolve
    
    c talk "\"으음, 저도... 오늘...\"" id c04_t_0820

    "[pl_name][josa_eun_neun] 뭐라고 대답해야 할지 고민하다가 방금의 대결이 떠올랐다." id c04_t_0821
    "뇌리에 박힌 대결의 하이라이트가 다시 튀어나왔다. [pl_name][josa_eun_neun] 머리에 열이 오르는 기분이었다." id c04_t_0822

    c ddam2 "\"(술집에서 \'그런 것\'까지 할 줄은...)\"" id c04_t_0823
    
    "[pl_name][josa_eun_neun] 자꾸만 머릿속에 떠오르는 광경을 억눌렀다. 엘레드 앞에서 표정을 관리하느라 힘들었다." id c04_t_0824

    #엘레드 다가옴
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at fwalk
    pause 2.2
    show tiger am_u
    with dissolve

    "엘레드는 [pl_name]에게 다가가서 어깨에 손을 올렸다. [pl_name][josa_eun_neun] 옷 위로도 엘레드의 두툼한 손을 느낄 수 있었다." id c04_t_0825
    
    c base "\"(술집 안에서는 익숙해져서 몰랐는데, 지금 엘레드에게서 술 냄새 엄청나게 나는구나...)\"" id c04_t_0826
    c sigh "\"(나도 똑같은 상태겠지? 으, 냄새만으로 또 취하는 기분인데...)\"" id c04_t_0827
    
    show tiger am_u talk_am
    with dissolve
    
    t "\"자네는 멀쩡히 걸을 수 있겠나?\"" id c04_t_0828

    show tiger am_u base_am
    with dissolve
    
    c talk "\"뭐, 괜찮을 것 같은데요...\"" id c04_t_0829
    
    "[pl_name][josa_eun_neun] 천천히 가게 방향으로 걷기 시작했다. 엘레드도 손을 얹은 채로 발을 맞추며 따라갔다." id c04_t_0830
    
    c sleep "\"(마지막에 마신 것 때문인가? 점점 더 어지러운데...)\"" id c04_t_0831
    
    "[pl_name]의 걸음걸이는 겉보기에 멀쩡해 보였지만, 머릿속은 그렇지 못했다." id c04_t_0832
    "온 세상이 흐물흐물하게 느껴졌다. 엘레드가 자신을 조금씩 끌어당기고 있는 것도 눈치채지 못했다." id c04_t_0833

    show tiger am_d smile_am
    with dissolve
    
    t "\"자네도 매력적인 육체를 가지고 있군. 보면 볼 수록 내 취향이라네...\"" id c04_t_0834

    "엘레드는 [pl_name]의 드러난 가슴을 보며 음흉한 생각을 했다." id c04_t_0835
    "아까 술집에서 \'한숨 자고 가자\'고 유혹하면 어땠을까? 같은 생각에 다시 갈증이 났다." id c04_t_0836

    c talk "\"하하. 저는 엘레드 님에 비하면 근육도 작고...\"" id c04_t_0837

    "[pl_name]의 머릿속에는 조금 전의 승부가 또 떠올랐다. 터질 것 같은 근육의 향연에 이어서, 야릇한 상황이 생각났다." id c04_t_0838
    "[pl_name][josa_eun_neun] 자꾸만 튀어나오려는 음란한 상상을 억지로 무시했다." id c04_t_0839

    show tiger am_u talk_am
    with dissolve
    
    t "\"전에도 말했지만, 둘만 있을 때는 격식 차리지 않아도 좋다네.\"" id c04_t_0840

    show tiger am_d base_am
    with dissolve

    c "\"어... 그래요.\"" id c04_t_0841
    
    "술에 취한 탓인지, [pl_name][josa_eun_neun] 엘레드의 말을 바로 수긍했다." id c04_t_0842
    "엘레드는 은근슬쩍 [pl_name]의 허리로 손을 옮기고 말했다." id c04_t_0843

    show tiger am_u talk_am
    with dissolve
    
    t "\"그리고 궁금한 게 있다면 무엇이든 물어보게. 나도 자네를 더 자세히... 알고 싶으니까.\"" id c04_t_0844

    show tiger am_d base_am
    with dissolve
    
    c "\"아! 궁금한 거라면, 처음 봤을 때부터 궁금한 게 있었는데...\"" id c04_t_0845
    
    "[pl_name][josa_eun_neun] 평소라면 절대 하지 않았을 질문을 꺼냈다." id c04_t_0846
    
    c "\"젖에 달린 \'그거\' 당겨봐도 돼요?\"" id c04_t_0847
    
    "엘레드는 당황스럽지만, 이것을 [pl_name]의 유혹으로 받아들였다. 심장이 두근거리며 어떻게 이 상황을 이끌어갈지 빠르게 생각했다." id c04_t_0848
    
    show tiger am_u smile_am
    with dissolve
    
    t "\"당연하지. 저기에서 보여주도록 하겠네.\"" id c04_t_0849

    show tiger am_d smile_am
    with dissolve
    
    "엘레드는 가까운 뒷골목으로 [pl_name][josa_eul_reul] 이끌었다." id c04_t_0850

    # 밤 뒷골목 배경
    scene bg back_alley_night with Fade(0.8, 0.8, 0.8)

    "밤의 뒷골목은 당연히 어두웠다. 아무리 밝은 달빛이라도 여기까지 환하게 비출 수는 없었다." id c04_t_0851
    
    "[pl_name][josa_eun_neun] 어렴풋이 보이는 잡동사니에 정신이 팔렸다." id c04_t_0852

    show tiger am_u talk_am red
    with dissolve
    
    t "\"... 이쪽을 보게.\"" id c04_t_0853

    #엘레드 갑옷 벗기
    play sound "audio/effect/puton.mp3" volume 0.5
    show tiger inn_u base red
    with dissolve
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at fwalk    

    "엘레드는 갑옷을 벗고 [pl_name]에게 가까이 다가왔다." id c04_t_0854
    
    c shy2 "\"(우와... 이렇게 가까이에서 보니까 더 엄청난데?)\"" id c04_t_0855
    
    "[pl_name][josa_eun_neun] 지금 상황을 자각하지 못하고, 엘레드의 몸에 대한 감상에 빠져있었다." id c04_t_0856

    show tiger at surprise_move :
        yoffset 135

    "바위처럼 울퉁불퉁한 근육의 굴곡이 선명하게 드러나고, 가슴에 달린 피어싱은 가볍게 흔들렸다." id c04_t_0857

    show tiger inn_d smile
    with dissolve
    
    t "\"만져도 좋네.\"" id c04_t_0858
    
    "[pl_name][josa_eun_neun] 말없이 손을 뻗어 금색 고리를 붙잡았다." id c04_t_0859
    "예고 없이 당기자, 탄력 있는 가슴이 파르르 떨렸다. 엘레드는 반사적으로 신음을 흘렸다." id c04_t_0860

    show tiger inn_u horny
    with dissolve

    show tiger at surprise_move :
        yoffset 135
    
    t "\"흐응!...\"" id c04_t_0861
    
    c "\"신기하다.\"" id c04_t_0862

    show tiger at surprise_move :
        yoffset 135
    
    "[pl_name][josa_i_ga] 피어싱을 당길 때마다 엘레드는 쾌락과 고통을 동시에 느꼈다." id c04_t_0863

    # 엘레드 bulge
    show tiger bulge_u
    with dissolve

    "흥분을 참지 못한 아랫도리는 속옷을 밀어 올리고 있었다. 엘레드는 유혹적인 몸짓 없이도 음란함을 가득 뿜어낼 수 있었다." id c04_t_0864
    
    show tiger bulge_d horny2
    with dissolve

    t "\"흐으... 궁금한 건 충분히 해결했나?\"" id c04_t_0865
    
    "엘레드는 욕망이 끓어오르는 눈빛으로 [pl_name][josa_eul_reul] 보았다. 에메랄드빛 눈동자 속에는 불길이 타오르고 있었다." id c04_t_0866
    
    c question2 "\"이걸 하면 느낌이 다른가요?\"" id c04_t_0867

    show tiger bulge_u horny2
    with dissolve
    
    t "\"나는 꽤 민감해졌다네. 덕분에 이렇게...\"" id c04_t_0868

    camera:
        perspective True
        parallel:
            ease 1.5 zpos -160 ypos 80
    
    show tiger :
        ease 1.5 zpos 90 yoffset -90
        

            
    
    "엘레드는 [pl_name]의 손목을 잡아 아래로 이끌었다. 손에 잡히는 속옷 안의 자지가 불끈거렸다." id c04_t_0869
    "엘레드는 입술을 핥으며 말했다." id c04_t_0870
    
    t "\"나도 충분히 만족하고 싶은데, 자네가 도와줘야 하지 않겠나?\"" id c04_t_0871
    
    c ddam2 "\"아, 어... 제가요?\"" id c04_t_0872

    camera:
        perspective True
        parallel:
            ease 1.5 zpos 0 ypos 0
    
    show tiger :
        ease 1.5 zpos 0 yoffset 135
    
    "[pl_name][josa_eun_neun] 취한 탓에 상황을 제대로 이해하지 못하고 얼빠진 대답을 했다." id c04_t_0873
    
    t "\"자네가 이렇게 만들었으니, 자네 잘못이라고 생각하게.\"" id c04_t_0874

    show tiger :
        zpos 90
    with dissolve

    "엘레드는 자기 자신을 위한 변명을 중얼거리며 [pl_name][josa_eul_reul] 벽으로 부드럽게 밀었다." id c04_t_0875
    
    "[pl_name][josa_eun_neun] 그제야 상황을 이해했다. 이대로 잡아먹힌다는 생각에 덜컥 겁이 났다." id c04_t_0876
    
    c "\"자, 잠깐. 지금 바로 해요? 그건... 곤란한데요.\"" id c04_t_0877
    
    "엘레드는 [pl_name]의 반응에 마음이 조급해졌다. 드디어 [pl_name]의 마음을 아주 조금 얻었나 싶더니, 손가락 틈새로 모래처럼 빠져나갔다." id c04_t_0878
    "엘레드는 지금 당장 [pl_name][josa_eul_reul] 안고 싶었다. 욕망이 앞서나가서 또 후회할 선택을 저질렀다." id c04_t_0879

    show tiger bulge_d smile
    with dissolve
    
    t "\"너무 부담스럽게 생각하지 말게. 친구 사이에 한 번쯤 {color=#ee3939}\'가볍게 즐기는 것\'{/color}도 좋지 않나?\"" id c04_t_0880

    menu :

        "수락한다." :
           
            "[pl_name][josa_eun_neun] 엘레드의 제안을 진지하게 고민했다." id c04_t_0881
        
        "거절한다." :

            "[pl_name][josa_eun_neun] 엘레드의 제안을 거절하려고 하다가 다시 고민해본다." id c04_t_0882
    
    c consider "\"(즐기는 친구 사이? 못 할 건 아니지만, 엘레드랑 그래도 괜찮을까?)\"" id c04_t_0883
    
    "[pl_name][josa_ra_ira]고 성욕이 없는 건 아니었다. 혼자서 대충 처리하는 것과, 둘이서 진득하게 시간을 보내는 것은 다르다." id c04_t_0884
    "[pl_name][josa_eun_neun] 당장의 욕구와 미래의 관계 사이에서 저울질했다." id c04_t_0885
    
    c base "\"(음, 그래도 모르는 수인보단 엘레드가 낫긴 하지. 엘레드라면 능숙하게 잘 할 테고, 거기도 크고...)\"" id c04_t_0886
    
    "취한 탓에 평소보다 마음의 장벽이 낮아졌다. [pl_name]의 마음은 욕구 쪽으로 조금 더 기울었다." id c04_t_0887
    
    c talk "\"그래요. 즐기기만 하는 사이라면...\"" id c04_t_0888

    show tiger bulge_u
    with dissolve
        
    t "\"후회하지 않게 해주겠네.\"" id c04_t_0889

    # 엘레드 알몸
    
    play sound "audio/effect/takeoff.mp3" volume 0.55
    show tiger nake_u at surprise_move2
    with Dissolve (0.2)

    "엘레드는 재빠르게 자기 속옷을 벗어 던지고, [pl_name]의 옷도 벗기기 시작했다." id c04_t_0890

    c nake_d shy2 "\"으, 조금 추운데.\"" id c04_t_0891

    show tiger :
        ease 1 yoffset 200
    
    "코트를 벗겨낸 엘레드는 허리를 조금 숙였다." id c04_t_0892

    with hpunch

    "순식간에 바지까지 벗겨진 [pl_name][josa_eun_neun] 가볍게 몸을 부르르 떨었다. 못 참을 정도는 아니지만 익숙한 느낌이 아니었다." id c04_t_0893

    show tiger nake_d
    with dissolve

    t "\"조금만 참으면 뜨겁게 해주겠네.\"" id c04_t_0894

    show tiger :
        ease 1 yoffset 135
    
    "엘레드는 [pl_name]의 옷을 모두 벗기고 일어섰다. 느리게 눈을 깜빡이는 [pl_name][josa_eul_reul] 마주 보았다." id c04_t_0895

    show tiger nake_u horny2
    with dissolve

    t "\"제길...\"" id c04_t_0896

    show tiger nake_d
    with dissolve
    
    "[pl_name][josa_wa_gwa]의 첫 입맞춤을 이런 식으로 하고 싶진 않았다." id c04_t_0897
    "하지만 입맞춤을 참는 건 더 싫었다. 욕망에 패배해 버린 자신이 가장 싫었다." id c04_t_0898

    show tiger nake_u horny3 :
        zpos 130
    with dissolve        

    "엘레드는 자괴감과 함께 다가갔다." id c04_t_0899
    
    with hpunch

    c horny4 "\"윽!...\"" id c04_t_0900

    play sound "audio/effect/SPS - (9).mp3" volume 0.5
    show tiger horny2
    with dissolve
    
    "엘레드는 [pl_name][josa_eul_reul] 벽에 세게 밀어붙이며 거칠게 입술을 핥았다." id c04_t_0901
    "엘레드의 혀가 저항 없이 [pl_name]의 입속으로 들어갔다. 엘레드는 눈을 감고 촉감에 집중했다." id c04_t_0902
    
    play channel1 "effect/breath.mp3" volume 0.55 fadeout 2.5
    
    c horny2 "\"흐응...\"" id c04_t_0903
    
    "[pl_name][josa_eun_neun] 눈을 게슴츠레 뜨고, 코로 뜨거운 숨을 내뱉었다." id c04_t_0904

    play sound "audio/effect/SPS - (8).mp3" volume 0.5

    "엘레드의 혀는 [pl_name]의 혓바닥을 부드럽게 문지르며 구석구석을 자극했다." id c04_t_0905
    
    c horny2 "\"(고양잇과는 역시 까슬까슬하네.)\"" id c04_t_0906
    
    "[pl_name][josa_eun_neun] 엘레드의 혀 감촉에 대한 감상을 간단하게 정리했다." id c04_t_0907
    
    show tiger nake_d horny at surprise_move2
    with Dissolve (0.2)

    "엘레드는 숙련된 기술로 [pl_name]의 혀를 애무하다가, 흥분을 참지 못하고 거칠게 빨아당겼다." id c04_t_0908

    play sound "effect/sticky2.mp3" volume 0.7

    "고요한 뒷골목에서 젖은 소리만 울려 퍼졌다. 엘레드의 손은 [pl_name]의 팔을 꽉 붙잡았다." id c04_t_0909
    
    c horny4 "\"(약간 아픈데...)\"" id c04_t_0910
    
    "[pl_name][josa_eun_neun] 그렇게 생각하면서도, 그냥 가만히 있었다. 적당한 쾌감이 느껴지기도 했고, 움직이기 귀찮기도 했다." id c04_t_0911
    "[pl_name][josa_eun_neun] 잡생각을 비우고 주어지는 쾌감을 즐겼다." id c04_t_0912

    show tiger nake_u horny2
    with dissolve
    
    t "\"후우...\"" id c04_t_0913

    show tiger :
        zpos 80
    with dissolve
    
    "긴 키스 끝에 엘레드는 살짝 뒤로 물러섰다. 둘 사이에 침이 얇게 실처럼 이어졌다." id c04_t_0914
    "엘레드의 자지는 욱신거릴 정도로 빳빳하게 위로 서 있었다." id c04_t_0915
    "당장이라도 구멍에 꽂아 넣고 싶지만, 엘레드의 굵기를 감당하려면 준비가 필수였다." id c04_t_0916

    show tiger nake_d talk
    with dissolve
    
    t "\"잠시만...\"" id c04_t_0917

    show oil :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "엘레드는 재빠르게 허브 오일을 꺼냈다. 병을 열자, [pl_name]에게 익숙한 냄새가 났다." id c04_t_0918

    hide oil
    show tiger nake_u talk
    with dissolve
    
    t "\"여기 잠깐 앉아보게. 다리는 들고.\"" id c04_t_0919

    show tiger nake_d base
    with dissolve

    camera:
        perspective True
        parallel:
            ease 0.5 ypos 20
            ease 0.5 ypos 0

    play sound "audio/effect/takeoff.mp3" volume 0.6
    
    "[pl_name][josa_eun_neun] 시키는 대로 대충 상자 위에 걸터앉았다." id c04_t_0920

    play sound "effect/sticky3.mp3" volume 0.7
    show tiger :
        zpos 130
    with dissolve

    "다리를 움직이자마자 엘레드의 손이 빠르게 다가왔다. 오일이 듬뿍 발라진 손가락이 [pl_name]의 구멍을 건드렸다." id c04_t_0921
    
    c horny4 "\"으읏...\"" id c04_t_0922

    show tiger nake_u talk
    with dissolve
    
    t "\"이대로는 아무것도 안 들어간다네. 심호흡하고 긴장을 풀도록.\"" id c04_t_0923

    play sound "effect/sticky.mp3" volume 0.65
    show tiger nake_u base
    with dissolve
    pause 0.5
    show tiger :
        ease 1 yoffset 175
        ease 1 yoffset 135
    
    "엘레드의 두툼한 손가락이 [pl_name]의 속으로 조금씩 들어갔다." id c04_t_0924
    
    c "\"하윽! 으, 후우우우우...\"" id c04_t_0925
    
    "[pl_name][josa_eun_neun] 움찔거리며 다리를 떨었다. 손가락 하나만으로도 쉽지 않았다. 의식적으로 숨을 크게 내쉬었다." id c04_t_0926
    
    show tiger nake_d talk
    with dissolve
    
    t "\"꽤 오래 걸리겠군...\"" id c04_t_0927

    show tiger nake_d base
    with dissolve
    pause 0.5
    play sound "effect/sticky2.mp3" volume 0.7
    show tiger :
        ease 1 yoffset 175
        ease 1 yoffset 135
    
    "엘레드는 일단 천천히 움직이면서 [pl_name]의 안쪽을 탐색했다." id c04_t_0928

    play sound "effect/sticky3.mp3" volume 0.7
    show tiger nake_u smile
    with dissolve
    
    t "\"자네는 여기쯤인가?\"" id c04_t_0929

    show tiger nake_u
    with dissolve
    
    c "\"조금, 조금 더 안쪽...\"" id c04_t_0930

    with hpunch
    play sound "effect/sticky.mp3" volume 0.65

    "엘레드는 손끝으로 [pl_name]의 전립선을 찾았다. 살살 문지르자 바로 [pl_name]의 허벅지가 부르르 떨렸다." id c04_t_0931
    "엘레드는 지금 당장 이 구멍에 넣고 싶은 충동을 느꼈다." id c04_t_0932

    play sound "audio/effect/SPS - (1).mp3" volume 0.7

    "흥분에 머리가 터질 것 같지만 어떻게든 억눌렀다. 대신 손가락 2개를 집어넣었다." id c04_t_0933
    
    with hpunch

    c "\"헉! 끄으으으으...\"" id c04_t_0934

    show tiger nake_u talk
    with dissolve
    
    t "\"힘들겠지만 좀 참아주게. 자네를 다치게 하고 싶지 않으니까.\"" id c04_t_0935

    play channel1 "effect/breath.mp3" volume 0.55 fadeout 2.5
    show tiger nake_u base
    with dissolve
    
    "[pl_name][josa_eun_neun] 헐떡이는 호흡으로 대답을 대신했다." id c04_t_0936

    play sound "audio/effect/SPS - (8).mp3" volume 0.5
    show tiger :
        ease 1 yoffset 175
        ease 1 yoffset 135

    "엘레드는 손가락을 움직이며 [pl_name]의 뒷구멍을 차근차근 넓혀갔다." id c04_t_0937
    "엘레드의 굵기에 익숙한 상대였다면, 이 정도 시점에서 본편으로 넘어갔다. 하지만 [pl_name]의 반응을 보아하니 아직 힘들 것 같았다." id c04_t_0938
    
    c horny3 "\"흐으... 응! 아흣!\"" id c04_t_0939

    with vpunch
    
    "[pl_name][josa_eun_neun] 전립선을 쿡쿡 찌르는 느낌에 저절로 신음을 뱉었다." id c04_t_0940

    show tiger nake_u smile
    with dissolve

    "엘레드가 작정하고 자극하자 쾌락이 조금씩 고통을 잠식하기 시작했다. 엘레드는 [pl_name]의 반응을 보며 미소지었다." id c04_t_0941

    show tiger nake_d smile
    with dissolve

    t "\"자네도 육체는 솔직하군. 앞으로도 자주 이렇게 대화하지 않겠나?\"" id c04_t_0942

    c "\"그, 그건... 하윽! 글쎄요.\"" id c04_t_0943

    show tiger nake_u fight
    with dissolve
    
    "엘레드는 또 대답을 회피하는 [pl_name] 때문에 약간 짜증이 났다." id c04_t_0944

    play sound "effect/sticky.mp3" volume 0.65
    show tiger :
        ease 0.4 yoffset 175
        ease 0.4 yoffset 135
        ease 0.4 yoffset 175
        ease 0.4 yoffset 135

    "원하는 대답을 듣고 싶어서, 좀 더 [pl_name]의 안쪽을 강하게 문지르며 괴롭혔다." id c04_t_0945

    show tiger nake_u smile
    with dissolve
    
    t "\"이쪽 입은 좋다고 말하는군?\"" id c04_t_0946
    
    with vpunch

    c horny4"\"아니, 우읏! 그아으으으...\"" id c04_t_0947
    
    "[pl_name]의 반박은 신음에 묻혀버렸다. 엘레드는 손가락으로 구멍을 휘저으며 다음 단계를 준비했다." id c04_t_0948

    if c4t_resque_pick==True and c4t_elred_win==True :
        jump c4t_see
    else :
        # 검은 화면
        scene bg backcol with Fade(0.8, 0.8, 0.8)

        "이 다음 엄청나게 섹스했다." id c04_t_0949
        jump c4t_after

label c4t_see:
    scene bg back_alley_night with Fade(0.8, 0.8, 0.8)
   
    $ persistent.tiger_unlocked[1]= True

    # 씬 보면 호감도 +1
    $ tiger_love +=1
    $ display_text = _("엘레드 호감도 변화")

    show tiger nake_u talk red
    with dissolve

    t "\"준비됐나?\"" id c04_t_0950

    show tiger nake_d base
    with dissolve

    "[pl_name][josa_eun_neun] 성욕으로 타오르는 에메랄드빛 눈동자를 마주했다." id c04_t_0951
    "무슨 일이 일어날지 알면서도 거부할 수 없었다. [pl_name][josa_eun_neun] 헐떡거리면서 고개를 끄덕였다." id c04_t_0952

    show tiger nake_u talk
    with dissolve

    t "\"떨어지면 위험하니 꽉 잡게.\"" id c04_t_0953

    show tiger nake_u base
    with dissolve

    with vpunch

    c nake_d ddam2 "\"뭐, 뭐를... 으악!\"" id c04_t_0954

    stop music fadeout 2.5

    # 여기서부터 cg
    
    scene bg tiger_s2_background
    show tiger_s2_01
    with Fade(0.8, 0.8, 0.8)
    play sound "effect/heart_beat.mp3" volume 0.75

    "엘레드는 [pl_name]의 다리 아래에 손을 집어넣고 번쩍 들어 올렸다." id c04_t_0955
    "[pl_name][josa_eun_neun] 반사적으로 팔을 허우적대다가 간신히 엘레드의 목쯤을 붙잡았다." id c04_t_0956
    "공중에 들어 올려진 [pl_name][josa_eun_neun] 크게 당황했다." id c04_t_0957
    "떨어지는 것보다 무서운 게 아래에서 느껴졌다. 엘레드의 자지는 불끈거리면서 [pl_name]의 뒷구멍을 툭툭 치고 있었다." id c04_t_0958
    
    t nake_d talk red "\"[pl_name]...\"" id c04_t_0959

    show tiger_s2_01 :
        ease 0.3 xoffset 10
        ease 0.5 xoffset -10
        ease 0.3 xoffset 0  

    play sound "audio/effect/sticky4.mp3" volume 0.7

    "엘레드는 조금씩 자지를 밀어 넣었다." id c04_t_0960
    "귀두는 쉽게 들어갔으나, 진짜 문제는 엄청나게 굵은 기둥이었다." id c04_t_0961

    play sound "audio/effect/CI-I - (12).mp3" volume 1

    hide tiger_s2_01
    show tiger_s2_frame
    show tiger_s2_02
    show tiger_s2_01_crop
    with vpunch

    
    c nake_d horny4 "\"잠깐, 천천히, 끄으으으윽!!...\"" id c04_t_0962
    
    "[pl_name][josa_eun_neun] 거의 숨넘어가는 소리를 내며 바들바들 떨었다." id c04_t_0963
    "도저히 뒤로 들어와서는 안 될 것이 쑤욱 들어왔다. 저절로 눈물이 흐를 정도로 아팠다." id c04_t_0964
    
    t horny3 "\"크윽!...\"" id c04_t_0965
    
    "엘레드도 고통스럽기는 마찬가지였다. 너무 성급하게 넣었는지, 자지가 꽉 조이다 못해 잘근잘근 씹히는 것 같았다." id c04_t_0966
    
    t "\"미안하네. 내가 너무 성급했군.\"" id c04_t_0967

    show tiger_s2_02 :
        ease 0.7 xoffset 18
        ease 0.1 xoffset 0
        ease 0.1 xoffset 13
        ease 0.1 xoffset 0
    show tiger_s2_01_crop :
        ease 0.7 xoffset 18
        ease 0.1 xoffset 0
        ease 0.1 xoffset 13
        ease 0.1 xoffset 0
    
    play sound "audio/effect/sticky.mp3" volume 0.65

    "엘레드는 진땀을 흘리며 허리를 뒤로 뺐다. 그러나 기둥의 가장 굵은 부분이 입구에 딱 걸렸다." id c04_t_0968
    
    c "\"으헉! 잠깐, 멈춰! 멈춰봐요... 지금 무리해서 빼면 찢어질 것 같은데.\"" id c04_t_0969
    
    t "\"그렇다고 더 넣을 수는 없지 않나.\"" id c04_t_0970
    
    "[pl_name][josa_eun_neun] 찰나의 순간에 판단을 내렸다." id c04_t_0971
    
    c "\"아니, 그냥 다 넣어버려요. 빨리!\"" id c04_t_0972

    play sound "audio/effect/sticky2.mp3" volume 0.7

    hide tiger_s2_02
    hide tiger_s2_01_crop
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    "[pl_name]의 재촉에 엘레드는 반신반의하면서 다시 [pl_name][josa_eul_reul] 끌어당겼다." id c04_t_0973
    
    c "\"하으으윽!...\"" id c04_t_0974
    
    "[pl_name][josa_eun_neun] 깊게 들어오는 자지가 내장을 밀어내는 것 같았다. 강제로 숨을 내쉴 수밖에 없었다." id c04_t_0975
    "뿌리까지 전부 박아 넣은 엘레드는 만족감과 동시에 약간 겁이 났다." id c04_t_0976
    
    t horny2 "\"자네, 괜찮나?\"" id c04_t_0977
    
    c "\"안 괜찮으니까, 가만히 있어봐요...\"" id c04_t_0978
    
    "[pl_name][josa_eun_neun] 헐떡거리면서 간신히 호흡했다. 안 그래도 취했는데 호흡까지 가빠지니 눈앞이 팽팽 돌았다." id c04_t_0979

    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_04
    with dissolve

    show tiger_s2_03 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0

    show tiger_s2_04 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0

    "[pl_name][josa_i_ga] 안정을 취하는 동안, 엘레드는 움직이지도 못하고 안절부절못했다." id c04_t_0980
    "흥분이 조금 가라앉으면 편해지겠지만, 오히려 [pl_name]의 안쪽이 자지를 마구 자극하고 있었다. 엘레드에게는 고문과도 같은 시간이었다." id c04_t_0981
    
    c horny3 "\"후우, 하아...\"" id c04_t_0982
    
    t "\"이제는 좀 어떤가?\"" id c04_t_0983

    hide tiger_s2_03
    hide tiger_s2_04
    show tiger_s2_03_crop
    show tiger_s2_05
    with dissolve
    hide tiger_s2_03_crop
    hide tiger_s2_05
    show tiger_s2_03
    show tiger_s2_04
    with dissolve
    
    
    "[pl_name][josa_eun_neun] 대답 대신 고개를 작게 끄덕였다." id c04_t_0984

    play sound "audio/effect/sticky2.mp3" volume 0.7
    hide tiger_s2_03
    hide tiger_s2_04
    hide tiger_s2_frame2
    show tiger_s2_06
    with Dissolve (0.8)

    "엘레드는 조심스럽게 움직이기 시작했다." id c04_t_0985
    "엘레드는 천천히 움직였을 뿐인데, 무시무시한 압박감이 [pl_name]의 심장까지 치고 올라왔다." id c04_t_0986
    
    c "\"(난 무슨 생각으로 이걸 하자고 했지?)\"" id c04_t_0987
    
    "고통보다 공포가 훨씬 더 컸다." id c04_t_0988
    "도망가고 싶지만, 도망갈 곳이 없었다. 그 아찔함이 이상하게 중독적이었다." id c04_t_0989

    play channel1 "audio/effect/wet_slap.mp3" volume 0.8
    
    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_06
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch   
    
    "엘레드는 조금씩 속도를 높였다." id c04_t_0990
    
    t "\"자네, 의외로 재능이 있군.\"" id c04_t_0991
    
    "[pl_name][josa_eun_neun] 겉으로 별다른 반응을 보이지 않았다. 너무 충격적인 감각을 처리하느라 뇌가 멈춰버린 기분이었다." id c04_t_0992


    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch   

    "엘레드는 [pl_name][josa_eul_reul] 꽉 붙잡고 욕망대로 움직였다." id c04_t_0993

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch  

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    "본능이 엘레드를 지배하는 순간이었다. 철벅철벅 소리가 점점 더 커졌다." id c04_t_0994
    "힘차게 움직일 때마다 [pl_name]의 자지가 엘레드의 가슴골을 때렸다." id c04_t_0995

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    c "\"하응! 아, 거기, 으흣!\"" id c04_t_0996
    
    with hpunch

    "엘레드는 [pl_name]의 허벅지가 쾌감에 바들바들 떠는 것을 느낄 수 있었다." id c04_t_0997
    "[pl_name]도 자신의 속에서 불끈거리는 엘레드의 자지가 느껴졌다." id c04_t_0998
    
    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    show white :
        alpha 0.7
    with Fade (0.2, 0.1, 0.15)
    hide white with Dissolve (0.25)

    "엘레드가 찌를 때마다 머릿속이 하얗게 번쩍거렸다." id c04_t_0999

    show tiger_s2_03 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_08 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_spike :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_line :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0

    "[pl_name]의 손톱이 엘레드에게 좀 더 깊게 박혔다." id c04_t_1000
    
    t "\"... 그대. 재촉하는 건가?\"" id c04_t_1001
    
    "[pl_name][josa_eun_neun] 엘레드의 말이 미묘하게 바뀐 것을 눈치채지 못했다." id c04_t_1002

    show tiger_s2_03 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_08 :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_spike :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
    show tiger_s2_line :
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0

    "애초에 엘레드가 뭐라고 말하는지 신경 쓸 수 없었다. [pl_name][josa_eun_neun] 그저 숨을 헐떡이며 엘레드에게 매달렸다." id c04_t_1003

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (12).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch  

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    c "\"하윽!... 아! 으흥! 하아...\"" id c04_t_1004
    
    "숨만 쉬어도 신음이 저절로 튀어나왔다." id c04_t_1005
    "맨정신이었다면 어떻게든 억누르려 했겠지만, 그럴 생각이 들지 않았다." id c04_t_1006
    "[pl_name][josa_eun_neun] 쏟아지는 쾌감에 허우적거릴 뿐이었다." id c04_t_1007
    
    t "\"제길, 못 참겠군!\"" id c04_t_1008

    play channel1 "audio/effect/wet_slap.mp3" volume 0.8

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (12).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch  

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.1)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.1)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    show tiger_s2_frame2
    hide tiger_s2_07
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    "엘레드는 그르렁거리며 더욱 빠르게 [pl_name][josa_eul_reul] 몰아붙였다." id c04_t_1009
    "굵은 자지가 내벽을 쓸어올리며 온갖 지점을 자극했다." id c04_t_1010
    "그것은 엘레드의 자지도 똑같이 자극당한다는 뜻이었다." id c04_t_1011

    with hpunch
    
    t "\"크윽!!...\"" id c04_t_1012

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    pause 0.4

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    pause 0.4

    hide tiger_s2_frame2
    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_07
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    hide tiger_s2_07
    show tiger_s2_frame2
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    stop channel1 fadeout 1.5 
    
    "엘레드는 몇 번 더 강력하게 찌르고는 그대로 굳어버렸다." id c04_t_1013
    "흥분을 참지 못하고 사정해 버린 것이다." id c04_t_1014
    
    play sound "audio/effect/sqz2.mp3" volume 0.7
    show tiger_s2_line2
    show tiger_s2_frame3
    with vpunch

    "진득한 수컷의 즙이 흘러나오기 시작했다." id c04_t_1015

    play sound "audio/effect/sqz3.mp3" volume 0.7
    with vpunch
    show tiger_s2_frame4
    show tiger_s2_09
    with vpunch
    
    c "\"흐억!\"" id c04_t_1016
    
    "속으로 뜨거운 물이 왈칵왈칵 들어오는 느낌에 [pl_name][josa_eun_neun] 화들짝 놀랐다." id c04_t_1017
    "안쪽으로 강하게 분출하는 게 느껴졌다. 화산에서 용암이 터져 나오는 것 같았다." id c04_t_1018
    
    play sound "audio/effect/sticky4.mp3" volume 0.7

    t "\"그르르르...\"" id c04_t_1019
    
    "엘레드는 반사적으로 튀어나오는 짐승의 소리를 억눌렀다." id c04_t_1020
    "이 정도로는 만족할 수 없었다." id c04_t_1021
    "자신의 모든 것을 쏟아부을 생각으로 엘레드는 다시 움직였다." id c04_t_1022

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    c "\"흐아앗! 자, 잠깐!... 으윽-\"" id c04_t_1023

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    t "\"미안하네. 도저히, 멈출 수가, 읏!\"" id c04_t_1024

    with hpunch
    
    "엘레드가 구멍에 깊숙이 박을 때마다, 정액이 질퍽하게 새어 나왔다." id c04_t_1025
    "엘레드는 정액이 바닥으로 흘러내리는 만큼 다시 안에 채워 넣고 있었다." id c04_t_1026
    "[pl_name][josa_eun_neun] 반사적으로 손을 꽉 쥐고 엘레드의 피부에 상처를 남겼다." id c04_t_1027

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.2)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.15)

    play sound "audio/effect/CI-I - (12).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    t "\"[pl_name], [pl_name]... 크윽!!\"" id c04_t_1028

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (4).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    pause 0.4

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (6).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch

    pause 0.4

    hide tiger_s2_03
    hide tiger_s2_08
    hide tiger_s2_09
    hide tiger_s2_spike
    hide tiger_s2_line
    show tiger_s2_frame5
    show tiger_s2_07
    show tiger_s2_10
    with Dissolve (0.3)

    play sound "audio/effect/CI-I - (20).mp3" volume 1
    hide tiger_s2_07
    hide tiger_s2_10
    hide tiger_s2_frame5
    show tiger_s2_03
    show tiger_s2_08
    show tiger_s2_09
    show tiger_s2_spike
    show tiger_s2_line
    with vpunch
    
    "몇 번의 강한 찌르기 끝에 엘레드는 \'진짜\' 절정을 느꼈다." id c04_t_1029

    play sound "audio/effect/sqz1.mp3" volume 0.7
    show tiger_s2_11
    with vpunch
    with vpunch

    "[pl_name][josa_eun_neun] 계속된 쾌감에 절여져서 자신이 사정을 했는지도 눈치채지 못했다." id c04_t_1030
    "안팎으로 푹 젖은 [pl_name][josa_eun_neun] 취기까지 더해서 몸이 축축 늘어지는 기분이었다." id c04_t_1031

    play sound "audio/effect/sqz2.mp3" volume 0.7
    hide tiger_s2_09
    hide tiger_s2_11
    hide tiger_s2_spike
    hide tiger_s2_line
    hide tiger_s2_line2
    show tiger_s2_12
    with dissolve

    show tiger_s2_03 :
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 0
    show tiger_s2_08 :
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 0
    show tiger_s2_12 :
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 15
        ease 0.7 xoffset -15
        ease 0.7 xoffset 0

    play channel1 "effect/breath.mp3" volume 0.55 fadeout 2.5

    t "\"하아, 하아...\"" id c04_t_1032
    
    "쾌락에 젖은 엘레드는 혀를 내밀고 헐떡거렸다." id c04_t_1033
    "[pl_name]도 상태는 별로 다르지 않았다. 격정적인 섹스 끝에 숨을 고르는 두 짐승만이 있었다." id c04_t_1034
    
    stop music fadeout 2.5

    $ renpy.end_replay()

label c4t_after:

    # 밤 뒷골목
    scene bg back_alley_night with Fade(0.8, 0.8, 0.8)
    play music "tense-and-depressed-142983.mp3" fadein 2.5 volume 0.4
    # 음악?

    "{i}잠시 후{/i}" id c04_t_1035
    
    show tiger nake0_d base red
    with dissolve

    "엘레드가 [pl_name][josa_eul_reul] 조심스레 내려놓자마자, [pl_name][josa_eun_neun] 비틀거리며 쓰러지려고 했다." id c04_t_1036

    with hpunch
    c nake0_d hurt "\"으윽...\"" id c04_t_1037
    
    show tiger nake0_u talk
    with dissolve

    t "\"괜찮나?!\"" id c04_t_1038
    
    show tiger nake0_u base
    with dissolve

    "엘레드는 당황해서 [pl_name][josa_eul_reul] 다시 붙잡았다." id c04_t_1039
    "다행히 [pl_name][josa_i_ga] 정액 웅덩이에 주저앉기 전에 잡을 수 있었다." id c04_t_1040
    
    c sleep "\"(너무 피곤하고 졸리다... 그냥 이대로 누워서 자고 싶은데.)\"" id c04_t_1041
    
    "[pl_name][josa_eun_neun] 자신의 방에 있는 푹신푹신한 침대가 절실해졌다." id c04_t_1042
    
    c sigh "\"집에 가야 하는데...\"" id c04_t_1043

    show tiger talk
    with dissolve

    t "\"그, 그렇지. 얼른 데려다 주겠네.\"" id c04_t_1044
    
    show tiger nake0_d base at surprise_move

    "엘레드는 허겁지겁 옷을 주워서 입히려다가, 정액으로 엉망진창이 된 [pl_name]의 하체를 보고 멈칫했다." id c04_t_1045
    
    show tiger sleep
    with dissolve

    "엘레드는 조금 망설이다가 결단을 내렸다." id c04_t_1046

    show tiger base
    with dissolve
    pause 0.5
    show tiger :
        yoffset 400
        zpos 120
    with Dissolve (1)

    play sound "effect/sticky2.mp3" volume 0.7
    show tiger nake0_d horny2
    with dissolve
        
    "[pl_name][josa_eun_neun] 간지러운 느낌에 반사적인 웃음을 흘렸다." id c04_t_1047
    "엘레드가 [pl_name]의 몸에 묻은 정액을 핥고 있었다. 까슬까슬한 혀가 왠지 기분 좋게 느껴졌다." id c04_t_1048
    "정작 엘레드는 최대한 빨리 마무리하기 위해 분주했다. 화끈한 정사 후의 여운을 느낄 틈은 없었다." id c04_t_1049
    
    show tiger base
    with dissolve
    pause 0.5
    show tiger :
        yoffset 0
        zpos 0
    with Dissolve (1)
    
    "엘레드는 입가를 스윽 훔쳐내고는 다시 옷 입히기에 집중했다." id c04_t_1050
    
    # 레스크 엘레드 옷 베이스로 복귀
    play sound "audio/effect/takeoff.mp3" volume 0.5
    show tiger am_d talk_am red
    with dissolve

    t "\"휴... 걸을 수 있겠나? 아니지, 가만히 있게.\"" id c04_t_1051
    
    show tiger am_u base_am
    with dissolve

    "엘레드는 [pl_name][josa_eul_reul] 번쩍 안아 들었다." id c04_t_1052
    "결혼식의 신랑처럼 들어 올려진 [pl_name][josa_eun_neun] 갑옷에 머리를 기댔다." id c04_t_1053
    "[pl_name][josa_eun_neun] 서늘한 금속의 감촉을 느끼며 잠이 들었다." id c04_t_1054

    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk(1500, 3.0, 6)
    pause 2.0
    
    # 가게 앞 (밤) 배경으로
    scene bg shop_outside2 with Fade(0.8, 0.8, 0.8)

    show tiger am_u talk_am red
    with dissolve

    t "\"... [pl_name]?\"" id c04_t_1055
    
    show tiger base_am
    with dissolve

    c am_d sigh "\"으음... 어?\"" id c04_t_1056
    
    "엘레드의 부름에 얕은 잠에서 깨어난 [pl_name][josa_eun_neun] 지끈거리는 두통에 이마를 짚었다." id c04_t_1057
    "[pl_name][josa_eun_neun] 몰랐지만, 엘레드는 가게 앞에서 몇 분 동안 [pl_name][josa_eul_reul] 깨우려고 노력했다." id c04_t_1058
    
    c hurt "\"집...\"" id c04_t_1059
    c talk "\"아, 감사합니다.\"" id c04_t_1060
    
    show tiger am_d
    with dissolve

    "엘레드는 천천히 [pl_name][josa_eul_reul] 내려주었다." id c04_t_1061
    "[pl_name][josa_eun_neun] 두통을 참아가며 열쇠로 문을 열었다." id c04_t_1062
    "문을 벌컥 열고 들어가는 [pl_name]의 뒤에서 엘레드가 말했다." id c04_t_1063
    
    show tiger am_u talk_am
    with dissolve

    t "\"걷기 힘들면 내가 다시 업어서-\"" id c04_t_1064
    
    show tiger base_am
    with dissolve

    c ddam2 "\"아, 아니. 괜찮습니다. 그게, 어, 두 번이나 폐를 끼칠 수는 없죠.\"" id c04_t_1065
    c talk "\"오늘은 정말 감사했습니다. 내일 다시 뵙죠.\"" id c04_t_1066
    
    "엘레드는 꾸벅 인사하는 [pl_name] 때문에 얼떨떨한 표정을 지었다. 문이 닫히는 것을 덩그러니 바라볼 수밖에 없었다." id c04_t_1067

    hide tiger
    show tiger am_d sad2_am
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (120, -200)

    "엘레드는 뭔가 이상하다는 느낌이 들었다. 한숨을 쉬고 가게에서 멀어져갔다." id c04_t_1068
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger sad3_am at walk(1500, 3.0, 6)
    pause 2.0

    # 레스크 방 (밤) 배경
    scene bg home3 with Fade(0.8, 0.8, 0.8)
    
    show cara am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 비틀거리면서도 간신히 자신의 방까지 도착했다." id c04_t_1069

    show cara inn_d sleep
    with dissolve
    pause 1.0
    show cara :
        ease 1.5 yoffset 200
    "바닥에 옷을 허물처럼 벗어놓고, 속옷 차림으로 침대에 눕자, 온몸이 버터처럼 녹아내리는 기분이었다." id c04_t_1070
    
    show cara sigh
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.20
    show sigh at sigh_move (-120, 100)

    c "\"하아아아...\"" id c04_t_1071
    
    "[pl_name][josa_eun_neun] 여러 가지 심정이 뒤섞인 한숨을 내뱉었다." id c04_t_1072

    show cara sleep
    with dissolve

    "오늘 하루 너무 많은 일을 겪어서 몸도 마음도 힘들었다. 어디 하나 안 아픈 곳이 없었다." id c04_t_1073
    
    c "\"(일단 자고 내일 생각하자.)\"" id c04_t_1074
    
    hide cara
    show cara inn_d hurt at surprise_move :
        yoffset 200

    c "\"(윽, 두통까지...)\"" id c04_t_1075
    
    show cara sleep
    with dissolve

    "머리가 또 지끈거려서 [pl_name][josa_eun_neun] 눈을 감고 천천히 호흡했다." id c04_t_1076
    "두통이 심해지는 것 보다, [pl_name][josa_i_ga] 잠에 드는 게 더 빨랐다." id c04_t_1077

    stop music fadeout 2.5

label c4t_end:
    # 레스크 방 낮배경
    scene bg home with Fade(0.8, 0.8, 0.8)
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    "{i}다음 날 아침{/i}" id c04_t_1078
    
    "아침의 밝은 햇빛이 [pl_name]의 방을 환하게 비추어도, [pl_name][josa_eun_neun] 일어날 생각이 없었다." id c04_t_1079
    
    show cara inn_d hurt
    with dissolve

    c "\"으으...\"" id c04_t_1080
    
    "물론 일어날 기력도 없었다." id c04_t_1081
    "처음 잠에서 깼을 때, 극심한 숙취에 머리가 수천 조각으로 쪼개지는 기분이었다." id c04_t_1082
    
    show cara sleep
    with dissolve

    "다시 한참을 자고 나니까 숙취는 그나마 덜 해졌다." id c04_t_1083
    
    c "\"(머리만 아프면 다행이지...)\"" id c04_t_1084
    
    "온몸이 근육통으로 뻐근했다. 팔다리는 그나마 괜찮은 듯하지만, 등과 허리가 찌릿찌릿했다." id c04_t_1085
    "그리고 가장 심한 곳은 \'구멍\'이었다. 활짝 열렸던 곳이 다시 닫히는 과정은 정말 이상한 느낌이었다." id c04_t_1086
    "[pl_name][josa_eun_neun] 또 한숨을 쉬었다." id c04_t_1087
    
    show cara sigh
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-120, -100)

    c "\"(내가 미쳤지 진짜...)\"" id c04_t_1088
    c "\"(오늘 걸어 다닐 수는 있을까? 회복 물약을 마시면 효과가 있으려나?)\"" id c04_t_1089
    
    show cara ddam
    with dissolve

    "[pl_name][josa_eun_neun] 엘레드와 뒷골목에서 화끈한 밤을 보냈던 게 자꾸 생각났다." id c04_t_1090
    "그 순간의 뜨거움이나 쾌락이 전부 후회되는 건 아니었다. 하지만 그 뒷감당을 하는 건 지금의 [pl_name]였다." id c04_t_1091

    c "\"(하... 차라리 꿈이었으면 좋았을 텐데. 앞으로 엘레드를 어떤 얼굴로 봐야 하지?)\"" id c04_t_1092

    show cara base at surprise_move

    "[pl_name][josa_eun_neun] 누운 채로 온갖 생각에 괴로워하다가 마침내 일어났다." id c04_t_1093
    "일단 씻고 가게 문을 열 생각이었다." id c04_t_1094

    # 1층배경
    scene bg shop with Fade(0.8, 0.8, 0.8)

    "다행히 회복 물약은 근육통에 효과가 있었다." id c04_t_1095
    "피곤함까지 없애주진 못했지만, [pl_name][josa_eun_neun] 청소와 상품 진열을 마치고 가게 문을 열었다." id c04_t_1096
    "늦잠을 잔 데다 혼자 준비해서 그런지 꽤 늦은 시간에 영업을 시작했다." id c04_t_1097
    "[pl_name][josa_eun_neun] 크게 하품하고 자리에 앉았다." id c04_t_1098
    
    c consider "\"(그동안 가헬에게 너무 많이 의존했나...)\"" id c04_t_1099

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c04_t_1100
    
    # 가헬 등장
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf am_d base :
        xoffset -1500
    show wolf at mirror, walk (0, 2.5, 5)

    "마침 가헬이 가게에 돌아왔다." id c04_t_1101
    
    hide wolf
    show wolf am_d pit
    with dissolve

    "미묘하게 털이 살짝 눌려있고, 땋은 머리가 평소랑 약간 달라 보였다." id c04_t_1102

    "척 봐도 잠을 제대로 못 잔 모양새였다. [pl_name][josa_eun_neun] 자신이 마시려던 물을 가헬에게 건넸다." id c04_t_1103
    
    c talk "\"괜찮아? 어제 완전히 기절한 줄 알았어.\"" id c04_t_1104
    
    "가헬은 욱신거리는 두통을 참으며 멀쩡한 척했다." id c04_t_1105
    
    show wolf am_u hurt2
    with dissolve

    w "\"이제 괜찮다.\"" id c04_t_1106

    show wolf sad2_am
    with dissolve

    w "\"... 걱정하게 해서 미안하다.\"" id c04_t_1107
    
    show wolf am_d sad_am
    with dissolve

    c consider "\"오늘은 더 쉬는 게 어때?\"" id c04_t_1108
    
    show wolf base :
        ease 0.2 yoffset -10 
        ease 0.2 yoffset 0 

    "[pl_name]의 말에 가헬은 고민하다가 고개를 끄덕였다. 오늘 회복해야 내일부터 제대로 일을 할 수 있을 것이다." id c04_t_1109
    "가헬은 [pl_name]의 얼굴을 보며 대답했다." id c04_t_1110
    
    show wolf am_u talk
    with dissolve

    w "\"너도 쉬어야 하지 않나? 피곤해 보인다.\"" id c04_t_1111
    
    show wolf am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 어제 엘레드와 있었던 일을 들킨 것 같아 괜히 뜨끔했다." id c04_t_1112
    
    c ddam2 "\"피곤하긴 한데... 으음, 손님이 없는 거 같으면 일찍 닫아야지.\"" id c04_t_1113
    
    show wolf am_u talk
    with dissolve

    w "\"그때는 나도 돕겠다.\"" id c04_t_1114
    
    show wolf am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 대답 대신 가헬의 등을 떠밀었다. 가헬은 터덜터덜 2층으로 올라갔다." id c04_t_1115
    
    # 가헬 걸어서 퇴장
    show wolf base at mirror
    with dissolve
    pause 0.5
    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 2.5, 5)
    pause 2.0

    c sigh "\"(휴... 손님이 별로 없어야 할 텐데.)\"" id c04_t_1116
    
    "..." id c04_t_1117
    
    "[pl_name]의 바람과 다르게, 쉴 틈 없이 바쁜 하루였다." id c04_t_1118
    
    "손님이 없어서 좀 쉬어볼까 싶으면 다음 손님이 찾아오기를 반복했다." id c04_t_1119
    
    c ddam2 "\"(손님 더 없지? 이제 그냥 문 닫아야지. 이러다 쓰러지겠네...)\"" id c04_t_1120
    
    "몸 상태는 그렇게 나쁘지 않았지만, 두뇌에 휴식이 필요했다. 빨리 영업을 끝내고 자고 싶었다." id c04_t_1121
    "[pl_name][josa_eun_neun] 가게 밖을 정리할 생각으로 자리에서 일어섰다." id c04_t_1122
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c04_t_1123
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger am_d base_am :
        xoffset -1500
    show tiger at walk (0, 2.5, 5)

    "거의 동시에 엘레드가 가게 문을 열고 들어왔다." id c04_t_1124
    "[pl_name][josa_eun_neun] 엘레드와 눈을 마주치고 반사적으로 움찔했다. 엘레드도 평소와 달리 쭈뼛거렸다." id c04_t_1125
    
    show tiger at surprise_move

    c talk "\"어, 어서 오세요, 엘레드 님.\"" id c04_t_1126
    
    "[pl_name][josa_eun_neun] 시선을 피하며 인사했다. 도저히 얼굴을 마주하기가 힘들었다." id c04_t_1127

    show tiger am_u talk_am
    with dissolve
    
    t "\"크흠, 너무 늦게 찾아와서 미안하네. 몸 상태는 좀 괜찮은가?...\"" id c04_t_1128
    
    show tiger am_d base_am
    with dissolve
        
    c ddam2 "\"아, 하하, 뭐, 괜찮습니다.\"" id c04_t_1129
    
    "[pl_name][josa_eun_neun] 뭐라고 말해야 할지 고민했다. 아무리 생각해도 이상한 변명이나 떠올랐다." id c04_t_1130
    
    c consider "\"(어제는 실수였다... 는 말이 안 되잖아. 그렇게 격렬하게 해놓고 실수가 말이 돼?\"" id c04_t_1131
    c sigh "\"기억이 안 난다고 거짓말할 수도 없고. 으으, 어색해...)\"" id c04_t_1132
    
    "고민에 빠진 [pl_name]의 표정이 좋지 않아서, 엘레드는 다시 물었다." id c04_t_1133
    
    show tiger am_u talk_am
    with dissolve

    t "\"그대, 정말로 괜찮은 건가?\"" id c04_t_1134
    
    show tiger am_d base_am
    with dissolve
    
    c talk "\"좀 피곤하긴 합니다만... 오늘 푹 쉬면 나아질 겁니다.\"" id c04_t_1135
    
    "엘레드는 [pl_name]의 태도에서 느껴지던 것이 무엇인지 깨달았다." id c04_t_1136
    
    show tiger sad3_am
    with dissolve
    
    "[pl_name]의 거리감이 전혀 줄어들지 않았다. 가까워지기는커녕 오히려 더욱 멀어진 것 같았다." id c04_t_1137
    "엘레드는 한숨 쉬듯 말했다." id c04_t_1138
    
    show tiger am_u sad2_am
    with dissolve

    t "\"그, 자네...가 괜찮다니 다행이군. 어제는 미안했네...\"" id c04_t_1139
    
    show tiger am_d sad3_am
    with dissolve

    c ddam2 "\"어제는!... 그, 서로 즐긴 거니까요. 사과하실 필요 없습니다.\"" id c04_t_1140

    "[pl_name][josa_eun_neun] 누가 듣고 있지 않나 조심하며 대답했다." id c04_t_1141

    "엘레드는 [pl_name]의 대답을 듣고 어제 했던 행동이 전부 후회되기 시작했다." id c04_t_1142
    "감정이 더 격해지기 전에 엘레드는 도망가고 싶었다." id c04_t_1143
    
    show tiger am_u sad2_am
    with dissolve

    t "\"그래... 얼굴도 봤으니, 오늘은 이만 가보겠네.\"" id c04_t_1144
    
    show tiger am_d sad3_am at mirror
    with dissolve
    pause 0.5
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk (-1500, 3.0, 6)

    c talk "\"아, 네. 안녕히 가십시오.\"" id c04_t_1145
    
    "[pl_name][josa_eun_neun] 힘없이 걸어가는 엘레드의 뒷모습에 인사했다." id c04_t_1146
    
    c question2 "\"(뭔가 이상한데? \'다음에 또 하자\'던가 그런 말도 안 하고...)\"" id c04_t_1147
    
    "[pl_name][josa_eun_neun] 다음에 엘레드를 보면 또 어떻게 대해야 할지 고민했다." id c04_t_1148
    
    c sigh "생각하자마자 또 머리가 아프네..." id c04_t_1149

    "[pl_name][josa_eun_neun] 생각을 그만두고 가게를 정리했다." id c04_t_1150

    "오늘은 평소보다 훨씬 일찍 잠에 들기로 했다." id c04_t_1151
    
    # 가게 밖 배경
    scene bg shop_outside with Fade(0.8, 0.8, 0.8)
    play music "audio/sad-soul-chasing-a-feeling-185750.mp3" fadein 2.5 volume 0.60

    show tiger am_d sad3_am
    with dissolve

    "엘레드는 속이 울렁거렸다. 자기 자신이 혐오스러워서 [pl_name] 앞에 있을 수가 없었다." id c04_t_1152
    
    t "\"(가볍게 즐기는 사이? 이딴 게 내 진심인가?)\"" id c04_t_1153
    
    "욕망이 앞서서 [pl_name]에게 하지 말기로 마음먹었던 짓을 해버렸다." id c04_t_1154
    "애초에 이런 식으로 육체적 관계를 시작하지 말아야 했다. 엎지른 물은 마법으로 주워 담을 수 있지만, 자신이 저지른 짓은 되돌릴 수 없었다." id c04_t_1155

    show tiger sad2_am
    with dissolve
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (120, -200)

    "이렇게 후회하는 것도 아무런 쓸모가 없었다." id c04_t_1156

    show tiger sad_am
    with dissolve

    "엘레드는 한숨을 쉬다가 눈에 눈물이 맺힌 것을 느꼈다." id c04_t_1157
    
    t "\"...\"" id c04_t_1158
    
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger at walk (1500, 3.0, 6)
    pause 2.0
    stop music fadeout 2.5

    "엘레드는 도망가듯 가게 앞을 떠나갔다." id c04_t_1159

    

    # 이러고 꿈 보여주고 끝내기
   
    jump chapter4_dream