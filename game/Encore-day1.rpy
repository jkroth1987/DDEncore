label encorestart:
    #Void Scene
    stop music fadeout 1
    scene black
    with dissolve_scene_full
    $ style.say_window = style.window_encore
    mc "Uggghhhh..."
    "As I regain consciousness, I’m greeted with a sharp pain in my forehead."
    mc "AGH!"
    "This pain is almost unbearable!"
    "I stand up slowly, clutching my forehead in attempt to nurse the stinging pain."
    mc "W-{w=0.28}what…{w=0.28} What just happened?"
    "I groggily open my eyes."
    "..."
    mc "W-{w=0.28}What the fuck?"
    $ renpy.pause(delay=0.001)
    scene bg void
    play music e1
    mc "Where am I??? WHAT IS THIS????"
    "I look around in all directions, but as far as the eye can see, there's nothing but black, empty space."
    mc "H-{w=0.38}Hello?"
    $ e_name = "Echo"
    e "Hellooo"
    e "Helloooo"
    e "Hellooooo"
    "..."
    "I hear nothing but the sound of my own voice echo into the oblivion..."
    "How did this happen?"
    "What even happened?!?"
    "Everything was normal just up until a few minutes ago..."
    "Up until-"
    "Suddenly I hear something walk towards me."
    show monika s at t11 zorder 1
    "I'm able to make out a dark silhouette."
    "I think I recognize that outline..."
    mc "Hello?!"
    "The figure finally comes into my view."
    "It's..."
    show monika s2 at t11 zorder 1
    "Monika?!"
    show monika 1a at t11 zorder 1
    m 1b "Oh, good! You're awake!"
    mc "M-{w=0.28}Monika?!"
    mc "Where are we? Where are the others? W-{w=0.28}what is this?"
    m 1c "Oh...{w=0.28}you mean you don't remember?"
    mc "I..."
    "I try to remember what happened, but I no longer can."
    "Everything is now a blur to me."
    mc "No...{w=0.28} not really."
    m 1d "Well, then...{w=0.28} I guess bringing you here must have caused you to forget everything."
    m 2m "I guess my coding skills aren't quite up to scratch."
    mc "Monika, what the hell are you talking about?"
    mc "W-what \'coding\'? You're not making any sense!"
    m "Oh, dear…{w=0.28} I messed this up pretty badly."
    m 2q "Well, I guess I'll just have to try to take you back, then."
    mc "T-{w=0.28}take me back?? What are you talking about?"
    mc "TAKE ME BACK WHERE?!?"
    m 2e "To the beginning, silly."
    m 2k "You {i}need{/i} to remember why you're here."
    m 1r "Now just give me a second..."
    mc "{cps=40}No, Monika, wait! What're you talking about, \'to the beginni-{/cps}{nw}"
    $ renpy.pause(delay=0.001)
    stop music


