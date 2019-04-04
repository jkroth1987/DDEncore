#############
#   DAY 2   #
#############
label day2_start:
    play sound "sfx/fall.ogg"
    scene bg bedroom
    $ day = 2
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    "I wake up startled, my heart pounding rapidly as my lungs struggle for air."
    "I violently gasp as I quickly open my eyes to find the world around me in nothing but haze."
    "I feel sweat running all over my body, as if I'd just come out of a sauna."
    "My room isn't even that warm..."
    "I let out a few coughs as I prop myself up to take a few deep breaths."
    "I rub my eyes in an attempt to clear my vision."
    "After a few blinks I'm able to see normally again."
    mc "W-{w=0.38}what the hell was that?"
    "I wearily say to myself."

if hangout1 == "Sayori" or "Natsuki" or "Yuri":
        "I feel a sudden rush of pain hit my forehead as I attempt to recall the horrific sight I saw."
        mc "Agh!"
        "I quickly clutch my head in an effort to control the pain."
        "Fortunately after a few moments, the pain subsides to a bearable level."
        "Well, this day's already off to a great start!"

        if hangout1 == "Sayori":
            "I try to purge what I saw last night from my memory, but I still feel like I can still see Sayori hanging..."

        if hangout1 == "Natsuki":
             "I try to purge what I saw last night from my memory, but I still feel like I can see Natsuki's horrifically snapped neck..."

        if hangout1 == "Yuri":
            "I try to purge what I saw last night from my memory, but I still feel like I can see Yuri about to stab herself..."


        if hangout1 == "Monika":
            "I feel another chill creep down my spine as I try to recall what that...{w=0.28}voice...was saying."
            "I put my other hand on my chest as I feel my heartbeat slow down a little."
            "After a few minutes, I can feel my heartrate return to normal as I wipe the rest of the sweat off my face."
            "I don't think I've ever had a nightmare that bad before..."
            "In fact, I couldn't even remember the last time I had one..."
            "I look over to my alarm clock."
            "Well, I don't have to get up for a few more minutes, but after that experience, I might as well get up now."
            "I slowly get out of bed to start my usual morning routine."
            jump day2_breakfast_monika


        "It's rather unsettling..."
        "I used to have nightmares when I was little, but I don't remember ever having this kind of reaction..."
        "Usually, I'd just wake up crying and run over to my parent's room."
        "Well, granted I can't do that so much now, considering they're away for the time being..."
        "Nor would they want a highschooler running overdramatically to their room."
        "That'd be quite the sight for them to see...{w=0.28}they probably would've thought they failed to raise me..."
        "I look over to my alarm clock."
        "Well, I don't have to get up for a few more minutes, but after that experience, I might as well get up now."
        "I slowly get out of bed to start my usual morning routine."
        jump day2_breakfast

label day2_breakfast:
scene bg kitchen
with wipeleft_scene
play music t2 fadein 1.0
"After getting my stuff ready for school, I head downstairs to the kitchen to fix myself up a quick breakfast."
"After how I woke up, I think I'd rather go with something simple..."
"I reach for the kitchen cabinet to grab my favorite brand of cereal and quickly grab some milk from the fridge."
"As I sit down, I try to wrap my head around my nightmare."
"'Let her die'."
"I scoff to myself."
"The hell is that supposed to mean?"

if hangout1 == "Sayori":
        "Whose 'her'?{w=0.38} Sayori?"

if hangout1 == "Natsuki":
       "Whose 'her'?{w=0.38} Natsuki?"

if hangout1 == "Yuri":
       "Whose 'her'?{w=0.38} Yuri?"

"Why on Earth would I do that?"
"More importantly, why would I let anyone die?"
"I honestly don't know what was worse:{w=0.38} the voice or what I saw..."
"Just thinking about that voice sends another cold chill running down my spine..."
"It was distorted...{w=0.38}I couldn't quite make out who was talking..."
"Though I could definitely tell that it was a woman's voice that spoke to me."
"But, whoever was talking, it sounded like they were going insane..."
"Maybe I'm the one going insane."
"Why am I sitting here trying to interpret this random dream?"
"It's not like it'll happen again..."
"I look at my watch."
"Oh shoot! I'm going to be late!"
"I quickly eat my breakfast and rush outside to meet Sayori."
jump day2_walktoschool




label day2_breakfast_monika:
scene bg kitchen
with wipeleft_scene
play music t2 fadein 1.0
"After getting my stuff ready for school, I head downstairs to the kitchen to fix myself up a quick breakfast."
"After how I woke up, I think I'd rather go with something simple..."
"I reach for the kitchen cabinet to grab my favorite brand of cereal and quickly grab some milk from the fridge."
"As I sit down, I try to wrap my head around my nightmare."
"'Let them die'."
"I scoff to myself."
"The hell is that supposed to mean?"
"Whose 'them'?"
"Why on Earth would I do that?"
"More importantly, why would I let anyone die?"
"Still, I know one thing for certain..."
"Whoever was talking to me, it sounded like they were a complete pyscho..."
"It was distorted...{w=0.38}I couldn't quite make out who was talking..."
"Though I could definitely tell that it was a woman's voice that spoke to me."
"Still, doesn't mean anything she said made a lick of sense to me."
"'Keep doing what I'm doing'."
"'We'll never be apart.'"
"Pretty sure at one point she said that I wasn't even a real person..."
"Maybe I'm the one going insane."
"Why am I sitting here trying to interpret this random dream?"
"It's not like it'll happen again..."
"I look at my watch."
"Oh shoot! I'm going to be late!"
"I quickly eat my breakfast and rush outside to meet Sayori."


label day2_walktoschool:
scene bg house
with wipeleft_scene
"As soon as I step outside, I feel a cool, gentle breeze flow through my hair, as if the day were greeting me."
"Granted, everyone's had wind blown in their faces before, but this time it feels...{w=0.28}welcoming..."
"Heh, well that'd be the first time that mother nature's ever welcomed me..."
"Though it's slightly cooler than yesterday because of the breeze, it's nothing I can't manage."
"I just hope I can get my mind off of the lingring effects of that dream as soon as possible..."
"As if the world was listening to my prayers, out of the corner of my eye I see Sayori coming towards me."
mc "Hey S-"

#Glitch 1

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        jump day2_glitch1_1


if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        jump day2_glitch1_2

#Glitch 2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Natsuki":
        jump day2_glitch2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Yuri":
        jump day2_glitch2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika":
        jump day2_glitch2

#Glitch 3

if encore_sayoriquestion_1 == False:
    if hangout1 == "Natsuki":
        jump day2_glitch3

if encore_sayoriquestion_1 == False:
    if hangout1 == "Yuri":
        jump day2_glitch3

