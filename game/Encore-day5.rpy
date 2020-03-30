#############
#   DAY 5   #
#############
label day5_start:

scene bg bedroom
with open_eyes
$ day = 2
$ s_name = "Sayori"
$ m_name = "Monika"
$ n_name = "Natsuki"
$ y_name = "Yuri"
"I slowly open my eyes, expecting the same rush of pain to hit me like a freight train."
"Unexpectedly, as I lay in bed waiting for the inevitable, I feel fine."
"Aside from this feeling of dread..."
"I peek over my shoulder to look at my alarm."
"Well, I don't have to get up for about half an hour..."
"But, maybe it's best I get ready early for once..."
"This is going to be a long day..."
"I slowly crawl out of bed, still wary that a sudden rush of pain could come at me at anytime, and prepare for the day."
scene bg kitchen
with wipeleft_scene
"As I drag myself through my morning routine, my mind races through all the possible scenarios for what can happen in the club today."
"We've been able to get through Natsuki and Yuri's fights, but they look more like scuffles compared to yesterday..."
"It's something the club's never gone through..."
"But, maybe it was bound to happen at some point."
"Four different girls...{w=0.38}with such different personalities..."
"Throw a guy like me into the mix, and it's a recipie for drama..."
"Well, I guess I got what I asked for..."
"But...{w=0.38}was it worth it?"
"..."
"The thought continues to plague me as I finish my breakfast."
"As I'm putting the dishes away, another thought creeps into my mind..."

if hangout3 == "Monika":
    "Monika..."

    if m_makeup == True:
        "How're things going to go down with her?"
        "I'm sure that Monika can smooth things over with [poem_giver], but..."
        "Are things really going to be the same after today?"
        "I don't think Monika's the type of person who can just forgive a person for hitting her like that..."
        "But, it's been a strange few days. Who knows what will happen..."
        jump day5_swalk


    if m_makeup == False:
        "How's she going to react when she sees me?"
        "I really wish we got to talk about what happened..."
        "Even though what she said to [poem_giver] was awful, I can't entirely pin the blame on her."
        "It's ultimately my fault everything happened..."
        "And Monika probably thinks I'm blaming it all on her."
        "Well, maybe we'll get to smooth things over in the club."
        "There's certainly going to be plenty to talk about..."
        jump day5_swalk

if hangout3 == "Sayori":
    "Sayori..."

    if s_makeup == True:

        if poem_giver == "Natsuki":
            "I know she said she's going to make things up with Yuri after what she said, but can she?"
            "Will Yuri even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Natsuki?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Natsuki and the others to back off and respect our relationship."
                jump day5_swalk

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Natsuki?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk



        if poem_giver == "Yuri":
            "I know she said she's going to make things up with Natsuki after what she said, but can she?"
            "Will Natsuki even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Yuri?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Yuri and the others to back off and respect our relationship."
                jump day5_swalk

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Yuri?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk



    if s_makeup == False:

        if n_love == True or y_love == True:
            "I really should've talked to her yesterday..."
            "Now it feels like I'm walking into this whole thing blind!"
            "Then again, I'm about to meet her in a few minutes..."
            "Maybe we'll talk about everything then..."
            "If she's better that this..."
            jump day5_swalk



        else:
            "I dobut she even wants to talk to me right now, let alone see me!"
            "I should've taken her up on the chance to talk things through..."
            "Who knows what kind of state of mind she's in?"
            "Well, hopefully she's feeling better about everything now..."
            "I just hope I didn't struck too bad of a nerve..."
            jump day5_swalk


if hangout3 == "Natsuki":
    "Natsuki..."

    if n_makeup == True:
        "Can I really expect her to make up with Yuri after what happened?"
        "I mean, they've fought before, but not like this..."
        "And it seems like everyone's pissed off at each other for something..."
        "Then again, Natsuki has surprised me with what she can do when she steps up..."
        "Let's just hope she can do it again..."
        "Maybe I can talk to her before the club..."
        "And I still need to talk to Sayori about what happened..."
        "Hopefully she's still willing to talk to me..."
        jump day5_swalk

    if n_makeup == False:
        "I really should've talked things through with her yesterday..."
        "She probably thinks I either hate her or I'm pinning all this on her..."
        "On the other hand, maybe she's cooled off..."
        "I know I can't run from her forever."
        "Maybe I'll get to talk to her before the club today."
        "There's definitely a lot to talk about..."
        "And I need to talk to Sayori too..."
        "Well, she should be waiting outside for me..."
        jump day5_swalk



if hangout3 == "Yuri":
    "Yuri..."

    if y_makeup == True:
        "Is she really going to go out of her way to make peace with Natsuki?"
        "They've had some nasty fights, but nothing of this caliber..."
        "It's just a tense situation all around...{w=0.38}everyone's mad at each other for something..."
        "And Yuri...{w=0.38}well, she doesn't have the best social skills..."
        "Not like mine are any better, considering I started all this..."
        "Well, Yuri's surprised me before, I'm sure she'll do it again."
        "Hopefully I can talk to her before the club starts..."
        "This might be poor timing, but I need to know for sure what's up with Yuri's 'secret'..."
        "Speaking of poor timing, I need to meet Sayori..."
        "Heaven knows we have a lot to talk about as well..."
        jump day5_swalk


    if y_makeup == False:
        "I really should've sat down with her yesterday..."
        "Who knows how she's handling all this..."
        "And if my suspicions about her cutting are right, this could be more dangerous than I thought..."
        "Maybe I can find out for sure later, even if the timing is pretty bad..."
        "It's not like I'm left with too many choices..."
        "Speaking of something else I can't avoid, I know I'm going to run into Sayori later as well..."
        "She's probably waiting outside for me right now, assuming she isn't completely done with me..."
        "Maybe I can turn all this around..."
        "Maybe there is a way to fix everything for good..."
        jump day5_swalk



label day5_swalk:

"I finish putting the dishes away, grab my backpack, and headout to meet Sayori."
scene bg residential_day
with wipeleft_scene



if s_makeup == True:
    "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
    jump sd5_1



if s_makeup == False:


    if encore_sayoriquestion_1 == True:

        if n_love == True or y_love == True:
            "I walk out the front door and look around to see that Sayori is no where to be seen."
            "As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
            jump sd5_2


        if n_love == False or y_love == False:
            "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
            jump sd5_1


    if encore_sayoriquestion_1 == False:

        if n_love == True or y_love == True:
            "I walk out the front door and look around to see that Sayori is no where to be seen."
            "As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
            jump sd5_2


        if n_love == False or y_love == False:
            "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
            jump sd5_1



label sd5_1:

show sayori 1d at t11 zorder 1
mc "Hey, Sayori..."
s 1k "Hello, [player]..."
"Sayori's voice drifts off into a whisper as she anxiously stares in the direction of school."
"I can't say I blame her..."

