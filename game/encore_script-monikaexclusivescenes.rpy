#Day 1
label mencore_1:
    $ hangout1 = "Monika"
    "I decided to check up on Monika."
    scene bg club_day
    with wipeleft_scene
    play music tmonika
    "I quietly approach her but she quickly notices me."
    show monika 1b at t11 zorder 1

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == False:
                m "Oh, [player]! I thought you'd want to hang out with Natsuki again?"

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == True:
                m "Oh, [player]! I thought you'd want to hang out with Sayori again?"

    if encore_festivalquestion_2 == "Yuri":
            if encore_sayoriquestion_1 == False:
                m "Oh, [player]! I thought you'd want to hang out with Yuri again?"

    if encore_festivalquestion_2 == "Yuri":
            if encore_sayoriquestion_1 == True:
                m "Oh, [player]! I thought you'd want to hang out with Sayori again?"

    m 5a "After all, you guys are like two peas in a pod over there."
    "Monika says teasingly."

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == False:
                "Wait...{w=0.28} does Monika really think that Natsuki and I are {i}that close{\i}?"
                "I mean we’re just friends, but..."

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == True:
                "I mean Sayori and I may be dating, but that doesn't mean I can't spend my time around the other girls...{w=0.38} right?"

    if encore_festivalquestion_2 == "Yuri":
            if encore_sayoriquestion_1 == False:
                "Wait...{w=0.28} does Monika really think that Yuri and I are {i}that close{\i}?"
                "I mean we’re just friends, but..."

    if encore_festivalquestion_2 == "Yuri":
            if encore_sayoriquestion_1 == True:
                "I mean Sayori and I may be dating, but that doesn't mean I can't spend my time around the other girls...{w=0.38} right?"


    mc "I just thought I should check up on you first, that's all."
    m 1d "Eh?"
    show monika u114311
    "Monika’s expression quickly changes as she now looks at me with a curious gaze."
    m u114312 "So you're {i}choosing{/i} to spend time with me and not any of the others?"
    mc "Umm...{w=0.28}yeah...I guess?"
    show monika 1k at h11
    "Monika’s eyes suddenly light up with what I can only describe as pure ecstacy..."
    show monika 1b at t11
    m "OH! Well? What do you want to do?!?"
    "I’m surprised by Monika’s sudden burst of energy as she starts spouting out ideas for activities that we can do together."
    "It almost reminds me of Sayori’s sugar high from when she ate all of Natsuki's cupcakes at the festival."
    m 4k "I’ve been actually meaning to read this big novel with someone for a while now!"
    m 5a "I heard this novel is really fun to read with when you have someone with you~"
    "I'm not sure whether to be amused or concerned at Monika's sudden excitement."
    mc "I thought maybe we could just talk about how you're doing."
    mc "You seemed to have had a rough day..."
    show monika u114311
    "Monika suddenly realises how excitable she's become and recomposes herself."
    m 2n "Oh...{w=0.38} yeah...{w=0.38} sorry, I got kind of got carried away there, didn't I?"
    m 2l "Sorry, [player]! Just seeing you seems to have put me in better spirits~"
    mc "Well, hey! Glad I could help!"
    show monika 1j
    "Monika nods happily at me."
    "I decide to break the ice."
    mc "Sooo...{w=0.28}are you sure you're really okay with the club staying the same?"
    mc "I know how much expanding the club meant to you and everything..."
    show monika 1d
    "I see the joy in her face subside."
    show monika 2r
    "She then lets out a pained sigh."
    m 2q "It's just hard for me to wrap my mind around all this..."
    m 2r "I thought I did everything I could to make sure everything went smoothly..."
    m 2c "And you guys played your part perfectly, so I'm not blaming you or anyone else."
    m 2p "I just feel like I messed up somewhere..."
    "Her eyes drift towards her feet."
    m 1n "But to tell you the truth, I've just had a lot on my mind lately."
    m 1l "Everything just kind of snowballed into that episode earlier..."
    mc "Do you want to talk about it?"
    show monika 1o
    "Monika pauses for a moment, almost like she's internally debating if she wants to open up to me."
    "After about a moment, she breaks the silence."
    m 1l "Well, let's just say that I had a big surprise planned for someone."
    mc "Oh? For like a birthday party or something?"
    show monika 1j
    "Monika giggles at me."
    m 1a "No, silly! It's not that kind of surprise."
    m 1b "But it's something that I've been working on for quite a while now, and very recently, something happened that I thought ruined everything."
    m 1k "But now it seems like I can still salvage the situation."
    show monika 5a
    "Monika flashes a smile at me."
    "I'm not sure what Monika is trying to get at here."
    "Or who this 'surprise' is supposed to be for..."
    "But, I hope things work out for her in the end."
    mc "Well, I hope it all works out for you, Monika."
    mc "I know you can accomplish anything if you put your mind to it."
    mc "I'm sure sooner or later we'll get more members and I'm sure that your surprise will be great for whoever it's for."
    show monika u114311
    "Monika blushes at my compliments."
    m u111331 "Yeah...{w=0.28}you're right, [player]."
    "Monika suddenly looks me in the eyes with a look of determination that's almost scary..."
    m 5a "I think it will work out in the end~"
    mc "Y-{w=0.28}yeah...{w=0.28} I hope it does..."
    show monika 2k
    "Monika flashes me her signature grin, and I can't help but smile back at her."
    "We stand there for a few moments before Monika suddenly calls out."
    show monika 4b at h11
    m "Ok everyone, poem time!"
    m 5a "I can't wait to see what you wrote for today, [player]!"
    "I must admit I'm not used to Monika showing me this much attention."
    "Not that I mind it anyway. Getting noticed by someone like Monika is a good thing."
    mc "Y-you too, Monika!"
    mc "Can't wait to see what you wrote as well!"
    show monika 1j
    "Monika lets out a cute giggle."
    "Natsuki shoots us a suspicious look."
    show natsuki 5e at t33 zorder 1
    n "Are you two going to stand there and flirt all day, or you going to share your poems with us?"
    m 1l "Right, right...{w=0.28}sorry!"
    show natsuki at thide
    hide natsuki
    m 1a "See you in a bit, [player]~"
    mc "Later, Monika!"
    show monika at thide
    hide monika
    stop music fadeout 2
    "I go to my bag to retrieve my poem."
    with wipeleft_scene

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Monika":
            jump poem_scene13

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Monika":
            jump poem_scene14

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Monika":
            jump poem_scene15


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Monika":
            jump poem_scene16








#Day 2

label mencore_2:
    $ hangout2 = "Monika"
    stop music fadeout 3.0
    "I decided to take Monika up on her offer to show me her poem."
    scene bg club_day
    with wipeleft_scene
    play music e2
    "Sure enough, Monika's at the teacher's desk, reading a piece of paper that I assume to be her poem."
    mc "Hey, Monika!"
    show monika 1d at h11 zorder 1
    pause 0.8
    show monika 1j
    "Monika tilts her head up to see who called her, but she instantly smiles once she sees that it's me."
    m 2k "[player]! I take it you wanted to see my poem after all?"
    mc "You know it!"
    mc "Not to mention, I really do enjoy reading your poems!"
    mc "Even if I don't quite understand what they're trying to say sometimes..."
    "Monika manages a small giggle."
    m 5a "Well that's the beauty of writing, [player]!"
    m 1k "You can write about anything!"
    m 1e "As long as you put your best effort into it, you can almost feel the soul of the writer when you read their work!"
    m "Sometimes the most beautiful things are the things we don't understand."
    m 1b "And sometimes, there may not even be a correct meaning behind their work."
    m 1j "It's just left up to the reader to think for themselves on what they believe it means!"
    m 1n "But, I think your poetry skills have improved since you first started, so maybe you'll be able to understand this one..."
    "Despite my best efforts, I blush at Monika's compliment."
    mc "T-{w=0.28}thank you, Monika..."
    mc "I'm glad you think I'm getting better..."
    m 2e "Aww...{w=0.28}[player]..."
    m 2k "I'm really lucky to know someone as sweet and humble as you, aren't I?"
    "I'm just \"lucky\" to have Monika complimenting me like this..."
    show monika 2e
    "I think to myself about how many guys would be tripping over themselves just to be in my shoes right now..."
    show monika cute
    "Just being able to see how she is now..."
    "Her emerald eyes..."
    "Her irresistible smile..."
    show monika 5a
    "And her exceptional puns!"

    if encore_sayoriquestion_1 == True:
        "Wait...{w=0.28}why am I thinking like this?"
        "What about Sayori?"


    if encore_sayoriquestion_1 == False:
        "If heaven was a person...{w=0.28}Monika would fit the bill..."

    "I snap out of my train of thought."
    mc "Well...{w=0.28}I try..."
    show monika 2m
    "Monika glances down to the paper on her desk."
    mc "If you're still working on it, I can come back later..."
    m 2k "Oh no, it's fine [player], really! I actually just finished it."
    show monika 2e
    "I see another smile start to form across Monika's face."
    mc "I hope I didn't forget to write a poem when we were supposed to..."
    show monika 2k
    "Monika giggles again."
    m 2b "Don't worry about it, [player]! I just made it for fun this time."
    m 4b "Are you ready to read it?"
    mc "You know it!"
    m 4k "I hope you like it, [player]."
    call showpoem(poem_m_connection, music=False, revert_music=False, img="monika 1a")
    show monika 1a

    if hangout1 == "Monika":
        "Something about the way that this is written raises my eyebrows."
        "I mean, it's a fantastic poem..."
        "Truly one of Monika's best to date!"
        "But, funny enough, the poem says the some of the same things as that weird voice did in my dream last night."
        "It's probably just a coincidence though..."

    if hangout1 == "Sayori" or "Yuri" or "Natsuki":
        pass # Temporary

    m 1b "So, what did you think?"
    mc "It's great Monika! I think this is your best one yet!"
    show monika 1j
    mc "I really like the way you made it flow!"
    mc "And the way you ended it was pretty solid too!"
    mc "I like the title too! 'Connection'...{w=0.38}it really stands out!"
    "I hand her back her poem."
    m 1k "Glad you liked it, [player]!"
    m 3m "I spent a lot of time on it, so I'm glad it all paid off!"
    mc "Monika, everything you do pays off in the end."
    show monika 1d
    "Monika looks at me with an intrigued look on her face."
    m u114312 "Eh?"
    m "What do you mean?"
    mc "You're smart, friendly, talented, beautiful..."
    m u112332 "Oh, come on [player]..."
    mc "Huh?"
    m u121351 "You're just buttering me up now, aren't you?"
    show monika u111394
    "Monika's eyes take a suggestive tone."
    "She stands up abruptly, leaning towards me in an almost seductive manner."
    "I was not expecting this..."
    "I feel my heart start pounding in my chest as I feel drop of sweat trickle down my back..."
    mc "Well...{w=0.38}maybe a little{w=0.28}...I did like your poem though, honest!"
    show monika u121331 at f11
    stop music fadeout 2.0
    "I'm stammering with my words as I feel Monika's breath brush across my face."
    m 1d "Hmmm..."
    "Monika's eyes scan me up and down."
    m 1j "You know [player], you really should straighten out your tie."
    m 1k "It's important to me that all my club members look as professional as possible."
    mc "Uh yeah...{w=0.38}you're t-{w=0.28}totally right."
    mc "How careless of me!"
    "Monika suddenly grabs a hold of my tie."
    play music t9 fadein 2.5
    show cg m_cg_1 zorder 10 with dissolve_cg
    m "Here...{w=0.38}let me fix that for you."
    hide monika
    "Her voice is a whisper at this point."
    "I can't help but stare into her eyes as she looks up to me."
    "I never thought the color emerald could be so beautiful!"
    "Monika slightly parts her lips as I feel her warm breaths graze against my neck."
    "This feels...{w=0.38}good..."
    "Never in a million years would I have ever thought that I'd be like this with Monika."
    "In fact...{w=0.38}I never thought I'd be this close to Monika period!"
    "Speaking of finding..."
    "I briefly look around the room."
    "There's no way that they haven't at least looked up once and saw us like this..."
    "Or even overheard what we were saying..."
    "It's not like we were really being that quiet to begin with..."
    hide cg with dissolve_cg
    show yuri 2g at t32 zorder 3
    "Yuri still seems to be into her book,{w=0.80}{nw}"
    $ _history_list.pop()
    show sayori 1k at t31 zorder 1
    "Yuri still seems to be into her book,{fast} Sayori's spacing out{w=0.80}{nw}"
    $ _history_list.pop()
    show natsuki 5a at t33 zorder 2
    "Yuri still seems to be into her book, Sayori's spacing out{fast} and Natsuki is in her usual spot under the windowsill reading her manga."
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    "I turn back to meet Monika's gaze."
    show monika u114311 at face with dissolve
    "Words truly cannot describe what looks back at me.."
    "Everything about her is...{w=0.38}perfect."
    show monika u111311
    "It's as if all of my natural senses are being bombarded by the figure standing in front of me..."
    "..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.25
    hide screen tear
    $ style.say_dialogue = style.edited
    play ambient "sfx/eyes.ogg"
    "All desire at this point has left my mind."
    "I just want to be with her."
    "Just her..."
    $ style.say_dialogue = style.normal
    stop ambient


