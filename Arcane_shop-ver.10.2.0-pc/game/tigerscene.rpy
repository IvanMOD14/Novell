##################### CG1 #####################
###############################################
image bg tiger_s1_01 :
    "images/bg/tiger/01/t_1.webp"
    zoom 0.6

image bg tiger_s1_02 :
    "images/bg/tiger/01/t_2.webp"
    zoom 0.6

image bg tiger_s1_03 :
    "images/bg/tiger/01/t_3.webp"
    zoom 0.6

image bg tiger_s1_04 :
    "images/bg/tiger/01/t_4.webp"
    zoom 0.6

image bg tiger_s1_05 :
    "images/bg/tiger/01/t_5.webp"
    zoom 0.6

image tiger_s1_p :
    "images/bg/tiger/01/t_p.webp"
    zoom 0.6

image tiger_s1_eye :
    "images/bg/tiger/01/t_eye.webp"
    zoom 0.6

image tiger_s1_surprise :
    "images/bg/tiger/01/t_surprise.webp"
    zoom 0.6

##################### CG2 #####################
###############################################
image bg tiger_s2_background :
    "images/bg/tiger/02/background.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_spike :
    "images/bg/tiger/02/spike.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_line :
    "images/bg/tiger/02/line.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_line2 :
    "images/bg/tiger/02/line2.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_01 :
    "images/bg/tiger/02/1.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_01_crop :
    Crop ((0, 400, 1928, 1100), "tiger_s2_01")
    align (0.5, 0.5)
    yoffset 408  

image tiger_s2_02 :
    "images/bg/tiger/02/2.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_03 :
    "images/bg/tiger/02/3.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_03_crop :
    Crop ((0, 400, 1928, 1100), "tiger_s2_03")
    align (0.5, 0.5)
    yoffset 408  

image tiger_s2_04 :
    "images/bg/tiger/02/4.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_05 :
    "images/bg/tiger/02/5.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_06 :
    "images/bg/tiger/02/6.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_07 :
    "images/bg/tiger/02/7.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_08 :
    "images/bg/tiger/02/8.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_09 :
    "images/bg/tiger/02/9.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_10 :
    "images/bg/tiger/02/10.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_11 :
    "images/bg/tiger/02/11.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_12 :
    "images/bg/tiger/02/12.webp"
    align (0.5, 0.5)
    zoom 0.551

image tiger_s2_frame :
    "images/bg/tiger/02/frame.webp"
    align (0.5, 0.5)
    xoffset 50
    zoom 0.5

image tiger_s2_frame2 :
    "images/bg/tiger/02/frame2.webp"
    align (0.5, 0.5)
    xoffset 50
    zoom 0.5

image tiger_s2_frame3 :
    "images/bg/tiger/02/frame3.webp"
    align (0.5, 0.5)
    xoffset 50
    zoom 0.5

image tiger_s2_frame4 :
    "images/bg/tiger/02/frame4.webp"
    align (0.5, 0.5)
    xoffset 50
    zoom 0.5

image tiger_s2_frame5 :
    "images/bg/tiger/02/frame5.webp"
    align (0.5, 0.5)
    xoffset 50
    zoom 0.5


layeredimage tiger_cg2_merge:

    group images:
    
        attribute pt1_01 default:
            "tiger_s2_02"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_01_crop"

layeredimage tiger_cg2_merge2:

    group images:
    
        attribute pt1_01 default:
            "tiger_s2_03"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_04"

layeredimage tiger_cg2_merge3:

    group images:
    
        attribute pt1_01 default:
            "tiger_s2_03_crop"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_05"

layeredimage tiger_cg2_merge4:

    group images:
    
        attribute pt1_01 default:
            "tiger_s2_03"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_08"

layeredimage tiger_cg2_merge5:

    group images:
    
        attribute pt1_01 default:
            "tiger_cg2_merge4"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_09"

layeredimage tiger_cg2_merge6:

    group images:
    
        attribute pt1_01 default:
            "tiger_s2_07"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_10"

