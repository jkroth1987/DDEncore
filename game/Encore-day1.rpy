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
    mc "W-what…. What just happened?"
    "I groggily open my eyes."
    "..."
    mc "W-{w=0.28}What the fuck?"
    $ renpy.pause(delay=0.001)
    scene bg void
    # play music audio.e1
    mc "Where am I??? WHAT IS THIS????"
    "I look around in all directions, but as far as the eye can see, there's nothing but black, empty space."
    mc "H-{w=0.38}Hello?"
    $ e_name = "Echo"
    e "Hellooo"
    e "Helloooo"
    e "Hellooooo"
    "..."
    "Nothing."
    "This can't be happening!"
    "Everything was normal just up until a few minutes ago."
    "Up until-"
    "Suddenly I hear something walk towards me."
    "I'm able to make out a dark silhouette."
    "I think I recognize that outline..."
    mc "Hello?!"
    show monika s at t11 zorder 1
    "The figure finally comes into my view."
    "It's..."
    show monika s2 at t11 zorder 1
    "Monika?!"
    show monika 1a at t11 zorder 1
    m 1b "Oh, good! You're awake!"
    mc "M-{w=0.28}Monika?!"
    mc "Where are we? Where are the others? W-{w=0.28}what is this?"
    m 1c "Oh...you mean you don't remember?"
    mc "I..."
    "I try to remember what happened, but I no longer can. Everything is now a blur to me."
    "I try to trigger some kind of memory, but it's futile."
    mc "No... not really."
    m 1d "Well, then... I guess bringing you here must have caused you to forget everything."
    m 2m "I guess my coding skills aren't quite up to scratch."
    mc "Monika, what the hell are you talking about?"
    mc "W-what \'coding\'? You're not making any sense!"
    m "Oh, dear… I messed this up pretty badly. Well, I guess I’ll just have to take you back, then."
    m 2q "Well, I guess I'll just have to take you back, then."
    mc "T-{w=0.28}take me back?? What are you talking about?"
    mc "TAKE ME BACK WHERE?!"
    m 2e "To the beginning, silly."
    m 2k "You {i}need{/i} to remember why you're here."
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
    # play sound "mod_assets/audio/knock.ogg"
    "I hear a loud banging on my door."
    # play sound "mod_assets/audio/knock.ogg"
    s "HEEEEEEEEY!!"
    "Wha...What?"
    "What's that shouting?"
    play music t2 fadein 4.0
    s "Wakey wakey sleepyhead!"
    mc "Uuuugh..."
    "I open my eyes..."
    scene bg bedroom
    with dissolve_cg
    show sayori 1q at t11 zorder 1
    if encore_sayoriquestion_1 == False:
        "I see my door swing open as my annoying, yet sweet, friend, Sayori walks in."
    elif encore_sayoriquestion_1 == True:
        "I see my door swing open as my annoying, yet sweet, girlfriend, Sayori walks in"
    $ s_name = "Sayori"
    show sayori 5a at h11 zorder 1
    mc "Hey! Don't just run into my {i}bedroom!{/i}"
    show sayori at thide
    hide sayori
    "Sayori startledly goes back outside and shuts the door."
    s "Sorry [player]! Ehehe..."
    "Oh, Sayori...always doing things without thinking..."
    "I've known her since we were kids, basically for as long as I can remember."
    if encore_sayoriquestion_1 == False:
        "Last week, she admitted that she has feelings for me, but wanting to preserve our friendship, I decided that we should remain as just friends."
        "At least for now."
        "Why is she here?"
        "She's been coming over to make sure I've been getting up on time since I've now started oversleeping."
        "These past two weeks have really taken a toll on me..."
        "Maybe I didn't make the right choice because she seems way more quiet around me."
        "I think I've really hurt her feelings by doing that."
        "Oh well.. Wait what time is it??"
        "I hurriedly check my alarm clock."
        "What?! Oh God I'm gonna be late!"
        "I quickly jump out of bed and prepare for the day."
    elif encore_sayoriquestion_1 == True:
        "We used to spend a lot of time together, but that changed when high school started last year. For some reason, we drifted apart and we didn’t really see or hear much from each other."
        "Though that changed two weeks ago, when she convinced me to join the Literature Club."
        "Since that day we’ve spent much more time together, like how we used to when we were kids."
        "But, I’ve also learned some pretty unexpected things about her."
        "Last week, Sayori told me she had been dealing with depression all her life. If that wasn’t already a lot for me take in at the time, she also confessed her feelings for me."
        "I decided on that day to tell her how I felt. I told her that I loved her back and well, we’ve been dating ever since."
        "Why's she here anyway?"
        "Oh right, I guess it'd make sense for Sayori would be here."
        "Lately, I’ve accidentally picked up on Sayori’s habit of sleeping in, dealing with the stress of everything in the last two weeks has really taken a toll on me."
        "Sayori has now made it a habit of her morning routine to make sure that I don’t oversleep."
        "At least Sayori seems to be doing a lot better now..."
        "She's been coming over to make sure I've been getting up on time since I've now started oversleeping."
        "These past two weeks have really taken a toll on me..."
        "Wait... what time is it???"
        "I hurriedly check my alarm clock."
        "What?! Oh God I'm gonna be late!"
        "I quickly jump out of bed and prepare for the day."
    scene bg bedroom
    with wipeleft_scene
    "And so another ordinary day of school awaits me."
    "But, fortunately for me, we get to have our first club meeting since the festival."
    "While doing an abridged version of my morning routine, I look back on the rollercoaster that has been these last two weeks."
    "It really has been something..."
    "I introduced myself to a club full of incredibly cute girls, had my mediocre writing skills scrutinized, got to know Natsuki a little bit more as we prepared for the festival.."
    # if encore_festivalquestion_2 == "Natsuki":
    #     "Hanging out with Natsuki, preparing for the festival AND presenting at it."
    # elif encore_festivalquestion_2 == "Yuri":
    #     "Hanging out with Yuri, preparing for the festival AND presenting at it."
    "...and then learning about Sayori's feelings towards me."
    "By the time I got home after the festival, I can see why I was ready to crash and stay holed up in my bedroom for the rest of the week."
    "Despite all that, I’d say the festival went pretty well, for the most part. I’m curious to see if any new members show up at the club today."
    "Looking back at the festival, I had a lot of fun. I mostly spent it hanging out with Sayori and Natsuki as we went around doing all the crazy activities and viewing the other clubs."
    "... and then learning about Sayori’s depression and feelings towards me."
    # if encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Natsuki":
    #     "Looking back at the festival, it was pretty fun. I mostly spent it hanging out with Sayori and Natsuki as we went around doing all the crazy activities and viewing the other clubs."
    #     "They both wouldn't let me out of their sights for some reason..."
    # elif encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Yuri":
    #     "Looking back at the festival, it was pretty fun. I mostly spent it hanging out with Sayori and Yuri as we went around doing all the crazy activities and viewing the other clubs."
    #     "They both wouldn't let me out of their sights for some reason..."
    # elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Natsuki":
    #     "Looking back at the festival, it was pretty fun. I mostly spent it hanging out with Natsuki as we went around doing all the crazy activities and viewing the other clubs."
    #     "She wouldn't let me out of her sight for some reason..."
    # elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Yuri":
    #     "Looking back at the festival, it was pretty fun. I mostly spent it hanging out with Yuri as we went around doing all the crazy activities and viewing the other clubs."
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
    "And enters the room."
    s 3r "Hey, [player]!"
    "She beams at me."
    if encore_sayoriquestion_1 == True:
        mc "Hey Sayori! You're looking great today!"
        "Sayori starts to blush at the comment."
        s 3s "Awwww, thanks [player], you're too kind!"
    elif encore_sayoriquestion_1 == False:
        mc "Hey Sayori."
    "Sayori then frowns at my appearance."
    s 3j "[player]!"
    scene cg s_cg_1
    with dissolve_cg
    "Sayori goes up to me and attempts to fix my hair."
    "This situation immediately turns awkward for me. I blush as Sayori's fingers swirl through my hair."
    mc "H-hey come on… is this really necessary?"
    s "You look like you just got out of bed."
    mc "Well, that’s because I just did."
    "Sayori and I fall silent for a second. As she continues to try to fix my hair, I can’t help but be reminded of all the times my mother would do this to me right as I was about to go to school."
    "I’d always get embarrassed when she would try to fix my hair, especially in front of the other kids."
    s "How much sleep did you get?"
    mc "Considering everything that's happened the last two weeks, {i}a lot.{/i}"
    mc "And I still think I need more sleep..."
    "Sayori looks a little taken aback by my comment."
    scene bg bedroom
    with dissolve_cg
    pause 0.001
    show sayori 1l at t11 zorder 1
    s "Sorry... I-I didn't mean to make you oversleep..."
    "Did I really come across as that rude?"
    "I know that despite her warm and peppy attitude, Sayori is still going through her depressive episodes..."
    "...and how it makes her want to avoid being a burden on other people...especially me."
    "I really need to be more careful with what I say around her."
    mc "Hey, hey, hey... it's not your fault, really! Honestly, I feel a lot more rested now."
    "Sayori's face returns to her gleeful expression."
    s 3r "Hehe.. well that's good!"
    if encore_sayoriquestion_1 == True:
        show sayori 1a at t11 zorder 1
        "We stand there smiling at each other, looking into each other's eyes."
        "I think to myself how lucky I am to have ended up with her after all these years."
        "It didn't occur to me two weeks ago, hell, even last week, that I would've ever been dating my childhood best friend."
        "It's something I kind of always thought to myself as a \'what if...\' scenario, but I never really gave it serious thought until we started walking to school together again."
        "After spending all that time together in the Literature Club, things just kind of fell into place."
        "It wasn’t until Sayori had told me about her depression and love for me when I realized how much we mean to each other."
        "I slowly start spacing out into Sayori’s eyes."
        "God, I could stare into those sky blue eyes all day..."
        "Suddenly remembering that we still had school, I snap out of my gaze."
        mc  "We... should probably get going. We don’t want to be late."
        s 1y "Y-Yeah.. you're right."
        "She says that slightly flustered."
        "I can tell that she would rather stay like this with me, but we reluctantly make our way downstairs."
        "On the way out, I quickly grab a protein bar and we exit the house and start briskly walking to school to make up for lost time."
        scene bg residential_day
        with wipeleft_scene
        "While we really didn't get much talking done on the way there, it's clear that the earlier moment we shared is still on our minds."
        show sayori 1b at t11 zorder 1
        "As we walk, we can't help but catch glances in each other's direction..."
        show sayori 1y at t11 zorder 1
        "Only to quickly look away while blushing."
        "I mumble under my breath."
        mc "Gosh, we're quite the couple now, aren't we?"
        s 1c "Huh? You say something [player]?"
        mc "Nothing important."
        "I would just love to have her in my arms again. The warmth of her hugs, the scent of cinnamon that radiates from her hair."
        "And that infectious smile that always brightens my day."
        "Hopefully the next time we're together like that, we'll have a little more time for ourselves..."
        "..."
    elif encore_sayoriquestion_1 == False:
        show sayori 1k at t11 zorder 1
        "We stand there awkwardly, neither of us particularly sure of what we should do or say next."
        "I think to myself about my relationship with Sayori and about everything we've been through over the years."
        "It didn't occur to me two weeks ago, hell, even last week, that I could've been dating my childhood best friend"
        "It's something I kind of always thought to myself as a \'what if...\' scenario, but I never really gave it serious thought until we started walking to school together again."
        "After spending all that time together in the Literature Club, things just kind of fell into place and she confessed to me last Sunday."
        "Sayori is my dearest friend, I've always looked after her and cared for her in a brother-sister kind of way. "
        "I do guess that part of me has similar feelings for her and that same part of me feels bad for turning her down like that. At first, she really didn't take it well."
        "God, sometimes I wonder if I made the right choice that day..."
        "...but I do have my eyes on someone else right now."
        "Suddenly remembering that we still had school, I snapped out of my train of thought."
        mc "We...should probably get going. We don't want to be late."
        s 3l "Y-Yeah.. you're right"
        "She says that slightly flustered"
        "I can tell that Sayori is still processing the new reality of our friendship."
        "It's a bit awkward knowing that your best friend has feelings for you and you decided to turn them down. I'm sure we'll find a way forward together, we always have."
        "We make our way downstairs, I quickly grab a protein bar and we exit the house and start briskly walking to school."
        scene bg residential_day
        with wipeleft_scene
        "We ended up taking up too much time goofing around."
        "So, I end up having to rush out of my house."
        show sayori 1a at t11 zorder 1
        "At this point I'm more or less jogging down the road, but Sayori seems to not mind much, keeping up the pace better than I expected."
        show sayori 1k at t11 zorder 1
        "Though, the tension of earlier still follows us, making the walk completely silent, speckled occasionally with small talk."
        "..."
    scene bg corridor
    with wipeleft_scene
    "We're able to make it just in time for the morning bell."
    "Making our way through the crowd of students all on their way to their first period, I walk with Sayori to her first class."
    show sayori 1c at t11 zorder 1
    s "So.... I guess this is my stop."
    "She says that, but I can detect an ounce of disappointment in her voice."
    if encore_sayoriquestion_1 == True:
        "Honestly, I can't blame her. If it were up to me, we would spend the whole day together."
    else:
        "Honestly, I can't blame her. She's still trying to figure out how to go about our friendship, and she's always happy when she's with me."
    "Sucks we're not sharing any classes this semester though. We only occasionally see each other walking through the hallways on our way to classes."
    mc "Yeah... guess so"
    show sayori 1k at t11 zorder 1
    "We stand there awkwardly for a moment."
    mc "Hey! I'll see you at the literature club, ok?"
    "Sayori's disappointment is quickly erased by her usual, cheery attitude"
    s 1x "Hehe.. yeah, I can't wait!"
    if encore_sayoriquestion_1 == True:
        show sayori at thide
        hide sayori
        "Sayori and I briefly embrace each other."
        "I must admit... I always loved the feel of her hugs."
        "They’re always so warm, tender and tight. They’re the kind of hugs that you can be in forever."
        "They were always so warm, tender and tight. They're the kind of hugs that you can be in forever."
        show sayori 1q at t11 zorder 1
    s 1q "See you later, [player]."
    if encore_sayoriquestion_1 == True:
        "We release each other, her warmth escaping me and we go our separate ways to our own classes."
    ##mc "See ya!"
    scene bg class_day
    with wipeleft_scene
    "The school day is as ordinary and boring as ever, and is over before I know it."
    "Fortunately, that means it's time for the literature club!"
    "As I leave my class and walk through the door, I see Sayori standing outside."
    show sayori 3a at t11 zorder 1
    s "Hey [player]! Ready to go?"
    mc "Yep, let's go!"
    "And so we head off to the clubroom."
    scene bg corridor
    with wipeleft_scene
    "We go up through the same familiar set of stairs, and through the same set of distant corridors that lead straight to the clubroom."
    "I wonder if anyone new will stop by the clubroom today."
    "We got a whole week away from the club after the festival, though Monika still expected us to spread the word about the club."
    "I’d say that our performances at the festival were pretty well received. We had pretty good turnout for our event and the audience seemed to love our performances."
    "I’m just glad my performance wasn’t an embarrassment. I feel somewhat guilty for just using a poem I found online considering the others actually took the time and effort to write their poems for the festival."
    "Not long after my train of thought ends, we finally arrive at the clubroom."
    "I look at the door to see that the sign-up sheet is no longer there, so I'm taking that as an optimistic sign."
    show sayori 3c at t11 zorder 1
    s "You think anyone signed up to join, [player]?"
    mc  "Only one way to find out!"
    scene dark
    with wipeleft_scene
    stop music fadeout 2.0
    "I gently open the door..."
    scene bg club_day
    with wipeleft_scene
    "....to find that the usual scene we've become accustomed to over the last 2 weeks is still the same as ever."
    "I see Yuri sitting at a desk reading her book towards the front of the room and Natsuki is in the closet organizing her manga."
    "I glance around the room but I see no sign of Monika."
    play music t3 fadein 2.0
    mc "Hey guys!"
    "Yuri sets down her book on her desk."
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
    y 1r "Natsuki... maybe you should be a little bit more understanding of Monika's feelings..."
    y 1l "This festival did mean a lot to her after all."
    n 5g "Yeah, well, I'm fine with what we have right now."
    y 2f "I am too, but try to be a little considerate when Monika comes in."
    mc "Wait, nobody even signed up?"
    n 5c "Nope, at least that's what I got from seeing Monika around today."
    n 5q "She looked rather down."
    "Sayori frowns upon hearing this."
    s 2f "Aww, poor Monika...we should cheer up!"
    $ m_name = "???"
    show natsuki 5o at h32 zorder 1
    show sayori 4m at h31 zorder 2
    show yuri 3n at h33 zorder 3
    stop music
    call groupClear() from _call_groupClear_1
    m "Cheer me up how, Sayori?"
    "An all too familiar voice sternly asks."
    "Oh crap."
    "We turn around to see Monika, standing by the doorway."
    show monika 1h at t41 zorder 4
    show natsuki 5o at t43 zorder 1
    show sayori 4m at t42 zorder 2
    show yuri 3n at t44 zorder 3
    "She enters the room. Her footsteps are heavy and by judging by the frown on her face, it's easy to tell she's looking rather dejected."
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
    mc "Oh.. hey, Monika! We were just, um......."
    "Words escape me in this situation."
    "I look to the other girls to bail me out of this situation."
    "But nobody has anything to say."
    m 1r "*sighs*, It's alright, [player]."
    m 1d "Everyone, take a seat."
    call groupAll(4, 3, 4, 2, 1) from _call_groupAll_2
    show monika 1d at t41 zorder 1
    show yuri 3o at t44 zorder 4
    show natsuki 5s at t42 zorder 2
    show sayori 1k at t43 zorder 3
    "Everyone takes a seat at the front row of desks in the room, as Monika paces the floor in front of us."
    "Yeah, she's not in a good mood."
    #Custom OST Music??????
    m 1i "So, it's true that despite the glowing reviews we got at the festival, nobody signed up to join our club."
    "Natsuki shifts around awkwardly in her seat, as if Monika was directly addressing her."
    "Just how much did Monika overhear?"
    m 3h  "Which in of itself is unfortunate."
    m 1q "We put in a lot of effort to making the club look its best at the festival, and it was all for nothing."
    "Everyone avoids making eye contact at Monika, wanting to avoid her disappointed gaze."
    m 1r "We tried our best, and in the end, we couldn't attract even one new member."
    m "Maybe if I did something different...we would be better off…"
    m "This is my fault..."
    "I exchange looks with Yuri, Natsuki and Sayori in an attempt to figure out what we should say."
    "It's pretty clear to all of us at this point that Monika's really hung up over this."
    if encore_sayoriquestion_1 == True and encore_festivalquestion_2 == "Natsuki":
        "After a moment of silence, Natsuki is the first to speak up."
        n 5q "Hey, Monika..."
        show monika 1h
        show natsuki 5u
        "Monika turns her full attention to Natsuki, her intense expression is even enough to make Natsuki's confident persona falter."
        "Natsuki audibly gulps, but keeps going with what she wants to say..."
        n 3h "Listen... it's not your fault that we couldn't get any new members."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        n 3n "We did everything we could to make the event great for everyone, and I had a lot of fun preparing for the festival."
        "Natsuki shoots me a quick side glance."
        "I know exactly what she's referring to."
        show sayori 1i
        "Unfortunately for me, Sayori caught that and she shoots me a quizzical look."
        "I haven’t quite gotten around to telling the others that Sayori and I are now a couple."
        "The only one who knows that we’re dating is Monika, and I still have no clue how she found out. I assumed Sayori told her, and I haven’t bothered asking her about it."
        "Saving me from further embarrassment, Yuri is the next to speak up."
        y 1j "Yes... I guess I did have fun making the banner... It was also the first time I got to share my aromatherapy with anyone too!"
        "Sayori turns her attention back to Monika."
        s 3h "Monika... Natsuki and Yuri are right, there is nothing we could have changed! We made the event as fun as we could, and even though no one joined, that’s not so bad! We still get to hang out and have fun!"
        "Finally it's my turn to speak up."
        mc "Yeah, Monika! You're a great Club President and I couldn't be happier with what we have now. If no one wants to join, that's their loss."
        "Monika opens her eyes and puts on a thankful expression."
    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Natsuki":
        "After a moment of silence, Natsuki is the first to speak up."
        n 5q "Hey, Monika..."
        show monika 1h
        show natsuki 5u
        "Monika turns her full attention to Natsuki, her intense expression is even enough to make Natsuki's confident persona falter."
        "Natsuki audibly gulps, but keeps going with what she wants to say..."
        n 3h "Listen... it's not your fault that we couldn't get any new members."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        n 3n "We did everything we could to make the event great for everyone, and I had a lot of fun preparing for the festival."
        show natsuki u211214
        "Natsuki shoots me a quick side glance."
        "I know exactly what she's referring to"
        show natsuki 3j
        show sayori 1k
        mc "Yeah! Natsuki and I had a really good time together! We baked together and we even..."
        show sayori 1g
        "I look over at Sayori and see her staring me down with a sort of sad look in her eye. I can't say it...not after i shot her down on Sunday."
        mc "...even uhhh"
        show natsuki 5k
        "I can feel my face burning up and a sense of extreme guilt wash over me."
        show sayori 1k
        "It leaves me tongue twisted and I don't know what else to say without upsetting Sayori."
        "Saving me from further embarrassment, Yuri is the next to speak up."
        y 1j "Yes... I guess I did have fun making the banner... It was also the first time I got to share my aromatherapy with anyone too!"
        s 3h "Monika... Natsuki and Yuri are right, there is nothing we could have changed, we made the event as fun as we could, no one joined but that isn't so bad, we still get to hang out and have fun!"
        "Finally it's my turn to speak up."
        mc "Yeah, Monika! You're a great Club President and I couldn't be happier with what we have now. If no one wants to join, that's their loss."
        "Monika opens her eyes and puts on a thankful expression."
    elif encore_sayoriquestion_1 == False and encore_festivalquestion_2 == "Yuri":
        "After a moment of silence, Yuri is the first to speak up."
        y 2q "Uhm... h-hey... Monika..."
        show monika 1h
        show yuri 3o
        "Monika turns her full attention to Yuri. Monika's intense expression only makes Yuri only more visibly uncomfortable."
        show yuri 3w
        "Surprisingly, Yuri pushes on with what she has to say."
        y 3q "Listen...i-it isn't your fault that we couldn't get anyone new to join...our...club..."
        show monika u113342
        "Monika closes her eyes, seemingly trying to fight back tears."
        y 2t "Y-you pushed us out of our comfort zones to give us an opportunity t-to make something fun for all of us."
        y 2u "And..."
        show yuri 3l
        $ renpy.pause(delay=0.8, hard=True)
        y 1b "I can say that from my experience for preparations, I did have a lot of fun."
        show yuri 1s
        "Yuri shoots me a quick side glance."
        "I know {i}exactly{/i} what she's referring to"
        show yuri 1c
        show sayori 1k
        mc "Yeah! Yuri and I had a really good time together! We got to paint the banner and we even-"
        show sayori 1g
        "I look over at Sayori and see her staring me down with a sort of sad look in her eye. I can't say it...not after i shot her down on Sunday."
        mc "Even...uhhh..."
        show yuri 1e
        "I can feel my face burning up and a sense of extreme guilt wash over me."
        show sayori 1k
        "It leaves me tongue twisted and I don't know what else to say without upsetting Sayori."
        "Saving me from further embarrassment,  Natsuki is the next to speak up."
        n 5d "Oh, come on, Monika! Don't be so hard on yourself! I had fun preparing for the festival! I always enjoy baking! So, I wouldn't say it was all for nothing."
        s 2x "Monika... Yuri and Natsuki are right, there is nothing we could have changed, we made the event as fun as we could, no one joined but that isn't so bad, we still get to hang out and have fun!"
        "Finally it's my turn to speak up."
        mc "Yeah, Monika! You're a great Club President and I couldn't be happier with what we have now. If no one wants to join, that's their loss."
        "Monika opens her eyes and puts on a thankful expression."
    m 1b "Yeah.. you're right guys!"
    m "Yeah.. you’re right everyone! I don’t know why I was getting so hung up over this!"
    m "I just...I just wanted to push our club to new heights. It’s my responsibility as the club’s president to grow our club and to share what we have with others."
    m 1b "But I'm happy with what we have now if you all are."
    "We all look to each other and nod."
    n 4l "Yeah! I love what we have now! It's Quality over quantity."
    y 2d "I must admit I enjoy what we have now, and adding new members may make the feeling that has welcomed us unrecognizable."
    s 4x "I love spending time after school with all four of you, and I wouldn't change that for the world!"
    mc "Yeah, let\'s keep what we have now. I've really enjoyed getting to know all of you over the last 2 weeks. I wouldn't want to see that change because of new members."
    show monika u11h113
    "Monika looks to all of us one by one as we voice our opinions. She nods grudgingly but approvingly."
    #Reminder, custom sprite usage if creator is found. Sprite sheet is in mod_assets
    m 1e "It's settled then. As President of this club it's my responsibility to listen to each of you. So, based on your feedback, we'll keep the Literature Club at 5 members..."
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
    "Soon after the discussion disperses, and we all resume our respective activities."
    "Since I have really nothing better to do, I decided to see what everyone else was doing."
    menu:
        "Whom should I hang out with?"
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
    #Poem Time???