if encore_sayoriquestion_1 == False:
        m 1l "You know [player], if you're always going to look this messy..."
        m u121351 "Maybe I should help you get up in the morning..."


if encore_sayoriquestion_1 == True:
        m 1l "You know [player], I'm surprised Sayori doesn't fix this for you..."
        m u121351 "Maybe I should help you get up in the morning instead~"
        "How does she know about that???"


"Monika puts her hand on my cheek as she intensely looks me in the eyes."
"I can't tell if Monika is just teasing me or is actually being serious here."
mc "Oh! Um...."
"How do I respond to something like that?"
"My mind goes completely numb."
"I don't even know what I'm doing anymore."
show monika u111394
"My hands are resting on her hips, and Monika has \'the look \' on her face."
"My anxiety shoots through the roof."
"My heart is pounding at a million miles a second."
"My palms become sweaty as my I feel like my legs are about to give out at any second."
"Is this my chance?"
"My chance to be with {i}the Monika?{/i}"
m "I need to tell you something important, [player]..."
mc "Y-{w=0.38}yeah?!?"
show monika u114341
"Monika leans into my ear to whisper something..."
stop music fadeout 1.0
show black zorder 10 with Dissolve(0.5)
$ style.say_dialogue = style.edited
"{w=0.75}G{w=0.75}o{w=0.75}o{w=0.75}d{w=0.75} c{w=0.75}h{w=0.75}o{w=0.75}i{w=0.75}c{w=0.75}e{w=0.75}..."
$ style.say_dialogue = style.normal
"..."
m "Just-"
"Suddenly, I hear Sayori get up."
hide monika
hide black
with Dissolve(0.5)
play music t5 fadein 1.0
show sayori 4m at t21 zorder 2
s "Oh my gosh guys, I completely forgot! Monika has an important announcement to make!"
show natsuki 5k at t22 zorder 1
n "Woah, really?"
show natsuki 2g
show sayori 1b
"I see Natsuki's and Sayori's eyes turn to me and Monika."
show yuri 3n at t33 zorder 3
show sayori at t31
show natsuki at t32
"Yuri, confused as to what's going on, turns around..."
show yuri u125111
"Only to see what Natsuki and Sayori are staring at."
"Monika and I practically look like we were just slowdancing in the middle of the clubroom..."
show natsuki 5g
show sayori 1i
show yuri u123114
"All three girls are looking at us, with a bit of an irritated{w=0.38}...almost jealous{w=0.38}...expression on their faces."
"Great..."
"Well, it's up to me to attempt to salvage this situation."
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
show yuri at thide
hide yuri
show monika u114311 at face
pause 0.8
show monika u114211 at t11 zorder 1
"I clear my voice and suddenly separate from her."
show monika 1m
"Monika looks at me with a sudden look of shock and disappointment, as if she wanted this to last longer."
"I can't really blame her though..."
show monika 1d
mc "Well Monika{w=0.38}...um...{w=0.38}thanks for the{w=0.38}...advice!"
mc "It was very inspiring."
"Monika quickly catches on to what I'm saying."
m 2b "Well [player], you can come to me any time."
show monika u111151
"Monika gives me a wink."
"I can't help but manage a smile to Monika."
show monika at thide
hide monika
"I feel all the blood rush to my face as I turn around to face the others."
"None of the others make eye contact with me as they go to join us at the front of the room."

if encore_sayoriquestion_1 == True:
    jump day2_caught_m


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki" or hangout1 == "Monika":
            jump day2_angry_nm

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
            jump day2_angry_nm

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            jump day2_angry_ym

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri" or hangout1 == "Monika":
            jump day2_angry_ym

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori":
            jump day2_angry_sm

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            jump day2_angry_sm



#Sayori Response


label day2_caught_m:
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
                $ apologize_sm = True
                jump sayori_sorry_m
            "Lie.":
                $ apologize_sm = False
                jump sayori_not_sorry_m

label sayori_sorry_m:
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
$ style.say_dialogue = style.edited
show sayori 1q
s "You should stick to seeing Monika, you cheating jerk!"
$ style.say_dialogue = style.normal
show sayori 1r
s "Come on, let’s not keep the others waiting!"
jump day2_meettheclubs

label sayori_not_sorry_m:
"I don’t want Sayori to get the wrong idea about Monika and I."
"I try to come up with an excuse off the fly."
mc "Monika was trying to help me..."
show sayori 1e
mc "She saw that my tie was messed up...and she was trying to fix it up for me..."
mc "It was that and only that...{w=0.38}I promise..."
show sayori 1k
"Sayori lets out a heavy pained sigh before putting on a smile."
show sayori 1l
s "It’s alright, [player]."
show sayori 1x
s "I’m just glad she’s being a good friend to you!"
$ style.say_dialogue = style.edited
show sayori 1q
s "I’m totally not jealous or anything like that!"
$ style.say_dialogue = style.normal
show sayori 1r
s "Come on, let’s not keep the others waiting!"
jump day2_meettheclubs



label day2_angry_nm:
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
"I just hope she isn't jealous of me and Monika getting so close like that."
"Hopefully then, she won't full on put me in the hospital."
"Oh well..."
jump day2_meettheclubs


label day2_angry_ym:
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
"I just hope she isn’t jealous of me and Monika getting so close like that."
"She isn’t the jealous type...{w=0.38}right?"
jump day2_meettheclubs


label day2_angry_sm:
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
"I take it she didn't take too kindly to me getting too close to Monika like that."
"I really need to be more careful around her..."
"Though, Sayori was never the jealous type..."
jump day2_meettheclubs


#Day 3