layeredimage tiger_cg2_merge7:

    group images:
    
        attribute pt1_01 default:
            "tiger_cg2_merge5"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_11"

layeredimage tiger_cg2_merge8:

    group images:
    
        attribute pt1_01 default:
            "tiger_cg2_merge2"
    
    group images2 :
        
        attribute pt2_01 default:
            "tiger_s2_12"

##############

layeredimage tiger_cg2:
   
    group background:
    
        attribute bg_01 default:
            "bg tiger_s2_background"
    
    group images:
    
        attribute im_01 default:
            "tiger_s2_01"
        attribute im_02:
            "tiger_cg2_merge"
        attribute im_03:
            "tiger_s2_03"
        attribute im_04:
            "tiger_cg2_merge2"
        attribute im_05:
            "tiger_cg2_merge3"
        attribute im_06:
            "tiger_s2_06"
        attribute im_07:
            "tiger_s2_07"
        attribute im_08:
            "tiger_cg2_merge4"
        attribute im_09:
            "tiger_cg2_merge5"
        attribute im_10:
            "tiger_cg2_merge6"
        attribute im_11:
            "tiger_cg2_merge7"
        attribute im_12:
            "tiger_cg2_merge8"
        
    group frames:
        
        attribute fm_01 :
            "tiger_s2_frame"
        attribute fm_02 :
            "tiger_s2_frame2"
        attribute fm_03 :
            "tiger_s2_frame3"
        attribute fm_04 :
            "tiger_s2_frame4"
        attribute fm_05 :
            "tiger_s2_frame5"
    
    group spike:

        attribute spike :
            "tiger_s2_spike"
    
    group lines:

        attribute ln_01 :
            "tiger_s2_line"
    
    group lines2:

        attribute ln_02 :
            "tiger_s2_line2"


##################### CG3 #####################
###############################################

image bg tiger_s3_background :
    "images/bg/tiger/03/1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_01 :
    "images/bg/tiger/03/1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_01_1 :
    "images/bg/tiger/03/1-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_02 :
    "images/bg/tiger/03/2.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_03 :
    "images/bg/tiger/03/3.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_04 :
    "images/bg/tiger/03/4.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_05 :
    "images/bg/tiger/03/5.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_06 :
    "images/bg/tiger/03/6.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_06_1 :
    "images/bg/tiger/03/6-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_07 :
    "images/bg/tiger/03/7.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_08 :
    "images/bg/tiger/03/8.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_08_1 :
    "images/bg/tiger/03/8-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_08_2 :
    "images/bg/tiger/03/8-2.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_09 :
    "images/bg/tiger/03/9.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_10 :
    "images/bg/tiger/03/10.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_11 :
    "images/bg/tiger/03/11.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_11_1 :
    "images/bg/tiger/03/11-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_11_2 :
    "images/bg/tiger/03/11-2.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_12 :
    "images/bg/tiger/03/12.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_12_1 :
    "images/bg/tiger/03/12-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_13 :
    "images/bg/tiger/03/13.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_14 :
    "images/bg/tiger/03/14.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_15 :
    "images/bg/tiger/03/15.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_16 :
    "images/bg/tiger/03/16.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_16_1 :
    "images/bg/tiger/03/16-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_17 :
    "images/bg/tiger/03/17.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_18 :
    "images/bg/tiger/03/18.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_19 :
    "images/bg/tiger/03/19.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_20 :
    "images/bg/tiger/03/20.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_21 :
    "images/bg/tiger/03/21.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_22 :
    "images/bg/tiger/03/22.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_23 :
    "images/bg/tiger/03/23.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_23_1 :
    "images/bg/tiger/03/23-1.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_24 :
    "images/bg/tiger/03/24.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_25 :
    "images/bg/tiger/03/25.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_26 :
    "images/bg/tiger/03/26.webp"
    align (0.5, 0.5)
    zoom 0.2755

