#게임 스타트#########################################################################
label game_start:
    
    $ cleanup_memory()
    scene bg shop
    show chapter_back
    with Fade(0.8, 0.8, 0.8)
    
    pause 0.2
    play channel1 "effect/fresh_snap.mp3" volume 0.7
    pause 0.1
    show chap
    pause 0.5
    show ter
    pause 1.0
    play channel2 "effect/finger_snap.mp3" volume 0.8
    pause 0.1
    show one
    pause 1.0

    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    hide chapter_back
    hide chap
    hide ter
    hide one
    with Dissolve (1.5)
    
    show screen book_icon with dissolve
    
    #정보 키워드
    $ display_text = _("정보 : 마법 상점")
    show screen affection_indicator
    
    c base "이곳은 나의 {color=#ee3939}'마법 상점'{/color}, 선반에 올려진 형형색색의 물약들이 창문을 통해 들어온 햇살에 반짝인다." id c01_0000
    
    c smile "그 햇살이 부드럽게 얼굴에 닿자 기분이 좋아져 미소를 지었다." id c01_0001

    c base "이 가게는 도시의 뒷골목에 위치해 있지만, 절묘하게 햇볕이 잘 들어오는 입지 때문에 망설이지 않고 바로 계약을 했었다." id c01_0002
    
    c "그래도 뒷골목은 뒷골목인지 영업 초기에는 손님들이 잘 찾아오지 않아 힘들었다." id c01_0003

    c "결국 나는 조금 더 수상한 (혹은 위험한) 물건도 취급하게 되었다." id c01_0004
    
    c "덕분에 수입은 확실히 넉넉해 졌고, 이대로만 벌어들인다면 성 안쪽에 가게를 차릴 수 있을지도 모른다는 허황된 상상까지 했다." id c01_0005

    c "물론 뒷골목의 편안한 내 가게를 떠날 생각은 없다. 나는 먼지떨이로 선반을 구석구석 털면서 쓸데없는 상상이나 저녁식사 같은 생각에 잠겨 들었다." id c01_0006

    play sound "audio/effect/crash2.mp3" volume 0.4
    with hpunch

    "{i}덜컹-!{/i}" id c01_0007
    
    #가헬 해금
    $ unlock_character("wolf")
    $ display_text = _("캐릭터 : 가헬")
    show screen affection_indicator

    show wolf
    with dissolve

    c "뭔가 부딪히는 소리에 깜짝 놀라 고개를 돌렸다." id c01_0008

    "푸른 빛이 느껴질 정도로 짙은 검은색의 털의 끝에는 일부 붉은색이 보인다. 윤기가 느껴지는 흰색 털이 조화를 이루는 이 늑대 수인은 가헬, 나이에 비해 엄청난 경력을 지닌 용병이다." id c01_0009

    "그걸 증명하듯 근육질로 탄탄한 몸에는 베인 상처가 가득했다." id c01_0010

    c "나는 가헬을 보디가드 겸 전속용병으로 장기 계약을 맺고, 계약금과 별개로 그의 숙식도 제공하고 있었다." id c01_0011

    c "가헬은 아무 말없이 그 깊고 푸른 눈으로 나를 불만스럽게 바라보고 있었다. 아무래도 그가 계단을 내려오다가 아래에 놓인 상자를 걷어찰 뻔해서 그런 것 같았다." id c01_0012

    c talk "\"좋은 아침...?\"" id c01_0013

    w "\"...\"" id c01_0014

    show wolf at down
    with ease

    "가헬은 대답 없이 자신의 발 밑에 놓인 상자를 옮기려고 허리를 숙였다." id c01_0015

    c "\"잠깐! 그거 아직 마법처리 안했어! 그냥 내버려 둬.\"" id c01_0016

    show wolf at normal
    with ease

    show wolf am_u talk
    with dissolve

    w "\"[pl_name], 이거 벌써 일주일은 여기 그대로 있었는데.\"" id c01_0017

    show wolf base
    with dissolve

    c base "그는 중저음의 허스키한 목소리로 나를 질책했다. 이상하게 잔소리를 듣는 기분이었다." id c01_0018

    c ddam2 "\"아... 다른 중요한 물건을 먼저 처리하느라, 하하...\"" id c01_0019

    c base "나는 먼지떨이를 내려놓고 괜히 물약을 이리저리 옮기며 가헬의 시선을 피했다." id c01_0020

    "가헬은 딱딱하게 굳은 얼굴을 억지로 피면서 말했다." id c01_0021

    show wolf am_d talk at normal
    with dissolve
    w "\"적어도 발에 채이지 않게 놔두지 그래?\"" id c01_0022

    show wolf base
    with dissolve
    c talk "\"알겠어, 나중에 옆으로 옮겨놓을게.\"" id c01_0023

    show wolf am_u angry
    with dissolve

    w "\"나중에?\"" id c01_0024

    c base "가헬은 내 말을 추궁하며 눈빛만으로 나를 꿰뚫으려는 듯 날카롭게 바라본다." id c01_0025

    c ddam2 "전장에서 죽을 고비를 수없이 넘긴 용병의 카리스마... 를 왜 느끼고 있는지 모르겠다." id c01_0026

    c ddam "이 상점의 주인은 나고 용병을 고용한 것도 난데... 무언가 역전된 느낌이었다." id c01_0027

    show wolf am_d base
    with dissolve

    c base "하는 수 없이, 나는 바닥에 쭈그려 앉아 낑낑대며 무거운 상자를 질질 끌어당겼다." id c01_0028

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at fwalk
    pause 0.5
    
    "그 꼴을 보다못한 가헬은 대신 옮겨주려는 셈인지 가까이 다가와 상자를 붙잡는다." id c01_0029

    menu:
        "내가 직접 옮긴다고 한다.":

            c talk "\"아냐, 됐어. 저번에 도와준 것도 그렇고, 가게에서 잡일꾼으로 쓰려고 고용한 것도 아닌데.\"" id c01_0031

            "가헬이 붙잡은 상자를 내가 끌어당기자, 그 두터운 팔근육이 무색하게 상자가 스르륵 빠져나온다." id c01_0032

            c talk "\"나도, 흡! 근육! 있어! 끄응...\"" id c01_0033

            c base "힘차게 기합을 넣고 상자를 들어올리니 눈앞이 거의 가려져 가헬의 귀만 보였다." id c01_0034

            show wolf am_d sad_am
            with dissolve
            
            c "검은색 귀는 왠지 아래로 처진 것 같았다." id c01_0035

            w "\"조심해.\"" id c01_0036

            "창고로 뒤뚱뒤뚱 걸어가는 내 뒷모습에 대고 가헬이 작게 말했다." id c01_0037


        "그가 옮겨주는 걸 지켜본다.":

            $ wolf_love += 1
            $ display_text = _("가헬 호감도 변화") 
            show screen affection_indicator

            show wolf at larger_down
            with ease
            show wolf at larger_normal
            with ease

            "가헬은 기합이라 하기도 힘든 작은 숨소리와 함께 상자를 번쩍 들어올렸다. 두터운 팔근육은 무거운 상자를 장난감처럼 가볍게 들고 있었다." id c01_0039

            w "\"이런 소소한 일은 나한테 맡겨, [pl_name].\"" id c01_0040

            c talk "\"그... 그래.\"" id c01_0041

            c base "무시무시한 힘의 차이에 할말을 잃은 나는 그냥 고개를 끄덕였다." id c01_0042

            show wolf talk
            with dissolve

            w "\"어디로 옮기면 될까?\"" id c01_0043

            c talk "\"어? 아, 여기 책상 위에.\"" id c01_0044

            play sound "effect/footstep.mp3" volume 0.85
            show wolf base at bwalk
            with Dissolve (0.2)

            c base "내가 후다닥 마법서적 몇 권을 치운 자리에 가헬은 상자를 내려놓았다." id c01_0045

            show wolf am_u wink
            with dissolve

            w "\"너라면 얼마든지 들어줄테니까, 필요하면 뭐든 부탁해.\"" id c01_0046
            
            show wolf am_d smile
            with dissolve

            c "가헬은 저번에도 무거운 연금솥을 설치하는데 도와줬다. 아까까지만 해도 칼바람처럼 매서운 눈빛으로 나를 바라보던 그는 자상한 눈빛으로 나를 보고 웃었다." id c01_0047

            c "나는 어색하게 웃으며 감사의 말을 전했다." id c01_0048

            c talk "\"... 항상 도와줘서 고마워.\"" id c01_0049

    hide wolf
    with dissolve

    c base "가헬과 함께 보낸 시간은 이제 겨우 한달에 불과했다. 그러나 그는 항상 내 옆에서 지내며, 나에게 도울 일은 없는지 끊임없이 물었다." id c01_0050

    c "그의 주요 임무는 호위로서 나를 지키는 것이지만, 그 이상의 일도 기꺼이 하려고 했다." id c01_0051

    c "물론 도와주는건 참 고마운 일이지만, 때로는 그게 조금 부담스럽게 느껴지고는 했다." id c01_0052

    c consider "(혹시 마음이 바뀌었다고 추가금을 요구하진 않겠지? 이번 달에는 다른 재료도 사야하고 던전 탐험 준비도 해야하고 아티팩트까지, 여윳돈이 많지 않은데...)" id c01_0053

    show wolf
    with dissolve
    show wolf talk
    with dissolve

    w "\"회복 물약 재고는 충분한가?\"" id c01_0054

    show wolf base
    with dissolve

    c talk "\"아... 충분하진 않지만 이번 주는 괜찮을 거야.\"" id c01_0055
    
    
    $ unlock_info_tag(0, "2")
    $ display_text = _("정보 : 회복 물약")
    show screen affection_indicator

    c base "{color=#ee3939}'회복 물약'{/color}은 손님들이 가장 많이, 자주 찾는 물건이라 가헬도 신경쓰는 것 같다." id c01_0056

    c "마탑에서 공증 받은 물건을 마탑보다 (조금 더) 싸게 판다고 하면, 용병들은 내 가게에 올 수 밖에 없다." id c01_0057

    c "나는 마탑 출신이 아니다. 인맥을 등에 업고 공증 문서를 뜯어낸 것에 가깝다." id c01_0058

    show wolf am_u talk
    with dissolve

    w "\"그럼 한 궤짝만 진열해놓도록 하지.\"" id c01_0059

    hide wolf
    with dissolve

    c talk "\"고마워. 한 궤짝 더 만들어 둬야겠네.\"" id c01_0060

    c base "아무튼 물약을 만들기 위해 재료가 필요하고, 그 재료는 던전에서 채집한다." id c01_0061

    c "흔한 연금술 재료는 도시에서 사면 되지만, 마법적 재료는 마법에 대한 이해가 있어야 제대로 다룰 수 있다. 결국 나는 맘에 드는 약초를 캐러 내가 직접 던전에 가고 있다." id c01_0062

    c "다행히 회복 물약의 주 재료인 마나 허브는 아무 던전에 가도 쉽게 찾을 수 있다. 하지만 던전에서 마물과 싸우는건 다른 문제다." id c01_0063

    c "혼자서 던전에 갔다가 목숨을 잃을 뻔 한 뒤로, 나는 호위 용병을 고용해서 던전에 가게 됐다. 그렇게 나는 한달 전 용병 길드에서 가헬을 만났다." id c01_0064

    show wolf am_u talk
    with dissolve

    w "\"진열은 끝났다.\"" id c01_0065

    show wolf am_d base
    with dissolve

    c talk "\"어? 아, 고마워.\"" id c01_0066
    
    c talk "\"앗! 청소는 내가 해도 되는데...\"" id c01_0067

    show wolf at mirror
    with dissolve
    pause 0.5
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (500, 1.6, 3)

    c base "내가 들고 있던 먼지떨이까지 뺏어들고 먼지를 학살하고 있는 가헬의 모습을 보며, 나는 우리가 처음 만났던 순간을 회상했다." id c01_0068