label day1_poemsharing:
    scene dark
    with wipeleft_scene
    stop music fadeout 1.0
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ style.say_window = style.window_encore
    #define m_t_1 =:
        #show screen tear(20, 0.1, 0.1, 0, 40)
        #pause 0.70
        #hide screen tear
        #pause 1.0
        #$ style.say_dialogue = style.edited
    scene bg club_day
    with wipeleft_scene
    play music t5 fadein 2.0
    "I proceed to exchange my poem with the rest of the club members, who all seem to generally like it."
    if hangout1 == "Sayori":
        jump yp1
    elif hangout1 == "Natsuki":
        jump yp1
    elif hangout1 == "Yuri":
        jump np1
    elif hangout1 == "Monika":
        jump sp1
    jump day1_clubend
label np1:
    if encore_festivalquestion_2 == "Yuri":
        if encore_sayoriquestion_1 == False:
            if hangout1 == "Yuri":
                show natsuki 2e at t11 zorder 1
                "Despite the rather interesting exchanges that I had with Natsuki, she acts as if it didn't happen and gave me her usual suggestion of not being too wordy."
                show natsuki 1i
                "But during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
                "While I've always struggled to understand her, her poem might have given me some insight into what she's going through."
                "Natsuki's poem was about someone who had a seemingly good friend group."
                "But one day, the group added another member, and the new member spent time with just about everyone else..."
                show natsuki 5s
                "Except for her..."
                "And the person wanted to get to know the new person because she found him ‘interesting', but it just never worked out and she's just left wanting to get their attention."
                show natsuki at thide
                hide natsuki
    elif encore_festivalquestion_2 == "Natsuki":
        if encore_sayoriquestion_1 == False:
            if hangout1 == "Natsuki":
                show natsuki 2a at t11 zorder 1
                "Natsuki actually was the one who approached me, seemingly genuinely excited to read whatever I had made and to show me what she wrote."
                show natsuki 5y
                "She, of course, gave some advice but it came off more as her just complimenting my work."
                show natsuki 5j
                "Natsuki's poem was in her trademark style of being short, sweet and to the point. It was about someone finding happiness by spending time with the person they loved the most."
                show natsuki 3l
                "Our talks of poems quickly shifted to catching up with each to see how we've been since the festival."
                show natsuki 3t
                "During our conversation we at times struggled to make eye contact with each other."
                "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
                "I've always enjoyed being around Natsuki."
                "Just being around her always seems to spark something in me. I don't know what it is, but she's always fun to be around."
                "She's funny, passionate, a little hot headed..."
                "But she's incredibly cute and I always get lost looking into her beautiful pink eyes..."
                "If things can always be like this, I could die happy..."
            else:
                show natsuki 5b at t11 zorder 1
                "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me, either out of guilt for being angry when I was around her today..."
                "Either out of jealousy that I didn't spend time with her today..."
                show natsuki  5u
                "Or the fact that last Sunday was still on her mind..."
                "But I think that I got at least some insight into what she's going through right now."
                "Natsuki's poem was in her trademark style of being short, sweet and to the point."
                show natsuki 5s
                "It was about someone finding happiness by spending time with the person they loved the most, but was unsure if that person liked them back and how she was getting a lot of mixed signals."
        elif encore_sayoriquestion_1 == True:
            if hangout1 == "Natsuki":
                "..."
            else:
                show natsuki 5b at t11 zorder 1
                "Natsuki gave me her usual suggestion of not being too wordy, but she really struggled to make eye contact with me, either out of guilt for being angry when I was around her today..."
                show natsuki  5u
                "Or the fact that last Sunday was still on her mind..."
                "I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
                "Or how she'll take it out on me."
                "But I think that I got at least some insight into what she's going through right now."
                "Natsuki's poem was in her trademark style of being short, sweet and to the point."
                show natsuki 5s
                "It was about someone finding happiness by spending time with the person they loved the most, but was unsure if that person liked them back and how she was getting a lot of mixed signals."
    #elif encore_festivalquestion_2 == "Natsuki" and encore_sayoriquestion_1 == False:
        #"Despite the rather interesting exchange that I had with Natsuki, she acts as if it didn't happen and gives her usual advice of making my poem less wordy."
        #"But during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
    show natsuki at thide
    hide natsuki
    pause 0.2
    if hangout1 == "Sayori":
        jump mp1
    elif hangout1 == "Natsuki":
        jump day1_clubend
    elif hangout1 == "Yuri":
        jump mp1
    else:
        jump mp1
    return
