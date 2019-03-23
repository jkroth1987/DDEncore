#Day 1
label yencore_1:
    $ hangout1 = "Yuri"
    "I go to Yuri first..."
    scene bg club_day
    with wipeleft_scene
    play music tyuri

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Yuri":
        show yuri 1g at t11 zorder 1
        "Yuri is in her usual spot at the front of the room, reading Portrait of Markov."
        "I carefully approach Yuri, not wanting to startle her."
        mc "Hey, Yuri."
        $ renpy.pause(delay=0.8, hard=True)
        show yuri 1e
        $ renpy.pause(delay=0.8, hard=True)
        show yuri 3p at h11
        "Yuri is immediately snapped out of her trance and turns her head to face me."
        y 2q "Oh! Hey, [player]!"
        show yuri 3l
        "Yuri sounds surprised to see me, but she quickly composes herself."
        y 1b "How are you doing this afternoon?"
        mc "Oh, I'm doing alright. Just wanted to see how you've been."
        show yuri u114221
        "Yuri's eyes glisten."
        y u122218 "You...c-{w=0.38}came to check up on me?"
        y 4a "How thoughtful..."
        show yuri 4b
        "Yuri starts playing with her hair, as if she's trying to compose herself."
        mc "I mean, yeah...{w=0.38}it's been a while since the festival..."
        show yuri 4e
        "Yuri continues to blush even harder."
        "I'll admit, looking back on the time I've spent with Yuri over the last two weeks, I feel a smile form across my face as well."
        "I quickly try to change the subject to avoid someone seeing us like this."
        show yuri 4a
        mc "Sooo...{w=0.38} how's reading Portrait of Markov been?"
        "Yuri snaps out of her gaze and back into reality."
        y 2f "Oh! Well the book has gotten to be very interesting. How about you? Did you have the chance to get any reading done?"
        mc "Yeah, I was able to read up to chapter five. I can't believe they left us on a cliffhanger right that!"
        show yuri 1c
        "Yuri chuckles to herself."
        y 1d "Well that's why there's chapter six! Come on, we can read it together!"
        mc "I'd like that Yuri."
        show yuri 1c
        "I see Yuri form another smile."
        y 2s "You're a really good friend...[player]."
        "She flashes a gentle smile at me."
        "It's very clear that between us hanging out last Sunday as well as the festival, she's really had me on her mind lately."
        "And if I were being honest with myself, I'd say I've spent the last two weeks with her on my mind as well."
        "Yuri may be a hard person to get a good read on sometimes, but I'm starting to think that maybe we can be more than just friends..."
        mc "Well...{w=0.38}I try..."
        show yuri 1s
        "We stand there for a few moments gazing at each other."
        "Suddenly I remember to grab my book."
        mc "Oh...{w=0.38} I should probably get my book."
        y 1i "I don't believe there's a need for that. If you want, you could..."
        y 4a "...{w=0.38}sit next to me again..."
        y 4c "I-{w=0.38}if you want! I really have no preference!"
        "Yuri becomes all flustered and is stumbling over her sentences."
        "I try to calm her down."
        mc "Hey...{w=0.38} it's okay! Really! I wouldn't mind at all..."
        "I start to feel my own face heating up with embarrassment."
        "As if this didn't need to be even more awkward for the both of us..."
        show yuri 4c at t44 zorder 1
        show sayori 2k at t41 zorder 2
        "Out of the corner of my eye, I notice Sayori staring stoically into space."
        "That's not like Sayori..."
        show sayori at thide
        hide sayori
        mc "What's up with Sayori?"
        show yuri at t11
        y 4a "Hmmm?"
        "Yuri turns to look at Sayori."
        show yuri 1e
        $ renpy.pause(delay=0.8, hard=True)
        y 1g "I'm not sure...{w=0.38} I haven't really seen her like that before."
        y 1t "I can't imagine what could possibly be troubling her..."
        mc "Yeah...{w=0.38} I'll be right back, okay?"
        show yuri 1a
        "Yuri smiles and nods approvingly at me."
        y 1b "I'll be waiting~"
        show yuri at thide
        hide yuri
        stop music fadeout 1.0

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Yuri":
        show yuri 1g at t11 zorder 1
        "Yuri is in her usual spot at the front of the room, reading her book."
        "I carefully approach Yuri, not wanting to startle her."
        mc "Hey, Yuri."
        $ renpy.pause(delay=0.8, hard=True)
        show yuri 1e
        $ renpy.pause(delay=0.8, hard=True)
        show yuri 3p at h11
        "Yuri is immediately snapped out of her trance and turns her head to face me."
        y 2q "Oh! H-{w=0.38}hello, [player]!"
        show yuri 3f
        "Yuri seems surprised to see me."
        y 1b "Forgive me, but I really wasn't expecting you to come over here..."
        mc "I hope I wasn't interupting you at the good part..."
        y 1p "N-{w=0.38}no! You weren't!"
        y 1q "I actually just started a new chapter..."
        mc "Oh! Well, hey, that's cool!"
        y "Y-{w=0.38}yeah...{w=0.38}I guess it is..."
        "I haven't really talked to Yuri like this before, so finding a non-literature subject to talk about is a bit...{w=0.38} challenging."
        "Still, I need to come up with at least something..."
        mc "Well, hey, I just wanted to see how you've been since the festival."
        show yuri u114221
        "Yuri's eyes glisten."
        y u122218 "You...c-{w=0.38}came to check up on me?"
        y 4a "That's very thoughtful of you, [player]..."
        show yuri 4b
        "Yuri starts playing with her hair, as if she's trying to compose herself."
        mc "I mean, yeah...{w=0.38}it's been a while since the festival..."
        mc "And you knocked it out of the park with your preformance last week!"
        show yuri 4e
        "Yuri continues to blush even harder."
        y "Oh...{w=0.38}well I'm glad you think I did well..."
        y "It means alot..."
        "I guess Yuri has a hard time processing compliments."
        "Well, better than how Natsuki handles most of my compliments anyway..."
        "I quickly try to change the subject to avoid someone seeing us like this."
        mc "Sooo...{w=0.38}what book is that anyways?"
        mc "Isn't that the book you gave me?"
        show yuri 4a
        "Yuri snaps out of her gaze and back into reality."
        y 2f "Oh, yeah! It's called Portrait of Markov."
        y 2d "It's one of my favorite reads so far!"
        mc "Ah, I see."
        y 2t "D-{w=0.38}did you get the chance to read it yet?"
        "I read the first chapter and sort of got lost with where the story was going midway through."
        "Granted it seemed pretty interesting at the time, and I wouldn't mind reading it again..."
        mc "I was able to get around to finishing the first chapter."
        mc "I'll admit from what I've read so far, the story's a little confusing to me."
        show yuri 1c
        "Yuri chuckles to herself."
        y 1d "Well, you have to read the second chapter to understand things better!"
        y 1t "W{w=0.38}-we can read it together..."
        y 1o "If you want..."
        "Yuri nervously looks off, as if she's unsure of her own suggestion."
        mc "I'd like that Yuri."
        show yuri u114221
        "Yuri's eyes widen."
        show yuri 1t
        y "Y-{w=0.38}you really mean that?"
        mc "Of course! It seems like an interesting read!"
        show yuri 1c
        "I see Yuri form another smile."
        y 2s "You are a really nice person afterall...{w=0.38}[player]."
        "She flashes a gentle smile at me."


        if encore_sayoriquestion_1 == False:
            "Yuri may be a hard person to get a good read on sometimes, but I'm starting to think that maybe we can finally be friends..."
            "And maybe more...{w=0.38} if we get that far..."

        if encore_sayoriquestion_1 == True:
            "Yuri may be a hard person to get a good read on sometimes, but I'm starting to think that maybe we can finally be friends..."


        mc "Well...{w=0.38}I try..."
        show yuri 1s
        "We stand there for a few moments gazing at each other."
        "Suddenly I realize I don't have my book."
        mc "Oh... I don't have the copy you gave me."
        y 1i "Well if you want we can use the same copy..."
        mc "How exactly would that work? Reading from the same copy?"
        y 4a "...{w=0.38}you could sit next to me..."
        y 4c "I-{w=0.38}if you want! I would understand if you didn't want to!"
        "Yuri becomes all flustered and is stumbling over her sentences."
        "I try to calm her down."
        mc "Hey...{w=0.38}it's okay! Really! If you're comfortable with that then I don't really see an issue with us sharing."
        y 1q "A-alright..."
        "I sitdown next to Yuri."
        show yuri 1q at t44 zorder 1
        show sayori 2k at t41 zorder 2
        "Out of the corner of my eye, I notice Sayori staring stoically into space."
        "That's not like Sayori..."
        show sayori at thide
        hide sayori
        mc "What's up with Sayori?"
        show yuri at t11
        y 4a "Hmmm?"
        "Yuri turns to look at Sayori."
        show yuri 1e
        $ renpy.pause(delay=0.8, hard=True)
        y 1g "I'm not sure...{w=0.38} I haven't really seen her like that before."
        y 1t "I can't imagine what could possibly be troubling her..."
        mc "Yeah...{w=0.38} I'll be right back, okay?"
        show yuri 1a
        "Yuri smiles and nods approvingly at me."
        y 1b "I won't start without you, [player]!"
        show yuri at thide
        hide yuri