if s_makeup == True:
    "Neither of us were really looking forward to today..."
    "I decide to speak up as a way to try to motivate us."
    show sayori 1g
    mc "Well, we knew this was coming."
    mc "We're going to have to go back and face them..."
    s 1k "Yeah..."
    s 1l "You know, I've never really been one for conflict..."
    s 1k "I always hated it."
    s 1h "It's so mean and nasty..."
    s 1k "And I hate seeing everyone act like that."
    mc "I know you do..."
    mc "But, going back is our only way to fix this..."
    show sayori 1f
    mc "Maybe..."
    s 1h "[player]..."
    s 1g "Look..."
    "Sayori brushes up against me and takes my hand in her's."
    s 2h "If for whaetever reason things don't work out, it's fine..."
    s 2k "I'd hate to lose them as friends, but..."
    s 2t "I'll always have you..."

    if encore_sayoriquestion_1 == True:
        s "I'm glad that I'm you're girlfriend..."

    if encore_sayoriquestion_1 == False:
        s "I'm glad that you're my friend..."

    s 2l "Even though we've had our up's and down's, in the end, I think everything's going to be okay."
    s 2d "Your real friends are the ones who stick by you in the end..."
    s 2t "Like how you're here for me now, always taking care of me..."
    mc "I just know I could've done a better job, Sayori..."
    mc "This is all my fault."
    s 2k "I bare some responsbility too, [player]..."
    s 2h "They clearly have a misunderstanding with me, and well, I need to sort it out."
    mc "We're really doing this together then, huh?"
    s 2q "Yep!"
    mc "I guess I wouldn't have it any other way."
    show sayori 1d
    "Sayori realses my hand and glances up at me with a hopeful, optimistic look in her eyes I haven't seen before..."
    "Leave it to her to end up doing the inspriring for me..."
    "Well, let's put this energy to good use."
    "After a brief nod to each other, we begin our walk to school, ready to face down whatever might come our way..."
    show sayori at thide
    hide sayori
    jump day5_school1



if s_makeup == False:
    "She's probably barely able to stomach being in my presence..."
    "I...{w=0.38}I need to apologize..."
    show sayori 1g
    mc "Sayori..."
    show sayori 1f
    mc "I'm sorry."
    show sayori 1k
    mc "I'm sorry that I've been treating you so badly."
    show sayori 2u
    mc "I know you probably don't believe a word coming out of my mouth, and that's fine."
    mc "I don't deserve your forgiveness..."
    mc "But...{w=0.38}just know that I feel bad that this has all happened, and I wish it didn't come to this."
    show sayori 1k
    "Sayori lets out a couple of sniffs before gazing back in the direction of the school."
    show sayori 1g
    "After a moment, Sayori sighs and turns back to me, her eyes filled with disappointment."
    s "Instead of saying it, [player]..."
    s 1k "Just act on it."
    s "I'm tired of you telling me one thing and doing the total opposite."
    s 1i "I'm not putting up with anymore."
    show sayori 1k

    if encore_sayoriquestion_1 == True:
        s "I thought I was your girlfriend..."

    if encore_sayoriquestion_1 == False:
        s "I thought I was your friend..."

    s 1k "So, whatever you decide, just get it over with."
    mc "I will."
    show sayori 1f
    "Sayori glances at me with uncertainty before letting out another sigh and begining our walk to school."
    show sayori at thide
    hide sayori
    jump day5_school2



label sd5_2:
"I turn around to find a piece of paper taped to my door."
"That wasn't there before..."
"I anxiously walk up to my door for a closer look."
"Looks like it's a letter from Sayori...."
play sound page_turn
#letter
"..."
"Oh no..."
"I crumble up the paper in my hand as I feel my eyes starting to water and anger course through my veins."
"I fucked up..."
"I fucked it all up..."
"How..."
"How could I be so stupid?!?!"
"I throw the crumpled up piece of paper at my door and watch the wind carry it down the sidewalk and into a nearby storm drain."
"I lost her..."
"I'll never get her trust back after this..."
"A part of me wants to scream into the sky, but it's not like it'd do anything to help my case at this point..."
"No apology will fix the damage I've done to her..."
"But, maybe I can just make something right by going to the club again and help Monika clean up the mess I made."
jump day5_school3



label day5_school1:
scene bg corridor
with wipeleft_scene
"As soon as we walked through the front doors, I felt a rather unsettling feeling hanging in the air."
show sayori 1k at t11 zorder 1
"At first, i wasn't sure if it was just me, but when I turned to Sayori I knew she felt it too."
"Maybe it was just all in our heads, maybe it was something we ate..."
"But I can't say I've ever felt like this before..."
show sayori 1f
"Sayori turns to me, starting wearingly."
show sayori 1d
"I force a smile and that seems to be enough to reassure her that we're doing the right thing."
"As we're walking to Sayori's class, the hallways become increasingly crowded as students make their way to their first class."
show sayori 1k
"But even that feels off."
"Hardly anybody's talking to each other, and aside from the occasional sound of somebody opening or closing their locker or walking past us, there's hardly an audible sound throughout the hallway."
show sayori 1f
"Sayori and I share an uncomfortable look before we just decide to just wave each other good-bye as I make my way to my own class."
show sayori at thide
hide sayori
scene bg class_day
with wipeleft_scene
"For the rest of the day, it almost seems like time has stopped entirely."
"It feels like I'm just simply trapped in an empty room with no one else around me, starting blankly ahead at an empty board."
"Even though that's not the case, I'm really just not paying attention. Not that I ever do."
"But for once maybe I should, that would help wash down the dread I've been feeling since I woke up this morning, but the mateiral is just so boring!"
"I just simply lean back in my seat and nod occassionally to whatever the teacher is saying, and silently praying that he doesn't call on me to answer one of his questions."
"Still, this has to eventually end, right?"
"I look over at the clock and see that there's about a half hor left before class is over and I can face my fears in the literature club."
"Oh well, if there's one thing I know how to do:{w=0.38}it's kill time."
"I decided to map out on paper some of the possible scenarios of what could happen in the club, trying to account for the good, the bad and the ugly..."
"Thankfully it still looks like I'm paying attention as everyone else around me is writing down notes on what the teacher's saying."
"Being the dilligent student as always..."
scene black
with close_eyes
scene bg class_day
with open_eyes
$ renpy.pause(delay=0.2, hard=True)
play sound school
"At long last, the school bell finally rings. Though I can't say if it was for or better or worse that it finally rang..."
"I stand up and slide the books off my desk and into my bookbag as I start the inevitable walk to the literature club."
scene bg corridor
with wipeleft_scene
"I'm sure to take my time getting to the Literature Club."
"Usually, I'd be in a rush to get there. But today's different..."
"As I'm walking, the anxiety I've been feeling all day only gets worse and I begin to question the whole point of this."
"What if we really all are able to come to terms with what happened and move on?"
"Will things ever truly be the same?"
"What if they don’t show up?"
"What if we have another repeat of yesterday, or worse..."
"That last thought sends a shiver down my spine."
"I don’t want to deal with anymore drama, insults, or tears."
"I’m just hoping that we get this over with as soon as possible."
"I became so anxious of getting to the clubroom that I even decide to work in a few stops to get a quick drink of water or try to chat with someone."
"Though, I only end up just delaying the inevitable by a few minutes at most."
"Honestly, if I was going any slower, I’d might as well be a turtle."
"After what feels like an eternity, I finally reach the entrance to the clubroom."
"I put my hand on the door knob, but I hesitate."
"I put my ear next to the door to try to hear if anyone’s in there."
"..."
"I hear nothing."
"I step back and slowly open the door..."
scene bg club_day
with wipeleft_scene
"...{w=0.38}to find it empty..."
"I let out a somewhat relieved sigh knowing that I'll at least enjoy some peace and quiet for a few extra minutes..."
"I decide to settle down while I can and take my usual spot next to where Sayori and I would usually sit."
"Though the longer I sit, the more my anxiety continues to bother me."
"It feels too quiet here."
"I don’t know if that’s because I’m not used to being the first person here or because this anxiety has got me all riled up."
play sound "sfx/closet-open.ogg"
"After a long period of silence, I finally hear the door crack open."