image tiger_s3_tongue :
    "images/bg/tiger/03/tongue.webp"
    zoom 0.24
    yoffset 0

    ease 0.5 yoffset -40
    ease 0.25 alpha 0.0
    ease 0 yoffset 0
    ease 0.5 alpha 1.0 yoffset -40

image tiger_s3_hand :
    "images/bg/tiger/03/hand.webp"
    zoom 0.35

        
##################### CG4 #####################
###############################################

image tiger_s4_ring :
    "images/bg/tiger/04/ring.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_ring2 :
    "images/bg/tiger/04/ring2.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_ring3 :
    "images/bg/tiger/04/ring3.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_ring4 :
    "images/bg/tiger/04/ring4.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_ring5 :
    "images/bg/tiger/04/ring4.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_tigerbeat :
    "images/bg/tiger/04/tigerbeat.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_mcbeat :
    "images/bg/tiger/04/mcbeat.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_spike :
    "images/bg/tiger/04/spike.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_surprise :
    "images/bg/tiger/04/surprise.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_fr :
    "images/bg/tiger/04/frame.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

image tiger_s4_fr2 :
    "images/bg/tiger/04/frame2.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

image tiger_s4_fr2_1 :
    "images/bg/tiger/04/frame2_1.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

image tiger_s4_fr3 :
    "images/bg/tiger/04/frame3.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

image tiger_s4_fr3_1 :
    "images/bg/tiger/04/frame3_1.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

image tiger_s4_fr4 :
    "images/bg/tiger/04/frame4.webp"
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51


image tiger_s4_ring_move:
    animation
    "tiger_s4_ring"
    pause 0.035
    "tiger_s4_ring2"
    pause 0.035
    "tiger_s4_ring3"
    pause 0.045
    "tiger_s4_ring2"
    pause 0.035
    "tiger_s4_ring"
    pause 0.035
    "tiger_s4_ring4"
    pause 0.035
    "tiger_s4_ring"
    pause 0.055
    "tiger_s4_ring5"
    pause 0.065
    "tiger_s4_ring"
    pause 0.035
    "tiger_s4_ring4"
    pause 0.045
    "tiger_s4_ring"
    pause 0.035
    "tiger_s4_ring5"
    pause 0.03
    "tiger_s4_ring"
    pause 0.03


image tiger_s4_hring :
    "images/bg/tiger/04/hring.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_hring2 :
    "images/bg/tiger/04/hring2.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_hring3 :
    "images/bg/tiger/04/hring3.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_hring4 :
    "images/bg/tiger/04/hring4.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_hring5 :
    "images/bg/tiger/04/hring4.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_hring_move:
    animation
    "tiger_s4_hring"
    pause 0.035
    "tiger_s4_hring2"
    pause 0.035
    "tiger_s4_hring3"
    pause 0.045
    "tiger_s4_hring2"
    pause 0.035
    "tiger_s4_hring"
    pause 0.035
    "tiger_s4_hring4"
    pause 0.035
    "tiger_s4_hring"
    pause 0.055
    "tiger_s4_hring5"
    pause 0.065
    "tiger_s4_hring"
    pause 0.035
    "tiger_s4_hring4"
    pause 0.045
    "tiger_s4_hring"
    pause 0.035
    "tiger_s4_hring5"
    pause 0.03
    "tiger_s4_hring"
    pause 0.03


image bg tiger_s4_background :
    "images/bg/tiger/04/background.webp"
    align (0.5, 0.5) 


image tiger_s4_back_shelf :
    "images/bg/tiger/04/back_shelf.webp"
    align (0.5, 0.5) 


image tiger_s4_front :
    "images/bg/tiger/04/front.webp"
    align (0.5, 0.5)
    zoom 0.14
    zpos 650

image tiger_s4_front2 :
    "images/bg/tiger/04/front2.webp"
    align (0.5, 0.5)
    zoom 0.14
    zpos 650    



    
