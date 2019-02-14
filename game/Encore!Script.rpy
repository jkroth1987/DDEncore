image sayori 1shadow = shadow("mod_assets/sprites/char_bases/s_base")
image sayori 1bshadow = shadow("mod_assets/sprites/char_bases/sb_base")
image natsuki 1shadow = shadow("mod_assets/sprites/char_bases/n_base")
image natsuki 1b shadow = shadow("mod_assets/sprites/char_bases/nb_base")
image yuri 1shadow = shadow("mod_assets/sprites/char_bases/y_base")
image yuri 1bshadow = shadow("mod_assets/sprites/char_bases/yb_base")
image monika 1shadow = shadow("mod_assets/sprites/char_bases/m_base")

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
label protoype_end:
    "That's it for this protoype."
    return


#############
#   DAY 2   #
#############
label day2_start:
    stop music
    play sound "sfx/fall.ogg"
    scene bg bedroom
    $ day = 2
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ e_name = "Extra"
    "I awake, startled and confused."
    if hangout1 != "Monika":
        "I quickly realize that my face is covered in sweat and that my head is throbbing."
        mc "Oh God.... what the hell was that?"
        "I prop myself up in my bed, holding on to my head in an attempt to still the pain, sweat trickles down my forehead"
        "..."
        "After a few minutes my head stops throbbing."
    else:
        "My head feels like its about ready to explode."
        "That voice..."
        "It felt so strange and yet..."
        "Familiar."
        "A chill inches down my spine and extends into my fingertips as I feel my chest get tighter."
        "My body is coated in a layer of sweat that only gets thicker with every second."
        mc "Calm down, it was just a dream..."
        "...Right?"
    "I look over to my alarm and see that I still have a few minutes before I have to get up, but after that experience I decide that I might as well get ready now."
    #Scene Transition
    scene bg living_room
    with wipeleft_scene
    play music t2 fadein 1.0
    "I take a shower, put on my Uniform, and fix myself up some breakfast."
    "I figured I'd go with something simple like a chocolate muffin and some Orange Juice."
    if encore_sayoriquestion_1 == True:
        "While eating my muffin, I grab my phone and send Sayori a quick good morning text"
        "After a few minutes she responds back and tells me that she'll be out in ten minutes and that I should wait by her place."
        "After finishing my breakfast I head outside to meet Sayori."
    else:
        "After finishing my breakfast I head outside to meet Sayori for our daily commute together."
    scene bg house
    with wipeleft_scene
    if hangout1 != "Monika":
        "While I'm waiting I ponder about last night's dream."
        "I get a chill remembering what I saw when I opened the door."
        "And that voice...what the hell was it talking about?"
    else:
        "While I'm waiting I ponder about last night's dream."
        "It felt so real."
        "Like someone or something was whispering in my ear..."
        "And that voice..."
        "It feels so familiar."
        "Like I've heard it before."
        "..."
        "I feel my headache coming back."
    "It was probably nothing, I think I'm probably just reading too much into this."
    "No point of trying to interpret a random, jumbled nightmare anyways."
    "Once I finish my thought, I catch out of the corner of my eye Sayori opening her front door and walking out to meet me."
    $ renpy.pause(delay=0.001)
    show s_kill zorder 1:
        alpha 0.028
        xalign 0.5 yalign 0.05
    $ renpy.pause(delay=0.011)
    hide sgone
    #(Possible Hanging Sayori glitch?)
    if encore_sayoriquestion_1 and hangout1 == "Sayori":
        play sound "sfx/fall.ogg"
        show sayori 1q at t11 zorder 2
        "I turn around and smile as she walks up to me and pulls me into a tight embrace."
        "Time seems to stop as we stand there, holding each other in plain sight without a care in the world."
        show sayori 1d at d11
        "Eventually we snap out of it."
    else:
        show sayori 1b at t11 zorder 1
        mc "Hey Sayori.."
        "I still feel guilty for making Sayori runoff yesterday. I wasn't trying to be insulting to her."
        "But I really underestimated the amount of time it'd take for Sayori to really get over this."
        s 2c "Hey [player]...how are you?"
        "I can tell Sayori's trying to be as friendly as possible, but it's not hard to tell that yesterday is still bugging her."
        mc "I'm..I'm good, what about you?"
        s 1l "Oh I'm good..."
        "She says that as she looks off in another direction, not wanting to make direct eye contact with me."
        mc "Well. hey, that's good!"
        show sayori 1d
        "Sayori manages a small smile."
        "If it weren't for the breeze that was going on outside, the air would be incredibly heavy."
        "We both try to find something to say, but we just end up standing there awkwardly looking at each other."
        "Finally, Sayori manages to break the silence."
    s 3l "Guess it's time for school, huh?"
    mc "Yeah...guess so."
    if encore_sayoriquestion_1 == True:
        show sayori 1y
        "We walk the rest of the way, holding each other's hands and making small talk."
    else:
        "And with that, we begin our daily walk to school."
    #Scene Transition
    #Outside Class
    scene image "bg/corridor.png"
    with wipeleft_scene
    show sayori 1b at t11 zorder 1
    "For once, we make it to school relatively early."
    "Sayori and I pass the time by slowly walking up and down the corridors around her classroom until the morning bell rings."
    s 3x "Well, there's the bell. I'll meet you same place as yesterday."
    mc "Sounds good to me!"
    if encore_sayoriquestion_1:
        "We quickly hug each other and walk off to our respective classrooms."
    else:
        pass
    scene bg class_day
    with wipeleft_scene
    "As always, the school day is boring and uneventful, and is over before I know it."
    "I just can't wait to head up to the club again."
    show sayori 1a at t11 zorder 1
    "I pack my things and head outside of the classroom where I'm greeted by Sayori, whose already standing there."
    s 2x "Hey, [player]! Ready to go?"
    mc "You know it!"
    "We then begin our walk to the clubroom..."
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    "We arrive at the clubroom with the usual scene greeting us."
    "Yuri is in her usual spot, intently reading the Portrait of Markov, while Natsuki is still rummaging around in the closet."
    "I see Monika using the teacher's desk at the front of the room, but when we walks in she flashes us a smile."
    "At least she seems to be in better spirits today."
    "Sayori takes a spot in the middle row next to the wall and sets her stuff down."
    menu:
        "Who should I hang out with?"
        "Sayori":
            $ s_modappeal +=1
            jump sencore_2
        "Natsuki":
            $ n_modappeal +=1
            jump nencore_2
        "Yuri":
            $ y_modappeal +=1
            jump yencore_2
        "Monika":
            $ m_modappeal +=1
            jump mencore_2
    #Who should I spend time with today?
    #Monika
    #Natsuki
    #Sayori
    #Yuri
    #Sayori is selected
    #(Scoreboard, S: 3, N: 1, Y: 0, M: 0)
    #Scene Transition
    #Clubroom Scene
