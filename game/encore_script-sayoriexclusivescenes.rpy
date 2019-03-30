#Day 1
label sencore_1:
    $ hangout1 = "Sayori"
    "I first go to Sayori..."
    scene bg club_day
    with wipeleft_scene

if encore_sayoriquestion_1 == True:
    play music tsayori
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
    s 1u "I...{w=0.38} I know...{w=0.38} [player]..."
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
    mc "Sayori, I don't think you're looking at this the right way at all..."
    s 1e "Eh?"
    mc "Look, I know that this is new for the both of us..."
    mc "But the way I see it: we're in this together for as long as we can."
    mc "Just knowing that I have someone to turn to whenever I feel down or need a smile on my face..."
    show sayori 1t
    mc "For me, that's all I need right now."
    mc "And we have been doing that for as long as we've known each other anyways, so I don't think that much has changed between us."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1l
    s "Y-yeah..."
    s "I guess you're right, [player]."
    s 1k "I know I shouldn't view our relationship like that..."
    $ renpy.pause(delay=0.8, hard=True)
    s 1v "But lately, I just can't stop asking myself that question..."
    show sayori 1k
    "Sayori looks away from me in an effort to compose herself again."
    "After a moment she calms down."
    mc "Hey, Sayori?"
    "Sayori curiously looks up at me."
    s 1e "Y-yeah?"
    mc "If you don't mind me asking...{w=0.38}when did you realize you had this?"
    s "Eh?"
    s "What do you mean?"
    mc "It's just that...{w=0.38}I've known you for as long as I can remember..."
    mc "I always saw you as someone who was always happy, bubbly, sometimes clumsy, but overall..."
    mc "Just a big bundle of joy and sunshine."
    mc "I never would've thought that in a million years that you would've ever been going through something like this."
    show sayori 1k
    "Sayori pauses, as if to reflect on what I just said."
    s 1v "I mean...{w=0.38} I've always had it..."
    s 1k "But, it got really bad when high school started."
    s "It’s only gotten worse, especially recently."
    s 3k "I guess with the stress of all the exams, schoolwork, drama and other things..."
    s 3l "Like my parents divorce..."
    s 1t "And just missing out on spending time with you..."
    "I feel my heart deflate as I hear this."
    "I never thought that me spending less time with Sayori over the years would have that kind of effect on her."
    "I feel so stupid!"


if encore_sayoriquestion_1 == False:
    "I feel apprehensive as I approach Sayori."
    "Given how our friendship has frayed recently, I'm not sure if she even wants me around right now..."
    "Hopefully I can make things right between us..."
    "Alright, here goes nothing!"
    mc "Hey, Sayori!"
    play music tsayori
    show sayori 2o at t11 zorder 1
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 2x
    s "Oh, hey, [player]!"
    "Sayori puts on her usual cheerful grin, but something about it just seems...{w=0.38}off..."
    mc "What's up?"
    "I slowly take a seat right next to her."
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
    mc "And if I've said or done anything lately that has you in this state of mind right now..."
    show sayori 1e
    mc "I want to let you know that I'm deeply, deeply sorry..."
    mc "I never wanted to hurt you or-"
    show sayori 2k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 2l
    play music t10 fadein 3.0
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
    "Rejecting her confession clearly didn’t help her state of mind..."
    "God, I feel so stupid!"
    mc "Sayori..."
    mc "How long have you felt like this?"
    show sayori 1v
    s "Eh?"
    s "What do you mean?"
    mc "It's just that...{w=0.38}I've known you for as long as I can remember..."
    mc "I always saw you as someone who was always happy, bubbly, sometimes clumsy, but overall..."
    mc "Just a big bundle of joy and sunshine."
    mc "I never would've thought that in a million years that you would've ever been going through something like this."
    "Sayori pauses, as if to reflect on what I just said."
    s "I mean...{w=0.38} I've always had it..."
    s 1k "But, it got really bad when high school started."
    s "It’s only gotten worse, especially recently."
    s 3k "I guess with the stress of all the exams, schoolwork, drama and other things..."
    s 3l "Like my parents divorce..."
    s 1t "And just missing out on spending time with you..."
    "I feel my heart deflate as I hear this."
    "I never thought that me spending less time with Sayori over the years would have that kind of effect on her."
    "And rejecting her confession just added more weight onto that..."



s 2t "I guess it just finally took enough of a toll on me to the point where I realized I had this."
s 1k "But my entire life...{w} I've always felt that everyone would be better off as if I didn't exist."
s "No matter how hard I'd try to give people my happiness, my time and my energy."
s "Just...{w=0.38} nothing ever felt like it was worth it and that they didn't need me to be happy."
s 1u "And If I ever opened up about how I really felt on the inside, that people would spend all their time trying to make me happy."
s "I'd just be a weight on their shoulders. They have too much to do and I don't want to add on to their stress."
s 1v "That's what I thought when we kind of drifted apart when high school started."
s "You had too much on your plate and me being around you would be too distracting for you, so I would always have to muster up the courage to even try to talk to you."
"I feel an overwhelming sense of guilt overtake me."
show sayori 1v at h11 zorder 1
mc "Sayori!"
"I hold both of her hands tightly and look into her eyes."
mc "I'm...{w=0.38} I'm so sorry...."
s 1t "You have nothing to apologize for, [player]."
mc "I do! If I'd just put you before my hobbies, if I showed you more that I cared..."
mc "Maybe things would be better..."
mc "I promise you, Sayori, I'm going to make this up to you starting right now."
"I see Sayori’s tears return as they drip onto her cheek."
s "Don't feel guilty for the way I feel, [player]."
mc "How can I not? I can't let you get worse!"
mc "I never really realized how my actions might have affected you…"
mc "So going forward, I'll try to be different..."
mc "For your sake."
s "[player]...{w=0.38}that’s the reason I didn’t want to tell you about this!"


if encore_sayoriquestion_1 == True:
        s 1w "You shouldn’t have to change yourself just to make me happy...{w=0.38}I’d be a terrible girlfriend!"

if encore_sayoriquestion_1 == False:
        s 1w "You shouldn’t have to change yourself just to make me happy...{w=0.38}I’d be a terrible friend!"

mc "No,{w=0.38} you wouldn’t be Sayori....{w=0.38}don’t say that..."
stop music fadeout 3.5
scene black
with Dissolve(1)
"Sayori hugs me tightly."
"I put my arms around her and close my eyes."
"I can feel my heart beat in sync with Sayori’s."
"I feel the warmth of her body radiate onto me."
"As emotional as we both are right now…{w=0.38} this is nice."
"We're like this for sometime before we hear some commotion come from the closet."
scene bg club_day
stop music
show sayori 1m at t11 zorder 1
n "DAMN IT, MONIKA!!!!"
play music t3
"Monika and Yuri let out a small giggle at Natsuki's apparent misfortune before going back to their respective activities."
"Sayori and I turn to each other, both shooting each other a concerned look over what just happened."
mc "I'm going to check on Natsuki."
show sayori 3t at t11 zorder 1
"Sayori wipes a tear and gives me an approving nod."
"I get up and carefully approach the closet..."
scene black
with wipeleft_scene
pause 0.8


play music t6 fadein 3.0
scene bg closet
with wipeleft_scene
if encore_festivalquestion_2 == "Natsuki":
    play music t6 fadein 3.0
    "I hear Natsuki rummaging around in the closet "
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
    n 5e "Ugh, I can't find my volume 12 of Parfait Girls! Everything's been moved around again!"
    mc "Do you want me to help you?"
    "Natsuki seems to be slightly offended at my suggestion."
    n 5f "No! I got it all under control! I don't need your help."
    n 5u "Idiot..."
    "Her voice trails off."
    mc "You sure?"
    n 4v "Yes! I'm not a kid, I can handle myself, you know!"
    "I'm reminded of the time we spent last Sunday and how she managed to carry all those cooking supplies from her house to mine."
    "Maybe she {i}can{/i} handle this by herself..."
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
    stop music
    y 3y1 "Right now?!"
    "Her voice rings with excitement."
    "Woah, where did this excitement come from, Yuri?"
    mc "Uh...{w=0.38} I don't know if we have the time for right now but maybe tomorrow we-"
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
    show monika at thide
    hide monika
    show yuri 4b at t11 zorder 1
    "As I’m getting my poem I curiously look off in Yuri’s direction, who is avoiding making eye contact with anyone."
    "I guess it takes a lot for Yuri to talk to someone, she really isn’t one for social interactions."
    "She must have really wanted to talk to me considering we really haven’t gotten the chance to really talk with each other in a meaningful way."
    "Oh well, I’m sure we’ll get the chance sooner or later."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    jump poem_scene1

if encore_festivalquestion_2 == "Yuri":
    play music t6 fadein 3.0
    "I hear Natsuki rummaging around in the closet "
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
    n 5e "Ugh, I can't find my volume 12 of Parfait Girls! Everything's been moved around again!"
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
    scene bg club_day
    with wipeleft_scene
    "As I head back towards the front of the room, I can hear Natsuki's exasperated sighs, followed by more of her yelling."
    n "Baka!"
    "What? I'll never get around to understanding Natsuki's weird logic..."
    "While walking out from the closet I'm abruptly stopped by Yuri."
    show yuri 3y5 at t11 zorder 1
    "She seems unusually excited to talk to me, as if she’s been waiting for this chance."
    "It’s very different from how she is normally..."
    y "Hey, [player]!"
    mc "Oh! Hey, Yuri!"
    show yuri u114221
    y "How have you been lately?"
    mc "Oh, I've doing alright, what about you?"
    y 3b "I'm doing great!"
    y 2b "I just got done finishing this chapter in Portrait of Markov and I was hoping that we could..."


if encore_sayoriquestion_1 == True:
    y 4c "Maybe read it together sometime...."
    "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
    "I did remember her mentioning how much she loved reading that book..."
    "Well, it wouldn't hurt to read it with her..."


if encore_sayoriquestion_1 == False:
    y 4c "Pick up where we left off..."
    "Her confidence falls apart. She's no longer meeting my eyes as her face heats up with embarrassment."
    "I didn't realize how much reading with Yuri meant to her..."
    "Well, I should promise to read with her again at some point..."


    mc "Yeah, sure! I'd love to do some reading with you!"
    stop music
    y 3y1 "Right now?!?"
    "Her voice rings with excitement."
    "Woah, where did this excitement come from, Yuri?"
    mc "Well...{w=0.38} I don't think now is the best time. Maybe tomorrow we could-"
    y 1y4 "But you're not doing anything right now, are you?"
    "Well, I suppose she's right there..."
    "But I must admit it's a surprise to see her being this forward."
    "And, I really feel like I should get back to Sayori..."
    "My thoughts are quickly interrupted by Monika calling the group."
    show yuri at t22
    show monika u222111 at l21
    m "Ok everyone, poem time!"
    show monika u111131
    show yuri 1y7
    "Yuri quickly gives Monika an agitated look but swiftly heads back to her desk to retrieve her poem, and everyone follows."
    show monika at thide
    hide monika
    show yuri 4b at t11 zorder 1
    "As I’m getting my poem I curiously look off in Yuri’s direction, who is avoiding making eye contact with anyone."
    "I guess it takes a lot for Yuri to talk to someone, she really isn’t one for social interactions."
    "She must have really wanted to talk to me considering we really haven’t gotten the chance to recently."
    "Oh well, I’m sure we’ll get the chance sooner or later."
    show yuri at thide
    hide yuri
    with wipeleft_scene
    jump poem_scene2

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori":
            jump poem_scene3

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump poem_scene4



