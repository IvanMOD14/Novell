label chapter3:

    $ cleanup_memory()
    $ _skipping = False
    scene bg warehouse
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
    show three
    pause 1.0

    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 1.5 volume 0.35

    hide chapter_back
    hide chap
    hide ter
    hide three
    with Dissolve (1.5)
    $ _skipping = True

    
    show screen book_icon with dissolve
    window hide

    c base "오늘의 가게는 유난히 한산했다." id c03_0000

    c "가헬은 소속된 용병단의 회의가 있는지 아침부터 용병 길드로 갔다." id c03_0001

    c "평소에는 항상 첫 손님의 자리를 차지하던 엘레드도 최근에 바쁜 일이 있는지 얼굴을 자주 비추지 못했다." id c03_0002

    c "손님도 별로 없기도 했고, 오늘은 창고 정리나 하기로 결정 했다." id c03_0003

    show cara base
    with dissolve

    c "나는 난장판으로 흩어진 책들을 책장에 꽂으며 최대한 창고를 깔끔하게 정리했다." id c03_0004

    show cara talk am_u
    with dissolve

    c "\"응? 이건...\"" id c03_0005

    show cara base
    with dissolve

    show necklace :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    #푸른 보석 목걸이 이미지
    c "손에 걸리는 끈이 있어서 당겨보니 작은 보석 목걸이였다. 푸른 보석을 보니 이게 무슨 물건이었는지 기억났다." id c03_0006

    hide necklace
    with dissolve
    
    c "내 스승님이 선물해 준 아티팩트로, 미리 저장한 장소를 찾아갈 수 있도록 도와주는 나침반 기능이 있다." id c03_0007

    show cara talk am_d
    with dissolve

    c "\"어라? 안 켜지네.\"" id c03_0008

    show cara base
    with dissolve

    c "아무래도 오래된 물건인 데다가 등급도 낮은 아티팩트니까 마력이 다 소진되어 더 이상 작동하지 않는 것 같다." id c03_0009
    
    c "이제는 그냥 싸구려 보석 목걸이나 다름없지만, 추억이 깃든 물건이니까 상자에 잘 보관하기로 했다." id c03_0010

    show cara consider
    with dissolve

    c "(그러고 보니 스승님은 뭐 하고 계시려나?)" id c03_0011

    c "나는 목걸이를 손에 든 채로 생각에 잠겼다." id c03_0012

    show cara base
    with dissolve
    
    c "내가 마법 상점을 차리기 위해 집을 떠난 지도 2년이 넘었다." id c03_0013
    
    c "나의 스승님 \'류호\'는 정말 특이한 수인이라 온 세상을 제집처럼 돌아다니곤 했다. 아마 지금도 내가 상상하기 힘든 곳에 있지 않을까 하는 생각이 들었다." id c03_0014

    play sound "effect/flash_fast.mp3" volume 0.25    
    show flash_blue at flash_fast
    pause 0.95
    hide flash_blue at flash_fast

    # 파란 이펙트 연출
    "{i}번쩍!!{/i}" id c03_0015

    show cara ddam2 am_u
    with dissolve
    with vpunch
    c "\"으악! 뭐, 뭐야?\"" id c03_0016

    show cara base am_d
    with dissolve

    

    play sound "effect/Resonance.mp3" volume 0.5

    show light_emit6 at light_move3
    show light_emit1 at light_move
    pause 0.5
    show light_emit5 at light_move2
    pause 0.3
    show light_emit2 at light_move
    pause 0.3
    show light_emit3 at light_move2



    c "갑자기 목걸이의 보석 부분에서 빛이 나기 시작했다." id c03_0017
    
    c "햇빛에 약간 반짝이는 정도가 아니라 눈부신 빛이 뿜어져 나오고 있었다." id c03_0018

    play sound "effect/dropstone.mp3" volume 0.5
    
    c "나는 깜짝 놀라서 목걸이를 떨어트리고 말았다." id c03_0019

    hide light_emit1
    hide light_emit2
    hide light_emit3
    hide light_emit5
    hide light_emit6
    with dissolve
    
    c "바닥에 떨어진 목걸이는 푸른 빛으로 발광하다가 언제 그랬냐는 듯 다시 원래대로 돌아왔다." id c03_0020
    
    show cara consider
    with dissolve

    stop music fadeout 3
    
    c "(대체 뭐지? 내가 모르는 마법이라도 숨겨져 있나?)" id c03_0021

    show cara consider
    with dissolve

    c "내가 어리둥절해하는 사이, 갑자기 창고가 짙은 안개로 가득 찼다." id c03_0022
    #스승님 등장 이펙트
    hide cara
    with dissolve

    play sound "effect/dingding.mp3" volume 0.4

    show dragon base_out out_d at cloud_show

    show cloud1 at cloud_rise
    with dissolve
    show cloud2 at cloud_rise2
    with dissolve
    show cloud3 at cloud_rise3
    with dissolve

    pause 1.7

    c "그리고 그 안개 속에서 류호가 불쑥 나타났다." id c03_0023

    $ unlock_character("dragon")
    $ display_text = _("캐릭터 : 류호")
    show screen affection_indicator

    hide dragon
    hide cloud1
    hide cloud2
    hide cloud3
    show dragon base_out out_d
    with dissolve

    c "정말 생각하지도 못한 방법으로 창고에 나타난 류호 때문에 나는 기절할 정도로 놀랐다." id c03_0024
    
    play music "lost-in-the-enchanted-woods-191319.mp3" fadein 2.5 volume 0.35

    with vpunch

    c ddam2 "\"스승님?!\"" id c03_0025

    show dragon talk_out out_u
    with dissolve  

    d "\"내가 맞게 찾아왔구나. 여기가 네 상점 맞느냐?\"" id c03_0026
    
    show dragon base_out
    with dissolve
    
    c base "\"네, 맞아요. 아니 근데 무슨 일로 여기까지...\"" id c03_0027

    show dragon dissappoint_out out_u
    with dissolve

    d "\"섭섭한 소리를 하는군. 그 목걸이를 좌표 삼아 오지 않았으면 1년은 더 걸렸을 게다. 편지만 달랑 남겨놓은 제자 덕분에 말이지.\"" id c03_0028

    show dragon base_out out_d
    with dissolve

    c base "(아 맞다 목걸이. 상자에 담아 놔야지.)" id c03_0029

    c "이 수인이 나에게 마법과 주술을 가르쳐준 \'류호\'다." id c03_0030
    
    c "류호가 입고 있는 특이한 옷은 이 대륙에서 보기 힘든 물건이다." id c03_0031
    
    show dragon sleep_out
    with dissolve

    c "바다 건너 머나먼 동쪽의 어떤 나라에서 태어난 용 수인인 류호는 매우 오랜 세월 동안 전 세계를 방랑했다." id c03_0032
    
    show dragon base_out
    with dissolve

    c "잘 기억나지 않지만, 보육원에서 나를 데려간 수인이 류호였다." id c03_0033
    
    c "그는 용의 둥지(라고 부르는 그냥 집)에서 나에게 마법과 주술을 가르쳤다." id c03_0034

    c talk "\"스승님이 집에 계셔야 말로 하죠.\"" id c03_0035

    show dragon talk_out out_u
    with dissolve
    
    d "\"한 마디도 안 지는 걸 보니 성격은 여전하군.\"" id c03_0036
    
    show dragon base_out out_d
    with dissolve

    c base "하지만 류호는 방랑벽이 심해서 걸핏하면 집을 나갔다." id c03_0037
    
    c "정작 그와 함께 지낸 시간은 그렇게 길지 않았다." id c03_0038
    
    c "류호와 나는 멀다면 멀고 가깝다면 가까운, 미묘한 사이다." id c03_0039
    
    c "보통의 사제 관계보다는 더 가깝지만, 흔히 생각하는 입양가정의 부자 관계는 아니었다." id c03_0040

    scene bg shop
    with Fade(0.8, 0.8, 0.8)
    
    show dragon base_out out_d
    with dissolve
    pause 1.0
    show dragon at mirror
    with dissolve
    pause 1.0
    show dragon at mirror2
    with dissolve

    "류호는 창고에서 나와 가게를 천천히 둘러보다가 말했다." id c03_0041

    show dragon talk_out out_u
    with dissolve

    d "\"흠, 나쁘지 않은 가게로구나. 상품 종류가 조금 적은 것 같지만... 다 이유가 있겠지?\"" id c03_0042

    show dragon base_out out_d
    with dissolve

    c talk "\"회복 물약을 집중적으로 팔고 있어요. 용병들이 많이 사가거든요.\"" id c03_0043

    show dragon talk_out out_u
    with dissolve

    d "\"어련히 잘 하리라 믿는다. 너는 어릴 때부터 나 없이도 잘 컸으니까. 내가 해준 건...\"" id c03_0044

    show dragon sleep_out
    with dissolve

    "류호는 뭔가 생각났는지 다른 화제를 꺼냈다." id c03_0045

    show dragon talk_out
    with dissolve

    d "\"그러고 보니 이 마을에 괜찮은 식당 있느냐? 안내까진 필요 없으니 대충 위치나 알려다오.\"" id c03_0046

    show dragon base_out out_d
    with dissolve

    c question2 "\"식당? 요즘도 모든 메뉴를 싹 쓸어 담고 그러는 건 아니죠?\"" id c03_0047

    show dragon talk_out out_u
    with dissolve

    d "\"흠! 그 정도는 먹어야 배가 부른 것을.\"" id c03_0048

    show dragon base_out out_d
    with dissolve

    c base "대략 3년 전, 내가 류호의 집을 떠나기 전에 있었던 일이다." id c03_0049
    
    c "몇 달 만에 집에 돌아온 류호는 내 성인식을 완전히 깜빡했다면서, 몇 년 늦었지만 기념 선물을 주겠다고 했다." id c03_0050
    
    $ unlock_info_tag(2, "1")
    $ display_text = _("정보 : 순간이동")
    show screen affection_indicator

    c "나는 그냥 비싸고 좋은 식사나 함께 하자고 했고, 류호는 {color=#ee3939}'순간이동'{/color}까지 써서 나를 성도에서 가장 유명한 식당에 데려다주었다." id c03_0051
    
    c consider "류호는 그 곳의 모든 메뉴를 주문했고, 그날의 식사는 형언하기 힘든 재앙이었다." id c03_0052
    
    # (류호 키워드1 : 대식가)

    c talk "\"그때 생각만 해도 벌써 배불러요. 모든 메뉴를 딱 한입씩 먹었는데도 배가 터지는 줄 알았다니까요.\"" id c03_0053

    show dragon talk_out out_u
    with dissolve

    d "\"넌 너무 적게 먹는다니까. 주술도 검술만큼 체력이 필요한 일이다.\"" id c03_0054

    show dragon base_out out_d
    with dissolve

    c base "음식을 30그릇씩 먹는 것과 체력이 무슨 상관인지 모르겠지만, 나는 그냥 웃는 표정으로 대답했다." id c03_0055
    
    c "류호는 내가 알려준 식당의 위치를 창문 밖으로 가늠해 보며 생각에 잠겼다. 뭔가 식당은 핑계고 다른 할말이 있는 눈치였다." id c03_0056

    show dragon sleep_out
    with dissolve

    d "\"에헴...\"" id c03_0057

    show dragon base_out out_d
    with dissolve

    c "류호는 헛기침할 뿐 나를 바라보지 않고 먼 곳만 바라봤다." id c03_0058
    
    menu :
        
        "어떤 일이냐고 물어본다." :

            c "갑자기 어색해진 분위기를 참지 못하고 나는 입을 열었다." id c03_0059

    c talk "\"무슨 일 있어요? 뭔가 중요한 할 말이라도...\"" id c03_0060

    show dragon talk_out out_u
    with dissolve

    d "\"그래, 중요한 일이지.\"" id c03_0061

    show dragon base_out
    with dissolve

    "류호는 자기 수염을 쓰다듬고는 말을 이었다." id c03_0062

    show dragon talk_out out_u
    with dissolve

    d "\"네가 편지를 남기고 떠난 게 언제였지?\"" id c03_0063

    show dragon base_out
    with dissolve

    c talk "\"어... 2년 전이요.\"" id c03_0064

    show dragon talk_out out_u
    with dissolve

    d "\"그럼 우리가 만난 지 12년이 되었구나.\"" id c03_0065

    show dragon sleep_out out_d
    with dissolve

    c base "류호는 눈을 감고 무언가를 생각하고 있었다. 아마도 우리의 첫 만남을 생각하고 있는 것 같다." id c03_0066
    
    c consider "정작 나는 그때가 잘 기억나지 않아서, 그냥 보육원을 떠났다는 것 밖에 생각나지 않았다." id c03_0067

    show dragon talk_out out_u
    with dissolve

    d "\"300년 넘게 살아온 나에게도 짧은 시간은 아니었다. 하지만 오늘따라 짧게만 느껴지는군." id c03_0068

    show dragon base_out out_d
    with dissolve

    c base "류호는 지나간 날을 추억하는 듯, 나의 눈을 보면서도 그 너머의 과거를 바라보고 있었다." id c03_0069

    show dragon talk_out out_u
    with dissolve

    d "\"곧... 나는 너에 대한 모든 기억을 잃을 것이다.\"" id c03_0070

    show dragon base_out out_d
    with dissolve
    
    c question2 "\"네? 그게 무슨 말이에요?\"" id c03_0071

    c consider "이해가 되지 않아서 나는 류호의 말을 곱씹었다. 류호가 나를 기억하지 못하게 된다고?" id c03_0072

    show dragon talk_out out_u
    with dissolve

    d "\"강대한 주술에는 대가가 필요하지. 어떻게든 미루고 있었지만 슬슬 한계인 것 같구나.\"" id c03_0073

    show dragon base_out out_d
    with dissolve

    c talk "\"기억을 제물로 사용한 주술이라니, 스승님 대체 무슨 주술을...\"" id c03_0074

    show dragon talk_out out_u
    with dissolve

    d "\"미안하지만 어쩔 수 없었다.\"" id c03_0075

    show dragon base_out out_d
    with dissolve    
    
    #(류호 키워드2 : 기억 상실)

    c consider "갑작스러운 얘기에 나는 머릿속이 복잡해졌다." id c03_0076
    
    c "류호는 앞으로도 나의 스승님이지만 나는 류호의 제자에서 모르는 수인이 되어버린다." id c03_0077
    
    c "당황스러운 예고에 나는 머릿속으로 앞으로의 일을 생각했다." id c03_0078

    show dragon talk_out out_u
    with dissolve

    d "\"사실 네 편지를 읽고 찾아갈지 말지 고민하기도 했단다. 독립한 제자가 나 없이도 잘 살아간다면 괜찮지 않을까 해서...\"" id c03_0079
    
    d "\"하지만 내가 너를 버릴 수는 없지 않겠느냐.\"" id c03_0080

    show dragon base_out out_d
    with dissolve

    c sad_am "\"스승님...\"" id c03_0081

    c base "류호는 원래부터 그런 수인이다. 오지랖이 넓어서 처음 보는 수인도 도와주는데, 제자인 나는 오죽하겠는가." id c03_0082
    
    c "나를 생각하는 류호의 마음에 약간 감동받았지만, 어쨌든 나를 잊어버리게 된다는 사실이 내 마음을 무겁게 짓눌렀다." id c03_0083

    show dragon laugh_out out_u
    with dissolve

    d "\"하하핫! 그렇게 얼빠진 표정 하지 말거라. 나도 다 계획이 있으니.\"" id c03_0084

    show dragon talk_out out_u
    with dissolve

    $ unlock_info_tag(2, "2")
    $ display_text = _("정보 : 봉인")
    show screen affection_indicator

    d "\"사라지는 기억을 붙잡아서 {color=#ee3939}'봉인'{/color}할 생각이다. 이미 준비는 끝났지.\"" id c03_0085

    show dragon laugh_out out_d
    with dissolve

    c "류호는 호탕하게 웃으며 내 어깨를 두드렸다." id c03_0086
    
    show dragon base_out out_d
    with dissolve

    c "기억을 수정하는 마법은 (도덕적 문제는 둘째치고) 엄청난 실력이 필요하다. 류호의 주술은 엄청난 경지에 다다른 게 틀림없다." id c03_0087

    c talk "\"그럼 봉인한 기억은 어떻게 되나요?\"" id c03_0088

    show dragon talk_out out_u
    with dissolve

    d "\"수정 구슬 비슷한 물질로 변할 거다. 여기서부터가 진짜 문제인데...\"" id c03_0089
    
    d "\"너에 대한 기억이 사라진 상태로 봉인구를 가져봤자, 그 안에 뭐가 들었는지 어떻게 알겠나? 뭔가 위험한 것을 봉인했다고 의심하면 봉인을 영영 풀어보지 않을 텐데.\"" id c03_0090

    show dragon base_out out_d
    with dissolve

    c talk "\"게다가 그렇게 강한 주술이면 풀기도 쉽지 않을 테니까요.\"" id c03_0091

    show dragon talk_out out_u
    with dissolve

    d "\"그래서 네가 나를 잘 설득해 주었으면 한다. 봉인 해제가 하루아침에 되는 일은 아니니까 시간은 충분히 있을 테고.\"" id c03_0092
    
    show dragon sleep_out
    with dissolve

    d "\"후... 쉽지 않은 일을 부탁해서 미안하구나.\"" id c03_0093

    show dragon base_out out_d
    with dissolve

    c consider "상황을 제대로 이해하자 머릿속이 두 배는 더 복잡해졌다. 나를 잊어버린 스승님을 어떻게 설득할 것인가." id c03_0094
    
    c "류호의 입장에서 생각하려니 더욱 막막한 느낌이 들었다. 심각한 내 표정을 보고 류호는 입을 열었다." id c03_0095

    show dragon talk_out out_u
    with dissolve

    d "\"그렇게 고민한다고 명쾌한 정답이 나올 일이더냐? 차라리 평소의 너답게 굴어야 번뜩이는 생각이 떠오를 텐데.\"" id c03_0096

    show dragon base_out out_d
    with dissolve

    c talk "\"평소처럼...\"" id c03_0097

    c base "아직 실마리는 잡지 못했지만, 오히려 그때가 오면 어떻게든 될 것 같다는 느낌이 들었다." id c03_0098

    show dragon talk_out out_u
    with dissolve

    d "\"그래. 그런 표정이 너다운 표정이지.\"" id c03_0099

    show dragon smile_out out_d
    with dissolve

    "류호는 가볍게 미소 지으며 [pl_name][josa_eul_reul] 바라본다." id c03_0100

    show dragon talk_out out_u
    with dissolve

    d "\"그러고 보니... 상점을 차린 목표는 이루었느냐?\"" id c03_0101

    show dragon base_out out_d
    with dissolve

    c talk "\"목표...\"" id c03_0102

    c base "처음에는 제대로 된 \'내 것\'을 갖는 게 목표였다. 보육원에서는 모든 것을 함께 써야 했고, 그만큼 모든 것이 부족했다." id c03_0103
    
    c "류호와 만난 뒤에도 류호가 베푸는 친절에 계속 기대어 살 수는 없었다. 그래서 나는 내가 할 수 있는 일로 \'마법 상점\'을 선택한 것이다." id c03_0104
    
    # (주인공 키워드4 : 마법 상점)

    c talk "\"상점이 적자 없이 잘 굴러가니 이루었다고 볼 수 있겠죠?\"" id c03_0105

    "류호는 [pl_name]의 대답에 조금 의외라고 생각하며 대답했다." id c03_0106

    show dragon talk_out out_u
    with dissolve

    d "\"흐음... 뭐, 그걸로 네가 만족한다면 됐다.\"" id c03_0107

    show dragon base_out out_d
    with dissolve

    "류호가 생각하기에 [pl_name]의 재능이라면 훨씬 더 엄청난 일을 해낼 수 있었다." id c03_0108
    
    "하지만 [pl_name][josa_i_ga] 그럴 생각이 없다면 괜히 부추길 필요는 없다고 생각했다." id c03_0109

    show dragon talk_out out_u
    with dissolve

    d "\"이번에도 늦고 말았지만, 개업 선물로 뭔가 바라는 것 없느냐?\"" id c03_0110

    show dragon base_out out_d
    with dissolve

    c base "나는 가헬에게 줘야 할 아티팩트가 번뜩 생각났다." id c03_0111
    
    c "류호라면 고급 아티팩트도 만들어낼 수 있을 것이다. 이런 절호의 기회는 쉽게 오지 않는다." id c03_0112

    c talk "\"맞다. 아티팩트가 하나 필요한데...\"" id c03_0113

    show dragon talk_out out_u
    with dissolve

    d "\"어떤 아티팩트?\"" id c03_0114

    show dragon base_out out_d
    with dissolve

    c talk "\"어, 마법 반사용 보호막이요. 보석 장신구로 만들면 더 좋고...\"" id c03_0115

    "[pl_name][josa_eun_neun] 비싸게 팔릴법한 아티팩트를 즉석에서 떠올렸다." id c03_0116
    
    show dragon sleep_out out_u
    with dissolve

    "류호는 잠깐 생각에 잠긴 뒤 적절한 물건을 소환했다." id c03_0117
    
    # 초록색 보석반지? 아니면 뭔가 다른 이미지 등장

    show ring :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "초록색 보석이 박힌 반지가 류호의 손바닥에 나타났다." id c03_0118

    hide ring
    with dissolve

    d "\"흠!...\"" id c03_0119

    # 류호 주술 이펙트

    play sound "effect/flash.mp3" volume 0.2
    show flash_orange at flash

    show charm1 at charm_move (0, 150, 1.17)
    pause 0.3
    show charm2 at charm_move (650, 700, 0.8)
    pause 0.3
    show charm3 at charm_move (1200, 1050, 1.25)
    pause 1.9
    hide flash_orange at flash
    hide charm1
    hide charm2
    hide charm3
    pause 0.5

    show ring :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    show ring_red :
        xcenter 0.5
        ycenter 0.5
    with Dissolve (1.5)


    "허공에 아름다운 문양이 떠오르더니, 보석에 류호의 주술이 새겨진다." id c03_0120
    
    show dragon base_out out_u
    with dissolve

    "아름다운 보석 반지로 만든 아티팩트니 값어치는 확실할 것이다. [pl_name][josa_eun_neun] 류호에게서 아티팩트를 받아 소중하게 금고에 넣어놨다." id c03_0121

    hide ring
    hide ring_red
    with dissolve

    c smile "\"감사합니다, 스승님. 정말 필요한 물건이었어요.\"" id c03_0122

    show dragon laugh_out out_d
    with dissolve

    d "\"하핫! 이 정도는 간단하지.\"" id c03_0123

    show dragon base_out
    with dissolve
 
    d "\"...\"" id c03_0124

    play sound "audio/effect/body_fall.mp3"  volume 0.8
    pause 0.1
    show dragon dissappoint_out at change(1, 0, 100)
    with hpunch

    d "\"쿨럭쿨럭!\"" id c03_0125

    "류호는 갑작스레 기침하며 주저앉았다." id c03_0126

    c talk "\"스승님?\"" id c03_0127

    show dragon talk_out out_u
    with dissolve

    d "\"이런... 벌써 시작되려는 모양이구나. 잠시 쉴만한 곳 없느냐?\"" id c03_0128

    scene bg home with Fade(0.8, 0.8, 0.8)

    "[pl_name][josa_eun_neun] 류호를 부축해서 자신의 방 침대에 눕혔다." id c03_0129

    c ddam2 "(뭔가 이런 일이 자꾸 생기는 기분인데...)" id c03_0130

    show dragon talk am_u
    with dissolve

    d "\"이런 모습까지 보이고 싶지는 않았는데... 미안하군.\"" id c03_0131

    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-110, -160)

    show dragon sigh am_d
    with dissolve

    "류호는 작은 한숨을 쉬고는 설명했다." id c03_0132

    show dragon talk am_u
    with dissolve

    d "\"기억을 봉인하는 과정에서 내가 잠시 잠들 수 있다. 오래 걸리지 않으니 너무 걱정하지는 말고...\"" id c03_0133

    play sound "effect/flash_fast.mp3" volume 0.25 
    show flash_orange at flash_fast
    pause 0.95
    hide flash_orange at flash_fast
    pause 0.3
    hide dragon
    show cloud_gold1 at cloud_gold_move (-50, -150)
    show cloud_gold2 at cloud_gold_move (100, 150)
    show dragon base am_d    
    with dissolve
    show cloud_gold3 at cloud_gold_move (-40, -100)
    show cloud_gold4 at cloud_gold_move (20, 60)
    # 류호 주술 이펙트

    "류호의 주변에 금빛 구름 문양이 생겨난다." id c03_0134

    hide cloud_gold1
    hide cloud_gold2
    hide cloud_gold3
    hide cloud_gold4
    with dissolve
    show dragon sleep am_d
    with dissolve

    "스르륵 사라진 문양과 함께 류호는 가만히 눈을 감았다." id c03_0135

    d "\"그럼, 잘 부탁한다.\"" id c03_0136

    "류호는 그 말을 마지막으로 잠들었다." id c03_0137

    hide dragon
    with dissolve
    
    show cara talk am_u
    with dissolve

    c "\"... 스승님?\"" id c03_0138

    hide sigh
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at sigh_move (-80, -170)
    show cara sigh am_d
    with dissolve

    "[pl_name][josa_eun_neun] 류호에게 가까이 다가갔다. 류호가 잘 숨 쉬고 있는지 확인하고 안도의 한숨을 내쉬었다." id c03_0139

    show cara base
    with dissolve
    
    c "깨어나기 전까지 잠시 기다려야 할 것 같다." id c03_0140
    
    "가게를 비워둘 수도 없는 일이라 [pl_name][josa_eun_neun] 1층으로 내려갔다." id c03_0141

    play sound "effect/footstep.mp3" volume 0.85
    show cara at walk (-1500, 2.8, 5)
    pause(0.5)

    scene bg shop with Fade(0.8, 0.8, 0.8)

    show cara 
    with dissolve

    c "(별일 없어야 할 텐데.)" id c03_0142

    "[pl_name][josa_eun_neun] 주술로 \'기억\'도 다룰 수 있다는 사실에 생각이 많아졌다." id c03_0143

    show cara consider
    with dissolve

    c "류호에게 뭔가 문제라도 생기면 모든 기억이 사라져 버리는 걸까?" id c03_0144
    c "멀쩡하게 기억이 잘 봉인되더라도, 애당초 기억이 봉인된 상태라는 게 괜찮은 걸까?" id c03_0145
    c "혹시 없던 기억도 집어넣을 수 있나? 류호가 깨어나면 뭐부터 확인해야 하지?" id c03_0146

    "[pl_name][josa_eun_neun] 가게 일을 하면서 온갖 잡생각에 빠졌다." id c03_0147

    stop music fadeout 2.5

