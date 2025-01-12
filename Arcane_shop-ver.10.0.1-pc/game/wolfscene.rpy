##################### CG1 #####################
###############################################
image bg wolf_s1_01 :
    "images/bg/wolf/01/w_1.webp"
    zoom 0.6

image bg wolf_s1_02 :
    "images/bg/wolf/01/w_2.webp"
    zoom 0.6

image bg wolf_s1_03 :
    "images/bg/wolf/01/w_3.webp"
    zoom 0.6

image bg wolf_s1_04 :
    "images/bg/wolf/01/w_4.webp"
    zoom 0.6

image wolf_s1_p1 :
    "images/bg/wolf/01/w_p1.webp"
    zoom 0.63

image wolf_s1_p2 :
    "images/bg/wolf/01/w_p2.webp"
    zoom 0.63

image wolf_s1_p3 :
    "images/bg/wolf/01/w_p3.webp"
    zoom 0.63


##################### CG2 #####################
###############################################
image wolf_s2_01 :
    "images/bg/wolf/02/w_1.webp"
    zoom 0.56

image wolf_s2_02 :
    "images/bg/wolf/02/w_2.webp"
    zoom 0.56

image wolf_s2_03_w :
    "images/bg/wolf/02/w_3_wolf.webp"
    zoom 0.56

image wolf_s2_03_mc :
    "images/bg/wolf/02/w_3_mc.webp"
    zoom 0.56

image wolf_s2_04_w :
    "images/bg/wolf/02/w_4_wolf.webp"
    zoom 0.56

image wolf_s2_04_mc :
    "images/bg/wolf/02/w_4_mc.webp"
    zoom 0.56

image wolf_s2_05_w :
    "images/bg/wolf/02/w_5_wolf.webp"
    zoom 0.56

image wolf_s2_05_mc :
    "images/bg/wolf/02/w_5_mc.webp"
    zoom 0.56

image wolf_s2_05_mc2 :
    "images/bg/wolf/02/w_5_mc2.webp"
    zoom 0.56

image wolf_s2_06 :
    "images/bg/wolf/02/w_6.webp"
    zoom 0.56

image wolf_s2_06_1 :
    "images/bg/wolf/02/w_6_1.webp"
    zoom 0.56

image wolf_s2_06_1a :
    "images/bg/wolf/02/w_6_1a.webp"
    zoom 0.56

image wolf_s2_06_2 :
    "images/bg/wolf/02/w_6_2.webp"
    zoom 0.56

image wolf_s2_07_w :
    "images/bg/wolf/02/w_7_wolf.webp"
    zoom 0.56

image wolf_s2_07_mc :
    "images/bg/wolf/02/w_7_mc.webp"
    zoom 0.56

image wolf_s2_08 :
    "images/bg/wolf/02/w_8.webp"
    zoom 0.56

image wolf_s2_09 :
    "images/bg/wolf/02/w_9.webp"
    zoom 0.56


image wolf_s2_cloud :
    "images/bg/wolf/02/w_cloud.webp"
    zoom 0.56

image wolf_s2_house :
    "images/bg/wolf/02/w_house.webp"
    zoom 0.56

image bg wolf_s2_sky :
    "images/bg/wolf/02/w_sky.webp"
    zoom 0.56

image wolf_s2_leaf :
    "images/bg/wolf/02/w_leaf.webp"
    zoom 0.56

image wolf_s2_heart :
    "images/bg/wolf/02/w_heart.webp"
    zoom 0.56