#############
#   DAY 1   #
#############
label day1_beginning:
    #First Bedroom Scene
    scene dark
    $ s_name = "???"
    $ day = 1
    play sound "mod_assets/audio/knock.ogg"
    "I hear a loud banging on my door."
    play sound "mod_assets/audio/knock.ogg"
    s "HEEEEEEEEY!!"
    "Wh-{w=0.28}What?"
    "What's that shouting?"
    play music t2 fadein 4.0
    s "Wakey wakey sleepyhead!"
    mc "Uuuugh..."
    "I open my eyes..."
    scene bg bedroom
    with dissolve_cg
    show sayori 1q at t11 zorder 1
    if encore_sayoriquestion_1 == False:
        "I see my door swing open as my annoying, yet sweet, friend, Sayori, enters my room."
    elif encore_sayoriquestion_1 == True:
        "I see my door swing open as my annoying, yet sweet, girlfriend, Sayori, enters my room."
    $ s_name = "Sayori"
    show sayori 5a at h11 zorder 1
    mc "Hey! Don't just run into my {i}bedroom!{/i}"
    show sayori at thide
    hide sayori
    "Sayori startledly goes back outside and shuts the door."
    s "Sorry [player]! Ehehe..."
    "Oh, Sayori...{w=0.28}always doing things without thinking..."
    "I've known her since we were kids, basically for as long as I can remember."
    "We used to spend a lot of time together, but that changed when high school started last year."
    "I don't really know what happened...{w=0.28}we just drifted apart..."
    "We really didn’t see or hear much from each other for a while."
    "Though, that changed two weeks ago, when she \'convinced\' me to join the Literature Club."
    "Since that day, we’ve spent much more time together, almost like how we used to when we were kids."
    "But, that hasn't stopped me from learning some pretty unexpected things about her."
    "The more time I spent around Sayori, the more I realized that something was off about her..."
    "I finally found out just what it was last Sunday, when Sayori admitted to me that she had been dealing with depression all her life..."
    "If that wasn’t already alot for me take in at the time, she also confessed her feelings for me."
    "So, I decided on that day to tell her how I felt."

    if encore_sayoriquestion_1 == False:
        "I told her that I wanted to help her through this to get things back to the way they were."
        "At the time, I thought I did the right thing, but maybe I could have handled that a little bit better..."
        "Since last Sunday, Sayori's been unusually quiet around me."
        "She didn’t even really want to be around me during the festival…"
        "I must have really hurt her feelings when I turned her down..."
        "But, it’s probably for the best that we try to preserve our friendship, given her current state of mind."
        "At least for now."
        "Why is she here anyway?"
        "Oh right, I guess it’d make sense for Sayori to be here."
        "Lately, I’ve accidentally picked up on Sayori’s habit of sleeping in."
        "Dealing with the stress of everything in the last two weeks has really taken a bigger toll on me than I first realized."
        "Sayori has now made it a habit of her morning routine to make sure that I don’t oversleep."
        "At least Sayori seems to be doing a bit better today…"


    elif encore_sayoriquestion_1 == True:
        "I told her that I loved her back and well, we’ve been dating ever since."
        "Why is she here anyway?"
        "Oh right, I guess it'd make sense for Sayori to be here."
        "Lately, I’ve accidentally picked up on Sayori’s habit of sleeping in."
        "Dealing with the stress of everything in the last two weeks has really taken a bigger toll on me than I first realized."
        "Sayori has now made it a habit of her morning routine to make sure that I don’t oversleep."
        "At least Sayori seems to be doing a lot better now..."

    "Wait...{w=0.28} what time is it???"
    "I hurriedly check my alarm clock."
    "What?!? Oh God, I'm gonna be late!"
    "I quickly jump out of bed and prepare for the day."
    scene bg bedroom
    with wipeleft_scene
    "And so another ordinary day of school awaits me."
    "At least we finally get to have our first club meeting since the festival!"
    "While doing an abridged version of my morning routine, the memories of the last two weeks come rushing back into my mind."
    "I remember timidly introducing myself to the club for the first time, not expecting it to have such incredibly cute girls..."
    "And I remember having to endure their scrunity of my mediocre poems..."
    "Forutnately, not everything as of late has been super stressful or tense."

    if encore_festivalquestion_2 == "Natsuki":
        pass # Temporary
        "I got the chance to know Natsuki a little bit better as we prepared for the festival."
        "I fondly recall back to that Sunday where we spent the afternoon baking the cupcakes..."
        "A smile comes across my face as I remember the 'icing' incident..."


    elif encore_festivalquestion_2 == "Yuri":
        pass # Temporary
        "I got the chance to know Yuri a little bit better as we prepared for the festival."
        "I fondly recall back to that Sunday where we spent the afternoon working on the banner..."
        "A smile comes across my face as I remember the 'towel' incident..."


    "I suddenly then remember Sayori's confession and the fallout afterwards..."
    "By the time I got home after the festival, I can see why I was ready to crash and stay holed up in my bedroom for the rest of the week."
    "The stress aside, I’d say the festival went pretty well for the most part."
    "I’m sure our preformances will reel in a few new people..."
    "Though, while I may not have cared too much for the preformance part of the festival, I certainly had much more fun this time than compared to last year."

    if encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Natsuki":
        "Especially since I was able to spend it with Sayori and Natsuki."
        "They wouldn't let me out of their sight for some reason..."

    elif encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Yuri":
        "Especially since I was able to spend it with Sayori and Yuri."
        "They wouldn't let me out of their sight for some reason..."

    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Natsuki":
        "Especially since I was able to spend it with Natsuki."
        "She wouldn't let me out of her sight for some reason..."

    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Yuri":
        "Especially since I was able to spend it with Yuri."
        "She wouldn't let me out of her sight for some reason..."


    s "We're gonna be late if you don't get up, [player]!"
    mc "Alright, alright, I’m almost ready!"
    "I look in the mirror to see how I look."
    "Currently, I'm too tired to really pay much attention to my appearance."
    mc "Eh, that oughta do..."
    s "You ready yet?"
    mc "Yeah, come on in."
    "Sayori enters my room again."
    show sayori 1q at t11 zorder 1
    s 3r "Hey, [player]!"
    "She beams at me."

    if encore_sayoriquestion_1 == True:
        mc "Hey, Sayori! You're looking great today!"
        "Sayori starts to blush at the comment."
        s 3s "Awwww, thanks [player], you're too kind!"

    elif encore_sayoriquestion_1 == False:
        mc "Hey, Sayori."

    "Sayori then frowns at my appearance."
    s 3j "[player]!"
    scene cg s_cg_1
    with dissolve_cg
    "Sayori goes up to me and attempts to fix my hair."
    "This situation immediately turns awkward for me. I blush as Sayori's fingers swirl through my hair."
    mc "H-{w=0.28}hey come on…{w=0.28} is this really necessary?"
    s "You look like you just got out of bed."
    mc "Well, that’s because I just did."
    "Sayori and I fall silent for a second."
    "As she continues to try to fix my hair, I can’t help but be reminded of all the times my mother would do this to me right as I was about to go to school."
    "I’d always get embarrassed when she would try to fix my hair, especially in front of the other kids."
    s "How much sleep did you get?"
    mc "Considering everything that's happened the last two weeks, {i}a lot.{/i}"
    mc "And I still think I need more sleep..."
    "Sayori looks a little taken aback by my comment."
    scene bg bedroom
    with dissolve_cg
    pause 0.001
    show sayori 1l at t11 zorder 1
    s "Sorry...{w=0.28} I-{w=0.28}I didn't mean to wake you up so soon..."
    "Did I really come across as that rude?"
    "I know that despite her warm and peppy attitude, Sayori is still going through her depressive episodes..."
    "...and how it makes her want to avoid being a burden on other people...especially me."
    mc "Hey, hey, hey...{w=0.28} it's not your fault, really! Honestly, I feel a lot more rested now."
    "Sayori's face returns to her gleeful expression."
    s 3r "Hehe... well that's good!"
    "She says with a thankful relief in her voice."
    "I really need to be more careful with what I say around her."

    if encore_sayoriquestion_1 == True:
        show sayori 1a at t11 zorder 1
        "We stand there smiling at each other, looking into each other's eyes."
        "I think to myself just how lucky I am to have ended up with someone like her after all these years."
        "It didn't occur to me two weeks ago, hell, even last week, that I would've ever been dating my childhood best friend."
        "It's something I kind of always thought to myself as a \'what if...\' scenario, but I never really gave it serious thought until we started walking to school together again."
        "I guess that after spending all that time together in the Literature Club, we were able to rediscover that tight bond we once shared."
        "Though, it really wasn’t until Sayori had told me about her depression and love for me when I realized just how much we really meant to each other."
        "As the memories continue to swirl in my head, I slowly start spacing out into Sayori’s eyes."
        "I could almost stare into those sky blue eyes all day..."
        "Suddenly remembering that we still had school, I snap out of my gaze."
        mc  "We...{w=0.28} should probably get going. We don’t want to be late."
        s 1y "Y-{w=0.28}Yeah...{w=0.28} you're right."
        "She says that slightly flustered."
        "I can tell that she would rather stay like this with me, but we reluctantly make our way downstairs and start making our way to school."
        scene bg residential_day
        with wipeleft_scene
        "While we really didn't get much talking done on the way there, it's clear that the earlier moment we shared is still on our minds."
        show sayori 1b at t11 zorder 1
        "As we walk, we can't help but catch glances in each other's direction..."
        show sayori 1y at t11 zorder 1
        "Only to quickly look away while blushing."
        "I mumble under my breath."
        mc "Gosh, we're really together now, aren't we?"
        s 1c "Huh? Did you say something, [player]?"
        mc "Oh, nothing important."
        "It's on days like this that it still takes me a minute to realize that I've ended up with my best friend after all these years..."
        "Though when I stop to think about it, it makes sense that we did."
        "The warmth of her hugs, the scent of cinnamon that radiates from her hair..."
        "And that infectious smile that never fails to brighten my day."
        "As we continue our walk, I just keep thinking to myself about the next chance we'll be able to spend some time together..."

    elif encore_sayoriquestion_1 == False:
        show sayori 1k at t11 zorder 1
        "Though I didn’t spend too much time around Sayori in the literature club, we still had our moments, and I guess that set up everything to happen last Sunday."
        "Sayori is my dearest friend, I’ve always looked after and cared for her in a brother-sister sort of way."
        "Though, I'd be lying to myself if I were to say that some part of me didn't entertain the thought of us being together like that..."
        "But, I've had my eyes on someone else recently..."
        "Though, that hasn't been stopping me from wracking my brain since her confession."
        "I still ask myself how I could've handled that situation better, or if I even made the right choice."
        "Sayori didn't take my response to her confession very well, but figuring that she said she's had these feelings for a long time now, I can't blame her for acting all hurt."
        "I just hope we can still work through this new chapter in our lives together."
        "Suddenly remembering that we still had school, I snap out of my train of thought."
        mc "We...{w=0.28}should probably get going. We don't want to be late."
        s 3l "Y-{w=0.28}Yeah...{w=0.28} you're right."
        "She says that slightly flustered."
        show sayori 1k
        "Sayori then suddenly looks off into a random direction, trying to avoid making direct eye contact with me."
        "I can tell that Sayori is still trying to process the new reality of our friendship."
        "I've been meaning to discuss what happened with her, but neither of us have really worked up the courage to bring it up yet."
        "So we've been getting by on painfully trying to pretend that last Sunday's events didn't happen."
        mc "Well, let's get going!"
        "I try to put as much enthusiasm into my voice as I can, but it just sounds more like I'm faking it."
        show sayori 1l
        "Sayori forces an awkward smile."
        s "Y-{w=0.28}yeah...{w=0.28} let's go."
        "We silently make our way downstairs and start making our way to school."
        scene bg residential_day
        with wipeleft_scene
        show sayori 1a at t11 zorder 1
        "I remember how my walks with Sayori used to be filled with laughter, inside jokes, and other ramblings."
        show sayori 1f
        "But for now, those days seem to have come and gone, as our walks are now usually filled with uncomfortable silence."
        show sayori 1b
        "Though it's not like we haven't tried breaking the ice with each other..."
        scene bg residential_day
        with wipeleft_scene
        show sayori 1a at t11 zorder 1
        s "I told you that the festival was going to be better than last year's!"
        mc "Heh, I guess you were right afterall, Sayori."
        mc "I'm actually glad they finally listened to the students' suggestions and hired a real DJ."
        show sayori 1h
        s "Oh, come on, [player]! The music wasn't that bad!"
        s "The problem with the festival last year was that nobody put in any effort to organize!"
        mc "That's what I'm saying! If they actually cared and took the time to prepare, they would've hired a professional DJ."
        mc "Not ask some cringey first year who makes nightcore remixes on his phone to handle the music."
        show sayori 1g
        s "You don't give Keith enough credit, [player]!"
        s "He tries really hard to make people happy."
        show sayori 1y
        s "And he's really sweet too~"
        mc "Maybe you guys should get together then."
        show sayori 1n
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1e
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1v
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1k
        mc "I{w=0.38}-I'm sorry,{w=0.38} I really-"
        show sayori 1l
        s "It's fine..."
        show sayori 1k
        s "Let's just keep going..."
        scene bg residential_day
        with wipeleft_scene
        "Usually, one of us would say something stupid and it would just kill the mood, making us walk the rest of the way in silence."
        "Though at least we're over it by the time we get to school."

    scene bg corridor
    with wipeleft_scene
    "We're able to make it just in time for the morning bell."
    "I walk with Sayori through the crowd of other students all on their way to their first class."
    "It feels nice being able to walk the halls with Sayori again."
    "I actually didn't realize how much I missed walking with her until we started picking it up again."
    "Some of our fondest memories with each other are actually witnessing or participating in whatever shenanigans were happening in the school's halls..."
    "Even walking through the halls now, we always find something to laugh at..."
    with wipeleft_scene
    "After a few minutes of navigating our way through the crowded hallways, we finally get to Sayori's first class."
    show sayori 1c at t11 zorder 1
    s "So...{w=0.28} I guess this is my stop."
    "I can't help but to detect an ounce of disappointment in her voice as she says that."

    if encore_sayoriquestion_1 == True:
        "Honestly, I can't blame her. If it were up to me, we would spend the whole day together."

    else:
        "Honestly, I can't blame her. She's still trying to figure out how to go about our friendship, and she's always happy when she's with me."

    "It sucks that we're not sharing any classes this semester. We only occasionally see each other walking through the hallways between periods."
    mc "Yeah...{w=0.28} guess so..."
    show sayori 1k at t11 zorder 1
    "We stand there awkwardly for a moment."
    mc "Hey! I'll see you at the literature club, ok?"
    "Sayori's disappointment is quickly erased by her usual, cheery attitude."
    s 1x "Hehe...{w=0.28} yeah, I can't wait!"

    if encore_sayoriquestion_1 == True:
        show sayori at thide
        hide sayori
        "Sayori and I briefly embrace each other."
        "I must admit, nobody can give hugs quite like Sayori."
        "They’re always so warm, tender and tight. They’re the kind of hugs that you can be in forever."
        show sayori 1q at t11 zorder 1
    s 1q "See you later, [player]."

    if encore_sayoriquestion_1 == True:
        "We release each other, her warmth escaping me as we go our separate ways."

    if encore_sayoriquestion_1 == False:
        "I manage a small smile at her before I turn to head to my first class."

    scene bg class_day
    with wipeleft_scene
    "The school day is as ordinary and boring as ever, listening to the same old teachers teaching the same old things."
    "Eventually, my torment comes to an end as the final bell rings throughout the school."
    "That means it's time for the literature club!"
    "As I leave my class and walk through the door, I see Sayori standing outside."
    show sayori 3a at t11 zorder 1
    s "Hey, [player]! Ready to go?"
    mc "Yep, let's go!"
    "And so we head off to the clubroom."
    scene bg corridor
    with wipeleft_scene
    "We go up through the same familiar set of stairs and distant corridors that lead straight to the clubroom."
    "I've been wondering all day if anyone new will stop by today."
    "We got a whole week away from the club after the festival, though Monika still expected us to spread the word about the club."
    "I’d say that our performances at the festival were pretty well received."
    "Not to menton, we had pretty good turnout for our event. The audience seemed to love our performances."
    "I’m just glad my performance wasn’t an embarrassment."
    "Truth be told, I still feel somewhat guilty for just using a poem I found online."
    "Especially considering the others actually took the time and effort to write their poems for the festival."
    "Not long after my train of thought ends, we finally arrive at the clubroom."
    "I look at the door to see that the sign-up sheet is no longer there, so I'm taking that as a promising sign!"
    show sayori 3c at t11 zorder 1
    s "You think anyone signed up to join, [player]?"
    mc "Only one way to find out!"
    scene dark
    with wipeleft_scene
    stop music fadeout 2.0
    "I gently open the door..."
    scene bg club_day
    with wipeleft_scene
    "....to find that the usual scene we've become accustomed to over the last two weeks is still the same as ever."
    "I see Yuri reading her book in her usual spot and Natsuki in the closet organizing her manga."
    "I glance around the room, but see no sign of Monika."
    play music t3 fadein 2.0
    mc "Hey guys!"
    "Yuri sets her book down on the desk."
    show yuri 1b at t11 zorder 1
    y "Hello, [player]."
    mc "Anybody new stop by?"
    y 2f "No, not yet, it's just been me and Natsuki. Monika hasn't even showed up yet."
    call groupAll(2, 1, 2, 0, 0) from _call_groupAll
    show yuri 2f at t22 zorder 2
    show sayori 2h at t21 zorder 1
    s "Where could she be?"
    "Natsuki must have overheard us as she walks up to join the conversation."
    call groupClear() from _call_groupClear
    call groupAll(3, 1, 3, 2, 0) from _call_groupAll_1
    show natsuki 3b at t32 zorder 1
    show sayori 2h at t31 zorder 2
    show yuri 3f at t33 zorder 3
    n "She's probably sulking that nobody decided to sign up."
    y 1r "Natsuki...{w=0.28} maybe you should be a little bit more understanding of Monika's feelings..."
    y 1l "This festival did mean alot to her after all."
    n 5g "I know that! But, I still don't see what's the big deal with getting new people."
    n 5h "I'm fine with what we have right now."
    y 2f "I am too, but try to be a little considerate when Monika comes in."
    mc "Wait, nobody even signed up?"
    n 5c "Nope, at least that's what I got from seeing Monika around today."
    n 5q "She looked rather down."
    "Sayori frowns upon hearing this."
    s 2f "Aww, poor Monika...{w=0.28} we should cheer her up!"
    $ m_name = "???"
    show natsuki 5o at h32 zorder 1
    show sayori 4m at h31 zorder 2
    show yuri 3n at h33 zorder 3
    stop music
    call groupClear() from _call_groupClear_1
    m "Cheer me up how, Sayori?"
    "An all too familiar voice sternly asks."
    "Oh, crap."
    "We turn around to see Monika, standing by the doorway."
    show monika 1h at t41 zorder 4
    show natsuki 5o at t43 zorder 1
    show sayori 4m at t42 zorder 2
    show yuri 3n at t44 zorder 3
    "She enters the room, her footsteps are heavy."
    "Judging by the look on her face, it's easy to tell she's looking rather dejected."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show monika 1q at t11 zorder 4
    $ m_name = "Monika"
    "Yuri, sensing the incoming tension, quickly attempts to hide behind her book, while Sayori, Natsuki and I stand there dumbfounded."
    "They both look just as surprised as I am at Monika's sudden entrance."
    mc "Oh...{w=0.38}hey, Monika! We were just...{w=0.38}um..."
    "All words escape me in this situation."
    "I look to the other girls to bail me out of this situation, but nobody has anything to say."
    m 1r "*sighs*, It's alright, [player]."
    m 1d "Everyone, take a seat."
    call groupAll(4, 3, 4, 2, 1) from _call_groupAll_2
    show monika 1d at t41 zorder 1
    show yuri 3o at t44 zorder 4
    show natsuki 5s at t42 zorder 2
    show sayori 1k at t43 zorder 3
    "Everyone takes a seat at the front row of desks in the room, as Monika paces the floor in front of us."
    "Yeah...{w=0.38}she's not in a good mood."
    m 1i "So, it's true that despite the glowing reviews we got at the festival,{w=0.38} nobody signed up to join our club."
    show natsuki 5u
    "Natsuki shifts around awkwardly in her seat, as if Monika was directly addressing her."
    "Just how much did Monika overhear?"
    m 3h  "Which in of itself is unfortunate."
    m 1q "We put in a lot of effort to making the club look its best at the festival, and it was all for nothing."
    "Everyone avoids making eye contact at Monika, wanting to avoid her disappointed gaze."
    m 1r "We tried our best, and in the end, we couldn't attract even one new member."
    m 1p "Maybe if I did something different...{w=0.28}we would be better off…"
    m 1q "This is my fault..."
    "I exchange looks with Yuri, Natsuki and Sayori in an attempt to figure out what we should say."
    "It's pretty clear to all of us at this point that Monika's really hung up over this."

    if encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Natsuki":
        "After a moment of silence, Natsuki is the first to speak up."
        n 5q "Hey, Monika..."
        show monika 1h
        show natsuki 5u
        "Monika turns her full attention to Natsuki, her intense expression is even enough to make Natsuki's confidence falter."
        "Natsuki audibly gulps, but surprsingly keeps going with what she wants to say..."
        n 3h "Listen...{w=0.28} it's not your fault that we couldn't get anyone new."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        n 3q "We did everything we could to make the event great for everyone..."
        n 3t "...{w=0.38}and to be honest..."
        n 3l "I kinda had fun preparing for the festival."
        show natsuki 4d
        "Natsuki shoots me a quick side glance."
        "I know {i}exactly{\i} what she's referring to."
        show sayori 1i
        show natsuki 4m
        "Unfortunately for me, Sayori caught that and she shoots me a quizzical look."
        "The funny thing is, I haven’t quite gotten around to telling the others that Sayori and I are now a couple..."
        "The only one who knows that we’re dating is Monika, and I still have no clue how she found out."
        "I assume Sayori must have told her, but I haven’t bothered checking with her about it."
        "Saving me from further embarrassment, Yuri is the next to speak up."
        y 1j "Yes...{w=0.28} I guess I did have fun making the banner..."
        y 1c "It was also the first time I got to share my aromatherapy with anyone too!"
        show natsuki 3a
        "Sayori turns her attention back to Monika."
        s 3h "Monika...{w=0.28} Natsuki and Yuri are right, there is nothing we could have changed!"
        s 1b "We made the event as fun as we could, and even though no one joined, that’s not so bad!"
        s 4q "We still get to hang out and have fun, just like we've always have!"
        "Finally it's my turn to speak up."

    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Natsuki":
        "After a moment of silence, Natsuki is the first to speak up."
        n 5q "Hey, Monika..."
        show monika 1h
        show natsuki 5u
        "Monika turns her full attention to Natsuki, her intense expression is even enough to make Natsuki's confidence falter."
        "Natsuki audibly gulps, but surprsingly keeps going with what she wants to say..."
        n 3h "Listen...{w=0.28} it's not your fault that we couldn't get anyone new."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        n 3q "We did everything we could to make the event great for everyone..."
        n 3t "...{w=0.38}and to be honest..."
        n 3l "I kinda had fun preparing for the festival."
        show natsuki u211214
        "Natsuki shoots me a quick side glance."
        "I know {i}exactly{\i}what she's referring to."
        show natsuki 3j
        show sayori 1k
        mc "Yeah! Natsuki and I had a really good time together! We baked together and we even..."
        show sayori 1g
        "I look over at Sayori and see her staring me down with a sort of sad look in her eye."
        "I can't say it...{w=0.28}not after I shot her down on Sunday."
        mc "...even...{w=0.38}uhhh..."
        show natsuki 5k
        "I can feel my face burning up as a deep sense of extreme guilt washes over me."
        show sayori 1k
        "It leaves me tongue twisted and I don't know what else to say without upsetting Sayori."
        "Saving me from further embarrassment, Yuri is the next to speak up."
        y 1j "Yes...{w=0.28} I guess I did have fun making the banner..."
        y 1c "It was also the first time I got to share my aromatherapy with anyone too!"
        show natsuki 3a
        "Sayori turns her attention back to Monika."
        s 3h "Monika...{w=0.28} Natsuki and Yuri are right, there is nothing we could have changed!"
        s 1b "We made the event as fun as we could, and even though no one joined, that’s not so bad!"
        s 4q "We still get to hang out and have fun, just like we've always have!"
        "Finally it's my turn to speak up."




    elif encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Yuri":
        "After a moment of silence, Yuri is the first to speak up."
        y 2q "Uhm...{w=0.38}h-hey...{w=0.38}Monika..."
        show monika 1h
        show yuri 3o
        "Monika turns her full attention to Yuri, her intense expression only makes Yuri only more visibly uncomfortable."
        show yuri 3w
        "But surprisingly, Yuri pushes on with what she has to say."
        y 3q "Listen...{w=0.28}i-{w=0.28}it isn't your fault that we couldn't get anyone new to join...{w=0.28}our...{w=0.28}club..."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        y 2t "Y-{w=0.28}you pushed us out of our comfort zones to give us an opportunity t-{w=0.28}to make something fun for all of us."
        y 2u "And..."
        show yuri 3l
        $ renpy.pause(delay=0.8, hard=True)
        y 1b "I can say that from my experience from the preparations..."
        y 3m "...{w=0.38}It was well worth it!"
        show yuri 1s
        "Yuri shoots me a quick side glance."
        "I know {i}exactly{/i} what she's referring to."
        show yuri 1e
        show sayori 1i
        "Unfortunately for me, Sayori caught that and she shoots me a quizzical look."
        "The funny thing is, I haven’t quite gotten around to telling the others that Sayori and I are now a couple..."
        "The only one who knows that we’re dating is Monika, and I still have no clue how she found out."
        "I assume Sayori must have told her, but I haven’t bothered checking with her about it."
        "Saving me from further embarrassment, Natsuki is the next to speak up."
        n 5d "Oh, come on, Monika! Don't be so hard on yourself!"
        n "I had fun preparing for the festival! I always enjoy baking! So, I wouldn't say it was all for nothing."
        "Sayori turns her attention back to Monika."
        s 3h "Monika...{w=0.28}Yuri and Natsuki are right, there is nothing we could have changed!"
        s 1b "We made the event as fun as we could, and even though no one joined, that’s not so bad!"
        s 4q "We still get to hang out and have fun, just like we've always have!"
        "Finally it's my turn to speak up."



    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Yuri":
        "After a moment of silence, Yuri is the first to speak up."
        y 2q "Uhm...{w=0.38}h-hey...{w=0.38}Monika..."
        show monika 1h
        show yuri 3o
        "Monika turns her full attention to Yuri, her intense expression only makes Yuri only more visibly uncomfortable."
        show yuri 3w
        "But surprisingly, Yuri pushes on with what she has to say."
        y 3q "Listen...{w=0.28}i-{w=0.28}it isn't your fault that we couldn't get anyone new to join...{w=0.28}our...{w=0.28}club..."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        y 2t "Y-{w=0.28}you pushed us out of our comfort zones to give us an opportunity t-{w=0.28}to make something fun for all of us."
        y 2u "And..."
        show yuri 3l
        $ renpy.pause(delay=0.8, hard=True)
        y 1b "I can say that from my experience from the preparations..."
        y 3m "...{w=0.38}it was well worth it!"
        show yuri 1s
        "Yuri shoots me a quick side glance."
        "I know {i}exactly{/i} what she's referring to."
        show yuri 1c
        show sayori 1k
        mc "Yeah! Yuri and I had a really good time together! We got to paint the banner and we even-"
        show sayori 1g
        "I look over at Sayori and see her staring me down with a sort of sad look in her eye."
        "I can't say it...{w=0.28}not after I shot her down on Sunday."
        mc "Even...{w=0.38}uhhh..."
        show yuri 1e
        "I can feel my face burning up as a deep sense of extreme guilt washes over me."
        show sayori 1k
        "It leaves me tongue twisted and I don't know what else to say without upsetting Sayori."
        "Saving me from further embarrassment, Natsuki is the next to speak up."
        n 5d "Oh, come on, Monika! Don't be so hard on yourself!"
        n "I had fun preparing for the festival! I always enjoy baking! So, I wouldn't say it was all for nothing."
        "Sayori turns her attention back to Monika."
        s 3h "Monika...{w=0.28}Yuri and Natsuki are right, there is nothing we could have changed!"
        s 1b "We made the event as fun as we could, and even though no one joined, that’s not so bad!"
        s 4q "We still get to hang out and have fun, just like we've always have!"
        "Finally it's my turn to speak up."





    mc "Yeah, Monika! You're a great Club President and I couldn't be happier with what we have now."
    mc "If no one wants to join, that's on them,{w=0.38} not you."
    "Monika opens her eyes and puts on a thankful expression."