label day2_meettheclubs:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    "We all sit at the front of the room, with Monika standing right in front of us."
    show monika at t11 zorder 4
    m 3b "Okay everyone! Here's the news!"
    m 3a "Starting next week, the Student Newspaper and Photography Club are going to be going around to all the different clubs and doing a profile on them."
    m 2a "It's part of their bi-annual \'Meet The Clubs\' piece that they do every semester."
    m "As of now, they're scheduled to meet with us to do their piece next Monday. So, I was hoping that we could think of something that'll really show off the club."
    show monika at t22
    show natsuki 5x at t21 zorder 1
    "Natsuki audibly groans."
    n 5e "Is this going to be like the festival again?"
    show monika 2d
    "Monika seems a little taken aback by this, but she shrugs it off."
    m 2c "No, not really. We won't have to be performing for anyone this time, and I certainly don't think we'll need to put in the same level of preparation for this compared to the festival."
    show natsuki 5g
    m 2b "But I would appreciate it if we could at least come up with something nice that'll show off the club. "
    show monika at t43
    show natsuki 1s at t41
    show yuri 1g at t44 zorder 3
    show sayori u115191 at t42 zorder 2
    "Everyone takes a moment to collect our thoughts."
    call groupAll(4, 2, 4, 1, 3) from _call_groupAll_3
    if encore_festivalquestion_2 == "Natsuki":
        "Finally, Yuri is the first one to speak up."
        show monika 1c
        show sayori 1b
        show natsuki 1k
        y 1f "You know...I did happen to keep the welcome banner we made for the festival. I'd just need to find it. It's somewhere at my house."
        n 1d "I wouldn't mind baking cupcakes again...I especially had fun doing it last time with [player]"
        show natsuki 1a
        "She says that directly looking at me."
        if hangout2 == "Sayori":
            show natsuki 2a
            "Natsuki certainly isn't letting what just happened between me and Sayori go."
        if encore_sayoriquestion_1 == True:
            "It also seems that Natsuki either hasn't put two and two together yet, or she isn't going to give this up without a fight."
            mc "Y-yeah... It was fun..."
            show sayori 1g
            "Sayori once again shoots me the same quizzical glance she gave me yesterday when Natsuki brought up the time we spent together last Sunday."
            "Sooner or later, I'm going to have to resolve all this and tell Natsuki that I'm with Sayori as well as tell Sayori everything that happened between me and Natsuki on Sunday so I could put her mind to rest."
            "But today is not that day!"
        else:
            mc "Y-yeah! Me too Nat!"
            show natsuki 1i
            "Natsuki looks at me with a puzzled look."
            n 2h "Did you really just call me ‘Nat'? Where did that come from?"
            mc "I don't know, I thought it'd be a cute little nickname for you."
            show natsuki 4s
            "Normally, Natsuki would shoot me an irritated look before proclaiming to everyone that she wasn't cute, but this time it doesn't even look like she knows how to get properly get mad at me."
            "She tries to pout but I can tell she's forcibly trying to hold back a grin."
            n 4q "Are you implying that I'm cute?"
            mc "And if I was?"
            n 4r "Uuuu!"
            "Natsuki suddenly looks off in another direction, only becoming more flustered."
            show natsuki 4s
            mc "I just love having fun with you."
            "Natsuki turns back to face me, no longer able to contain her grin."
            n u112212 "I'll let that slide.... just this once!"
            show sayori 1t
            "I chuckle to myself, but in the corner of my eye I see Sayori looking at me."
            "She's trying to force a grin, but I can tell that she's fighting back tears."
            show natsuki u111233
            mc "I-I mean..I always love spending time with you all and..."
            #show sayori 1t
            "Seeing Sayori just trying to hold back her tears derails my train of thought."
            "Great."
            "I never did take into account that she might not yet be comfortable with me being this flirty around Natsuki yet."
            if hangout2 == "Monika":
                "Heck, she probably isn't even comfortable seeing Monika and I get so close like that either."
            mc "Um... yeah... so..."
            "I look like an idiot as I try to find what to say next."
    else:
        "Finally, Natsuki is the first one to speak up."
        show monika 1c
        show sayori 1b
        show yuri 1e
        n 1k "I wouldn't mind baking cupcakes again, I still have plenty of ingredients left over."
        y 1b "I did happen to keep the welcome banner that [player] and I made for the festival. I'd just need to find it. It's somewhere at my house, and I wouldn't mind for some help looking for it."
        "She says that directly looking at me."
        if encore_sayoriquestion_1 == True:
            "I'm guessing we need some lines for if the player confessed to Sayori."
        #what? This line of dialogue has no correlation to the first
        else:
            mc "Y-yeah! You too Yuri!"
            show yuri 2t
            mc "I'd love to come over to your place anytime!"
            show yuri 2u
            mc "Preparing for the festival with you was really fun!"
            "Yuri looks off blushing like crazy."
            y 2q "Y-yeah... it was really nice..."
            show yuri 2p
            "She says that softly to herself, but quickly realizes that everyone overheard."
            y 1o "Oh! I mean... yeah, I would love your help!"
            show yuri 4c
            "I chuckle to myself, Yuri's mannerisms have always been adorable."
            show sayori 1t
            "In the corner of my eye I see Sayori looking at me."
            "She's trying to force a grin, but I can tell that she's fighting back tears."
            show yuri 4a
            mc "I-I mean.. I always love spending time with you all, and..."
            "Seeing Sayori this way derails my train of thought."
            "Not good."
            "I never did take into account that she might not yet be comfortable with me being this flirty around Yuri yet."
            if hangout2 == "Monika":
                "Heck, she probably isn't even comfortable seeing Monika and I get so close like that either."
            mc "Um... yeah... so..."
            show yuri 2u
            show sayori 1k
            "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    show yuri 1e
    show natsuki 1k
    show sayori 1b
    m 3b "I can type up a summary of what we do on a day-to-day basis and write some things down for what we can tell the Newspaper."
    s 2x "Ooh, ooh, I know what I can do!"
    "Everyone turns to Sayori."
    s 1x "I can go to the library and get some books for us to read! I'd think it'd look good for when they take pictures of us!"
    m 1b "Great call, Sayori!"
    m 1a "As for you, [player], do you have any ideas?"
    mc "Hmmmm..."
    "I take a few moments to think to myself."
    "Suddenly I got an idea."
    mc "Well, I can bring in some famous poems that we could also use for the photo ops, I'd think it'd be great to show that there's more to literature than just books."
    mc "Heck, maybe we can even use some of our own poems as well, I can organize them together like Monika did, but I'll need everyone else's poems."
    show yuri 1g
    show monika 1c
    show sayori u114111
    show natsuki u116113
    "Everyone pauses to reflect on what I just said."
    m 2b "That's a good idea, [player]! I'll hand you all my stuff tomorrow if that's ok with you."
    mc "That's perfectly fine!"
    s 2x "I have all my poems back at my place, I can give them to you later."
    y 1b "Same here, I'll give you them at tomorrow's meeting, [player]."
    n 3c "I think I have mine with me, let me check."
    show monika at thide
    show sayori at thide
    show yuri at thide
    hide monika
    hide sayori
    hide yuri
    show natsuki 1a at t11
    "Natsuki searches through her bag and retrieves a few sheets of paper."
    show natsuki 1d at t11
    n "Here you go, that should be everything."
    "Natsuki hands me the sheets of paper, and I carefully put them in my bag."
    mc "Thanks, Natsuki."
    show natsuki 1a at t41
    show monika 1a at t43 zorder 4
    show yuri 1a at t44 zorder 3
    show sayori 1a at t42 zorder 2
    m 1a "Okay everyone, you all know what to do. That concludes today's meeting! Be sure to find your poems and give them to [player]!"
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show sayori 1a at t11
    "We all pack up our things and head out."
    "Sayori and I split from the rest of the group on the way out and we begin our way home."
    stop music fadeout 1.0
    #Scene Transition
    #Outside House Scene
    scene bg house
    with wipeleft_scene
    play music t8 fadein 1.0
    if encore_sayoriquestion_1 == True:
        play music e4
        "Sayori and I walk home together holding hands."
        "It seems that we've gotten more comfortable with showing off our affection for each other in public, even if it's something simple as holding hands."
        "We make some small talk on the way home, mostly talking about how our day went."
        "Eventually we reach Sayori's house."
        show sayori 1a at t11 zorder 1
        s "Hey, [player]?"
        mc "Yeah?"
        s "I think I know where my poems are, I'll stop by your house in a bit and drop them off if that's okay with you."
        mc "Yeah, sure! I'll see you in a bit Sayori."
        "After a brief hug, both of us head to our houses."
        show sayori at thide
        hide sayori
        "Hopefully Sayori can stay over a little longer this time..."
    else:
        "Sayori and I walk home together..."
        "We make some small talk on the way home, mostly talking about how our day went."
        "Eventually we reach Sayori's house."
        show sayori 1b at t11
        s "So [player]..."
        mc "Yeah?"
        s 1y "You know, it's been a while since we got to hangout, you know?"
        mc "Yeah... it has been..."
        s 1l "Well, I know where my poems are so...."
        show sayori u111222
        "I see where Sayori is going with this."
        show sayori 1b
        mc "Well if you want to come over with your poems and hangout for a few hours, I wouldn't mind."
        s "Are you sure that's okay? I wouldn't want to ruin your plans for tonight..."
        if hangout2 == "Monika":
            "I take it Sayori probably thinks I'm going to have an extended cuddling session with Monika tonight based off what she saw earlier in the club."
        elif hangout2 == "Natsuki":
            "I take it Sayori probably thinks I'm going to have an extended cuddling session with Natsuki tonight based off what she saw earlier in the club."
        else:
            "I take it Sayori probably thinks I'm going to have an extended cuddling session with Yuri tonight based off what she saw earlier in the club."
        "While that's not a bad idea...."
        mc "Yeah, I got nothing going on for tonight. I'll see you in a bit okay?"
        s u222141 "Alright! I'll see you in a bit [player]!"
        show sayori at thide
        hide sayori
        "Sayori happily skips to her porch and enters her house."
        "Well that seemed to put her in a good mood."
    #Scene Transition
    #Bedroom Scene
    scene bg bedroom
    with wipeleft_scene
    "I drop my book bag in the middle of my room and change out of my uniform."
    "I then begin looking through the stack of papers on my desk in an attempt to search for my poems."
    "Fortunately, it didn't take too long to find all the ones I wrote."
    "Reading through them, I see how far I've progressed as a writer."
    "My more recent poems certainly seem more developed and structured compared to the first poem I wrote."
    if encore_sayoriquestion_1 == True:
        "I'm also reminded of the inspiration behind all these poems... my dear Sayori."
    else:
        pass
    if hangout2 == "Natsuki":
        "I'm also reminded of the inspiration behind all these poems...Natsuki."
    elif hangout2 == "Yuri":
        "I'm also reminded of the inspiration behind all these poems...Yuri."
    else:
        "I'm also reminded of the inspiration behind all these poems...Monika."
    "Just thinking of her allowed me to power through the arduous task of writing a poem."
    "I'm really lucky to have found someone like her."
    "I put down my poems and go to my bag to retrieve Natsuki's poems, which I put right next to mine."
    "I notice that Natsuki's stack of poems is slightly larger than my stack of papers."
    "Hmm... maybe I'm missing a poem, or she accidentally gave me something that's in that stack..."
    "Before I could investigate further, I hear my doorbell ring."
    "Wow, Sayori was a lot quicker than I'd thought she'd be."
    "I go downstairs and open the door..."
     #Scene Transition
     #Living room Scene
    scene bg house with wipeleft_scene
    "... to see Sayori standing outside with a stack of papers."
    show sayori 4br at t11 zorder 1
    s "Hey, [player]! I found them!"
    show sayori 1bq
    "She hands me the stack of poems."
    mc "That's awesome! Thank you Sayori! You're the best."
    show sayori 1bs
    "Sayori smiles brightly from my comment, I see a slight blush forming on her face."
    if encore_sayoriquestion_1 == True:
        "Alright! This is my chance!"
        show sayori 1bb
        mc "Hey, Sayori?"
        s 1bx "Yes, [player]?"
        mc "Y'know...since you're already here, why don't you come inside and hangout for a bit?"
        "Sayori responds almost instantly, as if she was waiting for me to ask this."
        show sayori 1bq at h11
        s "Yeah! I'd love to!"
        "Success!"
    "I move aside to let Sayori in, closing the door behind her."
    "I grab the stack of poems from her and lay them on the dining room table."
    scene bg living_room
    with wipeleft
    if encore_sayoriquestion_1 == True:
        "After dealing with the poem hoard, I head towards Sayori, who has found her way into the living room."
        show sayori 2bc at t11 zorder 1
        s "So... what exactly do you want to do?"
        stop music fadeout 1
        mc "I... I've definitely got more than a few ideas in mind..."
        s 1bn "O-Oh? And what would they be?"
        "She looks at me quizzically, an obviously sense of intrigue in her eyes."
        mc "Well...let me show you..."
        show sayori 1be at f11
        "We both shuffle closer to each other, until we're close enough to feel each other's breath."
        "Her breaths are shallow... her eyes are locked with mine. My vision feels hazy...her eyes...have they always been that beautiful blue color?"
        "The scent of cinnamon, mixed with the feeling of her soft breaths grazing my neck..."
        "Her gorgeous blue eyes... "
        "Suddenly I remember what I wanted to do."
        play music t6 fadein 1.0
        mc "Remember when we had that big debate over who could get more gold trophies in Mario Kart when we were little?"
        show sayori 1bo
        "Sayori pauses to remember."
        s 2bc "Yeah... why?"
        mc "I think it's time to settle that debate again."
        show sayori 1bq
        "Sayori giggles at my suggestion."
        s 4br "Alright, [player]. I'll warn you though, I won't hold back."
        "She manages to say in both a playful and ominous tone."
        "Growing up, Sayori and I had a bit of an \"annual competition\" to see who could get more gold trophies in Mario Kart."
        "Every so often we would trade the winning title, but I remember that I barely beat her out last time."
        "We also had a tradition where the loser would have to pay for the winner's ice cream at Gomaya's."
        "Usually when Sayori would win, she'd get the most ridiculously expensive sundae, almost as a way to rub it in that she won. Usually I'm humble and get something cheap."
        show sayori 1ba at s11
        "I power on my Wii and hand her one of the controllers. Seeing Mario Kart boot up really brings back a lot of memories. It's been years since I've played this game, and even longer since Sayori and I have played it together."
        "My skills are probably a little rusty, and I hope her's are too. "
        mc "What map should we play first?"
        "Sayori shoots me a sly look."
        show sayori c112171
        s "How about Rainbow Road?"
        mc "Really? You sure? I know its an iconic map, but it's hard remember."
        s 1bq "Yea, its fine, I know it's hard, but it's still fun."
        "We sit there choosing our racers. I choose Luigi, and she chooses Daisy. She used to play as Daisy a lot, and same with me with Luigi."
        show cg rr1 zorder 10 with dissolve_cg
        play music e7
        mc "May the best player win."
        s c121114 "Oh, you're on now."
        show cg rr2 with dissolve_cg
        "The race is off, the first thing I do is fall right off the map, Sayori falls off too."
        show sayori 1bn
        mc "Okay, yea this is a lot harder then I remember."
        s 1ba "Yea you're right, but I'm still having fun with you."
        show cg rr3 with dissolve_cg
        "We go at it back and forth passing each other over and over. I've been in first for most of the game, so that means I've been getting hit with lots of red shells."
        mc "Why do you have so many red shells?"
        s 1bc "I've been in second for most of the game, remember the farther you are from first place, the better items you get."
        mc "Yea you're right I forgot."
        show cg rr4 with dissolve_cg
        "Finally it comes down to the last stretch of the race, I'm barely in first. I try and gloat by throwing my last item randomly."
        "That very quickly comes back to bite me in the ass."
        mc "Oh crap, no, no, no, no!"
        "I end up hitting myself with a green shell."
        "Before I knew it she passed me and won."
        show sayori 1br at t11
        s "YAY! I WON!"
        "I sit there absolutely stunned."
        stop music fadeout 2
        "I just cost myself the game..."
        play music t6
        show sayori c112171
        hide cg with dissolve_cg
        s "Looks like you'll have to buy me my favorite sundae again!"
        show sayori 1bm at h11
        mc "Oh no, not if I have anything to say about it!"
        show sayori at thide
        hide sayori
        play sound "sfx/fall.ogg"
        "I playfully tackle her to the floor."
        "She giggles as she tries to get up, but fortunately I'm too strong for her."
        #show sayori 1bp at s11 zorder 1
        #exp
        show cg s_cg_2 pin with dissolve_cg
        s c116314 "H-hey... no fair, meanie! You promised!"
        "Sayori playfully pouts at me while giving me puppy eyes."
        "Under most circumstances, they really wouldn't work on me, but for some reason, today, they're super effective."
        mc "I know... I know... I'm gonna buy you whatever you want, I'm just messin with you, Sayori."
        #show sayori 1bn
        show cg s_cg_2 relieved with dissolve_cg
        "Sayori shoots me a look of relief"
        s 1bo "So when do I get my ice cream?"
        mc "As soon as you can get up."
        "Sayori manages to put up a good effort to get up, but again I'm too strong for her."
        stop music fadeout 2.0
        queue music t9
        mc "Hahaha...you haven't changed a bit, have you Sayori?"
        s "Neither have you, [player]."
        mc "Oh yeah? How so?"
        s 1bc "You've always been that brash, funny guy next door who always has his head in the clouds."
        s 1be "You've always been so kind to me, even when I don't think I deserve it. You've always looked out for me..."
        "I can hear Sayori's voice starting to break."
        show cg s_cg_2 happy with dissolve_cg
        s 1by "You always help me when I'm feeling down, even if you don't realize that."
        "Trying my best not to blush, eventually I break and crack a wide grin at her."
        s "You're the reason I even get up out of bed in the morning, [player]. You're the reason I can feel happiness and joy in my life. You're the reason I'm even alive."
        #show sayori at t11
        #exps
        s c112314 "Even when I'm at my lowest point... when those rainclouds just pour on me... you're my sunshine that I need to break them away..."
        s 4br "I see now that I'm the luckiest girl in the world to have you as my boyfriend..."
        show cg s_cg_2 happy tears with dissolve_cg
        "I see tears start to swell up in Sayori's eyes."
        "Listening to Sayori say that really hits me hard inside..."
        "I'm the reason she's alive? There's no way she would...you know...she would never..."
        "Before I can finish my train of thought, Sayori inches her face closer to mine."
        #show sayori 1be at f11
        s "[player]...I-"
        show cg s_cg_2 pucker with dissolve_cg
        #show white with Dissolve(0.25)
        "Sayori's lips suddenly meet mine."
        "Despite the sudden shock, I manage return her kiss. Our lips interlocking."
        "The taste of peach fills my mouth as our lips push back against each other. The smell of cinnamon radiating from her hair seems to put me in a trance."
        #hide white with dissolve_cg
        #show sayori 1be at t11 zorder 1
        "I pull back, and lock eyes with Sayori. As she lays there with baited breath."
        show cg s_cg_2 happy with dissolve_cg
        "There's a minute of silence between us as we get lost in each other's eyes."
        "Finally, I decide to break the silence."
        mc "So...I guess you won."
        s 4bq "Hehe...yeah. I won fair and square."
        stop music fadeout 2.0
        #show sayori 1bq at h11
        "I get off of Sayori and help her up."
        hide cg with dissolve_cg
        show sayori 1bq at t11
        mc "Well, I think that's enough video games for one day, want to see what's on TV?"
        s 2bx "Yeah, sure!"
        show sayori at thide
        hide sayori
        "We spend the next few hours watching some old movies and cuddling."
        "Eventually the sun sets and it starts to get dark out."
        show sayori 2bc at t11 zorder 1
        s "Well, I better head back and start getting ready for tomorrow."
        mc "Yeah... bummer that the day went by so fast."
        s 1bx "Yeah... but I'll see you tomorrow, [player]! I had so much fun with you today!"
        mc "I'm glad you did Sayori, I always love spending time with you."
        show sayori 1bs at f11 zorder 1
        "I walk Sayori out and we hug one last time before she gives me a kiss on the cheek and heads back to her house."
        show sayori at thide
        hide sayori
        "Man, am I the luckiest guy on Earth to have someone like her."
        "All I wish is that I could spend everyday like this with her..."
    else:
        show sayori 1bc at t11 zorder 1
        s "Sooo...got anything planned for us?"
        mc "not really we could just watch some tv if you want?"
        s 2bc "Yeah that's fine."
        play sound "sfx/fall.ogg"
        show sayori 1bb at s11
        "Sayori and I take a seat on the couch right next to each other and we begin flipping through the channels to see if there's anything remotely interesting worth watching."
        "Suddenly something catches Sayori's eye as I start rapidly moving through the channels."
        s 2bn "Ohhh [player]! Go back like  2 channels!"
        mc "Uhh, ok."
        "I flip back and we see that it's a cartoon we used to watch a lot when we were kids."
        mc "Oh wow... Expedition Time! I haven't seen this in ages!"
        s 1bq "Hehe..yeah we used to watch this together every Saturday, remember?"
        "I recall Sayori always walking over to my house every Saturday to watch it with me. It was your typical action-adventure kid-friendly series, though it had a really great story for it's time."
        show sayori 1bu
        "I see out of the corner of my eye that Sayori's tearing up."
        mc "What's wrong Sayori?"
        "She points at the TV. I see the episode title...this was the last episode they made."
        "That's a bummer. I thought it was at least still being made, though the show already had an incredibly long lifespan and it was starting to show that the producers were running out of ideas."
        "When Sayori and I started high school we stopped hanging out and we didn't get to watch it together as much."
        "I look at the date of the episode. I'm surprised, it only aired a few months ago."
        mc "I can't believe we missed the finale by a few months!"
        #exps
        # CHANGE : Changed them back to regular expressions due to a visual error
        s 1bt "Yeah, me too."
        "Sayori wipes her eyes."
        s 1bd "Well let's watch this episode together...for old time's sake!"
        mc "Let's do it!"
        show sayori 1bt
        "As we watch the episode, I can't help but feel a few years younger."
        show sayori 1bt
        "My mind is filled with all the memories I shared with Sayori. From when we first met, to all the times we played games, to moments like this...."
        "She really was always there for me...."
        "I miss spending time with Sayori, even if it was something simple as watching our favorite show together. Why did this have to change?"
        "I stop to think to myself."
        mc "No...I changed..."
        "Sayori perks up."
        #exp
        s c115112 "Did you say something, [player]."
        mc "Oh... it was nothing."
        show sayori 1bt
        "Sayori sighs and turns back to the TV."
        "I sigh to myself."
        "I really shouldn't keep this from her. I already shut her down once."
        mc "I was thinking to myself about the times we used to share, like this, you know?"
        show sayori c115112
        "Sayori turns back to me."
        mc "I was thinking about what changed that stopped us from doing this, and I see now that it was me."
        show sayori 1be
        mc "I guess I started getting way to into video games and anime for my own good, and I didn't realize that it was destroying all the relationships that I had."
        show sayori 1bv
        "Sayori tearfully looks at me."
        mc "And... I'm sorry Sayori. I shouldn't have done this to you or-{nw}"
        "Sayori puts her finger in my lips."
        s "It's fine, [player]."
        s 1bt "I'm just glad that we finally got to spend some time together."
        s "Like we always did."
        "Sayori recoils her finger."
        #exp
        show sayori c114312
        mc "But I've still been a bad friend to you. I've been way too careless with what I say or do around you."
        #exps
        s c111352 "Oh come on [player], don't let me stop you from doing what you want to do with your life."
        mc "But I don't even know what I want to do with my life!"
        mc "I don't even know what I feel right now."
        s 1be "What do you mean?"
        mc "I don't know... I just feel like lately I've just made a lot of decisions that I hadn't completely thought things through."
        if hangout2 == "Natsuki":
            mc "Look I'm glad I got to spend more time with the others in the club, and I'm glad I got to know Natsuki very well, but maybe I should start spending some more time around you again."
            "Sayori shoots me a quizzical look."
            s 2be "I thought you and Natsuki liked each other though."
        elif hangout2 == "Yuri":
            mc "Look I'm glad I got to spend more time with the others in the club, and I'm glad I got to know Yuri very well, but maybe I should start spending some more time around you again."
            "Sayori shoots me a quizzical look."
            s 2be "I thought you and Yuri liked each other though."
        else:
            if encore_festivalquestion_2 == "Natsuki":
                mc "Look I'm glad I got to spend more time with the others in the club, and I'm glad I got to know Natsuki and Monika very well, but maybe I should start spending some more time around you again."
            else:
                mc "Look I'm glad I got to spend more time with the others in the club, and I'm glad I got to know Yuri and Monika very well, but maybe I should start spending some more time around you again."
            "Sayori shoots me a quizzical look."
            s 2be "I thought you and Monika liked each other though."
        mc "I mean we do.... but we're friends. I guess on occasion we just happen to get a little too friendly."
        show sayori 1bq
        "We both chuckle to ourselves."
        mc "But look... I guess what I'm trying to say is\: I missed you."
        "Sayori pauses and takes a moment to reflect on what I just said."
        s 1bv "[player]...I...missed you too..."
        "Sayori is completely flustered, her face as bright as her bow."
        "Suddenly, we realize how close we have gotten and we pull away from each other."
        s 1by "I...I wouldn't mind that [player]."
        "Unable to say anything more to each other, we turn our attention back to the TV, finishing the rest of the episode."
        show sayori at thide
        hide sayori
        pause 0.8
        scene bg living_room_afternoon with Dissolve(0.75)
        image sayori e2bx = evening("mod_assets/sprites/2bx.png")
        image sayori e1bq = evening("mod_assets/sprites/1bq.png")
        show sayori e2bx at t11
        s "Well that was fun [player]! I really hate that I have to go though."
        mc "Ha, yeah, it really was fun. I'll talk to you tomorrow?"
        s e1bq "Yeah... I'd like that."
        show sayori at thide
        hide sayori
        "She smiles sweetly before turning out the door and starts walking to her home."
        "I close the door and grab my bag and head up stairs to my room this had been a fun night."
    #Scene Transition
    #Bedroom Night Scene
    scene bg bedroom_night
    with wipeleft_scene
    "After grabbing Sayori's poems from the dining table, I put her stack right next to mine and Natsuki's."
    if encore_sayoriquestion_1 == True:
        if encore_festivalquestion_2 == "Natsuki":
            if hangout2 != "Natsuki":
                "I remembered that Natsuki's stack was noticeably slightly larger than mine."
                "After comparing all three stacks, I realize that Sayori's stack and my stack have the same number of poems, and Natsuki's stack is still slightly larger than ours."
                "I begin to look through Natsuki's stack."
                "I recognize all of the poems she wrote. I even remember the first one she wrote."
                "I always found joy in reading her poems. They're so simple, yet they're just as hard hitting as Monika's, Sayori's and Yuri's poems."
                "Not to mention I always found her word choice to be cute and adorable. It really does suit her, even if she won't admit it."
                "Through my train of thought, one of the pieces of paper escapes my grip."
                "I put the stack back on my desk and bend down to grab the paper."
                "I look at the title.... I don't remember reading this one..."
                $ lpoem = "Natsuki"
                call showpoem(poem_en1, music=False, track=None, revert_music=False) from _call_showpoem_1
            else:
                "Yeah...this ones has a lot of variations."
                pass
        elif encore_festivalquestion_2 == "Yuri":
            #put yuri's stuff here
            pass
    else:
        if encore_festivalquestion_2 == "Natsuki":
            if hangout2 == "Natsuki":
                "After comparing all three stacks, I realize that Natsuki's stack and my stack have the same number of poems, and Yuri's stack is still slightly larger than ours."
                "I begin to look through Yuri's stack."
                "I recognize all of the poems she wrote. I even remember the first one she wrote."
                "At first, it was a bit hard to understand the meaning of her poems, but the more I read, the more I understood them."
                "Yuri was always probably one of the club's deepest writers."
                "Her poems may look convoluted and confusing on the surface, but once you got past that, you got to realize that Yuri's poems were always meaningful and articulate."
                "I always found joy in reading her poems. They can always be as fun to read as Natsuki's, and just as deep as Sayori's and Monika's."
                "She truly is a talented writer. Heck, she might even be one of the best writers I've ever met! I have learned a lot from her, her advice really has helped me improve."
                "Through my train of thought, one of the pieces of paper escapes my grip."
                "I put the stack back on my desk and bend down to grab the paper."
                "I look at the title.... I don't remember reading this one..."
                $ lpoem = "Yuri"
                #yuri likes you poem
            else:
                "This has a lot of variations."
        else:
            if hangout2 == "Yuri":
                "After comparing all three stacks, I realize that Sayori's stack and my stack have the same number of poems, and Natsuki's stack is still slightly larger than ours."
                "I begin to look through Natsuki's stack."
                "I recognize all of the poems she wrote. I even remember the first one she wrote."
                "I always found joy in reading her poems. They're so simple, yet they're just as hard hitting as Monika's, Sayori's and Yuri's poems."
                "Not to mention I always found her word choice to be cute and adorable. It really does suit her, even if she won't admit it."
                "Through my train of thought, one of the pieces of paper escapes my grip."
                "I put the stack back on my desk and bend down to grab the paper."
                "I look at the title.... I don't remember reading this one..."
                $ lpoem = "Natsuki"
                call showpoem(poem_en1, music=False, track=None, revert_music=False) from _call_showpoem_2
    "..."
    "Oh...shit."
    "This is going to be much harder than I thought..."
    "Not to mention, she's probably going to find out sooner or later that I have it..."
    if encore_sayoriquestion_1:
        "And when she does... it's not going to end well for one of us..."
    elif not encore_sayoriquestion_1:
        if hangout2 == "Natsuki":
            "I feel like I'm at a crossroads here. I like Natsuki but I wouldn't want to let Yuri down..."
        elif hangout2 == "Yuri":
            "I feel like I'm at a crossroads here. I like Yuri but I wouldn't want to let Natsuki down..."
        elif hangout2 == "Monika":
            if encore_festivalquestion_2 == "Natsuki":
                "I feel like I'm at a crossroads here. I like Monika but I wouldn't want to let Natsuki down..."
            else:
                "I feel like I'm at a crossroads here. I like Monika but I wouldn't want to let Yuri down..."
        "And with how I'm feeling about Sayori now..."
        "One way or another... somebody is going to get hurt because of me."
    "Did she... give this to me on purpose?"
    if lpoem == "Natsuki":
        "I put the poem back in Natsuki's stack, put on my pajamas and lay on my bed."
    else:
        "I put the poem back in Yuri's stack, put on my pajamas and lay on my bed."
    "What am I going to do?"
    "Do I talk to her about it tomorrow?"
    if encore_sayoriquestion_1:
        "Do I tell Sayori?"
        "How will Sayori feel about this?"
    else:
        "Who do I even tell about this?"
    "Through the millions of scenarios that play out in my head, my mind eventually wears me down and I drift into an uneasy sleep..."

