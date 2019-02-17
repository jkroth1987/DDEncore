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
    stop music fadeout 2.0
    jump day3_start
    