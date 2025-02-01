init offset = -2

init python:
    cara_description = _("  뒷골목에서 마법상점을 운영하는 주인공. 주로 용병들에게 회복 물약을 판매한다. \n  스스로 평범하다고 생각하지만, 다양한 비밀을 가지고 있다. 마법과 주술 둘 다 재능이 있다.\n  오드아이와 길쭉한 귀가 특징. 나름 독특한 외형이지만, 개과에서는 종종 보이는 특징이다. \n  의외로 눈치가 없는 구석도... 주변 수인들의 관심을 잘 이해하지 못하고 있다.")
    wolf_description = _("  유명 용병단에 소속된 숙련된 늑대 용병. 주인공과 호위 계약을 맺었지만, 가게 일까지 적극적으로 도와주고 있다. \n  얼핏 차가워보이는 인상이지만, 주인공에게 만큼은 다른 태도를 보여준다. \n  과거에 주인공과 어떤 관계가 있었던 것 같지만...")
    tiger_description = _("  백작 휘하 기사단의 호랑이 기사. 기사단장이면서 동시에 유명한 호색한이다. \n  자꾸만 주인공의 가게에 찾아와서 플러팅하는 중. 주인공이 굉장히 마음에 든 것 같다. \n  갑옷 이외에는 몸을 가리는게 거의 없다. 노출증이 있는 것 같기도...")
    bear_description = _("  마탑 소속 정식 마법사. 마탑 내에서 입지는 꽤 좁은 편이다. \n  마력누수 때문에 보통 마법사의 절반 수준의 마법밖에 못 쓴다. 타고난 육체 능력으로 보완하는 중. \n  주인공의 불법 행위를 눈감아주지만, 일방적으로 공범 관계라고 생각하는 듯 하다.")
    dragon_description = _("  300년 넘게 살아온 주술사. 주인공의 스승님이다. 평소에는 전 세계를 여행하는 방랑자이며, 주인공이 가게를 차린 뒤로 처음 찾아왔다. \n  걸치고 있는 옷도 불편한지, 훌렁훌렁 벗어버리는 타입. \n  어떠한 이유로 주인공에 대한 기억을 봉인하게 되었다.")
    lucas_description = _("  가까운 마을의 용병 길드에서 접수원으로 일하는 치타. 서류 업무는 거의 루카스 담당이다. \n  평소에는 지적이고 예의바른 직원이지만, 술에 취하면 완전히 다른 모습을 보여준다.")
    ahjin_description = _("  동방을 오가는 무역 상단의 주인. 상품의 가치를 알아보는 능력이 탁월하다. \n  상단에서는 식음료를 주로 취급하고 있다. 주력 상품은 술과 향신료. \n  최근들어 자꾸만 '매음굴의 주인'이라는 헛소문에 시달리는 중.")
    


init python:
    def update_character_description(character, new_description):
            if character in persistent.characters_details_2p:
                persistent.characters_details_2p[character]["text"] = new_description
                persistent.characters_details_2p[character]["changed"] = True
                persistent.characters_details_2p[character]["viewed"] = False

# 사용 예시:
# label some_label:
#     # 루카스의 설명 업데이트
#     $ update_character_description("lucas", _("길드접수원이다. 성실하고 친절한 성격으로 모두에게 인기가 많다."))

#     # 캐릭터 설명 확인
#     "루카스의 설명: [persistent.characters_details_2p['lucas']['text']]"





init python:
    def add_info(page_number, new_key, new_content):
        # """
        # 특정 페이지 번호에 두 번째 정보를 추가합니다.
        
        # :param page_number: 정보를 추가할 페이지 번호 (문자열)
        # :param new_key: 추가할 새로운 키
        # :param new_content: 추가할 새로운 내용
        # """
        if page_number in info_pages[0]:
            info_pages[0][page_number][new_key] = new_content


    def remove_info(page_number):
        # """
        # 특정 페이지 번호에서 두 번째 정보를 제거합니다.
        
        # :param page_number: 정보를 제거할 페이지 번호 (문자열)
        # """
        if page_number in info_pages[0] and key in info_pages[0][page_number]:
            del info_pages[0][page_number][key]

    def get_info_count(page_number):
        # """
        # 특정 페이지의 정보 개수를 반환합니다.
        
        # :param page_number: 확인할 페이지 번호 (문자열)
        # :return: 페이지의 정보 개수
        # """
        return len(info_pages[0].get(page_number, {}))


###위의 함수 사용 예시###
###따옴표 안에 있는 것들 따옴표 빼면 변수로 사용 가능.
    