label guild_past:

    scene bg guild_past with Fade(0.8, 0.8, 0.8)
    #play music "audio/spirit-of-adventure-130563.mp3" 

    #정보 키워드 추가
    $ unlock_info_tag(0, "3")
    $ display_text = _("정보 : 용병 길드")
    show screen affection_indicator
    
    "{color=#ee3939}'용병 길드'{/color}는 언제나 위험한 의뢰와 그보다 더 위험한 용병들로 가득 차있다." id c01_0069

    "명예와 충성심으로 움직이는 기사단과 달리 오직 힘과 돈으로 움직이는 용병들 사이에서 다툼이나 소란은 없는게 이상할 정도다." id c01_0070

    "특히나 육식계 수인이 많이 모이게 되는 용병 길드 건물은 조용할 날이 없다. 그런데 오늘은 달랐다." id c01_0071

    "[pl_name][josa_i_ga] 길드 문을 열자 이상할 정도로 한적한 실내에는 척 보기에도 등급 낮아보이는 용병들이나 몇 명 앉아있었다." id c01_0072

    c question2 "(무슨 일이 있었나? 왜 용병들이 코빼기도 안 보이지?)" id c01_0073

    c base "나는 궁금증에 휩싸였지만, 의문을 해결하는 것 보다 일단 의뢰를 접수하는 것이 우선이었다. 데스크 앞에 서자, 접수원 루카스가 친절한 미소와 함께 나를 바라보았다." id c01_0074

    show lucas talk am_u
    with dissolve

    $ unlock_character("lucas")
    $ display_text = _("캐릭터 : 루카스")
    show screen affection_indicator

    l "\"안녕하십니까 [pl_name]님.\"" id c01_0075

    show lucas base am_d
    with dissolve

    "그는 내가 여기 온 목적을 이미 알고 있는 것처럼 말했다." id c01_0076

    show lucas talk am_u
    with dissolve

    l "\"던전에 동행할 용병을 다시 찾으러 오셨나요?\"" id c01_0077

    show lucas base page_d
    with dissolve

    "나의 루틴을 잘 알고 있었던 듯이 그는 내 대답을 듣기도 전에 서류를 넘기며 적절한 용병을 찾기 시작했다." id c01_0078

    c talk "\"맞습니다, 루카스. 이번에도 같은 의뢰에요.\"" id c01_0079

    show lucas talk page_u
    with dissolve

    l "\"흐음... 지금 당장은 까다로운 조건을 제시한 용병 한 명만 가능합니다.\"" id c01_0080

    l "\"공고를 통해 용병을 모집해도 괜찮습니다만, 최근에는 마물 토벌 임무 때문에 평소보다 보수를 더 얹어주지 않으면 용병들이 거들떠보지도 않을 거에요.\"" id c01_0081

    show lucas base
    with dissolve

    c question2 "\"마물 토벌 임무라고요?\"" id c01_0082

    show lucas talk
    with dissolve

    l "\"그렇습니다. 성도 근처에서 마물의 활동이 늘어나고 있어, 백작님께서 기사단을 동원하셨죠.\"" id c01_0083

    l "\"하지만 마물의 수가 예상보다 많았는지, 최근에 대대적으로 용병들을 고용하더군요.\"" id c01_0084

    show lucas base page_d
    with dissolve

    c base "백작이 직접 나설 정도면 보통일은 아닐 것이다." id c01_0085
    
    show lucas base page_u
    with dissolve

    "루카스는 몇몇 가능성 있는 용병들의 문서를 살펴보다가 퇴짜놓기를 반복하면서 말했다." id c01_0086
    
    show lucas talk
    with dissolve

    l "\"{color=#ee3939}\'마물 콜로니\'{/color}가 생겼다고 하더군요.\"" id c01_0087
    
    show lucas base page_d
    with dissolve

    c "그의 설명을 듣자 길드가 이렇게까지 한적한 것을 이해할 수 있었다." id c01_0088

    c talk "\"직접 고용되지 않은 용병까지 다들 그 쪽 임무로 간 것이군요.\"" id c01_0089

    c base "실력이 부족하거나 목숨이 아까운게 아니라면 용병들이 눈에 불을 켜고 갈 만한 보수를 내걸었을 것이다." id c01_0090

    c consider "\"토벌 임무 보수가 상당히 좋나 봐요?\"" id c01_0091

    show lucas talk page_u
    with dissolve

    l "\"네, 기본적인 보수 외에도 마물로부터 얻은 소재의 권한까지 차지하게 됩니다.\"" id c01_0092
    
    show lucas base page_d
    with dissolve

    c base "백작이 건 계약금에 마물 소재까지 붙은 의뢰와 그냥 평범한 던전 공략의 호위, 비교할 것도 없었다." id c01_0093

    c talk "\"하... 공고를 붙여봤자 아무도 안 볼 것 같군요.\"" id c01_0094

    c base "갑작스런 상황에 짜증이 났지만, 결국 선택지는 처음부터 하나밖에 없었다." id c01_0095

    show lucas talk page_u
    with dissolve

    l "\"알겠습니다. 저쪽 빈 테이블에서 잠시만 기다려 주십시오.\"" id c01_0096

    hide lucas
    with dissolve

    "루카스는 2층으로 올라갔다가 곧바로 한 명의 용병을 데려왔다." id c01_0097

    show lucas at left, mirror
    with dissolve

    pause(0.3)

    show wolf out_d base at right
    with dissolve

    show lucas talk
    with dissolve

    l "\"조건을 협의한 뒤 계약이 성사되면 저에게 계약서를 보여주십시오.\"" id c01_0098

    show lucas base 
    with dissolve

    "루카스는 간결하게 안내한 후, 자신의 자리로 돌아갔다." id c01_0099

    hide lucas
    with dissolve
    pause(0.3)
    show wolf at normal
    with dissolve

    c talk "\"안녕하세요. [pl_name][josa_ra_ira]고 합니다.\"" id c01_0100

    c base "나는 그 용병을 바라보며 인사했다." id c01_0101

    c "내 앞에는 날카롭게 빛나는 눈동자를 가진 늑대 수인이 서 있었다." id c01_0102

    c "가죽 벨트와 어깨 갑옷 정도만 걸친 차림새는 노출도가 높아 자칫 경박해보일 수도 있지만, 그의 검고 하얀 털과 단련된 근육까지 모든 신체가 한 벌의 갑옷같은 형상을 이루었다." id c01_0103

    c "한쪽 어깨에 붉은 망토를 걸친 채로, 허리와 등 부분에 각각 한 자루 씩 장검을 착용한 모습이 아무래도 빠르고 유연한 검술을 사용하는 것 같았다." id c01_0104

    c "그의 깊은 푸른 눈과 그의 피부에 새겨진 수많은 흉터들은 그가 겪어온 수많은 전투와 경험을 드러내고 있었다." id c01_0105

    w "\"......\"" id c01_0106

    c question2 "(... 뭐지?)" id c01_0107
    
    show wolf at change(1.22, 0, 135)
    with dissolve
    pause 0.5
    show wolf bigeye at change(1.22, 0, 135)
    with dissolve
    pause(0.5)

    "그의 검푸른 동공이 확장된다. [pl_name][josa_eul_reul] 깊게 바라보는 듯하다." id c01_0108

    pause(0.5)
    show wolf base out_d at normal
    with dissolve   

    c consider "나는 답변없이 길어지는 침묵 속에서 이유모를 압박감에 조금씩 불편해지기 시작했다. 어색함을 참을 수 없어져 먼저 말을 꺼냈다." id c01_0109

    c talk "\"저...\"" id c01_0110

    show wolf out_u talk
    with dissolve

    w "\"아...! 미안하군. 나는 가헬이라고 한다.\"" id c01_0111

    show wolf out_d base
    with dissolve

    "뒤늦게 정신을 차린 가헬은 황급히 자기 소개를 했다." id c01_0112

    c "\"루카스 씨 말을 들어보니 계약에 조건이 있다고 하시던데.\"" id c01_0113

    show wolf talk
    with dissolve

    w "\"그렇다.\"" id c01_0114

    show wolf base
    with dissolve

    c base "가헬은 나에게 1년 동안의 장기 계약을 제안했다." id c01_0115

    c "일회성이 아닌 장기계약은 처음이라 듣자마자 고민이 깊어졌다. 하지만 지금 하고 있는 {color=#ee3939}\'사업\'{/color}을 위협하는 사건들이 종종 있었고, 던전 밖에서도 내 목숨을 지킬 수 있는 수단이 필요했다." id c01_0116

    c "그리고 가헬은 흔해빠진 용병과는 달랐다." id c01_0117

    c "다른 것보다 가헬의 망토에 달린 브로치를 알아보고 그를 믿을 수 있는 용병이라고 판단했다." id c01_0118

    $ unlock_info_tag(0, "4")
    $ display_text = _("정보 : 칼루리엔 용병단")
    show screen affection_indicator
    
    c "그 브로치에 새겨진 문양은 {color=#ee3939}\'칼루리엔\'{/color}이라는 유명한 용병단의 것으로, 그가 실력이 확실한 용병이라는 것을 증명해주는 물건이기도 했다." id c01_0119

    c consider "(위조품도 아닌 것 같고...)" id c01_0120

    c base "그 정도 실력자를 경호원으로 고용한다면 내 {color=#ee3939}\'사업\'{/color}도 별다른 문제 없이 안정적으로 진행될 것이다." id c01_0121

    c "하지만 그런 뛰어난 실력의 용병을 고용하려면 상당한 비용이 필요할 터. 그래서 나는 가격 문제로 두번째 고민을 시작했다." id c01_0122

    c talk "\"1년 계약이라... 뭐, 좋아요. 하지만 저도 조건이 있습니다.\"" id c01_0123
    
    c "\"숙식은 제공해드릴 테니 던전 밖에서도 호위를 부탁드려도 될까요?\"" id c01_0124

    "그가 곧장 대답했다." id c01_0125

    show wolf out_u talk
    with dissolve

    w "\"문제없다.\"" id c01_0126

    show wolf base
    with dissolve

    c base "나는 조금 더 자세히 상황을 설명하며 말을 계속했다." id c01_0127

    c talk "\"그리고 당장 계약금을 지불할 정도의 금화는 없습니다.\"" id c01_0128
    
    c "\"착수금을 제외한 나머지는 아티팩트로 지불하려는데, 한 달 뒤에 아티팩트가 완성되면 그 때 정식으로 계약서를 작성하는 게 어떨까요?\"" id c01_0129

    "그러나 그는 미소를 지으며 대답했다." id c01_0130

    show wolf out_d smile
    with dissolve

    w "\"그건 나중에 확인해도 좋다. 지금 바로 계약하지.\"" id c01_0131

    show wolf base
    with dissolve

    c base "내가 놀라 반문했다." id c01_0132

    c question2 "\"진심인가요?\"" id c01_0133

    show wolf out_u talk
    with dissolve

    w "\"마법 상점의 주인인 것은 알고 있다.\"" id c01_0134

    w "\"마법사이자 상인으로서 말의 무게를 지킬 수인이겠지?\"" id c01_0135

    show wolf out_d base
    with dissolve

    c base "계약 조건이 너무 유리해진 것 같아 의심스러운 마음도 들었지만, 결국 위험이 있더라도 충분히 감당할 수 있다고 판단해 그의 제안을 받아들였다." id c01_0136

    c talk "\"...알겠습니다. 그럼 계약하도록 하죠.\"" id c01_0137


