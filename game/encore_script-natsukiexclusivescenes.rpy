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
        "And, I really feel like I should check on Sayori..."
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
        "And, I really feel like I should check on Sayori..."
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
        "And, I really feel like I should check on Sayori..."
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
            mc "I...{w=0.38}don't take your meaning."
            s "I selfishly thought that if I tried putting all my time, energy and effort into making you happy..."
            show sayori 3u
            $ renpy.pause(delay=0.5, hard=True)
            show sayori 1v
            s "I dont know...{w=0.38}I thought that you would love me back..."
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
mc "I mean..."
"I feel a deep pit of guilt lurch inside my stomach."
"Maybe she’s got a point..."
show natsuki at thide
hide natsuki

if hangout1 == "Sayori":
    show sayori 1k at t11 zorder 2
    "I glance over to Sayori who appears to be spacing out."
    "Ah, she’ll be fine for a few minutes..."
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
    n 5q "But, I guess while you’re here..."
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
    mc "Alright, alright! Sheesh..."
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
    "I’m kind of getting hungry just by looking at it..."
    "Now that I think about it, there has been a lot of baking in this manga..."
    n "That has to be the best scene in this chapter!"
    n "It’s nice when you put all that hard work into something and it turns out great!"
    mc "Yeah, Iike those cupcakes we made last Sunday?"
    hide n_cg1_exp1 with dissolve
    show n_cg1_exp2 with dissolve
    "Natsuki nervously smiles."
    n "Y-{w=0.38}yeah... {w=0.38}like those cupcakes...."
    "Natsuki looks off, clearly flustered."
    mc "I had a lot of fun last Sunday though."
    mc "If you ever want to hangout again, just let me know."
    "Natsuki’s face only becomes more flush with crimson as she tries to fight back a smile."
    n "Uh..."
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
    n 5q "But, I guess while you’re here..."
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
    mc "Alright, alright! Sheesh..."
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
    "I’m kind of getting hungry just by looking at it..."
    "Now that I think about it, there has been a lot of baking in this manga..."
    n "That has to be the best scene in this chapter!"
    n "It’s nice when you put all that hard work into something and it turns out great!"
    mc "Yeah, Iike those cupcakes you make?"
    hide n_cg1_exp1 with dissolve
    show n_cg1_exp2 with dissolve
    "Natsuki nervously smiles."
    n "Y-{w=0.38}yeah...{w=0.38}like those cupcakes..."
    "Natsuki looks off, clearly flustered."
    mc "Yeah, they’re amazing!"
    mc "You should totally teach me how to make them! I’m a decent cook myself after all..."
    "Natsuki’s face only becomes more flush with crimson as she tries to fight back a smile."
    n "Uh..."
    mc "But I mean, if you’re busy, I understand."
    hide n_cg1_exp2 with dissolve
    show n_cg1_base with dissolve
    n "N-{w=0.38}no!"
    show n_cg1_exp2 with dissolve
    n "I mean..."
    "Natsuki struggles to get anything comprehensible out her mouth."
    "Finally she takes a deep breath."
    hide n_cg1_exp2 with dissolve
    show n_cg1_base with dissolve
    n "I guess it would be nice..."


if encore_sayoriquestion_1 == False:
    if hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Sayori" or hangout1 == "Natsuki":
        n "I just didn’t want to ask because I didn’t know if you had plans with [hangout1] or something..."
        "Right..."
        "Speaking of [hangout1]..."
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
            "Maybe I should go check up on her..."
            show sayori at thide
            hide sayori
            "I feel Natsuki place her hand on my shoulder."
            scene n_cg1_bg
            show n_cg1_base
            with dissolve_cg
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0


        if encore_festivalquestion_2 == "Natsuki":
            n "I wish we got to spend more time on Sunday though..."
            mc "Yeah...{w=0.38}me too..."

        if encore_festivalquestion_2 == "Yuri":
            n "I just wish we got to spend more time together..."
            mc "Yeah...{w=0.38}me too..."



if encore_sayoriquestion_1 == True:
        n "I just didn’t want to ask because I didn’t know if you had plans with Sayori or something..."
        "Right..."
        "Speaking of Sayori..."
        scene bg club_day
        with dissolve_cg
        show sayori 1k at t11
        "I look up to see Sayori still looking off into space."
        "Maybe I should go check up on her..."
        show sayori at thide
        hide sayori
        "I feel Natsuki place her hand on my shoulder."

        if encore_festivalquestion_2 == "Natsuki":
            scene n_cg1_bg
            show n_cg1_base
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0
            n "I wish we got to spend more time on Sunday though..."
            mc "Yeah...{w=0.38}me too..."

        if encore_festivalquestion_2 == "Yuri":
            scene n_cg1_bg
            show n_cg1_base
            show n_cg1_exp2 with dissolve
            stop music fadeout 2.0
            n "I just wish we got to spend more time together..."
            mc "Yeah...{w=0.38}me too..."

