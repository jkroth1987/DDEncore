#This is a copy of credits.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Import the datetime library for using time
init python:
    import datetime

    # To find the amount of time it should take for a block to go by,
    # divide the number of pixels it needs to move by 75.
    # Add 50 pixels per line after the first.
    #
    # Ex: 1620 / 75 = 21.6 seconds, rounded to 21.5

    # 1
    # 6 lines, +250 pixels
    c_text_1 = """Created and Directed By: Andrew J. Striedl
Writers: Agent Gold, Bug, Nick (Canad1an),
Rose, Ploxmaster708, Rudy, Andrew J. Striedl
Writing Contributors: Olivia Norton, Jacob Smallman
Artists: 3Monika4 (Monika), Elaina Sasso,
Kent Stone, SkynnarahSerenity49"""

    # 2
    # 6 lines, +250 pixels
    c_text_2 = """Coders: Agent Gold, Bug, Nico, Andrew J. Striedl\n
Coding Contributor: POBAW
General Contributions: Nep, Rezzy
Image Editing: POBAW, TheD0ctor,
Agent Gold, Andrew J. Striedl

Music: Daniel Kruyer (Angelic Beast)"""

    # 3
    # 5 lines, +200 pixels
    c_text_3 = """Sayori as Sayori
Natsuki as Natsuki
Yuri as Yuri
Monika as Monika
The MC as [player]""" # This will be re-defined lower down--if adjustments are needed, adjust that one!

    # 4
    # 6 lines, +250 pixels
    c_text_4 = """Special Thanks: Afrozer0 & Monika, Agent Gold, American Eagle, Astranova,
Blaze Bringer, BronzeBrawn, Bug, huser Entertainment,
Jacob Smallman, Kuudere Ghost, POBAW, Noa_AT, Orber,
Ploxmaster708, SaturnGamer72, Ronald McOnePuch, SlightlySimple,
Spaghetto, Sir Swampert, Olivia Norton


Life Saver: Agent Gold"""

    # 5
    # 6 lines, +250 pixels
    c_text_5 = """Inspired By: Dan Salvato

Inspired By:
Doki Doki: The Festival
Doki Doki: Exit Music
Doki Doki: Literature Club"""

    # 6
    # 4 lines, +150 pixels
    c_text_6 = """Assets Used

Ren'py Scripts: \"Script to make the dokies lean
forward then they talk\" by TSS~Danny#2610 (Discord)"""

    # 7
    # 29 lines, +1400 pixels
    c_text_7 = """Backgrounds Used

\"MC_Living_room_afternoon by Nuxill#7870.png\"
by Nuxill#7870(Discord) [[Community Asset Folder]

\"MC_Living_room_daytime by Nuxill#7870.png\"
by Nuxill#7870(Discord) [[Community Asset Folder]

\"Protagonist_Bedroom_Night by Alex.png\"
by Alex [[ORG]#9077(Discord) [[Community Asset Folder]

\"encoretextbox.png\" by TheD0ct0r#8275(Discord)

residential_dusk by SovietSpartan
closet_dark by POBAW
club_nothing by The Monika Before Story Team
closet_dark by Agent Gold
n_void_1 by Agent Gold

TV BG: https://images.freecreatives.com/wp-content/uploads/2016/06/Television-Display-Mock-up.jpg
rainbow_road1.png: https://wii.fandom.com/wiki/Rainbow_Road
rainbow_road2.png: Source Unknown
rainbow_road3.png: https://youtu.be/3KnriAbihms
rainbow_road4.png: https://youtu.be/3TA6rVtB28w
Daisy for CGs: https://www.pinterest.com/pin/453878468671138996/

bg void: www.videoblocks.com
bg void_2 b Kent Stone
Void Door: https://icouldcrybutidonthavetime.files.wordpress.com/2014/10/doors.jpg"""

    # 8
    # 41 lines, +2000 pixels
    c_text_8 = """Audio Used

Main Menu Theme \"Doki Doki Forever\"
sung by OR3O ft. rachie, Chi-chi, Kathy-chan★
-'OR3O' (Monika) : https://bit.ly/2mZJhiS
-'rachie' (Sayori) : https://www.youtube.com/user/splendiferousfantasy/
-'Kathy' (Yuri) : https://www.youtube.com/user/animerocker246
-'Chi-Chi' (Natsuki) : https://www.youtube.com/user/chisanaAi
-Lyrics, Melody: OR3O
-Additional Assistance: Genuine Music
https://www.youtube.com/user/JNguyenMusic1
-Links:
SPOTIFY: https://open.spotify.com/album/5jUz1WljGky4hbD3K0XMd0
SOUNDCLOUD: https://bit.ly/2QebCyi
ITUNES: https://apple.co/2yPipYr
AMAZON: https://www.amazon.com/gp/product/B078MFKXTQ

*\"Knocking On Door-SoundBible.com-84643603.mp3\" from
http://soundbible.com/1196-Knocking-On-Door.html
(converted to .ogg by Bug)

daudio.school: By Hajgare PaKufi on YouTube
(converted to .ogg by Andrew)

audio.fingersnap: By GamingSoundEffects on YouTube
(converted to .ogg by Andrew)

audio.bone: By SoundEffectsFactory on YouTube
(converted to .ogg by Andrew)

audio.neck: From Doki Doki Literature Club
(edited By Andrew)

audio.knife: By Soundchips on YouTube
(converted to .ogg by Andrew)

audio.stab: By SoundEffectsFactory on YouTube
(converted to .ogg by Andrew)

audio.drop: Public Domain
(converted to .ogg by Agent Gold)"""

    # 9
    # 5 lines, +200 pixels
    c_text_9 = """Sprites Used

\"Monika_Cute\" by radioactive64
Yandere Sayori by Agent Gold
Other Unique Sprites by Agent Gold"""

    # 10
    # 1 line, no extra pixels!
    c_text_10 = "Thanks For Playing!"