layeredimage wolf_cg2:
   
    group sky:
    
        attribute sky default:
            "bg wolf_s2_sky"
        attribute sky2 :
            "bg wolf_s2_sky"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.06
    
    group cloud:
    
        attribute cloud default:
            "wolf_s2_cloud"
        attribute cloud2:
            "wolf_s2_cloud"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.2

    group house:
    
        attribute house default:
            "wolf_s2_house"
        attribute house2:
            "wolf_s2_house"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.3
    
    group images:

        attribute im_01 default:
            "wolf_s2_01"
        attribute im_zoom:
            "wolf_s2_04_mc"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.41

    group images2:
        
        attribute im_02 :
            "wolf_s2_06_1"
        

    group images3:
        
        attribute im_mc :
            "wolf_s2_06_2"
        attribute im_mouth :
            "wolf_s2_08"
        attribute im_03 :
            "wolf_s2_07_mc"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.41

    group leaf:

        attribute leaf default:
            "wolf_s2_leaf"
        attribute leaf2:
            "wolf_s2_leaf"
            align (0.5, 0.32)
            anchor (0.5, 0.32)
            zoom 1.5

    group heart:

        attribute heart :
            "wolf_s2_heart"
        


##################### CG3 #####################
###############################################
image wolf_s3_01 :
    "images/bg/wolf/03/w_1.webp"
    zoom 0.551

image wolf_s3_02 :
    "images/bg/wolf/03/w_2.webp"
    zoom 0.551

layeredimage wolf_cg3:
   
    group paper:
    
        attribute paper default:
            "wolf_s3_01"

    group horny:
    
        attribute horny :
            "wolf_s3_02"

##################### CG4 #####################
###############################################
image wolf_s4_01 :
    "images/bg/wolf/04/w_1.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_02 :
    "images/bg/wolf/04/w_2.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_03 :
    "images/bg/wolf/04/w_3.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_04 :
    "images/bg/wolf/04/w_4.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_05 :
    "images/bg/wolf/04/w_5.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_05_add :
    "images/bg/wolf/04/w_5_add.webp"
    zoom 0.551

image wolf_s4_06 :
    "images/bg/wolf/04/w_6.webp"
    zoom 0.551
    yoffset 90

image wolf_s4_07 :
    "images/bg/wolf/04/w_7.webp"
    zoom 0.551

image wolf_s4_08 :
    "images/bg/wolf/04/w_8.webp"
    zoom 0.551

image wolf_s4_09 :
    "images/bg/wolf/04/w_9.webp"
    zoom 0.551

image wolf_s4_10 :
    "images/bg/wolf/04/w_10.webp"
    zoom 0.551

image wolf_s4_11 :
    "images/bg/wolf/04/w_11.webp"
    zoom 0.551
    yoffset 250

image wolf_s4_11_add :
    "images/bg/wolf/04/w_11_add.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_12 :
    "images/bg/wolf/04/w_12.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_13 :
    "images/bg/wolf/04/w_13.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_14 :
    "images/bg/wolf/04/w_14.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_15 :
    "images/bg/wolf/04/w_15.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_16 :
    "images/bg/wolf/04/w_16.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_17 :
    "images/bg/wolf/04/w_17.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_18 :
    "images/bg/wolf/04/w_18.webp"
    zoom 0.551
    yoffset 170

image wolf_s4_19 :
    "images/bg/wolf/04/w_19.webp"
    zoom 0.551
    yoffset 170



image wolf_s4_hand :
    "images/bg/wolf/04/w_hand.webp"
    zoom 0.4

    ease 0.3 xoffset 30
    ease 0.3 xoffset 0
    repeat 2

image wolf_s4_tongue :
    "images/bg/wolf/04/w_tongue.webp"
    zoom 0.36
    yoffset 0

    ease 0.5 yoffset -40
    ease 0.25 alpha 0.0
    ease 0 yoffset 0
    ease 0.5 alpha 1.0 yoffset -40