label sencore_1b:
    play music e4
    "During the walk home, I see Sayori catching glances at me every few minutes or so."
    show sayori 1k at t11 zorder 1
    "I guess she wants to tell me something..."
    "Since we're almost home, I'd figure I'd better ask her now."
    mc "Sayori?"
    show sayori 4m at h11 zorder 1
    s "H-huh? What is it, [player]?"
    mc "You have something on your mind?"
    s 3l "Well...{w=0.38} I was just wondering if you wanted to hangout today?"
    s "If you're free..."
    mc "Yeah! I'd love to spend more time with you!"
    s 4r "Yaaay~"
    "She beams, full of excitement and joy."
    "That's the Sayori I grew up with...{w=0.38} It's definitely a relief to see her in better spirits considering how she was earlier..."

    if hangout1 == "Sayori":
        "Maybe me being around her had something to do with her mood?"
        "Well, whatever it is, I'm just glad to see she's doing better!"

    if hangout1 == "Natsuki":
        "But, maybe I should've spent more time around her today..."
        "Well, as long as Sayori's happy, then it's a good thing for the both of us!"

    if hangout1 == "Yuri":
        "But, maybe I should've spent more time around her today..."
        "Well, as long as Sayori's happy, then it's a good thing for the both of us!"

    if hangout1 == "Monika":
        "But, maybe I should've spent more time around her today..."
        "Well, as long as Sayori's happy, then it's a good thing for the both of us!"


    "I smile to myself as I take Sayori's hand and continue the rest of the way in relative silence."
    show sayori at thide
    hide sayori
    with wipeleft_scene
    "After a few minutes, we arrive at our houses."
    show sayori 3x at t11 zorder 1
    s 3x "I’ll meet you over at your house, [player]. I need to make a quick stop at my place."
    mc "Alright, I'll see you in a bit!"
    show sayori 1y
    "We slowly embrace each other, but we quickly let go of each other as Sayori enters her house and I walk further down the street back to mine."
    stop music fadeout 2.0
    scene bg living_room
    with wipeleft_scene
    play music t6 fadein 2.0
    "After dropping off all my school stuff and changing out of my uniform, I head downstairs to wait for Sayori."
    "Not long after I sit down, I hear a knock on my door."
    mc "Come in!"
    show sayori 1ba at t11 zorder 1
    "Sayori enters my house and goes to meet me in my livingroom."
    "Seeing her again in my house reminds me of all the times she'd come over to hangout with me after school when we were younger."
    "Though, I'm just glad to be spending more time with her!"
    s 2bx "Hey, [player]!"
    mc "Hey, Sayori!"
    "I motion for her to join me on the couch."
    show sayori 1ba at s11 zorder 1
    "As she joins me, we grin at eachother, getting lost in each other's eyes."
    show sayori 1bd
    "That alone is enough to fill me with a craving to hold her in my arms."
    show sayori at thide
    hide sayori
    "Sayori rests her head on my shoulder. Instinctively, I wrap my arm around her."
    "The smell of cinnamon emanating from her hair is very apparent. I can't help but sniff a little."
    mc "Jeez...{w=0.38} you're a little cinnamon bun, aren't you?"
    show sayori 1by at t11 zorder 1
    "Sayori giggles and blushes at my compliment."
    s 1bs "You're so good to me, [player], you know that?"
    mc "I try. Remember what I promised?"
    s 1be "Eh?"
    mc "I promised you that I’d be by your side, that I’d care for you no matter what you’re feeling..."
    mc "And well, I guess I'm just doing what I think is right."
    show sayori 1be at s11 zorder 1
    "Sayori wraps her arms around me, burying her face into my chest."
    stop music fadeout 3.0
    show sayori 1bt
    s "You really do care about me, don't you, [player]?"
    mc "Of course I do! I'll do anything to make sure you're happy!"
    "I can feel that Sayori is trembling."
    s 1bk "Do I...{w=0.38}really deserve any of this?"
    mc "Deserve what?"
    mc "What do you mean?"
    play music t9 fadein 3.0
    s 1bu "Your affection...{w=0.38} your care for me."
    mc "Sayori, of course you do! You're the best thing that's ever happened to me!"
    mc "Just seeing your smile everyday is the spark that keeps me going through classes."
    mc "There's not a moment that I don't think of you and dream of when we can be together again."

if hangout1 == "Natsuki":
    show sayori 1bu
    s "Even when you were with Natsuki today?"
    "I'm not quite sure what Sayori's trying to get at..."
    "But, I'll ease her mind on this subject."
    mc "Even when I was with Natsuki today, I was thinking of you."
    mc "And like I said earlier, you matter the most to me right now."
    mc "Not her."

if hangout1 == "Yuri":
    show sayori 1bu
    s "Even when you were with Yuri today?"
    "I'm not quite sure what Sayori's trying to get at..."
    "But, I'll ease her mind on this subject."
    mc "Even when I was with Yuri today, I was thinking of you."
    mc "And like I said earlier, you matter the most to me right now."
    mc "Not her."


if hangout1 == "Monika":
    show sayori 1bu
    s "Even when you were with Monika today?"
    "I'm not quite sure what Sayori's trying to get at..."
    "But, I'll ease her mind on this subject."
    mc "Even when I was with Monika today, I was thinking of you."
    mc "And like I said earlier, you matter the most to me right now."
    mc "Not her."



"I feel Sayori's tears soaking into my shirt."
s 1bt "[player],{w=0.38} I...{w=0.38} I...{w=0.38} lo-"
mc "You don't need to strain yourself, Sayori...{w=0.38} I know what you mean."
"Sayori holds me tighter."
show sayori 1bv at t11 zorder 1
"After some time passes, Sayori releases her grip. I just can't help but get lost in those breathtaking sky blue eyes of hers."
show sayori 1bt
"Or her beautiful, precious smile..."
"Eventually, she brings me back to reality."
s 2bd "So...{w=0.38}got anything planned for us today?"
mc "Not really...{w=0.38} want to see what's on TV?"
s 1bq "Sounds good to me!"
show sayori at thide
hide sayori
"Turning on the TV, we spend many hours flipping through the channels watching various game shows, anime, sitcoms and whatever is passable enough to be on TV nowadays."
scene bg living_room_afternoon with dissolve_cg
show sayori 1ba at t11 zorder 1
"Eventually the sun begins to set."
s 1bd "Well, I guess that's my cue to head out."
mc "Yeah, guess so, I'll walk you back."
"The two of us head outside and back to Sayori's."
show sayori at thide
hide sayori
show bg residential_dusk with wipeleft_scene
"Walking back to Sayori's, I can't help but notice how beautiful everything looks in the sunset."
"The tinted pink sky...{w=0.38}the bright colors giving way to their darker shades..."
"I really should get out more..."
show sayori 1bq at t11 zorder 1
s "Hey, thanks for everything today!"
s 1bd "It really helped being able to spend time with you today..."
mc "Well, I'm glad I was able to help, Sayori! I'll see you tomorrow!"
s 1br "Try not to oversleep this time, [player]."
mc "I'll try my best."
"With that, Sayori and I embrace each other one last time before she heads back to her place."
show sayori at thide
hide sayori
"As I'm walking back to my house, I look back at Sayori's house one more time, smiling to myself knowing that I probably helped make her day."
jump day1_bedroom

##########################################
#Day 2
##########################################


