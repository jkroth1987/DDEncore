label sencore_1:
    $ hangout1 = "Sayori"
    "I first go to Sayori..."
    scene bg club_day
    with wipeleft_scene
    play music tsayori
    mc "Hey, Sayori!"
    show sayori 2x at t11 zorder 1
    s "Oh, hey, [player]!"
    "Sayori puts on her usual cheerful grin, but something about it just seems...off..."
    mc "What's up?"
    "I take a seat right next to her."
    s 1y "Oh, same old."
    "She smiles sadly at me."
    mc "Sayori..."
    "I gently place my hand on her shoulder."
    mc "You know that if anything's bothering you, you can talk to me. I'm here for you, Sayori."
    "I can hear Sayori start to sniffle."
    s 1u "I... I know... [player]....."
    if encore_sayoriquestion_1 == True:
        "I pat Sayori's shoulder as she struggles to compose herself."
        "A few minutes pass before Sayori stops sniffling."
        stop music fadeout 3.0
        mc "Hey, Sayori?"
        "Sayori curiously looks up at me."
        s 1v "Y-yeah?"
        mc "If you don't mind me asking... how long have you been like this?"
        s "What do you mean?"
        mc "It's just that... I've known you for as long as I can remember..."
        play music t10 fadein 3.0
        mc "I always saw you as someone who was always happy, bubbly, sometimes clumsy, but overall, just someone who's a big ball of sunshine."
        mc "I never would've thought that in a million years that you would've ever been going through something like this."
        #normally average sprite for Sayori
        "Sayori pauses, as if to reflect on what I just said."
        s 1v "I mean... I always had it..."
        s 1k "But it got really bad when high school started, and it’s only gotten worse, especially recently."
        s 3k "I guess with the stress of all the exams, schoolwork, drama and other things..."
        s 3l "Like my parents divorce..."
        s 1t "And just missing out on spending time with you..."
        "I feel my heart deflate as I hear this."
        "I never thought that me spending less time with Sayori over the years would have that kind of effect on her."
        if encore_sayoriquestion_1 == True:
            "And rejecting her confession probably didn’t help matters."
            "God, I feel so stupid!"
        else:
            "I feel so stupid!"
        s 2t "I guess it just finally took enough of a toll on me to the point where I realized I had this."
        s 1k "But my entire life...{w} I've always felt that everyone would be better off as if I didn't exist."
        s "No matter how hard I'd try to give people my happiness, my time and my energy."
        s "Just... nothing ever felt like it was worth it and that they didn't need me to be happy."
        s 1u "And If I ever opened up about how I really felt on the inside, that people would spend all their time trying to make me happy."
        s "I'd just be a weight on their shoulders. They have too much to do and I don't want to add on to their stress."
        s 1v "That's what I thought when we kind of drifted apart when high school started."
        s "You had too much on your plate and me being around you would be too distracting for you, so I would always have to muster up the courage to even try to talk to you."
        "I feel an overwhelming sense of guilt overtake me."
        show sayori 1v at h11 zorder 1
        mc "Sayori!"
        "I hold both of her hands tightly and look into her eyes."
        mc "I'm... i'm so sorry...."
        s 1t "You have nothing to apologize for, [player]."
        mc "I do! If I'd just put you before my hobbies, maybe you wouldn't be like this so much."
        mc "I promise you, Sayori. I'm going to make this up to you starting right now."
        "I see Sayori’s tears return as they drip onto her cheek."
        s "Don't feel guilty for the way I feel [player]."
        s 1w "I’m sorry I got you so worried about me… I didn’t mean to take away from Natsuki or anything like that!"
        if encore_sayoriquestion_1 == True:
            s "I’m a terrible girlfriend!"
        else:
            s "I'm a terrible friend!"
        mc "No, you aren't Sayori. Don't say that."
        stop music fadeout 3.5
        scene black
        with Dissolve(1)
        "Sayori hugs me tightly."
        "I put my arms around her and close my eyes."
        "I can feel my heart beat in sync with Sayori’s."
        "I feel the warmth of her body radiate onto mine."
        "As emotional as we both are right now… this is nice."
        "We're like this for sometime before I here some commotion come from the closet."
        scene bg club_day
    else:
        "We're like this for sometime before I here some commotion come from the closet."
    stop music
    show sayori 1m at t11 zorder 1
    n "DAMN IT, MONIKA!!!!"
    play music t3
    "Monika and Yuri giggle before going back to their respective activities."
    "Sayori and I turn to each other, both shooting each other a concerned look over what just happened."
    mc "I'm going to check on Natsuki."
    show sayori 3t at t11 zorder 1
    "Sayori wipes a tear and gives me an approving nod."
    "I get up and carefully approach the closet..."
    scene black
    with wipeleft_scene
    pause 0.8


    play music t6 fadein 3.0
    #if y_modappeal == 1 and n_modappeal == 0:
    scene bg closet
    with wipeleft_scene
    "I hear Natsuki rummaging around in the closet "
    mc "Natsuki?"
    "I ask ever so cautiously and as softly as I humanly can."
    show natsuki 5f at t11 zorder 1
    "Natsuki turns towards me, I can see the fire in her eyes"
    n 5e "WHAT?!?!"
    "The frustration in her voice takes me off guard."
    "I need to calm her down before this gets out of hand."
    mc "Hey.. hey... I just wanted to see what's been going on, that's all."
    show natsuki 5g at t11 zorder 1
    "Natsuki seems to calm down a little upon hearing this."
    n 5e "Ugh, I can't find my volume 12 of Parfait Girls set! Everything's been moved around again!"
    mc "Do you want me to help you?"
    "Natsuki seems to be slightly offended at my suggestion."
    n 5f "No! I got it all under control! I don't need your help."
    n 5u "Idiot..."
    "Her voice trails off."
    mc "You sure?"
    n 4v "Yes! I'm not a kid, I can handle myself, you know!"
    "I'm reminded of the time we spent last Sunday and how she managed to carry all those cooking supplies from her house to mine."
    "Maybe she can handle this by herself..."
    show natsuki 5g at t11 zorder 1
    mc "Suit yourself."
    show natsuki at thide
    hide natsuki
    scene bg club_day
    with wipeleft_scene
    "As I head back towards the front of the room, I can hear Natsuki's exasperated sighs, followed by more of her yelling."
    n "Baka!"
    "What? I'll never get around to understanding Natsuki's weird logic..."
    "While walking out from the closet I'm abruptly stopped by Yuri."
    show yuri 3y5 at t11 zorder 1
    "I noticed that she seems a lot more confident than normal."
    "She seems unusually excited to talk to me, as if she’s been waiting for this chance."
    "It’s very different from how she is normally..."
    mc "Oh, hey Yuri! What's up?"
    y "Hey [player]! How are you doing this afternoon?"
    mc "Oh, I'm doing alright, what about you?"
    y 3b "I'm doing great! I just got done finishing this chapter in my book and I was wondering if you'd like to...."
    y 4c "Maybe read it together sometime...."
    "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
    "I guess it's up to me reassure her."
    mc "Yeah, sure! I'd love to do some reading with you!"
    y 3y1 "Right now?!"
    "Her voice rings with excitement."
    "Woah, where did this excitement come from, Yuri?"
    mc "Um... I don't know if we have the time for right now but maybe tomorrow we-"
    y 1y4 "But you're not doing anything right now, are you?"
    "Well, she does have a point there...."
    "But I must admit it's a surprise to see her being this forward."
    "And, I really feel like I should get back to Sayori..."
    "My thoughts are quickly interrupted by Monika calling the group."
    show yuri at t22
    show monika u222111 at l21
    m "Ok everyone, poem time!"
    show monika u111131
    show yuri 1y7
    "Yuri quickly gives Monika an agitated look but swiftly heads back to her desk to retrieve her poem, and everyone follows."
    "As I’m getting my poem I curiously look off in Yuri’s direction, who is avoiding making eye contact with anyone."
    "I guess it takes a lot for Yuri to talk to someone, she really isn’t one for social interactions. She must have really wanted to talk to me considering we really haven’t gotten the chance to really talk with each other in a meaningful way."
    "Oh well, I’m sure we’ll get the chance sooner or later."
    #if n_modappeal == 1 and y_modappeal == 0:
        #"As I'm walking approaching the closest however, Yuri walks up to me."
        #show yuri 3y5 at t11 zorder 1
        #"I noticed that she seems a lot more confident than normal."
        #"It's very different from her shy and reserved persona."
        #mc "Oh, hey Yuri! What's up?"
        #y "Hey [player]! How are you doing this afternoon?"
        #mc "Oh, I'm doing alright, what about you?"
        #y 3b "I'm doing great! I just got done finishing this chapter in my book and I was wondering if you'd like to...."
        #y 5c "maybe read it together sometime...."
        #"Her confident facade falls apart. She's no longer meeting my eyes."
        #"I guess it's up to me reassure her."
        #mc "Yeah, sure! I'd love to do some reading with you!"
        #y 3y1 "Right now?!"
        #"Her voice rings with excitement."
        #"Woah, where did this excitement come from, Yuri?"
        #mc "Um... I don't know if we have the time for right now but maybe tomorrow we-"
        #y 1y4 "But you're not doing anything right now, are you?"
        #"Well, she does have a point there...."
        #"Plus I must admit it's a surprise to see her being this forward."
        #"But, I really feel like I should get back to seeing what's bother Natsuki..."
        #mc "Sorry, but I've really got to go see what's bothering Natsuki..."
        #show yuri 3b at t11 zorder 1
        #mc "Another time maybe?"
        #y 3w "It-it's fine [player]."
        #y 5b "I won't take up anymore of your time."
        #show yuri at thide
        #hide yuri
        #"I see Yuri's face turn bright red as she swiftly and turns around and heads back to her desk."
        #scene bg closet
        #with wipeleft_scene
        #"I hear Natsuki rummaging around in the closet "
        #mc "Natsuki?"
        #"I ask ever so cautiously and as softly as I humanly can."
        #show natsuki 4f at t11 zorder 1
        #"Natsuki turns towards me, I can see the fire in her eyes"
        #n 5e "WHAT?!?!"
        #"The frustration in her voice takes me off guard."
        #"I need to calm her down before this gets out of hand."
        #mc "Hey.. hey... I just wanted to see what's been going on, that's all."
        #show natsuki 5i at t11 zorder 1
        #"Natsuki seems to calm down a little upon hearing this."
        #n 5h "Ugh, I can't find my volume 12 of Parfait Girls set! Everything's been moved around again!"
        #mc "Do you want me to help you?"
        #"Natsuki seems to be slightly offended at my suggestion."
        #n 4h "No! I got it all under control! I don't need your help..."
        #n 5i "Idiot..."
        #"Her voice trails off."
        #mc "You sure?"
        #n 4v "Y-{w=0.18}Yes! I'm not a kid, I can handle myself, you know!"
        #"I'm reminded of the time we spent last Sunday and how she managed to carry all those cooking supplies from her house to mine."
        #"Maybe she can handle this by herself..."
        #show natsuki 5g at t11 zorder 1
        #mc "Suit yourself."
        #show natsuki at thide
        #hide natsuki
        #"As I head back towards the front of the room, I can hear Natsuki's exasperated sighs, followed by more of her yelling."
        #n "Idiot!"
        #"What? I'll never get around to understanding Natsuki's weird logic..."
        #"My train of thought is interrupted by Monika calling us to attention."
        #show monika 2b at t11 zorder 1
        #m "Ok everyone, poem time!"
        #call groupAll(2, 0, 0, 2, 1) from _call_groupAll_3
        #show monika 2b at t21 zorder 2
        #show natsuki 5e at t22 zorder 1
        #n "Ugh! Do we really need to do this now? I'm looking for something!"
        #m 1l "Sorry, Natsuki! I just wanted to make sure we have enough time to share!"
        #"Natsuki shoots Monika an irritated look."
        #n 5h "Alright, fine!"
        #call groupClear() from _call_groupClear_3
        #show monika at thide
        #hide monika
        #show natsuki 5g at t11 zorder 1
        #"Natsuki quickly glances back at the closest."
        #"I see the irritation from Natsuki's face is fade away as she  dejectedly looks at the floor and starts slowly walking to retrieve her poem."
        #mc "Hey, Natsuki."
        #"Natsuki turns to me, her face red and eyes glossy as if she was fighting back tears."
        #n 1n "Y-{w=0.18}Yeah?"
        #mc "I'm sure you'll find it sooner or later. I know it means alot to to you that you find that copy. Trust me I'd lose my stuff to if I lost something that was important to me."
        #show natsuki 5s at t11 zorder 1
        #"Natsuki struggles to maintain eye contact with me for longer than a few seconds."
        #mc "I know how you feel and I just wanted to let you know that my offer to help you still stands"
        #"Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
        #n 4s "T-thanks [player]."
        #mc "Hey, no problem. I hate seeing you get so worked up like this. I like seeing you happy."
        #"Natsuki stares off into space, as if to process what I just said."
        #mc "You alright, Natsuki?"
        #"Natsuki returns to reality."
        #n 5h "I'm fine! Let's just get this over with."
        #show natsuki at thide
        #hide natsuki
        #"Natsuki hurries off to the back of the room to retrieve her poem."
        #"I quietly sigh to myself as I walk over to retrieve my poem."
        #"It's always been hard for me to get a good read on Natsuki."
        #"Sometimes I don't know whether she acts that way on purpose..."
        #"...Or that she has an ulterior motive for trying to act that way."
        #"..."
    jump day1_poemsharing
