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
    mc "Sayori, I don't think you're looking at this the right way at all..."
    s 1e "Eh?"
    mc "Look I know that this is new for the both of us..."
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
    mc "It's just that...I've known you for as long as I can remember..."
    mc "I always saw you as someone who was always happy, bubbly, sometimes clumsy, but overall..."
    mc "Just a big bundle of joy and sunshine."
    mc "I never would've thought that in a million years that you would've ever been going through something like this."
    "Sayori pauses, as if to reflect on what I just said."
    s "I mean... I've always had it..."
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
"As emotional as we both are right now… this is nice."
"We're like this for sometime before I here some commotion come from the closet."
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
    n 5e "Ugh, I can't find my volume 12 of Parfait Girls set! Everything's been moved around again!"
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
    y "Hey, [player]!"
    mc "Oh! Hey, Yuri!"
    show yuri u114221
    y "How have you been lately?"
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
    s 1bk "Do I...{w=0.38} really deserve any of this?"
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
s 2bd "So...{w=0.38} got anything planned for us today?"
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
scene bg house
with wipeleft_scene
show sayori 1bq at t11 zorder 1
s "Hey, thanks for everything today!"
s 1bd "It really helped being able to spend time with you today..."
mc "Well, I'm glad I was able to help, Sayori! I'll see you tomorrow!"
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
    mc "Hey...{w=0.38} hey...{w=0.38} it's okay."
    show sayori 1v
    mc "You're incredibly strong for doing this all on your own, and I couldn't be more proud of you Sayori."
    show sayori u111352
    "I see a mixture of emotions on Sayori's face, as if she's trying to fight back tears while trying not to blush like an idiot."
    "But she's my idiot."
    "She's my Sayori."
    "And... I love her."
    "I just wished I had the courage to tell her that again..."
    "Sayori hugs me again and I gladly reciprocate."
    play sound "sfx/fall.ogg"
    scene black
    "She lays her head on my shoulder and holds my hand."
    "I lay my head on top of hers, and wrap my other arm around her."
    "The smell of cinnamon penetrates my nostrils with every breath I take."
    s "T-thank you.. [player]."
    mc "Don’t mention it, Sayori."
    s "Lately my emotions have been all over the place. First, I felt like I was a burden to you, and now…"
    "Her voice trails off."
    mc "What is it, Sayori?"
    "Sayori take a deep breath as she hugs me tighter."
    s "Now… I feel like I really shouldn’t be here."
    mc "What do you mean?"
    s "I don’t know… just the past few days I’ve had this feeling that I really shouldn’t be here, with you, that none of this should’ve happened."
    "I feel my heart sink into my stomach."
    "She doesn’t mean…"
    s "I’m not doubting our relationship or anything… it’s just… I guess you could say I feel out of place or something."
    s "I don’t know… it’s what actually convinced me to call my doctor."
    mc "Well, I’ll say this Sayori..."
    "I’m glad you’re here with me. I wouldn’t change any of this for the world."
    mc "I’m so glad that we found our feelings for each other."
    "Sayori only hugs me tighter as I say that."
    "Never in a million years did I think I would’ve ended up with someone like Sayori."
    "A guy like me and a girl like her?"
    "What are the odds…"
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