label void2_base:
    stop music fadeout 1.0
    scene bg sayori_void with Dissolve(1.0)
    $ m_name = "???"
    if hangout2 == "Monika":
        jump void2_m
    else:
        pass
    m "You wouldn’t have been in this situation if you just avoided them!"
    "Oh no… not this again…"
    m "You never listen do you?"
    if hangout1 != hangout2:
        if hangout1 == "Monika":
            $ difficult_line = False
            m "WHAT ARE YOU DOING?!?"
            m "Just when I thought everything was going right..."
            m "You switch to [hangout2]!"
            m "Why are making this needlessly difficult for us?"
        else:
            $ difficult_line = True
            m "When I told you to stay away from [hangout1]..."
            m "I didn't mean switch to [hangout2]!"
        
            if hangout1 == "Sayori" and hangout2 == "Natsuki":
                m "And you still somehow ended up making things worse for us by still sticking by with Sayori."
                m "Well... at least you managed to damage some of her trust in you."
                m "But thanks to your bumbling efforts, you have more or less restored that trust! You need to stay away from her like you did today!"
                m "You really are making this needlessly difficult for us, aren't you?"
                m "Let me help clarify something for you, [player]."
            #elif hangout1 == "Sayori" and hangout2 == "Yuri": # Nothing Different            
            #elif hangout1 == "Natsuki" and hangout2 == "Sayori": # Nothing Different            
            elif hangout1 == "Natsuki" and hangout2 == "Yuri":
                m "And I don't appreciate you getting close to Sayori like that!"
                m "Well... at least you managed to damage some of Natsuki's trust in you."            
                m "But you really are making this needlessly difficult for us, aren't you?"
                $ difficult_line = False
            # elif hangout1 == "Yuri" and hangout2 == "Sayori": # Nothing Different            
            elif hangout1 == "Yuri" and hangout2 == "Natsuki":
                m "And I don't appreciate you getting close to Sayori like that!"
            
        
        if difficult_line: # Any variation which doesn't use this line uses its own version of it.
            m "You really are making this needlessly difficult for us, aren't you?"
            
        m "Let me help clarify something for you, [player]." # All variations converge here.
    else:    
        m "You should’ve saved yourself for me…"
        m "Let them suffer.."
        m "Let them die…"
    "Suddenly I see a silhouette approach me."
    jump void2_p1