if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            with wipeleft_scene
            play music t3 fadein 1.0
            mc "Hey, Sayori!"
            show sayori 2x at t11 zorder 1
            s "Oh, hey, [player]!"
            "Sayori puts on her usual cheerful grin, but something about it just seems...{w=0.38}off..."
            mc "What's up?"
            "I take a seat right next to her."
            s 1y "Oh, same old."
            "She smiles sadly at me."
            mc "Sayori..."
            "She must be having her 'rainclouds' again..."
            "I gently place my hand on her shoulder."
            mc "You know that if anything's bothering you, you can talk to me."
            mc "I'm here for you, Sayori."
            stop music fadeout 3.0
            mc "I hate to see you like this, and I know you don't want to have those rainclouds over your head all the time."
            "I can hear Sayori start to sniffle."
            mc "And if I've said or done anything lately that has put you in this state of mind right now..."
            show sayori 1e
            mc "I want to let you know that I'm deeply, deeply sorry..."
            mc "I never wanted to hurt you or-"
            show sayori 2k
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 2l
            play music t9 fadein 3.0
            s "Nothing has really changed between us,{w=0.38} right?"
            mc "I mean, I want to think so..."
            show sayori 1k
            s "Hehe~"
            s "It's kind of funny, [player]."
            mc "I...{w=0.38} don't take your meaning."
            s "I selfishly thought that if I tried putting all my time, energy and effort into making you happy..."
            show sayori 3u
            $ renpy.pause(delay=0.5, hard=True)
            show sayori 1v
            s "I dont know...{w=0.38} I thought that you would love me back..."
            "I feel my heart sink like a stone in the ocean as Sayori chokes those words out..."
            show sayori 1u
            s 1k "But, I never was the one you wanted, was I?"
            s 1t "If I wasn't such a mess, you'd still be spending time with Yuri, wouldn't you?"
            s 1k "I can see why you like her so much..."
            s 1t "You deserve to have someone like her in your life..."
            s "I shouldn't be trying to keep you from her."
            "Maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourself over there with Yuri..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible friend!"
            s "You should just move on from me!"
            mc "No, Sayori...{w=0.38}don’t say that..."
            stop music fadeout 3.5
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto me."
            mc "Me spending time with Yuri isn't going to make me forget about you, Sayori."
            mc "And I'm just trying to figure out everything just as much as you are..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before we hear some commotion come from the closet."
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
            mc "Hey...{w=0.38} hey...{w=0.38} I just wanted to see what's been going on, that's all."
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
            n 5h "Y-{w=0.38}yeah?"
            mc "I'm sure you'll find it sooner or later. I know it means alot to you that you find that copy."
            mc "Trust me, I'd be pissed too if I lost something that was important to me."
            show natsuki 12b
            "Natsuki struggles to maintain eye contact with me for longer than a few seconds."
            mc "I know how you feel and I just wanted to let you know that my offer to help you still stands."
            show natsuki 12a
            "Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
            n 4q "T-{w=0.38}Thanks, [player]."
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
            with wipeleft_scene
            jump poem_scene9


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            with wipeleft_scene
            play music t3 fadein 1.0
            mc "Hey, Sayori!"
            show sayori 2x at t11 zorder 1
            s "Oh, hey, [player]!"
            "Sayori puts on her usual cheerful grin, but something about it just seems...{w=0.38}off..."
            mc "What's up?"
            "I take a seat right next to her."
            s 1y "Oh, same old."
            "She smiles sadly at me."
            mc "Sayori..."
            "She must be having her 'rainclouds' again..."
            "I gently place my hand on her shoulder."
            mc "You know that if anything's bothering you, you can talk to me."
            mc "I'm here for you, Sayori."
            mc "I hate to see you like this, and I know you don't want to have those rainclouds over your head all the time."
            "I can hear Sayori start to sniffle."
            stop music fadeout 3.0
            s 1u "I...{w=0.38} I know...{w=0.38} [player]....."
            "I pat Sayori's shoulder as she struggles to compose herself."
            mc "I just want you to get better, Sayori."
            mc "It's what matters the most to me right now."
            "A few minutes pass before Sayori stops sniffling."
            show sayori 1g
            s "I just don't want this relationship to be a one-way street, [player]."
            mc "It's not! Why would you think that?"
            s 1k "Well..."
            play music t9 fadein 3.0
            s "You've already done so much for me..."
            show sayori 1v
            s "What have I done for you in return?"
            s 1k "Other then dragging you away from the others."
            s 1t "If I wasn't such a mess, you'd still be spending time with Yuri, wouldn't you?"
            "I mean..."
            "I don't see spending some time around Yuri as a bad thing..."
            "But, maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourselves over there..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible girlfriend!"
            mc "No, you aren't Sayori...don’t say that..."
            stop music fadeout 3.5
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto me."
            mc "Yuri doesn't matter right now..."
            mc "Just us..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before we hear some commotion come from the closet."
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
            mc "Hey...{w=0.38} hey...{w=0.38} I just wanted to see what's been going on, that's all."
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
            n 5h "Y-{w=0.38}yeah?"
            mc "I'm sure you'll find it sooner or later. I know it means alot to you that you find that copy."
            mc "Trust me, I'd be pissed too if I lost something that was important to me."
            show natsuki 12b
            "Natsuki struggles to maintain eye contact with me for longer than a few seconds."
            mc "I know how you feel and I just wanted to let you know that my offer to help you still stands."
            show natsuki 12a
            "Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
            n 4q "T{w=0.38}-Thanks, [player]."
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
            with wipeleft_scene
            jump poem_scene11



