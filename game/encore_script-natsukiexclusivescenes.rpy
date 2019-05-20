#Day 1
label nencore_1:
    $ hangout1 = "Natsuki"
    "I decided to see what Natsuki was up to."
    scene bg closet
    with wipeleft_scene
    play music tnatsuki


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
    mc "I didn’t think you were that jumpy!"
    "I barely manage to contain my laughter."
    show natsuki 4f
    "Though that only makes Natsuki shoot me an irritated look."

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        pass # Temporary

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
            n 1i "Why are you here, anyway?"
            n 5y "Did Sayori finally realize how gross you are?"
            "Although, I may be with Sayori now..."
            "She wouldn't mind if I spent my time around someone else for the day,{w=0.38} right?"
            mc "What? Is it a crime if I spent just a little bit of time around you?"
            mc "Besides, it's been a while since the festival..."
            show natsuki 5s
            "Natsuki seems stumped at my retort as she struggles to articulate a response."
            "I decide to change the subject."

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        n 1i "Why are you here, anyway?"
        n 5y "Did Yuri finally realize how gross you are?"
        "I mean Yuri and I may be close..."
        "But she wouldn't mind if I spent my time around someone else for the day,{w=0.38} right?"
        mc "What? Is it a crime if I spent just a little bit of time around you?"
        show natsuki 5s
        "Natsuki seems stumped at my retort as she struggles to articulate a response."
        "I decide to change the subject."


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        n 1i "Why are you here, anyway?"
        n 5y "Did Yuri finally realize how gross you are?"
        "I mean Yuri and I may be close..."
        "And I may be together with Sayori now..."
        "But she wouldn't mind if I spent my time around someone else for the day,{w=0.38} right?"
        "I know Sayori wouldn't..."
        mc "What? Is it a crime if I spent just a little bit of time around you?"
        show natsuki 5s
        "Natsuki seems stumped at my retort as she struggles to articulate a response."
        "I decide to change the subject."




mc "What were you trying to do, anyway?"
n 3r "I'm trying to get the top box that has my manga."
n 3h "See the one with stickers on it?"
"I look up to see the box Natsuki's referring to."
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

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
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
        "Right before I can step out of the closest, Natsuki grabs my arm."
        n 2t "You didn't seem to mind when we got close last Sunday."
        "I stop dead in my tracks."
        "I feel the blood start to rush to my face."
        show natsuki u128211
        "I turn around to face Natsuki, who has a teasing look on her face."
        mc "That's only because you weren't calling me gross."

if encore_sayoriquestion_1 == False or encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        n 5t "Wait, I think we could use the teacher's chair for this!"
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
        "Right before I can step out of the closest, Natsuki grabs my arm."
        n 2t "Since when did you care so much about me?"
        "I stop dead in my tracks."
        "I feel the blood start to rush to my face."
        show natsuki u128211
        "I turn around to face Natsuki, who has a teasing look on her face."
        mc "Since when did you stop calling me gross?"

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        n 5t "Wait, I think we could use the teacher's chair for this!"
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
        "Right before I can step out of the closest, Natsuki grabs my arm."
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
"Natsuki and I gaze at each other before we realize how close our faces have gotten."
show natsuki 4x
"Natsuki suddenly lets go of my arm."
n 4y "Go get the chair...{w=0.38} you dummy!"
mc "Yes, your highness!"
show natsuki 4g
$ renpy.pause(delay=0.8, hard=True)
show natsuki at thide
hide natsuki
show bg class_day zorder 10 with wipeleft
"I nonchalantly walk to the front of the room to retrieve the small chair."
scene bg closet zorder 10 with wipeleft
scene bg closet
show natsuki 2u at t11 zorder 1
"When I return with the chair, I see her defeated face."
show natsuki 2c
mc "You know I didn't mean that in an insulting way, right?"
n 5e "I knew that, of course."
n 5y "What? Were you afraid of offending poor little me?"
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
"Defeated again, Natsuki reluctantly steps off and crosses her arms."
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


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
            mc "What do you have there?"
            show natsuki 2l at t11 zorder 1
            n "What I'm holding right now is the best manga in existence! You should totally read this!"
            mc "What's it called again?"
            n 2z "Parfait Girls!"
            "Never heard of it."
            "Still, I should probably give it a chance. It wouldn't hurt..."
            mc "Well, if you really recommend it, I'd be happy to read it with you."
            show natsuki 2k
            n "R-{w=0.38}right now?"
            "I mean I'm not doing anything else right now..."
            mc "Sure! Why not?"
            show natsuki 1d
            n "That's great!"
            show natsuki 1t
            n "I mean..."
            n 1w "It's about time someone shows you what real literature looks like!"
            show natsuki 1k at t22 zorder 1
            show yuri 3l at t21 zorder 2


if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False :
    if encore_festivalquestion_2 == "Yuri":
        mc "What do you have there?"
        show natsuki 2l at t11 zorder 1
        n "What I'm holding right now is the best manga in existence! You should totally read this!"
        mc "What's it called again?"
        n 2z "Parfait Girls!"
        "Never heard of it."
        "Still, I should probably give it a chance. It wouldn't hurt..."
        mc "Well, if you really recommend it, I'd be happy to read it with you."
        show natsuki 2k
        n "R-{w=0.38}right now?"
        "I mean I'm not doing anything else right now..."
        mc "Sure! Why not?"
        show natsuki 1d
        n "That's great!"
        show natsuki 1t
        n "I mean..."
        n 1w "It's about time someone shows you what real literature looks like!"
        show natsuki 1k at t22 zorder 1
        show yuri 3l at t21 zorder 2


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        show natsuki 2l at t11 zorder 1
        n "This one is the absolute best in the series! You should totally read this!"
        mc "Well, I'm only up to voulme 3. Are you telling me I have to wait for it to get really good?"
        n 2k "I mean there's lots of good moments between those two. I just happen to think that volume twelve has some of the best writing in the whole series."
        mc "Well if you want to prove me right, we better get finished with volume three as soon as we can."
        show natsuki 1k at t22 zorder 1
        show yuri 3l at t21 zorder 2