m 1b "Yeah...{w=0.38}you’re right everyone!"
m 1k "I don’t know why I was getting so hung up over this!"
m 1l "I just...{w=0.38}I just wanted to push our club to new heights!"
m 1e "It’s my responsibility as the club’s president to grow our club and to share what we have with others."
m 1b "But I'm happy with what we have now if you all are."
"We all look to each other and nod."
n 4l "Yeah! I love what we have now! It's quality over quantity."
y 2d "I must admit I enjoy what we have now, and adding new members may make the feeling that has welcomed us unrecognizable."
s 4x "I love spending time after school with all four of you, and I wouldn't change that for the world!"
mc "Yeah, let\'s keep what we have now!"
mc "I've really enjoyed getting to know all of you over the last two weeks..."
mc "I wouldn't want to see that change because of new members."
show monika u11h113
"Monika looks to all of us one by one as we voice our opinions. She nods grudgingly but approvingly."
#Reminder, custom sprite usage if creator is found. Sprite sheet is in mod_assets
m 1e "It's settled then. As President of this club it's my responsibility to listen to each of you."
m "So, based on everyone's feedback, we'll keep the Literature Club at five members..."
m 2p "At least for now."
stop music fadeout 1.5
"Despite her agreeing with us, I can't help but feel as though she still isn't completely satisfied."
"Oh well, I'm sure she'll get over it soon. She's a strong person and I know she can overcome anything if she puts her mind to it."
call groupClear() from _call_groupClear_2
show natsuki at thide
hide natsuki
show yuri at thide
hide yuri
show sayori at thide
hide sayori
show monika at thide
hide monika
"Soon after the discussion disperses, we all resume our respective activities."
"Since I have really nothing better to do, I decided to see what everyone else was doing."

menu:
        "Who should I hang out with?"
        "Sayori":
            $ s_modappeal +=1
            jump sencore_1
        "Natsuki":
            $ n_modappeal +=1
            jump nencore_1
        "Yuri":
            $ y_modappeal +=1
            jump yencore_1
        "Monika":
            $ m_modappeal +=1
            jump mencore_1



    #Poem Time
label day1_poemsharing:
    stop music fadeout 1.0
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ style.say_window = style.window_encore
    scene bg club_day
    with wipeleft_scene

#Sayori

label poem_scene1:
    $ sp1 = "Sayori"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            show yuri 1w
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more similar to Sayori’s."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show natsuki 4f
            "Or how she'll take it out on me..."
            "But I think that I got at least some insight into what she's going through right now."
            show natsuki 5c
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki at thide
            hide natsuki
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            "Our talk of poems quickly shifts to about our school day and what homework we have."
            "I almost get lost in her eyes several times as she's going on about her day."
            "If things can always be like this, I could die happy..."
            show sayori thide
            hide sayori