layeredimage wolf_cg4:
   
    yoffset 90

    group w_1:
    
        attribute w_1 default:
            "wolf_s4_01"

    group w_2:
    
        attribute w_2 :
            "wolf_s4_02"

    group w_3:
    
        attribute w_3 :
            "wolf_s4_03"
    
    group w_4:
    
        attribute w_4 :
            "wolf_s4_04"
    
    group w_5:
    
        attribute w_5 :
            "wolf_s4_05"
    
    group w_5_add:
    
        attribute w_5_add :
            "wolf_s4_05_add"
            yoffset 90
    
    group w_6:
    
        attribute w_6 :
            "wolf_s4_06"
    
    group w_7_8:
    
        attribute w_7 :
            "wolf_s4_07"
            yoffset 90
        attribute w_8 :
            "wolf_s4_08"
            yoffset 90

    group w_9:
    
        attribute w_9 :
            "wolf_s4_09"
            yoffset 90
    
    group w_10:
    
        attribute w_10 :
            "wolf_s4_10"
            yoffset 90
    
    group w_11:
    
        attribute w_11 :
            "wolf_s4_11"
            yoffset -160

    group w_11_12_add_13:
    
        attribute w_11_add :
            "wolf_s4_11_add"
            yoffset -80
        attribute w_12 :
            "wolf_s4_12"
            yoffset -80
        attribute w_13 :
            "wolf_s4_13"
            yoffset -80   

    group w_14_15:
    
        attribute w_14 :
            "wolf_s4_14"
            yoffset -80
        attribute w_15 :
            "wolf_s4_15"
            yoffset -80

    group w_16:
    
        attribute w_16 :
            "wolf_s4_16"
            yoffset -80
    
    group w_17:
    
        attribute w_17 :
            "wolf_s4_17"
            yoffset -80
    
    group w_18:
    
        attribute w_18 :
            "wolf_s4_18"
            yoffset -80
    
    group w_19:
    
        attribute w_19 :
            "wolf_s4_19"
            yoffset -80


layeredimage wolf_cg4g:
   
    yoffset -210

    group w_1:
    
        attribute w_1 default:
            "wolf_s4_01"

    group w_2:
    
        attribute w_2 :
            "wolf_s4_02"

    group w_3:
    
        attribute w_3 :
            "wolf_s4_03"
    
    group w_4:
    
        attribute w_4 :
            "wolf_s4_04"
    
    group w_5:
    
        attribute w_5 :
            "wolf_s4_05"
    
    group w_5_add:
    
        attribute w_5_add :
            "wolf_s4_05_add"
            yoffset 90
    
    group w_6:
    
        attribute w_6 :
            "wolf_s4_06"
    
    group w_7_8:
    
        attribute w_7 :
            "wolf_s4_07"
            yoffset 90
        attribute w_8 :
            "wolf_s4_08"
            yoffset 90

    group w_9:
    
        attribute w_9 :
            "wolf_s4_09"
            yoffset 90
    
    group w_10:
    
        attribute w_10 :
            "wolf_s4_10"
            yoffset 90
    
    group w_11:
    
        attribute w_11 :
            "wolf_s4_11"
            yoffset -160

    group w_11_12_add_13:
    
        attribute w_11_add :
            "wolf_s4_11_add"
            yoffset -80
        attribute w_12 :
            "wolf_s4_12"
            yoffset -80
        attribute w_13 :
            "wolf_s4_13"
            yoffset -80   

    group w_14_15:
    
        attribute w_14 :
            "wolf_s4_14"
            yoffset -80
        attribute w_15 :
            "wolf_s4_15"
            yoffset -80

    group w_16:
    
        attribute w_16 :
            "wolf_s4_16"
            yoffset -80
    
    group w_17:
    
        attribute w_17 :
            "wolf_s4_17"
            yoffset -80
    
    group w_18:
    
        attribute w_18 :
            "wolf_s4_18"
            yoffset -80
    
    group w_19:
    
        attribute w_19 :
            "wolf_s4_19"
            yoffset -80




##################### CG5 #####################
###############################################

