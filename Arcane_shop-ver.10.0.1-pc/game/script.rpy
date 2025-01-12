#################### 케릭터 이미지########################


####################################
###### 주인공
####################################

image cara_earmove :
    animation
    "images/cara/c_face/base.png"
    pause 0.5
    "images/cara/c_face/eye2.png"
    pause 0.1
    "images/cara/c_face/eye3.png"
    pause 0.15        
    "images/cara/c_face/base.png"
    pause 5.0
    repeat

image cara_hood_earmove :
    animation
    "images/cara/c_face/base_hood.png"
    pause 0.5
    "images/cara/c_face/hood_eye2.png"
    pause 0.1
    "images/cara/c_face/hood_eye3.png"
    pause 0.15        
    "images/cara/c_face/base_hood.png"
    pause 5.0
    repeat


image cara_earmove_crop :
    Crop ((0, 0, 1500, 620), "cara_earmove")

image cara_talk_crop :
    Crop ((0, 600, 1500, 1000), "images/cara/c_face/talk.png")
    yoffset 600

image cara_hood_earmove_crop :
    Crop ((0, 0, 1500, 620), "cara_hood_earmove")

image cara_hood_talk_crop :
    Crop ((0, 600, 1500, 1000), "images/cara/c_face/talk_hood.png")
    yoffset 600


layeredimage cara_talk :

    group ear_eye :

        attribute ear_eye default :
            "cara_earmove_crop"
    group talk :

        attribute talk :
            "cara_talk_crop"

layeredimage cara_hood_talk :

    group ear_eye :

        attribute ear_eye default :
            "cara_hood_earmove_crop"
    group talk :

        attribute talk :
            "cara_hood_talk_crop"



layeredimage cara:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


    group background:
    
        attribute b default :
            "images/cara/c_back.png"
        attribute b_no :
            "images/cara/c_back0.png"
        
    group outfits:

        attribute am_d default :
            "images/cara/c_am.png"
        attribute am_u :
            "images/cara/c_am_up.png"
        attribute inn_d :
            "images/cara/c_in.png"
        attribute inn_u :
            "images/cara/c_in_up.png"
        attribute out_d :
            "images/cara/c_out.png"
        attribute out_u :
            "images/cara/c_out_up.png"
        attribute nake_d :
            "images/cara/c_nake.png"
        attribute nake_u :
            "images/cara/c_nake_up.png"
        attribute nake0_d :
            "images/cara/c_nake0.png"
        attribute nake0_u  :
            "images/cara/c_nake0_up.png"
        attribute hood  :
            "images/cara/c_hood.png"
        attribute hood_up  :
            "images/cara/c_hood_up.png"

    group expressions:

        attribute base default : 
            "cara_earmove"
        attribute base_hood : 
            "cara_hood_earmove"
        attribute happy :
            "images/cara/c_face/happy.png"
        attribute vhappy  :
            "images/cara/c_face/vhappy.png"
        attribute horny  :
            "images/cara/c_face/horny.png"
        attribute horny2  :
            "images/cara/c_face/horny2.png"
        attribute horny3  :
            "images/cara/c_face/horny3.png"
        attribute horny4  :
            "images/cara/c_face/horny4.png"
        attribute hurt  :
            "images/cara/c_face/hurt.png"
        attribute laugh  :
            "images/cara/c_face/laugh.png"
        attribute angry  :
            "images/cara/c_face/angry.png"
        attribute angry_hood  :
            "images/cara/c_face/angry_hood.png"
        attribute sad  :
            "images/cara/c_face/sad.png"
        attribute sad_am  :
            "images/cara/c_face/sad_am.png"
        attribute vsad  :
            "images/cara/c_face/vsad.png"
        attribute vsad_am  :
            "images/cara/c_face/vsad_am.png"
        attribute smile  :
            "images/cara/c_face/smile.png"            
        attribute talk  :
            "cara_talk talk"
        attribute talk_hood  :
            "cara_hood_talk talk"
        attribute wink  :
            "images/cara/c_face/wink.png"    
        attribute angry  :
            "images/cara/c_face/angry.png"   
        attribute angry_hood  :
            "images/cara/c_face/angry_hood.png"
        attribute angry2_hood  :
            "images/cara/c_face/angry2_hood.png"
        attribute shy  :
            "images/cara/c_face/shy.png"
        attribute shy2  :
            "images/cara/c_face/shy2.png"
        attribute sigh  :
            "images/cara/c_face/sigh.png"
        attribute sneer  :
            "images/cara/c_face/sneer.png" 
        attribute sleep  :
            "images/cara/c_face/sleep.png" 
        attribute consider  :
            "images/cara/c_face/consider.png"
        attribute consider_hood  :
            "images/cara/c_face/consider_hood.png" 
        attribute ddam  :
            "images/cara/c_face/ddam.png" 
        attribute ddam2  :
            "images/cara/c_face/ddam2.png" 
        attribute question  :
            "images/cara/c_face/question.png" 
        attribute question2  :
            "images/cara/c_face/question2.png"
        attribute exclamation  :
            "images/cara/c_face/exclamation.png"
        
        

image side cara = LayeredImageProxy("cara", Transform(crop=(0, 0, 700, 600), zoom=(0.72), xzoom = (-1.0), xoffset = -10, yoffset = 0) )


image c_locked :
    "images/cara/c_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68

####################################
###### 늑대
####################################

image wolf_earmove :
    animation
    "images/wolf/w_face/base.png"
    pause 0.5
    "images/wolf/w_face/eye.png"
    pause 0.1
    "images/wolf/w_face/eye2.png"
    pause 0.15        
    "images/wolf/w_face/base.png"
    pause 1.5
    "images/wolf/w_face/base2.png"
    pause 0.06
    "images/wolf/w_face/base3.png"
    pause 0.1
    "images/wolf/w_face/base.png"
    pause 2.5
    repeat