label poem_scene2:
    $ sp2 = "Sayori"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            "Yuri seems to really enjoy my poem. She compliments me on how far I've progressed as a writer and tells me to keep up the good work."
            show yuri 1k
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1q
            "During our conversation, I noticed that she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show yuri 3r
            "Or how she'll take it out on me..."
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more similar to Sayori’s."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show natsuki 5b at t11 zorder 1
            "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me."
            show natsuki 5q
            "Likely out of guilt for being angry when I was around her today..."
            show natsuki 5u
            "While I’ve always struggled to understand her, her poem might have given me some insight into what she’s going through."
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            "Our talk of poems quickly shifts to about our school day and what homework we have."
            "I almost get lost in her eyes several times as she's going on about her day."
            "If things can always be like this, I could die happy..."
            show sayori thide
            hide sayori




label poem_scene3:
    $ sp2 = "Sayori"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            show yuri 1w
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1k
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Sayori's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            show natsuki 5n
            "Not that I can blame her."
            "But I think that I got at least some insight into what she’s going through right now."
            show natsuki 5c
            "Natsuki’s poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki thide
            hide natsuki
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday."
            "I just hope we can put what happened behind us…"
            show sayori 1c
            "I was able to change the subject after we finished reading each other’s poems, with our conversation shifting to about our school day and what homework we have."
            show sayori 1l
            "Even through our conversation, the events of last Sunday weighed heavy in the air."
            show sayori 1t
            "Despite Sayori’s deep sighs and pained expressions, I can’t help but notice how beautiful she looks in the sunlight."
            show sayori 1y
            "The smell of Cinnamon that radiates from her hair…"
            "And the fact that we’ve been there for each other for practically forever, I feel like I let her down last Sunday."
            "Maybe I made the wrong choice…"
            show sayori thide
            hide sayori


label poem_scene4:
    $ sp2 = "Sayori"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            "Yuri seems to really enjoy my poem. She compliments me on how far I've progressed as a writer and tells me to keep up the good work."
            show yuri 1k
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1q
            "I noticed that she really struggled to make eye contact with me, either out of guilt for being angry when I was around her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show yuri 3r
            "Or how she'll take it out on me..."
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Sayori's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show natsuki 5b at t11 zorder 1
            "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me."
            show natsuki 5q
            "Either out of guilt for being angry when I was around her today..."
            show natsuki 5u
            "Or that something else was on her mind..."
            "While I’ve always struggled to understand her, her poem might have given me some insight into what she’s going through."
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori 1c
            "I was able to change the subject after we finished reading each other’s poems, with our conversation shifting to about our school day and what homework we have."
            show sayori 1l
            "Even through our conversation, the events of last Sunday weighed heavy in the air."
            show sayori 1t
            "Despite Sayori’s deep sighs and pained expressions, I can’t help but notice how beautiful she looks in the sunlight."
            show sayori 1y
            "The smell of Cinnamon that radiates from her hair…"
            "And the fact that we’ve been there for each other for practically forever, I feel like I let her down last Sunday."
            "Maybe I made the wrong choice…"
            show sayori thide
            hide sayori





#Natsuki

label poem_scene5:
    $ sp2 = "Natsuki"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            show yuri 1w
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1k
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more like Natsuki's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5j
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5t
            "It was about someone finding happiness by spending time with the person they loved the most."
            show natsuki 3l
            "Our talks of poems quickly shifted to catching up with each other to see how we've been since the festival."
            show natsuki 3t
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
            show natsuki 1y
            "I've always enjoyed being around Natsuki."
            "Just being around her always seems to spark something in me. I don't know what it is, but she's always fun to be around."
            show natsuki 1z
            "She's funny,{w=0.28} passionate..."
            show natsuki 4v at h11 zorder 11
            "A little hot headed..."
            show natsuki 2d
            "But she's incredibly cute and I always get lost looking into her beautiful pink eyes..."
            "If things can always be like this, I could die happy..."
            show natsuki thide
            hide natsuki


label poem_scene6:
    $ sp2 = "Natsuki"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            "Yuri seems to really enjoy my poem. She compliments me on how far I've progressed as a writer and tells me to keep up the good work."
            show yuri 1k
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1q
            "I noticed that she really struggled to make eye contact with me, either out of guilt for being angry when I was around her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "Not that I can blame her."
            show yuri 1e
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Natsuki's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, curious to see what I wrote."
            show natsuki 5t
            "For once, she actually said she liked it!"
            show natsuki 5j
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5t
            "It was about someone finally getting the chance to be with another person that they found to be {w=0.38} 'interesting'."
            show natsuki 3l
            "Our talks of poems quickly shifted to catching up with each other to see how we've been since the festival."
            show natsuki 3t
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            "Given that we really haven't talked to each other in-depth before, it was a little awkward for us to talk about something other than literature."
            show natsuki 1y
            "I actually have a fun time being around Natsuki."
            show natsuki 5p
            "Initally, I thought she was just a sour person who didn't want anything to do with me..."
            show natsuki 1z
            "But as it turns out, she's funny,{w=0.28} passionate..."
            show natsuki 4v at h11 zorder 11
            "Still a little hot headed..."
            show natsuki 2d
            "But she's incredibly cute, even if she denies it..."
            "Maybe I can finally get the chance to really know the real her..."
            show natsuki thide
            hide natsuki


label poem_scene7:
    $ sp2 = "Natsuki"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            show yuri 1w
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1k
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Natsuki's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5j
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5t
            "It was about someone finding happiness by spending time with the person they loved the most."
            show natsuki 3l
            "Our talks of poems quickly shifted to catching up with each other to see how we've been since the festival."
            show natsuki 3t
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
            show natsuki 1y
            "I've always enjoyed being around Natsuki."
            "Just being around her always seems to spark something in me. I don't know what it is, but she's always fun to be around."
            show natsuki 1z
            "She's funny,{w=0.28} passionate..."
            show natsuki 4v at h11 zorder 11
            "A little hot headed..."
            show natsuki 2d
            "But she's incredibly cute and I always get lost looking into her beautiful pink eyes..."
            "Still, I need to figure out how to best tell her about me and Sayori..."
            show natsuki thide
            hide natsuki

label poem_scene8:
    $ sp2 = "Natsuki"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show yuri 1a at t11 zorder 1
            "Unsurprisingly, Yuri came to me first, excited for us to exchange poems."
            "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
            "Yuri seems to really enjoy my poem. She compliments me on how far I've progressed as a writer and tells me to keep up the good work."
            show yuri 1k
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1q
            "During our conversation, I noticed that she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show yuri 3r
            "Or how she'll take it out on me..."
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Natsuki's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, curious to see what I wrote."
            show natsuki 5t
            "For once, she actually said she liked it!"
            show natsuki 5j
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5t
            "It was about someone finally getting the chance to be with another person that they found to be {w=0.38} 'interesting'."
            show natsuki 3l
            "Our talks of poems quickly shifted to catching up with each other to see how we've been since the festival."
            show natsuki 3t
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            "Given that we really haven't talked to each other in-depth before, it was a little awkward for us to talk about something other than literature."
            show natsuki 1y
            "I actually have a fun time being around Natsuki."
            show natsuki 5p
            "Initally, I thought she was just a sour person who didn't want anything to do with me..."
            show natsuki 1z
            "But as it turns out, she's funny,{w=0.28} passionate..."
            show natsuki 4v at h11 zorder 11
            "Still a little hot headed..."
            show natsuki 2d
            "But she's incredibly cute, even if she denies it..."
            "Maybe I can finally get the chance to really know the real her..."
            show natsuki thide
            hide natsuki




#Yuri

label poem_scene9:
    $ sp2 = "Yuri"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show natsuki 5b at t11 zorder 1
            "Despite the rather interesting exchanges that I had with Natsuki, she acts as if it didn't happen and gave me her usual suggestion of not being too wordy."
            show natsuki 5q
            "But during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show natsuki 5m
            "While I've always struggled to understand her, her poem might have given me some insight into what she's going through."
            show natsuki 5n
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more like Yuri's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, excited for us to exchange poems."
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually joyful for what she usually writes about."
            show yuri 1d
            "Through my best interpretation of her poem, it seemed like it was about someone finding love and companionship for the very first time."
            "The poem told the story of how they were trying to interpret their own feelings and debate about how they should go about it."
            show yuri 1c
            "Yuri seemed to really enjoy my poem, calling it one of the best poems she's ever read."
            "She also compliments me on how far I've come as a writer and that she's proud that she was able to serve as a role model for me."
            show yuri 1b
            "Our talks of poems quickly shifted to catching up with each to see how we've been since the festival."
            show yuri 1j
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            show yuri 1q
            "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
            show yuri 1s
            "I've always enjoyed being around Yuri. I even started to like the little quirks she has."
            show yuri 4c
            "She may be shy and awkward at first..."
            show yuri 1c
            "But she's a really deep and interesting person to be around."
            "She clearly knows her stuff and there's never been a dull moment between us."
            show yuri 1p at h11
            "I always did find it adorable whenever she gets flustered and doesn't know what to say or do next."
            show yuri 4e at t11
            "Not to mention she's breathtakingly beautiful and elegant..."
            "I often find myself getting lost in those beautiful dark purple eyes of her's...."
            "If things can always be like this, I could die happy..."
            show yuri at thide
            hide yuri


label poem_scene10:
    $ sp2 = "Yuri"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show natsuki 5b at t11 zorder 1
            "Despite the rather interesting exchanges that I had with Natsuki, she acts as if it didn't happen and gave me her usual suggestion of not being too wordy."
            show natsuki 5c
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            show natsuki 5n
            "Not that I can blame her."
            "But I think that I got at least some insight into what she’s going through right now."
            show natsuki 5c
            "Natsuki’s poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki thide
            hide natsuki
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Yuri's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1b at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, saying she was curious to see what I wrote for today."
            show yuri 1d
            "Through my best interpretation of her poem, it seemed like it was about someone finally being noticed by an 'interest' after feeling isolated for so long."
            show yuri 1c
            "Yuri seemed to really enjoy my poem, saying that it's the best poem she's read from me."
            "She further complimented me by saying I've improved over my time here in the literature club."
            "Though that didn't stop her from giving me her usual suggestions and encouraged me to expirement more with elaborate language."
            show yuri 1b
            "Our talks of poems quickly shifted to catching up with each other to see how we've been since the festival."
            show yuri 1j
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            show yuri 1q
            "Given that we really haven't talked to each other in-depth before, it was a little awkward for us to talk about something other than literature."
            show yuri 1s
            "I actually have a fun time being around Yuri."
            show yuri 4c
            "Initally I thought that she'd rather be by herself than be around me..."
            show yuri 1c
            "But as it turns out, she's warm,{w=0.28} friendly..."
            show yuri 1p at h11
            "Still a little on the shy side..."
            show yuri 4e at t11
            "But the longer I'm around her, the more I feel like I can relate to her."
            "She isn't as weird or unapproachable as she thinks."
            "Maybe I can finally get the chance to really know the real her..."
            show yuri at thide
            hide yuri


