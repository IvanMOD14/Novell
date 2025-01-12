label chapter4_dream :

    transform w4c_anchor :
        align (0.5, 0.32)
        anchor (0.5, 0.32)
        zoom 1

    transform w4c_moving :
        ease 1.5 xoffset 15 yoffset -12
        ease 1.5 xoffset -12 yoffset 12
        repeat

    transform w4c_moving2 :
        ease 1.7 xoffset -10 yoffset -8
        ease 1.7 xoffset 10 yoffset 8
        repeat

    transform w4c_moving3 :
        ease 1.3 xoffset 25 yoffset -15
        ease 1.3 xoffset -25 yoffset 15
        repeat

    transform w4c_moving4 :
        ease 1.8 xoffset -25 yoffset -20
        ease 1.8 xoffset 25 yoffset 20
        repeat

    transform w4c_moving5 :
        ease 1.3 xoffset 18 yoffset -10
        ease 1.3 xoffset -18 yoffset 10
        repeat

    transform w4c_moving6 :
        ease 0.35 yoffset 18
        ease 0.75 yoffset 0
        repeat
    
    transform w4c_moving7 :
        ease 1.45 xoffset -15 yoffset -12
        ease 1.45 xoffset 15 yoffset 12
        repeat

    transform w4c_zoom (time, time2, add) :
        ease time zoom 1
        ease time2 zoom add


    # 꿈속 공간
    scene bg fantasy5 at w4c_anchor, w4c_moving
    show fantasy4 at w4c_anchor, w4c_moving2
    show fantasy3 at w4c_anchor, w4c_moving3
    show fantasy2 at w4c_anchor, w4c_moving4
    show fantasy at w4c_anchor, w4c_moving5
    show fantasy_dust at w4c_anchor, w4c_moving7
    play music "solitude-dark-ambient-electronic-197737.mp3" volume 0.55 fadein 2.5
    with Fade(0.8, 0.8, 0.8)

    "..." id c04d_0000

    "꿈속에서 [pl_name][josa_eun_neun] 천천히 걷고 있었다." id c04d_0001
    
    show cara at w4c_moving6
    with dissolve

    "자신이 왜, 어디로 걷고 있는 건지는 모르겠지만 그냥 걷고 있었다." id c04d_0002

    "주변 풍경은 울렁거리며 이상하게 움직이고 있었다." id c04d_0003

    "[pl_name][josa_eun_neun] 계속해서 앞으로 나아갔다." id c04d_0004

    n "\"나...\"" id c04d_0005

    "누군가가 [pl_name]의 귓가에 속삭였다." id c04d_0006
    
    "물속에서 소리를 듣는 것처럼 먹먹하게 들렸다." id c04d_0007
    
    "[pl_name][josa_eun_neun] 몸이 점점 무거워지는 기분이 들었다." id c04d_0008

    n "\"나에게...\"" id c04d_0009

    "속삭임이 자꾸만 반복되어 울린다." id c04d_0010
    
    "[pl_name][josa_eun_neun] 눈꺼풀까지 무거워져서 결국 눈을 감았다." id c04d_0011

    show cara sleep :
        yoffset 9
    with Dissolve (0.2)

    "팔다리도 움직일 수 없었다. 보이지 않는 손이 붙잡은 것 같았다." id c04d_0012

    show fantasy at w4c_moving5, w4c_zoom (0, 1.5, 3)
    show fantasy2 at w4c_moving4, w4c_zoom (0.1, 1.5, 5)
    show fantasy3 at w4c_moving3, w4c_zoom (0.3, 2, 9)
    show fantasy4 at w4c_moving2, w4c_zoom (0.45, 2.5, 16)
    show bg fantasy5 at w4c_moving, w4c_zoom (0, 4, 1.2)
    show cara :
        ease 4 zoom 0.65
    with dissolve
   
    pause 4
    show cara at w4c_moving2

    "밟고 있던 지면이 온데간데없이 사라져버리고, [pl_name][josa_eun_neun] 왠지 허공에 둥둥 떠있었다." id c04d_0013

    "어쩌면 자신이 공중으로 날아오른 걸지도 모른다." id c04d_0014

    "주변은 한번도 본 적 없는 이상한 풍경이었다. 밤하늘과 비슷하지만 바다처럼 일렁이고 있었다." id c04d_0015
    
    n "\"... 바쳐라.\"" id c04d_0016
    
    "속삭임은 점점 커지면서 사방에서 반복적으로 중얼거리고 있었다." id c04d_0017

    "[pl_name][josa_eun_neun] 조금 어지러운 기분이 들었다." id c04d_0018

    "자신의 몸이 위에서 아래로 떨어지는지, 아래에서 위로 솟구치는지 알 수 없었다." id c04d_0019
    
    "갑자기 [pl_name][josa_eun_neun] 이게 꿈이라는 걸 알아챘다." id c04d_0020
    
    "가끔 피곤하면 이런 일이 있었다." id c04d_0021
    
    "[pl_name][josa_eun_neun] 어떻게든 손가락이라도 움직여보려고 했다." id c04d_0022

    "아무튼 몸을 움직일 수 있게 되면 악몽에서 깨어날 수 있을 것이다." id c04d_0023
    
    "누군가의 중얼거림은 점점 격렬해져서 이제는 시끄럽게 느껴졌다." id c04d_0024
    
    n "\"나에게 운명을 바쳐라.\"" id c04d_0025

    stop music fadeout 2.0
    
    scene bg home with Fade(0.2, 0.3, 0.6, color="#fff")
    
    play sound "audio/effect/crash.mp3" volume 0.45
    show cara hurt inn_d at change(1, 0, 300)
    with vpunch

    c "\"윽!! 아이고...\"" id c04d_0026
    
    show cara sigh
    with dissolve

    "[pl_name][josa_eun_neun] 충격에 퍼뜩 잠에서 깼다." id c04d_0027
    
    show cara base
    with dissolve

    "침대에서 반쯤 미끄러진 자세로 깨어난 [pl_name][josa_eun_neun] 잠깐 멍하니 그 자세 그대로 있었다." id c04d_0028
    
    "자다가 떨어진 경험이 얼마만인지 기억도 나지 않았다." id c04d_0029
    
    show cara consider
    with dissolve

    c "(침대가 그렇게 높지 않아서 다행인가?... 다리에 멍은 안 생기겠지?)" id c04d_0030
    
    show cara base at change(1, 0, 0)
    with dissolve

    "휘청거리며 [pl_name][josa_eun_neun] 하체를 다시 침대 위로 끌어 올렸다." id c04d_0031
    
    show cara sleep
    with dissolve

    "갑작스레 잠에서 깬 탓인지 머리가 욱신거렸다." id c04d_0032
    
    "[pl_name][josa_eun_neun] 몽롱한 상태로 잠시 눈을 감았다." id c04d_0033
    
    hide cara
    with dissolve

    "..." id c04d_0034
    
    "잠깐 졸고 나니 개운하게 일어날 수 있었다." id c04d_0035
    
    show cara base inn_d
    with dissolve

    c "(뭔가, 꿈을 꾼 것 같은데...)" id c04d_0036
    
    "꿈의 내용은 물거품처럼 순식간에 사라져 버렸다." id c04d_0037

    play sound "audio/effect/puton.mp3" volume 0.5    
    show cara am_d
    with dissolve

    "[pl_name][josa_eun_neun] 옷을 챙겨 입으며 새로운 하루를 준비했다." id c04d_0038

    play sound "effect/footstep.mp3" volume 0.85
    show cara at walk (-1500, 2.8, 5)
    pause(0.5)
    
    stop music fadeout 2.5

    #챕터 추가하면 여기 바꾸기

    if wolf_route == True :
        
        jump c5w_start
    
    elif tiger_route == True :
        
        jump c5t_start


    
    