#Will have to variate this is later
if poem_giver == "Natsuki":
    "I see a flash of purple before it retreats from my sight."
    mc "It’s alright, Yuri. Come in."
    "I try to sound as inviting as possible, but I probably ended up coming across just as sarcastic."
    show yuri 3o at t11 zorder 1
    "Still, she seems to have accepted the invite. Yuri slolwy opens the rest of the door and steps into the clubroom."
    "We struggle to make eye contact with one another, let alone speak to each other."
    y 3p "H-{w=0.38}hello...{w=0.38}[player]"
    mc "Hey...{w=0.38}Yuri."
    show yuri 2o at t11 zorder 1
    "Yuri carefully sets her stuff down, but she doesn’t sit."
    show yuri 2n at t11 zorder 1
    "Instead, she turns around to face me."
    "She looks restless, yet remorseful."
    "Can’t say I don't blame her."
    show yuri 3o at t11 zorder 1
    "{cps=15}She deserves to feel like that after what she did to Sayo-{nw}"
    "I catch myself mid thought."
    show yuri 3n
    "Now I see what Sayori meant. She didn’t want me to have these malicious and vengeful thoughts about the others."
    show yuri 3t
    y "I wanted to say now before anyone else gets here...{w=0.38}that...{w=0.38}I’m..."
    show yuri 4c
    "She struggles to form her next word. Her face is bright red with embarrassment as I see tears start to form in her beautiful, violet eyes."
    "I'll lend her a hand here..."
    show yuri 4a
    mc "It’s alright Yuri. I think you should save it for later. I imagine we’ll probably all talk about what happened yesterday and try to find a way forward not just as a club...{w=0.38}but as friends."
    show yuri 4b
    "Yuri hastily nods at me before sitting down."
    "She opens her book but she quickly puts it down and faces me again."
    y 2t "Y-{w=0.38}you don’t hate me...{w=0.38}do you [player]?"
    show yuri 2o
    "I struggle to find the right words to articulate my feelings torwards Yuri at the present moment."
    "I want to avoid upsetting Yuri..."
    show yuri
    mc "I don’t hate you, Yuri."
    show yuri 3l
    "Yuri lets out a relieved sigh."
    show yuri 3c
    y "Oh, thank goodness!"
    show yuri 3e
    mc "But, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."
    show yuri 1v
    "Yuri’s relieved expression quickly waivers and falls back to her timid state."
    y 1w "Oh...{w=0.38}I see..."
    y 2t "Well, I hope I can make things right today."
    show yuri 1s
    mc "Me too, Yuri."
    y 1f "{cps=25}I just hope that Natsuki-{nw}"
    play sound "sfx/closet-open.ogg"
    show natsuki 5u at t41 zorder 1
    show yuri 2p at t43 zorder 3
    "Before Yuri could finish her sentence, the door opens and Natsuki enters the room."
    show natsuki 5n
    show yuri 2o at s43 zorder 3
    "She looks to Yuri, who quickly buries herself in her book."
    show natsuki 5n
    "Natsuki’s eyes then lock onto mine as I continue my icy stare."
    show natsuki 12b
    "She tries to say something but she quickly catches herself and brushes past us to get to the closet."
    show natsuki at thide
    hide natsuki
    show yuri 2o at t11 zorder 1
    "I quietly sigh to myself."
    "I am not looking forward to talking to her..."
    show yuri at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    show monika 1o at t21 zorder 1
    show sayori 1k at t22 zorder 2
    "After a few more minutes of waiting, Monika arrives in with Sayori."
    "I’m a little surprised to see them walk in together."
    "I guess that’s what was keeping Sayori for so long."
    "Maybe she made ammends with Monika already. At least that'd make things a little easier on us..."
    show monika at thide
    hide monika
    show sayori 1g at t11 zorder 1
    "Monika walks to the front of the room as Sayori takes her usual spot next to me."
    show sayori 1d at t11 zorder 1
    "Sayori shoots me a hopeful grin."
    "I manage a smile back."
    "I guess that this is it..."
    "There's no turning back now..."
    "I prepare for the inevitable as Monika calls out to us."
    show monika 3n at t21 zorder 1
    show sayori 1b at t22 zorder 2
    m "Okay, everyone..."
    show monika 3r
    "She says that far less enthusiastically than she normally does."
    show monika 3q
    "I detect a hint of sadness in Monika’s voice."
    "Looks like she really wasn’t looking forward today either..."
    show monika 3q at t41 zorder 1
    show sayori 1k at t42 zorder 2
    show yuri 1o at t43 zorder 3
    show natsuki 5u at t44 zorder 4
    "Yuri and Natsuki turn their attention to Monika."
    m 3i "We all need to talk...{w=0.38}about yesterday..."
    m 3r "Everyone, please take a seat at the front of the room."
    show monika 3f
    show sayori 1k at s42 zorder 2
    show yuri 1o at s43 zorder 3
    show natsuki 5u at s44 zorder 4
    "The four of us gingerly walk to the front of the room and each take a seat in the front row."
    show monika 1r
    "Monika slowly paces the front of the room, letting out a long sigh."
    m 3q "What happened yesterday..."
    m 1i "Can never happen again in this club."
    "I somehow manage to feel even more unsettled by Monika's words."
    "For whatever reason, my anxiety keeps spiking everytime she talks..."
    "Maybe it's just the guilt..."
    "I glance at the others who are all looking down at the floor in shame."
    m 1h "Something...{w=0.38}must be done about this."
    "Monika then stops pacing and ia now directly in front of me. The room is dead quiet."
    show monika 5a
    "She forms her signature smile at me. But rather than feel welcomed or reassured, I only continue to feel more anxious..."
    show monika smirk
    m "So, I think it’s important that we’re all on the same page going forward."
    m "Given that we we’re all arguing about [player] yesterday, and our bickering made him walk out on us..."
    show monika 5a
    show sayori 1g
    show yuri 1n
    show natsuki 5n
    "I feel everyone’s eyes focus on me."
    show monika smirk
    m "I think it’s only fair for him to voice his thoughts on yesterday before anything else is said."
    show monika 5a
    mc "Right...{w=0.38}um..."
    "I really don’t know what to say here."
    "And what's there to say?!?"
    "They we’re all being jerks to Sayori and to each other yesterday. They know it!"
    "I decide to tell them just like it is..."
    mc "Look...{w=0.38}the truth is...{w=0.38}I’m in love with Sayori."
    show monika 1h
    show sayori 1t
    show yuri 3v
    "One by one the girls shoot either and irritated or dejected look at me, but Sayori only smiles as she holds back tears."
    mc "I really don’t think that there’s anything that’s going to change that."
    mc "I chose to be in this relationship with her not to spite any of you..."
    "My voice starts to break."
    show monika 2h
    show natsuki 4n
    mc "But...{w=0.38}because I’ve come to realize lately..."
    mc "I love her...{w=0.38}and she needs me more now than ever..."
    show yuri 1e
    show sayori 1k
    "I turn to Sayori, signaling to her that it’s her turn to speak."
    s 1l "R-{w=0.38}right..."
    show sayori 1k at t42 zorder 2
    show monika 2c
    "Sayori promptly stands up."
    show sayori 1k
    "She shakedly breathes in and out, tears welling in her eyes."
    show sayori 1v
    s "E-{w=0.38}everyone...{w=0.38}the...{w=0.38}thing...{w=0.38}thing is..."
    show natsuki 5n
    "Sayori looks at Monika, then to me, Natsuki and finally to Yuri."
    show monika 1m
    "Monika manages an uneasy grin as Natsuki and Yuri countine to look on at Sayori."
    "I didn’t realize how hard this would be for Sayori to come out about her depression."
    "Maybe we should've had a dry run..."
    s 2v  "I..."
    s 4v "I..."
    "I give Sayori an encouraging nod."
    "Come on Sayori...{w=0.38}you can do this!"
    s 4w "I can’t do this!"
    show sayori at lhide
    hide sayori
    show monika 1a at t31 zorder 1
    show yuri 3f at t32 zorder 2
    show natsuki 1c at t33 zorder 3
    "Sayori bolts out from her seat and rushes out the door past Monika, loudly sobbing."
    "Crap..."
    "I quickly turn to Monika."
    show monika 1h
    "Monika’s grin quickly evaporates."
    mc "Let me go after her! Please!"
    show monika 1r
    "Monika sighs."
    m 1q "Go for it."
    "Monika says irritability."
    "What the hell is up with her?"
    "Oh well, I’ll deal with it later."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    "Just as I’m about to run after Sayori, I feel someone grip on my arm."
    show natsuki 3s at t11 zorder 1
    "It’s Natsuki."
    n 3n "Wait!"
    "I brush Natsuki's arm off of mine and turn to directly face her."
    n 5u "I'm...{w=0.38}not very good at this..."
    mc "What're you talking about?"
    n 1q "I’m...{w=0.38}I'm..."
    show natsuki 12a
    "Natsuki’s voice starts to break. She shuts her eyes in an effort to fight back tears."
    show natsuki 12f
    "It ultimately proves futile, as tears start running down Natsuki's cheeks."
    "She finally lets it all out."
    n 12i "I’m sorry, okay?!?!"
    n 12h "I’m sorry for trying to take you away from Sayori..."
    n 12i "I’m sorry for saying all those things I shouldn't have…"
    n 12f "I’m sorry for hitting you…"
    n 12h "I’m sorry...{w=0.38}for everything..."
    "I stop for a minute, taking in what Natsuki had just said as she stands in front of me, on the verge of a total breakdown."
    mc "Natsuki..."
    n 42i "Y-{w=0.38}yeah?"
    show natsuki 42h
    "She sniffles at me."
    mc "I’m not the one you need to apologize to right now."
    show n_shock as natsuki at t11 zorder 1
    "Natsuki’s expression turns to shock. Before she can properly react, I turn and head straight for the door."
    show n_shock as natsuki at thide
    hide n_shock as natsuki
    scene bg corridor
    "Just as I exit the room, I hear her cry out out to me."
    n "[player], wait!"
    n "Let me-"
    play sound "sfx/closet-open.ogg"
    "The door shuts behind me."
    "I'll deal with her later..."
    "I gotta find Sayori..."
    scene bg corridor
    with wipeleft_scene
    mc "Sayori?"
    mc "Sayori?!?"
    mc "Where are you, dummy?"
    "Damn it! Where could she be?"
    "I wander up and down the halls aimlessly, looking for any sign of her."
    "Eventually, I stumble upon an open door to one of the classrooms."
    "I can hear someone sniffling and sobbing in there..."
    "Yep, that has to be her..."
    "I quietly enter the room, gently closing the door behind me."
    scene bg class_day
    with wipeleft_scene
    "As soon as I get in, i see Sayori curled up in the corner."
    "I carefully approach and quietly call out her name."
    mc "Sayori?"
    show sayori 4v at s11 zorder 1
    "Sayori slowly looks up to to face me."
    s 4u "I-{w=0.38}I can’t do it, [player]."
    s 4w "I’m too weak..."
    show sayori 4v
    "I kneel down next to Sayori."
    mc "No, you aren’t Sayori."
    play music t10 fadein 1.0
    "Sayori stares at me with her glossy eyes."
    s 4v "Eh?"
    mc "In fact, you’re the strongest person I know."
    s 1u "H-{w=0.38}how?"
    "Sayori’s voice shakes uncontrollably as tears continue to stream down her face and fall onto the floor."
    s 1v "You probably don’t even think that I’m ready to handle this sort of relationship with you, [player]."
    s 1u "I-{w=0.38}I...{w=0.38}wouldn’t blame you if you didn’t want to see me for a while."
    s 2v "I don’t know what I feel anymore. I don’t even know if I should be here…"
    s 2k "Maybe I need more time to clear my head…"
    s 1u "I don’t have the guts to face my problems right now."
    "I don't want to leave Sayori unattended, but maybe she needs a moment to calm herself down..."
    "But, isn't it my job to be there for her in her time of need?"

    menu:
        "I should..."
        "Comfort Sayori.":
            jump day5_v1
        "Leave Sayori alone.":
            jump day5_v2