y "Um...{w=0.38}hey, [player]..."
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

#Yuri Interaction

if encore_sayoriquestion_1 == False or encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        y "So, [player]! How are you doing this afternoon?"
        mc "Oh, I'm doing alright, what about you?"
        y 3b "I'm doing great! I just got done finishing this chapter in my book and I was wondering if you'd like to...."
        y 4c "Maybe read it together sometime...."
        "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
        "She dragged me away from Natsuki for this?"
        "Well, I don’t get the chance to talk with Yuri much."
        "I guess she must be feeling left out that she hasn't talked to me for some reason."
        "I guess it’s up to me to try save Yuri from her own embarrassment..."
        mc "Yeah, sure! I'd love to do some reading with you!"
        stop music
        y 3y5 "Right now?!"
        "Her voice rings with excitement."
        "Woah, where did this excitement come from, Yuri?"
        mc "Um...{w=0.38} I don't know if we have the time for right now but maybe tomorrow we-"
        y 3y6 "But you're not doing anything right now, are you?"
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
        mc "I'm gonna go see how Sayori is. We can read another time, okay?"
        show yuri 3t
        "Yuri gives me a dejected look."
        y "It-{w=0.28}it's fine, [player]. I won't take up any more of your time."
        show yuri 4c
        "I see Yuri's face turn bright red as she swiftly turns around and heads back to her desk."
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
    if encore_festivalquestion_2 == "Yuri":
        y "So, [player]! How are you doing this afternoon?"
        mc "Oh, I'm doing alright, what about you?"
        y 3b "I'm doing great! I just got done finishing this chapter in my book and I was wondering if you'd like to...."
        y 4c "Maybe read it together sometime...."
        "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
        "She dragged me away from Natsuki for this?"
        "Well, I don’t get the chance to talk with Yuri much."
        "I guess she must be feeling left out that she hasn't talked to me for some reason."
        "I guess it’s up to me to try save Yuri from her own embarrassment..."
        mc "Yeah, sure! I'd love to do some reading with you!"
        stop music
        y 3y5 "Right now?!"
        "Her voice rings with excitement."
        "Woah, where did this excitement come from, Yuri?"
        mc "Um...{w=0.38} I don't know if we have the time for right now but maybe tomorrow we-"
        y 3y6 "But you're not doing anything right now, are you?"
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
        mc "I'm gonna go see how Sayori is. We can read another time, okay?"
        show yuri 3t
        "Yuri gives me a dejected look."
        y "It-{w=0.28}it's fine, [player]. I won't take up any more of your time."
        show yuri 4c
        "I see Yuri's face turn bright red as she swiftly turns around and heads back to her desk."
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

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        y "So, [player]! How have you been lately?"
        mc "Oh, I've been doing alright, what about you?"
        y 3b "I'm doing great!"
        y 2b "I just got done finishing this chapter in Portrait of Markov and I was hoping that we could..."
        y 4c "Pick up where we left off..."
        "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
        "I didn't realize how much reading with Yuri meant to her..."
        "Well, I should promise to read with her again at some point..."
        mc "Yeah, sure! I'd love to do some reading with you!"
        stop music
        y 3y5 "Right now?!?"
        "Her voice rings with excitement."
        "Woah, where did this excitement come from, Yuri?"
        mc "Well...{w=0.38} I don't think now is the best time. Maybe tomorrow we could-"
        y 3y6 "But you're not doing anything right now, are you?"
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
        mc "I'm gonna go see how Sayori is. We can read another time, okay?"
        show yuri 3t
        "Yuri gives me a dejected look."
        y "O-{w=0.28}oh, I see [player]."
        show yuri 3w
        y "Perphaps another time?"
        show yuri 4c
        "I see Yuri's face turn bright red as she swiftly turns around and heads back to her desk."
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


#Sayori Interaction

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
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
            "We're like this for some time before Monika calls the group to attention."
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
            "I just sigh to myself and walk over to my bag to retrieve my poem."
            with wipeleft_scene
            jump poem_scene5


if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
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
            s 1k "Other than dragging you away from the others."
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
            "We're like this for some time before Monika calls the group to attention."
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
            "I just sigh to myself and walk over to my bag to retrieve my poem."
            with wipeleft_scene
            jump poem_scene7

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
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
            s 1k "Other than dragging you away from the others."
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
            "We're like this for some time before Monika calls the group to attention."
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
            show yuri 4b at t11 zorder 1
            "As I’m getting my poem I curiously look off in Yuri’s direction, who is avoiding making eye contact with anyone."
            "I guess it takes a lot for Yuri to talk to someone..."
            "She really isn’t one for social interactions..."
            "She must have really wanted to talk to me considering we really haven’t gotten the chance to recently."
            "Oh well, I’m sure we’ll get the chance sooner or later."
            "I just sigh to myself and walk over to my bag to retrieve my poem."
            show yuri at thide
            hide yuri
            with wipeleft_scene
            jump poem_scene8


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
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
            "We're like this for some time before Monika calls the group to attention."
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
            "I just sigh to myself and walk over to my bag to retrieve my poem."
            show yuri 4b at t11 zorder 1
            "As I’m getting my poem I curiously look off in Yuri’s direction, who is avoiding making eye contact with anyone."
            "It really does take a lot for Yuri to talk to someone..."
            "She really isn’t one for social interactions..."
            "She must have really wanted to talk to me considering we really haven’t gotten the chance to recently."
            "Oh well, I’m sure we’ll get the chance sooner or later."
            "I just sigh to myself and walk over to my bag to retrieve my poem."
            show yuri at thide
            hide yuri
            with wipeleft_scene
            jump poem_scene6