label dragon_amnesia:
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    show cara 
    with dissolve
    
    "몇 시간 후, [pl_name][josa_eun_neun] 가게를 조금 일찍 닫기로 했다." id c03_0148
    
    "류호가 \'오래 걸리지 않는다\'고 했지만 신경 쓰여서 일에 제대로 집중을 하지 못했다. [pl_name][josa_eun_neun] 자신의 방에 누워있을 류호를 확인하러 갔다." id c03_0149
    show cara at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85
    show cara at walk (1500, 2.8, 5)
    pause(1.5)
    scene bg home with Fade(0.8, 0.8, 0.8)

    show dragon sleep am_d
    with dissolve

    c talk "\"스승님?\"" id c03_0150

    d "\"으음...\"" id c03_0151
    
    show dragon base am_d
    with dissolve

    "류호는 때마침 잠에서 깨어나 눈을 비볐다." id c03_0152
    
    show dragon sleep
    with dissolve
    pause(0.5)
    show dragon base
    with dissolve

    d "\"... ?\"" id c03_0153
   
    "류호는 [pl_name][josa_eul_reul] 보고 어리둥절한 표정을 지었다." id c03_0154
    
    "잠에서 덜 깬 것인지, 류호는 눈을 느리게 깜빡였다. 뒤늦게 자리에서 일어난 류호가 말했다." id c03_0155

    show dragon talk am_u
    with dissolve
   
    d "\"누구신지 모르겠으나, 우선 감사드리오.\"" id c03_0156
    
    d "\"... 근데 내가 어쩌다 이런 곳에서 자고 있던 것인지?\"" id c03_0157

    show dragon base am_d
    with dissolve
   
    "상황 파악이 덜 된 류호의 말투는 [pl_name][josa_i_ga] 처음 들어보는 것이었다. [pl_name][josa_eun_neun] 류호가 정말로 기억을 잃어버린 것인지 확인하고 싶었다." id c03_0158
   
    c "\"제 이름은 [pl_name]입니다. 그리고 여기는 제 마법 상점입니다. 저는...\"" id c03_0159
    
    $ dragon_trick_choice1 = False
    $ dragon_trick_choice2 = False