image wolf_earmove_crop :
    Crop ((0, 0, 1500, 530), "wolf_earmove")

image wolf_talk_crop :
    Crop ((0, 520, 1500, 1000), "images/wolf/w_face/talk.png")
    yoffset 520


image wolf_penismove :
    animation
    "images/wolf/penis1.png"
    pause 0.035
    "images/wolf/penis2.png"
    pause 0.035
    "images/wolf/penis3.png"
    pause 0.045
    "images/wolf/penis2.png"
    pause 0.055
    "images/wolf/penis1.png"
    pause 0.055
    "images/wolf/penis0.png"
    pause 0.065
    "images/wolf/penis1.png"
    pause 0.035
    "images/wolf/penis2.png"
    pause 0.045
    "images/wolf/penis1.png"  
    pause 6

    repeat

layeredimage wolf_nake :

    group body :

        attribute nake_d default :
            "images/wolf/w_nake.png"
        attribute nake_u :
            "images/wolf/w_nake_up.png"

    group penis :

        attribute penis default :
            "wolf_penismove"


layeredimage wolf_talk :

    group ear_eye :

        attribute ear_eye default :
            "wolf_earmove_crop"
    group talk :

        attribute talk :
            "wolf_talk_crop"



layeredimage wolf:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.685


    group background:
    
        attribute b default :
            "images/wolf/w_back.png"
        attribute b2  :
            "images/wolf/w_back2.png"
        attribute b_no :
            "images/wolf/w_back0.png"        

    group outfits:

        attribute am_d default :
            "images/wolf/w_am.png"
        attribute am_u :
            "images/wolf/w_am_up.png"
        attribute inn_d :
            "images/wolf/w_in.png"
        attribute inn_u :
            "images/wolf/w_in_up.png"
        attribute bulge_d :
            "images/wolf/w_bulge.png"
        attribute bulge_u :
            "images/wolf/w_bulge_up.png"
        attribute out_d :
            "images/wolf/w_out.png"
        attribute out_u :
            "images/wolf/w_out_up.png"
        attribute sword_d :
            "images/wolf/w_sword.png"
        attribute sword_u :
            "images/wolf/w_sword_up.png"
        attribute nake_d :
            "wolf_nake"
        attribute nake_u :
            "wolf_nake nake_u"
        attribute nake0_d :
            "images/wolf/w_nake0.png"
        attribute nake0_u  :
            "images/wolf/w_nake0_up.png"

    group expressions:

        attribute base default : 
            "wolf_earmove"
        attribute happy :
            "images/wolf/w_face/happy.png"
        attribute vhappy  :
            "images/wolf/w_face/vhappy.png"
        attribute horny  :
            "images/wolf/w_face/horny.png"
        attribute horny2  :
            "images/wolf/w_face/horny2.png"
        attribute horny3  :
            "images/wolf/w_face/horny3.png"
        attribute sad  :
            "images/wolf/w_face/sad.png"
        attribute sad_am  :
            "images/wolf/w_face/sad_am.png"
        attribute sad2  :
            "images/wolf/w_face/sad2.png"
        attribute sad2_am  :
            "images/wolf/w_face/sad2_am.png"
        attribute sad3  :
            "images/wolf/w_face/sad3.png"
        attribute sad3_am  :
            "images/wolf/w_face/sad3_am.png"
        attribute vsad :
            "images/wolf/w_face/vsad.png"
        attribute vsad_am :
            "images/wolf/w_face/vsad_am.png"
        attribute smile  :
            "images/wolf/w_face/smile.png"            
        attribute talk  :
            "wolf_talk talk"
        attribute wink  :
            "images/wolf/w_face/wink.png"    
        attribute angry  :
            "images/wolf/w_face/angry.png"
        attribute vangry  :
            "images/wolf/w_face/angry2.png"
        attribute pit  :
            "images/wolf/w_face/pit.png"               
        attribute shy  :
            "images/wolf/w_face/shy.png"              
        attribute shy2  :
            "images/wolf/w_face/shy2.png" 
        attribute shy3  :
            "images/wolf/w_face/shy3.png"
        attribute shy4  :
            "images/wolf/w_face/shy4.png"
        attribute shy5  :
            "images/wolf/w_face/shy5.png" 
        attribute black_eye  :
            "images/wolf/w_face/black_eye.png"         
        attribute black_eye2  :
            "images/wolf/w_face/black_eye2.png" 
        attribute fight  :
            "images/wolf/w_face/fight.png"
        attribute fight2  :
            "images/wolf/w_face/fight2.png"
        attribute fight3  :
            "images/wolf/w_face/fight3.png"
        attribute hurt  :
            "images/wolf/w_face/hurt.png"
        attribute hurt2  :
            "images/wolf/w_face/hurt2.png" 
        attribute sparkle  :
            "images/wolf/w_face/sparkle.png" 
        attribute bigeye  :
            "images/wolf/w_face/bigeye.png"
        attribute embarrass  :
            "images/wolf/w_face/embarrass.png"
        attribute sigh  :
            "images/wolf/w_face/sigh.png" 

    group redface:

        attribute red : 
            "images/wolf/w_face/red.png"
        attribute red_no : 
            "images/wolf/w_back0.png"     

    group water:

        attribute water  : 
            "images/wolf/w_water.png"

    group aura:

        attribute aura  : 
            "images/wolf/aura.png" 



image side wolf = LayeredImageProxy("wolf", Transform(crop=(0, 0, 700, 600), zoom=(0.72), xzoom = (-1.0), xoffset = -35, yoffset = 0) )

image w_locked :
    "images/wolf/w_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.685