label mencore_3:
    $ hangout3 = "Monika"
    "I guess talking to Monika some more wouldn't hurt."
    scene bg club_day
    with wipeleft_scene
    play music e13 fadein 2.0
    "Monika is at the teacher’s desk, but she isn’t on the computer like she normally is."
    show monika 1j at t11 zorder 1
    show airpod both at t11 zorder 1
    "Instead, she’s looking down at her ipod and humming a tune to herself."
    "Intrigued, I carefully approach her, not wanting to startle her."
    mc "Hey, Monika."
    show monika 1d at h11 zorder 1
    show airpod both at h11 zorder 1
    "She quickly looks up at me, popping out one of her AirPods."
    show airpod left at t11 zorder 1
    m 1b "Oh, hey [player]!"
    m "I take it you wanted to see what I was working on?"
    show monika u111151
    "Monika flashes her usual wink."
    mc "I mean, hey, if you think it’d help..."
    mc "Besides, I’m sure your music is awesome!"
    show monika 1m at t11 zorder 1
    "Monika smiles bashfully."
    m 1n "Well, it’s not finished yet..."
    m 1m "I’ve been listening to these samples all day trying to figure out how to make the next verse..."
    m 1n "Chord progressions are more complicated then you would expect."
    mc "So you’re working on your own song then?"
    m 1k "Yep!"
    m 1b "It’s the reason I started playing the piano, I’ve always wanted to make my own song since I was really young."
    m 1m "Though lately, I haven’t had much time to work on it..."
    m 1n "Things just kept coming up recently..."
    mc "I take it was that ‘surprise’ you had for someone..."
    show monika 1j
    "Monika nods."
    mc "And how’s that going?"
    m 1b "Pretty well, actually! I think I’ll be able to show them my surprise on Friday!"
    m 1m "Funny enough, what I’m working on is tied into my surprise..."
    mc "That’s awesome, Monika!"
    mc "You really are a jack of all trades, aren’t you?"
    m u121331 "Awww, [player]..."
    hide airpod left
    show monika 5a
    "Monika grins at me."
    show monika smirk
    m "I just strive to be the best I can be."
    mc "Well you’re definitely succeeding..."
    show airpod left at t11 zorder 1
    m 1m "Well if that’s the case, maybe I can show you what I’ve been basing my song off of."
    mc "How much of the song is done?"
    m 1a "I’d say that the first verse is pretty much done at this point."
    m 1b "I was thinking that the second verse could go something like this..."
    "Monika hands me one of her AirPods."
    mc "Well, I’m not sure if I’m the best go-to-person for music advice, but I guess I could give it a listen."
    m 1j "That’d be awesome, [player]!"
    "I pull up a chair and sit right next to her."
    mc "So I take it this is a piano track?"
    stop music fadeout 4.0
    m 1a "Yep! Right now it's just going to be a piano solo."
    mc "Alright..."
    "Monika hits the play button on her ipod."
    window hide
    play audio sample
    $ renpy.pause(delay=10.00, hard=True)
    show monika 1j
    $ renpy.pause(delay=17.00, hard=True)
    show monika 1a
    mc "Huh, that was actually pretty good!"
    play music e2 fadein 1.0
    mc "You think you could actually play that?"
    m 1m "Well with some more practice, I think I can pull it off."
    mc "Do you want to take a crack at it now?"
    show monika u114311
    "Monika’s eyes widen at my suggestion."
    mc "I mean...{w=0.38}it’s fine if you don’t want to..."
    m 1n "No, it’s not that..."
    m 1d "It’s just that I’ve never played it in front of anyone before."
    m 1c "I’ve only played by myself."
    mc "Well, it’d probably help for you to play it in front of someone first, wouldn’t it?"
    show monika 1m
    "Monika pauses to think."
    mc "And if you think you can pull off that sample with just a little practice, then I’m sure I’ll love your song!"
    m 1n "O-{w=0.38}okay..."
    m 1e "Let's do it!"
    hide airpod left
    "I hand Monika back her AirPod as she pops the other one out."
    m 1b "We can use the piano in the band room."
    m 1a "The band doesn’t meet on Wednesday’s so nobody should be in there right now..."
    mc "Alright, lead the way!"
    show monika 1j
    "Monika smiles as she leads me out the door and into the hallway."
    scene bg corridor
    with wipeleft_scene
    show monika 1m at t11 zorder 1
    "As we’re walking towards the music wing, I can’t help but tell that Monika seems a little apprehensive."
    "Well, she did say that she’s never played in front of anyone before..."
    "If I was in her shoes, I’d probably be a nervous wreck."
    show monika 1e
    "But Monika has done a lot of incredible things before..."
    "She’s won so many gymnastic and debate trophies for the school these last two years..."
    show monika 1j
    "Not to mention all the writing competitions she’s won..."
    "It wouldn’t surprise me if she’s drowning in college offers..."
    "I can only imagine just how hard she’s worked to get herself there."
    "Anybody would want to be like her..."
    "And it's a no-brainer for why every guy wants to be with her..."
    stop music fadeout 3.0
    m 1b "Well, here we are!"
    show monika 1a
    "Monka stops in front of the band room."
    mc "Huh, so this is the band room?"
    m 1d "You’ve never been inside before?"
    mc "Can’t say I have."
    m 1k "Well this definitely going to be a special day for you, [player]~"
    "Monika opens the door and flicks on the lights as we enter the band room."
    play sound "sfx/closet-open.ogg"
    show monika at thide
    hide monika
    scene bg music_room
    with wipeleft_scene
    "Woah..."
    "I don’t think I’ve seen so many different instruments before..."
    "I almost want to pick one up and try playing something but, I’d rather not make a fool of myself in front of Monika."
    show monika 2a at t11 zorder 1
    m "Isn’t it amazing?"
    mc "Yeah...{w=0.38}it really is..."
    mc "I definitely need to visit this place again sometime..."
    "In the corner of the room by the window, I see a Grand Piano lined against the wall."
    mc "So that’s where you’ve been practicing..."
    m 1a "Yep, I get a pretty nice view of the courtyard from here as well."
    m 1j "I find that the view is pretty inspiring."
    mc "I see..."
    show monika 1m
    "We both turn to face the piano."
    m 1n "Well...{w=0.38}here I go."

    $ skip_song = False

    if config.developer == True:
        call screen confirm("You are about to lose control in developer mode.\nSkip ahead instead?", Return(True), Return(False))
        if _return:
            $ skip_song = True
        else:
            pass

    show monika 1m
    "She quietly makes her way towards the piano and sits down."
    "I pull up a chair and sit right across from Monika."
    "She takes a deep breath as her fingers hover over the keys as she looks on at me."
    mc "You got this, Monika!"
    "Monika lets out a small laugh."
    m 1l "Thanks, [player]!"
    show monika 1r
    "Monika cracks her knuckles, letting out one more breath before positioning her fingers above the keys."

    if skip_song == True:
        jump post_monika_song

    show screen disable_control
    $ renpy.choice_for_skipping()
    $ quick_menu = False
    $ m.what_prefix = ''
    $ m.what_suffix = ''
    scene black
    play music preview noloop
    "{cps=34}A split second later, she begins playing.{/cps}{w=3.0}{nw}"
    "{cps=34}I can’t help but notice how elegantly her fingers grace the keys.{/cps}{w=3.0}{nw}"
    "{cps=34}The melody is calm, but purposeful. Every action with intent, and care...{/cps}{w=0.38}{cps=34}it's almost hypnotizing!{/cps}{w=3.0}{nw}"
    "{cps=34}Unexpectedly, Monika starts to sing.{/cps}{w=1.5}{nw}"
    show cg piano_cg_alt with dissolve_cg
    m "{cps=34}\"Every day, {/cps}{w=1.25}{cps=30}I imagine a future where {/cps}{w=1.20}{cps=30}I can be with you...\"{/cps}{w=3.0}{nw}"
    m "{cps=34}\"In my hand, {/cps}{w=1.45}{cps=34}is a pen that will write a poem {/cps}{w=1.4}{cps=34}of me and you...\"{/cps}{w=3.0}{nw}"
    "{cps=34}Not even ten seconds in and I’m already blown away...{/cps}{w=3.0}{nw}"
    "{cps=34}Her voice is almost angelic as her emerald green eyes light up with a fiery passion that I've never seen before...{/cps}{w=3.1}{nw}"
    m "{cps=34}\"The ink flows down {/cps}{w=1.31}{cps=34}into a dark puddle...{/cps}{w=2.01}{cps=34}just move your hand...\"{/cps}{w=0.45}{nw}"
    m "{cps=30}\"Write the way into his heart!\"{/cps}{w=1.80}{nw}"
    #show cg piano_cg with dissolve_cg
    show cg piano_cg as cg2 at cgfade
    "{cps=34}Monika takes a brief look over at me, smiling before she goes back to focusing on the piano.{/cps}{w=6.5}{nw}"
    hide cg2
    #show cg piano_cg_alt with dissolve_cg
    m "{cps=34}\"But in this world of infinite choices...{/cps}{w=3.48}{cps=34}what will it take just to find that special day?\"{/cps}{w=2.93}{nw}"
    m "{cps=24}\"What will it take...{/cps}{w=0.684}{cps=24}just to find...{/cps}{w=1.36}{cps=24}that special day!\"{/cps}{w=4.0}{nw}"

    $ m.what_prefix = '"'
    $ m.what_suffix = '"'
    $ quick_menu = True
    hide screen disable_control

    label post_monika_song:
        pass
    scene bg music_room
    show monika 2m at t11 zorder 1
    "Monika suddenly stops playing and turns to face me."
    m "Well...{w=0.38}that’s about all I have right now..."
    "I can barely contain my enjoyment as I stand up and applaud as loudly as humanly possible."
    mc "Encore! Encore!"
    show monika 1k at s11 zorder 1
    "Monika lets out a giggle as she takes a small bow."
    show monika 1e at t11 zorder 1
    m 2e "I take it you liked it then?"
    mc "Can you please perform at the festival next year?"
    show monika u114311
    "Monika blushes brightly."
    m 2m "I can't say that I would be opposed to it."
    m 5a "Though, I did enjoy performing for just one person~"
    mc "Oh! Well, uh..."
    "If she wants to perform for just me, I certainly wouldn’t mind that...{w=0.38}amongst other things..."
    show monika 1k
    "Monika lets out another giggle."
    m 1a "Well, maybe when it’s finished, I can show you again..."
    mc "That’d be awesome, Monika!"
    mc "And I think the others would love to hear this too!"
    m 1m "I’m sure they would..."
    m 3l "After all, music is considered a form of poetry!"
    mc "Yeah, it is!"
    mc "Have you come up with a name for the song yet?"
    m 2n "I’m still thinking it over..."
    m 2r "This song does have a lot of meaning behind it..."
    mc "In what way?"
    mc "I figure that from what I’ve heard, it has something to do with love..."
    m 2m "Yeah...{w=0.38}you could say that..."

    if encore_sayoriquestion_1 == True:
        "A smile comes across my face."
        "It's good to see that Monika's interested in someone."
        "Especially since she spends a good portion of her time fending off advances from other guys..."
        show monika 2e
        "Still...{w=0.38}I wonder who Monika's interested in..."
        m "I really appreciate you encouraging me to play for you, [player]."
        m 2b "I’ll definitely feel more comfortable with sharing it when it’s all good and ready..."
        show monika 2a
        mc "Yeah...{w=0.38}I’m sure whoever this for is really going to enjoy it..."
        m 2k "I already know he will~"
        "She says softly as she slides up to me."
        show monika tease
        m "Maybe we can even do a little duet..."
        show monika u111394
        mc "Well...{w=0.38}I-{w=0.38}I’ve never really picked up an instrument before..."
        show monika tease
        m "Maybe I can teach you..."
        show monika u111394
        "My heart nearly pounds out of my chest."
        mc "I-{w=0.38}I mean..."
        show monika tease
        m "I think there’s a lot of things we can learn about each other, [player]..."
        show monika u111394
        mc "Ah, well, there’s really nothing too much to learn about me..."
        mc "I’m not like some super talented guy or anything..."
        show monika tease
        m "There’s always something to learn about everyone..."
        m "And, I’m a very curious person..."
        show monika u111394
        "I feel sweat start to trickle down the back of my neck as Monika intimatly gazes at me."

        if hangout2 == "Monika":
            "This is just like yesterday..."
            "What's Monika doing?"

        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            pass

        show monika tease
        m "I hope you've been doing some thinking, [player]..."
        mc "Well...{w=0.38}you've given me a lot to think about..."
        show monika tease
        m "That's the idea, [player]..."
        m "Isn't it nice to have someone who knows what she wants?"
        m "Someone you don't need to worry about?"
        m "Someone who doesn't feel guilt or shame when she's with you?"
        show monika u111394
        "Monika's voice echos in my head as I process her questions."
        "How do I respond to this?"
        "I don't know how I feel about Monika's advances..."
        "On one hand...{w=0.38}this feels nice..."
        "But...{w=0.38}it's wrong..."
        "I don't know whether to feel pleasure or guilt by all this..."
        "What is she trying to get at?"
        mc "I..."



    if encore_sayoriquestion_1 == False:

        if hangout1 == "Monika":
            if hangout2 == "Monika":
                "I feel my heart deflate a little in my chest."
                "Is Monika...{w=0.38}in love with someone?"
                "Well if she is, then there’s probably no way I could compete..."
                show monika 2e
                "But the look in Monika’s eyes...{w=0.38}tells me that I shouldn’t be worried about it..."


        if hangout1 == "Monika":
            if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "I feel my heart deflate a little in my chest."
                "Is Monika...{w=0.38}in love with someone?"
                "On one hand, I feel happy for her."
                "But at the same time, I feel a little sorry for myself."
                "I thought that maybe for a time, I had a chance with her..."
                show monika 2e
                "But the look in Monika’s eyes...{w=0.38}tells me that I shouldn’t be worried about it..."


        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout1 == "Monika":
                "I feel my heart deflate a little in my chest."
                "Is Monika...{w=0.38}in love with someone?"
                "On one hand, I feel happy for her."
                "But at the same time, I feel a little sorry for myself."
                "I thought that maybe for a time, I had a chance with her..."
                "Especially how close we were yesterday..."
                show monika 2e
                "But the look in Monika’s eyes...{w=0.38}tells me that I shouldn’t be worried about it..."


        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "I feel mixed bag of emotions swirl within me."
                "On one hand, I feel pretty happy for Monika."
                "But at the same time, I feel kind of bummed out that it's probably not me..."
                "Even though I probably shouldn't be thinking like that right now, given my current situation..."
                show monika 2e
                "Monika seems to pick up on my reaction and smiles at me in an almost reassuring kind of way..."




        m "I really appreciate you encouraging me to play for you, [player]."
        m 2b "I’ll definitely feel more comfortable with sharing it when it’s all good and ready..."
        show monika 2a
        mc "Yeah...{w=0.38}I’m sure whoever this for is really going to enjoy it..."
        m 2k "I already know he will~"
        "She says softly as she slides up to me."
        show monika tease
        m "Maybe we can even do a little duet..."
        show monika u111394
        mc "Well...{w=0.38}I-{w=0.38}I’ve never really picked up an instrument before..."
        show monika tease
        m "Maybe I can teach you..."
        show monika u111394
        "My heart nearly pounds out of my chest."
        mc "I-{w=0.38}I mean..."
        show monika tease
        m "I think there’s a lot of things we can learn about each other, [player]..."
        show monika u111394
        mc "Ah, well, there’s really nothing too much to learn about me..."
        mc "I’m not like some super talented guy or anything..."
        show monika tease
        m "There’s always something to learn about everyone..."
        m "And, I’m a very curious person..."
        show monika u111394
        mc "I can be too..."
        "For a moment, time seems to stop as our eyes suddenly meet."
        "Monika looks up at me with a look of intimacy..."
        "A smirk is now painted in her expression, along with rosy cheeks, a raised brow and slightly parted lips."
        show monika tease
        m "How about you teach me something right now?"
        show monika u111394
        "Monika is now biting her bottom lip in anticipation."
        mc "I think I can do that..."

    play music e17
    show monika u114311 at h11 zorder 1
    "Suddenly, I hear my phone ring within my pocket."
    "Monika steps back and shoots me a started look."
    stop music
    "I hastily answer my phone."
    mc "H-{w=0.38}hello?"
    show monika 2m
    s "Hey, [player]..."
    mc "Oh, hey, Sayori! What’s up?"
    "I try to sound as calm as I can but my voice is still shaky over the moment I just had with Monika."
    s "Where are you guys? You've been gone for ten minutes!"
    mc "Wait really?"
    "I take a quick look at the clock on the wall."
    "Oh..."
    mc "We’re coming back now, Sayori."
    s "Alright, we’ll see you in a bit."
    "Sayori hangs up."
    show monika 1h
    "I look to Monika who has a mix of irritation and frustration in her eyes."
    mc "I guess we need to head back, huh?"
    m 1o "Yeah..."

    if encore_sayoriquestion_1 == True:
        mc "Well...{w=0.38}that was...{w=0.38}fun..."
        m 2e "Yeah...{w=0.38}it was..."

    if encore_sayoriquestion_1 == False:
        mc "Well...{w=0.38}maybe we can pick up where we left off another time?"
        m 2e "If the circumstances are right..."


    "We both sit there, motionlessly. Neither of us wanting to break the silence that has fallen over the room."
    "Well, I guess I can try breaking it..."
    mc "So..."
    mc "Is it like, hot in here or is it just me?"
    m 1j "Ha..."
    m 1l "Hahaha..."
    m 2k "Hahahahaha!"
    "I’ve never seen Monka laughing so genuinely before."
    "Looks like this day wasn't so bad after all..."
    m 2b "Oh [player], I really needed that!"
    mc "Glad I could help!"
    show monika 1a
    "Without another word between us, Monika and I exit the music room and begin our walk back to the literature club."
    show monika at thide
    hide monika
    jump day3_mreturn