label sencore_2:
    $ hangout2 = "Sayori"
    play music t4 fadein 2.0
    "I decided to see how Sayori was doing."
    scene bg club_day with wipeleft_scene
    mc "Hey, Sayori!"

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
            show sayori 1a at t11 zorder 1
            s "Oh, hey [player]!"
            show sayori 1d at t11 zorder 1
            "Sayori smiles as I take a seat next to her."
            show sayori 1c
            s "So, what we're you asking Monika about?"
            mc "Oh, I just wanted to see if I could get a little peek at what her announcement is going to be."
            show sayori 1g
            s "[player]..."
            s 1h "She's going to tell all of us, you know!"
            s "It's not nice to be nosy..."
            mc "Haha...{w=0.38}I know, I know..."
            show sayori 1q
            s "That's so like you though!"
            "I let out a small chuckle."
            mc "I guess some things never change, do they?"
            show sayori 1y
            s "Yeah...{w=0.38}I guess not..."
            "Sayori looks off to the front of the room."
            stop music fadeout 3.0
            mc "So...{w=0.38}how have things been with you today?"
            s 1l "I guess things have been alright..."
            s 1k "Though, I don't know if things have really changed or not..."
            "Sayori's voice trails off."
            s "I just still...{w=0.38}feel the same..."
            "I gently take Sayori's hand."
            mc "Sayori, look at me."
            show sayori 1u
            "Sayori looks at me as tears well within her eyes."
            mc "What's wrong?"
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1k
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1v
            play music t9 fadein 3.0
            s "I...{w=0.38}I don't know, [player]..."
            mc "What do you mean?"
            show sayori 1l
            "Sayori nervously swallows."
            show sayori 1k
            s "I thought that I'd be so much happier now that we're together..."
            s 1u "And while seeing you and spending time helps drive the rainclouds away for a little while..."
            s 1v "They just come back sooner or later, [player]..."

            if hangout1 == "Sayori":
                s "I-{w=0.38}I don't know why this keeps happening to me..."
                s 1w "Why does it keep happening, [player]!"
                "Without thinking I take Sayori into my arms."
                show sayori at thide
                hide sayori
                show cg s_cg_day2 with dissolve_cg
                "{cps=30}WIP{nw}"
                mc "Sayori listen to me..."
                mc "I don't really know how to help you through this..."
                mc "But I'll be there for you every step of the way..."
                mc "That much I can promise."
                mc "I know I can't wave away what you're feeling right now..."
                mc "But if being with you right now helps, then I hope I'm doing something right..."

            if hangout1 == "Natsuki":
                s "I felt really bad yesterday for dragging you away from Natsuki yesterday!"
                s "I didn't mean to pull you away from her or-"
                "Without thinking I take Sayori into my arms."
                show sayori at thide
                hide sayori
                show cg s_cg_day2 with dissolve_cg
                "{cps=30}WIP{nw}"
                mc "Sayori listen to me..."
                mc "I promised you that I'll be there for you every step of the way..."
                mc "Don't worry about me not getting the chance to know Natsuki better, we have the entire year in front of us..."
                s "You...{w=0.38}you wouldn't ever replace me for Natsuki, would you?"
                mc "Of course not, Sayori!"
                mc "Why would you think I'd do that?"
                s "I...{w=0.38}I don't know why..."
                s "That question's been bugging me all day..."

            if hangout1 == "Yuri":
                s "I felt really bad yesterday for dragging you away from Yuri yesterday!"
                s "I didn't mean to pull you away from her or-"
                "Without thinking I take Sayori into my arms."
                show sayori at thide
                hide sayori
                show cg s_cg_day2 with dissolve_cg
                "{cps=30}WIP{nw}"
                mc "Sayori listen to me..."
                mc "I promised you that I'll be there for you every step of the way..."
                mc "Don't worry about me not getting the chance to know Yuri better, we have the entire year in front of us..."
                s "You...{w=0.38}you wouldn't ever replace me for Yuri, would you?"
                mc "Of course not, Sayori!"
                mc "Why would you think I'd do that?"
                s "I...{w=0.38}I don't know why..."
                s "That question's been bugging me all day..."



            if hangout1 == "Monika":
                s "I really missed being able to spend time with you yesterday!"
                s "I didn't want to pull you away from Monika or-"
                "Without thinking I take Sayori into my arms."
                show sayori at thide
                hide sayori
                show cg s_cg_day2 with dissolve_cg
                "{cps=30}WIP{nw}"
                mc "Sayori listen to me..."
                mc "I promised you that I'll be there for you every step of the way..."
                mc "Don't worry about me not getting the chance to know Monika better, we have the entire year in front of us..."
                s "You...{w=0.38}you wouldn't ever replace me for Monika, would you?"
                $ style.say_dialogue = style.edited
                "{cps=10}I would...{nw}"
                $ style.say_dialogue = style.normal
                mc "Of course not, Sayori!"
                mc "Why would you think I'd do that?"
                s "I...{w=0.38}I don't know why..."
                s "That question's been bugging me all day..."
                $ style.say_dialogue = style.edited
                "Replace her..."
                $ style.say_dialogue = style.normal



            "I can feel Sayori tremble as she resists the urge to breakdown and sob..."
            s "Just...{w=0.38}promise me that you'll always be there for me, [player]."
            s "I-{w=0.38}I just need to hear that..."
            mc "I promise you, Sayori."
            mc "I'd never go back on my word to you..."
            mc "You know that..."
            "Sayori slowly pulls away from me."
            hide cg with dissolve_cg
            show sayori u116352 at t11 zorder 2
            "I put my hand on her cheek."
            mc "Hey...{w=0.38}hey...{w=0.38}it's okay."
            show sayori 1v
            mc "You're incredibly strong for putting up with this."
            mc "Don't give up."
            show sayori u111352
            "I see a mixture of emotions on Sayori's face, as if she's trying to fight back tears while trying not to blush like an idiot."
            "But...{w=0.38}she's my idiot."
            "She's my Sayori."

            if hangout1 == "Monika":
                "And..."
                $ style.say_dialogue = style.edited
                "{cps=10}You'll always be my dearest friend...{nw}"
                $ style.say_dialogue = style.normal
                "I love her..."


            if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
                "And...{w=0.38}I love her."


            "Sayori gently takes both of my hands and holds onto them firmly."
            s "T-{w=0.38}thank you...{w=0.38}[player]."
            mc "Anytime."
            s 1l "Lately my emotions have been all over the place."
            s 1k "First, I felt like I was a burden to you and everyone I knew, and now…"
            "Her voice trails off."
            mc "What is it, Sayori?"
            "Sayori take a deep breath as she holds my hands tighter."
            s 1u "Now…{w=0.38}I feel like I really shouldn’t be here."
            mc "What do you mean?"
            s 1v "I don’t know…{w=0.38}just the past few days I’ve had this feeling that I really shouldn’t be here, with you, that none of this should’ve happened."
            "I feel my heart sink into my stomach."
            "She doesn’t mean…"
            s 1l "I’m not doubting our relationship or anything…"
            s 1k "It’s just…{w=0.38}I guess you could say I feel out of place or something."
            show sayori 1e
            mc "Well, I’ll say this Sayori..."
            show sayori 1t
            mc "I’m glad you’re here with me. I wouldn’t change any of this for the world."
            mc "I’m glad that we found our feelings for each other."
            "Sayori's grip on me tightens."
            s 1k "Hey, [player]..."
            mc "Yes, Sayori?"
            s 1l "I'm going to rest for a little bit if that's okay with you..."
            s "Today's been...{w=0.38}draining...."
            mc "Alright, do you want me to leave or-"
            stop music fadeout 12.0
            show sayori at thide
            hide sayori
            play sound "sfx/fall.ogg"
            "Without warning Sayori plops her head onto my shoulder."
            "And...{w=0.38}she's out like a light..."


            if hangout1 == "Monika":
                "And...{w=0.38}she's out like a light..."
                mc "Rest-"
                $ style.say_dialogue = style.edited
                "{cps=10}In Peace{nw}"
                $ style.say_dialogue = style.normal
                mc "Sayori..."
                "I suddenly feel drowsy."

            if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
                mc "Rest easy, Sayori."
                "I mutter softly."
                "I can't help but notice how cute she looks sleeping on my shoulder."


            "Well, I might as well take this opportunity to get some shuteye myself..."
            scene black
            with close_eyes
            "Never in a million years did I think I would’ve ended up with someone like Sayori."
            "A guy like me and a girl like her?"
            "What are the odds…"
            "Speaking of finding..."
            "There's no way the others haven't noticed us."
            "I quickly crack open my eyes."
            scene bg club_day
            with open_eyes
            "I look around the room."
            show yuri 1g at t11 zorder 2
            "Yuri still seems to be into her book,{w=0.8}{nw}"
            show yuri at t32
            show monika 1c at t33 zorder 3
            "Yuri still seems to be into her book,{fast} Monika seems to be typing on the teacher's computer,{w=0.8}{nw}"
            show monika at t32
            show yuri at t31
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
            show yuri 3n at t31 zorder 2
            show monika at t32
            show natsuki at t33
            "Yuri, confused as to what's going on, turns around..."
            show yuri u125111
            "Only to see what Monika and Natsuki are staring at."
            "Thankfully, Sayori dozed off while we were like this, otherwise she'd be incredibly embarrassed."
            show monika 1h
            show natsuki 5g
            show yuri u123114
            "All three girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
            "Great..."
            "Well, it's up to me to attempt to salvage this situation."
            show monika at thide
            hide monika
            show yuri at thide
            hide yuri
            show natsuki at thide
            hide natsuki
            mc "Hey...{w=0.38}Sayori.."
            "I subtly nudge her."
            "She raises her head to look at me."
            mc "Wake up, dummy."
            show sayori 1p at t11 zorder 1
            s "Waaaah...{w=0.38}five more minutes like this, please?"
            show sayori at thide
            hide sayori
            play sound "sfx/fall.ogg"
            "Sayori puts her head back on my shoulder."
            "I just can't win today..."
            show monika 1p at t32 zorder 3
            show natsuki 5u at t33 zorder 1
            show yuri 2q at t31 zorder 2
            "Monika, Natsuki and Yuri all look off in different directions, trying to avoid making the situation even more awkward then it already is..."
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
            show monika 2p at t42 zorder 4
            show sayori 1e at t44
            show yuri 3q at t41 zorder 3
            show natsuki 3u at t43 zorder 2
            "But she quickly sees the situation we're in."
            "Immediately, Sayori's face matches her bow."
            "Oh Sayori, always putting us in these awkward situations."
            s u122322 "Oh...{w=0.38}s-{w=0.28}sorry guys! I was just..."
            show monika 1e
            "Monika shoots Sayori a warm smile."
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
                if hangout1 == "Sayori":
                    jump day2_angry_ns

            if encore_festivalquestion_2 == "Natsuki":
                if hangout1 == "Natsuki":
                    jump day2_angry_ns

            if encore_festivalquestion_2 == "Natsuki":
                if hangout1 == "Yuri":
                    jump day2_angry_ns

            if encore_festivalquestion_2 == "Natsuki":
                if hangout1 == "Monika":
                    jump day2_angry_ns


            if encore_festivalquestion_2 == "Yuri":
                if hangout1 == "Sayori":
                    jump day2_angry_ys

            if encore_festivalquestion_2 == "Yuri":
                if hangout1 == "Natsuki":
                    jump day2_angry_ys

            if encore_festivalquestion_2 == "Yuri":
                if hangout1 == "Yuri":
                    jump day2_angry_ys

            if encore_festivalquestion_2 == "Yuri":
                if hangout1 == "Monika":
                    jump day2_angry_ys