label magic_shop:

    scene bg shop with Fade(0.8, 0.8, 0.8)
    #play music "audio/spirit-of-adventure-130563.mp3"

    c base "이렇게 나와 가헬은 계약을 맺고 이 가게에서 같이 지내게 된 것이다." id c01_0138

    c "첫 인상과 다르게 가헬은 (말투가 여전히 차가운 것만 빼면) 의외로 살갑게 굴었고, 나도 적당히 말을 놓으면서 겉보기엔 마치 친구같은 관계가 되었다." id c01_0139

    c "심지어 가게 일 까지 적극적으로 도와주니, 편하면서도 불편한 기묘한 관계로 지내고 있다." id c01_0140

    c "가게의 아침 청소와 상품 진열을 마치고, 나는 카운터에서 손님을 맞을 준비를 한다." id c01_0141

    c "그리고 오픈 시간인 오전 9시쯤이 되면 항상 첫번째로 오는 인물이 있다." id c01_0142

    c "단골손님... 이라고 하기엔 조금, 아니 큰 문제가 있다는게 단점이지만." id c01_0143

    c "(흠... 이제 올 때 쯤 됐는데?)" id c01_0144

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c01_0145

    c "누가 ‘호랑이도 제 말을 하면 온다’고 했던가. 바로 그 호랑이가 지금 문을 열고 들어온게 보인다." id c01_0146

    show tiger
    with dissolve
    
    $ unlock_info_tag(0, "5")
    $ unlock_character("tiger")
    $ display_text = _("캐릭터 : 엘레드")
    $ display_text2 = _("정보 : 반슈타인 기사단")
    show screen affection_indicator
    show screen affection_indicator2
    
    c "문이 꽉 낄 정도로 거대한 덩치를 가진 이 호랑이 수인의 이름은 엘레드. 백작 휘하 {color=#ee3939}\'반슈타인\'{/color}  기사단 소속의 기사단장이다." id c01_0147

    show tiger talk_am
    with dissolve


    t "\"하하하, 안녕하신가!\"" id c01_0148

    show tiger base_am
    with dissolve

    "시원시원한 웃음과 함께 가게에 들어온 엘레드는 곧바로 [pl_name][josa_eul_reul] 발견하고 능글거리는 눈웃음을 짓는다." id c01_0149

    "엘레드가 한 걸음 씩 움직일 때마다 두꺼운 금속 부츠 특유의 절그럭 거리는 소리가 조금씩 들린다." id c01_0150

    c "그의 옷차림은 뭐랄까... 갑옷을 입었지만 입지 않은 상태라고 표현해야 할 정도로 기묘하다." id c01_0151

    c "나체와 다름없는 행색으로 거리를 활보하는 용병들은 발에 채이도록 많지만, 기사단이 이렇게 입고 다니는 것은 역시 느낌이 다르다." id c01_0152

    c "우선 시선이 가는 부분은 바로 그의 복부다." id c01_0153

    c "그의 크고 단단한 식스팩과 빈틈없는 옆구리가 맨살 그대로 보인다." id c01_0154
    
    c "그리고 시선을 조금만 내리면, 사타구니를 가리는 보호대와 허리천을 빼고 나머지 부분은 훤히 드러나 있다." id c01_0155

    c "나는 그의 뒷모습을 처음 본 날, 내가 무슨 저주에 걸려서 헛것을 보고 있는건 아닌지 의심했다." id c01_0156

    c "기사단에게 이런 갑옷을 만든 대장장이가 문제인지, 이런 꼬라지로 당당하게 걸어다니는 엘레드가 문제인지는 당분간 알 수 없을 것이다." id c01_0157

    c consider "용병의 갑옷 마냥 치명적인 급소만 방어하면 다른 건 아무래도 상관없다는 건가? 그러면 굳이 판금 갑옷을 입을 이유가..." id c01_0158

    c "그 찰나의 순간에 엘레드는 아래로 향하는 내 시선을 눈치 챘는지, 그의 초록색 눈동자를 위험하게 빛내며 말을 이었다." id c01_0159

    show tiger am_u talk_am
    with dissolve

    t "\"음, 드디어 여기에 관심이 가는가? 확실히 내 몸매가 좀 매력적이긴 하지!\"" id c01_0160

    show tiger am_d base_am
    with dissolve

    c base "저 뻔뻔한 수준의 당당함에 나는 할말을 잃었다." id c01_0161

    c shy "뭐, 매력적인건 부정할 수 없긴 하다. 진한 주황빛 털과 검은 줄무늬는 윤기가 흐르고 뒤에서 보이는 엉덩이 근육은 꽉 쥐면 터질것 처럼 단단..." id c01_0162

    c base "나는 망상을 접고 얼른 인사를 했다." id c01_0163

    c talk "\"안녕하십니까, 엘레드님. 오늘도 저희 가게의 첫 고객이시네요. 어떤 일로 오셨습니까?\"" id c01_0164

    c base "생각은 생각으로 묻어두고 나는 나름의 예법을 차려 정중하게 인사했다." id c01_0165

    c "엘레드는 사소한 것은 신경쓰지 않는 호탕한 성격이지만, 그의 혈통은 대대로 기사단장을 배출하는 명문 귀족가라서 격식을 차릴 필요가 있다." id c01_0166

    show tiger am_u wink_am
    with dissolve

    t "\"당연히 오늘도 자네의 멋진 모습을 내 눈에 담기 위해서 왔지! 어떤가, [pl_name]? 아직도 자네의 생각엔 변함이 없나?\"" id c01_0167

    show tiger shy_am
    with dissolve

    t "\"나 정도면 지위로 보나 외모로 보나 연인이 될 상대로써 충분하다고 보네만!\"" id c01_0168
    
    t "\"자네가 허락한다면 바로 오늘부터 성도의 명소를 둘러보며 서로의 미래를... (어쩌구 저쩌구)\"" id c01_0169

    show tiger am_d base_am
    with dissolve

    c "엘레드를 단골손님이라고 하기에 가장 큰 문제가 되는 부분이 이것이다." id c01_0170
    
    c "그에게 내 마법상점은 물건을 사러 오는 곳이 아니고 나에게 플러팅을 날리기 위해 오는 곳이다." id c01_0171

    c "나는 몇번이고 거절했지만 모두 소용이 없었다." id c01_0172

    c "그가 여기를 찾아온지 3개월이 지난 지금 그의 꾸준한 열정에 반할만도 했지만 그럴 수 없는 이유가 있다." id c01_0173

    c "엘레드는 성도에서 가장 유명한 바람둥이에 장소도 상황도 가리지 않는 호색한이라고 한다." id c01_0174

    c "저런 플러팅은 그에겐 숨쉬듯이 자연스러운 것이며, 저 행동이 나에게만 하는 것이라고 착각하면 어떤 꼴이 될지 자연스럽게 상상할 수 있다." id c01_0175

    c "엘레드와 연인이 되면 화끈하다못해 타들어가는 치정극을 찍어야 할 것이다." id c01_0176

    play sound "effect/footstep.mp3" volume 0.85
    show tiger at walk (-500, 1.6, 3)
    pause 0.5
    

    show wolf talk at right
    with dissolve

    w "\"엘레드님. 뭔가 구매를 하실 게 아니라면, 장사에 방해되니 이만 나가 주셨으면 합니다.\"" id c01_0177

    show wolf base 
    with dissolve

    c "내가 가식적인 미소를 유지한 채 거절하는 꼴을 보다 못한 가헬이 말을 꺼냈다." id c01_0178

    c "가헬은 아주 평온한 표정으로 사실상 쫓아내는 것과 다름 없는 말을 아무렇지 않게 했다." id c01_0179

    c "그냥 적당히 민폐 손님을 대하는 것과 다름이 없지만, 나는 가헬이 굉장히 짜증을 내고 있다는 걸 바로 느꼈다." id c01_0180

    show tiger am_u talk_am
    with dissolve

    t "\"가헬, 자네의 태도는 여전히 오만방자하기 그지없군.\"" id c01_0181
    
    t "\"[pl_name][josa_eul_reul] 좀 본받게. 서 있는 자세부터 이렇게 교양이 흘러넘치지 않나!\"" id c01_0182

    show tiger base_am
    with dissolve

    c talk "\"하하... 그것 참 감사한 일이네요.\"" id c01_0183

    c base "가헬이 처음에 엘레드에게 무례한 모습을 보였을 땐 귀족 모독죄로 잡혀갈까봐 얼굴이 사색이 됐다." id c01_0184

    c "하지만 엘레드는 가헬의 이런 태도에도 껄껄 웃으며 매번 받아친다. 무례한 언행에도 무신경한건지 어른의 여유를 나에게 어필하는 것인지는 모를 일이다." id c01_0185

    show tiger am_d talk_am
    with dissolve

    t "\"그리고 [pl_name], 이렇게 비리비리한 용병은 왜 고용하고 있는 것이지?\"" id c01_0186
    
    t "\"이 기회에 저런 비실한 녀석은 치워버리고 내게 오는 것은 어떤가.\"" id c01_0187

    show tiger base_am
    with dissolve

    c "가헬의 근육을 눈 앞에 두고 '비리비리하다'고 평가할 수 있는 것은 오직 엘레드 뿐일 거다." id c01_0188

    play sound "effect/footstep.mp3" volume 0.85
    show tiger am_u smile_am at fwalk
    with Dissolve (0.2)
    
    c "엘레드는 어느새 카운터에 바짝 다가와 근육을 자랑하듯 팔을 괸 자세로 나를 잡아먹을 듯 바라보고 있었다." id c01_0189

    t "\"그리고 몸처럼 거기도 좀 허약해 보이는데... 밤일은 제대로 할 수 있을지 의문이야.\"" id c01_0190
    
    t "\"나 정도 크기는 되야 연인에게 사랑받을 수 있다네.\"" id c01_0191

    show tiger at change(1.22, -500, 235)
    with ease
    show tiger at change(1.22, -500, 135)
    with ease

    show tiger wink_am
    with dissolve

    c "그가 슬쩍 고간 보호대를 내려 속옷을 보여주고, 내게 윙크를 한다. 꽉 찬 주머니처럼 빵빵한 속옷은 얇디 얇은 끈으로 간신히 제 기능을 하고있다." id c01_0192
    
    c shy "붉은색이군..." id c01_0193

    play sound "effect/footstep.mp3" volume 0.85
    show wolf am_u vangry at fwalk
    with Dissolve (0.2)

    w "\"그 돼지같이 둔중한 몸뚱이로 뭘 할 수 있다는 거지? 그리고 크기는 나도 지지 않는다.\"" id c01_0194

    show wolf am_d
    with Dissolve (0.2)
    show wolf at change (1.22, 500, 235)
    with ease

    play sound "audio/effect/crash.mp3" volume 0.45
    with hpunch

    c angry "\"그만!!\"" id c01_0195

    show tiger am_d base_am
    with dissolve
    show wolf base
    with dissolve
    show wolf at change (1.22, 500, 135)
    with ease
    show wolf am_d base 
    with dissolve

    c base "가헬이 정말로 하의를 내려 크기를 증명하려고 하자 나는 반사적으로 손에 잡힌 두꺼운 마법서적을 카운터에 내려쳤다." id c01_0196

    c "쾅 소리에 두 사람은 내 눈치를 보듯 옷매무새를 다듬었다. 가헬은 둘째치고 엘레드에게 호통을 친 상황에 머리가 아플 지경이었다." id c01_0197


    hide tiger
    hide wolf
    play sound "effect/footstep.mp3" volume 0.85
    show tiger at change (1.22, -500, 135), walk (600, 1.6, 3)
    show wolf at change (1.22, 500, 135)

    c "이대로 재판에 끌려가 끔찍한 모습으로 죽는건가 하는 생각도 들었지만, 다행히 엘레드는 웃음을 터트리며 가헬의 어깨에 (강제로) 팔을 걸쳤다." id c01_0198
     
    c "친구처럼 구는 엘레드와 얼음장처럼 차가운 가헬의 얼굴이 극명한 대비를 이루었다." id c01_0199

    show tiger laugh_am
    with dissolve

    t "\"크하하하! 자네 성격 하나는 맘에 드는군! 남자라면 그래야지!\"" id c01_0200

    c sneer "나는 속으로 안도의 한숨을 쉬면서 다행이라고 생각했다. 가헬도 엘레드의 팔을 떼어내기만 하고 괜히 다른 말을 얹지 않았다." id c01_0201


    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c01_0202

    show tiger base_am at change (1, 100, 0)
    show wolf at change (1, 500, 0)
    with dissolve

    c base "입구의 종이 울리며 다른 손님이 들어오는 것이 보였다." id c01_0203

    play sound "effect/footstep.mp3" volume 0.85
    show tiger at walk(-500, 1.6, 3)
    
    c "엘레드는 지금까지 방해해서 미안했는지, 금화 한 닢을 카운터 위에 올려두었다." id c01_0204

    c question2 "(잠깐, 저 금화를 어디서 꺼낸거지?)" id c01_0205

    c base "(...이런걸 생각할 때가 아니지)" id c01_0206

    c "나는 정신을 차리고, 그냥 가려는 엘레드에게 뭐라도 주려고 했다." id c01_0207

    menu:
        "허브오일을 준다.":

            $ tiger_understanding +=1
            $ oil += 1
            $ display_text = _("엘레드 이해도 변화") 
            show screen affection_indicator

            "[pl_name][josa_eun_neun] 푸른 빛이 감도는 고급 허브 오일을 엘레드에게 챙겨주기로 했다." id c01_0208

            c "나는 나가려는 엘레드를 불러 멈춰 세웠다." id c01_0209

            show oil:
                xcenter 0.5
                ycenter 0.5
            with dissolve

            c talk "\"털 관리에 좋은 겁니다. 외부활동을 하기 전에 발라두면 윤기나는 털을 유지 할 수 있을 거에요.\"" id c01_0210

            hide oil
            with dissolve

            show tiger am_u talk_am
            with dissolve

            t "\"음...? 이런 걸 받으려고 금화를 준 건 아니네만...\"" id c01_0211

            show tiger am_d happy_am
            with dissolve

            t "\"자네가 선물해주는 것을 거부할 수 는 없지! 감사히 받겠네!\"" id c01_0212

            c base "그저 금화가 부담되어 준 것이었지만, 엘레드는 생각보다 굉장히 좋아했다." id c01_0213


        "회복물약을 준다.":

            "[pl_name][josa_eun_neun] 회복 물약을 엘레드에게 챙겨주기로 했다." id c01_0214

            c base "나는 나가려는 엘레드를 불러 멈춰 세웠다." id c01_0215

            show potion :
                xcenter 0.5
                ycenter 0.5
            with dissolve

            c talk "\"언젠가 상처를 입으면 이걸 사용하세요. 효과가 좋을 겁니다.\"" id c01_0216

            hide potion
            with dissolve

            show tiger am_u talk_am
            with dissolve

            t "\"이게 그 유명한 자네 상점의 회복 물약인가!\"" id c01_0217

            t "\"뭔가 받으려고 금화를 준 건 아니지만, 잘 쓰겠네.\"" id c01_0218

            show tiger am_d base_am
            with dissolve

            c base "그가 만족해 하는 것 같다." id c01_0219

        "그냥 감사히 돈만 받는다.":

            "[pl_name][josa_eun_neun] 생각이 바뀌어서 그냥 금화를 받기로 했다." id c01_0220

            c base "(생각해보니 귀족이라 돈이 많을 텐데... 굳이 뭘 따로 줄 필요는 없겠지. 안 그래도 돈이 부족했는데 잘됐다.)" id c01_0221
            

    show tiger talk_am
    with dissolve

    t "\"내가 너무 방해 한 것 같군그래. 그럼, 내일 다시 오겠네 [pl_name]!\"" id c01_0222

    show tiger wink_am
    with dissolve

    c base "그는 앙큼한 윙크를 날리며 상점을 나갔다." id c01_0223

    hide tiger
    with dissolve

    c "주황색 뒤통수에 가헬의 시선이 칼날처럼 꽂혔다." id c01_0224

    c ddam2 "언제나 그랬지만 오늘 유난히 더 정신적으로 피곤해졌다. 아무리 금화 한 닢이면 남는 장사긴 해도, 아침부터 엘레드에게 기가 빨려 녹초가 되는 건 힘든 일이다." id c01_0225

    c base "나는 일단 방금 들어온 손님에게 어떤 물품을 찾는지 묻기로 했다." id c01_0226

    c talk "\"안녕하세요. 무엇을 찾으시나요?\"" id c01_0227

    n "\"아, 회복물약을 사러 왔습니다. 꼭 여기서 사야 한다는 얘기를 들었어요.\"" id c01_0228

    c base "나는 자동으로 준비된 멘트를 줄줄 읊기 시작했다." id c01_0229

    c talk "\"잘 오셨습니다. 저희 가게의 회복물약은 마탑에서 공인 받은 고품질로 유명하죠.\"" id c01_0230

    show potion :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    c talk "\"표준 규격 회복물약은 이쪽에 있습니다. 개당 가격은...\"" id c01_0231

    hide potion
    with dissolve

    "..." id c01_0232

    n "\"감사합니다.\"" id c01_0233

    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c01_0234

    c base "용병으로 보이는 수인이 물약 3개를 구매하고갔다." id c01_0235

    c "정말 소문이 어찌나 퍼졌는지 요즘은 이렇게 이른 시간부터 처음 보는 용병들이 와서 물약을 구매하곤 한다." id c01_0236
    
    c "나는 내심 뿌듯해 하며, 방금전의 개판을 조금이나마 잊을 수 있었다." id c01_0237

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (0, 1.6, 3)
    pause 1.7
    show wolf am_u angry 
    with dissolve

    w "\"그 근육돼지는 대체 언제까지 오려고 하는거지...\"" id c01_0238

    show wolf base
    with dissolve

    c "나와 달리 가헬은 여전히 엘레드가 불쾌했는지 짜증을 내며 돈을 금고에 집어넣었다." id c01_0239

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at fwalk

    c "가헬은 빈 자리에 물약을 진열하다가 뭔가 생각난 듯 나에게 성큼성큼 다가왔다." id c01_0240

    show wolf am_d talk
    with dissolve

    w "\"[pl_name], 저런 난봉꾼의 말에 절대 넘어가면 안 돼. 알겠지?\"" id c01_0241

    show wolf base
    with dissolve

    c "그가 두 손으로 내 어깨를 잡으며 굉장히 진지한 얼굴로 말한다." id c01_0242

    c "평소에도 가헬의 얼굴에 진지함이 모자란 편은 아니지만 지금은 거의 유언과 같은 비장함이 느껴질 정도였다." id c01_0243

    c "왜 이렇게까지 진지해진 것인지 이해할 수 없어서 나는 그냥 고개를 끄덕였다." id c01_0244

    c question2 "\"...? 알겠어.\"" id c01_0245

    c base "생각해보니 둘은 처음 만났을 때부터 별로 좋은 관계는 아니었다." id c01_0246

    c "나에게 작업을 거는 엘레드와 그를 쫒아내고 싶은 가헬, 그리고 다시 가헬을 얕보는 엘레드... 그렇게 둘의 삐걱거림은 날이 갈수록 커져만 갔다." id c01_0247

    c "사이에서 말려야 하나 싶지만 가헬과 엘레드 둘 다 그렇게까지 오래된 관계는 아니라서 중재하기 어렵기도 하다." id c01_0248

    c "이러다가 무기라도 꺼내드는 건 아닌가 하는 걱정도 눈꼽만큼 들긴 하지만 설마... 뭐, 내가 상관할바는 아니겠지." id c01_0249