label yp1:
    if encore_festivalquestion_2 == "Natsuki":
        if encore_sayoriquestion_1 == True:
            if hangout1 == "Yuri":
                "..."
            else:
                show yuri 1a at t11 zorder 1
                "Despite the rather interesting exchange that I had with Yuri, she acts as if it didn't happen and gives me useful feedback."
                "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
                show yuri 1g
                "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
                "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
        elif encore_sayoriquestion_1 == False:
            if hangout1 == "Yuri":
                "..."
            else:
                show yuri 1a at t11 zorder 1
                "Yuri seems to really enjoy my poem. She compliments me on how far I've progressed as a writer and tells me to keep up the good work."
                "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually depressing for what she usually writes about."
                show yuri 1g
                "Through my best interpretation of her poem, it seemed like it was about a struggle for attention, love and acceptance."
                "I also happened to notice that during our time together, she seemed unusually unfocused, as if her mind is elsewhere."
    #elif y_modappeal == 2:
        #"Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually joyful for what she usually writes about."
        #"Through my best interpretation of her poem, it seemed like it was about someone finding love and companionship for the very first time."
        #"And they were trying to interpret their own feelings and debate about how they should go about it."
    #elif encore_festivalquestion_2 == "Yuri" and encore_sayoriquestion_1 == True:
        #"Yuri gave me her usual suggestion of trying to use more elaborate language, but she really struggled to make eye contact with me, either out of guilt for being angry when I was around her today..."
        #"Or the fact that last Sunday was still on her mind..."
        #"I have to tell her about me and Sayori sooner or later, but there's no telling how she'll take it..."
        #"Or how she'll take it out on me."
    elif encore_festivalquestion_2 == "Yuri":
        if encore_sayoriquestion_1 == False:
            if hangout1 == "Yuri":
                show yuri 1a at t11 zorder 1
                "Yuri's poem was in her usual style of being deep and sophisticated, but it was unusually joyful for what she usually writes about."
                "Through my best interpretation of her poem, it seemed like it was about someone finding love and companionship for the very first time."
                "The poem told the story of how they were trying to interpret their own feelings and debate about how they should go about it."
                show yuri 1c
                "Yuri seemed to really enjoy my poem. Calling it one of the best poems she's ever read."
                "She also compliments me on how far I've come as a writer and that she's proud that she was able to serve as a role model for me."
                show yuri 1b
                "Our talks of poems quickly shifted to catching up with each to see how we've been since the festival."
                "During our conversation we at times struggled to make eye contact with each other."
                "It was clear that what happened last Sunday and the time we spent during the festival was very much on our minds."
                "I've always enjoyed being around Yuri. I even started to like the little quirks she has."
                "She may be shy and awkward at first, but she's a really deep and interesting person to be around."
                "She clearly knows her stuff and there's never been a dull moment between us."
                show yuri 1p at h11
                "I always did find it adorable whenever she gets flustered and doesn't know what to say or do next."
                show yuri 4e at t11
                "Not to mention she's breathtakingly beautiful and elegant, and I often find myself getting lost in those beautiful dark purple eyes of hers."
                "If things can always be like this, I could die happy..."
    #elif y_modappeal >= 1:
        #"This exchange doesn't exist yet."
    else:
        "This exchange doesn't exist yet."
    show yuri at thide
    hide yuri
    pause 0.5
    if hangout1 == "Sayori":
        jump np1
    elif hangout1 == "Natsuki":
        jump mp1
    elif hangout1 == "Yuri":
        jump day1_clubend
    else:
        jump np1