if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
            show sayori 1n at t11 zorder 1
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1e
            s "O-{w=0.38}oh! Hey, [player]..."
            show sayori 1c
            s "How're you?"
            "Sayori says that as if she wasn't expecting me."
            mc "You seem surprised."
            show sayori 1l
            s "I just didn't think that you'd get done talking with Monika so soon..."
            mc "Ah, I just wanted to ask her something."
            mc "Besides, if I heard you correctly earlier today, you said you wanted to spend more time together..."
            show sayori 1e
            mc "So, here I am..."


            if hangout1 == "Natsuki":
                s "I'm not taking you away from Natsuki or anything, right?"
                mc "No, no, not at all! She's fine."
                "Right?"
                show sayori at thide
                hide sayori
                show natsuki 1s at t11 zorder 2
                "I glance over to Natsuki who appears to organzing her manga again."
                "Ah, she’ll be fine for a few minutes…"
                show natsuki at thide
                hide natsuki


            if hangout1 == "Yuri":
                s "I'm not taking you away from Yuri or anything, right?"
                mc "No, no, not at all! She's fine."
                show sayori at thide
                hide sayori
                show yuri 1g at t11 zorder 2
                "I glance over to Yuri who appears to be deep into her book."
                "Ah, she'll be fine without me for a few minutes..."
                show yuri at thide
                hide yuri

            if hangout1 == "Monika":
                s "I'm not taking you away from Monika or anything, right?"
                mc "No, no, not at all! She's fine."
                show sayori at thide
                hide sayori
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


            show sayori 1e at t11
            mc "I came to see you, silly."
            show sayori 1y
            "Sayori nervously blushes, but quickly composes herself."
            show sayori 1c

            if hangout1 == "Sayori":
                s "So...{w=0.38}what we're you talking to Monika about?"
                "Looks like my suspicions were right..."
                "Still, I'll let Monika tell Sayori about what I said about her."

            if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
                s "So...{w=0.38}what we're you talking to Monika about?"


            mc "Oh, I just wanted to see if I could get a little peek at what her announcement is going to be."
            show sayori 1g
            s "[player]..."
            s 1h "She's going to tell all of us, you know!"
            s "It's not nice to be nosy..."
            mc "Haha...{w=0.38}I know, I know..."
            show sayori 1q
            s "That's so like you though!"
            "I let out a small chuckle."
            mc "I guess some things never change, do they?"
            show sayori 1y
            s "Yeah...{w=0.38}I guess not..."
            "Sayori looks off to the front of the room as an awkward silence forms between us."
            stop music fadeout 3.0
            mc "I just hope you've been feeling better since..."
            show sayori 1e
            mc "Well, you know..."
            show sayori 1k
            "For some reason that sounded a lot better in my head..."
            show sayori 1b
            s "I've been alright, [player]."
            show sayori 1d
            play music t10
            s "You don't need to worry about me so much."
            show sayori 1y
            s "You made your choice last Sunday..."
            mc "Do you want to talk about what happened?"
            show sayori 1i
            s "No."
            show sayori 1k
            s "Not now, at least...."
            show sayori 1f
            s "And not here."
            mc "I understand."
            mc "I just wanted to see how you've been Sayori."
            show sayori 1u
            mc "I can't help but at least worry a little about you."
            mc "You are my de-"
            show sayori 1v
            "I stop myself short as I see Sayori on the verge of tears."
            "I quickly rephrase myself."
            mc "Sayori, you're my friend."
            mc "And last Sunday didn't change how I feel about you."
            mc "I'm still going to stay true to my word and help you through this."
            mc "That's what matters the most to me right now."
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1k
            $ renpy.pause(delay=0.8, hard=True)
            s "[player], it's like I said..."
            s "I don't want you to worry so much about me..."
            show sayori 1t
            s "I deserve to live like this."
            s "I need to live this way."
            s "It's the price I have to pay for you to be happy with [encore_festivalquestion_2]..."
            "I can hardly believe what I'm hearing..."
            mc "Sayori..."
            mc "You're not looking at this the right way."
            mc "Your happiness is just as important to me as [encore_festivalquestion_2]'s or anyone else's!"
            mc "Please...{w=0.38}let me help you through this..."
            show sayori 1u
            mc "It would make me happy to see you get over this..."
            show sayori 1l
            "Sayori lets out a nervous laugh."
            s "The funny thing is [player]..."
            show sayori 1t
            s "I only feel happy when I'm around you..."

            if encore_festivalquestion_2 == "Natsuki":
                if hangout1 == "Sayori":
                    s "But, knowing that you'll never like me back in the same way I do..."
                    s "Seeing how you've had so much fun with Natsuki since you joined..."

            if encore_festivalquestion_2 == "Yuri":
                if hangout1 == "Sayori":
                    s "But, knowing that you'll never like me back in the same way I do..."
                    s "Seeing how you've had so much fun with Yuri since you joined..."

            if encore_festivalquestion_2 == "Natsuki":
                 if hangout1 == "Natsuki":
                    s "But, knowing that you'll never like me back in the same way I do..."
                    s "Especially seeing you have so much fun with Natsuki yesterday..."
                    s "And knowing how much fun you had with her last Sunday..."

            if encore_festivalquestion_2 == "Natsuki":
               if hangout1 == "Yuri":
                   s "But, knowing that you'll never like me back in the same way I do..."
                   s "Especially seeing you have so much fun with Yuri yesterday..."
                   s "And knowing how much fun you had with Natsuki last Sunday..."

            if encore_festivalquestion_2 == "Yuri":
               if hangout1 == "Yuri":
                    s "But, knowing that you'll never like me back in the same way I do..."
                    s "Especially seeing you have so much fun with Yuri yesterday..."
                    s "And knowing how much fun you had with her last Sunday..."

            if encore_festivalquestion_2 == "Yuri":
               if hangout1 == "Monika":
                   s "But, knowing that you'll never like me back in the same way I do..."
                   s "Especially seeing you have so much fun with Monika yesterday..."
                   s "And knowing how much fun you had with Yuri last Sunday..."

            if encore_festivalquestion_2 == "Natsuki":
               if hangout1 == "Monika":
                    s "But, knowing that you'll never like me back in the same way I do..."
                    s "Especially seeing you have so much fun with Monika yesterday..."
                    s "And knowing how much fun you had with Natsuki last Sunday..."


            show sayori 1u
            s "It just breaks my heart!"
            s 1v "I don't know why I keep feeling like this, [player]!"
            s 1w "I don't know anything!"
            s "I-"
            "Without thinking I take Sayori into my arms."
            show sayori at thide
            hide sayori
            show cg s_cg_day2 with dissolve_cg
            "{cps=30}WIP{nw}"
            mc "Sayori listen to me..."

            if hangout1 == "Sayori":
                mc "I don't really know how to help you through this..."
                mc "But I'll be there for you every step of the way..."
                mc "That much I can promise."


            if hangout1 == "Monika":
                mc "Me spending time with Monika isn't going to make me forget about my promise to you."
                $ style.say_dialogue = style.edited
                "{cps=10}Just you wait...{nw}"
                $ style.say_dialogue = style.normal
                mc  "I'll be there for you every step of the way..."


            if hangout1 == "Yuri":
                  mc "Me spending time with Yuri isn't going to make me forget about my promise to you."
                  mc  "I'll be there for you every step of the way..."


            if hangout1 == "Natsuki":
                mc "Me spending time with Natsuki isn't going to make me forget about my promise to you."
                mc  "I'll be there for you every step of the way..."



mc "I know I can't wave away what you're feeling right now..."
mc "But if being with you right now helps, then I hope I'm doing something right..."
"I can feel Sayori tremble as she resists the urge to breakdown and sob..."
s "Promise me that you'll always be there for me, [player]."
s "I-{w=0.38}I just need to hear that..."
mc "I promise you, Sayori."
mc "I'd never go back on my word to you..."
mc "You know that..."
"Sayori slowly pulls away from me."
hide cg with dissolve_cg
show sayori u116352 at t11 zorder 2
"I gently take Sayori's hand."
mc "Hey...{w=0.38}hey...{w=0.38}it's okay."
show sayori 1v

if hangout1 == "Monika":
    mc "You're incredibly strong for putting up with this."
    mc "Don't give up."
    $ style.say_dialogue = style.edited
    "{cps=10}She already has...{nw}"
    "{cps=10}Just give up on her...{nw}"
    $ style.say_dialogue = style.normal
    mc  "I'll be there for you every step of the way..."


if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Natsuki":
    mc "You're incredibly strong for putting up with this."
    mc "Don't give up."


show sayori u111352
"I see a mixture of emotions on Sayori's face, as if she's trying to fight back tears while trying not to blush like an idiot."
"But...{w=0.38}she's my idiot."
"She's my Sayori."
"And...{w=0.38}I just hope I'm doing the right thing..."
"Sayori gently takes both of my hands and holds onto them firmly."
s "T-{w=0.38}thank you...{w=0.38}[player]."
mc "Anytime."
s 1l "Lately my emotions have been all over the place."
s 1k "First, I felt like I was a burden to you and everyone I knew, and now…"
"Her voice trails off."
mc "What is it, Sayori?"
"Sayori take a deep breath as she holds my hands tighter."
s 1u "Now…{w=0.38}I feel like I really shouldn’t be here."
mc "What do you mean?"
s 1v "I don’t know…{w=0.38}just the past few days I’ve had this feeling that I really shouldn’t be here, that none of this should’ve happened."
"I feel my heart sink into my stomach."
"She isn't considering…"
s 1l "I’m not doubting my life or anything…"
s 1k "It’s just…{w=0.38}I guess you could say I feel out of place or something."
show sayori 1e
mc "Well, I’ll say this Sayori..."
show sayori 1t
mc "I’m glad you’re here."
mc "I’m glad that we can still be friends even after everything we've been through..."
"Sayori's grip on me tightens."
s 1k "Hey, [player]..."
mc "Yes, Sayori?"
s 1l "I'm going to rest for a little bit if that's okay with you..."
s "Today's been...{w=0.38}draining...."
mc "Alright, do you want me to leave or-"
stop music fadeout 12.0
show sayori at thide
hide sayori
play sound "sfx/fall.ogg"
"Without warning Sayori plops her head onto my shoulder."
"And...{w=0.38}she's out like a light..."
"Well, now I'm stuck."
"Not to mention, there's no way the others haven't noticed us."
"I look around the room."
show yuri 1g at t11 zorder 2
"Yuri still seems to be into her book,{w=0.8}{nw}"
show yuri at t32
show monika 1c at t33 zorder 3
"Yuri still seems to be into her book,{fast} Monika seems to be typing on the teacher's computer,{w=0.8}{nw}"
show monika at t32
show yuri at t31
show natsuki 5a at t33 zorder 1
"Yuri still seems to be into her book, Monika seems to be typing on the teacher's computer,{fast} and Natsuki is in her usual spot under the windowsill reading her manga."
"There's no way that they haven't at least looked up once and saw us like this, or overheard what we were saying, since we weren't really being that quiet to begin with."

if hangout1 == "Monika":
    "I'm worried how Monika might react if she saw me like with Sayori..."
    show monika 1q
    $ style.say_dialogue = style.edited
    "{cps=10}Let's find out...{nw}"
    $ style.say_dialogue = style.normal

if hangout1 == "Natsuki" or hangout1 == "Yuri":
    "I'm worried how [hangout1] might react if she saw me like this with Sayori..."

show monika 1j
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
show yuri 3n at t31 zorder 2
show monika at t32
show natsuki at t33
"Yuri, confused as to what's going on, turns around..."
show yuri u125111
"Only to see what Monika and Natsuki are staring at."
"Thankfully, Sayori dozed off while we were like this, otherwise she'd be incredibly embarrassed."
show monika 1h
show natsuki 5g
show yuri u123114
"All three girls are looking at us, with a bit of an irritated...{w=0.38}almost jealous...{w=0.38}expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show monika at thide
hide monika
show yuri at thide
hide yuri
show natsuki at thide
hide natsuki
mc "Hey...{w=0.38}Sayori.."
"I subtly nudge her."
"She raises her head to look at me."
mc "Wake up, dummy."
show sayori 1p at t11 zorder 1
s "Waaaah...{w=0.38}five more minutes like this, please?"
show sayori at thide
hide sayori
play sound "sfx/fall.ogg"
"Sayori puts her head back on my shoulder."
"I just can't win today..."
show monika 1p at t32 zorder 3
show natsuki 5u at t33 zorder 1
show yuri 2q at t31 zorder 2
"Monika, Natsuki and Yuri all look off in different directions, trying to avoid making the situation even more awkward then it already is..."
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
show monika 2p at t42 zorder 4
show sayori 1e at t44
show yuri 3q at t41 zorder 3
show natsuki 3u at t43 zorder 2
"But she quickly sees the situation we're in."
"Immediately, Sayori's face matches her bow."
"Oh Sayori, always putting us in these awkward situations."
s u122322 "Oh...{w=0.38}s-{w=0.28}sorry guys! I was just..."
show monika 1e
"Monika shoots Sayori a warm smile."
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
    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        jump day2_angry_ns


if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        jump day2_angry_ys




label day2_angry_ns:
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
    "I just hope she isn't jealous of me and Sayori getting so close like that."
    "Hopefully then, she won't full on put me in the hospital."
    "Oh well..."
    jump day2_meettheclubs