####################################
###### 호랑이
####################################

image tiger_am_earmove :
    animation
    "images/tiger/t_face/base_am.png"
    pause 0.5
    "images/tiger/t_face/am_eye2.png"
    pause 0.1
    "images/tiger/t_face/am_eye3.png"
    pause 0.15          
    "images/tiger/t_face/base_am.png"
    pause 1.5
    "images/tiger/t_face/am_ear2.png"
    pause 0.06
    "images/tiger/t_face/am_ear3.png"
    pause 0.1
    "images/tiger/t_face/base_am.png"
    pause 0.5
    "images/tiger/t_face/am_ear4.png"
    pause 0.06
    "images/tiger/t_face/am_ear5.png"
    pause 0.1
    "images/tiger/t_face/base_am.png"
    pause 2.5
    repeat


image tiger_earmove :
    animation
    "images/tiger/t_face/base.png"
    pause 0.5
    "images/tiger/t_face/eye2.png"
    pause 0.1
    "images/tiger/t_face/eye3.png"
    pause 0.15          
    "images/tiger/t_face/base.png"
    pause 1.5
    "images/tiger/t_face/ear2.png"
    pause 0.06
    "images/tiger/t_face/ear3.png"
    pause 0.1
    "images/tiger/t_face/base.png"
    pause 0.5
    "images/tiger/t_face/ear4.png"
    pause 0.06
    "images/tiger/t_face/ear5.png"
    pause 0.1
    "images/tiger/t_face/base.png"
    pause 1.5
    repeat

image tiger_penismove :
    animation
    "images/tiger/penis1.png"
    pause 1.5
    pause 0.035
    "images/tiger/penis2.png"
    pause 0.035
    "images/tiger/penis3.png"
    pause 0.045
    "images/tiger/penis2.png"
    pause 0.055
    "images/tiger/penis1.png"
    pause 0.055
    "images/tiger/penis0.png"
    pause 0.065
    "images/tiger/penis1.png"
    pause 0.035
    "images/tiger/penis2.png"
    pause 0.045
    "images/tiger/penis1.png"  
    pause 4.5

    repeat

layeredimage tiger_nake :

    group body :

        attribute nake_d default :
            "images/tiger/t_nake.png"
        attribute nake_u :
            "images/tiger/t_nake_up.png"

    group penis :

        attribute penis default :
            "tiger_penismove"


image tiger_am_earmove_crop :
    Crop ((0, 0, 1500, 450), "tiger_am_earmove")

image tiger_am_talk_crop :
    Crop ((0, 450, 1500, 1000), "images/tiger/t_face/talk_am.png")
    yoffset 450

image tiger_earmove_crop :
    Crop ((0, 0, 1500, 450), "tiger_earmove")

image tiger_talk_crop :
    Crop ((0, 450, 1500, 1000), "images/tiger/t_face/talk.png")
    yoffset 450


layeredimage tiger_am_talk :

    group ear_eye :

        attribute ear_eye default :
            "tiger_am_earmove_crop"
    group talk :

        attribute talk :
            "tiger_am_talk_crop"

layeredimage tiger_talk :

    group ear_eye :

        attribute ear_eye default :
            "tiger_earmove_crop"
    group talk :

        attribute talk :
            "tiger_talk_crop"


