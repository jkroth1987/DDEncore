#Day 1
label nencore_1:
    $ hangout1 = "Natsuki"
    "I decided to see what Natsuki was up to."
    scene bg closet
    with wipeleft_scene
    play music tnatsuki

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Natsuki":
        "I hear her utter an exasperated sigh from within the closet."
        "She seems to be annoyed by something."
        n "Ugh!"
        n "I swear if Monika cleans this closet one more time...{w=0.38} I will..."
        n "Why can she never put it back in the right spot?!?"
        n "I think I can reach that..."
        mc "Hey, Natsuki."
        show natsuki 1p at h11 zorder 1
        play sound "sfx/smack.ogg"
        n "EEEEH!"
        "In Natsuki’s miserable attempt to reach the top box, she ended up knocking down several books lined up on one of the lower shelves."
        n 4o "[player], don't sneak up to me like that!"
        mc "I’m sorry...{w=0.38}I didn’t mean to scare you like that."
        mc "I didn’t think you where that jumpy!"
        "I barley manage to contain my laughter."
        show natsuki 4f
        "Though that only makes Natsuki shoot me an irritated look."
        mc "What were you trying to do, anyways?"
        n 3r "I'm trying to get the top box that has my Parfait Girls set."
        n 3h "See the one with stickers on it?"
        "I look up to see the box Natsuki's refferring to."
        "Jeez...{w=0.38} how many rainbow stickers does one girl need?"
        mc "You know you just could have asked me to get it for you..."
        mc "I'm way taller than..."
        n 4w "BAKA! I can do it myself!"
        show natsuki 4x
        pause 0.7
        show natsuki u225212
        pause 0.7
        show natsuki 4n
        pause 0.7
        show natsuki 5u
        pause 0.7
        n 5t "Wait, could you get me the chair that I can stand on?"
        mc "You mean that swivel chair?"
        n 5c "Yeah, why?"
        mc "Remember the last time you got on that chair?"
        show natsuki 5o
        pause 0.7
        show natsuki 1v at h11
        n "I wasn't being careful enough! I'll be more careful this time!"
        mc "Yeah, I'd rather not have you fall on me again. Let me get something else this time."
        show natsuki 3h
        "I start to walk towards the front of the room where there's a sturdier chair that we can use."
        show natsuki 1i
        "Right before I can step out of the closest, I feel Natsuki grab my arm."
        n 2t "You didn't seem to mind when we got close last Sunday."
        "I stop dead in my tracks."
        "I feel the blood start to rush to my face."
        show natsuki u128211
        "I turn around to face Natsuki, who has a teasing look on her face."
        mc "That's only because you weren't calling me gross."
        show natsuki 1s
        "Natsuki's expression drops back to her signature pout."
        n 1q "You're impossible."
        mc "That makes two of us."
        show natsuki 1i
        "Natsuki and I gaze at each other before we realize how close our faces are too each other."
        show natsuki 4x
        "Natsuki suddenly lets go of my arm."
        n 4y "Go get the chair...{w=0.38} you dummy!"
        mc "Yes, your highness!"
        "I say that as sarcastically as I can."
        show black zorder 10 with wipeleft
        show natsuki u221232
        "I nonchalantly walk to the front of the room to retrieve the small chair."
        show natsuki 2u
        hide black with wipeleft
        "When I return with the chair, I see her defeated face."
        show natsuki 2c
        mc "You know I didn't mean that in an insulting way, right?"
        n 5e "I knew that, of course."
        n 5y "What? We're you afraid of offending poor little me?"
        mc "I..."
        "I don't know how I can honestly answer that..."
        n 3z "Hahaha~"
        n 1j "You make it too easy sometimes, [player]."
        mc "Yeah, yeah, just get the box."
        show natsuki 1g at h11
        "Natsuki places the chair before the shelf and steps onto it."
        show natsuki 4x
        "She reaches her arms out as far as she can..."
        show natsuki 1v at h11
        "But she still can't reach the top shelf."
        mc "Oh, just let me get it already."
        show natsuki 5s
        "Defeated again, Natsuki relcunatly steps off and crosses her arms."
        "I easily grab the box without the assistance of the chair."
        stop music fadeout 1.0
        scene bg club_day
        show natsuki 5g at t11 zorder 1
        with wipeleft_scene
        play music t4 fadein 1.0
        mc "Well, was that so hard?"
        n 5e "Oh, come on! I almost had it!"
        "Natsuki turns her attention to her box and begins searching through it."
        show natsuki at thide
        hide natsuki
        n "Got you now!"
        "She takes a manga book out of the box. The manga has a big 12 on the top right."
        show natsuki 2l at t11 zorder 1
        n "This one is the absolute best in the series! You should totally read this!"
        mc "Well, I'm only up to voulme 3. Are you telling me I have to wait for it get really good?"
        n 2k "I mean there's lots of good moments between those two. I just happen to think that volume 12 has some of the best writing in the whole series."
        mc "Well if you want to prove me right, we better get finished with volume 3 as soon as we can."
        show natsuki 1k at t22 zorder 1
        show yuri 3l at t21 zorder 2
        y "Um... hey, [player]..."
        "We turn around to unexpectingly see Yuri standing behind us."
        mc "Oh! Hey, Yuri! Didn't see you there!"
        y 1b "[player], could you come with me for a second?"
        n 3e "No, he can't! I was just going to start reading with him!"
        n 3g "Can't you wait?"
        y 1j "I really need to ask him something important, Natsuki."
        y 1r "You can afford to wait reading with him for at least a minute!"
        "Natsuki and I are caught offguard by Yuri's assertiveness."
        "It's very different from how she is normally..."
        show natsuki 1r
        "Natsuki can't even come up with anything to say back."
        "The only thing coming out of her mouth is a big-"
        n 4x "*sigh*"
        y 1d "I promise I won’t take long."
        "Yuri drags me way from Natsuki without me having the chance to say anything."
        show natsuki at thide
        hide natsuki
        show yuri at thide
        hide yuri
        scene bg club_day
        with wipeleft_scene
        show yuri 1b at t11 zorder 1

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Natsuki":
        y "So, [player]! How are you doing this afternoon?"
        mc "Oh, I'm doing alright, what about you?"
        y 3b "I'm doing great! I just got done finishing this chapter in my book and I was wondering if you'd like to...."
        y 4c "Maybe read it together sometime...."
        "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
        "She dragged me away from Natsuki for this?"
        "Well, I don’t get the chance to talk with Yuri much."
        "I guess she must be feeling left out that she hasn't talked to me for some reason."
        "I guess it’s up to me to try save her from embarrassment..."
        mc "Yeah, sure! I'd love to do some reading with you!"
        y 3y1 "Right now?!"
        "Her voice rings with excitement."
        "Woah, where did this excitement come from, Yuri?"
        mc "Um...{w=0.38} I don't know if we have the time for right now but maybe tomorrow we-"
        y 1y4 "But you're not doing anything right now, are you?"
        "Well, she does have a point there..."
        "But I must admit it's a surprise to see her being this forward."
        "She really didn’t need to drag me away from Natsuki."
        "And, I really feel like I should check on Sayori…"
        window hide(None)
        show yuri at t44
        show sayori 1k at t41 zorder 1
        pause 0.2
        window auto
        "I look over and see Sayori staring off into nothing."
        "She has a rather somber expression on her face."
        show sayori at thide
        hide sayori
        show yuri at t11
        mc "I'm gonna go see how Sayori is, we can read another time, okay?"
        show yuri 3t
        "Yuri gives me a dejected look."
        y "It-{w=0.28}it's fine, [player]. I won't take up anymore of your time."
        show yuri 4c
        "I see Yuri's face turn bright red as she swiftly and turns around and heads back to her desk."
        show yuri at thide
        hide yuri
        "I sigh to myself."
        "Man, what's with me today?"
        "First I offended Sayori, and now Yuri's upset with me."
        "I can only hope that this time things go better with Sayori..."
        stop music fadeout 1.0
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Natsuki":
        play music tnatsuki fadein 1.0
        "I hear her utter an exasperated sigh from within the closet."
        "She seems to be annoyed by something."
        n "Ugh!"
        n "I swear if Monika cleans this closet one more time...{w=0.38} I will..."
        n "Why can she never put it back in the right spot?!?"
        n "I think I can reach that..."
        mc "Hey, Natsuki."
        show natsuki 1p at h11 zorder 1
        play sound "sfx/smack.ogg"
        n "EEEEH!"
        "In Natsuki’s miserable attempt to reach the top box, she ended knocking down several books lined up on one of the lower shelves."
        n 4o "[player], don't sneak up to me like that!"
        mc "I’m sorry...{w=0.38}I didn’t mean to scare you like that."
        "I didn’t think you where that jumpy!"
        "I barley manage to contain my laughter."
        show natsuki 4f
        "Though that only makes Natsuki shoot me an irritated look."
        n 1i "Why are you here, anyways?"
        n 5y "Did Yuri finally realize how gross you are?"
        "I mean Yuri and I may be close now..."

        if encore_sayoriquestion_1 == False:
            "But Yuri certainly wouldn't mind me spending my time around the others,{w=0.38} right?"

        if encore_sayoriquestion_1 == True:
            "And I may be together with Sayori now..."
            "But Yuri certainly wouldn't mind me spending my time around the others,{w=0.38} right?"
            "I know Sayori wouldn't..."


        mc "What? Is it a crime if I spent just a little bit of time around you?"
        show natsuki 5s
        "Natsuki seems stumped at my retort as she struggles to articulate a response."
        "I decide to change the subject."
        mc "What were you trying to do, anyways?"
        n 3r "I'm trying to get the top box that has my Parfait Girls set."
        n 3h "See the one with stickers on it?"
        "I look up to see the box Natsuki's refferring to."
        "Jeez...{w=0.38} how many rainbow stickers does one girl need?"
        mc "You know you just could have asked me to get it for you..."
        mc "I'm way taller than..."
        n 4w "BAKA! I can do it myself!"
        show natsuki 4x
        pause 0.7
        show natsuki u225212
        pause 0.7
        show natsuki 4n
        pause 0.7
        show natsuki 5u
        pause 0.7
        n 5t "Wait, could you get me that chair that I can stand on?"
        "Natsuki points to the teacher's chair at the front of the room."
        mc "You want that chair?"
        n 5c "Yeah, why?"
        mc "It's a swivel chair, you'll probably fall off and land on me."
        show natsuki 5o
        pause 0.7
        show natsuki 1v at h11
        n "I'll be careful!"
        mc "Yeah...{w=0.38}I think I see something better that we can use..."
        show natsuki 3h
        "I start to walk towards the front of the room where there's a sturdier chair."
        show natsuki 1i
        "Right before I can step out of the closest, I feel Natsuki grab my arm."
        n 2t "Since when did you care so much about me?"
        "I stop dead in my tracks."
        "I feel the blood start to rush to my face."
        show natsuki u128211
        "I turn around to face Natsuki, who has a teasing look on her face."
        mc "Since when did you stop calling me gross?"
        show natsuki 1s
        "Natsuki's expression drops back to her signature pout."
        n 1q "You're impossible."
        mc "That makes two of us."
        show natsuki 1i
        "Natsuki and I gaze at each other before we realize how close our faces are too each other."
        show natsuki 4x
        "Natsuki suddenly lets go of my arm."
        n 4y "Go get the chair...{w=0.38} you dummy!"
        mc "Yes, your highness!"
        "I say that as sarcastically as I can."
        show black zorder 10 with wipeleft
        show natsuki u221232
        "I nonchalantly walk to the front of the room to retrieve the small chair."
        show natsuki 2u
        hide black with wipeleft
        "When I return with the chair, I see her defeated face."
        show natsuki 2c
        mc "You know I didn't mean that in an insulting way, right?"
        n 5e "I knew that, of course."
        n 5y "What? We're you afraid of offending poor little me?"
        mc "I..."
        "I don't know how I can honestly answer that..."
        n 3z "Hahaha~"
        n 1j "You make it too easy sometimes, [player]."
        mc "Yeah, yeah, just get the box."
        show natsuki 1g at h11
        "Natsuki places the chair before the shelf and steps onto it."
        show natsuki 4x
        "She reaches her arms out as far as she can..."
        show natsuki 1v at h11
        "But she still can't reach the top shelf."
        mc "Oh, just let me get it already."
        show natsuki 5s
        "Defeated again, Natsuki relcunatly steps off and crosses her arms."
        "I easily grab the box without the assistance of the chair."
        stop music fadeout 1.0
        scene bg club_day
        show natsuki 5g at t11 zorder 1
        with wipeleft_scene
        stop music fadeout 2
        mc "Well, was that so hard?"
        play music t4 fadein 1.0
        n 5e "Oh, come on! I almost had it!"
        "Natsuki turns her attention to her box and begins searching through it."
        show natsuki at thide
        hide natsuki
        n "Got you now!"
        "She takes a manga book out of the box. The manga has a big 12 on the top right."
        mc "What do you have there?"
        show natsuki 2l at t11 zorder 1
        n "What I'm holding right now is the best manga ever to have ever existed! You should totally read this!"
        mc "What's it called again?"
        n 2z "Parfait Girls!"
        "Never heard of it."
        "Still, I should probably give it a chance. It wouldn't hurt..."
        mc "Well, if you really recommend it, I'd be happy to read it with you."
        show natsuki 2k
        n "R-right now?"
        "I mean I'm not doing anything else right now..."
        mc "Sure! Why not?"
        show natsuki 1d
        n "That's great!"
        show natsuki 1t
        n "I mean..."
        n 1w "It's about time someone shows you what real literature looks like!"
        show natsuki 1k at t22 zorder 1
        show yuri 3l at t21 zorder 2
        y "Um...{w=0.38} hey, [player]..."
        "We turn around to unexpectingly see Yuri standing behind us."
        mc "Oh! Hey, Yuri! Didn't see you there!"
        y 1b "[player], could you come with me for a second?"
        n 3e "No, he can't! I was just going to start reading with him!"
        n 3g "Can't you wait?"
        y 1j "I really need to ask him something important, Natsuki."
        y 1r "You can afford to wait reading with him for at least a minute!"
        "Natsuki and I are caught offguard by Yuri's assertiveness."
        "It's very different from how she is normally..."
        show natsuki 1r
        "Natsuki can't even come up with anything to say back."
        "The only thing coming out of her mouth is a big-"
        n 4x "*sigh*"
        y 1d "I promise I won’t take long."
        "Yuri drags me way from Natsuki without me having the chance to say anything."
        show natsuki at thide
        hide natsuki
        show yuri at thide
        hide yuri
        scene bg club_day
        with wipeleft_scene
        show yuri 1b at t11 zorder 1


