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

    $ PLAYER = player.upper()


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
    "Welcome to the updated Doki Doki Encore DEMO!"
    "Before we begin, you need to answer a few quick questions."
    "Sayori confessed to you in the base game."
    menu:
        "Did you accept Sayori's confession? If you click 'yes', you will be starting off on her route in this mod. If you click 'no', you won't start on her route."
        "Yes":
            $ encore_sayoriquestion_1 = True
            $ s_modappeal = s_modappeal + 1
        "No":
            $ encore_sayoriquestion_1 = False
            $ s_modappeal = 0

    "Good, now there's Yuri and Natsuki..."
    "In the base game, you chose to spend the weekend with one of them for the festival preparations."
    "If you chose 'no' on the last question, you'll either start off on Yuri's or Natsuki's route in this mod depending on who you choose next."
    "If you chose 'yes' on the last question, well, you'll see how things will go, now won't you?"
    menu:
        "Who did you help prepare for the festival?"
        "Yuri":
            $ encore_festivalquestion_2 = "Yuri"
            $ y_modappeal = y_modappeal + 1
        "Natsuki":
            $ encore_festivalquestion_2 = "Natsuki"
            $ n_modappeal = n_modappeal + 1


    "Seeing as you're playing the updated version, I'll allow you to skip to the start of Day 3 so you can experience what happens next in the story."
    "If you want to play from the begining again, you'll at least get to see what's been changed since last time!"
    menu:
        "Skip to Day 3?"
        "Yes.":
            $ day3_skip = True
        "No.":
            $ day3_skip = False


#    "Have you played any other DDLC mods before this?"
#    "This won't affect gameplay in this DEMO, but it may affect gameplay in the Full Release."
#    "Some examples include, but are not limited to..."
#    "Blue Skies, Summertime, Coldest Summer, Divided Hearts, Purist, Fallen Angel, Exit Music, The Festival, Fruits of The Literature Club, The Good Ending and many others!"
#    "r/DDLCMods has a full list of mods that's pinned on the subreddit, feel free to check it out after you're finished playing!"
#    menu:
#        "Have you played any other mods?"
#        "Yes":
#            $ encore_modquestion_3 = True
#        "No":
#            $ encore_modquestion_3 = False


    if day3_skip == True:
        menu:
            "Who did you did you hangout with on the first day?"
            "Monika":
                $ hangout1 = "Monika"
            "Natsuki":
                $ hangout1 = "Natsuki"
            "Sayori":
                $ hangout1 = "Sayori"
            "Yuri":
                $ hangout1 = "Yuri"

        menu:
            "Who did you did you hangout with on the second day?"
            "Monika":
                $ hangout2 = "Monika"
            "Natsuki":
                $ hangout2 = "Natsuki"
            "Sayori":
                $ hangout2 = "Sayori"
            "Yuri":
                $ hangout2 = "Yuri"

$ poem_giver = "" # Will be either Yuri or Natsuki
$ is_love_poem = False
$ same_hangout = hangout1 == hangout2
$ conflicting_hangout = (hangout1 == "Natsuki" and hangout2 == "Yuri") or (hangout1 == "Yuri" and hangout2 == "Natsuki")
$ neutral_split_n = (hangout1 == "Natsuki" and (hangout2 == "Sayori" or hangout2 == "Monika")) or (hangout2 == "Natsuki" and (hangout1 == "Sayori" or hangout1 == "Monika"))
$ neutral_split_y = (hangout1 == "Yuri" and (hangout2 == "Sayori" or hangout2 == "Monika")) or (hangout2 == "Yuri" and (hangout1 == "Sayori" or hangout1 == "Monika"))

if encore_sayoriquestion_1 == True: # We accepted Sayori's confession
    if (hangout1 == "Sayori" or hangout1 == "Monika") and (hangout2 == "Sayori" or hangout2 == "Monika"):
        # Spent both days with Sayori, Monika, or split between them--show the love poem from the weekend hangout girl
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True

    elif encore_festivalquestion_2 == hangout1 and same_hangout == True:
        # Outside the confession, we have been 100% faithful to either Yuri or Natsuki
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True

    elif encore_festivalquestion_2 != hangout1 and same_hangout == True and (hangout1 == "Natsuki" or hangout1 == "Yuri"):
        # We spent the weekend with one girl, but spent the two days with the other -- the hangout girl gives the like poem
        $ poem_giver = hangout1
        $ is_love_poem = False

    elif encore_festivalquestion_2 == "Natsuki":
        if neutral_split_n == True:
            # We favored Natsuki over Yuri
            $ poem_giver = "Natsuki"
            $ is_love_poem = True

        elif neutral_split_y == True:
            # We haven't spent time with Natsuki since the weekend, and Yuri is taking interest
            $ poem_giver = "Yuri"
            $ is_love_poem = False

        elif conflicting_hangout == True:
            # We spent time with both of them, but Natsuki wins for having the weekend
            $ poem_giver = "Natsuki"
            $ is_love_poem = True


    elif encore_festivalquestion_2 == "Yuri":
        if neutral_split_y == True:
            # We favored Yuri over Natsuki
            $ poem_giver = "Yuri"
            $ is_love_poem = True

        elif neutral_split_n == True:
            # We haven't spent time with Yuri since the weekend, and Natsuki is taking interest
            $ poem_giver = "Natsuki"
            $ is_love_poem = False

        elif conflicting_hangout == True:
            # We spent time with both of them, but Yuri wins for having the weekend
            $ poem_giver = "Yuri"
            $ is_love_poem = True

    # End of Accepted Confession block
else: # We didn't accept Sayori's confession
    if encore_festivalquestion_2 == hangout1 and same_hangout == True:
        # We spent the weekend and two hangouts with Yuri or Natsuki... but wait!
        # The other girl will give a "like you" poem
        if encore_festivalquestion_2 == "Natsuki":
            $ poem_giver = "Yuri"
        else:
            $ poem_giver = "Natsuki"
        $ is_love_poem = False

    elif encore_festivalquestion_2 != hangout1 and same_hangout == True and (hangout1 == "Natsuki" or hangout1 == "Yuri"):
        $ poem_giver = hangout1
        $ is_love_poem = False

    elif neutral_split_n == True or neutral_split_y == True:
        # If we spent one day with either Yuri or Natsuki, the weekend girl gives the "like you" poem
        if encore_festivalquestion_2 == "Natsuki":
            $ poem_giver = "Natsuki"
        else:
            $ poem_giver = "Yuri"
        $ is_love_poem = False

    elif conflicting_hangout == True:
        if encore_festivalquestion_2 == "Natsuki":
            $ poem_giver = "Natsuki"
        else:
            $ poem_giver = "Yuri"
        $ is_love_poem = True

    elif (hangout1 == "Sayori" or hangout1 == "Monika") and (hangout2 == "Sayori" or hangout2 == "Monika"):
        # Spent both days with Sayori, Monika, or split between them--show the love poem from the weekend hangout girl
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True




"Shall we begin, [player]?"
"Every good story needs an encore!"
jump day3_start

if day3_skip == False:
    "Shall we begin, [player]?"
    "Every good story needs an encore!"
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
