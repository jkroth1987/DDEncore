image menu_animation_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 845
    ycenter 1200
    zoom 0.68
    
    pause menu_wait_time
    
    block:
        pause 0.1
        menu_position_s(0.5) # Pop into the scene
        pause 3.926
        #menu_center(0.25) # "Hey, hey! My heart's beating..."
        ycenter 1200
        pause 11.173
        #menu_position_s(0.25) # Natsuki's turn
        menu_position_s(0.0)
        pause 17.004
        #menu_center(0.25) # "Is it way too much if you had to choose just one of us?"
        ycenter 1200
        pause 6.736
        #menu_position_s(0.25) # "Tell me, tell me please...!"
        menu_position_s(0.0)
        pause 11.355
        ycenter 1200
        #menu_center(0.25) # "Will it be okay...?"
        pause 12.879
        #menu_position_s(0.25) # First verse is finishing
        menu_position_s(0.0)
        pause 21.29
        ycenter 1200
        #menu_center(0.25) # "I really lo-O-O-O-O--"
        pause 3.195
        "gui/menu_art_s_break.png"
        menu_position_s(0.0) # Monika interrupts
        pause 0.5
        "gui/menu_art_s.png"
        pause 2.0
        "gui/menu_art_s_break.png"
        pause 0.3
        "gui/menu_art_s.png"
        pause 0.5
        "gui/menu_art_s_break.png"
        pause 0.2
        "gui/menu_art_s.png"
        pause 60.167
        ycenter 1200
        #menu_center(0.5) # "We'll be together, forever, we're never gonna be apart!"
        pause 4.924
        #menu_position_s(0.5) # Wait for the end of the song
        menu_position_s(0.0)
        pause 12.482
        xcenter 845 ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_s2:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 845
    ycenter 1200
    zoom 0.68
    
    pause menu_wait_time
    
    block:
        #pause 0.1
        #menu_position_s(0.5) # Pop into the scene
        pause 4.526
        menu_position_s(0.0)
        menu_center(0.25) # "Hey, hey! My heart's beating..."
        pause 10.673
        menu_position_s(0.25) # Natsuki's turn
        ycenter 1200
        pause 17.004
        menu_position_s(0.0)
        menu_center(0.25) # "Is it way too much if you had to choose just one of us?"
        pause 6.236
        menu_position_s(0.25) # "Tell me, tell me please...!"
        ycenter 1200
        pause 11.355
        menu_position_s(0.0)
        menu_center(0.25) # "Will it be okay...?"
        pause 12.379
        menu_position_s(0.25) # First verse is finishing
        ycenter 1200
        pause 21.29
        menu_position_s(0.0)
        menu_center(0.25) # "I really lo-O-O-O-O--"
        pause 0.52
        "gui/menu_art_s_break.png"
        menu_center_vibrate(0.0, 0.425)
        #pause 0.425
        #menu_position_s(0.0) # Monika interrupts
        "gui/menu_art_s.png"
        xcenter 510 ycenter 1200 zoom 0.68 yoffset 0
        pause 65.667
        menu_position_s(0.0)
        menu_center(0.5) # "We'll be together, forever, we're never gonna be apart!"
        pause 3.924
        menu_position_s(0.5) # Wait for the end of the song
        ycenter 1200
        pause 12.482
        ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 825
    ycenter 1200
    zoom 0.6
    
    pause menu_wait_time
    
    block:
        menu_position_n(0.4) # Pop into the scene--Natsuki insists she show up first
        pause 15.049
        ycenter 1200
        # menu_center(0.25) # "Just like a sundae..."
        pause 12.049
        menu_center(0.0)
        menu_position_n(0.25) # Yuri's up next
        #menu_position_n(0.0)
        pause 11.441
        ycenter 1200
        #menu_center(0.25) # "Tell me, tell me please...!"
        pause 11.855
        #menu_position_n(0.25) # Sayori's turn
        menu_position_n(0.0)
        pause 46.207
        ycenter 1200
        #menu_center(0.25) # "Tasty love, something I want more of..." (Like more screen time, dang it!)
        pause 5.291
        menu_center(0.0)
        menu_position_n(0.25) # Yuri takes over, Natsuki's out for a while
        pause 66.439
        xcenter 825 ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_n2:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 825
    ycenter 1200
    zoom 0.6
    
    pause menu_wait_time
    
    block:
        #menu_position_n(0.4) # Pop into the scene--Natsuki insists she show up first
        pause 15.449
        menu_position_n(0.0)
        menu_center(0.25) # "Just like a sundae..."
        pause 11.799        
        #menu_position_n(0.25) # Yuri's up next
        xcenter 733 ycenter 1200 zoom 0.6
        pause 11.691
        menu_position_n(0.0)
        menu_center(0.25) # "Tell me, tell me please...!"
        pause 11.355
        menu_position_n(0.25) # Sayori's turn
        ycenter 1200
        pause 46.207
        menu_position_n(0.0)
        menu_center(0.25) # "Tasty love, something I want more of..." (Like more screen time, dang it!)
        pause 5.041
        xcenter 733 ycenter 1200 zoom 0.6
        #menu_position_n(0.25) # Yuri takes over, Natsuki's out for a while
        #ycenter 1200
        pause 66.689
        ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 865
    ycenter 1200
    zoom 0.58
    
    pause menu_wait_time
    
    block:
        pause 0.4
        menu_position_y(0.75) # Creep into the scene--maybe no one will notice?
        pause 26.348
        #menu_center(0.25) # "When we touch, it'll never be enough..."
        ycenter 1200 # Hide in favor of the front sprite
        pause 5.455
        menu_position_y(0.0) # Sayori's turn
        pause 41.354
        ycenter 1200 # Hide for the front sprite
        #menu_center(0.25) # "Hey, hey... When I'm next to you..."
        pause 10.906
        menu_position_y(0.0) # Sayori takes over--wait, what was...?!
        pause 17.329
        ycenter 1200
        #menu_center(0.25) # "Will it make the CUT if you have to choose just one of us?"
        pause 6.642
        #menu_position_y(0.25) # Monika's turn
        menu_position_y(0.0)
        pause 11.489
        ycenter 1200 # Hide for forward sprite
        #menu_center(0.25) # "How can I convey...?"
        pause 8.109
        menu_position_y(0.0) # Wait, Monika, I wasn't done!
        pause 40.449        
        xcenter 865 ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_y2:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 865
    ycenter 1200
    zoom 0.58
    
    pause menu_wait_time
    
    block:
        pause 0.4
        #menu_position_y(0.75) # Creep into the scene--maybe no one will notice?
        pause 27.098
        menu_position_y(0.0)
        menu_center(0.25) # "When we touch, it'll never be enough..."
        pause 4.955
        menu_position_y(0.25) # Sayori's turn
        ycenter 1200 # Hide in favor the the behind sprite
        pause 41.354
        menu_position_y(0.0)
        menu_center(0.25) # "Hey, hey... When I'm next to you..."
        pause 10.406
        menu_position_y(0.25) # Sayori takes over--wait, what was...?!
        ycenter 1200 # Hide for the behind sprite
        pause 17.329
        menu_position_y(0.0)
        menu_center(0.25) # "Will it make the CUT if you have to choose just one of us?"
        pause 6.142
        menu_position_y(0.25) # Monika's turn
        ycenter 1200
        pause 11.489
        menu_position_y(0.0)
        menu_center(0.25) # "How can I convey...?"
        pause 7.515
        "gui/menu_art_y_ghost.png"
        menu_center_vibrate(0.0, 0.344)
        #pause 0.344
        "gui/menu_art_y.png"
        ycenter 1200 xcenter 845 zoom 0.58 # Hide for the behind sprite
        #menu_position_y(0.0) # Wait, Monika, I wasn't done!
        pause 40.449
        ycenter 1200 # Hide offscreen at the end of the song
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 845
    ycenter 1200
    zoom 0.68
    
    pause menu_wait_time
    
    block:
        pause 0.25
        menu_position_m(0.6) # Pop into the scene--notice me sen... I mean, player!
        pause 85.308 # I have to wait HOW long?!
        ycenter 1200
        #menu_center(0.0) # Interrupt Sayori--she'll forgive me later, right?
        pause 11.093
        menu_center(0.0)
        menu_position_m(0.25) # Natsuki's turn
        pause 11.433
        #menu_center(0.25) # "Shall I leave you be...?"
        ycenter 1200
        pause 11.739
        menu_center(0.0)
        menu_position_m(0.25) # Yuri's turn...
        pause 7.859
        #menu_center(0.0) # Ah, nope, nope! Yuri doesn't get a turn after all!
        ycenter 1200
        pause 15.949
        #menu_position_m(0.25) # Lyrics are done... mostly!
        menu_position_m(0.0)
        pause 18.271
        #menu_center(1.0) # "Maybe we'll never be together but forever you'll be in my heart~"
        ycenter 1200
        pause 6.229
        xcenter 845 ycenter 1200 zoom 0.68 # Hide offscreen at the end of the song        
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

