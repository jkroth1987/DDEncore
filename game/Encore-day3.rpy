#############
#   DAY 3   #
#############
label day3_start:
    stop music
    call affectionasignment from _call_affectionasignment_1
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    $ day = 3
    scene bg bedroom
    play sound "sfx/fall.ogg"
    "I suddenly wake up with a fright."
    if hangout2 != "Monika":
        "I feel the urge to vomit but I'm successfully able to suppress it."
        "What was that?"
        "I prop myself up but I immediately feel my forehead sting."
        "I nurse my forehead and look at the clock."
        "Great... I don't have to be up for another hour."
        "I'm afraid to fall asleep again, mostly because I'm afraid that these nightmares are getting worse."
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "After a few minutes my forehead stops stinging."
        "I spend the rest of my time mostly just laying there thinking about my nightmare."
        if hangout2 == "Sayori":
            "About how I couldn't save Sayori..."
            "How I just watched her slowly choke to death..."
        elif hangout2 == "Natsuki":
            "About how I couldn't save Natsuki..."
            "How I just watched that figure make Natsuki's neck break..."
        else:
            "About how I couldn't save Yuri..."
            "How that figure made Yuri kill herself..."
        "And her corpse..."
        "I get nauseous just thinking about that horrible image I saw..."
    elif hangout2 == "Monika":
        "I gasp for air and prop myself up quickly."
        mc "What... was that?"
        "I feel a chill wrack my entire body as I shiver violently."
        "Why do I feel so cold?"
        "After a few minutes I stop shivering and look at the clock."
        "Great... I don't have to be up for another hour."
        "I'm afraid to fall asleep again, mostly because I'm afraid that voice is going to keep tormenting me."
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "I spend the rest of my time mostly just laying there thinking about that voice I keep hearing in my dreams."
        "What does it want with me?"
        "And what the hell does it mean by \‘keep doing what you're doing\'?"
        "I don't even know what I'm doing..."
    "Thankfully before I can think longer about it, my alarm sounds off."
    "I sigh to myself as I walk over to silence my alarm and go about my daily morning routine of getting ready for school."
    scene bg kitchen
    with wipeleft_scene
    play music t2 fadein 1.5
    "After showering and putting on my uniform, I head downstairs to make myself some breakfast."
    "I'm not particularly hungry so I just make myself a fruit bowl."
    if encore_sayoriquestion_1:
        "I send Sayori another good morning text."
        "The responds back rather quickly and tells me that she's already waiting outside for me."
        "Once again, Sayori's the first one out."
        "Popping the last piece of watermelon into my mouth, I gather my things, and head out to meet Sayori."
    else:
        if hangout2 == "Monika":
            "It takes me a while to find the motivation to eat. These nightmares are just getting weirder and weirder."
            "Am I really going insane?"
            "Hearing my stomach rumble I decide to finally start eating."
            "If I'm going insane, I'd rather not do it on an empty stomach."
            "Popping the last piece of watermelon into my mouth, I gather my things, and head out to meet Sayori."
        else:
            "After I finished making breakfast I glance over at the kitchen clock. I'm running late!"
            "I quickly get everything that's essential for school."
            "Popping the last piece of watermelon into my mouth, I gather my things, and head out to meet Sayori."
    #Scene Transition
    #Outside House Scene
    scene bg house
    with wipeleft_scene
    "Sayori's already standing by the adjacent sidewalk to my house."
    show sayori 1q at h11 zorder 1
    s "Hey, [player]!"
    "She beams at me, she seems really excited to see me today."
    if encore_sayoriquestion_1 and hangout2 == "Sayori" or hangout1 == "Sayori":
        "Her sky blue eyes reflect in the morning sun, the wind flows through her coral pink hair, and her smile is almost enough to erase the events of earlier this morning."
        mc "Hey, Sayori."
        show sayori 4q at h11
        "We walk up to each other and we briefly embrace each other."
        show sayori 1a at t11
        "We then begin our walk to school."
    else:
        mc "Hey. It's nice to see you today."
        s 1c "Just today?"
        mc "Today especially."
        s 1b "Oh yea and why is that?"
        mc "No real reason. It's just nice to see you."
        "We then begin our walk to school."
    s 3x "How are you doing this morning, [player]"
    mc "Oh...I've been alright I guess..."
    show sayori 1f
    "I don't want to ruin Sayori's cheery attitude, but my response seems to have already done it."
    "She frowns and looks worriedly at me."
    s 2h "[player], what's wrong?"
    stop music fadeout 2.0
    "I don't want to make her more worried about me, but I know that I can't hide anything from her for very long."
    "I'd feel guilty about not opening up about my own hardships to Sayori when she's done so with me."
    "But she can always get worked up when there's something wrong."
    #Tell Sayori
    #Don't Tell Sayori
    #(You can only gain or lose a point here with Sayori)
    #(Scoreboard, S: 4, N: 1, Y: 0, M: 0)
    menu:
        "Reluctantly, I..."
        "Tell Sayori.":
            $ tell_s = True
            jump day3_tellsayori
        "Don't Tell Sayori.":
            $ tell_s = False
            jump day3_notellsayori