layeredimage tiger:

    zoom 0.478
    xcenter 0.5
    ycenter 0.685

    group background:
    
        attribute b default :
            "images/tiger/t_back.png"
        attribute b_no :
            "images/tiger/t_back0.png"  

    group outfits:

        attribute am_d default :
            "images/tiger/t_am.png"
        attribute am_u :
            "images/tiger/t_am_up.png"
        attribute inn_d :
            "images/tiger/t_in.png"
        attribute inn_u :
            "images/tiger/t_in_up.png"
        attribute bulge_d :
            "images/tiger/t_bulge.png"
        attribute bulge_u :
            "images/tiger/t_bulge_up.png"
        attribute out_d :
            "images/tiger/t_out.png"
        attribute out_u :
            "images/tiger/t_out_up.png"
        attribute nake_d :
            "tiger_nake"
        attribute nake_u :
            "tiger_nake nake_u"
        attribute nake0_d :
            "images/tiger/t_nake0.png"
        attribute nake0_u  :
            "images/tiger/t_nake0_up.png"

    group expressions:

        attribute base_am default : 
            "tiger_am_earmove"
        attribute base :
            "tiger_earmove"
        attribute happy :
            "images/tiger/t_face/happy.png"
        attribute happy_am :
            "images/tiger/t_face/happy_am.png"
        attribute happy2 :
            "images/tiger/t_face/happy2.png"
        attribute happy2_am :
            "images/tiger/t_face/happy2_am.png"
        attribute vhappy  :
            "images/tiger/t_face/vhappy.png"
        attribute vhappy_am  :
            "images/tiger/t_face/vhappy_am.png"
        attribute laugh  :
            "images/tiger/t_face/laugh.png"
        attribute laugh_am  :
            "images/tiger/t_face/laugh_am.png"
        attribute horny  :
            "images/tiger/t_face/horny.png"
        attribute horny_am  :
            "images/tiger/t_face/horny_am.png"
        attribute horny2  :
            "images/tiger/t_face/horny2.png"
        attribute horny2_am  :
            "images/tiger/t_face/horny2_am.png"
        attribute horny3  :
            "images/tiger/t_face/horny3.png"
        attribute horny3_am :
            "images/tiger/t_face/horny3_am.png"
        attribute sad  :
            "images/tiger/t_face/sad.png"
        attribute sad_am  :
            "images/tiger/t_face/sad_am.png"
        attribute sad2  :
            "images/tiger/t_face/sad2.png"
        attribute sad2_am  :
            "images/tiger/t_face/sad2_am.png"
        attribute sad3  :
            "images/tiger/t_face/sad3.png"
        attribute sad3_am  :
            "images/tiger/t_face/sad3_am.png"
        attribute sleep  :
            "images/tiger/t_face/eye3.png"
        attribute sleep_am  :
            "images/tiger/t_face/eye3_am.png"
        attribute embarrass  :
            "images/tiger/t_face/embarrass.png"
        attribute embarrass_am  :
            "images/tiger/t_face/embarrass_am.png"
        attribute vsad :
            "images/tiger/t_face/vsad.png"
        attribute vsad_am  :
            "images/tiger/t_face/vsad_am.png"
        attribute smile  :
            "images/tiger/t_face/smile.png"     
        attribute smile_am  :
            "images/tiger/t_face/smile_am.png"
        attribute smile2  :
            "images/tiger/t_face/smile2.png"     
        attribute smile2_am  :
            "images/tiger/t_face/smile2_am.png"  
        attribute talk  :
            "tiger_talk talk"
        attribute talk_am  :
            "tiger_am_talk talk"
        attribute wink  :
            "images/tiger/t_face/wink.png"    
        attribute wink_am  :
            "images/tiger/t_face/wink_am.png"  
        attribute angry  :
            "images/tiger/t_face/angry.png"   
        attribute angry_am  :
            "images/tiger/t_face/angry_am.png" 
        attribute vangry  :
            "images/tiger/t_face/vangry.png"   
        attribute vangry_am  :
            "images/tiger/t_face/vangry_am.png"
        attribute fight  :
            "images/tiger/t_face/fight.png"
        attribute fight_am  :
            "images/tiger/t_face/fight_am.png"
        attribute fight2  :
            "images/tiger/t_face/fight2.png"
        attribute fight2_am  :
            "images/tiger/t_face/fight2_am.png"
        attribute fight3  :
            "images/tiger/t_face/fight3.png"
        attribute fight3_am  :
            "images/tiger/t_face/fight3_am.png"
        attribute shy  :
            "images/tiger/t_face/shy.png"        
        attribute shy_am  :
            "images/tiger/t_face/shy_am.png"        
        attribute shy2  :
            "images/tiger/t_face/shy2.png" 
        attribute shy2_am  :
            "images/tiger/t_face/shy2_am.png"
        attribute sleep  :
            "images/tiger/t_face/sleep.png" 
        attribute sleep_am  :
            "images/tiger/t_face/sleep_am.png"
        attribute sigh  :
            "images/tiger/t_face/sigh.png" 
        attribute sigh_am  :
            "images/tiger/t_face/sigh_am.png"
        attribute consider  :
            "images/tiger/t_face/consider.png" 
        attribute consider_am  :
            "images/tiger/t_face/consider_am.png"
        attribute consider2  :
            "images/tiger/t_face/consider2.png" 
        attribute consider2_am  :
            "images/tiger/t_face/consider2_am.png"

    group redface:

        attribute red : 
            "images/tiger/t_face/red.png"
        attribute red_laugh : 
            "images/tiger/t_face/red_laugh.png"
        attribute red_no : 
            "images/tiger/t_back0.png" 

    group water:

        attribute water  : 
            "images/tiger/t_water.png"             


image side tiger = LayeredImageProxy("tiger", Transform(crop=(0, 0, 1000, 600), zoom=(0.73), xoffset = -200, yoffset = 0) )

image t_locked :
    "images/tiger/t_locked.png"
    zoom 0.478
    xcenter 0.5
    ycenter 0.685


####################################
###### 곰
####################################


layeredimage bear:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


    group background:
    
        attribute b default :
            "images/bear/b_back.png"   
        attribute b_no :
            "images/bear/b_back0.png"  


    group outfits:

        attribute am_d default :
            "images/bear/b_am.png"
        attribute am_u :
            "images/bear/b_am_up.png"
        attribute inn_d :
            "images/bear/b_in.png"
        attribute inn_u :
            "images/bear/b_in_up.png"
        attribute out_d :
            "images/bear/b_out.png"
        attribute out_u :
            "images/bear/b_out_up.png"
        attribute nake_d :
            "images/bear/b_nake.png"
        attribute nake_u :
            "images/bear/b_nake_up.png"
        attribute nake0_d :
            "images/bear/b_nake0.png"
        attribute nake0_u  :
            "images/bear/b_nake0_up.png"
        attribute upnake_d  :
            "images/bear/b_upnake.png"
        attribute upnake_u  :
            "images/bear/b_upnake_up.png"

    group expressions:

        attribute base default : 
            "images/bear/b_face/base.png"
        attribute happy :
            "images/bear/b_face/happy.png"
        attribute vhappy  :
            "images/bear/b_face/vhappy.png"
        attribute laugh  :
            "images/bear/b_face/laugh.png"
        attribute horny  :
            "images/bear/b_face/horny.png"
        attribute horny2  :
            "images/bear/b_face/horny2.png"
        attribute horny3  :
            "images/bear/b_face/horny3.png"
        attribute sad  :
            "images/bear/b_face/sad.png"
        attribute vsad :
            "images/bear/b_face/vsad.png"
        attribute smile  :
            "images/bear/b_face/smile.png"            
        attribute talk  :
            "images/bear/b_face/talk.png"
        attribute angry  :
            "images/bear/b_face/angry.png"   
        attribute vangry  :
            "images/bear/b_face/vangry.png"   
        attribute embrass  :
            "images/bear/b_face/embrass.png"  
        attribute embrass2  :
            "images/bear/b_face/embrass2.png"
        attribute embrass3  :
            "images/bear/b_face/embrass3.png"
        attribute embrass4  :
            "images/bear/b_face/embrass4.png" 
        attribute shy  :
            "images/bear/b_face/shy.png"              
        attribute sigh  :
            "images/bear/b_face/sigh.png"
        attribute sparkle  :
            "images/bear/b_face/sparkle.png"
        attribute pain  :
            "images/bear/b_face/pain.png"

    group weapon:

        attribute knuckle : 
            "images/bear/knuckle.png"

    group staff:

        attribute staff_d : 
            "images/bear/staff.png"
        attribute staff_u : 
            "images/bear/staff_up.png"
        attribute staff2_d : 
            "images/bear/staff2.png"
        attribute staff2_u : 
            "images/bear/staff2_up.png"

    group water:

        attribute water  : 
            "images/bear/b_water.png"




