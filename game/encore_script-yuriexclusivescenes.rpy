label yencore_1:
    "I go to Yuri first..."
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    show yuri 1g at t11 zorder 1
    "Yuri is in her usual spot at the front of the room, reading Portrait of Markov."
    "I carefully approach her, not wanting to scare her."
    mc "Hey, Yuri."
    show yuri 3p at h11
    "Yuri is immediately snapped out of her trance and turns her head to face me."
    y 2q "Oh! Hey [player]!"
    show yuri 3l
    "She says that as if she wasn't expecting me, but she quickly composes herself."
    y 1b "How are you doing this afternoon?"
    mc "Oh, I'm doing alright. Just wanted to see how you've been."
    show yuri u114221
    "Yuri instantly blushes."
    y u122218 "You...came to check up on me?"
    y 4a "How thoughtful..."
    show yuri 4b
    "Yuri starts playing with her hair, as if she's trying to compose herself."
    mc "I mean.... yeah... it's been a while since the festival..."
    show yuri 4e
    "Yuri continues to blush even harder."
    "I'll admit, looking back on the time I've spent with Yuri over the last two weeks, I feel a smile form across my face as well."
    "I quickly try to change the subject to avoid someone seeing us like this."
    show yuri 4a
    mc "Sooo... how's reading Portrait of Markov been?"
    "Yuri snaps out of her gaze and back into reality."
    y 2f "Oh! Well the book has gotten to be very interesting. How about you? Did you have the chance to get any reading done?"
    mc "Yeah, I was able to read up to chapter 5. I can't believe they left us on a cliffhanger right that!"
    show yuri 1c
    "Yuri chuckles to herself."
    y 1d "Well that's why there's chapter 6! Come on! We can read it together!"
    mc "I'd like that Yuri."
    show yuri 1c
    "I see Yuri form another smile."
    y 2s "You're a really good friend... [player]."
    "She flashes a gentle smile at me."
    "It's very clear that between us hanging out last Sunday as well as the festival, she's really had me on her mind lately."
    "And if I were being honest with myself, I'd say I've spent the last two weeks with her on my mind as well."
    "Yuri may be a hard person to get a good read on sometimes, but I'm starting to think that maybe we can be more than just friends..."
    mc "Well.... I try..."
    show yuri 1y6
    "We stand there for a few moments gazing at each other."
    "Suddenly I remember to grab my book."
    mc "Oh... I should probably get my book."
    y 1i "I don't believe there's a need for that. If you want, you could..."
    y 4a "...sit next to me again..."
    y 4c "I-if you want! I really have no preference!"
    "Yuri becomes all flustered and is stumbling over her sentences."
    "I try to calm her down."
    mc "Hey... it's okay! Really! I wouldn't mind at all..."
    "I feel my own face start turning red."
    "As if this didn't need to be even more awkward for both of us."
    show yuri 4c at t44 zorder 1
    show sayori 2k at t41 zorder 2
    "Out of the corner of my eye, I notice Sayori staring stoically into space."
    "That's not like Sayori..."
    show sayori at thide
    hide sayori
    mc "What's up with Sayori?"
    show yuri at t11
    y 4a "Hmmm?"
    show yuri 1e
    "Yuri turns to look at Sayori."
    y 1g "I'm not sure.... I haven't really seen her like that before."
    y 1t "Maybe you should check up on her?"
    mc"Yeah... I'll be right back okay?"
    "Yuri smiles and nods approvingly at me."
    show yuri at thide
    hide yuri

    #Sayori's scene
    "I walk over to Sayori."
    mc "Hey, Sayori!"
    show sayori 2x at t11 zorder 1
    s "Oh, hey, [player]!"
    "Sayori puts on her usual cheerful grin, but something about it just seems...off..."
    mc "What's up?"
    "I take a seat right next to her."
    s 1y "Oh, same old."
    "She smiles sadly at me."
    mc "Sayori come on, I've known you long enough to know that's a lie."
    "I'll leave it at that but i can tell its her rainclouds"
    "I gently place my hand on her shoulder."
    mc "You know that if anything's bothering you, you can talk to me. I'm here for you, Sayori."
    "I can hear Sayori whimpering in my ear."
    s 1u "I… I know… [player]....."
    
    "I pat Sayori’s shoulder as she struggles to compose herself."
    "A few minutes pass before Sayori stops sniffling."
    stop music fadeout 3.0
    mc "Hey, Sayori?"
    "Sayori curiously looks up at me."
    s 1v "Y-yeah?"
    mc "If you don’t mind me asking… how long have you been like this?"
    s "What do you mean?"
    mc "It’s just that… I’ve known you for as long as I can remember..."
    play music t10 fadein 3.0
    mc "I always saw you as someone who was always happy, bubbly, sometimes clumsy, but overall, just someone who’s a big ball of sunshine."
    mc "I never would’ve thought that in a million years that you would’ve ever been going through something like this."
    #normally average sprite for Sayori
    "Sayori pauses, as if to reflect on what I just said."
    s 1v "I mean… I guess I’ve always had it. I dunno…"
    s 1k "It didn’t really start acting up until we started high school."
    s 3k "I guess with the stress of all the exams, schoolwork, drama and other things…"
    s 3l "Like my parents divorce…"
    s 1t "And just missing out on spending time with you…"
    "I feel my heart deflate as I hear this."
    "I never thought that me spending less time with Sayori over the years would have that kind of effect on her."
    if encore_sayoriquestion_1 == True:
        "And rejecting her confession probably didn’t help matters."
        "God, I feel so stupid!"
    else:
        "I feel so stupid!"
    s 2t "I guess it just finally took enough of a toll on me to the point where I realized I had this."
    s 1k "But my entire life I’ve always felt that everyone would be better off as if I didn’t exist."
    s "No matter how hard I’d try to give people my happiness, my time and my energy."
    s "Just… nothing ever felt like it was worth it and that they didn’t need me to be happy."
    s 1u "And If I ever opened up about how I really felt on the inside, that people would spend all their time trying to make me happy."
    s "I’d just be a weight on their shoulders. They have too much to do and I don’t want to add on to their stress."
    s 1v "That’s what I thought when we kind of drifted apart when high school started."
    s "You had too much on your plate and me being around you would be too distracting for you, so I would always have to muster up the courage to even try to talk to you."
    "I feel an overwhelming sense of guilt overtake me."
    show sayori 1v at h11 zorder 1
    mc "Sayori!"
    "I pull her into a tight embrace."
    mc "I’m… i’m so sorry…."
    s 1t "You have nothing to apologize for, [player]."
    mc "I do! If I’d just put you before my hobbies, maybe you wouldn’t be like this so much."
    mc "I promise you, Sayori. I’m going to make this up to you starting right now."
    "I feel Sayori’s tears return as they bleed into my shoulder."
    s "Don’t feel guilty for the way I feel [player]."
    s 1w "I’m sorry I got you so worried about me… I didn’t mean to take away from Natsuki or anything like that!"
    if encore_sayoriquestion_1 == True:
        s "I’m a terrible girlfriend!"
    else:
        s "I'm a terrible friend!"
    mc "No, you aren’t Sayori. Don’t say that."
    stop music fadeout 3.5
    scene black
    with Dissolve(1)
    "Sayori hugs me tightly."
    "We’re like this for sometime before I here some commotion come from the closet."
    scene bg club_day
    show sayori 1m at t11 zorder 1
    stop music
    show sayori 1m at t11 zorder 1
    n "DAMN IT, MONIKA!!!!"
    play music t3
    "Monika and Yuri giggle before going back to their respective activities."
    "Sayori and I turn to each other, both shooting each other a concerned look over what just happened."
    mc "I'm going to check on Natsuki."
    show sayori 1t
    "Sayori wipes a tear and gives me an approving nod."
    "I carefully approach the closet..."

    #Closet Scene
    scene bg closet
    with wipeleft_scene
    play music t6 fadein 1.0
    "I hear Natsuki rummaging around in the closet."
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
    "Maybe she {i}can{/i} handle this by herself..."
    show natsuki 5g at t11 zorder 1
    mc "Suit yourself."
    show natsuki at thide
    hide natsuki
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "As I head back towards the front of the room, I can hear Natsuki's exasperated sighs, followed by more of her yelling."
    n "Baka!"
    "What? I'll never get around to understanding Natsuki's weird logic..."
    "My train of thought is interrupted by Monika calling us to attention."
    play music t8 fadein 1.0
    show monika 4b at t11 zorder 4
    m "Ok, everyone! Poem time!"
    show natsuki 4e at t44 zorder 3
    n "Ugh! Do we really need to do this now? I'm looking for something!?"
    m 3f "Sorry, Natsuki! I just wanted to make sure we have enough time to share!"
    show natsuki 5g
    "Natsuki shoots Monika an irritated look."
    n 5e "Alright, fine!"
    show monika at thide
    hide monika
    show natsuki 5i
    "Natsuki quickly glances back at the closest."
    "I see the irritation from Natsuki's face is fade away as she dejectedly looks at the floor and starts slowly walking to retrieve her poem."
    mc "Hey, Natsuki."
    "Natsuki turns to me, her face red and eyes glossy as if she was fighting back tears."
    n 5h "Y-yeah?"
    mc "I'm sure you'll find it sooner or later. I know it means alot to to you that you find that copy. Trust me I'd lose my stuff too if I lost something that was important to me."
    show natsuki 12b
    "Natsuki struggles to maintain eye contact with me for longer than a few seconds."
    mc "I know how you feel and I just wanted to let you know that my offer to help you still stands."
    show natsuki 12a
    "Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
    n 4q "T-Thanks [player]."
    mc "Hey, no problem. I hate seeing you get so worked up like this. I like seeing you happy."
    show natsuki 1s
    "Natsuki stares off into space, as if to process what I just said."
    mc "You alright, Natsuki?"
    show natsuki 1i
    "Natsuki returns to reality."
    n 1e "I'm fine! Let's just get this over with."
    show natsuki at thide
    hide natsuki
    "Natsuki hurries off to the back of the room to retrieve her poem."
    "I quietly sigh to myself as I walk over to retrieve my poem."
    "It's always been hard for me to get a good read on Natsuki."
    "Sometimes I don't know whether she acts that way on purpose..."
    "...Or that she has an ulterior motive for trying to act that way."
    "..."
    jump day1_poemsharing