# 사용 예시:
# label some_label:
#     # 2번 페이지에 새로운 정보 추가
#     $ add_info("2", info_2_key2, "이것은 2번 페이지의 두 번째 정보입니다.")
#     $ add_info("2", info_2_key3, "이것은 2번 페이지의 세 번째 정보입니다.")

#     # 7번 페이지에 여러 정보 추가
#     $ add_info("7", info_7_key2, "이것은 7번 페이지의 두 번째 정보입니다.")
#     $ add_info("7", info_7_key3, "이것은 7번 페이지의 세 번째 정보입니다.")
#     $ add_info("7", info_7_key4, "이것은 7번 페이지의 네 번째 정보입니다.")

#     # 2번 페이지의 특정 정보 제거
#     $ remove_info("2", info_2_key2)

#     # 7번 페이지의 정보 개수 확인
#     $ info_count = get_info_count("7")
#     "7번 페이지의 정보 개수: [info_count]"

#     # 변경된 내용 확인
#     "2번 페이지 내용: [info_pages[0]['2']]"
#     "7번 페이지 내용: [info_pages[0]['7']]"




init python:
    
    #[0]
    title_1 = _("마법 상점")
    info_1_key = _("마법 상점")
    info_1_content = _("마법 지식으로 만든 상품을 판매하는 가게. [pl_name][josa_eun_neun] 주로 연금술로 만들어낸 물약을 취급한다.")

    title_2 = _("회복 물약")
    info_2_key = _("회복 물약")
    info_2_content = _("온갖 종류의 부상을 치유하기 위한 물약. 소독과 재생에 모두 사용할 수 있다. 단, 골절이나 이미 생긴 흉터에는 거의 효과가 없다.")

    title_3 = _("용병 길드")
    info_3_key = _("용병 길드")
    info_3_content = _("용병과 의뢰를 중개하는 길드. 왕국 내 길드 중에서도 가장 규모가 크다. 모든 도시에 지부가 최소 하나는 존재한다.")

    title_4 = _("칼루리엔 용병단")
    info_4_key = _("칼루리엔 용병단")
    info_4_content = _("유명한 용병단. 용병 길드 게시판에서 늘 그 이름과 문양을 볼 수 있다. 소속된 인원은 소수지만, 의뢰 평가 점수는 항상 높은 편이다.")
    
    title_5 = _("반슈타인 기사단")
    info_5_key = _("반슈타인 기사단")
    info_5_content = _("백작 휘하의 기사단. 치안 유지는 물론이고, 마물 토벌에도 적극적으로 참여한다. 현재 기사단장은 엘레드.")
    
    title_6 = _("특제 물약")
    info_6_key = _("특제 물약")
    info_6_content = _("[pl_name][josa_i_ga] 만든 강력한 회복 물약. 금지된 방법으로 만드는 물약이라서 대량으로 만들기는 어렵다. 가게에서 판매하는 물건이 아니다.")
    
    title_7 = _("마력진동")
    info_7_key = _("마력진동")
    info_7_content = _("던전처럼 마나의 흐름이 강한 곳에서 발생하는 현상. 갑작스럽게 흐름이 바뀔 때, 방향을 잃은 마나가 튀어나온다. 아주 위험한 현상은 아니지만, 영향을 받으면 어지럼증을 느끼거나 할 수 있다.")

    
    #[1]
    title_8 = _("마력 폭주")
    info_8_key = _("마력 폭주")
    info_8_content = _("체내 마력 흐름을 통제할 수 없는 상태. 보통은 마법을 잘못 사용하거나, 능력에 맞지 않게 무리하면 발생한다.")
    
    title_9 = _("전송 마법진")
    info_9_key = _("전송 마법진")
    info_9_content = _("마탑에서 운영하는 특수한 공간 연결 마법진. 아무리 먼 거리라도 몇 초 만에 이동할 수 있다. 그러나 무턱대고 쓰기엔 요금이 꽤 비싸다.")
    
    title_10 = _("마력 누수")
    info_10_key = _("마력 누수")
    info_10_content = _("보통 마법사의 마나 효율은 90% 이상이다. 바토의 마나 효율은 약 절반 정도로, 마법 사용에 미숙한 초보 수준이다.")
    
    title_11 = _("마탑")
    info_11_key = _("마탑")
    info_11_content = _("현재 왕국에서 가장 큰 마법사 사회. 마탑의 정규 교육 과정을 거치려면 아주 많은 돈이 필요하다. 귀족과는 서로 껄끄러운 관계.")
    
    title_12 = _("시술")
    info_12_key = _("시술")
    info_12_content = _("마법을 몸에 직접 새기는 행위. 주로 용병이 빠르게 강해지기 위한 수단으로 사용한다. 새기는 방법에 따라서 효과와 부작용도 천차만별.")
    
    title_13 = _("아티팩트")
    info_13_key = _("아티팩트")
    info_13_content = _("원래는 강력한 힘을 가진 고대 유물을 뜻한다. 그러나 언제부턴가 고대와 관련 없는 물건들도 강력하거나 유용하다면 아티팩트라고 부르기 시작했다.")
    
    title_14 = _("주술")
    info_14_key = _("주술")
    info_14_content = _("아득히 오래전부터 있었던 신비로운 기술. 그 강력함 때문에 전쟁도 여러 번 일어났으며, 주술사를 멸절한 국가도 있었다.")
    

    #[2]
    title_15 = _("순간이동")
    info_15_key = _("순간이동")
    info_15_content = _("\'공간 마법의 예술\'이라고도 불리는 고난도 마법. 숙련된 마법사도 적절한 매개체를 이용해서 시전한다. 류호의 구름 문양이 대표적인 예시.")

    title_16 = _("봉인")
    info_16_key = _("봉인")
    info_16_content = _("신비로운 힘으로 대상을 세계로부터 끊어내는 행위를 말한다. 다양한 형태의 격리 / 차단 마법이 발전하면서, 고전적인 봉인 기술은 크게 쇠퇴했다.")
    
    title_17 = _("술집")
    info_17_key = _("술집")
    info_17_content = _("술, 식사, 숙박 등을 제공하는 가게. 따로 거점이 없는 떠돌이 용병들이 모이는 장소기도 하다. 참고로, 용병 길드는 \'술집에서 용병과 계약하지 말 것\'을 권장하고 있다.")
    
    title_18 = _("강철손 상회")
    info_18_key = _("강철손 상회")
    info_18_content = _("어느 날 갑자기 나타난 조직. 상회라고 하지만 마탑에서는 그 정체를 범죄 조직으로 추정하고 있다.")
    
    title_19 = _("에일")
    info_19_key = _("에일")
    info_19_content = _("술집에서 가장 흔하게 파는 술. 냉각과 보존 마법의 발전으로 새로운 형태의 술도 생겨나고 있지만, 여전히 술 하면 에일이 가장 기본적이다.")
    
    title_20 = _("벌꿀 사과주")
    info_20_key = _("벌꿀 사과주")
    info_20_content = _("사과즙을 발효시켜 만든 술에 벌꿀을 첨가하여 맛을 조절한 술. 꿀의 단맛과 사과의 향기가 절묘한 조합을 자랑한다. 그러나 다른 술에 비해 흡수가 굉장히 빠르다.")
    
    title_21 = _("마법 보호막")
    info_21_key = _("마법 보호막")
    info_21_content = _("대부분의 방어 수단은 마력을 굴절시켜 약간 흘려보내는 정도에 그친다. 모든 종류의 마법으로부터 완전히 방어해 주는 보호막은 류호조차 불가능한 수준.")
    

    #[3]
    title_22 = _("남자 사냥")
    info_22_key = _("남자 사냥")
    info_22_content = _("성적인 만남을 위해 술집 등에서 어슬렁거리는 행위. 오직 \'남자 사냥\'만을 위한 공간도 있다고 한다.")

    title_23 = _("암시장")
    info_23_key = _("암시장")
    info_23_content = _("어떤 의미로든 떳떳하지 못한 거래가 이루어지는 곳. 과거에 암시장을 멸절하려던 시도가 실패로 돌아간 뒤, 귀족들도 어느 정도는 묵인해 주고 있다.")
    
    title_24 = _("특제 물약2")
    info_24_key = _("특제 물약2")
    info_24_content = _("신선한 피에서 생명력을 뽑아내 회복 물약과 섞은 것. 시간이 되감기는 것처럼 느껴질 정도로 강력한 회복력을 보여준다.")

    title_25 = _("산 제물")
    info_25_key = _("산 제물")
    info_25_content = _("강력한 주술을 쓰기 위해 목숨을 제물로 바치는 행위. 고대에는 이것 때문에 그야말로 수없이 많은 목숨이 희생되었다고 한다.")
    
    title_26 = _("용병왕")
    info_26_key = _("용병왕")
    info_26_content = _("일개 용병에서 왕이 되었다고 전해지는 인물. 분명 실존했던 수인이지만, 각색된 이야기가 너무 많아 대부분의 전설은 과장으로 여겨진다.")
    
    title_27 = _("드래곤고추")
    info_27_key = _("드래곤고추")
    info_27_content = _("새빨간 색이 특징인 고추 품종. 생으로도 먹지만, 주로 말려서 가루를 만들어 쓴다. 이름의 유래에 대해서는 아직도 박물학자 간의 논쟁이 많다.")
    
    title_28 = _("용린과")
    info_28_key = _("용린과")
    info_28_content = _("껍질이 용의 비늘과 닮았다 하여 이름 붙여진 과일. 속의 붉은 과육은 새콤달콤하다. 용병왕의 전설에도 등장하지만, 그 사실 여부는 밝혀지지 않았다.")
    


    #[4]
    title_29 = _("정보 길드")
    info_29_key = _("정보 길드")
    info_29_content = _("원래는 정보를 거래하는 길드였으나, 현재는 사실상 용병 길드와 병합되었다. 정보를 수집하는 일을 전문으로 한다.")
    
    title_30 = _("증류주")
    info_30_key = _("증류주")
    info_30_content = _("한번 발효된 술을 다시 증류해서 만든 술. 그 과정에서 맛과 향이 크게 변한다. 이 지역의 유명 증류주는 포도주나 사과주를 재료로 만든다.")
    
    title_31 = _("발광 마법")
    info_31_key = _("발광 마법")
    info_31_content = _("마나를 빛으로 변환하여 뿜어내는 마법. 하지만, 생활 속에서 광원이 필요하다면 다른 수단을 사용하는 게 더 효율적이다.")
    
    title_32 = _("강철손 상회2")
    info_32_key = _("강철손 상회2")
    info_32_content = _("이 조직은 장인들을 납치해서 노예처럼 부리고 있었다. 그러나 그 목적에 대해서는 아직 정확히 밝혀지지 않았다.")
    
    title_33 = _("???")
    info_33_key = _("???")
    info_33_content = _("???")
    
    title_34 = _("???")
    info_34_key = _("???")
    info_34_content = _("???")

    title_35 = _("???")
    info_35_key = _("???")
    info_35_content = _("???")
   