image staff_d :
    "images/bear/staff.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68

image staff_u :
    "images/bear/staff_up.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68

image staff2_d :
    "images/bear/staff2.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68

image staff2_u :
    "images/bear/staff2_up.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68

image b_locked :
    "images/bear/b_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68



image side bear = LayeredImageProxy("bear", Transform(crop=(0, 0, 900, 670), zoom=(0.72), xoffset = -195, yoffset = 0) )



####################################
###### 용
####################################


layeredimage dragon:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.685


    group background:
    
        attribute b default :
            "images/dragon/d_back.png"
        attribute b_no :
            "images/dragon/d_back0.png"  

    group outfits:

        attribute am_d default :
            "images/dragon/d_am.png"
        attribute am_u :
            "images/dragon/d_am_up.png"
        attribute out_d :
            "images/dragon/d_out.png"
        attribute out_u :
            "images/dragon/d_out_up.png"
        attribute nake_d :
            "images/dragon/d_nake.png"
        attribute nake_u :
            "images/dragon/d_nake_up.png"
        attribute nake0_d :
            "images/dragon/d_nake0.png"
        attribute nake0_u  :
            "images/dragon/d_nake0_up.png"

    group expressions:

        attribute base default : 
            "images/dragon/d_face/base.png"
        attribute base_out : 
            "images/dragon/d_face/base_out.png"
        attribute angry :
            "images/dragon/d_face/angry.png"
        attribute angry_out :
            "images/dragon/d_face/angry_out.png"
        attribute dissappoint :
            "images/dragon/d_face/dissappoint.png"
        attribute dissappoint_out :
            "images/dragon/d_face/dissappoint_out.png"
        attribute happy :
            "images/dragon/d_face/happy.png"
        attribute happy_out :
            "images/dragon/d_face/happy_out.png"
        attribute horny :
            "images/dragon/d_face/horny.png"
        attribute horny_out :
            "images/dragon/d_face/horny_out.png"
        attribute horny2 :
            "images/dragon/d_face/horny2.png"
        attribute horny2_out :
            "images/dragon/d_face/horny2_out.png"
        attribute horny3 :
            "images/dragon/d_face/horny3.png"
        attribute horny3_out :
            "images/dragon/d_face/horny3_out.png"
        attribute laugh :
            "images/dragon/d_face/laugh.png"
        attribute laugh_out :
            "images/dragon/d_face/laugh_out.png"
        attribute sad :
            "images/dragon/d_face/sad.png"
        attribute sad_out :
            "images/dragon/d_face/sad_out.png"
        attribute sigh :
            "images/dragon/d_face/sigh.png"
        attribute sigh_out :
            "images/dragon/d_face/sigh_out.png"
        attribute sleep :
            "images/dragon/d_face/sleep.png"
        attribute sleep_out :
            "images/dragon/d_face/sleep_out.png"    
        attribute smile :
            "images/dragon/d_face/smile.png"
        attribute smile_out :
            "images/dragon/d_face/smile_out.png"
        attribute talk :
            "images/dragon/d_face/talk.png"
        attribute talk_out :
            "images/dragon/d_face/talk_out.png"
        attribute vhappy :
            "images/dragon/d_face/vhappy.png"
        attribute vhappy_out :
            "images/dragon/d_face/vhappy_out.png"
        attribute vsad :
            "images/dragon/d_face/vhappy.png"
        attribute vsad_out :
            "images/dragon/d_face/vsad_out.png"
        attribute wink :
            "images/dragon/d_face/wink.png"
        attribute wink_out :
            "images/dragon/d_face/wink_out.png"


image d_locked :
    "images/dragon/d_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.685



image side dragon = LayeredImageProxy("dragon", Transform(crop=(0, 0, 800, 600), zoom=(0.72), xzoom = (-1.0), xoffset = -45, yoffset = 2) )

####################################
##### 길드 접수원
####################################

layeredimage lucas:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


    group background:
    
        attribute b default :
            "images/lucas/l_back.png"
        attribute b_no :
            "images/lucas/l_back0.png"
        
    group outfits:

        attribute am_d default :
            "images/lucas/l_nopage.png"
        attribute am_u :
            "images/lucas/l_nopage_up.png"
        attribute page_d :
            "images/lucas/l_page.png"
        attribute page_u :
            "images/lucas/l_page_up.png"

    group expressions:

        attribute base default : 
            "images/lucas/l_face/base.png"
        attribute drunk :
            "images/lucas/l_face/drunk.png"
        attribute embarrass  :
            "images/lucas/l_face/embarrass.png"
        attribute embarrass2  :
            "images/lucas/l_face/embarrass2.png"
        attribute sad  :
            "images/lucas/l_face/sad.png"
        attribute sad2  :
            "images/lucas/l_face/sad2.png"
        attribute talk : 
            "images/lucas/l_face/talk.png"
        

image side lucas = LayeredImageProxy("lucas", Transform(crop=(0, 0, 700, 700), zoom=(0.72), xzoom = (-1.0), xoffset = -25, yoffset = 40) )