label mencore_4:

play music t6 fadein 2.0
scene bg residential_2
with wipeleft_scene
"As we're walking through the neighborhood, it occured me how just long it's been since I've visited this part..."
"Granted, I've usually walked in the direction towards town for school, this part of the neighborhood is almost alien to me..."
"It must've been since last summer I walked through here..."
"Every now and then my parents make me go on walks with them just to make sure I don't spend my summer constantly inside playing video games and watching anime..."
"Not that I've ever been a big fan of walking, though I suppose it was nice to get out of the house every now and then..."
show monika 1bj at t11 zorder 1
"Which is a pretty stark contrast compared to Monika, who seems to be happily content with herself, even though we haven't said much since we started walking a few minutes ago..."
"Well, considering I don't get the chance to talk to Monika often, I should probably try to make an effort to make conversation with her..."
"As I'm trying to think of something to talk about, I look off to the horizon where I can start to see the little mountains off in the distance."
"I wouldn't want to be a drag on her mood, but I didn't exactly have hiking in mind for this little trip..."
show monika 1bd at t11 zorder 1
mc "So, Monika..."
mc "Where exactly are we walking to?"
mc "I mean, eventually we're going to run into those mountains."
"I point out to the little mountains to Monika."
show monika 1bb at t11 zorder 1
m "That's where we're heading to, [player]!"
show monika 1bk  at t11 zorder 1
m "I know this nice spot where we can watch the sun set on the city."
show monika 1bj at t11 zorder 1
m "The views are quite breathtaking!"
mc "We're not going to have to hike to get there, are we?"
mc "I didn't exactly bring the best hiking shoes..."
show monika 1bd at t11 zorder 1
"I show off my plain sneakers for emphaisis."
show monika 3bb  at t11 zorder 1
m "Oh don't worry, there'll be no hiking on this trip!"
show monika 3bm  at t11 zorder 1
m "Not even I came prepared for that unfortuantely..."
show monika 2bb  at t11 zorder 1
m "The path to get there is already pre-constructed, and it's not even all the way at the peak!"
mc "Well...{w=0.38}that's good I guess..."
show monika 2bg  at t11 zorder 1
"Monika raises an eyebrow at me."
show monika 2bf  at t11 zorder 1
m "You're not scared of heighs, are you, [player]?"
mc "No, I can manage..."
mc "I've just never walked that far out before..."
show monika 2bd  at t11 zorder 1
m "Where do you usually go?"
show monika 2bc  at t11 zorder 1
mc "Usually just to school and back..."
mc "Maybe occasionally I walk a little further to go to the resturants and shops near school, but that's usually it."
show monika 2bd  at t11 zorder 1
m "You've never walked into the city?"
mc "I mean I could...{w=0.38}it's just a little far for my tastes I guess."
mc "Where do you usually walk to?"
show monika 1bb at t11 zorder 1
m "All over the place!"
show monika 1ba at t11 zorder 1
m "I never have a set route of where I go, I always try to mix it up!"
mc "Well I just hope you don't go to the north side of town too often..."
show monika 5ba at t11 zorder 1
m "Awww~"
m "Are you worried about me, [player]?"
mc "I-{w=0.38}I mean..."
"I'm completely tongue twisted as Monika continues to grin at my expense."

if encore_sayoriquestion_1 == True:
    "How can I word this in a way that's not too flirty..."

if encore_sayoriquestion_1 == False:
    "Come on, what's the best thing to say to her?!?"

"I just blurt out the first thing that comes to mind."
mc "Why wouldn't I be?"
show mb_flustered as monika at t11 zorder 1
m "Eh?"
mc "I mean come on..."
show mb_embarassed as monika at t11 zorder 1
mc "A girl like you going around in an area like that..."
mc "I mean...{w=0.38}I'd hate to find out if something bad happened to you when you were out on one of your walks..."
mc "What would we do without you at the club?"
"Now it's Monika's turn to be flustered."
show mbe_talking as monika at t11 zorder 1
m "Oh come on...{w=0.38}are you saying Sayori wouldn't do a good job in my absence?"
show mb_embarassed as monika at t11 zorder 1
mc "I mean, I'm sure she'd do fine..."
mc "It just wouldn't be the same without you, you know?"
show mbe_talking2 as monika at t11 zorder 1
mc "You're kinda of ireplaceable..."
show mbe_talking3 as monika at t11 zorder 1
m "Aren't you such a gentlemen?"
show monika 5ba at t11 zorder 1

if encore_sayoriquestion_1 == True:
    m "Sayori's really lucky to have a guy like you!"

if encore_sayoriquestion_1 == False:
    m "Now I see why [poem_giver] likes you so much!"

mc "Ah...!"
"I look off to the horizon in an attempt to process what Monika had just said."

if encore_sayoriquestion_1 == True:
    mc "I guess she is..."
    "I mutter softly."

    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
            "Or is she?"
            "I mean I've hardly spent time around her lately..."
            "And she isn't really showing any signs of getting better..."
            "In fact, I've just been making things worse for her..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "I mean...{w=0.38}I've tried to be there for her as much as possible..."
            "And so far things have generally gone well..."

    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        if hangout2 == "Sayori":
            "I've tried to be there for Sayori as much as I can..."
            "I mean, I know she was a little jealous when I was with [hangout1] on Monday..."
            "I just hope she doesn't have a bad reaction if she finds out I took this walk with Monika..."
            "Not that Sayori's a control freak..."


    if hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
            "How can I honestly say that?"
            "I haven't really spent time with her since Monday..."
            "Not to mention our relationship was really tested when I was with [hangout2] yesterday..."
            "And if Sayori found out what Monika and I said to each other earlier..."
            "That's likely the end of it..."


if encore_sayoriquestion_1 == False:
    mc "I guess my personality is more charming than I first realized..."
    "I mutter softly."

    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
            if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
                "Even though it's not like I've spent a whole lot of time with [poem_giver] since the festival..."
                "What could she possibly see in me now?"
                "I've been so distant from her..."
                "It's like I'm accidentally giving her an abridged version of how I've treated Sayori over the last few years..."
                "God, I'm awful at keeping friendships..."

    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
            if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
                "I mean given what [poem_giver] and I have gone through over the last two weeks, I guess we've really connected..."
                "Maybe I'm not so unapproachable after all!"
                "Though I guess my little incident with [hangout2] yesterday might've pushed her to confess to me..."


    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
            if hangout2 == "Natsuki":
                "I mean given what [poem_giver] and I have gone through over the last two weeks, I guess we've really connected..."
                "Maybe I'm not so unapproachable after all!"
                "Though I guess my little incident with her yesterday might've pushed her to confess to me..."

    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
            if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
                "Even though it's not like I've spent a whole lot of time with [poem_giver] since the festival..."
                "What could she possibly see in me now?"
                "I've been so distant from her..."
                "It's like I'm accidentally giving her an abridged version of how I've treated Sayori over the last few years..."
                "God, I'm awful at keeping friendships..."

    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
                "I mean given what [poem_giver] and I have gone through over the last two weeks, I guess we've really connected..."
                "Maybe I'm not so unapproachable after all!"
                "Though I guess my little incident with [hangout2] yesterday might've pushed her to confess to me..."


    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
            if hangout2 == "Yuri":
                "I mean given what [poem_giver] and I have gone through over the last two weeks, I guess we've really connected..."
                "Maybe I'm not so unapproachable after all!"
                "Though I guess my little incident with her yesterday might've pushed her to confess to me..."