label yencore_2:

    $ hangout2 = "Yuri"
    "I decided to see what Yuri is up to."
    scene bg club_day
    with wipeleft_scene
    show yuri 1g zorder 1 at t11
    "I spot her in her usual spot at the front of the room."
    "I tepidly approach her as she seems to be absorbed into her book."
    show yuri 1e
    "However, she quickly spots me heading her way."
    y 2b "Hey, [player]!"
    "She smiles warmly at me."
    mc "Hey, Yuri! What's up?"
    y 1a "Oh, just reading Chapter 7. Did you finish Chapter 6 yet?"
    show yuri 2c
    mc "Yeah, I finished it last night! It was pretty interesting."
    "That wasn't completely true, I did finish the chapter, but I finished it during class when I was bored."
    "It's what got me through today honestly."
    y 2d "Well I'm glad you got to read it! I'm just getting started on Chapter 7..."
    y 4a "So we can read it together if you want..."
    "Yuri looks off in her usual flustered manner."
    show yuri 4e
    mc "You know I'd love to Yuri!"
    y "Oh, right... how silly of me."
    show yuri 2o
    "I take my usual spot next to Yuri."
    mc "I take it we're doing the same thing as last time?"
    y 2q "Y-yeah... that works for me."
    "I shoot Yuri a warm smile{w=0.68}{nw}"
    show yuri 4e
    "I shoot Yuri a warm smile{fast} which immediately causes her to blush."
    mc "Come on then, let's get ready."
    show yuri 2s
    "Yuri nods approvingly."
    "We begin to read Chapter 7."
    show yuri at thide
    hide yuri
    "..."
    play music e5
    "After reading for a few minutes, I see Yuri shifting unconfortably in her seat."
    mc "Everything good, Yuri?"
    show yuri 1q zorder 1 at t11
    y "Yeah, it's just that my posture isn't too good right now."
    "Oh right, her posture."
    "I can't believe I forgot about that."
    mc "Do you want to move to under the windowsill again?"
    y 2t "I mean... if you're comfortable here I don't mind...."
    mc "Yuri, I don't want you to be uncomfortable if sitting like this is going to make your back ache."
    show yuri 3p
    mc "I really don't mind where we read as long as we're together."
    "Oh..."
    show yuri 4c
    "Might've been a little too forward there..."
    "Yuri is completely caught off guard and frantically fiddles with her hair as she figures out how to respond."
    mc "Yeah... let's just sit down..."
    y "O-okay..."
    show yuri at thide
    hide yuri
    "Yuri and I take our seats under the windowsill."
    "Ironically enough, we actually once sat here, for the same reason."
    "I don't mind it though, I enjoy being this close to Yuri."
    "Yuri hands me the book as she peers over my shoulder to read the book."
    mc "Do you feel better now?"
    show yuri 2o zorder 1 at t11
    y "Yeah I do...I can't really see the book though..."
    mc "Oh my bad."
    "I try bringing the book closer to Yuri, but it makes makes my arm feel awkward."
    stop music fadeout 1.0
    y 1f "Let me try something."
    "Yuri pushes the book back towards me."
    mc "Oh?"
    show yuri 1e at s11
    play sound "sfx/fall.ogg"
    "She then puts her head on my shoulder."
    "I immediately feel the blood rush to my face as I'm filled with shock."
    "Not that I don't mind Yuri doing that, but the fact that she actually went out of her comfort zone to do this astonishes me."
    y 2q "This isn't too distracting for you... right?"
    mc "Oh no... not at all..."
    mc "I actually kind of like this."
    show yuri 4c
    "Yuri looks off and blushes."
    show yuri 3w
    pause 0.7
    show yuri 3k
    pause 0.6
    show yuri 3l
    pause 0.7
    show yuri 1s
    "She regains her composure and looks back at me."
    y 1t "Good... I was hoping you wouldn't find me weird for doing this."
    mc "Maybe you should do it more."
    "I say that teasingly."
    show yuri u111261
    "Yuri lets out a small giggle."
    y "Well if you want me too...I will..."
    mc "Noted."
    play music t8 fadein 1.0
    show yuri 1s
    "With our banter aside, we pick up where we left off."
    show yuri at thide
    hide yuri
    "The chapter actually turns out to be the best one yet."
    "In the chapter, the main character, this girl named Libitina, is given a second chance to repair her broken relationship with her Uncle, who she's currently living with."
    "Most of the chapter is told through a monologue as Libitina internally debates if it's worth repairing her relationship with her uncle..."
    "As she's on the run from a league of mad scientists who want her back for more experimentation purposes."
    "It's quite interesting actually, and through her logic, she knows mending fence with her uncle is the right thing to do and she might not get another chance to make him happy..."
    "But she doesn't know if in the end it's even worth it..."
    "After a while we reach the end of the chapter with Libitina deciding to talk to her friend about what she should do."
    show yuri 1h zorder 1 at t11
    y "Do you think she'll do it [player]?"
    mc "Hmmm?"
    y 1f "Do you think Libitina will end up making things right with her Uncle?"
    mc "I mean, I hope she does."
    show yuri 1e
    mc "Very rarely do people get a second chance to do the right thing."
    mc "If I was her, I'd take it."
    y 2j "Y-yeah... me too..."
    show yuri 1u
    "We sit for the next moments in silence, unsure of what to do next."
    "Yuri seems to be deep in thought, as if she's unsure of what to say next."
    "She takes a deep breath and turns to face me again."
    stop music fadeout 2.5
    y 1s "I'm really glad we get to spend time like this [player]."
    mc "Yeah, me too!"
    y "And..."
    "Yuri hesitates."
    mc "And what?"
    play music t10 fadein 3.0
    y 1t "I'm glad we've gotten as close as we have been over these last few weeks..."
    "I hear Yuri's voice break as she says that, but she continues to press on, sounding like she's trying to fight back tears."
    y 1v "Truth is, I haven't had real friend in years..."
    y 2q "Not since Middle School has anyone treated me like an actual person."
    y 2w "I've honestly almost forgotten what it was like to enjoy being in the company of someone who cares about you...."
    "I feel my heart sink into my chest as she says that."
    if encore_festivalquestion_2 == "Yuri":
        "Yuri did mention to me a few weeks ago that she usually spends all her time alone, but, I never knew she's been alone for so long."
    else:
        pass
    y 3s "And so...it means a lot to me that we have this kind of relationship..."
    show yuri 3p at h11
    "Without thinking, I take Yuri's hand."
    show yuri 3s at face with dissolve
    "Yuri looks up to me, her violet eyes being reflective in the sunlight and a smile slowly forming across her face."
    mc "Yuri...."
    mc "You don't have to be alone anymore."
    "Yuri's face turns full crimson."
    y 3t "[player]...I..."
    "Yuri squeezes my hand tightly."
    "We struggle to make eye contact for longer than a few seconds but I try to muster up the courage to keep talking."
    "But for some reason, I can't."
    "We're just entranced intently looking at each other, both stammering as we try to find what we want to say to each other."
    "I feel Yuri's gentle breaths brush against my face as she slowly leans into me."
    "This feels like heaven."
    "But I really don't know what to do."
    "Being like this with Yuri makes me wish to hold onto her and never let go."
    "But I'm afraid that someone's gonna catch us and immediately get the wrong idea..."
    show yuri at thide
    hide yuri with wipeleft
    show natsuki 5a zorder 2 at t33
    "I glance around the room to see Natsuki rummaging around in the closet,{w=0.80}{nw}"
    show sayori 1k zorder 1 at t31
    "I glance around the room to see Natsuki rummaging around in the closet,{fast} Sayori spacing out,{w=0.80}{nw}"
    show monika 1c zorder 3 at t32
    "I glance around the room to see Natsuki rummaging around in the closet, Sayori spacing out,{fast} and Monika working on something."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yuri 1u at face with dissolve
    "I turn back to face Yuri."
    "Is this it?"
    show yuri 1w
    "Is this my chance to finally make a move on Yuri?"
    "I mean we're already so close..."
    scene black with close_eyes
    "I close my eyes..."
    "I feel Yuri placing her hand on my chest as she pulls me in..."
    "Here goes nothing..."
    stop music fadeout 1.0
    "..."
    "Suddenly, I hear Monika stand up and walk to the front of the room."
    scene bg club_day with open_eyes
    play music t5 fadein 1.0
    show monika 3b zorder 1 at t11
    m "Okay, everyone! Gather around! I have an important announcement to make!"
    show sayori 1b zorder 2 at t21
    show monika 1c at t22
    "Suddenly, Monika and Sayori's eyes turn to me and Yuri."
    show natsuki 4k zorder 1 at t33
    show monika zorder 3 at t32
    show sayori at t31
    "Natsuki, confused as to what's going on, turns around..."
    show natsuki 4g
    "Only to see what Monika and Sayori are staring at."
    "Yuri and I were really just about too..."
    "And the position we're in really doesn't make it any easier to explain..."
    show natsuki 5f
    show monika 1h
    show sayori 1i
    "All 3 girls are looking at us, with a bit of an irritated...almost jealous...expression on their faces."
    "God Damn It."
    "Oh well."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    mc "Um... Yuri?"
    show yuri 1n at face with dissolve
    "Yuri snaps out of her gaze."
    y "Y-yeah? What's wrong?"
    mc "We kinda have to get up..."
    show monika 1c zorder 4 at t42
    show natsuki 5g zorder 1 at t43
    show sayori 1b zorder 2 at t41
    show yuri 2e zorder 3 at t44
    "Yuri turns to face the front of the room and she sees Monika, Sayori and Natsuki staring at us."
    show yuri 3p
    pause 0.7
    show natsuki xu2131
    show monika 1l
    show sayori 1l
    show yuri 4c
    "Yuri immediately stands up and brushes herself off, clearly embarrassed."
    y "Oh my gosh, I'm so sorry everyone!"
    y "I-I didn't mean for you guys to see us like that and..."
    show monika 1l
    show natsuki 5z
    show sayori 1q
    "Sayori, Monika and Natsuki all try to contain their laughter over what just happened but they're eventually able to compose themselves."
    show sayori 1a
    show natsuki 5a
    m 2b "It's alright, Yuri, come on."
    "She gestures for us to come toward the front of the room."
    show yuri at thide
    hide yuri
    "Yuri briskly walks to the front of her room and takes her usual spot."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    "I stand up as well and make my way to the room, joining the rest of the group."
    # if encore_festivalquestion_2 == "Yuri":
    #     show yuri 4a
    #     "While on my way to the front of the room, Yuri stops me."
    #     mc "Yuri?"
    #     y 4b "N-nothing [player]. It was nothing important."
    #     show yuri at thide
    #     hide yuri
    #     "She mutters that softly and avoids eye contact with me as she briskly walks back to her seat."
    #     "It's gonna to take awhile for us to bring up what we just went through."
    #     "Still, I wouldn't mind if we could pick up where we left off..."
    # else:
    #     "Natsuki needs a scene here."
    if encore_festivalquestion_2 == "Yuri":
        show natsuki 4g at t11
        play sound "sfx/smack.ogg"
        "While on the way to the front of the room, Natsuki gives me a \"friendly\" punch in the arm."
        mc "Ouch! Hey what was that for?"
        n "N-Nothing... dummy..."
        "She mutters that softly and avoids eye contact as she briskly walks past me."
        "Well, that was random."
    jump day2_meettheclubs
    