if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Natsuki":
        y "So, [player]! How have you been lately?"
        mc "Oh, I've doing alright, what about you?"
        y 3b "I'm doing great!"
        y 2b "I just got done finishing this chapter in Portrait of Markov and I was hoping that we could..."
        y 4c "Pick up where we left off..."
        "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
        "I didn't realize how much reading with Yuri meant to her..."
        "Well, I should promise to read with her again at some point..."
        mc "Yeah, sure! I'd love to do some reading with you!"
        y 3y1 "Right now?!?"
        "Her voice rings with excitement."
        "Woah, where did this excitement come from, Yuri?"
        mc "Well...{w=0.38} I don't think now is the best time. Maybe tomorrow we could-"
        y 1y4 "But you're not doing anything right now, are you?"
        "Well, I suppose she's right there..."
        "But I must admit it's a surprise to see her being this forward."
        "She really didn’t need to drag me away from Natsuki."
        "And, I really feel like I should check on Sayori…"
        window hide(None)
        show yuri at t44
        show sayori 1k at t41 zorder 1
        pause 0.2
        window auto
        "I look over and see Sayori staring off into nothing."
        "She has a rather somber expression on her face."
        show sayori at thide
        hide sayori
        show yuri at t11
        mc "I'm gonna go see how Sayori is, we can read another time, okay?"
        show yuri 3t
        "Yuri gives me a dejected look."
        y "O-{w=0.28}oh, I see [player]."
        show yuri 3w
        y "Perphaps another time?"
        show yuri 4c
        "I see Yuri's face turn bright red as she swiftly and turns around and heads back to her desk."
        show yuri at thide
        hide yuri
        "I sigh to myself."
        "Man, what's with me today?"
        "First I offended Sayori, and now Yuri's upset with me."
        "I can only hope that this time things go better with Sayori..."
        stop music fadeout 1.0
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
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
            s 1t "If I wasn't such a mess, you'd still be spending time with Natsuki, wouldn't you?"
            "I mean..."
            "I don't see spending some time around Natsuki as a bad thing..."
            "But maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourselves over there..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible girlfriend!"
            mc "No, you aren't Sayori...{w=0.38}don’t say that..."
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto mine."
            mc "Natsuki doesn't matter right now..."
            mc "Just us..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before Monika calls the group to attention."
            scene bg club_day
            show monika 4b at t22 zorder 2
            show sayori 1m at t21 zorder 1
            stop music
            m "Ok everyone, poem time!"
            s 1r "Oh yaaaaaay! Poem time!"
            "Sayori forces the biggest smile humanly possible."
            "That's gotta be the fakest reaction from Sayori that I've ever seen."
            show sayori at thide
            hide sayori
            show monika at thide
            hide monika
            "I just sigh to myself and walk over to my to my bag to retrieve my poem."
            with wipeleft_scene
            jump poem_scene7


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
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
            s 1t "If I wasn't such a mess, you'd still be spending time with Natsuki or Yuri, wouldn't you?"
            "I mean..."
            "I don't see spending some time around Natsuki or Yuri as a bad thing..."
            "But maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourself over there with Natsuki..."
            s "And how you were spending time with Yuri last Sunday..."
            s "And I ruined it for you!"
            s 1w "I'm a terrible girlfriend!"
            mc "No, you aren't Sayori...don’t say that..."
            scene black
            with Dissolve(1)
            "Sayori hugs me tightly."
            "I put my arms around her and close my eyes."
            "I can feel my heart beat in sync with Sayori’s."
            "I feel the warmth of her body radiate onto mine."
            mc "Natsuki doesn't matter right now..."
            mc "Just us..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before Monika calls the group to attention."
            scene bg club_day
            show monika 4b at t22 zorder 2
            show sayori 1m at t21 zorder 1
            stop music
            m "Ok everyone, poem time!"
            s 1r "Oh yaaaaaay! Poem time!"
            "Sayori forces the biggest smile humanly possible."
            "That's gotta be the fakest reaction from Sayori that I've ever seen."
            show sayori at thide
            hide sayori
            show monika at thide
            hide monika
            "I just sigh to myself and walk over to my to my bag to retrieve my poem."
            with wipeleft_scene
            jump poem_scene8