image menu_animation_m2:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 845
    ycenter 1200
    zoom 0.68
    
    pause menu_wait_time
    
    block:
        #pause 0.25
        #menu_position_m(0.6) # Pop into the scene--notice me sen... I mean, player!
        pause 86.158 # I have to wait HOW long?!
        menu_center(0.0) # Interrupt Sayori--she'll forgive me later, right?
        pause 11.093
        #menu_position_m(0.25) # Natsuki's turn
        xcenter 1180 ycenter 1200 zoom 0.68
        pause 11.683
        menu_position_m(0.0)
        menu_center(0.25) # "Shall I leave you be...?"
        pause 11.489
        #menu_position_m(0.25) # Yuri's turn...
        xcenter 1180 ycenter 1200 zoom 0.68
        pause 8.109
        menu_center(0.0) # Ah, nope, nope! Yuri doesn't get a turn after all!
        pause 15.699
        menu_position_m(0.25) # Lyrics are done... mostly!
        ycenter 1200
        pause 18.271
        menu_position_m(0.0)
        menu_center(1.0) # "Maybe we'll never be together but forever you'll be in my heart~"
        pause 5.229
        xcenter 1180 ycenter 1200 zoom 0.68
        pause 11.125 # Then wait for the song to repeat, and you'll be back in place
        repeat