layeredimage tiger_cg4_frame:
   
    align (0.5, 0.5)
    zoom 0.1
    zpos 650
    xpos 0.2
    ypos 0.51

    group frames:
    
        attribute fr_01 default:
            "images/bg/tiger/04/frame.webp"
        attribute fr_02 :
            "images/bg/tiger/04/frame2.webp"        
        attribute fr_02_1 :
            "images/bg/tiger/04/frame2_1.webp"        
        attribute fr_03 :
            "images/bg/tiger/04/frame3.webp"        
        attribute fr_03_1 :
            "images/bg/tiger/04/frame3_1.webp"        
        attribute fr_04 :
            "images/bg/tiger/04/frame4.webp"      

  

init python:
    for i in range(1, 20):  # 1부터 19까지
        num = str(i).zfill(2)  # 01, 02, ... 형식으로 변환
        renpy.image(f"tiger_s4_{num}", 
            Transform(
                "images/bg/tiger/04/{}.webp".format(i),
                align=(0.5, 0.5),
                zoom=0.2755
            )
        )

image tiger_s4_05_1 :
    "images/bg/tiger/04/5_1.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_05_2 :
    "images/bg/tiger/04/5_2.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_06_1 :
    "images/bg/tiger/04/6_1.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_07_1 :
    "images/bg/tiger/04/7_1.webp"
    align (0.5, 0.5) 
    zoom 0.2755

image tiger_s4_09_1 :
    "images/bg/tiger/04/9_1.webp"
    align (0.5, 0.5) 
    zoom 0.2755


layeredimage tiger_cg4:

    group background:
        # zoom 0.55
        attribute background default :
            "images/bg/tiger/04/background.webp"
            align (0.5, 0.5) 
            zoom 0.2755  

    group back_shelf:
        # zoom 0.8
        attribute back_shelf default :
            "images/bg/tiger/04/back_shelf.webp"
            align (0.5, 0.5) 
            zoom 0.2755


    group images:
    
        attribute im_01 default :
            "tiger_s4_01"
        attribute im_02 :
            "tiger_s4_05_1" #frame1
        attribute im_03 :
            "tiger_s4_05" #spike #frame2_1
        attribute im_04 :
            "tiger_s4_07" #tigerbeat
        attribute im_05 :
            "tiger_s4_09" #tigerbeat
        attribute im_06 :
            "tiger_s4_16 " #tigerbeat mcbeat #frame3
        attribute im_07 :
            "tiger_s4_17" #tigerbeat mcbeat #frame3_1
        attribute im_08 :
            "tiger_s4_18" #frame4


    group effect:
    
        attribute tigerbeat :
            "images/bg/tiger/04/tigerbeat.webp"
            align (0.5, 0.5) 
            zoom 0.2755
        
        attribute tigerbeat2 :
            "images/bg/tiger/04/tigerbeat.webp"
            align (0.5, 0.5) 
            zoom 0.2755
            yzoom 1.01 xzoom 0.99 xoffset 1
    
    group effect2:

        attribute mcbeat:
            "images/bg/tiger/04/mcbeat.webp"
            align (0.5, 0.5) 
            zoom 0.2755 
    
    group effect3:

        attribute spike :
            "images/bg/tiger/04/spike.webp"
            align (0.5, 0.5) 
            zoom 0.2755 
    
    group effect4:

        attribute surprise :
            "images/bg/tiger/04/surprise.webp"
            align (0.5, 0.5) 
            zoom 0.2755 

    group front:
        
        align (0.5, 0.5) 
        zoom 0.28
        
        attribute front_01 :
            "images/bg/tiger/04/front.webp"
        attribute front_02 default :
            "images/bg/tiger/04/front2.webp"

    group frames:
    
        align (0.5, 0.5) 
        zoom 0.248
        xoffset -1350
        yoffset 80

        attribute fr_01 :
            "images/bg/tiger/04/frame.webp"     
        attribute fr_02_1 :
            "images/bg/tiger/04/frame2_1.webp"        
        attribute fr_03 :
            "images/bg/tiger/04/frame3.webp"        
        attribute fr_03_1 :
            "images/bg/tiger/04/frame3_1.webp"        
        attribute fr_04 :
            "images/bg/tiger/04/frame4.webp" 