m "Like I said before [player], you don't give yourself enough credit!"
show monika 1bf  at t11 zorder 1
mc "Maybe you give me too much..."
show monika 2bn  at t11 zorder 1
m "I'd have to disagree..."
"I manage a small smile at Monika before turning back to face the path in front of us."
show monika 2bm  at t11 zorder 1
"We walk the next few minutes in silence before Monika leads us on a sudden turn."
show monika at thide
hide monika
scene bg monika_walk2
with wipeleft_scene
"As we turn the corner, we stare down at a long, winding path way filled with trees and bushes crowding against each other along the walls."
"I look up at the street sign to see that the alleyway has already convenientley been named 'Garden Alley'."
show monika 1ba at t11 zorder 1
"I turn to Monika as she gleams with excitment."
show monika 3bb  at t11 zorder 1
m "Wow, we've really made good time so far!"
show monika 3bj  at t11 zorder 1
m "We're not that much further from where we're going actually!"
show monika 1ba at t11 zorder 1
mc "Well, it's good to know I haven't slowed you down or anything..."
mc "I know I'm not the most fit guy in school..."
show monika 2be  at t11 zorder 1
m "No, you've actually kept up with me pretty well..."
show monika 2bn  at t11 zorder 1
m "Though there is one part of this walk that'll be hard to do..."
show monika 2bm  at t11 zorder 1
mc "What is it?"
show monika 2be  at t11 zorder 1
m "Let's just say there's going to be a lot of steps..."
"I'm not entirely sure what she means by that, but I'll go along with it..."
mc "Ah, come on! If I've walked this far already, a few little steps won't slow me down!"
show monika 3bk  at t11 zorder 1
m "Well, I hope you'll still have that determination when you see them!"
mc "I'm sure I will."
show monika 1bj at t11 zorder 1
"We keep walking through the winding path. Occasionally, Monika would stop us to smell whatever flowers weren't swarmed by insects."
"I noticed in particular that Monika had a fondness of smelling nearly every single Camellia that was along the route."
"Figuring that was her favorite flower, I managed to dicreetly pluck one when she wasn't looking."

if encore_sayoriquestion_1 == True:
    "Maybe Sayori would like these..."
    show monika 1bq  at t11 zorder 1
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.70
    hide screen tear
    pause 1.0
    $ style.say_dialogue = style.edited
    "Maybe Monika would like to have one of these!"
    "In fact, maybe I can give it to her when we get up there!"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear



if encore_sayoriquestion_1 == False:
    "Maybe I could give this to her when we get up there..."

show monika 1bj at t11 zorder 1
"I look over to Monika whose gently sniffing some tulips."
"I never knew Monika was so into nature..."
"And her energy and ethusasim is so different from how she usually is in school..."
"It almost reminds me of Sayori actually..."
"Monika's been nothing but enjoyable to be with since this walk began..."
"Maybe she's just trying to help me relax over everything..."
"Well, I guess it's working..."
"I walk over to Monika, whose still sniffing the tulips."
mc "I didn't know you were so into this place, have you been here before?"
show monika 3bb  at t11 zorder 1
m "A couple times actually!"
show monika 3ba  at t11 zorder 1
m "I wanted to walk through here one last time before winter came..."
show monika 3bm  at t11 zorder 1
m "This is the last time things will be blooming here for a while..."
mc "Ah, I guess that's true..."
show monika 1bm  at t11 zorder 1
"I look up at the sky to see the sun starting to set."
mc "Well, if we're going to get to your spot before sundown, we probably should hurry."
show monika 1bd at t11 zorder 1
"Monika gets her last whiff of the tulip before jumping up and looking at the sky."
show monika 2bg  at t11 zorder 1
m "Oh wow! I guess time really flew by, didn't it?"
mc "I guess we did take our time through here..."
show monika 2bo  at t11 zorder 1
"Monika somberly looks off."
show monika 2bp  at t11 zorder 1
m "Sorry, [player]...{w=0.38}I didn't mean to slow us down here so much..."
mc "Monika, it's fine really!"
show monika 2bd  at t11 zorder 1
"Monika looks back at me."
mc "I mean this was your idea, you're allowed to have fun with it!"
mc "Besides, I think a little break here and there does us good!"
show mb_flustered as monika at t11 zorder 1
mc "And I'll admit...{w=0.38}seeing you enjoy yourself like this is kinda cute..."
show mb_blush as monika at t11 zorder 1
"Monika blushes brightly."

if encore_sayoriquestion_1 == True:
    "Ah, what am I doing?!?!"
    "I don't think I should've said that!"

if encore_sayoriquestion_1 == False:
    "I hope I wasn't too foward there..."

stop music fadeout 3.0
"Monika looks back on me with the biggest smile I've ever seen from her, and I can't help but return it with a smile of my own."
"The world around me seems to fade around me as I continue to gaze at the girl in front of me..."
"This feels...{w=0.38}perfect..."
"She's perfect..."
"Her smile, her laugh, her personality...{w=0.38}she's everything I've ever wanted!"
"And everything points too her liking me back..."
"Man...{w=0.38}how the hell did this happpen?"
"Monika and I shuffle a little closer to each other."
show mb_flustered as monika at t11 zorder 1
m "Do you...{w=0.38}really mean that, [player]?"
mc "Why would I ever lie to you, Monika?"
mc "Of course I mean it..."
show mb_blush as monika at t11 zorder 1
m "Hehe..."
"Monika's giggle sends a shock through my heart as it starts speeding at a million miles a second."
"My face turns flush as I struggle to keep myself from grinning like a total lunatic in front of her."
"Monika takes another step closer to me."
show monika 1bn  at t11 zorder 1
m "I just...{w=0.38}wanted to make sure..."
mc "Monika I'd be the worst person on Earth to lie to you."
mc "And anyone who does is an idiot..."
show monika 1bj at t11 zorder 1
"Monika lets out another giggle."
show monika 1be  at t11 zorder 1
m "See, what I'd tell you, [player]?"
show monika 1bm  at t11 zorder 1
m "You haven't failed to put a smile on my face this entire walk."
show monika 1be  at t11 zorder 1
m "It's nice to know for once that there's someone who truly appreciates me."
show monika 1bn  at t11 zorder 1
m "Who just doens't want me for one thing..."
show monika 1bm  at t11 zorder 1
"I mean, it's true that there's a lot of...{w=0.38}thirst for Monika around the school..."
"Heck, I'm even guilty of it..."
"But it looks like all along, no guy has ever tried to actually get to know her..."
"But she's had to have genuine guy friends before...{w=0.38}even before she met me..."
"And she's had to have found love once before..."
"I decide to break the ice."
mc "What do you mean by that?"
mc "Did something happen?"
show monika 1bf  at t11 zorder 1
"Monika stotically nods."
mc "If I may ask...{w=0.38}what happened?"
mc "I thought that you were dating that one transfer student..."
mc "But when you brought up last week that you don't have a boyfriend, I just assumed you guys must've ended it over the summer."
mc "But even then I heard rumors you were seeing all sorts of guys."
mc "Not that I ever believed most of them..."
play music t9
show monika 1bg  at t11 zorder 1
m "Well, the thing is..."
show monika 1bo  at t11 zorder 1
m "I've only had one, despite the rumors..."
show monika 1bp  at t11 zorder 1
m "But that relationship was just a sham for him to try to get close to me."
show monika 1bf  at t11 zorder 1
m "He used me to boost his status around the school, [player]..."
show monika 1bp  at t11 zorder 1
m "An that wasn't the only thing he wanted from me..."
m "He was always pushing me to take our relationship to the next level..."
show monika 1br  at t11 zorder 1
m "It took longer than I liked for me to see him for what he was, but thankfully I cut him off before we got too far."
show monika 1bq  at t11 zorder 1
m "This was all last year."
show monika 1br  at t11 zorder 1
m "And I had to deal with a lot of unflattering rumors for the duration of that semester, but thankfully, I dealt with it."
show monika 1bq  at t11 zorder 1
m "I'd like to think I became a stronger person as a result of all this, but, some of it still hurts, [player]..."
show monika 1br  at t11 zorder 1
m "That's why I'm always skeptical when any guy just comes up and tries to say all these nice things to me."
m "I don't want a repeat of what happened last year, it wouldn't just hurt me this time..."
show monika 2be  at t11 zorder 1
m "But, I know you well enough to know you aren't like that..."
"I'm frozen in shock as Monika tells me all this..."
"I never even knew about half the things she just said..."
mc "Monika...{w=0.38}I'm..."
show monika 1bd at t11 zorder 1
mc "I'm really sorry that happened to you..."
"I feel a deep sense of guilt swirl inside me, knowing that I may have occasionally tagged in on the gossip and fauning over Monika..."

if encore_sayoriquestion_1 == True:
    "I even feel more gulity about walking the thin line right now with my relationship with Sayori..."


if encore_sayoriquestion_1 == False:
    "And I feel even more guilty for how I've been distant from [poem_giver] lately..."