label magic_shop_end:   

    scene bg shop2 with Fade(0.8, 0.8, 0.8)

    c base "손님이 올때마다 영업용 멘트를 하고 중간중간 재료 가공까지 신경쓰다보니 시간이 금방 흘러간다." id c01_0250

    c "어느새 창밖에는 해가 뉘엿뉘엿 저물어가고 따스한 노을빛이 가게 안으로 들어온다. 나는 오늘 장사를 마무리할 요량으로 말했다." id c01_0251

    c talk "\"이제 정리하고 마무리하자. 오늘도 도와줘서 고마워.\"" id c01_0252

    show wolf
    with dissolve

    c base "가헬은 고개를 끄덕이고는 진열된 물건들을 선반에 수납하기 시작했다." id c01_0253

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (-500, 1.6, 3)
    pause 1.3
    stop sound fadeout 0.7
    pause 0.4
    show wolf at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85 fadeout 0.5
    show wolf at walk (500, 2.5, 4)
    pause 2.6
    show wolf at mirror2
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85 fadeout 0.5
    show wolf at walk (0, 1.6, 3)
    pause 1.3
    stop sound fadeout 0.7
    pause 0.4
    hide wolf
    show wolf

    c "나는 금고와 장부를 정리하며 남은 물품들의 재고 파악을 했다." id c01_0254

    c consider "\"흠... 생각보다 회복물약이 더 모자라겠는걸?\"" id c01_0255

    c talk "\"다음주 정도에 던전에 가서 재료 수급을 하면 될꺼라고 생각 했는데, 지금 팔리는 속도를 보면 안될꺼 같아.\"" id c01_0256

    c "\"가헬, 내일부터 던전 진입 준비를 하고, 준비가 끝나는대로 바로 던전에 가자.\"" id c01_0257

    show wolf am_u talk
    with dissolve

    w "\"그래, 나도 장비 점검을 다시 해야겠군.\"" id c01_0257_01
    
    w "\"이번에도 {color=#ee3939}\'레타\'{/color} 던전에 가는 건가?\"" id c01_0258

    show wolf base
    with dissolve

    c "\"아니, 저번달엔 성도와 가까운 곳에 {color=#ee3939}\'마물 콜로니\'{/color}가 생겨서 먼 곳으로 갔던 거였어.\"" id c01_0259

    c "\"지금은 성도에서 제일 가까운 {color=#ee3939}\'타시아\'{/color} 던전으로 가는게 제일 좋겠지.\"" id c01_0260

    c base "던전마다 마력의 흐름에 따라 다양한 변화가 있지만 재료 채집의 관점에서 둘 사이에 유의미한 차이는 없다." id c01_0261

    c "누가 마나 허브를 죄다 뽑아서 씨를 말리지만 않았다면 어느 던전을 가도 괜찮으니 역시 가까운 던전이 가장 편하다." id c01_0262

    c talk "\"이전에도 자주 가던 던전이고, 딱히 엄청 위험한 몬스터가 발견된 곳도 아니니까 무리하게 준비할 필요는 없을거야.\"" id c01_0263

    show wolf am_d talk
    with dissolve

    w "\"[pl_name], 던전은 어떻게 변화할지 몰라. 아무리 위험도가 낮다고 하더라도 던전은 던전이야.\"" id c01_0264
    
    w "\"최악의 상황을 준비해야 목숨을 건질 수 있어.\"" id c01_0265

    show wolf base
    with dissolve

    c base "가헬의 진심이 담긴 충고에 절로 고개를 끄덕이게 된다. 무시무시한 마물이 가득한 던전도 다녔을 가헬이 말하니 무게감이 다르다." id c01_0266

    c talk "\"그건 그렇지... 제대로 준비해 둘게.\"" id c01_0267

    c base "하지만 그렇게 대답해놓고 마음 한구석에서는 안일한 생각이 튀어나왔다." id c01_0268

    c "지난 몇 년간 사망자도 없었고 초짜 용병들도 들락거리는 위험도 {color=#ee3939}\'하\'{/color} 던전에서 문제가 터져봤자 돌연변이 마물 정도일 것이다." id c01_0269
    
    c "연기폭탄 같은 것만 있어도 충분하지 않을까? " id c01_0270

    c talk "\"일단 준비는 내일부터 하고, 저녁이나 먹으러 가자.\"" id c01_0271

    c base "나는 가게 밖의 안내판을 뒤집어 영업 종료를 표시하고 문을 닫았다. 이렇게 또 하루가 지나간다." id c01_0272