#Day 2
    label nencore_2:
    $ hangout2 = "Natsuki"
    "I decided to see what Natsuki was doing."
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "I spot Natsuki in her usual spot by the closet."
    "She seems to be reading her manga."
    play music t6 fadein 1.0
    mc "Hey, Natsuki."
    show natsuki 1p at h11 zorder 1
    "Natsuki jumps at hearing my voice."


if hangout1 == "Natsuki":
    jump nat_continued

if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
    jump nat_first

label nat_continued:
show natsuki 2e
n "[player]! I thought I told you to stop scaring me like that!"
n "That's a good way to give someone a heart attack!"
mc "Oh, come on! How am I supposed to approach you then?"
mc "Send a pigeon carrier?"
show natsuki 5s
mc "Besides...{w=0.38}calling your name out this way is much more fun!"
n 5y "Yeah, I'd bet it'd be real fun for you to see me drop dead from you scaring me!"
mc "Er...{w=0.38}no, it really wouldn't..."
show natsuki 5n
n "Oh, [player]..."
n 1m "I don't know how much more my little heart can take..."
show natsuki u112253 at s11 zorder 1
"Natsuki then pretends to faint dramatically as she has the biggest smirk possible on her face..."
mc "Oh, come on! You're just being overdramatic now..."
show natsuki xu2143 at h11 zorder 1
"Natsuki lets out a laugh."
mc "Yeah, real funny..."
n 2l "[player], sometimes you make this too easy for me."
mc "Come on...{w=0.38}you'd know I'd help you if you ever really needed it..."
n 2j "I know that."
n 2t "You seem nice enough to, anyways..."
show natsuki u121143
"Natsuki's voice trails off as she smiles sweetly at me."
"I smile back."
"For once, I actually think she wanted me to hear that..."
"Despite Natsuki's sourness at times...{w=0.38}she can be sweet when she wants to..."
n 1k "Anyways...{w=0.38}want to read Parfait Girls?"
n 1h "Since...{w=0.38}you know..."
n 1i "We didn't get to start last time."
"Natsuki's eyes dart to the floor as she references the incident we had with Yuri yesterday."
"Well, hopefully, Natsuki and I can read in peace this time!"
mc "You know it!"
n 2d "Great! Wait here, I'll go get it!"
show natsuki at thide
hide natsuki
$ currentpos = get_pos()
stop music fadeout 2.0
"As I watch Natsuki disappear into the closet, I can't help but be reminded of what I saw last night..."
"That horrifying look she gave me when she came out..."
n "Hey, [player]!"
n "Come over here! I need your help with something!"
show vignette at vignettefade:
    alpha 0.8
show noise at noisefade:
    alpha 0.5
"My head starts to spin..."
"W{w=0.38}-what's happening?"
"I feel like I'm right back in my dream..."
"My eyes dart towards the closet..."
"What if...{w=0.38}'it' happens again?"
"Wait...{w=0.38}why am I thinking like this?"
n "Come on, dummy! I don't have all day!"
"I take a deep breath."
play music hb
show layer master at heartbeat
"{i}Come on [player], it was just a stupid dream.{/i}"
"You have no reason to be thinking like this..."
"I walk in and brace myself for the worst..."
show layer master
scene bg closet
with wipeleft_scene
"But all I see is Natsuki struggling to grab her manga."
play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
show natsuki 1c at t11 zorder 1
n "Jeez! It took you long enough to get in here! What were you doing?"
mc "Sorry...{w=0.38}spaced out there for a bit."
"There's no way I'm telling Natsuki about my dream last night..."
"Or the hallucinations I just experienced now or this morning..."
"She'll think I'm crazy..."
n 2b "Well...{w=0.38}hurry up and grab that one!"
"She points to a special edition copy of Parfait Girls."
"Unlike the normal copies that I've seen from the series, this one is golden and reflective."
"It's one of those books that really grabs your attention if it's on a shelf somewhere."
mc "Whatever you say, Natsuki."
show natsuki 1a
"I grab the copy of the manga and we walk out of the closet."
show natsuki at thide
hide natsuki
scene bg closet
with wipeleft_scene
"While walking out of the closet, I take a closer look at the manga copy."
"Jeez...{w=0.38}this looked like it was definitely expensive!"
"Now I see why Natsuki's always raising hell if she can't find her manga..."
mc "Wow, where'd you get this?"
show natsuki 3z at t11 zorder 1
n "That's what happens when you go to conventions, [player]!"
n 3t "I was able to buy it at a discounted price there."
n 5u "Otherwise getting it would've been super expensive..."
mc "Conventions, huh?"
show natsuki 5n
"I mean I may read manga every now and then, but I'm clearly nowhere as near as enthused about it as Natsuki is..."
show natsuki 5m
n "What? You've never been to one?"
mc "I can't say that I have."
show natsuki 3w
n "Well I'm going to have to fix that!"
mc "You're going to take me to one?"
show natsuki 5y
n "Well, obviously!"
n 5l "They're really fun, [player]! You can get all sorts of rare collectibles there!"
mc "Huh, never thought of it like that..."
n 3j "There's actually a convention happening in town next week that we could go to!"
"Wait..."
"Is she...{w=0.38}{i}asking me out?{/i}"
show natsuki 3o
"Apparently my facial expression gives my thoughts away."
show natsuki 3v
n "But it isn't a date!"
mc "I-{w=0.38}I never said it would be..."
show natsuki 5y
n "It's written all over your face, [player]."
"I feel my face hot with embrassement."
"I try to deny Natsuki's claim."
mc "I don't know what you're talking about!"
show natsuki 5z
"Natsuki lets another laugh."
n 3t "Whatever you say, [player]."
n 3d "Anyways, let's start reading!"
mc "Finally!"
"I say that with a sense of relief in my voice."
show natsuki 5y
"Though Natsuki sees an opportunity to take advantage of that, which I should've seen coming..."
n "Yeah, you can daydream while we read!"
show natsuki 1z
"I let out as a sigh as Natsuki continues to laugh at seeing me flustered."
"We both take our seats underneath the windowsill."
scene n_cg1_bg
show n_cg1_base
with dissolve_cg
n "Well, you ready?"
mc "Yeah...{w=0.38}any particular reason you wanted to read from this and not the other copy?"
n "Well the special edition has some exclusive art in it!"
n "Not to mention it manages to pack volumes one through six into it!"
mc "Wow, that's awesome!"
mc "You're pretty incredible to be able to get your hands on something like this!"
"Natsuki blushes."
stop music fadeout 5.0
show n_cg1_exp2 with dissolve
n "Oh, don't mention it..."
hide n_cg1_exp2
show n_cg1_exp3
n "Just start reading!"