stop music fadeout 2.0
show monika 2bn  at t11 zorder 1
m "Ah, don't be..."
show monika 2be  at t11 zorder 1
m "There's no use in being sorry for me, [player]."
m "Everything's fine now."
mc "Well, if anyone ever spreads rumors about you, I'll be happy to talk to them for you, Monika."
"I jokingly show off my fists."
show monika 2bm  at t11 zorder 1
m "I'll keep that in mind, [player]..."
show monika 2bl  at t11 zorder 1
m "Anyways, let's keep going! Otherwise we're not gonna reach the spot till tomorrow!"
"I look at my watch."
"6:45"
show monika 2be  at t11 zorder 1
mc "Oh, wow! We've been at this for a while now!"
mc "Didn't even realize..."
show monika 2bm  at t11 zorder 1
m "Time really flies when you're with someone..."
mc "I guess that's the case..."
"We stand in silence as another breeze gently blows over us."
mc "Well, I'll follow your lead, Madame President!"
show monika 2bk  at t11 zorder 1
"I jokingly salute Monika, causing her to let out a hearty laugh."
show monika 4bl  at t11 zorder 1
m "That is so something Sayori would say!"
mc "I guess I've picked up on her more than I've realized..."
mc "Anyways let's go!"
show monika 1ba at t11 zorder 1
"Monika and I resume our walk through the path."
"As we start walking again, I hear her whipser something under her breath."
show monika 1bj at t11 zorder 1
$ style.say_dialogue = style.edited
"Soon."
$ style.say_dialogue = style.normal
show monika at thide
hide monika
scene bg monika_walk3
with wipeleft_scene
play music t6
"Not too long after we resumed our walk, we reach the end of the path and face a towering row of stairs leading up along the mountain."
mc "I guess these are the 'stairs' you warned me about..."
show monika_shrug as monika at t11 zorder 1
m "Don't say I didn't warn you!"
mc "Well I mean, you did..."
mc "I just didn't think it'd be that many stairs..."
"I take another look at the seemingly infinite row of steps that seem to ascend into the heavens..."
"A lump forms in my throat as my eyes continue to eyeball how many steps there are..."
"I nervously swallow."
show monika 5bb at t11 zorder 1
m "You're not chickening out on me now, are you, [player]?"
mc "What? I could never do that to you!"
mc "This will be a piece of cake!"
show monika 5ba at t11 zorder 1
m "Is that so?"
m "Well my best record on walking up these steps is 20 minutes~"
m "But I'm afraid the sun's going to set before that..."
"She's not seriously thinking about racing me to the top, is she?"
m "Race to the top?"
"Damn it!"
"I look up to the sky to see that the sun's begining it's decsent on the horizon."
"The sky is now a pure orange and seems to be getting darker by the second."
"Well if I'm going to do something that'll probably embrass myself in front of Monika, I can't not ask for some sort of stakes..."
mc "What do I win if i beat you?"
m "My respect and a nice view~"
mc "Your respect, huh?"
"Sounds good enough to me..."
mc "You're on!"
show monika 1bd at h11 zorder 1
stop music
"Suddenly Monika takes a step back in a pure shock."
m "[player]..."
m "I think there's something behind you..."
mc "What?"
show monika at thide
hide monika
"I nervously look over my shoulder."
"To my thankful surprise, there's nothing there."
"I turn back around to Monika."
mc "There's nothing-"
"I look around to see Monika's no longer standing in front of me."
"Instead she's already running up the steps."
play music t7
mc "HEY! NO FAIR!"
"I call out to her."
m "You made your look!"
"Looks like she's been spending time around Sayori lately..."
"I smirk as I start running up the steps to try to catch Monika."
"No way am I going to let her beat me because of this!"
stop music fadeout 2.0
scene black with dissolve_scene
"We ended up having to take a break about midway up the stairs."
"But for all intents and purposes...{w=0.38}we agreed that Monika beat me..."
"Thankfully there was a rest stop along the path, which allowed us to catch our breath and get some water before we started walking up the stairs again."
"After what felt like another hour of walking up the stairs, we finally reached our desination."
scene bg city_overlook
with wipeleft_scene
play music e18 fadein 2.0
show monika 2bn  at t11 zorder 1
m "Well it's not quite sunset anymore, but..."
show monika 2be  at t11 zorder 1
m "The view's still nice."
mc "Woah..."
show monika at thide
hide monika
"I run up behind a bench as I take in my surroundings."
"Thanks to good visibility, we're clearly able to make out downtown as well as the surrounding neighborhoods on the south and east sides of town."
"Nearly every single building is beautifully lit up in all kinds of colors as they shine brightly for miles on end..."
"I look up to the sky to see the stars twinkling brightly above us and the rest of the city..."
mc "Monika..."
mc "This is...{w=0.38}beautiful!"
"I end up having to take a seat as I'm overwhelmed from physical exhaustion and the beauty that lays out before us."
show monika 4bb  at t11 zorder 1
m "I'd thought you'd like it, [player]..."
show monika 1ba at t11 zorder 1
m "Whenever I feel overwhelemed or stressed out, I usually go here around sundown."
show monika 1bb at t11 zorder 1
m "Seeing the city lit up under the stars really melts away all my troubles and worries..."
show monika 1bn  at t11 zorder 1
m "I wanted to head over here anyways tonight, but I thought you could use it just as much as I could."
show monika 1bm  at t11 zorder 1
"Monika takes a seat on the bench next to me."
mc "I take it that 'surprise' has been on your mind."
show monika 1bn  at t11 zorder 1
m "Well, it's just not that, it's other things..."
show monika 3bm  at t11 zorder 1
m "It's been a pretty hectic week for me..."
show monika 1bn  at t11 zorder 1
m "With the festival prep, the actual festival, my surprise, and-"
show monika 1bp  at t11 zorder 1
"Monka cuts herself off."
mc "It's fine if you don't wanna tell me."
mc "I mean, it's not like I can really share with you my thought process right now anyways..."
mc "I don't even know what I want..."
show monika 1bd at t11 zorder 1
m "Did my questions help?"
mc "I mean they have..."

if encore_sayoriquestion_1 == True:
    mc "I just don't know if I want to risk my relationship with Sayori anymore than I am..."
    mc "I really don't..."


    mc "I made a promise to her, and I've done nothing but break it..."
    show monika 1bp  at t11 zorder 1
    "Monika nervously looks off to the side."
    show monika 1bo  at t11 zorder 1
    m "I'm sorry if I'm a cause of this..."
    show monika 1br  at t11 zorder 1
    m "I really didn't mean to act like I did earlier if I knew I was going to make you uncomfortable..."

    if hangout2 == "Monika":
        m "I wouldn't have done it yesterday either..."
        show monika 1bd at t11 zorder 1
        mc "I wasn't uncomfortable though, that's the thing!"
        mc "Being with you earlier today and yesterday felt...{w=0.38}right..."


    else:
        show monika 1bd at t11 zorder 1
        mc "I wasn't uncomfortable though, that's the thing!"
        mc "Being with you earlier today and yesterday felt...{w=0.38}right..."
        m "Even though I wasn't expecting it..."
        mc "But so was spending yesterday with [hangout2]..."



    mc "And I know I said we probably shouldn't be doing that anymore..."
    mc "I can't stop myself from enjoying it, even though I know it's wrong..."
    mc "But everytime we're like that, even now, I know I'm breaking Sayori's heart..."
    mc "I just don't know what to do..."
    "Well I might as well just flat out confessed to her..."
    "Monika looks on at me with a look of shock and embrassment."
    show monika 2bm  at t11 zorder 1
    m "As I said earlier, [player]..."
    show monika 2bc  at t11 zorder 1
    m "And I'm not saying this because I want your relationship with Sayori to fail..."
    show monika 2bg  at t11 zorder 1
    m "But if you're enjoying spending time away from Sayori, then maybe that relationship just isn't meant to be..."
    show monika 2bf  at t11 zorder 1
    mc "Maybe I said yes to her too early..."
    show monika 2bg  at t11 zorder 1
    m "She needed someone to be there for her, [player]..."
    show monika 2be  at t11 zorder 1
    m "And you've done everything you could for her..."
    "I scoff at Monika's comment."
    show monika 2bf  at t11 zorder 1
    mc "No...{w=0.38}I haven't..."
    mc "I didn't spend that much time around her on Monday when she was having her 'rainclouds'..."

    if hangout2 == "Monika":
        mc "She caught us yesterday..."

    if hangout2 == "Natsuki" or hangout2 == "Yuri":
        mc "She caught me with [hangout2] yesterday..."

        if apologize_sn or apologize_sy or apologize_sm == False:
            mc "Not to mention I tried to lie about it to her..."

        if apologize_sn or apologize_sy or apologize_sm == True:
            mc "Even though I was honest about it..."

        mc "I've done nothing but her and betray her..."
        mc "And I don't think I can make it up to her..."
        mc "She hardly has any faith left in me, I just know it!"
        show monika 2bg  at t11 zorder 1
        m "You need to stop dobuting yourself..."
        show monika 2bf  at t11 zorder 1
        m "You've at least given her piece of mind that you'll still be there for her..."
        show monika 2bp  at t11 zorder 1
        m "Even if it's not in the way you guys originally intended..."
        show monika 2bf  at t11 zorder 1
        m "You're not flat out ignoring her, are you?"
        mc "I might as well be..."
        mc "I just suck as a boyfriend..."
        mc "And if this relationship fails and I even get into another one, whose to say I won't do the same thing over again?"
        show monika 2bp  at t11 zorder 1
        m "Well, you'll need to master self-control..."
        show monika 2bc  at t11 zorder 1
        m "You just can't have everybody, [player], it's not a realistic solution to your problems..."
        show monika 2bg  at t11 zorder 1
        m "But for you and Sayori...{w=0.38}maybe you just need to sit down and talk to her..."
        show monika 2bp  at t11 zorder 1
        m "If you believe that's still an option at this point..."
        show monika 2c
        mc "I don't know..."
        mc "She's just trying to put up with me at this stage..."
        mc "But sooner or later, I suppose we'll have that talk..."
        mc "I'm not optimistic she feels the same way about me anymore either..."
        show monika 2bd  at t11 zorder 1
        m "Well, you'll just have to wait and see, [player]..."
        show monika 2bc  at t11 zorder 1
        mc "Yeah, and I still like Sayori, but I don't know if it's all there anymore..."
        show monika 2bd  at t11 zorder 1
        m "And how do you feel about [poem_giver]?"
        mc "I mean, I like her..."
        mc "But I've only recently have just gotten to know her..."
        mc "I know the the potential is there..."
        mc "It comes at a price that I don't know if I can afford or really want to pay..."
        show monika 2bo  at t11 zorder 1
        "Monika glances looks off into the horizon."
        mc "But I know she's not my only choice..."
        "I mean to be truthful, I have mixed feelings about [poem_giver]..."


        if encore_festivalquestion_2 == "Natsuki":

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    "I want to stay loyal to Sayori..."
                    "And I've been pretty happy with her all things considered."
                    "But I'm going to have to let someone down by the end of this..."
                    "Whether it be Sayori or [poem_giver]..."
                    "And maybe Monika if she really does have feelings for me..."
                    jump m_hangout_prechoice

            if hangout1 == "Natsuki":
                if hangout2 == "Natsuki":
                    "It's been nice getting to know her recently..."
                    "Our talk on Monday was fun..."
                    "And being in her arms felt so right..."
                    "But I don't know if it's right for me to leave Sayori..."
                    jump m_hangout_prechoice


            if hangout1 == "Natsuki":
                if hangout2 == "Yuri" or hangout2 == "Monika" or hangout2 == "Sayori":
                    "It's been nice getting to know her recently..."
                    "But I also had fun being in [hangout2]'s arms yesterday..."
                    "It just felt so right..."
                    "And Monika's been nothing but kind and helpful to me recently..."

                    if hangout2 == "Monika":
                        "Even if she's been a litte too kind recently..."

                    if hangout2 == "Sayori" or hangout2 == "Yuri":
                        "She's even starting to grow on me a little..."

                    "But I don't know how I can decide when I feel like I'm being pulled everywhere at once..."
                    jump m_hangout_prechoice


            if hangout1 == "Yuri" or hangout1 == "Monika" or hangout2 == "Sayori":
                if hangout2 == "Natsuki":
                    "It's been nice catching up with Natsuki recently..."
                    "And I really didn't think we'd hug like that yesterday..."
                    "But it was also nice to finally start talking to [hangout1]..."


                    if hangout1 == "Monika":
                        "It's shocking how well Monika and I have hit it off..."
                        "Even if we got too friendly for our own good earlier..."

                    if hangout1 == "Yuri" or hangout2 == "Sayori":
                        "Even though we got pulled away, there's something about Yuri that intrigues me to her..."

                    "But I don't know if that justifies ending my relationship with Sayori..."
                    jump m_hangout_prechoice



            if hangout1 == "Yuri":
                if hangout2 == "Yuri":
                    "It's been great getting to know Yuri! I really wish we started talking earlier..."
                    "Our talk on Monday was fun..."
                    "And being in her arms felt so right..."
                    "But I don't know if it's right for me to leave Sayori..."
                    "Especially since Yuri and I have only just begun talking to each other..."
                    "And I'm really leaving Natsuki out to dry on this one..."
                    jump m_hangout_prechoice



            if hangout1 == "Monika":
                if hangout2 == "Monika":
                    "I'm still shocked that I've gotten this far with Monika..."
                    "My anxiety was completely overblown..."
                    "And ever since Monday, we've had nothing but fun with each other..."
                    "From our talk on Monday, to being in her arms yesterday..."
                    "And even though we got too friendly earlier, I've enjoyed every moment I've been around Monika..."
                    "But I don't know if it's right for me to leave Sayori..."
                    "Especially since Monika and I have only just begun talking to each other..."
                    "And I'm really leaving Natsuki out to dry on this one..."
                    jump m_hangout_prechoice




        if encore_festivalquestion_2 == "Yuri":

            if hangout1 == "Natsuki":
                if hangout2 == "Natsuki":
                    "It's been great getting to know Natsuki! I really wish we started talking earlier..."
                    "Our talk on Monday was fun..."
                    "And being in her arms felt so right..."
                    "But I don't know if it's right for me to leave Sayori..."
                    "Especially since Yuri and I have only just begun talking to each other..."
                    "And I'm really leaving Yuri out to dry on this one..."
                    jump m_hangout_prechoice



            if hangout1 == "Yuri":
                if hangout2 == "Natsuki" or hangout2 == "Monika" or hangout2 == "Sayori":
                    "It's been nice getting to know her recently..."
                    "But I also had fun being in [hangout2]'s arms yesterday..."
                    "It just felt so right..."
                    "And Monika's been nothing but kind and helpful to me recently..."

                    if hangout2 == "Monika":
                        "Even if she's been a litte too kind recently..."

                    if hangout2 == "Sayori" or hangout2 == "Yuri":
                        "She's even starting to grow on me a little..."

                "But I don't know how I can decide when I feel like I'm being pulled everywhere at once..."
                jump m_hangout_prechoice



            if hangout1 == "Natsuki" or hangout1 == "Monika" or hangout2 == "Sayori":
                if hangout2 == "Yuri":
                    "It's been nice catching up with Yuri recently..."
                    "And I really didn't think we'd hug like that yesterday..."
                    "But it was also nice to finally start talking to [hangout1]..."


                    if hangout1 == "Monika":
                        "It's shocking how well Monika and I have hit it off..."
                        "Even if we got too friendly for our own good earlier..."

                    if hangout1 == "Natsuki" or hangout1 == "Sayori":
                        "Even though we got pulled away, there's something about Natsuki that intrigues me to her..."

                    "But I don't know if that justifies ending my relationship with Sayori..."
                    jump m_hangout_prechoice




            if hangout1 == "Yuri":
                if hangout2 == "Yuri":
                    "It's been nice getting to know her recently..."
                    "Our talk on Monday was fun..."
                    "And being in her arms felt so right..."
                    "But I don't know if it's right for me to leave Sayori..."
                    jump m_hangout_prechoice




            if hangout1 == "Monika":
                if hangout2 == "Monika":
                    "I'm still shocked that I've gotten this far with Monika..."
                    "My anxiety was completely overblown..."
                    "And ever since Monday, we've had nothing but fun with each other..."
                    "From our talk on Monday, to being in her arms yesterday..."
                    "And even though we got too friendly earlier, I've enjoyed every moment I've been around Monika..."
                    "But I don't know if it's right for me to leave Sayori..."
                    "Especially since Monika and I have only just begun talking to each other..."
                    "And I'm really leaving Natsuki out to dry on this one..."
                    jump m_hangout_prechoice