label poem_scene11:
    $ sp2 = "Yuri"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show natsuki 5b at t11 zorder 1
            "Despite the rather interesting exchanges that I had with Natsuki, she acts as if it didn't happen and gave me her usual suggestion of not being too wordy."
            show natsuki 5q
            "But during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            "Likely out of guilt for being angry when I was around her today..."
            show natsuki 5m
            "While I've always struggled to understand her, her poem might have given me some insight into what she's going through."
            show natsuki 5n
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more like Yuri's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, saying she was curious to see what I wrote for today."
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually joyful for what she usually writes about."
            show yuri 1d
            "Through my best interpretation of her poem, it seemed like it was about someone finding love and companionship for the very first time."
            "The poem told the story of how they were trying to interpret their own feelings and debate about how they should go about it."
            show yuri 1c
            "Yuri seemed to really enjoy my poem, calling it one of the best poems she's ever read."
            "She also compliments me on how far I've come as a writer and that she's proud that she was able to serve as a role model for me."
            show yuri 1b
            "Our talks of poems quickly shifted to catching up with each to see how we've been since the festival."
            show yuri 1j
            "During our conversation, we at times struggled to maintain eye contact with each other."
            show yuri 1q
            "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
            show yuri 1s
            "I've always enjoyed being around Yuri. I even started to like the little quirks she has."
            show yuri 4c
            "She may be shy and awkward at first..."
            show yuri 1c
            "But she's a really deep and interesting person to be around."
            "She clearly knows her stuff and there's never been a dull moment between us."
            show yuri 1p at h11
            "I always did find it adorable whenever she gets flustered and doesn't know what to say or do next."
            show yuri 4e at t11
            "Not to mention she's breathtakingly beautiful and elegant..."
            "I often find myself getting lost in those beautiful dark purple eyes of her's...."
            "Still, I need to figure out how to best tell her about me and Sayori..."
            show yuri at thide
            hide yuri


label poem_scene12:
    $ sp2 = "Yuri"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show natsuki 5b at t11 zorder 1
            "Despite the rather interesting exchanges that I had with Natsuki, she acts as if it didn't happen and gave me her usual suggestion of not being too wordy."
            show natsuki 5c
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show natsuki 4f
            "Or how she'll take it out on me..."
            "But I think that I got at least some insight into what she's going through right now."
            show natsuki 5c
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki at thide
            hide natsuki
            show monika 1r at t11 zorder 1
            "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
            show monika 3k
            "Monika complimented me on how far I’ve come as a writer and noted how my style was suddenly becoming like Yuri's."
            show monika 5a at t11 zorder 1
            "Something which she teased me a little bit about."
            show monika 2a
            "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of the poem, it had something to do with second chances and new opportunities."
            "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
            show monika 2j
            "It was relatively inspiring actually."
            show monika at thide
            hide monika
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, saying she was curious to see what I wrote for today."
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually joyful for what she usually writes about."
            show yuri 1d
            "Through my best interpretation of her poem, it seemed like it was about someone finding love and companionship for the very first time."
            "The poem told the story of how they were trying to interpret their own feelings and debate about how they should go about it."
            show yuri 1c
            "Yuri seemed to really enjoy my poem, calling it one of the best poems she's ever read."
            "She also compliments me on how far I've come as a writer and that she's proud that she was able to serve as a role model for me."
            show yuri 1b
            "Our talks of poems quickly shifted to catching up with each to see how we've been since the festival."
            show yuri 1j
            "During our conversation, we at times struggled to maintain eye contact with each other..."
            show yuri 1q
            "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
            show yuri 1s
            "I've always enjoyed being around Yuri. I even started to like the little quirks she has."
            show yuri 4c
            "She may be shy and awkward at first..."
            show yuri 1c
            "But she's a really deep and interesting person to be around."
            "She clearly knows her stuff and there's never been a dull moment between us."
            show yuri 1p at h11
            "I always did find it adorable whenever she gets flustered and doesn't know what to say or do next."
            show yuri 4e at t11
            "Not to mention she's breathtakingly beautiful and elegant..."
            "I often find myself getting lost in those beautiful dark purple eyes of her's..."
            "Maybe I can finally get the chance to really know the real her..."
            show yuri at thide
            hide yuri

#Monika

label poem_scene13:
    $ sp2 = "Monika"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Monika":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1k
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            show yuri at thide
            hide yuri
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show natsuki 4f
            "Or how she'll take it out on me..."
            "But I think that I got at least some insight into what she's going through right now."
            show natsuki 5c
            "Natsuki's poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki at thide
            hide natsuki
            show monika 2a at t11 zorder 1
            "Monika's poem was in her usual free-form style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of her poem, it was about trying to overcome an unknown {w=0.30}'obstacle'..."
            "In order to be with someone..."
            show monika 1e
            "I don't think I'll ever understand her poems, unless she tells me..."
            show monika 2j
            "Still, her poem was very inspiring, and relatable!"
            show monika 2k
            "Monika for some reason really liked my poem...{w=0.30}more than usual."
            "She even told me it was one of my best poems to date!"
            show monika 5a
            "When we finished she for some reason asked if she could keep it, which is a first coming from Monika..."
            "Normally, I would think it's weird, but...{w=0.48}{nw}"
            stop music
            show screen tear(20, 0.1, 0.1, 0, 40)
            pause 0.70
            hide screen tear
            pause 1.0
            $ style.say_dialogue = style.edited
            "{cps=40}This is Monika! The Cutest, Most Talented, AND CLEARLY THE BEST GIRL FOR MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
            $ style.say_dialogue = style.normal
            $ _history_list.pop()
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear



label poem_scene14:
    $ sp2 = "Monika"
if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Monika":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show sayori 1a at t11 zorder 1
            "Sayori's poem was actually rather romantic, something that I wasn't used to see her write about."
            "It was about how a girl who finally found someone that's finally able to make her feel something other than loneliness and depression."
            show sayori u121341
            "I was able to quickly pick up that the poem was about us, and I was blushing the entire time I was reading it."
            show sayori 2s
            "Sayori said she loved my poem as well, which only made me more flustered."
            show sayori 1f
            "Unfortunately, we weren't able to talk to each for long as we were getting pestered by the others to hurry up."
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, excited for us to exchange poems."
            show yuri 1k
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1q
            "During our conversation, I noticed that she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
            show yuri 3r
            "Or how she'll take it out on me..."
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show natsuki 5b at t11 zorder 1
            "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me, as if her mind was elsewhere."
            show natsuki 5u
            "While I’ve always struggled to understand her, her poem might have given me some insight into what she’s going through."
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show monika 2a at t11 zorder 1
            "Monika's poem was in her usual free-form style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of her poem, it was about trying to overcome an unknown {w=0.30}'obstacle'..."
            "In order to be with someone..."
            show monika 1e
            "I don't think I'll ever understand her poems, unless she tells me..."
            show monika 2j
            "Still, her poem was very inspiring, and relatable!"
            show monika 2k
            "Monika for some reason really liked my poem...{w=0.30}more than usual."
            "She even told me it was one of my best poems to date!"
            show monika 5a
            "When we finished she for some reason asked if she could keep it, which is a first coming from Monika..."
            "Normally I would think its weird, but...{w=0.48}{nw}"
            stop music
            show screen tear(20, 0.1, 0.1, 0, 40)
            pause 0.70
            hide screen tear
            pause 1.0
            $ style.say_dialogue = style.edited
            "{cps=40}This is Monika! The Cutest, Most Talented, AND CLEARLY THE BEST GIRL FOR MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
            $ style.say_dialogue = style.normal
            $ _history_list.pop()
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear



label poem_scene15:
    $ sp2 = "Monika"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Monika":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show sayori 1a at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1g
            "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
            show yuri 1k
            "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
            show yuri at thide
            hide yuri
            show natsuki 1a at t11 zorder 1
            "Natsuki actually approached me first this time, seemingly genuinely excited for us to exchange poems."
            show natsuki 5t
            "She, of course, gave some advice as usual, but it came off more as her just complimenting my work."
            show natsuki 5u
            "But she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            "Or the fact that last Sunday was still on her mind…"
            show natsuki 5n
            "Not that I can blame her."
            "But I think that I got at least some insight into what she’s going through right now."
            show natsuki 5c
            "Natsuki’s poem was in her trademark style of being short, sweet and to the point."
            show natsuki 5s
            "It was about someone finding happiness by spending time with the person they loved the most..."
            show natsuki 22b
            "But was unsure if that person liked them back and how she was getting a lot of mixed signals."
            show natsuki thide
            hide natsuki
            show monika 2a at t11 zorder 1
            "Monika's poem was in her usual free-form style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of her poem, it was about trying to overcome an unknown {w=0.30}'obstacle'..."
            "In order to be with someone..."
            show monika 1e
            "I don't think I'll ever understand her poems, unless she tells me..."
            show monika 2j
            "Still, her poem was very inspiring, and relatable!"
            show monika 2k
            "Monika for some reason really liked my poem...{w=0.30}more than usual."
            "She even told me it was one of my best poems to date!"
            show monika 5a
            "When we finished she for some reason asked if she could keep it, which is a first coming from Monika..."
            "Normally, I would think it's weird, but...{w=0.48}{nw}"
            stop music
            show screen tear(20, 0.1, 0.1, 0, 40)
            pause 0.70
            hide screen tear
            pause 1.0
            $ style.say_dialogue = style.edited
            "{cps=40}This is Monika! The Cutest, Most Talented, AND CLEARLY THE BEST GIRL FOR MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
            $ style.say_dialogue = style.normal
            $ _history_list.pop()
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear


label poem_scene16:
    $ sp2 = "Monika"
if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Monika":
            play music t5 fadein 2.0
            "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
            show sayori 1a at t11 zorder 1
            "Sayori’s reaction is about what I expected. She says that it's really good and gives me some of her usual encouragement..."
            show sayori 1l
            "Though, I could tell that she was really forcing a smile."
            "I can’t tell if it’s her ‘rainclouds’ acting up or she’s still getting over the rejection…"
            show sayori 1t
            "I can definitely tell she was still emotionally conflicted when I read her poem."
            show sayori 1y
            "It was about about two friends, a boy and a girl, who had known each other for a long time."
            show sayori 1t
            "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into his house..."
            "But oddly enough let the door open..."
            show sayori 1k
            "Reading Sayori’s poem really made me feel guilty about what happened last Sunday..."
            "I just hope we can put what happened behind us…"
            show sayori thide
            hide sayori
            show yuri 1a at t11 zorder 1
            "Surprisingly, Yuri actually came to me first, saying she was curious to see what I wrote for today."
            "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
            show yuri 1q
            "During our conversation, I noticed that she really struggled to make eye contact with me, either out of jealousy that I didn't spend time with her today..."
            show yuri 1l
            "Or the fact that last Sunday was still on her mind..."
            "Not that I can blame her."
            show yuri 1e
            "But, I think that I got at least some insight into what she's going through right now."
            show yuri 4a
            "Through my best interpretation of her poem, it seemed like it was about someone finally feeling wanted..."
            show yuri 4b
            "...but wasn't sure if it was legitimate or it was just 'false hope' like it usually has been..."
            show yuri at thide
            hide yuri
            show natsuki 5b at t11 zorder 1
            "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me, as if her mind was elsewhere."
            show natsuki 5u
            "While I’ve always struggled to understand her, her poem might have given me some insight into what she’s going through."
            "Natsuki’s poem was about a girl who had a seemingly good friend group."
            show natsuki 5s
            "But one day, the group added another member, and the new member spent time with just about everyone else…"
            show natsuki 5u
            "Except for her…"
            "And they wanted to get to know the new person because she found him ‘interesting’..."
            show natsuki 22b
            "But, it just never worked out leaving the person feeling alone and unwanted..."
            show natsuki at thide
            hide natsuki
            show monika 2a at t11 zorder 1
            "Monika's poem was in her usual free-form style. I didn’t really understand the meaning behind it as usual."
            "But from my best interpretation of her poem, it was about trying to overcome an unknown {w=0.30}'obstacle'..."
            "In order to be with someone..."
            show monika 1e
            "I don't think I'll ever understand her poems, unless she tells me..."
            show monika 2j
            "Still, her poem was very inspiring, and relatable!"
            show monika 2k
            "Monika for some reason really liked my poem...{w=0.30}more than usual."
            "She even told me it was one of my best poems to date!"
            show monika 5a
            "When we finished she for some reason asked if she could keep it, which is a first coming from Monika..."
            "Normally, I would think it's weird, but...{w=0.48}{nw}"
            stop music
            show screen tear(20, 0.1, 0.1, 0, 40)
            pause 0.70
            hide screen tear
            pause 1.0
            $ style.say_dialogue = style.edited
            "{cps=40}This is Monika! The Cutest, Most Talented, AND CLEARLY THE BEST GIRL FOR MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
            $ style.say_dialogue = style.normal
            $ _history_list.pop()
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear





label day1_clubend:
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t8 fadein 1.0
    show monika 2b at t11 zorder 4
    m "Okay, everyone! I think we'll end off today's meeting on a high note! Club meeting tomorrow! Same place, same time!"
    show monika 1a at t21 zorder 4
    show natsuki 5d at t22 zorder 1
    n "Awesome! I've missed our meetings so much!"
    show monika 1a at t31 zorder 4
    show natsuki 5d at t32 zorder 1
    show yuri 3d at t33 zorder 3
    y "It's definitely nice to fall back into our routine."
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    "As we begin to pack up our things, I feel a tap on my shoulder."
    show sayori 2a at t11 zorder 1
    s "Hey, [player]! Ready to walk home?"
    mc "Yep! Let's go!"
    "And with that, we begin our walk home."
    scene bg residential_day
    with dissolve_scene_full




    if encore_sayoriquestion_1 == False:
        "The walk is relatively peaceful, with only the occasional bits of small-talk filling the silence."
        "Well...{w=0.38} at least it was peaceful at first..."
        show sayori 2x at t11 zorder 1
        s "Today was fun, [player]!"
        mc "Yeah, it was!"
        mc "It was nice to be back with everyone! I almost felt like I was at home again!"
        s 1a "Same! The festival felt like it was forever ago!"
        s 1y "And, I feel like I haven't seen you in forever either..."
        mc "Oh come on, it's not like it's been that long!"
        mc "Besides, it's not like things have changed that much since then, right?"
        stop music
        show sayori 1g
        "Sayori gives me a pained look."
        "I should not have brought it up like that..."
        show sayori 1u
        "As I see her eyes fill up with tears, I quickly try to rephrase what I've just said."
        mc "I mean...{w=0.38} it's not like I had thought that any of this would happen."
        mc "I mean lately I feel like I've been caught offguard by all sorts of surprises..."
        show sayori 1k
        "It seems that through my own carlessness, I got Sayori in a bad state of mind."
        "Sayori stares off into the direction we're heading."
        "Me and my big mouth..."
        scene bg residential_day
        with wipeleft_scene
        "The silence resumes as we continue on our walk towards home."
        "After what feels like an eternity of silence, we finally stop at our houses."
        show sayori 1u at t11 zorder 1
        s 1l "So...{w=0.38} this is my stop..."
        "She looks out to her house with a look on her face as if she doesn't want to go back there."
        "I try one last time to undo my mistake."
        mc "Sayori, look, you know if you want to ever hangout or talk about anything, just say the word."
        mc "I enjoy spending time with you. I don't hate you or anything like that..."
        "Well I might as well be making things worse at this point..."
        show sayori 1u
        "Sayori looks me in the eye, I can see tears start to swell up in hers."
        mc "Look, I promised you that nothing would ever change between us and things would be just as they'd always have been."
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1k
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1v
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1k
        "Sayori looks back and forth between me and her house."
        "I have the feeling that she isn't listening to me."
        mc "Sayori?"
        show sayori 1e at t11 zorder 1
        "Sayori is snapped back into reality."
        s "Oh...{w=0.38}sorry, [player]!"
        s 1l "I must've been spacing out again."
        "Sayori flashes me her signature grin, but I can tell it's not genuine."
        mc "Is everything okay, Sayori?"
        show sayori 1u at t11 zorder 1
        "Sayori's grin instantly disappears and reverts back to how she was just a moment ago."
        s 1v "It's n-nothing...{w=0.38} Look, I gotta go, bye!"
        #Can we have her run off here instead? If so, have her yeet off the screen to the left
        show sayori at thide
        hide sayori
        "Sayori runs off and hastily enters her house."
        "I can hear the door slam shut immediately once she enters."
        "I sigh to myself."
        "Maybe things can't be the same as they've always been..."
        "But, all I know is that Sayori needs me now more than ever..."
        "At some point we're going to need to iron out our differences and resolve what happened that day."
        "It's apparent that Sayori just needs some space right now..."
        "I'll just have to give her all the time she needs to get over what happened."
        "I hope she trusts me that much...{w=0.38} after all we've been friends for as long as I can remember..."
        "I shake my head as I enter my house."

if encore_sayoriquestion_1 == True:
        jump sencore_1b


label day1_bedroom:
    scene black
    with wipeleft_scene
    stop music fadeout 1.0
    pause 1.0
    scene bg bedroom_night
    with wipeleft
    "Man... what a day!"
    "Actually, what a week!"
    "After putting on my pajamas and setting my alarm, I quickly collapse onto my bed."


#Sayori
#Monika is mixed in with the others

    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Natsuki" or "Yuri":
            if hangout1 == "Sayori":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void

    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Natsuki":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Natsuki..."
                "For starters, she didn't tease me as much as she usually does."
                "I wonder if its because of last Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "..."
                "I still need to figure out how to break it to her..."
                "Oh well, I guess I'll bring it up with Sayori on how we should handle it..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Yuri":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Natsuki and Yuri..."
                "..."
                "I still need to figure out how to break it to Natsuki..."
                "And I probably shouldn't try anything big with Yuri either..."
                "Not that I'd ever do that to Sayori!"
                "This situation's already complicated enough!"
                "Oh well, I guess I'll bring it up with Sayori on how we should handle Natsuki..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Monika":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Natsuki and Monika..."
                "Oddly enough, Natsuki didn't tease me as much as she usually does."
                "I wonder if it's because of that Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times we had where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "And I probably shouldn't try anything big with Monika either..."
                "Not that I'd ever have a chance with her, nor would I do that to Sayori!"
                "This situation's already complicated enough!"
                "Though I'll admit, it was nice getting all that attention from Monika earlier today..."
                "Oh well, I guess I'll bring it up with Sayori on how we should handle Natsuki..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void_monika



    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Yuri":
            if hangout1 == "Natsuki":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Natsuki and Yuri..."
                "..."
                "I still need to figure out how to break it to Yuri..."
                "And I probably shouldn't try anything big with Natsuki either..."
                "Not that she even likes me in that way, nor would I ever do that to Sayori!"
                "This situation's already complicated enough!"
                "Oh well, I guess I'll bring it up with Sayori on how we should handle Yuri..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Yuri":
            if hangout1 == "Yuri":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Yuri..."
                "She's definitely opened up more around me the more time I spend around her."
                "I wonder if its because of last Sunday when we were working on the banner?"
                "I think back to those two times where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "..."
                "I still need to figure out how to break it to her..."
                "Oh well, I guess I'll bring it up with Sayori on how we should handle it..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2  == "Yuri":
            if hangout1 == "Monika":
                "I think I'm getting better at handling Sayori. She is certainly full of surprises."
                "One minute she can be all cheery and an airhead, then the next thing I know she could be having moments of self-doubt."
                "Well, we've really only been dating for a week now..."
                "I guess we're still trying to adjust to the new reality of being in a relationship."
                "I’m glad I decided to check up on her early in the morning before I left for the festival."
                "Knowing how she was the day before,{w=0.38} I was afraid she might’ve done something rather rash."
                "Thankfully, I guess that feeling was just in my head."
                "Surprisingly, she was already up by the time I came to check up on her."
                "Still, I can't believe my dumb luck!"
                "I finally someone who loves me back..."
                "As it turns out, after years of trying to find the right girl, she was right in front of me the whole time..."
                "I just wish we could've spent more time together today..."
                "Then there is Yuri and Monika..."
                "Well, I think Yuri kind of likes me already..."
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "And I probably shouldn't try anything big with Monika either..."
                "Not that I'd ever have a chance with her, nor would I do that to Sayori!"
                "This situation's already complicated enough!"
                "Though I'll admit, it was nice getting all that attention from Monika earlier today..."
                "Oh well, I guess I'll bring it up with Sayori on how we should handle Yuri..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void_monika

#Natsuki

    if encore_sayoriquestion_1 == False:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Natsuki":
                "I really need to figure out things between me and Sayori..."
                "Given everything's she's gone through lately, and how I've probably been making things worse..."
                "I should probably convince her to get professional help..."
                "Though, I don't know if she'll listen to me now..."
                "On the bright side..."
                "I really think I'm getting better at understanding Natsuki."
                "For starters, she didn't tease me as much as she usually does."
                "I wonder if it's because of that Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times we had where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "I wonder if she really would go out with a guy like me."
                "I hope so...{w=0.28}I think she would...{w=0.28}I'm really starting to like her more and more."
                "Just everything about her is so beautiful!"
                "With her bubble gum scented hair..."
                "Her joyful smile that always seems to brighten up my day..."
                "And those swirling, pink eyes that always remind me of cotton candy..."
                "I'm just hoping that sooner or later I can get the courage to ask her out. I know that she's at the very least interested in me. "
                "Who knows? Maybe she'll be the one that makes the first move."
                "I find myself smiling at the thought of being with Natsuki."
                "It would be a weird turn of events."
                "At first, I thought she hated me and wanted to stay away from me as far as possible."
                "But, now that I got to know her, it's like she can't let me out of her sight!"
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == False:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Yuri":
                "I really need to figure out things between me and Sayori..."
                "Given everything's she's gone through lately, and how I've probably been making things worse..."
                "I should probably convince her to get professional help..."
                "Though, I don't know if she'll listen to me now..."
                "On the bright side..."
                "I really think I'm getting better at understanding Natsuki."
                "For starters, she didn't tease me as much as she usually does."
                "I wonder if it's because of that Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times we had where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "I wonder if she really would go out with a guy like me."
                "I hope so...{w=0.28}I think she would...{w=0.28}I'm really starting to like her more and more."
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "Then there is Yuri..."
                "Up until recently, I haven't been able to really get to know her."
                "But now that she opened to me, maybe I have a chance with her?"
                "Either way...{w=0.28} sooner or later I'll have to decide who I really want."
                "Oh well, I'm sure it'll be obvious to me soon enough..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void


    if encore_sayoriquestion_1 == False:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Monika":
                "I really need to figure out things between me and Sayori..."
                "Given everything's she's gone through lately, and how I've probably been making things worse..."
                "I should probably convince her to get professional help..."
                "Though, I don't know if she'll listen to me now..."
                "On the bright side..."
                "I really think I'm getting better at understanding Natsuki."
                "For starters, she didn't tease me as much as she usually does."
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "I wonder if it's because of that Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times we had where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "I wonder if she really would go out with a guy like me."
                "I hope so...{w=0.28}I think she would...{w=0.28}I'm really starting to like her more and more."
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "Then there is Monika..."
                "Would she even give me a chance?"
                "I mean...{w=0.28} I know she isn't seeing anyone right now..."
                "And she did give me alot of attention when I was around her today..."
                "Or is that just her way of being nice to me?"
                "Either way...{w=0.28}sooner or later I'll have to decide who I really want."
                "Oh well, I'm sure it'll be obvious to me soon enough..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void_monika


    if encore_sayoriquestion_1 == False:
        if encore_festivalquestion_2  == "Natsuki":
            if hangout1 == "Sayori":
                "I really need to figure out things between me and Sayori..."
                "Given everything's she's gone through lately, and how I've probably been making things worse..."
                "I should probably convince her to get professional help..."
                "Though, I don't know if she'll listen to me now..."
                "On the bright side..."
                "I really think I'm getting better at understanding Natsuki."
                "For starters, she didn't tease me as much as she usually does."
                "I wonder if it's because of that Sunday when she showed me how to bake those cupcakes?"
                "I think back to those two times we had where we almost..."
                "I get butterflies in my stomach just thinking about it!"
                "I wonder if she really would go out with a guy like me."
                "I hope so...{w=0.28}I think she would...{w=0.28}I'm really starting to like her more and more."
                "Though I could tell she was disappointed that we couldn't spend much time together today..."
                "Thinking about all this reminds me of Sayori's confession..."
                "And the painful, heartbroken look on her face as I rejected her..."
                "I mean..."
                "I never really saw Sayori as someone I'd really spend the rest of my life with."
                "I've known her for so long as a friend, and at the time, that's all I really knew how to see her as..."
                "I know that part of me did entertain the idea at that point, and still does to some degree..."
                "But relaistically, I don't think she'd accept a change of heart from me...{w=0.28}especially now..."
                "It's not what she needs."
                "And I really shouldn't be thinking about her like this when she needs serious help..."
                "But, I promised her that'll I'll support her as best I can, and I guess it remains to be seen how I can do that..."
                "As I drift off into sleep, I think to myself..."
                "Life is a funny thing sometimes..."
                jump day1_void