image wolf_s5_arm :
    "images/bg/wolf/05/w_arm.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_belly :
    "images/bg/wolf/05/w_belly.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_belly2 :
    "images/bg/wolf/05/w_belly2.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_belly2_tran :
    "images/bg/wolf/05/w_belly2.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_belly2_line :
    "images/bg/wolf/05/w_belly2_line.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_belly2_line_add :
    "images/bg/wolf/05/w_belly2_line_add.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_bite :
    "images/bg/wolf/05/w_bite.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_body :
    "images/bg/wolf/05/w_body.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_breath :
    "images/bg/wolf/05/w_breath.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_cara :
    "images/bg/wolf/05/w_cara.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_eyehalf :
    "images/bg/wolf/05/w_eyehalf.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_mouth :
    "images/bg/wolf/05/w_mouth.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_penisdw :
    "images/bg/wolf/05/w_penisdw.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_penisup :
    "images/bg/wolf/05/w_penisup.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_screenseed :
    "images/bg/wolf/05/w_screenseed.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_screenseed2 :
    "images/bg/wolf/05/w_screenseed2.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_seed :
    "images/bg/wolf/05/w_seed.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seed2 :
    "images/bg/wolf/05/w_seed2.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seed3 :
    "images/bg/wolf/05/w_seed3.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seed4 :
    "images/bg/wolf/05/w_seed4.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seed5 :
    "images/bg/wolf/05/w_seed5.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seed_cara :
    "images/bg/wolf/05/w_seed_cara.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seedleft_cara :
    "images/bg/wolf/05/w_seedleft_cara.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_seedleft2_cara :
    "images/bg/wolf/05/w_seedleft2_cara.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_seedleft3_cara :
    "images/bg/wolf/05/w_seedleft3_cara.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_seedleft_wolf :
    "images/bg/wolf/05/w_seedleft_wolf.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_seedleft2_wolf :
    "images/bg/wolf/05/w_seedleft2_wolf.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seedleft3_wolf :
    "images/bg/wolf/05/w_seedleft3_wolf.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seedleft4_wolf :
    "images/bg/wolf/05/w_seedleft4_wolf.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_seedleft5_wolf :
    "images/bg/wolf/05/w_seedleft5_wolf.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_sweat :
    "images/bg/wolf/05/w_sweat.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_water_cara :
    "images/bg/wolf/05/w_water_cara.webp"
    zoom 0.551
    yoffset 60 

image wolf_s5_red :
    "images/bg/wolf/05/w_red.webp"
    zoom 0.551
    yoffset 60

image wolf_s5_back :
    "images/bg/wolf/05/w_back.webp"
    zoom 0.551
    yoffset 60

layeredimage wolf_cg5_wolfarm:
   

    xoffset 0
    yoffset 60


    group arm:
    
        attribute arm default:
            "wolf_s5_arm"

    group mouth:
    
        attribute mouth :
            "wolf_s5_mouth"
    
    group halfeye:
    
        attribute eyehalf :
            "wolf_s5_eyehalf"

    group red:
    
        attribute red :
            "wolf_s5_red"

    group breath:
    
        attribute breath :
            "wolf_s5_breath"

    group sweat:
    
        attribute sweat :
            "wolf_s5_sweat"
    
    group seedleft3 :
    
        attribute seedleft3 :
            "wolf_s5_seedleft3_wolf"
    
    group seedleft4 :
    
        attribute seedleft4 :
            "wolf_s5_seedleft4_wolf"
    
    group seedleft5 :
    
        attribute seedleft5 :
            "wolf_s5_seedleft5_wolf"
    