hide n_cg1_exp2 with dissolve
show n_cg1_exp5 with dissolve
"I stare into Natsuki’s eyes, her gaze meeting mine."
"Natsuki scootches closer to me, our arms practically touching."
"What is she doing?"
"Normally, she’d call me gross for getting near her..."
"I wouldn't ever expect her to get close to me like this..."
"And, while I don’t mind being this close to Natsuki..."
"I’m afraid that someone’s gonna catch us and immediately get the wrong idea..."
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
    mc "It really does. I like it..."
    n "Can we do this more?"
    n "Can we spend more time together?"
    "Natsuki’s questions catches me completely off guard. I wasn’t expecting her to be this forward."
    "Still though..."
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
        mc "Uh..."
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
        mc "It was wrong of me to act in such a way and I promise you..."
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
        mc "Natsuki looked kind of down..."
        show sayori 1e
        mc "I was trying to cheer her up..."
        mc "It was that and only that...{w=0.38}I promise..."
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
"She isn’t the jealous type...{w=0.38}right?"
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
    scene bg closet
    with wipeleft_scene
    play music e14 fadein 1.0
    "As I walk up to the closet, I can hear Natsuki talking to herself."
    n "Ugh...{w=0.38}where the hell is it?!?"

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            "Careful not to startle her like I have been recently, I gently knock on the closet door."

    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            "Careful not to startle her like I did yesterday, I gently knock on the closet door."

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
            "Careful not to startle her like I did on Monday, I gently knock on the closet door."

    else:
        "Careful not to startle her, I gently knock on the closet door."
        mc "N-{w=0.38}Natsuki?"

    "Natsuki finishes putting some boxes back on the shelf as she comes out of the closet."
    show natsuki 5u at t11 zorder 1
    mc "Hey, everything ok in there?"
    show natsuki 5m
    n "No..."
    show natsuki 42b
    "Natsuki turns away, attempting to compose herself."
    mc "Well, what’s wrong?"

    if hangout1 == "Natsuki" or hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            n 42c "I think I lost that special edition of Parfait Girls that we were reading yesterday..."
            "Well, I can see why she’d be upset about that..."

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
            n 42a "Why do you care?"
            n 42b "Aren't you supposed to be hugging [hangout2] right now?"
            "I awkwardly scratch the back of my head."
            "I should've known she would've brought that up..."

            if encore_sayoriquestion_1 == True:
                "She didn't look too happy yesterday when she saw me with [hangout2]..."

            if encore_sayoriquestion_1 == False:
                "She did punch me after all..."

            "How am I supposed to explain this to her? It's not like she's going to believe me..."
            "I mean...{w=0.38}it was pretty much spontaneous..."
            show natsuki 42a
            mc "Look, I get that you're angry with me over yesterday..."
            mc "I'm sorry, I didn't initate anything, it just happened, I swear!"
            n 42b "Whatever, I got too much to worry about to be angry at you for yesterday..."
            mc "So now will you tell me what's wrong?"
            show natsuki 42c
            "Natsuki lets out a long, reluctant sigh."
            n 42a "I think I lost one of my copies of Parfait Girls..."
            mc "Oh, no! Which one?"
            n 42e "It was special edition copy..."
            "Well, I can see why she’d be upset about that..."

    else:
        n 42a "Why do you care?"
        n "Aren't you supposed to be with [hangout2] right now?"
        n 42c "Because I'm not hugging you too."
        mc "Well, I didn't come over here for that..."
        show natsuki 5n
        "Natsuki raises an eyebrow at me."
        n 5i "Then why are you over here then?"
        n 5w "If you're hear to apologize for yesterday, don't."
        n 5x "I don't really care who you're with..."
        mc "Natsuki, I didn't come for any of that."
        mc "I just wanted to see how you were doing..."
        n 5w "I think you already know the answer to that!"
        show natsuki 5i
        "Natsuki looks over her shoulder into the closet."
        "I briefly look past her to see books and other items littered all over the closet floor."
        "So this is how she 'organizes'..."
        mc "I take it you're looking for something..."
        n 5w "Well, duh!"
        n 4x "I'm looking for my special edition of Parfait Girls..."
        mc "'Parfait Girls'?"
        n 4w "Yes, genius! It's the manga I like to read!"
        mc "I see..."
        "I've never heard of any manga called that before."
        "Which either means it's really bad, or I'm out of its target auidence."
        mc "Well, I'd be happy to help you look for it."
        mc "That is, if you need a helping hand..."
        show natsuki 5u
        "Natsuki takes a moment to think my offer over."
        n 5i "Alright."
        n 5h "You can make yourself useful and start looking through up there."
        "Natsuki points to the upper shleves."
        mc "Alright."
        "Natsuki grabs one of her manga cases and moves out of the way as I step into the closet."
        mc "So, what does it look like?"
        n 1w "It's pink and it'll say 'Special Edition' on it."
        n 1k "You'll know when it you see it."
        mc "Alright..."
        show natsuki at thide
        hide natsuki
        "I begin to look through the upper shelves for anything that resembles what Natsuki just described."
        scene bg closet
        with wipeleft_scene
        "After searching through the upper shelves, I still wasn't able to find anything that resembled what Natsuki described."
        show natsuki 1m at t11 zorder 1
        n "Anything?"
        "I somberly shake my head."
        mc "Nothing."
        mc "I will say though, you do have a pretty nice manga collection."
        show natsuki 4w
        n "Well, that's why you should've come to me sooner!"
        n 4y "I have the best manga collection in the entire school!"
        mc "Well, it certainly beats mine..."
        n 1k "What kinds of manga do you read?"
        mc "Ah, anything to do with action and adventure..."
        n 2w "Ugh! That's so typical!"
        n 2e "When this is over, I've got to show you some different kinds of manga!"
        mc "Well, I guess I could give it a try..."
        n 4l "There you go! That's the spirit!"
        n 4z "Get ready to dive head first into my world of manga, [player]!"
        "I don't know if that's a good thing or bad thing that she just said that..."
        "Either I'm going to be blown away with how shockingly good her favorite manga are..."
        "Or I'm going to be testing the limits of how much boredom someone can take..."
        "Still, it'd be nice to getting to know Natsuki a little bit better..."
        n 3u "But, I really would like to show you that Special Edition."
        n 3m "It'll give you a proper introduction into other types of manga."
        mc "You could just get me started with the regular edition..."
        mc "I mean, how badly do we need to find it?"
        n 42c "There's not many like it, [player]..."
        n 42a "It's not something I can just easily replace..."
        mc "In that case..."




    mc "Did you have it with you earlier today?"
    n 4m "Yeah, I had it with me it all day..."
    n 3q "I could’ve sworn I had it with me when I came here..."
    show natsuki 42b
    "Natsuki clenches her fists in frustration."
    n 42c "I swear to God if I can’t find it..."
    show natsuki 42d
    "Natsuki's voice breaks."
    "I glance around the room to see if anyone else is seeing this."
    "It seems like at any moment Natsuki will break down and start crying."
    "Well, I’m about to do something risky to try to calm her down..."
    mc "Natsuki..."
    "I put my hand on her shoulder."
    show natsuki 4m
    n "Eh...?"
    mc "We’ll find it..."
    show natsuki 5n
    mc "Ok?"
    show natsuki_sweet as natsuki at t11
    "Natsuki’s face turns another shade of crimson as she shrugs my hand off."
    n 5y "Alright lover-boy, calm down! Let’s keep this PG."
    show natsuki 5z
    mc "L-{w=0.38}lover boy???"
    mc "What’re you getting at here?"
    n 5e "You know exactly what I’m getting at."
    n 5g "Don’t act dumb!"
    mc "Ah, whatever..."
    "I try to change the subject fearing further embarrassment by Natsuki."
    mc "Well, if we’re going to find that manga, we should probably retrace your steps."
    mc "Where was the last time you remember reading it?"
    show natsuki 5s
    "Natsuki takes a long pause."
    n 2m "Well, I was reading it in Mrs. Suzuki’s class..."
    mc "Aren’t you the diligent student?"
    n 2o "Hey! You know her class is boring!"
    mc "At least you don’t have Ms. Saitō..."

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            n 5w "It’s not like you pay attention in her class either!"


    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            n 5w "You probably don't pay attention in her class either!"


    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
            n 5w "You probably don't pay attention in her class either!"


    else:
        n 5w "So why are you criticizing me for trying to pass the time in her class when you probably do the same thing!"


    show natsuki 5x
    mc "Fair point..."
    mc "Anyways, Suzuki’s probably left her room by now, so we can probably go check."
    n 1c "Alright, let’s go!"
    n 1b "The faster we find that manga, the more sane I'll be by the end of this!"
    "I let out a slight chuckle as we head out of the clubroom and into the hallway."
    scene bg corridor
    with wipeleft_scene
    "Fortunately it didn’t take too long for us to get to Ms. Suzuki’s classroom, considering it was just around the corner from the literature club."
    show natsuki 5u at t11 zorder 1
    "Though I could see Natsuki growing more apprehensive as we got closer to the room."
    "I could even hear her worryingly muttering to herself during the walk."
    n 5q "It’s gotta be there...{w=0.38}it has to be!"
    mc "Natsuki?"
    n 5n "Hmm?"
    "Natsuki suddenly looks up at me, breaking her train of thought."
    mc "If it’s not in Ms. Suzuki’s room, do you know where else it might be?"
    n 5q "That’s what worries me..."
    stop music fadeout 3.0
    n 1m "If it’s not in there, maybe it’s in the lost and found..."
    n 12c "Or someone stole it..."
    show natsuki 12b
    mc "Aww come on, who’d want to steal something like that?"
    n 12a "[player]..."
    n 1h "It was 9,000 Yen..."
    mc "Oh..."

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            show natsuki 1u
            "I didn’t realize Parfait Girls was worth that much..."
            n 1m "It’s very easy to take something like that and re-sell it online..."
            n 1n "It happened to a girl I knew back in Middle School..."
            n 1m "And if it happens to me, there’s no way I’d be able to get it back..."
            n 12c "My Dad wouldn’t care enough to help me..."
            show natsuki 12b
            mc "I see..."
            n 1t "At least I have you helping me..."
            mc "Ah well, it’s nothing..."
            mc "That’s what friends are for, right?"
            n 5t "Y-{w=0.38}yeah..."
            n 5l "And you aren’t half-bad, [player]!"
            mc "Well, it’s the least I could for you..."
            n 1m "Hey..."
            n 1n "I really do appreciate it..."
            n 1q "I know I come across as rude and unapproachable sometimes..."

        if encore_sayoriquestion_1 == True:

            if encore_festivalquestion_2 == "Natsuki":
                n 1m "But you helping me out, showing that you actually care, really does help..."
                n 1s "I just wish we started talking sooner..."
                jump day3_arrival

            if encore_festivalquestion_2 == "Yuri":
                n 1n "Maybe that's why we haven't talked much..."
                n 1m "I didn't chase you away did I?"
                mc "No, it's not that..."
                mc "Look, you're a cool person, and we still have plenty of time to get to know each other."
                mc "We have an entire school year in front of us."
                jump day3_arrival

        if encore_sayoriquestion_1 == False:

            if encore_festivalquestion_2 == "Natsuki":
                n 1m "But knowing that you’ll be there for me, really does help..."
                n 1s "I'm surprised you still stick around..."
                jump day3_arrival

            if encore_festivalquestion_2 == "Yuri":
                n 1n "Maybe that's why we haven't talked much..."
                mc "Ah, well, let's not worry about that..."
                mc "We still have the entire school year in front of us."
                mc "It's plenty of time for us to get to know each other."
                jump day3_arrival



    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            show natsuki 1u
            "I didn’t realize Parfait Girls was worth that much..."
            n 1m "It’s very easy to take something like that and re-sell it online..."
            n 1n "It happened to a girl I knew back in Middle School..."
            n 1m "And if it happens to me, there’s no way I’d be able to get it back..."
            n 12c "My Dad wouldn’t care enough to help me..."
            show natsuki 12b
            mc "I see..."
            n 1t "At least you're helping out..."
            mc "Ah well, it’s nothing..."
            mc "That’s what friends are for, right?"
            n 5t "Y-{w=0.38}yeah..."
            n 5l "And you aren’t half-bad, [player]!"
            mc "Well, it’s the least I could for you..."
            n 1m "Hey..."
            n 1n "This really means a lot to me..."
            n 1q "I know I come across as rude and unapproachable sometimes..."

            if encore_sayoriquestion_1 == True:

                if encore_festivalquestion_2 == "Natsuki":
                    n 1m "But you helping me out, showing that you actually care, really does help..."
                    n 1s "I just wish we started talking sooner..."
                    jump day3_arrival

                if encore_festivalquestion_2 == "Yuri":
                    n 1n "Maybe that's why we haven't talked much..."
                    n 1m "I didn't chase you away did I?"
                    mc "No, it's not that..."
                    mc "Look, you're a cool person, and we still have plenty of time to get to know each other."
                    mc "We have an entire school year in front of us."
                    jump day3_arrival

            if encore_sayoriquestion_1 == False:

                if encore_festivalquestion_2 == "Natsuki":
                    n 1m "But you helping me out, showing that you actually care, really does help..."
                    n 1s "I'm just glad someone kind of cares about me for once..."
                    jump day3_arrival

                if encore_festivalquestion_2 == "Yuri":
                    n 1n "Maybe that's why we haven't talked much..."
                    mc "Ah, well, let's not worry about that..."
                    mc "We still have the entire school year in front of us."
                    mc "It's plenty of time for us to get to know each other."
                    jump day3_arrival



    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
            show natsuki 1u
            "I didn’t think something like Parfait Girls could go for that much..."
            n 1m "It’s very easy to take something like that and re-sell it online..."
            n 1n "It happened to a girl I knew back in Middle School..."
            n 1m "And if it happens to me, there’s no way I’d be able to get it back..."
            n 12c "My Dad wouldn’t care enough to help me..."
            show natsuki 12b
            mc "I see..."
            n 1t "At least I have you helping me..."
            mc "Ah well, it’s nothing..."
            mc "That’s what friends are for, right?"
            n 5t "Y-{w=0.38}yeah..."
            n 5l "And you aren’t half-bad, [player]!"
            mc "Well, it’s the least I could for you..."
            n 1m "Hey..."
            n 1n "I really do appreciate it..."
            n 1q "I know I come across as rude and unapproachable sometimes..."

            if encore_sayoriquestion_1 == True:

                if encore_festivalquestion_2 == "Natsuki":
                    n 1m "But you helping me out, showing that you actually care, really does help..."
                    n 1s "I just wish we started talking sooner..."
                    jump day3_arrival

                if encore_festivalquestion_2 == "Yuri":
                    n 1n "Maybe that's why we haven't talked much..."
                    n 1m "I didn't chase you away did I?"
                    mc "No, it's not that..."
                    mc "Look, you're a cool person, and we still have plenty of time to get to know each other."
                    mc "We have an entire school year in front of us."
                    jump day3_arrival

            if encore_sayoriquestion_1 == False:

                if encore_festivalquestion_2 == "Natsuki":
                    n 1m "But you helping me out, showing that you actually care, really does help..."
                    n 1s "I'm just glad someone kind of cares about me for once..."
                    jump day3_arrival

                if encore_festivalquestion_2 == "Yuri":
                    n 1n "Maybe that's why we haven't talked much..."
                    mc "Ah, well, let's not worry about that..."
                    mc "We still have the entire school year in front of us."
                    mc "It's plenty of time for us to get to know each other."
                    jump day3_arrival



    else:
        show natsuki 1u
        "I almost forgot how much manga can go for these days..."
        n 1m "It’s very easy to take something like that and re-sell it online..."
        n 1n "It happened to a girl I knew back in Middle School..."
        n 1m "And if it happens to me, there’s no way I’d be able to get it back..."
        n 12c "My Dad wouldn’t care enough to help me..."
        show natsuki 12b
        mc "I see..."
        n 1t "At least I have you helping me..."
        mc "Ah well, it’s nothing..."
        mc "That’s what friends are for, right?"
        n 5t "Y-{w=0.38}yeah..."
        n 5l "And you aren’t half-bad, [player]!"
        mc "Well, it’s the least I could for you..."
        n 1m "Hey..."
        n 1n "I really do appreciate it..."
        n 1q "I know I come across as rude and unapproachable sometimes..."

        if encore_sayoriquestion_1 == True:

            if encore_festivalquestion_2 == "Natsuki":
                n 1m "Maybe that's why we haven't been around each other lately..."
                n 1m "I didn't do something bad, did I?"
                mc "No, you didn't..."
                mc "Look, you're a cool person, and I had fun last Sunday, I really did!"
                mc "We have the rest of the school year to make memories together, so let's not dwell on any time that we could've had together, okay?"
                jump day3_arrival

            if encore_festivalquestion_2 == "Yuri":
                n 1n "Maybe that's why we haven't talked much..."
                n 1m "I didn't chase you away did I?"
                mc "No, it's not that..."
                mc "Look, you're a cool person, and we still have plenty of time to get to know each other."
                mc "We have an entire school year in front of us."
                jump day3_arrival

        if encore_sayoriquestion_1 == False:

            if encore_festivalquestion_2 == "Natsuki":
                n 1m "But you helping me out, showing that you actually care, really does help..."
                n 1s "I'm just wish we got more time together..."
                jump day3_arrival

            if encore_festivalquestion_2 == "Yuri":
                n 1n "Maybe that's why we haven't talked much..."
                mc "Ah, well, let's not worry about that..."
                mc "We still have the entire school year in front of us."
                mc "It's plenty of time for us to get to know each other."
                jump day3_arrival