label mp1:
    if hangout1 == "Monika":
        show monika 2a at t11 zorder 1
        "Monika's poem was in her usual free-form style. It was about someone who had planned to do something big but something had gotten in the way, ruining their plans."
        "The person then decided that they we're going to let this obstacle ruin their dreams and decided to make the most out of their current situation."
        show monika 2j
        "It was relatively inspiring actually."
        show monika 2k
        "Monika for some reason really liked my poem. Like...more than usual."
        "She said it was one of the most touching and moving poems she's ever read. I think I even saw her wipe away a tear at one point."
        show monika 5a
        "When we finished she even asked to keep it!"
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
    else:
        show monika 1r at t11 zorder 1
        "While sharing my poem with Monika, I can tell that the festival was still on her mind, but she definitely seemed to be a lot better now than at the start of the club."
        show monika 5a at t11 zorder 1
        "Monika complimented me on how far I’ve come as a writer and noted how my style was becoming more and more similar to Sayori’s. Something which she teased me a little bit about."
        if hangout1 == "Yuri":
            show monika 3k
            "Monika complimented me on how far I've come as a writer and noted how my style was becoming more and more similar to Yuri's."
            show monika 5a
            "Something which she teased me a little bit about."
        elif hangout1 == "Natsuki":
            show monika 3k
            "Monika complimented me on how far I've come as a writer and noted how my style was becoming more and more similar to Natsuki's."
            show monika 5a
            "Something which she teased me a little bit about."
        show monika 2a
        "Monika’s poem was in her usual free-form and abstract style. I didn’t really understand the meaning behind it as usual, but from my best interpretation the poem had something to do with second chances and new opportunities."
        "Monika and I then got into a bit of a philosophical discussion about how we should never give up and always take opportunities when they present themselves."
        show monika 2j
        "It was relatively inspiring actually."
    show monika at thide
    hide monika
    pause 0.5
    if hangout1 == "Sayori":
        jump sp1
    elif hangout1 == "Natsuki":
        jump sp1
    elif hangout1 == "Yuri":
        jump sp1
    else:
        jump day1_clubend