layeredimage wolf_cg5g:
   

    xoffset 0
    yoffset -110


    group back:
    
        attribute back default:
            "wolf_s5_back"
    
    group body:
    
        attribute body default:
            "wolf_s5_body"
        attribute body2 :
            "wolf_s5_body"
            zoom 1.03
            xoffset -30 yoffset -20

    group cara:
    
        attribute cara default:
            "wolf_s5_cara"
    
    group cara_belly:
    
        attribute cara_belly :
            "wolf_s5_belly"
    
    group cara_belly2:
    
        attribute cara_belly2 :
            "wolf_s5_belly2"
    
    group penisdw:
    
        attribute penisdw :
            "wolf_s5_penisdw"
            zoom 1.03
            xoffset -30 yoffset -20
        
    group cara_belly2_tran:
    
        attribute cara_belly2_tran :
            "wolf_s5_belly2"
            alpha 0.45
          
    group arm:
    
        attribute arm default:
            "wolf_s5_arm"
        attribute arm2 :
            "wolf_s5_arm"
            zoom 1.03
            xoffset -30 yoffset -20

    group mouth:
    
        attribute mouth :
            "wolf_s5_mouth"
        attribute mouth2 :
            "wolf_s5_mouth"
            zoom 1.03
            xoffset -30 yoffset -20   
    
    group eyehalf:
    
        attribute eyehalf :
            "wolf_s5_eyehalf"
        attribute eyehalf2 :
            "wolf_s5_eyehalf"
            zoom 1.03
            xoffset -30 yoffset -20 

    group red:
    
        attribute red :
            "wolf_s5_red"
        attribute red2 :
            "wolf_s5_red"
            zoom 1.03
            xoffset -30 yoffset -20

    group breath:
    
        attribute breath :
            "wolf_s5_breath"
        attribute breath2 :
            "wolf_s5_breath"
            zoom 1.03
            xoffset -30 yoffset -20

    group sweat:
    
        attribute sweat :
            "wolf_s5_sweat"
        attribute sweat2 :
            "wolf_s5_sweat"
            zoom 1.03
            xoffset -30 yoffset -20
    
    group bite :
    
        attribute bite :
            "wolf_s5_bite"
    
    group belly_line :
    
        attribute belly_line :
            "wolf_s5_belly2_line"
        attribute belly_line2 :
            "wolf_s5_belly2_line_add"

    group seed :
    
        attribute seed :
            "wolf_s5_seed2"
          
    group cara_seed :
    
        attribute cara_seed :
            "wolf_s5_seed_cara"
    
    group cara_seed2 :
    
        attribute cara_seed2 :
            "wolf_s5_seedleft2_cara"
    
    group cara_seed3 :
    
        attribute cara_seed3 :
            "wolf_s5_seedleft3_cara"
    
    
    group seedleft3 :
    
        attribute seedleft3 :
            "wolf_s5_seedleft3_wolf"
            zoom 1.03
            xoffset -30 yoffset -20
        attribute seedleft3_1 :
            "wolf_s5_seedleft3_wolf"
    
    group seedleft4 :
    
        attribute seedleft4 :
            "wolf_s5_seedleft4_wolf"
            zoom 1.03
            xoffset -30 yoffset -20
        attribute seedleft4_1 :
            "wolf_s5_seedleft4_wolf"

    group penisup:
    
        attribute penisup :
            "wolf_s5_penisup"


    group seed2 :
    
        attribute seed2 :
            "wolf_s5_seed3"
    
    group seed3 :
    
        attribute seed3 :
            "wolf_s5_seed4"   

    group seedleft5 :
    
        attribute seedleft5 :
            "wolf_s5_seedleft5_wolf"
            zoom 1.03
            xoffset -30 yoffset -20
        attribute seedleft5_1 :
            "wolf_s5_seedleft5_wolf"
    
    group seedleft :
    
        attribute seedleft :
            "wolf_s5_seedleft_wolf"
    
    group seedleft2 :
    
        attribute seedleft2 :
            "wolf_s5_seedleft2_wolf"

    group seed4 :
    
        attribute seed4 :
            "wolf_s5_seed"
    
    group seed5 :
    
        attribute seed5 :
            "wolf_s5_seed5"
    
    group screenseed :
    
        attribute screenseed :
            "wolf_s5_screenseed"

    group screenseed2 :
    
        attribute screenseed2 :
            "wolf_s5_screenseed2"