if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            with wipeleft_scene
            play music t3 fadein 1.0
            mc "Hey, Sayori!"
            show sayori 2x at t11 zorder 1
            s "Oh, hey, [player]!"
            "Sayori puts on her usual cheerful grin, but something about it just seems...{w=0.38}off..."
            mc "What's up?"
            "I take a seat right next to her."
            s 1y "Oh, same old."
            "She smiles sadly at me."
            mc "Sayori..."
            "She must be having her 'rainclouds' again..."
            "I gently place my hand on her shoulder."
            mc "You know that if anything's bothering you, you can talk to me."
            mc "I'm here for you, Sayori."
            stop music fadeout 3.0
            mc "I hate to see you like this, and I know you don't want to have those rainclouds over your head all the time."
            "I can hear Sayori start to sniffle."
            mc "And if I've said or done anything lately that has put you in this state of mind right now..."
            show sayori 1e
            mc "I want to let you know that I'm deeply, deeply sorry..."
            mc "I never wanted to hurt you or-"
            show sayori 2k
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 2l
            play music t9 fadein 3.0
            s "Nothing has really changed between us,{w=0.38} right?"
            mc "I mean, I want to think so..."
            show sayori 1k
            s "Hehe~"
            s "It's kind of funny, [player]."
            mc "I...{w=0.38} don't take your meaning."
            s "I selfishly thought that if I tried putting all my time, energy and effort into making you happy..."
            show sayori 3u
            $ renpy.pause(delay=0.5, hard=True)
            show sayori 1v
            s "I dont know...{w=0.38} I thought that you would love me back..."
            "I feel my heart sink like a stone in the ocean as Sayori chokes those words out..."
            show sayori 1u
            s 1k "But, I never was the one you wanted, was I?"
            s 1t "If I wasn't such a mess, you'd still be spending time with Yuri or Natsuki, wouldn't you?"
            s 1k "I can see why you like them so much..."
            s 1t "You deserve to have someone like them in your life..."
            s 1u "Yuri with her beauty..."
            s "And Natsuki with her baking..."
            s "I shouldn't be trying to keep you from them."
            "Maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourself over there with Yuri..."
            s "And how you were spending time with Natsuki last Sunday..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible friend!"
            s "You should just move on from me!"
            mc "No, Sayori...{w=0.38}don’t say that..."
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto me."
            mc "Me spending time with Yuri or Natsuki isn't going to make me forget about you, Sayori."
            mc "And I'm just trying to figure out everything just as much as you are..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before we hear some commotion come from the closet."
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
            mc "Hey...{w=0.38} hey...{w=0.38} I just wanted to see what's been going on, that's all."
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
            mc "I'm sure you'll find it sooner or later. I know it means alot to you that you find that copy."
            mc "Trust me, I'd be pissed too if I lost something that was important to me."
            show natsuki 12b
            "Natsuki struggles to maintain eye contact with me for longer than a few seconds."
            mc "I know how you feel and I just wanted to let you know that my offer to help you still stands."
            show natsuki 12a
            "Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
            n 4q "T-Thanks, [player]."
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
            with wipeleft_scene
            jump poem_scene10


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            with wipeleft_scene
            play music t3 fadein 1.0
            mc "Hey, Sayori!"
            show sayori 2x at t11 zorder 1
            s "Oh, hey, [player]!"
            "Sayori puts on her usual cheerful grin, but something about it just seems...{w=0.38}off..."
            mc "What's up?"
            "I take a seat right next to her."
            s 1y "Oh, same old."
            "She smiles sadly at me."
            mc "Sayori..."
            "She must be having her 'rainclouds' again..."
            "I gently place my hand on her shoulder."
            mc "You know that if anything's bothering you, you can talk to me."
            mc "I'm here for you, Sayori."
            mc "I hate to see you like this, and I know you don't want to have those rainclouds over your head all the time."
            "I can hear Sayori start to sniffle."
            stop music fadeout 3.0
            s 1u "I...{w=0.38} I know...{w=0.38} [player]....."
            "I pat Sayori's shoulder as she struggles to compose herself."
            mc "I just want you to get better, Sayori."
            mc "It's what matters the most to me right now."
            "A few minutes pass before Sayori stops sniffling."
            show sayori 1g
            s "I just don't want this relationship to be a one-way street, [player]."
            mc "It's not! Why would you think that?"
            s 1k "Well..."
            play music t9 fadein 3.0
            s "You've already done so much for me..."
            show sayori 1v
            s "What have I done for you in return?"
            s 1k "Other then dragging you away from the others."
            s 1t "If I wasn't such a mess, you'd still be spending time with Yuri or Natsuki, wouldn't you?"
            "I mean..."
            "I don't see spending some time around Yuri or Natsuki as a bad thing..."
            "But maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourself over there with Yuri..."
            s "And how you were spending time with Natsuki last Sunday..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible girlfriend!"
            mc "No, you aren't Sayori...don’t say that..."
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto me."
            mc "Yuri doesn't matter right now..."
            mc "Just us..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before we hear some commotion come from the closet."
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
            mc "Hey...{w=0.38} hey...{w=0.38} I just wanted to see what's been going on, that's all."
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
            n 5h "Y-{w=0.38}yeah?"
            mc "I'm sure you'll find it sooner or later. I know it means alot to you that you find that copy."
            mc "Trust me, I'd be pissed too if I lost something that was important to me."
            show natsuki 12b
            "Natsuki struggles to maintain eye contact with me for longer than a few seconds."
            mc "I know how you feel and I just wanted to let you know that my offer to help you still stands."
            show natsuki 12a
            "Natsuki's face returns to its normal color, but she struggles to articulate what she wants to say next, but after a few moments she finally finds her voice."
            n 4q "T-{w=0.38}Thanks, [player]."
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
            with wipeleft_scene
            jump poem_scene12






    label yencore_2:

        $ hangout2 = "Yuri"
        "I decided to see what Yuri was up to."
        scene bg club_day
        with wipeleft_scene
        show yuri 1g zorder 1 at t11
        play music t6 fadein 2.0

if hangout1 == "Yuri":
    jump yur_continued

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
    jump yur_first




label yur_continued:
"I spot Yuri in her usual spot at the front of the room."
"I tepidly approach her as she seems to be absorbed into her book."
show yuri 1e
"However, she quickly spots me heading her way."
y 2b "Hey, [player]!"
"She smiles warmly at me."
mc "Hey, Yuri! What's up?"