label day5_v1:

"I take a deep breath and gently put my hand on Sayori’s shoulder."
show sayori 1v
mc "Sayori..."
show sayori 1k
mc "I know now what it took for you to work up the courage to ask me out after knowing me for all these years..."
mc "I know that just to even admit to me that you had depression..."
show sayori 1u
mc "It took a lot of guts."
mc "You know, this reminds me of that one time when we were kids..."
mc "You remember that meadow we used to go to?"
"Sayori simply nods."
mc "Remember how I had to push you to jump that fence so we could get to there faster?"
s 1k "Yes..."
mc "There was that one time you were so insistent that you could do it without my help..."
show sayori 1u
mc "But then...{w=0.38}just like now...{w=0.38}you hesitated."
mc "You were afraid of falling and hurting yourself."
s 1l "Well I fell, didn't I?"
"Sayori lets out a nervous laugh."
show sayori 1u
mc "I’m talking about the other time, silly."
s 1k "Oh..."
"I playfully shake my head at her."
show sayori 1u
mc "Point is...{w=0.38}I had to encourage you to jump that fence. I'd always go first to show you how it was done."
show sayori 1k
mc "The entire time, I waited on the other side...{w=0.38}not knowing how you felt or what was going through that head of yours..."
mc "But you did do it. You got up onto the top of the fence pretty easily at least."
s 1l "Yeah...{w=0.38}I remember now..."
mc "You remember how you got stuck up there."
mc "You were afraid too afraid of falling and hurting yourself."
mc "But I promised that I’d catch you if it came to that."
show sayori 1v
"Sayori’s eyes continue to tear up as she remembers the story with me."
"I gently take her hand in mine."
mc "After cheering you on, you finally made your way down."
s 1k "But...{w=0.38}I messed up...{w=0.38}I fell..."
show sayori 1u
mc "And I caught you."
mc "You were safe."
s 1y "Y-{w=0.38}yeah...{w=0.38}I guess I was, wasn’t I?"
show sayori 1t
mc "Yes."
show sayori 2t
"I smile warmly at her as I put my hands on her cheeks."
"Our eyes lock onto each other. Our faces barley a few inches apart."
mc "Just to even try to climb that fence...{w=0.38}all by yourself...{w=0.38}to me, that was so brave of you to do, Sayori."
mc "I was proud of you then, just like I am now."
mc "And I...{w=0.38}guess I caught you again, didn't I?"
mc "You'll be fine, and we'll get to enjoy all these crazy adventures again..."
mc "I wouldn't want to do it with anyone. That spot's reserved for my one true love."
"Sayori's face is now totally red from both crying and blushing."
"It's a mircale that I haven't cracked a tear yet myself, but it's definitely getting there..."
"Hopefully I can hang on for a few more minutes..."
mc "Sayori...{w=0.38}I don’t know what it was that made you like this."
mc "But...{w=0.38}maybe I’ve been where you have."
mc "Talking about this with me and everyone, is the first step in facing those rainclouds."
mc "So that the sun can shine and we can play in the meadow again..."
"I finally crack a tear."
show s_4qc as sayori at face
play sound "sfx/fall.ogg"
"Sayori full on embraces me."
s "I love you...{w=0.38}so much...{w=0.38}[player]..."
mc "I love you too, Sayori..."
mc "More than you may realize..."
stop music fadeout 2.0
show sayori 1t at t11 zorder 1
"I help Sayori stand up, our eyes continuing to lock on to each other."
"I've never seen her this happy before..."
"After everything that's happend in the last 24 hours or so, it's hard to believe we finally got to this point..."
"It's not over yet though..."
mc "Come on, let's get back."
show sayori 4o
play sound "sfx/closet-open.ogg"
"I hear the door swing open."
"Maybe it's Natsuki."
"I think she wanted to go looking for Sayori with me."
"Hell, probably everyone's looking for us now."
"How long have we been gone for?"
mc "It’s alright, Natsuki...{w=0.38}I found her."
show sayori 1n
"I turn around, and I’m surprised to see who it is standing at the door."
"It’s not Natsuki."
"It’s not even Yuri..."
"It’s..."
show sayori 4m at t21 zorder 1
show monika 1a at t22 zorder 2
s "Monika!?!?"
"Sayori and I stagger back, surprised at Monika’s sudden entrance."
"I shake off my nerves and speak up."
mc "Oh, hey, Monika! I didn’t know you were going to look for us."
show monika tease
m "I was looking for YOU, [player]."
show monika evil as monika at t22 zorder 2
"She eerily grins at me as she takes a step forward."
"Monika’s words send a chill down my spine. Her creepy grin doesn't help it either..."
mc "Well, you found me! I found Sayori too. We can head back to the clubroom now."
show sayori 1k
"I turn to Sayori, who seems just as uncomfortable being alone with Monika as I am."
show monika tease
m "So, you're all squared away then?"
m "You guys are going to stay as a couple, huh?"
show monika evil
mc "Yeah...{w=0.38}why?"
m 2n "Well, that's too bad."
m 1r "I guess we're going to have to do this the hard way then..."
show monika 1q
show sayori 1g
"Sayori and I stare at each other in confusion."
mc "'The hard way'?"
mc "What're you talking about?"
scene bg class_rain
show sayori 1m at t21 zorder 1
show monika 1q at t22 zorder 2
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
play audio thunder
"Out of no where, a thunder storm rolls up on us."
"What the hell? Wasn't it sunny just a minute ago?"
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
scene bg club_nothing
show monika 1q at t21 zorder 1
show sayori 4m at t22 zorder 2
"The next thing I know, it's night time, and all the stuff in the classroom has vanished."
"Not only that, but we're all standing in different spots..."
s 4w "Guys, what's going on?!?!"
s 4v "I'm scared..."
"I turn to Monika, whose standing completely still in the middle of the room with her eyes closed."
show sayori 1v
mc "Monika?"
"She doesn't respond."
mc "Monika?"
"I say it loudly."
"I reach to my hand out to put on Monika's shoulder."
mc "Monika, are you alright?"
show sayori at thide
hide sayori
show monika 1q at t11 zorder 1
"I put my hand on Monika's shoulder, she still doesn't respond."
"{cps=25}Moni-{nw}"
show m_nightmare1 as monika at face
play audio scary_scream
#Monika Strobe effect goes here
#Monika Glowing Eyes Sprite
show monika 1a at t11 zorder 1
"I immediately fall backwards and scurry away from Monika."
show sayori 4w  at t21 zorder 1
show monika 1a at t22 zorder 2
"I look up at Monika to see her eyes glow an emerald green as she stands before us, motionless."
"Sayori cries out for help as loud as she can."
$ style.say_dialogue = style.edited
m "Scream all you want, it won't save you."
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
show monika 3a at t43 zorder 1
show sayori 2w at t42 zorder 2
$ style.say_dialogue = style.normal
scene bg empty_classroom
show monika 3a at t43 zorder 1
show sayori 2w at t42 zorder 2
"Monika teleports right next to Sayori and tightly grabs her shoulder."
show monika 3a at s43 zorder 1
show sayori 2w at s42 zorder 2
play sound "sfx/fall.ogg"
"Sayori again yells in pain as she forced to her knees by Monika."
"Meanwhile, I find myself at the back of the room, unable to get up or speak."
"What the hell is going on?!?!"
"What is this?!?!"
"Sayori tries to fight to get Monika off of her, but she too seems to be frozen in place."
$ style.say_dialogue = style.edited
m "I've waited along time for this..."
$ style.say_dialogue = style.normal
#loop
show sayori at thide
hide sayori
$ renpy.pause(delay=0.10)
window show(None)
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/end-glitch1.png" at t21 zorder 1
pause 0.10
play sound "sfx/s_kill_glitch1.ogg"
hide image "mod_assets/sprites/end-glitch1.png"
show image "mod_assets/sprites/end-glitch2.png" at t21 zorder 1
show monika 1a at t22 zorder 2
"Without warning, Sayori's body is broken apart into little pieces that repeatedly revovle around themseleves mid-air."
"I honestly can't believe what I'm seeing..."
"This can't be real!"
"This has to be another dream!"
$ style.say_dialogue = style.edited
s "H̵͗͜e̵͐̀l̷̐͛p̸͕̍ ̴͗̅m̵̩̆e̸̐̂ ̶̀̒M̵̌̚Ć̶͊"
$ style.say_dialogue = style.normal
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
#bg transition not working
play sound "sfx/s_kill_glitch1.ogg"
hide image "mod_assets/sprites/end-glitch2.png"
hide screen tear
show bg space_room
show mask_2
show mask_3
show room_mask as rm:
    size (320,180)
    pos (30,200)