label dragon_trick :
       
    menu:
        "아들이라고 한다." :

            jump say_son
                                

        "연인이라고 한다." :

            jump say_lover

    
        "{color=#ee3939}제자라고 한다.{/color}" if dragon_trick_choice1 and dragon_trick_choice2 == True : #1번 2번 다 봐야 열리게 만들기

            #류호 이해도 상승 코딩
            $ dragon_understanding += 1 
            $ display_text = _("류호 이해도 변화")
            show screen affection_indicator

            "[pl_name][josa_eun_neun] 자신을 제대로 소개하기로 마음먹었다." id c03_0160
        
            c talk "\"사실 당신의 제자입니다.\"" id c03_0161

            show dragon talk am_u
            with dissolve
        
            d "\"제자? 흐음...\"" id c03_0162

            show dragon base am_d
            with dissolve
        
            "류호는 날카로운 눈빛으로 [pl_name][josa_eul_reul] 바라보았다." id c03_0163

            show dragon talk am_u
            with dissolve
        
            d "\"나에게서 몇 년이나 마법과 주술을 배웠는지 물어봐도 되겠소?\"" id c03_0164

            show dragon base am_d
            with dissolve
        
            "[pl_name][josa_eun_neun] 이 질문이 류호의 함정이라는 것을 바로 간파했다. [pl_name][josa_eun_neun] 대답 대신 간단한 주술을 선보이기로 했다." id c03_0165
            
            # 불꽃 이펙트

            show ember1
            show ember2
            pause 0.1
            show orangelight2
            with dissolve
            pause 0.5

            play sound "effect/magic.mp3" volume 0.65
            pause 0.4
            stop sound fadeout 0.46
            pause 0.07

            play channel1 "effect/fire_magic.mp3" volume 0.4
            show black_back :
                alpha 0.6
                xoffset 20
                yoffset 0
            show fire_back :
                parallel :
                    ease 1.2 alpha 1
                    ease 1.2 alpha 0.7
                    repeat
                parallel :
                    ease 1.2 zoom 1.2 xoffset -220 yoffset -50
                    ease 1.2 zoom 1.0 xoffset 20 yoffset 0
                    repeat

            show fire_gif :
                xcenter 0.5
                ycenter 0.5
                zoom 0.4
                
                parallel:
                    ease 1 yoffset -10
                    ease 1 yoffset 10
                    repeat
                parallel:
                    ease 1.4 zoom 0.43
                    ease 1.4 zoom 0.4
                    repeat
                parallel:
                    ease 1.2 alpha 0.7
                    ease 1.2 alpha 1
                    repeat


            with dissolve


            "주술로 피워낸 불꽃이 허공에서 일렁인다." id c03_0166
       
            c "\"이 정도면 대답이 되었을까요?\"" id c03_0167

            hide fire_back
            hide fire_gif
            hide black_back
            hide fire_back
            with Dissolve (1.0)

            hide ember1
            hide ember2
            hide orangelight2
            with Dissolve (1.0)

            show dragon laugh am_u
            with dissolve
        
            d "\"하하! 재치 있는 대답이었소.\"" id c03_0168

            show dragon sleep
            with dissolve
        
            "류호는 수염을 쓰다듬으며 말을 이었다." id c03_0169

            show dragon talk am_d
            with dissolve
        
            d "\"흐음... 기억에 없는 제자라, 신기한 일이군. 내 제자는 세상에 딱 두 명인 줄 알았는데.\"" id c03_0170

            show dragon base
            with dissolve
        
            c "\"역시 다른 제자가 있으셨군요.\"" id c03_0171
        
            "류호가 살아온 세월이 긴 만큼 다른 제자가 있으리라고 예상은 했다. [pl_name][josa_i_ga] 직접 듣는 것은 이번이 처음이었다." id c03_0172

            show dragon sad
            with dissolve
        
            d "\"그렇소. 한 명은... 내 연인이었고. 다른 한 명은, 전쟁에 목숨을 바쳤다네.\"" id c03_0173
     
            "과거를 추억하는 류호의 표정은 그리 좋지 않았다. 지나간 일이지만 떠올리기엔 씁쓸한 추억인 것 같다." id c03_0174

            show dragon talk am_u
            with Dissolve (1.0)
            pause 1
            show dragon base am_d
            with dissolve
            
            "류호는 [pl_name][josa_eul_reul] 보며 무언가를 말하려다 그만두었다." id c03_0175
        
            c question2 "(자세히 얘기하기엔 좀 곤란한 과거인가? 궁금한데...)" id c03_0176
        
            # (류호 키워드3 옛 제자)

    show dragon talk am_u
    with dissolve

    d "\"일단, 더 자세히 얘기해 주겠나? 내가 자네의 스승이라는 것부터, 지금 이 상황까지.\"" id c03_0177

    show dragon base am_d
    with dissolve

    "[pl_name][josa_eun_neun] 대략적인 일의 전말을 설명했다. [pl_name]도 잘 아는 건 아니지만, \'기억을 제물로 사용한 주술\'에 대해서 특히 강조했다." id c03_0178

    show dragon dissappoint
    with dissolve
    
    "류호는 반신반의하면서도 이야기를 끝까지 들었다." id c03_0179

    show dragon talk am_u
    with dissolve

    d "\"흠... 허황된 이야기는 아닌 것 같군.\"" id c03_0180

    show dragon base
    with dissolve

    c base "스승님은 아직 나를 100\% 신뢰하지는 않는 것 같다. 따지고 보면 방금 만난 수인이나 다름없으니 당연한 일이다. 류호도 납득하는 데 긴 시간이 필요할 것이다." id c03_0181

    c talk "\"저에게 마법과 주술을 가르친 것도, 제가 남겨놓은 편지도 기억나지 않으시나요?\"" id c03_0182

    show dragon talk am_d
    with dissolve

    d "\"편지? 편지 같은 게 있었던가?\"" id c03_0183

    show dragon base
    with dissolve

    c base "스승님이 확실하게 본 물건이라도 나와 관련된 기억이면 아예 사라지는 것 같다." id c03_0184

    c talk "\"그럼 집 2층에도 침대랑 책장이 있는 건 기억 나시나요? 거기에 편지가 있었는데.\"" id c03_0185

    show dragon talk am_u
    with dissolve

    d "\"음, 몇 년 전에 내가 옮겨뒀지. 편지는 기억나지 않는데...\"" id c03_0186

    show dragon base am_d
    with dissolve

    "2층에 침대와 책장을 놓은 것은 10년 전의 [pl_name][josa_ida_da]. [pl_name][josa_wa_gwa] 관련된 기억에 모순점이 없도록 류호의 기억이 수정된 것이다." id c03_0187
    
    "[pl_name][josa_eun_neun] 뭔가 다른 증거가 없는지 생각했다." id c03_0188

    c "\"옛날에 선물로 주신 목걸이도...\"" id c03_0189

    show dragon talk am_u
    with dissolve

    d "\"목걸이?\"" id c03_0190

    show necklace :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    # 푸른 보석 목걸이 이미지
    "[pl_name][josa_eun_neun] 창고에 보관해 놓은 푸른 보석 목걸이를 꺼내왔다. 류호는 그 물건을 알아보는 눈치였다." id c03_0191

    hide necklace
    with dissolve
    pause 0.5
    show dragon am_d
    with dissolve

    d "\"내 둥지에 있던 것이 맞구나. 이걸 자네에게 선물로 줬다고?\"" id c03_0192

    show dragon base
    with dissolve

    c "\"집을 찾는 나침반 아티팩트로 만들어서 주셨어요. 아, 이제 더 이상 작동하지는 않아요.\"" id c03_0193

    show dragon talk am_u
    with dissolve

    d "\"으음... 내 물건이 맞지만, 선물로 준 기억은 없군. 정말로 자네에게 선물로 준 물건이 맞나?\"" id c03_0194

    c "\"네, 첫 생일선물입니다.\"" id c03_0195

    show dragon dissappoint am_d
    with dissolve

    "류호는 고민이 깊어졌다." id c03_0196
    
    "[pl_name]의 말을 믿으면 모든 것이 딱 맞아떨어진다. 하지만 의심하면 모든 증거가 속임수처럼 보인다. 옛날에도 주술의 힘을 탐내서 자신을 속이려는 집단이 있었다." id c03_0197

    show dragon talk am_u
    with dissolve

    d "\"무슨 말을 하고 싶은지 잘 알겠소. 지금은 시간이 좀 필요하오.\"" id c03_0198

    show dragon base am_d
    with dissolve

    "지금 당장 어느 한쪽으로 결론 내리기엔 너무 이르다. 류호는 결국 판단을 좀 미루기로 했다." id c03_0199

    show dragon talk am_u
    with dissolve

    d "\"아무튼, 다시 한번 감사하오. 일단 몸을 회복하고 나서...\"" id c03_0200

    show dragon base am_d
    with dissolve

    # 꼬르륵 사운드? 꼭 있을 필요는 없을듯한데
    play sound "effect/stomachgrumble.mp3" volume 0.9
    pause 0.6

    "{i}꼬르륵!!{/i}" id c03_0201

    "류호의 배에서 엄청나게 요란한 소리가 났다. 대식가인 류호에게는 너무 긴 시간의 공복이었다." id c03_0202

    show ddam at ddam_move (920,25)
    show dragon happy
    with dissolve
    
    "류호가 조금 민망한 웃음을 짓는 동안 [pl_name][josa_eun_neun] 저녁을 고민했다." id c03_0203

    c "\"바로 먹을 수 있는 걸 사 올게요.\"" id c03_0204

    hide ddam
    show dragon talk am_u
    with dissolve

    d "\"굳이 그럴 필요 없네. 내가 직접 식당에 가는 편이...\"" id c03_0205

    # 류호 털썩
    play sound "audio/effect/body_fall.mp3"  volume 0.8
    pause 0.1
    show dragon dissappoint at change(1, 0, 100)
    with hpunch

    d "\"...윽!\"" id c03_0206

    
    "류호는 갑자기 느껴지는 이상한 감각에 자세가 무너졌다. [pl_name][josa_eun_neun] 류호의 몸 상태가 여전히 안 좋은 줄 착각했다." id c03_0207

    c "\"누워서 쉬고 계세요. 금방 갔다 올게요.\"" id c03_0208

    "류호가 말릴 새도 없이 [pl_name][josa_eun_neun] 급하게 상점을 나갔다." id c03_0209

    stop music fadeout 2.5

    jump dragon_01


######################################
##### jump menu start ################
######################################

label say_son : 

    if dragon_trick_choice1 == False :
    
        $ dragon_trick_choice1 = True   
        
        "[pl_name][josa_eun_neun] 류호를 속일 절호의 기회를 놓치지 않았다." id c03_0210

        c talk "\"사실 당신의 아들입니다.\"" id c03_0211

        show dragon talk am_u
        with dissolve
        play sound "effect/boing.mp3" volume 0.9
        show question at question_move (870, 0)
        with dissolve

        d "\"아들이라고? 그럼 자네 나이가...\"" id c03_0212

        "류호는 크게 당황하며 반문했다." id c03_0213

        hide question
        show dragon base am_d
        with dissolve

        c "\"24살 입니다.\"" id c03_0214

        show dragon dissappoint am_u
        with dissolve

        d "\"... 설마 그때 만난 늑대가? 아니, 그럴 리가 없어... 색도 너무 다르고, 낳았으면 내가 낳았을 텐데... 으음, 절대 불가능한 건 아닌가...\"" id c03_0215

        "류호는 혼잣말을 중얼거리며 심각한 고민에 빠졌다. [pl_name][josa_eun_neun] 생각보다 진지한 류호의 반응에 놀랐다. 빨리 진실을 말해줘야 할 것 같다." id c03_0216

        c "\"아, 아니. 그게... 진짜로 아들은 아닙니다. 스승님이 12년 전에 보육원에서 저를 거둬주신 것 뿐이죠.\"" id c03_0217

        show dragon talk am_d
        with dissolve

        d "\"그랬던가?\"" id c03_0218

        show dragon base am_d
        with dissolve

        c "\"네. 그리고 마법과 주술을 가르쳐주신 게 전부입니다.\"" id c03_0219

        "[pl_name][josa_eul_reul] 아들로 입양했다면 신분 증명에서 알 수 있었을 것이다. 제대로 속은 류호는 머쓱한 웃음을 지으며 말했다." id c03_0220

        show dragon laugh am_u
        with dissolve

        d "\"자네 꽤 짓궂은 구석이 있군. 하하!\"" id c03_0221

        "[pl_name][josa_eun_neun] 딱히 부정하지 않고 어깨를 으쓱했다." id c03_0222

        show dragon base am_d
        with dissolve

        jump dragon_trick
    
    if dragon_trick_choice1 == True :

        show dragon talk am_u
        with dissolve
        
        d "\"장난치지 마시게.\"" id c03_0223

        show dragon base am_d
        with dissolve

        jump dragon_trick



label say_lover : 

    if dragon_trick_choice2 == False :

        $ dragon_trick_choice2 = True

        "[pl_name][josa_eun_neun] 류호가 어디까지 기억을 잃은 것인지 궁금했다." id c03_0224

        c base "(설마 모든 기억을 잊어버린 건 아니겠지?)" id c03_0225
        
        c talk "\"사실 당신의 연인입니다.\"" id c03_0226

        show dragon talk am_u
        with dissolve

        d "\"... 뭐?!\"" id c03_0227

        "류호는 깜짝 놀랐다가 어이없다는 표정을 하더니, 버럭 화를 냈다." id c03_0228

        show dragon angry
        with dissolve

        d "\"함부로 그런 농담 하지 말게!\"" id c03_0229

        c base "류호가 이렇게까지 화를 내는 건 처음 봤다. 나도 모르게 류호의 역린을 건드린 것 같다." id c03_0230

        c ddam2 "\"죄송합니다. 스승님이 정말 기억을 잃었나 궁금해서 그만...\"" id c03_0231

        show dragon dissappoint am_d
        with dissolve

        d "\"흠! 내가 진짜로 오해하지 않은 걸 다행으로 여기도록 하시오.\"" id c03_0232

        "류호는 더 쏘아붙이고 싶은 걸 참으며 혀를 찼다." id c03_0233

        show dragon base
        with dissolve

        jump dragon_trick


    if dragon_trick_choice2 == True :

        show dragon talk am_u
        with dissolve
        
        d "\"장난치지 마시게.\"" id c03_0234

        show dragon base am_d
        with dissolve

        jump dragon_trick