label wolf_01:
   
    scene bg home
    with Fade(0.8, 0.8, 0.8)
    stop music fadeout 2.5

    c inn_d sleep "나는 평소보다 이른 아침에 잠에서 깼다. 밝은 햇빛이 창문을 통해 방 안을 비추고 있었다." id c01_0273

    c base "나는 조금만 더 잘까 고민하다가, 오늘 할일이 많다는 것을 상기하고 이르게 침대에서 벗어났다." id c01_0274

    scene bg shop2f
    with Fade(0.8, 0.8, 0.8)

    play sound "audio/effect/wood.mp3" volume 0.45 fadein 1.5

    c am_d base "아직은 어두운 상점 2층의 복도를 지나 1층에 내려가려고 하는데, 복도에서 조그맣게 끼기긱 소리가 들려온다." id c01_0275

    c question2 "(이게 무슨 소리지?)" id c01_0276

    c base "나는 호기심을 참지 못하고 소리를 따라갔다." id c01_0277

    scene bg shop2f_open_zoom
    with dissolve
    
    play sound "audio/effect/heavy_breath.mp3" volume 0.7 fadein 1.5

    "살짝 열린 문 틈새로 가헬의 거친 숨소리가 새어 나오고 있다." id c01_0278

    c "나는 가까이 갈수록 점점 커지는 그의 신음과 침대가 규칙적으로 삐걱이는 소리를 듣고 본능적으로 그가 무엇을 하고 있는지 깨달았다." id c01_0279

    stop sound fadeout 3.0

    menu:
        "문틈으로 가헬의 방안을 몰래 본다.":

            $ wolf_see += 1
            $ persistent.wolf_unlocked[0]= True

            jump wolf_see_01

      
        "가헬의 즐거운 시간을 방해하지 않기 위해 모른 척 자리를 비킨다.":

            scene bg shop2f
            with dissolve
            
            c "뭔가 아쉬운 느낌이 들었지만, 나는 그의 사생활을 지켜주기 위해 자리를 떠났다." id c01_0280

            c "(아침부터 활력이 넘치네.)" id c01_0281

            c "작게 열린 문 틈새로 눈이 마주칠까봐 나는 살금살금 뒤로 물러섰다. 서로 민망한 일이 생기지 않도록 배려해주기로 했다." id c01_0282

            c "나는 발소리를 죽이고 걸어가며 먼저 씻으러 가기로 했다. 냉철하고 노련한 용병의 모습을 보여주는 가헬도 역시 짐승의 면모가 있긴 하구나 생각했다." id c01_0283
            
            $ renpy.end_replay()
            
            scene bg shop
            with Fade (0.8, 0.8, 0.8)  

            jump magic_shop2


label wolf_see_01:

    scene bg wolf_s1_01
    with Fade(0.8, 0.8, 0.8)
    pause(1.0)
    
    play sound "audio/effect/heart_beat.mp3" volume 0.75 fadein 2.0

    "가헬은 방 안에서 조용히 혼자만의 시간을 보내고 있었기 때문에 살짝 열린 문 너머로 보이는 누군가의 존재를 의식하지 못했다." id c01_0284

    "방 안에서는 가죽 냄새와 수컷 늑대의 체취가 풍겼는데, 가헬의 거친 용병 생활에 어울리는 분위기였다. 평소에는 가죽 갑옷에 가려졌던 가헬의 몸이 완전히 나체가 되어있었다." id c01_0285

    "몸 곳곳에 움푹 패인 흉터 자국은 창문으로 들어오는 아침 햇살 아래서 빛나고 있었다." id c01_0286

    "아직 한낮처럼 밝지 않아서 그의 근육질 몸의 절반은 그림자에 가려졌지만, 어두운 실루엣과 대비되는 하얀 털로 덮인 팔다리는 극명한 대비를 이루며 시선을 끌었다." id c01_0287

    "가헬은 자위에 완전히 몰두한 채 침대에 기대어 붉은 얼굴을 하고 있었는데, 평소 금욕적인 태도와는 정반대의 모습이어서 보기 드문 광경이었다." id c01_0288

    "두터운 근육질의 허벅지와 거기에 지지않을 만큼 거대한 성기를 강하게 움켜쥐는 가헬의 커다란 손까지 모두 사나워 보였다." id c01_0289

    "검을 휘두를 때의 모습과도 비슷한, 아니 그보다 더 흉포한 기세가 느껴지는 순간이었다." id c01_0290

    #play sound "audio/effect/wolf1.mp3" volume 0.9   
    
    "그는 신음 소리가 복도에 울려 퍼지는 줄도 모른 채 지독한 쾌락에 빠져 있었다." id c01_0291
    
    c shy "(잠깐만 구경할까.)" id c01_0292

    stop music fadeout 3.0

    "수컷 늑대 특유의 사향과 땀 냄새가 뒤섞여 어지러울 정도로 진한 향기가 방 안을 가득 채웠다." id c01_0293

    #play sound "audio/effect/wolf6.mp3" volume 0.9

    "억누른 숨소리와 살이 스치는 소리가 고요한 방에 울려퍼진다." id c01_0294

    "힘에 겨운 듯 들썩이며 억눌린 신음을 내뱉는 가헬은 평소에 절대 볼 수 없는 모습이었다." id c01_0295

    ##music 삐걱이는소리
    play sound "audio/effect/wood.mp3" volume 0.45 fadein 1.5

    "가헬이 더 나은 각도를 찾기 위해 몸을 조금씩 움직일 때마다 침대 시트가 바스락거리고 침대가 삐걱거린다." id c01_0296

    c base "나는 경계심 많고 무뚝뚝한 평소의 가헬과 거리가 먼 짐승같은 모습에서 시선을 뗄 수 없었다." id c01_0297

    c "(엄청난데...)" id c01_0298

    "지나치게 큰 좆은 참지 못한 흥분으로 불끈거렸고, 기둥 표면에 도드라진 굵은 혈관이 꿈틀거렸다." id c01_0299

    scene bg wolf_s1_02
    with dissolve
    pause(1.0)

    "귀두 끝에서 프리컴 방울이 흘러내리며 창문 틈새로 들어오는 빛을 반사했다." id c01_0300

    show wolf_s1_p1
    with dissolve
    
    ##music 숨소리
    play sound "audio/effect/breath.mp3" volume 0.4

    "가헬이 능숙하게 성기를 쥐고 위아래로 문지를 때마다 그에게서 더 많은 음란한 소리가 흘러나왔다." id c01_0301

    "가헬은 신음을 참기 위해 송곳니로 아랫입술을 깨물며 버텼지만, 도저히 참을 수가 없었다." id c01_0302

    #play sound "audio/effect/wolf7.mp3" volume 0.7

    "그의 가쁜 숨소리는 낮은 으르렁거림으로 바뀌었다가 다시 거친 숨소리로 바뀌었고, 그 모든 소리는 해방되지 못한 흥분을 증기처럼 뿜어냈다." id c01_0303

    "그렇게 차갑고 신중한 인물이 쾌락에 굴복하는 모습은 매혹적이면서도 당황스러울 수밖에 없었다." id c01_0304

    "가헬의 푸른 눈동자는 퇴폐적인 쾌락으로 가득 차 있었고, 음탕한 자극에 너무 몰두한 나머지 문이 열려 있다는 사실을 눈치채거나 누가 자신을 지켜보고 있다는 의심조차 하지 못했다." id c01_0305

    #play sound "audio/effect/wolf6.mp3" volume 0.9

    w nake_d horny "\"하아... 후우... 그르르...\"" id c01_0306

    "가헬은 [pl_name]의 존재를 의식하지 못한 채 격렬한 움직임을 계속했고, 가까워지는 절정의 짜릿함이 척추를 타고 흘렀다." id c01_0307

    hide wolf_s1_p1
    with dissolve
    show wolf_s1_p2
    with dissolve

    "자기도 모르게 허벅지가 조여지고 손의 속도가 빨라졌다. 가헬은 한층 더 거칠게 자지를 문질렀다." id c01_0308

    ##music 찌걱이는 소리

    "움직임에 따라 핏줄 선 가슴근육이 꿈틀거리고, 멈추지 않고 흘러나온 프리컴은 손에 달라붙어 찌덕찌덕 소리를 냈다." id c01_0309

    "이 장관을 바라보는 관객은 가헬도 모르는 문 건너편의 [pl_name] 한 명 뿐이었지만 관객이 있는지도 모르는 이 무대는 점점 더 격렬해졌다." id c01_0310

    "고요한 방에 울려 퍼지는 신음소리는 지나친 쾌락에 오히려 고통스러워 하는 것처럼 느껴지기도 했다." id c01_0311

    "움직임에 따라 흔들리던 거대한 불알은 어느 순간 올라붙어서 경련을 일으키며 짜릿한 절정의 순간을 예고했다." id c01_0312

    w nake_u horny3 "\"하윽, 조금만 더...\"" id c01_0313

    "절정이 가까워지자 가헬의 손은 더 빠르게 거대한 자지를 가로질러 움직였고, 가쁜 호흡에 맞춰 리듬을 타며 꽉 쥐고 자지를 쥐어 짜내기 시작했다." id c01_0314

    "터져나오려는 욕망을 간신히 억누른 채로 하반신 깊은 곳에서 휘몰아치는 절정 전의 쾌락을 조금이라도 더 즐기고 있었다." id c01_0315

    "평소의 금욕적이던 검은 늑대는 어디가고 지금은 터져버릴 것 같은 쾌락의 파도에 휩쓸려 헐떡거리는 짐승만이 있었다. 찡그린 눈은 욕망으로 가득찼고 신음은 울부짖는 소리와 비슷해졌다." id c01_0316

    "끝없이 흘러나온 프리컴은 이제 거품이 잔뜩 생긴 불투명한 액체가 되어 아래로 흘러내렸고, 기둥을 따라 맥동하는 혈관줄기 사이를 가로질러 그의 거대한 불알 사이에 웅덩이를 만들어 냈다." id c01_0317

    "가헬이 자신의 자지를 문지를 때마다 더 많은 양의 액체가 그의 사타구니를 덮고 있는 검은 털로 스며들었다." id c01_0318

    "가헬의 호흡에 따라 들락날락하던 배가 꽉 조여들어 근육이 더욱 팽팽해졌고, 그것은 오랫동안 참아왔던 긴 황홀경이 시작한다는 신호였다." id c01_0319

    ##music 뭔가 나오는 소리
    play sound "audio/effect/sqz2.mp3" volume 0.65
    scene bg wolf_s1_03
    with dissolve
    with vpunch
    pause (0.5)
    with vpunch
    pause(1.2)


    "가헬의 온몸이 경련하듯 몇 번 꿈틀거리더니 첫 번째 분출이 터져 나왔다." id c01_0320
    play sound "audio/effect/sqz1.mp3" volume 0.7
    with hpunch
    pause (0.8)
    play sound "audio/effect/sqz1.mp3" volume 0.7
    pause (1.4)
    #play sound "audio/effect/wolf4.mp3" volume 0.8   
    w nake_u horny2 "\"크으윽! 아우우...!\"" id c01_0321

    "턱을 악물고 어떻게든 신음을 참아봤지만 터져나오는 짐승의 소리는 가릴 수 없었다." id c01_0322

    c ddam2 "(헉! 깜짝이야.)" id c01_0323

    "진하고 끈적해보이는 정액이 분수처럼 힘차게 분출되어 자신의 몸에 후두둑 떨어지고 그 아래 바닥을 더럽혔다." id c01_0324

    "그의 칠흑 같은 털은 땀과 정액에 적셔진 덕에 햇빛에 반짝이며 음란하고도 아름다운 광택을 뽐냈다." id c01_0325

    play sound "audio/effect/sqz3.mp3" volume 0.7
    with vpunch
    pause (0.8)

    "두 번째 파도가 치솟아도 가헬의 손은 멈추지 않았다." id c01_0326

    "몇 가닥의 백탁액 줄기가 끊임없이 계속해서 뿜어져 나왔고, 가헬의 괴물 같은 사정은 그의 거친 용병생활에서 쌓인 육욕이 남들보다 더하면 더했지 보통은 아니라는 걸 증명했다." id c01_0327

    #play sound "audio/effect/wolf7.mp3" volume 0.8

    w nake_u horny2 "\"그르르르르...\"" id c01_0328

    ##music 으르렁 거리는 소리

    "가헬은 자연스럽게 으르렁거리는 소리를 내기 시작했다. 낮은 울림의 늑대 울음소리는 밖으로도 새어나가 나의 등골을 오싹하게 만들었다." id c01_0329

    "가헬의 묵직한 불알은 모든 정액을 뱉어낼 기세로 심장 박동처럼 반복해서 꿈틀거렸다." id c01_0330

    "그에 지지 않을 만큼 손도 빠르게 왕복하며, 다음 분출이 이어질 때마다 온 몸을 부르르 떨었다." id c01_0331

    "가헬의 근육질 몸통에 쏟아진 정액이 복근 사이 골짜기를 따라 아래로 질질 흘러내리는 광경은 왠지 모를 공포심과 유혹적인 아름다움을 동시에 자아냈다." id c01_0332

    "흥분으로 인해 달궈진 몸에서 뿜어져 나오는 땀 냄새와 걸쭉한 분출로 인한 냄새가 섞여 독특한 수컷의 향기를 만들었다." id c01_0333

    "가헬의 음탕한 향기는 숨이 막힐 정도로 뜨겁고 축축하게 방 안을 가득 채웠고, 가헬의 커다란 몸은 멈추지 않고 정액을 자신과 주변에 계속 쏟아냈다." id c01_0334

    #play sound "audio/effect/wolf2.mp3" volume 0.9 fadein 1

    "목구멍에서 터져 나오는 신음은 쾌락과 울부짖음 사이에서 방황했다." id c01_0335

    scene bg wolf_s1_04
    with dissolve
    pause(1.0)   

    ##music 쓰러지는 소리

    play sound "audio/effect/body_fall.mp3" volume 0.8 fadein 0.5

    "마침내 가헬은 쾌락의 여파에 굴복한 듯 침대위에 쓰러졌고, 땀과 정액에 흠뻑 적셔진 털이 눈부신 태양빛 아래 흑단처럼 빛났다." id c01_0336

    play sound "audio/effect/slow_breath.mp3" volume 0.6

    "긴장이 풀리고 한층 편안해져 보이는 가헬은 숨을 크게 몰아쉬고 여전히 정액이 꿀럭꿀럭 새어 나오고 있는 그의 자지 끝 테두리를 살살 어루만졌다." id c01_0337

    "번개처럼 스쳐 지나간 절정을 다시 찾는 것처럼 손끝으로 구석구석 쾌락의 잔재를 끌어냈다." id c01_0338

    "숨을 헐떡이며 오르가즘 후의 행복감에 젖어 있는 가헬의 모습은 마치 여러명과 방탕한 섹스라도 한 것 같아서, 지금까지 봐왔던 냉철하고 노련한 용병으로서의 이미지와는 사뭇 대조적으로 보였다." id c01_0339

    w nake_d horny "\"후우... 하......\"" id c01_0340

    "가헬은 잠시 누워 있다가 다시 몸을 움직이기 시작했다. 불과 몇 분 전 그가 경험한 엄청난 분출에도 불구하고, 더 많은 것을 갈망하는 지속적인 욕망이 가헬의 안쪽에서부터 갉아먹는 것처럼 솟아올랐다." id c01_0341

    "한번의 클라이막스로는 완전히 충족되지 않은 욕구." id c01_0342

    hide wolf_s1_p2
    with dissolve
    show wolf_s1_p3
    with dissolve

    "그의 손은 여전히 발기된채 간헐적으로 정액이 조금씩 흘러내리는 자지를 향해 내려갔고, 손가락은 다시 기둥을 꽉 쥐고 움직일 준비를 했다." id c01_0343

    c ddam2 "(...이걸 또 한다고?)" id c01_0344

    c "나는 자신이 가헬의 자위를 전부 지켜봤다는 사실을 깨닫고 슬금슬금 도망갈 궁리를 했다." id c01_0345

    "한동안 서있느라 굳어버린 다리로 소리나지 않게 살금살금 계단쪽으로 걸어갔다." id c01_0346

    scene bg shop2f
    with dissolve

    c base "다행히 가헬은 눈치채지 못한 것 같았다. 질척거리는 소리, 신음소리, 땀과 정액 냄새가 점점 멀어진다." id c01_0347

    scene bg shop
    with Fade (0.8, 0.8, 0.8)    

    c "나는 1층까지 내려와서야 한숨을 푹 내쉬었다." id c01_0348

    c consider "..." id c01_0349

    c "뭔가 봐선 안될 것 같은 걸 봐버린 기분이다." id c01_0350

    $ renpy.end_replay()