############################################
######### 영구데이터 업데이트 기능 ###########
############################################


############ 새 페이지 업데이트 ##############
# init python:
#     # info_tags 업데이트
#     if persistent.info_tags is not None:
#         # 새로 추가할 태그 데이터 - 이 부분만 수정하면 됨
#         new_tag_data = {
#             "1": {"unlocked": False, "name": "키워드_33", "viewed": False},
#             "2": {"unlocked": False, "name": "키워드_34", "viewed": False},
#         }
        
#         # 새 데이터의 첫 번째 항목을 기준으로 중복 검사
#         check_keyword = new_tag_data["1"]["name"]
#         has_keyword = any(
#             any(item["name"] == check_keyword for item in page.values())
#             for page in persistent.info_tags
#         )
        
#         # 키워드가 없을 때만 새 데이터 추가
#         if not has_keyword:
#             persistent.info_tags.append(new_tag_data)
            
#     # info_pages 업데이트
#     if persistent.info_pages is not None:
#         # 새로 추가할 페이지 데이터 - 이 부분만 수정하면 됨
#         new_page_data = {
#             "1": {info_33_key: info_33_content},
#             "2": {info_34_key: info_34_content},
#         }
        
#         # 새 데이터의 첫 번째 항목을 기준으로 중복 검사
#         check_key = list(new_page_data["1"].keys())[0]  # 첫 번째 키 가져오기
#         has_info = any(
#             any(check_key in page_item for page_item in page.values())
#             for page in persistent.info_pages
#         )
        
#         # info key가 없을 때만 새 데이터 추가
#         if not has_info:
#             persistent.info_pages.append(new_page_data)
    

    
#     # 변경사항 저장
#     renpy.save_persistent()


init python:
    def add_to_page(page_index, new_tag_data, new_page_data):
        """특정 페이지에 새로운 데이터 추가"""
        if persistent.info_tags is not None and len(persistent.info_tags) > page_index:
            # info_tags 업데이트
            current_page = persistent.info_tags[page_index]
            next_key = str(len(current_page) + 1)
            
            if next_key not in current_page:
                current_page[next_key] = new_tag_data
                
        if persistent.info_pages is not None and len(persistent.info_pages) > page_index:
            # info_pages 업데이트
            current_page = persistent.info_pages[page_index]
            next_key = str(len(current_page) + 1)
            
            if next_key not in current_page:
                current_page[next_key] = new_page_data
                
        renpy.save_persistent()

    # 사용 예시:
    # 5번째 페이지(인덱스 4)에 새 데이터 추가

    ###### 페이지 내부에 추가 #########
    # new_tag = {"unlocked": False, "name": "키워드_44", "viewed": False}
    # new_page = {info_44_key: info_44_content}
    # add_to_page(4, new_tag, new_page)