label day3_arrival:
    show natsuki 5s
    "Natsuki nervously glances down at the floor."
    "I see that we’re at the room."
    mc "Hey, we’ll find it..."
    mc "I’m willing to walk around the entire school with you until we find it."
    show natsuki_sweet as natsuki at t11 zorder 1
    "Natsuki weakly smiles at me as she opens the door."
    play sound "sfx/closet-open.ogg"
    show natsuki_sweet as natsuki at thide
    hide natsuki
    scene bg class_day
    with wipeleft_scene
    "Sure enough, the room is free of the presence of anyone else, so we’ll be able to search freely."
    show natsuki 1u at t11 zorder 1
    "Natsuki walks over to desk and begins looking around for any sign of her manga."
    n 3m "This is where I last remember having it."
    show natsuki 3n
    mc "Well maybe it’s in her little bin..."
    "Usually, the teachers have their own little lost and found bins that they keep in their rooms before they go turn in it into the lost and found at the office."
    "I go to the front of the room where Suzuki keeps her bin and begin digging through it."
    n 1m "I’ll check in the closet, maybe someone put it in there..."
    mc "Good idea."
    show natsuki at thide
    hide natsuki
    "Natsuki walks to the back of the room and begins throwing stuff out of the closet."
    mc "Hey! You know we’re gonna have to put all that back, right?"
    n "We’ll worry about that later!"
    n "Finding that manga is priority number one right now!"
    "I just sigh as I continue neatly taking things out of the bin and searching for the manga."
    "I just hope she doesn’t tear this room apart in order to find it..."
    "Because either way, someone’s going to make me clean everything up..."
    scene bg class_day
    with wipeleft_scene
    "After searching the entire bin, I wasn’t able to find Natsuki’s manga."
    "I call out to Natsuki."
    mc "Any luck in the closet?"
    show natsuki 42b at t11 zorder 1
    "Natsuki emerges from the closet with a dejected look."
    n 42c "No..."
    n 42a "How about you?"
    "I shake my head."
    mc "It’s not in the bin."
    n 42b "Great..."
    play music t9 fadein 1.0
    show natsuki 12b at s11 zorder 1
    "Natsuki shuts her eyes as she slumps down next to the closet door."
    mc "N-{w=0.38}Natsuki?"
    n 12c "It took me months to save up for it..."
    n 12b "I had to skip out on lunch so many times..."
    n 12d "I had to beg my Dad to let me do his chores..."
    n 12e "It was pain enough to convince him to even give me an allowance..."
    n 12d "And now all my work was for nothing..."
    show natsuki at thide
    hide natsuki
    "Natsuki buries her face in her hands."
    "I stand there absolutely stunned with what I just heard."
    "I knew Natsuki never had the greatest relationship with her Father, but still..."
    "I can’t believe she put herself through all that just for some manga..."
    "And there probably isn’t much I can do right now to make her feel better..."
    "I sigh as I begin putting everything back in the bin."
    stop music fadeout 2.0
    "Suddenly, I notice a pink book stacked among several textbooks on Mrs. Suzuki’s desk."
    "That’s odd..."
    "I put bin back on the shelf and pull the pink book out."
    "..."
    "Well, I don’t believe it..."
    mc "Hey, Natsuki!"
    show cg n_day3cg_1 zorder 10 with dissolve_cg
    "Natsuki looks up at me with glossy, tear-filled eyes."
    show cg n_day3cg_2
    n "W-{w=0.38}what?!?"
    n "If you’re going to try to say something encouraging, save it..."
    show cg n_day3cg_1
    n "I give up..."
    mc "Well, you really shouldn’t..."
    n "We’re not going to find it!"
    mc "Are you sure about that?"
    show cg n_day3cg_2
    n "Eh?"
    "I hold up Natsuki’s manga."
    show cg n_day3cg_3
    n  "Are you serious?!?!"
    hide cg with dissolve_cg
    play music e3 fadein 1.0
    show natsuki 1l at t11 zorder 1
    "Natsuki wipes the tears from her eyes and abruptly stands up."
    n 1d "W-{w=0.38}where was it?!?"
    show natsuki 1a
    mc "Hiding between some textbooks."
    mc "I guess you accidentally handed it in..."
    n 1l "Who cares?!?!"
    "Natsuki practically runs up to me and takes the manga from me like Sayori takes her cupcakes..."
    show natsuki 1s
    "She carefully examines the manga to check for any creases or other damage before flipping through the book."
    n 1a "Yep...{w=0.38}just how I remember it!"
    "I can’t help but smile at Natsuki’s little celebration."
    mc "Well...{w=0.38}that’s one crisis averted for today, eh?"
    n 1y "That's a serious understatement!"
    mc "Ah, well..."
    "I nervously scratch the back of my head."
    mc "It was no trouble...{w=0.38}I’m just glad I could-"
    stop music
    play sound "sfx/fall.ogg"
    show natsuki_bliss as natsuki at face
    "Without warning Natsuki suddenly embraces me."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        "Much like yesterday, my mind goes blank."
        "I don’t know what’s gotten into Natsuki lately...{w=0.38}but I have to admit, I kind of like this side of her..."
        "Well, she did let me hug her back yesterday...."
        "I wrap my arms around her."
        "After a few minutes, Natsuki still isn't letting go."
        "That's...{w=0.38}unusual..."
        "Natsuki's not one for prolonged physical contact."
        "And my hugs with Sayori never really lasted this long..."
        "But, I'm not sure if I really should really break the hug, considering Natsuki seems to be in total bliss..."
        "And this is...{w=0.38}really nice..."
        "But, maybe she wants me to make the first move here..."
        "We can't stay like this forever..."

        if encore_sayoriquestion_1 == True:
            "And it isn't it kind of bad to be letting someone who isn't your signifcant other hold you for this long?"

        if encore_sayoriquestion_1 == False:
            pass

        menu:
            "Keep Hugging.":
                $ natsuki_continued_hug = True
                jump n_khug
            "Break The Hug.":
                $ natsuki_continued_hug = False
                jump n_bhug


if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        "Much like yesterday, my mind goes blank."
        "I don’t know what’s gotten into Natsuki lately...{w=0.38}but I have to admit, I kind of like this side of her..."
        "But, she could just be using this moment to let out her stress..."
        "If I risk hugging her back, she'll probably have another meltdown..."
        "But she did let me hug her back yesterday..."

        if encore_sayoriquestion_1 == True:
            "But, I'm already enough in trouble because of it..."

        if encore_sayoriquestion_1 == False:
            pass



if hangout1 == "Natsuki":
    if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
        "This is...{w=0.38}unexpected..."
        "Natsuki's not exactly one to go out of her way to hug people..."

        if encore_festivalquestion_2 == "Natsuki":
            "In fact, I've barely gotten close to her at all, except that one time lat Sunday..."

        if encore_festivalquestion_2 == "Yuri":
            "In fact, I've barely gotten close to her at all, knowing how she'll freak out and call me gross..."

        "Not to mention, she didn't like seeing me getting close to [hangout2] yesterday..."
        "So I'd be risking her calling me out on that..."
        "But considering she isn't showing any signs of letting go, it really wouldn't hurt to return the hug, would it?"

        if encore_sayoriquestion_1 == True:
            if hangout2 == "Monika" or hangout2 == "Yuri":
                "Though, Sayori was pretty angry at me yesterday for getting too close to [hangout2]..."


        if encore_sayoriquestion_1 == False:
            pass


else:
    "This is...{w=0.38}unexpected..."
    "In fact, Natsuki specfically said she didn't even want to hug me..."

    if encore_festivalquestion_2 == "Natsuki":
        "In fact, I've barely gotten close to her at all, except that one time last Sunday..."

    if encore_festivalquestion_2 == "Yuri":
        "In fact, I've barely gotten close to her at all, knowing how she'll freak out and call me gross..."

    "Not to mention, she didn't like seeing me getting close to [hangout2] yesterday..."
    "So I'd be risking her calling me out on that..."
    "But considering she isn't showing any signs of letting go, it really wouldn't hurt to return the hug, would it?"

    if encore_sayoriquestion_1 == True:
        if hangout2 == "Monika" or hangout2 == "Yuri":
            "Though, Sayori was pretty angry at me yesterday for getting too close to [hangout2]..."


    if encore_sayoriquestion_1 == False:
        "Though, if I do hug her, would she think I like her as more than a friend?"



menu:
    "Hug Natsuki Back.":
        $ natsuki_hug = True
        jump n_hug
    "Stay Still.":
        $ natsuki_hug = False
        jump n_nohug


label n_hug:

    if encore_sayoriquestion_1 == True:
        "I mean, it's just a hug..."
        "I wrap my arms around her."
        jump day3_npos

    if encore_sayoriquestion_1 == False:
        "I wrap my arms around her."
        jump day3_npos

label n_khug:

    if encore_sayoriquestion_1 == True:
        "I mean, it's just a hug..."
        "And she can pull away when she wants to..."
        "I keep Natsuki in my embrace."
        jump day3_npos

    if encore_sayoriquestion_1 == False:
        "Ah, I'm sure she'll pull away when she wants to..."
        "I keep Natsuki in my embrace."
        jump day3_npos

label day3_npos:

    "She really does go out of her way to make herself cute as possible..."
    show natsuki_sweet as natsuki at t11 zorder 1
    "Suddenly, I feel Natsuki pull away from me."
    mc "What is it?"
    n 1h "N-{w=0.38}nothing!"
    n 1q "Nothing at all..."
    show natsuki 1i
    "Natsuki’s barely able to hide her grin as she’s barely able to look at me."
    n 1t "T-{w=0.38}thanks for finding it...{w=0.38}[player]..."
    mc "No problem..."
    show natsuki_sweet as natsuki at t11 zorder 1
    "We stand there awkwardly for a moment, neither of sure of what to do next."
    "I would offer to continue the hug, but it seems the magic of the moment has fleeted."
    n 1m "H-{w=0.38}hey, [player]?"
    show natsuki 1n
    mc "Yeah?"
    play music t9 fadein 1.0
    n 1m "Can you...{w=0.38}promise not to tell any of the others what I was saying earlier?"
    show natsuki 1n
    mc "About how you saved up so much money to get that?"
    show natsuki 12b
    "Natsuki merely nods."
    mc "I mean, I’m not gonna tell anyone, but..."
    mc "You didn’t need to go that far to get this, Natsuki."
    n 12c "No offense, [player], but you really don’t understand what my life is like..."

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            mc "You never really did give the full picture..."
            n 42a "I’ll give you a summary..."


    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            mc "I really don't..."
            n 42a "Well, let me tell you something..."

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":
            mc "I really don't..."
            n 42a "Well, let me tell you something..."


    else:
        mc "I mean, I don't..."
        mc "We really don't know that much about each other..."
        n 42a "Well, let me tell you about my home life..."
        n 42bb "Short version: it sucks."
        mc "Can I get a longer version?"
        show natsuki 42c
        "Natsuki let's out a pained sigh."


    n 5q "If I ever want anything for myself, it costs an arm and a leg..."
    n 5r "My Dad’s so friggin’ selfish..."
    n 4x "It’s not like we’re tight on money or anything, in fact, we’re decently well-off..."
    n 4w "He spends it all on himself!"
    n 42a "He barely sees me as his own child..."
    n 42b "Just as some nuisance he has to deal with for at least two more years..."
    n 5m "Sometimes he’s so ridiculously strict, and other times, he just doesn’t care about what I do..."
    n 42b "We fight a lot to say the least..."
    mc "I’m...{w=0.38}really sorry, Natsuki..."
    mc "I wish there was something I could do..."
    n 42a "You can’t."
    n 1q "I just have to put up with his crap until I move away to college."
    n 2h "He’s more than happy to send me as far away as possible if it means he doesn’t have to see me anymore..."
    n 2r "He even hated the idea of having to give me an allowance! He just spends most of his time at home drinking beer in front of our tv!"
    n 2x "He’s just so...!"
    show natsuki 42c
    "Natsuki lets out a deep sigh."
    n 42a "I just hope you get along with your parents, [player]."
    n 42b "It’s something I never got the chance to experience..."
    mc "I’d say they’re fair for the most part..."
    show natsuki 1t
    "Natsuki lets out a slight chuckle."
    n 1l "Well, looks like they didn’t do too bad with you..."
    mc "I’ll be sure to tell them that the next time I see them."
    n 1k "They’re not around?"
    mc "They’re out in the countryside helping my Grandparents out..."
    n 1u "Oh..."
    n 3h "I never met mine..."
    n 5m "Heck, I’ve only ever really known my Dad for a good chunk of my life..."
    mc "What happened to your Mom?"
    show natsuki 12d
    "Natsuki shuts her eyes as if she’s trying to suppress her tears."
    mc "I-{w=0.38}it’s fine..."
    mc "I’m sure that she’s a great person and would be proud of who you are..."
    $ renpy.pause(delay=0.8, hard=True)
    show natsuki 12a
    $ renpy.pause(delay=0.8, hard=True)
    show natsuki 5u
    $ renpy.pause(delay=0.8, hard=True)
    show natsuki 5t
    n "Heh...{w=0.38}I’d like think that too..."
    n 1a "Anyways, I guess that’s enough reminiscing about my messed up childhood..."
    n 1d "We should probably get back before Monika throws a major fit or something!"
    mc "I’d be more worried about Sayori calling me a hundred times..."
    n 1y "Ha! I know what you mean!"
    n 1z "Let’s go, [player]!"
    "With her manga in hand, Natsuki and I exit the classroom and head back to the literature club."
    stop music fadeout 1.0
    show natsuki at thide
    hide natsuki
    jump day3_nreturn1


label n_nohug:

    "I stand there as Natsuki continues to squeeze me tighter."
    "Just let it out Natsuki..."
    show natsuki 1u at t11 zorder 1
    "After a few moments, she loosens her grip and steps back."
    jump day3_nminus

label n_bhug:

    show natsuki 1u at t11 zorder 1
    "I gently release myself from Natsuki and take a step back."
    show natsuki 1n
    "Natsuki gives me a hurt look, as if she wanted our hug to continue."
    jump day3_nminus