if encore_festivalquestion_2 == "Yuri":
    y 1a "Oh, just reading Chapter seven. How about you?"
    "Aside from that horrific nightmare I had last night..."
    "And the hallucination I experienced this morning..."
    "Which there's no chance I'm sharing any of that with Yuri..."
    mc "Oh, I'd say it's been alright. Nothing too exciting."
    show yuri 1d
    y "Well, that's good to hear, [player]!"
    show yuri 1f
    y "Were you able to finish chapter six?"
    show yuri 2c
    mc "Yeah, I finished it last night actually. It was pretty interesting!"
    "That wasn't completely true, I did finish the chapter, but I finished it today during class when I was bored."
    "I wouldn't want to give Yuri the impression that I'm a slacker..."
    y 2j "Well I'm glad you got to read it! I just got started with reading chapter seven actually..."
    y 4a "So we can read it together if you want..."
    show yuri 4b
    "Yuri looks off in her usual flustered manner."
    show yuri 4e
    mc "You know I'd love to Yuri!"
    y "Oh, right...{w=0.38}how silly of me."
    show yuri 2q
    "I sit down next to Yuri."
    mc "I take it we're doing the same thing as last time?"
    y "Y-{w=0.38}yeah...{w=0.38}that works for me."
    "I shoot Yuri a warm smile{w=0.68}{nw}"
    stop music fadeout 4.0
    show yuri 4e
    "I shoot Yuri a warm smile{fast}, which immediately causes her to blush."
    mc "Well, let's get reading!"
    show yuri 2s
    "Yuri nods approvingly at me as we begin to read chapter seven."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    play music e5
    show yuri 1h at t11
    "After reading for a few minutes, I see Yuri shifting unconfortably in her seat."
    mc "Everything good, Yuri?"
    show yuri 1q zorder 1 at t11
    y "Yeah, it's just that my posture isn't too good right now."
    "Oh right, her 'posture'."
    "I can't believe I forgot about that..."
    mc "Do you want to move to under the windowsill again?"


if encore_festivalquestion_2 == "Natsuki":
    y 1a "Oh, just reading Portrait of Markov. How about you?"
    "Aside from that horrific nightmare I had last night..."
    "And the hallucination I experienced this morning..."
    "Which there's no chance I'm sharing any of that with Yuri..."
    mc "Oh, I'd say it's been alright. Nothing too exciting."
    show yuri 1d
    y "Well, that's good to hear, [player]!"
    show yuri 1f
    y "Did you happen to start reading?"
    show yuri 2q
    y "Since we didn't quite get the chance to start last time..."
    show yuri 2c
    mc "Yeah, I started read some of it last night actually. It was pretty interesting!"
    "That wasn't completely true, I did read, but I read it during class..."
    "I wouldn't want to give Yuri the impression that I'm a slacker..."
    mc "I think I understand the story a little bit better now too!"
    y 2j "Well I'm glad you got to read it!"
    y 2b "How far did you get in?"
    mc "I just about finished up the second chapter."
    show yuri 2q
    y "Well, if still want to we could..."
    y 4a "Read together..."
    show yuri 4b
    "Yuri looks off in her usual flustered manner."
    show yuri 4e
    mc "You know I'd love to Yuri!"
    mc "And we were just about to do it yesterday anyways."
    y "Oh, right...{w=0.38}how silly of me."
    show yuri 2q
    "I sit down next to Yuri."
    mc "So how do we actually do this?"
    y 2e "Well, I was just thinking I hold one side of the book and you hold the other."
    mc "Yeah...{w=0.38}good thinking, Yuri!"
    "I shoot Yuri a warm smile{w=0.68}{nw}"
    stop music fadeout 4.0
    show yuri 4e
    "I shoot Yuri a warm smile{fast}, which immediately causes her to blush."
    mc "Well, let's get reading!"
    show yuri 2s
    "Yuri nods approvingly at me as we begin to read chapter three."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    play music e5
    show yuri 2d zorder 1 at t11
    "It was a little awkward at first but Yuri and I end up setting up a good system."
    "Whenever I got done with a page, I'd use my thumb to flip the page and Yuri would catch it with her fingers and put it to the side."
    show yuri 2o
    "After reading for a few minutes, I see Yuri shifting unconfortably in her seat."
    mc "Everything good, Yuri?"
    show yuri 1q zorder 1 at t11
    y "Yeah, it's just that my posture isn't too good right now."
    "Her 'posture'?."
    "..."
    "Oh..."
    "How did I miss that before?"
    mc "Do you want to move somewhere else?"


y 2t "I mean...{w=0.38}if you're comfortable here I don't mind...."
mc "Yuri, I don't want you to be uncomfortable if sitting like this is going to make your back ache."
show yuri 3p
mc "I really don't mind where we read as long as we're together."

if encore_sayoriquestion_1 == True:
    "Oh..."
    show yuri 4c
    "I don't think I should've put it like that..."
    mc "Yeah...{w=0.38}let's just sit down..."
    y "O-{w=0.38}okay..."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    "Yuri and I take our seats under the windowsill."
    "I'll admit, I'm not used to sitting here..."
    "But it feels kind of nice..."

if encore_sayoriquestion_1 == False:
    "Oh..."
    show yuri 4c
    "Might've been a little too forward there..."
    "Yuri is completely caught off guard and frantically fiddles with her hair as she figures out how to respond."
    mc "Yeah...{w=0.38}let's just sit down..."
    y "O-{w=0.38}okay..."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    "Yuri and I take our seats under the windowsill."
    "Ironically enough, we actually sat here before..."
    "For the exact same reason..."
    "I don't mind it though, I enjoy being like this with Yuri."