label magic_shop2:

    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    c base "나는 상점 1층으로 내려와 던전에 들어가기 위한 준비를 시작했다. 상점 안의 선반을 둘러보며 챙길 물품을 둘러 보고 있었다." id c01_0351

    c "(일단 기본적인 물품부터 챙기자.)" id c01_0352

    c "로프, 후크와 같은 물품들을 챙기고 눈에 들어온 랜턴에 손을 뻗다가 망설였다." id c01_0353

    c "불빛은 마법으로도 밝힐 수 있어서 가져갈지 말지 고민하다, 가헬의 충고가 떠올라 일단 챙기기로 한다. 그 외에도 침낭 등 잡다한 물품들을 챙겼다." id c01_0354

    show potion :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    c "그리고 전투에서 발생 할 수 있는 부상을 생각해 회복 물약도 챙긴다." id c01_0355

    hide potion
    with dissolve
    
    c "문득 지하실에 숨겨둔 특제 물약이 생각났다." id c01_0356
    
    $ unlock_info_tag(0, "6")
    $ display_text = _("정보 : 특제 물약")
    show screen affection_indicator

    c "마탑 소속 연금술사들이 {color=#ee3939}\'고급\'{/color} 이라고 구분지어 파는 비싼 상급 회복 물약을 내 방식대로 흉내낸 것이다." id c01_0357

    c "당연한 얘기지만 강력한 효과를 내기 위해 {color=#ee3939}\'금지된 방법\'{/color}을 사용한 물건이라 많이 만들지도 못한다." id c01_0358

    c "효과가 강력한 만큼 위험도가 높은 던전에 갈 일이 있으면 보험삼아 가지고 간다. 그러나 이 물약은 제작법의 문제도 있고, 마탑의 공증을 받을 때 절대 비밀로 한 물건이라 들켜서는 안 된다." id c01_0359

    c "대부분 당연히 이 물약도 공증을 받았다고 생각하겠지만, 혹시라도 마탑에 이 물약의 정체를 들키면 죽는 것 보다 끔찍한 꼴이 될 것이다." id c01_0360

    c "이번에 가는 던전은 위험도도 낮으니 굳이 가져갈 필요가 있을까 하는 고민이 들었다." id c01_0361

    c consider "(하지만 보험삼아 들고가서 나쁠거 없는데... 지금까지 잘 숨겼고...)" id c01_0362

    menu:
        "역시 가헬의 충고를 생각해서 챙기기로 한다.":

            $ high_potion += 1
            
            c base "나는 특제 물약을 챙기기로 했다." id c01_0363

            c "(맞아, 던전은 던전... 혹시 모르니까 하나 챙기자. 잘 숨기고 다니면 되겠지.)" id c01_0364

            show high_potion :
                xcenter 0.5
                ycenter 0.5
            with dissolve

            "[pl_name][josa_eun_neun] 지하실의 비밀 금고에서 특제 물약을 챙겨 왔다." id c01_0365

            hide high_potion
            with dissolve

            "붉은 빛이 감도는 이 물약을 신중하게 감싸서 가방 안쪽에 넣었다." id c01_0366

            c "나는 좀도둑이 가방 안에 손을 넣더라도 쉽게 가져가지는 못할 정도로 꽁꽁 숨겨두었다." id c01_0367


      
        "괜히 유난 떨지 않고 다른 물건이나 챙겼다.":
        
            c base "(목숨만 건져 나오면 가게에서 치료할 수 있는데, 굳이 가져가지 말까...)" id c01_0368

            c "가헬의 말이 조금 걸렸지만 어차피 가는 곳은 하급던전이다. 나는 남는 공간에 붕대나 좀 더 챙겼다." id c01_0369

    
    c consider "(대충 여기에서 챙길 수 있는 물품은 다 챙겼나?)" id c01_0370

    c base "이제 육포와 건조 과일 같은 보존식품을 구매하기 위해 식료품점에 갈 준비를 했다." id c01_0371

    show wolf
    with dissolve

    c "주머니에 돈을 챙기는 그때 2층에서 발걸음이 들려 왔다. 왠지 개운한 표정의 가헬이 내려왔다." id c01_0372

    c talk "\"좋은 아침이야, 가헬.\"" id c01_0373

    show wolf am_u talk
    with dissolve

    w "\"좋은 아침. 벌써 준비중인가? 내가 좀더 일찍 일어났어야 했군.\"" id c01_0374

    show wolf base
    with dissolve

    c base "가헬은 아무래도 {color=#ee3939}\'바쁜 일\'{/color}을 마치고 내려온 것 같다." id c01_0375

    c "나는 의뭉스런 미소를 지으며 그를 빤히 보았다. 내 시선을 느꼈는지, 가헬이 얼굴에 의문을 띄운다." id c01_0376

    show wolf am_d talk
    with dissolve

    w "\"... 내 얼굴에 뭐가 묻었나.\"" id c01_0377

    show wolf base
    with dissolve

    c wink "\"아니 그냥, 오늘따라 더 듬직해 보여서?\"" id c01_0378

    show wolf am_u talk
    with dissolve

    w "\"...? 갑자기 무슨 말인지 모르겠군. 아무튼 먼저 씻고 와서 도와줘도 될까?\"" id c01_0379

    show wolf base
    with dissolve

    c base "나는 조금 놀라버렸다." id c01_0380

    c "가헬은 평소에 내가 그렇게 씻으라고 매번 말해도 가끔 씻을까 말까 하는... 몸에 물 묻히는 걸 정말 싫어하는 늑대였기 때문이다." id c01_0381

    c question2 "\"씻는다고...? 네가?\"" id c01_0382

    "가헬이 조금 얼굴을 붉히며 변명을 한다." id c01_0383

    show wolf am_u shy3
    with dissolve

    w "\"나도, 씻고 싶을 때 정도는 있다고.\"" id c01_0384

    c base "가헬의 배와 가슴이 묘하게 번들번들한 것을 보고, 조금 전 2층에서의 상황이 저절로 떠올랐다." id c01_0385

    show wolf am_u shy
    with dissolve

    c sneer "(하긴, 그런건가... 슬쩍 넘어가줘야겠군.)" id c01_0386

    c talk "\"뭐... 그래, 그럴 수 있지.\"" id c01_0387

    show wolf am_u shy2
    with dissolve

    c base "나는 관심 없는 척 화제를 다른 곳으로 돌렸다." id c01_0388

    show wolf am_u shy3
    with dissolve

    c talk "\"아무튼 이제 식료품점에 가서 보존식품을 사고... 아! 용병 길드도 들러야해서 조금 늦을꺼야.\"" id c01_0389
    
    c "\"혼자 가도 괜찮으니 천천히 씻어.\"" id c01_0390

    c base "평소라면 바로 짐꾼을 해주겠다며 따라 나섰을 가헬이 끄덕이며 수긍한다." id c01_0391

    show wolf am_d talk
    with dissolve

    w "\"알겠다. 그럼 나도 나대로 정비하고 있을게.\"" id c01_0392

    show wolf base
    with dissolve

    c "나는 가헬을 두고 상점밖으로 나섰다." id c01_0393

    stop music fadeout 2.5


label street :

    scene bg street with Fade(0.8, 0.8, 0.8)  
    play music "audio/spirit-of-adventure-130563.mp3" volume 0.9 fadein 1.0  

    c base "식료품점에서 육포와 건조과일을 넉넉히 사두고, 용병 길드에 들러 던전에 대한 새로운 정보가 있는지, 새롭게 배포된 지도가 있는지 확인했다." id c01_0394

    $ unlock_info_tag(0, "7")
    $ display_text = _("정보 : 마력진동")
    show screen affection_indicator

    c "별다른 정보는 없었고, 가끔 던전 내부에서 {color=#ee3939}\'마력진동\'{/color}이 일어난다는 것 뿐이었다." id c01_0395

    c "던전 속 마나의 흐름이 바뀌면서 생기는, 일종의 {color=#ee3939}\'튀는 물방울\'{/color}과 같은 것이다. 심하면 마력이 역류하지만 딱히 그럴 가능성은 없어보인다." id c01_0396

    c "나는 다시 상점가로 돌아가며 더 챙겨야 할 것들이 없는지 머릿속으로 다시 체크했다." id c01_0397

    c "용병 길드 앞에서 오른쪽 길목으로 돌자 수많은 인파가 몰려 있는게 보인다." id c01_0398

    c "심하게 부러진 나무 파편들과 섞여 땅바닥에 구르고 있는 과일들, 창을 든 경비대들과 그 틈새로 보이는 화난 사람들 몇명. 딱 봐도 뭔가 큰 일이 있었던 거 같다." id c01_0399

    c consider "과일가게엔 미안하지만 길거리가 꽉 막힌건 짜증이 났다. 이 거리를 쭉 지나가면 바로 상점인데, 돌아서 가려면 구불구불한 뒷골목을 빙 돌아가야 했다." id c01_0400