if encore_festivalquestion_2 == "Yuri":
    "I open the manga and we begin reading."

if encore_festivalquestion_2 == "Natsuki":
    "I open the manga and we begin reading, starting where we roughly left off in volume three."


with wipeleft_scene
hide n_cg1_exp3 with dissolve
show n_cg1_exp1 with dissolve
play music e3
"As we read throughout the manga, Natsuki sure enoughs points out all the differences between the special edition and the original."
"While I don't have much of a preference for reading either one, since they're the same all things considered, the special edition artwork does add a nice touch to this copy."
"I also noticed that the longer we read, the closer Natsuki has gotten to me..."
hide n_cg1_exp1 with dissolve
show n_cg1_exp5 with dissolve
"It also gets to a point where she goes quiet, and she looks at me more than she looks at the manga..."
"At first I try to ignore it, but it becomes distracting enough to the point where I can't continue reading."
"I turn to my right and I see that Natsuki's not even looking at the book anymore."
"She's just...{w=0.38}staring at me..."
"With an intimate look in her eyes..."
mc "Umm...{w=0.38}whatcha doing?"
stop music fadeout 1.0
"Natsuki doesn't respond."
"It seems as if she's in some kind of trance..."
"I don't know what to do."

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        "Sure, I don't mind Natsuki looking at me like this..."
        "But I'm afraid that someone's gonna catch us and immediately get the wrong idea..."
        "Especially considering how Yuri was yesterday..."

if encore_sayoriquestion_1 == True:
        "Sayori wouldn't be too happy if she saw us like this..."

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
play music t9 fadein 2.0
play sound "sfx/fall.ogg"
show cg n_cg_1 zorder 10 with dissolve_cg
hide natsuki
"Natsuki then suddenly embraces me tightly."
"I'm so surprised by Natsuki's sudden embrace that I nearly drop the manga."
"Her hug feels...{w=0.38}warm..."
"My mind goes blank in this siutation."

if encore_sayoriquestion_1 == False:
    "Natsuki's willingly hugging me!"
    "She moves to whisper in my ear."
    n "This feels nice, [player]."
    mc "It really does...{w=0.38}I like it..."
    n "I can almost get used to this..."
    "Natsuki's comment catches me completely off guard..."
    "She's usually never this forward..."
    "Still though..."
    "I think I could get used to this too..."

if encore_sayoriquestion_1 == True:
    "I mean on one hand, this feels nice..."
    "But it feels...{w=0.38}wrong too..."
    "Isn't being like this with someone other than your girlfriend technically cheating?"
    "Well it's not like I can really move Natsuki now..."
    "I'm pretty screwed either way, so I just sigh and accept whatever is to come..."
    n "This feels nice, [player]."
    mc "It really does...{w=0.38}I like it..."
    n "We should do this more..."
    "Natsuki's usually never this forward..."



stop music fadeout 1.0
hide cg with dissolve_cg
"Before I can respond, Monika stands up and walks to the front of the room."
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
"All three girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show monika at thide
hide monika
show sayori at thide
hide sayori
show yuri at thide
hide yuri
"I subtly nudge Natsuki."
mc "Um...{w=0.38}hey...{w=0.38}Natsuki."
show natsuki 1n at t11 zorder 1
"Natsuki looks up at me with a disoriented look."
mc "You...{w=0.38}we kind of need to get up."
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
show sayori 1k
show monika 1p
show yuri 1q
"Sayori, Monika and Yuri all look off in different directions, trying to avoid making the situation even more awkward then it already is as they take their seats at the font of the room..."
show sayori at thide
hide sayori
show monika at thide
hide monika
show yuri at thide
hide yuri


if encore_sayoriquestion_1 == True:
    jump day2_caught_n



if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Natsuki":
            jump day2_angry_yn


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump day2_angry_sn



#Natsuki Varaitions
label nat_first:
show natsuki 2e at t11 zorder 2
n "[player]! W-{w=0.38}what are you doing here?"
n 2g "Shouldn't you be with [hangout1] right now?"
n "Why are you over here?"
mc "I mean…"
"I feel a deep pit of guilt lurch inside my stomach."
"Maybe she’s got a point..."
show natsuki at thide
hide natsuki

if hangout1 == "Sayori":
    show sayori 1k at t11 zorder 2
    "I glance over to Sayori who appears to be spacing out."
    "Ah, she’ll be fine for a few minutes…"
    show sayori at thide
    hide sayori

if hangout1 == "Yuri":
    show yuri 1g at t11 zorder 2
    "I glance over to Yuri who appears to be deep into her book."
    "Ah, she'll be fine without me for a few minutes..."
    show yuri at thide
    hide yuri


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

show natsuki 1i at t11 zorder 2
mc "What, I’m not allowed to spend time with you?"