######################################
##### jump menu end ##################
######################################

    
label dragon_01 :

    # 길거리 저녁 배경
    scene bg street2 with Fade(0.8, 0.8, 0.8)
    play music "audio/middle-ages-147373.mp3" volume 0.45 fadein 2.5

    "[pl_name][josa_eun_neun] 식당으로 뛰어가다가 무언가 맛있는 냄새에 이끌려 자연스럽게 걸음을 멈추고 고개를 돌렸다." id c03_0235

    show chicken_stick :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "길거리의 노점상에서 꼬치구이를 굽고 있는 것이 보였다. [pl_name][josa_eun_neun] 식당보다 여기서 음식을 사는 것이 더 좋을 거 같다고 생각했다." id c03_0236

    "[pl_name][josa_eun_neun] 길거리의 노점상에서 팔고 있던 모든 꼬치구이를 샀다." id c03_0237

    hide chicken_stick
    with dissolve
    
    "가게 주인이 [pl_name][josa_eul_reul] 이상하게 바라보았지만, 그는 신경 쓰지 않았다. 어차피 이 정도 양을 먹어도 류호는 배부르지 않을 것이다." id c03_0238
 
    c "(그래도 꼬치구이 50개는 좀 무겁네...)" id c03_0239

    "[pl_name][josa_eun_neun] 꼬치구이를 양팔에 가득 안고 다시 자신의 상점으로 향했다." id c03_0240
 
    # 가게 저녁 배경
    scene bg shop2 with Fade(0.8, 0.8, 0.8)

    "맛있는 냄새를 풍기며 가게로 돌아온 [pl_name][josa_eun_neun] 식탁에 꼬치구이를 펼쳐놓았다. 노릇하게 구워진 각종 채소와 고기의 냄새가 식욕을 자극한다." id c03_0241
    
    "마침 계단을 내려오는 발소리가 들려서 [pl_name][josa_eun_neun] 고개를 들었다." id c03_0242
 
    c talk "\"몸은 괜찮으신, 헉!\"" id c03_0243

    show dragon nake0_d
    with dissolve

    $ unlock_character_image("dragon", "dragon b_no nake0_d")
    $ display_text = _("이미지 : 류호(알몸)")
    show screen affection_indicator
 
    "[pl_name][josa_eun_neun] 류호가 여기서도 알몸으로 다닐 줄은 몰랐다. 과거에도 집에 오면 옷을 아무 데나 훌렁 벗어던져서 특이하다고 생각했다." id c03_0244

    play sound "effect/footstep.mp3" volume 0.85
    show dragon at fwalk
    
    "알몸으로 나타난 류호는 [pl_name]의 반응에 신경 쓰지 않고 가까이 다가왔다." id c03_0245
     
    "용족 특유의 피부는 매끈하게 빛나고, 두터운 팔다리는 어른의 매력이 느껴진다." id c03_0246
    
    "그러나 무엇보다 시선을 끄는 것은 류호의 슬릿이다. 이런 \'내부로 수납된 생식기\'는 아무래도 흔치 않다." id c03_0247
    
    "류호는 아무렇지도 않은 듯 평범하게 말을 꺼냈다." id c03_0248

    show dragon talk nake0_u
    with dissolve
 
    d "\"내 몸 상태는 괜찮소.\"" id c03_0249

    show chicken_stick :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    
    d "\"이게 그 음식인가?\"" id c03_0250

    hide chicken_stick
    with dissolve
    pause 0.2
    show dragon base nake0_d
    with dissolve
 
    c "\"그, 뭐라도 입고 오세요.\"" id c03_0251

    show dragon :
        ease 0.4 yoffset 110
        ease 0.4 yoffset 135
 
    "류호는 [pl_name]의 말에 이해가 가지 않는 듯 어깨를 으쓱했다." id c03_0252

    play sound "effect/boing.mp3" volume 0.9
    show question at question_move (870, 0)
    show dragon talk nake0_u
    with dissolve
 
    d "\"음? 나는 딱히 춥지 않소.\"" id c03_0253

    hide question
    show dragon base nake0_d
    with dissolve
 
    c "\"아니 그게 아니라...\"" id c03_0254

    show dragon talk nake0_u
    with dissolve
 
    d "\"집에서는 벗고 있는 게 익숙해서... 아무래도 옷을 입으면 답답해서 말이오.\"" id c03_0255

    show dragon base
    with dissolve
 
    c ddam "(그... 그 허술한 옷을 입는 것도 답답하다고?)" id c03_0256
 
    "[pl_name][josa_eun_neun] 뭐라고 대답할 의지를 잃었다. 수인 사회는 노출에 꽤 관대하지만, 류호는 정도가 다르다." id c03_0257
    
    "[pl_name][josa_eun_neun] 알면 알수록 정말 특이한 수인이라고 생각했다." id c03_0258

    show dragon talk nake0_d
    with dissolve
 
    d "\"허기가 심해서 그런데, 염치 불고하고 먼저 먹어도 되겠소?\"" id c03_0259

    show dragon base
    with dissolve
 
    "[pl_name][josa_i_ga] 고개를 끄덕이자, 류호는 꼬치구이를 집어 들었다. 오랜만에 보는 류호의 식사는 여전히 놀라웠다." id c03_0260
    
    "먹는 속도가 특별히 빠른 것은 아니지만, 한순간도 쉬지 않고 끊임없이 음식이 들어가는 기세가 엄청났다." id c03_0261
    
    "[pl_name]도 꼬치를 하나 들고 고기를 씹었다. 그는 기름진 고기와 향신료가 잘 어울리는 맛이라고 생각했다." id c03_0262
 
    c base "(여전히 잘 드시네.)" id c03_0263
 
    "간단한 식사와 뒷정리가 끝나고, [pl_name][josa_eun_neun] 류호를 자신의 방에서 재우려고 했다. 류호가 더 쉬어야 한다고 생각했기 때문이다." id c03_0264

    show dragon talk nake0_u
    with dissolve
 
    d "\"다시 말하지만, 이제 몸 상태는 괜찮소.\"" id c03_0265

    show dragon base nake0_u
    with dissolve
 
    c talk "\"하지만 아까 쓰러질 뻔했잖아요.\"" id c03_0266

    show dragon talk nake0_d
    with dissolve
 
    d "\"아까 그것은... 여기 때문에 그렇다네.\"" id c03_0267

    show dragon base
    with dissolve

    "류호는 자신의 슬릿을 가리켰다. 부끄러움 없는 류호의 태도에 [pl_name][josa_i_ga] 더 부끄러워졌다." id c03_0268
 
    c shy "\"거기가... 왜요?\"" id c03_0269

    show dragon talk nake0_u
    with dissolve

label dragon_cg1_start :

    scene bg shop2
    show dragon talk nake0_u :
        zoom 1.22
        yoffset (153-18)

    d "\"갑자기 안쪽에 뭔가 끼인 것 같소.\"" id c03_0270

    show dragon base nake0_d
    with dissolve
 
    c base "(거기 안에는 당연히... 아!)" id c03_0271
 
    "류호는 기억이 봉인되면서 구슬 같은 게 생길 거라고 했다." id c03_0272
 
    c consider "(그게 설마... 그 안쪽에?)" id c03_0273
 
    "불가능한 일은 아니다. 단지 좀 민망할 뿐이다. [pl_name][josa_eun_neun] 류호에게 설명했다." id c03_0274
 
    c  talk "\"봉인으로 기억이 담긴 구체가 만들어진다고 했으니, 그게...\"" id c03_0275

    show dragon dissappoint
    with dissolve
 
    d "\"흐으음...\"" id c03_0276
 
    "류호는 잠시 고민하더니 [pl_name][josa_i_ga] 깜짝 놀랄 말을 했다." id c03_0277

    show dragon talk nake0_u
    with dissolve
 
    d "\"빼는 걸 도와주겠소?\"" id c03_0278

    show dragon base nake0_d
    with dissolve

    menu:
        "슬릿 안쪽이 궁금하니까 도와준다." :
            
            # 류호 씬 해금
            $ persistent.dragon_unlocked[0]= True
            stop music fadeout 2.5

            jump dragon_see_01

        "민망한 일이 될 것 같으니까 거절한다." :

            "뭘 어떻게 도와줄 수 있는지 생각하자 부끄러워졌다. [pl_name][josa_eun_neun] 고개를 저으며 말했다." id c03_0279

            c "\"그것까진 좀...\"" id c03_0280

            show dragon talk nake0_u
            with dissolve

            d "\"흐음, 아쉽군. 혼자서 어떻게든 해보겠소.\"" id c03_0281
        
            show dragon base nake0_d
            with dissolve

            "[pl_name][josa_eun_neun] 류호를 자신의 방에서 재우고, 자신은 가헬의 방에서 자기로 했다." id c03_0282
            
            c base "(내일은 가헬도 돌아올 테고, 할 일도 많이 남아있다.)" id c03_0283
        
            c "(오늘은 푹 자자...)" id c03_0284
        
            "결심이 무색하게 [pl_name][josa_eun_neun] 그날 밤에 잠을 설쳤다." id c03_0285

            stop music fadeout 2.5
            $ renpy.end_replay()

            jump magic_shop_elred