label tiger_01 :

    menu:
        "귀찮긴 하지만 어떻게든 뚫고 가자.":

            c base "나는 수많은 인파 사이를 헤치고 나가기로 했다." id c01_0401

            c ddam2 "\"잠깐, 잠시만... 지나갈게요! 으악!\"" id c01_0402

            c "싸움구경을 나온 사람들 사이를 어떻게든 비집고 들어가자 거의 숨이 막혀 죽을 것 같았다." id c01_0403

            c "낑낑대며 인파를 뚫고 지나가면서 동시에 가방을 놓치지 않게 조심하느라 안간힘을 썼다." id c01_0404

            n "\"이게 어떻게 내 책임이야!\"" id c01_0405

            n "\"그럼 내 책임이란 말이야?\"" id c01_0406

            c ddam "고성이 오가는 길바닥을 헤치고 지나가니 온 몸에 힘이 쭉 빠진다." id c01_0407

            c base "나는 한숨을 몰아쉬고는 다시 정신을 차리고 상점을 향해 걸어갔다." id c01_0408

            jump chapter1_end

        "시간은 좀 더 걸리더라도 골목길을 통해 가자.":

            jump tiger_see_01


label tiger_see_01 :
    $ persistent.tiger_unlocked[0]= True
    $ tiger_see += 1
    
    stop music fadeout 2.5
    scene bg back_alley
    with Fade(0.8, 0.8, 0.8)

    c base "혼잡한 거리를 피하기 위해 골목길로 들어갔다." id c01_0409

    c "역시 뒷골목에는 햇빛이 잘 들어오지 않아서 대낮인데도 어두운 느낌이 있다." id c01_0410

    c "소란스러운 길바닥에서 조용한 뒷골목을 걸으니 내 발소리가 유난히 크게 들린다." id c01_0411

    "{i}.....!!{/i}" id c01_0412

    play channel1 "effect/wet_slap.mp3" volume 0.7

    "발걸음 사이로 뭔가 이질적인 소리가 들린다." id c01_0413

    "마치 끈적한 풀 같은 걸 내려치는 소리와 비슷한..." id c01_0414

    c "기묘한 소리가 나자 나도 모르게 집중하자 방향을 느낄 수 있었다." id c01_0415
    
    "가는 길에서 오른쪽으로 꺾자 소리가 확실히 크게 들렸다." id c01_0416

    stop channel1 fadeout 2.5
    
    play channel2 "audio/effect/heavy_breath.mp3" volume 0.7 fadein 1.5

    n "\"하윽...\"" id c01_0417

    c "이번에는 누군가의 신음소리와 함께 섞여서 들린다." id c01_0418

    stop channel2 fadeout 5.0

    scene bg tiger_s1_01
    with Fade (0.8, 0.8, 0.8)
    play sound "audio/effect/heart_beat.mp3" volume 0.75 fadein 2.5

    c "내가 상상한게 맞는지 확인해보고 싶다는 생각을 하며 다시 길목을 돌자 역시나 {color=#ee3939}\'보통 뒷골목에서 볼 수 없는 광경\'{/color}이 있었다." id c01_0419

    "건물 틈새로 내리쬐는 밝은 아침 햇살을 받아 반짝반짝 빛나는 근육을 과시하는건 알몸의 엘레드였다." id c01_0420

    "그리고 그의 밑에는 마찬가지로 알몸의 검은 늑대수인이 벽을 붙잡은 채 숨을 헐떡이고 있었다." id c01_0421

    "그들은 어두운 뒷골목 아래서 열정적인 몸의 대화를 나누고 있었다." id c01_0422

    c "나는 어떤일이 벌어지고 있을지는 예상했었다. 하지만, 엘레드가 있는 것은 상상하지 못했다." id c01_0423

    c ddam2 "\"헉!...\"" id c01_0424

    "엘레드의 두터운 덩치는 좁은 골목길을 꽉 채우고있다. 수많은 시간의 훈련으로 단련된 듯한 그의 상체 근육이 잔뜩 부풀어오른게 보인다." id c01_0425

    "거대한 근육 위에 새겨진 호랑이 특유의 줄무늬가 그의 야성적인 모습을 더욱 강조하고 있다." id c01_0426
    
    show tiger_s1_eye
    show tiger_s1_surprise
    with hpunch
    with dissolve
    pause(0.5)

    "엘레드가 [pl_name][josa_eul_reul] 발견한다." id c01_0427

    "깜짝 놀라 굳어있는 [pl_name][josa_eul_reul] 향해 시선을 옮긴 엘레드도 마찬가지로 놀란 것 같았다." id c01_0428

    hide tiger_s1_surprise
    with dissolve

    "하지만 그것은 나의 착각이였는지, 그는 바로 능청스럽게 씨익 웃으며 나한테 말을 건넨다." id c01_0429

    t nake_d talk "\"이것 참, 아침부터 관객이 있을줄은. 하하하! 공연을 즐기러 왔나?\"" id c01_0430

    c base "내가 어떻게 대답할지 고민하는 사이 엘레드는 다시 움직이기 시작했다. 그의 젖꼭지에 달린 금색 피어싱이 반짝거리며 음탕한 몸짓에 맞춰 흔들리는게 보였다." id c01_0431

    menu:
        "빨리 이 자리를 뜬다.":
            
            c "나는 엘레드를 내버려 두고 발길을 돌리기로 결정했다." id c01_0432

            c consider "(음란한건 귀족들이 더 하다더니 진짜인가봐...)" id c01_0433

            c base "엘레드가 바람둥이인 것은 알고 있었지만 길거리에서 대놓고 이런 짓을 하다니, 정말 상상 이상의 변태였구나 하며 슬금슬금 물러섰다." id c01_0434

            c "엘레드의 녹색 눈이 나를 잡아먹을 듯 바라보고 있지만, 어떻게든 무시하며 뒤돌아섰다." id c01_0435
            
            c "내가 잘못한 것도 아닌데 왠지 죄책감이 들어서 골목길을 뛰어가듯 급하게 걸어갔다." id c01_0436

            stop sound fadeout 1.5
            
            $ renpy.end_replay()

            jump chapter1_end

        
        "계속 지켜보기로 한다.":
            $ tiger_love += 1
            $ display_text = _("엘레드 호감도 변화") 
            show screen affection_indicator

            c "나는 홀린듯이 고개를 끄덕였다. 엘레드는 씨익 웃으며 혀를 낼름거렸다." id c01_0437

    
    hide tiger_s1_eye
    with dissolve

    t nake_u talk "\"그럼, 본격적으로 해볼까?\"" id c01_0438

    scene bg tiger_s1_02
    with dissolve
    pause(1.0)

    "엘레드는 상대방의 허리를 강하게 움켜잡으며 무식할 정도로 두꺼운 자지를 안쪽 깊숙히 박아넣었다. 강한 충격에 늑대는 다리를 덜덜 떨며 잔뜩 긴장했다." id c01_0439

    "그는 엘레드와 달리 부끄러움이 남긴 했는지 벽에 숨듯 고개를 들지 못하고 이쪽을 보지 못했다." id c01_0440

    t nake_d horny2 "\"젠장... 너무 꽉 조이는군.\"" id c01_0441

    #play sound "audio/effect/tiger4.mp3" volume 0.7 fadein 1.0

    "엘레드는 헐떡거리며 으르렁 거리는 신음소리를 냈다." id c01_0442

    if oil == 1 :

        show oil:
            xcenter 0.5
            ycenter 0.5
        with dissolve

        "그는 잠시 허리를 뒤로 빼더니 바닥에 널부러진 갑옷에서 무언가 작은 병을 꺼낸다. 엘레드의 손에 들린 것은 허브오일이었다." id c01_0443

        c question2 "(저거... 내가 준거 거 아냐?)" id c01_0444

        c ddam2 "(이런데 쓰라고 준게 아니었는데...)" id c01_0445

        hide oil
        with dissolve

        "엘레드는 병을 열고 내용물을 전부 자신의 굵직한 육봉에 들이부었다. 두꺼운 손가락으로 기름이 뚝뚝 떨어지는 기둥을 쓸어내리는 모습이 외설적이다." id c01_0446

        play sound "audio/effect/sticky.mp3" volume 0.6

        "그대로 손가락을 상대방의 뒷구멍에 몇번 찔러넣더니, 다시 자지를 쑤셔 넣고 허리를 거칠게 흔들기 시작했다." id c01_0447

        with vpunch

        "깊은 곳을 찌를 때 마다 늑대의 검은 꼬리가 파르르 떨리면서 쾌락을 표현했다." id c01_0448

        n "\"박아주세요... 구멍, 하윽, 너무 좋아요...\"" id c01_0449

        "검은 늑대는 쾌락에 이성이 점점 마비되는지 [pl_name]의 존재를 잊어버리고 수치스러운 말을 줄줄 내뱉었다." id c01_0450

    else:

        "엘레드는 뻑뻑한 느낌에 조금 불편한지 콧김을 내뿜었다." id c01_0451

        t nake_d horny2 "킁..." id c01_0452

        "하지만 곧 적응 했는지 허리를 움직이는 속도가 점점 올라가기 시작했다." id c01_0452_01

    play sound "audio/effect/heavy_breath2.mp3" volume 0.5 fadein 1.0   

    "두 짐승의 헐떡임과 끙끙 대는 신음이 은밀한 뒷골목에서 들을 수 있는 유일한 소리였다. 엘레드는 절정에 가까워지자 상대방의 허리를 더욱 강하게 붙잡았다." id c01_0453

    "털 속으로 손가락이 파고들 정도로 강하게 움켜쥐고는 그대로 살짝 들어올렸다." id c01_0454

    n "\"허억...!\"" id c01_0455

    if oil == 1 :

        with vpunch

        t nake_d vhappy "\"원하는, 대로! 크하하하!!\"" id c01_0456

    "엘레드는 팔 힘으로 상대를 장난감처럼 다루기 시작했다." id c01_0457

    stop sound fadeout 2.0

    play channel1 "audio/effect/sex_slap.mp3" volume 0.4 fadein 2.5

    "불알과 불알이, 허벅지와 허벅지가 강렬하게 부딪히며 철벅철벅 천박한 소리를 낸다. 늑대 수인은 자비없는 힘과 속도에 일방적으로 유린당하면서 벽을 긁을 뿐이었다." id c01_0458
    
    "녹색 눈이 욕구와 쾌락으로 번들거리는 것 같았다." id c01_0459

    "잠시 뒤 엘레드가 낮게 으르렁거리며 절정이 임박했음을 예감했다." id c01_0460

    "엘레드는 마지막으로 엉덩이를 세게 밀어붙여 가장 깊은 곳까지 밀어넣는다." id c01_0461

    stop channel1 fadeout 2.5
    
    with hpunch
    pause (0.4)

    t nake_u horny3 "\"크으윽!\"" id c01_0462

    play sound "audio/effect/sqz1.mp3" volume 0.7
    scene bg tiger_s1_03
    with dissolve
    with hpunch
    pause (1.0)

    "오르가즘이 엘레드의 척추를 타고 흐르며 온 몸의 근육을 떨게 만든다. 그의 복근이 강하게 조여지고, 두꺼운 허벅지에는 힘이 들어가 핏줄이 불거져 나온다." id c01_0463

    "동시에 그의 아래 깔린 늑대수인도 절정을 시작했고, 손을 짚은 벽돌에는 발톱 자국을 남길 정도로 힘이 들어갔다." id c01_0464

    play sound "audio/effect/sqz3.mp3" volume 0.7
    with hpunch
    pause(0.8)

    "엘레드의 자지는 꿈틀거리며 정액을 마구 뱉어낸다. 거기에 짓눌린 늑대수인도 사정을 시작했다." id c01_0465

    play sound "audio/effect/sqz4.mp3" volume 0.6
    with vpunch
    pause(0.8)

    "엘레드는 뜨겁고 진한 정액으로 구멍 속을 빠르게 채워넣었다. 걸쭉한 수컷의 즙이 강력한 급류가 되어 깊은 곳을 향해 흘러갔다." id c01_0466

    #play sound "audio/effect/tiger2.mp3" volume 0.75 fadein 1.0
    with vpunch
    pause(0.3)
    t nake_u horny3 "\"크르르렁...!\"" id c01_0467

    "엘레드는 황홀경에 빠져 짐승의 소리를 냈다." id c01_0468

    "그의 자지는 여전히 상대방의 구멍 안에서 맥박치며 사정을 계속했다. 엘레드의 정액양은 한 명의 뱃속에 담기에는 너무 많았다." id c01_0469

    play sound "audio/effect/sqz2.mp3" volume 0.6
    scene bg tiger_s1_04
    with dissolve
    with hpunch
    pause (1.0)   

    "결국 역류하기 시작한 백탁액이 틈새에서 뿜어져 나온다." id c01_0470
    
    play channel1 "audio/effect/sex_slap.mp3" volume 0.45 fadein 3

    "사정을 이어가면서도 허리와 엉덩이는 멈추지 않았다. 육중한 불알이 살과 마주치며 철퍽 거린다." id c01_0471

    scene bg tiger_s1_05
    with dissolve
    pause (1.0)

    stop channel1 fadeout 2.5

    "엘레드는 원초적인 만족감이 척추 기저부에서 몸 전체로 퍼져 나가는 여운을 즐긴다." id c01_0472

    play sound "audio/effect/slow_breath2.mp3" volume 0.8

    t nake_u horny "\"후우...\"" id c01_0473

    "엘레드의 불알을 타고 흘러내리는 꾸덕한 정액은 방울방울 맺혀 떨어진다. 늑대수인이 흘린 정액도 뒷골목 바닥에 얼룩을 만든다." id c01_0474

    "수컷 짐승들의 짙은 냄새가 그들 주변을 가득 채우며 코를 자극한다." id c01_0475

    show tiger_s1_eye
    with dissolve
    pause(0.5)

    "마침내 엘레드는 자지를 빼내고 다시 나를 바라본다." id c01_0476

    "아직 흥분이 가시지 않은 듯 헐떡거리는 엘레드는 땀과 정액으로 흠뻑 젖은 몸을 가볍게 쓸어낸다." id c01_0477

    show tiger_s1_p
    with dissolve

    "그의 자지는 여전히 단단하게 위로 솟아 있었고 귀두에서는 정액이 조금씩 흘러내린다." id c01_0478

    #play sound "audio/effect/tiger5.mp3" volume 0.7 fadein 1.5

    "포식자의 눈동자는 내 눈동자를 마주하며 반짝인다. 엘레드는 그르렁 거리는 소리를 내며 말했다." id c01_0479

    t nake_u talk "\"공연은 끝나지 않았다네. 자네도 함께 하겠나?\"" id c01_0480

    hide tiger_s1_p
    with dissolve

    c "욕망으로 뜨겁게 달아오른 눈이 나를 바라보는 것이 보인다." id c01_0481

    menu:
        "거절한다":    

            c "나는 고개를 좌우로 흔들었다." id c01_0482

    "순간 당황한 표정의 엘레드가 능청스러운 웃음을 지으며 다시 말한다." id c01_0483

    t nake_d smile "\"그러지 말고, 조용한 곳에 가서...\"" id c01_0484

    c ddam2 "\"오늘은 좀 바빠서요.\"" id c01_0485

    c base "빨리 도망가고 싶어서 아무 말이나 내뱉어버렸다." id c01_0486

    c "만약 바쁘지 않았더라도 엘레드와 화끈한 일탈을 즐길 생각은 없지만 마치 바빠서 거절한 것 처럼 대답해버렸다." id c01_0487

    c "엘레드와 연애도 할 생각이 없는데 이런 불장난은 가당치않은 소리다." id c01_0488

    c "(아무렴 어때. 일단 빨리 가자.)" id c01_0489

    c "나는 알몸의 수컷 둘을 내버려두고 가게를 향해 돌아섰다. 뒤통수에 시선이 꽂히는 기분이 들었지만 그냥 무시했다." id c01_0490

    scene bg back_alley
    with Fade (0.8, 0.8, 0.8)
    play music "audio/chill-abstract-intention-12099.mp3" volume 0.7 fadein 2.5

    show tiger nake_u sad2
    with dissolve

    $ unlock_character_image("tiger", "tiger b_no base nake_d")
    $ display_text = _("이미지 : 엘레드(발기)")
    show screen affection_indicator

    t "\"하, 하하...\"" id c01_0491

    show tiger base
    with dissolve

    "[pl_name][josa_i_ga] 시야에서 안보일 정도로 멀어지자 엘레드는 조금씩 무표정으로 변해갔다." id c01_0492

    "뒤늦게 절정의 여운에서 벗어난 늑대가 머뭇 거리며 질문한다." id c01_0493

    n "\"엘레드 님?...\"" id c01_0494

    show tiger nake0_d
    with dissolve
    
    $ unlock_character_image("tiger", "tiger b_no base nake0_d")
    $ display_text = _("이미지 : 엘레드(알몸)")
    show screen affection_indicator

    "평소처럼 아직 끝나지 않은 행위를 이어가기 위해 그가 말을 붙였으나 엘레드는 이미 바닥에 놓인 갑옷을 줍고 있었다. 그러자 늑대 수인이 다시 말을 꺼냈다." id c01_0495

    n "\"아직 두세번은 더...\"" id c01_0496

    "엘레드는 단호한 목소리로 그의 말을 끊었다." id c01_0497

    show tiger nake0_u talk
    with dissolve

    with vpunch
    t "\"그만!, 오늘은 여기까지.\"" id c01_0498

    show tiger nake0_d base
    with dissolve

    "평소와는 다른 기사 엘레드의 낮고 진지한 목소리가 울려 퍼졌다." id c01_0499

    play sound "audio/effect/puton.mp3" volume 0.6
    show tiger am_d sad2_am
    with dissolve

    "엘레드는 자책이 섞인 무거운 한숨을 내쉬며, 갑옷을 급히 입었다." id c01_0500

    show tiger am_u sad2_am
    with dissolve

    t "\"...젠장.\"" id c01_0501

    show tiger am_d
    with dissolve

    "엘레드는 자기 자신을 이해할 수 없는 일이 요즘따라 계속되는 것 같아 착잡한 기분이었다." id c01_0502

    scene bg street
    with Fade (0.8,0.5,0.8)

    c "뒷골목을 빠져나오자 익숙한 길거리가 나온다. 정신없는 와중에 가게까지 잘 찾아온 것 같다." id c01_0503

    c "(그래서 아까 본 건... 진짜였을까.)" id c01_0504

    $ renpy.end_replay()