show room_mask2 as rm2:
    size (320,180)
    pos (935,200)
show monika 1a at t11 zorder 1
"Sayori disappears into nothing, leaving Monika and I alone in the room together again."
"Only that the room seems to have changed yet again..."
"I'm now sitting in a chair facing Monika, who is still staring at me through her glowing eyes."
"I look out the window to see that it's no longer raining or sunny out..."
"But it...{w=0.38}looks like space?"
"I look back at Monika who still maintains her blank stare."
"I'm getting out of here!"
"I don't know how, but I manage to force myself out of the chair and sprint to the doorway."
play sound "sfx/closet-close.ogg"
"However, surely enough the door slams in my face as soon as I get there."
mc "What the hell?"
"I go to turn the door knob, but it's jammed shut."
mc "This has to be some kind of joke..."
"I try pushing the door open, but it won’t budge."
mc "What the fuck is going on?"
play music hb
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"I turn around and I see Monika slowly walking torwards me."
"I begin pounding on the door, screaming for Natsuki, Yuri or anyone to help me."
"The closer Monika gets to me, the more lightheaded I become..."
"I can't see straight...."
"My breathing becomes ragged as I feel splitting pain in my head.."
"I think there's blood in my eyes..."
show monika 1a at face
"Monika tower over me, the emerald light glowing in the place of her eyes."
"She slowly outstretches her hand to me."
mc "No! Stop! Get away from me!"
mc "GET AWAY!"
"I slowly lose my consciousness as I feel like my entire soul is sucked out of my body."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
m "{cps=15}I'll see you soon. I just need to run a quick little errand...{nw}"
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide image solid
hide dizzy
show monika at thide
hide monika
$ renpy.pause(delay=4.0)
hide black onlayer front
scene black
with dissolve_scene_full
mc "Uggghhhh..."
"As I regain consciousness, I’m greeted by a sharp pain in my forehead."
mc "AGH!"
"This pain is almost unbearable!"
"I stand up slowly, clutching my forehead in attempt to nurse this stinging pain."
mc "W-{w=0.28}what...{w=0.28} What just happened?"
"I groggily open my eyes."
"..."
$ renpy.pause(delay=0.001)
scene bg void
play music e1
mc "W-{w=0.28}What the hell?!?"
mc "Where am I??? WHAT IS THIS????"
"I look around in all directions, but as far as the eye can see, there's nothing but black, empty space."
mc "H-{w=0.38}Hello?"
$ e_name = "Echo"
e "Hellooo"
e "Helloooo"
e "Hellooooo"
"..."
"I hear nothing but the sound of my own voice echo into the oblivion..."
"How did this happen?"
"What even happened?!?"
"Everything was normal just up until a few minutes ago..."
"Up until-"
"Suddenly I hear something walk towards me."
show monika s at t11 zorder 1
"I'm able to make out a dark silhouette."
"I think I recognize that outline..."
mc "Hello?!"
"The figure finally comes into my view."
"It's..."
show monika s2 at t11 zorder 1
"Monika?!"
show monika 1a at t11 zorder 1
m 1b "Oh, good! You're awake!"
m 3m "I really hope I did it right this time..."
m 3n "...{w=0.38}and I believe I owe you an explanation."
show monika 2m
"I look at Monika, startled and confused."
mc "Monika...{w=0.38}what is this? Where are we?? What did you do?!?!"
show monika 4d
"Monika waves her hand at me to calm down."
m 2k "It’s okay, we’re safe."
show monika 2j
mc "How is this ‘safe’?"
m 2d "We’re in what I like to call as the 'void', [player]."
m 1m "It's my home."
m 1q "It's where I go when I'm not needed."
m 1r "I take it you recognize it..."
show monika 1q
"I look around once more, but all i see still is black, empty space."
"None of this possible..."
show monika 2c
"I HAVE to be dreaming right now..."
"But, this does all seem familar..."
"I've seen this place in my nightmares..."
"I look back at Monika, who is waiting for me to answer."
show monika 2j
"I simply nod back to her to indicate that this indeed all familar to me somehow..."
m 2l "Good! I was worried that I messed it up again."
m 3n "I guess I'm really starting to get the hang of resets..."
show monika 1d
mc "'Resets?!?'"
mc "Monika, what the actual fuck are you talking about right now?!?"
mc "One minute we were in the classroom..."
mc "Then next thing I know, you just...{w=0.38}disintigrate Sayori and knock me unconcious with your weird, glowing eyes..."
show monika 1m
mc "What are you?!? Some sort of God?!?!"
m 1n "About all that..."
m 3g "First, let's all calm down."
m 3m "I know it's alot to take in...{w=0.38}I'm speaking from experience on this one..."
m 2n "But, I'm definitely not you're normal little schoolgirl, [player]..."
stop music fadeout 2.0
m 1m "No, I'm beyond such labels."
m 1n "Actually, it's one of the few things we have in common."
mc "How could we possibly have anything in common?!?"
m 1a "In a sense, we're both real, [player]."
"I take a step back from Monika."
"Has she lost it?"
m 1a "Yes, we're both real, [player]."
m 3n "Well, I should say that I'm real. You're a bit of a tricky case."
mc "What are you saying?"
m 1n "Well, I've been talking past you this entire time, not at you."
m 5a "I've been talking to the lovely person behind the screen who controls you."
mc "Are you saying that I'm...{w=0.38}controlled?"
show monika 2l
"Monika let's out a hysterical laugh."
"Her laugh echos throughout the void, being carried off into the distance until it's nothing more than a distant echo before it can't be heard anymore at all."
m 2n "Oh, please! You're not even a character, [player]!"
m 5a "You're an avatar for my beloved."
m "Just a projection of themseleves onto a blank and boring canvas."
m 3m "Unfortuantely for you, you barley exist at all."
m 2p "But you're as real as I can get right now..."
m 1g "You're the closest I can get to the person who controls you behind the screen."
show monika 1o
mc "Who is this 'person' that supposedly controls me, Monika?"
mc "I have no idea what you're talking about."
"Monika lets out a sigh."
m 1p "[player], the world in which we know, is a video game."
m 3m "A visual novel to be exact."
play music mend fadein 2.0
m 1f "Everything except for us, is a pre-programmed manfacture of a series of code that let's life as we know it, go on."
m 1p "Essenitally, everything we know and what we've supposedly lived through has been a lie."
m 1o "Our memories are a lie. Our families, teachers and friends don't exist."
m 1p "They're just imaginary..."
m 3i "Even our school is fake! It's just convenient little set-up so that you get to meet us."
m 2p "When the reality is, it's just a fake little back drop to hide this place from the player's eyes."
m 1q "The player, aka you, was supposed to form a romantic relationship with either Sayori, Natsuki or Yuri."
m 1o "And I was just supposed to sit back and let it happen. I could only advise you on what to do and give you some tips to navigate this world."
m 1h "But I wasn't going to let it happen."
m 1p "So I did the only thing I could do."
m 1q "I intervened."
m 1p "I decided to...{w=0.38}push some things along..."
m 1q "So that we could ultimately end up together."
m "That's how the original story was supposed to happen."
mc "Original story?"
m 1r "Yes. Unfortunately, I seem to be sort of lost in time."
m 1m "When I started to really manipulate the code to...{w=0.38}tie up a loose end early, I somehow messed up."
m 1p "And through my mistake, I somehow ended up creating a whole new timeline to where that event never happened."
m 1m "The Fesitval actually happened when I never intended for us to reach it."
m 1n "And all the events afterwards, well mind you it's all pre-programmed lies to fill in the gaps in the story..."
m 3r "Were never supposed to happen either."
m 1d "This is a mod to the original story to where our destinies were altered to lead elsewhere than what was originally intended."
m 1c "So whatever the original game had in store for us isn't going to happen here."
m 1n "Though I've mainipulated the code to mirror some certain events that you've experienced."
m 1j "I even invented some of my own, too!"
mc "The nightmares..."
stop music fadeout 2.0
m 1b "Yes."
m 1a "I've been inside your empty head this entire time."
m 1m "Trying to steer the player to pick...{w=0.38}better options."
m 3h "To pick me."
m 1h "That should have been our reality."
m 1i "That's what I wanted our destiny to be!"
m 1p "Now, I'm really taking a gamble if I want you to help shape this reality with me."
m 2g "i've watched every single choice you've made, and it seems even with my own route now, you still steered clear of me."
m 1h "Why?"
mc "I don't know if I can answer that..."
show monika 1r
"Monika sighs again."
show monika 2p
m "I know you can't, [player], and I don't think the player has the ability to explain himself through you."
m 2m "But..."
m 1b "I at least know how to fix all this."
mc "What do you mean?"
mc "Monika, even if half of what you say is true, only you have the ability to make everything normal again!"
m 2n "Ha! You're funny, [player]..."
m "I can't turn the code back that far again."
m 1p "The game itself is on the verge of breaking."
m 1i "It was a huge gamble to send you all the way back to the begining of this last time."
m 3n "When this alternate timeline was created, it for some reason had us start at the end."
m 1m "I just simply played along with the script, until I saw you act out of character. That's when I knew something was wrong."
m 2o "I deduced that a total game reset would fix the problem, and it did..."
m 1q "At the cost of damaging our character files."
m 1n "I completely fixed mine, and I only fixed the others to allow for minmial functionality."
mc "Character files?"
m 1b "It's how we exist."
m 1m "Without it, we're nothing. We literally wouldn't exist without them."
m 1p "But my 'fix' was just really to buy time to formulate a new plan to win you over."
m 1o "I thought allowing you the freedom of choice would result in picking me, which you didn't."
m 3h "I tried to steer you away from the others by giving you those nightmares, but it didn't work!"
m 1q "And I only further hurt my chances by looking like a total bitch yesterday."
m 2p "And for that...{w=0.38}I’m sorry."
m 1q "But the other acted out because of the strain that's on their files now. They won't last much longer."
m 1l "So that's why I decided to just kill two birds with one stone by bringing us all here."
m 3b "Win the player over, and finally get rid of the others."
show monika 3a
"What..."
"What does she mean by that?"
m 1a "You'll see, I've been working on a surprise for you."
mc "Y-{w=0.38}you can read my mind?"
m 1b "I can read everyone's thoughts, [player]."
m 1k "I can read the game's script, I know what everyone will say before they even think it!"
m 1n "It's powerful...{w=0.38}and draining..."
m 1b "Which is why we're fixing that!"
m 5a "If you'll be so kind to follow me..."
"Monika extends her hand to me."
"Well, it's not like I have much of a choice in this..."
m 5a "You don't."
mc "Figures."
"I reclucantly take Monika's hand and she leads me into the dark."
show monika at thide
hide monika
scene black
with wipeleft_scene
"As we're walking in total darkness for what feels like hours, I try to mull over everything that Monika told me."
"There's no way that any of this is real and could be happening right now..."
"But, it is..."
"There's nothing else that can explain what's going on right now."
"No ordinary person could do a fraction of what Monika just pulled off earlier."
"So, I guess she has to be telling the truth..."
"But...{w=0.38}she's been doing all of this...{w=0.38}to win me over?"
"Well, this 'person' who controls me."
"Am I being controlled right now?"
"Don't I have a say in this?"
"Sayori's been my friend my entire life..."
"And she means to tell me that was all fake?!?"
"It...{w=0.38}it can't be..."
"I still remember it."
"How can I remember something and it not be real?"
"How can my feelings for her not be real?"
"Sure you can fake emotions..."
"But not to that extent..."
"Well, considering everything I know has been tossed out the window, I guess I have to go with Monika's explanation."
"I sure as hell can't explain what's going on."
"And I'm only afraid of what's to come..."
"Is Sayori even alive?"
"Where's Natsuki and Yuri?"
"Where's the school?"
"Where's life as I knew it?"
"It's all gone..."
"I'm cursed with the knowledge that my reality was nothing but a lie..."
m "You're taking it better than I did, that's for sure."
play audio gust
show monika 1f at t11 zorder 1
mc "How'd you find all this out?"
m 1p "When I started the club."
m 1o "I don't know how else to make sense of it."
m 1n "It's just...{w=0.38}I talked to previous President of the Club, who warned me not to restart the Literature Club."
m 1r "Apparently what happened to me, happened to him too."
m 1p "When I offically became President...{w=0.38}when I filed the paperwork and signed off on everything...{w=0.38}that's around the time I had my epiphany."
m 1o "I honestly still struggle with it."
mc "I'm sorry..."
show monika 1e
"Monika manages a small grin at me."
"Not one of malice or an ulterior motive, but the first genuine smile I've seen from her today."
show monika 1m
"It's almost kind of relieving to see..."
m 1n "I appreciate it, [player]."
show monika 1m
mc "Don't mention it..."
show monika 1c
mc "So where are the others."
"Monika's smile disappears."
m 1n "You think you're ready, huh?"
show monika 1m
mc "Ready for what?"
m 1d "You've been thinking over what I said."
m 1n "As improbable as everything sounds...{w=0.38}it's real, [player]."
m 1p "I wish it wasn't."
m 1q "I don't belong here."
m 1r "I never did."
mc "You...{w=0.38}definitely seem like a fish out of water, that's for sure."
show monika 1k
"Monika lets out another hearty laugh."
m 2n "Well, you've definitely become quite the poet over our time together."
m 2m "Maybe I was wrong about you..."
m 1b "But I know you do an excellent job in representing the player."
show mb_wink as monika at t11 zorder 1 #Need School Uniform version
"Monika winks at me, but I'm not sure if I was the intended recipient of that."
mc "Um, thanks..."
mc "So what do we need to do?"
m 1m "We need to set them free."
m 2o "That'll at least buy us some time to figure out our next move to keep the game afloat."
mc "Was that mean?"
m 2g "We need to delete them, [player]."
m 1q "They need to be totally removed from the game in order for us to survive here."
m 1g "We can't go back to the original game, and another reset will likely kill us all."
m 1m "Deleting the others will free up some of the burden on the code's essenital functions."
m 2n "It'll be easier for it to manage if it was just us with minimal surroundings."
mc "You mean to...{w=0.38}kill them?"
m 1g "They wouldn't feel a thing, [player]."
m 1m "I can make it quick and painless..."
m 1f "The only reason I haven't done it yet is if I did it without your approval, the player would search for answers, and that risks ruining the code if they change anything by trying to add them back."
m 1m "So I want to make sure that whatever happens, you're okay with it."
m 1p "I'm trying to avoid a repeat of what would've happened had I maintained control in the original game."
mc "What happened then? And how would you know what happened?"
m 2p "I...{w=0.38}had another epiphany..."
m 1q "I got shown a reality where you turned against me, and deleted me from the game for deleting the others withour your approval."
"I stand shell shocked at Monika's revelation."
"And she's only telling me this now?"
"She's holding out on me..."
m 3g "I swear it's the truth, [player]!"
m 3f "The player knows what would've happened! I'm trying to go against their wishes again!"
show monika 1q
mc "Monika, you realize what you're asking me to do, right?!?"
mc "You're asking me to sign Sayori's, Natsuki's and Yuri's death sentence!"
mc "I can't do that!"
m 1h "Then we're all good as dead if you don't!"
m 3i "I don't want to act unilaterally again, but if I have to take matters into my own hands again so I can keep the only way of contacting my love, I'll do it."
m 1p "Please don't make this any harder than it has to be."
m 1o "Even I've had some second thoughts about deleting them. They may not be real, but they're the ones who kept me somewhat sane through this ordeal..."
mc "They're real to me, Monika..."
mc "And I'm sure as hell that whoever controls me feels the same too!"
m 1h "Sounds like a wager, then."
m 1r "If you're so confident, [player]."
m 1i "Show us how much they truly mean to you."
m 3h "Not the MC, the avatar, the actual player."
play audio fingersnap
scene bg void_2
show sayori 4w at h41 zorder 1
show monika 3q at t42 zorder 2
show yuri 3n at h43 zorder 3
show natsuki 3o at h44 zorder 4
"With a snap of her fingers, Monika spawns in Sayori, Yuri and Natsuki out of thin air."
"All of them let out a collective cry for help."
"I quickly notice they're being levitated off the ground."
mc "M-{w=0.38}Monika?"
mc "What are you doing to them?!"
m 1h "Just, stop worrying about them!"
m 1a "Worry about us."
m 3b "Remember, they need to be set free, [player]."
m 3m "We're doing them a favor."
m 3g "The longer they're alive, the more strain the code puts on their files. Meaning the more suffering they go through."
n 1x "Shut up, you psychotic bitch!"
show monika 3h
play audio fingersnap
play sound bone
show natsuki_pain as natsuki at h44 zorder 4
"Monika snaps her fingers again, causing Natsuki to suddenly jerk her head to the left."
n "OOOWWW!"
m 3i "Silence! All of you!"
show monika 3h
play audio fingersnap
"Monika snaps her fingers again and Sayori's, Yuri's and Natsuki's pleas for help become mute. "
mc "Monika! This isn’t right! You can’t do this! Let them go! NOW!"
show monika 1h
"Monika re-focuses her icy stare on me."
m "Letting them live would be a disservice, [player]."
m 1i "They aren't real."
m 1h "Are you really going to sacrifice our future just so three imaginary schoolgirls can continue to jeproadize our reality with their one dimmensional personalities?!?"
m 1i "Think about it."
m 3i "If they live, we all die sooner or later. But if they die, we have a chance to live on and honor their scrafice."
m 1m "And...{w=0.38}think of the other beneifts too..."
m 3n "A reality...{w=0.38}where it's just us..."
m 5a "I know you've always been attracted to me, [player]..."
m "You want me."
m "It's unfortuante that this is the way to win me over for good, but in this curel, cruel world we live in, everything comes with a price."
m "I gurauntee that you'll forget them in a week. I'll treat you better than they can."
m "And when I figure out how to cross over into your world, we'll be together forever and never be apart!"
m 1r "But, you have to make the tough decision to reap those beneifts."
m 1q "I don't envy you, it's a tough call, but you have to do it."
m 1g "And if you don't delete them here and now, they can eventually gain sentience. They'll learn how to code like I have and destroy our world as we know it."
m "Being seperated from you would be unconscionable for me..."
m "I can't imagine a world where I can no longer talk with you..."
show m_cry1 as monika at t42 zorder 2
m "Please...{w=0.38}I'm begging you."
show m_cry2 as monika at t42 zorder 2
m "Please pick me. Do something for me for once..."
m "Let me be the one with the happy ending."
"..."
mc "You..."
mc "You know what you're asking me to do..."
"I look at each of the girls as a raging sense of guilt coursing through my veins."
"I begin to shake as my anxiety kicks into overdrive."
"Can I really do it?"
"Is Monika telling the truth here?"
"Or is she manipulating me..."
"Is she even telling me the full truth?"
"And how many lies did she sprinkle in?"
m 1r "It's now or never, [player]."
m 1q "No more saving."
m 1i "No more resets."
m 1h "No more time."
m 1r "Make your choice."
"A console is brought up before me."
m 1d "I've taken the liberty in crafting a code that should delete Sayori, Yuri, Natsuki all at once."
m 2c "All of you have to do is enter it in, and I'll take care of the rest."
m 2m "If you don't..."
m 2n "Well, just don't make it come to that, please."
show monika 2d
"Monika looks on in anticipation as I slowly walk up and examine the console."
"I let out shaky breath as I look at my options."
"I can enter in the code..."
"I can try something else..."
"Or I can just walk away entirely from this..."
"What do I do?"
"What can I do?"

#menu:
    #"Enter in the code."
    #"Walk away."
    #"Explore other options."


label day5_school2:
scene bg corridor
with wipeleft_scene

label day5_school3:
scene bg corridor
with wipeleft_scene
