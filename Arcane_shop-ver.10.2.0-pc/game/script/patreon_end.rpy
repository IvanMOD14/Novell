label patreon_end:

    
    hide screen book_icon with dissolve
    stop music fadeout 2.5

    scene bg backcol with Fade(0.8, 0.8, 0.8)
 
    "챕터가 끝났습니다." id p_end_0000

    "플레이 해주셔서 감사합니다!" id p_end_0001

    show screen credits
    with dissolve

    "게임을 만드는데 많은 도움을 주신 분들 입니다. 정말로 감사드립니다." id p_end_0002
    
    "이름을 클릭하면 SNS와 같은 프로필 페이지로  방문하실 수 있습니다." id p_end_0003

    hide screen credits
    show screen special_thanks
    with dissolve

    "게임을 지원해주신 모든 분들께 감사드립니다." id p_end_0004

    "패트리온에서 새로운 빌드가 먼저 출시되니 많은 관심 부탁 드려요!" id p_end_0005

    show screen patreon_button
    with dissolve

    show click :
        xoffset 670
        yoffset -270
    with dissolve

    "이미지를 클릭하시면 패트리온 페이지로 넘어갈 수 있습니다." id p_end_0006

    "한 번 더 클릭하면 메인화면으로 넘어갑니다." id p_end_0007

    hide screen patreon_button
    hide screen special_thanks
    hide click
    with dissolve

    menu :

        "예." :

            "끝." id p_end_0008