label day3_nminus:

    n 5q "Well...{w=0.38}uh...{w=0.38}T-{w=0.38}thanks for finding it, [player]."
    show natsuki 5s
    mc "No problem, Natsuki..."
    mc "It’s what friends are for, right?"
    n 5q "Y-{w=0.38}yeah...{w=0.38}friends..."
    show natsuki 5u
    "Natsuki looks off to the side as a mix of emotions swirl on her face."
    mc "You okay, Natsuki?"
    n 5m "Hmm? Yeah, I’m fine I guess..."
    mc "I thought you’d be happy that we got the manga back?"
    n 12c "I am, it’s just..."
    n 12b "Ugh! Nevermind!"
    n 1s "Let’s just go back to the clubroom..."
    mc "Alright..."
    "Natsuki averts eye-contact with me as she clutches her manga tightly and walks out of the clubroom."
    show natsuki at thide
    hide natsuki
    "I just don’t get her sometimes..."
    "I sigh as I start fast walking to catch up to her."
    jump day3_nreturn2



label nencore_4:

play music t6 fadein 2.0
scene bg school
with wipeleft_scene
"Sure enough, I take my usual route to school and I arrive pretty much on the dot."
"As I'm waiting on the sidewalk by the school, I peer both ways down the street for any sign of Natsuki."
"Surprisingly, not only is there no sign of Natsuki, but there's hardly anyone around."
"Well then again, who hangs around after school on a Wednesday?"
"I'm sure she'll be here any minute, the bus runs pretty periodically through here anyways."
"I just hope I don't get called out for looking too suspicious..."
$ n_name = "???"
n "Hey, weirdo! What are you doing?"
$ n_name = "Natsuki"
"Damn it."
"I turn my head to see who was yelling at me."
show natsuki 1ba at t11 zorder 1
"Unsurprisingly, I see Natsuki walking over towards me."
show natsuki 5bg
mc "You're late."
"I say teasingly."
n 5bw "It's not my fault! There was a lot of traffic out on Rockefeller street!"
mc "There's always traffic on Rockefeller street..."
n 4bx "Exactly! That's why I just I got off the bus and walked all the way here."
n 5bd "By the time I rode it all the way here, you probably would've gotten the cops called on you or something for standing like a weirdo by the school!"
show natsuki 5bz
mc "Good to see you didn't leave your sense of humor on the bus..."
show natsuki 1bx
n "Uuu..."
"Natsuki lightly punches me in the arm."
mc "Hey! What was that for?"
n 3by "For acting like a smart ass!"
n 3bz "And there's more where that came from if you keep acting like one!"
mc "Dually noted..."

if natsuki_continued_hug == True:
    jump n_line_13

if natsuki_continued_hug == False:
    jump n_line_14

if natsuki_hug == True:
    jump n_line_13

if natsuki_hug == False:
    jump n_line_14

label n_line_13:

"Natsuki joyfully giggles."
"She always did have a twisted sense of humor..."
"Can't say I'm not that different either..."
jump n_walk

label n_line_14:

"Considering my screw up around her earlier today, I imagine she wouldn't hesistate to let loose on me if I stepped out of line."
"In fact, I'm surprised how quickly she seems to have gotten over it."
"Not that she's one to hold onto gruges for very long, but I should probably be more careful around her..."
jump n_walk





label n_walk:

n 3bb "Anyways, let's get going!"
n 3bc "We wait any longer and they'll be totally sold out!"
mc "Yeah, let's get going!"
show natsuki 3ba
"Natsuki and I begin making our way in the direction of the city."
show natsuki at thide
hide natsuki
scene bg city_sidewalk
with wipeleft_scene
"Early on, Natsuki and I are able to move at a pretty rapid pace towards the bookstore."
"But our progress gets hindered by a growing number of people crowding on the sidewalk the farther we get into the city."
"And thanks to all the cars driving, there isn't exactly a safe way of bypassing the crowds, so we're forced to move with them block to block."
show natsuki 5br at t11 zorder 1
"At one point, Natsuki tried taking me by the arm in attempt to cut through the crowd, but I really couldn't keep up with her thanks to her small size."
show natsuki 5bx
"Naturally, that irritated her."
n 5bw "You just had to be so tall!"
mc "Well, it's not like I can do much about it..."
mc "I'm pretty sure we're almost there..."
n 1bm "We still got two more blocks to go, [player]..."
n 1bq "I'm just worried it'll be sold out by the time we get there..."
show natsuki 1bn
mc "I'm sure there's bound to be at least a few copies left..."
mc "You think they would've planned for this sort of thing..."
n 1bq "I hope so..."
n 1bn "I don't think I'd have time to walk to the other store and make it back in time before my dad gets home..."
n 1bu "And I don't really want to order it online..."
mc "Right..."

if natsuki_continued_hug == True:
    jump n_d_3

if natsuki_continued_hug == False:
    jump n_d_4

if natsuki_hug == True:
    jump n_d_3

if natsuki_hug == False:
    jump n_d_4


label n_d_3:

"I remembered that with the way Natsuki described her father to me, he doesn't exactly seem lke the most open-minded person..."

if encore_sayoriquestion_1 == False:
    "In fact, I remembered that there was a rather specfic reason that Natsuki stored her manga collection in school rather then at home..."
    "But even then, I'm sure she's stowed away a few copies in her room somewhere..."

    if hangout1 == "Monika" or hangout2 == "Monika":
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 0.70
        hide screen tear
        pause 1.0
        $ style.say_dialogue = style.edited
        n "I don't even know what my dad would do if he found this!"
        n "He'd probably beat the shit out of me because I'm an ungrateful little twerp!"
        $ style.say_dialogue = style.normal
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        "I blink a few times just to make sure I didn't just imagine Natsuki saying that."
        show natsuki 1bn
        mc "Did you say something?"
        "Natsuki shoots me a puzzled look."
        n 1bk "No, why?"
        mc "Ah, forget that..."
        "Maybe I just heard some random conversation..."
        mc "Anyways..."
        jump n_converge

    else:
        pass
        jump n_converge


if encore_sayoriquestion_1 == True:
    "I guess that's why she's resorted to storing her manga in the closet back at the clubroom..."
    "From the times I've seen it, it's a pretty large collection, no wonder why she's always fighting with Monika about it..."

    if hangout1 == "Monika" or hangout2 == "Monika":
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 0.70
        hide screen tear
        pause 1.0
        $ style.say_dialogue = style.edited
        n "I don't even know what my dad would do if he found it!"
        n "He'd probably beat the shit out of me because I'm an ungrateful little twerp!"
        n "I don't even know why Monika tolerates putting trash in the closet! It belongs in the garbage!"
        $ style.say_dialogue = style.normal
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        "I blink a few times just to make sure I didn't just imagine Natsuki saying that."
        show natsuki 1bn
        mc "Did you say something?"
        "Natsuki shoots me a puzzled look."
        n 1bk "No, why?"
        mc "Ah, forget that..."
        "Maybe I just heard some random conversation..."
        mc "Anyways..."
        jump n_converge

    else:
        pass
        jump n_converge

label n_d_4:

if encore_sayoriquestion_1 == False:
    "I remembered that there was a reason that Natsuki stored her manga collection in school rather then at home..."
    "But even then, I'm sure she's stowed away a few copies in her room somewhere..."
    "I think she said something about being afraid if her dad found out about her collection..."

    if hangout1 == "Monika" or hangout2 == "Monika":
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 0.70
        hide screen tear
        pause 1.0
        $ style.say_dialogue = style.edited
        n "I don't even know what my dad would do if he found this!"
        n "He'd probably beat the shit out of me because I'm an ungrateful little twerp!"
        $ style.say_dialogue = style.normal
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        "I blink a few times just to make sure I didn't just imagine Natsuki saying that."
        show natsuki 1bn
        mc "Did you say something?"
        "Natsuki shoots me a puzzled look."
        n 1bk "No, why?"
        mc "Ah, forget that..."
        "Maybe I just heard some random conversation..."
        mc "Anyways..."
        jump n_converge

    else:
        pass
        jump n_converge

if encore_sayoriquestion_1 == True:
    "I'm not entirley sure why Natsuki doesn't keep her manga at home like most people would..."
    "Maybe she's embrassed at what her parents would think if they saw it?"
    "Then again, the series does seem something typical that girls would read..."
    "Even if it might be a little out of Natsuki's age range..."
    "Still, I'm sure she as a perfectly good reason for storing all her manga in the closet back at the club..."

    if hangout1 == "Monika" or hangout2 == "Monika":
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 0.70
        hide screen tear
        pause 1.0
        $ style.say_dialogue = style.edited
        n "I don't even know what my dad would do if he found this!"
        n "He'd probably beat the shit out of me because I'm an ungrateful little twerp!"
        $ style.say_dialogue = style.normal
        $ _history_list.pop()
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        "I blink a few times just to make sure I didn't just imagine Natsuki saying that."
        show natsuki 1bn
        mc "Did you say something?"
        "Natsuki shoots me a puzzled look."
        n 1bk "No, why?"
        mc "Ah, forget that..."
        "Maybe I just heard some random conversation..."
        mc "Anyways..."
        jump n_converge

    else:
        pass
        jump n_converge



label n_converge:

mc "I'm sure that all the bookstores in town have the new copy on them..."
n 1bm "Well it's usually avalible first at the one we're going to..."
n "It's where I got the last few editions when they just came out."
n 1bn "I couldn't get the last edition on the day it came out, I had to go the week after to get it then..."
mc "Well I can get it for you if we can't find it there..."
mc "It's not like I have any plans for tonight..."
"Except trying to sort out the cluster that is my emotions right now..."
n 1bm "You don't have to do that for me, [player], really..."
mc "I insist..."
show natsuki 5bu
"Natsuki pauses for a moment to think over my offer."
show natsuki 5bw
"Eventually she lets out a defeated sigh."
n 5bq "Well...{w=0.38}let's just see if they have it first..."
mc "Seems reasonable to me."
n 5bt "Thank you, [player]..."
mc "Ah, don't mention it..."

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        mc "I know how much you love the series."
        n 4bl "Well, you aren't wrong..."

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 2bt "And it seems like you've been enjoying it so far..."
                show natsuki 2ba
                mc "I have."

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 2bt "I'm just glad I got you to stick to reading the series..."
                show natsuki 2ba
                mc "You've done a pretty good job so far..."

        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 2bq "Though we are kind of falling behind..."
                show natsuki 2ba
                mc "Yeah, I really want to get back into the swing of things..."
                mc "It's just there's been a lot going on my end lately..."


        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n 2bu "Though we really need to catch up..."
                show natsuki 2ba
                mc "Yeah, I really want to get back into reading it..."
                mc "It's just there's been a lot going on my end lately..."



if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        mc "You seem pretty into the series, so..."
        n 4bl "Guilty as charged on that one!"

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 2bt "And it seems like you've been enjoying it so far..."
                show natsuki 2ba
                mc "I have."

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 2bt "You seemed like you were getting into it yesterday..."
                show natsuki 2ba
                mc "I was."

        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 2bq "To bad we haven't been able to read together yet."
                show natsuki 2ba
                mc "Well hey, the new edition is gonna provide some motivation!"


        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n 2bq "I just wish I can get you into reading it."
                show natsuki 2ba
                mc "Well, I'm more than willing to sit down and read with you sometime!"
                mc "The new edition is going to provide some extra motivation!"



if encore_sayoriquestion_1 == True:
    mc "I can tell you're really into the series, so..."
    n 4bl "You'd be right!"

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            n 2bt "And it seems like you've been enjoying reading the series so far..."
            show natsuki 2ba
            mc "I have."


    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            n 2bt "You seemed pretty interested yesterday yourself..."
            show natsuki 2ba
            mc "I did, and still am!"

    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            n 2bq "Sucks we've lucked out on reading together..."
            show natsuki 2ba
            mc "Well hey, with the new edition, we'll have a reason to find time together!"

    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            n 2bq "I just wish I can get you into reading it."
            show natsuki 2ba
            mc "Well, I'm more than willing to sit down and read with you sometime!"
            mc "The new edition is going to provide some extra motivation!"