if encore_festivalquestion_2 == "Natsuki":
    mc "We really haven't talked since the festival, after all..."
    show natsuki 5x at t11 zorder 2
    "Natsuki crosses her arms, thinking over what I just said."
    n 5w "It’s not like I wanted you to come spend time me or with anything!"
    n "Lately you've been spending your time around the others!"
    n 5q "But, I guess while you’re here…"
    n 5h "You want to read Parfait Girls with me?"
    mc "Yeah, sure! I'd love to!"
    mc "It's been a while since we've gotten to read together."
    show natsuki 4w
    n "That's why you should've come to me sooner, dummy!"
    n "At this rate we'll be lucky to finish the series by the end of the year!"
    mc "Well, in that case, we better get reading!"
    show natsuki 3z
    n "Well, let's get going!"
    "Natsuki takes me by the arm and drags me to our spot near the windowsill."
    mc "Alright, alright! Sheesh…"
    show natsuki at thide
    hide natsuki
    scene bg closet
    with wipeleft_scene
    play sound "sfx/fall.ogg"
    "Natsuki's eagerness for us to read again clearly gets the best of her as she practically throws me to the ground."
    mc "Ow! Hey! Was that really necessary?"
    show natsuki 1w at t11 zorder 2
    n "Duh!"
    show natsuki 1z
    stop music fadeout 3.0
    "Natsuki giggles to herself before letting out a warm smile."
    "I never really realized how much I missed her cute little giggle..."
    "Natsuki takes a seat next to me."
    play music e3
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "Sooooo...{w=0.38}remind me why we aren't sitting at the desks again?"
    hide n_cg1_exp1
    show n_cg1_exp3
    n "Why do you always ask stupid questions?"
    mc "Ummm..."
    "I don’t really know what Natsuki’s trying to get at here..."
    n "Ugh! Nevermind, just start reading!"
    mc "You must really like this series if you’re going through all this trouble of making sure I finish it."
    hide n_cg1_exp3 with dissolve
    show n_cg1_exp2 with dissolve
    n "W-{w=0.38}well someone needs to show you what real literature looks like!"
    mc "If you say so."
    "I open to the first page and begin reading."
    hide n_cg1_exp2 with dissolve
    show n_cg1_exp5 with dissolve
    "Natsuki looks over my shoulder as I read."
    mc "You sure you’re still good reading like that?"
    hide n_cg1_exp5 with dissolve
    show n_cg1_base with dissolve
    n "Yeah, I can see fine from here."
    show n_cg1_exp3
    n "Don’t worry about me...{w=0.38}just keep reading!"
    mc "Okay, okay."
    n "Dummy!"
    "I sigh to myself as I keep on reading."
    hide n_cg1_exp3 with wipeleft_scene
    "As we keep on reading, I slowly get back into the grove of the story."
    "It's been so long I actually almost forgot what the series was about!"
    show n_cg1_exp1 with dissolve
    "Suddenly Natsuki points to a slide on the book."
    n "Oooh! I love that scene!"
    mc "Hmmm?"
    "My eyes turn to the slide that Natsuki’s pointing to."
    "The girls are shown admiring this massive marvel cake they were baking for this competition they're in."
    "I’ll admit, the artwork here makes the cake look very realistic."
    "I’m kind of getting hungry just by looking at it…"
    "Now that I think about it, there has been a lot of baking in this manga…"
    n "That has to be the best scene in this chapter!"
    n "It’s nice when you put all that hard work into something and it turns out great!"
    mc "Yeah, Iike those cupcakes we made last Sunday?"
    hide n_cg1_exp1 with dissolve
    show n_cg1_exp2 with dissolve
    "Natsuki nervously smiles."
    n "Y-{w=0.38}yeah… {w=0.38}like those cupcakes…."
    "Natsuki looks off, clearly flustered."
    mc "I had a lot of fun last Sunday though."
    mc "If you ever want to hangout again, just let me know."
    "Natsuki’s face only becomes more flush with crimson as she tries to fight back a smile."
    n "Uh…"
    mc "But I mean, if you’re busy, I understand."
    hide n_cg1_exp2 with dissolve
    show n_cg1_base with dissolve
    n "N-no! I’d love to!"
    show n_cg1_exp2 with dissolve