label day2_angry_ys:
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
    "I just hope she isn’t jealous of me and Sayori getting so close like that."
    "She isn’t the jealous type…{w=0.38}right?"
    jump day2_meettheclubs










label day2_poems:
scene bg bedroom
with wipeleft_scene
play music t6 fadein 1.0
"I drop my book bag in the middle of my room and change out of my uniform."
"I begin looking through the messy stack of papers on my desk in an attempt to find the poems I wrote."
"I just hope I didn't accidentally throw them away..."
"..."
"Come on...{w=0.38}they gotta be here somewhere!"
"..."
"..."
"..."
"A-ha! There they are!"
"I pull my poems out of my stack and start organzing them a little."
"Reading through them, I see how far I've progressed as a writer."
"My more recent poems certainly seem more developed and structured compared to the first poem I wrote."



if encore_sayoriquestion_1 == True:
    jump day2_v1

if encore_sayoriquestion_1 == False:
    jump day2_v2

label day2_v1:

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
      "I'm also reminded of the inspiration behind all these poems...{w=0.38}my dear Sayori."
      "Just thinking about her allowed me to power through this ardious task."
      "I guess I did end up writing it for her after all..."

if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        "Reading through my old poems again, I noticed the subject matter become more cutsey over time for some reason..."
        "I guess that must be Natsuki's advice at work..."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."

if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        "Looks like Yuri's advice finally paid off!"
        "Though I can't forget that Sayori was my inspiration for a lot of these..."

if hangout1 == "Sayori":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."


if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        "As I look over my poems, I see them becoming more cutsey, something that Natsuki would like..."
        "I guess Natsuki's advice actually got through to me..."
        "Granted I didn't see anything wrong with my poems to begin with, I guess her insistence on focusing on the more 'simple' side of things reasonated with me..."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."


if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        "As I look over my poems, I see them becoming more cutsey, something that Natsuki would like..."
        "I guess Natsuki's advice actually got through to me..."
        "Even though, Sayori was my inspiration for most of these poems..."
        "Granted I didn't see anything wrong with my poems to begin with, I guess her insistence on focusing on the more 'simple' side of things reasonated with me..."
        "If I ever told Natsuki this, she'd never let me hear the end of it..."


if hangout1 == "Natsuki":
    if hangout2 == "Yuri":
        "As I look over my poems, I see them becoming more cutsey, something that Natsuki would like..."
        "I guess Natsuki's advice actually got through to me..."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "Even if Natsuki may have influenced me a bit..."
        "Funny enough, as I continue looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation from more people than I realized..."



if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        "Looks like Yuri's advice finally paid off!"
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "Even if Yuri may have influenced me a bit..."
        "Looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        "Looks like Yuri's advice finally paid off!"
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "Even if Yuri may have influenced me a bit..."
        "Funny enough, as I continue looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
        "Guess I've gotten more inspirtation from more people than I realized..."


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        "Looks like Yuri's advice finally paid off!"
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "Even if Yuri may have influenced me a bit..."
        "Especially with my last poem..."

if hangout1 == "Yuri":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Monika":
    if hangout2 == "Sayori":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."

if hangout1 == "Monika":
    if hangout2 == "Natsuki":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
        "Guess I've gotten more inspirtation than I first realized..."

if hangout1 == "Monika":
    if hangout2 == "Yuri":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that Sayori was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Monika":
    if hangout2 == "Monika":
        "Guess Monika was right...{w=0.38}I am getting better!"
        "I can't help but think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Maybe I was trying to impress her the whole time..."



if poem_giver == "Natsuki":
    "I put down my poems and go to my bag to retrieve Natsuki's poems, which I put right next to mine."
    "I notice that in Natsuki’s stack of poems there’s a pink piece of paper."
    "Hmm…{w=0.38}I don’t remember Natsuki ever writing her poems down on pink paper..."
    "Maybe she accidentally gave me something…"
    jump day2_sarrive

if poem_giver == "Yuri":
    "I put down my poems and go to my bag to retrieve Yuri's poems, which I put right next to mine."
    "I notice that in Yuri's stack of poems there’s a purple piece of paper."
    "Hmm…{w=0.38}I don’t remember Yuri ever writing her poems down on purple paper..."
    "Maybe she accidentally gave me something…"
    jump day2_sarrive



label day2_v2:

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
      "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
      "I guess by spending all that time around her, I picked up on her writing habits..."
      "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Sayori liked it..."
      "I guess that was the part of me that wanted to accept her confession..."

if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
         "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
         "I guess by spending all that time around her, I picked up on her writing habits..."
         "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Sayori liked it..."

         if encore_festivalquestion_2 == "Natsuki":
             "I guess I can see why this wasn't up to Natsuki's standards..."
             "Still, she didn't really seem to mind..."

         if encore_festivalquestion_2 == "Yuri":
            "I guess I can finally see Yuri's point of needing to eventually pick a style and sticking with it..."
            "Though, a little experimentation never hurt anyone..."


if hangout1 == "Sayori":
    if hangout2 == "Yuri":
         "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
         "I guess by spending all that time around her, I picked up on her writing habits..."
         "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Sayori liked it..."

         if encore_festivalquestion_2 == "Natsuki":
             "I guess I can see why this isn't cute enough for Natsuki..."

         if encore_festivalquestion_2 == "Yuri":
             "I guess I can finally see Yuri's point of needing to eventually pick a style and sticking with it..."
             "Now that I think about it, I never really realized just how dark some of her poems were..."


if hangout1 == "Sayori":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that [encore_festivalquestion_2] was my inspiration for a lot of these..."
        "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Sayori liked it..."
        "I guess that was the part of me that wanted to accept her confession..."



if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."


        if encore_festivalquestion_2 == "Natsuki":
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Even if her writing style is rather simple, she uses it pretty effectivly to get her message across."
             "Looking back at my poems, I realize why Natsuki likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she hated me at first, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "Hopefully I can get another chance to hangout with her..."
             "Though I need to be mindful about how Sayori feels..."


        if encore_festivalquestion_2 == "Yuri":
             "I guess I can finally see Yuri's point of needing to eventually pick a style and sticking with it..."
             "Now that I think about it, I never really realized just how dark some of her poems were..."
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Looking back at my poems, I realize why Yuri likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she just preferred her books over people, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "Hopefully I can get another chance to hangout with her..."
             "Though I need to be mindful about how Sayori feels..."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."

        if encore_festivalquestion_2 == "Natsuki":
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Even if her writing style is rather simple, she uses it pretty effectivly to get her message across."
             "Looking back at my poems, I realize why Natsuki likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she hated me at first, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "I hope she was joking when she said that trip to that convention wouldn't be a date..."

        if encore_festivalquestion_2 == "Yuri":
            "I guess I can finally see Yuri's point of needing to eventually pick a style and sticking with it..."
            "Now that I think about it, I never really realized just how dark some of her poems were..."
            "Granted, I never minded if they were, it's a pretty stunning contrast between the way Natsuki and Yuri write their poems."
            "Still, I respect and appreciate Yuri as a writer just as much as Natsuki."
            "Now that I think about it, it's been a while since Yuri and I got to spend some time together..."
            "Hopefully I can hangout with her again soon..."


if hangout1 == "Natsuki":
    if hangout2 == "Yuri":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."

        if encore_festivalquestion_2 == "Natsuki":
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Even if her writing style is rather simple, she uses it pretty effectivly to get her message across."
             "Looking back at my poems, I realize why Natsuki likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she hated me at first, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "Hopefully I can hangout with her again soon..."


        if encore_festivalquestion_2 == "Yuri":
            "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Natsuki liked it..."
            "I guess I finally see Yuri's point of needing to eventually pick a style and sticking with it..."
            "Now that I think about it, I never really realized just how dark some of her poems were..."
            "Granted, I never minded if they were, it's a pretty stunning contrast between the way Natsuki and Yuri write their poems."
            "Still, I respect and appreciate Yuri as a writer just as much as Natsuki."
            "Now that I think about it, it's been a while since Yuri and I got to spend some time together..."
            "I still can't believe how close we were today!"
            "Maybe in a few days I can make something happen between us..."



if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that [encore_festivalquestion_2] was my inspiration for a lot of these..."


        if encore_festivalquestion_2 == "Natsuki":
            "And looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
            "Guess I've gotten more inspirtation than I first realized..."

        if encore_festivalquestion_2 == "Yuri":
            "Looking over my later poems, I see why Yuri liked some of my earlier ones so much..."
            "They were fairly descriptive and the subject matter was rather dark compared to some of my more recent ones."
            "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."
        "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Sayori liked it..."

        if encore_festivalquestion_2 == "Natsuki":
            "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Yuri liked it..."
            "I guess I finally see why Natsuki wasn't crazy over my last poem..."
            "Now that I think about it, I never really realized just how lighthearted some of her poems were..."
            "Granted, I never minded if they were, it's a pretty stunning contrast between the way Natsuki and Yuri write their poems."
            "Still, I respect and appreciate Yuri as a writer just as much as Natsuki."
            "Now that I think about it, it's been a while since I got spend some time around Natsuki..."
            "Hopefully I can get another chance to hangout with her..."
            "Though I need to be mindful about how Sayori feels..."


        if encore_festivalquestion_2 == "Yuri":
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Even if her writing style is rather complex, she uses it pretty effectivly to get her message across."
             "Looking back at my poems, I realize why Yuri likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she just preferred her books over people, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "Hopefully I can get another chance to hangout with her..."
             "Though I need to be mindful about how Sayori feels..."




if hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."

        if encore_festivalquestion_2 == "Natsuki":
            "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Yuri liked it..."
            "I guess I finally see why Natsuki wasn't crazy over my last poem..."
            "Now that I think about it, I never really realized just how lighthearted some of her poems were..."
            "Granted, I never minded if they were, it's a pretty stunning contrast between the way Natsuki and Yuri write their poems."
            "Still, I respect and appreciate Yuri as a writer just as much as Natsuki."
            "Even though I thought Natsuki hated me at first, it's quite remarkable how much closer we've gotten over these last two weeks..."
            "I hope she was joking when she said that trip to that convention wouldn't be a date..."


        if encore_festivalquestion_2 == "Yuri":
            "Despite her insecurities about her writing, I always thought her poems were fun to read!"
            "Even if her writing style is rather complex, she uses it pretty effectivly to get her message across."
            "Looking back at my poems, I realize why Yuri likes them so much..."
            "She finally found someone that she can relate to..."
            "Even though I thought she just preferred her books over people, it's quite remarkable how much closer we've gotten over these last two weeks..."
            "I just hope I can get another chance to hangout with her..."