transform menu_position_s(t=0.25):
    easein t xcenter 510 ycenter 500 zoom 0.68

transform menu_position_n(t=0.25):
    easein t xcenter 733 ycenter 470 zoom 0.6

transform menu_position_y(t=0.25):
    easein t xcenter 935 ycenter 465 zoom 0.6

transform menu_position_m(t=0.25):
    easein t xcenter 1185 ycenter 500 zoom 0.68

transform menu_center(t=0.25):
    easein t xcenter 845 ycenter 640 zoom 1.00
    
transform menu_center_vibrate(t=0.25, end=1.0): # The end time is like saying "pause end" after this position is reached.
    easein t xcenter 845 ycenter 640 zoom 1.00
    
    block:
        yoffset 0
        linear 0.0833 yoffset -10
        repeat
    
    time end # We need this to be here, or the repeat block would loop forever.


###### ALL RIGHT, GOLD. WHAT'S GOING ON HERE? ######
# Each girl's menu sprite has its own animation instructions which are synced to the song
# as it plays when the player launches the game. This will move them to the center when
# their lines come up and move them back when their line finishes (including some abrupt
# transitions for Monika's meddling moments).
# 
# All girls will disappear at the end of the song, then start their animations over with it.
# If they were in sync before the repeat, they should be in sync after it.