if encore_festivalquestion_2 == "Yuri":
    mc "We never really got the chance to know each other."
    show natsuki 5x at t11 zorder 2
    "Natsuki crosses her arms thinking over what I just said."
    n 5w "It’s not like I wanted you to come spend time me or with anything!"
    n "You always just seem so busy hanging around the others!"
    n 5q "But, I guess while you’re here…"
    n 5h "You want to read this with me?"
    "Natsuki shows me the cover of the book she’s reading."
    mc "Parfait Girls...?"
    "It's a series I've never heard of in my life."
    "That probably means I'm either not in its target audience, or it just plain sucks."
    n 2j "Take a look!"
    "Natsuki shoves the book into my hands."
    "I examine the book."
    "It features four girls in colorful attire striking animated feminine poses."
    "Great...{w=0.38}an off-brand version of Sailor Moon."
    "And...{w=0.38}it seems exceedingly...{w=0.38}'moe'."
    "Still, I should try to respectful of Natsuki's interests."
    "It is a Literature Club after all..."
    mc "Hmmm...{w=0.38}I don’t think I’ve ever read this before."
    mc "Is it good?"
    show natsuki 4o
    n "Good?"
    show natsuki 3z
    n "It’s the best thing ever! And I’m going to show you!"
    "Natsuki takes me by the arm and pretty much drags me to a spot near the windowsill."
    mc "Alright, alright! Sheesh…"
    show natsuki at thide
    hide natsuki
    scene bg closet
    with wipeleft_scene
    play sound "sfx/fall.ogg"
    "I don't think Natsuki appreciated my tone seeing as she practically throws me to the ground."
    mc "Ow! Hey! Was that really necessary?"
    show natsuki 1w at t11 zorder 2
    n "Duh!"
    show natsuki 1z
    stop music fadeout 3.0
    "Natsuki giggles to herself before letting out a warm smile."
    "I never really realized how cute her giggle or smile was before..."
    "Natsuki takes a seat next to me."
    play music e3
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "Sooooo...{w=0.38}why not sit at the desks?"
    hide n_cg1_exp1
    show n_cg1_exp3
    n "Do you always ask stupid questions?"
    mc "Ummm..."
    "I don’t really know what Natsuki’s trying to get at here..."
    n "Ugh! Nevermind, just start reading!"
    mc "You must really like this series if you’re going through all this trouble of getting me into it."
    hide n_cg1_exp3 with dissolve
    show n_cg1_exp2 with dissolve
    n "W-{w=0.38}well someone needs to show you what real literature looks like!"
    mc "If you say so."
    "I open to the first page and begin reading."
    hide n_cg1_exp2 with dissolve
    show n_cg1_exp5 with dissolve
    "Natsuki looks over my shoulder as I read."
    mc "You sure you’re good reading like that?"
    hide n_cg1_exp5 with dissolve
    show n_cg1_base with dissolve
    n "Yeah, I can see fine from here."
    show n_cg1_exp3
    n "Don’t worry about me...{w=0.38}just keep reading!"
    mc "Okay, okay."
    n "Dummy!"
    "I sigh to myself as I keep on reading."
    "..."
    "..."
    "..."
    "This manga looks like it's about a bunch of friends in high school."
    "Your usual run-of-the-mill slice-of-life manga."
    "..."
    "There'll probably be a harem by chapter five..."
    "Not to mention, I kind of grew out of these by the time I was twelve..."
    "It's very rare for there to be an actual point in these types of manga."
    "By the end of the first few chapters I’m already feeling kind of bored."
    hide n_cg1_exp3 with dissolve
    show n_cg1_exp1 with dissolve
    "Suddenly Natsuki points to a slide on the book."
    n "Oooh! I love that scene!"
    mc "Hmmm?"
    "My eyes turn to the slide that Natsuki’s pointing to."
    "The girls are shown admiring this massive marvel cake they were baking for this competition they're in."
    "I’ll admit, the artwork here makes the cake look very realistic."
    "I’m kind of getting hungry just by looking at it…"
    "Now that I think about it, there has been a lot of baking in this manga…"
    n "That has to be the best scene in this chapter!"
    n "It’s nice when you put all that hard work into something and it turns out great!"
    mc "Yeah, Iike those cupcakes you make?"
    hide n_cg1_exp1 with dissolve
    show n_cg1_exp2 with dissolve
    "Natsuki nervously smiles."
    n "Y-{w=0.38}yeah...{w=0.38}like those cupcakes…"
    "Natsuki looks off, clearly flustered."
    mc "Yeah, they’re amazing!"
    mc "You should totally teach me how to make them! I’m a decent cook myself after all..."
    "Natsuki’s face only becomes more flush with crimson as she tries to fight back a smile."
    n "Uh…"
    mc "But I mean, if you’re busy, I understand."
    hide n_cg1_exp2 with dissolve
    show n_cg1_base with dissolve
    n "N-{w=0.38}no!"
    show n_cg1_exp2 with dissolve
    n "I mean…"
    "Natsuki struggles to get anything comprehensible out her mouth."
    "Finally she takes a deep breath."
    hide n_cg1_exp2 with dissolve
    show n_cg1_base with dissolve
    n "I guess it would be nice…"


if encore_sayoriquestion_1 == False:
    if hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Sayori" or hangout1 == "Natsuki":
        n "I just didn’t want to ask because I didn’t know if you had plans with [hangout1] or something…"
        "Right…"
        "Speaking of [hangout1]…"
        scene bg club_day
        with dissolve_cg



        if hangout1 == "Yuri":
            show yuri 1l at t11
            "I look up to see Yuri still apparently reading her book."
            "Huh...{w=0.38}I don't think she's turned the page in a while..."
            "Maybe I should go check up on her..."
            show yuri at thide
            hide yuri
            "I feel Natsuki place her hand on my shoulder."
            scene n_cg1_bg
            show n_cg1_base
            with dissolve_cg
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0

        if hangout1 == "Monika":
            show monika 1o at t11
            "I look up to see Monika starting stoically out the window."
            "Maybe I should go check up on her..."
            show monika 1h at face
            stop music
            $ style.say_dialogue = style.edited
            "{cps=25}You should've checked on me sooner!{nw}"
            $ style.say_dialogue = style.normal
            show monika at thide
            hide monika
            "I feel Natsuki place her hand on my shoulder."
            scene n_cg1_bg
            show n_cg1_base
            with dissolve_cg
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0



        if hangout1 == "Sayori":
            show sayori 1k at t11
            "I look up to see Sayori still looking off into space."
            "Maybe I should go check up on her…"
            show sayori at thide
            hide sayori
            "I feel Natsuki place her hand on my shoulder."
            scene n_cg1_bg
            show n_cg1_base
            with dissolve_cg
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0


        if encore_festivalquestion_2 == "Natsuki":
            n "I wish we got to spend more time on Sunday though…"
            mc "Yeah…{w=0.38}me too…"

        if encore_festivalquestion_2 == "Yuri":
            n "I just wish we got to spend more time together..."
            mc "Yeah…{w=0.38}me too…"



if encore_sayoriquestion_1 == True:
        n "I just didn’t want to ask because I didn’t know if you had plans with Sayori or something…"
        "Right…"
        "Speaking of Sayori…"
        scene bg club_day
        with dissolve_cg
        show sayori 1k at t11
        "I look up to see Sayori still looking off into space."
        "Maybe I should go check up on her…"
        show sayori at thide
        hide sayori
        "I feel Natsuki place her hand on my shoulder."

        if encore_festivalquestion_2 == "Natsuki":
            scene n_cg1_bg
            show n_cg1_base
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0
            n "I wish we got to spend more time on Sunday though…"
            mc "Yeah…{w=0.38}me too…"

        if encore_festivalquestion_2 == "Yuri":
            scene n_cg1_bg
            show n_cg1_base
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0
            n "I just wish we got to spend more time together..."
            mc "Yeah…{w=0.38}me too…"