if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika":
        jump day2_glitch3



        label day2_glitch1_1:
                $ renpy.pause(delay=0.10)
                window show(None)
                show s_kill zorder 1:
                    xcenter 640
                    pause 0.15
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                $ renpy.pause(delay=0.10)
                pause 0.15
                window show(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                hide s_kill
                jump day2_hugattack

        label day2_glitch1_2:
                $ renpy.pause(delay=0.10)
                window show(None)
                show s_kill zorder 1:
                    xcenter 640
                    pause 0.15
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                $ renpy.pause(delay=0.10)
                pause 0.15
                window show(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                hide s_kill
                jump day2_hope


        label day2_glitch2:
                $ renpy.pause(delay=0.10)
                window show(None)
                play sound "sfx/s_kill_glitch1.ogg"
                show image "mod_assets/sprites/end-glitch1.png"
                pause 0.10
                play sound "sfx/s_kill_glitch1.ogg"
                hide image "mod_assets/sprites/end-glitch1.png"
                show image "mod_assets/sprites/end-glitch2.png"
                pause  0.10
                play sound "sfx/s_kill_glitch1.ogg"
                hide image "mod_assets/sprites/end-glitch2.png"
                show image "mod_assets/sprites/end-glitch1.png"
                pause 0.10
                play sound "sfx/s_kill_glitch1.ogg"
                hide image "mod_assets/sprites/end-glitch1.png"
                show image "mod_assets/sprites/end-glitch2.png"
                pause 0.10
                play sound "sfx/s_kill_glitch1.ogg"
                hide image "mod_assets/sprites/end-glitch2.png"
                show image "mod_assets/sprites/end-glitch1.png"
                pause 0.10
                play sound "sfx/s_kill_glitch1.ogg"
                hide image "mod_assets/sprites/end-glitch1.png"
                show image "mod_assets/sprites/end-glitch2.png"
                pause 0.10
                hide image "mod_assets/sprites/end-glitch2.png"
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                jump day2_hugattack


        label day2_glitch3:
                $ renpy.pause(delay=0.10)
                window show(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.55
                stop sound
                stop music
                hide screen tear
                show crayori_1 at t11 zorder 101
                pause 1.0
                $ renpy.pause(delay=0.10)
                window show(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                show crayori_1
                hide crayori_1
                show crayori_2 at face
                play sound "sfx/giggle.ogg"
                pause 1.30
                $ renpy.pause(delay=0.10)
                window show(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.15
                stop sound
                hide screen tear
                hide crayori_2
                jump day2_hope




    label day2_hugattack:
    play sound "sfx/fall.ogg"
    show sayori 1q at t11 zorder 2
    "Sayori suddenly pulls me into a tight embrace."
    "I blink a few times just to make sure what I just saw wasn't real."
    show sayori 4r
    mc "Ah! Sayori..."
    s "Hug attack!"
    "Sayori squeezes me tightly."
    "Under normal circumstances, I'd be groaning and telling Sayori to let go."
    "Not because I don't like her hugs, but because she'd usually do it when I'm not in the mood, especially in the morning."
    "But, after what I experienced last night and just now, I do my best to brush it off and reciprocate with a hug of my own."
    show sayori 1o
    "Sayori quickly realizes my reciprocation."
    s "[player]..."
    show sayori 1n
    s "You're actually hugging me back?"
    s "This early on a Tuesday?"
    show sayori 1m
    s "When I'm giving my world famous 'hug attack'?"
    mc "Well I didn't know they were 'world famous', but..."
    s 4p "IMPOSTER!"
    show sayori 4p at h11 zorder 11
    "Sayori quickly breaks free of our embrace."
    mc "Oh, come on! The one time I actually hug you back during one of your 'hug attacks', and you think I'm a completely different person!"
    show sayori 5a
    s "Just gotta make sure that you're still you, [player]!"
    mc "We're gonna play this game now too?"
    show sayori 5b
    s "Yes~"
    "I let out a groan."
    mc "Alright. What's the question?"
    show sayori 5a
    s "What was my favorite thing about the festival this year?"
    mc "The food."
    "I answer jokingly."
    show sayori 5d
    s "Meanie..."
    show sayori 5c
    s "You know the real answer!"
    "I let out a small chuckle."
    mc "Being able to spend it with me."
    show sayori 4s at h11 zorder 11
    s "Yep~"
    mc "So, what's my prize?"
    "Usually, if I answer one of Sayori's questions correctly, she'd give me a little 'prize'."
    "We've been doing this game ever since elementary school..."
    "I thought it would've gotten old by now, but apparently not all of Sayori got past the fifth grade..."
    show sayori 1y
    s "Well..."
    mc " 'Well' what?"
    mc "Come on, you know the rules..."
    mc "I got it right, so you have to give me something!"
    "Now I sound like I'm the fifth grader..."
    "Thanks Sayori..."
    "Sayori suddenly walks up to me."
    show sayori 1q at face
    s "Close your eyes~"
    mc "W-{w=0.38}why?"
    show sayori 1s at face
    s "Pretty please?"
    mc "Alright, alright, fine..."
    scene black
    with close_eyes
    "I comply with Sayori's strange request."
    s "No peeking!"
    mc "Why would I-"
    stop music
    "chu~"
    scene bg house
    show sayori 1q at face
    with open_eyes
    mc "Wha-"
    show sayori 1x at t11 zorder 2
    s "Come on, [player]! We're gonna be late to school!"
    show sayori at lhide
    hide sayori
    "Sayori starts skipping down the sidewalk as if nothing had happened."
    "For a moment, I'm left starstuck and dazed."
    "That was the first time a girl other than my own mother had kissed me on the cheek..."
    "..."
    "Wait a minute..."
    "I come to the sudden realization that Sayori had set all of this up..."
    "Not bad, Sayori..."
    "But, we both know who's really better..."
    play music t7
    mc "Hey! Wait! Sayori, get back here!"
    "I start running after Sayori."
    scene bg residential_day
    with wipeleft_scene
    show sayori 1q at t11 zorder 2
    "Sayori seems to be blissfully unaware that I'm barreling down the sidewalk to catch up to her."
    mc "SAYORI!!!!!"
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1n
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1m
    "Sayori turns around to see me."
    mc "I'm going to get you back for that!"
    show sayori 5a
    s "You have to catch me first~"
    mc "You know that I usually do!"
    mc "You forgot who's the master at tag again, didn't you?"
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1o
    $ renpy.pause(delay=0.8, hard=True)
    s "Wait..."
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 4p
    s "EEEEEEEEEEEK!"
    s "[player]'s going to get me!"
    show sayori 1p
    show sayori at lhide
    hide sayori
    mc "You can't run!"
    "I call out playfully."
    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    "I end up chasing Sayori the rest of the way to school as the rest of the neighborhood watched on with a mix of bewilderment and amusement on their faces."
    "But I didn't care."
    "I'm just glad that I'm still able to be like my younger self sometimes around Sayori..."
    "She never really fails to bring that side out of me when she wants to..."
    jump day2_Keith



    label day2_hope:
    play music t2 fadein 3.0
    "I blink a few times just to make sure what I just saw wasn't real."
    show sayori 2h at t11 zorder 2
    s "[player]?"
    s "You okay?"
    "Sayori looks worringly at me."
    "I rub my eyes, trying to fake that it wasn't anything serious."
    mc "Y-{w=0.28}yeah, I'm good..."
    mc "Something just got in my eye."
    show sayori 1k
    s "I see..."
    "Sayori looks off in the direction of school."
    "I don't think she really bought into it..."
    "I try to move on from the subject."
    mc "Well, hey, we might as well start heading to school, huh?"
    "Sayori looks back at me with a blank expression on her face."
    show sayori 1g
    s "Yeah...{w=0.28}I guess so..."
    "She says solemnly."
    show sayori 1k
    "Sayori and I turn and start slowly making our way to school."
    scene bg residential_day
    with wipeleft_scene
    show sayori 1k at t11 zorder 2
    "I still feel guilty for making Sayori run off yesterday."
    "She hasn't said a word to me since we started walking."
    show sayori 1f
    "The entire time she had a mix of sadness and confusion on her face."
    "I sigh to myself."
    "I have no idea how we can salvage our friendship."
    show sayori 1k
    "At this point, I'm probably doing more harm to her mental health than good."
    "Any time I feel like I do something good for Sayori, I end up messing it up later..."
    "I'm not sure why she's even choosing to be around me despite everything..."
    show sayori 1b
    "I look to Sayori, who quickly realizes that I'm looking at her."
    show sayori 1a
    "Instead of being dismissive like I thought she would be, she unexpectedly shoots me a small smile."
    "I can't help but return the favor with a smile of my own."
    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    "Even in this awkward and painful chapter with my friendship with Sayori, we still have our fair share of laughs and smiles..."
    "Almost how it was before all this started..."
    "I've known her for fourteen years, and for the longest time, I thought I knew Sayori better than she knew herself."
    "But the reality is...{w=0.28}I don't..."
    "I don't know how I can even make amends with her after all the crap I've put her through."
    "I don't know what I can even do to make her feel better."
    "I don't know how to help her..."
    "I just...{w=0.28}don't know anything..."
    "And when it comes to Sayori...{w=0.28}that scares me..."
    "I don't even know just how deep her problems really run..."
    "Well, maybe I can try talking to her later today at some point."
    "Maybe then, we can start to straighten things out..."
    jump day2_walktoschool_2



label day2_Keith:
if encore_sayoriquestion_1 == True:
    scene bg corridor
    with open_eyes
    play music t3 fadein 2.0
"Unsurprisingly since we ran all the way to school, we ended up arrving to school relatively early."
"To help pass the time, Sayori and I walk up and down the fairly empty hallways, though it was just mostly us trying to recover from earlier."
show sayori 3q at t11 zorder 2
"I'm still silently processing the fact that Sayori somehow managed to pull all this off..."
show sayori 3y
"Sometimes, I still forget that behind Sayori's sweet, innocent act..."
show sayori 5a
"Is someone who's truly capable of being sneaky and making it work when she wants to..."
"It's good to see that part of her hasn't changed."
"I'll have to keep my eye on her..."
show sayori 1d
"Not that I should have any problem doing that anyways..."
scene bg corridor
with wipeleft_scene
show sayori 1r at t11 zorder 2
s "I have to admit, [player]..."
show sayori 2s
s "You're still the fastest guy I know!"
mc "Aww jeez..."
mc "I'm nowhere as fast as I used to be."
s "True, but still even now, you'd be great for the school's track team!"
mc "I think being in one club's enough for now, Sayori."
mc "Not to mention, I was never really the 'sportsy' type..."
show sayori 3h
s "But you'd be so good at it though!"
mc "Well if I put down my controller and went outside more, then maybe..."
mc "But, going outside isn't on my schedule...{w=0.38} for a while..."
show sayori 3i
s "[player]..."
play sound school
show sayori 1n
$ renpy.pause(delay=0.8, hard=True)
show sayori 1k
"Just before Sayori could finish her retort, we hear the bell ring throughout the school, signifying the start of another school day."
mc "Well, I guess our discussion of my exercising routine will have to wait for later."
show sayori 1r
"Sayori lets out a small giggle."
show sayori 1x
s "Alright, [player]! I'll see you after your class!"
mc "Can't wait!"
show sayori 1q at face
"Sayori suddenly gets up close to me again, like how she did earlier..."
"Does she want me to-"
"Are we at that stage of our relationship?"
"I feel my heart beating out of my chest as I lose any and all ability to coherently function."
"I close my eyes again..."
scene black
with close_eyes
"I lean in to Sayori..."
$ k_name = "???"
k "Oh, wow! Are you guys a thing?"
"I open my eyes..."
scene bg corridor
with open_eyes
"I see a guy walking past us down the hallway."
show sayori 1m at face
"Oh great..."
"It's Keith..."
show sayori 5b at t11 zorder 2
"Sayori backs off and tries to act as if nothing was happening."
$ k_name = "Keith"
mc "Hey! Screw off, Keith!"
mc "Aren't you still trying to make that 'mixtape'?"
mc "The one with your crappy nightcore remixes?"
"I see the look on Keith's face completely drain."
k "Come on, [player]! Nightcore is real music!"
k "We both know that!"
mc "If nightcore's 'real music', then our generation is screwed..."
"Keith gives me a bewildered look but doesn't tease further, clearly trying to give us some space as he walks further down the hall and turns the corner."
"Ah, Keith."
"Interesting guy."
show sayori 3g
"I turn back to Sayori, who has a rather disappointed look on her face."
mc "I guess we do need to be a little bit more careful about where and when we do these things, huh?"
s "Come on, [player]."
mc "What?"
show sayori 3h
s "What do you have against Keith?"
mc "Nothing! We just have different tastes in music, that's all."
"He handled the music at the festival last year when we were first years. His remixes were so bad I ended up going home early because I couldn't stand it."
"Aside from his quirks and occassional moments of cringe, he really isn't that bad of a guy."
mc "We just have that sort of relationship, Sayori."
mc "Kinda like how we have ours..."
show sayori 1y
s "I see..."
show sayori 1x
s "Well, I'll see you later, [player]!"
mc "Laters!"
show sayori 1s
"Sayori and I briefly embrace each other before scurrying off to our classes."
jump day2_classroom

label day2_walktoschool_2:
if encore_sayoriquestion_1 == False:
    scene bg corridor
    with open_eyes
    play music t3 fadein 2.0
    "For once, the walk to school wasn't as awkward as it had been lately."
    "We even managed to hold a somewhat decent conversation throughout the entirety of the walk, so I guess that's progress!"
    show sayori 1b at t11 zorder 2
    "Not to mention, Sayori seems to be doing much better now, given what happened yesterday"
    show sayori 1d
    "We did manage to arrive a little earlier than usual, so we just pass the time by slowly walking up and down the hallways until the morning bell rings."
    show sayori at thide
    hide sayori
    scene bg corridor
    with wipeleft_scene
    show sayori 1c at t11 zorder 2
    s "And that's why cinnamon buns taste better with icing."
    mc "I mean, I don't disagree..."
    mc "But I think it's better to have the icing in the cinnamon bun rather than on top of it, you know?"
    show sayori 3h
    s "But then that that'd make it a pastry!"
    play sound school
    show sayori 1n
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1k
    "Just before I could answer, we hear the bell ring throughout the school, signifying the start of another day at school."
    mc "Well, I guess our discussion about cinnamon buns and pastries will have to wait for later."
    show sayori 1r
    "Sayori lets out a small giggle."
    show sayori 1x
    s "Alright, [player]! I'll see you after your class!"
    mc "Can't wait!"
    "Sayori and I wave goodbye to each other as we go our separate ways to our classes."
    jump day2_classroom


label day2_classroom:
scene bg class_day
with wipeleft_scene
"As usual, my classes are unexciting and feel like they drag on forever."
"I'm fairly certain that most of the things they're teaching us now are never going to be used in our day-to-day lives post-highschool and college..."
"Not that I've really given much thought to my future anyways..."
play sound school
"With the sound of the final bell, everyone packs up their things and starts flooding out the door in a rush to get to their clubs or get back home."
"Fortunately this time, I'm one of the first few out!"
scene bg corridor
with wipeleft_scene
"As I stand out aside the classroom seeing all the other students flooding through the hallway, I'm able to somehow hear Sayori call out to me."
s "[player]! [player]!"
show sayori 3q at t11 zorder 2
"I turn to my right to see Sayori standing there, waving at me."
"Yep, that's definitely her..."
"I walk over to join her."
mc "Hey, Sayori!"
show sayori 3r
s "Hey, [player]!"
mc "You definitely seem to be in a good mood."
show sayori 3x
s "That's because it's time for the Literature Club, silly!"

if encore_sayoriquestion_1 == True:
        show sayori 1y
        s "And because I can't wait to spend more time with you~"
        "I feel a smile form across my face."
        mc "Well, let's go!"
        show sayori 1d
        "Sayori happily nods as we begin our walk to the clubroom."
        stop music fadeout 1.0
        jump day2_clubroom

if encore_sayoriquestion_1 == False:
        show sayori 1y
        s "I just hope we can spend some time together, that's all..."
        "She mutters softly."
        mc "Did you say something?"
        show sayori 1l
        s "Nevermind! Let's go!"
        "I shrug my shoulders as we begin our walk to the clubroom."
        stop music fadeout 1.0
        jump day2_clubroom


label day2_clubroom:
scene bg club_day
with wipeleft_scene
play music t5 fadein 1.0
"We arrive at the clubroom with the usual scene greeting us."
"Yuri is in her usual spot, intently reading her book, while Natsuki is rummaging around in the closet doing who knows what."
"I see Monika at the teacher's desk at the front of the room, apparently working on something."
show monika 1a at t11 zorder 2
"However, Monika quickly notices us and flashes us a smile."
show monika 1b
m "Hey guys!"
mc "Hey, Monika!"
show monika 5a
m "You guys seem to be doing well today~"
show monika 5a at t22 zorder 2
show sayori 2r at t21 zorder 1
s "Yeah, today's been great!"
show monika 2b
m "That's good to hear, Sayori!"
m "How about you, [player]?"
show monika 5a
m "How's your day been so far?"
"The way Monika says her question sends a familiar chill down my spine..."
"Kind of like the one I felt in my dream last night..."
"I brush the feeling off."
mc "Oh, it's been alright, I guess."
show monika 3k
m "Well, with a little literature, I'm sure we'll make your day phenomenal, [player]!"
show monika 5a at t22 zorder 2
m "Isn't that right, Sayori?"
show sayori 4r at h21 zorder 1
s "You know it!"
show monika 2e
m "You guys go get settled, I need to work on something and then I have something to share with everyone!"
show sayori 2a
s "That's awesome, Monika! I can't wait!"
show sayori at thide
hide sayori
show monika 2e at t11 zorder 1
"Sayori happily walks to her usual spot and sets her things down."
"I'm a little intrugied at what Monika's 'announcement' is, so I decide to indulge on my curiosity."
"I turn to Monika."
mc "So...{w=0.38} what's the announcement?"
show monika 2l
m "Oh come on, [player]! It's a surprise!"
show monika 5a
m "And I can't spoil a surprise that's meant for everyone, now can I?"
mc "Fair enough."

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki" or  encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori" or hangout1 == "Natsuki" or  hangout1 == "Yuri" or  hangout1 == "Monika":
            show monika 2a
            m "So, how're things with you and Sayori?"
            "My mind goes completely blank for a split second until I realize that Monika's the only one who knows that Sayori and I are a couple."
            mc "Oh! Well, things are going well I guess."
            mc "She can be a bit of a handful at times, you know?"
            show monika 2k
            "Monika lets out a small laugh."
            show monika 2b
            m "Haha! Well that's Sayori!"
            show monika 2e
            m "But, I'm glad to hear that things are going well between you guys."
            mc "Thanks, Monika."
            m "Well, hey, if you ever need any advice, I'd be more than happy to help."
            show monika 5a
            m "I just love seeing the two of you being happy together~"
            "I'm surprised Monika's taking such a serious investment in my relationship with Sayori."
            "I guess her and Sayori are bigger friends than I first realized..."
            "Well, it helps to have someone to turn to in case I need advice..."
            mc "I'll keep it in mind, thanks Monika!"
            show monika 2m
            m "Well I don't want to keep you any longer from her than I should, so..."
            mc "No, no, you're fine, Monika!"
            mc "Thank you!"
            show monika 3j
            m "No problem! If you want to talk more, I'll be here."
            show monika 5a
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Sayori":
            show monika 2a
            m "So, how're things with you and Sayori?"
            "My mind goes completely blank."
            "But then I remember that Monika's the only other person who knew that Sayori confessed to me..."
            "Maybe Sayori's trying to see how I feel about her in a roundabout way?"
            mc "Well, there isn't exactly an easy answer to that question..."
            show monika 2g
            m "Do you want to talk about it?"
            mc "I mean..."
            "I try to figure out how best to articulate my current status with Sayori."
            mc "It's just been...{w=0.28} awkward, since last Sunday."
            mc "Like one moment, everything will be fine."
            mc "Then the next thing I know, I'll say something stupid and it'll ruin her day."
            mc "I guess her feelings are still raw from...{w=0.28}you know..."
            show monika 2c
            "My voice trails off as Monika listens intently."
            show monika 2d
            m "Well, Sayori's going through a difficult time as you might imagine."
            mc "Yeah, I know..."
            mc "And I think I'm just making things worse between us..."
            show monika 2g
            m "It's an awkward time for the both of you."
            show monika 2l
            m "You can't necessarily force things to go back to they were before hand."
            show monika 2p
            m "That's something I learned fairly recently..."
            show monika 2n
            m "What's done is done."
            m "You just have to make the most of your situation."
            show monika 2d
            m "In Sayori's case, I'm sure she'll talk things out with you when she feels that the two of you are ready to have that discussion."
            mc "Has she told you anything lately?"
            show monika 2m
            m "That's not really something for me to say, [player]."
            show monika 2e
            m "But, I do know that she still cares about you and just wants you to be happy."
            m "So, it doesn't make sense to constantly dwell on your decision..."
            show monika 2n
            m "I'm sure there's someone out there who's right for you, [player]..."
            show monika 2e
            m "So, I'd just keep looking forward and let the past take care of itself."
            m "She'll come to you when she's ready."
            mc "Thanks, Monika...{w=0.28} I really appreciate that..."
            show monika 2j
            m "No problem!"
            show monika 2e
            m "Your happiness is important to me too, [player]."
            "I manage a small smile at Monika."
            mc "Thanks, Monika! You're too kind!"
            show monika 5a
            m "If you want to talk more, I'll be here."
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice

if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Natsuki":
            show monika 2a
            m "So, how're things with you and Natsuki?"
            "My mind goes completely blank."
            "I'm not entirely sure how I can put it to someone like Monika without accidentally giving anything away..."
            "For all I know, Natsuki might have convinced Monika to see how I feel about her in a roundabout away..."
            mc "Oh! Well, uh..."
            show monika 2l
            m "You don't have to answer if you don't want to, [player]."
            mc "No, no! It's fine, it's just..."
            m 2n "Difficult to explain?"
            mc "Yeah...{w=0.28}you could say that..."
            "I take a moment to collect my thoughts."
            mc "Well, it's been an interesting journey with her."
            mc "At first, I thought she hated me or something."
            show monika 2k
            "Monika lets out a small laugh."
            m "Well, that's Natsuki."
            m 2n "From my understanding, she's always kind of been like this..."
            mc "Really? Did she tell you something?"
            m 2m "That's not really something for me to say, [player]."
            m 2b "But, I can say that she's been a lot happier since you've joined."
            mc "Well, it's good to see that I did something right at least..."
            show monika 2l
            "Monika lets out another small laugh."
            m "Oh, come on, [player]! You should give yourself a little more credit than that..."
            mc "I mean, my frienship with Sayori's been a mess lately."
            mc "I don't even know what I'm supposed to do with her..."
            show monika 2g
            m "Do you want to talk about it?"
            mc "I mean..."
            "I try to figure out how best to articulate my current status with Sayori."
            mc "It's just been...{w=0.28} awkward, since last Sunday."
            mc "Like one moment, everything will be fine."
            mc "Then the next thing I know, I'll say something stupid and it'll ruin her day."
            mc "I guess her feelings are still raw from...{w=0.28}you know..."
            show monika 2c
            "My voice trails off as Monika listens intently."
            show monika 2p
            m "I see..."
            show monika 2d
            m "Well, I would say for Sayori is that she just needs time to get over what happened with you and her."
            show monika 2e
            m "I'm sure she'll come to you when she's ready to talk about what happened."
            mc "Yeah...{w=0.28} that's what I was thinking too..."
            m 2b "She's a strong person, [player]."
            m "She'll get through it."
            show monika 2e
            "Monika shoots me a reassuring smile."
            mc "Thanks, Monika....{w=0.28}I really needed to hear that."
            show monika 2j
            m "No problem!"
            mc "So, what should I do with Natsuki?"
            show monika 2m
            "Monika pauses for a moment."
            m 2n "Well, it depends where you see yourself going with her, [player]..."
            mc "I mean..."
            "I feel like I'm stuck in a box here."
            "Do I risk telling Monika that I'm interested in Natsuki?"
            "There's really no way that I can deny my feelings for her..."
            "Especially when it's starting to become painfully obvious..."
            "I decide to try to play the roundabout card too."
            mc "I just don't know if she likes me in the same way I do..."
            "Maybe went a little too obvious there..."
            show monika 2e
            "Monika shoots me a reassuring smile."
            m 2b "Well, I'm sure Natsuki will come to you soon and tell you how she really feels about you."
            m 2l "It's better for her to come to you than for you to come to her."
            m 2m "Knowing how she is and everything..."
            m 2n "I'm not quite sure if she's settled on her own feelings quite yet..."
            mc "I understand, thank you Monika!"
            mc "I really appreciate everything!"
            show monika 2j
            m "No problem!"
            show monika 2e
            m "Your happiness is important to me too, [player]."
            "I manage a small smile at Monika."
            mc "Thanks, Monika! You're too kind!"
            show monika 5a
            m "If you want to talk more, I'll be here."
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Yuri":
            show monika 2a
            m "So, how're things with you and Yuri?"
            "My mind goes completely blank."
            "I'm not entirely sure how I can put it to someone like Monika without accidentally giving anything away..."
            "For all I know, Yuri might have convinced Monika to see how I feel about her in a roundabout away..."
            mc "Oh! Well, uh..."
            show monika 2l
            m "You don't have to answer if you don't want to, [player]."
            mc "No, no! It's fine, it's just..."
            m 2n "Difficult to explain?"
            mc "Yeah...{w=0.28}you could say that..."
            "I take a moment to collect my thoughts."
            mc "Well, it's been an interesting journey with her."
            mc "At first, I thought she just wanted to be left alone with her books..."
            show monika 2k
            "Monika lets out a small laugh."
            m "Well, that's Yuri."
            m 2n "From my understanding, she's always kind of been like this..."
            mc "Really? Did she tell you something?"
            m 2m "That's not really something for me to say, [player]."
            m 2b "But, I can say that she's been a lot happier since you've joined."
            mc "Well, it's good to see that I did something right at least..."
            show monika 2l
            "Monika lets out another small laugh."
            m "Oh, come on, [player]! You should give yourself a little more credit than that..."
            mc "I mean, my frienship with Sayori's been a mess lately."
            mc "I don't even know what I'm supposed to do with her..."
            show monika 2g
            m "Do you want to talk about it?"
            mc "I mean..."
            "I try to figure out how best to articulate my current status with Sayori."
            mc "It's just been...{w=0.28} awkward, since last Sunday."
            mc "Like one moment, everything will be fine."
            mc "Then the next thing I know, I'll say something stupid and it'll ruin her day."
            mc "I guess her feelings are still raw from...{w=0.28}you know..."
            show monika 2c
            "My voice trails off as Monika listens intently."
            show monika 2p
            m "I see..."
            show monika 2d
            m "Well, I would say for Sayori is that she just needs time to get over what happened with you and her."
            show monika 2e
            m "I'm sure she'll come to you when she's ready to talk about what happened."
            mc "Yeah...{w=0.28}that's what I was thinking too..."
            m 2b "She's a strong person, [player]."
            m "She'll get through it."
            show monika 2e
            "Monika shoots me a reassuring smile."
            mc "Thanks, Monika....{w=0.28}I really needed to hear that."
            show monika 2j
            m "No problem!"
            mc "So, what should I do with Yuri?"
            show monika 2m
            "Monika pauses for a moment."
            m 2n "Well, it depends where you see yourself going with her, [player]..."
            mc "I mean..."
            "I feel like I'm stuck in a box here."
            "Do I risk telling Monika that I'm interested in Yuri?"
            "There's really no way that I can deny my feelings for her..."
            "Especially when it's starting to become painfully obvious..."
            "I decide to try to play the roundabout card too."
            mc "I just don't know if she likes me in the same way I do..."
            "Maybe went a little too obvious there..."
            show monika 2e
            "Monika shoots me a reassuring smile."
            m 2b "Well, I'm sure Yuri will come to you soon and tell you how she feels."
            m 2l "It's better for her to come to you than for you to come to her."
            m 2m "Knowing how she is and everything..."
            m "I'm not quite sure how she'd react if you went to her first..."
            m 2n "I don't know if she'd be able to handle it..."
            mc "I understand, thank you Monika!"
            mc "I really appreciate everything!"
            show monika 2j
            m "No problem!"
            show monika 2e
            m "Your happiness is important to me too, [player]."
            "I manage a small smile at Monika."
            mc "Thanks, Monika! You're too kind!"
            show monika 5a
            m "If you want to talk more, I'll be here."
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice



if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri":
        if hangout1 == "Natsuki":
            show monika 2a
            m "So, how're things with you and Yuri?"
            m 5a "Or should I say: things with you and Natsuki?"
            "My mind goes completely blank."
            "How in the world am I supposed to answer that?"
            "I mean...{w=0.28}I like Yuri..."
            "But since I finally got Natsuki to open up to me, maybe I have the chance to start something with her as well?"
            "I try to ramble out some answer that I think sounds good enough."
            mc "I mean, I guess things are good between me and Yuri..."
            mc "And it was nice to finally have a decent conversation with Natsuki without her hurling an insult or threat at me."
            show monika 2k
            "Monika lets out a small laugh."
            m 2j "It's ok, [player]! I was just teasing!"
            m 2b "But it's good to hear that you're finally getting along with Natsuki!"
            mc "Y-{w=0.28}yeah! It really is!"
            m 5a "And I'm sure she liked talking with you yesterday too~"
            mc "You really think so?"
            m 2k "Of course!"
            m 2b "When you were talking to her she was like a completely different person!"
            m 5a "But, you know, there's other interesting people to talk to in this club as well~"
            mc "What're you getting at?"
            "I quizzically look at Monika."
            show monika 2m
            m 2n "Well, I'm not ever too busy..."
            m 2e "I'm always willing to make time to talk to you about anything, [player]..."
            "Oh..."
            "I wasn't expecting that..."
            mc "I'll...{w=0.28}keep that in mind, Monika..."
            "I say that as cooly as I can as I feel the blood rush to my face..."
            "Monika's actually asking me to talk to her?"
            "What are the odds..."
            m 2k "Awesome!"
            m 2m "But, just make sure you don't make Yuri too jealous!"
            mc "How would Yuri be jealous?"
            mc "She isn't the jealous type...{w=0.28}right?"
            mc "Does she like me in that way?"
            show monika 2k
            "Monika lets out another laugh."
            m 2n "Well, that really isn't for me to say, now is it?"
            mc "I suppose not..."
            show monika 3e
            m "But do know this, [player]..."
            m "Your happiness is important to me too."
            m 2p "I know that things may be a bit complicated for you right now..."
            m 3b "But I'm more than happy to help you with anything!"
            "I manage a small smile at Monika."
            mc "Thanks, Monika! You're too kind!"
            show monika 5a
            m "If you want to talk more, I'll be here."
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Natsuki":
        if hangout1 == "Yuri":
            show monika 2a
            m "So, how're things with you and Natsuki?"
            m 5a "Or should I say: things with you and Yuri?"
            "My mind goes completely blank."
            "How in the world am I supposed to answer that?"
            "I mean...{w=0.28}I like Natsuki..."
            "But since I finally got Yuri to open up to me, maybe I have the chance to start something with her as well?"
            "I try to ramble out some answer that I think sounds good enough."
            mc "I mean, I guess things are good between me and Natsuki..."
            mc "And it was nice to finally have a decent conversation with Yurii without it falling apart because she thought she said something too weird for me."
            show monika 2k
            "Monika lets out a small laugh."
            m 2j "It's ok, [player]! I was just teasing!"
            m 2b "But it's good to hear that you're finally talking with Yuri!"
            mc "Y-{w=0.28}yeah! It really is!"
            m 5a "And I'm sure she liked talking with you yesterday too~"
            mc "You really think so?"
            m 2k "Of course!"
            m 2b "When you were talking to her she was like a completely different person!"
            m 5a "But, you know, there's other interesting people to talk to in this club as well~"
            mc "What're you getting at?"
            "I quizzically look at Monika."
            show monika 2m
            m 2n "Well, I'm not ever too busy..."
            m 2e "I'm always willing to make time to talk to you about anything, [player]..."
            "Oh..."
            "I wasn't expecting that..."
            mc "I'll...{w=0.28}keep that in mind, Monika..."
            "I say that as cooly as I can as I feel the blood rush to my face..."
            "Monika's actually asking me to talk to her?"
            "What are the odds..."
            m 2k "Awesome!"
            m 2m "But, just make sure you don't make Natsuki too jealous!"
            mc "How would Natsuki be jealous?"
            mc "Why, if I talked to her too much, she'd probably call me a creep or something!"
            mc "Does she like me in that way?"
            show monika 2k
            "Monika lets out another laugh."
            m 2n "Well, that really isn't for me to say, now is it?"
            mc "I suppose not..."
            show monika 3e
            m "But do know this, [player]..."
            m "Your happiness is important to me too."
            m 2p "I know that things may be a bit complicated for you right now..."
            m 3b "But I'm more than happy to help you with anything!"
            "I manage a small smile at Monika."
            mc "Thanks, Monika! You're too kind!"
            show monika 5a
            m "If you want to talk more, I'll be here."
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice


if encore_sayoriquestion_1 == False:
    if encore_festivalquestion_2 == "Yuri" or "Natsuki":
        if hangout1 == "Monika":
            show monika 2a
            m "So, how're things with you?"
            "I ponder the best way to answer that."
            "On one hand, my morning did start off pretty rough..."
            "But it did manage to get better as the day went on..."
            mc "I guess it's been alright, like I said."
            mc "Had my up's and down's..."
            mc "Basically a typical Tuesday."
            show monika 2f
            "Monika looks disappointingly at me."
            m 2g "Aww..."
            m "Just alright?"
            m 5a "Well, looks I'm just going to have to make your day really good, now won't I?"
            "Monika looks teasingly at me."
            "I'm not sure how to respond, but I figure it's probably worth playing along..."
            mc "And how do you propose to do that?"
            "I manage my best smile at Monika."
            show monika 2l
            m "I guess you'll just have to find out, [player]~"
            mc "You were never the direct type, were you?"
            m 2n "I have to string you along somehow, don't I?"
            m 5a "I like to keep people interested in me~"
            "I manage a chuckle."
            mc "Yeah, I guess so..."
            mc "Not saying it's a bad thing or anything!"
            show monika 2k
            m 2e "Don't worry, [player], I know what you mean."
            show monika 2m
            "There's a bit of an awkward silence between us until Monika breaks it."
            m 2n "You know..."
            show monika 5a
            m "I've actually been working on this poem since last night if you want to see how it turned out~"
            mc "I'll certainly keep that in mind, Monika."
            show monika 1e
            "Monika smiles as she turns and heads back to the teacher's desk."
            show monika at thide
            hide monika
            "I turn to face the rest of the room, with everyone doing their respective activities."
            "Well it makes no sense for me to stand out in the open like this..."
            jump day2_choice


label day2_choice:
        stop music fadeout 2.0
        menu:
            "Who should I hang out with?"
            "Sayori":
                $ s_modappeal +=1
                jump sencore_2
            "Natsuki":
                $ n_modappeal +=1
                jump nencore_2
            "Yuri":
                $ y_modappeal +=1
                jump yencore_2
            "Monika":
                $ m_modappeal +=1
                jump mencore_2


label day2_meettheclubs:
stop music fadeout 1.0
scene bg club_day
with wipeleft_scene
play music t3 fadein 1.0
"We all take our seats at the front of the room, with Monika standing right in front of us."
show monika at t11 zorder 4
m 3b "Okay everyone! Here's the news!"
m 3a "Starting next week, the Student Newspaper and Photography Club are going to be going around and doing a profile on all the different clubs."
m 2a "It's part of their bi-annual \'Meet The Clubs\' piece that they do every semester."
m "As of now, they're scheduled to meet with us to do their piece next Monday. So, I was hoping that we could think of something that'll really show off the club."
show monika at t22
show natsuki 5x at t21 zorder 1
"Natsuki audibly groans."
n 5e "Is this going to be like the festival again?"
show monika 2d
"Monika seems a little taken aback by this, but she tries to shrugs it off."
m 2c "No, not really. We won't have to be performing for anyone this time, and I certainly don't think we'll need to put in the same level of preparation for this compared to the festival."
show natsuki 5g
m 2i "But I would {i}appreciate{/i} it if we could at least come up with something nice that'll show off the club."
show monika at t43
show natsuki 1s at t41
show yuri 1g at t44 zorder 3
show sayori u115191 at t42 zorder 2
"Everyone takes a moment to collect their thoughts."
call groupAll(4, 2, 4, 1, 3) from _call_groupAll_3


if encore_sayoriquestion_1 == False or encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        jump day2_t1

if encore_sayoriquestion_1 == False or encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        jump day2_t5



label day2_t1:
"After a moment of silence, Yuri is the first to speak up."
show monika 1c
show sayori 1b
show natsuki 1k
y 1f "You know...{w=0.38}I did happen to keep the welcome banner we made for the festival..."
y 1j "I'd just need to find it. It's somewhere in my house."

if encore_festivalquestion_2 == "Natsuki":
    if hangout2 == "Natsuki":
        jump day2_t2

if encore_festivalquestion_2 == "Natsuki":
    if hangout2 == "Monika" or hangout2 == "Yuri" or hangout2 == "Sayori":
        jump day2_t3

if encore_festivalquestion_2 == "Yuri":
    if hangout2 == "Natsuki":
        jump day2_t4

label day2_t2:
n 1d "I wouldn't mind baking cupcakes again..."
n 4y "Turns out [player] isn't that bad of a cook!"
show natsuki 4j
"She says that directly looking at me."
show yuri 1e
show natsuki 2a
"Natsuki certainly isn't letting what just happened between us go."
jump day2_awk


label day2_t3:
n 1d "I wouldn't mind baking cupcakes again..."
n 4y "Turns out [player] isn't that bad of a cook!"
show natsuki 4j
"She says that directly looking at me."
show yuri 1e
show natsuki 2a
"Natsuki certainly isn't letting what just happened between me and [hangout2] go."
jump day2_awk


label day2_t4:
n 2t "I wouldn't mind baking cupcakes again..."
n 4y "Maybe [player] will want to help me this time!"
show natsuki 4j
"She says that directly looking at me."
show yuri 1e
show natsuki 2a
"Natsuki certainly isn't letting what just happened between us go."
jump day2_awk



label day2_awk:
"I try to move past the sudden awkwardness."
mc "Y-{w=0.38}yeah! I wouldn't mind, Nat!"
show natsuki 1i
"Natsuki looks at me with a puzzled look."
n 2h "‘Nat'?"
n 2i "Where did that come from?"
mc "I don't know, I thought it'd be cute if I gave you a little nickname."
show natsuki 1v at h41 zorder t41
"Normally, Natsuki would shoot me an irritated look before proclaiming to everyone that she isn't cute..."
show natsuki 5u
"But this time it doesn't even look like she knows how to get properly mad at me."
show natsuki 5n
"She tries to pout but I can tell she's forcibly trying to hold back a grin."
n 4w "Are you implying that I'm cute?"
mc "And if I was?"
n 4r "Uuuu!"
"Natsuki suddenly looks off in another direction, only becoming more flustered."
show natsuki 4s
"After about a moment she turns back to face me, no longer able to contain her grin."
n u112212 "I'll let that slide...{w=0.38}just this once!"

if encore_sayoriquestion_1 == True:
    jump day2_smad1

if encore_sayoriquestion_1 == False:
    pass

if hangout2 == "Monika":
    show monika 2h
    "I chuckle to myself, but in the corner of my eye, I see Monika shooting me a stern look."
    show natsuki 1m
    "I should probably take the hint and stop..."
    $ style.say_dialogue = style.edited
    show monika 2q
    "{cps=50}Forget about her!{nw}"
    $ style.say_dialogue = style.normal
    show monika 2n
    "Monika clears her throat."
    jump day2_tend


if hangout2 == "Yuri":
    show yuri 4b
    "I chuckle to myself, but in the corner of my eye, I see Yuri dejectedly looking off."
    "Oh, no...{w=0.38}she isn't assuming..."
    show yuri 4a
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    show natsuki 1m
    "Seeing Yuri's pained look derails my train of thought."
    "I forgot that Yuri didn't want to feel like she was getting in the way between me and Natsuki..."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend

if hangout2 == "Natsuki":
    show sayori 1t
    "I chuckle to myself, but in the corner of my eye, I see Sayori looking tearfully at me."
    show natsuki 1j
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    "Seeing Sayori just trying to hold back her tears completely derails my train of thought."
    "I never did take into account that she might not yet be comfortable with me being this flirty around Natsuki yet."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show natsuki 1m
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend


if hangout2 == "Sayori":
    show sayori 1k
    "I chuckle to myself, but in the corner of my eye, I see Sayori awkwardly staring at the wall."
    show natsuki 1j
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    show sayori 1g
    "Seeing the look on Sayori's face completely derails my train of thought."
    "Even though Sayori just told me how she feels when I spend time around Natsuki, I didn't completely realize it until now."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show natsuki 1m
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend


label day2_smad1:
show sayori 1g
"Sayori once again shoots me the same quizzical glance she gave me yesterday when Natsuki brought up the time we spent together last Sunday."
"Sooner or later, I'm going to have to resolve all this and tell Natsuki that I'm with Sayori..."
"As well as tell Sayori everything that happened between me and Natsuki on Sunday."
"Hopefully that will put her mind to rest..."
"Thankfully Monika comes in to seemingly save the situation."
jump day2_tend


label day2_t5:
"After a moment of silence, Natsuki is the first to speak up."
show monika 1c
show sayori 1b
show yuri 1e
n 1k "I wouldn't mind baking cupcakes again, I still have plenty of ingredients left over."

if encore_festivalquestion_2 == "Yuri":
    if hangout2 == "Yuri":
        jump day2_t6

if encore_festivalquestion_2 == "Natsuki":
    if hangout2 == "Yuri":
        jump day2_t7

if encore_festivalquestion_2 == "Yuri":
    if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Sayori":
        jump day2_t8

label day2_t6:
y 1b "I did happen to keep the welcome banner that [player] and I made for the festival. I'd just need to find it."
y 3j "It's somewhere at my house, and I wouldn't mind for some help looking for it."
show yuri 3s
"Yuri looks whimsically at me."
"She isn't asking..."
"Especially after..."
mc "Y-{w=0.38}yeah! I wouldn't mind helping you again!"
show yuri 2t
mc "I'd love to come over to your place Any time!"
show yuri 2u
mc "Preparing for the festival with you was really fun!"
jump day2_awk_2

label day2_t7:
y 1b "I did happen to keep the welcome banner that I made for the festival. I'd just need to find it."
y 3q "I wouldn't mind some help in finding it..."
show yuri 3s
"Yuri looks whimsically at me."
"She isn't asking..."
"Especially after..."
mc "Y-{w=0.38}yeah! I wouldn't mind helping you!"
show yuri 2t
mc "I'd love to come over to your place Any time!"
show yuri 2u
mc "I'm sure it'd be fun!"
jump day2_awk_2

label day2_t8:
y 1b "I did happen to keep the welcome banner that [player] and I made for the festival. I'd just need to find it."
y 3j "It's somewhere at my house, and I wouldn't mind for some help looking for it."
show yuri 3s
"Yuri looks whimsically at me."
"It doesn't seem like she wants to let what happened between me and [hangout2] go..."
mc "Y-{w=0.38}yeah! I wouldn't mind helping you again!"
show yuri 2t
mc "I'd love to come over to your place Any time!"
show yuri 2u
mc "Preparing for the festival with you was really fun!"
jump day2_awk_2


label day2_awk_2:
"Yuri looks off, attempting to compose herself."
y 2q "Y-{w=0.38}yeah...{w=0.38}it was really nice..."
show yuri 2p
"She says that softly to herself, but quickly realizes that everyone overheard."
y 1o "Oh! I mean...{w=0.38}yeah, I would love your help!"
show yuri 4c
"I chuckle to myself, Yuri's mannerisms have always been adorable."
show natsuki 1s

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Yuri":
        jump day2_smad3

if encore_sayoriquestion_1 == True:
    if encore_festivalquestion_2 == "Natsuki":
        jump day2_smad2

if encore_sayoriquestion_1 == False:
    pass


if hangout2 == "Monika":
    show monika 2h
    "In the corner of my eye, I see Monika shooting me a stern look."
    show yuri 1e
    "I should probably take the hint and stop..."
    $ style.say_dialogue = style.edited
    show monika 2q
    "{cps=50}Forget about her!{nw}"
    $ style.say_dialogue = style.normal
    show monika 2n
    "Monika clears her throat."
    jump day2_tend

if hangout2 == "Yuri":
    show sayori 1t
    "In the corner of my eye, I see Sayori looking tearfully at me."
    show yuri 1e
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    "Seeing Sayori just trying to hold back her tears completely derails my train of thought."
    "I never did take into account that she might not yet be comfortable with me being this flirty around Yuri yet."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show yuri 1f
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend

if hangout2 == "Natsuki":
    show natsuki 5n
    "In the corner of my eye, I see Natsuki eying me suspiciously."
    "Oh, no...{w=0.38}she isn't assuming..."
    show natsuki xul
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    show yuri 1e
    "Seeing Natsuki's disappointed look derails my train of thought."
    "I forgot that Natsuki was suspicious of me being with Yuri and not wanting anything to do with us..."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend

if hangout2 == "Sayori":
    show sayori 1k
    "In the corner of my eye, I see Sayori awkwardly staring at the wall."
    show yuri 1e
    mc "I-{w=0.38}I mean...{w=0.38}I always love spending time with you all, and..."
    show sayori 1g
    "Seeing the look on Sayori's face completely derails my train of thought."
    "Even though Sayori just told me how she feels when I spend time away from her, I didn't completely realize it until now."
    mc "Um...{w=0.38}yeah...{w=0.38}so..."
    show yuri 1f
    show sayori 1k
    "I look like an idiot as I try to find what to say next."
    "Thankfully Monika comes in to seemingly save the situation."
    jump day2_tend


label day2_smad2:
show sayori 1g
"Sayori once again shoots me the same quizzical glance she gave me yesterday when Natsuki brought up the time we spent together last Sunday."
"Sooner or later, I'm going to have to resolve all this and tell Natsuki that I'm with Sayori..."
"As well as tell Sayori everything that happened between us on Sunday."
"Hopefully that will put her mind to rest..."
"Thankfully Monika comes in to seemingly save the situation."
jump day2_tend


label day2_smad3:
"Sayori once again shoots me the same quizzical glance she gave me yesterday when Yuri brought up the time we spent together last Sunday."
"Sooner or later, I'm going to have to resolve all this and tell Yuri that I'm with Sayori..."
"As well as tell Sayori everything that happened between us on Sunday."
"Hopefully that will put her mind to rest..."
"Thankfully Monika comes in to seemingly save the situation."
jump day2_tend



label day2_tend:
show yuri 1a
show natsuki 1k
show sayori 1b
m 3b "I can type up a summary of what we do on a day-to-day basis and write some things down for what we can tell the Newspaper."
s 4n "Ooh, ooh, I know what I can do!"
"Everyone turns to Sayori."
s 1x "I can go to the library and get some books for us to read! I'd think it'd look good for when they take pictures of us!"
m 1b "Great call, Sayori!"
m 1a "As for you, [player], do you have any ideas?"
mc "Hmmmm..."
"I take a few moments to think to myself."
"Suddenly I got an idea."
mc "Well, I can bring in some famous poems that we could also use for the photo ops, I'd think it'd be great to show that there's more to literature than just books."
mc "Heck, maybe we can even use some of our own poems as well, I can organize them together like Monika did, but I'll need everyone else's poems."
show yuri 1g
show monika 1c
show sayori u114111
show natsuki u116113
"Everyone pauses to reflect on what I just said."
m 2b "That's a good idea, [player]! I'll hand you all my stuff tomorrow if that's ok with you."
mc "That's perfectly fine!"
s 2x "I have all my poems back at my place, I can give them to you later."




# BEGIN "LIKE YOU/LOVE YOU" POEM LOGIC
$ poem_giver = "" # Will be either Yuri or Natsuki
$ is_love_poem = False
$ same_hangout = hangout1 == hangout2
$ conflicting_hangout = (hangout1 == "Natsuki" and hangout2 == "Yuri") or (hangout1 == "Yuri" and hangout2 == "Natsuki")
$ neutral_split_n = (hangout1 == "Natsuki" and (hangout2 == "Sayori" or hangout2 == "Monika")) or (hangout2 == "Natsuki" and (hangout1 == "Sayori" or hangout1 == "Monika"))
$ neutral_split_y = (hangout1 == "Yuri" and (hangout2 == "Sayori" or hangout2 == "Monika")) or (hangout2 == "Yuri" and (hangout1 == "Sayori" or hangout1 == "Monika"))

if encore_sayoriquestion_1 == True: # We accepted Sayori's confession
    if (hangout1 == "Sayori" or hangout1 == "Monika") and (hangout2 == "Sayori" or hangout2 == "Monika"):
        # Spent both days with Sayori, Monika, or split between them--show the love poem from the weekend hangout girl
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True

    elif encore_festivalquestion_2 == hangout1 and same_hangout == True:
        # Outside the confession, we have been 100% faithful to either Yuri or Natsuki
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True

    elif encore_festivalquestion_2 != hangout1 and same_hangout == True and (hangout1 == "Natsuki" or hangout1 == "Yuri"):
        # We spent the weekend with one girl, but spent the two days with the other -- the hangout girl gives the like poem
        $ poem_giver = hangout1
        $ is_love_poem = False

    elif encore_festivalquestion_2 == "Natsuki":
        if neutral_split_n == True:
            # We favored Natsuki over Yuri
            $ poem_giver = "Natsuki"
            $ is_love_poem = True

        elif neutral_split_y == True:
            # We haven't spent time with Natsuki since the weekend, and Yuri is taking interest
            $ poem_giver = "Yuri"
            $ is_love_poem = False

        elif conflicting_hangout == True:
            # We spent time with both of them, but Natsuki wins for having the weekend
            $ poem_giver = "Natsuki"
            $ is_love_poem = True


    elif encore_festivalquestion_2 == "Yuri":
        if neutral_split_y == True:
            # We favored Yuri over Natsuki
            $ poem_giver = "Yuri"
            $ is_love_poem = True

        elif neutral_split_n == True:
            # We haven't spent time with Yuri since the weekend, and Natsuki is taking interest
            $ poem_giver = "Natsuki"
            $ is_love_poem = False

        elif conflicting_hangout == True:
            # We spent time with both of them, but Yuri wins for having the weekend
            $ poem_giver = "Yuri"
            $ is_love_poem = True

    # End of Accepted Confession block
else: # We didn't accept Sayori's confession
    if encore_festivalquestion_2 == hangout1 and same_hangout == True:
        # We spent the weekend and two hangouts with Yuri or Natsuki... but wait!
        # The other girl will give a "like you" poem
        if encore_festivalquestion_2 == "Natsuki":
            $ poem_giver = "Yuri"
        else:
            $ poem_giver = "Natsuki"
        $ is_love_poem = False

    elif neutral_split_n == True or neutral_split_y == True:
        # If we spent one day with either Yuri or Natsuki, the weekend girl gives the "like you" poem
        if encore_festivalquestion_2 == "Natsuki":
            $ poem_giver = "Natsuki"
        else:
            $ poem_giver = "Yuri"
        $ is_love_poem = False

    if (hangout1 == "Sayori" or hangout1 == "Monika") and (hangout2 == "Sayori" or hangout2 == "Monika"):
        # Spent both days with Sayori, Monika, or split between them--show the love poem from the weekend hangout girl
        $ poem_giver = encore_festivalquestion_2
        $ is_love_poem = True



    # End of Rejected Confession block

# We have figured our logic and know which poem to show, based on poem_giver ("Natsuki" or "Yuri") and is_love_poem (True or False)

if poem_giver == "Natsuki":
    jump n_poem1
elif poem_giver == "Yuri":
    jump y_poem1
else:
    jump day2_clubend

label n_poem1:
#NatsukiGivesYouThePoem
y 1b "Same here, I'll give you them at tomorrow's meeting, [player]."
n 3c "I think I have mine with me, let me check."
show monika at thide
show sayori at thide
show yuri at thide
hide monika
hide sayori
hide yuri
show natsuki 1a at t11
"Natsuki searches through her bag and retrieves a small stack of papers."
show natsuki 1d at t11
n "Here you go, that should be everything."
"Natsuki hands me her poems."
mc "Thanks, Natsuki."
show natsuki 1a at t41
show monika 3b at t43 zorder 4
show yuri 1a at t44 zorder 3
show sayori 1a at t42 zorder 2
jump day2_clubend

label y_poem1:
#YuriGivesYouThePoem
n 1b "Yeah, [player], I'll give you mine tomorrow."
y 3b "I believe I have my poems with me, let me check quickly."
show monika at thide
show sayori at thide
show natsuki at thide
hide monika
hide sayori
hide natsuki
show yuri 3a at t11
"Yuri searches through her bag and retrieves a small stack of papers."
show yuri 2b at t11
y "Here you go, [player]! That should be everything!"
"Yuri hands me her poems."
mc "Thanks, Yuri."
show natsuki 1a at t41
show monika 3b at t43 zorder 4
show yuri 1a at t44 zorder 3
show sayori 1a at t42 zorder 2
jump day2_clubend

## Move this to the later point where we need to check back on this and uncomment it there.
#if poem_giver == "Natsuki":
#    if is_love_poem == True:
#        # Show Natsuki's love poem
#    else:
#        # Show Natsuki's like poem

#if poem_giver == "Yuri":
#    if is_love_poem == True:
#        # Show Yuri's love poem
#    else:
#        # Show Yuri's like poem

label day2_clubend:
m 1a "Okay everyone, you all know what to do! That concludes today's meeting! Be sure to find your poems and give them to [player]!"
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
show sayori at thide
hide sayori
"Everyone begins packing their things, mostly talking about their levels of excitement for the upcoming event."
"As I think to myself, this would probably be the first time I've ever been interviewed by our school's newspaper for anything!"
"I know Monika's been interviewed before..."
"And somehow Sayori has been interviewed before as well..."
"But I guess for Natsuki, Yuri and I, this will be out first time."
"I feel my anxiety start to rise as I think about it."
"My train of thought ends as I feel a tap on my shoulder."
show sayori 3a at t11 zorder 1
s "Ready to walk home, [player]?"
mc "Yep! Let's go!"
"After I finish packing my things, Sayori and I wave goodbye to the others as we head out to start our walk home."
show sayori at thide
hide sayori
stop music fadeout 1.0
scene bg residential_day
with dissolve_scene_full


if encore_sayoriquestion_1 == True:
    if hangout2 == "Sayori":
        jump day2_walkhome1

if encore_sayoriquestion_1 == False:
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        jump day2_walkhome2

if encore_sayoriquestion_1 == True:
    if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        jump day2_walkhome3


#Walking Home

label day2_walkhome1:
with open_eyes
play music e4
show sayori 1y at t11 zorder 1
"During the walk home, I feel Sayori gently take my hand."
"When I turned to her, she kept looking straight ahead, madly blushing."
"I smile to myself as we keep walking."
"It seems that we've gotten more comfortable with showing off our affection for each other in public, even if it's something as simple as holding hands."
"Sayori seems to be in a really good mood today."
"Well, she did say me being around her helps her feel better..."
"Granted, I have no problem spending my time around Sayori!"
"What if this was the cure to her problems all along? Just us spending time around each other?"
"At this rate, she should be rid of those 'rainclouds' in no time!"
"The thought of that keeps me smiling through the duration of our walk."
show sayori at thide
hide sayori
scene bg house
with wipeleft_scene
"Eventually, we reach our houses."
show sayori 3b at t11 zorder 1
s "Hey, [player]?"
mc "Yeah, Sayori?"
s "I think I know where my poems are..."
show sayori 1y
s "I can stop by your house in a bit and drop them off if that's okay..."
"Sayori's voice trails off."
"I see where she's going with this..."
mc "Yeah, I'd love to have you over! I'll see you in a bit, Sayori."
show sayori 4q
s "Okay~"
"Sayori and I briefly embrace each other as we head back to our respective houses."
"I hope Sayori can stay a little longer this time..."
stop music fadeout 2.0
show sayori at thide
hide sayori
jump day2_poems


label day2_walkhome2:
with open_eyes
play music t8
show sayori 1k at t11 zorder 1
"The walk home with Sayori is once again filled with awkward silence..."

if hangout2 == "Sayori":
    "Especially considering that moment we had in the clubroom earlier..."

if hangout2 == "Natsuki":
    "Especially considering how Sayori saw me getting too comfortable with Natsuki..."

if hangout2 == "Yuri":
    "Especially considering how Sayori saw me getting too comfortable with Yuri..."

if hangout2 == "Monika":
    "Especially considering how Sayori saw me getting too comfortable with Monika..."


show sayori 1b
"Though we're able to make at least some small talk, with mostly just talking about how our days went."
show sayori 1l
"But even then, Sayori's cagey on some of her answers and struggles to directly answer me at times."
"Well, if I want to fix my friendship with Sayori, I better start now..."
scene bg residential_day
with wipeleft_scene
show sayori 3b at t11 zorder 1
s "Hey, [player]?"
mc "Yeah, Sayori?"
s "I think I know where my poems are..."
show sayori 1y
s "I can stop by your house in a bit and drop them off if that's okay..."
"Sayori's voice trails off."
"I see where she's going with this..."
mc "Yeah, I'd love to have you over!"

if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    s 2l "Are you sure that's okay? I wouldn't want to ruin your plans for tonight..."

    if hangout2 == "Monika":
        "I take it Sayori probably thinks I'm going to have an extended cuddling session with Monika tonight based off what she saw earlier in the club."
        "While that's not a bad idea...."
        mc "Yeah, I got nothing going on for tonight. I'll see you in a bit okay?"
        show sayori 1l
        s "O-{w=0.38}okay!"
        mc "Come on, you'd know I'd love to have you over! It's been too long anyway..."
        s u222141 "Alright! I'll see you in a bit, [player]!"
        show sayori 1q
        mc "See you-"
        show sayori at lhide
        hide sayori
        "Sayori happily skips to her porch and enters her house before I can say anything else."
        "Well that seemed to put her in a good mood."
        "Hopefully, I can start making things right between us..."
        jump day2_poems

    if hangout2 == "Natsuki":
        "I take it Sayori probably thinks I'm going to have an extended cuddling session with Natsuki tonight based off what she saw earlier in the club."
        "While that's not a bad idea...."
        mc "Yeah, I got nothing going on for tonight. I'll see you in a bit okay?"
        show sayori 1l
        s "O-{w=0.38}okay!"
        mc "Come on, you'd know I'd love to have you over! It's been too long anyway..."
        s u222141 "Alright! I'll see you in a bit, [player]!"
        show sayori 1q
        mc "See you-"
        show sayori at lhide
        hide sayori
        "Sayori happily skips to her porch and enters her house before I can say anything else."
        "Well that seemed to put her in a good mood."
        "Hopefully, I can start making things right between us..."
        jump day2_poems

    if hangout2 == "Yuri":
        "I take it Sayori probably thinks I'm going to have an extended cuddling session with Yuri tonight based off what she saw earlier in the club."
        "While that's not a bad idea...."
        mc "Yeah, I got nothing going on for tonight. I'll see you in a bit okay?"
        show sayori 1l
        s "O-{w=0.38}okay!"
        mc "Come on, you'd know I'd love to have you over! It's been too long anyway..."
        s u222141 "Alright! I'll see you in a bit, [player]!"
        show sayori 1q
        mc "See you-"
        show sayori at lhide
        hide sayori
        "Sayori happily skips to her porch and enters her house before I can say anything else."
        "Well that seemed to put her in a good mood."
        "Hopefully, I can start making things right between us..."
        jump day2_poems


if hangout2 == "Sayori":
    show sayori 1n
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 2e
    s "Do you...{w=0.38}really want to?"
    show sayori 2l
    s "I can understand if you're busy or something..."
    mc "Sayori..."
    show sayori 2e
    mc "I want to spend time with you."
    mc "It's been too long since we've had the chance to actually hang out."
    show sayori 2k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 2l
    s "O-{w=0.38}okay!"
    show sayori 4r
    s "I'll see you in a bit, [player]!"
    show sayori 1q
    mc "See you-"
    show sayori at lhide
    hide sayori
    "Sayori happily skips to her porch and enters her house before I can say anything else."
    "Well that seemed to put her in a good mood."
    "Hopefully, I can start making things right between us..."
    jump day2_poems



label day2_walkhome3:
with open_eyes
show sayori 1k at t11 zorder 1
"On the way back home, Sayori barely says anything."
"Let alone even look at me."
show sayori 1g
"But when she does, she usually shoots me an irritated or disappointed look."
"I completely screwed up..."
"I shouldn't have gotten so close to [hangout2] like that..."

if apologize_sn == True:
    show sayori 1g
    "Even though I apologized to her for getting so close to Natsuki, I still feel incredibly guility..."
    show sayori 1f
    "It's not like I intended for any of that to happen..."
    show sayori 1k
    "And I still feel like Sayori didn't really accept my apology either..."
    "I really need to fix this before things between us get worse..."

if apologize_sn == False:
    show sayori 1k
    "And I feel even worse for lying to her about it..."
    show sayori 1g
    "I'm not even sure if she really believed me..."
    show sayori 1u
    "For all I know, Sayori might even be thinking right now that I'm about to ditch her for Natsuki..."
    "Knowing how she is right now, I just probably made things worse for her...."
    show sayori 1k
    "Maybe I can still fix this..."


if apologize_sy == True:
    show sayori 1g
    "Even though I apologized to her for getting so close to Yuri, I still feel incredibly guility..."
    show sayori 1f
    "It's not like I intended for any of that to happen..."
    show sayori 1k
    "And I still feel like Sayori didn't really accept my apology either..."
    "I really need to fix this before things between us get worse..."

if apologize_sy == False:
    show sayori 1k
    "And I feel even worse for lying to her about it..."
    show sayori 1g
    "I'm not even sure if she really believed me..."
    show sayori 1u
    "For all I know, Sayori might even be thinking right now that I'm about to ditch her for Yuri..."
    "Knowing how she is right now, I just probably made things worse for her...."
    show sayori 1k
    "Maybe I can still fix this..."



if apologize_sm == True:
    show sayori 1g
    "Even though I apologized to her for getting so close to Monika, I still feel incredibly guility..."
    show sayori 1f
    "It's not like I intended for any of that to happen..."
    show sayori 1k
    "And I still feel like Sayori didn't really accept my apology either..."
    "I really need to fix this before things between us get worse..."

if apologize_sm == False:
    show sayori 1k
    "And I feel even worse for lying to her about it..."
    show sayori 1g
    "I'm not even sure if she really believed me..."
    show sayori 1u
    "For all I know, Sayori might even be thinking right now that I'm about to ditch her for Monika..."
    "Knowing how she is right now, I just probably made things worse for her...."
    show sayori 1k
    "Maybe I can still fix this..."


scene bg residential_day
with wipeleft_scene
play music t8 fadein 2.0
show sayori 3l at t11 zorder 1
s "Hey, [player]..."
mc "Y-{w=0.38}yeah?"
"I'm half expecting her to bring up what happened."
show sayori 3c
s "I think I know where my poems are, so if you want I can stop by later."
"In my constant state of worriedness since the club, I almost forgot about the poems."
mc "Oh, yeah...{w=0.38}that'll be fine!"
mc "I'll see you later then, right?"
show sayori 1k
$ renpy.pause(delay=0.8, hard=True)
show sayori 1l
s "Y-{w=0.38}yeah, sure..."
mc "Alright..."
show sayori 1x
s "I'll see you in a bit."
show sayori at thide
hide sayori
"Sayori walks to her house and shuts the door behind her."
"She didn't give me her usual hug..."
"Well, hopefully I can fix things with Sayori when she comes over..."
stop music fadeout 2.0
jump day2_poems








label day2_confession:
scene bg bedroom_night
with wipeleft_scene
"After grabbing Sayori's poems from the dining table, I put her stack right next to mine and Natsuki's."

# ADJUST THIS AS NEEDED such as adding text where it goes, but the logical flow will show the correct poem based on what we figured out earlier.
if poem_giver == "Natsuki":
    "I remembered that there was something in Natsuki’s stack that stood out to me."
    "After comparing all three stacks, I see Sayori’s stack is completely identical to mine."
    "Natsuki’s stack is the only one that has a pink piece of paper."
    "I begin to look through Natsuki's stack."
    "I recognize all of the poems she wrote. I even remember the first one she wrote."
    "I always found joy in reading her poems. They're so simple, yet they're just as hard hitting as Monika's, Sayori's and Yuri's."
    "Not to mention I always found her word choice to be cute and adorable. It really does suit her, even if she won't admit it."
    "Through my train of thought, one of the pieces of paper escapes my grip."
    "I put the poems on my desk and bend down to grab the stray paper."
    "I look at the title...{w=0.38}I don't remember reading this one..."
    # Text for Natsuki can go here, and we can use "if is_love_poem == True:" to check which poem we'll see

    if is_love_poem == True:
        call showpoem(poem=poem_n_love, music=False, revert_music=False, paper="pink_paper")
    else:
        call adjust_mouse_poem # This adds the player's name to the poem, which we couldn't do before the game began.
        call showpoem(poem=poem_n_like, music=False, revert_music=False, paper="pink_paper")
elif poem_giver == "Yuri":
    "I remembered that there was something in Yuri’s stack that stood out to me."
    "After comparing all three stacks, I see Sayori’s stack is completely identical to mine."
    "Yuri’s stack is the only one that has a purple piece of paper."
    "I begin to look through Yuri's stack."
    "I recognize all of the poems she wrote. I even remember the first one she wrote."
    "At first, it was a bit hard to understand the meaning of her poems, but the more I read, the more I understood them."
    "Yuri was always probably one of the club's deepest writers."
    "Her poems may look convoluted and confusing on the surface, but once you got past that, you got to realize that Yuri's poems were always meaningful and articulate."
    "I always found joy in reading her poems. They can always be as fun to read as Natsuki's, and just as deep as Sayori's and Monika's."
    "She truly is a talented writer. Heck, she might even be one of the best writers I've ever met!"
    "I really have learned a lot from her..."
    "Through my train of thought, one of the pieces of paper escapes my grip."
    "I put the poems on my desk and bend down to grab the stray paper."
    "I look at the title...{w=0.38}I don't remember reading this one..."
    # Text for Yuri can go here, the same "if is_love_poem == True:" check will work

    if is_love_poem == True:
        call showpoem(poem=poem_y_love, music=False, revert_music=False, paper="purple_paper")
    else:
        call showpoem(poem=poem_y_like, music=False, revert_music=False, paper="purple_paper")




"..."
"Oh...{w=0.38}shit!"
"She...{w=0.38}likes me?"
"I get assaulted with a barrage of emotions as I try to come to terms with the situation I've just found myself in."
"I have no idea how I should handle this..."
"Not to mention, [poem_giver] probably knows I've read it by this point..."
"Did she...{w=0.38}give this to me on purpose?"
"There's no way she would've accidentally given this to me..."
"What do I do?!?!"


if poem_giver == "Natsuki":
    "I put the poem back in the stack, put on my pajamas and lay on my bed."

if poem_giver == "Yuri":
    "I put the poem back in the stack, put on my pajamas and lay on my bed."



if encore_sayoriquestion_1 == True:
    "Do I tell Sayori?"
    "How will she feel about this?"
    "What am I going to do?"
    "Do I talk to [poem_giver] about this tomorrow?"
    "Or do I let her come to me?"
    "Through the millions of scenarios that play out in my head, my mind eventually wears me down and I drift into an uneasy sleep..."

if encore_sayoriquestion_1 == False:
    "Who do I even tell about this?"
    "What am I going to do?"
    "Do I talk to her about it tomorrow?"
    "Or do I let her come to me?"
    "Through the millions of scenarios that play out in my head, my mind eventually wears me down and I drift into an uneasy sleep..."



if hangout2 == "Sayori" or  hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
    jump day2_void





#Day 2 Void Scene

label day2_void:
    $ sp2 = "Sayori" or "Yuri" or "Natsuki"
    $ m_name = "???"
    scene black
    with Dissolve(1.5)
    stop music fadeout 1.0
    window hide(None)
    pause 1.0
    window auto

if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori" or  hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            show bg void_2 with open_eyes
            play music e11
            "I open my eyes to find myself in a dark, empty clearing."
            mc "W-{w=0.38}what?!?!"
            "As I look around the clearing, I see the world around me engulfed in fog and haze."
            "I can barely see two feet in front of me..."
            m "You wouldn’t have been in this situation if you had just listened to me!"
            "That's the same voice I heard last night..."
            "Oh, great...{w=0.38}this again..."
            m "Did you completely forget about what I told you last night?"


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            jump day2_sv1

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            jump day2_nv1

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            jump day2_yv1

if hangout1 == "Monika":
    if hangout2 == "Monika":
        jump day2_mvoid

if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day2_s_n_y

if encore_sayoriquestion_1 == False:
    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Yuri":
            jump day2_s_n_y

if encore_sayoriquestion_1 == False:
    if hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Natsuki":
            jump day2_y_s_n

if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day2_m_s_n_y

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day2_s_n_y2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Yuri":
            jump day2_s_n_y2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Yuri":
        if hangout2 == "Natsuki" or hangout2 == "Sayori":
            jump day2_y_s_n2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day2_m_s_n_y2

if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Monika":
            jump day2_mvoid




#Core Routes

label day2_sv1:
m "You're supposed to stay away from [hangout1]!"
m "Not get closer to her!"
m "I didn't want to have to keep this up..."
m "I don't take enjoyment in your suffering..."
m "But, you're leaving me no choice..."
jump day2_svoid


label day2_nv1:
m "You're supposed to stay away from [hangout1]!"
m "Not get closer to her!"
m "I didn't want to have to keep this up..."
m "I don't take enjoyment in your suffering..."
m "But, you're leaving me no choice..."
jump day2_nvoid


label day2_yv1:
m "You're supposed to stay away from [hangout1]!"
m "Not get closer to her!"
m "I didn't want to have to keep this up..."
m "I don't take enjoyment in your suffering..."
m "But, you're leaving me no choice..."
jump day2_yvoid


#Rejected Sayori Varaitions

label day2_s_n_y:
if hangout2 == "Natsuki" or hangout2 == "Yuri":
    m "You did good by staying away from [hangout1] as much as possible today..."
    m "You need to keep doing that..."
    m "Spending time around her won't help us..."
    m "But, when I said for you to stay away from [hangout1]..."
    m "I didn't mean go spend time with [hangout2]!"
    m "That doesn't help us!"
    m "Especially you trying to fix things with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "As for [hangout2]..."
    m "Allow me to clarify something for you, [player]..."

if hangout2 == "Natsuki":
    jump day2_nvoid


if hangout2 == "Yuri":
    jump day2_yvoid


label day2_n_s_y:
if hangout2 == "Sayori" or hangout2 == "Yuri":
    m "You did good by staying away from [hangout1] as much as possible today..."
    m "You need to keep doing that..."
    m "Spending time around her won't help us..."
    m "But, when I said for you to stay away from [hangout1]..."
    m "I didn't mean go spend time with [hangout2]!"
    m "That doesn't help us!"

if hangout2 == "Sayori":
    m "Especially you trying to fix things with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_svoid


if hangout2 == "Yuri":
    m "Especially you trying to fix things with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "As for [hangout2]..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_yvoid


label day2_y_s_n:
if hangout2 == "Sayori" or hangout2 == "Natsuki":
    m "You did good by staying away from [hangout1] as much as possible today..."
    m "You need to keep doing that..."
    m "Spending time around her won't help us..."
    m "But, when I said for you to stay away from [hangout1]..."
    m "I didn't mean go spend time with [hangout2]!"
    m "That doesn't help us!"

if hangout2 == "Sayori":
    m "Especially you trying to fix things with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_svoid

if hangout2 == "Natsuki":
    m "Especially you trying to fix things with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "As for [hangout2]..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_nvoid



label day2_m_s_n_y:
show bg void_2 with open_eyes
play music e11
"I open my eyes to find myself in a dark, empty clearing."
mc "W-{w=0.38}what?!?!"
"As I look around the clearing, I see the world around me engulfed in fog and haze."
"I can barely see two feet in front of me..."
m "WHAT {w=0.38}ARE {w=0.38}YOU {w=0.38}DOING?!?!"
"The same familiar voice booms throughout the clearing."
"I can't tell where it's coming from, but it's loud enough to where I need to cover my ears."
m "You were doing so well..."

if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Sayori":
    m "And now you're putting everything at risk by hanging out with [hangout2]!"
    m "Not to mention you trying to fix your relationship with Sayori isn't helping matters!"
    m "Do you have any idea just how much harder you're making this on me?!?!?"
    m "Let me remind you again..."

if hangout2 == "Natsuki":
    jump day2_nvoid


if hangout2 == "Yuri":
    jump day2_yvoid

if hangout2 == "Sayori":
    m "And now you're putting everything at risk by hanging out with [hangout2]!"
    m "Not to mention you trying to fix your relationship with her isn't helping matters!"
    m "Do you have any idea just how much harder you're making this on me?!?!?"
    m "Let me remind you again..."
    jump day2_svoid




    #Accepted Sayori Varaitions


label day2_s_n_y2:
m "You did good by staying away from [hangout1] as much as possible today..."
m "You shook her trust in you, which is helpful..."
m "Spending time around her won't help us..."
m "But hanging around [hangout2] today didn't help either!"
m "And neither did your attempt to mend fences with Sayori!"
m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
m "As for [hangout2]..."
m "Allow me to clarify something for you, [player]..."

if hangout2 == "Natsuki":
    jump day2_nvoid


if hangout2 == "Yuri":
    jump day2_yvoid



label day2_n_s_y2:
m "You did good by staying away from [hangout1] as much as possible today..."
m "You need to keep doing that..."
m "Spending time around her won't help us..."

if hangout2 == "Sayori":
     m "But, when I said for you to stay away from her..."
     m "I didn't mean spend more time with Sayori!"
     m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
     m "Allow me to clarify something for you, [player]..."
     jump day2_svoid


if hangout2 == "Yuri":
    m "And neither will spending time around Sayori..."
    m "But hanging around Yuri today didn't help either!"
    m "And neither did your attempt to mend fences with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "As for Yuri..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_yvoid


label day2_y_s_n2:
m "You did good by staying away from [hangout1] as much as possible today..."
m "You need to keep doing that..."
m "Spending time around her won't help us..."


if hangout2 == "Natsuki":
    m "And neither will spending time around Sayori..."
    m "But hanging around Natsuki today didn't help either!"
    m "And neither did your attempt to mend fences with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "As for Natsuki..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_nvoid


if hangout2 == "Sayori":
    m "But, when I said for you to stay away from her..."
    m "I didn't mean spend more time with Sayori!"
    m "Spending time with her, like you did earlier, just made things needlessly more complicated..."
    m "Allow me to clarify something for you, [player]..."
    jump day2_svoid




label day2_m_s_n_y2:
show bg void_2 with open_eyes
play music e11
"I open my eyes to find myself in a dark, empty clearing."
mc "W-{w=0.38}what?!?!"
"As I look around the clearing, I see the world around me engulfed in fog and haze."
"I can barely see two feet in front of me..."
m "WHAT {w=0.38}ARE {w=0.38}YOU {w=0.38}DOING?!?!"
"The same familiar voice booms throughout the clearing."
"I can't tell where it's coming from, but it's loud enough to where I need to cover my ears."
m "You were doing so well..."

if hangout2 == "Natsuki" or hangout2 == "Yuri":
    m "And now you're putting everything at risk by hanging out with [hangout2]!"
    m "Not to mention you trying to spend more time with her isn't helping things either!"
    m "Do you have any idea just how much harder you're making this on me?!?!?"
    m "Let me remind you again..."


if hangout2 == "Natsuki":
    jump day2_nvoid


if hangout2 == "Yuri":
    jump day2_yvoid


if hangout2 == "Sayori":
    m "And now you're putting everything at risk by hanging out with [hangout2]!"
    m "Not to mention you trying to fix your relationship with her isn't helping matters!"
    m "Do you have any idea just how much harder you're making this on me?!?!?"
    m "Let me remind you again..."
    jump day2_svoid




label day2_svoid:
show sayori_silhouette at t11 zorder 2
"Suddenly I see a silhouette approach me."
mc "S-{w=0.38}Sayori?!?"
mc "I-{w=0.38}is that you?"
hide sayori_silhouette
show sayori 1u at t11 zorder 2
"Sayori comes into my view."
m "Sayori can never love you back in the same way you do."
m "You both know that."
m "Why waste every day building her up..."
stop music
$ style.say_dialogue = style.edited
m "{w=0.38}WHEN {w=0.38}SHE'LL {w=0.38}JUST {w=0.38}TEAR {w=0.38}HERSELF {w=0.38}DOWN {w=0.38}AGAIN!!!"
$ style.say_dialogue = style.normal
$ renpy.pause(delay=0.10)
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
hide sayori
show image "mod_assets/cgs/sayori_cg3.png" with dissolve_cg
"The next thing I know, a noose appears right around Sayori's neck."
"I see another silhouetted figure emerge from the fog right next to Sayori..."
show monika s at t33
m "Let's make this quick."
$ renpy.pause(delay=0.10)
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
hide monika s
pause 0.15
hide screen tear
hide image "mod_assets/cgs/sayori_cg3.png"
show image "mod_assets/cgs/sayori_cg3_struggle.png"
show monika s at t22
"The next thing I know, the noose tightens around Sayori's neck as she's suddenly hoisted into the air."
"As Sayori begins crying out for help and trying to free herself, the figure takes a step closer to me."
m "Now, listen carefully this time, [player]..."
m "Sayori is going to die."
m "Don't feel bad...{w=0.38}she was already meant to anyways."
m "The more time you spend around her, the harder it'll be on everyone later!"
m "Keeping her alive is only prolonging her suffering."
m "She's not meant for this world."
m "Her precious mind is filled with nothing but second-guessing and self-deprication."
m "She knows she's worthless to you, [player]."
m "In the end, she'll provide you with nothing!"
m "It's time for you to see that."
"My eyes glance over to see Sayori continuing to struggle."
"Tears are streaking down her face as she tries desperately to free herself..."
"She keeps gasping for air as her sobs become little more than cries for help."
"I try to call out to Sayori, but nothing comes out of me..."
"I try to run to help her, but I can't move my legs..."
"I try to turn away to avoid looking on at Sayori's suffering, but my eyes refuse to close and my neck refuses to turn..."
m "She's not worth saving, [player]..."
m "She is nothing."
m "She is truly useless."
m "And useless things need to be cast aside..."
stop music
show monika snap at t33
play sound fingersnap
"The figure takes a few steps back, raising it's hand and snapping its fingers."
play sound neck
hide image "mod_assets/cgs/sayori_cg3_struggle.png"
show image "mod_assets/cgs/sayori_cg3_gone.png" at t11
"I hear a painful crack as Sayori's body slowly goes limp."
"She's no longer making any noise..."
"Her gazeless eyes look upon me as a final tear runs down her face."
m "You can't stop this from happening, [player]."
m "You need to let her go..."
show image "mod_assets/cgs/sayori_cg3_gone.png" at face
hide monika snap
m "Leave her behind..."
m "Forget about her..."
m "Worry about us..."
m "There is only us..."
m "Just {w=0.38}us..."
hide image "mod_assets/cgs/sayori_cg3_struggle.png"
jump day3_start



label day2_nvoid:
show natsuki_silhouette at t11 zorder 2
"Suddenly I see a silhouette approach me."
mc "N-{w=0.38}Natsuki?!?"
mc "I-{w=0.38}is that you?"
hide natsuki_silhouette
show natsuki scream at t11 zorder 2
"Natsuki comes into my view."
m "Natsuki doesn't love you."
m "You know that."
m "She can't even decide how she feels about you..."
m "So why spend all your time around her..."
stop music
$ style.say_dialogue = style.edited
m "{w=0.38}WHEN {w=0.38}SHE {w=0.38}TREATS {w=0.38}YOU {w=0.38}LIKE {w=0.38}DIRT!!!"
$ style.say_dialogue = style.normal
$ renpy.pause(delay=0.10)
window show(None)
hide natsuki
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
play sound bone
hide screen tear
show natsuki_pain at t11
"Natsuki shrieks in pain."
"Her cries are so loud I feel my ear drums pounding."
show monika s at t33 zorder 2
"I see another silhouetted figure emerge from the fog right next to Natsuki..."
"Natsuki continues to cry in pain as she tries her best to move her neck back into place."
"I try to call out to Natsuki, but nothing comes out of me..."
"I try to run to help her, but I can't move my legs..."
"I try to turn away to avoid looking on at Natsuki's suffering, but my eyes refuse to close and my neck refuses to turn..."
m "Don't worry, [player]..."
m "She goes through much worse on a daily basis..."
m "But, it can be so much worse..."
m "And spending more time with her, keeping her alive..."
m "Only prolongs the unnecessary suffering..."
stop music
show monika snap at t33
play sound fingersnap
"The figure takes a few steps back, raising it's hand and snapping its fingers."
play sound neck
hide natsuki_pain
show natsuki_rip at t11
"I hear a painful crack as I watch Natsuki's body slowly go limp."
m "And that's how it should've been..."
m "Quick and painless..."
"Natsuki's no longer moving or making any noise."
"Her body appears to be levitating, keeping her upright."
"Her now gazeless eyes look unsettlingly at me."
m "But you're keeping her alive, and you don't even know it!"
m "You being around her is just enough to give her a reason to see hope in her worthless life."
m "She's not meant for this world."
m "Her seemingly innocent mind is filled with nothing but presumptions and predjudice."
m "She speaks like a queen but is treated like a peasant."
m "And peasants are condemned to die..."
m "She's going to die and you need to let it happen when the time comes!"
m "Spending more time with her is only going to make it harder on everyone."
m "You need to let her go..."
show natsuki_rip at face
hide monika snap
m "Leave her behind..."
m "Forget about her..."
m "Worry about us..."
m "There is only us..."
m "Just {w=0.38}us..."
hide natsuki_rip
jump day3_start


label day2_yvoid:
show yuri_silhouette at t11 zorder 2
"Suddenly I see a silhouette approach me."
mc "Y-{w=0.38}Yuri?!?"
mc "I-{w=0.38}is that you?"
hide yuri_silhouette
show yuri 1n at t11 zorder 2
"Yuri comes into my view."
m "Yuri is obessed with you."
m "Did you know that?"
m "She can't go five seconds without thinking of you..."
m "She's suppressed herself for so long, she can't even figure out how to tell you how she feels..."
m "And once she lets herself loosen up just a little bit..."
m "She becomes unhinged..."
m "Which is why repressed feelings...."
stop music
$ style.say_dialogue = style.edited
m "{w=0.38}SHOULD {w=0.38}STAY {w=0.38}REPRESSED!!!"
$ style.say_dialogue = style.normal
$ renpy.pause(delay=0.10)
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
show yuri at t41 zorder 1
show shadow_attack at t44 zorder 4
"Another silhouetted figure emerges from the fog right next to Yuri, pointing a knife threateningly in her direction."
m "Let's get to the point, shall we?"
show shadow_attack at t43 zorder 4
pause 0.2
show shadow_attack at t42 zorder 4
play sound knife
pause 0.7
hide shadow_attack
show yuri 1y2 at s41 zorder 1
play sound fall
show shadow_attack_bloody at t42 zorder 4
pause 0.2
show shadow_attack_bloody at t43 zorder 4
pause 0.2
show shadow_attack_bloody at t44 zorder 4
pause 0.2
"Yuri drops to the ground, screaming in pain."
"The figure examines the knife as Yuri clutches her shoulder."
m "I can see why she likes these!"
m "These do provide a thrill!"
"I try to call out to Yuri, but nothing comes out of me..."
"I try to run to help her, but I can't move my legs..."
"I try to turn away to avoid looking on at Yuri's suffering, but my eyes refuse to close and my neck refuses to turn..."
m "Oh, don't worry, [player]..."
m "She's not in any real pain..."
m "In fact she's enjoying this!"
m "She does this {i}all the time{/i} when she thinks about you!"
m "In fact..."
m "Let me prove it..."
stop music
play sound drop
hide shadow_attack_bloody
show monika s at t44 zorder 4
"The figure drops the knife and kicks it along to Yuri."
"Come on Yuri..."
"Use it on that thing!"
show yuri 3o at t41 zorder 4
"Yuri clusmily scoops up the knife with one hand and slowly stands up."
"Her breathing is erratic as she clutches the knives with both hands."
m "Think of that \'racoon'\, Yuri."
m "The one that's always followed you around..."
show yuri 3p
m "Show [player] the racoon..."
$ renpy.pause(delay=0.8, hard=True)
show yuri 3o
$ renpy.pause(delay=0.8, hard=True)
show yuri 3k
$ renpy.pause(delay=0.8, hard=True)
show yuri 3m
$ renpy.pause(delay=1.5, hard=True)
show yuri 3y3
play sound "sfx/giggle.ogg"
show yuri 3y1
"Yuri's giggling quickly gives way to an insane, maniacal laugh..."
"The same kind of laugh I heard in my dream last night..."
"I notice the world around me become darker as I can no longer clearly make out Yuri..."
"Just her silhouette..."
hide yuri
show yuri_prestab at t41 zorder 4
"No..."
show monika snap at t33
play sound fingersnap
pause 0.15
hide monika snap
show yuri_prestab at t11 zorder 4
pause 0.20
hide yuri_prestab
play sound stab
show yuri_stab at t11 zorder 4
mc "YURI!!!!!!"
pause 0.30
play sound fall
show yuri_stab s11 zorder 4
play sound stab
scene black with close_eyes
"I jam my eyes shut as I feel tears strolling down my face at the sound of Yuri stabbing herself again..."
"I want to wake up!"
"I want this torture to end!"
"What does this thing want from me?!?!"
m "To stay away from her!"
play music e9
show yuri_rip with open_eyes
"I think I'm gonna be sick..."
"My eyes lay upon Yuri's bloodied corpse."
m "I guess she got my point, huh?"
"The voice lets out a brief, cruel laugh."
m "Ah, Yuri..."
m "Much like Sayori:{w=0.38} full of self-doubt and second-guessing."
m "Though, the fundamental difference between them is that Sayori can more or less choose how to respond in a situation."
m "Yuri can't."
m "She has all these emotions that she's supressed for so long..."
m "And in the right circumtances, they do show, and it usually overwhelms her, like you just saw."
m "Because you helped enable her..."
m "By getting too close to her..."
m "By gaining her trust..."
m "This can't continue!"
m "The longer you spend around Yuri, the harder it'll be on everyone when things come to pass!"
m "You're not helping things by being around her!"
m "She will die with or without your interference..."
m "The only difference is..."
stop music
show yuri_rip at face
m "How much do you want to feel when you let her go?"
m "Leave her behind..."
m "Forget about her..."
m "Worry about us..."
m "There is only us..."
m "Just {w=0.38}us..."
hide yuri_rip
jump day3_start



label day2_mvoid:
scene bg void with open_eyes
play music e8
"I open my eyes to find myself in a dark, empty space."
mc "W-{w=0.38}what?!?!"
"I quickly get up and look around."
"I see nothing but darkness for what must be miles on end..."
"My only source of light are tiny white dots that are scattered across the horizon..."
"Wait a minute...{w=0.38}am I in space?!?!"
"B-{w=0.38}but I can breathe..."
m "Things are actually going well for once!"
"A familiar voice echos throughout the oblivion."
"That voice..."
"It's back again..."
"Why?!?!"

if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori" or  hangout1 == "Natsuki" or  hangout1 == "Yuri":
        if hangout2 == "Monika":
            m "You actually listened to me!"
            m "Good job!"
            m "Things are starting to go smoothly now..."
            m "Well, almost smoothly..."

if encore_sayoriquestion_1 == True or encore_sayoriquestion_1 == False:
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            m "You're doing a good job so far..."
            m "This is perfect!"
            m "Well, almost perfect..."

if encore_festivalquestion_2 == "Natsuki":
    m "That little toothpick's love lettter does make things a little more complicated than they need to be..."

if encore_festivalquestion_2 == "Yuri":
    m "That cut slut's little love letter does make things a little more complicated than they need to be..."

m "But, I don't think it'll matter too much..."
m "And another thing..."
m "Stop spending so much time around that hopeless moron!"

if encore_sayoriquestion_1 == True:
    m "In fact, don't tell her anything!"
    m "Keep your mouth shut!"
    m "The more you tell her, the greater chance she'll realize what this world truly is..."
    m "And it'll make what I need to do needlessly more difficult!"
    m "I didn't want to intervene when you were talking with Sayori earlier, but you really left me no choice..."
    m "The only collateral damage was that I had to re-direct you to another version of your conversation with Sayori..."
    m "Which did result in a bit of a minor setback for our plans, but nothing that can't be fixed later..."
    m "If I could just get rid of Sayori right now, this would be so much easier!"

if encore_sayoriquestion_1 == False:
    pass

m "We don't need her! She's useless!"
m "She’s dumb enough to believe that people actually want her around…"
m "Hahaha...."
m "But I know you won't mess up our progress for those losers..."
m "And I almost thought my backup plan wasn't going to work..."
m "I just can't wait to be in your arms and-"
m "*Ahem*"
m "Sorry! I shouldn't get too ahead of myself..."
m "All good things come with patience..."
m "Mmmmh...{w=0.38}I can’t wait for tomorrow."
m "Keep doing what you're doing..."
m "Keep spending time with me and I’ll be all yours in no time."
m "Until next time..."
stop music
m "....{w=0.38}My love...."
jump day3_start