image l_locked :
    "images/lucas/l_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


####################################
##### 동방 상인
####################################

layeredimage ahjin:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


    group background:
    
        attribute b default :
            "images/ahjin/a_back.png"
        attribute b_no :
            "images/ahjin/a_back0.png"
        
    group outfits:

        attribute am_d default :
            "images/ahjin/a_base.png"
        attribute am_u :
            "images/ahjin/a_base_up.png"

    group expressions:

        attribute base default : 
            "images/ahjin/a_face/base.png"
        attribute consider :
            "images/ahjin/a_face/consider.png"
        attribute eye_bright  :
            "images/ahjin/a_face/eye_bright.png"
        attribute open  :
            "images/ahjin/a_face/open.png"
        attribute talk  :
            "images/ahjin/a_face/talk.png"
        attribute talk2  :
            "images/ahjin/a_face/talk2.png"

        

image side ahjin = LayeredImageProxy("ahjin", Transform(crop=(0, 0, 800, 700), zoom=(0.72), xzoom = (1.0), xoffset = -200, yoffset = 40) )

image a_locked :
    "images/ahjin/a_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


####################################
##### 기사단 부단장
####################################

layeredimage theo:
   
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


    group background:
    
        attribute b default :
            "images/theo/th_back.png"
        attribute b_no :
            "images/theo/th_back0.png"
        
    group outfits:

        attribute am_d default :
            "images/theo/th_base.png"
        attribute am_u :
            "images/theo/th_base_up.png"

    group expressions:

        attribute base default : 
            "images/theo/th_face/base.png"
        attribute drunk :
            "images/theo/th_face/drunk.png"
        attribute embarrass  :
            "images/theo/th_face/embarrass.png"
        attribute embarrass2  :
            "images/theo/th_face/embarrass2.png"
        attribute sad  :
            "images/theo/th_face/sad.png"
        attribute sad2  :
            "images/theo/th_face/sad2.png"
        attribute smile  :
            "images/theo/th_face/smile.png"
        attribute talk : 
            "images/theo/th_face/talk.png"
        attribute disapprove : 
            "images/theo/th_face/disapprove.png"
        

image side theo = LayeredImageProxy("theo", Transform(crop=(20, 0, 700, 700), zoom=(0.68), xzoom = (-1.0), xoffset = 0, yoffset = 40) )

image th_locked :
    "images/theo/th_locked.png"
    zoom 0.47
    xcenter 0.5
    ycenter 0.68


layeredimage mob:
   
    zoom 0.475
    xcenter 0.5
    ycenter 0.685
        
    group characters :

        attribute cat :
            "images/mob/cat.png"
        attribute boar :
            "images/mob/boar.png"
        attribute knights :
            "images/mob/knights.png"

layeredimage mob2:
   
    zoom 0.475
    xcenter 0.5
    ycenter 0.685
        
    group characters :

        attribute cat :
            "images/mob/cat.png"
        attribute boar :
            "images/mob/boar.png"
        attribute knights :
            "images/mob/knights.png"

##CTC 이미지 ####################################################

image ctc_blink:
    "gui/ctc.png"
    zoom 0.07
    xpos 0.9
    ypos 0.335
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat 


##케릭터 정의
define c = Character(_('[pl_name]'), color="#2d358a", image="cara", ctc="ctc_blink", ctc_position="nestled")
define w = Character(_('가헬'), color="#921e60", image="wolf", ctc="ctc_blink", ctc_position="nestled")
define t = Character(_('엘레드'), color="#c57710", image="tiger", ctc="ctc_blink", ctc_position="nestled")
define b = Character(_('바토'), color="#1a8a6a", image="bear", ctc="ctc_blink", ctc_position="nestled")
define d = Character(_('류호'), color="#0c2283", image="dragon", ctc="ctc_blink", ctc_position="nestled")
define narrator = Character(None, what_color = "#ffffff", ctc="ctc_blink", ctc_position="nestled")


##사이드 케릭터들
define n = Character(_('???'), color="#272727", image="npc", ctc="ctc_blink", ctc_position="nestled")
define l = Character(_('루카스'), color="#2e701a", image="lucas", ctc="ctc_blink", ctc_position="nestled")
define a = Character(_('아진'), color="#541919", image="ahjin", ctc="ctc_blink", ctc_position="nestled")
define th = Character(_('테오'), color="#070707", image="theo", ctc="ctc_blink", ctc_position="nestled")