label day3_tellsayori:
    "I decided to tell her."
    show sayori 1g
    play music m1 fadein 2.0
    mc "The past two nights... I've had these awful nightmares. I have no idea what's causing them."
    s "..."
    s 1h "...Do you... want to talk about it?"
    mc "I-"
    "My words get caught in the back of my throat."
    "An overwhelming feeling of dread washes over me."
    "This feeling..."
    "Somehow, this is worse than this morning."
    s 1g "[player]?"
    "Hearing Sayori's voice relieves the near crippling dread."
    mc "Sayori...I..."
    if hangout2 == "Sayori":
        mc "I watched you die..."
        mc "I couldn't save you."
        mc "All I could do was watch you, struggling to breathe..."
        s 1k "..."
        mc "I know it was just a dream, but it felt too close to reality for some reason..."
        mc "The way you frantically clawed at the rope..."
        #(shocked Sayori sprite)
        s u115232 "Rope...?"
        #DEMO CUT OFF
    elif hangout2 == "Yuri":
        mc "I watched Yuri die..."
        mc "I couldn't save her."
        mc "I watched this figure attack Yuri.. she was helpless to defend herself and I couldn't step in to help her..."
        s 1k "..."
        mc "I know it was just a dream, but it felt too close to reality for some reason..."
        mc "I... then saw this figure give Yuri a knife and she just stabbed herself..."
        #(shocked Sayori sprite)
        s u115232 "A knife?!?!?"
        #DEMO CUT OFF
    elif hangout2 == "Natsuki":
        mc "Sayori.. I..."
        mc "I watched Natsuki die..."
        mc "I couldn't save her."
        mc "I saw this shadow torturing her right in front of me."
        mc "It made Natsuki bend her neck in incredibly painful ways..."
        s 1k "..."
        mc "I know it was just a dream, but it felt too close to reality for some reason..."
        mc "I...then saw this shadow snap it's fingers and it made Natsuki's neck break."
        #(shocked Sayori sprite)
        s u115232 "She broke her neck?!?!"
        #DEMO CUT OFF
    else:
        mc "I've been having these weird dreams lately."
        mc "In my dreams, there's been this really strange voice that's been telling me to pursue it."
        mc "I also think it's telling me to stay away from you guys for some reason."
        mc "I have no idea why."
        s 1k "..."
        mc "I know it was just a dream, but it feels too real for some reason..."
        mc "It keeps telling me to ‘keep doing what I'm doing' and that it ‘has plans for us'."
        #(shocked Sayori sprite)
        s u115232 "Plans?!?!"
        #DEMO CUT OFF
    stop music
    scene encore_demoend
label day3_notellsayori:
    "OH! Uhmm..."
    "You weren't supposed to choose this options, and there is nothing here yet..."
    "So, uhm..."
    "..."
    "Awkward."
    return
    