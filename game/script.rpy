# Entry point
label start:
    $ menu_wait_time = 7.253

    #Hey Nico, you're probably seeing this and wondering I added anything, so I left a message
    #in the 'mod_assets' folder full of additions, take a look and fill free to
    #add to it to update me on additions you make. Keep a different log though
    #that way we can refer to older updates if need be.
    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ e_name = "Extra"


    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    $ encore_sayoriquestion_1 = False
    $ encore_festivalquestion_2 = "Yuri"
    $ encore_modquestion_3 = False
    $ style.say_window = style.window_encore

    #These are the appeal points for the day, they determine daily events, like scene sequences
    $ n_modappeal = 0
    $ s_modappeal = 0
    $ y_modappeal = 0
    $ m_modappeal = 0

    #These are the stored appeal points, they determine the ending the player recieves if the ending is determined by time spent with the girls
    $ n_modappealstored = 0
    $ s_modappealstored = 0
    $ y_modappealstored = 0
    $ m_modappealstored = 0

    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 2.0
    scene bg residential_day with dissolve_scene_full
    "..."
    "Welcome to Doki Doki Encore!"
    "Before we begin, I have a few questions for you about your time before meeting us."
    menu:
        "Did you accept Sayori's confession?"
        "Yes":
            $ encore_sayoriquestion_1 = True
            $ s_modappeal = s_modappeal + 1
        "No":
            $ encore_sayoriquestion_1 = False
            $ s_modappeal = 0
    menu:
        "Who did you help prepare for the festival?"
        "Yuri":
            $ encore_festivalquestion_2 = "Yuri"
            $ y_modappeal = y_modappeal + 1
        "Natsuki":
            $ encore_festivalquestion_2 = "Natsuki"
            $ n_modappeal = n_modappeal + 1
    menu:
        "Have you played any other mods?"
        "Yes":
            $ encore_modquestion_3 = True
        "No":
            $ encore_modquestion_3 = False
    "..."
    jump encorestart

label programmer_meme:
    "The following scene variations have not been implimented."
    "If you're seeing this, that means there was either an error, or the programmer decided to be lazy and put nothing here."
    "Either way, looks like this is the end of the prototype. So..."
    "..."
    "*whistling*"
    "Uhm...bye."
    return

#label endgame(pause_length=4.0):
    #$ quick_menu = False
    #stop music fadeout 2.0
    #scene black
    #show end
    #with dissolve_scene_full
    #pause pause_length
    #$ quick_menu = True
    #return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