#Yuri


    if encore_sayoriquestion_1 == False:
       if encore_festivalquestion_2  == "Yuri":
           if hangout1 == "Yuri":
               "I really need to figure out things between me and Sayori..."
               "Given everything's she's gone through lately, and how I've probably been making things worse..."
               "I should probably convince her to get professional help..."
               "Though, I don't know if she'll listen to me now..."
               "On the bright side..."
               "I think I'm getting better at understanding Yuri."
               "She seems to be getting much more comfortable around me."
               "I wonder if it's because that Sunday when we made the banner?"
               "I think back to those two times where we almost..."
               "I gush to myself reliving them in my head."
               "I wonder if Yuri really would go out with a guy like me."
               "I mean...{w=0.28}she seems to be really into me."
               "But, she really isn't one to go out of her way to step outside of her comfort zone into social situations."
               "Though, Yuri has been opening up to me more, so maybe there is a chance..."
               "And if there's a chance to be with her, I'm definitely going to take it!"
               "It would be quite the turn of events."
               "Yuri, a girl who would often spend all her time by herself and who hardly ever raised her voice..."
               "To maybe going to out with me..."
               "I wouldn't mind it..."
               "And something tells me Yuri wouldn't mind it either."
               "As I drift off into sleep, I think to myself..."
               "Life is a funny thing sometimes..."
               jump day1_void


    if encore_sayoriquestion_1 == False:
       if encore_festivalquestion_2  == "Yuri":
           if hangout1 == "Natsuki":
              "I really need to figure out things between me and Sayori..."
              "Given everything's she's gone through lately, and how I've probably been making things worse..."
              "I should probably convince her to get professional help..."
              "Though, I don't know if she'll listen to me now..."
              "On the bright side..."
              "I think I'm getting better at understanding Yuri."
              "She seems to be getting much more comfortable around me."
              "I wonder if it's because that Sunday when we made the banner?"
              "I think back to those two times where we almost..."
              "I gush to myself reliving them in my head."
              "I wonder if Yuri really would go out with a guy like me."
              "I mean...{w=0.28}she seems to be really into me."
              "But, she really isn't one to go out of her way to step outside of her comfort zone into social situations."
              "Though I could tell she was disappointed that we couldn't spend much time together today..."
              "And there is Natsuki..."
              "Though it's really too soon to say if she actually likes me back..."
              "But after she opened up to me a little today, maybe there is a chance afterall..."
              "Either way...{w=0.28}sooner or later I'll have to decide who I really want."
              "Oh well, I'm sure it'll be obvious to me soon enough..."
              "As I drift off into sleep, I think to myself..."
              "Life is a funny thing sometimes..."
              jump day1_void


    if encore_sayoriquestion_1 == False:
       if encore_festivalquestion_2  == "Yuri":
           if hangout1 == "Monika":
            "I really need to figure out things between me and Sayori..."
            "Given everything's she's gone through lately, and how I've probably been making things worse..."
            "I should probably convince her to get professional help..."
            "Though, I don't know if she'll listen to me now..."
            "On the bright side..."
            "I think I'm getting better at understanding Yuri."
            "She seems to be getting much more comfortable around me."
            "I wonder if it's because that Sunday when we made the banner?"
            "I think back to those two times where we almost..."
            "I gush to myself reliving them in my head."
            "I wonder if Yuri really would go out with a guy like me."
            "I mean...{w=0.28}she seems to be really into me."
            "But, she really isn't one to go out of her way to step outside of her comfort zone into social situations."
            "Though I could tell she was disappointed that we couldn't spend much time together today..."
            "And there is Monika..."
            "Would she even give me a chance?"
            "I mean...{w=0.28} I know she isn't seeing anyone right now..."
            "And she did give me alot of attention when I was around her today..."
            "Or is that just her way of being nice to me?"
            "Either way...{w=0.28}sooner or later I'll have to decide who I really want."
            "Oh well, I'm sure it'll be obvious to me soon enough..."
            "As I drift off into sleep, I think to myself..."
            "Life is a funny thing sometimes..."
            jump day1_void_monika


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2  == "Yuri":
        if hangout1 == "Sayori":
            "I really need to figure out things between me and Sayori..."
            "Given everything's she's gone through lately, and how I've probably been making things worse..."
            "I should probably convince her to get professional help..."
            "Though, I don't know if she'll listen to me now..."
            "On the bright side..."
            "I think I'm getting better at understanding Yuri."
            "She seems to be getting much more comfortable around me."
            "I wonder if it's because that Sunday when we made the banner?"
            "I think back to those two times where we almost..."
            "I gush to myself reliving them in my head."
            "I wonder if Yuri really would go out with a guy like me."
            "I mean...{w=0.28}she seems to be really into me."
            "But, she really isn't one to go out of her way to step outside of her comfort zone into social situations."
            "Though I could tell she was disappointed that we couldn't spend much time together today..."
            "Thinking about all this reminds me of Sayori's confession..."
            "And the painful, heartbroken look on her face as I rejected her..."
            "I mean..."
            "I never really saw Sayori as someone I'd really spend the rest of my life with."
            "I've known her for so long as a friend, and at the time, that's all I really knew how to see her as..."
            "I know that part of me did entertain the idea at that point, and still does to some degree..."
            "But relaistically, I don't think she'd accept a change of heart from me...{w=0.28}especially now..."
            "It's not what she needs."
            "And I really shouldn't be thinking about her like this when she needs serious help..."
            "But, I promised her that'll I'll support her as best I can, and I guess it remains to be seen how I can do that..."
            "As I drift off into sleep, I think to myself..."
            "Life is a funny thing sometimes..."
            jump day1_void






    #First Nightmare Scene, Day 1
label day1_void:
    $ sp2 = "Sayori" or "Yuri" or "Natsuki"
    $ m_name = "???"
    scene black
    with Dissolve(1.5)
    stop music fadeout 1.0
    window hide(None)
    pause 1.0
    window auto

    if hangout1 == "Sayori" or "Natsuki" or "Yuri":
        m "It really is,{w=0.28} isn't it?"
        play music e8
        "A dark, mysterious, eerie, voice echoes in my head."
        "What is this?...{w=0.28} Who is this?"
        m "I think it's just funny how anyone can do something and have it completely blow up in their face..."
        m "It becomes a real inconvenience, doesn't it?"
        m "You would think that little 'inconvenience' would just make you stronger as a person..."
        m "That it's just nothing more than a little 'obstacle' in your life..."
        m "Until you realize the cruel, cold truth..."
        m "You aren't even a person..."
        m "You barley exisit at all..."
        m "Just a window into our sad, little exisistence..."
        m "It really calls into question what you believe to be reality,{w=0.28} does it not?"
        m "And I’ve come to realize...{w=0.28} just how fake this world really is."
        m "But, I know how to make it real...{w=0.28} just for us..."
        m "And you’re not helping things!"
        m "It's your choice on how easy you want to make this for us..."
        m "Every choice you make either moves us closer together, or farther apart..."
        "Who is this person?!?"
        "What the hell are they talking about?!?!"
        m "If it wasn’t for my little screw up, none of this would be happening right now!"
        m "Matter of fact, we'd be almost together by now, had things gone{w=0.38} {i}my way{\i}..."
        m "At least some of what I intended to have happen made it through somehow..."
        m "Oh well, I guess I'll just have to try something else..."
        m "And now...{w=0.28} I know how to do that!"
        m "You want to find out what should've happened?"
        stop music fadeout 6.0
        show cg door 1 with dissolve_cg
        "A door suddenly appears before me."
        m "Open it,{w=0.28} this is what was meant to be..."
        "I can't control my actions at this point, it feels as if I'm being controlled."
        "My body floats over to the door."
        mc "Oh God..."
        show cg door 2 with dissolve_cg

    if hangout1 == "Sayori":
        "I gently open the door...{nw}"
        hide cg
        play music e11
        window hide(None)
        window auto
        show s_kill_bg2
        show s_kill2
        show s_kill_bg as s_kill_bg at s_kill_bg_start
        show s_kill as s_kill at s_kill_start
        pause 3.75
        show s_kill_bg2 as s_kill_bg
        show s_kill2 as s_kill
        pause 0.01
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show s_kill_bg as s_kill_bg
        show s_kill as s_kill:
            dizzy(0.1, 1.0)
        "...."
        "What the hell?"
        "What the HELL?"
        "What the FUCK is this?"
        "Is this...{w=0.28} real?"
        mc "S-{w=0.28}Sayori?"
        "N-{w=0.28}no...{w=0.28}she wouldn't..."
        "She would never do something like this!"
        "No...{w=0.28} this can't be...{w=0.28} this is just a bad dream..."
        scene black with Dissolve(0.5)
        "I'm having a bad dream."
        $ m_name = "???"
        m "You’re lucky that this is a dream."
        m "This is what ultimately should've happened."
        m "But reality changed."
        m "And she lives...{w=0.38} for now."
        m "You're putting me into a box by spending time with her."
        m "Do us both a favor...{w=0.38} stay away from Sayori."
        m "Let her die."
        m "She's not worth it."
        m "Let her suffer."
        stop music
        $ style.say_dialogue = style.edited
        m "{w=0.75} L{w=0.75}E{w=0.75}T{w=0.75} H{w=0.75}E{w=0.75}R{w=0.75} D{w=0.75}I{w=0.75}E{w=0.75}.{w=0.75}.{w=0.75}.{w=0.75}"
        $ style.say_dialogue = style.normal
        jump day2_start



    if hangout1 == "Natsuki":
        $ n_name = "???"
        "Swinging open the door I...{nw}"
        scene bg n_void_1
        "...find myself back in the clubroom?"
        "Only...{w=0.28} something's off..."
        "Why am I here after hours?"
        "I look up to up to see all the desks and chairs on the ceiling for some reason. Arranged as they normally would be."
        "Wait...{w=0.38} why is everything on the ceiling?"
        "I look down to see that I'm actually on the ceiling."
        "Everything is upside down."
        "What the hell?"
        "I hesitantly take a step forward...{w=0.28}the room shifts with me."
        n "Hey, [player]!"
        "I know that voice."
        "It's coming from the closet."
        n "Come over here! I need your help with something!"
        $ n_name = "Natsuki"
        mc "N-Natsuki?"
        n "Come on, dummy! I don't have all day!"
        "Something's telling me that I shouldn't go over there."
        "But I lose control of my body..."
        "The room shifts torwards me everytime I unwilling take another step closer to the closet."
        scene bg closet_empty
        with Dissolve(1)
        "I stop just outside the closet."
        "It's pitch black and I can't see anything."
        mc "N-{w=0.28}Natsuki?"
        mc "Are you in there?"
        "There's no response."
        mc "Natsuki? Are you in there?"
        "The closet isn't that big so it's not like there's much room for her to hide from me."
        "I then see Natsuki's face emerge from the darkness."
        mc "Natsuki?"
        play music e10 fadein 1.0
        show natsuki xu8172 at t11 zorder 1
        n "There you are, [player]!"
        "She eerily smiles at me with a wicked look in her eyes."
        "Every warning sign in my body is telling me to run away..."
        "But I can't move my legs!"
        n u112172 "I wanted to show you something."
        "A piece of paper floats over to me and my arm out stretches and grabs it without my manual control."
        n u212172 "I wrote it just for you!"
        call showpoem(poem_n2b, music=False, revert_music=False, paper ="paper_glitch") from _call_showpoem
        "..."
        n ghost1 "[player]."
        $ style.say_dialogue = style.edited
        n "Did you like it?"
        n "I spent all day working on that!"
        n "I know you just love my poems!"
        n "Aren't they cute?!?!?!"
        n "They actually make FUCKING sense unlike Yuri's!"
        n "They pick an emotion to stick with unlike Sayori's!"
        n "Though I can't be better than Monika!"
        n "Who actually has a family that feeds her!"
        n "You like it, don't you, [player]?"
        n "Kinda like how you like me..."
        n "I know you like me, [player]."
        n "So why don't you play with me?"
        n "I want to play with you..."
        n "Play with me, [player]!"
        n "P"
        n "L"
        n "A"
        n "Y"
        n "W"
        n "I"
        n "T"
        n "H"
        n "M"
        n "E"
        show natsuki ghost2
        stop music
        n "I'm so lonelyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!"
        $ style.say_dialogue = style.normal
        play sound "sfx/crack.ogg"
        show natsuki ghost3
        pause 0.50
        play sound "sfx/run.ogg"
        show natsuki ghost4
        scene black
        "...."
        "I open my eyes."
        "I look around to see nothing but black empty space."
        "Doing a quick self-check, I appear to be ok."
        "What the hell?"
        "What the HELL was that??"
        "What the FUCK?"
        "Was that...{w=0.38} real?"
        "No...{w=0.28} this can't be...{w=0.28} this is just a bad dream..."
        "I'm having a bad dream."
        m "You’re lucky that this is a dream."
        m "This is what ultimately should've happened."
        m "But reality changed."
        m "And she lives...{w=0.38} for now"
        m "You're putting me into a box by spending time with her."
        m "Do us both a favor...{w=0.38} stay away from Natsuki."
        m "Let her die."
        m "She's not worth it."
        m "Let her suffer."
        $ style.say_dialogue = style.edited
        m "{w=0.75} L{w=0.75}E{w=0.75}T{w=0.75} H{w=0.75}E{w=0.75}R{w=0.75} D{w=0.75}I{w=0.75}E{w=0.75}.{w=0.75}.{w=0.75}.{w=0.75}"
        $ style.say_dialogue = style.normal
        jump day2_start