"Yuri hands me the book as she peers over my shoulder to read."
mc "Do you feel better now?"
show yuri 2o zorder 1 at t11
y "Yeah I do...{w=0.38}I can't really see the book though..."
mc "Oh! My bad."
"I try bringing the book closer to Yuri, but it makes makes my arm feel awkward."
stop music fadeout 1.0
y 1f "Let me try something."
"Yuri pushes the book back towards me."
mc "Oh?"
show yuri at thide
hide yuri
show cg y_cg_1 with dissolve_cg
play sound "sfx/fall.ogg"
"She then puts her head on my shoulder."
"I immediately feel the blood rush to my face as I'm filled with shock."
"Not that I don't mind Yuri doing that, but the fact that she actually went out of her comfort zone to do this astonishes me."
y "This isn't too distracting for you...{w=0.38}right?"
mc "Oh no...{w=0.38}not at all..."
mc "I actually kind of like this..."
"Yuri looks off and blushes."
"She regains her composure and looks back at me."
y "Good...{w=0.38}I was hoping you wouldn't find me weird for doing this."
mc "I like it when you're expressive, you should do it more."
"Yuri lets out a small giggle."
y "Well, if you want me too...{w=0.38}I will..."
mc "Noted."
"With our banter aside, we pick up where we left off."
play music t8 fadein 1.0
hide cg y_cg_1 with wipeleft_scene
"The chapter actually turns out to be the best one yet!"
"In the chapter, the main character, this girl named Libitina, is given a second chance to repair her broken relationship with her Uncle, who she's currently living with."
"Most of the chapter is told through a monologue as Libitina internally debates if it's worth repairing her relationship with her uncle..."
"As she's on the run from a league of escapees who want her back in order to complete some 'ritual'."
"It's quite interesting actually, and through her logic, she knows mending fences with her Uncle is the right thing to do..."
"She knows that she might not get another chance to make him happy...{w=0.38}but she doesn't know if it's even worth it in the long run..."
"After a while we reach the end of the chapter, with Libitina deciding to talk to her friend about what she should do."
show yuri 1h zorder 1 at t11
y "Do you think she'll do it, [player]?"
mc "Hmmm?"
y 1f "Do you think Libitina will end up making things right with her Uncle?"
mc "I mean, I hope she does."
show yuri 1e
mc "Very rarely do people get a second chance to do the right thing."
mc "If I was her, I'd take it."
y 2j "Y-{w=0.38}yeah...{w=0.38}me too..."
show yuri 1u
"We sit for the next few moments in silence, unsure of what to do next."
show yuri 3k
"Yuri seems to be deep in thought."
show yuri 3l
"She takes a deep breath and turns to face me again."
stop music fadeout 2.5
y 1s "I'm really glad we get to spend time like this, [player]."
mc "Yeah, me too!"
show yuri 1q
y "And..."
show yuri 2o
"Yuri hesitates."
mc "And what?"
play music t9 fadein 3.0
y 1t "I'm glad that you've given me a chance..."
"I hear Yuri's voice break as she says that, but she continues to press on, sounding like she's trying to fight back tears."
y 1v "Truth is, I haven't had real friend in years..."
y 2q "Not since Middle School has anyone treated me like an actual person..."
y 2w "I've honestly almost forgotten what it was like to enjoy being with someone who cares about you..."
"I feel my heart sink into my chest as she says that."

if encore_festivalquestion_2 == "Yuri":
    "Yuri did mention to me a few weeks ago that she usually spends all her time alone, but, I never knew she's been alone for so long."
    y 3s "And so...{w=0.38}it means a lot to me that we finally got to spend time together again..."

if encore_festivalquestion_2 == "Natsuki":
    "I always knew Yuri was introverted, but I never thought she had it that bad..."
    y 3s "And so...{w=0.38}it means a lot to me that we finally get to spend time together..."


show yuri 3p at h11
"Without thinking, I take Yuri's hand and lean in to her."
show yuri 3s at face with dissolve
"Yuri looks up to me, her violet eyes being reflective in the sunlight."
"I see a smile slowly forming across her face."
mc "Yuri..."
mc "You don't have to be alone anymore."
show yuri 4e
"Yuri's face turns full crimson."
y 3t "[player]...{w=0.38}I..."
"Yuri squeezes my hand tightly."
show yuri 3q
"We struggle to make eye contact for longer than a few seconds."

if encore_sayoriquestion_1 == True:
    "I quickly realize the situation I've put myself into."
    "This doesn't feel right..."
    "How would Sayori react if she found us like this?"
    show yuri 3s
    "And I don't think I can exactly get out of this situation without making Yuri feel self-conscious..."
    "Maybe nobody's seen us like this yet?"




if encore_sayoriquestion_1 == False:
    "I try to muster up the courage to keep talking."
    "But for some reason...{w=0.38}I can't..."
    "We're just intently looking at each other, both stammering as we try to find what we want to say to each other."
    show yuri 3s
    "I feel Yuri's gentle breaths brush against my face as she slowly leans in as well."
    "This feels like heaven."
    "But, I really don't know what to do."
    "This is the perfect opportunity for me to make progress with Yuri..."
    "Significant progress..."
    "But...{w=0.38}I'm afraid that someone's gonna catch us and immediately get the wrong idea..."



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

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        "What do I do?"
        show yuri 1w
        "What can I do?"
        "If I pull away now, Yuri will get self-conscious and will freak out..."
        "But if I don't pull away...{w=0.38}one thing could lead to another and that wouldn't be right..."
        "Instead I just opt to stay still and maybe Yuri doesn't do anything..."
        "I can't really blame her...{w=0.38} she doesn't know about Sayori yet..."
        "And we were in pretty much the same situation last Sunday..."
        show yuri 1s
        y "[player]..."

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        "What do I do?"
        show yuri 1w
        "What can I do?"
        "If I pull away now, Yuri will get self-conscious and will freak out..."
        "But if I don't pull away...{w=0.38}one thing could lead to another and that wouldn't be right..."
        "Instead I just opt to stay still and maybe Yuri doesn't do anything..."
        "I can't really blame her...{w=0.38} she doesn't know about Sayori yet..."
        "I don't think Yuri would actually kiss me..."
        show yuri 1s
        y "[player]..."


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
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

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        "Is this it?"
        show yuri 1w
        "Is this my chance to finally make a move on Yuri?"
        "I mean we're already so close..."
        "Though is she really about to-"
        show yuri 1s
        y "[player]..."





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
"Yuri and I were really just about to..."
"And the position we're in really doesn't make it any easier to explain..."
show natsuki 5f
show monika 1h
show sayori 1i
"All 3 girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show monika at thide
hide monika
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
mc "Um...{w=0.38}Yuri?"
show yuri 1n at face with dissolve
"Yuri snaps out of her gaze."
y "Y-{w=0.38}yeah? What's wrong?"
mc "We kinda have to get up..."
show monika 1c zorder 4 at t42
show natsuki 5g zorder 1 at t43
show sayori 1i zorder 2 at t41
show yuri 2e zorder 3 at t44
"Yuri turns to face the front of the room and she sees Monika, Sayori and Natsuki staring at us."
show yuri 3p
pause 0.7
show yuri 4c
"Yuri immediately stands up and brushes herself off, clearly embarrassed."
y "Oh my gosh, I'm so sorry everyone!"
y "I-{w=0.38}I didn't mean for you guys to see us like that and..."
show sayori 1k
show monika 1p
show natsuki 5u
"Monika, Natsuki and Sayori all look off in different directions, trying to avoid making the situation even more awkward then it already is..."
show monika 1e
"Eventually, Monika speaks up."
m 2b "It's alright, Yuri, come on."
"She gestures for us to come toward the front of the room."
show yuri at thide
hide yuri
"Yuri briskly walks to the front and takes her usual spot."
show monika at thide
hide monika
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
"I stand up as well and make my way to the room, joining the rest of the group."

if encore_sayoriquestion_1 == True:
    jump day2_caught_y


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump day2_angry_sy

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki" or hangout1 == "Monika" or hangout1 == "Yuri":
            jump day2_angry_ny





label yur_first:
"I spot her in her usual spot at the front of the room."
"I tepidly approach her as she seems to be absorbed into her book."
show yuri 1e at t11
"However, she quickly spots me heading her way."
show yuri 1b
y "Oh! Hello, [player]!"
show yuri 1q
y "H-{w=0.38}how're you doing today?"
"Despite Yuri's warm smile, she still seems surprised that I came to see her."


if hangout1 == "Sayori" or hangout1 == "Natsuki":
    "Especially considering how she was yesterday..."

if hangout1 == "Monika":
    pass