mc "Anyways, I think we're here."
"We promptly stop right by the entrance to the bookstore."
n 1bc "Yep! This is the place!"
mc "I knew this looked familiar..."
n 3bk "You've been here before?"
mc "Yeah, a few times..."
mc "Haven't had the chance to go recently."
n 3bl "Well you'll see how much they've expanded their manga section!"
n 4bl "They actually ended up moving it to the second floor!"
mc "Woah, really?!? That's awesome!"
mc "I'll let you lead the way, ladies first after all..."
"I gesture for Natsuki to enter the store."
n 5by "Wow! What a gentleman!"
"She says sarcastically."
mc "So you doubt me?"
"I walk over and hold the door open for Natsuki."
show natsuki 5bz
"She lets out a small laugh before eventually composing herself."
n 4by "Okay, okay...{w=0.38}I believe you."
show natsuki 1bj
"Natsuki happily enters the bookstore with me tailing right behind her."
scene bg library
with wipeleft_scene
"As we step into the lobby, we're greeted with a long line by the register, with additional clusters of people walking around and looking at the various shelves."
show natsuki 1bu at t11 zorder 1
"That only makes Natsuki even more visibly anxious."
"Noticing this, I try to reassure her."
mc "Well...{w=0.38}it doesn't seem like there's too many people coming up and down the stairs..."
n 1bq "Let's hope they're not sold out..."
"Natsuki and I head to the stairwell and walk up to the second floor."
show natsuki at thide
hide natsuki
scene bg manga
with wipeleft_scene
stop music fadeout 2.0
"As so as we reach to the second floor, Natsuki anxiously rushes to the manga section, while I slowly follow behind her."
show natsuki 1bu at t11 zorder 1
"Natsuki frantically begins searching through the shelves to find anything related to Parfait Girls, while I'm on the otherside browsing at the selection."
"Considering Natsuki has probably spent much more time here than me, chances are she'd find it sooner."
"As I'm browsing, I come across some old familar titles I used to read when I was kid."
"'Exterminator'...{w=0.38}'Interstellar Pirates'..."
"Hey! This is something I haven't read in a long time!"
"I pull off the shelves a copy of 'The Galaxy War Chronicles'..."
"I lost my copies of these years ago!"
"It was one of my favorite things to read growing up..."
"I even remember seeing the movies with Sayori..."
"Though it was her more reluctantly seeing it with me so we can get ice cream afterwards..."
"In fact, I didn't even know that these were still in distribution, let alone that they were still making new editions!"
"And it would look like I could just about afford it!"
"I can probably order the previous volumes online somewhere..."
show natsuki 1bz at h11 zorder 1
play music e3 fadein 2.0
n "YES!"
"My train of thought is interupted by Natsuki's sudden cheering."
mc "What is it?"
n "I found it!"
show natsuki at thide
hide natsuki
show cg n_day3_h2 with dissolve_cg
"Natsuki proudly twirls around as she clutches the book close to her chest."
"I just stand there smiling as Natsuki does her little celebration."
"She really is something..."
"Even though she can be a handful at times, seeing her this happy is quite infectious."
"She probably doesn't even realize how cute she looks right now..."
"All things considered, Natsuki isn't that hard of a person to make happy, so long as you keep an open and understanding mind..."
"It makes me wonder if I can make her even more happy..."
"Suddenly I see Natsuki twirling a little too close to the bookshelves."
mc "Hey, just make sure you don't hit the shelves..."
scene bg manga
show natsuki 1be at t11 zorder 1
n "Oh come on! It's not like I'm that clumsy!"
show natsuki 1bg
mc "Heh, well fair point..."
mc "But hey, I'm glad you found it!"
n 4bl "It was the last copy they had!"
mc "I guess we're just that lucky."
n 4bt "Yeah..."
n 4by "I'm glad you could share in the moment with me, [player]!"
mc "Hey, it's what I do..."
n 2bk "Are you getting anything while we're here?"
mc "Yeah, I'm getting this!"
show natsuki 2bc
"I proudly show Natsuki the copy of 'The Galaxy Chronicles'."
n "'The Galaxy Chronciles', huh?"
n 2bd "I haven't read it recently, but it's pretty good!"
n 2bt "Even if it's a little boy-ish for my tastes..."
mc "Well, maybe we can read this one together too!"
mc "We can broaden our horizons together!"
n 4by "Well, look at you, getting me to into other kinds of manga!"
n 5by "Looks like the student has become the master!"
mc "Ah, well..."
"I embarrassingly scratch the back of my head."
mc "That's how the literature club works, doesn't it?"
mc "Stepping outside our comfort zones to read new things?"
n 1ba "Yep! Pretty much!"
n 1bt "Anyways, let's head downstairs and buy these!"
n 1bz "I'm already getting excited just thinking about reading them!"
mc "You and me both!"
"Natsuki and I happily trot downstairs to the register."
show natsuki at thide
hide natsuki
scene bg library
with wipeleft_scene
"Despite a relatively long wait in line, we're finally able to have our turn at the register."
show natsuki 1ba at t11 zorder 1
"Being the gentleman I am, I let Natsuki go first."
stop music fadeout 2.0
show natsuki 5bu
"However, her cheerful mood quickly disappears as the price comes up on the screen."
show natsuki
"She's had to have counted her money at least a dozen times before finally letting out a defeated sigh."
n 5bq "[player]..."
play music t9
n 5bm "I don't think I can afford it..."
n 5bu "It was a lot more than I thought it'd be..."
mc "How short are you?"
n 12ba "300 yen..."
mc "Oh..."
"Yikes."
"We pull ourselves briefly to the side to let the peple behind us pay for their things."
n 12bb "This is my fault...{w=0.38}I should've known it would've been that expensive..."
n 12ba "Even though I've been saving up for months now..."
show natsuki 12bd
"Natsuki clenches the manga tightly in an effort to compose herself."
"I decide to look down my wallet."
"Well, if we pool our money together, we could afford it..."
"Though I wouldn't be able to buy the copy I wanted..."
"Well...{w=0.38}Natsuki clearly wants her copy more than I want mine, so..."
mc "Natsuki."
show natsuki 12ba
n "W-{w=0.38}what?"
"She looks as tears start to well in her eyes."
mc "If we pool our money together, we can afford it."
n "[player], no..."
n "Don't bail me out because of my mistake..."
mc "But you didn't do anything wrong!"
mc "Trust me...{w=0.38}you want your manga more than I want mine..."
mc "I can get this whenever..."
n 12bc "[player]..."
n 12ba "Why are you so nice to me?"

if natsuki_continued_hug == True:
    jump n_d_5

if natsuki_continued_hug == False:
    jump n_d_6

if natsuki_hug == True:
    jump n_d_5

if natsuki_hug == False:
    jump n_d_6

label n_d_6:

n "Especially since I blew up at you earlier..."
n "I didn't even think you'd want to go with me..."
mc "Look, what happened earlier was my fault...{w=0.38}okay?"
mc "I just kinda froze..."
mc "It was my fault for misunderstanding, and I'm sorry..."
show natsuki 12be
n "I'm sorry for blowing up at you earlier too..."
show natsuki 42bd
"We stand there awkwardly by the register for a few moments as people continue to walk in and out of the lobby."
mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"
show natsuki 42be
"Natsuki reluctantly sighs."
stop music fadeout 2.0
n 42bb "Alright, fine..."
n 12ba "Just don't tell anyone about this, okay?"
mc "You have my word."
"Natsuki sheepishly hands over her money and the manga as I walk over to re-join the line."
"After a few minutes I'm able to pay for Natsuki's manga, return my own and begin our walk back."
show natsuki at thide
hide natsuki
jump n_resolved


label n_d_5:

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n "I know I haven't always been nice back..."
                n "But you've put up with me better than anyone ever has!"
                n 42bb "I'm just so selfish and self-asborbed..."
                show natsuki 12ba
                mc "No, you aren't..."
                mc "Look, I understand you better than anyone in the club."
                mc "I know why you're like this..."
                mc "And, it doesn't change my opinion on you, it just makes me want to spend more time around you!"
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me pay for the manga, okay?"



        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n "I was a little worried that you didn't want to talk to me on Monday when you were [hangout1]..."
                n "And I know I wasn't in the best mood at the time..."
                n 12bb "And I wasn't really sure how I felt about us being together yesterday..."
                show natsuki 42ba
                mc "It was surprsing to be sure..."
                mc "But look, I understand you better than anyone in the club right now."
                mc "I know why you're like this..."
                mc "And, it doesn't change my opinion on you, it just makes me want to spend more time around you!"
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me pay for the manga, okay?"



        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n "I know we haven't had the chance to spend a lot of time together recently..."
                n "But I thought that was because I did something to piss you off..."
                n 42bb "I thought I might've accidentally driven you away..."
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been meaning to spend more time with you."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your home situation..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"



        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n "And why are you showing so much interest in me now?"
                n "We haven't really been around each other since the festival..."
                n 42bb "I didn't mean to drive you away or anything..."
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been meaning to spend more time with you."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your home situation..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"




show natsuki 42be
"Natsuki reluctantly sighs."
stop music fadeout 2.0
n 12bb "Alright, fine..."
n 12ba "Just don't tell anyone about this, okay?"
mc "You have my word."
"Natsuki sheepishly hands over her money and the manga while I quickly walk over to re-join the line."
"After a few minutes I'm able to pay for Natsuki's manga, return my own and begin our walk back."
show natsuki at thide
hide natsuki
jump n_resolved

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n "And why are you showing so much interest in me now?"
                n "Ever since the festival, you've been coming over and talking to me..."
                n 42bb "And I remember how gross I thought you were..."
                n "But I've just been wrong..."
                n "I'm sorry for driving you away..."
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "Look, I understand now why you're like this..."
                mc "It doesn't really make me think any less of you..."
                mc "And I want to spend more time around you!"
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"


        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n "And why are you showing so much interest in me now?"
                n "You've only started coming to talk to me since yesterday!"
                n 42bb "And I remember how gross I thought you were..."
                n "But I've just been wrong..."
                n "And I didn't know if you were going to come back to me after yesterday..."
                show natsuki 12ba
                mc "Well yesterday was still kind of surprsing..."
                mc "But, you didn't do anything wrong, Natsuki..."
                mc "Look, I understand now why you're like this..."
                mc "It doesn't really make me think any less of you..."
                mc "And I want to spend more time around you!"
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"



        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n "And why are you showing so much interest in me now?"
                n "You've only started coming to talk to on Monday, and you didn't even come back to talk to me yesterday!"
                n 42bb "What's the big idea, [player]?"
                n "Did I do something wrong?"
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been meaning to spend more time with you."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your home situation..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"



        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n "And why are you showing so much interest in me now?"
                n "We haven't really been around each other..."
                n 42bb "I was afraid that I pushed you away..."
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been wanting to get to know better for a while now.."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"

show natsuki 42be
"Natsuki reluctantly sighs."
stop music fadeout 2.0
n 12bb "Alright, fine..."
n 12ba "Just don't tell anyone about this, okay?"
mc "You have my word."
"Natsuki sheepishly hands over her money and the manga while I quickly walk over to re-join the line."
"After a few minutes I'm able to pay for Natsuki's manga, return my own and begin our walk back."
show natsuki at thide
hide natsuki
jump n_resolved

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri" or encore_festivalquestion_2 == "Natsuki":

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n "And why are you showing so much interest in me now after you've spent so much time with Sayori?"
                n "Ever since the festival, you've been coming over and talking to me..."
                n 42bb "And I remember how gross I thought you were..."
                n "But I've just been wrong..."
                n "I'm sorry for driving you away..."
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "Look, I understand now why you're like this..."
                mc "It doesn't really make me think any less of you..."
                mc "And I want to spend more time around you!"
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"


        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n "And why are you showing so much interest in me now after you've spent so much time with Sayori?"
                n "You've only started coming to talk to me since yesterday!"
                n 42bb "And I remember how gross I thought you were..."
                n "But I've just been wrong..."
                n "And I didn't know if you were going to come back to me after yesterday..."
                show natsuki 12ba
                mc "Well yesterday was still kind of surprsing..."
                mc "But, you didn't do anything wrong, Natsuki..."
                mc "Look, I understand now why you're like this..."
                mc "It doesn't really make me think any less of you..."
                mc "And I want to spend more time around you!"
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"

        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n "And why are you showing so much interest in me now after you've spent so much time with Sayori?"
                n "You've only started coming to talk to on Monday, and you didn't even come back to talk to me yesterday!"
                n 42bb "What's the big idea, [player]?"
                n "Did I do something wrong?"
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been meaning to spend more time with you."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your home situation..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"

        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n "And why are you showing so much interest in me now after you've spent so much time with Sayori?"
                n "We haven't really been around each other..."
                n 42bb "I was afraid that I pushed you away..."
                show natsuki 12ba
                mc "You didn't do anything wrong, Natsuki..."
                mc "I've been wanting to get to know better for a while now.."
                mc "I just haven't gotten the chance to until today..."
                mc "I'm sorry if you felt like I was avoding you..."
                mc "Espeically now considering how you explained to me your life outside of school..."
                show natsuki 42bb
                "Natsuki clenches the manga tighter."
                mc "Look...{w=0.38}let me make it up to you and pay for the manga, okay?"