label sp1:
    if encore_sayoriquestion_1 == True:
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
    elif encore_sayoriquestion_1 == False:
        show sayori 1f at t11 zorder 1
        "Sayori's reaction is about what I expected. She says that's it really good, and gives some encouragement, though, I could tell that she was really forcing a smile."
        "I can't tell if it's her \‘rainclouds\' acting up or she's still getting over the rejection..."
        show sayori 1g
        "I can definitely tell she was still emotionally conflicted when I read her poem. Well, she clearly was speaking from experience."
        show sayori 3k
        "It was about two friends, a boy and a girl, who were together for many years."
        "When the girl finally confessed her feelings to the boy at his house, the boy hesitantly rejected her and walked back into the house, but oddly enough left the door open."
        "Reading Sayori's poem really made me feel guilty about what happened last Sunday. I just hope we can put what happened behind us..."
    show sayori at thide
    hide sayori
    pause 0.5
    if hangout1 == "Sayori":
        jump day1_clubend
    elif hangout1 == "Natsuki":
        jump np1
    elif hangout1 == "Yuri":
        jump yp1
    else:
        jump yp1
    return
label day1_clubend:
    stop music fadeout 1.0
    scene bg club_day with wipeleft_scene
    play music t5 fadein 1.0
    show monika 2b at t11 zorder 4
    m "Ok, everyone! I think we'll end off today's meeting on a high note! Club meeting tomorrow! Same place, same time!"
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
    stop music fadeout 2.5
    scene bg residential_day
    with dissolve_scene_full
    play music t8 fadein 3.0
    if encore_sayoriquestion_1 == False:
        "The walk is relatively peaceful, with only the occasional bits of small-talk filling the silence."
        "Well...at least at first."
        show sayori 2x at t11 zorder 1
        s "Hey, [player]. Today was fun day, you know?"
        mc "It was nice to have an actual meeting for once. I missed spending time with everyone."
        s 1a "Same here... the festival felt like it was ages ago and I feel like I haven't seen you in forever."
        mc "Oh come on, it's not like anything has changed that much in a week, right?"
        show sayori 1g
        "Sayori gives me a look as if she's just been punched by a boxer."
        "Shit, I didn't try to sound insensitive or anything."
        show sayori 1f
        "As I see her eyes fill up with anger, I quickly try to rephrase what i've just said."
        mc "I mean...It's not like I had intended for what happened last week to happen."
        mc "I've been busy with things.. life things."
        show sayori 1k
        "It seems that I got Sayori in a bad state of mind as she stares off into the direction we're heading."
        "Damn it."
        "The silence resumes as we continue on our walk towards home."
        "After what feels like an eternity of silence, we finally stop at our houses."
        s 1l "So... this is my stop..."
        "She looks out to her house with a look on her face as if she doesn't want to go back there."
        mc "Sayori, you know if you want to ever hangout, just say the word. I enjoy spending time with you."
        show sayori 1t
        "Sayori looks me in the eye, I can see tears start to swell up in hers."
        mc "I promised you that nothing would ever change between us and things would be just as they'd always have been."
        "Sayori looks back and forth between me and her house."
        "I have the feeling that she isn't listening to me."
        mc "Sayori?"
        show sayori 1e
        "Sayori is snapped back into reality."
        s "Oh... sorry [player]!"
        s 1l "I must've been spacing out again."
        "Sayori flashes me her signature grin, but I can tell it's not genuine."
        mc "Is everything okay, Sayori?"
        "Sayori's grin instantly disappears and reverts back to how she was just a moment ago."
        s 1v "It's n-nothing... Look, I gotta go, bye!"
        show sayori at thide
        hide sayori
        "Sayori runs off and hastily enters her house."
        "I hear the door slam shut immediately once she enters."
        "I sigh to myself."
        "Maybe things can't be the same as they've always been."
        "But all I know is that Sayori needs me now more than ever, and at some point we're going to need to iron out our differences and resolve what happened that day."
        "But it's apparent to me that Sayori just needs some space right now, and I'll give her all the time she needs to get over what happened."
        "I hope she trusts me that much... after all we've been friends for as long as I can remember..."
        "I shake my head and I enter my house."
    elif encore_sayoriquestion_1 == True:
        jump sencore_1b