mc "Hey, Yuri! What's up?"
show yuri 1l at t11
"Yuri quickly composes herself."
y 1b "Oh, just reading some Portrait of Markov."
show yuri 1c
"Yuri proudly shows me the cover of the book."
"There's a familar ominous-looking eye symbol on the front cover."
mc "Oh yeah! Isn't that the horror novel you gave me a couple of weeks ago?"
show yuri 1f
y "Why yes, yes it is."
y "Have you had the chance to read it yet?"
"Well..."
"I did read it, but I might've forgotten what it was about..."
mc "I've read up to the first chapter."
show yuri 1e
y "What do you think of it so far?"
mc "I mean, so far it's been decent, though I'm a little confused with the story so far."
mc "It looks promising so far though, so I'm holding out that it'll get better."
show yuri 1c
y "Well I can assure you, [player], the more you read, the more you'll learn and fall in love with the story."
mc "Well, it sounds like I should read it more!"
mc "Though, I'll admit, I haven't really had the time to read it lately."
y 1e "Would you like a refresher on what the book is about?"
mc "I think that'd be helpful."
mc "I do remember it has something to do with human experimentation..."
show yuri 4c
"Yuri nervously looks off."
y "Y-{w=0.38}yeah...{w=0.38}it is a focal point in this novel..."
y "Are you not comfortable with reading something that's about that sort of thing?"
mc "I mean, it's not often that I do read something that revolves around a plot point like that."
mc "Its not going to scare me off from reading it."
show yuri 1k
"Yuri sighs with relief."
show yuri 1s
y "Well that's good! Usually when I explain the plot to someone, it scares them off."
mc "What was the plot again?"
y 1j "It's about this girl in high school who moves in with her long-lost younger sister..."
y 1l "But as soon as she does so, her life gets really strange."
mc "How so?"
y 1b "She gets targeted by these people who escaped from a human experiment prison..."
y 1k "And while her life is in danger, she needs to desperately choose who to trust."
"Ah, it's one of those kinds of novels..."
"The kind that seems to have a normal story for the first few chapters and then has a messed up twist and everything goes to hell..."
"That reminds me of a story actually..."
show yuri 3d
y "It's a really great novel! It's one of my favorites!"
mc "Well, if that's the case, mind if I join you?"
show yuri 4c
"Yuri's face starts turning a bright shade of red."

if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori" or  hangout1 == "Natsuki" or  hangout1 == "Monika":
        y "Oh...{w=0.38}I wouldn't want to pull you away from [hangout1] or anything like that!"
        mc "Nah, you aren't, she's fine."
        "Right?"
        show yuri at thide
        hide yuri


    if hangout1 == "Sayori":
        show sayori 1k at t11 zorder 2
        "I glance over to Sayori who appears to be spacing out."
        "Ah, she’ll be fine for a few minutes…"
        show sayori at thide
        hide sayori


    if hangout1 == "Natsuki":
        show natsuki 1s at t11 zorder 2
        "I glance over to Natsuki who appears to organzing her manga again."
        "Ah, she’ll be fine for a few minutes…"
        show natsuki at thide
        hide natsuki



    if hangout1 == "Monika":
        show monika 1c at t11 zorder 2
        "I glance over to Monika who appears to be writing something."
        "Ah, she seems busy..."
        show monika 1q
        $ style.say_dialogue = style.edited
        "{cps=25}I'm really not...{nw}"
        $ style.say_dialogue = style.normal
        show monika 1c
        "I wouldn't want to disturb her..."
        show monika at thide
        hide monika



show yuri 4c at t11
mc "Afterall, you did say you wanted us to read together yesterday."

if encore_festivalquestion_2 == "Yuri":
    mc "And it's been ages since the fesitval..."
    y 2q "Yeah...{w=0.38}I did...{w=0.38}and you're right..."

if encore_festivalquestion_2 == "Natsuki":
    mc "And I've always wanted to get to know you better..."
    y 2q "I-{w=0.38}I see..."



"I take a seat right next to Yuri."
show yuri 4c
y "Ah...!"
mc "You alright?"
y "Y-{w=0.38}yeah, I'm fine!"
y "It's just that...{w=0.38}I'm not used to reading in the company of another person."
mc "Ah, well let me know if I end up distracting you or anything."
y "A-{w=0.38}alright..."
show yuri 2t
y "Do you have the copy I gave you?"
mc "Ah, I left it at home..."
mc "Sorry..."
show yuri 3q
y "N{w=0.38}-no, it's fine...{w=0.38}if you want..."
show yuri 4c
y "Uuuuu....."
"Yuri's voice trails off as if she seems embarrassed to say what's on her mind."
mc "What is it?"
y "Well...{w=0.38}it's a bit of a weird idea..."
mc "I won't judge you, I promise."
show yuri 3o
y "O{w=0.38}-okay..."
y "Well..."
show yuri 3n
y "Do you both want to share the same copy?"
"I don't see how that's a weird idea..."
mc "Yeah, sure! It works for me."
show yuri 2q
y "O-{w=0.38}okay..."
"Yuri puts the book between us."
show yuri 2h
y "It's kind of hard to see..."
show yuri 2e
"Yuri leans towards me, I feel her arm pressed against mine."
"I guess this is what she meant..."
"It feels like my left arm is in the way, and I have to use my right to hold the book."
mc "Ah, I guess it'll be hard to turn the page..."
show yuri 2f
y "Here..."
"Yuri takes her left arm and holds the left side of the book between her thumb and forefinger."
"I still don't know where to put my left arm though...."
"There really isn't a good spot for me to put it..."

if encore_sayoriquestion_1 == False:
    "I would think about wrapping my arm around her, but that probably wouldn't be a good idea..."

if encore_sayoriquestion_1 == True:
    "If I was in this situation with Sayori, I'd probably wrap my arm around her..."
    "But something tells me I probably shouldn't try that on Yuri..."


"Ah, I'll just suffer through it..."
show yuri 2b
stop music fadeout 2.0
y "Ready to begin, [player]?"
mc "Yeah, let's get started!"
show yuri 2c
"Yuri manges a cheerful grin and we begin reading."
show yuri at thide
hide yuri
with wipeleft_scene
play music e5
show yuri 1h at t11
"After reading for a few minutes I see Yuri start to move around in her seat as if she were uncomfortable."
mc "Everything good, Yuri?"
show yuri 1q at t11
y "Yeah, it's just that my posture isn't too good right now."
"Her ‘posture'?"
"My eyes can't help but glance at Yuri's..."
"Oh..."
"How did I miss that?"
"Yeah...{w=0.38} I can see how that can be an issue for her...."
"And me."

if hangout1 == "Monika":
    $ style.say_dialogue = style.edited
    "{cps=25}She probably stuffs her chest...{nw}"
    $ style.say_dialogue = style.normal



if hangout1 == "Sayori" or  hangout1 == "Natsuki" or hangout1 == "Monika":
    pass

mc "Maybe we should move to a better spot?"
y "I mean...{w=0.38}if you're comfortable here I don't mind...."
mc "Yuri, I don't want you to be uncomfortable if sitting like this is going to make your back ache."
show yuri 3p
mc "I really don't mind where we read as long as we're together."