show natsuki 42be
"Natsuki reluctantly sighs."
stop music fadeout 2.0
n 12bb "Alright, fine..."
n 12ba "Just don't tell anyone about this, okay?"
mc "You have my word."
"Natsuki sheepishly hands over her money and the manga while I quickly walk over to re-join the line."
"After a few minutes I'm able to pay for Natsuki's manga, return my own and begin our walk back."
show natsuki at thide
hide natsuki
jump n_resolved


label n_resolved:

play music t8 fadein 2.0
scene bg city_sidewalk
with wipeleft_scene
show natsuki 5bu at t11 zorder 1
"As we walk out of the bookstore, I hand the bag over to Natsuki."
n 5bq "You really didn't have to do that for me, [player]..."
mc "It's nothing, really..."
mc "That's what friends are for, right?"
show natsuki 1bq
"Natsuki doesn't answer and simply sheeplishly takes the bag as we start walking, but after a few minutes she speaks up again."
n 1bm "I really can't thank you enough, [player]..."
n "Nobody's ever been that kind to me..."
show natsuki 5bn
mc "Well, hopefully I won't be the last person to treat you fairly..."
mc "I'm just glad I'm your friend, Natsuki."
mc "You're not so bad to hang around..."
n 5bt "Y-{w=0.38}yeah...{w=0.38}you too..."
"Natsuki blushes brightly as we continue on the direction to the school."
show natsuki at thide
scene bg school
with wipeleft_scene
"The walk back to school was surprisingly quicker than it was to the bookstore."
"Though it does mean that it's pretty much time for Natsuki and I to part ways until tomorrow."
show natsuki 5bk at t11 zorder 1
mc "Well...{w=0.38}I guess this is your stop..."
show natsuki 5bq
n "Yeah...{w=0.38}I guess so..."
"Theres an obvious trace of disappointment in her voice as she looks down at the ground."
mc "Well, I can stay until the bus comes if you'd want..."
n 5bm "Actually..."
n 5bq "Do you...{w=0.38}mind if I walk you back to your place?"
n 5bn "I know I have some time before my dad comes home..."
"I'm thrown off by Natsuki's request."
"I mean...{w=0.38}I wouldn't mind spend some more time with her, but I'm not exactly sure why she'd want to walk me back with me."

if natsuki_continued_hug == True:
    jump n_d_7

if natsuki_continued_hug == False:
    jump n_d_8

if natsuki_hug == True:
    jump n_d_7

if natsuki_hug == False:
    jump n_d_8

label n_d_7:

"Though I don't want to screw this up again with Natsuki, so I'll take her up on her off this time."

label n_d_8:

pass

mc "Uh...{w=0.38}sure..."
mc "I wouldn't mind..."
n 4bd "Great!"
"I'm not sure what her motivation is here, but I'll roll with it."
show natsuki 1bj
"We start walking back to my place, with Natsuki noticeably walking closer to me than normal."
stop music fadeout 2.0
scene bg residential_day
with wipeleft_scene
"The walk back was mostly silent, with Natsuki almost holding my hand at a few points."
"I shoot her an occasional look, but she doesn't seem to notice."
"I can't say I'd be against holding her hand right now..."
"I mean...{w=0.38}we've had quite the day together..."
show natsuki 1bu at t11 zorder 1
mc "So...{w=0.38}this is where I live..."

if encore_festivalquestion_2 == "Natsuki":
    mc "Well, of course you'd recognize the place..."
    show natsuki 1bu
    n "Yeah...{w=0.38}I remember..."
    "Natsuki somberly scans up at my house."

if encore_festivalquestion_2 == "Yuri":
    mc "Not bad, huh?"
    show natsuki 1bu
    n "Yeah...{w=0.38}it's really nice, [player]..."
    "She somberly scans up and down my house."

mc "Is something wrong?"
n 12ba "Can you do me a favor, [player]?"
mc "Uh...{w=0.38}sure?"
show natsuki 12bb
"Natsuki hands me her manga book, her hands shaking."
n 12be "Can you hold onto this until tomorrow?"
n 12ba "Just put it in the closet when you get into the club..."
mc "Why?"
play music t9

if natsuki_continued_hug == True:
    jump n_d_9

if natsuki_continued_hug == False:
    jump n_d_10

if natsuki_hug == True:
    jump n_d_9

if natsuki_hug == False:
    jump n_d_10


label n_d_9:

show natsuki 42ba
n "You know why!"
"Suddenly, it clicks for me."
mc "It's because of your dad, isn't it?"
n 42bd "Yes!"
"She barely squeaks out."
n 42bb "He'd kick me out of the house and disown me if he ever found me reading that..."
"My anxiety that I've supressed earlier about Natsuki's home life suddenly bursts out into the open."
mc "Natsuki...{w=0.38}I know earlier you said it wasn't that bad but..."
mc "Is it really that bad?"
show natsuki 42bf
"Natsuki meerly nods her head as tears start rolling down her face."
n 42bg "It hasn't been bad recently..."
n 42bb "He's been in a good mood lately..."
n 42bi "But I'm scared that one little thing will set him off like always!"
n 42bh "And he'll take it out on me one way or another..."
"I drop the manga as I take Natsuki into my arms."
scene black
with close_eyes
mc "Natsuki..."
mc "I'm so sorry..."
mc "You need to get away from him!"
n "Fat chance I can!"
"She abruptly pulls away from me."
scene bg residential_day
with open_eyes
show natsuki 42bh at t11 zorder 1
n "If I leave, he'll find me."
n 42bd "He can and will do that."
n 42ba "And when he catches me, it'll be the end of me..."
mc "What does he do you do?!?"
mc "Does he...{w=0.38}physically hurt you?"
n 42bg "He hasn't in a while thankfully..."
n 42be "But it's not like I'm spared from his harsh insults..."
n 42bd "And anytime I fight back, it gets worse..."
n 42be "I guess because I've put up with his crap lately, he's found me tolerable..."
mc "I guess that's all you can do for now, until you can get away..."
n 42ba "Believe me, first chance I get, I'm getting away from him!"
mc "Well, look..."
mc "If anything ever happens, just come to me okay?"
mc "I mean, I guess walking from school to here helps make this all a little more familar to you, right?"
show natsuki 4bt
"Natsuki lets out a little chuckle."
n "Yeah...{w=0.38}it does..."
n 4bm "I'm sorry for not telling you the full truth earlier..."
n 4bq "I didn't want you to worry about me..."
show natsuki 1bm
mc "I've been worried!"
mc "Ever since you told me, it's been nagging in the back of my mind..."
mc "Look if something ever happened to you...{w=0.38}I don't know what I'd do!"
mc "Nothing would be the same without you, Natsuki..."
show natsuki 5bu
"Natsuki stares off with a mixed expression of guilt and embarrassment."
n 5bm "Well...{w=0.38}it means a lot that you really care about me, [player]..."
n 5bc "I'll come to you if I ever need you, okay?"
mc "Okay..."
show natsuki 5bu
"We stand in silence for a few moments before Natsuki breaks it."
show natsuki 5bm
n "Well, I gotta head home..."
n 5bl "All the emotions aside...{w=0.38}I had fun today, [player]!"
n 5bt "You really did make this a better day than I thought it was gonna be..."
mc "I'm glad I helped..."
n 5ba "You did."
n 5bl "Well, I'll see you tomorrow!"
mc "You too!"
show natsuki at thide
hide natsuki
"We embrace each other one last time before Natsuki walks off back in the direction of the school."
"I smile to myself as I watch her walk off into the horizon, knowing that I helped make her day..."
"I pick up the bag containing her manga and enter my house."
stop music fadeout 2.0
jump day3_night

label n_d_10:

n 42ba "Look...{w=0.38}I debated telling you this earlier, but I think I'll just say it now..."
mc "Well, what is it?"
n 42bb "There's a reason I keep my manga in the clubroom and not at home..."
n 42ba "There's a reason I'm so defensive about everything..."
n "To put it plainly...{w=0.38}I don't exactly have the best home situation..."
n 42bc "I never really did..."
mc "What do you mean by that?"
n 42ba "I live with my dad..."
n 42bb "And he's not exactly the most supportive parent out there..."
n 42bc "He doesn't let me do anything without his say so, and never cares to help me with anything!"
n 42ba "If I ever want something for myself, it's like pulling teeth."
n 42bd "Needless to say, we fight...{w=0.38}a lot..."
n 5bn "It took me months to save up the money I showed you..."
n 5bu "And it was a bigger pain to try to earn it..."
n 5bm "It's not like we're tight on money...{w=0.38}we're pretty well off..."
n 5bx "It's just that my dad's a selfish jerk who keeps all our money to himself and spends it on stuff he wants!"
n 5bn "He doesn't care about me..."
show natsuki 5bm
"I stand there completetly stunned at Natsuki's revleations."

if encore_sayoriquestion_1 == True:
    "I never knew Natsuki dealt with something like that on a daily basis..."
    "It would explain why she's rough around the edges..."


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        "She mentioned something before about not having the greatest relationship with her dad, but..."
        "I didn't think it was that bad..."

    if encore_festivalquestion_2 == "Yuri":
        "I never knew Natsuki dealt with something like that on a daily basis..."
        "It would explain why she's rough around the edges..."

"Yet, there's something nagging at the back of my mind here..."
"Just how bad is it really for her?"
mc "When you guys say you fight a lot...{w=0.38}what does he exactly do..."
show natsuki 42bf
"Tears start to stream down Natsuki's face."
"My heart drops into my stomach as my fists tighten in anger."
"What did he do to her?!?"
n 42bg "He insults me in every way imaginable..."
n 42bh "He's...{w=0.38}hit me before too..."
mc "Has he done it recently?"
n 42bg "He hasn't in a while thankfully..."
n 42be "But it's not like I'm spared from his harsh insults..."
n 42bd "And anytime I fight back, it gets worse..."
mc "Jesus..."
"I drop the manga as I take Natsuki into my arms."
scene black
with close_eyes
mc "Natsuki..."
mc "I'm so sorry..."
mc "You need to get away from him!"
n "Fat chance I can!"
"She abruptly pulls away from me."
scene bg residential_day
with open_eyes
show natsuki 42bh at t11 zorder 1
n "If I leave, he'll find me."
n 42bd "He can and will do that."
n 42ba "And when he catches me, it'll be the end of me..."
n 42bb "I have to put up with him...{w=0.38}for now..."
mc "Can you really do that though?"
n 5bm "I've done it for this long..."
n 5bs "I just need to do it for two more years, then I'm off to college and I'll never have to see his face again!"
mc "Well if something happens in the mean time, I'd take you in..."
mc "I don't want you to be in danger like this, Natsuki!"
mc "If something happened to you...{w=0.38}I don't know what I'd do..."
n 5bm "Well...{w=0.38}it means a lot that you really care about me, [player]..."
n 5bt "Not too many people would even offer to do something like that for me..."
n 5bc "I'll come to you if I ever need you, okay?"
mc "Okay..."
show natsuki 5bu
"We stand in silence for a few moments before Natsuki breaks it."
show natsuki 5bm
n "Well, I gotta head home..."
n 5bl "All the emotions aside...{w=0.38}I had fun today, [player]!"
n 5bt "You really did make this a better day than I thought it was gonna be..."
mc "I'm glad I helped..."
n 5ba "You did."
n 5bl "Well, I'll see you tomorrow!"
mc "You too!"
show natsuki at thide
hide natsuki
"We embrace each other one last time before Natsuki walks off back in the direction of the school."
"I smile to myself as I watch her walk off into the horizon, knowing that I helped her today in some way..."
"I pick up the bag containing her manga and enter my house."
stop music fadeout 2.0
jump day3_night