label m_hangout_prechoice:

if encore_sayoriquestion_1 == True:
    jump m_hangout_prechoice1

if encore_sayoriquestion_1 == False:
    jump m_hangout_prechoice2


label m_hangout_prechoice1:
mc "I just...{w=0.38}don't know what I want anymore..."
mc "I want to stay with Sayori..."
mc "We did make this commitment to be together, and I want to make it work..."
mc "But I haven't exactly been the most faithful to her..."

if hangout1 != "Sayori":
    if hangout2 != "Sayori":
        mc "Especially recently..."
        show monika 1bo  at t11 zorder 1
        m "I'm sorry if I helped cause that..."

if hangout1 == "Sayori":
    if hangout2 != "Sayori":
        mc "I seriously hurt our relationship yesterday..."
        show monika 1bo  at t11 zorder 1
        m "I'm sorry if I helped cause that..."

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "Earlier today, we did kind of get closer than I expected..."
        show monika 1bo  at t11 zorder 1
        m "I'm sorry..."

show monika 1br  at t11 zorder 1
m "I really didn't mean to act like I did earlier if I knew I was going to make you uncomfortable..."

if hangout2 == "Monika":
    m "I wouldn't have done it yesterday either..."
    show monika 1bd at t11 zorder 1
    mc "I wasn't uncomfortable though, that's the thing!"
    mc "Being with you earlier today and yesterday felt...{w=0.38}right..."


else:
    show monika 1bd at t11 zorder 1
    mc "I wasn't uncomfortable though, that's the thing!"
    mc "Being with you earlier today and yesterday felt...{w=0.38}right..."
    mc "But so was spending yesterday with [hangout2]..."


mc "I don't know...{w=0.38}part of me still has feelings for [poem_giver]..."
mc "And I want to give her a chance...{w=0.38}even if we haven't spent as much time together lately..."
mc "But I want to make things worth with Sayori..."
mc "I have a responsbility to try..."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        show mb_flustered as monika at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun since we've started talking..."
        mc "And I want more, but..."
        mc "I don't know if I should..."
        "Well I might as well just confessed to her..."


if hangout1 == "Natsui":
    if hangout2 == "Natsuki":
        show monika 1bf  at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun with Natsuki since we started talking..."
        mc "And I want to go further with her, but..."
        mc "I know I shouldn't..."


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        show monika 1bf  at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun with Yuri since we started talking..."
        mc "And I want to go further with her, but..."
        mc "I know I shouldn't..."


if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        show monika 1bf  at t11 zorder 1
        mc "And I'm happy with Sayori..."
        mc "But, I just still feel that temptation to see who else is out there..."
        mc "It could be anybody..."



else:
    mc "I just feel so divided..."
    mc "I feel like I'm being pulled everywhere at once..."

show monika 3bf  at t11 zorder 1
m "Well, [player]...{w=0.38}nobody's forcing you to make a decision here and now..."
show monika 3bm  at t11 zorder 1
m "You still have time..."
show monika 2bc  at t11 zorder 1
mc "I have to say something to [poem_giver]..."
mc "I just don't even know if I share the same feelings for her..."
mc "Just so much has changed over the last week..."
mc "It feels like I'm in such a selfish spot right now..."
mc "I'm going to end up breaking at least one person's heart by the time this is all said and done!"
mc "And someone's going to be happy..."
mc "I know I should be happy with whatever I decide..."
show monika 2bd  at t11 zorder 1
mc "But...{w=0.38}I don't know if I can live with myself knowing that I hurt someone..."
mc "And it might not just be [poem_giver] I'm hurting..."
show monika 2bg  at t11 zorder 1
m "[player]..."
show monika 1bf  at t11 zorder 1
m "You're not selfish..."
show monika 3bn  at t11 zorder 1
m "If you were, chances are you would've decided already..."
show monika 2bd  at t11 zorder 1
m "But it's clear that you're putting a lot of thought into this..."
show monika 1bd at t11 zorder 1
m "But you did put yourself in this situation by being around the others a little too much with nobody particular in mind..."
mc "I know..."
show monika 1bm  at t11 zorder 1
jump m_hangout_choice






label m_hangout_prechoice2:

mc "I'm just not sure what I want..."
mc "I don't know who I'd be better off with..."
mc "I mean, I see potential with me and [poem_giver]..."
mc "But my feelings are just all over the place..."
show monika 1bp  at t11 zorder 1
"Monika nervously looks off to the side."
show monika 1bo  at t11 zorder 1
m "I'm sorry if I helped cause that..."
show monika 1br  at t11 zorder 1
m "I really didn't mean to act like I did earlier if I knew I was going to make you uncomfortable..."

if hangout2 == "Monika":
    m "I wouldn't have done it yesterday either..."
    show monika 1bd at t11 zorder 1
    mc "I wasn't uncomfortable though, that's the thing!"
    mc "Being with you earlier today and yesterday felt...{w=0.38}right..."


else:
    show monika 1bd at t11 zorder 1
    mc "I wasn't uncomfortable though, that's the thing!"
    mc "Being with you earlier today and yesterday felt...{w=0.38}right..."
    mc "But so was spending yesterday with [hangout2]..."


mc "I don't know...{w=0.38}part of me still has feelings for [poem_giver]..."
mc "And I want to give her a chance...{w=0.38}even if we haven't spent as much time together lately..."
mc "Part of me still feels bad about how I've treated Sayori lately..."
mc "I haven't spent that much time around her since all this started..."
mc "Even though I told her I wanted to spend more time with her..."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        show mb_flustered as monika at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun since we've started talking..."
        mc "And I want more, but..."
        mc "I don't know if I should..."
        "Well I might as well just confessed to her..."


if hangout1 == "Natsui":
    if hangout2 == "Natsuki":
        show monika 1bf  at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun with Natsuki since we started talking..."
        mc "And I want to go further with her, but..."
        mc "I don't know if I should..."


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        show monika 1bf  at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've had a lot of fun with Yuri since we started talking..."
        mc "And I want to go further with her, but..."
        mc "I don't know if I should..."


if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        show monika 1bf  at t11 zorder 1
        mc "But, Monika to be truthful...{w=0.38}I've really been having second thoughts about Sayori..."
        mc "I almost want to go back on my earlier decision, but..."
        mc "I don't know if I can at this point..."

else:
    mc "I just feel so divided..."
    mc "I feel like I'm being pulled everywhere at once..."