label sencore_1b:
    play music e4
    "During the walk home, I see Sayori look towards me every few minutes or so."
    show sayori 1k at t11 zorder 1
    "I guess she wants to tell me something, and since we're about at my house, I'd better ask her about it now."
    mc "Sayori?"
    show sayori 4m at h11 zorder 1
    s "H-huh? What is it, [player]?"
    mc "You have something on your mind?"
    s 3l "Well... I was just wondering if you wanted to hangout today?"
    mc "Yeah! I'd love to!"
    s 4r "Yay!"
    "She beams, seemingly full of excitement."
    s 3x "I’ll meet you at your place once we head back. I want to drop off all my stuff."
    mc "Sure! No problem, Sayori!"
    show sayori 1q at t11 zorder 1
    "I notice that she gently holds my hand on the way back."
    "Upon noticing it, I look to her."
    show sayori 1y at t11 zorder 1
    "I feel a small smile, slowly spreading across my face."
    "I notice that she's too flustered to make eye contact with me."
    show sayori at thide
    hide sayori
    "We make the rest of the walk back in silence."
    "Eventually we make it back to her place."
    show sayori 1x at t11 zorder 1
    s "Hey, [player], I'll see you in a bit, okay?"
    mc "Alright, Sayori."
    show sayori 1y
    "We slowly embrace each other, but we quickly let go of each other as Sayori enters her house and I walk further down the street back to my house."
    stop music fadeout 2.0
    scene bg living_room
    with wipeleft_scene
    "After dropping off all my school stuff and changing out of my uniform, I head downstairs to wait for Sayori."
    "A few minutes later, I hear a knock on my door."
    mc "Come in!"
    show sayori 1ba at t11 zorder 1
    "Sayori enters my house."
    "She's wearing her casual clothes, and while I have seen them before, I can’t help but notice how beautiful she looks."
    play music t6 fadein 2.0
    s 2bx "Hey, [player]!"
    mc "Hey, Sayori!"
    "I motion for her to join me on the couch."
    show sayori 1ba at s11 zorder 1
    "As she joins me, once again, we get lost looking into each others eyes."
    show sayori 1bd
    "Though, just that alone is enough to fill me with a craving to hold her in my arms."
    show sayori at thide
    hide sayori
    "Sayori rests her head on my shoulder. Instinctively, I wrap my arm around her."
    "The smell of cinnamon emanating from her hair is very apparent. I can't help but sniff a little."
    mc "Geez... you're a little cinnamon bun, aren't you?"
    show sayori 1by at t11 zorder 1
    "Sayori giggles and blushes at my compliment."
    s 1bs "You're so good to me, [player], you know that?"
    mc "I try. Remember what I promised."
    mc "I promised you that I’d be by your side, that I’d care for you no matter what. That I’d be with you no matter what you’re feeling."
    show sayori 1be at s11 zorder 1
    "Sayori wraps her arms around me, burying her face into my chest."
    stop music fadeout 3.0
    s "You really do care about me, don't you, [player]? "
    mc "Of course I do! I'll do anything to make sure you're happy."
    "I can feel that Sayori is trembling"
    s 1bk "Do I.... really deserve any of this?"
    mc "Deserve what?"
    play music t9 fadein 3.0
    s 1bu "Your affection... your care for me."
    mc "Sayori, of course you do. You're the best thing that's ever happened to me. You're literally the spark that keeps me going, and everyday I wake up looking forward to spending time with you."
    "I feel Sayori's tears soaking into my shirt."
    s 1bt "[player], I.... I... lo-"
    mc "You don't need to strain yourself, Sayori. It's ok, don't force yourself."
    "Sayori holds me tighter."
    show sayori 1bv at t11 zorder 1
    "After some time passes, Sayori releases her grip. I can't help but get lost in those eyes..."
    "Those breathtaking sky blue eyes of hers."
    "Eventually, she brings me back to reality."
    s 2bd "So... got anything planned for us today?"
    mc "Not really... want to see what's on TV?"
    s 1bq "Sounds good to me!"
    show sayori at thide
    hide sayori
    "Turning on the TV, we spend many hours flipping through the channels watching various game shows, anime, sitcoms and whatever is passable enough to be on TV nowadays."
    scene bg living_room_afternoon
    with dissolve_long
    show sayori 1ba at t11 zorder 1
    "Eventually the sun begins to set."
    s 1bd "Well, I guess that's my cue to head out."
    mc "Yeah, guess so, I'll walk you back."
    "The two of us head outside, and back to Sayori's."
    scene bg house
    with wipeleft_scene
    show sayori 1bq at t11 zorder 1
    s "Hey, thanks for everything today! I had fun!"
    mc "Glad you did Sayori! I'll see you tomorrow!"
    s 1br "Try not to oversleep this time, [player]."
    mc "I'll try my best."
    "With that, we hug each other and she heads inside her house while I walk back to mine."
    jump day1_bedroom