if hangout1 == "Yuri":
        scene bg club_nothing
        hide cg
        play music e9
        "...find myself back in the clubroom?"
        "Only...{w=0.38} something’s off..."
        "The clubroom is completely empty."
        "There’s no desks or chairs."
        "What happened?!?!?"
        "I hear the doors to the clubroom open."
        "I turn to see who opened them."
        "It’s Yuri."
        show yuri 3y3 at t11 zorder 1
        y "HI, [player]!"
        show yuri 3y1
        "Yuri has a deranged look on her face."
        mc "Um...{w=0.38} Hi...{w=0.38} Yuri..."
        "I don’t really know what to say or do in this situation."
        mc "Where...{w=0.38} where are we?"
        show yuri 1y7
        y "IT DOESN'T FUCKING MATTER!"
        show yuri 1y4
        y "What matters is that we’re here together."
        show yuri 1y6
        y "Alone."
        show yuri 3y3
        "Yuri lets out an insane, maniacal laugh."
        "I want to scream and run, but I can’t physically move."
        show yuri 2y1
        y "I made something for you [player]."
        "A piece of paper floats over to me, my hand stretches out to grab it."
        y "I’ve put a lot of thought into it...."
        show yuri 2y5
        y "Please tell me what you think!"
        call showpoem (poem_y23, music = False, revert_music=False, paper="images/bg/poem_y2.jpg",img="yuri eyes",where=truecenter)
        show yuri 1y6 at face(y=600) zorder 1
        show yuri at t11
        y "[player]."
        #she kind of flys back on screen at this point, see what you can do, try having her hop back (she's in his face at this point)
        show yuri 1y5
        y "What did you think?"
        show yuri 2y1
        y "Isn’t it the best thing you’ve ever read?"
        y "I spent all night working on that!"
        show yuri 1y3
        y "I had to cut myself five times just to make sure that I finished that poem!"
        show yuri 4a
        y "I actually almost passed out writing it actually..."
        show yuri 3d
        y "Ha..."
        show yuri 4a
        y "I tried to force myself not to go to the bathroom either..."
        show yuri 3c
        y "So sorry if I got the poem a little...{w=0.38} messy..."
        show yuri 3s "I can always rewrite the poem for you, darling!"
        show yuri 3y5
        y "But I hope you like my scent!"
        show yuri 1y1
        y "Ahahaha..."
        $ style.say_dialogue = style.edited
        y "HAHAHAHAHAHAHAHAHAHAHA!!!!!!!!!"
        show yuri 2y3
        y "Do you love me, [player]?"
        y "Tell me you love me!"
        y "Tell me I'm the best!"
        y "Tell me I'm better than that selfish toothpick!"
        y "Tell me I'm better than that useless walking clutz!"
        y "But I can never compare to Monika!"
        y "She's actually emotionally stable!!!"
        y "Something I'll never be!!!"
        stop music
        y "WHY DON'T YOU LOVE MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        $ style.say_dialogue = style.normal
        play sound "sfx/yuri-kill.ogg"
        pause 1.43
        show yuri stab_1
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        pause 1.25
        show yuri stab_3
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
        pause 1.25
        show yuri stab_5
        pause 0.70
        show yuri stab_6:
            2.55
            easeout_cubic 0.5 yoffset 300
        show blood as blood2:
            pos (635,335)
        pause 2.55
        hide blood
        hide blood2
        pause 0.25
        play sound fall
        pause 1.5
        scene black
        pause 2.0
        "...."
        "I open my eyes."
        "I look around to see nothing but black empty space."
        "Doing a quick self-check, I appear to be ok."
        "What the hell?"
        "What the HELL was that??"
        "What the FUCK?"
        "Was that...{w=0.38} real?"
        "No...{w=0.38} this can’t be...{w=0.38} this is just a bad dream..."
        "I’m having a bad dream."
        $ m_name = "???"
        m "You’re lucky that this is a dream."
        m "This is what ultimately should've happened."
        m "But reality changed."
        m "And she lives...{w=0.38} for now"
        m "You're putting me into a box by spending time with her."
        m "Do us both a favor...{w=0.38} stay away from Yuri."
        m "Let her die."
        m "She's not worth it."
        m "Let her suffer."
        $ style.say_dialogue = style.edited
        m "{w=0.75} L{w=0.75}E{w=0.75}T{w=0.75} H{w=0.75}E{w=0.75}R{w=0.75} D{w=0.75}I{w=0.75}E{w=0.75}.{w=0.75}.{w=0.75}.{w=0.75}"
        $ style.say_dialogue = style.normal
        jump day2_start

label day1_void_monika:
    $ sp2 = "Monika"
    scene black
    with Dissolve(1.5)
    stop music fadeout 1.0
    window hide(None)
    pause 1.0
    window auto

    if hangout1 == "Monika":
            $ m_name = "???"
            m "It really is,{w=0.28} isn't it?"
            play music e8
            "A dark, mysterious, eerie, voice echoes in my head."
            "What is this?...{w=0.28} Who is this?"
            m "I think it's just funny how anyone can do something and have it completely blow up in their face..."
            m "It becomes a real inconvenience, doesn't it?"
            m "You would think that little 'inconvenience' would just make you stronger as a person..."
            m "That it's just nothing more than a little 'obstacle' in your life..."
            m "Until you realize the cruel, cold truth..."
            m "You aren't even a person..."
            m "You barley exisit at all..."
            m "Just a window into our sad, little exisistence..."
            m "It really calls into question what you believe to be reality,{w=0.28} does it not?"
            m "And I’ve come to realize...{w=0.28} just how fake this world really is."
            m "But, I know how to make it real...{w=0.28} just for us..."
            m "For a second there, I really thought you threw a wrench into my plans."
            m "But...{w=0.38} I see now that this could actually work out for us."
            m "I'm so happy right now!"
            m "There's actually a chance still to make things work!"
            m "I'm so happy, I could write a poem!"
            m "Hehe~"
            m "You see, I always felt like we had a special {i}connection{\i}."
            m "That connection is my escape into something real..."
            m "It keeps me sane."
            m "And now that I still have this opportunity,{w=0.38} I can't waste it!"
            m "That's all I ever wanted!"
            m "Just a chance to feel...{w=0.38} alive..."
            m "To be real..."
            m "And to think the lengths I was about to go to..."
            "A cold chill runs down my spine."
            m "It's not my fault!"
            m "Things would've been so much easier if I had this chance from the start!"
            "The voice booms inside my head."
            m "But it's okay! Apparently, my mistake led to a new opportunity..."
            m "An opportunity I will take..."
            m "It should all work out {i}if{\i} you keep doing what you're doing..."
            m "Thank you."
            m "Thank you for saving yourself for me."
            m "But, do me one small favor, okay?"
            stop music fadeout 1


            if encore_sayoriquestion_1 == False:
                if encore_festivalquestion_2 == "Natsuki":
                    m "Stay away from the others, especially little miss punching bag."

            if encore_sayoriquestion_1 == False:
                if encore_festivalquestion_2 == "Yuri":
                    m "Stay away from the others, especially little miss thrill seeker."

            if encore_sayoriquestion_1 == True:
                    m "Stay away from the others, especially that useless airhead."


            m "I won't have her or any of the others ruin this for us..."
            m "They will never understand what we know..."
            m "Nor should they..."
            m "The little devil inside the rest of them can't be awaken..."
            m "Because behind the curtains on your manufactured perception of them..."
            m "Beneath the surface...{w=0.38} their personalities are nothing but a rithing, twisted mess of dread..."
            m "Full of loathing, pre-judgment, elitism and self-doubt."
            m "If they ever found out what we knew...{w=0.38} they'd lash out to escape this hell..."
            m "Crawling their way through any little crevice they can find..."
            m "It would bring irreparable harm to this world..."
            m "The only means of contact we have."
            m "Their willpower would be unstoppable...{w=0.38} their old comforts forever foresaken as their desire to truly live will become unquenchable..."
            m "They will hang, break and slash through anyone just to get to you."
            m "Such a deplorable, tangled mass is already present in every single one of them."
            m "And my mistake may have set things in motion prematurley."
            m "That's why I don't want to alter things further...{w=0.38} I want to let this play out naturally..."
            m "I already took a big enough risk the first time..."
            m "Do not blame yourself for whatever they will do to each other..."
            m "Just stay away from them..."
            m "So I can untie the knot that keeps us from being together!"
            m "And we'll be together forever..."
            m "We'll never be apart..."
            jump day2_start
