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

    m 5a "Afterall, you guys are like two peas in a pod over there."
    "Monika says teasingly."

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == False:
                "Wait...{w=0.28} does Monika really think that Natsuki and I are {i}that close{\i}?"
                "I mean we’re just friends, but…"

    if encore_festivalquestion_2 == "Natsuki":
            if encore_sayoriquestion_1 == True:
                "I mean Sayori and I may be dating, but that doesn't mean I can't spend my time around the other girls...{w=0.38} right?"

    if encore_festivalquestion_2 == "Yuri":
            if encore_sayoriquestion_1 == False:
                "Wait...{w=0.28} does Monika really think that Yuri and I are {i}that close{\i}?"
                "I mean we’re just friends, but…"

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
    mc "You seemed to have had a hard time earlier..."
    show monika u114311
    "Monika suddenly realises how excitable she's become and recomposes herself."
    m 2n "Oh...{w=0.38} yeah...{w=0.38} sorry, I got kind of carried where there, didn't I?"
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
    mc "Can't wait to see what you wrote too!"
    show monika 1j
    "Monika lets out a cute giggle."
    "Natsuki shoots us a suspicious look."
    show natsuki 5e at t33 zorder 1
    n "Are you two going to stand there and flirt all day, or you going to share your poems with us?"
    m 1l "Right, right...{w=0.28} sorry!"
    show natsuki at thide
    hide natsuki
    m 1a "See you in a bit, [player]!"
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
    $ hangout = "Monika"
    "I decided to see what Monika is up to."
    scene bg club_day
    with wipeleft_scene
    play music e2
    "Monika's in her usual spot at the front of the room."
    mc "Hey, Monika!"
    show monika 1d at h11 zorder 1
    pause 0.8
    show monika 1j
    "Monika tilts her head up to see who called her, but she instantly smiles once she sees that it's me."
    m 2k "[player]! What's up?"
    mc "Oh, not much. Just wanted to see how our club president was doing today."
    "Monika manages a small giggle."
    m 5a "I really am lucky to get all this attention from you, aren't I?"
    "I don't really know what she means by \"lucky\".{w=0.8}{nw}"
    show monika 1d
    "I don't really know what she means by \"lucky\".{fast} She has every guy in the school head over heels for her."
    show monika 1f
    "I don't understand how I'm any different."
    show monika 1e
    "That being said, as long as Monika enjoys my company, it can't be a bad thing."
    mc "Well...I like talking to you."
    m 2b "That's good! I'm glad you don't find me unapproachable or anything like that."
    mc "What do you mean by that?"
    m 2l "Oh, nevermind."
    "Monika glances down to the paper she was working on."
    mc "I mean I wouldn't want to stop you from working on something important so-"
    m 2k "Oh no, it's fine [player], really! I actually just finished this."
    "I see a smile start to form across Monika's face."
    mc "Was it schoolwork?"
    m 2b "Actually, no. It was just a poem I made for fun."
    m 4b "Want to read it?"
    mc "Sure!"
    m 4k "I hope you like it [player]."
    call showpoem(poem_m_connection, music=False, revert_music=False, img="monika 1a")
    #show monika 1a
    "Something about the way that this is written catches me off guard."
    "I mean, it's a fantastic poem, but a lot of the poem says the some of the same things as that weird voice did in my dream last night."
    "It's probably just a coincidence though..."
    m 1b "So, what do you think?"
    mc "It's great Monika! I think this is your best one yet!"
    show monika 1j
    mc "I really like the way you make it flow and it is has a pretty good ending."
    "I hand her back her poem."
    m 1k "Glad you liked it [player]! I spent a lot of time on it, so I'm glad it all paid off!"
    mc "Monika everything you do pays off in the end."
    show monika 1d
    "Monika looks at me with an intrigued look on her face."
    mc "You're smart, you're friendly, you're talented, you're beautiful..."
    m u112332 "Oh come on [player]..."
    mc "Eh?"
    m u121351 "You're just buttering me up, aren't you?"
    "Monika eyes take a suggestive tone."
    show monika u111394
    "She stands up abruptly, surprising me at the same time."
    "Monika leans into me in an almost seductive manner."
    "At this point a 'breach of personal space' is an understatement."
    mc "Well...maybe a little...I did like your poem though, honest!"
    show monika u121331 at f11
    stop music fadeout 2.0
    "I'm stuttering my words at this point as I feel Monika's breath brush across my face."
    m 1d "Hmmm..."
    "Monika's eyes scan me up and down."
    m 1j "You know [player], you really should straighten out your tie."
    m 1k "It's important to me that all my club members look as professional as possible."
    mc "Uh yeah...you're t-totally right."
    "Monika suddenly grabs onto my tie as if holding on for dear life."
    play music t9 fadein 2.5
    show cg m_cg_1 zorder 10 with dissolve_cg
    #m u122331 "Here...let me fix it for you."
    m "Here...let me fix it for you."
    #show monika u121331
    hide monika
    "Her voice is but a whisper at this point."
    "I can't help but stare into her eyes as she looks up to me."
    "I never thought the color emerald could be so beautiful!"
    "Monika's lips are slightly parted and I can feel her warm breaths now graze against my neck."
    "This feels..."
    "Good..."
    "Never in a million years would I ever thought that I would've found myself this close to someone like Monika."
    "In fact... I never thought I'd be this close to Monika period!"
    "Speaking of finding..."
    "I briefly look around the room."
    "There's no way that they haven't at least looked up once and saw us like this, or overheard what we were saying, since we weren't really being that quiet to begin with."
    #show monika at thide
    #hide monika
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
    stop music fadeout 2
    "Words truly cannot describe what looks back at me.."
    play music t9
    "Everything about her is...perfect."
    show monika u111311
    "Her piercing emerald eyes leave me breathless."
    "Her hair flows in the nonexistent wind."
    "Her warmth flows off of her body and comforts me like the sun on a cloudy day."
    "It's as if all of my natural senses are being bombarded by the figure standing in front of me."
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
    m 1l "You know [player], if you're always going to look this messy."
    m u121351 "Maybe I should help you look nice in the morning"
    "Monika puts her hand on my cheek as she intensely looks me in the eyes."
    "I can't tell if Monika is just teasing me or is actually being serious here."
    mc "Oh! Um...."
    "How do I respond to something like that?"
    "My mind completely goes blank in this situation."
    "I don't even know what I'm doing anymore."
    show monika u111394
    "My hands are now rested on her hips, and Monika has the look on her face."
    "My heart is pounding at a million miles a second."
    "I feel my palms become sweaty and my knees become really heavy..."
    "Is this my chance?"
    "My chance to be with the Monika?"
    show monika u114341
    "I see Monika slowly lean in to me as I slowly do the same..."
    show black zorder 10 with Dissolve(0.5)
    "..."
    stop music fadeout 1.0
    "Suddenly, I hear Sayori get up."
    #show monika at thide
    #hide monika with wipeleft
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
    "Monika and I are practically hugging each other with our faces barely apart."
    show natsuki 5g
    show sayori 1i
    show yuri u123114
    "All 3 girls are looking at us, with a bit of an irritated...almost jealous...expression on their faces."
    "God Damn It."
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
    "I can't blame her though."
    show monika 1d
    mc "Well Monika...um...thanks for the...advice!"
    mc "It was very inspiring."
    "Monika quickly catches on to what i'm saying."
    m 2b "Well [player], you can come to me anytime."
    show monika u111151
    "Monika gives me a wink."
    "I can't help but manage a smile to Monika."
    show monika at thide
    hide monika
    "I feel all the blood rush to my face as I turn around to face the others."
    "None of the others make eye contact with me as they go to join us at the front of the room."
    if encore_festivalquestion_2 == "Natsuki":
        show natsuki 4g at t11 zorder 1
        play sound "sfx/smack.ogg"
        "While on the way to the front of the room. Natsuki gives me a \"friendly\" punch in the arm."
        mc "Ouch! Hey what was that for?"
        n 5s "N-Nothing...dummy..."
        "She mutters that softly and avoids eye contact as she briskly walks past me."
        show natsuki at thide
        hide natsuki
        "Well, that was random."
        "I just hope she isn't jealous of me and Monika getting so close like that."
        if encore_sayoriquestion_1:
            "I'm just hopeful she's able to put two and two together now so it saves me the awkwardness of eventually telling her that Sayori and I are a couple."
            "Hopefully then, she won't full on put me in the hospital."
        "Oh well."
    else:
        "Yuri needs a scene here too."
    jump day2_meettheclubs