if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        "As I look through my poems, I come to realize just how much [encore_festivalquestion_2] has influenced my writing."
        "I guess by spending all that time around her, I picked up on her writing habits..."

        if encore_festivalquestion_2 == "Natsuki":
            "Though funny enough, my last poem deviates a little from the trend, and after reading over it, I see why Yuri liked it..."
            "I guess I finally see why Natsuki wasn't crazy over my last poem..."
            "Now that I think about it, I never really realized just how lighthearted some of her poems were..."
            "Granted, I never minded if they were, it's a pretty stunning contrast between the way Natsuki and Yuri write their poems."
            "Still, I respect and appreciate Yuri as a writer just as much as Natsuki."
            "Now that I think about, it's been a while since I've gotten the chance to spend some time wth Natsuki..."
            "Hopefully we can hangout again soon..."


        if encore_festivalquestion_2 == "Yuri":
             "Despite her insecurities about her writing, I always thought her poems were fun to read!"
             "Even if her writing style is rather complex, she uses it pretty effectivly to get her message across."
             "Looking back at my poems, I realize why Yuri likes them so much..."
             "She finally found someone that she can relate to..."
             "Even though I thought she just preferred her books over people, it's quite remarkable how much closer we've gotten over these last two weeks..."
             "Especially how we were earlier today..."
             "I feel like if I give it a few more days, I may finally be ready to ask her out..."
             "Assuming she doesn't make the first move..."

if hangout1 == "Yuri":
    if hangout2 == "Monika":
        "Guess Monika was right..."
        "I am getting better!"
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that [encore_festivalquestion_2] was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Monika":
    if hangout2 == "Sayori":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I had some help from Sayori..."

        if encore_festivalquestion_2 == "Natsuki":
            "And looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
            "Guess I've gotten more inspirtation than I first realized..."

        if encore_festivalquestion_2 == "Yuri":
            "Looking over my later poems, I see why Yuri liked some of my earlier ones so much..."
            "They were fairly descriptive and the subject matter was rather dark compared to some of my more recent ones."
            "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Monika":
    if hangout2 == "Natsuki":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that [encore_festivalquestion_2] was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more cutsey, something that Natsuki would like..."
        "Guess I've gotten more inspirtation than I first realized..."

if hangout1 == "Monika":
    if hangout2 == "Yuri":
        "Guess Monika was right..."
        "I am getting better!"
        "I think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Though I can't forget that [encore_festivalquestion_2] was my inspiration for a lot of these..."
        "And looking over my later poems, I see them becoming more dark and detailed, something which Yuri would like..."
        "Guess I've gotten more inspirtation than I first realized..."


if hangout1 == "Monika":
    if hangout2 == "Monika":
        "Guess Monika was right...{w=0.38}I am getting better!"
        "I can't help but think back to the last poem I wrote..."
        "Monika..."
        "I guess all her motivation finally rubbed off on me."
        "Maybe I was trying to impress her the whole time..."




if poem_giver == "Natsuki":
    "I put down my poems and go to my bag to retrieve Natsuki's poems, which I put right next to mine."
    "I notice that in Natsuki’s stack of poems there’s a pink piece of paper."
    "Hmm…{w=0.38}I don’t remember Natsuki ever writing her poems down on pink paper..."
    "Maybe she accidentally gave me something…"
    jump day2_sarrive

if poem_giver == "Yuri":
    "I put down my poems and go to my bag to retrieve Yuri's poems, which I put right next to mine."
    "I notice that in Yuri's stack of poems there’s a purple piece of paper."
    "Hmm…{w=0.38}I don’t remember Yuri ever writing her poems down on purple paper..."
    "Maybe she accidentally gave me something…"
    jump day2_sarrive


label day2_sarrive:
"Before I could investigate further, I hear my doorbell ring."
"Wow, Sayori was a lot quicker than I'd thought she'd be."
"I go downstairs to let Sayori in..."
scene bg house with wipeleft_scene
"I open the door to see Sayori standing outside with her poems."
show sayori 4br at t11 zorder 1
s "Hey, [player]! I found them!"
show sayori 1bq
"She proudly hands me them."
mc "That's awesome! Thank you Sayori! You're the best!"
show sayori 1bs
"Sayori blushes at my compliment."
mc "So...{w=0.38}wanna come in?"
show sayori 1ba
s "Yeah, I'd love to!"
mc "Awesome!"
"I let Sayori into my house."
scene bg living_room
with wipeleft
"After putting Sayori's poems on the dining room table, I head back to Sayori, who has found her way into the living room."

if encore_sayoriquestion_1 == True:
    jump day2_sinteraction

if encore_sayoriquestion_1 == False:
    jump day2_sinteraction2

label day2_sinteraction:
show sayori 2bc at t11 zorder 1
s "So...{w=0.38}what exactly do you want to do?"

if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        show sayori 1by
        s "It's been a while since we've got to spend a lot of time together..."


mc "I...{w=0.38}I've definitely got more than a few ideas in mind..."
s 1bn "O-{w=0.38}Oh? And what would they be?"
"She looks at me quizzically, an obvious sense of intrigue in her eyes."
mc "Well...{w=0.38}let me show you..."

if encore_sayoriquestion_1 == True:
    if hangout2 == "Sayori":
        show sayori 1be at f11
        "We slowly shuffle closer to each other until we're close enough to feel each other's breath."
        "Her breaths are shallow...{w=0.38}her eyes are locked with mine."
        "My vision feels hazy...{w=0.38}her eyes...{w=0.38}have they always been that beautiful blue color?"
        "The scent of cinnamon, mixed with the feeling of her soft breaths grazing my neck..."
        "Her gorgeous blue eyes..."
        stop music
        "Suddenly I remember what I wanted to do."
        jump day2_smash

if encore_sayoriquestion_1 == True:
    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" or hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
            stop music fadeout 2.0
            show sayori 1bi
            "Sayori shoots me a disapproving look."
            s "Show me what, [player]?"
            s 1bj "Didn't you already get your chance to do that with [hangout2] earlier?"

if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    show sayori 1bl
    s "It's bad enough that we haven't gotten to spend much time together in the club lately..."
    s 1bh "But this?"
    "I feel my heart sink into my stomach as I feel the guilt from earlier return."

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        show sayori 1bl
        "My jaw drops."
        "Sayori's never been passive-aggressive, let alone aggressive, with me before..."
        s "I mean when I was with you in the club yesterday, I felt really better about everything..."
        s 1bh "But this?"
        "I feel my heart sink into my stomach as I feel the guilt from earlier return."