###### WHY DOES YURI HAVE TWO IMAGES? ######
# On the title screen, the images are showing in Z order according to when they're added.
# So we add Yuri first, and she shows up behind everyone else. We add Monika last,
# and she's in front of the others (which is just like her to do).
#
# If Yuri just comes to the front with that Z order, Natsuki will be drawn over her even though
# she's supposed to be behind her now. I don't know how much control we have over Z order here
# (just trying to use zorder in the images caused errors), so I took the "Hollywooding" approach.
# Yuri 2 is hidden at Y = 1200 when Yuri 1 is showing and vice versa. The switch is made
# instantly, so it always looks like one Yuri is in view--just a question of if she's in front of
# or behind Natsuki. The two Yuris are also synced with each other, of course.

###### THERE'S A LOT OF MAGIC NUMBERS HERE. WHERE'D THEY COME FROM? ######
# The girls' base positions are based loosely on where they are normally and where the
# center of their block of the menu screen is. Sayori was the base here--she's at 510
# and the center is 845. 845 - 510 = 335, and 845 + 335 = 1180, which is Monika's position.
# Yuri and Natsuki's positions are each 223 away from Sayori and Monika's, putting everyone
# about equal distance from their nearest neighbor. The other values for zoom and Y position
# are kinda arbitrary.
#
# When characters need to be hidden, I put them at Y = 1200 to put them out of sight below
# the screen. Make sure their zoom is appropriate or they still might peek out.

###### NOT THE POSITIONS, YOU FOOL, THE MUSIC TIMING! ######
# Oh right, that. I opened the song in Audacity and paused it at key moments, making
# note of the current timestamp in seconds. The timestamps I recorded will be listed
# as the last thing in this file for reference.
#
# To figure the time for the character's next transition, take the timestamp they need
# to move on, subtract the last timestamp they moved on (or their appearance beginning
# if they haven't moved yet), and subtract any transition times they spent in between.
# For instance, Sayori's first move to the center is at 11.779. The animation start is
# at 7.253, and she spends 0.6 seconds getting into place (a pause and a transition time).
# So 11.779 - 7.253 - 0.6 = 3.926, which is her first pause time. She moves back when
# it's Natsuki's turn at 22.702, so 22.702 - 11.779 - 0.25 for the last transition = 10.673,
# and so on. Each character's timings need to be calculated and adjusted individually--
# I've synced them up to start with, but adjusting them may desync them, so use caution.

###### CURRENT KNOWN ISSUES ######
# The girls sometimes blink for a moment if things get out of sync when switching to and
# from the "in front of everything" sprites. There's no consistency to this--it's probably
# just the engine missing a beat once in a while randomly. We could try to compensate for
# it, but that would likely cause more problems than it would fix.

###### IMPORTANT TIMESTAMPS ######
# Here are the timestamps I recorded using Audacity which the girls are currently synced to.
# Listen to the song with this list in front of you, and you'll understand which moment each
# one is referring to.
#
# Approximate start point: 7.253
# Sayori start: 11.779
# Natsuki start: 22.702
# Yuri start: 34.751
# Sayori start: 39.956
# Natsuki start: 46.442
# Sayori start: 58.047
# Sayori end: 70.676
#
# Yuri start: 81.560
# Sayori start: 92.216
# Sayori glitch: 92.986
# Monika interrupt: 93.411
# Natsuki start: 104.504
# Yuri start: 109.795
# Monika start: 116.187
# Yuri start: 127.926
# Yuri goes ghost: 135.691
# Monika replace: 136.035
# Monika end: 151.734
#
# Sayori in: 159.078
# Sayori out: 163.502
#
# Monika in: 170.255
# All out: 176.484
#
# Ending: 180.356
# Sort of next start: 187.609 (7.253 after the song loops, which is where the animation normally begins)
# So the total wait time from Monika's ending to the next start is 11.125
#
# If all the girls disappear at the end of the song at the same time, everything is synced correctly!