label dragon_see_01 : 

    $ dragon_see += 1
    $ dragon_love += 1 
    $ display_text = _("류호 호감도 변화")
    show screen affection_indicator

    c "\"... 도와드릴게요.\"" id c03_0286

    "[pl_name]의 대답에 류호는 [pl_name][josa_eul_reul] 방으로 이끌었다." id c03_0287

    # 레스크의 방으로 배경 전환

    scene bg dragon_s1_back
    show dragon_s1_01
    with Fade(0.8, 0.8, 0.8) 
    play sound "effect/heart_beat.mp3" volume 0.75


    "류호는 바닥에 누워서 자리를 잡았다. [pl_name][josa_eun_neun] 이런 상황에서 류호 특유의 \'어른의 능숙함\'을 느끼는 게 약간 어색했다." id c03_0288

    d talk nake_d "\"너무 뻣뻣하게 서 있지 말고... 가까이 오게나.\"" id c03_0289

    scene bg dragon_s1_back :

        parallel:
            ease 1.78 zoom 1.08

        parallel :
            ease 0.16 yoffset 15
            ease 0.6  yoffset 0
            ease 0.39 yoffset 70
            ease 0.63 yoffset 0

    show dragon_s1_01 :
        
        parallel:
            ease 1.78 zoom 1.3

        parallel :
            ease 0.16 yoffset 20
            ease 0.6  yoffset 0
            ease 0.39 yoffset 80
            ease 0.63 yoffset 0
    
    "[pl_name][josa_i_ga] 가까이 다가가자, 류호는 다리를 살짝 벌리며 자신의 슬릿을 가리켰다." id c03_0290

    scene bg dragon_s1_back :
        zoom 1.08
        ease 1.5 yoffset 80
    show dragon_s1_01 :
        zoom 1.3
        ease 1.5 yoffset 160
    pause 1.5

    d talk nake_d "\"우선, 입구를 만져보겠소?\"" id c03_0291

    show dragon_s1_02 :
        zoom 1.3
        yoffset 160
    with dissolve
    
    "남근이 있을 법한 자리에는 갈라진 틈이 있을 뿐이었다. [pl_name][josa_eun_neun] 손가락으로 그 틈새를 건드려보았다." id c03_0292
    
    "촉감은 그냥 피부와 크게 다를 바 없지만, 류호는 민감하게 반응했다." id c03_0293

    play channel1 "effect/breath.mp3" volume 0.4 fadeout 2.5

    "가볍게 문지르는 것만으로도 류호는 흥분에 달아오르기 시작했다. 뜨거운 숨을 내쉰 류호는 바로 다음 단계로 진행했다." id c03_0294
    
    d horny "\"손가락 하나만 넣어보시오.\"" id c03_0295
    
    c talk "\"네...\"" id c03_0296

    play channel2 "effect/sticky.mp3" volume 0.65
    hide dragon_s1_02
    show dragon_s1_03 :
        zoom 1.3
        yoffset 160
    with dissolve
    
    "[pl_name][josa_i_ga] 손가락을 밀어넣자, 생각보다 쉽게 쑥 들어갔다. 구멍 안쪽은 뜨끈하고 약간 축축했다." id c03_0297

    "[pl_name][josa_eun_neun] 구슬이 어디 있을지 생각하며 손가락을 살살 움직였다. 류호는 [pl_name]의 의도를 파악하고 말했다." id c03_0298
    
    d horny2 "\"아니, 훨씬 더 깊이 있는 것 같다네. 지금은 입구를 넓히는 데 집중하게.\"" id c03_0299

    play sound "effect/sticky3.mp3" volume 0.7
    hide dragon_s1_03
    show dragon_s1_04 :    
        zoom 1.3
        yoffset 160
    with dissolve
    hide dragon_s1_04
    show dragon_s1_03 :    
        zoom 1.3
        yoffset 160
    with dissolve
    show dragon_s1_04 :    
        zoom 1.3
        yoffset 160
    with dissolve
    hide dragon_s1_04
    show dragon_s1_03 :    
        zoom 1.3
        yoffset 160
    with dissolve
    
    c base "왠지 류호의 명령에 끌려가는 것 같지만, 손가락을 더욱 움직였다. 손이 점점 축축해지는 게 기분이 이상했다." id c03_0300
    
    d "\"흐음, 뭔가 윤활제로 쓸 것을 갖고 있소? 향유라던가.\"" id c03_0301
    
    if oil == 1 and tiger_see == 1:
            
        "[pl_name][josa_eun_neun] 엘레드가 쓴 허브 오일이 번뜩 생각났다. 엘레드가 썼던 상황을 생각하면 윤활제로 쓰기 딱 좋은 물건인 것 같다." id c03_0302
        
        c talk "\"허브 오일은 어때요?\"" id c03_0303
        
        d "\"좋네.\"" id c03_0304
    else :
   
        "[pl_name][josa_eun_neun] 적당한 물건이 있나 생각했다." id c03_0305
        
        c "(기름 중에서도 향이 괜찮은 물건이라면...)" id c03_0306
        
        c talk "\"음... 허브 오일 같은 거요?\"" id c03_0307
        
        d "\"충분하네.\"" id c03_0308
    
    c "\"잠시만 기다려주세요. 금방 가져올게요.\"" id c03_0309

    play sound "effect/sticky4.mp3" volume 0.6
    hide dragon_s1_03
    show dragon_s1_slit:
        zoom 1.3
        yoffset 160   
    with dissolve
    
    "[pl_name][josa_eun_neun] 허브 오일을 찾으러 방에서 나갔다. 류호는 텅 빈 아래가 아쉬워서 입을 쩝쩝거렸다." id c03_0310
    
    "기왕이면 느긋하고 진한 교미를 즐기고 싶지만, 지금은 구슬을 빼는 게 먼저다." id c03_0311
    
    "[pl_name][josa_eun_neun] 창고에서 허브 오일을 가져왔다." id c03_0312

    "조심스레 방문을 열자 보이는 것은 여전히 바닥에 엎드린 류호였다. 류호가 다리를 벌린 모습은 굉장히 외설적이었다." id c03_0313

    play sound "effect/sticky.mp3" volume 0.65
    show dragon_s1_03 :
        zoom 1.3
        yoffset 160
    with dissolve
    pause 1.5

    play sound "effect/sticky4.mp3" volume 0.6
    hide dragon_s1_03
    hide dragon_s1_finger
    with dissolve
    
    "류호는 손으로 슬릿 안을 헤집으며 구슬을 찾다가 손을 뺐다. 살짝 열린 슬릿은 흥분을 참으며 흘러나온 액으로 흥건했다."    
    
    c "(오일 필요 없었던 거 아닌가?)" id c03_0314
    
    d horny "\"혼자서는 빼기가 힘들군... 내 생각보다 더 깊이 있는 것 같네.\"" id c03_0315

    show oil :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "[pl_name][josa_eun_neun] 일단 허브 오일 병을 열었다. 상쾌한 풀 내음이 은은하게 퍼진다. 손에 기름을 듬뿍 뿌리자 번들거리는 자신의 털이 신기했다." id c03_0316

    hide oil
    with dissolve
    
    d "\"우선 천천히 넣어보게나.\"" id c03_0317

    c "\"네...\"" id c03_0318

    play sound "effect/sticky2.mp3" volume 0.7
    show dragon_s1_03 :
        zoom 1.3
        yoffset 160
    with dissolve
    pause 1.5
    
    "[pl_name][josa_eun_neun] 손가락을 천천히 류호의 슬릿에 넣었다. 미끄럽고 축축한 액체가 섞이면서 질척한 소리를 낸다. 슬릿은 부드럽게 [pl_name]의 손을 삼켰다." id c03_0319
    
    c "(느낌 이상해...)" id c03_0320
    
    d horny2 "\"흐으... 조금 더 깊게...\"" id c03_0321

    menu :
        "손을 넣는다." :



            hide dragon_s1_03
            play sound "effect/sticky.mp3" volume 0.65
            show dragon_s1_05 :
                zoom 1.3
                yoffset 160
            show dragon_s1_finger
            with dissolve
            
            "류호가 미리 넓혀놓은 덕분에 무리 없이 손목까지 들어갔다. 뜨겁고 축축한 내부가 [pl_name]의 손을 꽉 조여왔다." id c03_0322
    
    "조금씩 안쪽으로 손을 뻗자, 무언가 만져지는 게 있었다. 하지만 구슬은 아닌 것 같았다." id c03_0323
    
    c "(이게 뭐지?)" id c03_0324

    play channel1 "effect/breath.mp3" volume 0.4
    with hpunch
    
    d "\"으음!...\"" id c03_0325
    
    c "(... 귀두인가?)" id c03_0326
    
    "당연히 슬릿 안에 자지가 있다는 건 알고 있지만, 직접 만지는 건 역시 기분이 묘하다." id c03_0327

    play sound "effect/sticky2.mp3" volume 0.7
    show dragon_s1_06 :
        zoom 1.3
        yoffset 160
    show dragon_s1_finger2
    with dissolve
    hide dragon_s1_finger2
    with dissolve
    show dragon_s1_finger2
    with dissolve
    
    "더 안쪽으로 손을 집어넣자 자연스럽게 남근의 표면을 훑게 됐다." id c03_0328

    hide dragon_s1_finger
    hide dragon_s1_finger2
    with dissolve
    
    "류호는 흥분에 다리를 잘게 떨었다. 어느 정도는 이런 상황을 예상하긴 했다." id c03_0329

    with vpunch    
    d "\"하윽!\"" id c03_0330
    
    "[pl_name][josa_eun_neun] 따뜻한 목욕물에 팔을 담그는 것처럼 천천히 깊게 집어넣었다. 류호의 슬릿은 놀랄 정도로 벌어져서 [pl_name]의 팔근육을 부드럽게 감싸고 있었다." id c03_0331
    
    c base "(사람 안에 팔이 이렇게...)" id c03_0332
    
    "이 정도로 깊게 들어갈 거라고 예상하지 못했다. [pl_name][josa_eun_neun] 약간 무섭다는 생각을 하면서도 동시에 호기심이 생겼다." id c03_0333
    
    c base "(대체 어디까지 들어갈 수 있지?)" id c03_0334

    
    hide dragon_s1_06
    play sound "effect/sticky3.mp3" volume 0.7
    show dragon_s1_05 :    
        zoom 1.3
        yoffset 160
    with dissolve

    show dragon_s1_06_1 :    
        zoom 1.3
        yoffset 160
    with dissolve

    hide dragon_s1_06_1
    show dragon_s1_05_1 :    
        zoom 1.3
        yoffset 160
    with dissolve

    show dragon_s1_06_1 :    
        zoom 1.3
        yoffset 160
    with dissolve

    
    "본래의 목적을 잊은 건 아니지만, 부끄러움이나 공포 같은 감정은 궁금증에 묻혀 사라졌다. [pl_name][josa_eun_neun] 더 안쪽을 향해 팔을 쑤욱 밀어 넣었다." id c03_0335

    with vpunch 
    
    d "\"허윽! 거, 거기!...\"" id c03_0336

    show dragon_s1_arm
    with dissolve
    
    "[pl_name]의 손끝에 뭔가 단단한 것이 닿았다. 말캉한 내벽에서 이질적으로 딱딱한 물체는 구슬밖에 없을 것이다." id c03_0337

    show dragon_s1_arm2
    with dissolve
    hide dragon_s1_arm2
    with dissolve
    
    "[pl_name][josa_eun_neun] 그것을 움켜잡으려 했지만, 생각보다 쉽지 않았다. 주먹을 쥘 수 있을 만큼 공간이 넉넉하지 않았다. 구석에 꽉 끼인 것을 손으로 툭툭 건드리는 게 한계였다." id c03_0338
    
    with hpunch

    d horny3 "\"크흡! 하아... 으흣!\"" id c03_0339
    
    "구슬을 잡기 위해 움직일 때마다 류호의 반응도 더 강해졌다." id c03_0340
    
    "자지의 꿈틀거림이 피부로 느껴지지만 [pl_name][josa_eun_neun] 신경 쓰지 않았다. 잡힐 듯 잡히지 않는 구슬이 약간 짜증 날 뿐이었다." id c03_0341

    hide dragon_s1_arm
    with dissolve
    
    "반면 [pl_name]의 손에 자극당하는 류호는 흥분을 참느라 고생했다." id c03_0342
    
    "구멍 안에 뭘 넣은 지도 꽤 오래돼서 힘들 줄 알았는데, 오히려 오랜만에 즐기는 쾌락에 몸이 녹아내리는 기분이었다." id c03_0343

    play sound "effect/sticky3.mp3" volume 0.7
    play channel1 "audio/effect/heavy_breath.mp3" volume 0.7
    
    "고요한 방에 찔꺽거리는 소리와 숨소리만 울려 퍼졌다."  id c03_0344
    
    d horny2 "\"후우... 자네, 생각보다 거칠군.\"" id c03_0345
    
    "류호는 가쁜 숨을 내쉬면서도 여유롭게 웃었다. 한계까지 벌어진 구멍과 욱신거리는 자지는 해방을 원하고 있지만, 류호는 조금만 더 참았다." id c03_0346
    
    c talk "\"뭔가... 손을 밀어내는 것 같은데요.\"" id c03_0347
    
    "[pl_name]의 착각이 아니었다. 류호의 슬릿 내벽이 손을 조금씩 밀어내고 있었다." id c03_0348
    
    d "\"윽... 나올 것, 같네...\"" id c03_0349

    stop channel1 fadeout 3
    
    c talk "\"손을 뺄까요?\"" id c03_0350

    play sound "effect/sticky2.mp3" volume 0.7
    hide dragon_s1_06_1
    show dragon_s1_05_1 :    
        zoom 1.3
        yoffset 160
    with dissolve
    
    "구슬이 나오는 건지 다른 게 나오는 건지 알 수 없지만, 아무튼 [pl_name][josa_eun_neun] 팔을 조금 뒤로 뺐다." id c03_0351

    play channel1 "audio/effect/fast_breath.mp3" volume 0.45 fadein 0.8
    with vpunch
    
    d horny3 "\"잠깐, 하으으으읏!!\"" id c03_0352
    
    "자지를 강하게 자극당한 류호는 다리를 부들부들 떨면서 사정을 참았다. 지금 슬릿 밖으로 남근이 나와야 구슬을 빼기 편해진다." id c03_0353

    d "\"천천히 빼 주게. 흡! 끄으으...\"" id c03_0354

    play sound "effect/sticky.mp3" volume 0.65
    hide dragon_s1_05_1
    show dragon_s1_07 :    
        zoom 1.3
        yoffset 160
    with dissolve
    hide dragon_s1_ball
    show dragon_s1_08 :    
        zoom 1.3
        yoffset 160
    with dissolve    
    
    "[pl_name][josa_i_ga] 축축해진 팔을 빼내자, 류호의 자지가 쑤욱 빠져나왔다." id c03_0355

    play sound "effect/ball_bouncing.mp3" volume 0.7
    show dragon_s1_ball :
        zoom 1.65
        yoffset 290
    with dissolve
    hide dragon_s1_ball
    show dragon_s1_ball2 :
        zoom 1.7
        yoffset 290
    with dissolve
    

    scene bg dragon_s1_back :
        zoom 1.08
        yoffset 80
        ease 1.5 zoom 1.00 yoffset 0 xoffset 0
    show dragon_s1_08 :
        zoom 1.3
        yoffset 160
        ease 1.5 zoom 1.0 yoffset 0 xoffset 0
    show dragon_s1_ball2 :
        zoom 1.7
        yoffset 290
        ease 1.5 zoom 1.09 yoffset 30 xoffset 30
    
    "거의 동시에 슬릿에서 구슬이 퐁 하고 빠져나와 바닥에 떨어졌다."  id c03_0356
    
    d horny3 nake_d "\"하으윽!!\"" id c03_0357
  
    play sound "audio/effect/sqz1.mp3" volume 0.7
    pause 0.1
    hide dragon_s1_ball2
    show dragon_s1_09 
    show dragon_s1_ball2 :
        zoom 1.09
        yoffset 30 xoffset 30
    with dissolve    
    with vpunch
    play sound "audio/effect/sqz2.mp3" volume 0.7
    pause 0.5
    with vpunch
    with vpunch
    
    "류호는 결국 참지 못하고 정액을 분출하기 시작했다." id c03_0358
    
    d horny3 nake0_d "\"그으으으...\"" id c03_0359
    
    "꾸덕꾸덕한 액체가 바닥으로 왈칵 쏟아진다. 류호는 숨을 내쉬며 정액이 흐르도록 내버려두었다." id c03_0360
    
    "오랫동안 싸지 않았던 탓인지 찐득한 액이 꿀럭꿀럭 나왔다." id c03_0361

    play sound "audio/effect/slow_breath.mp3" volume 0.6

    hide dragon_s1_ball2
    show dragon_s1_10
    show dragon_s1_ball2 :
        zoom 1.09
        yoffset 30 xoffset 30
    with dissolve
    with hpunch
    
    "류호는 사정의 여운에 헐떡이며 몸을 떨었다." id c03_0362

    

    "[pl_name][josa_eun_neun] 진한 정액 냄새에 약간 얼떨떨했다. 류호가 싸버리는 걸 보게 될 줄은 몰랐다." id c03_0363
    
    "스승님의 무너진 모습도 놀랍긴 하지만, 지금은 열심히 움직인 팔이 피곤해서 빨리 쉬고 싶어졌다." id c03_0364
    
    c "(일단 끈적한 것부터 씻어야겠다.)" id c03_0365
    
    "류호는 절정의 여운에서 벗어나지 못한 채 그대로 무너졌다." id c03_0366

    play sound "audio/effect/body_fall.mp3"  volume 0.8

    scene bg home
    with Fade(0.8, 0.8, 0.8)

    show dragon horny3 nake_u
    with dissolve

    $ unlock_character_image("dragon", "dragon b_no nake_d")
    $ display_text = _("이미지 : 류호(발기)")
    show screen affection_indicator
    
    c talk "\"그럼 오늘은 주무세요. 저는 다른 방에서 잘게요.\"" id c03_0367

    scene bg shop2f
    with Fade(0.8, 0.8, 0.8)
    
    "류호에게 뒤처리를 맡기고 [pl_name][josa_eun_neun] 방에서 나갔다. 류호는 쾌락에 푹 빠져있어서 [pl_name][josa_i_ga] 뭐라고 했는지 듣지도 못했다." id c03_0368
    
    "[pl_name][josa_eun_neun] 류호를 자신의 방에서 재우고, 자신은 가헬의 방에서 자기로 했다. 내일은 가헬도 돌아올 테고, 할 일도 많이 남아있다." id c03_0369
    
    c "(오늘은 푹 자자...)" id c03_0370
    
    "결심이 무색하게 [pl_name][josa_eun_neun] 그날 밤에 잠을 설쳤다." id c03_0371