#This defines the CGs that disappear after a few seconds
#These are the colored CGs used for scene cgs
image e_credits_cg1:
    "mod_assets/cgs/credits/1.png"
    size(640, 360)

image e_credits_cg2:
    "mod_assets/cgs/credits/2.png"
    size(640, 360)

image e_credits_cg3:
    "mod_assets/cgs/credits/3.png"
    size(640, 360)

image e_credits_cg4:
    "mod_assets/cgs/credits/4.png"
    size(640, 360)

image e_credits_cg5:
    "mod_assets/cgs/credits/5a.png"
    size(640, 360)
    8.6
    "mod_assets/cgs/credits/5b.png"

image e_credits_cg6:
    "mod_assets/cgs/credits/6.png"
    size(640, 360)

image e_end_letter = "mod_assets/cgs/end_letter.jpg"

#DDLC Logo
image encore_credits_logo:
    "/mod_assets/encore.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#Team Salvato logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#This styles the different text in the credits
style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)

#These are the animations applied to the make the credits and images scroll
transform e_credits_text_scroll(y = 920, t = 15, end = -200):
    anchor (0.5, 0.5) subpixel True
    yoffset y
    linear t yoffset end

transform e_credits_scroll_right:
    xalign 0.9
    credits_scroll

transform e_credits_scroll_middle:
    xalign 0.5
    credits_scroll

transform e_credits_scroll_left:
    xalign 0.1
    credits_scroll

transform e_credits_text_scroll_right(y = 920, t = 15, end = -200):
    xpos 960
    e_credits_text_scroll(y, t, end)

transform e_credits_text_scroll_middle(y = 920, t = 15, end = -200):
    xpos 640
    e_credits_text_scroll(y, t, end)

transform e_credits_text_scroll_left(y = 920, t = 15, end = -200):
    xpos 320
    e_credits_text_scroll(y, t, end)

    #Disable player interactions
#    $ config.keymap['game_menu'] = []
#    $ config.keymap['hide_windows'] = []
#    $ renpy.display.behavior.clear_keymap_cache()
#    $ quick_menu = False
#    $ config.skipping = False
#    $ config.allow_skipping = False

#This is where the credits scroll starts
label encore_credits:
    python:
        # Adjust this so we have the player's name in place
        c_text_3 = """Sayori as Sayori
Natsuki as Natsuki
Yuri as Yuri
Monika as Monika
The MC as """ + player
        #Disable player interactions
        config.keymap['game_menu'] = []
        config.keymap['hide_windows'] = []
        renpy.display.behavior.clear_keymap_cache()
        quick_menu = False
        config.skipping = False
        config.allow_skipping = False
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    #play music "<from 50.0>bgm/credits.ogg" noloop # Credits song
    play music e6 noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show encore_credits_logo
    pause 9.12
    #Each CG is shown.

    show e_credits_cg1 at e_credits_scroll_middle as credits_image_1

    pause 2.0

    #Actual names for the credits
    show credits_text c_text_1 at e_credits_text_scroll_middle(y = 1170, t = 21.5, end = -450) as credits_text_1

    pause 12.5

    show e_credits_cg2 at e_credits_scroll_middle as credits_image_2

    pause 2.0

    show credits_text c_text_2 at e_credits_text_scroll_middle(y = 1170, t = 21.5, end = -450) as credits_text_2

    pause 12.5

    show e_credits_cg3 at e_credits_scroll_middle as credits_image_1

    pause 2.0

    show credits_text c_text_3 at e_credits_text_scroll_middle(y = 1120, t = 20.5, end = -400) as credits_text_1

    pause 11.5

    show e_credits_cg4 at e_credits_scroll_middle as credits_image_2

    pause 2.0

    show credits_text c_text_4 at e_credits_text_scroll_middle(y = 1170, t = 21.5, end = -450) as credits_text_2

    pause 12.5

    show e_credits_cg5 at e_credits_scroll_middle as credits_image_1

    pause 2.0

    show credits_text c_text_5 at e_credits_text_scroll_middle(y = 1170, t = 21.5, end = -450) as credits_text_1

    pause 12.5

    show e_credits_cg6 at e_credits_scroll_middle as credits_image_2

    pause 2.0

    show credits_text c_text_6 at e_credits_text_scroll_middle(y = 1070, t = 19.0, end = -350) as credits_text_2

    pause 9.0

    show credits_text c_text_7 at e_credits_text_scroll_middle(y = 1570, t = 32.0, end = -850) as credits_text_1

    pause 17.0
    hide credits_image_1
    hide credits_image_2

    show credits_text c_text_8 at e_credits_text_scroll_middle(y = 2180, t = 48.0, end = -1450) as credits_text_2

    pause 30.0

    show credits_text c_text_9 at e_credits_text_scroll_middle(y = 1120, t = 20.5, end = -400) as credits_text_1

    pause 11.5

    show credits_header c_text_10 at e_credits_text_scroll_middle(y = 920, t = 7.5, end = 360) as credits_text_2

    pause 9.5

    scene black with Dissolve(1.0)

    play sound page_turn
    show e_end_letter with Dissolve(1)
    $ pause()

    call screen dialog(message="Restart required.\nThe game will now exit.", ok_action=Quit(confirm=False))
#    hide e_end_letter with Dissolve(1)
#    pause 0.5

    return