hide n_cg1_exp2 with dissolve
show n_cg1_exp5 with dissolve
"I stare into Natsuki’s eyes, her gaze meeting mine."
"Natsuki scootches closer to me, our arms practically touching."
"What is she doing?"
"Normally, she’d call me gross for getting near her…"
"I wouldn't ever expect her to get close to me like this…"
"And, while I don’t mind being this close to Natsuki..."
"I’m afraid that someone’s gonna catch us and immediately get the wrong idea…"
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
show natsuki at thide
hide natsuki
play music t9
play sound "sfx/fall.ogg"
show cg n_cg_1 zorder 10 with dissolve_cg
"Natsuki suddenly embraces me tightly."
"I'm so surprised by Natsuki's sudden embrace that I nearly drop the manga."
"Her hug feels...{w=0.38}warm..."
"My mind goes blank in this siutation."

if encore_sayoriquestion_1 == False:
        "Natsuki's willingly hugging me!"
        "She moves to whisper in my ear."

        if hangout1 == "Monika":
            $ style.say_dialogue = style.edited
            "Tighter daddy."
            $ style.say_dialogue = style.normal

n "This feels nice, [player]."
mc "It really does...{w=0.38}I like it..."
n "We should do this more..."
"She's usually never this forward..."
jump day2_gg


if encore_sayoriquestion_1 == True:
    "I mean on one hand, this feels nice..."
    "But it feels...{w=0.38}wrong too..."
    "Isn't being like this with someone other than your girlfriend technically cheating?"
    "Well it's not like I can really move Natsuki now..."
    "I'm pretty screwed either way, so I just sigh and accept whatever is to come..."
    "Natsuki moves to whisper in my ear."

    if hangout1 == "Monika":
        $ style.say_dialogue = style.edited
        "Tighter daddy."
        $ style.say_dialogue = style.normal

    n "This feels nice, [player]."
    mc "It really does. I like it…"
    n "Can we do this more?"
    n "Can we spend more time together?"
    "Natsuki’s questions catches me completely off guard. I wasn’t expecting her to be this forward."
    "Still though…"
    "I don’t feel like this is right..."
    "Natsuki's usually never this up-front about her feelings..."
    jump day2_gg



if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika" or hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Natsuki":


        if hangout1 == "Monika":
          "I’m with Sayori after all, how would she react to seeing us like this?"
          $ style.say_dialogue = style.edited
          "Let's find out..."
          $ style.say_dialogue = style.normal

        if hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Natsuki":
            pass # Temporary


if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika" or hangout1 == "Yuri" or hangout1 == "Sayori":


        if hangout1 == "Monika":
            "I'm left feeling a little hesistant on how best to respond to Natsuki."
            "Monika...{w=0.38}how'd she react to finding us like this?"
            $ style.say_dialogue = style.edited
            "Let's find out..."
            $ style.say_dialogue = style.normal

        if hangout1 == "Yuri":
            "I'm left feeling a little hesistant on how best to respond to Natsuki."
            "Yuri...{w=0.38}how'd she react to finding us like this?"

        if hangout1 == "Sayori":
            "I'm left feeling a little hesistant on how best to respond to Natsuki."
            "Sayori...{w=0.38}how'd she react to finding us like this?"

label day2_gg:
stop music
hide cg with dissolve_cg
"Before I can respond, Monika stands up and walks to the front of the room."
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
"Only to see what Monika and Sayori are staring at."
"Natsuki and I are practically cuddling at this point."
show monika 1h
show sayori 1i
show yuri u123114
"All three girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show monika at thide
hide monika
show sayori at thide
hide sayori
show yuri at thide
hide yuri
"I subtly nudge Natsuki."
mc "Um...{w=0.38}hey...{w=0.38}Natsuki."
show natsuki 1n at t11 zorder 1
"Natsuki looks up at me with a disoriented look."
mc "You...{w=0.38}we kind of need to get up."
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
show sayori 1k
show monika 1p
show yuri 1q
"Sayori, Monika and Yuri all look off in different directions, trying to avoid making the situation even more awkward then it already is as they take their seats at the font of the room..."
show sayori at thide
hide sayori
show monika at thide
hide monika
show yuri at thide
hide yuri


#Sayori Response

if encore_sayoriquestion_1 == True:
    jump day2_caught_n

    label day2_caught_n:
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
                jump sayori_sorry_n
            "Lie.":
                $ apologize_sn = False
                jump sayori_not_sorry_n

        label sayori_sorry_n:
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

        label sayori_not_sorry_n:
        "I don’t want Sayori to get the wrong idea about Natsuki and I."
        "I try to come up with an excuse off the fly."
        mc "Natsuki looked kind of down…"
        show sayori 1e
        mc "I was trying to cheer her up…"
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




if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Natsuki":
            jump day2_angry_yn


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump day2_angry_sn

#Yuri Response

label day2_angry_yn:
show yuri 3v at t11 zorder 1
"While on my way to the front of the room, Yuri abruptly stops me."
"She doesn't look too happy with what she just saw, but she also looks like she's unsure if she wants to confront me about what just happened..."
"I decide to speak first."
mc "Y-{w=0.38}yeah, Yuri?"
show yuri 4d
y "N-{w=0.38}nothing, [player]...{w=0.38}It was nothing important."
show yuri 4c
"She looks off to the other side of the room as she mutters softly."
show yuri at thide
hide yuri
"Yuri then briskly walks past me, taking a seat and joining the others."
"Well, that was random..."
"I just hope she isn’t jealous of me and Natsuki getting so close like that."
"She isn’t the jealous type…{w=0.38}right?"
jump day2_meettheclubs