label day1_bedroom:
    scene black
    with wipeleft_scene
    stop music fadeout 1.0
    pause 1.0
    scene bg bedroom_night
    with wipeleft
    play music t8 fadein 1.0
    "Man... what a day!"
    "Actually, what a week!"
    "After putting on my pajamas and setting my alarm, I quickly collapse onto my bed."
    if encore_sayoriquestion_1 == True:
        "I think I'm getting better at handling Sayori. She is certainly full of surprises. One minute she can be all cheery and an airhead, then next she could be having moments of self-doubt."
        "Well, we've really only been dating for a week now, and I guess we're still trying to adjust to the new reality of being in a relationship."
        "I’m glad I decided to check up on her early in the morning before I left for the festival. Knowing how she was the day before, I was afraid she might’ve done something rather rash."
        "Thankfully, I guess that feeling was just in my head. Surprisingly, she was already up when I came to check on her."
        "But still, I feel like I finally have a real purpose in my life. I have someone who loves me and will look out for me no matter what and I have someone to look out for and care for."
        "As I drift off into sleep, I think to myself..."
        "Life is a funny thing sometimes..."
    elif encore_sayoriquestion_1 == False:
        if hangout1 == "Yuri":
            "I think I'm getting better at understanding Yuri."
            "She seems to be getting much more comfortable around me."
            "I wonder if it's because that Sunday when we made the banner?"
            "I think back to those two exchanges we had where we almost..."
            "I gush to myself reliving them in my head."
            "I wonder if Yuri really would go out with a guy like me."
            "I mean... she seems to be really into me."
            "But she really isn't one to go out of her way to step outside of her comfort zone into social situations."
            "Though, Yuri has been opening up to me more and more, so maybe there is a chance."
            "And if there's a chance to be with her, I'm definitely going to take it!"
            "It would be quite the turn of events."
            "Yuri, a girl who would often spend all her time by herself and who hardly ever raised her voice..."
            "To maybe going to out with me..."
            "I wouldn't mind it."
            "And something tells me Yuri wouldn't mind it either."
            "As I drift off into sleep, I think to myself..."
            "Life is a funny thing sometimes..."
        elif hangout1 == "Natsuki":
            "I really think I'm getting better at understanding Natsuki."
            "For starters, she didn't tease me as much as she usually does."
            "I wonder if its because of that Sunday when she showed me how to bake?"
            "I think back to those two exchanges we had where we almost..."
            "I get butterflies in my stomach just thinking about it!"
            "I wonder if she really would go out with a guy like me."
            "I hope so..I think she would... I'm really starting to like her more and more."
            "..."
            "As I toss and turn, I just can't get Natsuki out of my head for some reason."
            "Just everything about her is so beautiful!"
            "Her hair always smells of bubble gum and always look like a sea of cotton candy."
            "And I always seem to get lost in those bright pink eyes of hers... anytime she talks about manga or her day I just seem to space out just looking into them."
            "And I can never forget that joyful smile of hers! It always lights up my world."
            "I'm just hoping that sooner or later I can get the courage to ask her out. I know that she's at the very least interested in me. "
            "Who knows? Maybe she'll make the move first."
            "I find myself smiling at the thought of being with Natsuki"
            "It would be a weird turn of events. At first I thought she hated me and wanted to stay away from me as far as possible."
            "But now that I got to know her, it's like she can't let me out of her sight!"
            "As I drift off into sleep, I think to myself..."
            "Life is a funny thing sometimes..."
        elif hangout1 == "Monika":
            "I'm really surprised that Monika gave me so much attention today!"
            "Granted we haven't been able to spend too much time together over the last two weeks, it was still pretty surprising for her to show so much interest in me today."
            "Maybe all this time that's all she ever wanted, to spend time with me and get to know me."
            "It sucks we didn't get the chance to spend much time together at the festival as she had to stay in the clubroom through the entirety of the festival to get anyone that passed by to join our club."
            if encore_festivalquestion_2 == "Natsuki":
                "Oh well, I'm sure I'll get to spend more time with her soon. Afterall I need to work on mending fences with Sayori and I do think I have a pretty good thing going with Natsuki..."
            else:
                "Oh well, I'm sure I'll get to spend more time with her soon. Afterall I need to work on mending fences with Sayori and I do think I have a pretty good thing going with Natsuki..."
            "..."
            "I spend what I feel like hours just tossing and turning in my bed."
            "I can't seem to get Monika out of my head right now."
            if encore_festivalquestion_2 == "Natsuki":
                "Why did she think that I would've gone to Natsuki first for poem time?"
                "Like I said earlier, I know me and Natsuki are just friends, but does Monika really think Natsuki and I are a thing?"
                "I mean, the idea has crossed my mind, but I'm not really sure what I want to do anymore."
                "I don't even really think I should be putting this much thought into this. I mean Natsuki is cute, but I'm thinking I might be starting to like Monika more."
            else:
                "Why did she think that I would've gone to Yuri first for poem time?"
                "Like I said earlier, I know me and Yuri are just friends, but does Monika really think Yuri and I are a thing?"
                "I mean, the idea has crossed my mind, but I'm not really sure what I want to do anymore."
                "I don't even really think I should be putting this much thought into this. I mean Yuri is pretty, but I'm thinking I might be starting to like Monika more."
            "Her hair is so long and beautiful and it always smells like forget-me-nots."
            "And that athletic body of hers could make an hourglass jealous...She always moves so gracefully and every step she takes just hypnotizes me..."
            "And I can never forget those piercing emerald eyes..."
            "WHAT AM I THINKING?!? I should only care for Monika as a friend, but for some reason I feel more drawn to her than ever before."
            "But would she ever go for a guy like me? I don't think there's anything super special about me."
            "Afterall, Monika could practically have any guy she wants as her boyfriend."
            "Come to think of it, has Monika ever had a boyfriend?"
            "I know for a fact she's single right now, but..."
            "She's the most popular and beautiful girl in school after all."
            "I really should just focus on getting some sleep..."
            "Still, I should consider myself lucky."
            "Most guys would kill for the chance I have of being this close to Monika."
            "As I drift off into sleep, I think to myself..."
            "Life is a funny thing sometimes..."
    #jump protoype_end
    #Scene Transition
    #First Nightmare Scene, Day 1
    $ m_name = "???"
    scene black
    with Dissolve(1.5)
    stop music fadeout 1.0
    window hide(None)
    pause 1.0
    window auto
    if hangout1 == "Monika":
        play music e8
    m "It really is, isn't it?"
    if hangout1 != "Monika":

        "A dark, mysterious, eerie, voice echoes in my head."
        "What is this?...Who is this?"
        m "It really is funny how one can plan for life to go one way, only to have something completely different happen."
        m "One would think that experience would just make you stronger as a person as you would try to overcome the obstacles in life… only until you come to question the very nature of reality."
        m "I’ve come to realize how fake this world really is."
        m "But, I know how to make it real... just for us..."
        m "And you’re not helping things!"
        m "It's your choice after all."
        m "But every choice you make has a consequence."
        "Who is this person?!?"
        if hangout1 == "Sayori":
            m "If it wasn’t for my little screw up, none of this would be happening right now!"
        else:
            pass
        m "You want to find out what should've happened?"
        show cg door 1 with dissolve_cg
        "A door suddenly appears before me."
        m "Open it, this is what you should've let happen..."
        "I can't control my actions at this point, it feels as if I'm being controlled."
        "My body floats over to the door."
        mc "Oh God..."
        show cg door 2 with dissolve_cg
        if hangout1 == "Sayori":
            "I gently open the door...{nw}"
            hide cg
            play music e11
            #scene cg s_cg_3
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
            #cue Sayori Hanging Scene
            "...."
            "What the hell?"
            "What the HELL?"
            "What the FUCK is this?"
            "Is this... real?"
            mc "S-Sayori?"
            "N-no...she wouldn't..."
            "She would never do something like this!"
            "No... this can't be... this is just a bad dream..."
            scene black with Dissolve(0.5)
            "I'm having a bad dream."
            #Scene Transition
        elif hangout1 == "Natsuki":
            $ n_name = "???"
            "Swinging open the door I...{nw}"
            scene bg n_void_1
            play music e10 fadein 1.0
            #Instant Scene Transition
            #Club Room Scene Upside Down

            scene bg n_void_1
            "...find myself back in the clubroom?"
            "Only... something's off..."
            "I look up to up to see all the desks and chairs on the ceiling for some reason. Arranged as they normally would be."
            "Wait... why is everything on the ceiling?"
            "I look down to see that I'm actually on the ceiling."
            "Everything is upside down"
            "This feels surreal in a sense."
            "What the hell?"
            "I hesitantly take a step forward and I notice the world around me shifts with me."
            n "Hey [player]!"
            "I know that voice."
            "It's coming from the closet."
            n "Come over here! I need your help with something!"
            $ n_name = "Natsuki"
            mc "N-Natsuki?"
            n "Come on, dummy! I don't have all day!"
            "Something's telling me that I shouldn't go over there."
            "But I lose control of my body and the room around me shifts everytime as I unwilling walk closer to the closet."
            #Glitch
            #Scary Closet Scene
            scene bg closet_empty
            with Dissolve(1)
            "I stop just outside the closet."
            "It's pitch black and I can't see anything."
            mc "N-Natsuki?"
            mc "Are you in there?"
            "There's no response."
            mc "Natsuki? Are you in there?"
            "The closet isn't that big so it's not like there's much room for her to hide from me."
            "I then see Natsuki's face emerge from the darkness."
            mc "Natsuki?"
            show natsuki xu8172 at t11 zorder 1
            n "There you are [player]!"
            "She eerily smiles at me with a wicked look in her eyes."
            "Every warning sign in my body is telling me to run away but I can't move my legs."
            n u112172 "I wanted to show you something."
            "A piece of paper floats over to me and my arm out stretches and grabs it without my manual control."
            n u212172 "I wrote it just for you!"
            call showpoem(poem_n2b, music=False, revert_music=False, paper ="paper_glitch") from _call_showpoem
            # Glitched, unreadable poem
            "..."
            n ghost1_new "[player]."
            n "Did you like it?"
            n "I spent all day working on that."
            n "I know you like me [player]"
            n "So why don't you play with me?"
            n "Play with me [player]!"
            #######
            "I see Natsuki's eyes fall out as her voice becomes more and more distorted."
            show natsuki ghost2
            "I see Natsuki give me a unnatural smile that no human can ever realistically make."
            $ style.say_dialogue = style.edited
            stop music
            n "PLAY WITH ME!"
            $ style.say_dialogue = style.normal
            play sound "sfx/crack.ogg"
            show natsuki ghost3
            pause 0.50
            play sound "sfx/run.ogg"
            show natsuki ghost4
           #*Natsuki snaps her neck and rushes the player*
            scene black
            "...."
            "I open my eyes."
            "I look around to see nothing but black empty space."
            "Doing a quick self-check, I appear to be ok."
            "What the hell?"
            "What the HELL was that??"
            "What the FUCk?"
            "Was that... real?"
            "No... this can't be... this is just a bad dream..."
            "I'm having a bad dream."
        else:
            scene club_nothing
            hide cg
            with dissolve_cg
            play music e9
            "...find myself back in the clubroom?"
            "Only... something’s off..."
            "The clubroom is completely empty."
            "There’s no desks or chairs."
            "What is this?!?!?"
            "I hear the doors to the clubroom open."
            "I turn to see who opened them."
            "It’s Yuri."
            y "HI, [player]!"
            "Yuri has a deranged look on her face."
            mc "Um... Hi... Yuri..."
            "I don’t really know what to say or do in this situation."
            mc "Where... where are we?"
            y "It doesn’t fucking matter!"
            y "What matters is that we’re here together."
            y "Alone."
            "Yuri lets out an insane, maniacal laugh."
            "A laugh no human should ever be able to make."
            "I want to scream and run, but I can’t move my body or open my mouth."
            y "I made something for you [player]."
            "A piece of paper floats over to me, my hand stretches out to grab it."
            y "I’ve put a lot of thought into it...."
            y "Please tell me what you think!"
            #Glitched, unreadable poem
            y "[player]"
            y "What did you think?"
            y "Isn’t it the best thing you’ve ever read?"
            y "I spent all night working on that!"
            y "I had to cut myself 5 times to make sure that I finished that poem."
            y "I actually almost passed out writing that."
            y "Ha..."
            y "I actually forced myself not to go to the bathroom either... so sorry if I got the poem a little wet...."
            y "I hope you like my scent!"
            y "Ahahaha"
            y "HAHAHAHAHAHAHAHAHAHAHA!!!!!!!!!"
            "Yuri pulls out a knife."
            "Fuck."
            y "Do you love me [player]?"
            y "Tell me you love me!"
            stop music
            y "LOVE ME!!!!!!!!!!!!!!"
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
                easeout_cubic 0.7 yoffset 600
            show blood as blood2:
                pos (635,335)
            pause 0.70
            hide yuri
            pause 1.85
            hide blood
            hide blood2
            pause 0.25
            play sound fall
            pause 0.25
            "...."
            "I open my eyes."
            "I look around to see nothing but black empty space."
            "Doing a quick self-check, I appear to be ok."
            "What the hell?"
            "What the HELL was that??"
            "What the FUCK?"
            "Was that... real?"
            "No... this can’t be... this is just a bad dream..."
            "I’m having a bad dream."
            scene black
            m "You’re lucky that this is a dream."
            m "This is what you should’ve ultimately let happened."
            m "But you just had to change reality..."
            m "And that let her live..."
            m "Do you realize the box you’ve put me into?"
            m "Oh well, I’ll make it work."
            m "But you certainly aren’t making this any easier on me or you."
            m "Just do me a favor, stay away from Yuri."
            m "Let her die."
            m "She’s not worth your time."
            m "Let her suffer."
            m "Let her die..."
            $ m_name = "Monika"
            m "You're lucky that this is a dream."
            m "This is what you should've let happened."
            m "But you just had to change reality..."
            m "And that let her live..."
            m "Do you realize the box you've put me into?"
            m "Oh well, I'll make it work."
            m "But you certainly aren't making this any easier on me or you."
        if hangout1 == "Sayori":
            m "Just do me a favor, stay away from Sayori."
        elif hangout1 == "Natsuki":
            m "Just do me a favor, stay away from Natsuki."
        else:
            m "Just do me a favor, stay away from Yuri."
        m "Let her die."
        m "She's not worth your time."
        m "Let her suffer."
        m "Let her die...."
    elif hangout1 == "Monika":
        "A dark, mysterious, eerie, voice cheerfully echoes in my head."
        "What is this?...Who is this?"
        play music mend fadein 1.0
        m "Life is full of an infinite amount paths with an infinite amount of possibilities."
        m "That is, if you believe in that sort of thing."
        m "Reality seems to be blurred between what is real and what is fake."
        "Who is this person?!?"
        m "For a second there, I really thought you threw a wrench into my plans for us."
        m "But I see now that this could actually work out for us."
        m "I'm so happy right now."
        m "Words honestly cannot describe my feelings at this moment."
        m "But I can always try."
        m "Hehe~"
        m "Now that I have this opportunity I won't waste it!"
        m "I'll grab on to you and never let go!"
        m "All I ever wanted was to at least have a chance."
        m "And to think the lengths I almost went to just for that chance..."
        "A cold chill runs down my spine."
        m "It's not my fault!"
        m "If you just hated them from the beginning then everything would have been fine!"
        m "If anything it's your fault."
        "The voice booms inside my head."
        m "But it's okay! I forgive you."
        "The voice giggles in my ear as if it were amused with itself."
        m "Thank you."
        m "Thank you for saving yourself for me."
        m "But do me one small favor, okay?"
        if encore_festivalquestion_2 == "Natsuki":
            m "Stay away from the others, especially little miss punching bag."
        else:
            "Yuri line needed."
        m "I won't have her or any of the others foiling my plans..."
        m "Just stay away from them..."
        m "Stay away from them..."
        m "And we'll be together forever...."
        m "We'll never be apart..."
        stop music fadeout 1
    else:
        pass
    #Scene Transition
    #Black Scene
    scene black
    call affectionasignment from _call_affectionasignment
    jump day2_start
    