if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
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
            s 1t "If I wasn't such a mess, you'd still be spending time with Natsuki, wouldn't you?"
            s 1k "I can see why you like her so much..."
            s 1t "You deserve to have someone like her in your life..."
            s "I shouldn't be trying to keep you from her."
            "Maybe I should've come to Sayori sooner..."
            show sayori 1u
            "She's clearly been bottling this up for a while now..."
            s "Just the way you seemed to be enjoying yourself over there with Natsuki..."
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
            mc "Me spending time with Natsuki isn't going to make me forget about you, Sayori."
            mc "And I'm just trying to figure out everything just as much as you are..."
            mc "I should've come to you sooner, I'm sorry..."
            "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
            "We're like this for sometime before Monika calls the group to attention."
            scene bg club_day
            show monika 4b at t22 zorder 2
            show sayori 1m at t21 zorder 1
            stop music
            m "Ok everyone, poem time!"
            s 1r "Oh yaaaaaay! Poem time!"
            "Sayori forces the biggest smile humanly possible."
            "That's gotta be the fakest reaction from Sayori that I've ever seen."
            show sayori at thide
            hide sayori
            show monika at thide
            hide monika
            "I just sigh to myself and walk over to my to my bag to retrieve my poem."
            with wipeleft_scene
            jump poem_scene5

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
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
                s 1t "If I wasn't such a mess, you'd still be spending time with Natsuki or Yuri, wouldn't you?"
                s 1k "I can see why you like them so much..."
                s 1t "You deserve to have someone like them in your life..."
                s 1u "Natsuki with her baking..."
                s "And Yuri with her beauty..."
                s "I shouldn't be trying to keep you from them."
                "Maybe I should've come to Sayori sooner..."
                show sayori 1u
                "She's clearly been bottling this up for a while now..."
                s "Just the way you seemed to be enjoying yourself over there with Natsuki..."
                s "And how you were spending time with Yuri last Sunday..."
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
                mc "Me spending time with Natsuki or Yuri isn't going to make me forget about you, Sayori."
                mc "And I'm just trying to figure out everything just as much as you are..."
                mc "I should've come to you sooner, I'm sorry..."
                "I hear Sayori sniffle as she works to prevent herself from breaking down and sobbing..."
                "We're like this for sometime before Monika calls the group to attention."
                scene bg club_day
                show monika 4b at t22 zorder 2
                show sayori 1m at t21 zorder 1
                stop music
                m "Ok everyone, poem time!"
                s 1r "Oh yaaaaaay! Poem time!"
                "Sayori forces the biggest smile humanly possible."
                "That's gotta be the fakest reaction from Sayori that I've ever seen."
                show sayori at thide
                hide sayori
                show monika at thide
                hide monika
                "I just sigh to myself and walk over to my to my bag to retrieve my poem."
                with wipeleft_scene
                jump poem_scene6





                #Day 2
                label nencore_2:
                $ hangout2 = "Natsuki"
                "I decided to see what Natsuki is up to."
                stop music fadeout 1.0
                scene bg club_day
                with wipeleft_scene
                "Natsuki's in her usual spot by the closet at the back of the room reading Parfait Girls."
                play music t6 fadein 1.0
                mc "Hey, Natsuki."
                show natsuki 1p at h11 zorder 1
                "Natsuki jumps at hearing my voice."
                show natsuki 2e
                n "[player]! I thought I told you to stop scaring me like that!"
                mc "Oh come on! Where's the fun in that?"
                show natsuki 5s
                "Natsuki gives me her signature pout."
                n 5t "Yeah, I'd bet it'd be fun to see me drop dead."
                mc "Er...no...no, it wouldn't..."
                show natsuki xu2143
                "Natsuki lets out a laugh."
                n 2l "Oh, [player], sometimes you make this too easy on me."
                mc "Oh come on, you'd know I'd help you if it ever did come to that."
                n 2j "I don't doubt that."
                show natsuki u121143
                "She smiles sweetly at me."
                n 1k "Anyways... want to read some more Parfait Girls?"
                n 1h "Since...you know..."
                n 1i "We didn't get to finish last time."
                mc "You know it."
                n 2d "Great, wait here I'll grab the book."
                show natsuki at thide
                hide natsuki
                $ currentpos = get_pos()
                stop music fadeout 2.0
                "As I watch Natsuki disappear into the closet, I can't help but think back to the dream I had last night."
                "Before I can finish my thought I hear Natsuki calling me"
                n "Hey [player]!"
                n "Come over here! I need your help with something!"
                #Static
                #Heartbeat
                show vignette at vignettefade:
                    alpha 0.8
                show noise at noisefade:
                    alpha 0.5
                "My head starts to spin.."
                "This is just like the dream...I have the same feeling as last night...."
                "I don't want to go in there..."
                "What if..'it' happens again?"
                n "Come on, dummy! I don't have all day!"
                "I take a deep breath."
                play music hb
                show layer master at heartbeat
                "{i}Come on [player], it was just a stupid dream.{/i}"
                "I walk in and brace myself..."
                show layer master
                #Scene Transition
                scene bg closet
                with wipeleft_scene
                "But all I see is Natsuki struggling to grab a book."
                play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
                show natsuki 1c at t11 zorder 1
                n "Jeez! It took you long enough to get in here! What took so long?"
                mc "Sorry... spaced out there for a bit."
                "There's no chance in hell I'm telling Natsuki about my dream last night. She'll think I'm mental."
                n 2b "Well...hurry up and grab that one!"
                "She points to a special edition copy of Parfait Girls."
                "Unlike the normal copies of the series, this one is golden and reflective. It's one of those books that really grabs your attention if it's on a shelf somewhere."
                mc "Whatever you say, Natsuki."
                show natsuki 1a
                "I grab the book and we walk out of the closet and sit at our usual spot under the window."
                #Scene Transition
                scene n_cg1_bg
                show n_cg1_base
                with dissolve_cg
                play music e3
                n "You ready?"
                mc "Yeah... how come you wanted us to read the special edition this time?"
                n "This one has some exclusive art in it, not to mention it manages to pack volumes 3 through 6 into it!"
                mc "Wow that's awesome! Thanks Natsuki! You're really awesome to get your hands on something like this"
                "Natsuki blushes."
                show n_cg1_exp2 with dissolve
                n "Oh, don't mention it, come on start reading!"
                hide n_cg1_exp2 with dissolve
                show n_cg1_base with dissolve
                "We read for a bit when but before long I feel Natsuki start to wrap around my arm. At first I try to ignore it but it becomes distracting enough to the point where I can't read anymore."
                "I turn to my right and I see that Natsuki's not even looking at the book anymore."
                stop music fadeout 1.0
                "She's looking... into my eyes."
                mc "Umm...whatcha doing?"
                "Natsuki doesn't respond."
                show n_cg1_exp5 with dissolve
                "It seems as if she's in some kind of trance..."
                "I don't know what to do."
                "Sure, I don't mind being this close to Natsuki."
                "But I'm afraid that someone's gonna catch us and immediately get the wrong idea..."
                scene bg club_day
                with dissolve_cg
                show yuri 1g at t11 zorder 2
                "I glance around the room to see Yuri reading her book,{w=0.8}{nw}"
                show sayori 1k at t31 zorder 1
                show yuri at t33
                "I glance around the room to see Yuri reading her book,{fast} Sayori spacing out,{w=0.80}{nw}"
                show monika 1c at t32 zorder 3
                "I glance around the room to see Yuri reading her book, Sayori spacing out,{fast} and Monika working on something."
                show monika at thide
                hide monika
                show sayori at thide
                hide sayori
                show yuri at thide
                hide yuri
                show natsuki u114213 at t11 zorder 1
                "I then turn back to Natsuki, meeting her gaze."
                #show natsuki u114253 at f11
                play music t9 fadein 2.0
                play sound "sfx/fall.ogg"
                show cg n_cg_1 zorder 10 with dissolve_cg
                hide natsuki
                "Natsuki then suddenly embraces me tightly."
                "Her hug feels...warm..."
                "I naturally reciprocate, putting the manga down and wrapping both of my arms around her."
                "Natsuki moves to whisper in my ear."
                n u112253 "This feels nice, [player]."
                mc "It really does. I like it..."
                n u114214 "Promise me that we can always be like this?"
                "Natsuki's question catches me completely off guard. I wasn't expecting her to be this forward."
                "Still though..."
                "I wouldn't mind if we could always be like this..."
                #show natsuki at thide
                #hide natsuki
                stop music fadeout 1.0
                hide cg with dissolve_cg
                "Before I can answer, Monika stands up and walks to the front of the room."
                play music t5 fadein 1.0
                show monika 3b at t11 zorder 4
                m "Okay, everyone! Gather around! I have an important announcement to make!"
                show sayori 1b at t21 zorder 2
                show monika 1c at t22
                "Suddenly, Monika and Sayori's eyes turn to me and Natsuki."
                show yuri 3e at t33 zorder 3
                show sayori at t31
                show monika at t32
                "Yuri, confused as to what's going on, turns around..."
                show yuri u125111
                "Only to see what Monika and Natsuki are staring at."
                "Natsuki and I are practically cuddling at this point."
                show monika 1h
                show sayori 1i
                show yuri u123114
                "All 3 girls are looking at us, with a bit of an irritated...almost jealous...expression on their faces."
                "God Damn It."
                "Well, it's up to me to attempt to salvage this situation."
                show monika at thide
                hide monika
                show sayori at thide
                hide sayori
                show yuri at thide
                hide yuri
                "I subtly nudge Natsuki."
                mc "Um...hey...Natsuki."
                show natsuki 1n at t11 zorder 1
                "Natsuki looks up at me with a disoriented look, as if she really didn't want to move."
                mc "You...we kind of gotta get up."
                mc "Monika has an announcement to make."
                n u124212 "Ugh, do we have to?"
                n 2s "Why is it every time I try to spend time with you like this, it gets ruined?!?"
                "Natsuki might have said that last part too loudly."
                show natsuki u114213 at t44 zorder 4
                show monika 2c at t42 zorder 3
                show sayori 1i at t41 zorder 1
                show yuri u125111 at t43 zorder 2
                "She turns to see the other three looking at us."
                show natsuki 1p at h44 zorder 4
                "She turns as bright red as her hair ties."
                show natsuki at thide
                hide natsuki
                show sayori at t31
                show monika at t32
                show yuri at t33
                "She hurriedly stands up and storms to the front of the room, plopping into a seat and turns to look out the window, not wanting to make eye contact with any of us."
                show sayori 1q
                show monika 1j
                show yuri 1i
                "Sayori, Monika and Yuri all try to contain their laughter over what just happened but they're eventually able to compose themselves and start making their way to the front of the room."
                show sayori at thide
                hide sayori
                show monika at thide
                hide monika
                show yuri 1g at t11
                "While on my way to the front of the room, Yuri stops me."
                mc "Yeah, Yuri?"
                y 1q "N-nothing [player]. It was nothing important."
                "She mutters that softly and avoids eye contact as she briskly walks past me."
                show yuri at thide
                hide yuri
                "Well, that was random."
                "I just hope she isn't jealous of me and Natsuki getting so close like that."
                #Scene Transition
                jump day2_meettheclubs