if apologize_sn == True or apologize_sy == True or apologize_sm == True:
    show sayori 1be
    mc "Look...{w=0.38}I'm really, really sorry about what happened earlier..."
    play music t9 fadein 2.0
    mc "What I did was wrong, even though I didn't initate what happened."
    mc "In all honesty, I was caught off guard when [hangout2] got up to me like that."
    mc "And at the time, I just didn't know what to do, I felt stuck..."
    show sayori 1bg
    mc "I could have handled that better, and I should have."
    show sayori 1bk
    mc "I know apologized earlier but you didn't really seem to accept it..."
    show sayori 1bf
    mc "So, I just hope we can move past this."
    show sayori 1bk
    "Sayori looks off before letting off a big sigh."
    show sayori 2bl
    s "I didn't really want to say anything because I didn't want to cause problems back there..."
    show sayori 2bg
    s "But, [player], I'm very disappointed in you...."
    mc "I know..."
    show sayori 1bl
    s "I mean was having a hard time earlier and seeing you..."
    s 1bu "With [hangout2] like that..."
    s 4bv "Really, really hurt, [player]..."
    "Sayori's on the verge of breaking down and crying right in front of me."
    "This is all my fault."
    mc "Sayori, even if you don't believe me, just know that I'd never do anything to hurt you."
    mc "I didn't go up to [hangout2] with the intention I'd be in her arms like that! I swear!"
    show sayori 1bt
    mc "You're my girlfriend! And I love you, and will only love you!"
    mc "That's my promise to you."
    show sayori 1bk
    "Sayori takes a moment to compose herself."
    show sayori 1bh
    s "I believe you, [player]..."
    s "And I forgive you."
    show sayori 1bk

    if hangout2 == "Natsuki" or hangout2 == "Yuri":
        s "But I'm surprised [hangout2] would do something like that..."
        mc "She doesn't know we're dating..."
        show sayori 1bn
        s "Oh yeah..."
        s 1bc "Well, I guess sooner or later we'll need to tell everyone about us..."
        mc "Yeah....{w=0.38}we will..."
        mc "I guess we can figure that out later."
        stop music fadeout 2.0
        mc "In the meantime..."
        jump day2_smash

    if hangout2 == "Monika":
        s "But I'm surprised Monika would do something like that..."
        mc "Didn't you tell her we were dating?"
        show sayori 1bn
        $ renpy.pause(delay=0.8, hard=True)
        show sayori 1bg
        s "N-{w=0.38}no..."
        show sayori 1bh
        s "I didn't even know she knew!"
        mc "Strange..."
        show sayori 1bl
        s "It's not like she was eavesdropping on us when I told you..."
        mc "Maybe she just saw us one time and assumed?"
        "Wait, that wouldn't make sense..."
        stop music
        "Suddenly it hits me."
        mc "She...{w=0.38}did say something rather strange before the festival though..."
        show sayori 1bh
        s "What'd she say?"
        mc "I remember her just saying that she's 'glad that I took responsibility for you'."
        show sayori 1bo
        mc "'Especially given that exchange you had with her yesterday'."
        mc "And then something like 'I'm glad you didn't leave her hannging this time'."
        show sayori 1bl
        s "Did she say anything else..."
        mc "Yeah, I-"
        $ renpy.pause(delay=0.10)
        window show(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 0.15
        hide screen tear
        show sayori 1be at t11
        "Suddenly remember what I wanted to do!"
        jump day2_smash

if apologize_sn == False or apologize_sy == False or apologize_sm == False:
    show sayori 1bg
    mc "Sayori, I-"
    play music t9 fadein 2.0
    s 1bh "I saw what happened, [player]..."
    s 1bl "I didn't really want to say anything because I didn't want to cause problems back there..."
    s 1bg "But...{w=0.38}why did you lie to me, [player]?"
    s 4bv "How could you do that to me?!?"
    "It seems like I have no way out of this."
    "I might as well man up now and tell her the truth."
    show sayori 1be
    mc "I didn't want you to get the wrong idea about what happened, Sayori..."

if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        s 4bw "How can I not?!?"
        "I'm shocked by Sayori's shouting."
        "She rarely raises her voice like that..."
        s 4bv "These past few days I feel like you've been completetly ignoring me!"
        mc "I haven't! Why would you think that?"

    if hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
            s 1bj "I mean, it's pretty obvious what happened..."
            s 1bi "Everyone saw it..."
            s 1by "I just want to know what happened..."
            s 1bl "Because..."
            "Sayori's voice starts to break as tears start to well in her eyes."
            show sayori 3bv
            s "I'm glad I got to spend some time with you yesterday..."
            s 4bt "It really did help..."
            s "And I don't expect you to spend all your time around me..."
            s 3bu "But what I saw earlier..."
            s "What you were doing with [hangout2]..."
            s "It hurt, [player]..."



    if hangout1 == "Natsuki" or hangout1 == "Yuri":
        show sayori 3bv
        s "Yesterday you spent your time with [hangout1] until you saw me dealing with my rainclouds..."
        s "And today you were...{w=0.38}like that with [hangout2]!"
        s "Even as I was dealing with my rainclouds again!"

    if hangout1 == "Monika":
        show sayori 3bv
        s "Yesterday you spent all your time with Monika..."
        s "And today you were...{w=0.38}like that with [hangout2]!"
        s "Even as I was dealing with my rainclouds again!"




    s 1bu "W-{w=0.38}what's going on here, [player]?"
    s "D-{w=0.38}did I do something wrong?"
    s "Do you not want me around anymore?"
    mc "Sayori!"
    mc "Don't be like that!"
    mc "You know that isn't true!"
    show sayori 1bv
    mc "Look, to tell you the truth, I didn't go up to [hangout2] to be with her like that!"
    mc "That was all her! I swear!"
    show sayori 1bk
    mc "I didn't know what to do, I blanked out..."
    mc "And that was wrong for me to do that to you..."
    show sayori 1bu
    mc "I'm sorry."
    show sayori 1bt
    mc "I was wrong to lie about this to you."
    mc "I was wrong not to say anything to [hangout2]..."
    mc "And I just hope you can forgive me in spite of everything..."
    show sayori 1bk
    mc "I know I don't deserve it..."
    mc "But you're my girlfriend..."
    mc "And I love you, and I stupidly thought lying to you was the right choice..."
    show sayori 1bt
    mc "It won't happen again. That I can promise you."
    show sayori 1bk
    "Sayori takes a deep sigh before turning back to me."
    show sayori 1bg
    s "Okay..."
    s "I forgive you."
    show sayori 1bj
    s "But it better not happen again."
    mc "It won't."
    show sayori 1bd
    "Sayori shoots me a gentle smile."
    mc "I guess we'll sort out everything else with [hangout2] later?"
    show sayori 4bd
    s "Just come here silly!"
    s "It's about time I get my turn with you!"
    mc "Don't need to tell me twice!"
    scene black
    with close_eyes
    "Sayori and I spend what feels like hours tightly embracing each other in my livingroom."
    "I feel awful for treating Sayori the way I have been latelty."
    "I chose her...{w=0.38}out of the other three!"
    "I can't be having second thoughts or trying to backout now!"
    "I love her..."
    "We've always been there for each other..."
    "I care about her, and she cares about me..."
    "I want her to be happy like how she wants me to be happy..."
    "So, which is why I'm going to make this up to her!"
    stop music fadeout 2.0
    mc "Hey, Sayori?"
    s "Yeah?"
    scene bg living_room
    with open_eyes
    show sayori 1be at t11
    jump day2_smash



if hangout1 == "Sayori":
    show sayori 1bl
    s "I mean..."
    s 1bk "It was really nice that we got to spend some time together in the club yesterday..."
    s 1bf "But I missed spending time with you again today..."
    s 1bl "I want you to get along with everyone else, but..."
    s 4bu "What I saw...{w=0.38}really hurt, [player]!"
    s 4bv "Even if you were just trying to protect me, that wasn't right!"
    s "You're not thinking of leaving me, are you?"
    mc "Of course not, Sayori!"
    mc "Look, I just wanted to see how [hangout2] was doing, that's all!"
    show sayori 1bk
    mc "I didn't intend to be like that with her!"
    mc "It just...{w=0.38}happened..."
    mc "I didn't initate it, I swear!"
    mc "When it happened, I blanked out..."
    mc "I should've said something..."
    mc "And it was wrong of me not to..."
    show sayori 1bu
    mc "I'm sorry."
    show sayori 1bt
    mc "I was wrong to lie about this to you."
    mc "I was wrong not to say anything to [hangout2]..."
    mc "And I just hope you can forgive me in spite of everything..."
    show sayori 1bk
    mc "I know I don't deserve it..."
    mc "But you're my girlfriend..."
    mc "And I love you, and I stupidly thought lying to you was the right choice..."
    show sayori 1bt
    mc "It won't happen again. That I can promise you."
    show sayori 1bk
    "Sayori takes a deep sigh before turning back to me."
    show sayori 1bg
    s "Okay..."
    s "I forgive you."
    show sayori 1bj
    s "But it better not happen again."
    mc "It won't."
    show sayori 1bd
    "Sayori shoots me a gentle smile."
    mc "I guess we'll sort out everything else with [hangout2] later?"
    show sayori 4bd
    s "Just come here silly!"
    s "It's about time I get my turn with you!"
    mc "Don't need to tell me twice!"
    scene black
    with close_eyes
    "Sayori and I spend what feels like hours tightly embracing each other in my livingroom."
    "I feel awful for treating Sayori the way I have been latelty."
    "I chose her...{w=0.38}out of the other three!"
    "I can't be having second thoughts or trying to backout now!"
    "I love her..."
    "We've always been there for each other..."
    "I care about her, and she cares about me..."
    "I want her to be happy like how she wants me to be happy..."
    "So, which is why I'm going to make this up to her!"
    stop music fadeout 2.0
    mc "Hey, Sayori?"
    s "Yeah?"
    scene bg living_room
    with open_eyes
    show sayori 1be at t11
    jump day2_smash












label day2_smash:
mc "Remember when we had that big debate over who could get more gold trophies in Mario Kart when we were little?"
show sayori 1bo
"Sayori pauses to remember."
s 2bc "Yeah...{w=0.38}why?"
mc "I think it's time to settle that debate again."
show sayori 1bq
play music t6 fadein 1.0
show sayori 4br
"Sayori giggles at my suggestion."
show sayori c112171
s "Alright, [player]. I'll warn you though, I won't hold back."
"She manages to say that in both a playful and ominous tone."
"Growing up, Sayori and I had a bit of an \"annual competition\" to see who could get the most gold trophies in Mario Kart."
"Every so often we would trade the winning title, but I remember that I barely beat her out last time."
"We also had a tradition where the loser would have to pay for the winner's ice cream at Gomaya's."
"Usually when Sayori would win, she'd get the most ridiculously expensive sundae, almost as a way to rub it in that she won."
"Usually I'd be humble and get something cheap."
show sayori 1ba at s11
"I power on my Wii and hand her one of the controllers. Seeing Mario Kart boot up on the screen again triggers a flood of memories from my childhood."
"It's been years since I've played this game, and even longer since Sayori and I have played it together."
"My skills are probably a little rusty, and I hope her's are too. "
mc "What map should we play first?"
"Sayori shoots me a sly look."
show sayori c112171
s "How about Rainbow Road?"
mc "You really think we should start off on that map considering how long it's been?"
mc "Only reason I even remember it was because of how fustrating it was..."
s 1bq "It could still be fun~"
s 4br "Unless you're too chicken!"
mc "Alright, you're on!"
stop music fadeout 3.0
"As we sit there choosing our racers, I decide to go with my old main...{w=0.38}Luigi."
"As I expected, Sayori chooses Daisy, her all time favorite."
show cg rr1 zorder 10 with dissolve_cg
play music e7
mc "Well, here we go!"
s c121114 "Good luck, [player]!"
show cg rr2 with dissolve_cg
"The race is off, the first thing I do is fall right off the map with Sayori quickly following."
show sayori 1bn
mc "Now you see why I always hated this map."
s 1ba "Yeah...{w=0.38}but this is still pretty fun!"
"A smile manages to form across my face."
"Sayori's always able to find the joy in almost anything."
show cg rr4 with dissolve_cg
"While early on Sayori and I trade leads for first place, after a while, I'm able to stay in first fairly comofortably."
"Of course, that means I've been getting bombarded with red shells."
mc "Why do you have so many red shells?"
s 1bc "The farther you are from first place, the better items you get."
mc "Oh, yeah..."
mc "I need to play this more."
"Sayori lets out a giggle as she throws out another red shell that nearly hits me."
mc "Nice try!"
"However as soon as I say that, Sayori's able to pass me."
s "Thank you~"
"Sayori and I continue to trade leads for most of the first two laps, neither of us able to gain much distance on each other before the other takes the lead again."
"Finally it comes down to the last stretch of the race, I'm barely in first."
"I can almost see the finish line…"
show cg rr3 with dissolve_cg
"Seemingly out of nowhere, one of the npc players start to catch up to us."
"In the blink of an eye, the npc passes Sayori and is right on my tail!"
"I don’t need two things to worry about!"
"Well, time to use the shells I've been saving for the end!"
"I start throwing out my shells randomly in an effort to get the npc and Sayori off my tail."
"My first shell hits the NPC successfully, its kart quickly spirals out of control before promptly falling off the map."
"However, Sayori was able to doge the other shells I threw."
"I look to see that I still have one left."
"With the finish line only about ten seconds away, and with Sayori and I neck-and-neck, it’s now or never that I use my last shell."
mc "Take this!"
"In desperation, I throw my last shell out randomly."
"However…{w=0.38}I come to regret that decision rather quickly..."
mc "Oh crap...{w=0.38}NOOOO!"
"I somehow end up hitting myself with the shell I just threw..."
"Before I know it, Sayori passes me and wins the race..."
hide cg rr3 with dissolve_cg
stop music fadeout 2.0
show sayori 1br at t11
s "YAY! I WON!"
"I sit there absolutely stunned."
"I just cost myself the game..."
play music t6
show sayori c112171
s "Looks like you'll have to buy me my favorite sundae again!"
show sayori 1bm at h11
mc "Oh no, not if I have anything to say about it!"
show sayori at thide
hide sayori
play sound "sfx/fall.ogg"
"I playfully tackle her to the floor."
"She giggles as she tries to get up, but fortunately I'm too strong for her."
show cg s_cg_2 pin with dissolve_cg
s c116314 "H-{w=0.38}hey...{w=0.38}no fair, meanie! You promised!"
show cg s_cg_2 happy with dissolve_cg
"Sayori playfully pouts at me while giving me puppy eyes."
"Under most circumstances, they really wouldn't work on me, but for some reason, today, they're super effective."
mc "I know...{w=0.38}I know...{w=0.38}I'm gonna buy you whatever you want, I'm just messing with you, Sayori."
show cg s_cg_2 relieved with dissolve_cg
"Sayori shoots me a look of relief."
s 1bo "So when do I get my ice cream?"
mc "As soon as you can get up."
show cg s_cg_2 pin with dissolve_cg
"Sayori manages to put up a good effort to get up, but again I'm too strong for her."
stop music fadeout 2.0
mc "Hahaha...{w=0.38}you haven't changed a bit, have you Sayori?"
s "Neither have you, [player]."
mc "What do you mean?"
play music t9
show cg s_cg_2 happy with dissolve_cg
s 1bc "You've always been that brash, funny guy next door who always has his head in the clouds."
s 1be "You've always been so kind to me, even when I don't think I deserve it. You've always looked out for me..."
"I can hear Sayori's voice starting to break."
s 1by "You always help me when I'm feeling down, even if you don't realize that."
"Trying my best not to blush, eventually I break and crack a wide grin at her."
s "You're the reason I even get up out of bed in the morning, [player]."
s "You're the reason I can feel happiness and joy in my life."
s "You're the reason I'm even alive."
s "Even when I’m at my lowest point…{w=0.38}when my rainclouds just pour on me…"
s "You’re the sunshine that I need to break them away…"
s 4br "I see now that I'm the luckiest girl in the world to have you as my boyfriend..."
show cg s_cg_2 happy tears with dissolve_cg
"I see tears start to swell up in Sayori's eyes."
"Listening to Sayori say that really hits me hard inside..."
"I'm the reason she's alive? There's no way she would...{w=0.38}you know...{w=0.38}she would never..."
"Before I can finish my train of thought, Sayori inches her face closer to mine."
s "[player]...{w=0.38}I-"
show cg s_cg_2 pucker with dissolve_cg
"Sayori's lips suddenly meet mine."
"Despite the sudden shock, I manage return her kiss, our lips interlocking."
"The taste of peach fills my mouth as our lips push back against each other. The smell of cinnamon radiating from her hair seems to put me in a trance."
"I pull back, and lock eyes with Sayori. As she lays there with baited breath."
show cg s_cg_2 happy with dissolve_cg
"There's a minute of silence between us as we get lost in each other's eyes."
"Finally, I decide to break the silence."
mc "So...{w=0.38}I guess you won."
s 4bq "Hehe...{w=0.38}yeah. I won fair and square."
stop music fadeout 2.0
"I get off of Sayori and help her up."
hide cg with dissolve_cg
show sayori 1bq at t11
play music t6 fadein 2.0
mc "Well, I think that's enough video games for one day, want to see what's on TV?"
s 2bx "Yeah, sure!"
show sayori at thide
hide sayori
"We spend the next few hours watching some old movies and cuddling."
scene bg living_room_afternoon with dissolve_cg
"Eventually the sun sets and it starts to get dark out."
show sayori 2bc at t11 zorder 1
s "Well, I better head back and start getting ready for tomorrow."
mc "Yeah...{w=0.38}bummer that the day went by so fast."
s 1bx "Yeah...{w=0.38}but I'll see you tomorrow, [player]! I had so much fun with you today!"
mc "I did too, Sayori! I'll see you tomorrow!"
show sayori 1bs at f11 zorder 1
"Sayori gives me one more hug before leaving to go back to her house."
show sayori at thide
hide sayori
"Man, am I the luckiest guy on Earth to have someone like her."


if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        jump day2_ref1

label day2_ref1:
"All I wish is that I could spend everyday like this with her..."
stop music fadeout 2.0
jump day2_confession


if hangout1 == "Sayori":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        jump day2_ref2

if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 "Monika":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika" or hangout2 == "Sayori":
        jump day2_ref2


label day2_ref2:
"I really should spend more time around her..."
"She is my girlfriend afterall..."
stop music fadeout 2.0
jump day2_confession


label day2_sinteraction2:
show sayori 1bc at t11 zorder 1
s "Sooo...{w=0.38}got anything planned for us?"
mc "No, not really..."
mc "We could just watch some tv if you want?"
s 2bc "Yeah, that's fine with me."
play sound "sfx/fall.ogg"
show sayori 1bb at s11
"Sayori and I take a seat on the couch right next to each other."
"We begin flipping through the channels to see if there's anything remotely interesting worth watching."
"Suddenly something catches Sayori's eye as I start rapidly moving through the channels."
s 2bn "Ohhh [player]! Go back like two channels!"
mc "Okay...."
"I flip back and we see that it's a cartoon we used to watch a lot when we were kids."
mc "Oh wow...{w=0.38}Expedition Time! We haven't seen this in ages!"
s 1bq "Hehe...{w=0.38}yeah we used to watch this together every Saturday, remember?"
"I recall Sayori always walking over to my house every Saturday to watch it with me. It was your typical action-adventure kid-friendly series, though it had a really great story for it's time."
show sayori 1bu
"I suddenly see Sayori tearing up."
mc "What's wrong Sayori?"
"She points at the TV. I see the episode title...{w=0.38}this was the last episode they made."
"That's a bummer. I thought it was at least still being made."
"Though the show already had an incredibly long lifespan already and it was starting to show that the producers were running out of ideas."
"When high school started and when we stopped hanging out as often, I guess we both stopped watching it regularily..."
"I look at the date of the episode."
"Huh..."
"It only aired a few months ago!"
mc "I can't believe we missed the finale!"
mc "By a few months too!"
s 1bt "Yeah, me too."
"Sayori wipes her eyes."
s 1bd "Well let's watch this episode together...{w=0.38}for old time's sake!"
mc "Let's do it!"
show sayori 1bt
"Sayori smiles as I rewind the TV to the start of the episode."
show sayori at thide
hide sayori
scene bg living_room
with wipeleft
"As we watch the episode, I can't help but feel a few years younger."
show sayori 1bd at t11 zorder 1
"My mind is filled with all the memories I have of Sayori."
show sayori 1be
"From when we first met, all the games we played, to moments like this..."
show sayori 1bd
"She really was always there for me...."
show sayori 1bx
"And I was there for her back then..."
"What changed?"
stop music
"The realization then hits me."
mc "No...{w=0.38}I changed{w=0.38}..."
"Sayori perks up."
s c115112 "Did you say something, [player]."
mc "Oh...{w=0.38}it was nothing."
show sayori 1bk
"Sayori sighs and turns back to the TV."
"I can't help but sigh to myself either."
"I really shouldn't keep this from her..."
"I already shut her down once."
play music t10 fadein 3.0
mc "I was thinking to myself about the times we used to share, like this, you know?"
show sayori c115112
"Sayori turns back to me."
mc "I was thinking about what changed that stopped us from doing this, and..."
mc "I see now that it was me."
show sayori 1be
mc "I guess I started getting way too into video games and anime for my own good..."
mc "I didn't really realize that it was destroying all the relationships that I had."
show sayori 1bt
"Sayori tearfully looks at me."
mc "And...{w=0.38}I'm sorry, Sayori. I shouldn't have done this to you or-"
show sayori 3bt
"Sayori puts her finger in my lips."
s "It's fine, [player]."
s 3bt "I'm just glad that we finally get to spend some time together."
s "Like we always did."
"Sayori recoils her finger."
show sayori c114312
mc "But I've still been a bad friend to you! I've been way too careless with what I say or do around you."
mc "Especially how things went last Sunday..."
show sayori 1bk
mc "With how I so carlessly hurt you...."
mc "I'm sorry..."
show sayori 1bt
mc "I really, truly-"
s c111352 "Come on, [player]..."
s 1bt "I know you wouldn't try to hurt me..."
s 1bk "But you made your choice last Sunday, and I just have to learn how to live with it..."
s 1bh "I know things are different between us now, but..."
s 1bt "Don't let regret rule your life, [player]..."
s 1bt "Look what it did to me!"
mc "But I don't even know what I want to do with my life!"
mc "I don't even know what I feel right now!"
s 1be "What do you mean?"
mc "I don't know...{w=0.38}I just don't know what I want now..."
s "I don't think I understand..."
mc "Look I'm glad I got to spend more time with the others in the club."


if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
    mc "I'm glad I got to know [encore_festivalquestion_2] very well..."


if hangout1 == "Sayori":
    mc "I'm glad that I got to spend time with you yesterday..."

if hangout1 == "Natsuki":
    mc "I'm glad that I got to spend time with Natsuki yesterday..."

if hangout1 == "Yuri":
    mc "I'm glad that I got to spend time with Yuri yesterday..."

if hangout1 == "Monika":
    mc "I'm glad that I got to spend time with Monika yesterday..."


if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "And I'm glad I got to spend time with you again today..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [encore_festivalquestion_2] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."

if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Sayori":
        mc "And I'm glad I got to spend time with you today..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [hangout1] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        mc "And I'm glad I got to spend time with her again today..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [hangout1] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."

if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Natsuki":
        mc "And I'm glad I got to spend more time with Natsuki today as well..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [hangout2] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        mc "And I'm glad I got to spend time with her again today..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [hangout1] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."


if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
    if hangout2 == "Yuri":
        mc "And I'm glad I got to spend more time with Yuri today as well..."
        mc "I don't know...{w=0.38}I feel like I should start spending some more time around you..."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and [hangout2] liked each other though."
        mc "I mean we do...{w=0.38}but we're friends. I guess on occasion we just happen to get a little too friendly."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        mc "And I'm glad I got to spend time with her again today..."
        mc "But maybe I should start spending some more time around you again."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and Monika liked each other though."
        s "Or do you like [encore_festivalquestion_2]?"
        mc "I mean like them, but, I guess that it's too early to say for sure, isn't it?"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Monika":
        mc "And I'm glad I got to finally hang around Monika today..."
        mc "And I'm glad that I got to spend some time around Monika lately..."
        mc "But maybe I should start spending some more time around you again."
        mc "I feel like that I've been too distant from you lately..."
        "Sayori shoots me a quizzical look."
        s 2be "I thought you and Monika liked each other though."
        s "Or do you like [encore_festivalquestion_2]?"
        mc "I mean like them, but, I guess that it's too early to say for sure, isn't it?"



show sayori 1bq
"We both chuckle to ourselves."
mc "But look...{w=0.38}I guess what I'm trying to say is:{w=0.38} I missed you."
show sayori 1bk
"Sayori pauses and takes a moment to reflect on what I just said."
s 1bt "[player]...{w=0.38}I..{w=0.38}missed you too..."
show sayori 1by
"Sayori has a mix of emotions on her face as she becomes as bright red as her bow."
s 1by "I...{w=0.38}I wouldn't mind spending more time around you, [player]."
mc "Yeah...{w=0.38}it's been too long..."
"Unable to say anything more to each other, we turn our attention back to the TV, finishing the rest of the episode."
show sayori at thide
hide sayori
pause 0.8
scene bg living_room_afternoon with Dissolve(0.75)
image sayori e2bx = evening("mod_assets/sprites/2bx.png")
image sayori e1bq = evening("mod_assets/sprites/1bq.png")
"The sun sets just as the episode is finished."
"They truly went out with a bang!"
show sayori e2bx at t11
s "Well that was fun [player]!"
mc "Yeah, it was! It was a little hard to follow with some the new characters though."
s "I guess we can watch the lead up to the finale together sometime!"
mc "Yeah! That sounds great!"
s "Well, I have to head back, [player]."
mc "Alright, I'll talk to you tomorrow!"
s e1bq "Laters!"
show sayori at thide
hide sayori
"Sayori smiles sweetly before turning out the door and exiting my house."
"I sit there for a moment reflecting on today's events."
"Sayori and I were finally able to at least put some of last Sunday's events behind us..."
"Well, progress is progress!"
"I think that to myself as I grab Sayori's poems and head upstairs."
stop music fadeout 2.0
jump day2_confession