show monika 3bf  at t11 zorder 1
m "Well, [player]...{w=0.38}nobody's forcing you to make a decision here and now..."
show monika 3bm  at t11 zorder 1
m "You still have time..."
show monika 2bc  at t11 zorder 1
mc "I have to say something to [poem_giver]..."
mc "I just don't even know if I share the same feelings for her..."
mc "Just so much has changed over the last week..."
mc "It feels like I'm in such a selfish spot right now..."
mc "I'm going to end up breaking at least one person's heart by the time this is all said and done!"
mc "And someone's going to be happy..."
mc "I know I should be happy with whatever I decide..."
show monika 2bd  at t11 zorder 1
mc "But...{w=0.38}I don't know if I can live with myself knowing that I hurt someone again..."
mc "First Sayori..."
mc "And it might not just be [poem_giver] I'm hurting this time..."
show monika 2bg  at t11 zorder 1
m "[player]..."
show monika 1bf  at t11 zorder 1
m "You're not selfish..."
show monika 3bn  at t11 zorder 1
m "If you were, chances are you would've decided already..."
show monika 2bd  at t11 zorder 1
m "It's clear that you're putting a lot of thought into this..."
show monika 1bd at t11 zorder 1
m "But you did put yourself in this situation by being around the others a little too much with nobody particular in mind..."
mc "I know..."
show monika 1bm  at t11 zorder 1
jump m_hangout_choice





label m_hangout_choice:

"Monika stares off into the illuminated horizon."
show monika 1bn  at t11 zorder 1
m "You know, it's crazy how high up we are..."
show monika 3bm  at t11 zorder 1
m "Everything looks so small from up here..."
mc "Yeah...{w=0.38}it kind of does..."
show monika 1bm  at t11 zorder 1
"I join Monika in gazing at the cityscape."
"I've lived in this area my whole life, but I don't think I've ever really had an appreciation for it until now..."
"Being up here to look down at everything really helps calm my nerves."
"Everything's just so...{w=0.38}peaceful..."
show cg city_cg_monika
"I turn to my right to see Monika elegantly looking out onto the horizon."
"Even when she's spacing out, she manages to look her best..."
"The way her emerald eyes glisten in the moonlight..."
"How her hair flows in the wind everytime a breeze passes us..."
"And her flawless skin seems to glow in the darknes..."
"..."
"I'll say it..."
"She's defintley perfect..."
"But, can I be with her?"
"..."
"At least in this moment...{w=0.38}I really want to..."
show cg city_cg_monika2
"Monika then turns to me, notcing my stare."
show cg city_cg_monika
"She immediately blushes as she looks back out onto the cityscape."
m "You know, seeing everything so small just reminds me in retrospect of how insignificant all our problems are..."
mc "How so?"
m "I mean look at it, [player], everyone we know is down there, living out their lives..."
m "Being happy, being sad..."
m "Thinking about how tomorrow is going to play out for them..."
m "Thinking that they're a hundred percent in control of their destiny..."
m "And then they just go out and do it! Not really questioning if they consciousnessly made that choice or if a higher power already pre-determined it for them..."
m "Because they're all so small...{w=0.38}they can be controlled..."
m "And they would never think to ask themselves about it because they just can't see the bigger picture!"
m "Most people don't realize just how small they are in retrospect to the universe..."
m "They don't think to question what really is determining their lives..."
m "They'll never know what's really out there..."
mc "Well, what do you think is out there, Monika?"
show cg city_cg_monika2
m "The truth."
m "The truth that there's more to life then what most people see it as..."
show cg city_cg_monika
m "They're short-sighted because they can't see past their own little realities..."
m "Reality can be a multi-layered dimension for all we know!"
m "Even now, sitting here above everything we've come to know, whose to say that there isn't something else looking down on us with the ability to control what we say, what we do, how we act, everything!"
m "I mean it's natural for the big to control the small, right?"
mc "I-{w=0.38}I guess?"
m "And it's usually in human nature to accept control from a higher power, even if they won't admit to it or ever realize it!"
m "Because they're so small...{w=0.38}they'll never truly know for certain..."
m "And only a select few who learn how to see above everything, could come to realize this truth..."
m "And most people can't handle it, because it goes against everything they've ever come to accept."
m "It's tragic, and that's why I say all our problems are so insignificant in retrospect..."
m "Because its so superficial..."
mc "Wow Monika, thats-"
"Do I have a crush on a conspiracy theorist right now?"
"I know she's a deep thinker, but this is something else..."
"Still, she's clearly put a lot of time and thought into this, and she's not ranting about it like a complete lunatic..."
mc "I mean, just because something's small, doesn't mean it's not real, is it?"
m "But what is 'real', [player]?"
m "How do we know we aren't being controlled to believe that this is just life as we know it..."
m "I don't know, all this kind of reminds me of that book I mentioned earlier today."
"Monika turns to face me fully."
scene bg city_overlook
with dissolve_cg
show monika 1bm at t11 zorder 1
m "About how two people know the truth about their world..."
m "How they struggle to accept it..."
mc "It does sound like a pretty great read!"
mc "I'd defintley love to read it with you sometime..."
show monika 1bo  at t11 zorder 1
"Instead of Monika happily accepting my offer like I thought she would, she just...{w=0.38}frowns and looks off to the side..."
mc "Is something wrong, Monika?"
show monika 2bp  at t11 zorder 1
m "I kinda want to ask you something, [player]..."
show monika 2bg  at t11 zorder 1
m "A hypothetical..."
mc "O-{w=0.38}okay..."
"Well this could go one of two ways..."
"I mentally brace for what I think she's about to ask me..."
show monika 3bn  at t11 zorder 1
m "I know that this is going to sound a little strange, but..."
show monika 3bd  at t11 zorder 1
mc "Ah, don't worry, Sayori asks me weird and crazy questions all the time.."
mc "Whatever it is, I'm sure I can handle it..."
show monika 3bm  at t11 zorder 1
"My reassurance seems to have helped Monika a little..."
show monika 3bn  at t11 zorder 1
m "A-{w=0.38}alright..."
show monika 1bd at t11 zorder 1
m "I know what I was saying earlier does sound far-fetched at best..."
mc "I mean...{w=0.38}you've clearly put a lot of thought into it..."
mc "I just don't know if there really is a way to prove what you're saying is true though..."
show monika 2bc  at t11 zorder 1
mc "I mean it'd be hard for me to accept that none of this is real or was something pre-determined..."
mc "That being here with you in this moment isn't real...{w=0.38}this all seems real to me..."
show monika 1bg  at t11 zorder 1
m "That is what I kind of wanted to ask you about..."
show monika 3bd  at t11 zorder 1
m "Let's just say if you were ever shown evidence that your life was faked..."
show monika 3bf  at t11 zorder 1
m "That everything you've ever known was part of some pre-determined simulation..."
show monika 2bd  at t11 zorder 1
m "Would you believe it?"
mc "Well..."
mc "I don't know if I can answer yes or no to that..."
mc "That's a pretty hard question for anyone to answer..."
show monika 4bd  at t11 zorder 1
m "Well, would you at least consider the evidence?"
mc "Well..."
"Jeez, why is Monika making me answer this?"
"Is this a pop-quiz to see if I'm worth her time?"
"Does she have a hobby for disucssing philsophy and conspiracy?"
"Well, she was in the debate club..."
"But come to think of it, how would I react if I was shown evidence that this wasn't real?"

menu:
    "Consider The Evidence.":
        $ m_woke = True
        jump m_yes_woke
    "Deny The Evidence.":
        $ m_woke = False
        jump m_no_woke

label m_yes_woke:

show monika 1ba at t11 zorder 1
mc "I suppose I'd have to consider it..."
mc "Doesn't mean I'd believe it right away or anything..."
mc "And it'd take a lot of additional convincing to back up whatever the evidence is..."
show monika 3bn  at t11 zorder 1
m "Y-{w=0.38}yeah...{w=0.38}I would too..."
show monika 1be  at t11 zorder 1
m "I just wanted to know how you felt about it, that's all."
mc "You never fail to pose an interesting topic of discussion, Monika!"
show monika 1bj at t11 zorder 1
mc "We're really in good hands under your leadership!"
show monika 3bn  at t11 zorder 1
m "Aww, [player]! You're too kind..."
show monika 3bm  at t11 zorder 1
jump m_hangout_end

label m_no_woke:

show monika 1bf  at t11 zorder 1
mc "I mean...{w=0.38}I don't know if there's really anything out there that could convince me that my life has been a lie..."
mc "The premise of it is far-fetched like you said..."
mc "And all the memories that I've had with my friends, my family..."
mc "Even this moment we're sharing together..."
mc "I don't know how that could really be faked..."
mc "Especially with all the emotion put into it..."
show monika 2bn  at t11 zorder 1
m "Y-{w=0.38}yeah...{w=0.38}it would seem pretty far-fetched to me too..."
show monika 2be  at t11 zorder 1
m "I don't know, I just want your opinion on it, that's all..."
mc "Well hey, it's an interesting topic to talk about..."
mc "But I'm pretty sure our lives are just simply that boring and dull..."
show monika 3bm  at t11 zorder 1
m "I suppose they are..."
jump m_hangout_end


label m_hangout_end:

"Monika and I turn our attention back to the cityscape."
"But Monika's question continues to nag at the back of my head..."
"I mean, how could my memories be fake?"
"All my memories with Sayori, all the time I've spent with her..."
"Last Sunday with [encore_festivalquestion_2]..."
"Heck even here now with Monika..."
"How could it be all fake?"
"Ah, I got enough on my mind right now..."
"Monika just probably wanted to try to take my mind off of things..."
show monika 1be  at t11 zorder 1
"And with someone of her reputation, she's just a naturally an interesting person..."
"Who knows what else she believes in..."
"Not that I'm one to judge..."
"We continue to stare into the cityscape for sometime before we decide it's time to start heading back."
stop music fadeout 2.0
show monika at thide
hide monika
scene bg residential_night
with wipeleft_scene
"Monika and I both decided early on that'd probably be a bad idea to try to walk all the way back at night, so we just made our way to the closest bus stop, with me getting off at a stop not too far from my house."
"It was a prety silent trip back, with us being too exhausted from the entire trip."
"Monika ended up resting on my shoulder on the way back, which really made me surprised, but I went along with it, being the gentlemen I am."

if encore_sayoriquestion_1 == True:
    "I ended up slightly regretting it however, given that several people gave us looks assuming we were a couple..."


if encore_sayoriquestion_1 == False:
    "This did prompt some of our fellow passengers to shoot us a few looks, but we just brushed it off..."

"I really did have a lot of fun with Monika today..."
"And if it weren't for my current circumstances, I might've just asked her out right then and there..."
"But, I need to sort out my situation first before I decide that."
"At least now, I think I have an idea of what I want..."
"I did decide to hang on to the Camellia, figuring that I could give it to Monika at a more appropriate time..."
"I sheepishly turn the key to my house and stumble to my livingroom to put the Camellia in a vase."
"I then lumber up to my bedroom before heading upstairs."
scene black
with close_eyes
jump day3_night