label void2_p1:
    $ hangout2 = "Natsuki"
    #the song "e1 (The Void)" is a song that has a jumpy opening like Sayonara
    #so it's probably best used JUST as something scary happens
    if hangout2 == "Sayori":
        "The figure comes into my view...{w=0.68}{nw}"
        show sayori silhouette at t11
        "The figure comes into my view...{fast}it's Sayori."
        m "Sayori can never love you the same way I do."
        m "She's not worth your time..."
        m "You can't spend everyday with her."
        m "Leave her."
        m "Forget about Sayori."
        m "Forget about Natsuki."
        m "There's just us."
        m "There is only us."
        hide sayori
        show image "mod_assets/cgs/sayori_cg3.png" with dissolve_cg
        "Suddenly, I see a rope appear around Sayori's neck"
        "Her body is levitated into the air."
        show image "mod_assets/cgs/sayori_cg3_struggle.png" with dissolve_cg
        "She struggles to break herself free."
        "She viciously claws at the rope, but only ends up cutting her fingers, loosening her grip on the rope."
        "I try to call out Sayori's name, but nothing comes out of me..."
        "I try to run to her to help her, but I can not move..."
        "No..."
        "NO!"
        "I won't let her die!"
        "I can't let her die!"
        "Not like this...."
        "As I watch Sayori struggle and gasp for air, the voice continues it's merciless chant, only growing louder with every word it utters."
        m "Leave her."
        m "Forget her"
        m "Let her die."
        m "There is only us..."
        m "LEAVE HER...."
        "What seems like an eternity of torture, Sayori eventually stops struggling and goes limp."
        scene bg sayori_void
        show sayori gone at face
        play sound "mod_assets/Neck_Break.ogg"
        stop music
        m "FORGET HER!!!!!!!!!!!!!!!!!!!!!!!!!!"
        "The voice echoes loudly inside my head."
        "As if I suddenly developed eagle vision, this hellish dream suddenly focuses upon Sayori's now gazeless eyes."
        "They're bloodshot red and blank..."
        "I feel like I'm going to throw up..."
    elif hangout2 == "Yuri":
        "The figure comes into my view...{w=68}{nw}"
        show yuri silhouette at t11 zorder 3
        "The figure comes into my view...it's Yuri."
        m "Yuri can never love you the same way I do."
        m "She's not worth your time..."
        m "You can't spend everyday with her."
        m "Leave her."
        m "Forget about Yuri."
        m "Forget about Natsuki."
        m "Forget about Sayori."
        m "There's just us."
        m "There is only us."
        show monika stabby at t44 zorder 2
        "I see a shadowy figure appear right next to Yuri."
        "The figure is wielding a knife in its hand."
        m "Let's get to the point, shall we?"
        show monika stabby at t54
        pause 0.3
        play sound "mod_assets/stab.ogg"
        "The figure thrusts the knife into Yuri's shoulder."
        show yuri silhouette at sink2
        show monika bloodystabby at t44
        "Yuri lets out a painful scream as her knees buckles onto the ground."
        "I try to call out Yuri's name, but nothing comes out of me..."
        "I try to run to her to help her, but I can't move..."
        show yuri silhouette at levitate
        "The figure raises it's free arm, levitating Yuri off the ground."
        "Yuri is hyperventilating and screaming."
        "No..."
        "NO!"
        "I won't let her die!"
        "I can't let her die!"
        "Not like this...."
        show monika bloodystabby at t54 zorder 4
        show yuri silhouettebloody
        "The figure takes a wild swipe across Yuri's chest."
        "Yuri lets out another cry of pain."
        m "Don't worry, [player]."
        m "She's enjoying this."
        m "She does this thing all the time while thinking of you..."
        m "Here let me prove it."
        show monika s at t44
        show yuri silhouettebloody at s11
        "The figure drops the knife and lowers Yuri onto the floor."
        "Yuri is clutching her chest with one hand, but scoops up the knife with her other hand."
        "Come on, Yuri... please use it on that monster."
        show monika s3 at t44
        stop music
        "The figure snaps it's fingers."
        show yuri stabhouette0
        pause 1.43
        play sound "mod_assets/stab.ogg"
        show yuri stabhouette1
        show blood:
            pos (610,485)
        pause 0.25
        "Yuri looks me dead in the eye as she stabs herself..."
        "I see blood pour of Yuri's mouth like a waterfall..."
        "She gasps as I see the light from her eyes flicker."
        show yuri stabhouette1:
            2.55
            easeout_cubic 0.7 yoffset 600
        pause 1.85
        hide blood
        pause 0.25
        play sound fall
        hide yuri
        m "Leave her."
        m "Forget her."
        m "Let her die."
        m "There is only us..."
        m "LEAVE HER...."
        stop music
        m "FORGET HER!!!!!!!!!!!!!!!!!!!!!!!!!!"
        "The voice echoes loudly inside my head."
        hide monika
        show image "mod_assets/cgs/yuri_v4.png":
            subpixel True
            linear 20 zoom 1.5 xcenter 0.3 ycenter 0.3
        "I try to look away but this hellish dream forces my eyes upon Yuri's now gazeless corpse."
        "They're bloodshot red and blank..."
        "I feel like I'm going to throw up..."
        scene black
    else:
        m "You wouldn’t have been in this situation if you just avoided them!"
        "Oh no... not this again..."
        m "You never listen do you?"
        m "You should’ve saved yourself for me..."
        m "Let them suffer.."
        m "Let them die..."
        #(Show Natsuki Silhoute)
        show natsuki silhouette at t11
        "Suddenly I see a silhouette approach me."
        #(Natsuki sprite comes into view)
        show natsuki 1m at t11 zorder 3 with dissolve_cg
        "The figure comes into my view... it’s Natsuki."
        m "Natsuki can never love you the same way I do."
        m "She’s not worth your time..."
        m "You can’t spend everyday with her."
        m "Leave her."
        m "Forget about Natsuki."
        m "Forget about Yuri."
        m "Forget about Sayori."
        m "There’s just us."
        m "There is only us."
        #(Show Monika "Snap" sprite)
        show monika s at t33 zorder 2
        "I see a shadowy figure appear right next to Natsuki."
        #(Rotate Natsuki's head to the right) (Natsuki Screaming) (Use neck break sound effect)
        play sound neck_break
        show natsuki breakneck at n_struggle
        show monika s3 at t33 zorder 2
        "It raises its arm and Natsuki’s neck suddenly jerks to the right at a painful 45 degree angle."
        "I hear Natsuki cry out in pain as she struggles to move her neck back."
        "I try to call out Natsuki’s name, but nothing comes out of me..."
        "I try to run to her to help her, but I can’t move..."
        "No..."
        "NO!"
        "I won’t let her die!"
        "I can’t let her die!"
        "Not like this...."
        show natsuki breakneck2 at t11 zorder 3
        play sound neck_break
        "The figure raises it’s arm a little higher, which makes Natsuki’s neck bend ever further to the right."
        "No matter how hard she struggles, she can’t move her neck back into place."
        show monika s at t33 zorder 2
        m "She was born to suffer, [player]."
        m "You can’t save her, and the longer you keep her alive, the more she will suffer."
        m "Leave her."
        m "Forget her"
        m "Let her die."
        m "There is only us..."
        m "LEAVE HER...."
        show natsuki breakneck3 at t11 zorder 3
        play sound neck_break
        "The figure snaps it’s fingers."
        #Natsuki’s neck breaks (Show dead Natsuki sprite) (Use neck break sound effect)
        #Natsuki falls to the floor. (Sink Natsuki Corpse)
        show natsuki dead:
            2.55
            easeout_cubic 0.7 yoffset 600
        pause 3.3
        play sound fall
        hide natsuki
        "N-no..."
        "She can’t be..."
        "Natsuki is no longer moving or making any sound."
        m "FORGET HER!!!!!!!!!!!!!!!!!!!!!!!!!!"
        show monika at thide
        hide monika
        "The voice echoes loudly inside my head."
        #(Zoom in on Natsuki's Corpse)
        show natsuki dead:
            subpixel True xcenter 640 yanchor 1.0 ypos 0.90 yoffset 500 zoom 1.70
        "I try to look away but this hellish dream forces my eyes upon Natsuki’s now gazeless corpse."
        "They’re bloodshot red and blank..."
        "I feel like I’m going to throw up...."
        "The figure comes into my view... it's Natsuki."
        m "Natsuki can never love you the same way I do."
        m "She's not worth your time..."
        m "You can't spend everyday with her."
        m "Leave her."
        m "Forget about Natsuki."
        m "Forget about Yuri."
        m "Forget about Sayori."
        m "There's just us."
        m "There is only us."
        "I see a shadowy figure appear right next to Natsuki."
        "It raises its arm and Natsuki's neck suddenly jerks to the right at a painful 75 degree angle."
        "I hear Natsuki cry out in pain as she struggles to move her neck back."
        "I try to call out Natsuki's name, but nothing comes out of me..."
        "I try to run to her to help her, but I can't move..."
        "No..."
        "NO!"
        "I won't let her die!"
        "I can't let her die!"
        "Not like this...."
        "The figure raises it's arm a little higher, which makes Natsuki's neck bend further to the right."
        "No matter how hard she struggles, she can't move her neck back into place."
        m "She was born to suffer, [player]."
        m "You can't save her, and the longer you keep her alive, the more she will suffer."
        m "Leave her."
        m "Forget her"
        m "Let her die."
        m "There is only us..."
        m "LEAVE HER...."
        "The figure snaps it's fingers."
        #*Natsuki's neck breaks*
        #*Natsuki falls to the floor.*
        "N-no..."
        "She can't be..."
        "Natsuki is no longer moving or making any sound."
        stop music
        m "FORGET HER!!!!!!!!!!!!!!!!!!!!!!!!!!"
        "The voice echoes loudly inside my head."
        "I try to look away but this hellish dream forces my eyes upon Natsuki's now gazeless corpse."
        "They're bloodshot red and blank..."
        "I feel like I'm going to throw up..."
    $ m_name = "Monika"
    jump day3_start
