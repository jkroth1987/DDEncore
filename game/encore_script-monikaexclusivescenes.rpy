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
    m 2n "Oh...{w=0.38} yeah...{w=0.38} sorry, I got kind of carried away there, didn't I?"
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
    "Instead, she’s looking down at her ipod and humming a tune to herself."
    "Intrigued, I carefully approach her, not wanting to startle her."
    mc "Hey, Monika."
    show monika 1d at h11 zorder 1
    "She quickly looks up at me, popping out one of her AirPods."
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
    show monika 5a
    "Monika grins at me."
    show monika smirk
    m "I just strive to be the best I can be."
    mc "Well you’re definitely succeeding..."
    m 1m "Well if that’s the case, maybe I can show you what I’ve been working on."
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
    #Possible Sample Music
    mc "Huh, that was actually pretty good!"
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
    m 1b "Well, here we are!"
    show monika 1a
    "Monka stops in front of the band room."
    mc "Huh, so this is the band room?"
    m 1d "You’ve never been inside before?"
    mc "Can’t say I have."
    m 1k "Well this definitely going to be a special day for you, [player]~"
    "Monika opens the door and flicks on the lights as we enter the band room."
    show monika at thide
    hide monika
    scene bg club_day
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
    show monika 1m
    "She quietly makes her way towards the piano and sits down."
    "I pull up a chair and sit right across from Monika."
    "She takes a deep breath as her fingers hover over the keys as she looks on at me."
    mc "You got this, Monika!"
    "Monika lets out a small laugh."
    m 1l "Thanks, [player]!"
    show monika 1r
    "Monika cracks her knuckles, letting out one more breath before positioning her fingers above the keys."
    "A split second later, she begins playing."
    "I can’t help but notice how elegantly her fingers grace the keys."
    "The melody is calm, but purposeful. Every action with intent, and care...{w=0.38}it's almost hypnotizing!"
    "Unexpectedly, Monika starts to sing."
    m "Every day, I imagine a future where I can be with you..."
    m "In my hand, is a pen that will write a poem for me and you..."
    "Not even ten seconds in and I’m already blown away..."
    "Her voice is almost angelic as her emerald green eyes light up with a fiery passion I've never seen before..."
    m "The ink flows down into a dark puddle...{w=0.38}just move your hand..."
    m "Write the way into his heart!"
    "Monika takes a brief look over at me, smiling before she goes back to focusing on the piano."
    m "But in this world of infinite choices...what would it take just to find that special day?"
    m "What will it take...{w=0.38}just to find...{w=0.38}that special day!"
    "Monika suddenly stops playing and turns to face me."
    show monika 2m
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
    "I feel my heart deflate a little in my chest."
    "Is Monika...{w=0.38}in love with someone?"
    "Well if she is, then there’s probably no way I could compete..."
    show monika 2e
    "But the look in Monika’s eyes...{w=0.38}tells me that I shouldn’t be worried about it..."
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
    show monika u114311 at h11 zorder 1
    "Suddenly, I hear my phone ring within my pocket."
    "Monika steps back and shoots me a started look."
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
    m 2b "Oh [player], I really needed that."
    mc "Glad I could help!"
    show monika 1a
    "Without another word between us, Monika and I exit the music room and begin our walk back to the literature club."
    show monika at thide
    hide monika
    jump day3_mreturn