label chapter1_end :
    
    stop music fadeout 2.5
    scene bg shop
    with Fade (0.8,0.8,0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.45

    c ddam "\"드디어 상점에 도착했다...\"" id c01_0505

    show wolf talk
    with dissolve

    w "\"[pl_name].\"" id c01_0506

    show wolf base
    with dissolve

    c talk "\"어? 가헬, 벌써 준비 끝났어?\"" id c01_0507
    
    show wolf am_u talk
    with dissolve

    w "\"벌써라니, 한참 지났는데.\"" id c01_0508

    show wolf base
    with dissolve

    c base "가헬이 이끄는 대로 상점 안에 들어가니 벌써 2시가 넘어가고 있었다." id c01_0509
    
    c "이렇게까지 정신없이 보낸 하루는 처음이다. 준비를 위해 영업을 하루 쉬길 잘했다는 생각이 든다." id c01_0510

    show wolf am_d talk
    with dissolve

    w "\"준비는 거의 끝났다. 방금은 대장간에서 칼을 갈았고.\"" id c01_0511

    show wolf base
    with dissolve

    c talk "\"나는 식량이랑 지도를...\"" id c01_0512

    if tiger_see == 1 and wolf_see ==1 :

        c ddam "자꾸만 오늘 본 것들이 생각난다." id c01_0513

        c shy "가헬의 손에 주물러지는 기둥이나, 엘레드의 두툼한 귀두나..." id c01_0514
        
        c "두 눈으로 보고도 믿지 못할 광경이긴 했다. 아무리 그래도 길거리에서 그럴 줄은..." id c01_0515

        c ddam2 "굵기는 역시 엘레드가 이긴 것 같지만, 길이는 가헬이 좀 더... 아니, 내가 대체 무슨 생각을 하고 있는거지?" id c01_0516

        c base "어떻게든 정신을 차리기 위해 가방에서 물건을 꺼내 정리하며 말을 이었다." id c01_0517

    elif tiger_see == 0 and wolf_see == 1 :

        c ddam "자꾸만 오늘 본 것들이 생각난다." id c01_0518

        c shy "어쩌면 수컷으로서 당연한 것이긴 한데, 가헬에게 그렇게 짐승같은 모습이 있을 줄은..." id c01_0519

        c base "어떻게든 정신을 차리기 위해 가방에서 물건을 꺼내 정리하며 말을 이었다." id c01_0520

    elif tiger_see == 1 and wolf_see == 0 :

        c ddam "자꾸만 오늘 본 것들이 생각난다." id c01_0521

        c shy "두 눈으로 보고도 믿지 못할 광경이긴 했다. 아무리 그래도 길거리에서 그럴 줄은..." id c01_0522

        c base "어떻게든 정신을 차리기 위해 가방에서 물건을 꺼내 정리하며 말을 이었다." id c01_0523

    else:

        c base "배에서 나는 꼬르륵 소리가 내 말을 방해한다." id c01_0524

        c "돌아오는 길에 너무 힘을 많이 썼나보다. 나는 가방에서 물건을 꺼내 정리하며 말을 이었다." id c01_0525

    c talk "\"아 배고프다. 지금까지 점심도 못먹었어... 빵을 좀 먹어야겠어.\"" id c01_0526

    show wolf am_u talk
    with dissolve

    w "\"... 치즈를 꺼내올까?\"" id c01_0527

    show wolf am_d base
    with dissolve

    c talk "\"그래!\"" id c01_0528

    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (-1500, 2.8, 5)

    if tiger_see == 1 : 
        
        c base "괜히 큰 소리로 말했더니 오히려 어색하게 갈라지는 목소리를 냈다. 부끄러움을 숨기기 위해 나는 찬물을 들이켰다. 크게 한숨을 쉬고 나니 좀 진정이 되는 것 같다." id c01_0529

        c "....." id c01_0530

        c "점심을 먹고 던전에 대해 가헬과 얘기했다." id c01_0531

    else:

        c base "점심을 먹고 던전에 대해 가헬과 얘기했다." id c01_0532

    hide wolf
    show wolf talk
    with dissolve

    w "\"{color=#ee3939}\'마력진동\'{/color}은 조금 주의하는게 좋아.\"" id c01_0533

    show wolf base
    with dissolve

    c talk "\"그렇긴 한데 아직 엄청 약하기도 하고, 내일 얼른 갔다오면 될거야.\"" id c01_0534

    show wolf am_u pit
    with dissolve

    c base "내 말에 가헬은 토를 달지 않았지만 역시 못미더운 표정이었다." id c01_0535

    c "..." id c01_0536

    c "나는 다음날 던전에 들어가서야, 내 생각이 안일했다는 걸 뼈저리게 깨달았다." id c01_0537

    hide screen book_icon with dissolve
    stop music fadeout 2.5

    jump chapter2