label magic_shop_elred:

    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    "다음 날 아침, [pl_name][josa_eun_neun] 푹 잠들지 못해서 피곤한 상태로 영업준비를 했다. 류호의 얼굴을 보기가 조금 껄끄러웠다." id c03_0372

    play sound "effect/footstep.mp3" volume 0.85
    
    "청소를 끝내고 물약을 진열하는 도중에 발소리가 들렸다." id c03_0373

    show dragon base_out out_d
    with dissolve
    
    "류호가 1층으로 내려왔다. 류호의 얼굴은 [pl_name][josa_wa_gwa] 대조적으로 반짝반짝 윤이 났다." id c03_0374
    
    c talk "\"아, 스승님.\"" id c03_0375

    show dragon talk_out out_u
    with dissolve
    
    d "\"잘 잤소? 어제보다 더 피곤해 보이네만.\"" id c03_0376

    show dragon base_out out_d
    with dissolve
    
    c ddam2 "\"아하하, 뭐...\"" id c03_0377
    
    "[pl_name][josa_eun_neun] 헛웃음으로 대답했다." id c03_0378

    show dragon base_out out_u
    with dissolve
    
    show ball :
        xcenter 0.5
        ycenter 0.5
    with dissolve

    "류호는 품속에서 그 \'구슬\'을 꺼냈다." id c03_0379

    show dragon talk_out
    with dissolve
    
    d "\"이것 말인데... 자네 말대로 봉인이 맞네.\"" id c03_0380

    show dragon base_out out_d
    with dissolve
    pause 0.3
    hide ball
    with dissolve
    
    "기억이 봉인된 구슬은 마치 수정으로 만든 것처럼 보인다. 류호는 그것을 다시 품에 넣으며 말했다." id c03_0381

    show dragon talk_out out_u
    with dissolve
    
    d "\"어제는 정말 고마웠소. 이 봉인은... 조금 더 느긋하게 분석하고 다시 오겠네.\"" id c03_0382

    show dragon base_out
    with dissolve
    
    c talk "\"또 떠나시게요?\"" id c03_0383
    
    "류호는 [pl_name][josa_i_ga] 무슨 생각을 하는지 눈치챘다." id c03_0384
    
    "류호가 언제 돌아올지는 아무도 모른다. 하루가 걸릴지 1년이 걸릴지 류호 본인도 장담할 수 없다. 류호가 살아온 세월이 보통 수인들과는 다르기 때문일 것이다." id c03_0385

    show dragon talk_out
    with dissolve
    
    d "\"허허... 너무 걱정하지 말게. 그럼, 다음에 또 오겠소.\"" id c03_0386

    show dragon base_out out_d
    with dissolve

    show cloud1 at cloud_rise
    with dissolve
    show cloud2 at cloud_rise2
    with dissolve
    show cloud3 at cloud_rise3
    with dissolve

    pause 1.5
    
    hide dragon
    with dissolve

    hide cloud1
    hide cloud2
    hide cloud3
    with dissolve
    
    "류호는 특유의 문양과 함께 순간이동으로 사라졌다. 도저히 출입문을 사용하지 않는 것도 류호다운 모습이었다." id c03_0387
    
    scene bg shop with Fade(0.8, 0.8, 0.8)

    "{i}다음 날{/i}" id c03_0388

    "폭풍처럼 휩쓸고 간 류호 덕분에 정신없는 하루가 지나고, 마법 상점은 다시 평범한 일상으로 돌아왔다." id c03_0389

    show wolf am_d
    with dissolve

    "그리고 가헬도 돌아왔다. 딱 하루 자리를 비운 것뿐이지만, 가헬은 그 사이 무슨 일이 있었는지 궁금해했다." id c03_0390
    
    "[pl_name][josa_eun_neun] 류호가 가게에 찾아온 일을 (많은 부분은 생략하고) 설명했다. [pl_name]의 이야기를 듣는 가헬은 호기심으로 눈을 반짝였다." id c03_0391
    
    "류호가 떠났다는 이야기에 가헬은 아쉬움을 감추지 못하며 말했다." id c03_0392

    show wolf am_u talk
    with dissolve

    w "\"아쉽군. 가능하면 직접 만나 뵙고 싶었는데.\"" id c03_0393
    
    show wolf am_d base
    with dissolve

    c question2 "\"스승님을? 왜?\"" id c03_0394
    
    "[pl_name][josa_eun_neun] 약간 당황해서 반사적으로 반문했다. 기억을 잃은 류호를 가헬에게 소개하기는 어려울 것이다." id c03_0395
    
    show wolf am_u talk
    with dissolve

    w "\"... 너의 스승이니까.\"" id c03_0396
    
    show wolf am_d base
    with dissolve

    "가헬은 어떻게 말해야 할지 고민하다가 결국 실없는 소리를 했다. [pl_name][josa_wa_gwa] 가까운 수인이라면 당연히 알고 싶지만, 그걸 [pl_name]에게 설명할 수 없었다." id c03_0397
    
    "가헬은 급하게 주제를 돌렸다." id c03_0398
    
    show wolf am_u talk
    with dissolve

    w "\"용병단 회의에서 나온 얘기인데, 던전의 마물은 결국 기사단이 소탕했다고 하더군.\"" id c03_0399

    show wolf am_d base
    with dissolve

    "[pl_name][josa_eun_neun] 가헬이 갑자기 말을 얼버무린 게 이상했지만, 더 파고들지 않았다." id c03_0400
    
    c base "(그냥... 물어보지 말아야겠다.)" id c03_0401
    
    c talk "\"그래? 그동안 기사단장님이 못 오는 이유가 있었구나.\"" id c03_0402
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c03_0403

    play channel1 "effect/footstep.mp3" volume 0.85
    show wolf at walk (500, 1.6, 3)
    pause 0.5
    show tiger am_u laugh_am at left
    with dissolve

    t "\"하하하! 오랜만이네, [pl_name]. 내가 그립지는 않았나?\"" id c03_0404

    show tiger am_d base_am
    with dissolve

    "때마침 나타난 엘레드의 우렁찬 목소리가 가게에 쩌렁쩌렁 울려 퍼진다. 가헬은 조금 짜증난 표정이지만 엘레드에게 고개 숙여 인사를 하긴 했다." id c03_0405

    c "\"어서 오십시오, 엘레드님. 오랜만입니다.\"" id c03_0406

    #엘레드 가까이
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger smile_am at fwalk
    with Dissolve (0.2)

    c base "내가 엘레드에게 인사하자 엘레드는 나에게 가까이 다가왔다. 엘레드의 체취가 느껴질 정도로 바짝 다가오자 부담스러운 시선이 느껴진다." id c03_0407

    show tiger am_u wink_am
    with dissolve

    t "\"그동안 자네 모습을 보지 못해 너무나 힘들었다네.\"" id c03_0408

    show tiger base_am
    with dissolve

    c base "(그래봤자 일주일 아닌가?)" id c03_0409

    c talk "\"하하, 영광입니다.\"" id c03_0410

    c base "나는 마음에도 없는 말을 거의 반사적으로 내뱉었다. 엘레드의 플러팅이 아주 조금은 익숙해진 모양이다." id c03_0411

    # 엘레드 원위치
    play channel1 "effect/footstep.mp3" volume 0.85
    show tiger am_d at bwalk
    with Dissolve (0.2)

    "가헬이 두 사람 사이에 끼어들었다." id c03_0412

    show wolf am_u talk
    with dissolve

    w "\"얼굴 다 보셨으면 이만 돌아가 주십시오.\"" id c03_0413

    show wolf base
    show tiger am_u talk_am
    with dissolve

    t "\"오늘은 반슈타인 기사단의 단장으로서 중요한 용무가 있다네.\"" id c03_0414

    show tiger base_am
    with dissolve

    "엘레드는 가헬을 슬쩍 바라보고 다시 [pl_name]에게 말했다." id c03_0415

    show tiger talk_am
    with dissolve

    t "\"그런데, 사업과 관련된 얘기라서 말이지... 일개 용병이 들어도 될 내용일지는 모르겠군?\"" id c03_0416

    show tiger am_d laugh_am
    with dissolve

    "엘레드는 능글맞은 얼굴로 은근히 가헬을 무시했다. 가헬은 상대할 가치도 없다고 생각해서 입을 다물었다. 둘 사이에 아무런 대화도 없이 날카로운 시선만이 오간다." id c03_0417

    show tiger base_am
    with dissolve

    c "왜 또 이런 구도가 되는 건지 모르겠다. 나는 둘을 떼어놓기 위해 한마디 했다." id c03_0418

    menu:
        "가헬의 편을 들어준다." :
            
            $ wolf_love += 1
            $ display_text = _("가헬 호감도 변화") 
            show screen affection_indicator

            c talk "\"가헬이 저보다 가게 일을 많이 하니까, 자격은 충분하다고 생각합니다.\"" id c03_0419
  
            show wolf smile am_d
            with dissolve
            show tiger sad2_am
            with dissolve

            "[pl_name]의 말에 가헬은 조금 기쁜 듯 미소를 지었다. 엘레드는 약간 당황한 듯했지만 금방 웃음을 되찾았다." id c03_0420

            show tiger am_u talk_am
            with dissolve
  
            t "\"뭐 그렇다면야. 듣는 것 정도는 문제없겠지.\"" id c03_0421

            show wolf base
            show tiger am_d base_am
            with dissolve

        "엘레드의 기분을 맞춰준다." :

            $ tiger_love += 1
            $ display_text = _("엘레드 호감도 변화") 
            show screen affection_indicator

            c talk "\"비밀이 필요한 일이라면 어쩔 수 없지요.\"" id c03_0422

            show wolf sad_am am_d
            with dissolve
            show tiger laugh_am am_u
            with dissolve
 
            "[pl_name]의 말에 가헬의 귀는 축 처졌다. 엘레드는 크게 웃으며 가헬의 등을 팡팡 쳤다." id c03_0423
 
            t "\"크하하! 사실 그 정도는 아니라네. 자네도 그냥 같이 듣게.\"" id c03_0424

            show tiger base_am am_u
            with dissolve
            show wolf talk am_u
            with dissolve           
 
            w "\"엘레드 경은 농담 솜씨도 아주, 정말, 굉장히 뛰어나십니다.\"" id c03_0425
            show wolf base am_d
            show tiger am_d
            with dissolve
    
    c sneer "(이렇게 유치하게 싸울 줄은...)" id c03_0426
 
    "다행히 신경전은 빠르게 마무리되었다." id c03_0427
 
    show tiger am_u talk_am
    with dissolve
    
    t "\"최근에 마물과 싸울 일이 많아서 물자 소모가 심했다네. 다른 보급은 문제없지만, 회복 물약은...\"" id c03_0428
    
    t "\"음, 자네는 알지 모르겠지만 귀족들과 마탑은 사이가 좋지 못하다네.\"" id c03_0429
    
    t "\"그래서 회복 물약을 보급할 다른 방법을 고민했지. 자네의 마법 상점도 그 후보라네.\"" id c03_0430
 
    show tiger am_d base_am
    with dissolve

    c talk "\"회복 물약을 대량으로 구매하시겠다면 환영입니다. 기한은 언제까지-\"" id c03_0431
 
    "엘레드는 크게 웃으며 [pl_name]의 말을 끊었다." id c03_0432

    show tiger am_u laugh_am
    with dissolve
 
    t "\"하하하! 아직 후보라니까. 뭐, 이걸 핑계로 자네 얼굴을 한 번이라도 더 보려고 왔다네.\"" id c03_0433
    
    show tiger am_d base_am
    with dissolve

    c base "(진짜 얼굴 보려고 온 거야?)" id c03_0434
 
    "엘레드는 [pl_name]에게 윙크하며 또 플러팅을 시작했다." id c03_0435
 
    show tiger am_u wink_am
    with dissolve

    t "\"그만큼 내가 자네에게 진심이라는 것을 알아주었으면 하네.\"" id c03_0436

    show tiger am_d base_am
    with dissolve

    c talk "\"하하... 감사합니다.\"" id c03_0437
 
    "[pl_name][josa_eun_neun] 엘레드의 말을 가볍게 생각했다. 엘레드가 평소에 하던 \'미래를 약속하는 말\'도 그렇게 진심이라고 생각하지 않았다." id c03_0438
    
    "평소와 같은 반응에 엘레드는 씁쓸한 표정으로 한숨 쉬었다." id c03_0439

    show tiger am_u sad2_am
    with dissolve
 
    t "\"그래서 자네의 마음이 궁금하다네. 나를 어떻게 생각하는지... 나에게 기회는 있는지 말이야.\"" id c03_0440
 
    show tiger am_d base_am
    with dissolve

    "엘레드는 평소와는 다른 진지한 표정으로 [pl_name][josa_eul_reul] 바라보았다. 처음 보는 표정에 [pl_name][josa_eun_neun] 크게 당황했다." id c03_0441
    
    "엘레드가 아무리 진심이어도 연애를 하기엔 넘어야 할 산이 많다. 엘레드가 바람둥이인 건 물론이고, 종족에 나이에 신분까지 달라도 너무 다르다." id c03_0442
    
    "수인 사회가 개방적인 것과 별개로, [pl_name][josa_i_ga] 생각하기에 엘레드와의 연애는 험난해 보였다." id c03_0443
 
    "[pl_name]의 복잡한 표정을 본 가헬은 엘레드를 쫓아낼 생각으로 말했다." id c03_0444

    show wolf angry am_u
    with dissolve

    w "\"용무가 끝났으면 돌아가 주십시오.\"" id c03_0445

    show tiger angry_am am_u
    with dissolve 
    
    "엘레드는 가헬을 험악하게 노려보는가 싶더니 표정을 풀었다." id c03_0446

    show tiger talk_am am_d
    with dissolve 
 
    t "\"뭐, 어차피 그럴 생각이었다네. 근데 가헬군에게 할 얘기가 있어서 말이야. 잠깐만 따라 나오겠나?\"" id c03_0447

    show tiger base_am
    with dissolve 
    show wolf base am_d
    with dissolve
 
    c ddam2 "(헉! 이번엔 진짜로 귀족을 모욕했다고 잡혀가는 거 아냐?)" id c03_0448
 
    "[pl_name]의 걱정이 무색하게 두 사람은 딱히 싸우려는 기색 없이 가게 밖으로 나갔다." id c03_0449
 
    c consider "(... 내가 안 따라가도 괜찮겠지?)" id c03_0450

    stop music fadeout 2.5
 
    # [가게 밖으로 장면 전환]
    scene bg shop_outside with Fade(0.8, 0.8, 0.8)

    show tiger smile_am am_d
    with dissolve

    "가게 밖으로 나온 가헬은 엘레드의 능글맞은 미소를 마주했다." id c03_0451

    show tiger talk_am am_u
    with dissolve
 
    t "\"긴장할 필요 없네. 그냥, 연장자로서 작은 조언을 하나 하려고 하는데...\"" id c03_0452

    show tiger base_am
    with dissolve
 
    w "\"...\"" id c03_0453
 
    "가헬의 침묵을 대답으로 받아들인 엘레드는 말을 이었다." id c03_0454

    show tiger talk_am am_d
    with dissolve
 
    t "\"경비견 자리에 만족하는 게 아니라면, 지금보다는 더 적극적으로 나서야 할걸세. 누가 언제 [pl_name][josa_eul_reul] 훔쳐 갈지 걱정만 하다가는-\"" id c03_0455
 
    w talk "\"조언 감사합니다.\"" id c03_0456

    show tiger base_am
    with dissolve
 
    "가헬은 엘레드의 말을 자르며 쓸데없는 소리로 치부했다. 그러나 돌아선 가헬의 등 뒤에 꽂히는 엘레드의 말에 우뚝 서고 말았다." id c03_0457

    show tiger talk_am am_u
    with dissolve
 
    t "\"후회하는 날이 온다네. 이건 내 경험담이지. 자신의 마음을 주지 않으면서, 어떻게 다른 사람의 마음을 얻겠나?\"" id c03_0458

    show tiger base_am am_d
    with dissolve
 
    "평소의 가헬이라면 마음을 여기저기 뿌리고 다니는 엘레드보단 낫다고 받아칠 것이다. 하지만 정곡을 찌르는 엘레드의 말에 가헬의 머릿속은 복잡해졌다." id c03_0459
    
    "이번만큼은 패배를 인정한 가헬이 짧게 대답했다." id c03_0460
 
    w "\"... 명심하겠습니다.\"" id c03_0461
 
    "호탕하게 웃는 엘레드를 뒤로 하고 가헬은 가게로 다시 들어갔다." id c03_0462
 
    # 가게로 배경 전환
    scene bg shop with Fade(0.8, 0.8, 0.8)
    play music "audio/sad-soul-chasing-a-feeling-185750.mp3" fadein 2.5 volume 0.60
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c03_0463

    show wolf sad_am
    with dissolve
 
    "가헬이 문을 열자 멍하니 딴생각에 빠져있던 [pl_name][josa_i_ga] 화들짝 놀랐다." id c03_0464
 
    c talk "\"앗, 금방 왔네? 또 서로 으르렁거린 건 아니지?\"" id c03_0465

    show wolf sad2_am am_u
    with dissolve
 
    w "\"... 별일 없었다.\"" id c03_0466

    show wolf sad_am am_d
    with dissolve
 
    c "\"그러면 다행이고... 근데 표정이 별로 안 좋은데.\"" id c03_0467

    show wolf sad3_am
    with dissolve
 
    "가헬은 엘레드의 조언을 곱씹으며 [pl_name][josa_eul_reul] 바라보았다." id c03_0468

    "이대로는 정말 계약기간을 다 채우고 그냥 헤어지게 될지도 모른다. 그렇지만 엘레드처럼 들이대는 건 더욱 승산이 없다고 가헬은 생각했다." id c03_0469

    show wolf sad2_am am_u
    with dissolve
 
    w "\"그냥 조금 지쳐서 그렇다. 오늘은... 조금 쉬어도 될까?\"" id c03_0470

    show wolf sad_am am_d
    with dissolve
 
    c "\"그래. 가게 일은 너무 무리하지 마.\"" id c03_0471
 
    c consider "(별일이네.)" id c03_0472
 
    "[pl_name][josa_i_ga] 쉬라고 해도 듣지 않던 가헬이 나서서 쉬겠다고 하는 날이 올 줄은 몰랐다." id c03_0473

    show wolf sad2_am am_u
    with dissolve
 
    w "\"잠시... 나갔다 올게.\"" id c03_0474

    show wolf sad_am am_d
    with dissolve
 
    "[pl_name][josa_eun_neun] 군말 없이 가헬을 배웅했다. [pl_name][josa_i_ga] 보기에도 가헬은 휴식이 필요했다." id c03_0475