if encore_sayoriquestion_1 == True:
    "Oh..."
    show yuri 4c
    "I don't think I should've put it like that..."
    mc "Yeah...{w=0.38}let's just sit down..."
    y "O-{w=0.38}okay..."
    "I see Yuri crack a small smile."

if encore_sayoriquestion_1 == False:
    "Oh..."
    show yuri 4c
    "Might've been a little too forward there..."
    "Yuri is completely caught off guard and frantically fiddles with her hair as she figures out how to respond."
    mc "Yeah...{w=0.38}let's just sit down..."
    y "O-{w=0.38}okay..."
    "I see Yuri crack a small smile."


y 4e "I think I might know a good spot."
"Yuri leads me to the windowsill where we take our seats."
show yuri at thide
hide yuri
scene bg club_day with wipeleft_scene
show yuri 1a at t11
"Oddly enough, I find it enjoyable to be next to Yuri."
show yuri 3q
"Yeah, she might be a slow talker and have strange mannerisms..."
show yuri 3c
"But overall, she's pretty fun to be around."
show yuri 2e
"Derailing my train of thought, Yuri hands me the book as she peers over my shoulder to read the book."
mc "Do you feel better now?"
show yuri 2o zorder 1 at t11
mc "Oh, my bad."
"I try bringing the book closer to Yuri, but it makes makes my arm feel awkward."
stop music fadeout 1.0
y 1f "Let me try something."
"Yuri pushes the book back towards me."
mc "Oh?"
show yuri at thide
hide yuri
show cg y_cg_1 with dissolve_cg
play sound "sfx/fall.ogg"
"She then puts her head on my shoulder."
"I immediately feel the blood rush to my face as I'm filled with shock."
"Not that I don't mind Yuri doing that, but the fact that she actually went out of her comfort zone to do this astonishes me."
y "This isn't too distracting for you...{w=0.38}right?"
mc "Oh no...{w=0.38}not at all..."
mc "I actually kind of like this..."
"Yuri looks off and blushes."
"She regains her composure and looks back at me."
y "Good...{w=0.38}I was hoping you wouldn't find me weird for doing this."
mc "I like it when you're expressive, you should do it more."
"Yuri lets out a small giggle."
y "Well, if you want me too...{w=0.38}I will..."
mc "Noted."
"With our banter aside, we pick up where we left off."
play music t8 fadein 1.0
hide cg y_cg_1 with wipeleft_scene
"The chapter actually turns out to be the best one yet!"
"In the chapter, the main character, this girl named Libitina, is given a second chance to repair her broken relationship with her Uncle, who she's currently living with."
"Most of the chapter is told through a monologue as Libitina internally debates if it's worth repairing her relationship with her uncle..."
"As she's on the run from a league of escapees who want her back in order to complete some 'ritual'."
"It's quite interesting actually, and through her logic, she knows mending fences with her Uncle is the right thing to do..."
"She knows that she might not get another chance to make him happy...{w=0.38}but she doesn't know if it's even worth it in the long run..."
"After a while we reach the end of the chapter, with Libitina deciding to talk to her friend about what she should do."

if hangout1 == "Monika":
    $ style.say_dialogue = style.edited
    "{cps=25}Pretty lame...{nw}"
    $ style.say_dialogue = style.normal

if hangout1 == "Sayori" or  hangout1 == "Natsuki" or hangout1 == "Monika":
    pass

show yuri 1h zorder 1 at t11
y "Do you think she'll do it, [player]?"
mc "Hmmm?"
y 1f "Do you think Libitina will end up making things right with her Uncle?"
mc "I mean, I hope she does."
show yuri 1e
mc "Very rarely do people get a second chance to do the right thing."
mc "If I was her, I'd take it."
y 2j "Y-{w=0.38}yeah...{w=0.38}me too..."
show yuri 1u
"We sit for the next few moments in silence, unsure of what to do next."
show yuri 3k
"Yuri seems to be deep in thought."
show yuri 3l
"She takes a deep breath and turns to face me again."
stop music fadeout 2.5
y 1s "I'm really glad we get to spend time like this, [player]."
mc "Yeah, me too!"
show yuri 1q
y "And..."

if hangout1 == "Monika":
    $ style.say_dialogue = style.edited
    show yuri 2y4
    "{cps=45}I'M GOING TO CUT YOU OPEN AND HARVEST YOUR ORGANS{nw}"
    $ style.say_dialogue = style.normal

if hangout1 == "Sayori" or  hangout1 == "Natsuki" or hangout1 == "Yuri":
    pass

show yuri 2o
"Yuri hesitates."
mc "And what?"
play music t9 fadein 3.0
y 1t "I'm glad you've given me a chance..."
"I hear Yuri's voice break as she says that, but she continues to press on, sounding like she's trying to fight back tears."
y 1v "Truth is, I haven't had real friend in years..."
y "I've usally just spent all my time by myself reading..."
y 2q "And not since Middle School has anyone treated me positively..."
y 2w "I've honestly almost forgotten what it was like to enjoy being with someone with similar interests..."
"I feel my heart sink into my chest as she says that."


if encore_festivalquestion_2 == "Yuri":
    "Yuri did mention to me a few weeks ago that she usually spends all her time alone, but, I never knew she's been alone for so long."
    y 3s "And so...{w=0.38}it means a lot to me that we finally got to spend time together again..."


if encore_festivalquestion_2 == "Natsuki":
    "I always knew Yuri was introverted, but I never thought she had it that bad..."
    y 3s "And so...{w=0.38}it means a lot to me that we finally get to spend time together..."



show yuri 3p at h11
"Without thinking, I take Yuri's hand and lean in to her."
show yuri 3s at face with dissolve
"Yuri looks up to me, her violet eyes being reflective in the sunlight."
"I see a smile slowly forming across her face."
mc "Yuri..."
mc "You don't have to be alone anymore."
show yuri 4e
"Yuri's face turns full crimson."
y 3t "[player]...{w=0.38}I..."
"Yuri squeezes my hand tightly."
show yuri 3q
"We struggle to make eye contact for longer than a few seconds."

if encore_sayoriquestion_1 == True:
    "I quickly realize the situation I've put myself into."
    "This doesn't feel right..."
    "How would Sayori react if she found us like this?"
    show yuri 3s
    "And I don't think I can exactly get out of this situation without making Yuri feel self-conscious..."
    "Maybe nobody's seen us like this yet?"