label sencore_2:
    $ hangout2 = "Sayori"
    "I decided to see what Sayori is up to."
    scene bg club_day with wipeleft_scene
    "I place my stuff down on a desk across from us and sit next to her."
    mc "Hey, Sayori!"
    show sayori 1a at t11 zorder 1
    s "Oh, hey [player]!"
    "She sounds a bit surprised, as if she wasn't expecting me to spend more time with her."
    mc "How are things?"
    s 1c "I guess things are little better now, I've set up an appointment with my doctor this Saturday to talk about how I can fight my depression."
    show sayori 1b
    "I feel a sense of relief course through my body. Any good news regarding Sayori's depression is a good thing."
    "I'm even more impressed that she's taking the initiative to face this head on, especially so soon."
    mc "Do you...want me to come with you to the doctors?"
    s 3l "Nah, it's okay. I think this is something I can manage on my own for right now."
    show sayori 1k
    "She says that with a little shakiness in her voice."
    stop music fadeout 1.0
    "She then suddenly pulls me into a side embrace."
    show sayori u115313 at f11
    "It was a surprise to be sure, but I quickly reciprocate."
    s 1t "But if I ever need anything...you'll be the first to know...okay?"
    s u113313 "Promise me that you'll always be there for me, [player]."
    mc "I promise you, Sayori."
    show sayori 1v
    play music t9 fadein 1.0
    mc "I promised you that I'll be there for you for the rest of our lives, and I intend to keep that promise."
    show sayori u116352 at t11
    "Sayori pulls away and I can see her trying to fight back tears."
    "I put my hand on her cheek."
    mc "Hey...hey...it's okay."
    show sayori 1v
    mc "You're incredibly strong for doing this all on your own, and I couldn't be more proud of you Sayori."
    show sayori u111352
    "I see a mixture of emotions on Sayori's face, as if she's trying to fight back tears while trying not to blush like an idiot."
    "But she's my idiot."
    "She's my Sayori."
    "And... I love her."
    "I just wished I had the courage to tell her that..."
    play sound "sfx/fall.ogg"
    scene black
    "She lays her head on my shoulder and holds my hand."
    "I lay my head on top of hers, and wrap my other arm around her."
    "The smell of cinnamon penetrates my nostrils with every breath I take."
    "Never in a million years would I ever thought that I would've found someone like her."
    "Speaking of finding..."
    "There's no way the others haven't noticed us."
    stop music fadeout 1.0
    scene bg club_day
    with open_eyes
    "I briefly look around the room."
    show yuri 1g at t11 zorder 2
    "Yuri still seems to be into her book,{w=0.8}{nw}"
    show yuri at t33
    show monika 1c at t32 zorder 3
    "Yuri still seems to be into her book,{fast} Monika seems to be typing on the teacher's computer,{w=0.8}{nw}"
    show monika at t31
    show yuri at t32
    show natsuki 5a at t33 zorder 1
    "Yuri still seems to be into her book, Monika seems to be typing on the teacher's computer,{fast} and Natsuki is in her usual spot under the windowsill reading her manga."
    "There's no way that they haven't at least looked up once and saw us like this, or overheard what we were saying, since we weren't really being that quiet to begin with."
    "Suddenly, Monika stands up and walks to the front of the room."
    play music t5 fadein 1.0
    show monika 1b at t21 zorder 3
    show natsuki 4k at t22 zorder 1
    show yuri at thide
    hide yuri
    m "Okay, everyone! Gather around! I have an important announcement to make!"
    show monika 1c
    show natsuki 2g
    "Suddenly, Monika and Natsuki's eyes turn to me and Sayori."
    show yuri 3n at t33 zorder 2
    show monika at t32
    show natsuki at t31
    "Yuri, confused as to what's going on, turns around..."
    show yuri u125111
    "Only to see what Monika and Natsuki are staring at."
    "Thankfully, Sayori dozed off while we were like this, otherwise she'd be incredibly embarrassed."
    show monika 1h
    show natsuki 5g
    show yuri u123114
    "All 3 girls are looking at us, with a bit of an irritated...almost jealous...expression on their faces."
    "God Damn It."
    "Well, it's up to me to attempt to salvage this situation."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    mc "Hey...Sayori.."
    "I subtly nudge her."
    "She raises her head to look at me."
    mc "Wake up dummy."
    show sayori 1p at t11 zorder 1
    s "Waaaah... 5 more minutes like this... please?"
    show sayori at thide
    hide sayori
    play sound "sfx/fall.ogg"
    "Sayori puts her head back on my shoulders."
    "Fuck."
    show monika 1l at t32 zorder 3
    show natsuki xu2131 at t31 zorder 1
    show yuri 2i at t33 zorder 2
    "I look to all three of the girls, who can't help but at least crack a grin at the situation I'm in."
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    mc "Monika has an announcement to make. Come on, let's not make her wait."
    s "Okay..."
    show sayori 1q at h11 zorder 1
    "Sayori stands up and stretches..."
    show sayori 1n
    pause 0.8
    show monika 2c at t42 zorder 4
    show sayori 1e at t44
    show yuri u125111 at t43 zorder 3
    show natsuki xu2131 at t41 zorder 2
    "But she quickly sees the situation we're in."
    "Immediately Sayori's face matches her bow."
    "Oh Sayori, always putting us in these awkward situations."
    s u122322 "Oh... s-sorry guys! I was just..."
    show monika 1l
    show natsuki 5z
    show yuri 2c
    "Natsuki, Monika and Yuri all try to contain their laughter."
    "Finally, Monika is able to compose herself."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show monika 1k at t21 zorder 2
    show sayori at t22
    m "It's alright, Sayori, come on."
    "She gestures for us to come toward the front of the room."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    if encore_festivalquestion_2 == "Natsuki":
        show natsuki 4g at t11 zorder 1
        "While on my way to the front of the room,{w=0.4}{nw}"
        $ _history_list.pop()
        play sound "sfx/smack.ogg"
        "While on the way to the front of the room,{fast} Natsuki gives me a \"friendly\" punch in the arm."
        mc "Ouch! Hey what was that for?"
        n 5s "N-Nothing...dummy..."
        "She mutters that softly and avoids eye contact as she briskly walks past me."
        show natsuki at thide
        hide natsuki
        "Well, that was random."
        "I just hope she isn't jealous of me and Sayori getting so close like that."
        if encore_sayoriquestion_1:
            "I'm just hopeful she's able to put two and two together now so it saves me the awkwardness of eventually telling her that Sayori and I are a couple."
            "Hopefully then, she won't full on put me in the hospital."
        "Oh well."
    else:
        "Yuri needs a scene here too."
    jump day2_meettheclubs