label tavern_talk:
    
    # 길거리 배경 전환
    scene bg street with Fade(0.8, 0.8, 0.8)

    "길거리에 나선 가헬은 무작정 걷기 시작했다. 화창한 날씨에 아름답게 빛나는 길거리는 가헬의 눈에 들어오지 않았다. 가헬에게 필요한 건 몸보다 마음의 휴식이었다." id c03_0476

    w sad_am "(후회, 후회라...)" id c03_0477
    
    "사실 몇 달 전까진 이렇게 되리라 상상하지도 못했다." id c03_0478
    
    "[pl_name][josa_eun_neun] 가헬을 전혀 알아보지 못했지만, 가헬은 용병 길드에서 [pl_name][josa_eul_reul] 다시 만나자마자 한눈에 알아볼 수 있었다." id c03_0479
    
    "어른이 된 [pl_name][josa_i_ga] 살아 숨 쉬는 게 믿기지 않았다." id c03_0480
    
    w "(12년 전 보육원 사고에서 살아남은 수인은 아무도 없는 줄 알았는데...)" id c03_0481
    
    "그 사고를 떠올리기만 해도 머리가 지끈거린다. [pl_name]에게 과거의 보육원 얘기를 꺼내기도 조심스러웠다." id c03_0482
    
    "가헬 본인도 떠올리고 싶지 않은 사건인데, 혹여나 [pl_name]의 상처를 후벼파는 짓은 하고싶지 않았다." id c03_0483
    
    "어쩌면 [pl_name][josa_eun_neun] 너무 큰 충격을 받아서 자신을 잊어버렸을지도 모른다." id c03_0484
    
    w sad2_am "\"휴...\"" id c03_0485
    
    "가헬은 한숨을 쉬며 부정적인 생각을 떨쳐냈다. 지금 신경 써야 할 일은 현재의 [pl_name][josa_ida_da]." id c03_0486
    
    "[pl_name][josa_wa_gwa] 연인이 되는 상상을 하자 가슴이 울렁거렸다." id c03_0487
    
    "조금만 손을 뻗으면 닿을 것 같기도 하고, 영영 닿을 수 없는 곳에 있는 것 같기도 했다." id c03_0488
    
    "복잡한 머릿속에 가헬의 인상은 저절로 심각해졌다. 지나가는 수인들은 가헬의 흉흉한 기세에 알아서 비켜 갔다." id c03_0489
    
    w sad_am "(나는, 어떻게 해야 하지...)" id c03_0490
    
    "[pl_name]에 대한 욕심이 없는 건 아니지만, 동시에 지금의 관계를 잃고 싶지 않다. 가헬은 정답 없는 생각에 깊이 빠져있다가 술집 앞까지 왔다." id c03_0491

    stop music fadeout 2.5
    
    # [술집으로 배경 전환]
    scene bg pub with Fade(0.8, 0.8, 0.8)
    play music "medieval-fantasy-142837.mp3" volume 0.5  fadein 2.5
    
    $ unlock_info_tag(2, "3")
    $ display_text = _("정보 : 술집")
    show screen affection_indicator

    "{color=#ee3939}'술집'{/color}은 용병들이 술을 퍼마시는 것 이외에도 식사나 숙박을 해결하러 오는 곳이기도 하다." id c03_0492
    
    "지금은 북적이는 시간대가 아니지만, 밤에는 다양한 수인들이 잔뜩 모여 떠들썩해진다." id c03_0493
    
    "오크통, 술, 그릴과 음식 냄새가 아주 전형적인 술집의 향기다. 익숙한 공간의 냄새가 가헬의 마음을 아주 조금은 가볍게 했다." id c03_0494
    
    "테이블을 지나 카운터에 가까이 가자 익숙한 수인이 가헬에게 말을 걸었다." id c03_0495

    show lucas talk am_u
    with dissolve
    
    l "\"가헬님? 여기서 뵙는군요.\"" id c03_0496

    show lucas base am_d at right
    show bear at left
    with dissolve
    
    "바에는 길드 접수원 루카스와 바토가 앉아있었다. 가헬과 루카스는 용병 길드에서 몇 번씩 본 사이라서 간단하게 인사했다." id c03_0497
    
    w talk "\"안녕하십니까, 루카스 씨.\"" id c03_0498
    
    "그리고 가헬은 바토 쪽을 바라보았다. 언제 한번 본 것 같지만, 잘 모르는 수인이라 어색하게 눈을 마주쳤다." id c03_0499
    
    show lucas talk am_u
    with dissolve

    l "\"가헬님, 이쪽은 바토님입니다. 마탑 소속 마법사이십니다. 바토님, 이쪽은 가헬님입니다. 칼루리엔 용병단 소속 용병이죠.\"" id c03_0500
    
    show lucas base am_d
    with dissolve

    w base "(아, [pl_name][josa_i_ga] 말했던 마탑의 지인이 이 수인이군...)" id c03_0501
    
    w talk "\"[pl_name]에게 얘기 들었습니다. 공증받는 데 도움을 주셨다고.\"" id c03_0502
    
    "바토는 작게 놀라면서 고개를 끄덕였다." id c03_0503

    show bear happy
    with dissolve
    
    b "\"앗, 형이 얘기했었군요. 헤헤...\"" id c03_0504

    show question :
        zoom 0.7
        xalign 0.07
        yalign 0.8
    
    w base "(형? 생각보다 더 친한 사이인가?)" id c03_0505

    hide question
    pause 0.01
    show bear base
    with dissolve
    
    "가헬은 마음속에서 생겨나려는 질투심을 억눌렀다. 엘레드의 조언 때문에 자꾸만 마음이 조급해지는 것 같았다." id c03_0506
    
    "가헬은 간단하게 다른 화제를 꺼냈다." id c03_0507
    
    w talk "\"루카스 씨는 웬일로 술집에 오셨습니까?\"" id c03_0508
    
    "루카스는 특유의 부드러운 미소를 지으며 대답했다." id c03_0509
    
    show lucas talk am_u
    with dissolve

    l "\"마탑에서 용병 길드에 협조 요청을 보냈습니다. 그런데 오늘은 제가 쉬는 날이라 길드 밖에 있었습니다. 바토님을 만나러 술집으로 오게 된 것입니다.\"" id c03_0510

    show lucas base am_d
    with dissolve

    show question :
        zoom 0.7
        xalign 0.07
        yalign 0.8
    
    w base "(휴일인데 일 얘기를 하러...?)" id c03_0511

    hide question
    
    "가헬의 생각을 읽기라도 한 듯, 바토는 빠르게 변명을 붙였다." id c03_0512

    show bear talk am_u
    with dissolve
    
    b "\"내일 다시 오겠다고 했는데, 거기 직원분이 술집에서 기다리라고 해서...\"" id c03_0513

    show bear base am_d
    show lucas talk am_u
    with dissolve

    l "\"괜찮습니다. 어차피 본격적인 업무는 내일부터 시작하니까요.\"" id c03_0514
    show lucas base am_d
    with dissolve

    w talk "\"마탑에서 용병 길드에 요청할 정도의 일... 최근에 그런 일이 있었습니까?\"" id c03_0515
    
    "가헬의 질문에 루카스는 작은 종이를 꺼내 눈으로 훑었다. 바토와 얘기하며 메모한 내용이었다." id c03_0516

    #강철손 상회 정보 키워드 추가
    $ unlock_info_tag(2, "4")
    $ display_text = _("정보 : 강철손 상회")
    show screen affection_indicator
    
    show lucas talk page_u
    with dissolve

    l "\"성도 주변에서 갑자기 세력을 키운 {color=#ee3939}\'강철손 상회\'{/color}에 대한 조사 의뢰입니다.\"" id c03_0517
    
    l "\"마탑에선 이 상회를 범죄 조직으로 의심하고 있더군요. 마탑에서 금지한 마법을 반복적으로 사용한 것으로 추정 중입니다.\"" id c03_0518
    
    l "\"길드에서는 이들에 대한 소문부터 증언까지 다양한 정보를 모을 예정입니다.\"" id c03_0519
    
    show lucas base am_d
    with dissolve

    w talk "\"음... 강철손 상회... 저는 들어본 적 없습니다.\"" id c03_0520

    show bear talk am_u
    with dissolve
    
    b "\"최근에서야 본격적으로 활동하기 시작한 것 같아요.\"" id c03_0521

    show bear base am_d
    with dissolve
    
    "대화가 끝나자 살짝 어색한 분위기가 세 사람을 감싼다." id c03_0522

    #에일 이미지 추가
    show beer :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    $ unlock_info_tag(2, "5")
    $ display_text = _("정보 : 에일")
    show screen affection_indicator

    "가헬은 술집에 온 목적을 떠올리고 {color=#ee3939}'에일'{/color} 한 잔을 주문했다." id c03_0523

    hide beer
    with dissolve
    
    show lucas talk am_u
    with dissolve

    l "\"그러고 보니 가헬님은 휴식하러 오셨겠군요. 시간을 뺏어 죄송합니다.\"" id c03_0524
    
    show lucas base am_d
    with dissolve

    w talk "\"괜찮습니다.\"" id c03_0525
    
    "바토와 루카스는 정말로 대화만 하러 온 것인지, 두 사람 앞에는 음료도 없이 작은 간식만 한 접시 덩그러니 놓여있었다." id c03_0526

    #접시위의 햄과 치즈 넣기
    show ham_cheese :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    "예쁘게 장식된 햄과 치즈는 꽤 고급품이었다. 그마저도 거의 먹지 않았는지 그대로 남아있었다." id c03_0527
    
    w base "(소금 비스킷을 두고 저걸 시키다니, 입맛이 고급인가? 마탑 소속 마법사들은 부자라더니...)" id c03_0528

    hide ham_cheese
    with dissolve
    
    "가헬은 술의 맛을 즐길 새도 없이 에일을 쭉 들이켰다. 곧바로 한 잔 더 주문하는 가헬을 보고 루카스는 조심스레 말을 꺼냈다." id c03_0529
    
    show lucas talk am_u
    with dissolve

    l "\"가헬님, 뭔가 고민이라도 있으신가요?\"" id c03_0530
    
    show lucas base am_d
    with dissolve

    w "\"......\"" id c03_0531

    menu :
        "고민을 이야기 한다." :

            $ talk_Gahel_worry = True

            w talk "\"별일은 아니고, 친구가 힘들어하길래 걱정이 돼서 그렇습니다. 친구가 좋아하는 수인이 너무 인기가 많아서 힘들다더군요.\"" id c03_0532
    
            "가헬은 자신의 얘기를 살짝 돌려서 말했다. 루카스와 바토는 흥미진진한 이야기에 귀를 쫑긋 세웠다." id c03_0533
            
            w "\"그 친구는 당장이라도 고백하고 싶어 하지만, 거절당할까 봐 고민하고 있습니다.\"" id c03_0534

            play sound "effect/boing.mp3" volume 0.9
            show question at question_move (380, 70)
            
            "바토는 뭔가 의문이 들어서 가만히 생각해 보았다." id c03_0535
            
            b "(지금... 가헬씨 본인 이야기 아닌가?)" id c03_0536

            play sound "effect/sparkle.mp3" volume 0.5
            hide question
            show bear sparkle
            with dissolve
            
            "그런 생각이 들자, 가헬의 얘기가 너무나 궁금해졌다. 바토는 침을 꿀꺽 삼키고 가헬의 다음 말을 기다렸다." id c03_0537
            
            w "\"게다가 어떤 기사는 이미 거절당했다고 하더군요.\"" id c03_0538
            
            "가헬은 은근슬쩍 자신의 희망 사항을 사실인 것처럼 살짝 바꿔서 말했다." id c03_0539

            show bear base
            with dissolve
            
            show lucas talk am_u
            with dissolve
            
            l "\"그럴 수가. 정말 안타까운 일입니다.\"" id c03_0540

            show lucas base am_d
            with dissolve

        "고민을 이야기 하지 않는다." :

            w talk "\"조금 피곤해서 그렇지, 별일 없었습니다.\"" id c03_0541
   
    #벌꿀 사과주 이미지

    show honey_ale :
        xcenter 0.5
        ycenter 0.5
    with dissolve
    
    $ unlock_info_tag(2, "6")
    $ display_text = _("정보 : 벌꿀 사과주")
    show screen affection_indicator

    "가헬의 말을 듣던 루카스는 갑자기 심각한 표정이 되더니 {color=#ee3939}'벌꿀 사과주'{/color}를 주문했다. 달달하지만 은근히 도수가 높은 술이라 많이 마시면 더 빠르게 취하는 술이다." id c03_0542

    hide honey_ale
    with dissolve
    
    if talk_Gahel_worry == True :
        "루카스는 술을 홀짝이다가 입을 열었다." id c03_0543
        
        show lucas talk am_u
        with dissolve
        
        l "\"그래도, 용기있게 고백하는 편이 낫지 않을까요? 안 하고 후회하는 건 평생 간다고 하잖아요.\"" id c03_0544
        
        show lucas base am_d
        with dissolve
        
        w "\"역시 그렇습니까...\"" id c03_0545
        
        "엘레드와 비슷한 조언에 가헬의 마음은 더 복잡해졌다. 경험에서 나오는 조언인 건 알지만, [pl_name]에게 거절당하고 싶지는 않았다." id c03_0546
        
        "가헬이 고민하는 사이 루카스는 술을 한번에 쭉 들이키고 말했다." id c03_0547
        
        show lucas talk am_u
        with dissolve

        l "\"사실 제가 조언할 입장은 아닙니다만... 휴우우...\"" id c03_0548

        show lucas base am_d
        with dissolve

    else :
        "루카스는 술을 연신 홀짝였다." id c03_0549
    
    "루카스는 깊은 한숨을 내쉬고 우울한 표정을 지었다. 친절하고 부드러운 모습만 보여주던 루카스의 처음 보는 모습에 가헬은 약간 놀랐다." id c03_0550
    
    "바토는 조심스레 루카스에게 말을 걸었다." id c03_0551

    if talk_Gahel_worry == True :
        
        show bear talk am_u
        with dissolve
        
        b "\"루카스씨도 뭔가 고민이 있으신가 봐요.\"" id c03_0553

        show bear base am_d
        with dissolve
    else :
        
        show bear talk am_u
        with dissolve
        
        b "\"뭔가 고민이 있으신가 봐요.\"" id c03_0554

        show bear base am_d
        with dissolve

    show lucas talk am_u
    with dissolve

    l "\"그게...\"" id c03_0555
    
    show lucas base am_d
    with dissolve

    scene bg pub with Fade(0.8, 0.8, 0.8)

    "{i}잠시 후{/i}" id c03_0556

    show bear at left
    with dissolve
    show lucas sad at right
    with dissolve
    
    l "\"흐어어엉... 어떻게 그렇게 매정하게 차버릴 수 있어...\"" id c03_0557
    
    show lucas sad2
    with dissolve

    "술이 약간 들어가자마자 루카스는 다른 사람처럼 변했다." id c03_0558
    
    "최근에 연인에게 이별을 통보받은 얘기를 시작으로, 도저히 루카스의 말을 멈출 수가 없었다. 루카스는 굵은 눈물을 뚝뚝 흘리며 연거푸 술잔을 기울였다." id c03_0559
    
    "술이 들어갈 수록 점점 감정적으로 변하면서 했던 말을 반복하기 시작했다. 가헬과 바토는 난감한 상황에 식은땀을 흘리며 루카스를 말렸다." id c03_0560
    
    w talk "\"저, 루카스씨. 술은 그만 드시는 게 좋을 것 같습니다.\"" id c03_0561
    
    show lucas sad am_u
    with dissolve

    l "\"그렇죠. 접수원 월급이 넘쳐나는 건 아니니까... 그, 그 녀석은 내가 월급쟁이라서 싫었을까? {i}*훌쩍훌쩍*{/i}\"" id c03_0562
    
    show lucas sad2 am_d
    with dissolve

    "도저히 끝나지 않을 것 같은 술주정에 바토는 대책을 궁리했다. 떠오른 생각을 가헬에게 귓속말했다." id c03_0563

    show bear embrass3 am_u
    show ddam at ddam_move (320,75)
    with dissolve
    
    b "\"제가 숙박용 방을 하나 빌릴게요. 거기서 한숨 자게 하죠.\"" id c03_0564

    hide ddam
    show bear base am_d
    with dissolve
    
    "가헬은 바토의 제안에 고개를 끄덕였다. 이대로 술주정을 들어주다간 내일 아침이 밝을 지경이었다." id c03_0565

    hide bear
    with dissolve
    
    "바토가 슬그머니 자리에서 일어나는 걸 보고, 가헬은 루카스의 상태를 확인했다." id c03_0566
    
    show lucas drunk
    with dissolve

    l "\"으음... 나쁜 하이에나... 내 마음도 훔쳐가고...\"" id c03_0567
    
    "루카스는 헛소리를 중얼거리며 졸고 있었다. 눈앞에 손을 흔들어도 전혀 반응이 없었다." id c03_0568
    
    w base "(차라리 잘 됐군...)" id c03_0569

    scene bg black with Fade(0.8, 0.8, 0.8)
    
    "마침 바토가 돌아와서 3번 방을 가리켰다." id c03_0570
    
    "두 사람은 루카스를 질질 끌어서 침대에 던졌다. 루카스는 다행히 푹 잠든 것 같다." id c03_0571

    scene bg pub with Fade(0.8, 0.8, 0.8)

    show bear
    with dissolve
    pause 0.5
    play sound "audio/effect/sigh.mp3" volume 0.23
    show sigh at mirror, sigh_move2 (75, -120)
    show bear sigh
    with dissolve

    "술 마시던 자리에 돌아온 가헬과 바토는 긴장이 풀려서 숨을 푹 내쉬었다." id c03_0572

    show bear laugh am_u
    with dissolve
    
    b "\"하하... 처음으로 \'진짜\' 술집을 경험한 것 같네요.\"" id c03_0573

    show bear base am_d
    with dissolve
    
    w talk "\"가능하면 모르는 게 나았을 겁니다.\"" id c03_0574

    show bear smile
    with dissolve
    
    "소소한 농담을 주고받은 두 사람은 진이 빠져 허탈한 웃음을 흘렸다." id c03_0575

    show bear talk am_u
    with dissolve
    
    b "\"아참, 방 값을 내면서 술도 전부 계산했어요.\"" id c03_0576

    show bear base
    with dissolve
    
    w "\"음? 한두 푼이 아니었을 텐데... 다음엔 제가 대접하겠습니다.\"" id c03_0577
    
    w "(하긴 부자에겐 푼돈일지도 모르겠군.)" id c03_0578

    show bear talk am_d
    with dissolve
    
    if talk_Gahel_worry == True :
        b "\"가헬씨도 힘내세요. 다음에 또 봐요.\"" id c03_0579

        show bear base
        with dissolve
        
        "가헬의 연애 이야기를 기억하고 있던 바토는 의미심장한 말을 남기고 갔다." id c03_0580

        hide bear
        with dissolve
        
        "가헬은 단순히 루카스의 술주정 뒷처리 때문이라고 생각했다." id c03_0581

    else :
        b "\"다음에 또 봐요.\"" id c03_0582

        hide bear
        with dissolve
    
    "연인에게 헌신적인 루카스도 실연당하는 것을 보면, 역시 연애는 모두 어려워하는 것 같다." id c03_0583
    
    "딱히 감정 정리에 도움이 되지 않았지만, 마음은 약간 편해졌다." id c03_0584
    
    "마지막으로 에일을 한 잔 더 마시고 가헬도 술집을 나갔다." id c03_0585

    play sound "effect/door.mp3" volume 0.9

    pause 2.8

    stop sound fadeout 2.5
    stop music fadeout 2.5