if encore_sayoriquestion_1 == False:
    "I try to muster up the courage to keep talking."
    "But for some reason...{w=0.38}I can't..."
    "We're just intently looking at each other, both stammering as we try to find what we want to say to each other."
    show yuri 3s
    "I feel Yuri's gentle breaths brush against my face as she slowly leans in as well."
    "This feels like heaven."
    "But, I really don't know what to do."
    "This is the perfect opportunity for me to make progress with Yuri..."
    "Significant progress..."
    "But...{w=0.38}I'm afraid that someone's gonna catch us and immediately get the wrong idea..."



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

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        "What do I do?"
        show yuri 1w
        "What can I do?"
        "If I pull away now, Yuri will get self-conscious and will freak out..."
        "But if I don't pull away...{w=0.38}one thing could lead to another and that wouldn't be right..."
        "Instead I just opt to stay still and maybe Yuri doesn't do anything..."
        "I can't really blame her...{w=0.38} she doesn't know about Sayori yet..."
        "And we were in pretty much the same situation last Sunday..."
        show yuri 1s
        y "[player]..."

        if hangout1 == "Monika":
            $ style.say_dialogue = style.edited
            show yuri 2y3
            "{cps=35}I'M GOING TO CUT MYSELF TONIGHT AND THINK OF YOU{nw}"
            $ style.say_dialogue = style.normal

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        "What do I do?"
        show yuri 1w
        "What can I do?"
        "If I pull away now, Yuri will get self-conscious and will freak out..."
        "But if I don't pull away...{w=0.38}one thing could lead to another and that wouldn't be right..."
        "Instead I just opt to stay still and maybe Yuri doesn't do anything..."
        "I can't really blame her...{w=0.38} she doesn't know about Sayori yet..."
        "I don't think Yuri would actually kiss me..."
        show yuri 1s
        y "[player]..."

        if hangout1 == "Monika":
            $ style.say_dialogue = style.edited
            show yuri 2y4
            "{cps=35}I'M GOING TO CUT MYSELF TONIGHT AND THINK OF YOU{nw}"
            $ style.say_dialogue = style.normal


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
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

        if hangout1 == "Monika":
            $ style.say_dialogue = style.edited
            "{cps=35}AND NOTHING WILL HAPPEN AS LONG AS I'M IN CONTROL!{nw}"
            $ style.say_dialogue = style.normal

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        "Is this it?"
        show yuri 1w
        "Is this my chance to finally make a move on Yuri?"
        "I mean we're already so close..."
        "Though is she really about to-"
        show yuri 1s
        y "[player]..."

        if hangout1 == "Monika":
            $ style.say_dialogue = style.edited
            show yuri 2y3
            "{cps=35}I'M GOING TO CUT MYSELF TONIGHT AND THINK OF YOU{nw}"
            $ style.say_dialogue = style.normal





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
"Yuri and I were really just about to..."
"And the position we're in really doesn't make it any easier to explain..."
show natsuki 5f
show monika 1h
show sayori 1i
"All 3 girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show monika at thide
hide monika
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
mc "Um...{w=0.38}Yuri?"
show yuri 1n at face with dissolve
"Yuri snaps out of her gaze."
y "Y-{w=0.38}yeah? What's wrong?"
mc "We kinda have to get up..."
show monika 1c zorder 4 at t42
show natsuki 5g zorder 1 at t43
show sayori 1i zorder 2 at t41
show yuri 2e zorder 3 at t44
"Yuri turns to face the front of the room and she sees Monika, Sayori and Natsuki staring at us."
show yuri 3p
pause 0.7
show yuri 4c
"Yuri immediately stands up and brushes herself off, clearly embarrassed."
y "Oh my gosh, I'm so sorry everyone!"
y "I-{w=0.38}I didn't mean for you guys to see us like that and..."
show sayori 1k
show monika 1p
show natsuki 5u
"Monika, Natsuki and Sayori all look off in different directions, trying to avoid making the situation even more awkward then it already is..."
show monika 1e
"Eventually, Monika speaks up."
m 2b "It's alright, Yuri, come on."
"She gestures for us to come toward the front of the room."
show yuri at thide
hide yuri
"Yuri briskly walks to the front and takes her usual spot."
show monika at thide
hide monika
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
"I stand up as well and make my way to the room, joining the rest of the group."









if encore_sayoriquestion_1 == True:
    jump day2_caught_y

    label day2_caught_y:
        show sayori 1i at t11 zorder 2
        "While on my way to the front of the room, Sayori stops me."
        "Oh no..."
        mc "H-{w=0.38}hey Sayo-"
        s 1j "What was that about, [player]?"
        "Sayori sternly looks at me, a mix of pain and anger building up in her eyes."
        mc "Uh…"
        "How do I explain this to her?"

        menu:
            "Should I..."
            "Apologize.":
                $ apologize_sn = True
                jump sayori_sorry_y
            "Lie.":
                $ apologize_sn = False
                jump sayori_not_sorry_y

        label sayori_sorry_y:
        "I sigh to myself."
        "I might as well man up and apologize."
        mc "Sayori..."
        show sayori 1e
        mc "I’m sorry."
        mc "It was wrong of me to act in such a way and I promise you…"
        mc "I love you and only you."
        show sayori 1g
        mc "That was just a..."
        mc "...mistake..."
        mc "I promise it won't happen again."
        show sayori 1k
        "Sayori lets out a pained sigh before putting on a smile."
        show sayori 1l
        s "It’s alright, [player]."
        show sayori 1x
        s "I forgive you."
        show sayori 1r
        s "Come on, let’s not keep the others waiting!"
        jump day2_meettheclubs

        label sayori_not_sorry_y:
        "I don’t want Sayori to get the wrong idea about Yuri and I."
        "I try to come up with an excuse off the fly."
        mc "She was having trouble reading the book I was reading..."
        show sayori 1e
        mc "I was trying to give her a better…{w=0.38}angle for her to read..."
        mc "It was that and only that…{w=0.38}I promise…"
        show sayori 1k
        "Sayori lets out a heavy pained sigh before putting on a smile."
        show sayori 1l
        s "It’s alright, [player]."
        show sayori 1x
        s "I’m just glad you're being a good friend to her!"
        show sayori 1r
        s "Come on, let’s not keep the others waiting!"
        jump day2_meettheclubs


#Sayori Response 2.0

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump day2_angry_sy

        label day2_angry_sy:
        show sayori 2t at t11 zorder 1
        "While on my way to the front of the room, I see Sayori approach me."
        "She looks rather upset..."
        mc "Y-{w=0.38}yeah, Sayori?"
        s "So..."
        s "This is what false hope really feels like..."
        mc "W-{w=0.38}what?"
        mc "What do you mean?"
        s "I just hope you're happy with your choices, [player]."
        show sayori at thide
        hide sayori
        "Sayori turns and walks to the front of the room, doing her best to compose herself."
        "I take it she didn't take too kindly to me getting too close to Yuri like that."
        "I really need to be more careful around her..."
        "Though, Sayori was never the jealous type..."
        jump day2_meettheclubs


#Natsuki Response

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki" or hangout1 == "Monika" or hangout1 == "Yuri":
            jump day2_angry_ny



label day2_angry_ny:
    show natsuki 4g at t11 zorder 1
    "While on my way to the front of the room,{w=0.4}{nw}"
    $ _history_list.pop()
    play sound "sfx/smack.ogg"
    "While on the way to the front of the room,{fast} Natsuki gives me a \"friendly\" punch in the arm."
    mc "Ouch! Hey, what was that for?"
    n 5s "N-{w=0.38}Nothing...{w=0.38}dummy..."
    "She mutters that softly and avoids eye contact as she briskly walks past me."
    show natsuki at thide
    hide natsuki
    "Well, that was random."
    "I just hope she isn't jealous of me and Yuri getting so close like that."
    "Hopefully then, she won't full on put me in the hospital."
    "Oh well..."
    jump day2_meettheclubs