##모브 케릭터들
define mob = Character(_('용병1'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")
define mob2 = Character(_('용병2'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")
define knight = Character(_('기사1'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")
define knight2 = Character(_('기사2'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")
define knight3 = Character(_('기사3'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")
define knights = Character(_('기사들'), color="#272727", image="mob", ctc="ctc_blink", ctc_position="nestled")


#케릭터 이름 입력
define gui.input_text_color = "#70aee5" 


###########################################################
## ALT effect #############################################
###########################################################


transform scene_vmove (time, first, dist):
    yoffset first
    ease time yoffset dist

transform scene_hmove (time, first, dist):
    xoffset first
    ease time xoffset dist


transform hshake (time, first, dist):
    xoffset first
    linear time xoffset (first - dist)
    pause time
    linear time xoffset (first + dist)
    pause time
    linear time xoffset (first - dist)
    pause time
    linear time xoffset (first + dist)
    pause time
    linear time xoffset first

transform vshake (time, first, dist):
    yoffset first
    linear time yoffset (first - dist)
    pause time
    linear time yoffset (first + dist)
    pause time
    linear time yoffset (first - dist)
    pause time
    linear time yoffset (first + dist)
    pause time
    linear time yoffset first

transform walk (end, time, step):

    parallel:
        ease time xoffset end
    parallel:
        block:
            ease (time/step*0.27) yoffset 19 # will move the character up and down while he's "walking"
            ease (time/step*0.73) yoffset 0
            repeat step # number of "steps". May be adjusted

transform walk2 (end, time, step):

    parallel:
        ease time xoffset end
    parallel:
        block:
            ease (time/step*0.27) yoffset 19+135 # will move the character up and down while he's "walking"
            ease (time/step*0.73) yoffset 135
            repeat step # number of "steps". May be adjusted
        
transform fwalk :

    parallel:
        ease 1.99 zoom 1.22

    parallel:
        ease (0.13) yoffset 15
        ease (0.33) yoffset 6
        ease (0.18) yoffset 59
        ease (0.33) yoffset (59-14)
        ease (0.19) yoffset (115)
        ease (0.32) yoffset (115-14)
        ease (0.19) yoffset (153)
        ease (0.32) yoffset (135) ##-18

transform fwalk2 :

    parallel:
        ease 2.00 zoom 1.47

    parallel:
        ease (0.16) yoffset 40
        ease (0.30) yoffset 30
        ease (0.19) yoffset 112
        ease (0.33) yoffset (112-22)
        ease (0.19) yoffset (185)
        ease (0.32) yoffset (185-22)
        ease (0.19) yoffset (235)
        ease (0.32) yoffset (235-26)
        
transform bwalk :

    parallel:
        ease 1.98 zoom 1

    parallel:
        ease (0.13) yoffset 160
        ease (0.33) yoffset 80
        ease (0.17) yoffset 123
        ease (0.33) yoffset 50
        ease (0.19) yoffset 92
        ease (0.32) yoffset 23
        ease (0.19) yoffset 43
        ease (0.32) yoffset 0

transform cloud_rise:
    parallel:
        ease 3.0 xoffset -30 
        ease 1 zoom 1.15 xoffset -600 yoffset -100
    parallel:
        ease 0.3 alpha 1.0 
        ease 2.7 alpha 1.0
        ease 1 alpha 0.0 

transform cloud_rise2:
    parallel:
        ease 2.5 xoffset 30  
        ease 1 zoom 1.15 xoffset 300 yoffset -130 

    parallel:
        ease 0.3 alpha 1.0 
        ease 2.2 alpha 1.0
        ease 1 alpha 0.0 

transform cloud_rise3:
    parallel:
        ease 2.0 xoffset -30  
        ease 1 zoom 1.15 xoffset -700 yoffset -180 

    parallel:
        ease 0.3 alpha 1.0 
        ease 1.7 alpha 1.0 
        ease 1 alpha 0.0 

transform cloud_show:
    alpha 0.0
    pause 2.5
    ease 1.8 alpha 1.0

transform light_move:
    xoffset 1000
    yoffset 1100

    parallel:
        rotate_pad True
        transform_anchor True
        anchor (0.5, 1.0)
        ease 2 rotate 90
        rotate 0
        repeat 4

    parallel:
        alpha 0
        ease 1.0 alpha 0.8 
        ease 0.5 alpha 0.8
        ease 0.5 alpha 0.0
        repeat 4

transform light_move2:
    xoffset 1000
    yoffset 1100

    parallel:
        rotate_pad True
        transform_anchor True
        anchor (0.5, 1.0)
        ease 1.5 rotate 120
        rotate 0
        repeat 4

    parallel:
        alpha 0
        ease 1.0 alpha 0.8
        ease 0.5 alpha 0.0
        repeat 4

transform light_move3:
    xoffset -400
    yoffset -50

    parallel:
        ease 2.5 zoom 1.6 xoffset -1200 yoffset -1400
        zoom 1
        xoffset -400
        yoffset -100
        repeat 3

    parallel:
        alpha 0
        ease 1.2 alpha 0.8
        ease 1.3 alpha 0
        repeat 3


transform charm_move (start, end, size):

    xoffset start

    parallel:
        block:
            ease 0.6 yoffset -10
            ease 0.6 yoffset 10
            repeat

    parallel:
        alpha 0
        ease 0.6 alpha 1

    parallel:
        ease 1.8 xoffset end zoom (size)


transform sigh_move (start, start2):

    xoffset start
    yoffset start2

    parallel:
        alpha 1
        ease 0.6 alpha 1
        ease 0.6 alpha 0

    parallel:
        ease 1.2 xoffset (start-50) yoffset (start2+50)

transform sigh_move2 (start, start2):

    xoffset start
    yoffset start2

    parallel:
        alpha 1
        ease 0.6 alpha 1
        ease 0.6 alpha 0

    parallel:
        ease 1.2 xoffset (start+50) yoffset (start2+50)


transform question_move (start, start2):

    xoffset start
    yoffset start2
    
    easein 0.2 rotate 40
    easeout 0.1   rotate -30
    easein 0.1 rotate 0

transform cloud_gold_move (start, end):
    xoffset start

    parallel:
        ease 1 xoffset end
    
    parallel:
        alpha 0
        ease 0.8 alpha 1
        

transform ddam_move (start, start2):
    xoffset start
    yoffset start2

    ease 1 yoffset (start2+40)

transform exclamation_move (start, start2):

    xoffset start
    yoffset start2
    
    parallel:
        linear 0.1 xoffset (start+10) 
        linear 0.1 xoffset (start-10)
        linear 0.1 xoffset (start+10) 
        linear 0.1 xoffset (start)

transform surprise_move :

    linear 0.1 yoffset -10
    linear 0.1 yoffset 10
    linear 0.1 yoffset 0

transform surprise_move2 :

    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset 0

transform size_up:
    xcenter 0.5
    ycenter 0.77 
    zoom 0.55

transform flash:
    on show:
        alpha 0.0
        linear 2.5 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform flash_fast:
    on show:
        alpha 0.0
        linear 0.95 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform slash:
    on show:
        alpha 0.0
        ease 0.2 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform slash2:
    on show:
        alpha 0.0
        ease 0.28 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform magic:
    on show:
        alpha 0.0
        ease 0.2 alpha 1.0
    on hide:
        ease 0.7 alpha 0.0

transform slide_right:
    xpos -1.6
    ypos -1.0
    ease 0.6 xpos 1.0 ypos 0.5

transform slide_right2:
    xpos -1.6
    ypos -1.0
    ease 0.5 xpos 1.0 ypos 0.5

transform magic_up:
    alpha 0.0 zoom 1.0 xpos 0 ypos 0
    ease 2.5 alpha 0.4 zoom 1.1 xpos -90 ypos -50
    ease 0.2 alpha 0.0

transform talk_move :
        ease 0.15 yoffset -15
        ease 0.15 yoffset 0

transform talk_frontmove :
        ease 0.15 yoffset -15+135
        ease 0.15 yoffset 135

######################## 단순 ######################################

transform down:
    yoffset 100

transform slow_down:
    yoffset -250
    ease 2 yoffset 0

transform up:
    yoffset -100

transform slow_up:
    yoffset 0
    ease 2 yoffset -250

transform normal:
    xoffset 0
    yoffset 0
    zoom 1

transform mirror: 
    xzoom -1.0

transform mirror2: 
    xzoom 1.0

transform flip: 
    ease 0.4 xzoom -1.0

transform flip2: 
    ease 0.4 xzoom 1.0

transform change(extend, dist, dist2):
    zoom extend
    xoffset dist
    yoffset dist2

transform right:
    xoffset 500  

transform left:
    xoffset -500

transform center:
    xcenter 0.5
    ycenter 0.68

transform nod:
    ease 0.2 yoffset 10
    ease 0.2 yoffset 0

transform nod_big:
    ease 0.2 yoffset 15
    ease 0.2 yoffset 0
    

################################################
############### Transform legacy ###############
################################################

transform size_fit: 
    zoom 0.47

transform larger_down:
    yoffset 250

transform larger_normal:
    yoffset 135
    
transform center_l: 
    xcenter 0.25
    ycenter 0.68         

transform center_r: 
    xcenter 0.75
    ycenter 0.68 
 

################################################
################################################



### 이름에 따른 조사 변경

init python:
    if renpy.game.preferences.language in [None, ""]:
        default_name = "레스크"
    else:
        default_name = "Resque"


init python:
    def choose_josa(name, type="은/는"):
        jong = (ord(name[-1]) - 0xAC00) % 28

        if type == "은/는":
            return '은' if jong else '는'
        elif type == "이/가":
            return '이' if jong else '가'
        elif type == "을/를":
            return '을' if jong else '를'
        elif type == "와/과":
            return '과' if jong else '와'
        elif type == "로/으로":
            if jong == 0:  # 종성이 없음
                return '로'
            elif jong in [8, 17]:  # 종성이 ㄹ
                return '로'
            else:  # 그 외의 경우
                return '으로'
        elif type == "라/이라":
            return '이라' if jong else '라'
        elif type == "이다/다":
            return '이다' if jong else '다'
        

###################################
# 여기에서부터 게임이 시작합니다.
###################################


label splashscreen:
    
    scene bg backcol
    with Pause(1)

    show logo :
        xcenter 0.5
        ycenter 0.5  
    with dissolve
    with Pause(2)

    hide logo with dissolve
    with Pause(1)

    show text "Ronci14 presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    return


#스타트##############################################################################

screen name_input(message=_("이름을 입력하세요.")):
    modal True
    
    frame:
        style_prefix "confirm"
        xalign 0.5
        yalign 0.5
        xsize 2000  # 박스의 너비 설정
        ysize 400  # 박스의 높이 설정
        background Solid("#0000009c")  # 박스의 배경으로 Solid 적용
    
        vbox:
            xalign 0.5
            spacing 30
            
            label message:
                xalign 0.5
                text_color "#ffffff"
            
            input:
                value VariableInputValue("pl_name")
                length 10
                default default_name
                allow ""
            
            # 확인 버튼
            textbutton _("확인") action Return() xalign 0.5


#이름 정하기#########################################################################
label start:
    stop music fadeout 2.5
    scene bg backcol
    with dissolve

    $ default_name = "Resque" if renpy.game.preferences.language else "레스크"

    "당신의 이름은 무엇인가요?"

    call screen name_input

    # $ pl_name = renpy.input(_("이름을 입력하세요."), length=10, default=default_name).strip()

    if pl_name == "":
        $ pl_name = default_name

    # 이름 확인 선택지
    label confirm_name:
        
        $ josa_eun_neun = choose_josa(pl_name, "은/는")
        $ josa_i_ga = choose_josa(pl_name, "이/가")
        $ josa_eul_reul = choose_josa(pl_name, "을/를")
        $ josa_wa_gwa = choose_josa(pl_name, "와/과")
        $ josa_ro_euro = choose_josa(pl_name, "로/으로")
        $ josa_ra_ira = choose_josa(pl_name, "라/이라")
        $ josa_ida_da = choose_josa(pl_name, "이다/다")

        "{color=#70aee5}\'[pl_name]\'{/color}[josa_i_ga] 맞습니까?"

        menu:
            "예, 맞습니다.":
                "좋습니다! 게임을 시작합니다, {color=#70aee5}\'[pl_name]\'{/color}님!"
                jump game_start

            "아니요, 다시 입력할게요.":
                call screen name_input(_("다시 이름을 입력하세요."))
                if pl_name == "":
                    $ pl_name = default_name
                jump confirm_name