label void2_m:
    play music m1 fadein 2.0
    m "This is great!"
    m "Everything is coming along well so far."
    if encore_festivalquestion_2 == "Yuri":
        m "Well, everything besides that cut slut's little love letter..."
    else:
        m "Well, everything besides that damn toothpick’s little love letter…"
    m "And I don’t appreciate you getting so close to that walking clutz either."
    if hangout1 == "Yuri":
        m "Honestly, if she could disappear, that'd be great. She's useless!"
    else:
        m "Honestly, she’s dumb to be the real life hangman…"
        
    m "But I know you aren’t stupid enough to mess up all our progress for those losers."
    m "Hahaha..."
    m "Ahem."
    m "Sorry I just lose myself in my..."
    m "Excitement."
    m "Mmmmh... I can’t wait for tomorrow."
    m "Just keep spending time with me and I’ll be all yours in no time."
    m "Until next time..."
    m "....My love...."
    stop music fadeout 2
    jump day3_start


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

label affectionasignment:
    $ n_modappealstored = n_modappealstored + n_modappeal
    $ s_modappealstored = s_modappealstored + s_modappeal
    $ y_modappealstored = y_modappealstored + y_modappeal
    $ m_modappealstored = m_modappealstored + m_modappeal
    $ n_modappeal = 0
    $ s_modappeal = 0
    $ y_modappeal = 0
    $ m_modappeal = 0