label chapter3_end:
    
    scene bg shop2 with Fade(0.8, 0.8, 0.8)
    play music "audio/eco-technology-145636.mp3" fadein 2.5 volume 0.40

    "[pl_name][josa_eun_neun] 영업을 마칠 시간까지 일을 하면서도 엘레드 생각에 머릿속이 복잡했다. 앞으로 엘레드를 어떻게 대해야 할지 결심이 서지 않았다." id c03_0586
    
    "괜히 책을 펼쳐서 눈에 들어오지도 않는 글자를 읽다가, 페이지를 너무 세게 잡아서 찢어버릴 뻔했다." id c03_0587
    
    "말린 약초는 잡는 족족 으스러지는 바람에 손에 묻은 가루를 닦느라 고생했다." id c03_0588
    
    "[pl_name][josa_eun_neun] 영업을 마치고 상품을 정리하다가 손에 손톱자국이 난 걸 발견했다. 그제서야 손이 저릴 정도로 주먹을 꽉 쥐고 있었다는 걸 깨달았다." id c03_0589
    
    c sigh "(차라리 나도 가헬이랑 같이 쉬러 나갈걸 그랬나.)" id c03_0590
    
    play sound "audio/effect/bell.mp3" volume 0.6
    "{i}딸랑~{/i}" id c03_0591

    show wolf sad3_am
    with dissolve
    
    "마침 가헬이 가게로 돌아왔다. [pl_name][josa_eun_neun] 가헬의 얼굴을 보고 깜짝 놀랐다. 생각보다 일찍 돌아온 건 물론이고, 힘없이 축 처진 표정은 가헬답지 않았다." id c03_0592
    
    c talk "\"일찍 왔네? 무슨 일 있었어?\"" id c03_0593

    show wolf talk am_u
    with dissolve
    
    w "\"별일 없었다...\""  id c03_0594

    show wolf base
    with dissolve

    w "\"...\""  id c03_0595
    
    show wolf talk
    with dissolve

    w "\"사실 술집에서 루카스씨가 과음을 해서 작은 소동이 있긴 했다.\"" id c03_0596

    show wolf base
    with dissolve
    
    c "\"그 루카스씨? 별일 맞네.\"" id c03_0597

    show wolf talk am_d
    with dissolve
    
    w "\"아무튼, 덕분에 잘 쉬었다.\"" id c03_0598
    
    show wolf base
    with dissolve

    "전혀 잘 쉰 표정이 아니었지만, 가헬은 2층으로 올라갔다." id c03_0599

    show wolf at mirror
    with dissolve
    play sound "effect/footstep.mp3" volume 0.85
    show wolf at walk (1500, 2.8, 5)
    pause 2
    
    c base "(가헬도 신경쓰이네...)" id c03_0600
    
    c "가헬이 무슨 생각을 하는지 잘 모르겠지만, 상태가 저런 것은 뭔가 엘레드와 관련이 있는 것 같다. 가헬은 엘레드와 별일 없었다고 했지만, 아무래도 아닌것 같다." id c03_0601
    
    c sigh "어떻게 해결해야 할지 난감한 문제에 골치가 아프다. 나는 인간관계가 넓지 않아서 누구한테 물어보기도 마땅치 않다. 가헬과 엘레드를 제외하면 가까운 수인은 류호 스승님 정도..." id c03_0602
    
    c question2 "(그러고 보니 스승님은 괜찮으려나?)" id c03_0603
    
    c base "류호는 나에 대한 기억은 잃었을지언정, 인생의 경험을 잃지는 않았을 것이다." id c03_0604
    
    c "조언을 받을 수 있을지는 모르겠지만, 시도 해볼 가치는 있다." id c03_0605
    
    c "류호가 언제 돌아올지 모르는 게 문제일 뿐이다." id c03_0606

    c sigh "(어휴. 정말 쉬운 일이 하나도 없네.)" id c03_0607

    scene bg black with Fade(0.8, 0.8, 0.8)

    "[pl_name][josa_eun_neun] 뻑뻑한 눈을 비비며 잘 준비를 했다. 최근에 수면이 부족했던 탓도 있고, 생각을 많이 해서 그런지 유난히 피곤했다." id c03_0608
    
    "[pl_name][josa_eun_neun] 눈을 감자마자 깊은 잠에 빠져들었다." id c03_0609
    
    "다음 날부터 무슨 일이 벌어질지 상상도 하지 못하고..." id c03_0610

    stop music fadeout 2.5

    jump routechoice