#Sayori Response 2.0


label day2_angry_sn:
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
"I take it she didn't take too kindly to me getting too close to Natsuki like that."
"I really need to be more careful around her..."
"Though, Sayori was never the jealous type..."
jump day2_meettheclubs

#Day 3
label nencore_3:
    $ hangout3 = "Natsuki"
    "I'll see what Natsuki is up to."
    scene bg club_day
    with wipeleft_scene


"As I wask up to the closet, I can hear Natsuki talking to herself."

N: “Aggh, where the hell is it?”

"Careful not to startle her like I did yesterday, I poke my head in and ask her what's wrong."

Mc: “Hey Nat, everything ok in there?”

"I see Natsuki put some boxes and books back on the shelf, then she turns towards me." (Show frown)

N: “No, I'm not able to find my special edition Parfait Girls Manga that we were reading yesterday.”

Mc: “Have you checked the top shelves?”

N: “No... I'm not, you know..."
#show Natsuki look around, looking uncomfortable
"Do you think you could look up there?”

Mc: “Of course.”

N: “Thanks.”

"I check the top shelves first, then the rest for good measure."
"However, I don't find the manga."


N: “You find it?”

Mc: “No I didn’t."
MC "I looked everywhere in there, sorry Nat.”

N: “Hmm."
N "I dont know where I could have left it, I only ready it in here.”

Mc: “Did you maybe take it to another class?”

N: “I can’t remember..”

Mc: “Maybe we should retrace your steps?”

N: “Hmm, that's actually a good idea."
N "Eheh I'm surprised you thought of it”

Mc: “H-Hey!"
Mc: "You saying im dumb?”

"Natsuki Giggles."

N: “Noo, I’d never do that.”

Mc: Hmph.”

# Show A frown comes across Natsuki’s face as she pouts

N: “Oh come on, I'm only teasing you..”

Mc: "I know.”

"I laugh to show her I'm only kidding."

N: “Hey, I actually felt bad for saying that..”

Mc: “Aww it's okay."
Mc: "Come on, lets go find your book.”

N: “Fine, lets go check my last class.”

Mc: “Okay, lead the way."
"
Natsuki and I leave the clubroom to go find her manga."

(Hallway scene)

"As we walk down the hallway, I look over to see that Natsuki is looking at her feet, I stop and put my hand on her shoulder." #show arms crossed

N: “...Huh?”

Mc: “You okay?”

N: “Not really... I'm worried we might not find the book..”

Mc: “It's ok Nat, I know we’ll find it."
Mc: "We just gotta trace back what you did before the club today and it'll pop up.”

N: “Really..?"
N: "What if we don’t… that book cost alot and it was a special edition."
N: "...And I was really hoping to finish the book with you.”

Mc: “I know we’ll find it, just stay positive okay?”

N: "Okay.”



"We walk for about another 5 minutes in silence until we get to classroom."
"We open the door and start looking."
"After about 20 minutes of looking, we covered almost the entire room and haven't found anything yet."

N: “This is pointless."
N: "It's not in here, I'm gonna check the closet one more time and see if I might have skipped over it.”

Mc: “I'll keep looking out here then.”
"
"Nat goes into the closet as I continue to look around the room."
"A few minutes pass as I notice a box by one of the desks."
"I walk over to it and look inside to see the book sitting in the box."
"With a grin on my face, I pick it up and walk over to the closet where Nat is still looking and call out to her."

Mc: “Hey Nat, come out here”

"Natsuki emerges from the closet."
" As soon as she sees the book, she smiles, walks up to me and wraps her arms around me."
"I'm taken aback by her hug, but..."

#choose to hug back
#choose to not hug back

(chooses to hug back)

."..nonetheless, I gently wraps my arms around her."
"After a brief moment, she pulls back and her face turns beet red."

N: “T-thanks for finding it..where was it?”

Mc: “No problem, and it was in that box right there.”

"I point to the box."

N: “Oh yeah, that's right!"
N: "I put it in there at the beginning of class cause I didn't want to lose it."
#May need to rewrite it a bit to be cleaner
N: "I guess that's ironic, isn't it?”

"We both laugh at the remark."

Mc: “Well, I’m glad we found it.”

N: “Yeah, me too...”

#show this, don't tell: A frown appears on her face and she looks down at the floor

Mc: “Are you okay Nat?”

N: “Y-yeah, I just feel bad about breaking the hug... I liked it."
N: "I'm just not used to feeling cared about...”

Mc: “What?"
Mc: "Don’t you get any from your family?”

N: “No, my dad doesn’t really do any of that kind of stuff.”

Mc: “Oh my.. doesn't he give you any kind of attention?”

#show, don't tell: she looks up at me and tears well up in her eyes

N: “I-I don’t want to talk about this anymore.”

Mc: “Ok, just know that I’m always here for you if you ever want to talk.”

N: “T-Thank you.”
"Without warning, she hugs me again."
"When I wrap my arms around her this time, she doesn’t break free."
"we stay like this for a couple minutes before we let go of each other."

Mc: “You wanna go back to the club and read?”

#show, don't tell: She wipes the tears from her eyes

N: “Y-yeah”

We leave the classroom and walk back to the club room."
"On the walk back, I can’t help but wonder what her home life's like."

#(option to not hug back is chosen *your mean if you choose this* )

"I choose not to hug back."
"When she notices I’m not hugging back, she backs up."

N: “Well.. uh, thanks for finding it [player].”

Mc: “No problem Nat.”

N: “Let’s go back to the clubroom, the others might wonder where we are.”

Mc: “Yeah you're right, lets go.”

"We leave the classroom and Nat seems to be hurrying to back to the clubroom."
"Is it because I didn’t hug her back?"
"I didn’t mean to upset her... Maybe I should have hugged her."