label n_makeup:

"I should work things out with Natsuki."
"I start texting back."
mc "Yeah, if you want you can come over to my place."
"Natsuki quickly replies back."
n "Alright, I'm going there now. I'll be there in a few minutes."

if encore_festivalquestion_2 == "Natsuki":
    pass

if encore_festivalquestion_2 == "Yuri":
    "After I text Natsuki my address, I put my phone down and stare back at my celling."

"Man...{w=0.38}what am I even going to say to her..."
"This day has been a complete catastrophe..."
"I don't even know what I'm going to say to Natsuki, let alone know what she's going to say to me..."
"Maybe she just wants to apologize for what she said earlier..."
"I mean, I haven't known her to be a nasty person, but today, all my expectations went out the window."
"I can't believe anyone would've said that to someone as kind as Sayori..."
"It's enough to make my blood boil..."
"..."
"*sighs*"
"Maybe cleaning up the living room for Natsuki's arrival would be a better use of my time..."
"I can get angry at her later..."
"I get off of my bed and head downstairs to start cleaning up the living room."
scene bg living_room
with wipeleft
play sound doorbell
"Just as I about finish cleaning the living room, I hear the doorbell ring."
mc "Coming, coming!"
"I take a deep breath before walking over and opening the door."
scene bg house
with wipeleft
show natsuski 1n at t11 zorder 1
"As expected, I find Natsuki waiting on my porch."
"She looks up at me through a guilty and pained expression."
"I simply sigh and wordlessly invite her in."
show natsuki at thide
hide natsuki
scene bg living_room
with wipeleft
show natsuki 5u at t11 zorder 1
"After closing the door behind us, I lead Natsuki to the living room. We both take our seats on the couch, unable to make consistent eye contact with one another."
"I bow my head as I try to figure out something to break the tension."
"I'm not even sure where to begin..."
show natsuki 5n
"There's absolutely no excuse for what she said."
"Even if she doesn't know about Sayori's depression, it's just one of the things you don't just say to people."
"But, I think at least owe Natsuki a chance to explain herself..."
show natsuki 5o
"We wait for several minutes in painfully awkward silence before she speaks up."
n 5q "I messed up..."
show natsuki 5u
mc "Clearly, you did."
n 1m "I know you're angry with me..."
n 1q "You have every right to be..."
n 1m "And I'm sure she's pissed at me too..."
n 1q "Hell, I'd completely understand if you guys never want to talk to me again..."
n 1m "Just everything about this day has just sucked..."
show natsuki 1n
mc "Well, you're not wrong there..."
show natsuki 12b
mc "But how could you even say that to Sayori?"
mc "Look, in the time I've known you, I've gotten to understand that you're a passionate and direct person..."
mc "And there's nothing inherently wrong with that. I like people who're up-front..."
mc "I know you and Yuri can get a little heated, but this goes beyond anything I've ever seen from you..."
mc "So I guess I just want to know why acted out..."
play music t9 fadein 1.0
show natsuki 12c
"Natsuki lets out a shaky sigh."
show natsuki 12a
n "I let my emotions get the better of me again."
n 12b "After I tried to calm down Yuri, she clearly wasn't having it, and so we got into a big fight over it."
n 12d "It got hurtful for us pretty quick..."
n 12e "We said a bunch of things to each other that I'm not going to ever repeat..."
n 12d "And I guess along the way, something inside me snapped."
n 12f "I was doing being talked down to."
n 12g "I was done being pushed around."
n 12f "I dealt with it enough at home, and I'm not going to suffer through it school too."
n 12h "So I lashed out at everyone."
n 12f "I had so much pent-up anger over my life that I just exploded."
n 12i "I really, really, didn't mean to hurt anyone."
n "I know I can't take back what I said, but I just wanted to let you know just how sorry I am for everything..."
n 12h "Nothing can explain the immense pain and guilt I feel right now..."

if y_love == True:
    n "And now that you and Yuri are a thing...{w=0.38}it just hurts..."
    n 12i "After everything we've been through...{w=0.38}it hurts to know that I wasn't good enough for you..."
    n 12f "And how I acted earlier only proves that..."
    n "I'm sorry..."
    "Natsuki starts sobbing as I sit frozen in shock."
    "I know Natsuki's had it bad outside of school..."
    "And while there's certainly no way she can undo the hurt she's caused Sayori, I'm glad to at least to hear from her that she knows she's in the wrong..."
    "But, I have to come to terms that I'm a pretty big reason she blew up in the first place..."
    "I helped make her lash out..."

if y_love == False:
    n "I know you didn't mean to hurt Yuri..."
    n 12i "In all honesty, as much as we fight, I do want to be her friend..."
    n 12f "But, I understand if everyone hates me..."
    n "I just piss off everyone that's close to me..."
    "Natsuki starts sobbing as I sit frozen in shock."
    "I know Natsuki's had it bad outside of school..."
    "And while there's certainly no way she can undo the hurt she's caused Sayori, I'm glad to at least to hear from her that she knows she's in the wrong..."


"I hand Natsuki my tissue box. She gently plucks a tissue from the box and uses it to wipe her tears away."
n 12b "T-{w=0.38}thanks, [player]..."
mc "Yeah...{w=0.38}no problem..."
"We sit for the next few moments in silence."

if y_love == True:
    jump n_talk1

if y_love == False:
    jump n_talk2

label n_talk1:

"I wait for Natsuki to collect herself before I say anything."
show natsuki 1n
mc "I think I owe you an apology as well, Natsuki..."
mc "I messed up too, and I see now that I'm a pretty big reason this all happened."
mc "So, I shouldn't be as mad as I should at you."
show natsuki 5n
mc "This really is all my fault..."
mc "I led you on and I hurt you..."
n 5m "You did."


if encore_festivalquestion_2 == "Natsuki":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "I thought that after everything we've been through, that you might've liked me more than just as friends..."
                n 1m "Even though we haven't been talking for very long, I thought I was able to tell that you really weren't like most boys..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 12b "But, maybe I was wrong again..."
                jump n_converge1


    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I was wondering what would be next for us after the festival..."
                n 1m "Ever since you joined, I've had a lot of fun spending time around you."
                n 2t "Whether it was reading manga, or doing stuff at the festival..."
                n 2q "It just felt so right being around you..."
                n 2s "I did worry for a time if you were going to come back to me..."
                n 2m "But, you did!"
                n 5q "The more I got to know you, the more I felt like you actually cared about me..."
                m 5m "I thought you weren't doing it for show, but..."
                n 12b "Maybe I was wrong again..."
                jump n_converge1


    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "After we spent all that time together at the festival, I was wondering what would be next for us..."
                n 1m "I really enjoyed spending time around you, [player]..."
                n 2t "You always went out of your way to make sure I was having the best day as possible..."
                n 5q "Nobody has ever really done that for me before..."
                n 5s "But, when I saw you with [hangout2] the other day, I started to have dobuts about where you wanted to take our relationship..."
                n 5m "And when you came to see me yesterday, my worries went away for a little while..."
                n 12b "Now I see that I was right to be suspicious of you..."
                jump n_converge1



    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 != "Natsuki":
                n 5q "Ever since we started talking, I always wondered what you were trying to get out of me."
                n 1m "I didn't want to be pushed around or taken advantage of..."
                n "I was used to it..."
                n 2t "But, for a time, you proved me wrong..."
                n "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5s "But, when you went off with [hangout3] the other day, I started to get suspicious of what you were up to."
                n "In my experience, when people stop talking to me all of a sudden, it's either because I messed up or they lost interest in me..."
                n 12b "I see now that it's both..."
                jump n_converge1




    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "After we spent all that time together, I started to wonder where our relationship was going to go next..."
                n 1m "I really enjoyed spending time with you..."
                n 1n "And I wanted more..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5n "But this week, you practically ignored me until yesterday!"
                n 5q "I wasn't sure what your reason was, but I wanted to try to get back to where we were..."


                if natsuki_hangout == True:
                    n 5l "And I'm really glad you wanted to spend more time with me after school..."
                    n 5t "I really had a great time picking up Parfait Girls with you..."
                    n 5s "And for a while, I hoped that we were on the right track to being more than just friends..."



                else:
                    pass


                n 12b "But now, it seems like it's too late..."
                jump n_converge1




if encore_festivalquestion_2 == "Yuri":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "I thought that after everything we've been through, that you might've liked me more than just as friends..."
                n 1m "Even though we haven't been talking for very long, I thought I was able to tell that you really weren't like most boys..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 12b "But, maybe I was wrong again..."
                jump n_converge1


    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "And I was so happy when you finally came over to me and started talking on Tuesday..."
                n 5q "Once we started reading together, I started feeling so much more comfortable around you..."
                n 5n "I didn't know if that was just going to be a one time thing or something...."
                n 2m "But, you came back to me yesterday too!"
                n 5q "Even though we've only been talking for two days now, I really thought you cared about me..."
                m 5m "I thought you weren't doing it for show, but..."
                n 12b "Maybe I was wrong again..."
                jump n_converge1


    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "And I was so happy when you finally came over to me and started talking on Monday..."
                n 5q "Even if we didn't get to read together like we wanted to, I appreciated the gesture, and I figured maybe we'd get the chance to hangout again..."
                n 5s "But, when I saw you with [hangout2] the other day, I started to have dobuts..."
                n 5m "But then you came back to me..."
                n 12b "Now I'm just so confused and hurt..."
                jump n_converge1


    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 != "Natsuki":
                n 5q "Ever since we started talking, I always wondered what you were trying to get out of me."
                n 1m "I didn't want to be pushed around or taken advantage of..."
                n "I was used to it..."
                n 2t "But, for a time, you proved me wrong..."
                n "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5s "But, when you went off with [hangout3] the other day, I started to get suspicious of what you were up to."
                n "In my experience, when people stop talking to me all of a sudden, it's either because I messed up or they lost interest in me..."
                n 12b "I see now that it's both..."
                jump n_converge1


    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "I was actually kind of glad to see you when you finally came over to me and started talking on yesterday..."
                n 5t "Surprisingly, you weren't too bad..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and listened to what I was going through..."

                if natsuki_hangout == True:
                    n 5l "And I'm really glad you wanted to spend more time with me after school..."
                    n 5t "I really had a great time picking up Parfait Girls with you..."
                    n 5s "And for a while, I hoped that we were on the right track to being friends..."
                    jump n_converge1


                else:
                    pass


                n 12b "At least, that's what I thought..."
                jump n_converge1



label n_converge1:

"I bow my head in guilt as Natsuki finishes her speech."
"It's hard to come to terms with how much my mistake hurt her..."
"I never meant to drive her or anyone to this point..."
"But, we're both in the wrong, and we should fix things now before it gets worse..."
"I finally muster up the willpower to speak up again."
show natsuki 12a
mc "I'm sorry, Natsuki..."
show natsuki 1n
mc "It was never my intention to hurt you or anyone else..."
mc "Truthfully, my emotions are all over the place right now too."
mc "I know it's not an excuse for what I did to you, but I'm in just as much turmoil over this as you are..."
n 1m "Are you and Yuri...{w=0.38}together now?"
show natsuki 1n
mc "I don't know..."
mc "I didn't really expect everything to hit the fan at once..."
mc "So, right now I just want to fix make sure that there's no more misunderstandings between us."
n 1q "I get what you mean..."
n 1m "I'll talk to Sayori tomorrow when I get the chance..."
n 1n "How is she?"
mc "I haven't had the chance to check up on her yet, but I'll text her later."
n 1q "Okay..."
n 1u "Well, I'll try to forgive you for what happened earlier. I just can't deal with it right this second..."
mc "I understand."
stop music fadeout 3.0
"We sit for the next few minutes in silence before Natsuki speaks up again."
n 1m "Do you think the club's ever going to be the same?"
show natsuki 1n
mc "I don't know..."
mc "Hopefully, we can all put aside our differences in time for Monday at least, but after that, who knows."
n 1m "I don't want the club to disband, [player]!"
n 1n "It's really the only place I can call home!"
mc "I know..."
mc "I'd hate to see the club break apart too..."
mc "I have no idea what's going to happen with Monika and Yuri. There's no telling if there'll even be a meeting tomorrow."
n 1m "Sayori would try to come, wouldn't she?"
show natsuki 1n
mc "Knowing her, probably. She's not one to hold onto grudges."
mc "But, hopefully we can all apologize to each other go back to being friends..."
n 1q "Yeah..."
n 1m "Well, I'm glad you let me come over to hear me out..."
show natsuki 1n
mc "I suppose it's the least we could do."
mc "I trust that you'll stay to your word and work things out with Sayori at least..."
n 1t "Well, I think I owe everyone an apology at this point..."
mc "I do too..."
"We both let out an awkward chuckle before the room returns to silence."
show natsuki 1u
"At least Natsuki and I smoothed things over for the most part."
"Let's just hope it goes just as well for tomorrow..."
n 1m "So, I guess I'll see you tomorrow at the club then?"
mc "I'll be there."
mc "Just let me know if you see Monika or Yuri around."
n 1m "I will."
n 5m "And let me know how Sayori is doing..."
show natsuki 5n
mc "I'll be sure to."
n 1q "Well, I'll get going now..."
n 1m "If I stay any longer, I'll miss the bus."
show natsuki 1n
mc "It's alright, thank you for everything, Natsuki."
mc "I just hope in the next few days we can get back to being friends again..."
n 1m "Me too."
n 1t "Later, [player]!"
mc "See you tomorrow!"
show natsuki at thide
hide natsuki
"I lead Natsuki out the door and gently close it behind her."
"I watch out the window as Natsuki walks off to the horizon in the direction of the nearest bus stop."
mc "That wasn't too bad..."
"I mumble to myself."
"I'm still a little surprised Natsuki went out of her way to directly apologize to me..."
"Even though she was awful during that fight, I'm glad that she recognized her mistakes."
"It's going to take time for Natsuki and I to move past what happened, but maybe we can get back to where we were soon..."
"I just hope everything goes smoothly tomorrow..."
jump day4_night




label n_talk2:

"I sit there frozen in shock as I attempt to process the situation."
"I've never seen Natsuki come so clean about her mistakes..."
"Maybe I shouldn't be so mad at her..."
"I wait for Natsuki to collect herself before I say anything."
show natsuki 1n
mc "Well, I'm glad that you've come to recognize what you said back there was wrong..."
mc "But, I'm a pretty big reason for what happened as well, so I'm really sorry that all had to happen..."
mc "So, I shouldn't be as mad as I should at you."
show natsuki 5n
mc "This really is all my fault..."
mc "I led on Yuri and hurt her..."
mc "And who knows who else I've hurt in the process..."
mc "I'm just so confused about everything right now..."
n 5m "I know what you mean..."



if encore_festivalquestion_2 == "Natsuki":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "You know, after everything we've been through, I thought that you might've liked me more than just as friends..."
                n 1m "Even though we haven't been talking for very long, I thought I was able to tell that you really weren't like most boys..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 12b "But, I messed up by showing just how awful I am..."
                jump n_converge2


    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I was wondering what would be next for us after the festival..."
                n 1m "Ever since you joined, I've had a lot of fun spending time around you."
                n 2t "Whether it was reading manga, or doing stuff at the festival..."
                n 2q "It just felt so right being around you..."
                n 2s "I did worry for a time if you were going to come back to me..."
                n 2m "But, you did!"
                n 5q "The more I got to know you, the more I felt like you actually cared about me..."
                m 5m "I knew you weren't doing it for show, but..."
                n 12b "I don't expect you to like me after this..."
                jump n_converge2


    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "After we spent all that time together at the festival, I was wondering what would be next for us..."
                n 1m "I really enjoyed spending time around you, [player]..."
                n 2t "You always went out of your way to make sure I was having the best day as possible..."
                n 5q "Nobody has ever really done that for me before..."
                n 5s "But, when I saw you with [hangout2] the other day, I started to have dobuts about where you wanted to take our relationship..."
                n 5m "And when you came to see me yesterday, my worries went away for a little while..."
                n 12b "But now I dobut you want to be with me after I showed what an awful person I am..."
                jump n_converge2



    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 != "Natsuki":
                n 5q "Ever since we started talking, I always wondered what you were trying to get out of me."
                n 1m "I didn't want to be pushed around or taken advantage of..."
                n "I was used to it..."
                n 2t "But, for a time, you proved me wrong..."
                n "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5s "But, when you went off with [hangout3] the other day, I started to get suspicious of what you were up to."
                n "In my experience, when people stop talking to me all of a sudden, it's either because I messed up or they lost interest in me..."
                n 12b "And after today, it's probably both..."
                jump n_converge2




    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "After we spent all that time together, I started to wonder where our relationship was going to go next..."
                n 1m "I really enjoyed spending time with you..."
                n 1n "And I wanted more..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5n "But this week, you practically ignored me until yesterday!"
                n 5q "I wasn't sure what your reason was, but I wanted to try to get back to where we were..."


                if natsuki_hangout == True:
                    n 5l "And I'm really glad you wanted to spend more time with me after school..."
                    n 5t "I really had a great time picking up Parfait Girls with you..."
                    n 5s "And for a while, I hoped that we were on the right track to being more than just friends..."



                else:
                    pass


                n 12b "But now, it's probably too late..."
                jump n_converge2




if encore_festivalquestion_2 == "Yuri":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "I thought that after everything we've been through, that you might've liked me more than just as friends..."
                n 1m "Even though we haven't been talking for very long, I thought I was able to tell that you really weren't like most boys..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 12b "But, I messed up by showing just how awful I am..."
                jump n_converge2


    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "And I was so happy when you finally came over to me and started talking on Tuesday..."
                n 5q "Once we started reading together, I started feeling so much more comfortable around you..."
                n 5n "I didn't know if that was just going to be a one time thing or something...."
                n 2m "But, you came back to me yesterday too!"
                n 5q "Even though we've only been talking for two days now, I really thought you cared about me..."
                m 5m "I knew you weren't doing it for show, but..."
                n 12b "I don't expect you to like me after this..."
                jump n_converge2

    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "And I was so happy when you finally came over to me and started talking on Monday..."
                n 5q "Even if we didn't get to read together like we wanted to, I appreciated the gesture, and I figured maybe we'd get the chance to hangout again..."
                n 5s "But, when I saw you with [hangout2] the other day, I started to have dobuts..."
                n 5m "But then you came back to me..."
                n 12b "And now, I dobut you want to be with me after I showed what an awful person I am..."
                jump n_converge2


    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 != "Natsuki":
                n 5q "Ever since we started talking, I always wondered what you were trying to get out of me."
                n 1m "I didn't want to be pushed around or taken advantage of..."
                n "I was used to it..."
                n 2t "But, for a time, you proved me wrong..."
                n "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and what I was going through..."
                n 5m "I thought you weren't going to try to play me because I looked like an easy girl to get or something..."
                n 5s "But, when you went off with [hangout3] the other day, I started to get suspicious of what you were up to."
                n "In my experience, when people stop talking to me all of a sudden, it's either because I messed up or they lost interest in me..."
                n 12b "And after today, it's probably both..."
                jump n_converge2


    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                n 5q "To be honest, I always wondered if I'd ever get to know you..."
                n 1m "Ever since you joined, I always had to watch you spend time with everyone else!"
                n 5q "Even though I was suspicious of you, I didn't want to scare you away or anything like that..."
                n 5m "I was actually kind of glad to see you when you finally came over to me and started talking on yesterday..."
                n 5t "Surprisingly, you weren't too bad..."
                n 2t "You actually took me seriously..."
                n "You were kind, funny..."
                n 2y "A bit of a mediocre taste in manga..."
                n 5q "But, you actually cared about how I felt and listened to what I was going through..."

                if natsuki_hangout == True:
                    n 5l "And I'm really glad you wanted to spend more time with me after school..."
                    n 5t "I really had a great time picking up Parfait Girls with you..."
                    n 5s "And for a while, I hoped that we were on the right track to being friends..."
                    jump n_converge2


                else:
                    pass


                n 12b "But now, you probably hate me..."
                jump n_converge2


label n_converge2:

"My face is flushed with embrassment as Natsuki finishes her speech."
"I never expected to have that kind of impact on Natsuki in such a short time..."
"I try fumble out some sort of answer."
show natsuki 1n
mc "Well Natsuki, I...{w=0.38}really appreciate everything you said there..."
mc "I don't hate you because of what happened earlier..."
mc "In fact, I don't hate you at all!"
mc "I'm glad you recognized what you said was wrong and that you're willing to make things right with Sayori..."
n 5q "I think I owe everyone an apology at this rate..."
mc "Well, I think I do too..."
show natsuki 1t
"We both let out an awkward chuckle before the room returns to silence."
n 1m "So, how's Sayori?"
show natsuki 1n
mc "I haven't had the chance to check up on her yet, but I'll text her later."
n 1q "Okay..."
n 1u "Well, I'll try to forgive you for what happened earlier. I just can't deal with it right this second..."
mc "I understand."
stop music fadeout 3.0
"We sit for the next few minutes in silence before Natsuki speaks up again."
n 1m "Do you think the club's ever going to be the same?"
show natsuki 1n
mc "I don't know..."
mc "Hopefully, we can all put aside our differences in time for Monday at least, but after that, who knows."
n 1m "I don't want the club to disband, [player]!"
n 1n "It's really the only place I can call home!"
mc "I know..."
mc "I'd hate to see the club break apart too..."
mc "I have no idea what's going to happen with Monika and Yuri. There's no telling if there'll even be a meeting tomorrow."
n 1m "Sayori would try to come, wouldn't she?"
show natsuki 1n
mc "Knowing her, probably. She's not one to hold onto grudges."
mc "But, hopefully we can all apologize to each other go back to being friends..."
n 1q "Yeah..."
n 1m "Well, I'm glad you let me come over to hear me out..."
show natsuki 1n
mc "I suppose it's the least we could do."
mc "I trust that you'll stay to your word and work things out with Sayori at least..."
n 1m "I will."
n 1q "And hopefully I can make things right with Monika and Yuri too..."
show natsuki 1u
mc "I'm sure we'll be able to put this behind us."
n 1q "Yeah..."
show natsuki 1u
"Natsuki nervously glances down at the floor."
"It's going to be tough to get things back to the way they were..."
"But, at least Natsuki and I smoothed things over for the most part."
"Let's just hope it goes just as well for tomorrow..."
n 1m "So, I guess I'll see you tomorrow at the club then?"
mc "I'll be there."
mc "Just let me know if you see Monika or Yuri around."
n 1m "I will."
n 5m "And let me know how Sayori is doing..."
show natsuki 5n
mc "I'll be sure to."
n 1q "Well, I'll get going now..."
n 1m "If I stay any longer, I'll miss the bus."
show natsuki 1n
mc "It's alright, thank you for everything, Natsuki."
mc "I'm gladd we worked things out..."
n 1m "Yeah, me too."
n 1t "Well, later, [player]!"
mc "See you tomorrow!"
show natsuki at thide
hide natsuki
"I lead Natsuki out the door and gently close it behind her."
"I watch out the window as Natsuki walks off to the horizon in the direction of the nearest bus stop."
mc "That wasn't too bad..."
"I mumble to myself."
"I'm still a little surprised Natsuki went out of her way to directly apologize to me..."
"Even though she was awful during that fight, I'm glad that she recognized her mistakes."
"It's going to take time for Natsuki and I to move past what happened, but I don't think it changed my feelings for her that much..."
"I guess I'll find out for sure tomorrow..."
jump day4_night




label n_nomakeup:

"I don't want to be around her right now..."
"I start texting back."
mc "We can talk about what happened another time."
mc "I want some time to myself after all this..."
"Natsuki responds after a few minutes."
n "Okay. I just wanted to say that I'm sorry for how I acted. I shouldn't have said that to Sayori and I'm sorry I acted like a total bitch. I just wanted to say that in person so you know that I mean it..."
mc "I apprecaite it."
"I put my phone down and lay back on my bed."
"Hopefully everything will have calmed down by tomorrow..."
"Heck, I still don't know if I even want to go back to the club tomorrow..."
"But, given it's the last day we'll meet before the photoshoot, it's probably best I get working on laminating the poems for Monika..."
"I'd hate to make this situation even worse..."
"I walk over to my desk, pull the poems out from one of the drawers and begin organzing them for laminating."
jump day4_night
