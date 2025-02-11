### 画廊/手机相册 ###
init python:

    g = Gallery()

    g.button ("Help a Horse")
    g.unlock("terrance cg1 01")
    g.image("terrance cg1 01")
    g.image("terrance cg1 02")
    g.image("terrance cg1 03")
    g.image("terrance cg1 04")
    g.image("terrance cg1 05")
    g.image("terrance cg1 06")
    g.image("terrance cg1 07")
    g.image("terrance cg1 08")
    g.image("terrance cg1 09")
    g.image("terrance cg1 10a")
    g.image("terrance cg1 10b")
    g.image("terrance cg1 11a")
    g.image("terrance cg1 11b")
    g.image("terrance cg1 12")
    g.image("terrance cg1 13")
    g.image("terrance cg1 14")
    g.image("terrance cg1 15")

    g.button ("Gunther's Offer 1")
    g.unlock("gunther cg1 00")
    g.image("gunther cg1 00")
    g.image("gunther cg1 01")
    g.image("gunther cg1 02")
    g.image("gunther cg1 03")
    g.image("gunther cg1 04")
    g.image("gunther cg1 05")
    g.image("gunther cg1 06")
    g.image("gunther cg1 07")
    g.image("gunther cg1 08")
    g.image("gunther cg1 09")
    g.image("gunther cg1 10")

    g.button ("Gunther's Offer 2")
    g.unlock("gunther cg2 01")
    g.image("gunther cg2 00")
    g.image("gunther cg2 01")
    g.image("gunther cg2 02")
    g.image("gunther cg2 03")
    g.image("gunther cg2 04")
    g.image("gunther cg2 05")
    g.image("gunther cg2 06")
    g.image("gunther cg2 07")
    g.image("gunther cg2 08")
    g.image("gunther cg2 09")

    g.button ("Odachi's Work")
    g.unlock("odachi cg1 01")
    g.image("odachi cg1 01")
    g.image("odachi cg1 02")
    g.image("odachi cg1 03a")
    g.image("odachi cg1 03b")
    g.image("odachi cg1 04")
    g.image("odachi cg1 05")
    g.image("odachi cg1 06a")
    g.image("odachi cg1 06b")
    g.image("odachi cg1 07a")
    g.image("odachi cg1 07b")
    g.image("odachi cg1 08")
    g.image("odachi cg1 09")
    g.image("odachi cg1 10a")
    g.image("odachi cg1 10b")
    g.image("odachi cg1 11")
    g.image("odachi cg1 12")

    g.button ("Special Oil")
    g.unlock("marcus cg1 01")
    g.image("marcus cg1 01")
    g.image("marcus cg1 03")
    g.image("marcus cg1 02")
    g.image("marcus cg1 04a")
    g.image("marcus cg1 04b")
    g.image("marcus cg1 05a")
    g.image("marcus cg1 05b")
    g.image("marcus cg1 06a")
    g.image("marcus cg1 06b")
    g.image("marcus cg1 07a")
    g.image("marcus cg1 08a")
    g.image("marcus cg1 09")

    g.button ("Sweet Sauce")
    g.unlock("terrance cg2 00")
    g.image("terrance cg2 00")
    g.image("terrance cg2 01")
    g.image("terrance cg2 02")
    g.image("terrance cg2 03")
    g.image("terrance cg2 04")
    g.image("terrance cg2 05")
    g.image("terrance cg2 06")
    g.image("terrance cg2 07")
    g.image("terrance cg2 09")
    g.image("terrance cg2 ass01")
    g.image("terrance cg2 ass02")

    g.button ("Murry's Partners 2")
    g.unlock("murrycg1 a 00")
    g.image("murrycg1 a 00")
    g.image("murrycg1 a 01")
    g.image("murrycg1 a 01a")
    g.image("murrycg1 a 02")
    g.image("murrycg1 a 03")
    g.image("murrycg1 a 04")
    g.image("murrycg1 a 05")
    g.image("murrycg1 a 06")
    g.image("murrycg1 a 07")
    g.image("murrycg1 a 08")
    g.image("murrycg1 a 09")
    g.image("murrycg1 a 10")

    g.button ("Murry's Partners 1")
    g.unlock("murrycg1 b 00")
    g.image("murrycg1 b 00")
    g.image("murrycg1 b 01")
    g.image("murrycg1 b 01a")
    g.image("murrycg1 b 02")
    g.image("murrycg1 b 03")
    g.image("murrycg1 b 04")
    g.image("murrycg1 b 05")
    g.image("murrycg1 b 06")
    g.image("murrycg1 b 07")
    g.image("murrycg1 b 08")
    g.image("murrycg1 b 09")
    g.image("murrycg1 b 10")
    


screen gallery:

    tag menu

    use game_menu(_("Gallery")):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            has fixed:
                yfit True
                vbox:
                    grid 3 3:
                        #offset (60, 100)
                        yspacing 50
                        xspacing 25
                        vbox:
                            add g.make_button("Gunther's Offer 1", "gunther cg1 00",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2 # add g.make_button("NAME OF BUTTON","NAME OF THUMBNAIL ART",locked="NAME OF GALLERY LOCK IMAGE")
                            textbutton "Replay \"Gunther's Offer 1\"": # textbutton "Replay \"NAME OF REPLAY\""
                                xpos 0.0
                                text_size 30
                                action Replay("gunther_nsfw_01a") #action Replay("NAME OF REPLAY")

                        vbox:
                            add g.make_button("Gunther's Offer 2", "gunther cg2 01",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2 # add g.make_button("NAME OF BUTTON","NAME OF THUMBNAIL ART",locked="NAME OF GALLERY LOCK IMAGE")
                            textbutton "Replay \"Gunther's Offer 2\"": # textbutton "Replay \"NAME OF REPLAY\""
                                xpos 0.0
                                text_size 30
                                action Replay("gunther_nsfw_01b") #action Replay("NAME OF REPLAY")
                        
                        vbox:
                            add g.make_button("Help a Horse", "terrance cg1 00",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Help a horse\"":
                                xpos 0.0
                                text_size 30
                                action Replay("terrance_bond_02")

                        vbox:
                            add g.make_button("Sweet Sauce", "terrance cg2 02",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Sweet Sauce\"":
                                xpos 0.0
                                text_size 30
                                action Replay("terrance_bond_03_sex")

                        vbox:
                            add g.make_button("Odachi's Work", "odachi cg1 10a",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Odachi's Work\"":
                                xpos 0.0
                                text_size 30
                                action Replay("odachi_bond_02a")

                        vbox:
                            add g.make_button("Special Oil", "marcus cg1 04a",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Special Oil\"":
                                xpos 0.0
                                text_size 30
                                action Replay("private_bath1")

                        vbox:
                            add g.make_button("Murry's Partners 1", "murrycg1 b 00",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Murry's Partners 1\"":
                                xpos 0.0
                                text_size 30
                                action Replay("murry_partner_gatr_start")

                        vbox:
                            add g.make_button("Murry's Partners 2", "murrycg1 a 00",locked="gallery_lock", xalign=0.5, yalign=0.5) zoom 0.2
                            textbutton "Replay \"Murry's Partners 2\"":
                                xpos 0.0
                                text_size 30
                                action Replay("murry_partner_saur_start")


                        