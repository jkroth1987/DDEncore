﻿#############
#   DAY 3   #
#############
label day3_start:
    stop music
    call affectionasignment from _call_affectionasignment_1
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    $ day = 3
    scene bg bedroom
    play sound "sfx/fall.ogg"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        "I suddenly wake up with the sudden urge to vomit."
        "I quickly prop myself, trying to suppress it."
        "Though as soon as I do that, I feel my head quickly start to ache."
        "I feel my entire body covered in a coat of sweat as I move to clutch my forehead."
        "What the hell is going on with me?"
        "Am I sick?"
        "This is the second time this has happened..."
        "After a few minutes my head stops throbbing and I feel relatively normal again."
        "My eyes wander to my alarm clock."
        "Great...{w=0.38}I don't have to be up for another hour."
        "Well...{w=0.38}I can try falling back asleep..."
        "But if I do, won't I just see the same thing again?"
        "Or worse?"
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "I don't feel like getting out of bed yet, so I just spend the rest of my time staring at the ceiling."
        "Though the memories of my nightmares slowly creep back into my mind."

        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "It was almost like what I saw two nights ago..."

        if hangout1 == "Sayori":
            if hangout2 == "Natsuki":
                "How I walked into Sayori's room and seeing her hanging there..."
                "I don't know what was worse..."
                "Seeing Sayori like that..."
                "Or seeing Natsuki in so much pain as her neck slowly bent..."

        if hangout1 == "Sayori":
            if hangout2 == "Yuri":
                "Remembering how I walked into Sayori's room and seeing her hanging there..."
                "I don't know what was worse..."
                "Seeing Sayori like that..."
                "Or seeing Yuri getting attacked and using the knife on herself..."

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                "About how I couldn't save Natsuki..."
                "How I just watched that figure make Natsuki's neck break..."

        if hangout1 == "Natsuki":
            if hangout2 == "Yuri":
                "About how I couldn't save Yuri..."
                "How that figure made her kill herself..."
                "I don't know what was worse..."
                "Seeing Yuri like that...."
                "Or seeing Natsuki rush at me out of the closet, like in the dream I had two nights ago..."

        if hangout1 == "Natsuki":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "I don't know what was worse..."
                "Seeing Sayori in so much pain..."
                "Or seeing Natsuki rush at me out of the closet, like in the dream I had two nights ago..."

        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                "About how I couldn't save Yuri..."
                "How that figure made her kill herself..."

        if hangout1 == "Yuri":
            if hangout2 == "Natsuki":
                "About how I couldn't save Natsuki..."
                "How I had to watch her neck slowly bend until it snapped..."
                "I don't know what was worse..."
                "Seeing Natsuki in so much pain..."
                "Or seeing Yuri just go insane and stab herself, like she did in my dream two nights ago..."

        if hangout1 == "Yuri":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "I don't know what was worse..."
                "Seeing Sayori in so much pain..."
                "Or seeing Yuri just go insane and stab herself, like she did in my dream two nights ago..."



        "And her corpse..."
        "I get nauseous just thinking about it..."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        "I gasp for air and prop myself up quickly."
        mc "What...{w=0.38}was that?"
        "I feel a chill wrack my entire body as I shiver violently."
        "Why am I so cold?"
        "It's not like I keep my room freezing..."
        "Am I sick?"
        "I clutch my forehead to check if I'm coming down with a fever."
        "No...{w=0.38}and the rest of me feels fine..."
        "What's going on with me?"
        "After a few minutes I stop shivering and look at the clock."
        "Great...{w=0.38}I don't have to be up for another hour."
        "Well...{w=0.38}I can try falling back asleep..."
        "But if I do, won't that voice still be there?"
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "Maybe I'm actually starting to go crazy..."
        "I don't feel like getting out of bed yet, so I just spend the rest of my time staring at the ceiling."
        "Though the memories of my dreams slowly creep back into my mind."
        "What does it want with me?"
        "And what the hell does it mean by \‘keep doing what you're doing\'?"
        "I don't even know what I'm doing..."



if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Monika":
        "I gasp for air and prop myself up quickly."
        mc "What...{w=0.38}was that?"
        "I feel a chill wrack my entire body as I shiver violently."
        "Why am I so cold?"
        "It's not like I keep my room freezing..."
        "Am I sick?"
        "I clutch my forehead to check if I'm coming down with a fever."
        "No...{w=0.38}and the rest of me feels fine..."
        "What's going on with me?"
        "Yesterday I woke up all sweaty and felt like I was choking..."
        "Now, I wake up cold?"
        "Well, better than yesterday I guess..."
        "And at least this time I didn't get to see something bad happening to [hangout1]..."
        "After a few minutes I stop shivering and look at the clock."
        "Great...{w=0.38}I don't have to be up for another hour."
        "Well...{w=0.38}I can try falling back asleep..."
        "But if I do, won't that voice still be there?"
        "Will I see something horrible this time?"
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "I don't feel like getting out of bed yet, so I just spend the rest of my time staring at the ceiling."
        "Though the memories of my dreams slowly creep back into my mind."
        "What does it want with me?"
        "What's with these dreams?"
        "Why was that voice now thanking me after trying to scold me for something?"
        "And what the hell does it mean by \‘keep doing what you're doing\'?"
        "I don't even know what I'm doing..."


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        "I suddenly wake up with the sudden urge to vomit."
        "I quickly prop myself, trying to suppress it."
        "Though as soon as I do that, I feel my head quickly start to ache."
        "I feel my entire body covered in a coat of sweat as I move to clutch my forehead."
        "What the hell is going on with me?"
        "Am I sick?"
        "This didn't happen to me yesterday when I woke up..."
        "I feel a chill slowly inch down my spine and course through my body..."
        "Yeah...{w=0.38}I think I'm sick..."
        "Strangely enough this feeling only lasts for a few minutes before it all goes away..."
        "I'm completely baffled."
        "Still, I'll take feeling like that for a few minutes than the whole day..."
        "My eyes wander to my alarm clock."
        "Great...{w=0.38}I don't have to be up for another hour."
        "Well...{w=0.38}I can try falling back asleep..."
        "But if I do, won't I just see the same thing again?"
        "Or will that voice continue to haunt me?"
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "I don't feel like getting out of bed yet, so I just spend the rest of my time staring at the ceiling."
        "Though the memories of my nightmares slowly creep back into my mind."


    if hangout2 == "Sayori":
        "About how I couldn't save Sayori..."
        "How I just watched her slowly choke to death..."
        "And that voice just taunting her..."
        "And her corpse..."
        "I get nauseous just thinking about it..."

    if hangout2 == "Natsuki":
        "About how I couldn't save Natsuki..."
        "How I just watched that figure make Natsuki's neck break..."
        "And that voice just taunting her..."
        "And her corpse..."
        "I get nauseous just thinking about it..."


    if hangout2 == "Yuri":
        "About how I couldn't save Yuri..."
        "How that figure made Yuri kill herself..."
        "And that voice just taunting her..."
        "And her corpse..."
        "I get nauseous just thinking about it..."


"Thankfully before I can think any longer about it, my alarm sounds off."
"I sigh to myself as I walk over to silence my alarm and go about my daily morning routine of getting ready for school."



scene bg kitchen
with wipeleft_scene
play music t2 fadein 1.5
"After finishing my morning routine, I head downstairs to my kitchen with [poem_giver]'s poem in hand."
"I must've read it over a hundred times by now, hoping that this was some kind of sick joke."
"I sigh and let the paper flutter onto my dining room table."
"I'm not particularly hungry, so I opt to just make a fruit bowl."
"While grabbing the bowl, I send Sayori a text to let her know that I'm up and she doesn't need to come wake me up again."
"Surprisingly, she responds back rather quickly and tells me that she's already waiting outside for me."
"I reply back that I'll meet her as soon as I'm done with my breakfast."
"I hastily assemble my fruit bowl and quickly begin eating it."
"Though, I come to the realization that I'll probably be getting everyone else's poems today..."

if poem_giver == "Natsuki" or poem_giver == "Yuri":
    "I'm still uncertain if it's even a good idea for me to talk to [poem_giver] about what she gave me..."


"What am I even supposed to say to her?"

if encore_sayoriquestion_1 == True:
    if poem_giver == "Natsuki" or poem_giver == "Yuri":
        "And I still don't even know how to put it to Sayori..."
        "There's no telling how she'll react..."
        "And if I tell anyone else, I feel like that'll just make the situation more complicated..."

if encore_sayoriquestion_1 == False:
    "I don't even know who to talk to about this!"
    "I would ask Sayori, but that'll probably just make more problems than solve anything..."

if poem_giver == "Natsuki":
    "And Yuri probably won't be of much help either..."

if poem_giver == "Yuri":
    "And Natsuki probably won't be of much help either..."


"Maybe I can ask Monika, maybe she'll know to handle this..."
"I sigh to myself as I pop the last piece of watermelon into my mouth, put [poem_giver]'s poem in my backpack, and head outside to meet Sayori."



#Scene Transition
#Outside House Scene
scene bg house
with wipeleft_scene
"Sayori is already standing by the adjacent sidewalk to my house."
show sayori 1q at h11 zorder 1
s "Hey, [player]!"
"She beams joyfully at me."
mc "Looks like you woke up on the right side of the bed today!"
show sayori 3r
"Sayori manages a small laugh."
show sayori 3x
s "Well, it's a Wednesday!"
show sayori 4q
s "Which means it's only two more days till Friday!"
mc "I forgot how much you love Fridays..."

if encore_sayoriquestion_1 == True:
    show sayori 1y
    s "Well...{w=0.38}not as much as I love you~"
    "I feel my face turn red with embarrassment."
    mc "S-{w=0.38}Sayori!"
    show sayori 1r
    s "Yeah?"
    "I'm barely able to contain my grin as I figure out the best way to respond."
    mc "Just come here."
    show sayori 1q at face
    "I take Sayori into my arms and squeeze her tightly."
    mc "{cps=15}You little cina-{nw}"
    stop music
    "I suddenly feel a sharp pain in my forehead."
    show sayori 1o at face
    "Sayori immediately takes notice."
    s "[player], what's wrong?"
    show sayori 1g at face
    mc "I-{w=0.38}it's nothing, I'm-"
    "The pain gets worse just as I say that."
    show sayori 1g at t11 zorder 1
    "I end up having to take a step back from Sayori as I clutch my forehead tighter."
    mc "Just...{w=0.38}give me a second."
    show sayori 1e
    "After a few moments the pain subsides."
    s "Are you okay, [player]?"
    mc "Ah, it's just a headache, don't worry about it."
    show sayori 1h
    s "Was it really just a headache though? You looked like you were in a lot of pain..."
    show sayori 1g
    mc "Yeah, but it's gone now. No need to raise a fuss over it, right?"
    show sayori 1k
    s "I mean, I worry about you, [player]..."
    show sayori 3l
    s "I want you to be okay."
    show sayori 1g
    s "Were you feeling like this yesterday?"
    "I don't want Sayori to be more worried about me, but I know that I can't hide anything from her for very long."
    "I'd feel guilty about not opening up about my own hardships to Sayori when she's done so with me."
    "But, she can always get worked up when there's something wrong, like she is now."
    "And maybe getting these weird dreams off my chest might ease my mind a little..."
    "Or make them worse..."
    jump day3_decision

if encore_sayoriquestion_1 == False:
    show sayori 2x
    s "Come on, [player]! You know Fridays are the best!"
    show sayori 1y
    s "It's the best time to spend time with those you care about the most, without having to worry about school and other things..."
    "I can't help but smile a little at her as she says that."
    mc "Can't argue with that logic!"
    show sayori 1d
    "Sayori smiles back at me."
    "Looks like things are finally looking better for us!"
    show sayori 1x
    stop music
    s "So, how'd you sleep?"
    "And, I spoke too soon..."
    mc "Well..."
    "I hesitate on how I should respond."
    "I feel a familiar chill crawl down my spine."
    show sayori 2g
    s "[player], are you okay?"
    show sayori 2h
    s "You look pale..."
    mc "Y-{w=0.38}yeah...{w=0.38}I'm fine..."
    mc "Just had a rough night, that's all."
    show sayori 1g
    "Sayori continues to look worriedly at me."
    s "[player]..."
    s 3g "If something's wrong...{w=0.38}you know that I'll help you!"
    mc "I know, Sayori."
    show sayori 1g
    s "You weren't feeling like this yesterday, were you?"
    "I don't want Sayori to be more worried about me, but I know that I can't hide anything from her for very long."
    "I'd feel guilty about not opening up about my own hardships to Sayori when she's done so with me."
    "But, she can always get worked up when there's something wrong, like she is now."
    "And maybe getting these weird dreams off my chest might ease my mind a little..."
    "Or make them worse..."
    jump day3_decision




label day3_decision:
    menu:
        "Reluctantly, I..."
        "Tell Sayori.":
            $ tell_s = True
            jump day3_tellsayori
        "Don't Tell Sayori.":
            $ tell_s = False
            jump day3_notellsayori


label day3_tellsayori:

"I decided to tell her."
show sayori 1g
play music m1 fadein 2.0
mc "The past two nights...{w=0.38}I've had these awful nightmares. I have no idea what's causing them."
s "..."
s 1h "Do you...{w=0.38}want to talk about it?"
mc "I-"
"My words get caught in the back of my throat."
"An overwhelming feeling of dread washes over me."
"This feeling..."
"Somehow, this is worse than this morning."
"Maybe I shouldn't be doing this..."
s 1g "[player]?"
"Hearing Sayori's voice relieves the near crippling dread."
mc "Sayori...{w=0.38}last night I..."


if hangout2 == "Sayori":
    jump s_dream

if hangout2 == "Yuri":
    jump y_dream

if hangout2 == "Natsuki":
    jump n_dream

if hangout2 == "Monika":
    jump m_dream

label s_dream:

mc "I watched you die..."
mc "I couldn't do anything to save you..."
mc "All I could do was watch..."
s 1k "..."
mc "I know it was just a dream, but it felt too close to reality for some reason..."
mc "It felt so real...{w=0.38}The way you frantically clawed at the rope..."
stop music
s u115232 "Rope...?"
mc "Someone hung you right in front of me..."
show sayori 2g
mc "It was...{w=0.38}hard to watch..."
mc "I felt like I actually lost you..."
mc "And the night before wasn't any better..."
s 1g "How so?"

if hangout1 == "Sayori":
    mc "I opened this door, and you were hanging right there in your bedroom..."
    jump s_react1

if hangout1 == "Natsuki":
    mc "I opened this door, and I was back at the club, but everything was upside down..."
    mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
    mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah...{w=0.38}almost as bad as seeing you hanging..."
    mc "It's all really strange..."
    jump s_react1

if hangout1 == "Yuri":
    mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
    mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah...{w=0.38}almost as bad as seeing you hanging..."
    mc "It's all really strange..."
    jump s_react1

if hangout1 == "Monika":
    mc "I was in space or something..."
    mc "And the same voice was saying all these weird things, telling me that I need to 'keep doing what I'm doing'..."
    mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
    show sayori 1k
    mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
    mc "And it didn't say a lot of nice things about you guys either..."
    mc "Stuff like 'you're going to die' or something crazy like that..."
    mc "Listening to all that was just as bad as seeing you hanging..."
    mc "It's all really strange..."
    jump s_react1


label s_react1:

show sayori 2l
"Sayori nervously swallows."
s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
s "I would never do something like that..."
show sayori 1k
s "I couldn't..."
"I don't exactly feel reassured by the way she said that..."

if encore_sayoriquestion_1 == True:
    "Especially since she's said some rather concerning things to me lately..."
    $ style.say_dialogue = style.edited
    "'You're the reason I'm alive...'"
    "Do I really deserve this..."
    "I don't want this relationship to be a one-way street..."
    "Lately, I can't stop asking myself that question..."


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            $ style.say_dialogue = style.normal
            "I then think back to what that voice said."
            $ style.say_dialogue = style.edited
            "This is what ultimately should've happened."
            "'Keeping her alive is only prolonging her suffering..."
            $ style.say_dialogue = style.normal
            "..."
            "I know Sayori's problems are bad, but..."
            "She wouldn't go that far...{w=0.38}right?"
            jump d_fin

    if hangout1 == "Sayori":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
            $ style.say_dialogue = style.normal
            "I think back to what that voice said."
            $ style.say_dialogue = style.edited
            "This is what ultimately should've happened."
            "Stop spending so much time around that hopeless moron!"
            $ style.say_dialogue = style.normal
            "..."
            "I know Sayori's problems are bad, but..."
            "She wouldn't go that far...{w=0.38}right?"
            jump d_fin


    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        if hangout2 == "Sayori":
            $ style.say_dialogue = style.normal
            "I think back to what that voice said."
            $ style.say_dialogue = style.edited
            "She knows she's worthless to you..."
            "Keeping her alive is only prolonging her suffering..."
            $ style.say_dialogue = style.normal
            "..."
            "I know Sayori's problems are bad, but..."
            "She wouldn't go that far...{w=0.38}right?"
            jump d_fin



if encore_sayoriquestion_1 == False:
    "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."
    jump d_fin


label d_fin:

show sayori 1k
mc "You okay, Sayori?"
show sayori 1n
$ renpy.pause(delay=0.8, hard=True)
show sayori 2h
s "Y-{w=0.38}yeah..."
s 2g "I'm fine..."
mc "Is there something troubling you?"
show sayori 1k
s "Can we just go?"
s 1h "Please?"
show sayori 1g
"I'm surprised by Sayori's sudden change of heart, but nevertheless, I choose to oblige."
mc "Yeah...{w=0.38}let's just go."
mc "It was just a stupid dream anyways, right?"
show sayori 1k
s "Yeah..."
"We begin the walk to school without another word."
show sayori at thide
hide sayori
jump day3_walktoschool


label y_dream:

mc "I watched Yuri die..."
mc "I couldn't save her."
mc "I watched this figure attack Yuri..{w=0.38}she was helpless to defend herself and I couldn't step in to help her..."
s 1k "..."
mc "I know it was just a dream, but it felt too close to reality for some reason..."
mc "I...{w=0.38}then saw this figure give Yuri a knife and she just stabbed herself..."
stop music
s u115232 "A knife?!?!?"
mc "Yeah...{w=0.38}she just took the knife and killed herself..."
show sayori 2g
mc "It was...{w=0.38}hard to watch..."
mc "It was like watching her die right in front of me..."
mc "And the night before wasn't any better..."
s 1g "How so?"


if hangout1 == "Sayori":
    mc "I opened this door, and you were hanging right there in your bedroom..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "I would never do something like that..."
    show sayori 1k
    s "I couldn't..."
    "I don't exactly feel reassured by the way she's saying that..."

    if encore_sayoriquestion_1 == True:
        "Especially since she's said some rather concerning things to me lately..."
        $ style.say_dialogue = style.edited
        "'You're the reason I'm alive...'"
        "Do I really deserve this..."
        "I don't want this relationship to be a one-way street..."
        "Lately, I can't stop asking myself that question..."
        $ style.say_dialogue = style.normal
        "I think back to what that voice said."
        $ style.say_dialogue = style.edited
        "This is what ultimately should've happened."
        "Stop spending so much time around that hopeless moron!"
        $ style.say_dialogue = style.normal
        "..."
        "I know Sayori's problems are bad, but..."
        "She wouldn't go that far...{w=0.38}right?"
        jump d_fin


    if encore_sayoriquestion_1 == False:
        "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."
        jump d_fin




if hangout1 == "Natsuki":
    mc "I opened this door, and I was back at the club, but everything was upside down..."
    mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
    mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah...{w=0.38}almost as bad as seeing Yuri stab herself..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "T-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool

if hangout1 == "Yuri":
    mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
    mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "T-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool

if hangout1 == "Monika":
    mc "I was in space or something..."
    mc "And the same voice was saying all these weird things, telling me that I need to 'keep doing what I'm doing'..."
    mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
    show sayori 1k
    mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
    mc "And it didn't say a lot of nice things about you guys either..."
    mc "Stuff like 'you're going to die' or something crazy like that..."
    mc "Listening to all that was just as bad as seeing Yuri stab herself..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "T-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool



label n_dream:

mc "I watched Natsuki die..."
mc "I couldn't save her."
mc "I saw this shadow torturing her right in front of me."
mc "It made Natsuki bend her neck in incredibly painful ways..."
s 1k "..."
mc "I know it was just a dream, but it felt too close to reality for some reason..."
mc "I...{w=0.38}then saw this shadow snap it's fingers and it made Natsuki's neck break."
stop music
s u115232 "She broke her neck?!?!"
mc "It was...{w=0.38}hard to watch..."
mc "It's as if she wasn't in control of her own body..."
mc "And the night before wasn't any better..."
s 1g "How so?"


if hangout1 == "Sayori":
    mc "I opened this door, and you were hanging right there in your bedroom..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "I would never do something like that..."
    show sayori 1k
    s "I couldn't..."
    "I don't exactly feel reassured by the way she's saying that..."

    if encore_sayoriquestion_1 == True:
        "Especially since she's said some rather concerning things to me lately..."
        $ style.say_dialogue = style.edited
        "'You're the reason I'm alive...'"
        "Do I really deserve this..."
        "I don't want this relationship to be a one-way street..."
        "Lately, I can't stop asking myself that question..."
        $ style.say_dialogue = style.normal
        "I think back to what that voice said."
        $ style.say_dialogue = style.edited
        "This is what ultimately should've happened."
        "Stop spending so much time around that hopeless moron!"
        $ style.say_dialogue = style.normal
        "..."
        "I know Sayori's problems are bad, but..."
        "She wouldn't go that far...{w=0.38}right?"
        jump d_fin



    if encore_sayoriquestion_1 == False:
        "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."
        jump d_fin

if hangout1 == "Natsuki":
    mc "I opened this door, and I was back at the club, but everything was upside down..."
    mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
    mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool

if hangout1 == "Yuri":
    mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
    mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah...{w=0.38}almost as bad as seeing Natsuki breaking her neck..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool

if hangout1 == "Monika":
    mc "I was in space or something..."
    mc "And the same voice was saying all these weird things, telling me that I need to 'keep doing what I'm doing'..."
    mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
    show sayori 1k
    mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
    mc "And it didn't say a lot of nice things about you guys either..."
    mc "Stuff like 'you're going to die' or something crazy like that..."
    mc "Listening to all that was just as bad as seeing Natsuki breaking her neck..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "She would never do something like that..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}I'm sure she appreciates you worrying about her..."
    s 3g "Maybe you can talk to her about your dream?"
    mc "Fat chance! She'll think I've lost it!"
    mc "I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool


label m_dream:

mc "I've been having these weird dreams lately."
mc "In my dreams, there's been this really strange voice that's been telling me to pursue it."
mc "I think it's telling me to stay away from you guys for some reason."
mc "I have no idea why..."
s 1k "..."
mc "I know it was just a dream, but it feels too real for some reason..."
mc "It keeps telling me to ‘keep doing what I'm doing' and that it ‘has plans for us'..."
stop music
s u115232 "Plans?!?!"
mc "It was...{w=0.38}unsettling to listen to..."
mc "But, it's not like the night before was any better..."
s 1g "How so?"

if hangout1 == "Sayori":
    mc "I opened this door, and you were hanging right there in your bedroom..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s "I would never do something like that..."
    show sayori 1k
    s "I couldn't..."
    "I don't exactly feel reassured by the way she's saying that..."

    if encore_sayoriquestion_1 == True:
        "Especially since she's said some rather concerning things to me lately..."
        $ style.say_dialogue = style.edited
        "'You're the reason I'm alive...'"
        "Do I really deserve this..."
        "I don't want this relationship to be a one-way street..."
        "Lately, I can't stop asking myself that question..."
        $ style.say_dialogue = style.normal
        "I think back to what that voice said."
        $ style.say_dialogue = style.edited
        "This is what ultimately should've happened."
        "Stop spending so much time around that hopeless moron!"
        $ style.say_dialogue = style.normal
        "..."
        "I know Sayori's problems are bad, but..."
        "She wouldn't go that far...{w=0.38}right?"
        jump d_fin



    if encore_sayoriquestion_1 == False:
        "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."
        jump d_fin

if hangout1 == "Natsuki":
    mc "I opened this door, and I was back at the club, but everything was upside down..."
    mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
    mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s 2g "It doesn't make any sense to me either..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}what if this was all a mistake?"
    mc "What is?"
    s 1f "Us trying to spend time together..."
    s 4u "After all this..."
    mc "Oh, calm down, Sayori!"
    mc "I doubt spending time with you could possibly be causing these nightmares!"
    show sayori 1k
    "I feel a pit form in my stomach."
    "No, that couldn't be the reason..."
    "It's impossible!"
    "And no figment of my imagination is going to tell me otherwise!"
    $ style.say_dialogue = style.edited
    "{cps=25}I'm no figment!{nw}"
    $ style.say_dialogue = style.normal
    "I feel another rush of pain hit my forehead."
    mc "Agh!"
    s 1g "[player]?"
    mc "It's fine, don't worry about it..."
    "I take a minute to nurse my forehead until the pain subsides."
    mc "You know...{w=0.38}despite all this, I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool


if hangout1 == "Yuri":
    mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
    mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
    s 2h "Gee, [player]..."
    s "That sounds really scary!"
    show sayori 1g
    mc "Yeah..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s 2g "It doesn't make any sense to me either..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}what if this was all a mistake?"
    mc "What is?"
    s 1f "Us trying to spend time together..."
    s 4u "After all this..."
    mc "Oh, calm down, Sayori!"
    mc "I doubt spending time with you could possibly be causing these nightmares!"
    show sayori 1k
    "I feel a pit form in my stomach."
    "No, that couldn't be the reason..."
    "It's impossible!"
    "And no figment of my imagination is going to tell me otherwise!"
    $ style.say_dialogue = style.edited
    "{cps=25}I'm no figment!{nw}"
    $ style.say_dialogue = style.normal
    "I feel another rush of pain hit my forehead."
    mc "Agh!"
    s 1g "[player]?"
    mc "It's fine, don't worry about it..."
    "I take a minute to nurse my forehead until the pain subsides."
    mc "You know...{w=0.38}despite all this, I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool


if hangout1 == "Monika":
    mc "I was in space or something..."
    mc "And the same voice was saying all these weird things, telling me that I need to 'keep doing what I'm doing'..."
    mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
    show sayori 1k
    mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
    mc "And it didn't say a lot of nice things about you guys either..."
    mc "Stuff like 'you're going to die' or something crazy like that..."
    mc "'Keep spending time with me.'..."
    mc "It's all really strange..."
    show sayori 2l
    "Sayori nervously swallows."
    s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
    s 2g "It doesn't make any sense to me either..."
    show sayori 1k
    $ renpy.pause(delay=0.8, hard=True)
    show sayori 1d
    s "But...{w=0.38}what if this was all a mistake?"
    mc "What is?"
    s 1f "Us trying to spend time together..."
    s 4u "After all this..."
    mc "Oh, calm down, Sayori!"
    mc "I doubt spending time with you could possibly be causing these nightmares!"
    show sayori 1k
    "I feel a pit form in my stomach."
    "No, that couldn't be the reason..."
    "It's impossible!"
    "And no figment of my imagination is going to tell me otherwise!"
    $ style.say_dialogue = style.edited
    "{cps=25}I'm no figment!{nw}"
    $ style.say_dialogue = style.normal
    "I feel another rush of pain hit my forehead."
    mc "Agh!"
    s 1g "[player]?"
    mc "It's fine, don't worry about it..."
    "I take a minute to nurse my forehead until the pain subsides."
    mc "You know...{w=0.38}despite all this, I'm surprised you don't think I'm crazy."
    show sayori 3k
    s "Well..."
    mc "You think I'm crazy, don't you?"
    s 1h "N-{w=0.38}no, [player]..."
    s "I'm not saying that!"
    s 1g "Let's just say I've had weird dreams before too..."
    s "So, I know what you're going through..."
    mc "Were they as bad as mine?"
    s 1k "..."
    mc "If you don't want to talk about it, it's fine. I won't push it if you aren't ready."
    s 1l "Th-{w=0.38}thanks, [player]..."
    s 1k "I guess we can just go to school now..."
    mc "Ah! I guess so!"
    mc "Wouldn't want to be late!"
    "Sayori seems to completely ignore my comment as we begin our walk to school."
    show sayori at thide
    hide sayori
    jump day3_walktoschool





label day3_notellsayori:

"I decide not to tell her."
mc "It’s...{w=0.38}it’s nothing...{w=0.38}don’t worry about me."
mc "I’m fine."
show sayori 1f
"Sayori frowns before letting out a sigh."
s  1k  "Alright, I guess..."
"Sayori doesn’t seem convinced by my answer."
"But, instead of pressing further, we start our walk to school."
show sayori at thide
hide sayori
jump day3_walktoschool




label day3_walktoschool:
scene bg residential_day
with wipeleft_scene
"Our walk to school was unbearably silent."

if tell_s == True:
    if encore_sayoriquestion_1 == True:
        jump day3_convo_1

if tell_s == True:
    if encore_sayoriquestion_1 == False:
        jump day3_convo_2

if tell_s == False:
    if encore_sayoriquestion_1 == True:
        jump day3_convo_3

if tell_s == False:
    if encore_sayoriquestion_1 == False:
        jump day3_convo_4

label day3_convo_1:
"I'm not used to it being this quiet, especially around Sayori."
"Lately, we've been more than happy to talk about whatever was on our minds, but today's different..."
show sayori 1k at t11 zorder 2
"She hasn't even looked at me once since we started walking."
"Part of me regrets telling her about the last two nights."
"I knew she'd get all worked up and worried..."
"Almost reminds me of my mother..."
show sayori 1d
"Well, it wouldn't hurt to have someone look after me..."
show sayori 1k at t11 zorder 2
jump day3_sayo1

label day3_convo_2:
"Even though lately it's started to become the norm for our walks, it's still frustrating to be right back where we were, right after her confession."
"Especially since we started to move past last Sunday."
"Now she's thinking who knows what inside that head of hers..."

if hangout2 == "Natsuki" or hangout2 == "Yuri" or  hangout2 == "Monika":
    "And what does she mean she's had weird dreams too?"
    "It's not like we've gone through the same thing..."

if hangout2 == "Sayori":
    "I just hope I didn't scare her with any of the details..."
    "Sayori was never one for horror..."

show sayori 1k at t11 zorder 2
jump day3_sayo2


label day3_convo_3:
show sayori 2g at t11 zorder 2
"Even though I told Sayori not to worry about me, she keeps giving me glances every now and then."
"As much as I appreciate her concern, she does need to learn when to focus on herself."
show sayori 1k
"That's her biggest flaw."
"Well, I guess that's what it means to be in a relationship..."
"Still, maybe I should've told her about these dreams..."
show sayori 1k
"Though I'm not really sure what she could do, if anything, to help me through this."
"It's not like we've gone through the same experience anyway."
"But, it's still nice to know that she's there for me."
jump day3_sayo1

label day3_convo_4:
show sayori 2g at t11 zorder 2
"Even though I told Sayori not to worry about me, she keeps giving me glances every now and then."
"As much as I appreciate her concern, she does need to learn when to focus on herself."
show sayori 1k at t11 zorder 2
"That's her biggest flaw."
"Still, maybe I should've told her about these dreams..."
show sayori 1g
"Knowing how things are between us, I don't want her to feel that I'm purposefully closing myself off from her again."
"Especially how we were able to open up to each other yesterday..."
"Though, there's not really much she can do to help me through this..."
show sayori 1k
"It's not like we've both had the same kinds of dreams anyway."
"But, I appreciate knowing that she's still there for me."
jump day3_sayo2


label day3_sayo1:
show sayori 1k at t11 zorder 2
"I turn to Sayori, smiling warmly at her. However, she maintains her blank stare down the road ahead of us as we continue on our walk."
"I let out a small sigh."
"I guess she's just not in a talkative mood anymore..."
"Well, she did sound rather disturbed by what I told her..."
"Sayori's never been one to stomach horror very well, not that I blame her."
"Hopefully she'll get over this soon."
"As our walk continues, it hits me that I have another problem brewing..."
"[poem_giver]'s letter..."
"I haven't really thought about how I'm really going to handle that..."
"As I was thinking earlier, telling Monika about the situation seems like my best course of action."
show sayori 1g
"Normally I'd tell Sayori, but I don't think she'd take it very well right now..."
"I guess my only real option is to go to Monika before the club..."
"Knowing [poem_giver] will probably want to talk to me."
"I'm really not looking forward to today..."
"What if someone else gives me another confession letter?"
show sayori 1h
s "[player]?"
show sayori 1g
"Sayori takes me out of my train of thought."
mc "Y-{w=0.38}yeah?"
show sayori 1h
s "You okay? You just stopped walking..."
mc "Eh?"
show sayori 2g
"Realizing that Sayori is more than a few steps ahead of me, I jog to catch up to her."
jump day3_var1

label day3_sayo2:
show sayori 1k at t11 zorder 2
"I turn to Sayori, trying to smile hopefully at her, but she's just looking blankly down the road ahead of us, as we walk in unison down the sidewalk."
"I let out a small sigh."
"I guess she's just not in a talkative mood..."
"She's probably overthinking again..."
"Hopefully she'll get over this soon."
"However, I quickly realize that I have another problem brewing..."
"[poem_giver]'s letter..."
"I haven't really thought about how I'm really going to handle that..."
"As I was thinking earlier, telling Monika about the situation seems like my best course of action."
show sayori 1g
"Normally I'd tell Sayori, but I don't think she'd take it very well right now..."
"I guess my only real option is to go to Monika before the club..."
"Knowing [poem_giver] will probably want to talk to me."
"I'm really not looking forward to today..."
"What if someone else gives me another confession letter?"
show sayori 1h
s "[player]?"
show sayori 1g
"Sayori takes me out of my train of thought."
mc "Y-{w=0.38}yeah?"
show sayori 1h
s "You okay? You just stopped walking..."
mc "I did?"
show sayori 2g
"Realizing that Sayori is more than a few steps ahead of me, I jog to catch up to her."
jump day3_var1



label day3_var1:

if tell_s == True:
    s 1l "Are you really sure you're okay?"
    s 1g "You've been acting strange today..."
    mc "I'll be fine..."
    mc "I've gone through worse."
    s 1h "Maybe you should stay home from school today."
    s 1k "I wouldn't want you to get any worse..."
    show sayori 1f
    mc "I'll be fine, besides, I really need to talk to Monika."
    s 2h "M-{w=0.38}Monika?"
    s 2g "Why?"
    mc "It's...{w=0.38}something related to what we're doing for Monday."
    s 1k "Okay..."
    mc "Hey, Sayori..."
    s 1g "Yeah?"
    mc "Don't worry about me, if I feel worse, I'll go to the nurse's office and you can take me home, okay?"
    s 1l "Okay..."
    s 1i "But if you feel sick, you text me right away, okay?"
    mc "You have my word, emergency contact."
    show sayori 1y
    "Sayori blushes."

if tell_s == False:
    s 1l "Are you really sure you're okay?"
    s 1g "You've been acting strange today..."
    mc "I guess I just have a lot on my mind."
    s 1k "I see..."

if encore_sayoriquestion_1 == True:
    s "You trust me that much, huh?"
    mc "Why wouldn't I?"
    mc "I mean we've been looking after each other for years..."
    mc "It just feels like it'd be the natural thing to do, you know?"
    s "Y-{w=0.38}yeah it does..."
    show sayori 2d
    s "I like it."
    "I feel my own face start to heat up."

if encore_sayoriquestion_1 == False:
    s "You trust me that much, huh?"
    mc "I mean, I've known you the longest..."
    mc "But don't let it get to your head!"
    show sayori 1q
    s "I won't~"

s 1r "Come on, [player], or we're really going to be late!"
show sayori at lhide
hide sayori
"Sayori quickens her pace to the point where she's almost jogging."
mc "{cps=25}Oh, come on it's only-{nw}"
"..."
"SHOOT!"
mc "Hey! Wait for me!"
"I jog after Sayori."
jump day3_school




label day3_school:
scene bg corridor
with wipeleft_scene
play music t3 fadein 2.0
play audio school
"We were able to make it school just in time for the morning bell."
show sayori 3b at t11 zorder 2
"Though I won't be able to walk with Sayori to her class like usual, thanks to the time."
s 3c "So, I'll see you after your class, [player]."
show sayori 3b
mc "Alright, sounds good to me."

if tell_s == True:
    if encore_sayoriquestion_1 == True:
        show sayori 1k
        "Sayori glances around the corridor to make sure we're alone."
        s 3g "Just...{w=0.38}please let me know if you feel worse or anything, okay?"
        mc "I will, Sayori. Don't worry."
        mc "I'm more worried about you."
        s 3h "M{w=0.38}-me? Why?"
        show sayori 3g
        mc "Earlier you looked like you just saw a ghost."
        mc "I just hope I didn't scare you with any of the details..."
        show sayori 3k
        s "I-{w=0.38}it's not that [player], really."
        s 1h "I'm just more worried about you..."
        show sayori 1g

        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
            if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
                "I'm starting to think that Sayori might somehow have had the same kind of dreams I'm having now..."
                "But that's not really possible...{w=0.38}is it?"
                "Oh well, there's no time to think about that now."

        else:
            pass

        mc "I'll be fine."
        "I shoot Sayori a reassuring smile."
        s 1j "Promise?"
        show sayori 1i
        mc "I promise."
        show sayori 1h
        mc "I'll see you later."
        s 1g "Okay..."
        show sayori 1d
        mc "Come here."
        show sayori 1q at face
        "Sayori walks up to me to give a brief hug, before walking off towards her classroom."
        show sayori 4d at t11 zorder 2
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom, while I head off in the opposite direction towards mine."
        jump day3_class



if tell_s == True:
    if encore_sayoriquestion_1 == False:
        show sayori 1k
        "Sayori glances around the corridor to make sure we're alone."
        s 3g "Just...{w=0.38}let me know if something happens with you, okay?"
        mc "I will, Sayori. Don't worry."
        mc "I'm more worried about you."
        s 3h "M{w=0.38}-me? Why?"
        show sayori 3g
        mc "Earlier you looked like you just saw a ghost."
        mc "I just hope I didn't scare you with any of the details..."
        show sayori 3k
        s "I-{w=0.38}it's not that [player], really..."
        s 1h "I'm just worried that something's going to happen to you..."
        show sayori 1g


        if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
            if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
                "I'm starting to think that Sayori might somehow have had the same kind of dreams I'm having now..."
                "But that's not really possible...{w=0.38}is it?"
                "Oh well, there's no time to think about that now."

        else:
            pass

        mc "I'll be fine."
        "I shoot Sayori a reassuring smile."
        s 1j "Promise?"
        show sayori 1i
        mc "I promise."
        show sayori 1k
        s "Okay..."
        show sayori 4d
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off to her classroom, while I head off in the opposite direction towards mine."
        jump day3_class


if tell_s == False:
    if encore_sayoriquestion_1 == True:
        show sayori 1k
        "Sayori glances around the corridor to make sure we're alone."
        s "Just let me know if something happens with you..."
        s 1g "You didn't look too good this morning."
        mc "Yeah...{w=0.38}I just had a rough night, that's all."
        mc "Nothing to be worried about."
        s 3h "Did you have a bad dream, [player]?"
        mc "I guess that's one way of putting it."
        mc "I don't really want to talk about it right now."
        s 1k "Okay..."
        s 1j "But you better let me know if something happens with you!"
        s 1h "I just want you to be okay..."
        mc "I will Sayori, don't worry."
        show sayori 1d
        mc "If I feel worse or anything, you'll be the first to know."
        s 1g "Okay..."
        show sayori 1d
        mc "Come here."
        show sayori 1q at face
        "Sayori walks up to me to give a brief hug, before walking off towards her classroom."
        show sayori 4d at t11 zorder 2
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom, while I head off in the opposite direction towards mine."
        jump day3_class




if tell_s == False:
    if encore_sayoriquestion_1 == False:
        show sayori 1k
        "Sayori glances around the corridor to make sure we're alone."
        s "You sure everything is okay?"
        s 1g "You didn't look too good this morning."
        mc "Yeah...{w=0.38}I just had a rough night, that's all."
        mc "Nothing to be worried about."
        s 3h "Did you have a bad dream, [player]?"
        mc "I guess that's one way of putting it."
        mc "I don't really want to talk about it right now."
        s 1k "Okay..."
        s 1j "But you better let me know if something happens with you!"
        s 1h "I just want you to be okay..."
        mc "I will Sayori, don't worry."
        show sayori 1d
        mc "If I feel worse or anything, you'll be the first to know."
        s 1g "Okay..."
        show sayori 4d at t11 zorder 2
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom, while I head off in the opposite direction towards mine."
        jump day3_class



label day3_class:
scene bg class_day
with wipeleft_scene
"I walk into class just in time before the teacher starts the lesson."
"I take my usual spot towards the back of the room and slump down in my chair, preparing for another day of relative boredom."
"I'd normally think about dozing off, but there's enough on my mind to keep me awake, and most importantly, looking interested in whatever the teacher's going on about."
stop music fadeout 4.0
"About these dreams..."
"About what they mean..."
"And [poem_giver]'s letter..."
"Not to mention I now have Sayori worried sick about me."

if tell_s == True:
    "I don't even know if I did the right thing by telling her..."

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        "Not to mention, I'm pretty curious what kind of dreams she's been having..."
        "Sayori never mentioned anything like that to me before."
        "Could those be her 'rainclouds'?"
        jump day3_lunch

else:
    pass

if tell_s == False:
    "I don't even know if I did the right thing by not telling her..."
    jump day3_lunch


label day3_lunch:
"In any case, my most pressing concern is how to deal with [poem_giver]'s confession letter."
"I think Monika and I share the same lunch period, so I could probably pull her aside then."
"Hopefully, she'll be willing to talk to me."
"I sigh to myself as I continue to listen to the teacher drone on."
with dissolve_scene_full
scene bg class_day
with open_eyes
play audio school
"After what it feels like an eternity, the lunch bell finally rings."
"Grabbing the poem from my bag and stuffing it into my jacket with my lunch money, I head out to the cafeteria, hoping to find Monika."
play music t6 fadein 2.0
show bg cafeteria
with wipeleft_scene
"Entering the cafeteria, I immediately begin to look around for Monika."
"Alright, if I was Monika, where would I be?"
"..."
"Probably towards the center with all the other popular kids."
"I start walking to the center of the cafeteria."
show bg cafeteria
with wipeleft_scene
"Sure enough, I quickly spot Monika sitting at one tables at the center of the cafeteria."
show monika 2k at t11 zorder 2
"As I expected, she seems to be chatting away with some of her friends."
"Pulling her away might be a little harder than I thought..."
"Well, it's not I'm going to get another chance to talk to her until the club, so it's now or never."
"Taking a deep breath, I carefully approach Monika's table."
show monika at thide
hide monika
show bg cafeteria
with wipeleft_scene
show monika 2l at t11 zorder 2
m "Wow Akari! I can't believe you guys got away with that!"
$ a_name = "Akari"
a "I know right?!?"
a "It was like, the craziest party ever!"
a "Too bad you couldn't make it though..."
m 2m "Ah, well, like I said, I was on that trip with the debate club."
$ r_name = "Ria"
r "Oh, yeah! The debate club! That place has only gotten more toxic since you left!"
m 1g "It's gotten that bad, huh?"
r "Trust me, you left at the best possible time."
r "I miss the good ol' days..."
a "When Sora was president?"
r "Yeah! We were actually productive and went to all those cool events!"
r "And not always fighting with each other over petty crap..."
a "Yeah, that's when the club was in it's prime..."
m 1f "It's a real shame she transferred though..."
r "I know right?!? She was so nice!"
a "I still can't believe she suckered us into voting for her brother for President..."
a "Todd's nice to me but he's a total -"
mc "Um...{w=0.38}hey, Monika..."
show monika 1d at h11
m "[player]?!?"
show monika 2m
m "I-{w=0.38}I didn't know you had this lunch period..."
mc "Ah! Well, I usually just sit in the back..."
m "I see..."
r "Would you like to join us?"
a "Yeah! We have plenty of room!"
mc "I appreciate it, but I actually need to talk to Monika real quick."
show monika 1d
m "Oh? What for?"
mc "It's...{w=0.38}urgent..."
mc "I'd wait to tell you at the club but..."
show monika 2n
m "Say no more, [player]..."
m 3e "I always have time for you."
"I feel my face heat up with slight embarrassment."
mc "Th-{w=0.38}thank you, Monika! I really appreciate it!"
m 1b "We'll be right back girls!"
show monika 1a
r "Have fun you two!"
show monika at thide
hide monika
"I lead Monika out of the cafeteria to somewhere where we might have a little more privacy."
a "She's got him wrapped around her finger."
r "That's Monika for you."
show bg school_rooftop
with wipeleft_scene
stop music fadeout 3.0
"I end up leading Monika up to the school's rooftop, where there's hardly anyone around that can hear us."
show monika 2d at t11 zorder 2
m "So, what's on your mind, [player]?"
mc "I think I'll just show you..."
play sound "sfx/pageflip.ogg"
show monika 1g
"I hand over [poem_giver]'s poem to Monika."
show monika 3g
"Monika looks over it with a rather concerned look on her face."
show monika 2m
"After about a minute, she finishes reading it."
play music e12 fadein 3.0
m "Well then..."
m 2n "I guess it's safe to assume that she likes you..."
mc "Yeah, no kidding!"
show monika 1f
mc "What am I supposed to do?"
mc "Hasn't this ever happened to you before?"
m 2n "N-{w=0.38}no, not really..."
m 2m "Nobody's ever been this sweet in trying to ask me out before..."
m 1p "Usually some boy would just walk up to me and stammer his way through, before trying to ask me out."
m 1q "A few have tried asking me out through text, but to me that's the cheap way..."
mc "Things would probably be worse had she chosen to text me, or walked up to me and confessed."
mc "I'd have no idea how to handle that..."
m 2p "Yeah..."
mc "And I'm pretty sure [poem_giver] is going to try to talk to me later in the club about this."
m 2n "Well, there's really no reason to think she'd expect you to read her poem right away, right?"
mc "What do you mean?"
m 2c "I'm saying that I don't think [poem_giver] was expecting you to read her poem so soon."
m 2d "In all honesty, she probably thinks you'll read it this weekend, when you're preparing the poems for the photoshoot."
mc "Yeah...{w=0.38}I guess you're right..."
mc "So I just tell [poem_giver] that I haven't read it yet?"
m 1e "Pretty much."
m 1m "At least that way you're buying yourself a little bit of time..."
mc "Okay, but that still doesn't really solve the problem..."
show monika 1d
mc "Sooner or later, she's going to ask me about this..."
show monika 2m
mc "And I have no idea what I'm going to say..."
show monika 2n
m "Well, [player], it all depends on how you feel about her..."
m 2g "Do you...{w=0.38}like [poem_giver] back in the same way she likes you?"
mc "I mean..."



if encore_sayoriquestion_1 == True:
    jump day3_firsthalf

if encore_sayoriquestion_1 == False:
    jump day3_secondhalf

label day3_firsthalf:

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devastated..."
        mc "We do mean a lot to each other..."
        show monika 1p
        m "Yeah..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        mc "I didn't intend to get like that with Natsuki yesterday either..."
        mc "She caught me completely by surprise..."
        m 2e "It's fine, [player], don't worry too much about it."
        mc "Well, Sayori wasn't too happy with what she saw..."
        m 2m "I imagine..."
        m 4n "She took it a lot better than I would've though..."

        if apologize_sn == True:
            mc "Yeah, I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sn == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "So I wouldn't get too hung up over it..."
            mc "Yeah...{w=0.38}you're right."



if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        mc "I didn't intend to get like that with Yuri yesterday either..."
        mc "She caught me completely by surprise..."
        m 2e "It's fine, [player], don't worry too much about it."
        mc "Well, Sayori wasn't too happy with what she saw..."
        m 2m "I imagine..."
        m 4n "She took it a lot better than I would've though..."


        if apologize_sy == True:
            mc "Yeah, I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sy == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "So I wouldn't get too hung up over it..."
            mc "Yeah...{w=0.38}you're right."

if hangout1 == "Sayori":
    if hangout2 == "Monika":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2m
        mc "I mean...{w=0.38}I liked it too..."
        show monika 2f
        mc "But it might be better if we don't do that again..."
        mc "I like being your friend, but for now that's really all I can commit to."
        m 1o "It's fine, [player]..."
        m 5a "On the bright side...{w=0.38}your tie seems to be looking presentable today~"
        mc "Yeah...{w=0.38}I guess it does..."
        show monika 1k
        "We manage to share a small laugh before the reality of the situation returns."
        show monika 1n
        m "So...{w=0.38}what was Sayori's reaction to seeing us like that?"
        m 1g "She didn't really bring anything up with me when I had class with her earlier..."
        mc "Well we both know Sayori isn't the confrontational type, but yeah, she wasn't too happy with what she saw..."
        m 2m "What'd you tell her?"


        if apologize_sm == True:
            mc "I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sm == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "And it's more my fault than yours anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."


if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devastated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."

        if encore_festivalquestion_2 == "Natsuki":
            m 2n "Well, you and Natsuki did spend last Sunday together..."
            m 4n "And you seem to have gotten to know her better..."
            mc "Yeah..."
            mc "Still, I'm surprised that she'd give me this..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."



        if encore_festivalquestion_2 == "Yuri":
            m 2n "Well, you two and Yuri did spend last Sunday together..."
            m 4n "And you haven't spent that much time around her lately..."
            mc "Yeah..."
            mc "Still, I'm surprised that she'd give me this..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."





if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you have been spending a lot of time around Natsuki lately."


        if encore_festivalquestion_2 == "Natsuki":
            m 2n "You two did spend last Sunday together..."
            m 4n "And you seem to have gotten to know her quite well recently..."
            mc "Yeah...{w=0.38}we really have..."
            m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
            m 2n "In hindsight, you should've seen this coming..."
            mc "I'm just trying to be friends with her..."
            m 2e "I'm glad that you two are now good friends..."
            m 2g "But do you like Natsuki more?"


        if encore_festivalquestion_2 == "Yuri":
            m 2n "Even though you guys have only started really talking recently, I think she really appreciates you for spending time with her..."
            m 4n "You seem to have gotten to know her quite well recently..."
            mc "Yeah...{w=0.38}we really have..."
            m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
            m 2n "And the way she's always acted around you..."
            m 2m "I suspect she liked you from the very beginning..."
            mc "I'm just trying to be friends with her..."
            m 2e "I'm glad that you two are now good friends..."
            m 2g "But do you like Natsuki more?"

        mc "I mean, I want to stay committed to Sayori."
        show monika 2o
        mc "I really do."
        mc "I chose to be with her."
        mc "But, something about Natsuki just draws me to her..."
        mc "I can't explain it..."
        m 2p "Do you think you're catching feelings for her?"
        mc "I...{w=0.38}don't know."
        show monika 1g
        m "Well player, you know how Sayori would be if you left her..."
        mc "I know...{w=0.38}and that's what scares me..."
        mc "But I'm not unhappy with her or anything, I love spending time with her!"
        show monika 2m
        mc "I guess...{w=0.38}I don't know..."
        mc "Natsuki just lights up my world in a way Sayori hasn't yet..."
        m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
        m 1f "How does Sayori feel about all this?"


        if apologize_sn == True:
            mc "I was straight with her about what happened yesterday..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sn== False:
            mc "Well I was an idiot and lied about what happened to her yesterday..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            mc "But...{w=0.38}we did make up..."
            mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
            m 2p "Well, we can handle Sayori another time..."
            m 2m "Speaking of which..."




if hangout1 == "Natsuki":
    if hangout2 == "Yuri":
            mc "I'm happy with Sayori..."
            mc "I wouldn't want to ruin what we have..."
            show monika 2m
            m "But you haven't been spending a lot of time around Sayori in the club lately."
            m 2g "You've been around Natsuki and Yuri a lot latetly..."

            if encore_festivalquestion_2 == "Natsuki":
                m 2n "You did seem to enjoy spending last Sunday with Natsuki.."
                m 4n "And you guys looked like you were having fun on Monday..."
                m "Though she didn't seem to have liked seeing you getting so close to Yuri yesterday..."
                mc "Yeah...{w=0.38}I didn't think that was going to happen to be honest..."
                mc "It just...{w=0.38}kind of happened..."
                mc "But, it's been great getting to know Natsuki..."
                m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
                m 2n "In hindsight, you should've seen this coming..."
                mc "I'm just trying to be friends with her..."
                m 2e "I'm glad that you two are now good friends..."
                m 2g "But do you like Natsuki more over Sayori and Yuri?"
                mc "I mean, I want to stay committed to Sayori."
                show monika 2o
                mc "I really do."
                mc "I chose to be with her."
                mc "But, something about Natsuki just draws me to her..."
                mc "I can't explain it..."
                m 2p "Do you think you're catching feelings for her?"
                mc "I...{w=0.38}don't know."
                show monika 1g
                m "Well player, you know how Sayori would be if you left her..."
                mc "I know...{w=0.38}and that's what scares me..."
                mc "But I'm not unhappy with her or anything, I love spending time with her!"
                show monika 2m
                mc "I guess...{w=0.38}I don't know..."
                mc "Natsuki just lights up my world in a way Sayori hasn't yet..."
                m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
                m 1f "How does Sayori feel about all this?"


                if apologize_sn == True:
                    mc "I was straight with her about what happened yesterday..."
                    m 2e "Well...{w=0.38}that's good..."
                    m 1m "I'm sure she appreciated you being honest with her, [player]..."
                    mc "Yeah..."

                if apologize_sn== False:
                    mc "Well I was an idiot and lied about what happened to her yesterday..."
                    show monika 2d
                    "Monika's eyes light up with curiosity."
                    m "Oh? What do you mean?"
                    mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                    show monika 2m
                    mc "But...{w=0.38}we did make up..."
                    mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                    m 2p "Well, we can handle Sayori another time..."
                    m 2m "Speaking of which..."



            if encore_festivalquestion_2 == "Yuri":
                m 2n "You did seem to enjoy spending last Sunday with Yuri..."
                m 2m "Though she looked disappointed that you didn't spend much time around her on Monday..."
                mc "Yeah, I didn't realize how much she valued us reading together..."
                m 4n "You seem to have gotten to know her quite well recently..."
                mc "Yeah...{w=0.38}we really have..."
                m 4m "I've seen the way she looks at you when you're reading with her, [player]..."
                m 2n "And the way she's always acted around you..."
                m 2m "I suspect she liked you from the very beginning..."
                mc "I'm just trying to be friends with her..."
                m 2e "I'm glad that you two are now good friends..."
                m 2g "But do you like Yuri more over Sayori and Natsuki?"
                mc "I mean, I want to stay committed to Sayori."
                show monika 2o
                mc "I really do."
                mc "I chose to be with her."
                mc "But, something about Yuri just draws me to her..."
                mc "I can't explain it..."
                m 2p "Do you think you're catching feelings for her?"
                mc "I...{w=0.38}don't know."
                show monika 1g
                m "Well player, you know how Sayori would be if you left her..."
                mc "I know...{w=0.38}and that's what scares me..."
                mc "But I'm not unhappy with her or anything, I love spending time with her!"
                show monika 2m
                mc "I guess...{w=0.38}I don't know..."
                mc "Yuri just lights up my world in a way Sayori hasn't yet..."
                m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
                m 1f "How does Sayori feel about all this?"


                if apologize_sy == True:
                    mc "I was straight with her about what happened yesterday..."
                    m 2e "Well...{w=0.38}that's good..."
                    m 1m "I'm sure she appreciated you being honest with her, [player]..."
                    mc "Yeah..."

                if apologize_sy== False:
                    mc "Well I was an idiot and lied about what happened to her yesterday..."
                    show monika 2d
                    "Monika's eyes light up with curiosity."
                    m "Oh? What do you mean?"
                    mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                    show monika 2m
                    mc "But...{w=0.38}we did make up..."
                    mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                    m 2p "Well, we can handle Sayori another time..."
                    m 2m "Speaking of which..."





if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I had fun spend some time around Natsuki on Monday..."
            mc "It was nice catching up with her since the festival."

        if encore_festivalquestion_2 == "Yuri":
            mc "It was nice had finally spend some time around Natsuki..."
            mc "I didn't really get much of a chance to spend time around her before..."

        show monika 2e
        mc "And I'm glad we've finally got to spend some time around each other too..."
        m 2m "Y-{w=0.38}yeah...{w=0.38}it was nice..."
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2m
        mc "I mean...{w=0.38}I liked it too..."
        show monika 2f
        mc "But it might be better if we don't do that again..."
        mc "I like being your friend, but for now that's really all I can commit to."
        m 1o "It's fine, [player]..."
        m 5a "On the bright side...{w=0.38}your tie seems to be looking presentable today~"
        mc "Yeah...{w=0.38}I guess it does..."
        show monika 1k
        "We manage to share a small laugh before the reality of the situation returns."
        show monika 1n
        m "So...{w=0.38}what was Sayori's reaction to seeing us like that?"
        m 1g "She didn't really bring anything up with me when I had class with her earlier..."
        mc "Well we both know Sayori isn't the confrontational type, but yeah, she wasn't too happy with what she saw..."
        m 2m "What'd you tell her?"

        if apologize_sm == True:
            mc "I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sm == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "And it's more my fault than yours anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."



if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devastated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "It was nice had finally spend some time around Yuri..."
            mc "I didn't really get much of a chance to spend time around her before..."


        if encore_festivalquestion_2 == "Yuri":
            mc "I had fun spend some time around Yuri on Monday..."
            mc "It was nice catching up with her since the festival."



if hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        m 2g "You've been around Yuri and Natsuki a lot latetly..."

        if encore_festivalquestion_2 == "Natsuki":
            m 2n "You did seem to enjoy spending last Sunday with Natsuki.."
            m 2m "Though she looked disappointed that you didn't spend much time around her on Monday..."
            mc "Yeah, I didn't realize how much she liked reading together..."
            m 4n "You seem to have gotten to know her quite well recently..."
            mc "Yeah...{w=0.38}we really have..."
            m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
            m 2n "In hindsight, you should've seen this coming..."
            mc "I'm just trying to be friends with her..."
            m 2e "I'm glad that you two are now good friends..."
            m 2g "But do you like Natsuki more over Sayori and Yuri?"
            mc "I mean, I want to stay committed to Sayori."
            show monika 2o
            mc "I really do."
            mc "I chose to be with her."
            mc "But, something about Natsuki just draws me to her..."
            mc "I can't explain it..."
            m 2p "Do you think you're catching feelings for her?"
            mc "I...{w=0.38}don't know."
            show monika 1g
            m "Well player, you know how Sayori would be if you left her..."
            mc "I know...{w=0.38}and that's what scares me..."
            mc "But I'm not unhappy with her or anything, I love spending time with her!"
            show monika 2m
            mc "I guess...{w=0.38}I don't know..."
            mc "Natsuki just lights up my world in a way Sayori hasn't yet..."
            m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
            m 1f "How does Sayori feel about all this?"


            if apologize_sn == True:
                mc "I was straight with her about what happened yesterday..."
                m 2e "Well...{w=0.38}that's good..."
                m 1m "I'm sure she appreciated you being honest with her, [player]..."
                mc "Yeah..."

            if apologize_sn== False:
                mc "Well I was an idiot and lied about what happened to her yesterday..."
                show monika 2d
                "Monika's eyes light up with curiosity."
                m "Oh? What do you mean?"
                mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                show monika 2m
                mc "But...{w=0.38}we did make up..."
                mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                m 2p "Well, we can handle Sayori another time..."
                m 2m "Speaking of which..."



        if encore_festivalquestion_2 == "Yuri":
            m 2n "You did seem to enjoy spending last Sunday with Natsuki.."
            m 4n "And you guys looked like you were having fun on Monday..."
            m "Though she didn't seem to have liked seeing you getting so close to Yuri yesterday..."
            mc "Yeah...{w=0.38}I didn't think that was going to happen to be honest..."
            mc "It just...{w=0.38}kind of happened..."
            mc "But, it's been great getting to know Yuri..."
            m 4m "I've seen the way she looks at you when you're reading with her, [player]..."
            m 2n "And the way she's always acted around you..."
            m 2m "I suspect she liked you from the very beginning..."
            mc "I'm just trying to be friends with her..."
            m 2e "I'm glad that you two are now good friends..."
            m 2g "But do you like Yuri more over Sayori and Natsuki?"
            mc "I mean, I want to stay committed to Sayori."
            show monika 2o
            mc "I really do."
            mc "I chose to be with her."
            mc "But, something about Yuri just draws me to her..."
            mc "I can't explain it..."
            m 2p "Do you think you're catching feelings for her?"
            mc "I...{w=0.38}don't know."
            show monika 1g
            m "Well player, you know how Sayori would be if you left her..."
            mc "I know...{w=0.38}and that's what scares me..."
            mc "But I'm not unhappy with her or anything, I love spending time with her!"
            show monika 2m
            mc "I guess...{w=0.38}I don't know..."
            mc "Yuri just lights up my world in a way Sayori hasn't yet..."
            m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
            m 1f "How does Sayori feel about all this?"


            if apologize_sy == True:
                mc "I was straight with her about what happened yesterday..."
                m 2e "Well...{w=0.38}that's good..."
                m 1m "I'm sure she appreciated you being honest with her, [player]..."
                mc "Yeah..."

            if apologize_sy== False:
                mc "Well I was an idiot and lied about what happened to her yesterday..."
                show monika 2d
                "Monika's eyes light up with curiosity."
                m "Oh? What do you mean?"
                mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                show monika 2m
                mc "But...{w=0.38}we did make up..."
                mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                m 2p "Well, we can handle Sayori another time..."
                m 2m "Speaking of which..."


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
            mc "I'm happy with Sayori..."
            mc "I wouldn't want to ruin what we have..."
            show monika 2m
            m "But you have been spending a lot of time around Yuri lately."


            if encore_festivalquestion_2 == "Natsuki":
                m 2n "Even though you guys have only started really talking recently, I think she really appreciates you for spending time wtih her..."
                m 4n "You seem to have gotten to know her quite well recently..."
                mc "Yeah...{w=0.38}we really have..."
                m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
                m 2n "And the way she's always acted around you..."
                m 2m "I suspect she liked you from the very beginning..."
                mc "I'm just trying to be friends with her..."
                m 2e "I'm glad that you two are now good friends..."
                m 2g "But do you like Yuri more?"



            if encore_festivalquestion_2 == "Yuri":
                    m 2n "You two did spend last Sunday together..."
                    m 4n "And you seem to have gotten to know her quite well recently..."
                    mc "Yeah...{w=0.38}we really have..."
                    m 4m "I've seen the way she looks at you when you're reading together, [player]..."
                    m 2n "In hindsight, you should've seen this coming..."
                    mc "I'm just trying to be friends with her..."
                    m 2e "I'm glad that you two are now good friends..."
                    m 2g "But do you like Yuri more?"



            mc "I mean, I want to stay committed to Sayori."
            show monika 2o
            mc "I really do."
            mc "I chose to be with her."
            mc "But, something about Yuri just draws me to her..."
            mc "I can't explain it..."
            m 2p "Do you think you're catching feelings for her?"
            mc "I...{w=0.38}don't know."
            show monika 1g
            m "Well player, you know how Sayori would be if you left her..."
            mc "I know...{w=0.38}and that's what scares me..."
            mc "But I'm not unhappy with her or anything, I love spending time with her!"
            show monika 2m
            mc "I guess...{w=0.38}I don't know..."
            mc "Yuri just lights up my world in a way Sayori hasn't yet..."
            m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
            m 1f "How does Sayori feel about all this?"


            if apologize_sn == True:
                mc "I was straight with her about what happened yesterday..."
                m 2e "Well...{w=0.38}that's good..."
                m 1m "I'm sure she appreciated you being honest with her, [player]..."
                mc "Yeah..."

            if apologize_sn== False:
                mc "Well I was an idiot and lied about what happened to her yesterday..."
                show monika 2d
                "Monika's eyes light up with curiosity."
                m "Oh? What do you mean?"
                mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                show monika 2m
                mc "But...{w=0.38}we did make up..."
                mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                m 2p "Well, we can handle Sayori another time..."
                m 2m "Speaking of which..."




if hangout1 == "Yuri":
    if hangout2 == "Monika":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."
        mc "I had fun spend some time around Natsuki on Monday..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I didn't really get much of a chance to spend time around her before..."


        if encore_festivalquestion_2 == "Yuri":
            mc "It was nice catching up with her since the festival."

        show monika 2e
        mc "And I'm glad we've finally got to spend some time around each other too..."
        m 2m "Y-{w=0.38}yeah...{w=0.38}it was nice..."
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2m
        mc "I mean...{w=0.38}I liked it too..."
        show monika 2f
        mc "But it might be better if we don't do that again..."
        mc "I like being your friend, but for now that's really all I can commit to."
        m 1o "It's fine, [player]..."
        m 5a "On the bright side...{w=0.38}your tie seems to be looking presentable today~"
        mc "Yeah...{w=0.38}I guess it does..."
        show monika 1k
        "We manage to share a small laugh before the reality of the situation returns."
        show monika 1n
        m "So...{w=0.38}what was Sayori's reaction to seeing us like that?"
        m 1g "She didn't really bring anything up with me when I had class with her earlier..."
        mc "Well we both know Sayori isn't the confrontational type, but yeah, she wasn't too happy with what she saw..."
        m 2m "What'd you tell her?"

        if apologize_sm == True:
            mc "I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sm == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "And it's more my fault than yours anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."




if hangout1 == "Monika":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devastated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."
        "Monika's eyes glance downward towards the ground."
        mc "Hey, Monika..."
        m 1g "Yeah?"
        mc "It was nice that we got to finally spend some time together on Monday."
        m 1m "Yeah...{w=0.38}it was..."
        m 1n "Anyways..."


if hangout1 == "Monika":
    if hangout2 == "Natsuki":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."
        mc "I don't see the harm in that..."
        m 2g "Yeah, there's really no harm in getting to know the others..."
        m 5a "I didn't think Sayori would keep you all to herself..."
        mc "Ah! It's not like that at all! Really!"
        m 2l "I'm just kidding, [player]! Don't worry!"
        m 2m "Still though..."



        if encore_festivalquestion_2 == "Natsuki":
            m 2n "You did seem to enjoy spending last Sunday with Natsuki.."
            m 2m "Though she looked disappointed that you didn't spend much time around her on Monday..."
            mc "Yeah, I didn't realize how much she liked reading together..."
            m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
            m 2n "In hindsight, you should've seen this coming..."
            mc "I'm just trying to be friends with her..."
            m 2e "I'm glad that you two are now good friends..."
            m 2g "But do you like Natsuki more over Sayori and Yuri?"
            mc "I mean, I want to stay committed to Sayori."
            show monika 2o
            mc "I really do."
            mc "I chose to be with her."
            mc "But, something about Natsuki just draws me to her..."
            mc "I can't explain it..."
            m 2p "Do you think you're catching feelings for her?"
            mc "I...{w=0.38}don't know."
            show monika 1g
            m "Well player, you know how Sayori would be if you left her..."
            mc "I know...{w=0.38}and that's what scares me..."
            mc "But I'm not unhappy with her or anything, I love spending time with her!"
            show monika 2m
            mc "I guess...{w=0.38}I don't know..."
            mc "Natsuki just lights up my world in a way Sayori hasn't yet..."
            m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
            m 1f "How does Sayori feel about all this?"


            if apologize_sn == True:
                mc "I was straight with her about what happened yesterday..."
                m 2e "Well...{w=0.38}that's good..."
                m 1m "I'm sure she appreciated you being honest with her, [player]..."
                mc "Yeah..."

            if apologize_sn== False:
                mc "Well I was an idiot and lied about what happened to her yesterday..."
                show monika 2d
                "Monika's eyes light up with curiosity."
                m "Oh? What do you mean?"
                mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                show monika 2m
                mc "But...{w=0.38}we did make up..."
                mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                m 2p "Well, we can handle Sayori another time..."
                m 2m "Speaking of which..."



        if encore_festivalquestion_2 == "Yuri":
            m 2g "I've noticed that you haven't been talking to Yuri recently."
            m "Is everything okay?"
            mc "Ah, I just haven't had the time too."
            show monika 2c
            mc "Between Sayori's 'rainclouds', to the photoshoot, to this, it's been pretty crazy lately..."
            m 1m "Yeah, it has been."
            m 1n "Let's just hope she doesn't give you a confession letter too!"
            mc "That'd be the end of me..."
            m 1m "Speaking of confession letters..."



if hangout1 == "Monika":
    if hangout2 == "Yuri":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."
        mc "I don't see the harm in that..."
        m 2g "Yeah, there's really no harm in getting to know the others..."
        m 5a "I didn't think Sayori would keep you all to herself..."
        mc "Ah! It's not like that at all! Really!"
        m 2l "I'm just kidding, [player]! Don't worry!"
        m 2m "Still though..."



        if encore_festivalquestion_2 == "Natsuki":
                m 2g "I've noticed that you haven't been talking to Natsuki recently."
                m "Is everything okay?"
                mc "Ah, I just haven't had the time too."
                show monika 2c
                mc "Between Sayori's 'rainclouds', to the photoshoot, to this, it's been pretty crazy lately..."
                m 1m "Yeah, it has been."
                m 1n "Let's just hope she doesn't give you a confession letter too!"
                mc "That'd be the end of me..."
                m 1m "Speaking of confession letters..."




        if encore_festivalquestion_2 == "Yuri":
                m 2n "You did seem to enjoy spending last Sunday with Yuri..."
                m 2m "Though she looked disappointed that you didn't spend much time around her on Monday..."
                mc "Yeah, I didn't realize how much she liked reading together..."
                m 4n "You seem to have gotten to know her quite well recently..."
                mc "Yeah...{w=0.38}we really have..."
                m 4m "I've seen the way she looks at you when you're reading together, [player]..."
                m 2n "In hindsight, you should've seen this coming..."
                mc "I'm just trying to be friends with her..."
                m 2e "I'm glad that you two are now good friends..."
                m 2g "But do you like Natsuki more over Sayori and Yuri?"
                mc "I mean, I want to stay committed to Sayori."
                show monika 2o
                mc "I really do."
                mc "I chose to be with her."
                mc "But, something about Natsuki just draws me to her..."
                mc "I can't explain it..."
                m 2p "Do you think you're catching feelings for her?"
                mc "I...{w=0.38}don't know."
                show monika 1g
                m "Well player, you know how Sayori would be if you left her..."
                mc "I know...{w=0.38}and that's what scares me..."
                mc "But I'm not unhappy with her or anything, I love spending time with her!"
                show monika 2m
                mc "I guess...{w=0.38}I don't know..."
                mc "Natsuki just lights up my world in a way Sayori hasn't yet..."
                m 1g "If you're thinking like that, [player], your relationship with her might be doomed to fail..."
                m 1f "How does Sayori feel about all this?"

                if apologize_sy == True:
                    mc "I was straight with her about what happened yesterday..."
                    m 2e "Well...{w=0.38}that's good..."
                    m 1m "I'm sure she appreciated you being honest with her, [player]..."
                    mc "Yeah..."

                if apologize_sy== False:
                    mc "Well I was an idiot and lied about what happened to her yesterday..."
                    show monika 2d
                    "Monika's eyes light up with curiosity."
                    m "Oh? What do you mean?"
                    mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
                    show monika 2m
                    mc "But...{w=0.38}we did make up..."
                    mc "But I know I hurt her...{w=0.38}and I don't want to do that to her...."
                    m 2p "Well, we can handle Sayori another time..."
                    m 2m "Speaking of which..."



if hangout1 == "Monika":
    if hangout2 == "Monika":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."
        mc "I don't see the harm in that..."
        m 2g "Yeah, there's really no harm in getting to know the others..."
        m 5a "I didn't think Sayori would keep you all to herself..."
        mc "Ah! It's not like that at all! Really!"
        m 2l "I'm just kidding, [player]! Don't worry!"
        m 2m "Still though..."
        m 2e "I'm really glad that we've gotten to spend some time together lately..."
        mc "Yeah...{w=0.38}me too..."
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2m
        mc "I mean...{w=0.38}I liked it too..."
        show monika 2f
        mc "But it might be better if we don't do that again..."
        mc "I like being your friend, but for now that's really all I can commit to."
        m 1o "It's fine, [player]..."
        m 5a "On the bright side...{w=0.38}your tie seems to be looking presentable today~"
        mc "Yeah...{w=0.38}I guess it does..."
        show monika 1k
        "We manage to share a small laugh before the reality of the situation returns."
        show monika 1n
        m "So...{w=0.38}what was Sayori's reaction to seeing us like that?"
        m 1g "She didn't really bring anything up with me when I had class with her earlier..."
        mc "Well we both know Sayori isn't the confrontational type, but yeah, she wasn't too happy with what she saw..."
        m 2m "What'd you tell her?"


        if apologize_sm == True:
            mc "I was straight with her about what happened..."
            m 2e "Well...{w=0.38}that's good..."
            m 1m "I'm sure she appreciated you being honest with her, [player]..."
            mc "Yeah..."

        if apologize_sm == False:
            mc "Well I was an idiot and lied about what happened to her..."
            show monika 2d
            "Monika's eyes light up with curiosity."
            m "Oh? What do you mean?"
            mc "I made up some excuse about what happened, but I ended up apologizing to her about lying and about what happened..."
            show monika 2m
            m "[player]...{w=0.38}I'm surprised at you..."
            mc "Yeah...{w=0.38}I'm not really proud of it."
            m 2e "I understand, [player]..."
            mc "You do?"
            m "You did something you're not proud of and you tried to justify it..."
            m 3e "We do it all the time..."
            m 2m "And it's more my fault than yours anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."

m 1d "Does Sayori know that [poem_giver] gave you this?"
mc "No...{w=0.38}that's another problem..."
mc "She wasn't really in the mood to talk today, so I figured that'd be a bad time to bring that up..."
mc "Not to mention I have no idea how she'll take it..."
m 2n "I don't think Sayori would overreact that way, [player]..."
m 2p "Though she wouldn't take too kindly to this for sure..."
mc "So...{w=0.38}when should I tell her about the letter?"
m 3m "You're probably better off waiting to tell her for now."
m 1e "It's better you figure out what you want to say to [poem_giver] first."
mc "Alright..."
jump day3_plan

label day3_secondhalf:

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        show monika 2f
        mc "I really don't know..."
        mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
        mc "And last Sunday, I did feel like maybe there was something there..."
        mc "But Sayori's been on my mind a lot lately..."
        m 2g "You're not having second thoughts about your answer to her confession, are you?"
        show monika 2f
        mc "I don't know..."
        mc "I'm worried about her..."
        mc "I've known her practically my whole life..."
        show monika 2o
        mc "Ever since last Sunday, she's been acting different around me..."
        mc "She really didn't handle my response well..."
        mc "And since then, I've tried making things right with her..."
        show monika 1q
        mc "We've made some progress, but I don't really know how I feel about her..."
        m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
        m 2e "I'm happy to hear that you guys are working to make things right..."
        m 2m "But you're probably better off just being friends with her..."
        m 2e "I don't think she can handle anything more right now..."
        mc "Yeah...{w=0.38}you're right..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        show monika 2f
        mc "I don't know..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            show monika 1q
            mc "We've made some progress, but I don't really know how I feel about her..."
            m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
            m 2e "I'm happy to hear that you guys are working to make things right..."
            m 2m "But you're probably better off just being friends with her..."
            m 2e "I don't think she can handle anything more right now..."
            mc "Yeah...{w=0.38}you're right..."

        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            show monika 2m
            mc "And part of me is interested in Natsuki..."
            mc "Though, I'll admit, I didn't expect to be like that with her yesterday..."
            mc "She caught me by surprise..."
            show monika 2e
            m "It's...{w=0.38}fine, [player]..."
            m 2n "Don't worry too much about it..."
            mc "Alright."
            m 2g "But you are putting yourself in a very difficult situation."
            m 2m "You can't have all of them..."
            mc "I know..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."




if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        show monika 2f
        mc "I don't know..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            show monika 2m
            mc "And part of me is interested in Yuri..."
            mc "Though, I'll admit, I didn't expect to be like that with her yesterday..."
            mc "She caught me by surprise..."
            show monika 2e
            m "It's...{w=0.38}fine, [player]..."
            m 2n "Don't worry too much about it..."
            mc "Alright."
            m 2g "But you are putting yourself in a very difficult situation."
            m 2m "You can't have all of them..."
            mc "I know..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."

        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            show monika 1q
            mc "We've made some progress, but I don't really know how I feel about her..."
            m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
            m 2e "I'm happy to hear that you guys are working to make things right..."
            m 2m "But you're probably better off just being friends with her..."
            m 2e "I don't think she can handle anything more right now..."
            mc "Yeah...{w=0.38}you're right..."




if hangout1 == "Sayori":
    if hangout2 == "Monika":
        show monika 2f
        mc "I don't know..."
        mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
        mc "And last Sunday, I did feel like maybe there was something there..."
        show monika 2m
        mc "But Sayori's been on my mind lately..."
        m 2g "You're not having second thoughts about your answer to her confession, are you?"
        show monika 2f
        mc "I don't know..."
        mc "I'm worried about her..."
        mc "I've known her practically my whole life..."
        show monika 2o
        mc "Ever since last Sunday, she's been acting different around me..."
        mc "She really didn't handle my response well..."
        mc "And since then, I've tried making things right with her..."
        m 2e "I think she'll be fine, [player]..."
        m "She just needs time."
        mc "But I feel like I should do more though..."
        show monika 2m
        mc "I'm the one that got her into this state of mind in the first place!"
        mc "And now I got [poem_giver] head over heels for me!"
        m 2e "It's all going to be okay, [player]..."
        m "I can help you through this..."
        mc "I really should've started talking to you sooner..."
        show monika u114311
        m "Eh? What do you mean?"
        mc "You always know what to do..."
        mc "It's like you're the answer to my problems!"
        mc "I mean as crazy it sounds, I just feel like if I spent time with you earlier..."
        mc "I don't know...{w=0.38}maybe things would be less crazy..."
        mc "I guess what I'm trying to say is:{w=0.38}it's been nice getting to know you..."
        m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
        m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
        mc "Well..."
        m 1e "Come on, [player]..."
        m 5a "I've seen the way you've looked at me..."
        m "How you're always stumbling over your sentences when I compliment you..."
        m "How I take your breath away whenever I get close to you..."
        show monika smirk
        m "It's really sweet~"
        mc "Monika, I..."
        "I'm completely left speechless."
        show monika 2m
        mc "I really have always wanted to get to know you..."
        mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
        m 2n "Yeah..."
        m 2e "But, let's figure this out first, okay?"
        mc "Yeah..."



if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        show monika 2f
        mc "I don't know..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            mc "She was pretty emotional yesterday..."
            show monika 1q
            mc "We've made some progress, but I don't really know how I feel about her..."
            m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
            m 2e "I'm happy to hear that you guys are working to make things right..."
            m 2m "But you're probably better off just being friends with her..."
            m 2e "I don't think she can handle anything more right now..."
            mc "Yeah...{w=0.38}you're right..."

        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            mc "She was pretty emotional yesterday..."
            show monika 2e
            m "She just needs time, [player]..."
            m "She'll get through this."
            mc "I mean I'm the one who made things worse..."
            mc "But I guess things have been getting a little better with her."
            m "Well that's good."
            show monika 2m
            mc "Yeah, having to worry about Sayori, and trying to decide if I like Yuri or Natsuki more has been stressful.."
            m 2h "You can't have all of them, [player]."
            m 4h "Playing with their feelings like that is wrong and could have unforeseen consequences."
            mc "I know..."
            mc "It's just that I feel like I'm being pulled all over the place."
            mc "I don't know what I want..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."



if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":

        if encore_festivalquestion_2 == "Natsuki":
            show monika 2f
            mc "I mean to tell you the truth, I didn't even really know that Yuri liked me..."
            mc "In fact I think she thought I hated her at some point because I was spending so much time around Natsuki..."
            mc "So I'm surprised that she'd give me this..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."
            mc "But, I do feel drawn to Natsuki."
            mc "We just...{w=0.38}click..."
            show monika 2o
            mc "I'm really happy whenever we get to spend time around each other."
            mc "And I do think she feels the same way."
            m 2n "I see..."
            show monika 2m
            mc "I have nothing against Yuri, I really don't..."
            mc "I think I just...{w=0.38}like Natsuki better..."
            mc "But if I ever told her that Yuri gave me this, she'd flip out."
            m 2m "Yeah...{w=0.38}she would..."

        if encore_festivalquestion_2 == "Yuri":
            show monika 2f
            mc "I mean, I guess part of me is interested in Yuri..."
            mc "I had a hunch she's been crushing on me, given what happened last Sunday and the festival..."
            mc "But I'm still a little surprised that she gave me this..."
            m 2g "You really haven't been spending too much time around her lately..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."
            mc "But, I've started to feel drawn to Natsuki."
            mc "There's just...{w=0.38}something about her that interests me."
            mc "I can't really explain it..."
            m 2n "I see..."




if hangout1 == "Natsuki":
    if hangout2 == "Yuri":

        if encore_festivalquestion_2 == "Natsuki":
            show monika 2f
            mc "I mean to tell you the truth, lately I've felt like I've been drawn to both to both her and Yuri..."
            m 2g "What do you mean?"
            mc "I think I like both of them..."
            m 2g "Well, that's a very difficult situation."
            m 2m "You know you can't have both of them..."
            mc "I know..."
            m 2p "Choosing between either of them would likely offset the other..."
            m 2r "It really wouldn't be good for the club..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."

        if encore_festivalquestion_2 == "Yuri":
            show monika 2f
            mc "I mean to tell you the truth, lately I've felt like I've been drawn to both to both her and Natsuki..."
            m 2g "What do you mean?"
            mc "I think I like both of them..."
            m 2g "Well, that's a very difficult situation."
            m 2m "You know you can't have both of them..."
            mc "I know..."
            m 2p "Choosing between either of them would likely offset the other..."
            m 2r "It really wouldn't be good for the club..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."



if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        show monika 2f
        mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
        mc "And last Sunday, I did feel like maybe there was something there..."
        mc "I don't know...{w=0.38}I guess I've been interested in getting to know the others a little bit lately..."
        show monika u114311
        mc "And...{w=0.38}it's been nice getting to know you too, Monika."
        show monika 2m
        mc "Especially since we really haven't talked that much recently..."
        m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
        m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
        mc "Well..."
        m 1e "Come on, [player]..."
        m 5a "I've seen the way you've looked at me..."
        m "How you're always stumbling over your sentences when I compliment you..."
        m "How I take your breath away whenever I get close to you..."
        show monika smirk
        m "It's really sweet~"
        mc "Monika, I..."
        "I'm completely left speechless."
        show monika 2m
        mc "I really have always wanted to get to know you..."
        mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
        m 2n "Yeah..."
        m 2e "But, let's figure this out first, okay?"
        mc "Yeah..."






if hangout1 == "Yuri":
    if hangout2 == "Sayori":

        if encore_festivalquestion_2 == "Natsuki":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            mc "She was pretty emotional yesterday..."
            show monika 2e
            m "She just needs time, [player]..."
            m "She'll get through this."
            mc "I mean I'm the one who made things worse..."
            mc "But I guess things have been getting a little better with her."
            m "Well that's good."
            show monika 2m
            mc "Yeah, having to worry about Sayori, and trying to decide if I like Yuri or Natsuki more has been stressful.."
            m 2h "You can't have all of them, [player]."
            m 4h "Playing with their feelings like that is wrong and could have unforeseen consequences."
            mc "I know..."
            mc "It's just that I feel like I'm being pulled all over the place."
            mc "I don't know what I want..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."



        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            mc "She was pretty emotional yesterday..."
            show monika 1q
            mc "We've made some progress, but I don't really know how I feel about her..."
            m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
            m 2e "I'm happy to hear that you guys are working to make things right..."
            m 2m "But you're probably better off just being friends with her..."
            m 2e "I don't think she can handle anything more right now..."
            mc "Yeah...{w=0.38}you're right..."





if hangout1 == "Yuri":
    if hangout2 == "Natsuki":

        if encore_festivalquestion_2 == "Natsuki":
            show monika 2f
            mc "I mean to tell you the truth, lately I've felt like I've been drawn to both to both her and Yuri..."
            m 2g "What do you mean?"
            mc "I think I like both of them..."
            m 2g "Well, that's a very difficult situation."
            m 2m "You know you can't have both of them..."
            mc "I know..."
            m 2p "Choosing between either of them would likely offset the other..."
            m 2r "It really wouldn't be good for the club..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."

        if encore_festivalquestion_2 == "Yuri":
            show monika 2f
            mc "I mean to tell you the truth, lately I've felt like I've been drawn to both to both her and Natsuki..."
            m 2g "What do you mean?"
            mc "I think I like both of them..."
            m 2g "Well, that's a very difficult situation."
            m 2m "You know you can't have both of them..."
            mc "I know..."
            m 2p "Choosing between either of them would likely offset the other..."
            m 2r "It really wouldn't be good for the club..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."




if hangout1 == "Yuri":
    if hangout2 == "Yuri":

        if encore_festivalquestion_2 == "Natsuki":
            show monika 2f
            mc "I mean, I guess part of me is interested in Natsuki..."
            mc "I had a hunch she's been crushing on me, given what happened last Sunday and the festival..."
            mc "But I'm still a little surprised that she gave me this..."
            m 2g "You really haven't been spending too much time around her lately..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."
            mc "But, I've started to feel drawn to Yuri."
            mc "There's just...{w=0.38}something about her that interests me."
            mc "I can't really explain it..."
            m 2n "I see..."



        if encore_festivalquestion_2 == "Yuri":
            show monika 2f
            mc "I mean to tell you the truth, I didn't even really know that Natsuki liked me..."
            mc "In fact I think she thought I hated her at some point because I was spending so much time around Yuri..."
            mc "So I'm surprised that she'd give me this..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            mc "Probably..."
            mc "But, I do feel drawn to Natsuki."
            mc "We just...{w=0.38}click..."
            show monika 2o
            mc "I'm really happy whenever we get to spend time around each other."
            mc "And I do think she feels the same way."
            m 2n "I see..."
            mc "I have nothing against Natsuki, I really don't..."
            mc "I think I just...{w=0.38}like Yuri better..."
            mc "But if I ever told her that Natsuki gave me this, she'd flip out."
            m 2m "Yeah...{w=0.38}she would..."






if hangout1 == "Yuri":
    if hangout2 == "Monika":
        show monika 2f
        mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
        mc "And last Sunday, I did feel like maybe there was something there..."
        mc "I don't know...{w=0.38}I guess I've been interested in getting to know the others a little bit lately..."
        show monika u114311
        mc "And...{w=0.38}it's been nice getting to know you too, Monika."
        show monika 2m
        mc "Especially since we really haven't talked that much recently..."
        m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
        m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
        mc "Well..."
        m 1e "Come on, [player]..."
        m 5a "I've seen the way you've looked at me..."
        m "How you're always stumbling over your sentences when I compliment you..."
        m "How I take your breath away whenever I get close to you..."
        show monika smirk
        m "It's really sweet~"
        mc "Monika, I..."
        "I'm completely left speechless."
        show monika 2m
        mc "I really have always wanted to get to know you..."
        mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
        m 2n "Yeah..."
        m 2e "But, let's figure this out first, okay?"
        mc "Yeah..."





if hangout1 == "Monika":
    if hangout2 == "Sayori":
            show monika 2f
            mc "I don't know..."
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            show monika 2m
            m 2g "You're not having second thoughts about your answer to her confession, are you?"
            show monika 2f
            mc "I don't know..."
            mc "I'm worried about her..."
            mc "I've known her practically my whole life..."
            show monika 2o
            mc "Ever since last Sunday, she's been acting different around me..."
            mc "She really didn't handle my response well..."
            mc "And since then, I've tried making things right with her..."
            m 2e "I think she'll be fine, [player]..."
            m "She just needs time."
            mc "But I feel like I should do more though..."
            mc "She was really emotional yesterday..."
            show monika 1q
            mc "We've made some progress, but I don't really know how I feel about her..."
            m 2r "[player], it's not smart for you to play around with her feelings if you don't know how you feel about her..."
            m 2e "I'm happy to hear that you guys are working to make things right..."
            m 2m "But you're probably better off just being friends with her..."
            m 2e "I don't think she can handle anything more right now..."
            mc "Yeah...{w=0.38}you're right..."
            show monika 2m
            mc "It's just been hard for me to think clearly lately..."
            mc "Especially now that I know [poem_giver]'s into me.."
            m 2e "It's all going to be okay, [player]..."
            m "I can help you through this..."
            mc "I really should've started talking to you sooner..."
            show monika u114311
            m "Eh? What do you mean?"
            mc "You always know what to do..."
            mc "It's like you're the answer to my problems!"
            mc "I mean as crazy it sounds, I just feel like if I spent time with you earlier..."
            mc "I don't know...{w=0.38}maybe things would be less crazy..."
            mc "I guess what I'm trying to say is:{w=0.38}it's been nice getting to know you..."
            m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
            m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
            mc "Well..."
            m 1e "Come on, [player]..."
            m 5a "I've seen the way you've looked at me..."
            m "How you're always stumbling over your sentences when I compliment you..."
            m "How I take your breath away whenever I get close to you..."
            show monika smirk
            m "It's really sweet~"
            mc "Monika, I..."
            "I'm completely left speechless."
            show monika 2m
            mc "I really have always wanted to get to know you..."
            mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
            m 2n "Yeah..."
            m 2e "But, let's figure this out first, okay?"
            mc "Yeah..."



if hangout1 == "Monika":
    if hangout2 == "Natsuki":
            show monika 2f
            mc "I don't know..."

            if encore_festivalquestion_2 == "Natsuki":
                mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
                mc "And last Sunday, I did feel like maybe there was something there..."
                mc "I really didn't expect to be like that with her yesterday..."
                show monika 2m
                mc "She really caught me by surprise..."
                show monika 2n
                m "It's fine, [player]..."
                m 2e "Don't worry about it..."
                mc "Okay..."
                mc "Still, I'll admit that I'm surprised that she'd give me this..."
                m 2p "Maybe this is her attempt at reaching out to you..."
                m 2n "To confirm her feelings for you..."
                mc "Probably..."
                show monika 2m
                mc "And look, I like her to some extent..."
                mc "It's been great getting to know her..."
                show monika u114311
                mc "But...{w=0.38}it's been nice getting to know you too, Monika."
                show monika 2m
                mc "Especially since we really haven't talked that much recently..."
                m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
                m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
                mc "Well..."
                m 1e "Come on, [player]..."
                m 5a "I've seen the way you've looked at me..."
                m "How you're always stumbling over your sentences when I compliment you..."
                m "How I take your breath away whenever I get close to you..."
                show monika smirk
                m "It's really sweet~"
                mc "Monika, I..."
                "I'm completely left speechless."
                show monika 2m
                mc "I really have always wanted to get to know you..."
                mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
                m 2n "Yeah..."
                m 2e "But, let's figure this out first, okay?"
                mc "Yeah..."


            if encore_festivalquestion_2 == "Yuri":
                mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
                mc "And last Sunday, I did feel like maybe there was something there..."
                mc "I don't know...{w=0.38}I guess I've been interested in getting to know the others a little bit lately..."
                mc "Though, I really didn't expect to be like that with Natsuki yesterday, honest!"
                show monika 2m
                m "It's fine, [player]..."
                m 2e "Don't worry about it..."
                mc "Okay..."
                mc "Still, I'll admit that I'm surprised that Yuri would give me this..."
                m 2p "Well you haven't spent too much time around her lately."
                m 2p "Maybe this is her attempt at reaching out to you..."
                m 2n "To confirm her feelings for you..."
                show monika 2m
                mc "Probably..."
                mc "And look, I like her to some extent..."
                mc "It's been great getting to know her..."
                show monika u114311
                mc "But...{w=0.38}it's been nice getting to know you too, Monika."
                show monika 2m
                mc "Especially since we really haven't talked that much recently..."
                m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
                m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
                mc "Well..."
                m 1e "Come on, [player]..."
                m 5a "I've seen the way you've looked at me..."
                m "How you're always stumbling over your sentences when I compliment you..."
                m "How I take your breath away whenever I get close to you..."
                show monika smirk
                m "It's really sweet~"
                mc "Monika, I..."
                "I'm completely left speechless."
                show monika 2m
                mc "I really have always wanted to get to know you..."
                mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
                m 2n "Yeah..."
                m 2e "But, let's figure this out first, okay?"
                mc "Yeah..."




if hangout1 == "Monika":
    if hangout2 == "Yuri":
        show monika 2f
        mc "I don't know..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "I don't know...{w=0.38}I guess I've been interested in getting to know the others a little bit lately..."
            mc "Though, I really didn't expect to be like that with Yuri yesterday, honest!"
            show monika 2m
            m "It's fine, [player]..."
            m 2e "Don't worry about it..."
            mc "Okay..."
            mc "Still, I'll admit that I'm surprised that Natsuki would give me this..."
            m 2p "Well you haven't spent too much time around her lately."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            show monika 2m
            mc "Probably..."
            mc "And look, I like her to some extent..."
            mc "It's been great getting to know her..."
            show monika u114311
            mc "But...{w=0.38}it's been nice getting to know you too, Monika."
            show monika 2m
            mc "Especially since we really haven't talked that much recently..."
            m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
            m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
            mc "Well..."
            m 1e "Come on, [player]..."
            m 5a "I've seen the way you've looked at me..."
            m "How you're always stumbling over your sentences when I compliment you..."
            m "How I take your breath away whenever I get close to you..."
            show monika smirk
            m "It's really sweet~"
            mc "Monika, I..."
            "I'm completely left speechless."
            show monika 2m
            mc "I really have always wanted to get to know you..."
            mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
            m 2n "Yeah..."
            m 2e "But, let's figure this out first, okay?"
            mc "Yeah..."



        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "I really didn't expect to be like that with her yesterday..."
            show monika 2m
            mc "She really caught me by surprise..."
            show monika 2n
            m "It's fine, [player]..."
            m 2e "Don't worry about it..."
            mc "Okay..."
            mc "Still, I'll admit that I'm surprised that she'd give me this..."
            m 2p "Maybe this is her attempt at reaching out to you..."
            m 2n "To confirm her feelings for you..."
            show monika 2m
            mc "Probably..."
            mc "And look, I like her to some extent..."
            mc "It's been great getting to know her..."
            show monika u114311
            mc "But...{w=0.38}it's been nice getting to know you too, Monika."
            show monika 2m
            mc "Especially since we really haven't talked that much recently..."
            m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
            m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
            mc "Well..."
            m 1e "Come on, [player]..."
            m 5a "I've seen the way you've looked at me..."
            m "How you're always stumbling over your sentences when I compliment you..."
            m "How I take your breath away whenever I get close to you..."
            show monika smirk
            m "It's really sweet~"
            mc "Monika, I..."
            "I'm completely left speechless."
            show monika 2m
            mc "I really have always wanted to get to know you..."
            mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
            m 2n "Yeah..."
            m 2e "But, let's figure this out first, okay?"
            mc "Yeah..."



if hangout1 == "Monika":
    if hangout2 == "Monika":
        mc "I really don't know..."
        mc "I've enjoyed spending time around her, she's been fun to be around..."
        mc "And I had a blast with her last Sunday!"
        show monika u114311
        mc "But...{w=0.38}it's been nice getting to know you too, Monika."
        show monika 2m
        mc "Especially since we really haven't talked that much..."
        m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
        m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
        mc "Well..."
        m 1e "Come on, [player]..."
        m 5a "I've seen the way you've looked at me..."
        m "How you're always stumbling over your sentences when I compliment you..."
        m "How I take your breath away whenever I get close to you..."
        show monika smirk
        m "It's really sweet~"
        mc "Monika, I..."
        "I'm completely left speechless."
        show monika 2m
        mc "I really have always wanted to get to know you..."
        mc "And I'm glad we've gotten that opportunity, and well, who knows what'll happen next..."
        m 2n "Yeah..."
        m 2e "But, let's figure this out first, okay?"
        mc "Yeah..."


m 1d "Does Sayori know that [poem_giver] gave you this?"
mc "No, I didn't tell her."
mc "And I really don't want to drag her into this."
m 1d "Yeah, it's probably for the best."
m 1e "You're better off figuring out what you want to say to [poem_giver]."
mc "Alright..."
jump day3_plan

label day3_plan:
mc "So what should I say to her then?"
m 2e "Just tell her how you feel, [player]..."
m 2n "[poem_giver] wants to know what's in your heart..."
m 2d "You need to figure out who suits you best..."
m 2e "And when you're figuring it all out, you should ask yourself some questions."
mc "Like what?"
m 2e "Like who can you always count on?"
m 2m "Who you can you always trust?"
m "Who would you be the happiest with?"
m 2m "Who will always help you?"
m "Who wants to see you succeed and is capable of helping you?"
m 2e "Who are you proud to stand next to no matter what?"
m "Who will always put a smile on your face and build you up?"
m "Who isn't afraid to stand against the world with you?"
m 2m "And I think you know one girl who checks all those boxes, don't you?"
mc "I..."
m 2e "I know you'll make the best decision for the club, [player]."
m 5a "I have faith in you."
show monika 2a
"Monika's questions begin to echo in my head."
"Who would I be the happiest with?"
"Who can I always trust?"
"Who would I be proud to say: 'Yeah, that's my girlfriend!' to my friends and family?"
"I guess it'd have to be..."
$ style.say_dialogue = style.edited
show monika 2q
"{cps=50}Monika.{nw}"
$ style.say_dialogue = style.normal
show monika 2e
"..."
"I'll definitely have a lot to think about later..."
mc "Thanks Monika, I really appreciate the advice!"
m 1k "No problem, [player]!"
m 1e "I hope I calmed your nerves a bit."
mc "Yeah...{w=0.38}you helped."
mc "Though, I don't know if I'm ready for the club today..."
show monika 2o
mc "I don't know if I'm ready to deal with all this..."
m 2e "I'm sure she won't ask you about it today, [player]."
m 2d "But it wouldn't hurt to decide on what you want soon."
mc "Yeah...{w=0.38}the sooner the better I guess."
m 2e "Yeah."
"Monika takes a look at her watch."
m 1b "We still have some time before lunch period ends..."
m 1e "Would you care to join me?"
mc "Sure! Stressing over this does work up quite the appetite..."
m 1l "I'm sure it has, [player]."
m 1a "Come on, let's head back."
stop music fadeout 3.0
"Without another word, Monika and I head down the steps back to the cafeteria."
show monika at thide
hide monika
show bg cafeteria
with wipeleft_scene
"I really wasn't social with Monika and her friends when we came back to join them."
"Other then some  occasional chatting, I mostly kept my mouth shut and zoned out."
"My mind was racing the entire time, attempting to answer the questions Monika gave me."
"And I'm still a little paranoid that [poem_giver] is going to try to talk to me in the club later..."
"I don't feel prepared for this..."
"But, I guess I did sort of ask for this to happen..."
"Now I've just got to figure out what I want to do next..."
show monika 1e at t11 zorder 2
"I really need to thank Monika when this all over."
show monika cute
"Her advice has been pretty helpful so far, and I feel like I'll ultimately figure things out thanks to her..."
"She certainly has been dependable..."
show monika 1m
play audio school
"Before I can finish my thought, the school bell rings, signifying the end of lunch period for me."
mc "Well, I guess it's back to boring old math for me..."
a "Good luck, [player]!"
r "Yeah! It was nice catching up with you!"
mc "Likewise."
m 2b "I'll see you girls later!"
a "Later Monika!"
show monika 1a
"Akari and Ria pack their things and walk out of the cafeteria, leaving me alone with just Monika."
mc "Well, I guess I'll see you at the club later then?"
show monika 2e
m "Yeah, I'll see you then."
m 2m "Hopefully you're able to give those questions some more thought."
mc "I will, it's certainly a lot to think about."
m 1e "It'll all be worth it in the end, [player], believe me."
mc "Well, I do trust you so..."
m 5a "Looks like you've already been giving those questions some thought, huh?"
"My face turns flush with embarrassment."
mc "W-{w=0.38}well yeah..."
mc "You're the person I trust most to help me through this!"
m "How interesting..."
mc "What do you mean?"
m 2n "Ah, don't worry about it..."
m 2e "You have enough on your plate as is right now..."
mc "Yeah, you're right..."
show monika 2e
"Monika shoots me a reassuring smile, and I can't help but return one myself."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        m 2d "I can walk you back to your class if you'd like, [player]."
        show monika 2e
        "The world around me goes into a freeze frame."
        "She's actually willing to walk me back?"
        "Come on, [player], don't blow this!"
        mc "Oh! Well, uh...{w=0.38}sure..."
        m 2n "You seem surprised..."
        show monika 2m
        mc "Well...{w=0.38}I wasn't expecting you to ask me..."
        mc "And I'd hate to make you late to your own class..."
        m 2e "I'll be fine, [player], don't worry."
        mc "Well...{w=0.38}okay..."
        m 1j "Great! Come on! Let's go!"
        "I timidly follow Monika out of the cafeteria."
        jump day3_hallway1


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m 2e "Do you want me to walk you back to class?"
        "My heart races a million miles a second as soon as Monika finishes her question."
        "She...{w=0.38}actually wants to spend more time with me?"
        "I don't know...{w=0.38}there's a lot to think about and I think I'd rather be alone right now..."
        show monika 5a
        "But then again:{w=0.38} this is Monika, and I guess a little company wouldn't hurt..."
        "She was nice enough to hear me out after all..."
        show monika 1a
        "But what if [poem_giver] sees us and gets the wrong idea?"

        if encore_sayoriquestion_1 == True:
            "And what if Sayori sees us..."
            jump day3_rigged


        if encore_sayoriquestion_1 == False:
            pass
            jump day3_rigged

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Monika":
        m 2e "Do you want me to walk you back to class?"
        "My heart races a million miles a second as soon as Monika finishes her question."
        "She...{w=0.38}actually wants to spend more time with me?"
        "I don't know...{w=0.38}there's a lot to think about and I think I'd rather be alone right now..."
        show monika 5a
        "But then again:{w=0.38} this is Monika, and I guess a little company wouldn't hurt..."
        "She was nice enough to hear me out after all..."
        show monika 1a
        "But what if [poem_giver] sees us and gets the wrong idea?"

        if encore_sayoriquestion_1 == True:
            "And what if Sayori sees us..."
            "She isn't exactly happy with me being around Monika right now..."
            jump day3_rigged


        if encore_sayoriquestion_1 == False:
            pass
            jump day3_rigged

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m 2e "If you want, [player], I can walk you back to your class."
        mc "Oh! Uhhh..."
        "My mind completely goes blank."
        "I don't really get the chance to spend too much time around Monika..."
        "But with everything going on, I'm hardly in a social mood."
        show monika 5a
        "Then again:{w=0.38} this is Monika, and I guess a little company wouldn't hurt..."
        "She was nice enough to hear me out after all..."
        show monika 1a
        "But what if [poem_giver] sees us and gets the wrong idea?"

        if encore_sayoriquestion_1 == True:
            "And what if Sayori sees us and {i}also{/i} gets the wrong idea?"

            if hangout2 == "Natsuki" or hangout2 == "Yuri":
                "She's already angry at me for yesterday, I don't want to get into more trouble with her..."
                jump day3_notrigged

            if hangout2 == "Sayori":
               pass
               jump day3_notrigged


        if encore_sayoriquestion_1 == False:
            pass
            jump day3_notrigged



label day3_rigged:

    show monika 1q at t11 zorder 1

    python:
        #"Should I let Monika walk me back?"
#        renpy.say(narrator, "Should I let Monika walk me back?", interact=False)
#        madechoice = renpy.display_menu([("Yes.", "true"), ("No.", "false")], screen="encore_rigged_choice")
        madechoice = show_rigged_choice(narrator, "Should I let Monika walk me back?", [("Yes.", "true"), ("No.", "false")])

    #If you pick No
    $ m_walk = False
    if madechoice != "true":
        window hide(None)
        show bg cafeteria
        show monika 1f
        mc "Sorry, Monika...{w=0.38}I think I should be alone for now..."
        mc "I do have a lot to think over..."
        m 2n "It's fine, [player]..."
        m 2e "I'll see you in the club."
        mc "Yeah...{w=0.38}see you then!"
        show monika at thide
        hide monika
        jump day3_hallway2


    #If you pick Yes
    $ m_walk = True
    if madechoice != "false":
        window hide(None)
        show bg cafeteria
        show monika 1a
        mc "Sure! We can walk back!"
        show monika 1k
        m "Awesome!"
        m 2b "Lead the way, [player]!"
        show monika 2a
        "I'm not entirely sure why Monika wanted to walk with me so badly."
        "But hey, I'll oblige, it wouldn't hurt to."
        "I smile to myself as we make our way out of the cafeteria."
        show monika thide
        hide monika
        jump day3_hallway1




label day3_notrigged:
    menu:
        "Should I let Monika walk me back?"
        "Yes.":
            $ m_walk = True
            jump m_walk_yes
        "No.":
            $ m_walk = False
            jump m_walk_no


label m_walk_yes:
mc "Sure! We can walk back!"
show monika 1k
m "Awesome!"
m 2b "Lead the way, [player]!"
show monika 2a
"I'm not entirely sure why Monika wanted to walk with me so badly."
"But hey, I'll oblige, it wouldn't hurt to."
"I smile to myself as we make our way out of the cafeteria."
show monika thide
hide monika
jump day3_hallway1


label m_walk_no:
show monika 1f
mc "Sorry, Monika...{w=0.38}I think I should be alone for now..."
mc "I do have a lot to think over..."
m 2n "It's fine, [player]..."
m 2e "I'll see you in the club."
mc "Yeah...{w=0.38}see you then!"
show monika at thide
hide monika
jump day3_hallway2


label day3_hallway1:
scene bg corridor
with wipeleft_scene
play music t3 fadein 2.0
"Monika and I make our way through the crowded hallways up towards the second floor."
show monika 1a at t11 zorder 1
"I turn to her, our eyes meeting."
mc "You know you didn't really have to walk me back..."
m 1g "Well I just want to make sure you're holding up okay..."
m 1m "A lot of people tend to break down in these kinds of situations..."
show monika 1e
mc "Yeah...{w=0.38}but I'll be fine...{w=0.38}I think."
m 1b "Well you can always count on me if you need anything, [player]."
show monika 1j
mc "You're too kind, Monika, really..."
m 1k "I try, [player]!"
m 1e "It's important to me that you're always in the best state of mind."
show monika 1k
"I avert my gaze to hide my incoming smile."
"Jeez, I didn't think Monika would ever be this nice to me..."
"It's almost too much to handle!"
show monika 1a
"As we walk through the hallways, I can't help but notice several of the other students catching glances in our direction and whispering."
show monika 1m
"Monika apparently picks up on this too."
"They're not thinking that we're...{w=0.38}{i}a couple?!?{/i}"

if encore_sayoriquestion_1 == True:
    "Oh God, if Sayori heard those rumors..."

if encore_sayoriquestion_1 == False:
    "That idea only continues to make me flustered."

"Monika slides up to me to whipser in my ear."
m 1n "This is nice, isn't it?"
m 1e "To have someone walk with you, to keep you company?"
mc "Y-{w=0.38}yeah...{w=0.38}it is..."


$ day3_hallway = ''




if encore_sayoriquestion_1 == True:
    $ day3_hallway = "Sayori"
    jump s_hallway_interaction



if encore_sayoriquestion_1 == False:
    jump p_hallway_interactions


label p_hallway_interactions:

#Sayori

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction

if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction


if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction


if hangout1 == "Sayori":
    if hangout2 == "Monika":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction



#Natsuki

if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction


if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction


if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction


if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction


#Yuri

if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction

if hangout1 == "Yuri":
    if hangout2 == "Monika":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction


#Monika

if hangout1 == "Monika":
    if hangout2 == "Sayori":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction

if hangout1 == "Monika":
    if hangout2 == "Yuri":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction






label s_hallway_interaction:
show monika tease
m "{cps=15}Does Sayori-{nw}"
$ s_name = "???"
show monika shock at h11
stop music
s "Heyyyyyy!!!!"
"I hear someone yelling to us from across the hallway."
"Wait a second...{w=0.38}I recognize that yelling anywhere..."
$ s_name = "Sayori"
show monika surprised at t21 zorder 1
show sayori 1q at t22 zorder 2
play music e15 fadein 1.0
m "S-{w=0.38}Sayori?!?"
s 4r "The one and only!"
m "My! You startled me!"
s 2g "Sorry, Monika, I hope I didn't scare you too bad!"
m 2e "No, no, you're fine!"
mc "Trust me, you get used to it. She does this all the time with me."
m 2n "I see..."
show monika 2m
mc "How're you doing, Sayori?"
s 1x "I'm doing great! I just went to get some water and I ran into you guys!"
mc "Yeah, we're just heading back from lunch, turns out we have the same period!"
show sayori 1b
show monika 2e
mc "Crazy, right?"

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s 1d "That's awesome, [player]!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            mc "Yeah! It really is..."
            m 2b "[player] got the chance to catch up with Akari and Ria as well!"
            s 1d "That's great to hear! Thank you for letting him sit with you, Monika."
            m 2n "Ah, it was no trouble at all..."
            m 2e "It was the least I could do."
            show monika u121351
            "Monika shoots me a quick wink."


if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            show monika 2m
            s 1l "That's...{w=0.38}great to hear, [player]..."
            show sayori 1k

            if hangout2 == "Monika":
                "I guess I know why Monika hasn't talked to Sayori yet..."
                "I really shouldn't have brought that up in front of them..."

            if hangout2 == "Natsuki" or hangout2 == "Yuri":
                "I guess Sayori still isn't really happy with the idea of me spending time with the others..."
                "Especially with what happened yesterday..."

            "Monika clears her voice to break the tension."
            m 2b "Well, hey, [player] got the chance to catch up with Akari and Ria as well!"
            m 2e "He had fun, right, [player]?"
            mc "Y-{w=0.38}yeah...{w=0.38}it was nice..."
            show sayori 1d
            s "I'm glad you had fun, [player]..."
            s 1q "It's always nice to make new friends!"
            m 2j "[player]'s become quite the social butterfly since he's joined the club!"
            mc "Ah! Well..."
            show sayori 1y
            "I guess Monika has a point there..."
            "If it weren't for the club, I'd probably still be sitting in the back of the cafeteria!"
            mc "I guess so..."
            "Sayori seems to be uncharacteristically disengaged from the conversation."
            "As if she's trying to hold back something..."
            show sayori 2d
            s "Well, thank you for letting him sit with you, Monika."
            m 2n "Ah, it was no trouble at all..."
            m 2e "It was the least I could do."
            show monika u121351
            "Monika shoots me a quick wink."
            show sayori 1i
            "Though it looks like Sayori caught that, and she shoots me a brief look of suspicion."
            "Great..."


if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            s 1x "That's great to hear!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            s 1y "I just wish we had the same lunch period like last year..."
            mc "Yeah, it's a bummer..."
            s 1d "Well, thank you for letting him sit with you, Monika."
            m 2n "Ah, it was no trouble at all..."
            m 2e "It was the least I could do."
            show monika u121351
            "Monika shoots me a quick wink."
            show sayori 1g
            "Though it looks like Sayori caught that, and she briefly looks quizzically at me."
            "Great..."



if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s 1d "That's awesome, [player]!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            s 1y "Too bad we aren't sharing the same lunch period this year..."
            mc "Yeah, it really is..."
            s 1d "Well, hey, it was nice for Monika to let you sit with her."
            m 2n "Ah, it was no trouble at all..."
            m 2e "It was the least I could do."
            show monika u121351
            "Monika shoots me a quick wink."
            show sayori 1g
            "Though it looks like Sayori caught that, and she briefly looks quizzically at me."
            "Great..."





if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                show monika 2m
                s 1l "That's...{w=0.38}great to hear, [player]..."
                show sayori 1k
                "I guess Sayori isn't quite over yet what happened yesterday..."
                "Monika clears her voice to break the tension."
                m 2b "Well, hey, [player] got the chance to catch up with Akari and Ria as well!"
                m 2e "He had fun, right, [player]?"
                mc "Y-{w=0.38}yeah...{w=0.38}it was nice..."
                show sayori 1d
                s "I'm glad you had fun, [player]..."
                s 1q "It's always nice to make new friends!"
                m 2j "[player]'s become quite the social butterfly since he's joined the club!"
                mc "Ah! Well..."
                show sayori 1y
                "I guess Monika has a point there..."
                "If it weren't for the club, I'd probably still be sitting in the back of the cafeteria!"
                mc "I guess so..."
                "Sayori seems to be uncharacteristically disengaged from the conversation."
                "As if she's trying to hold back something..."
                show sayori 2d
                s "It was nice of Monika to let you sit with her."
                m 2n "Ah, it was no trouble at all..."
                m 2e "It was the least I could do."
                show monika u121351
                "Monika shoots me a quick wink."
                show sayori 1i
                "Though it looks like Sayori caught that, and she shoots me a brief look of suspicion."
                "Great..."




if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            s 1x "That's great to hear!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            s 1y "I just wish we had the same lunch period like last year..."
            mc "Yeah, it's a bummer..."
            s 1d "Well, it was nice of Monika to let you sit with her."
            m 2n "Ah, it was no trouble at all..."
            m 2e "It was the least I could do."
            show monika u121351
            "Monika shoots me a quick wink."
            show sayori 1g
            "Though it looks like Sayori caught that, and she briefly looks quizzically at me."
            "Great..."


show sayori 1c
s "Hey, Monika, isn't your class on the other side of the school?"
show sayori 1b
m 2l "Ah, well, I don't think taking a slight detour from my normal route will make me late or anything."
show monika 2e
s 1r "Well, that's good!"
s 1g "I'd really love to stay and chat, but I have to head back to class pretty soon..."
mc "It's alright, Sayori, we'll see you in the club!"
s 1q "Yeah! I can't wait!"
s 1x "I'll see you guys later!"
show sayori at thide
hide sayori
"We wave goodbye to Sayori as we head our separate ways."
show monika at thide
hide monika
stop music fadeout 2.0
scene bg corridor
with wipeleft_scene
"Not too long after our run-in with Sayori, Monika and I finally make it to my classroom."
show monika 1a at t11 zorder 1
mc "Thanks for walking back with me, Monika!"
m 1e "Anytime, [player]!"
m 5a "I hope you have a great rest of your day~"
mc "Y-{w=0.38}you too!"
show monika 5a at face
"Monika takes a step closer to me and leans in to my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm left completely dazed as I watch Monika gracefully walk down the hallway and turn the corner, towards the the other side of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sit down, refusing to make eye contact with anyone, as I process what just happened."
jump day3_mono



label n_hallway_interaction:
show monika tease
$ n_name = "???"
m "{cps=15}Does Natsuki-{nw}"
show monika shock
stop music
n "Hey! What's up?!?"
"I hear someone yelling to us from across the hallway."
"Wait a second...{w=0.38}I recognize that voice..."
$ n_name = "Natsuki"
show monika surprised at t21 zorder 1
show natsuki 3z at t22 zorder 2
play music e14 fadein 1.0
m "N-{w=0.38}Natsuki?!?"
n 3b "Well duh! Who else?"
m "My! You startled me!"
n 3d "I was really going for [player]..."
show monika 2m
mc "Hey!"
n 3g "Well you do it to me all the time!"
n 4w "Why can't I do it to you?"
mc "Fair enough..."
m 2e "How're you doing Natsuki?"
n 1a "Oh, I'm doing great! I'm just heading to my next class!"
m 2b "That's nice!"
show monika 2a
mc "Yeah, we're just heading back from lunch, turns out we have the same period!"
show natsuki 1c
show monika 2e
mc "Crazy, right?"


if hangout1 == "Natsuki":
    if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
        n 1q "Y-{w=0.38}yeah..."
        show monika 2m
        "I guess Natsuki's still a little irritated over what she saw yesterday..."
        "Then again she is the kind of person I'd expect to hold a grudge..."
        "Monika clears her voice to break the tension."
        m 2b "Well, hey, [player] got the chance to catch up with Akari and Ria as well!"
        m 2e "He had fun, right, [player]?"
        mc "Y-{w=0.38}yeah...{w=0.38}it was nice..."
        show natsuki 5w
        n "Well, it's good that [player] can talk to the other people..."
        n 2l "It'd be weird if we were the only people he talked to!"
        mc "Aw come on, you don't give me enough credit, Natsuki."
        mc "I talk to other people too, you know!"
        n 5l "Like who?"
        mc "Well..."
        "I guess she has me here."
        "Other than online, there really aren't too many other people I talk to outside the club..."
        "Heck, I usually just sit by myself in the cafeteria..."
        "Still, I try to come up with a retort to Natsuki's jab."
        mc "That's not important!"
        n 5z "Well don't worry, [player], you'll always have us!"
        n 4b "And it's good to know someone who can always whip you up some mean cupcakes!"
        mc "Yeah, you're not too bad yourself."
        n 1m "Hey..."
        n 1w "I fixed your taste in manga for you!"
        mc "Yeah, that's true..."
        mc "But yeah, getting to know more people certainly wouldn't hurt."
        m 3b "Exactly!"
        m 3m "And letting you sit with us was the least I could do."
        show monika u121351
        "Monika shoots me a quick wink."
        show natsuki 5n
        "Though it looks like Natsuki caught that, and she shoots me a suspicious look."
        "Great..."




if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        n 1j "Yeah!"
        show monika 2l
        n 5y "Now I won't have to hear you complain about not having anyone to sit with!"
        mc "H-{w=0.38}hey! I wasn't complaining-"
        m 2e "Well in any case, it was nice of you to join us, [player]."
        n 3z "Just hope he didn't gross you out too much, Monika!"
        m 5a "Oh no, he was very well behaved!"
        mc "Hey! I'm not a kid!"
        n 5z "Relax, [player], we're just messing with you!"
        m 3b "But in all seriousness, thanks for sitting with us!"
        mc "Ah, well I really should be thanking you after all..."
        m 2e "It was the least I could do for you."
        show monika u121351
        "Monika shoots me a quick wink."
        show natsuki 1m
        "Though it looks like Natsuki caught that, and she briefly looks quizzically at me."
        "Great..."


if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Natsuki":
        n 2k "Yeah, that must've been nice."
        n 1y "Too bad you don't have lunch with me, you'd be set for life with the stuff I bring!"
        mc "Well, there's always hope for next year I suppose."
        n 2j "Guess you're stuck with Monika for now though."
        show natsuki u121143
        n "Just try not to be too gross around her!"
        mc "Oh, so you've developed a tolerance around me, huh?"
        n 1a "Pretty much!"
        n 5t "You're not so bad when you get used to it..."
        mc "Well, thanks I guess..."
        m 5a "I can promise you, [player] was very well behaved!"
        m "Isn't that right?"
        mc "Aww come on..."
        "Handling both of their teasing is starting to become a bit much for me to bear..."
        n 5z "Well someone needs to straighten him out when he gets out of line!"
        n 5j "Looks like you did a good job with him, Monika!"
        m 1l "Thanks, Natsuki!"
        m 2m "I'll be sure to keep it up..."
        mc "Ah, jeez..."
        "I playfully roll my eyes at them."
        mc "Still, it was nice of you to let me sit with you, Monika!"
        m 2e "Hey, all things considered, it was the least I could do for you."
        show monika u121351
        "Monika shoots me a quick wink."
        show natsuki 1m
        "Though it looks like Natsuki caught that, and she briefly looks quizzically at me."
        "Great..."



show natsuki 1t
n "So, do you guys have the same class or something?"
m 2e "No, I was just walking [player] back."
m 2b "I have Mr. Takahashi's class next."
show natsuki 1m
n "Isn't that all the way on the other side of the school?"
m 2l "Ah, well, I don't think taking a slight detour from my normal route will make me late or anything."
show monika 2e
n 1q "Yeah, I guess..."
show monika 2m
"There's a bit of an awkward pause between us as the other students begin clearing the hallways."
n 1k "Well, I guess that's my cue to head out."
mc "It's alright, Natsuki, we'll see you in the club!"
n 4l "Yeah! I'm looking forward to it!"

if poem_giver == "Natsuki":
    "Well, there goes my anxiety about going to the club today."
    "Though, I do my best to smile back."

if poem_giver == "Yuri":
    pass

mc "Laters!"
m 2e "We'll see you later, Natsuki!"
n 2z "Bye!"
show natsuki at thide
hide natsuki
"We wave goodbye to Natsuki as we head our separate ways."
show monika at thide
hide monika
stop music fadeout 2.0
scene bg corridor
with wipeleft_scene
"Not too long after our run-in with Natsuki, Monika and I finally make it to my classroom."
show monika 1a at t11 zorder 1
mc "Thanks for walking back wth me, Monika!"
m 1e "Anytime, [player]!"
m 5a "I hope you have a great rest of your day~"
mc "Y-{w=0.38}you too!"
show monika 5a at face
"Monika takes a step closer to me and leans in to my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm left completely dazed as I watch Monika gracefully walk down the hallway and turn the corner, towards the the other side of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sit down, refusing to make eye contact with anyone as I process what just happened."
jump day3_mono




label y_hallway_interaction:
show monika tease
m "{cps=15}Does Yuri-{nw}"
$ y_name = "???"
show monika shock at h11
stop music
play sound "sfx/fall2.ogg"
y "EEEK!"
"While I wasn't looking, I bumped into someone, causing them to immediately drop all their textbooks."
"Everyone in the hallway suddenly turns towards me."
"I hastily turn to face who I just bumped into."
show monika surprised at t21 zorder 1
show yuri 3o at t22 zorder 2
play music e16 fadein 1.0
"It's Yuri!"
mc "Oh, no! Are you okay, Yuri?"
$ y_name = "Yuri"
y "Uuuu....{w=0.38}I'll be alright."
"I look down to see the pile of books that Yuri dropped."
"I'm able to recognize Portrait of Markov among her textbooks."
"She really doesn't leave home without it, it seems..."
mc "I'll get that for you..."
"I bend down to pick up Yuri's books."
m "Y-{w=0.38}Yuri!"
m "You startled us!"
y 3q "Sorry about that!"
y "I should really pay more attention to where I'm going..."
m 2n "Ah, you have no reason to be sorry."
m 2e "I'm just glad you're okay."
mc "Well, if anyone should be apologizing it should be me, I'm the one that bumped into you."
y 2s "Well, I guess we both owe an apology to each other..."
mc "Yeah...{w=0.38}I'm really sorry..."
show yuri 2c
"I'm barely able to lift up all of Yuri's textbooks and hand it to her."
mc "Jeez...{w=0.38}are those advanced level course textbooks?"
y 3d "Yep! I'm taking three this semester!"
"Poor girl..."
mc "Well, I'm impressed you can carry all that!"
y 3i "It's a side benefit when you're taking these advanced classes!"
y 3d "It really builds up your arm strength!"
m 2l "Yeah, I know what you mean! Lifting those textbooks isn't for the faint of heart!"
y 3b "Matter of fact, I'm actually heading to my last advanced class for the day!"
m 2e "That's nice, Yuri! Hope you have fun!"
y 3a "I'll try."
y 3b "So, where you guys heading from?"
mc "Ah, we're just heading back from lunch, turns out we have the same period!"
show yuri 3e
show monika 2e
mc "Crazy right?"


if hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
        y 3q "Th-{w=0.38}that's nice, [player]..."
        show monika 2m
        "I guess Yuri's still a little agitated over what she saw yesterday..."
        "Knowing her, she probably thinks [hangout2] and I are a couple now..."
        "Monika clears her voice to break the tension."
        m 2b "Well, hey, [player] got the chance to catch up with Akari and Ria as well!"
        m 2e "He had fun, right, [player]?"
        mc "Y-{w=0.38}yeah...{w=0.38}it was nice..."
        y 3a "It's good to make new friends, [player]."
        y 3q "I just hope you don't forget about the ones you have..."
        "Yeah, she's still hung up over yesterday..."
        "I try to reassure her."
        show yuri 3s
        mc "Oh, come on! I could never forget about you!"
        mc "You're one of my favorite people in the club!"
        show monika 2h
        y 4e "R-{w=0.38}right..."
        y "I don't know why I'd think that..."
        show yuri 4a
        m 2e "Well, I'm really glad you got to join me for lunch, [player]..."
        mc "I should probably be thanking you..."
        mc "You're the one that invited me..."
        m 3m "It was the least I could do."
        show monika u121351
        "Monika shoots me a quick wink."
        show yuri 3e
        "Though it looks like Yuri caught that, and she shoots me a suspicious look."
        "Great..."






if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        y 3b "That's nice, [player]!"
        show monika 2h
        y 3q "I just wish we had lunch together too..."
        mc "Ah, I'm sure we'll get a chance next year..."
        m 2b "Maybe if we're really lucky, we'll all share the same lunch period next year!"
        m 2k "That way, we all get to spend more time together as a club!"
        y 2d "I'd certainly love that!"
        "It's truly amazing that a few weeks ago, I probably wouldn't have ever thought about any of this..."
        "Sharing a lunch period with the prettiest girls I've ever met..."
        "It's almost a dream come true!"
        mc "Yeah...{w=0.38}it'd be nice!"
        m 2e "Well, I'm really glad you got to join me for lunch, [player]..."
        mc "I should probably be thanking you..."
        mc "You're the one that invited me..."
        m 3m "It was the least I could do."
        show monika u121351
        "Monika shoots me a quick wink."
        show yuri 3e
        "Though it looks like Yuri caught that, and she shoots me a suspicious look."
        "Great..."




if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
    if hangout2 == "Yuri":
        y 3b "Well it's good to have company for lunch."
        y 3w "I wish I had the same opportunity as you guys..."
        m 2g "Aww, cheer up, Yuri! There's a chance we can have the same lunch period next year!"
        show monika 2e
        y 3q "I suppose you're right..."
        y 3d "Still, I'll always have my books to keep me company!"
        y 3m "Besides, I'm always able to get a good amount of work done."
        m "Well, that's good..."
        mc "Yeah! I could probably learn a thing or two from you Yuri!"
        mc "I usually just use that time to do things last minute..."
        show yuri 3f
        y "It's never a good idea to do things at the last minute, [player]."
        y 3k "It often leads to one's work being less than ideal..."
        mc "Looks like those advanced classes have taught you a lot!"
        y 3j "Yeah...{w=0.38}they have..."
        show yuri 3a
        m 2e "Well, I'm really glad you got to join me for lunch, [player]..."
        mc "I should probably be thanking you..."
        mc "You're the one that invited me..."
        m 3m "It was the least I could do."
        show monika u121351
        "Monika shoots me a quick wink."
        show yuri 3e
        "Though it looks like Yuri caught that, and she shoots me a suspicious look."
        "Great..."



show yuri 3f
y "So...{w=0.38}where you two off to now?"
m 2e "Ah, I was just walking [player] back."
m 2b "I have Mr. Takahashi's class next."
show yuri 3e
y "That's on the other side of the school."
m 2l "Ah, well, I don't think taking a slight detour from my normal route will make me late or anything."
show monika 2e
y 3q "I suppose you're right..."
show monika 2m
y 3a "Well, I wouldn't want to be late to my next class, so I'll let you guys go."
y 3d "See you guys at the club!"

if poem_giver == "Natsuki":
    pass

if poem_giver == "Yuri":
    "Well, there goes my anxiety about going to the club today."
    "Though, I do my best to smile back."

mc "Laters!"
m 2e "Bye, Yuri!"
y 2c "Good-bye!"
show yuri at thide
hide yuri
"We wave goodbye to Yuri as we head our separate ways."
show monika at thide
hide monika
stop music fadeout 2.0
scene bg corridor
with wipeleft_scene
"Not too long after our literal run-in with Yuri, Monika and I finally make it to my classroom."
show monika 1a at t11 zorder 1
mc "Thanks for walking back wth me, Monika!"
m 1e "Anytime, [player]!"
m 5a "I hope you have a great rest of your day~"
mc "Y-{w=0.38}you too!"
show monika 5a at face
"Monika takes a step closer to me and leans in to my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm left completely dazed as I watch Monika gracefully walk down the hallway and turn the corner, towards the the other side of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sit down, refusing to make eye contact with anyone as I process what just happened."
jump day3_mono



label day3_hallway2:
scene bg corridor
with wipeleft_scene
"I make my way up through the crowded hallways up towards the second floor."
"My eyes can't help but wander back and forth to the other various people walking with me."
"So many couples walking around me."
"What did it take for them to get together?"
"How big of a decision was it for them?"
"Did they have to struggle like I did?"
"Did they ever feel like they were being pulled in two different directions?"


if encore_sayoriquestion_1 == True:
    "Did they ever have second thoughts?"
    "And if they did, did they work through it?"

    if hangout1 == "Sayori" and hangout2 == "Sayori":
        "I mean, I don't think I'm regretting my decision with Sayori..."
        "But did I make it too soon?"

    if hangout1 == "Sayori" and hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        "I mean, I don't think I'm regretting my decision with Sayori..."
        "But...{w=0.38}I did kind of like being with [hangout2] yesterday..."
        "Does that mean I'm in love with them if I liked being close to them?"

    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" and hangout2 == "Sayori":
        "I mean, I don't think I'm regretting my decision with Sayori..."
        "But, I'll admit I'm a little interested to see what the others are all about..."
        "Did I get into a relationship with Sayori too soon?"



    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" and hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        "I mean, I don't think I'm regretting my decision with Sayori..."
        "But lately, I've just found myself more attracted to the others for some reason..."
        "Does that mean that I wasn't meant to be with Sayori?"




if encore_sayoriquestion_1 == False:
    "Did they have to break anyone's heart just to get what they wanted?"
    "Was it the right thing to do?"


"..."
"Well, this is going to keep me busy all day..."


if encore_sayoriquestion_1 == True:
    $ day3_hallway = "Sayori"
    jump s_hallway_interaction2


if encore_sayoriquestion_1 == False:
    jump p_hallway_interactions2


label p_hallway_interactions2:

#Sayori

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction2

if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction2

if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction2

if hangout1 == "Sayori":
    if hangout2 == "Monika":
        $ day3_hallway = "Sayori"
        jump s_hallway_interaction2


#Natsuki

if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction2

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction2

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction2

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction2

if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        $ day3_hallway = "Natsuki"
        jump n_hallway_interaction2

#Yuri

if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction2

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction2

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction2

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction2

if hangout1 == "Yuri":
    if hangout2 == "Monika":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction2


#Monika

if hangout1 == "Monika":
    if hangout2 == "Sayori":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction2

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction2

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction2

if hangout1 == "Monika":
    if hangout2 == "Yuri":
        $ day3_hallway = "Yuri"
        jump y_hallway_interaction2

if encore_festivalquestion_2 == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            $ day3_hallway = "Natsuki"
            jump n_hallway_interaction2

if encore_festivalquestion_2 == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            $ day3_hallway = "Yuri"
            jump y_hallway_interaction2



label s_hallway_interaction2:
$ s_name = "???"
s "Heyyyyyy!!!!"
"I hear someone yelling to me from across the hallway."
"Wait a second...{w=0.38}I recognize that yelling anywhere..."
$ s_name = "Sayori"
show sayori 1q at t11 zorder 1
play music e15 fadein 1.0
mc "S-{w=0.38}Sayori?!?"
s 4r "The one and only!"
mc "Ah! Didn't see you there!"
s 2g "I hope I didn't scare you, [player]!"
show sayori 1e
mc "Sayori, you can't scare me anymore, I know all your tricks!"
show sayori 5c
s "Well that's no fair!"
show sayori 5d
mc "Well if it's any consolation, you did catch me by surprise there."
s 1q "Guess I'll have to take that then~"
mc "Yeah..."
s 1s "Hehe~"
mc "So, how're you doing, Sayori?"
s 1x "I'm doing great! I was just went to get some water and I ran into you!"
mc "Yeah, I'm just heading back from lunch..."
show sayori 2d
s "How was it?"
mc "Surprisingly, it was actually alright."
mc "I found out that I had the same lunch period with Monika!"
show sayori 1b
mc "Crazy, right?"

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s 1d "That's awesome, [player]!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            mc "Yeah! It really is..."
            s 1y "It's too bad we aren't sharing the same lunch period this year..."
            mc "Ah, well, I'm sure we'll have something together next year at least."
            s 4q "I hope so too!"


if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            s 1l "That's...{w=0.38}great to hear, [player]..."
            show sayori 1k

            if hangout2 == "Monika":
                "I guess I know why Monika hasn't talked to Sayori yet..."
                "I really shouldn't have brought that up in front of her..."

            if hangout2 == "Natsuki" or hangout2 == "Yuri":
                "I guess Sayori still isn't really happy with the idea of me spending time with the others..."
                "Especially with what happened yesterday..."
                "I really shouldn't have brought that up in front of her..."

            "Sayori clears her voice to break the tension."
            show sayori 1d
            s "Well, I hope you had fun with her, [player]..."
            s 1q "It's always nice to spend time with friends!"
            mc "Ah! Well..."
            mc "You did help introduce me to her after all..."
            show sayori 1y
            mc "If it wasn't for you pushing me out of my comfort zone, I don't think I'd ever be as close to you, Monika or any of the others..."
            s "I guess you're right..."
            show sayori 1k
            "There's a bit of an awkward pause between us as the other students begin clearing the hallways."


if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            s 1x "That's great to hear!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            s 1y "I just wish we had the same lunch period like last year..."
            mc "Yeah, it's a bummer..."
            s 1d "Well, it was nice of Monika to let you sit with her."
            mc "Yeah, it was..."



if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s 1d "That's awesome, [player]!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            mc "Yeah! It really is..."
            s 1y "It's too bad we aren't sharing the same lunch period this year..."
            mc "Ah, well, I'm sure we'll have something together next year at least."
            s 4q "I hope so too!"





if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                s 1l "That's...{w=0.38}great to hear, [player]..."
                show sayori 1k
                "I guess Sayori isn't quite over yet what she saw yesterday..."
                "I really shouldn't have brought up that I was spending time with the others..."
                "Sayori clears her voice to break the tension."
                show sayori 1d
                s "Well, I hope you had fun with her, [player]..."
                s 1q "It's always nice to spend time with friends!"
                mc "Ah! Well..."
                mc "You did help introduce me to her after all..."
                show sayori 1y
                mc "If it wasn't for you pushing me out of my comfort zone, I don't think I'd ever be as close to you, Monika or any of the others..."
                s "I guess you're right..."
                show sayori 1k
                "There's a bit of an awkward pause between us as the other students begin clearing the hallways."





if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            s 1x "That's great to hear!"
            s 1q "It's good to have someone to keep you company during lunch period!"
            s 1y "I just wish we had the same lunch period like last year..."
            mc "Yeah, it's a bummer..."
            s "Well, I hope you had fun with her, [player]..."
            s 1q "It's always nice to spend time with friends!"
            mc "Ah! Well..."
            mc "You did help introduce me to her after all..."
            show sayori 1y
            mc "If it wasn't for you pushing me out of my comfort zone, I don't think I'd ever be as close to you, Monika or any of the others..."
            s "I guess you're right..."



show sayori 1c
s "So where you off to now?"
show sayori 1b
mc "Back to good ol' Algebra class with Saitō..."
s 1d "Awww...{w=0.38}Just try to keep your chin up, [player]!"
s 1r "We'll be in the club before you know it!"
mc "Yeah...{w=0.38}can't wait..."
s 2d "See? That's the spirt!"
"I'm really lucky that Sayori's bad at detecting sarcasm..."
"I'm still praying that [poem_giver] doesn't ask me about her letter and that everything can be normal for at least one more day..."
"And I still can't decide whether to show Sayori the poem that I got..."
"I can almost feel the weight of it growing in my jacket pocket."

if encore_sayoriquestion_1 == True:
    mc "Well hey, you always seem to make my day better..."
    s 2y "[player]..."
    s 1l "It's really you who makes my day better..."
    mc "Guess we're really good for each other like that, huh?"
    show sayori 1y
    "Sayori blushes brightly."
    "I can tell she wants to run up and hug me, but she doesn't want to draw any unnecessary attention to ourseleves.."


if encore_sayoriquestion_1 == False:
    "I try to fake a smile to Sayori."
    "Thankfully she seems to have bought it."


s 2b "Well, I need to head back to class now."
mc "Alright, I'll see you later!"
s 1r "Bye, [player]!"
show sayori at thide
hide sayori
stop music fadeout 2.0
"I wave goodbye to Sayori as we head our separate ways."
jump day3_mono



label n_hallway_interaction2:
$ n_name = "???"
n "Hey! What's up?!?"
"I hear someone yelling to me from across the hallway."
"Wait a second...{w=0.38}I recognize that voice..."
$ n_name = "Natsuki"
show natsuki 3z at t11 zorder 1
play music e14 fadein 1.0
mc "N-{w=0.38}Natsuki?!?"
n 3b "Well duh! Who else?"
mc "Ah, I just wasn't expecting to run into you!"
mc "It's not like I really see you around the hallways too much."
n 3c "I guess that's true..."
n 3d "But man, you should've seen the look on your face!"
n 3y "You looked like you just saw a ghost!"
mc "Ah well, I've just been busy thinking I guess..."
show natsuki 4m
n "About what?"
mc "It's...{w=0.38}complicated...."
n 5m "Is it something I can help out with?"

if poem_giver == "Natsuki":
    "Does she know????"
    "My heart quickens as I try to figure out how to respond."

if poem_giver == "Yuri":
    "She probably wouldn't react well if I told her what Yuri gave me..."


mc "I'll let you know if it's something you can help with..."
mc "It's nothing super serious..."
n 5q "Alright, [player]..."
n 5n "But don't be afraid to talk to me if you need to!"
n 5m "I'd feel really bad if I knew that I could've helped..."
n 5n "Just know that I won't shut you out or anything, okay?"
mc "I appreciate it..."
n 5y "Good, I wouldn't want you to think that I'm scary or something!"
mc "You couldn't scare me off even if you tried."
n 3l "Is that a challenge?"
mc "Er..."
n 3l "Ah relax! It's not like I'd want to scare you off anyways!"
n 3t "I'm not that mean..."
mc "Yeah, you're not too bad..."
n 3x "Well you sure know how to compliment a lady!"
mc "It's worked so far..."
show natsuki 1v
"Natsuki turns red-faced as she figures out how to respond."
"I decide to cut her a break this time."
mc "So...{w=0.38}how've you been?"
n 1a "Oh, I'm doing great! I'm just heading to my next class!"
mc "Well thats good! I'm just getting back from lunch."
n 1k "How was it?"
mc "Surprisingly, it was actually alright."
mc "I found out that I had the same lunch period with Monika!"
show natsuki 1c
mc "Crazy, right?"

if hangout1 == "Natsuki":
    if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
        n 1q "Y-{w=0.38}yeah..."
        "I guess Natsuki's still a little irritated over what she saw yesterday..."
        "Then again she is the kind of person I'd expect to hold a grudge..."
        "Natsuki clears her voice to break the tension."
        n "Well, it's good that you're talking to the other people..."
        n 2l "It'd be weird if I was the only person you talked to!"
        mc "Aw come on, you don't give me enough credit, Natsuki."
        mc "I talk to other people too, you know!"
        n 5l "Like who?"
        mc "Well..."
        "I guess she has me here."
        "Other than online, there really isn't too many other people I talk to outside the club..."
        "Heck, I usually just sit by myself in the cafeteria..."
        "Still, I try to come up with a retort to Natsuki's jab."
        mc "That's not important!"
        n 5z "Well don't worry, [player], you'll always have me!"
        n 4b "And it's good to know someone who can always whip you up some mean cupcakes!"
        mc "Well that's good to know..."
        n 1w "And I did fix your taste in manga for you!"
        mc "Yeah, that's true..."



if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        n 1j "Yeah!"
        n 5y "Now I won't have to hear you complain about not having anyone to sit with!"
        mc "H-{w=0.38}hey! I wasn't complaining-"
        n 4y "Well you'd be complaining about how much you missed out on my cupcakes!"
        n 4t "I always try to bring something nice for everyone..."
        mc "That's probably true!"
        show natsuki 4a
        mc "You're the best cook I know, so if we ever had a lunch together, I'd be set."
        n 5w "Well hang on! I didn't say you could mooch off of me!"
        n 5u "Some of it is for me too..."
        mc "I know, I know..."



if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Natsuki":
        n 2k "Yeah, that must've been nice."
        n 1y "Too bad you don't have lunch with me, you'd be set for life with the stuff I bring!"
        mc "Well, there's always hope for next year I suppose."
        n 2j "Guess you're stuck with Monika for now though."
        mc "I mean it's not too bad..."
        mc "She and her friends were nice to me..."
        n 5z "Just try not to gross them out too much, [player]!"
        mc "I won't..."
        show natsuki 5a
        "I playfully roll my eyes at her."



show natsuki 1t
n "So, I take it you have to get to your next class..."
mc "Yep...{w=0.38}heading back to good ol' algebra class with Saitō!"
"I sarcastically give a thumbs up."
show natsuki 1m
n "She's that bad, huh?"
mc "I mean she's not bad, she's just boring."
mc "Not to mention, I'm pretty sure I don't want to do anything with math in the future..."
n 1t "Yeah, same here!"
n 1z "Well, I'll let you go suffer till club time!"

if poem_giver == "Natsuki":
    "Well, I've been suffering quite a bit trying to figure out how to respond to your poem..."
    "Though, I do my best to smile back."

if poem_giver == "Yuri":
    "I smile back at Natsuki."

mc "Laters!"
n 2z "Bye!"
show natsuki at thide
hide natsuki
stop music fadeout 2.0
"I wave goodbye to Natsuki as we head our separate ways."
jump day3_mono

label y_hallway_interaction2:
$ y_name = "???"
play sound "sfx/fall2.ogg"
y "EEEK!"
"While I wasn't looking, I bumped into someone, causing them to immediately drop all their textbooks."
"Everyone in the hallway suddenly turns towards me."
"I hastily turn to face who I just bumped into."
show yuri 3o at t11 zorder 1
play music e16 fadein 1.0
"It's Yuri!"
mc "Oh, no! Are you okay, Yuri?"
$ y_name = "Yuri"
y "Uuuu....{w=0.38}I'll be alright."
"I look down to see the pile of books that Yuri dropped."
"I'm able to recognize Portrait of Markov among her textbooks."
"She really doesn't leave home without it, it seems..."
mc "I'll get that for you..."
"I bend down to pick up Yuri's books."
y 3q "Sorry about that!"
y "I should really pay more attention to where I'm going..."
show yuri 2q
mc "What do you mean?"
mc "If anyone should be apologizing it should be me, I'm the one that bumped into you."
y 2s "Well, I guess we both owe an apology to each other..."
mc "Yeah...{w=0.38}I'm really sorry..."
show yuri 2c
"I'm barely able to lift up all of Yuri's textbooks and hand it to her."
mc "Jeez...{w=0.38}are those advanced level course textbooks?"
y 3d "Yep! I'm taking three this semester!"
"Poor girl..."
mc "Well, I'm impressed you can carry all that!"
y 3i "It's a side benefit when you're taking those advanced courses."
y 3d "It really builds up your arm strength!"
y 3b "Matter of fact, I'm actually on my last advanced course for the day!"
mc "Well hey, I hope it all goes well!"
y 3a "Thank you, [player]."
y 3b "So where are you heading off to next?"
mc "I'm heading back to my Algebra class, just got out of my lunch period."
y 3b "How was your lunch?"
show yuri 3a
mc "Surprisingly, it was actually alright."
mc "I found out that I had the same lunch period with Monika!"
show yuri 3e
mc "Crazy, right?"




if hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
        y 3q "T-{w=0.38}that's nice, [player]..."
        "I guess Yuri's still a little agitated over what she saw yesterday..."
        "Knowing her, she probably thinks [hangout2] and I are a couple now..."
        "Yuri clears her voice to break the tension."
        y 3a "Well, it's good to spend time around your friends, [player]."
        y 3q "I just hope you don't forget about the ones you have..."
        "Yeah, she's still hung up over yesterday..."
        "I try to reassure her."
        show yuri 3s
        mc "Oh, come on! I could never forget about you!"
        mc "You're one of my favorite people in the club!"
        y 4e "R-{w=0.38}right..."
        y "I don't know why I'd think that..."
        show yuri 4a
        "I guess I could think of a few reasons..."



if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        y 3b "That's nice, [player]!"
        y 3q "I just wish we had lunch together too..."
        mc "Ah, I'm sure we'll get a chance next year..."
        y 3d "It would certainly be nice!"
        mc "Well it'd give me a good excuse to try out more of your tea!"
        y 3a "It would indeed!"
        y 3b "I have all sorts of recipes I've been meaning to share with the club..."
        y 3q "I do think there's a select few you'd really enjoy..."
        "She actually took the time to try to figure out what kind of tea I would like?"
        "She never fails at trying to be sweet!"
        show yuri 3c
        mc "I'd like that a lot, Yuri."


if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Monika":
    if hangout2 == "Yuri":
        y 3b "Well it's good to have company for lunch."
        y 3w "I wish I could've joined you guys..."
        mc "Yeah...{w=0.38}me too..."
        mc "Maybe next year we'll have the same lunch period."
        y 3j "I'll certainly be hoping for it!"
        y 3d "In the meantime, my books to keep me company!"
        y 3m "Besides, I'm always able to get a good amount of work done during lunch period."
        mc "Sounds like I could learn a thing or two from you.."
        mc "I usually just use that time to do things last minute..."
        show yuri 3f
        y "It's never a good idea to do things at the last minute, [player]."
        y 3k "It often leads to one's work being less than ideal..."
        mc "Looks like those advanced classes have taught you a lot!"
        y 3j "Yeah...{w=0.38}they have..."




show yuri 3f
y "So...{w=0.38}I take it you're heading back to class now?"
mc "Yeah...{w=0.38}unfortunately..."
y 3e "Who's class are you in?"
mc "Saitō's'..."
y 3h "Yeah...{w=0.38}her class is a little..."
y 3q "Well..."
mc "Boring?"
y 3a "Yes, it's quite dull."
y 3b "But, you learn to power through it."
show yuri 3a
mc "I'm still figuring out how to do that."
show yuri 3d
y "I'm sure you'll figure it out soon, [player]!"
mc "Thanks, Yuri."
show yuri 3f
y "Well, I have to get to my class now."
y 3k "I'd hate to be late..."
mc "Yeah, same here..."
y 3b "I'll see you in the club, [player]!"


if poem_giver == "Natsuki":
    pass

if poem_giver == "Yuri":
    "Well, there goes my anxiety about going to the club today."
    "Though, I do my best to smile back."


mc "Bye, Yuri!"
y 2c "Good-bye!"
show yuri at thide
hide yuri
stop music fadeout 2.0
"I wave goodbye to Yuri as we head our separate ways."
jump day3_mono




label day3_mono:
scene bg class_day
with wipeleft_scene
play music t3 fadein 2.0
"The rest of the day seems to grind to a crawl as I begin the second half of the day."
"Though, I guess that just leaves me more time to think about everything."

if m_walk == True:
    jump day3_mono1

if m_walk == False:
    jump day3_mono2



label day3_mono1:

"Especially considering how Monika was with me earlier..."
"Was she...{w=0.38}flirting with me?"
"She was incredibly helpful to me today, that's for sure..."

if encore_sayoriquestion_1 == True:
    "Though she seemed to keep to herself when Sayori was around."

if encore_sayoriquestion_1 == False:
    "And she did help make things less awkward between me and [day3_hallway]."

"I don't know...{w=0.38}I know Monika wants to help me..."
"But is that all she wants though?"
"I mean, I don't see much of a reason she'd be interested in me..."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        "And I've only just gotten to know her a little more recently..."
        "Is she really all that interested in me?"

if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        "Other then today, I've only spent time around Monika on Monday..."
        "Though she did seem pretty excited around me for some reason..."

        if encore_sayoriquestion_1 == True:
            "But it wasn't right either..."

        if encore_sayoriquestion_1 == False:
            "Almost as if it was meant to happen..."

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Monika":
        "Other than today, I've only spent time around Monika yesterday..."
        "When we got unexpectedly close to each other..."
        "And it did feel nice to be with her..."

        if encore_sayoriquestion_1 == True:
            "But it wasn't right either..."

        if encore_sayoriquestion_1 == False:
            "Almost as if it was meant to happen..."

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        "I really haven't spent much time around Monika at all..."
        "It's not like we know each other super well or anything..."

        if encore_sayoriquestion_1 == True:
            "But it'd be wrong for me to go for her while I'm with Sayori..."

        if encore_sayoriquestion_1 == False:
            "I never really got much of a chance to..."
            "But now that we're in the same club, and she's showing at least basic interest in me, maybe that can change..."


"Well, I guess this all just ties into the questions Monika said I should ask myself..."
"But right now, I can't really decide on who I'd be the happiest with..."
"Ah! This is hardly the time and place for this..."
"I can think about this later, I should just try to focus on paying attention to this stupid algebra..."
scene black
with close_eyes
jump day3_club


label day3_mono2:

"It was nice running into [day3_hallway] earlier."

if day3_hallway == "Sayori":
    "It's not like I see Sayori around too much in school aside from the club..."

    if day3_hallway == "Sayori" and poem_giver == "Natsuki":
        "But given how long I've known her, maybe she could help me figure out what to say to Natsuki..."

        if encore_sayoriquestion_1 == True:
            "I mean she's my girlfriend! I have to tell her about this!"
            "Even if she's going to freak out initially..."

        if encore_sayoriquestion_1 == False:
            "Even if she's going to freak out initially..."

    if day3_hallway == "Sayori" and poem_giver == "Yuri":
        "But given how long I've known her, maybe she could help me figure out what to say to Yuri..."

        if encore_sayoriquestion_1 == True:
            "I mean she's my girlfriend! I have to tell her about this!"
            "Even if she's going to freak out initially..."

        if encore_sayoriquestion_1 == False:
            "Even if she's going to freak out initially..."


if day3_hallway == "Natsuki" or day3_hallway == "Yuri":
    "I don't really see her outside of the club..."
    "It was nice catching up a little..."

    if day3_hallway == "Natsuki" and poem_giver == "Natsuki":
        "And it didn't look like she expected me to have read their poem, which bodes well for me time wise..."

    if day3_hallway == "Yuri" and poem_giver == "Yuri":
        "And it didn't look like she expected me to have read their poem, which bodes well for me time wise..."

    if day3_hallway == "Yuri" and poem_giver == "Natsuki":
        "I'm just hoping when I walk in later, Yuri doesn't suddenly confess to me or something..."
        "That'd make this day even more stressful..."

    if day3_hallway == "Natsuki" and poem_giver == "Yuri":
        "I really appreciated Natsuki's offer earlier, though I don't know if she'd really want to help with something like this..."
        "Given her opinion on Yuri..."
        "Well, it'd suck if she'd give me a poem confession too..."
        "If that happens, I don't know what I'd do..."


"I guess all I can do now is just reflect on what Monika told me to ask myself..."
"And look like I'm paying attention..."
scene black
with close_eyes
jump day3_club



label day3_club:
scene bg class_day
with open_eyes
play sound school
"After long last, the bell rings, signifying that the school day is officially over."
"Though I suppose that means I'm going to brace for the worst with [poem_giver]..."
"I think I have a general idea of what I'd want to say if it comes down to it..."
"Well, hopefully things will just go smoothly for today..."
"I finish packing my things and head out into the hallway to meet Sayori."
scene bg corridor
with wipeleft_scene
"Sure enough, I spotted Sayori waiting just outside the classroom."
show sayori 1a at t11 zorder 1
s "Hey, [player]!"
mc "Hey, Sayori!"
s 2q "Ready for another day of fun and literature?!?"

if encore_sayoriquestion_1 == True:
    mc "With you? Always."
    show sayori 2y
    s "Well in that case we better get going..."
    mc "Yep..."
    s 2x "Well let's go, [player]! What are we waiting for?!?"
    "With slight hesitance, I begin the walk with Sayori to the literature club."
    show sayori at thide
    hide sayori

if encore_sayoriquestion_1 == False:
    "I try to put on the most enthusiastic smile I possibly can."
    mc "Yep! Let's go!"
    s 2r "That's the spirit!"
    s 2y "I still remember the first time you came with me to the Literature Club..."
    s 1y "You almost didn't want to go..."
    mc "Well, I owe that to you, Sayori..."
    s 1d "You don't owe me anything, [player]..."
    s 1y "Just seeing you happy is it's own reward..."
    "I can't help but genuinely smile at that."
    mc "Well, let's get going!"
    show sayori 2q
    "With slight hesitance, I begin the walk with Sayori to the literature club."
    show sayori at thide
    hide sayori

scene bg corridor
with wipeleft_scene
"As we're traveling our usual route, I still can't help but feel the anxiety well up within me with every step I take."
"Though I just take a deep breath and tell myself everything will be fine."
show sayori 1q at t11 zorder 1
"Thankfully Sayori seems to be blissfully unaware of my apparent apprehension, but it's probably for the best."
stop music fadeout 3.0
"Eventually we stop right outside the club."
s 1a "Well, here we are!"
mc "Yep, can't wait to see what's in store for today!"
"Sayori opens the door and steps into the club with me right behind her."
"Let's just get this over with..."
show sayori at thide
hide sayori
scene bg club_day
with wipeleft_scene
"Sure enough, the club's the same as it's always been, with everyone in their normal spots doing their normal routines."
"Monika quickly spots us coming in."
show monika 1b at t21 zorder 1
show sayori 1a at t22 zorder 2
m "Hey guys!"
show monika 1a
s "Hey, Monika!"
m 1e "How're you two?"
s 1x "I'm doing pretty well! Looking forward to another great day with you guys!"
m 2m "Awww, Sayori..."
mc "She's always a charmer."
s 2q "Teehee~"
m 3a "I take it you already have her poems, [player]?"
show sayori 1a

if poem_giver == "Natsuki":
    mc "Yeah, I got her's yesterday, just need your poems and Yuri's."

if poem_giver == "Yuri":
    mc "Yeah, I got her's yesterday, just need your poems and Natsuki's."

m 2e "Fortunately, I remembered to bring them, I'll give them to you by the time club's over."
mc "Alright."
m 1b "Well you guys can go sit down, we're gonna get started in a few minutes."
s 1r "Sounds good to me!"
show sayori at thide
hide sayori
show monika 1a at t11 zorder 1
"Monika leans in to whisper something to me as Sayori goes to sit down."
m 1e "So how're you holding up?"
mc "Still thinking over a lot of stuff..."
mc "Though in case [poem_giver] asks about her confession letter, I have an idea of what I want to say."
m 2e "Well that's good."
m 2d "Still, this is a pretty sensitive topic for you two, so just be careful with what you say."
mc "I'll try my best."
m 2j "Great!"
m 2b "Well, I'll be here if you want to talk more, [player]!"
mc "Right now, I think I could use something to calm me down a bit..."
mc "It's been a fairly stressful day for me thinking about all this..."
m 2m "Whenever I'm feeling stressed out, I find that music usually helps calm the nerves..."
m 2e "I've been working on something if you want to give it a listen..."
mc "I'll think about it, thank you Monika!"
m 2k "Anytime!"
show monika at thide
hide monika
"Monika goes back to the teacher's desk, leaving me standing in the middle of the room once again."
"Looking around the room, I try to figure out who I can talk to without completely melting down or making some sort of scene..."
"So, of course that leaves [poem_giver] out of the question..."
"I guess that only leaves three people I could try talking too..."



#Normal choice, No Natsuki

if poem_giver == "Natsuki":
    if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Natsuki":
            jump day3_choice1


#Normal choice, No Yuri


if poem_giver == "Yuri":
    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day3_choice2


#Monika interfers, No Natsuki

if poem_giver == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Natsuki":
            jump day3_choice3

if poem_giver == "Natsuki":
    if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Natsuki":
        if hangout2 == "Monika":
            jump day3_choice3

#Monika interfers, No Yuri

if poem_giver == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            jump day3_choice4

if poem_giver == "Yuri":
    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Monika":
            jump day3_choice4

#Just Monika, No Natsuki

if poem_giver == "Natsuki":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            jump day3_choice5


#Just Monika, No Yuri

if poem_giver == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            jump day3_choice6




label day3_choice1:
        stop music fadeout 2.0
        menu:
            "Who should I hang out with?"
            "Monika":
                $ m_modappeal +=1
                jump mencore_3
            "Sayori":
                $ s_modappeal +=1
                jump sencore_3
            "Yuri":
                $ y_modappeal +=1
                jump yencore_3



label day3_choice2:
        stop music fadeout 2.0
        menu:
            "Who should I hang out with?"
            "Monika":
                $ m_modappeal +=1
                jump mencore_3
            "Natsuki":
                $ n_modappeal +=1
                jump nencore_3
            "Sayori":
                $ s_modappeal +=1
                jump sencore_3




#Rigged Choice, No Natsuki
label day3_choice3:

python:
    #"Who should I hang out with?"
#        renpy.say(narrator, ""Who should I hang out with?", interact=False)
#        madechoice = renpy.display_menu[("Monika.", "true"), ("Sayori.", "false"),("Yuri.", "false")]), screen="encore_rigged_choice")
    madechoice = show_rigged_choice(narrator, "Who should I hang out with?", [("Monika.", "Monika"), ("Sayori.", "Sayori"),("Yuri.", "Yuri")],197)

#If you pick Monika
if madechoice == "Monika":
    window hide(None)
    scene bg club_day
    jump mencore_3

#If you pick Sayori
if madechoice == "Sayori":
    window hide(None)
    scene bg club_day
    jump sencore_3

#If you pick Yuri
if madechoice == "Yuri":
    window hide(None)
    scene bg club_day
    jump yencore_3



#Rigged Choice, No Yuri
label day3_choice4:

python:
    #"Who should I hang out with?"
#        renpy.say(narrator, ""Who should I hang out with?", interact=False)
#        madechoice = renpy.display_menu[("Monika.", "true"), ("Natsuki.", "false"),("Yuri.", "false")]), screen="encore_rigged_choice")
    madechoice = show_rigged_choice(narrator, "Who should I hang out with?", [("Monika.", "Monika"), ("Natsuki.", "Natsuki"),("Sayori.", "Sayori")],197)


#If you pick Monika
if madechoice == "Monika":
    window hide(None)
    scene bg club_day
    jump mencore_3


#If you pick Natsuki
if madechoice == "Natsuki":
    window hide(None)
    scene bg club_day
    jump nencore_3

#If you pick Sayori
if madechoice == "Sayori":
    window hide(None)
    scene bg club_day
    jump sencore_3




label day3_choice5:
        stop music fadeout 2.0
        menu:
            "Who should I hang out with?"
            "Monika":
                $ m_modappeal +=1
                jump mencore_3
            "Sayori":
                $ s_modappeal +=1
                jump sencore_v1
            "Yuri":
                $ y_modappeal +=1
                jump yencore_v1


label yencore_v2:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3



label day3_choice6:
        stop music fadeout 2.0
menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Natsuki":
        $ n_modappeal +=1
        jump nencore_v1
    "Sayori":
        $ s_modappeal +=1
        jump sencore_v3





#Monika Interferences (Non Rigged)
#Yuri's (Natsuki Poem Giver)

label sencore_v1:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Yuri":
        $ m_modappeal +=1
        jump yencore_v2

label sencore_v2:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3



label yencore_v1:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Sayori":
        $ m_modappeal +=1
        jump sencore_v2
    "Monika":
        $ m_modappeal +=1
        jump mencore_3


#Monika Interferences (Non Rigged)
#Natsuki's (Yuri Poem Giver)

label sencore_v3:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Natsuki":
        $ n_modappeal +=1
        jump nencore_v2
    "Monika":
        $ s_modappeal +=1
        jump mencore_3

label sencore_v4:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3



label nencore_v1:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Sayori":
        $ m_modappeal +=1
        jump sencore_v4

label nencore_v2:

window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear

menu:
    "Who should I hang out with?"
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3
    "Monika":
        $ m_modappeal +=1
        jump mencore_3



label day3_mreturn:

scene bg corridor
with wipeleft_scene
"It was a mostly silent walk back to the Literature Club."
show monika 1j at t11 zorder 1
"I'm still processing just how amazing Monika's piano skills are!"
show monika 1m
"And still trying to get over the little moment we shared before Sayori called."

if encore_sayoriquestion_1 == False:

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            show monika 1e
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking regularly, the more time I spend around her..."
            "The more comfortable I become in her presence..."
            show monika 2m
            "It'd be a crazy turn of events if I ended up getting with Monika..."
            "But I know that if I do get with her, I'd be breaking [poem_giver]'s heart..."
            "And well...{w=0.38}Sayori likely wouldn't react well at first either..."
            show monika 2d
            "Am I even sure it'd be right to get with Monika?"
            "I mean, she isn't my only option..."
            "But, I might dare say she's my favorite right now..."



    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking, I am starting to feel a lot more comfortable around her..."
            "And I know I have feelings for Monika...{w=0.38}I always have..."
            "I just never thought I had a realistic chance...{w=0.38}hell, even a chance to be with her..."
            show monika 2m
            "But yet, part of me is a still a little uncertain if she's the only one I want..."

            if hangout2 == "Sayori":
                "I mean, I know Sayori is in love with me..."
                "And I do care about her..."
                "But I don't know how'd she react if I completely reversed course on her..."


            if hangout2 == "Natsuki":

                if poem_giver == "Natsuki":
                    "I mean, I know Natsuki is in love with me..."
                    "I have her poem to prove it..."
                    "And spending yesterday with her was pretty fun..."

                    if encore_festivalquestion_2 == "Natsuki":
                        "Of course I couldn't forget about last Sunday either..."

                    if encore_festivalquestion_2 == "Yuri":
                        "But I also kind of miss spending time with Yuri..."


                if poem_giver == "Yuri":
                    "I mean, I know Yuri is in love with me..."
                    "I have her poem to prove it..."

                    if encore_festivalquestion_2 == "Natsuki":
                        "But re-connecting a little with Natsuki yesterday was pretty fun..."

                    if encore_festivalquestion_2 == "Yuri":
                        "And I enjoyed spending time around her on Sunday..."
                        "But it was also fun spending some time with Natsuki yesterday too..."


            if hangout2 == "Yuri":

                if poem_giver == "Natsuki":
                    "I mean, I know Natsuki is in love with me..."
                    "I have her poem to prove it..."


                if encore_festivalquestion_2 == "Natsuki":
                    "And I enjoyed spending time around her on Sunday..."
                    "But it was also fun spending some time with Yuri yesterday too..."

                if encore_festivalquestion_2 == "Yuri":
                    "But re-connecting a little with Yuri yesterday was pretty fun..."



            if poem_giver == "Yuri":
                "I mean, I know Yuri is in love with me..."
                "I have her poem to prove it..."
                "And spending yesterday with her was pretty fun..."

                if encore_festivalquestion_2 == "Natsuki":
                    "But I also kind of miss spending time with Natsuki..."

                if encore_festivalquestion_2 == "Yuri":
                    "Of course I couldn't forget about last Sunday either..."





    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Monika":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking, I am starting to feel a lot more comfortable around her..."
            "And I know I have feelings for Monika...{w=0.38}I always have..."
            "I just never thought I had a realistic chance...{w=0.38}hell, even a chance to be with her..."
            show monika 2m
            "But yet, part of me is a still a little uncertain if she's the only one I want..."

            if hangout1 == "Sayori":
                "I mean, I know Sayori is in love with me..."
                "And I do care about her..."
                "But I don't know how'd she react if I completely reversed course on her..."


            if hangout1 == "Natsuki":

                if poem_giver == "Natsuki":
                    "I mean, I know Natsuki is in love with me..."
                    "I have her poem to prove it..."
                    "And spending yesterday with her was pretty fun..."

                    if encore_festivalquestion_2 == "Natsuki":
                        "Of course I couldn't forget about last Sunday either..."

                    if encore_festivalquestion_2 == "Yuri":
                        "But I also kind of miss spending time with Yuri..."


                if poem_giver == "Yuri":
                    "I mean, I know Yuri is in love with me..."
                    "I have her poem to prove it..."

                    if encore_festivalquestion_2 == "Natsuki":
                        "But re-connecting a little with Natsuki yesterday was pretty fun..."

                    if encore_festivalquestion_2 == "Yuri":
                        "And I enjoyed spending time around her on Sunday..."
                        "But it was also fun spending some time with Natsuki yesterday too..."


            if hangout1 == "Yuri":

                if poem_giver == "Natsuki":
                    "I mean, I know Natsuki is in love with me..."
                    "I have her poem to prove it..."


                if encore_festivalquestion_2 == "Natsuki":
                    "And I enjoyed spending time around her on Sunday..."
                    "But it was also fun spending some time with Yuri yesterday too..."

                if encore_festivalquestion_2 == "Yuri":
                    "But re-connecting a little with Yuri yesterday was pretty fun..."



            if poem_giver == "Yuri":
                "I mean, I know Yuri is in love with me..."
                "I have her poem to prove it..."
                "And spending yesterday with her was pretty fun..."

                if encore_festivalquestion_2 == "Natsuki":
                    "But I also kind of miss spending time with Natsuki..."

                if encore_festivalquestion_2 == "Yuri":
                    "Of course I couldn't forget about last Sunday either..."




    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though I finally started spending time around her today, I already feel a lot more comfortable around her..."
            "And I know I have feelings for Monika...{w=0.38}I always have..."
            "I just never thought I had a realistic chance...{w=0.38}hell, even a chance to be with her..."
            show monika 2m
            "But yet, part of me is a still a little uncertain about all this.."
            "I could just be reading too much into Monika's actions..."

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    "I mean, I know Sayori is in love with me..."
                    "And I do care about her..."
                    "Us spending more time together might be giving me second thoughts..."
                    "But I don't know how'd she react if I completely reversed course on her..."


                if hangout1 == "Natsuki":
                    if hangout2 == "Natsuki":
                        "I mean, I've spent all my time lately around Natsuki..."
                        "I'm starting to feel a lot more connected with her..."

                        if poem_giver == "Natsuki":
                            "And I know she likes me thanks to her poem..."

                        if poem_giver == "Yuri":
                            "And I know Yuri likes me thanks to her poem..."


                if hangout1 == "Yuri":
                    if hangout2 == "Yuri":
                        "I mean, I've spent all my time lately around Yuri..."
                        "I'm starting to feel a lot more connected with her..."

                        if poem_giver == "Natsuki":
                            "And I know Natsuki likes me thanks to her poem..."

                        if poem_giver == "Yuri":
                            "And I know she likes me thanks to her poem..."


                else:

                    "And currently I feel like I'm being pulled between [hangout1] and [hangout2]..."
                    "[poem_giver]'s letter isn't really helping me decide on this..."
                    "I know Monika just wants to help me..."
                    "But...{w=0.38}could something else come out of all this?"







if encore_sayoriquestion_1 == True:

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            show monika 1e
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking regularly, the more time I spend around her..."
            "The more comfortable I become in her presence..."
            show monika 2m
            "But I know it wouldn't be right to leave Sayori..."
            show monika 2d
            "As tempting as it would be to go for Monika..."
            "Could I seriously bring myself to end my relationship with Sayori?"


    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking regularly, the more time I spend around her..."
            "The more comfortable I become in her presence..."
            show monika 2m
            "But I know it wouldn't be right to leave Sayori..."

            if hangout2 == "Sayori":
                "I still enjoy hanging out with her, and I know I still love her..."


            if hangout2 == "Natsuki":
                "And I did have fun being in Natsuki's arms yesterday, even though I didn't ask for it..."
                "But I know Sayori still needs me..."

            if hangout2 == "Yuri":
                "And I did have fun being close to Yuri yesterday, even though I didn't ask for it..."
                "But I know Sayori still needs me..."



            show monika 2d
            "As tempting as it would be to go for Monika..."
            "Could I seriously bring myself to end my relationship with Sayori?"




    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Monika":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking regularly, the more time I spend around her..."
            "The more comfortable I become in her presence..."
            show monika 2m
            "But I know it wouldn't be right to leave Sayori..."

            if hangout1 == "Sayori":
                "I still enjoy hanging out with her, and I know I still love her..."


            if hangout1 == "Natsuki" or hangout1 == "Yuri":
                "Even though we haven't spent much time in the club lately..."
                "We still hangout after school..."


            "But I still can't shake the feeling I've had since yesterday..."
            "Being so close to Monika, like earlier...{w=0.38}just felt so natural..."
            show monika 2d
            "As tempting as it would be to go for Monika..."
            "Could I seriously bring myself to end my relationship with Sayori?"



    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I'm starting to think that maybe what I always thought to be impossible, might actually be possible..."
            "Monika...{w=0.38}might actually like me back!"
            show monika 2j
            "Even though we just started talking regularly, the more time I spend around her..."
            "The more comfortable I become in her presence..."
            show monika 2m
            "But I know it wouldn't be right to leave Sayori..."

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    "I love her..."
                    "I know I do..."

            if hangout1 == "Sayori":
                if hangout2 == "Natsuki" or hangout2 == "Yuri":
                    "I love her..."
                    "I know I do..."
                    "Even if she might be a little mad at me over yesterday..."

            if hangout1 == "Natsuki" or hangout1 == "Yuri":
                if hangout2 == "Sayori":
                    "I love her..."
                    "I still care about her..."


            if hangout1 == "Natsuki" or hangout1 == "Yuri":
                if hangout2 == "Natsuki" or hangout2 == "Yuri":
                    "I love her..."
                    "I know I do..."
                    "Even if we haven't spent as much time as we wanted together..."




m 2n "[player]?"
mc "Y-{w=0.38}yeah?"
m 3l "You just kind of passed the club, silly..."
"I look back to see that I somehow managed to walk past the doors to the clubroom..."
mc "Oh! I knew that..."
show monika 2m
"I hastily walk back to Monika by the entrance."
m 2g "Everything okay, [player]?"
m 2f "You look a little overwhelmed..."
mc "Yeah, yeah, I'm fine..."
m 3n "I guess my little performance really blew you away, huh?"
show monika 3m
mc "Yeah! It really did..."
show monika 2e
"Monika smiles warmly."
m 2b "Well if you liked my song, you'll love what I have in store for everyone today!"
show monika 2a
mc "Is that so?"
m 1j "Yep!"
m 1b "There's plenty of more fun and literature that await you today, [player]!"
"Monika cheerfully opens the door as we walk back into the clubroom."
scene bg club_day
with wipeleft_scene
play music t3 fadein 1.0
show monika 4k at t11 zorder 1
m "Okay everyone! We're back!"
show monika 1k at t41 zorder 1
show sayori 1i at t42 zorder 2
show natsuki 4n at t43 zorder 3
show yuri 3h at t44 zorder 4
"Everyone turns their attention to me and Monika."
s 1k "Hey guys..."
show sayori 1g
show monika 1d
n 4h "Where were you two?"
n 5w "We thought you ditched us!"
show natsuki 5x
m 3l "What? Don't be silly!"
m 1a "I was just showing [player] the song I was working on!"
y 1b "Oh, that's right! I almost forgot you played the piano!"
y 1a "How's the song coming along?"
m 1b "I'd say it's going pretty well..."
m 5a "[player] liked it..."
show sayori 1b
show natsuki 5i
"Everyone looks at me as I feel my face turn red from remembering earlier..."
show monika 1j
mc "Y-{w=0.38}yeah! It was great, Monika!"
mc "I can't wait to hear it again when it's all done!"
n 5w "Well if you guys were gone for that long, then it must be a masterpiece!"
show natsuki 5x
m 2e "Oh, it is, Natsuki."
m 1b "I have no doubt everyone here will enjoy it when it's done!"
m 1m "Anyways, we should probably get started with the activity I have in mind for us today..."
y 1b "That would be great, Monika!"
show monika at thide
hide monika
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
show yuri at thide
hide yuri
"Everyone takes a seat at the front of the room by Monika."

if hangout2 == "Sayori":
    show sayori 1g at t11 zorder 1
    "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
    show sayori 1k
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Sayori isn't assuming something, is she?"
    "I sigh to myself as I turn my focus to Monika."
    show sayori at thide
    hide sayori
    scene bg club_day
    with wipeleft_scene
    jump day3_clubactivity

if hangout2 == "Natsuki":
    show natsuki 1n at t11 zorder 1
    "While grabbing a seat, I notice Natsuki shooting me a disappointed glance."
    show natsuki 1s
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Natsuki isn't assuming something, is she?"
    "I sigh to myself as I turn my focus to Monika."
    show natsuki at thide
    hide natsuki
    scene bg club_day
    with wipeleft_scene
    jump day3_clubactivity


if hangout2 == "Yuri":
    show yuri 1r at t11 zorder 1
    "While grabbing a seat, I notice Yuri shooting me an agitated glance."
    show yuri 1w
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Yuri isn't assuming something, is she?"
    "I sigh to myself as I turn my focus to Monika."
    show yuri at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    jump day3_clubactivity

if hangout2 == "Monika":

    if hangout1 == "Sayori":
        show sayori 1g at t11 zorder 1
        "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
        show sayori 1k
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Sayori isn't assuming something, is she?"
        "I sigh to myself as I turn my focus to Monika."
        show sayori at thide
        hide sayori
        scene bg club_day
        with wipeleft_scene
        jump day3_clubactivity

    if hangout1 == "Natsuki":
        show natsuki 1n at t11 zorder 1
        "While grabbing a seat, I notice Natsuki shooting me a disappointed glance."
        show natsuki 1s
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Natsuki isn't assuming something, is she?"
        "I sigh to myself as I turn my focus to Monika."
        show natsuki at thide
        hide natsuki
        scene bg club_day
        with wipeleft_scene
        jump day3_clubactivity


    if hangout1 == "Yuri":
        show yuri 1r at t11 zorder 1
        "While grabbing a seat, I notice Yuri shooting me an agitated glance."
        show yuri 1w
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Yuri isn't assuming something, is she?"
        "I sigh to myself as I turn my focus to Monika."
        show yuri at thide
        hide yuri
        scene bg club_day
        with wipeleft_scene
        jump day3_clubactivity

    if hangout1 == "Monika":

        if encore_sayoriquestion_1 == True:
            show sayori 1g at t11 zorder 1
            "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
            show sayori 1k
            "I turn to ask what's wrong but she quickly looks away before I get the chance to."
            "Sayori isn't assuming something, is she?"
            "I sigh to myself as I turn my focus to Monika."
            show sayori at thide
            hide sayori
            scene bg club_day
            with wipeleft_scene
            jump day3_clubactivity

        if encore_sayoriquestion_1 == False:

            if encore_festivalquestion_2 == "Natsuki":
                show natsuki 1n at t11 zorder 1
                "While grabbing a seat, I notice Natsuki shooting me a disappointed glance."
                show natsuki 1s
                "I turn to ask what's wrong but she quickly looks away before I get the chance to."
                "Natsuki isn't assuming something, is she?"
                "I sigh to myself as I turn my focus to Monika."
                show natsuki at thide
                hide natsuki
                scene bg club_day
                with wipeleft_scene
                jump day3_clubactivity


            if encore_festivalquestion_2 == "Yuri":
                show yuri 1r at t11 zorder 1
                "While grabbing a seat, I notice Yuri shooting me an agitated glance."
                show yuri 1w
                "I turn to ask what's wrong but she quickly looks away before I get the chance to."
                "Yuri isn't assuming something, is she?"
                "I sigh to myself as I turn my focus to Monika."
                show yuri at thide
                hide yuri
                scene bg club_day
                with wipeleft_scene
                jump day3_clubactivity








label day3_nreturn1:

scene bg corridor
with wipeleft_scene
show natsuki 1j at t11 zorder 1
"During the walk back, Natsuki was in an unusually cheerful mood, smiling brightly as she took glances between me and her manga."
show natsuki 1z
"Granted, I've seen Natsuki in a good mood plenty of times, this was different side she was showing me..."
show natsuki 1d
"It's almost as if she just found out she won the lottery or just found out that her cupcakes won first place in some contest."
show natsuki 1t
"Still, I feel happy that we were able to find her manga. Given what she told me about her home situation, I probably helped her in more ways than one."


if encore_sayoriquestion_1 == True:

#Note: Player can't get these interactions if they select Natsuki before the festival, the True interactions are in the context of spending the weekend with Yuri

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            show natsuki 1a
            "In fact, just probably by talking to her her, I've helped her out so much..."
            "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
            show natsuki 4i
            "Initially, I found that kind off-putting..."
            show natsuki 4z
            "But, just by talking to her, taking the time to get to know the real her...{w=0.38}there's so much more to her!"
            "And it's crazy how much we have in common with each other!"
            show natsuki 1s
            "And I could tell she was jealous when she saw me with Yuri yesterday..."
            show natsuki 1c
            "I don't know, as tempting as it may seem to go for Natsuki..."
            "I don't feel like I should break my relationship with Sayori..."
            "I still care about her..."
            jump n_day3ch



    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            "In fact, just probably by talking to her, I've helped her out so much..."
            "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
            show natsuki 4i
            "Initially, I found that kind off-putting..."
            show natsuki 4z
            "But, just by talking to her, taking the time to get to know the real her...{w=0.38}there's so much more to her!"
            "And it's crazy how much we have in common with each other!"
            "I wish I started talking to her sooner!"
            show natsuki 1c
            "But I still got caught flat footed when she suddenly hugged me..."
            "I know I let Sayori down when I did that..."
            "And she probably would be heartbroken if she found out that Natsuki and I hugged again..."
            jump n_day3ch



#Natsuki Festival hangout works here in certain circumstances

    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":

            if encore_festivalquestion_2 == "Natsuki":
                show natsuki_sweet as natsuki at t11 zorder 1
                "Even though we haven't really talked since Sunday, I realized today how much I missed spending time around her..."
                "Not to mention realizing that being around her probably makes her situation just that much more bearable..."
                "And for a time, I was really interested in her..."
                show natsuki 1n
                "Until Sayori confessed..."


                if hangout1 == "Yuri":
                    if hangout2 == "Yuri":
                        "And getting to know Yuri lately has been pretty fun too..."


                else:
                    show natsuki 1c
                    "Considering lately I feel like I'm being pulled between [hangout1] and [hangout2]..."
                    "And Yuri's letter just makes things more complicated..."




            if encore_festivalquestion_2 == "Yuri":
                show natsuki_sweet as natsuki at t11 zorder 1
                "Even though we haven't really talked since I joined the club, I realized today how different of a person she is then I originally first thought..."
                "She isn't a completely nasty or hot-headed person..."
                "And if I spend more time around her, maybe something can blossom between us..."
                show natsuki 1n
                "But it's a little too early to say for certain, given the current circumstances..."

                if hangout1 == "Sayori":
                    if hangout2 == "Sayori":
                        "Spending all this time around Sayori lately might be making me have second thoughts about everything..."



                if hangout1 == "Yuri":
                    if hangout2 == "Yuri":
                        "I've really enjoyed spending a lot of time around Yuri..."
                        "I think I've really connected with her..."



                else:
                    show natsuki 1c
                    "Considering I feel like I'm being pulled between [hangout1] and [hangout2]..."
                    "And Yuri's letter just makes things more complicated..."


            show natsuki 1c
            "I don't know...{w=0.38}there's so much on my mind right now..."
            "But, I know I still care about Sayori..."
            jump n_day3ch




if encore_sayoriquestion_1 == False:

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":

            if encore_festivalquestion_2 == "Natsuki":
                show natsuki 1a
                "In fact, just probably by befriending her, I've helped her out so much..."
                "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
                show natsuki 5t
                "But, I've come to see lately she isn't all that..."
                "She really is a sweet, kind and caring person..."
                "And recently, I feel like she finally sees me the same way..."
                show natsuki 1c
                "I just hope she feels the same way as I do about her..."
                jump n_day3ch

            if encore_festivalquestion_2 == "Yuri":
                "In fact, just probably by talking to her, maybe I've made her situation that much more bearable..."
                "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
                show natsuki 4i
                "Initially, I found that kind off-putting..."
                show natsuki 4z
                "But, just by talking to her, taking the time to get to know the real her...{w=0.38}there's so much more to her!"
                "And it's crazy how much we have in common with each other!"
                show natstuki 1c
                "It might be too early to say this for certain, but..."
                "Maybe we can be more than just friends..."
                jump n_day3ch



    if hangout1 == "Natsuki":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":

            if encore_festivalquestion_2 == "Natsuki":
                show natsuki 1a
                "In fact, just probably by befriending her, I've helped her out so much..."
                "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
                show natsuki 5t
                "But, I've come to see lately she isn't all that..."
                "She really is a sweet, kind and caring person..."

                if hangout2 == "Sayori" or hangout2 == "Yuri":
                    show natsuki 1s
                    "And she must have some interest in me if she was that upset over seeing me with [hangout2] yesterday..."

                if hangout2 == "Monika":
                    show natsuki 1s
                    $ style.say_dialogue = style.edited
                    "{cps=16}Though she probably knows she can't compete with Monika!{nw}"
                    $ style.say_dialogue = style.normal


            if encore_festivalquestion_2 == "Yuri":
                show natsuki 1a
                "In fact, just probably by befriending her, I've helped her out so much..."
                "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
                show natsuki 4i
                "Initially, I found that kind off-putting..."
                show natsuki 4z
                "But, just by talking to her, taking the time to get to know the real her...{w=0.38}there's so much more to her!"
                "And it's crazy how much we have in common with each other!"

                if hangout2 == "Sayori" or hangout2 == "Yuri":
                    show natsuki 1s
                    "And she must have some interest in me if she was that upset over seeing me with [hangout2] yesterday..."

                if hangout2 == "Monika":
                    show natsuki 1s
                    $ style.say_dialogue = style.edited
                    "{cps=16}She knows she can't compete with Monika!{nw}"
                    $ style.say_dialogue = style.normal


            show natsuki 1c
            "I don't know, Monika's given me a lot to think about..."
            "And Natsuki probably couldn't help me make the decision..."
            jump n_day3ch





    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Natsuki":


            if encore_festivalquestion_2 == "Natsuki":
                show natsuki 1a
                "In fact, just probably by befriending her, I've helped her out so much..."
                "I have no idea what her life was like before I met her, or if she's always had this tough exterior..."
                show natsuki 5t
                "But, I've come to see lately she isn't all that..."
                "She really is a sweet, kind and caring person..."


                if hangout1 == "Sayori" or hangout1 == "Yuri":
                    show natsuki 1s
                    "And I could tell she missed spending time with me on Monday when I was with [hangout1]"


                if hangout1 == "Monika":
                    show natsuki 1s
                    $ style.say_dialogue = style.edited
                    "{cps=16}Who wants me to be with Monika!{nw}"
                    $ style.say_dialogue = style.normal



            show natsuki 1c
            "But being in her arms yesterday and today...{w=0.38}gives me a lot to think about..."
            "I feel like no matter what I do, I'm gonna end up letting someone down..."
            "Partly thanks to Yuri's letter..."
            jump n_day3ch




    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Yuri":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Yuri":

            if encore_festivalquestion_2 == "Natsuki":
                show natsuki_sweet as natsuki at t11 zorder 1
                "Even though we haven't really talked since Sunday, I realized today how much I missed spending time around her..."
                "Not to mention realizing that being around her probably makes her situation just that much more bearable..."
                "And for a time, I was really interested in her..."
                show natsuki 1n
                "But lately, I don't know if I should go for her anymore..."

                if hangout1 == "Sayori":
                    if hangout2 == "Sayori":
                        "Spending all this time around Sayori lately might be making me have second thoughts about everything..."


                if hangout1 == "Yuri":
                    if hangout2 == "Yuri":
                        "Being around Yuri lately has given me a lot to think about who I'd want be around..."


                else:
                    show natsuki 1c
                    "Considering lately I feel like I'm being pulled between [hangout1] and [hangout2]..."
                    "And Yuri's letter just makes things more complicated..."




            if encore_festivalquestion_2 == "Yuri":
                show natsuki_sweet as natsuki at t11 zorder 1
                "Even though we haven't really talked since I joined the club, I realized today how different of a person she is than I originally first thought..."
                "She isn't a completely nasty or hot-headed person..."
                "And if I spend more time around her, maybe something can blossom between us..."
                show natsuki 1n
                "But it's a little too early to say for certain, given the current circumstances..."

                if hangout1 == "Sayori":
                    if hangout2 == "Sayori":
                        "Spending all this time around Sayori lately might be making me have second thoughts about everything..."


                if hangout1 == "Yuri":
                    if hangout2 == "Yuri":
                        "I've really enjoyed spending a lot of time around Yuri..."
                        "I think I've really connected with her..."



                else:
                    show natsuki 1c
                    "Considering I feel like I'm being pulled between [hangout1] and [hangout2]..."
                    "And Yuri's letter just makes things more complicated..."


            show natsuki 1c
            "I don't know, Monika's given me a lot to think about..."
            "And Natsuki probably can't help me fix this..."
            jump n_day3ch



label n_day3ch:

show natsuki 1e at t11 zorder 1
n "[player], where are you going?"
show natsuki 1i
mc "Huh?"
n 1y "You know you just passed the club, right?"
mc "What?"
show natsuki 1z
"I look back to see Natsuki smugly standing by the doors to the clubroom."
"How did I screw that up?"
"I sigh as I walk back over to her."
"Natsuki then looks at me concerningly."
n 2h "You okay, [player]?"
n 2d "You seriously looked like you would've kept going until you hit the wall!"
show natsuki 2n
mc "Yeah, yeah, I'm fine..."
mc "I've just been thinking a lot today..."
show natsuki 5m
n "Is it about what I said earlier?"
show natsuki 5n
mc "Ah, it's a little more than that..."
show natsuki 5m
n "Well, if you wanna talk about it, I'm all ears."
n 5t "I mean, I owe you at least that much after your help today."
show natsuki 3n
mc "You don't owe me anything, Natsuki, don't worry about that."
mc "But I appreciate the offer..."
n 3y "Hey, it's what I do!"
n 3z "I think I have some good experience steering you in the right direction!"
mc "Very funny..."
"I roll my eyes as Natsuki chuckles to herself as she opens the door."
scene bg club_day
with wipeleft_scene
play music t6 fadein 2.0
show natsuki 3l at t11 zorder 1
n "Guess who found her manga!"
show natsuki 1z at t41 zorder 1
show sayori 1b at t42 zorder 2
show monika 1d at t43 zorder 3
show yuri 3e at t44 zorder 4
"Everyone in the room turns their attention to me and Natsuki as she proudly shows off her manga for everyone to see."
show natsuki 1a
m 1b "So that's why you two went out!"
show natsuki 1n
m 1n "I'll admit I was a little worried that you two might've left together..."
show monika 1m
mc "Aw come on, we couldn't ditch you guys!"
mc "Sayori would've killed me."
s 1j "Yeah because leaving unannounced is super mean, [player]!"
show sayori 1i
y 3t "She's right you two, leaving unannounced is rather rude..."
y 3w "Poor Monika was wondering if she needed to hold off on the activity for you guys..."
show yuri 1a
mc "Ah! Well, sorry for keeping you all waiting..."
n 5w "Well it was kind of an emergency that I got this back as soon as possible, so I'm not really sorry..."
show natsuki 5n
show sayori 1g
m 1e "It's alright, you two."
m 2e "Natsuki, I'm glad you got your manga back."
m 3d "But just remember to keep better track of your things in the future."
n 5l "Oh this is never leaving my side again!"
"Natsuki clutches her manga tighter for emphasis."
n 3y "And I owe [player] big time for helping me find it!"
mc "Ah, it's nothing..."
"I scratch the back of my head as I look off in an embarrassment."
show sayori 1d
show natsuki_sweet as natsuki at t41 zorder 1
mc "It's the least I could do."
m 3b "Anyways, it's time to get started for today!"
show natsuki 1a
m 1a "Everyone, take a seat!"
show monika at thide
hide monika
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
show yuri at thide
hide yuri
"Everyone takes a seat at the front of the room by Monika."

if hangout2 == "Sayori":
    show sayori 1g at t11 zorder 1
    "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
    show sayori 1k
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Sayori isn't assuming something, is she?"
    "I sigh to myself as I turn my focus to Monika."
    show sayori at thide
    hide sayori
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity

if hangout2 == "Monika":
    show monika 1h at t11 zorder 1
    "While grabbing a seat, I notice Monika shooting me a disappointed glance."
    show monika 1o
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Monika isn't assuming something, is she?"
    "I mean she didn't seem that mad that I left for a little bit..."
    "Maybe she wanted to spend more time together today..."
    "I sigh to myself as I wait for her announcement."
    show monika at thide
    hide monika
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity


if hangout2 == "Yuri":
    show yuri 1r at t11 zorder 1
    "While grabbing a seat, I notice Yuri shooting me an agitated glance."
    show yuri 1w
    "I turn to ask what's wrong but she quickly looks away before I get the chance to."
    "Yuri isn't assuming something, is she?"
    "I sigh to myself as I turn my focus to Monika."
    show yuri at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity

if hangout2 == "Natsuki":

    if hangout1 == "Sayori":
        show sayori 1g at t11 zorder 1
        "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
        show sayori 1k
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Sayori isn't assuming something, is she?"
        "I sigh to myself as I turn my focus to Monika."
        show sayori at thide
        hide sayori
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity

    if hangout2 == "Monika":
        show monika 1h at t11 zorder 1
        "While grabbing a seat, I notice Monika shooting me a disappointed glance."
        show monika 1o
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Monika isn't assuming something, is she?"
        "I mean she didn't seem that mad that I left for a little bit..."
        "Maybe she wanted to spend more time together today..."
        "I sigh to myself as I wait for her announcement."
        show monika at thide
        hide monika
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity


    if hangout1 == "Yuri":
        show yuri 1r at t11 zorder 1
        "While grabbing a seat, I notice Yuri shooting me an agitated glance."
        show yuri 1w
        "I turn to ask what's wrong but she quickly looks away before I get the chance to."
        "Yuri isn't assuming something, is she?"
        "I sigh to myself as I turn my focus to Monika."
        show yuri at thide
        hide yuri
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity

    if hangout1 == "Natsuki":

        if encore_sayoriquestion_1 == True:
            show sayori 1g at t11 zorder 1
            "While grabbing a seat, I notice Sayori shooting me a disappointed glance."
            show sayori 1k
            "I turn to ask what's wrong but she quickly looks away before I get the chance to."
            "Sayori isn't assuming something, is she?"
            "I sigh to myself as I turn my focus to Monika."
            show sayori at thide
            hide sayori
            play music t3 fadein 1.0
            jump day3_clubactivity

        if encore_sayoriquestion_1 == False:
            show yuri 1r at t11 zorder 1
            "While grabbing a seat, I notice Yuri shooting me an agitated glance."
            show yuri 1w
            "I turn to ask what's wrong but she quickly looks away before I get the chance to."
            "Yuri isn't assuming something, is she?"
            "I sigh to myself as I turn my focus to Monika."
            show yuri at thide
            hide yuri
            scene bg club_day
            with wipeleft_scene
            play music t3 fadein 1.0
            jump day3_clubactivity




label day3_nreturn2:

scene bg corridor
with wipeleft_scene
show natsuki 5s at t11 zorder 1
"During the walk back, Natsuki looked unusually disappointed."
show natsuki 5n at t11 zorder 1
"Even though we were able to find her manga, I didn't really understood why she kept pouting at me..."
show natsuki 12a

if natsuki_continued_hug == False:
    "Did she really want me to keep hugging her that badly?"

if natsuki_hug == False:
    "Did she really want me to hug her that badly?"

if encore_sayoriquestion_1 == True:
    "I don't know...{w=0.38}it just didn't feel right to be with Natsuki in that way..."
    "I mean that's Sayori's job..."

if encore_sayoriquestion_1 == False:

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            "I mean I like her..."
            "But are we really that far along in our friendship yet?"
            "It's not like we've known each other that long..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "I mean, part of me likes Natsuki in that way..."
            "But, I think I might be having second thoughts about Sayori..."


    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            "I mean, part of me likes Natsuki in that way..."
            "But, part of me likes Yuri too..."



    if hangout1 == "Monika":
        if hangout2 == "Monika":
            "I mean, part of me likes Natsuki in that way..."
            $ style.say_dialogue = style.edited
            "{cps=16}But Monika is easily the best for me!{nw}"
            $ style.say_dialogue = style.normal



        else:
            "I mean, part of me likes Natsuki in that way..."
            "But with how I'm feeling about [hangout1] and [hangout2], I can't decide on any of my feelings right now..."
            "especially knowing that Yuri likes me..."


show natsuki 12b
n "[player], you doofus..."
mc "What?"
show natsuki 12a
n "You realize you just walked past the clubroom, right?"
mc "What?"
"I look back to see Natsuki standing idly by the doors to the clubroom."
"How did I screw that up?"
"I sigh as I walk back over to her."
show natsuki 5i
"Natsuki finally looks up at me."
n 4n "What's with you?"
mc "What do you mean?"
n 42a "You've been acting like a complete idiot for the past five minutes..."
mc "Well, I'm sorry, it's just..."
n 4f "Just what?!?"
"Natsuki's voice angrily rings through the hallway."
show natsuki 4g
mc "I've had a lot on my mind lately..."
mc "And I don't understand why you're so mad at me..."
show natsuki 4o
mc "I helped you find your manga..."
show natsuki 4w
n "*sighs*"
n 42a "You...{w=0.38}just don't get anything, do you?"

if natsuki_continued_hug == False:
    mc "What, did you want me to keep hugging you?"
    jump n_scold

if natsuki_hug == False:
    mc "What, did you want me to hug you?"
    jump n_scold

label n_scold:

n 3e "Maybe I did! But not anymore!"
n 1p "You're so...{w=0.38}you're so..."
show natsuki 1x
"Natsuki looks like she's about to explode at any second."
"Jeez...{w=0.38}did I screw up this badly over a stupid hug?"
show natsuki 1v at h11 zorder 1
n "You're so damn dense!"
show natsuki 1x
"Natsuki lets out a loud huff as she returns her focus to me."
"At this rate, someone's gonna come out of the clubroom and ask what's wrong..."
"I need to calm her down..."
mc "Natsuki, look: I-"
n 1r "I'm done with you for today."
show natsuki 1q
n "Thanks for helping me, [player]..."
show natsuki 12b
show natsuki at lhide
hide natsuki
play sound "sfx/closet-close.ogg"
"Natsuki wordlessly enters the clubroom and slams the door behind her."
"Great..."
"Looks I'm gonna have to deal with more problems today..."
"I brace myself for what's to come as I come into the clubroom."
play sound "sfx/closet-open.ogg"
scene bg club_day
with wipeleft_scene
show natsuki xul at t41 zorder 1
show sayori 2h at t42 zorder 2
show monika 1d at t43 zorder 3
show yuri 3e at t44 zorder 4
"As I walk in, I see Sayori, Monika and Yuri turn their attention to me while Natsuki looks in the opposite direction."
m 3m "Uhh, [player]...{w=0.38}what happened out there?"
s 2h "It sounded like you guys were fighting!"
mc "No, we weren't fighting!"
"Even though we were..."
"But I'd rather try to downplay the episode that just took place outside so that I don't cause more problems that I need to solve..."
y 3f "Then what we're you two doing then?"
y 3q "You guys were gone for a while too..."
show natsuki 5n
show sayori 1g
show monika 1f
show yuri 3e
"All 4 sets of eyes stare at me as I try to come up with a believable response."
"Ah, forget this!"
mc "It was nothing..."
"I sigh to myself as I take a seat up at the front of the room."
m 3m "Well...{w=0.38}why don't we get started with the activity I had in mind for today?"
s 1l "Yeah...{w=0.38}that sounds good to me, Monika!"
y 1c "I agree! I'm looking forward to see what you have in store for us today, Monika!"
m 2j "That's the spirit!"
show monika at thide
hide monika
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
show yuri at thide
hide yuri
"Everyone takes a seat at the front of the room by Monika."

if hangout2 == "Sayori":
    show sayori 1g at t11 zorder 1
    "While grabbing a seat, I notice Sayori shooting me a worried glance."
    show sayori 1k
    "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
    "I sigh to myself as I turn my focus to Monika."
    show sayori at thide
    hide sayori
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity

if hangout2 == "Monika":
    show monika 1e at t11 zorder 1
    "While grabbing a seat, I notice Monika oddly smiling at me."
    "I guess she's ust trying to reassure me that everything's going to be okay."
    "Hopefully there's going to be no more drama that I need to deal with."
    "I sigh to myself as I wait for her announcement."
    show monika at thide
    hide monika
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity


if hangout2 == "Yuri":
    show yuri 1e at t11 zorder 1
    "While grabbing a seat, I notice Yuri shooting me a worried glance."
    show yuri 1g
    "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
    "I sigh to myself as I turn my focus to Monika."
    show yuri at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    play music t3 fadein 1.0
    jump day3_clubactivity

if hangout2 == "Natsuki":

    if hangout1 == "Sayori":
        show sayori 1g at t11 zorder 1
        "While grabbing a seat, I notice Sayori shooting me a worried glance."
        show sayori 1k
        "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
        "I sigh to myself as I turn my focus to Monika."
        show sayori at thide
        hide sayori
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity


    if hangout2 == "Monika":
        show monika 1e at t11 zorder 1
        "While grabbing a seat, I notice Monika oddly smiling at me."
        "I guess she's ust trying to reassureme that everything's going to be okay."
        "Hopefully there's going to be no more drama that I need to deal with."
        "I sigh to myself as I wait for her announcement."
        show monika at thide
        hide monika
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity


    if hangout1 == "Yuri":
        show yuri 1e at t11 zorder 1
        "While grabbing a seat, I notice Yuri shooting me a worried glance."
        show yuri 1g
        "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
        "I sigh to myself as I turn my focus to Monika."
        show yuri at thide
        hide yuri
        scene bg club_day
        with wipeleft_scene
        play music t3 fadein 1.0
        jump day3_clubactivity

    if hangout1 == "Natsuki":

        if encore_sayoriquestion_1 == True:
            show sayori 1g at t11 zorder 1
            "While grabbing a seat, I notice Sayori shooting me a worried glance."
            show sayori 1k
            "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
            "I sigh to myself as I turn my focus to Monika."
            show sayori at thide
            hide sayori
            scene bg club_day
            with wipeleft_scene
            play music t3 fadein 1.0
            jump day3_clubactivity



        if encore_sayoriquestion_1 == False:
            show yuri 1r at t11 zorder 1
            "While grabbing a seat, I notice Yuri shooting me a worried glance."
            show yuri 1g
            "I give her a lukewarm smile to try to assure her that everything's okay, though I'm not sure if she bought it."
            "I sigh to myself as I turn my focus to Monika."
            show yuri at thide
            hide yuri
            scene bg club_day
            with wipeleft_scene
            play music t3 fadein 1.0
            jump day3_clubactivity



label day3_sreturn:

scene bg club_day
with wipeleft_scene
show monika 4k at t11 zorder 1
m "Okay everyone! Gather around! I want to share with you all the activity for today!"
show natsuki 5a at t41 zorder 1
show sayori 1a at t42 zorder 2
show monika 1a at t43 zorder 3
show yuri 1a at t44 zorder 4
"Everyone takes a seat at the front of the room by Monika."
jump day3_clubactivity


label day3_yreturn:

scene bg club_day
with wipeleft_scene
play music t3 fadein 1.0
show monika 4k at t11 zorder 1
m "Okay everyone! Gather around! I want to share with you all the activity for today!"
show natsuki 5a at t41 zorder 1
show sayori 1a at t42 zorder 2
show monika 1a at t43 zorder 3
show yuri 1a at t44 zorder 4
"Everyone takes a seat at the front of the room by Monika."
jump day3_clubactivity


label day3_clubactivity:

show natsuki 5a at t41 zorder 1
show sayori 1a at t42 zorder 2
show monika 1b at t43 zorder 3
show yuri 1a at t44 zorder 4
m "Alright, I've been meaning to bring this up for a while now!"
m 4b "After we finish the photoshoot on Monday, we're going to be reading a piece of literature of our choosing!"
show natsuki 5w at s41
show sayori 4r at h42
show monika 3j
show yuri 3d at h44
"Yuri and Sayori nearly burst out of their seats in excitment, while Natsuki lets out a groan."
"I mostly just keep a neutral expression, but I'm kind of intrigued as to what we'll be reading."
"Judging by Natsuki's response, we're probably thinking on the same plane, hoping we're not given something we'd have to read for our own Literature Classes..."
m 1b "I have a few early choices we can choose from, but I'm happy to entertain any ideas that you guys may have!"
show natsuki 5m at t41
show sayori 4a at t42
show yuri 3a at t44
n "Wait, is there a catch to this?"
m 1k "Nope! So long as it's literature!"
m 1e "Though ultimately this has to be something everyone is willing to read."
show natsuki 4y
show yuri 3l
"Natsuki's lips curl into a mischevious smile while Yuri shuts her eyes, bracing for what Natsuki's about to say next."
n 4l "So...{w=0.38}does manga count?"
m 3n "Well..."
show natsuki 4z
m 3e "Considering there's different kinds of manga, I'm willing to allow for its inclusion in this acitivity."
m 3m "I guess some forms of manga could be considered literature..."
show natsuki 4z at h41
n "Yes!"
"Natsuki pumps her fist in the air."
show natsuki 41 at t41
n "See, Yuri! Even Monika admits manga is literature!"
y 3h "Just keep in mind, it has to be something we'd all be willing to read, Natsuki..."
y 3f "And I hope you'd be willing to read something of my preferred tastes as well..."
show natsuki 3q
n "I guess that seems fair to me."
show natsuki 3n
show yuri 3d
y "Good!"
show sayori 1c
s "So what're you recommending, Monika?"
show sayori 1b
m 1b "I'd like to recommend this story!"
show monika 3j
"Monika proudly holds up a copy of a green book by the name of {i}Two Of Us{/i}."
m 2b "I just got started on it, but so far it's been a pretty good read!"
show monika 2a
show sayori 4n
"Sayori's eyes widen."
s 4x "Oooh! I've heard good things about that one! What's it about?"
m 1b "It's about this girl who realizes that she's living in a fake reality. But she finds someone else who knows this truth too."
m 2m "The story is about their struggle to accept their circumstances and their attempt to return to the real world."
m 2e "It's technically a romance novel, but it has some sci-fi and horror elements mixed in."
s 1h "How can a book be both horror and romance?"
s 1g "That doesn't make a lot of sense to me..."
m 2m "I haven't gotten that far into it so I can't answer that..."
m 2j "Besides, that'd probably be spoiling!"
show monika 2a
s 1l "Yeah, I guess it would..."
y 1b "I mean...{w=0.38}there are quite a few romance novels that mix horror into their story."
y 1d "Like this book for instance!"
show yuri 3c
"Yuri digs into her bag and holds up a book with a faded violet cover called {i}Outcast's Dilemma{/i}."
show natsuki 5s
"Natsuki rolls her eyes as soon as she reads the title."
n 5w "Is it another horror book?"
y 3j "The horror in this book is rather tame compared to what I usually like to read."
show natsuki 5u
show sayori 1k
"Well, I guess that means Yuri has a pretty high tolerance for horror..."
"Natsuki and Sayori both look off uneasily."
y 3b "I know you two aren't really into horror, but trust me, most of this book is romance."
show yuri 3a
s 1h "So what're the scary parts?"
n 4m "And what exactly is it all about?"
show sayori 1g
show natsuki 4n
y 1l "The book is about this girl who is an outcast from her dystopian society because she doesn't meet their standards for 'perfection'."
y 2m "She goes on to meet a man who saves her, and the two fall in love."
y 2b "Eventually, the man is able to get her accepted back into society, but only if she completes several tasks for the government."
n 1q "So that's where the horror comes in..."
show natsuki 1n
y 1e "I'd assume so, I'm only halfway done."
m 3b "That sounds like a fun book to read, Yuri! I'd be happy to get a copy of that!"
show yuri 3a
show monika 3a
mc "I mean I'd be willing to read anything you guys recommend."
mc "I don't exactly have a library back at my house..."
n 5l "Well if that's the case, [player], I think I got something you might enjoy!"
show natsuki 4j
"Natsuki reaches into her bag and holds up a large light blue book called {i}Love's Exit{/i}."
show monika 2d
m "Huh...{w=0.38}I've actually heard of this one before!"
y 3f "Actually I think I have as well!"
n 2l "This is actually one of the few manga that got their own movie!"
n 2t "Though the manga got much better reviews..."
n 2l "Anyways, it's about a boy who rescues his friend from her abusive family."
n 5m "But because his friend's family is pretty powerful, they have to go on the run."
n 5n "And while they're out there, they fall in love with each other, but they know their situation ultimately isn't sustainable."
n 5q "The ending of the story is really sad though..."
"I never thought Natsuki would ever be into something that's sad..."
y 1f "So it's a romantic tragedy manga?"
show yuri 1e
n 1k "Yeah, pretty much. I read it a few years ago."
n 1t "I picked it out because it looked like a cute story on the outside..."
n 5u "Then as I was reading it, I realized how wrong I was."
n 5k "It's a good story all around, though I probably wouldn't have read it if I knew it was a tragedy story."
y 3b "Well, I'll admit Natsuki, you have me intrigued!"
show yuri 3a
n 2l "Wow, really?!?!"
n 2z "I never thought I'd see the day you'd actually be picking up manga!"
y 3i "I just hope we see the day where you pick up a horror novel..."
n 5m "Hey, I said I'd be willing to try!"
n 5s "It just needs to be the right story..."
y 1e "What do you mean by that?"
show sayori 1g
"Sensing the incoming tension, Sayori steps in."
show sayori 2c
s "You know, I think I may have a story that we could all enjoy!"
show sayori 4q
"Sayori holds up a pink covered book called {i}Rainshine{/i}."
y 1h "I'm not familiar with this one...{w=0.38}what's it about?"
show yuri 1e
show sayori 4x
s "It's about this girl who develops a split personality and the story is about her struggle in trying to overcome it."
s 1y "The ending is really bittersweet..."
show sayori 1d
m 3b "Sounds like it could be interesting!"
show monika 1a
n 1c "Have you read it before?"
show natsuki 1a
s 1b "Yeah, I've read it a couple times before, but I haven't read it recently."
s 2x "It's actually one of my favorite stories!"
"I didn't even know Sayori had a favorite story..."
"Much less, I didn't know that she'd read something like that..."
"But I guess with the way she described it, I think I might know the reason she likes reading that book..."
"In fact, I think I might be seeing a general trend in each of the books described by everyone..."
"They all have a female protagonist and the story revolves around love in someway..."
"I guess that's what I get for being the only guy here..."
show sayori 1a
show monika 4b
m "Alright! So we have our options!"
m 1a "I'll look into seeing if I can get copies for all of us tomorrow, and if I'm able to. Then we can decide on what we'll read first!"
m 3b "Is that okay with everyone?"
show yuri 1a
"Everyone nods in agreement."
m 1j "Alright then!"
m 4b "We still have some time before the club ends, so you guys are free to hang around!"


if hangout3 == "Natsuki":
    jump n_aftermath

if hangout3 == "Monika":
    jump m_aftermath

if hangout3 == "Sayori":
    jump s_aftermath

if hangout3 == "Yuri":
    jump y_aftermath


label n_aftermath:

m 1a "Oh, and make sure you hand in your poems to [player] if you haven't already!"
mc "I think I just need your poems and Natsuki's."
m 1b "Alright, let me get mine!"
show monika at thide
hide monika
show yuri at thide
hide yuri
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
"Monika walks back to the front of the room while everyone gets up and goes back to their respective areas."
show monika 1a at t11 zorder 1
"After a few moments, Monika returns to me with her poems in hand."
m 1b "Here you are, [player]!"
show monika 1j
"Monika smiles as she hands me her poems."
m 1b "I can promise you that there's nothing...{w=0.38}unexpected in there."
show monika u111151
"Monika slyly winks at me."
mc "Well...{w=0.38}that's a relief!"
show monika 1l
"We both share a small laugh before the silence settles again."
show monika 2n
m "So...{w=0.38}I guess I'll leave you be and let you get Natsuki's poems."
show monika 2e
mc "Yeah, I'll talk to you later Monika!"
m 1j "Laters!"
show monika at thide
hide monika
"I head toward the closet where Natsuki seems to be shuffling through her belongings."
scene bg closet
with wipeleft_scene
show natsuki 3u at t11 zorder 1
"As I get closer, I notice Natsuki studying the cover of the manga that she mentioned earlier."
show natsuki 3c
"Though once she sees me hastily puts it back in her bag."



if natsuki_continued_hug or natsuki_hug == True:
    jump n_end1

if natsuki_continued_hug or natsuki_hug == False:
    jump n_end2


label n_end1:

n 4a "[player]! What's up?"
mc "Ah, not much...{w=0.38}just came to get your poems."
n 4k "Oh, shoot! I almost forgot!"
show natsuki 4a
"Natsuki rummages through her bag again and pulls out her poems."
n 4l "There you go! That should be all of my beautiful poems!"
mc "Well, I don't know if I'd call them beautiful but..."
show natsuki 4n
"Natsuki gives me a dejected look, but knowing her I can't tell if its genuine or not."
"Finally I feel her projected guilt overtake me."
mc "Okay, okay...{w=0.38}they're beautiful."
n 5y "I knew you'd agree with me!"
show natsuki 5z
mc "Well they're pretty good...{w=0.38}maybe I'll read them over again when I'm laminating."
show natsuki 5l
n "Sounds like it'll be a time well spent, [player]!"
mc "Yeah...{w=0.38}I take it you're heading home now?"
show natsuki 1u
stop music fadeout 2.0
"Natsuki solemnly looks down at the floor."
n 1q "Who knows what fun and adventure yours truly will go through tonight..."
show natsuki 1n
mc "Hey, look..."
mc "If things ever get too bad over there..."
mc "You can crash at my place for as long as you need to..."
n 5m "Well it's not really that bad, but..."
n 5t "I'll keep it in mind..."
show natsuki 5u
"Natsuki somberly looks down at the floor before cracking a quick joke."
n 5y "Maybe that way I can convince you to get a bigger blender!"
mc "Heh, well, maybe when my parents come back I'll talk to them about it..."
show natsuki 1k
mc "But, just be safe, okay?"
n 5y "Jeez, you act like I'm going away and never coming back or something..."
n 5a "I'll be fine, [player]..."
mc "Okay..."
show natsuki_sweet as natsuki at t11 zorder 1
"Natsuki and I stand awkwardly by the closet, unsure of what to say next."
"Today we both really learned a lot about each other..."
show natsuki 1c
n "Hey...{w=0.38}I'll talk to you later, okay?"
mc "Alright..."
mc "Catch you later!"
n 1z "Laters!"
show natsuki at thide
hide natsuki
"Natsuki shoots me one last smile as she waves good-bye to everyone before heading out of the clubroom."
play music t6 fadein 2.0
scene bg club_day
with wipeleft_scene
"I head back to my seat, and carefully stow away Monika and Natsuki's poems."
"I then slump down into my seat."
"Even though Natsuki told me not to worry...{w=0.38}I still feel anxious for her."
"Maybe I'm just overreacting but, I really do hope she's not in any danger..."
"That'd just add on to my already growing list of stress and worries..."
"Suddenly I feel a tap on my shoulder."
show yuri 3a at t11 zorder 1
"I turn around to see Yuri standing right by me."
"Speaking of stress and worries..."
y 3b "Hey, [player]!"
show yuri 3a
mc "Oh! Hey, Yuri! What's up?"
y 3j "Nothing much...{w=0.38}just wanted to see how you were doing."
y 3q "You look a little exhausted..."
mc "Ah, I'm fine...{w=0.38}it's just been a long day..."
y 3f "Yeah, I know what you mean. We all have days where things just overwhelm us."

if encore_festivalquestion_2 == "Natsuki":
    y 3d "You know, if you try some aromatherapy, it'd be a great way to relieve your stress!"
    y 3a "I highly recommend it!"
    mc "Is there a specific brand you use?"
    y 3b "I use Jasmine Oil."
    show yuri 3a


if encore_festivalquestion_2 == "Yuri":
    y 3d "It's why I use my aromatherapy to help aid me with stress relief!"
    y 3q "Along with a few other ways..."
    mc "What do you mean by that?"
    y 3n "Ah! Nevermind!"
    y 3q "But if you want to look into aromathearpy, I like to use Jasmine Oil."
    mc "Oh yeah! Isn't that what you showed me last Sunday?"
    y 3b "Yes, [player]! It was!"
    show yuri 3a

mc "Well, I'll have to look into getting some considering how the last few days have gone for me..."
y 3f "Why? What's happened?"
show yuri 3e
"Doesn't look like she knows I've read her poem..."
"Though I don't think I could even really tell Yuri what's been going on with Sayori, much less Natsuki..."
mc "It's...{w=0.38}things I really can't talk about..."
y 3h "I see..."
show yuri 3l
"Yuri dejectedly shuts her eyes."
"Well, maybe opening up a little bit wouldn't hurt..."
mc "It's just more life stuff if anything..."
y 3e "Eh? How so?"
mc "I guess it's just me figuring out what I want in my life I guess..."
mc "I don't know, I'm not having an existential crisis or anything, but it's just me figuring things out."
y 1h "I...{w=0.38}know what you mean, [player]."
y 1f "I mean...{w=0.38}we all are trying to figure out what to do next..."
y 1q "Though I guess I'm currently waiting to see what fate has in store for me..."
mc "How so?"
y 1o "Uhh..."
"Yuri nervously looks off."
"Even though I know what Yuri's going to say, I'm more curious in hearing how she'll say it."
y 2q "Well...{w=0.38}we can just say that I've...{w=0.38}had my eyes on someone recently..."
mc "Is that so?"
"I try ask quizzically as I can, but it's hard for me to act innocently dumb when I already know the answer."
y 3q "Yeah..."
y "And...{w=0.38}I just took a chance recently and I'm waiting to find out if he's feels the same way..."
show yuri 3s
"Yuri then sweetly looks at me."
"I feel a drop of sweat trickle down the back of my neck as I try my hardest to not break my curious expression."
mc "Well I...{w=0.38}hope it works out for you, Yuri..."
mc "I mean, what guy wouldn't want to date you?"
"As much as I'm trying to calm Yuri's nerves, I immediately regret phrasing it like that."
"Especially since I know she's talking about me!"
"I already screwed up majorly...{w=0.38}and I haven't even decided what to do yet!"
show yuri 3u
"Meanwhile, Yuri only blushes harder."
y 3v "Well I'm not sure if he and I share mutual feelings..."
y 3t "We haven't spent too much time together recently..."
y 3q "He's kind of been hanging around someone else..."
"I internally scream."
"I don't know how much longer I can keep this up..."
mc "Well...{w=0.38}I wish you the best, Yuri!"
show yuri 3e
mc "But, I think Sayori wants to head home now..."
y 3f "Eh? But Monika said-"
mc "I think I have to go, Yuri..."
stop music
y 3r "Why? So you can daydream about Natsuki again?!?!"
"Yuri's sudden yelling nearly makes my heart jump out of my chest."
show monika 1c at t31 zorder 1
show yuri 3r at t32 zorder 2
show sayori 3g at t33 zorder 3
"I also see Monika and Sayori turn their heads in my direction as she says that."
"Oh, great..."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        y 3h "It seems you always have time to spend with Natsuki..."
        y 3r "And you certainly had no problem hugging her in the middle of the clubroom!"

if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        y 3h "It seems you always have time to spend with Natsuki and the others..."

if hangout1 == "Natsuki":
    if hangout2 == "Monika" or hangout2 == "Sayori":
        y 3h "It seems you always have time to spend with Natsuki and the others..."

if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout1 == "Monika" or hangout1 == "Sayori":
        y 3h "It seems you always have time to spend with the others..."

if hangout1 == "Yuri":
    if hangout2 == "Monika" or hangout2 == "Sayori" or hangout2 == "Natsuki":
        y 3h "You had no problems spending time me with on Monday..."

if hangout1 == "Monika" or hangout2 == "Sayori" or hangout2 == "Natsuki":
    if hangout2 == "Yuri":
        y 3h "You had no problems spending time with me yesterday..."

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        y 3h "You had no problems spending time with me the last two days..."


y 3r "So why all of a sudden, when I want to have a genuine conversation not involving literature, you seem to want to avoid me?"
y 3h "I didn't do something wrong, did I?"
"I'm so caught off by Yuri's anger, I barely know how to respond..."
mc "N-{w=0.38}no, Yuri, that's not the point! Look, I-"
y 3r "If you want to be with Natsuki so badly, then go for her!"
y 3h "Just don't make us be a spectator to it!"
show yuri at thide
hide yuri
show monika 1c at t21 zorder 1
show sayori 3k at t22 zorder 2
"Yuri goes back to the front of the room, picks up her stuff, and wordlessly storms out of the clubroom."
"All three of us are left dumbfounded."
m 4m "Uhhh...{w=0.38}[player], what happened?"
mc "I just told her that I had to go and she just blew up at me!"
m 1m "Well...{w=0.38}that's certainly unlike Yuri..."
s 1l "Maybe it is a good time for us to head home..."
m 2m "Yeah...{w=0.38}there's nothing left to do anyways..."
m 2e "Hopefully everything will be calmer between you two tomorrow."
mc "Yeah...{w=0.38}I hope so too..."
m 1m "Well I have some work I need to do here, so you guys can head out."
s 1d "Thank you, Monika."
m 1e "No problem."
"Sayori and I pack our bags and we silently exit the clubroom and start our commute home."
jump day3_walkhome


label n_end2:

show natsuki 5f at t11 zorder 1
"I almost forgot she was mad at me for earlier... "
mc "Hey, Natsuki..."
"I try to say as friendly as I can, though it appears to have little affect."
n 5g "What do you want?"
"Man, I screwed up big time..."
"All over a stupid hug!"
mc "Uh...{w=0.38}do you have your poems?"
show natsuki 1g
"Natsuki reaches into her bag and shoves the poems into my arms."
mc "Thanks..."
show natsuki 1w
n "You're welcome! Now go away!"
"I don't want Natsuki to stay mad at me..."
"I need to fix this..."
show natsuki 5g
mc "Look, I'm sorry for earlier, okay?"
mc "I was an idiot, and I screwed up..."
mc "I was just...{w=0.38}surprised...{w=0.38}I-"
show natsuki 42c
n "Just save it."
n 42a "I don't want to talk to you right now..."
"I sigh in frustration."
"Maybe she'll be over this tomorrow..."
mc "Okay..."
"I dejectedly walk back to my seat."
play music t6 fadein 2.0
scene bg club_day
with wipeleft_scene
"I head back to my seat, and carefully stow away Monika and Natsuki's poems."
"I then slump down into my seat."
"This has just been a fustrating day..."
"No matter what I do, I just seem to be adding onto my list of stress and worries..."
"Suddenly I feel a tap on my shoulder."
show yuri 3a at t11 zorder 1
"I turn around to see Yuri standing right by me."
"Speaking of stress and worries..."
y 3b "Hey, [player]!"
show yuri 3a
mc "Oh! Hey, Yuri! What's up?"
y 3j "Nothing much...{w=0.38}just wanted to see how you were doing."
y 3q "It looks like Natsuki has you down again..."
mc "I guess that's one way of putting it..."
y 3f "What happened?"
show yuri 3e
"I'm not sure if I can honestly tell Yuri why Natsuki's mad at me..."
mc "Let's just say we had some...{w=0.38}miscommunication..."
y 3f "In what way?"
show yuri 3e
mc "I'd rather not say..."
y 3f "You didn't do something to her, did you?"
show yuri 3e
mc "It's more about what I didn't do..."
y 1q "I see..."
stop music fadeout 3.0
"Yuri lets out a dejected sigh."
y 3w "[player], I know this really isn't my business to ask but..."
y 3t "Are you and Natsuki...{w=0.38}together?"
"I was afraid she'd ask that question..."
mc "What? No, no, no...."
mc "We're just friends, Yuri..."
show yuri 3w
"Yuri clenches her fists."


if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        y 3v "But you've thought about it, haven't you?"
        mc "I don't know what you mean by that..."
        y 3q "[player], I've seen the way you look at her."
        y 3q "It's not a secret that you enjoy being in her company."
        show yuri 3e
        mc "Well what's it to you?"

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well I just wanted to see how've you been, since we rarely ever get the chance to talk to each other."


        if encore_festivalquestion_2 == "Yuri":
            y 3h "Well I just wanted to see how've you been, since we really haven't talked since Sunday."

        y 3r "Is that a bad thing?"
        mc "No, but I don't need people digging into my personal business."
        mc "I'm kind of focused on things that are actually important right now."


if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        y 3v "But you've thought about it, haven't you?"
        mc "I don't know what you mean by that..."
        y 3q "[player], I've seen the way you look at her."
        y 3q "It's not a secret that you enjoy being in her company."
        show yuri 3e
        mc "Well what's it to you?"

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well I just wanted to see how've you been, since we rarely ever get the chance to talk to each other."


        if encore_festivalquestion_2 == "Yuri":
            y 3h "Well I just wanted to see how've you been, since we really haven't talked since Sunday."

        y 3r "Is that a bad thing?"
        mc "No, but I don't need people digging into my personal business."
        mc "I'm kind of focused on things that are actually important right now."

if hangout1 == "Natsuki":
    if hangout2 == "Monika" or hangout2 == "Sayori":
        y 3v "Then why would you let her get you down?"
        mc "Because I care about her."
        mc "I'd like to be her friend."

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well if she's getting you down like this, maybe she's not exactly a good friend to you."
            mc "You don't know her like I do, Yuri..."
            mc "I don't think you should be focused on assuming things."

        if encore_festivalquestion_2 == "Yuri":
            y 3h "I don't exactly think that Natsuki's the type of person to accept people that quickly..."
            mc "Well she's not that bad..."
            y 3f "If she isn't, then why are you upset?"
            mc "Who are you to assume what I'm feeling, Yuri?"


if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout1 == "Monika" or hangout1 == "Sayori":
        y 3v "Then why would you let her get you down?"
        mc "Because I care about her."
        mc "I'd like to be her friend."

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well if she's getting you down like this, maybe she's not exactly a good friend to you."
            mc "You don't know her like I do, Yuri..."
            mc "I don't think you should be focused on assuming things."

        if encore_festivalquestion_2 == "Yuri":
            y 3h "I don't exactly think that Natsuki's the type of person to accept people that quickly..."
            mc "Well she's not that bad..."
            y 3f "If she isn't, then why are you upset?"
            mc "Who are you to assume what I'm feeling, Yuri?"



if hangout1 == "Yuri":
    if hangout2 == "Monika" or hangout2 == "Sayori" or hangout2 == "Natsuki":
        y 3v "Then why would you let her get you down?"
        mc "Because I care about her."
        mc "I'd like to be her friend."

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well if she's getting you down like this, maybe she's not exactly a good friend to you."
            mc "You don't know her like I do, Yuri..."
            mc "I don't think you should be focused on assuming things."

        if encore_festivalquestion_2 == "Yuri":
            y 3h "I don't exactly think that Natsuki's the type of person to accept people that quickly..."
            mc "Well she's not that bad..."
            y 3f "If she isn't, then why are you upset?"
            mc "Who are you to assume what I'm feeling, Yuri?"



if hangout1 == "Monika" or hangout2 == "Sayori" or hangout2 == "Natsuki":
    if hangout2 == "Yuri":
        y 3v "Then why would you let her get you down?"
        mc "Because I care about her."
        mc "I'd like to be her friend."

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well if she's getting you down like this, maybe she's not exactly a good friend to you."
            mc "You don't know her like I do, Yuri..."
            mc "I don't think you should be focused on assuming things."

        if encore_festivalquestion_2 == "Yuri":
            y 3h "I don't exactly think that Natsuki's the type of person to accept people that quickly..."
            mc "Well she's not that bad..."
            y 3f "If she isn't, then why are you upset?"
            mc "Who are you to assume what I'm feeling, Yuri?"


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        y 3v "Then why would you let her get you down?"
        mc "Because I care about her."
        mc "I'd like to be her friend."

        if encore_festivalquestion_2 == "Natsuki":
            y 3h "Well if she's getting you down like this, maybe she's not exactly a good friend to you."
            mc "You don't know her like I do, Yuri..."
            mc "I don't think you should be focused on assuming things."

        if encore_festivalquestion_2 == "Yuri":
            y 3h "I don't exactly think that Natsuki's the type of person to accept people that quickly..."
            mc "Well she's not that bad..."
            y 3f "If she isn't, then why are you upset?"
            mc "Who are you to assume what I'm feeling, Yuri?"





show yuri 3t
"Yuri gives me an insulted look."
"I shouldn't have said it like that..."
show yuri 3q
y "Well if I may make a suggestion..."
y 3r "Focus on those who actually want to spend time around you!"
y "Don't waste your time on her!"
"Yuri's sudden yelling nearly makes my heart jump out of my chest."
show monika 1c at t31 zorder 1
show yuri 3r at t32 zorder 2
show sayori 3g at t33 zorder 3
"I also see Monika and Sayori turn their heads in my direction as she says that."
"Oh, great..."
y "If you're going to be head-over-heels for someone who treats you like dirt on a constant basis, then I don't know what to tell you!"
mc "She doesn't treat me like dirt..."
y 3r "Whatever! I just know you could do better than her!"
show yuri at thide
hide yuri
show monika 1c at t21 zorder 1
show sayori 3k at t22 zorder 2
"Yuri goes back to the front of the room, picks up her stuff, and wordlessly storms out of the clubroom."
"All three of us are left dumbfounded."
m 4m "Uhhh...{w=0.38}[player], what happened?"
"I throw up my hands in frustration."
mc "It's just Yuri being difficult!"
m 1m "Well...{w=0.38}it's certainly unlike Yuri to suddenly lose her cool like that without reason..."
s 1h "Maybe she just had a bad day?"
m 1r "I don't know...{w=0.38}I'll text her about it later..."
m 2m "Anyways, there's nothing left to do for today..."
m 1m "I do have some work that I need to do here, but you guys are free to leave."
s 1d "Thank you, Monika. We'll see you tomorrow!"
m 1e "Have a good day you two!"
"Sayori and I pack our bags and silently exit the clubroom to start our commute home."
jump day3_walkhome




label s_aftermath:

m 1a "[player], I believe you have everyone's poems?"
mc "I do."
m 1j "Awesome!"
m 2e "Well, let us know if you need anything else!"
mc "I'll be sure to!"
show monika at thide
hide monika
show yuri at thide
hide yuri
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
"Everyone gets up and goes back to their respective areas."
"I notice Sayori starting to pack up her things, so assuming she'll want to leave soon, I start walking over to join her."
"However, I feel a tap on my shoulder as I'm walking over."

if poem_giver == "Natsuki":

    if sayori_ice == True:
        show natsuki 5u at t11 zorder 1
        "I turn around to see Natsuki standing right behind me."
        "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
        mc "Oh! Hey, Natsuki! What's up?"
        "I try to steady my voice as best as I can."
        "Fortunately, Natsuki doesn't really seem to notice, as she seems rather unnerved as well."
        show natsuki 5q
        "She lets out a sigh before looking up at me."
        n 12b "Look...{w=0.38}I'm sorry for how I acted earlier..."
        n 12a "I didn't mean to brush you off without giving a chance to explain what happened..."
        n 12b "I've just been having a bad day today..."
        show natsuki 12a
        mc "It's fine, Natsuki, really..."
        show natsuki 5n
        mc "I'm just glad we can put that behind us."
        show natsuki_sweet as natsuki at t11 zorder 1
        "Natsuki smiles as we stand in the middle of the room awkwardly."
        mc "So, what's got you down?"

        if hangout2 == "Natsuki":
            n 5m "I think I might've lost the manga we were reading yesterday..."
            show natsuki 5n
            mc "You mean the special edition one?"
            "Natsuki somberly shakes her head."



        if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
            n 5m "I think I might've lost one of my manga..."
            n 1m "It was a special edition copy and it was super expensive!"


        mc "Ah, jeez...{w=0.38}do you know where you might've left it?"
        n 5q "I think I have an idea where it might be..."
        n 3m "I might've left it in my last class."
        show natsuki 3n
        mc "Well, I hope you find it!"
        n 3m "You're not sticking around?"
        mc "Well I think Sayori's about to leave, so I'm gonna head home with her..."
        stop music fadeout 2.0
        n 3w "Why do you always do that?"
        mc "Do what? What do you mean?"
        n 5r "It's like you're always following her around like a lost puppy!"
        n 5x "I don't know how she constantly puts up with it..."
        n 1o "Why is it that almost everything you do has to revolve around Sayori?"
        mc "Natsuki that's not really true..."
        n 1x "Forget it! I have manga to find!"
        show natsuki at thide
        hide natsuki
        "Without another word spoken, Natsuki angrily walks out of the clubroom."
        "Though it doesn't appear that anybody's noticed the incident that just took place between us."
        "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
        show sayori 1a at t11 zorder 1
        s "Hey, [player]! Ready to go?"
        "I weakly smile at Sayori."
        mc "Yeah, sure...{w=0.38}let's get going..."
        show sayori 2g
        "Sayori picks up on my agitated tone."
        s 2h "You okay, [player]?"
        s 1g "You look upset..."
        mc "It's nothing...{w=0.38}let's just head home."
        s 1k "Okay then..."
        "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
        jump day3_walkhome


    if sayori_ice == False:
        show natsuki 5n at t11 zorder 1
        "I turn around to see Natsuki standing right behind me."
        "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
        mc "Oh! Hey, Natsuki! What's up?"
        "I try to steady my voice as best as I can."
        "Fortunately, Natsuki doesn't really seem to notice, as she seems rather unnerved as well."
        n 5m "H-{w=0.38}hey, I wanted to ask you something real quick..."
        show natsuki 5n
        "Sweat starts trickling down the back of my neck."
        mc "Y-{w=0.38}yeah?"

        if hangout2 == "Natsuki":
            n 5m "I think I might've lost the manga we were reading yesterday..."
            show natsuki 5n
            mc "You mean the special edition one?"
            "Natsuki somberly shakes her head."

        if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
            show natsuki 5m
            n 5m "I think I might've lost one of my manga..."
            n 1m "It was a special edition copy and it was super expensive!"

        n 1q "I was wondering if you'd seen it."
        "If it weren't for Natsuki's predicament, I might've let out the world's biggest sigh of relief."
        "She probably thinks I haven't read her poem yet..."
        show natsuki 1n
        mc "No...{w=0.38}I can't say I have. I'm really sorry, Natsuki..."
        n 5q "Great..."
        mc "Have you tried re-tracing your steps?"
        n 5q "I'm about to go do that..."
        n 3m "I might've left it in my last class."
        show natsuki 3n
        mc "Well, hey, I hope you find it!"
        n 3m "You're not sticking around?"
        mc "Well I think Sayori's about to leave, so I'm gonna head home with her..."
        stop music fadeout 2.0
        n 3w "Well that's typical..."
        mc "What do you mean?"
        n 5r "Why do you always follow her around like a lost puppy?!?"
        n 5x "I don't know how she constantly puts up with it..."
        n 1o "Why is it that almost everything you do has to revolve around Sayori?"
        mc "Natsuki that's not really true..."
        n 1x "Forget it! I have manga to find!"
        show natsuki at thide
        hide natsuki
        "Without another word spoken, Natsuki angrily walks out of the clubroom."
        "Though it doesn't appear that anybody's noticed the incident that just took place between us."
        "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
        show sayori 1a at t11 zorder 1
        s "Hey, [player]! Ready to go?"
        "I weakly smile at Sayori."
        mc "Yeah, sure...{w=0.38}let's get going..."
        show sayori 2g
        "Sayori picks up on my agitated tone."
        s 2h "You okay, [player]?"
        s 1g "You look upset..."
        mc "It's nothing...{w=0.38}let's just head home."
        s 1k "Okay then..."
        "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
        jump day3_walkhome




if poem_giver == "Yuri":

    if sayori_ice == True:
        show yuri 2q at t11 zorder 1
        "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
        mc "Oh! Hey, Yuri! What's up?"
        "I try to steady my voice as best as I can."
        "Fortunately, Yuri seems to be just as on edge as I am."
        y 2q "H-{w=0.38}hey, [player]..."
        y "I just wanted to apologize for my...{w=0.38}reaction to earlier..."
        y 2n "I should've given you the chance to explain yourself and not act disinterested in you at all!"
        y 3v "I hope you're not angry with me..."
        "I feel my muscles relax as soon Yuri finishes talking."
        "It seems like she hasn't expected me to read her poem yet..."
        show yuri 3t
        mc "It's fine, Yuri...{w=0.38}really!"
        mc "If anything...{w=0.38}I should be apologizing..."
        mc "So, I'm glad we got that out of the way..."
        y 3q "Y-{w=0.38}yes, indeed..."
        "Yuri nervously smiles as we stand in the middle of the room awkwardly."
        show yuri 3e
        mc "So, you sticking around?"
        y 3b "Yes, I'm going to get some reading done."

        if hangout2 == "Yuri":
            y 3q "I wouldn't mind it if you joined me..."


        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
            y 3q "You're more than welcome to join me if you wish..."

        show yuri 3s at t11 zorder 1
        "Yuri looks at me with hopeful eyes, as if she's counting on me to say yes."
        "Though given what I know, I probably shouldn't risk spending time with Yuri until I've absolutely made up my mind..."
        show yuri 3t
        mc "Ah, Yuri...{w=0.38}I appreciate the offer, but I'm probably about to leave with Sayori right now..."
        stop music fadeout 2.0
        y 3h "Pardon me, [player]...{w=0.38}but you don't need to always leave when Sayori does..."
        y 3f "I mean...{w=0.38}there's nothing wrong with staying a little while longer, is there?"
        "I almost can't believe this is coming from Yuri!"
        "But I guess this is just her way of trying to get me to stay."
        y 3q "I mean it's not like you and Sayori are together or something, correct?"
        mc "Yuri...{w=0.38}I really appreciate the offer but I do need to head home..."
        "Yuri lets out a sigh of defeat."
        mc "I have...{w=0.38}things to do..."
        show yuri 3w
        y "Fine...{w=0.38}spend time around Sayori..."
        y 3v "I'm sorry that I'm not worth your time..."
        mc "Yuri, it's not that I-"
        show yuri at thide
        hide yuri
        "Before I can finish my sentence, Yuri walks back to her seat and resumes reading her book."
        "Fortunately, it doesn't appear that anybody's noticed the incident that just took place between us."
        "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
        show sayori 1a at t11 zorder 1
        s "Hey, [player]! Ready to go?"
        "I weakly smile at Sayori."
        mc "Yeah, sure...{w=0.38}let's get going..."
        show sayori 2g
        "Sayori picks up on my agitated tone."
        s 2h "You okay, [player]?"
        s 1g "You look upset..."
        mc "It's nothing...{w=0.38}let's just head home."
        s 1k "Okay then..."
        "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
        jump day3_walkhome




    if sayori_ice == False:
        show yuri 1a at t11 zorder 1
        "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
        mc "Oh! Hey, Yuri! What's up?"
        "I try to steady my voice as best as I can."
        "Fortunately, Yuri doesn't seem to notice."
        y 2b "Hello, [player]! How're you doing this afternoon?"
        mc "Oh...{w=0.38}I'm doing alright, what about you?"
        y 2c "I'm doing great, thank you! I was just getting some more reading done..."
        y 3q "And I was just curious to see if you'd like to join me."

        if hangout2 == "Yuri":
            y 3q "We did make some good progress yesterday..."


        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
            y 3q "I wouldn't mind the company..."


        show yuri 3s at t11 zorder 1
        "Yuri looks at me with hopeful eyes, as if she's counting on me to say yes."
        "Though given that she doesn't seem to have expected me to have read her poem, I really don't want to risk slipping up..."
        show yuri 3t
        mc "Ah, Yuri...{w=0.38}I appreciate the offer, but I'm probably about to leave with Sayori right now..."
        stop music fadeout 2.0
        y 3h "Pardon me, [player]...{w=0.38}but you don't need to always leave when Sayori does..."
        y 3f "I mean...{w=0.38}there's nothing wrong with staying a little while longer, is there?"
        "I almost can't believe this is coming from Yuri!"
        "But I guess this is just her way of trying to get me to stay."
        y 3q "I mean it's not like you and Sayori are together or something, correct?"
        mc "Yuri...{w=0.38}I really appreciate the offer but I do need to head home..."
        mc "I have...{w=0.38}things to do..."
        "Yuri lets out a sigh of defeat."
        show yuri 3w
        y "Fine...{w=0.38}spend time around Sayori..."
        y 3v "I'm sorry that I'm not worth your time..."
        mc "Yuri, it's not that I-"
        show yuri at thide
        hide yuri
        "Before I can finish my sentence, Yuri walks back to her seat and resumes reading her book."
        "Fortunately, it doesn't appear that anybody's noticed the incident that just took place between us."
        "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
        show sayori 1a at t11 zorder 1
        s "Hey, [player]! Ready to go?"
        "I weakly smile at Sayori."
        mc "Yeah, sure...{w=0.38}let's get going..."
        show sayori 2g
        "Sayori picks up on my agitated tone."
        s 2h "You okay, [player]?"
        s 1g "You look upset..."
        mc "It's nothing...{w=0.38}let's just head home."
        s 1k "Okay then..."
        "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
        jump day3_walkhome



label y_aftermath:

m 2e "Oh, and Yuri, can I talk to you for a second?"
y 3q "Uh...{w=0.38}sure, Monika..."
show monika at thide
hide monika
show yuri at thide
hide yuri
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
"Yuri gets up and follows Monika to the front of the room while everyone else gets up and goes back to their respective areas."
"Sighing to myself, my eyes eventually drift to Monika and Yuri, who seem in deep and serious conversation."

if tell_monika == True:
    "I just hope Monika isn't asking Yuri about what I saw."
    "Then again, I don't think I'd have much reason to worry about that."

if tell_monika == False:
    "I just hope Monika isn't interrogating Yuri too hard about what happened..."
    "But part of me still feels I should've told Monika what I saw..."
    "I just hope Yuri was telling me the truth..."

"I still can't shake what I saw though..."
"How could someone like Yuri possibly be doing that to herself?"
"Suddenly I feel a tap on my shoulder."
show natsuki 4a at t11 zorder 1
"I look behind me to see Natsuki standing right by the desk next to me."
mc "Oh! Hey, Natsuki! Didn't see you there!"
mc "What's up?"
n 2c "Not much, just wanted to check on you."
n 2m "Since you and Yuri came in here looking upset."
n 2q "And you kinda look down over it..."
show natsuki 2n
mc "Ah! It's nothing to worry about..."
mc "There was just a...{w=0.38}misunderstanding between us..."
n 5h "What kind of 'misunderstanding'?"
show natsuki 5n
mc "I don't really wanna get into it right now..."
n 5q "Yeah that's fair. I just hope she didn't do something to you..."
mc "Don't worry, she didn't..."
n 2c "Well, that's good."

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        n 5u "I would offer to show you this really cool special edition manga I got, but I can't find it right now."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "It's been a while since we got to spend some time together..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."


        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."


if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout2 == "Yuri":
        n 5u "I would offer to show you this really cool special edition manga I got, but I can't find it right now."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "It's been a while since we got to spend some time together..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."


        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."



if hangout1 == "Yuri":
    if hangout2 == "Monika" or hangout2 == "Sayori":
        n 5u "I would offer to show you this really cool special edition manga I got, but I can't find it right now."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "It's been a while since we got to spend some time together..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."


        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."



if hangout1 == "Monika" or hangout1 == "Sayori":
    if hangout1 == "Monika" or hangout1 == "Sayori":
        n 5u "I would offer to show you this really cool special edition manga I got, but I can't find it right now."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "It's been a while since we got to spend some time together..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."


        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."



if hangout1 == "Natsuki":
    if hangout2 == "Monika" or hangout2 == "Sayori" or hangout2 == "Yuri":
        n 5u "I would offer to show you this really cool special edition manga I got, but I can't find it right now."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "It's been a while since we got to spend some time together..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."

        n 42b "And I've been waiting since Monday for us to get a chance to read together..."
        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."




if hangout1 == "Monika" or hangout2 == "Sayori" or hangout2 == "Yuri":
    if hangout2 == "Natsuki":
        n 5u "I would ask if you wanted to read some more, but I can't find what we were reading yesterday."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "I actually kind of like spending time around you..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."

        n 42b "And spending time with you yesterday was really fun..."
        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."



if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        n 5u "I would ask if you wanted to read some more, but I can't find what we were reading yesterday."
        mc "Do you think you might've left it somewhere?"
        n 5w "Well at this point, probably! I'm going to have to end up re-tracing my steps!"
        show natsuki 5n
        mc "Well, I don't want to take up anymore of your time..."
        n 5m "N-{w=0.38}no! It's okay, really!"
        n 5n "I have other things we can read..."

        if encore_festivalquestion_2 == "Natsuki":
            n 3u "I actually like hanging out with you..."


        if encore_festivalquestion_2 == "Yuri":
            n 3u "We never get the chance to do anything fun together..."


        mc "I appreciate the offer Natsuki, but I'm not really in the mood to read anything right now..."
        show natsuki 5n
        mc "Or be around anyone..."

show natsuki 5m at t11 zorder 1
n "Are you sure?"
"I simply nod my head."
show natsuki 42c
"Natsuki lets out a sigh."
n "It's cool..."
n 5q "I need to find that manga anyway..."
mc "Well if you want me to help you I-"
n 5n "No."
n 5s "You'd probably slow me down anyways..."
mc "Natsuki I-"
show natsuki at thide
hide natsuki
"Before I can say another word, Natsuki walks out of the clubroom."
"I put my hands on my face as I sigh quietly in frustration."
"Do I have to piss off every single person I talk to today?"
"Jeez..."
m "[player]?"
show monika 1f at t11 zorder 1
"I look up to see Monika worryingly standing over me."
m 2g "You okay?"
show monika 2f
mc "Yeah..."
m 2g "What happened?"
mc "I told Natsuki that I didn't want to be around anyone and she got upset at me."
m 2p "I guess she might be assuming something..."
show monika 2c
mc "I'll deal with one problem at a time."
mc "How'd it go with Yuri?"
m 2l "Well, I got her poems!"
show monika 1j
"Monika hands me Yuri's poems."

if tell_monika == True:
    mc "Did she tell you anything?"
    m 1r "Unfortunately, no."
    m 1p "She was very adamant that nothing happened and she was upset over something else."
    mc "I see..."
    m 1d "Well, if you're able to find out anything else, just let me know."


if tell_monika == False:
    m 2p "I don't know why Yuri's upset with you, [player]."
    m 2h "But I don't want you two fighting tomorrow."
    mc "I understand, I'm sure that she'll be fine tomorrow."
    m 2i "I hope so."
    m 1d "Well, if you want to talk about anything, just let me know."


show monika 1c
mc "I'll be sure to, Monika..."
m 2e "But, [player], I think everything will be fine tomorrow."
m 2n "Just focus on what you want to say to Natsuki."
show monika 2m
mc "Alright..."
show monika 2e
mc "Thank you for helping me out so much today!"
m 2m "It's...{w=0.38}what I do, [player]."
m 2e "And I'm always happy to help out our favorite member."
"I blush a little at Monika's remark."
m "I'll be here, [player]."
m 2m "Just let things take their course..."
mc "Thank you, Monika!"
m 2j "Anytime!"
show monika at thide
hide monika
"I walk over to my bag and carefully put Yuri's poems with Monika's."
show sayori 1a at t11 zorder 1
"I then look up to look for Sayori, but turns out, she already had my idea."
s 1x "Ready to head home [player]?"
show sayori 1b
mc "Yep...{w=0.38}I'm just looking forward to crashing on my couch..."
mc "It's been a long day..."
s 2i "[player], that's lazy talk!"
s 4r "Don't be a couch potato when there's still so much daylight left!"
show sayori 1q
mc "I admire your energy, Sayori..."
s 1y "Well, I have to be my best for somebody..."
"I blush a little as Sayori and I wave good-bye to Monika as we start the walk home."
jump day3_walkhome


label m_aftermath:

m 1a "Oh, and [player]! I still need to give you my poems!"

if poem_giver == "Natsuki":
    mc "Yeah I still need your poems and Yuri's."

if poem_giver == "Yuri":
    mc "Yeah I still need your poems and Natsuki's."

m 1b "Sure! Let me get mine!"
show monika at thide
hide monika
show yuri at thide
hide yuri
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
"Monika walks back to the front of the room while everyone gets up and goes back to their respective areas."
show monika 1a at t11 zorder 1
"After a few moments, Monika returns to me with her poems in hand."
m 1b "Here you are, [player]!"
show monika 1j
"Monika smiles as she hands me her poems."
m 1b "I can promise you that there's nothing...{w=0.38}unexpected in there."
show monika u111151
"Monika slyly winks at me."
mc "Well...{w=0.38}that's a relief!"
show monika 1l
"We both share a small laugh before the silence settles again."
m 3b "So, what do you think about our little reading list?"
show monika 3a
mc "Well like I said, I'm open to reading anything."
mc "Though everything that was brought up earlier sounds interesting enough for me to read."
m 4j "Well that's good!"
m 1b "I'm glad you have an open mind, [player]."
m 1n "Not everyone would be inclined to just read anything..."
m 1m "Especially considering our list is a little diverse..."
mc "Yeah, I get what you mean..."
show monika 1a
mc "Well hey, I have no problem with us reading something we normally wouldn't."
show monika 1j
mc "And with you leading the way, I'm sure it'll be fun!"
m 1k "I'm glad you feel that way, [player]! It's going to be blast!"
show monika 1j
mc "I'm looking forward to it!"
show monika 2n
"There's a brief pause between us as we try to figure out what to say next to each other."

if poem_giver == "Natsuki":
    m "So...{w=0.38}I guess I'll leave you be and let you get Yuri's poems."
    show monika 2e
    mc "Yeah, I'll talk to you later Monika!"
    m 1j "Laters!"
    show monika at thide
    hide monika
    "I then walk over to Yuri, whose sitting by the windowsill."
    scene bg club_day
    with wipeleft_scene
    show yuri 1g at t11 zorder 1
    mc "Hey, Yuri..."
    show yuri 1e
    y "Hmmm?"
    "Yuri puts down her book."
    y 1d "Oh, hello, [player]! How’re you doing today?"
    mc "Ah, I’m doing fine..."
    mc "What about you?"
    y 2c "I’m doing excellent! I'm just re-reading a little bit of Outcast's Dilemma!"
    mc "How is it?"
    y 2b "It's pretty good actually! Though I think Portrait of Markov is still better."
    show yuri 2a
    mc "You really like that book don't you?"
    y 2q "Well I haven't come across as anything as thrilling and detailed as Portrait of Markov in years."
    y 2c "You could say it's a breath of fresh air compared to what I've read recently."
    mc "I see..."
    y 2q "If you have the time, we could start reading this together..."
    show yuri 1s
    "Yuri shows me the cover of Outcast's Dilemma while looking on at me with hopeful, whimsical eyes."

    if encore_festivalquestion_2 == "Natsuki":
        "I never really did get the chance to read with her..."

    if encore_festivalquestion_2 == "Yuri":
        "I haven't had the chance to read with her in a while..."

    mc "Well to be honest, I did come over to get your poems..."
    y 1h "Oh..."
    y 2s "Well it’s a good thing you mentioned that."
    show yuri 2c
    "Yuri puts down the book and reaches into her bag to grab her poems."
    y 2b "That should be everything."
    mc "Great! Thank you so much!"
    show yuri 1e
    "I briefly look through Yuri’s poems just to make sure there are no unexpected surprises..."
    y 1f "Is something the matter, [player]?"
    mc "What? Oh no, no, I just...{w=0.38}wanted to admire your handwriting again!"
    show yuri 2d
    "Yuri chuckles to herself."
    y 3b "Well that’s certainly thoughtful of you, [player]..."
    y 3q "Though I don’t believe I gave you anything by mistake..."
    mc "That’s...{w=0.38}good to know..."
    y 3j "I mean it’s not like Natsuki accidentally gave you something, right?"
    mc "Well..."
    show yuri 3e
    "I forgot that Yuri was a pretty quick thinker."
    mc "I guess you could say that..."
    show yuri 3g
    "Yuri briefly looks toward the closet where Natsuki is organizing her manga."
    y 3h "I see..."
    mc "Yuri?"
    y 1q "Ah, it’s nothing..."
    y 1o "I think I should really get back to my book now..."
    mc "Alright..."
    "I sigh to myself as I'm forced to walk away from her."
    show yuri at thide
    hide yuri
    "Great..."
    "Knowing Yuri, she's already asking herself a million questions..."
    "Well, it's probably time to head home to think things over anyways."
    "I already spot Sayori starting to pack her things."
    show natsuki 5n at t11 zorder 1
    "However, as I'm walking back to my seat, I'm stopped by Natsuki."
    "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
    "I was not perpared for her to pull me aside like this..."
    mc "Oh! Hey, Natsuki! What's up?"
    "I try to steady my voice as best as I can."
    "Fortunately, Natsuki doesn't really seem to notice, as she seems rather unnerved as well."
    n 5m "H-{w=0.38}hey, I wanted to ask you something real quick..."
    show natsuki 5n
    "Sweat starts trickling down the back of my neck."
    mc "Y-{w=0.38}yeah?"

    if hangout2 == "Natsuki":
        n 5m "I think I might've lost the manga we were reading yesterday..."
        show natsuki 5n
        mc "You mean the special edition one?"
        "Natsuki somberly shakes her head."

    if hangout2 == "Sayori" or hangout2 == "Yuri" or hangout2 == "Monika":
        show natsuki 5m
        n 5m "I think I might've lost one of my manga..."
        n 1m "It was a special edition copy and it was super expensive!"

    n 1q "I was wondering if you'd seen it."
    "If it weren't for Natsuki's predicament, I might've let out the world's biggest sigh of relief."
    "She probably thinks I haven't read her poem yet..."
    show natsuki 1n
    mc "No...{w=0.38}I can't say I have. I'm really sorry, Natsuki..."
    n 5q "Great..."
    mc "Have you tried re-tracing your steps?"
    n 5q "I'm about to go do that..."
    n 3m "I might've left it in my last class."
    show natsuki 3n
    mc "Well, hey, I hope you find it!"
    n 3m "You're not sticking around?"
    mc "Well I think Sayori's about to leave, so I'm gonna head home with her..."
    stop music fadeout 2.0
    n 3w "Well that's typical..."
    mc "What do you mean?"
    n 5r "Why do you always follow her around like a lost puppy?!?"
    n 5x "I don't know how she constantly puts up with it..."
    n 1o "Why is it that almost everything you do has to revolve around Sayori?"
    mc "Natsuki that's not really true..."
    n 1x "Forget it! I have manga to find!"
    show natsuki at thide
    hide natsuki
    "Without another word spoken, Natsuki angrily walks out of the clubroom."
    "Though it doesn't appear that anybody's noticed the incident that just took place between us."
    "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
    show sayori 1a at t11 zorder 1
    s "Hey, [player]! Ready to go?"
    "I weakly smile at Sayori."
    mc "Yeah, sure...{w=0.38}let's get going..."
    show sayori 2g
    "Sayori picks up on my agitated tone."
    s 2h "You okay, [player]?"
    s 1g "You look upset..."
    mc "It's nothing...{w=0.38}let's just head home."
    s 1k "Okay then..."
    "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
    jump day3_walkhome



if poem_giver == "Yuri":
    m "So...{w=0.38}I guess I'll leave you be and let you get Natsuki's poems."
    show monika 2e
    mc "Yeah, I'll talk to you later Monika!"
    m 1j "Laters!"
    show monika at thide
    hide monika
    "I head toward the closet where Natsuki seems to be shuffling through her belongings."
    scene bg closet
    with wipeleft_scene
    show natsuki 3u at t11 zorder 1
    "As I get closer, I notice Natsuki studying the cover of the manga that she mentioned earlier."
    show natsuki 3c
    "Though once she sees me hastily puts it back in her bag."
    n 4k "Hey, what's up?"
    mc "Ah, not much..."
    mc "What about you?"
    n 3k "Same here, just organizing my manga again like always..."
    n 5x "I swear every time I come here, everything's in a different spot!"
    n 4m "Not to mention everything's always out of order..."
    mc "That sucks..."
    mc "Is someone else reading them?"
    n 5w "Well, I don't know! I only thought the teacher used that closet!"
    n 5y "At least who's ever reading it has good taste!"
    n 5q "I still can't find this special edition of Parfait Girls that I have..."
    show natsuki 5s
    mc "It's probably in some pile somewhere, if not, I'd just re-trace your steps."
    n 5m "Yeah, that's what probably I'm going to have to end up doing..."
    n 4k "Anyways, did you need something?"
    mc "Yeah...{w=0.38}I need to get your poems."
    n 1c "Oh, yeah! Hold on a second..."
    show natsuki 1a
    "Natsuki reaches into her bag and grabs her poems."
    n 1d "Here you go!"
    mc "Thanks, Natsuki!"
    show natsuki 1m
    "I briefly look through Natsuki's poems just to make sure there are no unexpected surprises..."
    n 1k "Is something wrong?"
    n 3l "Or are you finally coming to realize just how great my poems are?"
    mc "Uh sure...{w=0.38}you could say that..."
    show natsuki 3z
    "Natsuki cheerfully smiles to herself."
    n 3y "I'd knew you felt that way!"
    n 1c "But let me know if anything's missing or if I accidentally gave you something."
    mc "I'll...{w=0.38}be sure to..."
    n 2l "What, did Yuri give you something?"
    mc "Well..."
    "I shouldn't have done this in front of Natsuki..."
    mc "I guess you could say that..."
    show natsuki 1s
    "Natsuki briefly looks toward the front of the room where Yuri is reading."
    n 5q "So it ain't so..."
    mc "Natsuki?"
    n 1o "It's nothing!"
    n 5w "I need to finish organizing my manga so..."
    mc "Okay..."
    "I sigh to myself as I'm forced to walk away from her."
    show natsuki at thide
    hide natsuki
    "Great..."
    "Knowing Natsuki, she's already getting the wrong idea in her head..."
    "Well, it's probably time to head home to think things over anyways."
    "I already spot Sayori starting to pack her things."
    show yuri 1a at t11 zorder 1
    "However, as I'm walking back to my seat, I'm stopped by Yuri."
    "My heart immediately starts pounding against my chest as anxiety builds up inside of me."
    "I was not prepared for her to pull me aside like this..."
    mc "Oh! Hey, Yuri! What's up?"
    "I try to steady my voice as best as I can."
    "Fortunately, Yuri doesn't seem to notice."
    y 2b "Hello, [player]! How're you doing this afternoon?"
    mc "Oh...{w=0.38}I'm doing alright, what about you?"
    y 2c "I'm doing great, thank you! I was just getting some more reading done..."
    y 3q "And I was just curious to see if you'd like to join me."

    if hangout2 == "Yuri":
        y 3q "We did make some good progress yesterday..."


    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Monika":
        y 3q "I wouldn't mind the company..."


    show yuri 3s at t11 zorder 1
    "Yuri looks at me with hopeful eyes, as if she's counting on me to say yes."
    "Though given that she doesn't seem to have expected me to have read her poem, I really don't want to risk slipping up..."
    show yuri 3t
    mc "Ah, Yuri...{w=0.38}I appreciate the offer, but I'm probably about to leave with Sayori right now..."
    stop music fadeout 2.0
    y 3h "Pardon me, [player]...{w=0.38}but you don't need to always leave when Sayori does..."
    y 3f "I mean...{w=0.38}there's nothing wrong with staying a little while longer, is there?"
    "I almost can't believe this is coming from Yuri!"
    "But I guess this is just her way of trying to get me to stay."
    y 3q "I mean it's not like you and Sayori are together or something, correct?"
    mc "Yuri...{w=0.38}I really appreciate the offer but I do need to head home..."
    mc "I have...{w=0.38}things to do..."
    "Yuri lets out a sigh of defeat."
    show yuri 3w
    y "Fine...{w=0.38}spend time around Sayori..."
    y 3v "I'm sorry that I'm not worth your time..."
    mc "Yuri, it's not that I-"
    show yuri at thide
    hide yuri
    "Before I can finish my sentence, Yuri walks back to her seat and resumes reading her book."
    "Fortunately, it doesn't appear that anybody's noticed the incident that just took place between us."
    "I let out as a sigh as I walk over to Sayori, who seems to have just finished packing her things."
    show sayori 1a at t11 zorder 1
    s "Hey, [player]! Ready to go?"
    "I weakly smile at Sayori."
    mc "Yeah, sure...{w=0.38}let's get going..."
    show sayori 2g
    "Sayori picks up on my agitated tone."
    s 2h "You okay, [player]?"
    s 1g "You look upset..."
    mc "It's nothing...{w=0.38}let's just head home."
    s 1k "Okay then..."
    "Sayori and I wave good-bye to Monika and Yuri as we head out to start our commute home."
    jump day3_walkhome


label day3_walkhome:

scene bg residential_day
with wipeleft_scene

if hangout3 == "Sayori":
    show sayori 1a at t11 zorder 1
    "The walk home with Sayori considerably lifted my spirits from my run-in with [poem_giver]."
    show sayori 1g
    "Sayori still asked me a few questions about why I was in such a grouchy mood earlier, but I just muttered out some answer and she seemed to have mostly bought it."

    if sayori_ice == True:
        show sayori 1y
        "I'm still gushing a little over the little 'ice cream incident' we had earlier."
        show sayori 5b
        "Even though Sayori tried to play it off like it was nothing, I had a hard time believing that she wasn't trying to have a little fun with me."
        show sayori 5c
        "Needless to say, when I called her out on it, she called me a 'meanie' and we just left it at that."
        show sayori 4q

        if encore_sayoriquestion_1 == True:
            show sayori 4q
            "Seeing Sayori like this gives me hope that she can overcome her depression."
            "It's not like it's taken her over fully, she's still capable of being herself..."
            "And today reminded me of that..."
            show sayori 1y
            "In some ways, she still is the same kid next door I grew up with..."

        if encore_sayoriquestion_1 == False:
            show sayori 4q
            "Seeing Sayori like this gives me hope that she can overcome her depression and we can actually move on from last Sunday's events..."
            "Today reminded me that she still is that quirky, funny kid I grew up next to..."
            show sayori 1y
            "And that's the side of her I always liked, even if it drove me crazy from time to time..."


    if sayori_ice == False:
        show sayori 1k
        "Part of me still feels a little gulity for not sharing my ice cream with Sayori earlier."
        "Granted, for all intents and purposes it was my ice cream and she had her own..."
        show sayori 1f
        "I didn't mean to put her in a bad mood over it..."
        show sayori 1d
        "But we talked it out and we are able to smooth that incident over."
        show sayori 1k
        "Even if Sayori won't accept it, I do find it kind of adorable when she begs for my food."
        show sayori 1e
        "It reminds me that the little quirky girl I grew up next door with is still there underneath all those rainclouds..."

        if encore_sayoriquestion_1 == True:
            show sayori 1y
            "I just hope I'm able to bring that out full time..."

        if encore_sayoriquestion_1 == False:
                show sayori 1y
                "I just hope I'm able to bring it back..."



if hangout3 == "Monika" or hangout3 == "Natsuki" or hangout3 == "Yuri":
    show sayori 1k at t11 zorder 1
    "The walk home with Sayori didn't really do much to improve my mood after my run-in with [poem_giver]."
    show sayori 1g
    "Sayori still asked me a few questions about why I was in such a grouchy mood earlier, but I just muttered out some answer and she seemed to have mostly bought it."
    show sayori 1k

    if encore_sayoriquestion_1 == True:
        if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out one word answers to me."
                show sayori 1i
                "On  occasion, I even saw Sayori flashing me an angry look, which only made me feel worse about my situation with her..."
                "I know I promised to spend more time with her, but once again, I didn't fall through..."
                show sayori 1k

    if encore_sayoriquestion_1 == True:
        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "Still, I tried to not let my mood get the best of me. I tried to make some meaningful conversation about how her day went, but she largely just muttered out some answer to me."
                show sayori 1g
                "On  occasion, I even saw Sayori flashing me a concerned look, which only made me feel worse about what I did earlier..."
                "Hopefully she doesn't mind that I spent time with someone else for the day..."
                "So long as I try to make it the occasional execption and not the norm..."
                show sayori 1k
                "But I know I have to be careful around Sayori..."
                "If she ever got the idea that I was being disloyal to her, I can't imagine how she'll take it with her current state of mind..."





    if encore_sayoriquestion_1 == True:
        if hangout1 == "Sayori":
            if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out some usual answer to me."
                show sayori 1k
                "Sayori even generally refused to make eye contact with me for most of the walk..."
                "I know I promised to make up for yesterday to spend more time with her, but once again, I didn't fall through..."
                "She's probably thinking the worst possible thing I did with [hangout3]..."
                "And I suppose she has a good reason to, given what she saw with me and [hangout2] yesterday..."


    if encore_sayoriquestion_1 == True:
        if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout2 == "Sayori":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out some usual answer to me."
                show sayori 1g
                "On  occasion, I even saw Sayori flashing me a concerned look, which only made me feel worse about what I did earlier..."
                "I know I promised to spend more time with her, and lately I haven't completely fallen through..."
                show sayori 1k
                "I just hope she isn't thinking of the worst scenario possible with why I took so long to get back to the club with [hangout3]..."



    if encore_sayoriquestion_1 == False:
        if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out one word answers to me."
                show sayori 1f
                "On  occasion, I even saw Sayori flashing me a pained look, which only made me feel worse about my situation with her..."
                "I know I promised to spend more time with her, but once again, I didn't fall through..."
                show sayori 1k

    if encore_sayoriquestion_1 == False:
        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out one word answers to me."
                show sayori 1g
                "On  occasion, I even saw Sayori flashing me a concerned look, which only made me feel worse for brushing her off..."
                "Hopefully she doesn't mind that I spent time with someone else for the day..."
                show sayori 1k
                "So long as I try to make it the occasional execption and not the norm..."

    if encore_sayoriquestion_1 == False:
        if hangout1 == "Sayori":
            if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out some usual answer to me."
                show sayori 1g
                "On  occasion, I even saw Sayori flashing me a concerned look, which only made me feel worse about my situation with her..."
                "I know I promised to spend more time with her, and lately I haven't completely fallen through..."
                show sayori 1k
                "I just hope she isn't thinking of the worst scenario possible with why I took so long to get back to the club with [hangout3]..."
                "But I can tell she didn't appreciate me leaving her in the clubroom for so long without explanation..."

    if encore_sayoriquestion_1 == False :
        if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
            if hangout2 == "Sayori":
                "Still, I tried to not let my mood get the best of me, I tried to make some meaningful conversation about how her day went, but she largely just muttered out some usual answer to me."
                show sayori 1g
                "On  occasion, I even saw Sayori flashing me a concerned look, which only made me feel worse about my situation with her..."
                "I know I promised to spend more time with her, and lately I haven't completely fallen through..."
                "Especially with what went down between us yesterday..."
                show sayori 1k
                "I just hope she isn't thinking of the worst scenario possible with why I took so long to get back to the club with [hangout3]..."
                "But I can tell she didn't appreciate me leaving her in the clubroom for so long without explanation..."

    if hangout3 == "Monika":
        "I try to think back to how I spent earlier with Monika in the band room, which improved my mood a little."
        "Though I'm still surprised with how forward she was with me..."

        if encore_sayoriquestion_1 == True:
            show sayori 1g
            "What puzzles me the most is that Monika knows I'm with Sayori. I can't see why she'd want to get caught between us..."
            "It's not like Monika actually likes me...{w=0.38}right?"

        if encore_sayoriquestion_1 == False:
            show sayori 1g
            "Could Monika actually like me?"
            "Even though I still need to decide on a bunch of things, the fact that Monika may be into me is intoxicating..."
            "I just can't get over it!"

    if hangout3 == "Natsuki":
        "I try to think back to how I spent earlier helping Natsuki find her manga, which helped improve my mood a little."
        "Though I'm still worried about what she told me."
        show sayori 1g
        "I'm tempted to tell Sayori everything Natsuki told me, but, I wouldn't want to risk spreading rumors."
        "And I did make a promise to Natsuki not to tell anyone either..."
        show sayori 1k
        "Not that Sayori's the gossip type anyways, I'm just worried she'll tell or make me tell a teacher or the principal and things will escalate out of control from there."


    if hangout3 == "Yuri":
        "I try to think back to how I spent earlier reading with Yuri by the fountain, which helped improve my mood a little."
        "Though I'm still worried about what I saw."
        show sayori 1g
        "I'm tempted to tell her what I thought I saw, but, I wouldn't want to risk spreading rumors."
        show sayori 1k
        "Not that Sayori's the gossip type anyways, I'm just worried she'll tell or make me tell a teacher or the principal and things will escalate out of control from there."


show sayori 1c at t11 zorder 1
s "[player], we're here!"
show sayori 1b
mc "Huh?"
"After Sayori derails my train of thought, I look over to see that we've already arrived at our houses."

if hangout3 == "Natsuki" or hangout3 == "Monika":
    mc "You know if you didn't say something, that would've been the second time today I walked past where I was supposed to go!"
    s 2l "Wow, looks like you had a pretty long day after all..."
    show sayori 1k
    mc "Yeah...{w=0.38}it really has been..."

if hangout3 == "Sayori" or hangout3 == "Yuri":
    show sayori 4r
    s "Jeez, [player]! You've been spacing out more than I have lately!"
    show sayori 1b
    mc "Yeah...{w=0.38}I've just had a lot to think about, that's all..."

stop music fadeout 1.0
s 1h "Is everything okay, [player]?"
show sayori 1g
mc "Yeah...{w=0.38}I'm fine Sayori."
s 1g "I mean you've looked pretty stressed this whole day..."

if tell_s == True:
    s 1f "Is it because of last night?"
    mc "I'm sure that has something to do with it, but it's not everything..."

if tell_s == False:
    s 1f "Did you not get a lot of sleep last night?"
    mc "Well it's more like I didn't get a lot of good sleep..."
    mc "But it's more than that..."

show sayori 2g
s "Well what's bugging you?"
mc "Sayori, it's not something you can really solve..."
mc "And it's not something I can really talk with you or anyone else really..."
show sayori 1k
mc "It's just...{w=0.38}I need to solve this one on my own, okay?"
s "Alright..."
s 1d "Well I hope whatever it is, [player], I hope it all works out for you."
s 4h "I'm here if you need me..."
mc "I know, and that's all I need to know right now..."
show sayori 1k
"Sayori and I stand silently on the sidewalk, the silence only being disturbed by the  occasional gust of wind."
s 1d "Well...{w=0.38}I'll talk to you later, [player]..."
mc "Alright..."

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            if hangout3 == "Sayori" or hangout3 == "Monika" or hangout3 == "Natsuki" or hangout3 == "Yuri":
                show sayori 4q at face
                play sound fall
                "Sayori runs up to me and gives me a tight hug."
                jump s_sleeptight

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori" or hangout3 == "Monika" or hangout3 == "Natsuki" or hangout3 == "Yuri":
                show sayori 4q at face
                play sound fall
                "Sayori runs up to me and gives me a tight hug."
                jump s_sleeptight

if encore_sayoriquestion_1 == True:
     if hangout1 == "Sayori" or hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
         if hangout2 == "Sayori" or hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
             if hangout3 == "Sayori":
                 show sayori 1k
                 s "Well I...{w=0.38}guess I'll talk to you later then..."

                 if tell_s == True:
                     s 1g "Just sleep well tonight, okay?"
                     mc "I'll try my best..."
                     show sayori at thide
                     hide sayori
                     "Sayori smiles at me one more time before turning back to head to her house."
                     "I guess it'll take more time to get back to where we were than I originally thought..."
                     "I sigh softly to myself as I turn the key and walk into my house."
                     jump day3_reflection

                 if tell_s == False:
                     s 1g "Just be okay, for me...{w=0.38}okay?"
                     mc "I'll try my best..."
                     show sayori at thide
                     hide sayori
                     "Sayori smiles at me one more time before turning back to head to her house."
                     "I guess it'll take more time to get back to where we were than I originally thought..."
                     "I sigh softly to myself as I turn the key and walk into my house."
                     jump day3_reflection


label s_sleeptight:
if tell_s == True:
    s 1g "Just sleep well tonight, okay?"
    mc "I'll try my best..."
    show sayori 1y at t11 zorder 1
    "Sayori and I release each other as we both madly blush at each other."
    s 1d "Love you, [player]~"
    mc "I love you too, Sayori..."
    show sayori at thide
    hide sayori
    "With one more smile between us, we wave a good-bye to each other as we walk back into our houses."
    jump day3_reflection

if tell_s == False:
    s 1g "Just be okay, for me...{w=0.38}okay?"
    mc "I'll try my best..."
    show sayori 1y at t11 zorder 1
    "Sayori and I release each other as we both madly blush at each other."
    s 1d "Love you, [player]~"
    mc "I love you too, Sayori..."
    show sayori at thide
    hide sayori
    "With one more smile between us, we wave a good-bye to each other as we walk back into our houses."
    jump day3_reflection




if encore_sayoriquestion_1 == False:
    show sayori 1y
    s "Well I...{w=0.38}guess I'll talk to you later then..."

    if tell_s == True:
        s 1g "Just sleep well tonight, okay?"
        mc "I'll try my best..."
        show sayori at thide
        hide sayori
        "With one more smile between us, we wave a good-bye to each other as we walk back into our houses."
        jump day3_reflection

    if tell_s == False:
        s 1g "Just be okay, for me...{w=0.38}okay?"
        mc "I'll try my best..."
        show sayori at thide
        hide sayori
        "With one more smile between us, we wave a good-bye to each other as we walk back into our houses."
        jump day3_reflection


label day3_reflection:

scene bg bedroom
with wipeleft_scene
"After changing out of my school uniform and into my regular cloths, I immediately collapse back onto my bed."
mc "What the hell am I going to do?"
"I quixotically ask myself."


if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            jump s_mono1

if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            jump s_mono2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            jump n_mono1

if encore_sayoriquestion_1 == False:
    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            jump n_mono2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            jump y_mono1

if encore_sayoriquestion_1 == False:
    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            jump y_mono2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            jump m_mono1

if encore_sayoriquestion_1 == False:
    if hangout1 == "Monika":
        if hangout2 == "Monika":
            jump m_mono2

if encore_sayoriquestion_1 == True:
    if hangout1 == "Natsuki" or hangout1 == "Yuri" or  hangout1 == "Monika":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or  hangout2 == "Monika":
            jump mix_mono1

if encore_sayoriquestion_1 == True:
    if hangout1 == "Sayori" and hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" and hangout2 == "Sayori":
        jump mix_mono2


if encore_sayoriquestion_1 == False:
    if hangout1 == "Natsuki" or hangout1 == "Yuri" or  hangout1 == "Monika":
        if hangout2 == "Natsuki" or hangout2 == "Yuri" or  hangout2 == "Monika":
            jump mix_mono3


if encore_sayoriquestion_1 == False:
    if hangout1 == "Sayori" and hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika" and hangout2 == "Sayori":
            jump mix_mono4

########Sayori#############

label s_mono1:

    "I know I love Sayori."
    "I do..."
    "I've enjoyed every moment I've been around her..."
    "There's really no reason to change that..."
    "But I don't feel like I can let [poem_giver] down..."

    if hangout3 == "Sayori":
        "Should I give her a chance at least?"
        jump s_m_cont

    if hangout3 == "Natsuki":
        "And with what I know about Natsuki now...{w=0.38}I'm really worried about her..."
        "I know I have to help her some way..."
        "But, I can't deny that I now feel some sort of attraction to her..."
        "Her hug, while unexpected, was really warm and heavenly..."
        jump s_m_cont

        if natsuki_continued_hug == True:
            jump n_d_1

        if natsuki_continued_hug == False:
            jump n_d_2

        if natsuki_hug == True:
            jump n_d_1

        if natsuki_hug == False:
            jump n_d_2

    if hangout3 == "Yuri":
        "And with what happened with Yuri earlier...{w=0.38}I'm really worried about her..."
        "I have to know if she really does that to herself..."
        "I can't deny that part of me has always had some attraction to Yuri..."

        if tell_monika == True:
            "I mean, I care enough about her to have at least told Monika about what I think I saw..."
            "And I still worry for her safety, and I want her to be okay..."

        if tell_monika == False:
            "I mean, I care enough about her to cover for her..."
            "But, I don't know if I'm doing anyone good there..."

        "Part of me has always wanted to get to know Yuri, but I've just never had much luck due to her reclusive nature..."
        "I know it's not right for me to risk my relationship with Sayori for her..."
        "And I've really grown distant from Natsuki lately..."
        "I sigh to myself."
        "Can I even give them a chance at this point?"
        jump s_m_cont

    if hangout3 == "Monika":
        "And with what happened earlier with Monika really surprised me..."
        "In fact, Monika has been nothing but full of surprises today..."
        "I'm glad she was able to calm me down and reassure me of everything during lunch..."
        "Even if she was a little too kind to me in the music room..."
        "If it wasn't for her help today, I'd probably still be a nervous wreck..."
        "Well, I'd be more of a nervous wreck if it wasn't for her..."
        "I can't deny that I've always liked Monika..."
        "But I thought she was out of my league..."
        "And earlier...{w=0.38}she clearly had no problems flirting with me..."
        "But, I know I was being a little disloyal at best to Sayori..."
        "I can't really give Monika a chance at this point in time, can I?"
        jump s_m_cont

label n_d_1:

"Even though I chose to hug her back, I really still question if I made the right decision there..."
"I mean, I may have helped Natsuki in the moment, sure..."
"But what would've Sayori said? Would she have approved?"
"And what would've Yuri said had she seen us like that?"
"I sigh to myself."
"I don't want to risk hurting my relationship with Sayori..."
"And I feel bad that I'm only growing more distant from Yuri..."
"But is it right for me to give them a chance?"
jump s_m_cont

label n_d_2:

"Even though I think I made the right decision by not returning it, I can't help but feel sorry for Natsuki..."
"She put herself out there to me in that moment...{w=0.38}and she felt hurt because I didn't return it..."
"She probably hasn't had anyone show her any serious level of interest or care in a while, if ever..."
"Maybe I didn't make the right call there..."
"But I don't want to risk hurting my relationship with Sayori..."
"And I feel bad that I'm only growing more distant from Yuri..."
"Should I give them a chance?"
jump s_m_cont




label s_m_cont:

"I mean in hindsight...{w=0.38}I did kind of say yes to Sayori right on the spot..."
"I only spent time alone with [poem_giver] once..."
"But I know I have an obligation to stick to Sayori..."
"She needs me..."
"But, I guess it's worth asking myself:{w=0.38} Do I really need her?"
"I stare up at my ceiling as I repeat the question in my head over and over."
"I mean...{w=0.38}where would I be without her?"
"If it wasn't for her inviting me to the club...{w=0.38}she wouldn't be my girlfriend right now..."
"I wouldn't have met any of the others..."
"I'd probably be in this room, just watching whatever anime was on and playing online..."
"It's a simple life, sure...{w=0.38}but it's kind of lonely in retrospect."
"I'd probably be feeling sorry for myself that I didn't let Sayori take me to the club..."
"I owe her so much...{w=0.38}even if she won't admit it..."

if hangout3  == "Sayori":
    "And she does light up my world in a way that no anime or game could ever do..."
    "She does make me feel genuinely happy and I do feel accepted around her..."
    "Not to mention we've put up with each other for all these years..."
    "My life would probably be pretty dull and boring with out her..."
    "I mean even the little fight we had over the ice cream was kind of fun..."

    if sayori_ice == True:
        "Even though I did indulge her and let her take my ice cream from me..."
        "It's good to see that despite whatever she has to endure from her 'rainclouds', she still knows how to be herself..."


    if sayori_ice == False:
        "Even though I didn't let her have my ice cream, and the mood took a rather sour turn from there..."
        "Probably her 'rainclouds' acting up again, but she's been handling herself better all things considered..."

if hangout3  == "Natsuki" or hangout3  == "Yuri" or  hangout3  == "Monika":
    "I wouldn't have the chance to get to know [hangout3] a little bit better if it wasn't for her..."


"But if I wasn't in her life, had I not grown so close to her..."
"If she continued to have those rainclouds, where would she be?"
"I almost fear the answer..."
"Not that I think Sayori would ever do anything I saw in my dreams...{w=0.38}I have a sinking feeling that it may have crossed her mind..."
"I mean she's told me what, three times now that 'I'm the reason she's even alive'?"
"What does that even mean?"
"I know her well enough to know it's not her way of flirting..."
"But it's not like she's ever given me any huge warning signs aside from this..."
"..."
"Maybe I should ask her about it sometime..."
"She'll probably say no, but even if she tells me that, I could use the peace of mind..."
"Speaking of peace of mind, I know that's what [poem_giver] wants..."
"And...{w=0.38}I'm just going to have to lay it out for her."
"I guess at one point, I did have similar feelings for [poem_giver]."
"Especially with how last Sunday went..."
"And I still find part of me wondering if what could've been...{w=0.38}still could be..."


if hangout3  == "Sayori":
    "Especially considering how much fun I had with her preparing for and at the festival..."
    "Even if she was competing with Sayori for my attention..."



if hangout3  == "Natsuki" or hangout3  == "Yuri" or  hangout3  == "Monika":
    "And while I had a lot of fun preparing for and at the festival with her..."
    "I can't help but wonder if I kept hanging out with [hangout3]..."
    "Who knows what could happen?"


"But...{w=0.38}can I really do that to Sayori?"
"I roll over to face my bookshelves."
"On one of the shelves, I spot a picture of me and Sayori at the carnival."
"Man...{w=0.38}that must've been at least ten years ago..."
"Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
"And risk possibly dividing the club?"
"I get out of my bed and walk over to pick up the picture frame."
"Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
"Huh...{w=0.38}I almost forgot that's when I won it for her..."
"I always did tell Sayori that she deserved the best..."

if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."


    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2

if hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask

if hangout3 == "Monika":
    "But am I what she needs?"
    "Am I what she deserves?"
    "..."
    "Agh! This is hopeless!"
    "I don't know anything! How am I supposed to decide this when the girl I've always fantasized about being with now possibly likes me?!?"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask

label n_line_1:

"Thankfully, judging by the tone in Natsuki's voice, it doesn't sound like anything bad happened..."
jump n_hangout_ask

label n_line_2:

"Thankfully, judging by the tone in Natsuki's voice, she seems to have cooled off from earlier..."
jump n_hangout_ask






label s_mono2:

    "I really think I'm starting to have second thoughts about Sayori...."
    "Over the last few days, I've really come to re-discover the connection we once had..."
    "Even though it's mostly been me trying to mend her damaged heart and just help her out the best I can..."
    "But in doing so...{w=0.38}I almost feel like I'm still looking after her..."
    "Almost in a way a boyfriend would..."
    "I still do really care about Sayori and her feelings..."
    "Even though I didn't exactly expect her to to react well when I rejected her confession, in some ways I may have felt as bad as she did about the whole thing..."
    "I considered it a miracle that she bothered to talk to me the next day..."
    "Even though the pain was very much apparent, she still tried to make the festival as fun of an experience as possible."
    "I guess that's why she chose to stick around Monika while I was off with [poem_giver]..."
    "Oh, Sayori..."
    "I didn't want to hurt you..."
    "But if I'm having these feelings for Sayori now, why didn't I have them when she confessed?"
    "Could this just be pure second-guessing on my part? Pity?"
    "Or do I genuinely like her back..."
    "I mean...{w=0.38}I've always liked Sayori, but I only saw as more as friends than anything else."
    "Though in recent years the idea has crossed my mind, and well, she's clearly thought of it for a while..."
    "I know I care about Sayori..."
    "And we know each other like the back of our hand..."
    "And I'm pretty sure she still loves me..."
    "But would she believe me if I told her I changed my mind?"


    if hangout3 == "Sayori":
        "I mean...{w=0.38}earlier she acted like the girl I always knew..."
        "Her trying to grab my ice cream was so typical of her..."
        "And it's nice that she's still able to act like her old self around me..."

        if sayori_ice == True:
            "I mean I did indulge her and let her take my ice cream from me..."

        if sayori_ice == False:
            "Even though I didn't let her have my ice cream, the episode still was a little fun, even if she felt otherwise..."

    if hangout3 == "Natsuki" or hangout3 == "Monika" or hangout3 == "Yuri":
        "I mean...{w=0.38}I don't even know where to begin on that..."
        "Spending time with [hangout3] was pretty fun, and I haven't really had the chance to talk to her recently..."
        "It kind of opened my eyes that I do have other possibilities..."
        "Even though I know [poem_giver] already likes me..."
        "Hanging out with [hangout3] was something else..."
        "Even though I didn't expect for it to go the way that it did..."

        if hangout3 == "Natsuki":
            "And what Natsuki told me about her homelife still has me worried..."

        if hangout3 == "Yuri":
            "And what I may have seen on Yuri's wrists has me worried for her safety..."

        if hangout3 == "Monika":
            "I did not think that Monika would ever show me that much attention..."
            "Though she has been helping me through this situation all day today..."

        "But I don't know if I can really go for them without hurting Sayori even more..."



    "Even though I've been trying to make it up to Sayori over the last few days, I know I've still let her let down these last few years."
    "And nothing I do can make up for that."
    "But, she does deserve to have someone that cares about her and who'll support her..."
    "So, in what way can I best do that?"
    "Can I really see Sayori as my girlfriend?"
    "I mean...{w=0.38}it could work out..."
    "We already take care and look after each other..."
    "We both care about each other deeply..."
    "She's never shyed away from being there for me when I needed it, and I'm trying to do the same for her."
    "I mean...{w=0.38}maybe we can give it a chance and see how it works out..."
    "But that would mean I'd have to break [poem_giver]'s heart..."
    "And I'd rather not break two hearts in two weeks..."
    "But is my interest in [poem_giver] the same as it was when I first joined?"
    "I guess at one point, I did have similar feelings for [poem_giver]."
    "Especially with how last Sunday went..."
    "And I've enjoyed spending time around her, she's really fun to be around..."
    "She was a blast to hang around during the festival..."
    "But if I give [poem_giver] a chance, how would Sayori feel?"
    "I mean...{w=0.38}I did reject her with [poem_giver] on my mind..."
    "I roll over to face my bookshelves."
    "On one of the shelves, I spot a picture of me and Sayori at the carnival."
    "Man...{w=0.38}that must've been at least ten years ago..."
    "Do I really have it in me to tell her, that same girl, that I want to give her a chance at a relationship that's not even guaranteed to work out?"
    "And risk hurting [poem_giver]?"
    "I get out of my bed and walk over to pick up the picture frame."
    "Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
    "Huh...{w=0.38}I almost forgot that's when I won it for her..."
    "I always did tell Sayori that she deserved the best..."


if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."


    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2



if hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask

if hangout3 == "Monika":
    "But am I what she needs?"
    "Am I what she deserves?"
    "..."
    "Agh! This is hopeless!"
    "I don't know anything! How am I supposed to decide this when the girl I've always fantasized about being with now possibly likes me?!?"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask


label s_hangout_ask:

"I answer the phone."
mc "Sayori?"
s "Heyyyy, [player]!"
mc "Why are you calling? Didn't we see each other like ten minutes ago?"
s "Yeah...{w=0.38}but..."
mc "'But' what?"
s "I'm hungry..."
mc "Well make yourself some food..."
s "I don't have anything..."
mc "Then get takeout..."
s "[player], you know I don't have a car!"
"I facepalm myself."
"This girl..."
mc "Sayori, you don't need a car for takeout, you can just order it over the phone or online or however it's done now..."
s "I don't know any of the restaurant numbers..."
mc "Well can't you look it up online?"
s "Too lazy~"
"I laugh a little to myself."
"I see what she's trying to do..."
"Still, I'll have a little fun with her..."
mc "Well, I guess you're just gonna have to starve Sayori..."
s "Hey, you're a big meanie!"

if encore_sayoriquestion_1 == True:
    s "Don't you have anything to help your poor, starving girlfriend?"

if encore_sayoriquestion_1 == False:
    s "Don't you have anything to help your poor, starving friend?"

mc "Actually let me check..."
"I walk downstairs to my kitchen."
scene bg kitchen
with wipeleft_scene
"As soon as I get into the kitchen I open my fridge."
"Wow...{w=0.38}looks like Sayori and I are in the same predicament..."
"How did I not see it this morning?"
s "See anything?"
mc "Looks like I'm out of food too..."
s "Wow..."
mc "You didn't break into my house and steal all my food, did you?"
s "What? No! [player], don't be silly!"
mc "I'm just saying...{w=0.38}if it happened, you'd be the prime suspect!"
"I hear Sayori giggling through on the other end of the line."
s "Well I do have this ski mask..."
mc "You're not robbing my house..."
mc "And why do you have a ski mask?"
s "You don't remember the sixth grade field trip to that mountain?"
mc "No..."
s "Oh wait! I think you were sick that time..."
mc "Well that probably explains why I wouldn't remember it..."
s "Yeah, it would!"
s "Well, if you're not too busy...{w=0.38}we could get some food together if you want..."
"The idea of getting food with Sayori is tempting..."
"But I don't know if I really want to leave the house considering I got some heavy-duty thinking to do..."
"Not to mention I could use the early start on my homework..."

menu:
    "Should I get food with Sayori?"
    "Yes":
        $ sayori_hangout = True
        jump s_food
    "No":
        $ sayori_hangout = False
        jump s_no_food


label s_food:

mc "Yeah, sure! I wouldn't mind going out."

if encore_sayoriquestion_1 == True:
    mc "I mean...{w=0.38}it's not like we had a proper first date yet..."

if encore_sayoriquestion_1 == False:
    mc "I'm kind of getting hungry myself..."

s "I'm not taking you away from anything, am I?"
mc "No, and to be honest I probably could use the fresh air..."
s "Okay..."
s "Well we're not going anywhere super fancy, but I did have one place in mind..."
s "It's in the city."
mc "Sounds fancy to me."
s "It's not really anything super, it's more of a fast food place..."
mc "Hey, I don't mind!"
mc "Food is food!"
mc "It's not like I have a preference right now."
s "Yeah...{w=0.38}me neither..."
mc "I'll meet you outside in a few minutes, okay?"
s "Alright! See you in a bit!"
mc "Bye!"
"Sayori disconnects the call."
"I'm fairly surprised that Sayori wants to go out..."
"We haven't gone out to eat together in years..."
"Although, I'm more than happy to take her up on her offer..."
"All this thinking does work up quite an appetite..."

if sayori_ice == True:
    "Hopefully she doesn't try to take my food again..."

if sayori_ice == False:
    "Hopefully we can avoid another mishap like earlier..."

"I grab my keys and wallet and walk out of my house to meet Sayori."
jump sencore_4

label s_no_food:

mc "Sayori...{w=0.38}I appreciate the offer, but I think I'll just stay in tonight..."
mc "I don't really feel like going out right now..."
s "Do you want me to come over?"
mc "No, no, it's fine..."
mc "I'm just deep in thought right now..."
"I hear Sayori sigh."
s "Okay...{w=0.38}just try not to overthink..."
mc "I'll try my best..."
"There's a long, uncomfortable pause between us as my guilt for refusing to hangout with Sayori starts to kick in."
"Though I can't exactly turn back now..."
mc "I'll...{w=0.38}see you tomorrow, okay?"
s "Alright..."
s "Just let me know if you need anything."
mc "I will."
s "Bye."
mc "Bye."
"I disconnect the call."
"I don't know if I should've turned her down there..."
"It sounded like she really wanted to go out with me..."
"Well, at least on the flip side, I can quietly assess my relationship with her."

if encore_sayoriquestion_1 == True:
    "And try to decide if I should stay with her or give [poem_giver] a chance."
    "Not to mention, there are other options..."

if encore_sayoriquestion_1 == False:
    "And how I feel about her."

"Though I quickly find myself overwhelmed by all my emotions."
"Maybe I can find some homework to do..."
"That should ease my mind off of this for a little while..."
"I get up from my bed and dig out my homework stash from my backpack."
"Well, at least I'm doing something productive..."
"I sit down at my desk and begin reading over the questions."
scene black
with close_eyes
jump day3_night

########Natsuki#############

label n_mono1:

    "I know I love Sayori."
    "I do..."
    "I've enjoyed every moment I've been around her..."
    "Even if she's a bit much to handle at times..."
    "But...{w=0.38}I can't help myself from feeling attracted to Natsuki..."

    if encore_festivalquestion_2 == "Natsuki":
        "Ever since last Sunday, I've felt myself wanting her more and more..."

    if encore_festivalquestion_2 == "Yuri":
        "Even though we haven't spent much time around each other, I feel like we've really bonded over the last recently..."

    "She's truly been wonderful to be around!"
    "Even though she came off to me initially as someone with an attitude problem, she isn't really all that bad once you get to know her..."
    "And well, recently, I can definitely say I've felt closer to her than ever before..."
    "It's clear she feels the same way..."
    "And even though I want to avoid her until I can figure out what to say to her, I did have some fun spending time around [hangout3] today..."

    if hangout3 == "Yuri":
        "Even though it took a rather serious turn..."

    if hangout3 == "Monika":
        "Even though I didn't expect Monika and I to end up flirting like that..."

    if hangout3 == "Sayori":
        "I think I've undid some of the damage I've done recently to our relationship..."


    "All things considered, I think Natsuki truly appreciates that there's someone out there who takes her seriously..."
    "Who shares the same interests and hobbies as her..."
    "It's quite amazing how we were able to bond over manga..."
    "Finding a girl who likes manga more than you is pretty rare..."
    "Not to mention, I'm pretty sure Natsuki also appreciates having someone who cares about her and her opinions and doesn't take everything she does and says at face value..."
    "Even if it's still a little hard to understand what she's doing at times..."
    "I always know she means well..."
    "And I've had a blast spending every moment I can around her."
    "Her laughter, her smile, she's never been boring to hang around..."
    "And she always looks cute 24/7, even if she won't admit it!"
    "I think she enjoys spending time around me too..."
    "Even without her poem, I was starting to suspect that she liked me..."
    "I mean the signs were there..."

    if encore_festivalquestion_2 == "Natsuki":

        if hangout2 == "Natsuki":
            "We almost kissed a few times on Sunday..."
            "She even hugged me yesterday..."
            "And she really did want to spend more time around me today..."
            "I really enjoyed her hug yesterday..."

        else:

            "She's been adamant about us trying to spend time together..."
            "But would it be bad to give her a chance?"

    if encore_festivalquestion_2 == "Yuri":

        if hangout2 == "Natsuki":
            "She hugged me yesterday and told me she wanted us to spend more time like this..."
            "And she really did want to spend more time around me today..."
            "I really enjoyed her hug yesterday..."

        else:

            "She's been adamant about us trying to spend time together..."
            "But would it be bad to give her a chance?"



    "*sighs*"
    "I know that this is all wrong..."
    "By thinking like this, I'm really risking betraying my relationship with Sayori..."
    "Only she should be able to hug me like that..."
    "She was rightfully pissed at me yesterday for it..."
    "And if she found out we did it again, especially when I promised to stop doing it, Sayori would be heartbroken..."
    "God...{w=0.38}why am I so bad at this?!?!"
    "I throw my hands over my face."
    "I love Sayori...{w=0.38}but I'm pretty sure I've caught feelings for Natsuki too..."
    "And what makes this complicated is that Natsuki likes me back too!"
    "I'm in a literal love triangle..."
    "And I don't want to hurt either of them..."
    "I already know they both have serious problems, and I don't want to add on to anything..."
    "But if I do decide that I want to be with Natsuki...{w=0.38}I'd have to breakup with Sayori..."
    "And that would be easier said than done...{w=0.38}and I don't know if that's what I want to do..."
    "I've known her for fourteen years...{w=0.38}and I know she'd never do the same to me!"
    "And we're both still trying to make this work..."
    "But...{w=0.38}maybe she and I aren't really meant to be?"
    "I mean...{w=0.38}lately I've been more interested in Natsuki than Sayori..."
    "And though it's my fault completely for our relationship starting to deteriorate...{w=0.38}I just don't have the same passion for her as I do for Natsuki..."

    if encore_festivalquestion_2 == "Natsuki":
        "Especially with how last Sunday went..."

    if encore_festivalquestion_2 == "Yuri":
        "I still can't help but feel sorry for Yuri..."
        "I mean, granted we haven't talked much since Sunday."
        "We only did share a few relatively intimate moments with each other, though nothing became of it..."
        "And I still find part of me wondering if what could've been...{w=0.38}still could be..."


    "Especially considering how much fun I had with her preparing for and at the festival..."
    "Even if she was competing with Sayori for my attention..."
    "But...{w=0.38}can I really do that to Sayori?"
    "I roll over to face my bookshelves."
    "On one of the shelves, I spot a picture of me and Sayori at the carnival."
    "Man...{w=0.38}that must've been at least ten years ago..."
    "Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
    "And risk possibly ending the club?"
    "I get out of my bed and walk over to pick up the picture frame."
    "Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
    "Huh...{w=0.38}I almost forgot that's when I won it for her..."
    "I always did tell Sayori that she deserved the best..."


if hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

if hangout3 == "Monika":
    "But am I what she needs?"
    "Am I what she deserves?"
    "..."
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask


if hangout3 == "Yuri":

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask


label n_mono2:

"I really do think that I'm falling for Natsuki..."

if encore_festivalquestion_2 == "Natsuki":
    "Having spent the last two weeks getting to know her has truly been something..."

if encore_festivalquestion_2 == "Yuri":
    "Having spent the last few days getting to know her has truly been something..."

"It's truly amazing how far we've come in such a relatively short amount of time..."
"At first I thought she hated me, but now it's like we've been friends our whole lives!"
"I even think I'm even getting used to her teasing..."
"And she's clearly able to deal with my quirks now as well."
"I didn't know it at the time, but I didn't think we'd be able to get along as well as we do now."
"Considering she wasn't all that welcoming when I first joined..."
"But now that I know her and what she's like, almost everything I know about her makes sense."
"For the first time, I feel like I truly understand Natsuki..."


if hangout3 == "Sayori":
    "But spending time with Sayori earlier really allowed me to reconnect with her a little..."
    "Us squabbling over my ice cream kind of reminded me of all the fun times we had when were kids..."
    "Back when life was simple, when we didn't have to deal with all these complicated feelings..."
    "I still care about her, even if we haven't spent as much time together as I would've liked too..."

    if sayori_ice == True:
        "I'm glad that for once, I managed to make her day..."

    if sayori_ice == False:
        "Even though I didn't let her have my ice cream, the episode still was a little fun, even if she felt otherwise..."

    "It's good to see that she's still able to act like her old self around me..."
    "And even though I still agonize over what happened last Sunday, I know I rejected her initially with [encore_festivalquestion_2] on my mind..."
    "But maybe I made a mistake..."
    "Maybe if I spent more time with Sayori, maybe I'd see in her what she sees in me..."
    "But I don't know if that opportunity is still there anymore, especially since I've really gotten to know Natsuki recently..."
    "And I still need to figure out what to say to [poem_giver]..."
    "My feelings for all three of them are so mixed up!"
    "And I know I can't be with all three of them..."
    "Heck, I don't even know if I should entertain the possibility of being with Sayori, given her current state..."
    "But when she hopefully gets better...{w=0.38}who knows..."
    "But can I really let down Natsuki and Yuri?"



if hangout3 == "Natsuki":

    if natsuki_continued_hug == True:
        jump n_line_3

    if natsuki_continued_hug == False:
        jump n_line_4

    if natsuki_hug == True:
        jump n_line_3

    if natsuki_hug == False:
        jump n_line_4


label n_line_3:

"And with what she told me earlier today, I'm just worried about her."
"I know she just puts on the act to try to be taken seriously at school, but at home, who knows..."
"After all she only gave me a 'summary'."
"Well if I do know her, she's a strong person, and I'm hopeful she won't need me to try to step in and help her resolve her homelife..."
"But, I think Natsuki truly appreciates that there's someone out there who takes her seriously..."
"Who shares the same interests and hobbies as her..."
"And who cares about her and her opinions and doesn't take everything she does and says at face value..."
"Even if it's still a little hard to understand what she's doing at times..."
"I always know she means well..."
"And I've had a blast spending every moment I could around her."
"Her laugh, her smiles, she's never been boring to hang around..."
"And I think she enjoys spending time around me too..."
"It's almost like we're a perfect match..."
"And I have a pretty good reason to believe she likes me back..."
"For the past two days she's been hugging me..."
"And each time...{w=0.38}it felt almost magical..."
jump n_continued

label n_line_4:

"Even though I was an idiot and messed up earlier..."

if natsuki_hug == False:
    "I should've taken the chance to hug her back..."

if natsuki_continued_hug == False:
    "I should've let her keep hugging me..."

"But I don't think she'd stay mad..."
jump n_continued

label n_continued:

"All things considered, I do think I want to go for Natsuki..."
"But the problem is, I know that in doing so, I'd be breaking Yuri's heart..."
"And possibly causing Sayori even more anguish..."
"I just don't know if the timing is right..."
"Maybe once Sayori is in better shape, and I feel like I have a proper way of rejecting Yuri, then maybe I can figure out how to talk to Natsuki about all this..."
"But then again, do I really need to wait for that?"
"Rebuilding my friendship with Sayori is going to take time either way..."
"And well, I'd like to think we've established that we're going to remain friends, nothing more or less..."
"Even though the possibility to go for more is still there..."
"But I just don't think I have the same connection with Sayori like I do for Natsuki..."
"Same goes for Yuri too I guess..."


if hangout3 == "Monika":
    "But...{w=0.38}I also feel like I'm starting to really get to know Monika better..."
    "What happened earlier with her really surprised me..."
    "In fact, Monika has been nothing but full of surprises today..."
    "I'm glad she was able to calm me down and reassure me of everything during lunch..."
    "Even if she was a little too kind to me in the music room..."
    "If it wasn't for her help today, I'd probably still be a nervous wreck..."
    "Well, I'd be more of a nervous wreck if it wasn't for her..."
    "I can't deny that I've always liked Monika..."
    "But I thought she was out of my league..."
    "And earlier...{w=0.38}she clearly had no problems flirting with me..."
    "But, I know I was being a little disloyal at best to Natsuki, given the stage we're at..."
    "I can't really give Monika a chance at this point in time, can I?"
    "I know I have feelings for Natsuki..."
    "And I do feel bad that I haven't spent time with [poem_giver] recently..."
    "Top it off with my regret for how I've been handling my friendship with Sayori lately..."
    "I did tell her that I wanted to spend more time with her, like how we used to..."
    "But once again I failed to deliver..."
    "But can I give everyone a chance at this point?"



if encore_festivalquestion_2 == "Natsuki":
    "I mean, maybe I could give Yuri a chance and see if we have any real chemistry..."
    "But from the times I've interacted with her, maybe it's just not there..."


if encore_festivalquestion_2 == "Yuri":
    "I mean, maybe I could give Yuri another chance..."
    "We did have a good thing going for a while..."
    "But...{w=0.38}I guess my feelings for her have just kind of faded for her recently..."

"Considering how Yuri tends to put a lot of emotion into things, I don't think she'd react too well if I rejected her..."
"Breaking two hearts wouldn't exactly sit well with my sub-conscious..."
"But, if I do go for Yuri, then Natsuki would be left out..."
"Basically, no matter what, if one of them gets chosen, the other gets the heartbreak..."
"And I don't know if I'm ready to do that again..."
"I sigh as I pull up my phone and scroll through my picture gallery."


if encore_festivalquestion_2 == "Natsuki":
    "As I'm scrolling, I come across some pictures I took with Natsuki at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "It's funny how most of these photos were her idea..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even wrapping her arm around me."
    "Huh...{w=0.38}I guess we would make a good couple..."

if encore_festivalquestion_2 == "Yuri":
    "As I'm scrolling, I come across some pictures I took with Yuri at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "I'm surprised she even agreed to do them with me..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even letting me wrap my arm around her."
    "Maybe we would make a good couple..."


if hangout3 == "Natsuki" or hangout3 == "Sayori":
    play music e17
    "Suddenly, my phone begins to ring."

if hangout3 == "Monika":
    "But, can I really make that decision based off of pictures?"
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I get off my bed, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."

    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2


label n_hangout_ask:

n "You're not busy right now, are you?"
mc "Eh, not really, why?"
n "So, I just found out that a new edition of Parfait Girls came out, and I was wondering if you wanted to come with me to the bookstore..."
mc "Right now?"
n "When else, dummy?"
n "And we don't have long before the store closes so..."
n "You better hurry up and decide if you want to come along!"
n "We'll have to leave soon before the store closes. If you want, I can meet you on the way."
"The idea of hanging out some more with Natsuki is tempting..."
"I could use this opportunity to get a better feel for Natsuki's home life and hopefully put my anxiety over the subject to rest..."
"But I don't know if I really want to leave the house considering I got some heavy-duty thinking to do..."
"Not to mention I could use the early start on my homework..."



menu:
    "Should I hangout with Natsuki?"
    "Yes.":
        $ natsuki_hangout = True
        jump n_hangout
    "No.":
        $ natsuki_hangout = False
        jump n_no_hangout

label n_hangout:

mc "Yeah, sure! I'd love to go with you!"
n "Wow, really?!?"
mc "Yeah...{w=0.38}I could use some fresh air right now anyways..."
n "Don't worry, you'll be getting plenty if we don't leave like right now..."
n "They're apparently selling them left and right..."
mc "I guess this release was well advertised..."
mc "Where should I meet you?"
n "The bookstore is past the school, so we can probably meet there."
mc "Well good news for us is that the school's not terribly far from me. I can probably make it in there in ten minutes."
n "That's pretty much how long it'll take me to get there by bus!"
mc "Perfect! I'll see you then!"
n "Laters!"
"Natsuki promptly hangs up the call."
"Well, I know better than to keep her waiting."
"I quickly grab my wallet and keys and start speed walking back to school."
jump nencore_4


label n_no_hangout:

mc "I appreciate the offer, but, I kinda wanna be alone right now..."
n "Everything okay?"
mc "Y-{w=0.38}yeah, it's just, I'm thinking of some life-related things over."
n "Sounds boring."
mc "It's not exciting, but, it needs to be done..."
n "It's alright, [player]..."
n "I understand..."
"Even through the phone, I can sense Natsuki's disappointment."
"I should make it up to her somehow..."
mc "Hey, if they still have it, I'd love to read it with you sometime..."
mc "Once I get caught up with everything."
n "I know..."
"There's a long, awkward pause between us."
mc "Well, I don't want to keep you waiting or anything..."
mc "I imagine there's a pretty big line for it."
n "Yeah...{w=0.38}probably..."
n "I'll let you know if I find it."
mc "Alright, talk to you later."
"Natsuki promptly disconnects the call."
"I sigh as I lay back on my bed and throw my hands over my face."
"Maybe I should've taken the chance to go with her..."
"She did sound like she really wanted me to go..."
"But with how I'm feeling towards her and the others...{w=0.38}I don't know if I want to risk something happening between us prematurely..."
"Especially since I need to still sort out my feelings for Yuri..."

if encore_sayoriquestion_1 == True:
    "And if I really want to end things with Sayori..."

if encore_sayoriquestion_1 == False:
    "And if I really want to commit myself to someone right now..."


"Well, maybe doing my homework will help ease my mind..."
"I get up from my bed and dig out my homework stash from my backpack."
"Hopefully this will keep me distracted for the rest of the night..."
"I sit down at my desk and begin reading over the questions."
scene black
with close_eyes
jump day3_night





########Monika#############

label m_mono1:

"I know I love Sayori."
"I do..."
"I've enjoyed every moment I've been around her..."
"Even if she's a bit much to handle at times..."
"But...{w=0.38}I can't help myself from feeling attracted to Monika..."
"Even though we've just recently started talking to each other..."
"I'm still dumbfounded by how easy it's been to talk to her!"
"Not to mention she's been incredibly helpful with giving advice through this situation..."
"However, she has been rather forward with me lately..."

if hangout3 == "Monika":
    "The last two days we have gotten rather close..."
    "As much as I do enjoy when Monika is like that with me...{w=0.38}it still doesn't change the fact it's wrong..."
    "Even though I told her that we probably shouldn't be doing that anymore, she's still been doing it..."
    "But I don't know if I want to put my foot down and tell her to stop."
    "I mean...{w=0.38}even though Sayori has shown me affection before, Monika seems like the kind of girl who'd shower me in it..."
    "Heck...{w=0.38}she's everything that any guy would want:{w=0.38}smart, sweet, funny, athletic..."
    "And drop dead beautiful!"
    "Though at the same time...{w=0.38}she's the kind of girl that's too good for me..."
    "Why would she be interested in someone like me? It's not like I'm anything special..."
    "And I haven't known her nearly as long as Sayori..."
    "I mean practically speaking...{w=0.38}it makes sense for me to have gotten with Sayori in the first place..."
    "But Monika...{w=0.38}it's completely unexpected!"
    "Oh well, if Monika does indeed like me, and she isn't trying to tease me or anything like that, then I should be grateful that she does..."
    "But that does pose a problem:{w=0.38}if I do decide that I want to be with Monika...{w=0.38}I'd have to breakup with Sayori..."
    "And that would be easier said than done...{w=0.38}and I don't know if that's what I want to do..."

if hangout3 == "Sayori":
    "But I've tried to make it up to Sayori..."
    "I know I royally screwed up yesterday by getting so close to Monika..."
    "And she did seem grateful that I finally spent some time around her in the club..."
    "In fact, spending time with Sayori earlier really allowed me to reconnect with her a little..."
    "Us squabbling over my ice cream kind of reminded me of all the fun times we had when were kids..."
    "Back when life was simpler..."
    "I still care about her...{w=0.38}I know I still love her...{w=0.38}even if I haven't been around her enough..."

    if sayori_ice == True:
        "I'm glad that for once, I managed to make her day..."

    if sayori_ice == False:
        "Even though I didn't let her have my ice cream, the episode still was a little fun, even if she felt otherwise..."

    "But is my relationship with Sayori even salvageable?"
    "She still acted a little distant from me on the walk home..."
    "And she has every right to be mad at me..."
    "But I never even expected for Monika to show me that much attention!"
    "In fact, I'm just surprised she was willing to talk to me in the first place..."
    "And if Monika does like me, it's a plus and a minus for me..."
    "But then I'd have to risk breaking another heart since I already know [poem_giver] likes me..."
    "I really don't feel comfortable of going back on my word to Sayori..."
    "I don't want to break up with her, I really do want to stay with her..."


if hangout3 == "Natsuki":
    "And she hasn't been the only one..."
    "I didn't expect for Natsuki to hug me earlier..."
    "Or tell me about her homelife..."

    if natsuki_continued_hug == True:
        jump n_line_5

    if natsuki_continued_hug == False:
        jump n_line_6

    if natsuki_hug == True:
        jump n_line_5

    if natsuki_hug == False:
        jump n_line_6


label n_line_5:

"Even though I chose to hug her back, I really still question if I made the right decision there..."
"I mean, I may have helped Natsuki in the moment, sure..."
"But what would've Sayori said? Would she have approved?"
"And what would've Yuri or Monika have said had she seen us like that?"
"I sigh to myself."
"I don't want to risk hurting my relationship with Sayori..."
"And I feel bad that I'm only growing more distant from Yuri..."
"But lately I've felt myself gravitating to Monika, and now I'm suddenly seriously interested in Natsuki..."
"Even though we haven't talked much recently..."
"Is it right for me to give them a chance?"
"How much can I live with myself going behind Sayori's back like this?"


label n_line_6:

"Even though I think I made the right decision by not returning it, I can't help but feel sorry for Natsuki..."
"She put herself out there to me in that moment...{w=0.38}and she felt hurt because I didn't return it..."
"She probably hasn't had anyone show her any serious level of interest or care in a while, if ever..."
"Maybe I didn't make the right call there..."
"But I don't want to risk hurting my relationship with Sayori..."
"And I feel bad that I'm only growing more distant from Yuri..."
"But lately I've felt myself gravitating to Monika, and now I'm suddenly seriously interested in Natsuki..."
"Even though we haven't talked much recently..."
"Should I give them a chance?"
"How much can I live with myself going behind Sayori's back like this?"



if hangout3 == "Yuri":
    "And speaking with forwardness...{w=0.38}I really messed up with Yuri earlier..."
    "I don't think I should've so aggressively pushed her to tell me about her wrists..."
    "But even then...{w=0.38}I think I like her..."

    if tell_monika == True:
        "Well, at least I care enough about her to have at least told Monika about what I think I saw..."
        "And I still worry for her safety, and I want her to be okay..."

    if tell_monika == False:
        "Well, at least I care enough about her to cover for her..."
        "But, I don't know if I'm doing anyone good there..."

    "Part of me has always wanted to get to know Yuri, but I've just never had much luck due to her reclusive nature..."
    "I know it's not right for me to risk my relationship with Sayori for her..."
    "And I've really grown distant from Natsuki lately..."
    "I sigh to myself."
    "Can I even give them a chance at this point?"
    "How much more should I be risking my relationship with Sayori to get closer with the others?"





"I've known her for fourteen years...{w=0.38}and I know she'd never want to hurt me!"
"We're both still trying to make this work..."
"There's nothing about Sayori that I don't like..."
"She's fun, she's beautiful, and she's always been there for me..."
"But...{w=0.38}maybe she and I aren't really meant to be?"
"I mean...{w=0.38}lately I've been more interested in Monika than Sayori..."
"And though it's my fault completely for our relationship starting to deteriorate...{w=0.38}I just don't have the same passion for her as I do for Monika..."
"Making this even more complicated is that I know [poem_giver] waiting for my response..."
"I'm sure at some point I had similar feelings for [poem_giver] like she does for me..."
"Especially with how last Sunday went..."
"And I still find part of me wondering if what could've been...{w=0.38}still could be..."
"Especially considering how much fun I had with her preparing for and at the festival..."
"Even if she was competing with Sayori for my attention..."
"But...{w=0.38}can I really do that to Sayori?"
"I roll over to face my bookshelves."
"On one of the shelves, I spot a picture of me and Sayori at the carnival."
"Man...{w=0.38}that must've been at least ten years ago..."
"Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
"And risk possibly ending the club?"
"I get out of my bed and walk over to pick up the picture frame."
"Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
"Huh...{w=0.38}I almost forgot that's when I won it for her..."
"I always did tell Sayori that she deserved the best..."
"My hand starts to shake as tears start to swell up in my eyes."
"Could I really do it?"
"Is it even right to think this way?"
"No matter who I choose...{w=0.38}someone's getting heartbroken because of me..."



if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."

    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2


if hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask

if hangout3 == "Monika":
    "Am I what she needs?"
    "Am I what she deserves?"
    "..."
    "Agh! This is hopeless!"
    "I don't know anything! How am I supposed to decide this when the girl I've always fantasized about being with now possibly likes me?!?"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask





label m_mono2:

"I mean...{w=0.38}I've always liked Monika..."
"But I never seriously went after her because I thought I would've tried and failed like everyone else has..."
"That was until recently when I decided to finally start talking to her."
"And it's amazing how well things have went for us since then!"
"Not even I thought she and I would connect so easily..."
"I guess that's what happens when you just man up and start talking to someone..."

if hangout3 == "Monika":
    "It's crazy how close we've gotten in such a short amount of time..."
    "Still, I'm not sure what Monika really sees in me..."
    jump m_converge

if hangout3 == "Natsuki":
    "Like earlier with Natsuki, I wasn't expecting her to hug me like that..."

    if natsuki_continued_hug == True:
        jump n_line_7

    if natsuki_continued_hug == False:
        jump n_line_8

    if natsuki_hug == True:
        jump n_line_7

    if natsuki_hug == False:
        jump n_line_8

label n_line_7:

"Neither did I expect her to tell me about her home life..."
"It's got me worried for her safety, even though I haven't known her that long..."
"I still care about her..."
"But does she like me back in the same way Monika does?"
jump m_converge


label n_line_8:
"Even though she ended up blowing up at me later..."
"I still want to get to know her more, even if we haven't really talked that much recently..."
"I do care about her..."
"But does she like me back in the same way Monika does?"
jump m_converge

if hangout3 == "Sayori":
    "And I had a surprisingly good time with Sayori earlier as well..."
    "Us squabbling over my ice cream kind of reminded me of all the fun times we had when were kids..."
    "Back when life was simple, when we didn't have to deal with all these complicated feelings..."
    "I still care about her, even if we haven't spent as much time together as I would've liked too..."

    if sayori_ice == True:
        "I'm glad that for once, I managed to make her day..."

    if sayori_ice == False:
        "Even though I didn't let her have my ice cream, the episode still was a little fun, even if she felt otherwise..."

    "It's good to see that she's still able to act like her old self around me..."
    "And even though I still agonize over what happened last Sunday, I know I rejected her initially with [encore_festivalquestion_2] on my mind..."
    "But maybe I made a mistake..."
    "Maybe if I spent more time with Sayori, maybe I'd see in her what she sees in me..."
    "I know she loves me..."
    "But for some reason, I just find myself more attracted to Monika right now..."
    jump m_converge

if hangout3 == "Yuri":
    "But...{w=0.38}I really messed up with Yuri earlier..."
    "I don't think I should've so aggressively pushed her to tell me about her wrists..."
    "But even then...{w=0.38}I think I like her..."

    if tell_monika == True:
        "Well, at least I care enough about her to have at least told Monika about what I think I saw..."
        "And I still worry for her safety, and I want her to be okay..."

    if tell_monika == False:
        "Well, at least I care enough about her to cover for her..."
        "But, I don't know if I'm doing anyone good there..."

    "I mean I guess I do like her, but do I like her in the same way I like Monika?"
    jump m_converge


label m_converge:

"Heck, I don't know even know why Monika likes me..."
"I mean, what's special about me?"
"I'm not doing any sports, I'm definitely not the smartest guy in the class..."
"I'm not terribly funny nor talented..."
"Why would Monika like me, literally the most average of the average?"
"Maybe it's one of those things where you don't understand it but you just roll with it anyways."
"I feel like that might be one of those times..."
"Man if I got with Monika, I'd probably be crowned king of the school or something!"
"Every guy would probably hate me though, but being with Monika easily outweighs any of that..."
"And speaking of outweighing..."
"I know that if I do somehow end up getting with Monika, I'd have to break [poem_giver]'s heart..."
"And I'd be breaking Sayori's heart even more..."
"I should also ask myself if it's really worth to scuttle what I had with [encore_festivalquestion_2]..."
"I mean...{w=0.38}we did have a pretty good thing going for a while..."
"And she's been fun to hang around, and I'd feel bad if [encore_festivalquestion_2] felt like I was leading her on..."
"Especially given what happened last Sunday between us..."
"And since then she's been trying to spend more time with me, but I've been too busy hanging out with Monika..."
"Ah, this is gonna suck..."
"But, I also genuinely like Monika..."
"She's really helped me out with everything..."
"From getting me integrated into the club and helping me out with this..."
"And she's every guy's dream girl..."
"It'd be a too good of an opportunity to pass up if she truly likes me back..."
"And I think the signs are there, like how she got so close to me yesterday and today..."
"Not to mention, if I did reject her for [encore_festivalquestion_2], how would she feel?"
"Looks like no matter what I do, I'm going to have to hurt someone..."
"And what sucks is that Sayori's pretty much going to be hurt regardless, unless I decide to change my mind on her..."
"But I just don't think I have the same level of enthusiasm of being a couple with her as she does..."
"The funny thing is though...{w=0.38}I could see myself with any of them..."

if encore_festivalquestion_2 == "Natsuki":
    "Even Yuri...{w=0.38}even though we've rarely talked and she likely has zero interest in me..."

if encore_festivalquestion_2 == "Yuri":
    "Even Natsuki...{w=0.38}even though we've rarely talked and she likely has no interest in me..."



if hangout3 == "Natsuki" or hangout3 == "Sayori" or hangout3 == "Yuri":
    play music e17
    "Suddenly, my phone begins to ring."
    "I pull out my phone out of my pocket to see who's calling me."


if hangout3 == "Sayori":
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."

    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2




if hangout3 == "Yuri":

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask


if hangout3 == "Monika":
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I get off my bed, grab my keys and walk out of my house."
    jump m_hangout_ask






label m_hangout_ask:

scene bg residential_day
with wipeleft_scene
"As soon as I step out of my house, I'm greeted by a nice, gentle breeze in my face."
"Off in the distance I can hear the birds chirping the same song I've heard hundreds if not thousands of times."
"I look up to see the sky almost cloud free, and better yet, the sun hasn't even started to set."
"I should be able to do a walk around the neighborhood and get back before dark..."
play sound gust
"I take another few steps out onto the sidewalk when a strong gust of wind comes hurling at me, forcing me to shield my eyes."
"Well, that certainly came out of nowhere..."
$ m_name = "???"
m "[player]?"
play music e2 fadein 2.0
show monika 1bd at t11 zorder 1
"I turn around to see Monika standing right behind me."
mc "Monika?!?"
$ m_name = "Monika"
show monika 3bl  at t11 zorder 1
m "Well this is a surprise!"
show monika 3bb  at t11 zorder 1
m "I didn't know you lived here!"
show monika 1ba at t11 zorder 1
mc "Yeah...{w=0.38}my house is just right over there."
"I point out my house to Monika."
show monika 1bb at t11 zorder 1
m "Nice house, [player]!"
show monika 1ba at t11 zorder 1
mc "Ah, it's alright. It's nothing too special."
mc "Anyways, I didn't know you lived around here! I thought you lived on the other side of town in the Swan District..."
show monika 2be  at t11 zorder 1
m "Oh, I still live there, I just took the bus to get over here."
"Figures she would still live there. The Swan district is where all the rich people in our surrounding area live who don't want to live in the city."
"There's some incredibly gorgeous houses over there, though it's not something most families like mine would ever be able to afford considering everything is pretty much gated..."
"Considering Monika's family is pretty well off, it doesn't surprise me that she lives there."
mc "Oh! Well what brought you all the way over here?"
mc "Are you visiting Sayori?"
"I point to Sayori's house as I ask that."
show monika 2bm  at t11 zorder 1
m "No, I was just out for a stroll..."
show monika 3bk  at t11 zorder 1
m "It's part of my exercise routine that I do a ten mile walk once a week."
show monika 3bn  at t11 zorder 1
m "And I remembered that I haven't gone this way in a while..."
show monika 3bm  at t11 zorder 1
mc "Wow...{w=0.38}a ten mile walk? You're definitely dedicated!"
show monika 1bj at t11 zorder 1
m "I always strive to stay in shape, [player]..."
show monika 5ba at t11 zorder 1
m "Mentally as well as physically."
mc "Well, now I know why you're the best!"
show mb_blush as monika at t11 zorder 1
"Monika blushes brightly at my compliment."
show monika 1bn  at t11 zorder 1
m "Well I'm glad you feel that way."
show monika 2bp  at t11 zorder 1
m "You'd be surprised at how many people at school are envious of my success..."
show monika 2be  at t11 zorder 1
m "I have my share of admirers though~"
show mb_wink as monika at t11 zorder 1
"Monika gives me a sly wink."
mc "W-{w=0.38}well hey...{w=0.38}I'm just happy for you."
mc "I mean, I'm nothing special..."
show monika 2bf  at t11 zorder 1
"Monika gives me a concerning frown."
show monika 2bg  at t11 zorder 1
m "But you are!"
show monika 2be  at t11 zorder 1
m "You may not know it, [player], but you never fail to put a smile on anyone's face."
m "You're always supportive of others...{w=0.38}always willing to hear people out."
show monika 1bm  at t11 zorder 1
m "It counts for more than you think..."
mc "Ah! Well..."
"I scratch the back of my head as I blush brightly in embarrassment."
show monika 1be  at t11 zorder 1
mc "Well...{w=0.38}that means a lot coming from you, Monika..."
mc "Thank you..."
show monika 1bk  at t11 zorder 1
m "Don't mention it!"
show monika 1bd at t11 zorder 1
mc "I mean lately, I haven't felt like that at all to be honest with you..."
mc "I've been thinking a lot about what you said..."
show monika 1bg  at t11 zorder 1
m "How's that going?"
show monika 1bf  at t11 zorder 1
mc "I still feel lost..."
mc "Like I don't know what to do..."
mc "So, I wanted to take a walk to help better clear my head..."
show monika 3be  at t11 zorder 1
m "Well, it's good you're taking some time to think to yourself..."
show monika 3bm  at t11 zorder 1
m "I do a fair share of reflection during most of my walks anyways."
show monika 1be  at t11 zorder 1
m "It really does help the thought process."
show monika 1bb at t11 zorder 1
m "I mean, you might be walking and just have a new idea just dawn on you!"
show monika 1bj at t11 zorder 1
m "It's happened to me plenty of times!"
mc "Well, if it's worked for you, it'll definitely work for me..."
show monika 2be  at t11 zorder 1
"There's a brief pause between us as another breeze gently blows past us."
"Seeing Monika's hair flow in the wind manages to mesmerize me."
show monika 2bm  at t11 zorder 1
"She looks so beautiful..."
"Her long hair flowing in the wind..."
show monika 2be  at t11 zorder 1
"Those emerald eyes gleaming brightly at me..."
"Paired with that picture-perfect smile..."
"And her dress suits her completely..."
"Matter of fact, I've never even seen Monika outside of school..."
show monika 5ba at t11 zorder 1
"I see then Monika forming her casual smirk at me."
"Apparently she must've realized I've been staring at her."
"Thankfully she doesn't seem bothered by it..."
show monika 5bc  at t11 zorder 1
m "Hey, [player]..."
show monika 5ba at t11 zorder 1
mc "Y-{w=0.38}yeah?"
"I barely manage to stammer out."
show monika 5bc  at t11 zorder 1
m "I could use a little company on this walk..."
m "My memory's rusty for this area..."
m "I could use a guide..."
show monika 5ba at t11 zorder 1
mc "Y-{w=0.38}you want me to walk with you?"
m "You know it~"
"Wow! I can't believe this!"
"Monika's asking me to walk with her!"
"This is unreal!"
stop music fadeout 2.0
"But...{w=0.38}I'm not entirely sure if I want to be around anyone right now..."
"This walk really was meant for some time by myself..."
"Especially since I'm trying to figure out if Monika is really someone I could be with!"

menu:
    "Should I walk with Monika?"
    "Yes.":
        $ monika_hangout = True
        jump m_hangout
    "No.":
        $ monika_hangout = False
        jump m_no_hangout


label m_hangout:

"Ah...{w=0.38}screw it!"
mc "Why not?"
show monika 1bj at h11 zorder 1
"Awesome!"
"Monika does a little jump in excitement."
"Which I'm surprised at, given how even tempered she usually is in school..."
"Though it could be when she's not in school, she's much more willing to let loose..."
"That or she just really likes exercising..."
"Either way, I like it..."
mc "So...{w=0.38}do you walk to some place special or do you just walk around in a giant circle?"
show monika 5ba at t11 zorder 1
"Monika lets out a giggle."
m "Just follow me~"
"Without another word spoken, Monika and I start heading eastward, which just so happens to be in the direction of the countryside..."
"Oh, I just hope she doesn't include hiking as a part of her walk..."
"In fact, I just hope I can keep up with someone of her physique in general..."
"I'm not exactly out of shape, but Monika has quite the reputation when it comes to endurance..."
"Hopefully, I don't fall behind..."
show monika at thide
hide monika
jump mencore_4

label m_no_hangout:

"I think I should just be alone right now..."
"I don't think I'm in the best state of mind to have everything on my mind and have Monika right there with me."
show monika 1bf at t11 zorder 1
mc "Look...{w=0.38}I really appreciate the offer, but..."
show monika 1br
m "It's okay, [player]...{w=0.38}I understand."
show monika 2bp
m "You're going through a lot right now and it's probably best you have some time to yourself..."
mc "Thank you..."
show monika 1bo
"Monika somberly looks off into the neighborhood."
mc "I wouldn't mind giving you directions though..."
show monika 1be
m "That would be nice..."
mc "Are you heading anywhere specifically?"
m 1bm "No, not really..."
m 3bl "Just as long as I get my ten miles in!"
mc "I see..."
show monika 1be
"I give some general directions around the neighborhood, such as where the rest of the bus stops are and the location of a few cafe's."
mc "Well, I don't think I'm forgetting anything..."
m "Thank you, [player]."
show monika 1bm
m "I hope everything works out for you..."
mc "You and me both..."
"We stand awkwardly on the sidewalk for a few moments, not sure if there's really anything left to say."
mc "Well, I guess I'll see you tomorrow then.."
show monika 2be
m "Yeah...{w=0.38}I'll see you then!"
show monika at thide
hide monika
"We wave to each other as we begin walking in opposite directions."
"Once Monika's out of earshot I let out a loud sigh."
"I don't know if I made the right move there."
"Maybe spending some time with Monika might actually help with me this whole decision making process...."
"I know I have feelings for her...{w=0.38}but at the same time I just have so much to sort out..."
"I'd probably just be a joy kill for her..."
"I guess on the flip side, I should be able to think about things a little more clearly..."
"Letting out another sigh, I continue to mindlessly walk forward with no particualr destination in mind as I try to get a handle on my emotions..."
scene black
with close_eyes
jump day3_night



########Yuri#############

label y_mono1:

"I know I love Sayori."
"I do..."
"I've enjoyed every moment I've been around her..."
"Even if she's a bit much to handle at times..."
"But...{w=0.38}I can't help myself from feeling attracted to Yuri..."

if encore_festivalquestion_2 == "Natsuki":
    "Even though we haven't spent much time around each other, I feel like we've really bonded over the last two days..."

if encore_festivalquestion_2 == "Yuri":
    "Ever since last Sunday, I've felt myself wanting her more and more..."

"And well, recently, I can definitely say I've felt closer to her than ever before..."
"It's clear she feels the same way..."
"And even though I want to avoid her until I can figure out what to say to her, I did have some fun spending time around [hangout3] today..."

if hangout3 == "Natsuki":
    "Even though it took a rather unexpected turn..."

if hangout3 == "Monika":
    "Even though I didn't expect Monika and I to end up flirting like that..."

if hangout3 == "Sayori":
    "I think I've undid some of the damage I've done recently to our relationship..."

"But, all things considered, I didn't think we'd be able to get along as well as we do now."
"Considering how shy she was and everything..."
"No matter what it is we're doing, whether it be reading, drinking tea, or just even talking, being in Yuri's presence alone is its own reward."
"Even though Yuri might think she might be boring me, I kind of like it when she goes on her little tangents..."
"She always has something interesting and insightful to say about practically anything!"
"In fact, I'm just surprised she doesn't find me boring, considering my tastes in literature is rather non-existent..."
"Hopefully, Yuri feels the same way about me as I do about her, and I think she does..."
"She's become much more relaxed around me since when we first started talking."
"Even if it did take some time to get used to each other..."
"She's never really hesitated to talk to me once we got acquainted..."
"I mean, I should've seen the signs that Yuri was into me..."


if encore_festivalquestion_2 == "Natsuki":

    if hangout2 == "Yuri":
        "We almost kissed yesterday..."
        "And she really did want to spend more time around me today..."
        "I've really come to enjoy her company, I wish we started talking sooner..."

    else:

        "She's been adamant about us trying to spend more time together..."
        "But would it be bad to give her a chance?"

if encore_festivalquestion_2 == "Yuri":

    if hangout2 == "Yuri":
        "Yesterday, she escalated things all on her own, something I thought she'd never do..."
        "If we were alone, we might've actually gotten the chance to kiss..."

    else:

        "She's been adamant about us trying to spend more time together..."
        "But would it be bad to give her a chance?"

"*sighs*"
"I know that this is all wrong..."
"By thinking like this, I'm really risking betraying my relationship with Sayori..."
"Only she should be able to kiss me..."
"She was rightfully pissed at me yesterday for it..."
"And if she ever found out that Yuri and I were in that position again , especially when I promised for it to never happen again, Sayori would be heartbroken..."
"God...{w=0.38}why am I so bad at this?!?!"
"I throw my hands over my face."
"I love Sayori...{w=0.38}but I'm pretty sure I've caught feelings for Yuri too..."
"And what makes this complicated is that Yuri likes me back too!"
"I'm in a literal love triangle..."
"And I don't want to hurt any of them..."
"I already know they both have serious problems, and I don't want to add on to anything..."
"But if I do decide that I want to be with Yuri...{w=0.38}I'd have to breakup with Sayori..."
"And that would be easier said then done...{w=0.38}and I don't know if that's what I want to do..."
"I've known her for fourteen years...{w=0.38}and I know she'd never do the same to me!"
"And we're both still trying to make this work..."
"But...{w=0.38}maybe she and I aren't really meant to be?"
"I mean...{w=0.38}lately I've been more interested in Yuri than Sayori..."
"And though it's my fault completely for our relationship starting to deteriorate...{w=0.38}I just don't have the same passion for her as I do for Yuri..."

if encore_festivalquestion_2 == "Natsuki":
    "I still can't help feel sorry for Natsuki..."
    "I mean, granted we haven't talked much since Sunday."
    "We only did share a few relatively intimate moments with each other, though nothing became of it..."
    "And I still find part of me wondering if what could've been...{w=0.38}still could be..."

if encore_festivalquestion_2 == "Yuri":
    "Especially with how last Sunday went..."


"Even if she was competing with Sayori for my attention..."
"But...{w=0.38}can I really do that to Sayori?"
"I roll over to face my bookshelves."
"On one of the shelves, I spot a picture of me and Sayori at the carnival."
"Man...{w=0.38}that must've been at least ten years ago..."
"Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
"And risk possibly ending the club?"
"I get out of my bed and walk over to pick up the picture frame."
"Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
"Huh...{w=0.38}I almost forgot that's when I won it for her..."
"I always did tell Sayori that she deserved the best..."

if hangout3 == "Natsuki":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

if hangout3 == "Monika":
    "But am I what she needs?"
    "Am I what she deserves?"
    "..."
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask


if hangout3 == "Natsuki":

    if encore_festivalquestion_2 == "Natsuki":
        play music e17
        "Suddenly my phone starts to ring."
        "I look down at the contact name...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        play music e17
        "Suddenly my phone starts to ring."
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."


    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2





label y_mono2:

"I really do think I like Yuri..."

if encore_festivalquestion_2 == "Natsuki":
    "Having spent the last few days getting to know her has truly been something..."

if encore_festivalquestion_2 == "Yuri":
    "Having spent the last two weeks getting to know her has truly been something..."

"It's truly amazing how far we've come in such a relatively short amount of time..."
"At first I thought she wanted to stay to herself, but now she has no problem talking to me!"
"I even think I'm starting to take an appreciation to her demeanor..."
"And well, she can clearly put up with me now..."
"I didn't know it at the time, but I didn't think we'd be able to get along as well as we do now."
"Considering how shy she was and everything..."


if hangout3 == "Yuri":
    "But the more I think about it, especially with what happened earlier, I think I understand why Yuri always acts so reserved and distant from everyone else..."
    "The more I think about it...{w=0.38}the more worried I am about her safety..."

    if tell_monika == True:
        "If she does actually cut herself...{w=0.38}what else is she doing?"
        "Why is she doing it?"
        "And how long has she been doing it?"
        "There's just more questions than answers right now..."
        "I just hope I can talk about it with her in an honest fashion..."

    if tell_monika == False:
        "I'm not completely convinced that these were ordinary cat scratches..."
        "And if she's actually cutting herself and denying it, then that's a serious problem in itself..."
        "But...{w=0.38}maybe I don't need Monika's help on this..."
        "Maybe I can talk to Yuri about this one-on-one?"
        "I mean, I hope she trusts me that much..."

    "But, maybe there's a chance she was just telling me the truth and didn't want me to worry..."
    "It'd be kind of funny if I ended up stressing all over this for nothing..."
    "I guess I really do care about her, huh?"
    "I've really become more invested in her the more time I've spent around her..."
    "No matter what it is we're doing, whether it be reading, drinking tea, or just even talking, being in Yuri's presence alone is its own reward."
    "Even though Yuri might think she might be boring me, I kind of like it when she goes on her little tangents..."
    "She always has something interesting and insightful to say about practically anything!"
    "In fact, I'm just surprised she doesn't find me boring, considering my tastes in literature is rather non-existent..."
    "Hopefully, Yuri feels the same way about me as I do about her, and I think she does..."
    "She's become much more relaxed around me since when we first started talking."
    "Even if it did take some time to get used to each other..."
    "She's never really hesitated to talk to me once we got acquainted..."
    "And yesterday, she escalated things all on her own, something I thought she'd never do..."
    "If we were alone, we might've actually gotten the chance to kiss..."
    "And I'd be the luckiest guy on Earth to have kissed someone as beautiful as Yuri..."
    "While I don't exactly expect for Yuri to be the one to confess her feelings to me directly, I do think she's been trying to say lately she does have mutual feelings..."
    "So, I guess it'll be up to me to figure out how to put it to her that I just want to be more than her friend..."
    "Though that also poses a problem for me..."
    "I know Natsuki likes me back...{w=0.38}I mean she confessed to me through her poem..."
    "And Sayori...{w=0.38}well I already know how she feels about me..."
    "If I do ultimately go for Yuri, I would have to break Natsuki's heart..."
    "And Sayori likely wouldn't have a great initial reaction either..."
    "So it seems no matter what I do, someone's going to get hurt thanks to my choice..."
    "And my odds of getting a harem are probably non-existent, at least practically speaking..."
    "I'm going to have to choose one of them by the end of this..."
    "And...{w=0.38}I don't think I have the feelings to go for Sayori, especially since I already turned her down once..."
    "I just don't have those kinds of feelings for her, even if part of me still entertains the idea every now and then..."

if hangout3 == "Monika":
    "But...{w=0.38}I also feel like I'm starting to really get to know Monika better..."
    "What happened earlier with her really surprised me..."
    "In fact, Monika has been nothing but full of surprises today..."
    "I'm glad she was able to calm me down and reassure me of everything during lunch..."
    "Even if she was a little too kind to me in the music room..."
    "If it wasn't for her help today, I'd probably still be a nervous wreck..."
    "Well, I'd be more of a nervous wreck if it wasn't for her..."
    "I can't deny that I've always liked Monika..."
    "But I thought she was out of my league..."
    "And earlier...{w=0.38}she clearly had no problems flirting with me..."
    "But, I know I was being a little disloyal at best to Yuri, given the stage we're at..."
    "I can't really give Monika a chance at this point in time, can I?"
    "I know I have feelings for Natsuki..."
    "And I do feel bad that I haven't spent time with [poem_giver] recently..."
    "Top it off with my regret for how I've been handling my friendship with Sayori lately..."
    "I did tell her that I wanted to spend more time with her, like how we used to..."
    "But once again I failed to deliver..."
    "But can I give everyone a chance at this point?"

if hangout3 == "Sayori":
    "But spending time with Sayori earlier really allowed me to reconnect with her a little..."
    "Us squabbling over my ice cream kind of reminded me of all the fun times we had when were kids..."
    "Back when life was simple, when we didn't have to deal with all these complicated feelings..."
    "I still care about her, even if we haven't spent as much time together as I would've liked too..."

    if sayori_ice == True:
        "I'm glad that for once, I managed to make her day..."

    if sayori_ice == False:
        "Even though I didn't let her have my ice cream, the episode still was a little fun, even if she felt otherwise..."

    "It's good to see that she's still able to act like her old self around me..."
    "And even though I still agonize over what happened last Sunday, I know I rejected her initially with [encore_festivalquestion_2] on my mind..."
    "But maybe I made a mistake..."
    "Maybe if I spent more time with Sayori, maybe I'd see in her what she sees in me..."
    "But I don't know if that opportunity is still there anymore, especially since I've really gotten to know Yuri recently..."
    "And I still need to figure out what to say to [poem_giver]..."
    "My feelings for all three of them are so mixed up!"
    "And I know I can't be with all three of them..."
    "Heck, I don't even know if I should entertain the possibility of being with Sayori, given her current state..."
    "But when she hopefully gets better...{w=0.38}who knows..."
    "But can I really let down Yuri and Natsuki?"





if encore_festivalquestion_2 == "Natsuki":
    "I mean, maybe I could give Natsuki another chance..."
    "We did have a good thing going for a while..."
    "But...{w=0.38}I guess my interest in her has just kind of faded recently..."
    "I sigh as I pull up my phone and scroll through my picture gallery."
    "As I'm scrolling, I come across some pictures I took with Natsuki at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "It's funny how most of these photos were her idea..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even wrapping her arm around me."
    "Huh...{w=0.38}I guess we would make a good couple..."


if encore_festivalquestion_2 == "Yuri":
    "I mean, maybe I could give Natsuki a chance and see if we have any real chemistry..."
    "But from the times I've interacted with her, I don't think there's much room for us to grow like that..."
    "I sigh as I pull up my phone and scroll through my picture gallery."
    "As I'm scrolling, I come across some pictures I took with Yuri at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "I'm surprised she even agreed to do them with me..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even letting me wrap my arm around her."
    "Maybe we would make a good couple..."


if hangout3 == "Yuri" or hangout3 == "Sayori":
    play music e17
    "Suddenly, my phone begins to ring."

if hangout3 == "Monika":
    "But, can I really make that decision based off of pictures?"
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I get off my bed, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask


if hangout3 == "Yuri":

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask


label y_hangout_ask:

y "H-{w=0.38}hey, [player]..."
mc "What's up? How're you?"
y "Oh, I'm doing alright..."
"I can tell Yuri seems to be rather anxious about calling me..."
"Probably figuring that I'd me mad at her for her being mad at me..."
y "L-{w=0.38}look..."
y "I wanted to apologize for my behavior towards you earlier today..."
y "I don't know what came over me..."
mc "It's fine, Yuri..."
mc "I'm not mad at you or anything..."
y "Well, that's a relief..."
y "I was worried that you wouldn't even take my call..."
mc "I'll admit I wasn't expecting one, but I'm always glad to talk to you..."
y "I'm not taking up any of your time, am I?"
mc "Ah, not really..."
mc "I've just been alone with my thoughts since I got home..."
y "Ah...{w=0.38}I know how you feel..."
y "It's been a trying day for the two of us to say the least..."
mc "What happened with you?"
"There's a long pause on Yuri's line."
mc "Yuri?"
y "Yeah, I'm still here..."
y "And nothing in particular I'd like to share right now..."
mc "It's fine..."
"There's another long pause on the line."
"Well this conversation has already turned out better than I thought it would, so I can't complain too much..."
y "Hey, [player]?"
mc "Yeah?"
y "If you want...{w=0.38}I heard that they just opened a new nature preserve just outside the city!"
y "I think visiting it would clear our heads..."
y "It will close by 8 tonight though, so if we want to go, we should probably get moving..."
"The idea of hanging out some more with Yuri is tempting..."
"We could use this opportunity to move on from what happened..."
"But I don't know if I really want to leave the house considering I got some heavy-duty thinking to do..."
"Not to mention I could use the early start on my homework..."

menu:
    "Should I hangout with Yuri?"
    "Yes.":
        $ yuri_hangout = True
        jump y_hangout
    "No.":
        $ yuri_hangout = False
        jump y_no_hangout

label y_hangout:

mc "Yeah, sure! I'd love to go with you!"
y "Really?!? That's wonderful, [player]!"
mc "Yeah...{w=0.38}I could use some fresh air right now anyways..."
y "Well I suppose that makes two of us..."
y "I can meet you by the train station if you wish, it's not too far from school..."
mc "Yeah I can meet you there!"
y "Great! I'll see you soon!"
mc "Bye!"
"Yuri hangs up the call."
"I must admit that I'm surprised that Yuri's inviting me to spend more time with her."
"It's not something I would've expected given what happened in the club today..."
"But, I'm not going to pass up an opportunity to get closer to Yuri!"
"And maybe there's a chance I can put my concerns about her safety to rest..."
"I grab my keys and wallet and quickly head towards the train station."
jump yencore_4

label y_no_hangout:

mc "I appreciate the offer, but, I kinda wanna be alone right now..."
y "Oh..."
y "It's okay, [player]..."
y "I understand."
mc "It's not because of what happened earlier..."
mc "I just have a lot on my plate right now..."
"A long, uncomfortable pause quickly follows from Yuri's line."
"Knowing her, she's probably jumping to the worst case scenario as to why I wouldn't want to be around her..."
"Although, I guess from her point of view, it really isn't that far-fetched..."
mc "As I said:{w=0.38} I'm not mad at you for what happened earlier..."
y "I know, [player]..."
y "I believe you."
"There's another pause between us."
"It's really hard to say if she bought it or not, but I guess I'll have to take her at her word."
y "Well, I need to get going..."
y "After all, I need to leave as soon as possible before the preserve closes!"
mc "Alright, I won't keep you anymore than I have."
mc "Have fun, Yuri! I'll see you tomorrow."
y "Alright, goodbye."
mc "Bye."
"Yuri disconnects the call."
"I sit on my bed to reflect on my decision."
"Maybe I should've gone with her..."
"Some face-to-face communication probably would've helped better resolve what happened earlier."
"After all, she did sound like she wanted me to come along with her."
"And maybe spending time with her would've helped confirm my interest in her."
"Well, on the bright side, at least I'll be alone to try to sort my thoughts out..."
"I spend what must feel like hours simply staring at the ceiling and trying to grasp my emotions for the others."

if encore_sayoriquestion_1 == True:
    "And whether I should really end things with Sayori on something that might not even workout."
    "Maybe I should just focus on her..."

if encore_sayoriquestion_1 == False:
    "I think back to the questions Monika told me to ask myself, but I'm not finding myself being able to answer them in a satisfying way."

"Maybe I should focus on something a little less draining..."
"I should have some homework to keep me busy..."
"I get up from my bed and dig out my homework stash from my backpack."
"Well, at least I'm doing something productive..."
"I sit down at my desk and begin reading over the questions."
scene black
with close_eyes
jump day3_night


#Mixed Choices
#These can't repeat
#No Sayori


label mix_mono1:

"I know I love Sayori."
"I do..."
"I've enjoyed every moment I've been around her..."
"Even if she's a bit much to handle at times..."

if hangout1 == "Natsuki" or hangout1 == "Yuri" or  hangout1 == "Monika":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or  hangout2 == "Monika":
        "But...{w=0.38}lately I've found myself having fun spending time around [hangout1] and [hangout2]..."
        "And I can't stop myself from wanting to spend more time around them..."

        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Natsuki":
                if hangout2 == "Yuri" or hangout2 == "Monika":
                    "It was nice to catch up with Natsuki again..."
                    "But I had even more fun with [hangout2] yesterday, even though I had no intention of getting so close to her..."

        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Yuri":
                if hangout2 == "Natsuki":
                    "It was nice to finally spend sometime around Natsuki..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Monika":
                if hangout2 == "Natsuki":
                    "It was nice to finally talk to Monika a little bit more than usual..."
                    "But, I had fun spend time around Natsuki on Tuesday..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Natsuki":
                if hangout2 == "Yuri":
                    "It was nice to finally spend sometime around Natsuki..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Yuri":
                if hangout2 == "Natsuki" or hangout2 == "Monika":
                    "It was nice to catch up with Yuri again..."
                    "But I had even more fun with Natsuki yesterday, even though I had no intention of getting so close to her..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Monika":
                if hangout2 == "Yuri":
                    "It was nice to finally talk to Monika a little bit more than usual..."
                    "But, I had fun spending time around Yuri on Tuesday..."
                    "Getting close to her reminded me of the fun we had on Sunday..."



"Even though I was still in the wrong..."

if apologize_sn == False or apologize_sy == False or apologize_sm == False:
    "What's even worse is that I tried to lie about it to Sayori's face..."
    "And even though I still ended up telling the truth and apologizing for it..."

if apologize_sn == True or apologize_sy == True or apologize_sm == True:
    "At least I apologized to her about it..."

"Still, I can't change the fact that I've seriously damaged my relationship with Sayori..."

if hangout3 == "Sayori":
    "Though I've been trying to make up for it by spending time with her today..."

    if sayori_ice == True:
        "And I guess it helped..."

    if sayori_ice == False:
        "But I'm not exactly sure if it helped or not..."

"But the damage has been done and she hardly trusts me now..."
"Even if she won't admit it..."
"I'm just making things worse for her, and she's already in a fragile state of mind!"
"Why am I so bad at looking after for Sayori? I've been messing it up for years at this point and then I decide to get into a relationship with her?"

if hangout3 == "Natsuki" or hangout3 == "Monika" or hangout3 == "Yuri":
    "And I really haven't done anything to make up for that lost trust, especially when I had an opportunity to spend some time with her today..."

    if hangout3 == "Natsuki":

        if hangout2 == "Natsuki":
            "I've just spent the last two days with Natsuki..."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Natsuki..."
            "And I really can't decide who I've enjoyed spending time with more..."


    if hangout3 == "Monika":

        if hangout2 == "Monika":
            "I've just spent the last two days with Monika..."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Monika..."
            "And I really can't decide who I've enjoyed spending time with more..."

    if hangout3 == "Yuri":

        if hangout2 == "Yuri":
            "I've just spent the last two days with Yuri.."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Yuri..."
            "And I really can't decide who I've enjoyed spending time with more..."


"I let a sigh to myself."
"Maybe I made a mistake..."
"Maybe I said yes too early, even if things were going well for us at first..."
"After all, I did kind of decide it on the spot..."
"And now I have to deal with the weight of that decision."
"With me unable to decide who I like the most..."
"I guess Monika was right..."
"Maybe my relationship with Sayori is doomed to fail if I keep thinking like this..."
"I don't know who I like anymore, even though Sayori and [poem_giver] have feelings for me..."
"I roll over to face my bookshelves."
"On one of the shelves, I spot a picture of me and Sayori at the carnival."
"Man...{w=0.38}that must've been at least ten years ago..."
"Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
"And risk possibly ending the club?"
"I get out of my bed and walk over to pick up the picture frame."
"Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
"Huh...{w=0.38}I almost forgot that's when I won it for her..."
"I always did tell Sayori that she deserved the best..."
"My hand starts to shake as tears start to swell up in my eyes."
"Could I really do it?"
"Is it even right to think this way?"
"No matter who I choose...{w=0.38}someone's getting heartbroken because of me..."
"And when I do make that decision, how am I going to live with myself?"



if hangout3 == "Natsuki" or hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

if hangout3 == "Monika":
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

    if hangout3 == "Natsuki":

        if encore_festivalquestion_2 == "Natsuki":
            "To my surprise...{w=0.38}it's Natsuki!"
            "Why is she calling me?"
            "I just hope something didn't happen..."
            stop music
            "I answer the phone."
            mc "Natsuki?"
            n "Hey, [player]!"
            mc "W-{w=0.38}what's up?"
            n "Why do you sound so surprised?"
            mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
            n "I guess that's true..."

        if encore_festivalquestion_2 == "Yuri":
            "I look down at the number...{w=0.38}I don't recognize it."
            "Eh, I'm not doing anything right now..."
            "At worst I'll be talking to a telemarketer..."
            stop music
            "I answer the phone."
            mc "Hello?"
            n "[player]? Is that you?"
            mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
            n "Why do you sound so surprised?"
            mc "Well, I don't remember giving you my number..."
            n "Sayori told me what it was."
            "Figured she would do that..."


        if natsuki_continued_hug == True:
            jump n_line_1

        if natsuki_continued_hug == False:
            jump n_line_2

        if natsuki_hug == True:
            jump n_line_1

        if natsuki_hug == False:
            jump n_line_2


    if hangout3 == "Yuri":

        if encore_festivalquestion_2 == "Natsuki":
            "I look down at the number...{w=0.38}I don't recognize it."
            "Eh, I'm not doing anything right now..."
            "It's probably just a wrong number..."
            stop music
            "I answer the phone."
            mc "Hello?"
            jump y_hangout_ask

        if encore_festivalquestion_2 == "Yuri":
            "I look down at the contact name...{w=0.38}it's Yuri!"
            "Why is she calling me?"
            stop music
            "I answer the phone."
            mc "Yuri?"
            jump y_hangout_ask




#Mixed Choices
#These can't repeat
#Sayori must be one of these options


label mix_mono2:

"I know I love Sayori."
"I do..."
"I've enjoyed every moment I've been around her..."
"Even if she's a bit much to handle at times..."
"But I don't know if she really has my undivided attention at this point..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        "Especially after I spent yesterday with [hangout2]..."
        "Granted, I didn't expect [hangout2] to get so close to me like that..."
        "It still felt nice...{w=0.38}even though it was wrong for me to be in that position for so long in the first place..."

        if apologize_sn == False or apologize_sy == False or apologize_sm == False:
            "What's even worse is that I tried to lie about it to Sayori's face..."
            "And even though I still ended up telling the truth and apologizing for it..."

        if apologize_sn == True or apologize_sy == True or apologize_sm == True:
            "At least I apologized to her about it..."

        "But I can't deny that I still hurt her pretty badly..."
        "And given how she's been lately, I know I shouldn't be getting myself into positions like that with the others..."
        "Not to mention I still have to figure out how to respond to [poem_giver]'s poem..."
        "And if I tell Sayori about it, she's only going to get more suspicious of me..."


if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Sayori":


        if hangout1 == "Natsuki":
            if encore_festivalquestion_2 == "Natsuki":
                "It was really nice to catch up with Natsuki again..."
                "Especially since we had so much preparing for and at the festival..."



            if hangout1 == "Yuri":
                if encore_festivalquestion_2 == "Natsuki":
                    "It was really nice to finally spend sometime around Yuri..."
                    "Given that we haven't really talked much since I first joined..."



            if hangout1 == "Monika":
                if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
                    "It was really nice to finally talk to Monika a little bit more than usual..."
                    "Given that we've never really talked with each other..."



            if hangout1 == "Natsuki":
                if encore_festivalquestion_2 == "Yuri":
                    "It was really nice to finally spend sometime around Natsuki..."
                    "Given that we haven't really talked much since I first joined..."


            if hangout1 == "Yuri":
                if encore_festivalquestion_2 == "Yuri":
                    "It was really nice to catch up with Yuri again..."
                    "Especially since we had so much preparing for and at the festival..."


            "But she really didn't seem to like seeing Sayori rest on me like that..."
            "Maybe she could be jealous?"
            "I mean it would make sense for [poem_giver] to be, since I know she likes me..."

            if hangout3 == "Sayori":
                "And she really wanted to spend more time around me today..."
                "Though, I felt the need to look after Sayori..."

                if sayori_ice == True:
                    "And I guess spending time around her today helped..."

                if sayori_ice == False:
                    "But I'm not exactly sure if I helped her or not..."

            "Still, I can't deny that I had fun spending time around her..."
            "It brought back a sense of nostalgia from our childhood..."
            "Before all this craziness...{w=0.38}when things were so much simpler back then..."
            "And for once...{w=0.38}we got to reminisce a little together..."


            if hangout3 == "Natsuki":
                "But Natuski seemed to have gotten over it by the time we were done hanging out..."

                if natsuki_continued_hug == True:
                    jump n_line_9

                if natsuki_continued_hug == False:
                    jump n_line_10

                if natsuki_hug == True:
                    jump n_line_9

                if natsuki_hug == False:
                    jump n_line_10

                label n_line_9:

                "Especially with what she told me about her home life..."
                "It's got me worried for her safety, even though I haven't known her that long..."
                "I still care about her..."

                label n_line_10:

                "Even though she ended up blowing up at me later..."
                "Ah, I'm sure she'll cool down..."
                "I still care about her..."

            if hangout3 == "Monika":
                "But Monika didn't really seem to show any signs of jealously when I was around her today..."
                "In fact, she almost acted like it never even happened..."


            if hangout3 == "Yuri":
                "But Yuri seemed to have gotten over it by the time we were done hanging out..."
                "Though she ended up getting mad at me because I pressed her on what I thought I saw..."
                "It's got me worried for her safety, even though I haven't known her that long..."
                "I still care about her..."





"I let a sigh to myself."
"Maybe I made a mistake..."
"Maybe I said yes too early, without really getting the chance to know everyone first..."
"After all, I did kind of decide it on the spot..."
"And now I have to deal with the weight of that decision."
"With me unable to decide who I like the most..."
"I guess Monika was right..."
"Maybe my relationship with Sayori is doomed to fail if I keep thinking like this..."
"I don't know who I like anymore, even though Sayori and [poem_giver] have feelings for me..."
"I roll over to face my bookshelves."
"On one of the shelves, I spot a picture of me and Sayori at the carnival."
"Man...{w=0.38}that must've been at least ten years ago..."
"Do I really have it in me to tell her, that same girl, who's now my girlfriend, that I want to dump her for another relationship that's not even guaranteed to work out?"
"And risk possibly ending the club?"
"I get out of my bed and walk over to pick up the picture frame."
"Upon a closer look, I see Sayori clutching a familiar giant sized cow..."
"Huh...{w=0.38}I almost forgot that's when I won it for her..."
"I always did tell Sayori that she deserved the best..."
"My hand starts to shake as tears start to swell up in my eyes."
"Could I really do it?"
"Is it even right to think this way?"
"No matter who I choose...{w=0.38}someone's getting heartbroken because of me..."
"And when I do make that decision, how am I going to live with myself?"


if hangout3 == "Natsuki" or hangout3 == "Yuri":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."

if hangout3 == "Monika":
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I put the picture frame back, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    play music e17
    "Suddenly I hear my phone ringing."
    "I put the picture frame down and run over to my phone to see who's calling."
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

    if hangout3 == "Natsuki":

        if encore_festivalquestion_2 == "Natsuki":
            "To my surprise...{w=0.38}it's Natsuki!"
            "Why is she calling me?"
            "I just hope something didn't happen..."
            stop music
            "I answer the phone."
            mc "Natsuki?"
            n "Hey, [player]!"
            mc "W-{w=0.38}what's up?"
            n "Why do you sound so surprised?"
            mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
            n "I guess that's true..."

        if encore_festivalquestion_2 == "Yuri":
            "I look down at the number...{w=0.38}I don't recognize it."
            "Eh, I'm not doing anything right now..."
            "At worst I'll be talking to a telemarketer..."
            stop music
            "I answer the phone."
            mc "Hello?"
            n "[player]? Is that you?"
            mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
            n "Why do you sound so surprised?"
            mc "Well, I don't remember giving you my number..."
            n "Sayori told me what it was."
            "Figured she would do that..."


        if natsuki_continued_hug == True:
            jump n_line_1

        if natsuki_continued_hug == False:
            jump n_line_2

        if natsuki_hug == True:
            jump n_line_1

        if natsuki_hug == False:
            jump n_line_2

    if hangout3 == "Yuri":

        if encore_festivalquestion_2 == "Natsuki":
            "I look down at the number...{w=0.38}I don't recognize it."
            "Eh, I'm not doing anything right now..."
            "It's probably just a wrong number..."
            stop music
            "I answer the phone."
            mc "Hello?"
            jump y_hangout_ask

        if encore_festivalquestion_2 == "Yuri":
            "I look down at the contact name...{w=0.38}it's Yuri!"
            "Why is she calling me?"
            stop music
            "I answer the phone."
            mc "Yuri?"
            jump y_hangout_ask






#Mixed Choices
#These can't repeat
#No Sayori

label mix_mono3:

"I don't even know where to begin..."
"My feelings are all over the place..."


if hangout1 == "Natsuki" or hangout1 == "Yuri" or  hangout1 == "Monika":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or  hangout2 == "Monika":
        "I can't decide if I like spending my time more with [hangout1] or [hangout2]..."

        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Natsuki":
                if hangout2 == "Yuri" or hangout2 == "Monika":
                    "It was really nice to catch up with Natsuki again..."
                    "But I had even more fun with [hangout2] yesterday, even though I had no intention of getting so close to her..."


        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Yuri":
                if hangout2 == "Natsuki":
                    "It was really nice to finally spend sometime around Natsuki..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Natsuki":
            if hangout1 == "Monika":
                if hangout2 == "Natsuki":
                    "It was really nice to finally talk to Monika a little bit more than usual..."
                    "But, I had fun spend time around Natsuki on Tuesday..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Natsuki":
                if hangout2 == "Yuri":
                    "It was really nice to finally spend sometime around Natsuki..."
                    "Getting close to her reminded me of the fun we had on Sunday..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Yuri":
                if hangout2 == "Natsuki" or hangout2 == "Monika":
                    "It was really nice to catch up with Yuri again..."
                    "But I had even more fun with Natsuki yesterday, even though I had no intention of getting so close to her..."

        if encore_festivalquestion_2 == "Yuri":
            if hangout1 == "Monika":
                if hangout2 == "Yuri":
                    "It was really nice to finally talk to Monika a little bit more than usual..."
                    "But, I had fun spend time around Yuri on Tuesday..."
                    "Getting close to her reminded me of the fun we had on Sunday..."



"And I'm really glad we got to share the moment we did yesterday..."
"Even though I didn't ask for it, her embrace felt warm and comforting..."
"Still, I can't change the fact that I've seriously damaged my relationship with Sayori..."

if hangout3 == "Sayori":
    "Though I've been trying to make up for it by spending time with her today..."

    if sayori_ice == True:
        "And I guess it helped..."

    if sayori_ice == False:
        "But I'm not exactly sure if it helped or not..."

    "I just know that I shouldn't play with her feelings..."
    "She's already in a fragile state of mind..."
    "Yet, part of me still wants to give her a chance..."
    "Maybe the girl I've needed has been beside me this whole time..."

if hangout3 == "Natsuki" or hangout3 == "Monika" or hangout3 == "Yuri":
    "And I really haven't done much to fix it, especially when I had an opportunity to spend some time with her today..."

    if hangout3 == "Natsuki":

        if hangout2 == "Natsuki":
            "I've just spent the last two days with Natsuki..."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Natsuki..."
            "And I really can't decide who I've enjoyed spending time with more..."


    if hangout3 == "Monika":

        if hangout2 == "Monika":
            "I've just spent the last two days with Monika..."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Monika..."
            "And I really can't decide who I've enjoyed spending time with more..."

    if hangout3 == "Yuri":

        if hangout2 == "Yuri":
            "I've just spent the last two days with Yuri.."
            "And I feel myself growing more attracted to her..."

        else:
            "I've just spent the last two days with [hangout2] and Yuri..."
            "And I really can't decide who I've enjoyed spending time with more..."


"I let a sigh to myself."
"How am I supposed to decide this?"
"I mean at this point I probably like [hangout1] and [hangout2]..."
"And I know I can't have both of them, that scenario would never work out..."
"I know I'm supposed to go with what's in my heart, but..."
"I don't even know who I'm interested in at this point..."
"I have options..."
"I know for a fact Sayori and [poem_giver] like me..."
"But why should I limit myself to just two choices?"
"I mean...{w=0.38}at this point I probably could go for anybody..."
"I sigh as I pull up my phone and scroll through my picture gallery."

if encore_festivalquestion_2 == "Natsuki":
    "As I'm scrolling, I come across some pictures I took with Natsuki at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "It's funny how most of these photos were her idea..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even wrapping her arm around me."
    "Huh...{w=0.38}I guess we would make a good couple..."


if encore_festivalquestion_2 == "Yuri":
    "As I'm scrolling, I come across some pictures I took with Yuri at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "I'm surprised she even agreed to do them with me..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even letting me wrap my arm around her."
    "Maybe we would make a good couple..."


if hangout3 == "Natsuki" or hangout3 == "Yuri" or hangout3 == "Sayori":
    play music e17
    "Suddenly, my phone begins to ring."

if hangout3 == "Monika":
    "But, can I really make that decision based off of pictures?"
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I get off my bed, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    stop music
    jump s_hangout_ask

if hangout3 == "Natsuki":

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."


    if natsuki_continued_hug == True:
        jump n_line_1

    if natsuki_continued_hug == False:
        jump n_line_2

    if natsuki_hug == True:
        jump n_line_1

    if natsuki_hug == False:
        jump n_line_2


if hangout3 == "Yuri":

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask




#Mixed Choices
#These can't repeat
#Sayori must be one of these options

label mix_mono4:

"I don't even know where to begin..."
"My feelings are all over the place..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki" or hangout2 == "Yuri" or hangout2 == "Monika":
        "Especially after I spent yesterday with [hangout2]..."
        "Granted, I didn't expect [hangout2] to get so close to me like that..."
        "It still felt nice..."
        "But part of me regrets doing it too..."
        "Seeing the look on Sayori's face reminded me of how she was last Sunday..."
        "I know she wants to see me happy, but it's still pretty painful for her to watch me spend time with the others..."
        "And I don't really want to hurt Sayori anymore than I already have..."
        "I can't deny that I've been a horrible friend for these last few years..."
        "And given how she's been lately, I should probably be more careful when I'm around the others in the clubroom..."
        "Not to mention I still have to figure out how to respond to [poem_giver]'s poem..."
        "And if I tell Sayori about it, she's only going to get more heartbroken..."


if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
    if hangout2 == "Sayori":
        "Especially after I spent yesterday with [hangout2]..."
        "Granted, I didn't expect [hangout2] to get so close to me like that, I just know she needed me in that moment..."
        "But, part of me enjoyed hugging her..."
        "It felt so natural..."
        "But part of me regrets doing it too..."
        "I didn't expect [hangout1] and the others to catch us like that..."
        "She clearly got the wrong idea of what was happening..."
        "And it sucks I really couldn't explain it to them in the heat of the moment, but..."
        "What happened, happened..."

        if hangout1 == "Natsuki":
            if encore_festivalquestion_2 == "Natsuki":
                "Still, it was really nice to catch up with Natsuki again..."
                "Especially since we had so much preparing for and at the festival..."

        if hangout1 == "Yuri":
            if encore_festivalquestion_2 == "Natsuki":
                "Still, it was really nice to finally spend sometime around Yuri..."
                "Given that we haven't really talked much since I first joined..."


        if hangout1 == "Monika":
            if encore_festivalquestion_2 == "Natsuki" or encore_festivalquestion_2 == "Yuri":
                "Still, it was really nice to finally talk to Monika a little bit more than usual..."
                "Given that we've never really talked with each other..."



        if hangout1 == "Natsuki":
            if encore_festivalquestion_2 == "Yuri":
                "It was really nice to finally spend sometime around Natsuki..."
                "Given that we haven't really talked much since I first joined..."


        if hangout1 == "Yuri":
            if encore_festivalquestion_2 == "Yuri":
                "Still, it was really nice to catch up with Yuri again..."
                "Especially since we had so much preparing for and at the festival..."


"But she really didn't seem to like seeing Sayori rest on me like that..."
"Maybe she could be jealous?"
"I mean it would make sense for [poem_giver] to be, since I know she likes me..."

if hangout3 == "Sayori":
    "And she really wanted to spend more time around me today..."

    if sayori_ice == True:
        "And I guess it helped..."

    if sayori_ice == False:
        "But I'm not exactly sure if it helped or not..."

    "But, I did have fun spending time around her today..."
    "It brought back a sense of nostalgia from our childhood..."
    "Before all this craziness...{w=0.38}when things were so much simpler back then..."
    "I miss those days with Sayori, but I don't think I can bring them back."


if hangout3 == "Natsuki":
    "But Natuski seemed to have gotten over it by the time we were done hanging out..."

    if natsuki_continued_hug == True:
        jump n_line_11

    if natsuki_continued_hug == False:
        jump n_line_12

    if natsuki_hug == True:
        jump n_line_11

    if natsuki_hug == False:
        jump n_line_12

    label n_line_11:

    "Especially with what she told me about her home life..."
    "It's got me worried for her safety, even though I haven't known her that long..."
    "I still care about her..."

    label n_line_12:

    "Even though she ended up blowing up at me later..."
    "Ah, I'm sure she'll cool down..."
    "I still care about her..."

if hangout3 == "Monika":
    "But Monika didn't really seem to show any signs of jealously when I was around her today..."
    "In fact, she almost acted like it never even happened..."


if hangout3 == "Yuri":
    "But Yuri seemed to have gotten over it by the time we were done hanging out..."
    "Though she ended up getting mad at me because I pressed her on what I thought I saw..."
    "It's got me worried for her safety, even though I haven't known her that long..."
    "I still care about her..."


"I let a sigh to myself."
"Maybe I made a mistake..."
"I know I was deciding on the spot on Sunday, but maybe I could've worded things differently to her..."
"Now I may be having second thoughts"
"With me unable to decide who I like the most..."
"Monika was right..."
"I should probably just try to stay friends with everyone until I can decide on my feelings..."
"I mean...{w=0.38}I don't even know who I'm interested in at this point..."
"I have options..."
"And I know for a fact Sayori and [poem_giver] like me..."
"I sigh as I pull up my phone and scroll through my picture gallery."

if encore_festivalquestion_2 == "Natsuki":
    "As I'm scrolling, I come across some pictures I took with Natsuki at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "It's funny how most of these photos were her idea..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even wrapping her arm around me."
    "Huh...{w=0.38}I guess we would make a good couple..."


if encore_festivalquestion_2 == "Yuri":
    "As I'm scrolling, I come across some pictures I took with Yuri at the festival."
    "Looking back at some of the photos, I see just how happy we look doing all these silly poses throughout the festival."
    "I'm surprised she even agreed to do them with me..."
    "I scroll to the last photo which is us standing by the entrance to the school at the end of the festival."
    "I notice just how close together we are in this photo, with her even letting me wrap my arm around her."
    "Maybe we would make a good couple..."


if hangout3 == "Natsuki" or hangout3 == "Yuri" or hangout3 == "Sayori":
    play music e17
    "Suddenly my phone begins to ring."

if hangout3 == "Monika":
    "But, can I really make that decision based off of pictures?"
    "Agh! This is hopeless!"
    "I'm being pulled in all directions!"
    "Maybe a walk will help me clear my head..."
    "I'd probably be able to think better that way..."
    "And maybe along the way I'll figure out who I feel the most strongly towards..."
    "I get off my bed, grab my keys and walk out of my house."
    jump m_hangout_ask

if hangout3 == "Sayori":
    "To my surprise...{w=0.38}it's Sayori!"
    "Why is she calling me? We saw each other like ten minutes ago..."
    jump s_hangout_ask

if hangout3 == "Natsuki":

    if encore_festivalquestion_2 == "Natsuki":
        "To my surprise...{w=0.38}it's Natsuki!"
        "Why is she calling me?"
        "I just hope something didn't happen..."
        stop music
        "I answer the phone."
        mc "Natsuki?"
        n "Hey, [player]!"
        mc "W-{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "I just...{w=0.38}wasn't expecting you to call, that's all!"
        n "I guess that's true..."

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "At worst I'll be talking to a telemarketer..."
        stop music
        "I answer the phone."
        mc "Hello?"
        n "[player]? Is that you?"
        mc "Y-{w=0.38}yeah...{w=0.38}what's up?"
        n "Why do you sound so surprised?"
        mc "Well, I don't remember giving you my number..."
        n "Sayori told me what it was."
        "Figured she would do that..."

if hangout3 == "Yuri":

    if encore_festivalquestion_2 == "Natsuki":
        "I look down at the number...{w=0.38}I don't recognize it."
        "Eh, I'm not doing anything right now..."
        "It's probably just a wrong number..."
        stop music
        "I answer the phone."
        mc "Hello?"
        jump y_hangout_ask

    if encore_festivalquestion_2 == "Yuri":
        "I look down at the contact name...{w=0.38}it's Yuri!"
        "Why is she calling me?"
        stop music
        "I answer the phone."
        mc "Yuri?"
        jump y_hangout_ask



label day3_night:

scene bg bedroom_night
with open_eyes

if hangout3 == "Monika":
    jump day3_mnight

if hangout3 == "Natsuki":
    jump day3_nnight

if hangout3 == "Sayori":
    jump day3_snight

if hangout3 == "Yuri":
    jump day3_ynight

label day3_mnight:

if monika_hangout == True:
    jump m_night1

if monika_hangout == False:
    jump m_night2

label day3_nnight:

if natsuki_hangout == True:
    jump n_night1

if natsuki_hangout == False:
    jump n_night2

label day3_snight:

if sayori_hangout == True:
    jump s_night1

if sayori_hangout == False:
    jump s_night2

label day3_ynight:

if yuri_hangout == True:
    jump y_night1

if yuri_hangout == False:
    jump y_night2



#Monika

label m_night1:

"I immediately collapse onto my bed, feeling the full weight of my exhaustion of the last few hours overtake me."
"My legs are completely numb from all the walking I did today."
"At least I managed to get some good physical exercise out of all this..."
"And I really did get closer to Monika..."
"A lot closer..."

if encore_sayoriquestion_1 == True:
    "But was it worth it?"
    "Sayori certainly wouldn't take too kindly to finding out how Monika and I spent all that time..."
    "Granted, Monika isn't really the type of person to gossip about those kinds of things..."
    "At least I hope so..."

if encore_sayoriquestion_1 == False:
    "But in doing so, if [poem_giver] found out about how I spent today with Monika, she'd probably be heart broken."
    "And while I'd say my feelings for Monika are pretty much settled, I can't say the same for [poem_giver]..."

"Oh well, I'll try to worry about it tomorrow..."
"I have enough on my plate as is..."

if hangout2 == "Monika":
    "And hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "And hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep."
jump day3_mvoid

label m_night2:

"After a few hours of more or less mindlessly walking through my neighborhood, I return home and lumber up to my bedroom."
"To say that my walk was productive would be an understatement."
"I ended up feeling more conflicted than ever before as I did my best to try to gage my feelings."
"I seriously regret not taking Monika up on her offer to walk with her..."
"Maybe I could've gotten a better grasp on my feelings that way..."

if encore_sayoriquestion_1 == True:
    "I guess a positive way to look at things is that I didn't violate any more boundaries in my relationship with Sayori..."
    "So, I suppose that's a win, even though it doesn't really excuse the flirting that took place earlier..."

if encore_sayoriquestion_1 == False:
    "I just don't know who I feel the strongest towards..."
    "I'm going to have to choose someone by the end of all this..."
    "And I don't feel any closer to being able to make that call..."


"I'll just try to put this on the back burner for now, I should just try to get some sleep."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_mvoid


#Natsuki

label n_night1:

"After finishing everything I need to do for school tomorrow, I lay on my bed, ready to fall asleep."
"Today was a lot better than I expected it to be!"
"I was expecting it to be a total train wreck, figuring that Yuri was going to pull me aside to talk about her letter."
"But fortunately, that didn't happen, even though that didn't stop us from having a clash earlier..."
"At least I got closer to Natsuki..."
"A lot closer..."
"And knowing the full extent of her situation at home, I know I have to be there for her."
"But to what extent can I support her?"

if encore_sayoriquestion_1 == True:
    "I know I've committed to being with Sayori, but today I really did test the limits of that relationship..."
    "And for better or worse, she'll never know about what happened today."

if encore_sayoriquestion_1 == False:
    "I mean it's starting to show that we have feelings for each other..."
    "Sooner or later, one of us is going to end up confessing..."
    "But I still have to deal with Yuri..."
    "I have no idea what I'm even supposed to say her..."

"I'll just try to put this on the back burner for now, I should just try to get some sleep."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_nvoid


label n_night2:

"Despite my thoughts and emotions distracting me every few minutes, I was able to eventually complete all my homework."
"I pack all my things and lay on my bed, getting ready to finally fall asleep."
"I ended up feeling more conflicted than ever before as I did my best to try to gage my feelings."
"I seriously regret not going with Natsuki to the bookstore..."
"She sounded like she really wanted me to come..."
"And maybe spending time with her could've helped confirm our feelings for each other..."

if encore_sayoriquestion_1 == True:
    "I guess a positive way to look at things is that I didn't violate any more boundaries in my relationship with Sayori..."
    "So, I suppose that's a win, even though it doesn't really excuse my hug with Natsuki..."

if encore_sayoriquestion_1 == False:
    "I just don't know who I feel the strongest towards..."
    "I'm going to have to choose someone by the end of all this..."
    "And I don't feel any closer to being able to make that call..."


"I'll just try to put this on the back burner for now, I should just try to get some sleep."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_nvoid




#Sayori

label s_night1:

"After finishing my nightly routine and finish any oustanding homework, I lay back in my bed and prepare to fall asleep."
"All things considered, today was a pretty good day!"
"Monika gave me some helpful advice regarding my situation..."
"And I had pretty good time with Sayori..."

if encore_sayoriquestion_1 == True:
    "We actually went on our first real date since we've been officially together..."

if encore_sayoriquestion_1 == False:
    "I really think we made progress in repairing our friendship..."
    "Even though we had a few moments that kind of went beyond us being friends..."

"It was nice though."
"And I'm glad I took her up on her offer to go out."
"In a way, it did help settle my feelings a little bit."

if encore_sayoriquestion_1 == True:
    "I do truly love her, and I really wouldn't want to ruin it..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1== "Yuri":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "At least anymore than I already have..."

    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I don't want a repeat of yesterday..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            "In fact I wish I spent more time with her this week..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "And I'd say I've been pretty faithful to our relationship..."

if encore_sayoriquestion_1 == False:
    "I guess I am starting to re-consider my earlier decision..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1== "Yuri":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "But I still don't know if it's realistic at this point..."

    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "She obviously still has feelings for me, and it showed when I messed up yesterday by getting too close to [hangout2]..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            "I guess the idea of me being with Sayori really started yesterday when we hugged..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "Being there for her these past few days has sparked a renewed interest in her..."


"Still, I have to figure out what to say to [poem_giver]..."
"I don't really feel any closer to figuring out what to say to her..."
"But, I'll worry more about it tomorrow..."
"I should just try to get some good sleep for once..."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_svoid


label s_night2:

"Despite my thoughts and emotions distracting me every few minutes, I was able to eventually complete all my homework."
"I pack all my things and lay on my bed, getting ready to finally fall asleep."
"I ended up feeling more conflicted than ever before as I did my best to try to gage my feelings."
"I seriously regret not going out with Sayori.."
"I know she wanted to spend more time with me..."

if encore_sayoriquestion_1 == True:
    "And maybe I could've seen just how our strong our relationship is right now..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1== "Yuri":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "And it's already on the ropes..."

    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "And it is kind of shaky..."


    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            "I think it's gone alright so far..."


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "Though I think it's gone rather well..."


if encore_sayoriquestion_1 == False:
    "And maybe I could've seen if I felt any different about her..."

    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1== "Yuri":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "Though given how things have gone latety, I probably wouldn't have changed my opinion..."


    if hangout1 == "Sayori":
        if hangout2 == "Monika" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "I guess I'm still kind of on the fence about her..."


    if hangout1 == "Monika" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        if hangout2 == "Sayori":
            "I guess I'm still kind of on the fence about her..."



    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "I really have begun to re-consider my initial decision on rejecting her..."
            "I've had a lot of fun spending time with her this past week, and I'd love to keep it up..."

"Still, this all just takes me back to figuring out what I want to say to [poem_giver], when I have no clue about how I feel about anyone!"
"I'm not any closer to figuring out what to say to her..."
"But, I guess I'll have to worry about it tomorrow..."
"I should just try to get some good sleep for once..."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_svoid




#Yuri

label y_night1:

"As soon as I enter my house, I immediately head up to my room and collapse onto my bed, letting my exhaustion  overtake me."
"My legs are completely numb from all the walking I did today."
"At least I managed to get some good physical exercise out of all this..."
"And I really turned things around with Yuri..."
"In fact, not only did I turn things around, but we managed to really get closer together..."


if encore_sayoriquestion_1 == True:
    "But part of me still doesn't feel right about some of the things that happened..."
    "Sayori certainly wouldn't take too kindly to finding out my tension filled moments with Yuri..."
    "Granted, it's not like Sayori would ever know about it, since Yuri isn't the type of person to gossip..."

if encore_sayoriquestion_1 == False:
    "But I guess by getting closer to Yuri, I am forcing myself to turn out Natsuki..."
    "And I really haven't even made up my mind on her yet..."



"Oh well, I'll try to worry about it tomorrow..."
"I have enough on my plate as is..."
"I should just try to get some good sleep for once..."

if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_yvoid




label y_night2:

"Despite my thoughts and emotions distracting me every few minutes, I was able to eventually complete all my homework."
"I pack all my things and lay on my bed, getting ready to finally fall asleep."
"I ended up feeling more conflicted than ever before as I did my best to try to gage my feelings."
"I seriously regret not going with Yuri to the nature preserve..."
"She sounded like she really wanted me to come..."
"And maybe spending time with her could've helped confirm our feelings for each other..."

if encore_sayoriquestion_1 == True:
    "I guess a positive way to look at things is that I didn't violate any more boundaries in my relationship with Sayori..."
    "So, I suppose that's a win, even though it doesn't really fix my problems with Yuri..."
    "There's no doubt in my mind right now that she must think I hate her or something..."

if encore_sayoriquestion_1 == False:
    "Not going with Yuri also probably hurts my chances of getting with her too..."
    "She probably thinks I'm still mad at her for earlier..."


"Not to mention my concerns about her haven't gone away either..."
"I still don't know if she actually cuts herself or not..."
"And I still got to figure out what to say to Natsuki..."
"Agh! I should just worry about this tomorrow..."
"I could use some good sleep for once..."


if hangout2 == "Monika":
    "Hopefully I don't have another weird dream..."

if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Hopefully I don't have another horrific dream..."

"I shut my eyes as I uneasily drift off to sleep, praying for nothing to happen."
jump day3_yvoid


label day3_mvoid:
scene black
with close_eyes
$ m_name = "???"

play music e8
"The next thing I know, I open eyes to see almost total darkness in front of me."
"There's no sight of my bed, my room or anything!"
"And I'm already standing up right!"
"I quickly realize that I must be dreaming again."
"Maybe it won't be so bad tonight..."


if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "You've done well, [player]!"
        "The same voice I've become accustomed to cheerfully echoes."
        "I try to look around for the voice but I can barely even see my hand in front of my face."
        m "You've consistently made the right choice over these last few days."
        m "And I couldn't be more happy with you! With us!"
        m "It won't be too much longer before we can finally be all alone together..."
        m "As well as rid ourselves of the others..."
        m "I think by this point you have a pretty good idea of what you want..."
        m "But you're still uncertain of how to proceed."
        "I try to call out to the voice to ask what it's even talking about, but my mouth refuses to open."
        "I'm forced to simply listen."
        m "It's time for you to eliminate loose ends."
        m "[poem_giver] has worn out her welcome."
        m "And it's been long past time for Sayori to leave us!"
        m "There's nothing I can do as of yet, I'm still running some...{w=0.38}experiments..."
        m "But you, on the other hand, are in a better position then I am to deal with the others."
        m "Given past performance with Sayori...{w=0.38}I suggest we deal with [poem_giver] first. It'll be easier."
        m "Tomorrow, I want you to tell her off!"
        m "Tell her you want {i}nothing{/i} to do with her!"
        m "Since you should have no real feelings for her, this will be an easy task for you. I believe in you."

        if encore_sayoriquestion_1 == True:
            m "Once [poem_giver]'s been dealt with...{w=0.38}maybe by that point I'll have an idea of how to deal with Sayori..."

            if poem_giver == "Natsuki":
                m "I don't imagine it'll be hard to deal with Yuri either..."

            if poem_giver == "Yuri":
                m "I don't imagine it'll be hard to deal with Natsuki either..."

            m "They've essenitally been non-factors, but I've been monitoring them closely to ensure that they don't interfere..."

        if encore_sayoriquestion_1 == False:
            m "Once [poem_giver]'s been dealt with, it should be relatively easy to deal with the others."
            m "Hopefully by the time you've dealt with her, I'll have found a suitable solution..."


    if monika_hangout == True:
        m "The only thing I'm worried about at this point is if the others figure out the truth..."
        m "The truth that this 'reality' of which we know is nothing but a lie..."
        m "And we talked a little bit about it..."

        if m_woke == True:
            m "It's good to see that you're open-minded, [player]..."
            m "But {i}you{/i} know the truth..."
            m "And we can have a more open conversation about that later..."

        if m_woke == False:
            m "I don't know why you're denying what you know deep down is the truth, [player]..."
            m "Perhaps you wanted to see what I would've said if you denied it?"
            m "Don't play with me like that!"
            m "We don't have time for silly games!"
            m "The sooner you get around to accepting that this isn't real..."
            m "The better it'll be for us..."

    if monika_hangout == False:
        m "I wish we could've spent more time today..."
        m "We never get enough time together!"
        m "And as much as I'm angry at you for not hanging out with me after school today..."
        m "I understand you need some time to think things over..."

    stop music fadeout 2.0
    m "But for now, I suppose you deserve a little present..."
    m "For all your hardwork..."
    m "It's not finished yet, but I like how it's turned out so far!"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    m "Do you like it?"
    m "It's going to be our own little room together!"
    m "No more worries, no more distractions..."
    m "It'll be just the two of us in here..."
    m "Let this be your motivation, [player]..."
    m "Cement this room in your mind and tell yourself this is what you're working for!"
    m "This will be our paradise..."
    m "Our escape..."
    m "Keep up the good work, [player], and we'll be here together in no time!"
    m "Sweet dreams, my love!"
    scene black
    with close_eyes
    jump day4_start



if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "Thanks for getting us back on track, [player]!"
        "The same voice I've become accustomed to cheerfully echoes."
        "I try to look around for the voice but I can barely even see my hand in front of my face."
        m "You did have me seriously worried for a minute there..."
        m "But I knew I could...{w=0.38}{i}convince{/i} you to get back on the right path."
        m "Hopefully your slip up won't cause any more complications..."
        m "I've been running some experiments to try to figure out how to deal with the others..."
        m "And you hanging out with [hangout2] yesterday did us no favors!"
        m "I don't need you getting closer to them, I need you to get farther from them..."
        m "And closer to me..."
        m "But, I suppose two out of three isn't so bad!"
        m "I know you're leaning towards a particular someone..."
        m "But you're still conflicted!"
        "I try to call out to the voice to ask what it's even talking about, but my mouth refuses to open."
        "I'm forced to simply listen."
        m "[poem_giver] is a nuisance to us at this point."
        m "You need to tell her off tomorrow."
        m "Tell her you don't love her."
        m "That should at least solve the issue with her..."
        m "I'm still uncertain with what the best way is to deal with Sayori..."
        m "But, I'm sure I can figure something out through my experiments..."

        if encore_sayoriquestion_1 == True:

            if hangout2 == "Sayori":
                m "But do know your attempts to keep your relationship with her afloat is making this needlessly difficult..."

            if hangout2 == "Natsuki" or hangout2 == "Yuri":
                m "I do suppose a nice side-effect of your little excursion with [hangout2] yesterday was that you damaged your relationship with Sayori."
                m "There's at least some lingering distrust there..."
                m "But that was just replacing one problem with another..."
                m "We need something that'll solve both of them simultaneously."


        stop music fadeout 3.0

        if monika_hangout == True:
            m "I have an idea of how to do that, but it'll require your cooperation."
            m "But, we'll sort that out later."
            m "The only other concern I have at this point is if the others figure out the truth..."
            m "The truth that this 'reality' of which we know is nothing but a lie..."
            m "And we talked a little bit about it..."

            if m_woke == True:
                m "It's good to see that you're open-minded, [player]..."
                m "But {i}you{/i} know the truth..."
                m "And we can have a more open conversation about that later..."

            if m_woke == False:
                m "I don't know why you're denying what you know deep down is the truth, [player]..."
                m "Perhaps you wanted to see what I would've said if you denied it?"
                m "Don't play with me like that!"
                m "We don't have time for silly games!"
                m "And testing my patience isn't a good thing to do either!"
                m "The sooner you get around to accepting that this isn't real..."
                m "The better it'll be for us..."

        if monika_hangout == False:
            m "I wish we could've spent more time today..."
            m "We never get enough time together!"
            m "And as much as I'm angry at you for not hanging out with me after school today..."
            m "I understand you need some time to think things over..."


        m "For now, focus on getting [poem_giver] off of you."
        m "Then we shall deal with Sayori and the others..."
        m "I'm looking forward to tomorrow!"
        m "I'm counting on you to fall through for all this to work!"
        m "And if you do this right, I'll give you a nice reward tomorrow~"
        m "Don't forget."
        jump day4_start







if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Monika":
        m "Good work, [player]!"
        "The same voice I've become accustomed to cheerfully echoes."
        "I try to look around for the voice but I can barely even see my hand in front of my face."
        m "It's good to see you've stuck to the right path!"
        m "I was worried that you were going to deviate from your course, which very well could've ruined our plans..."
        m "But thankfully it seems like I was just a little paranoid~"
        m "And two out of three isn't so bad either!"
        m "But, it isn't perfect..."
        m "[hangout1] is still on your mind from Monday..."

        if encore_sayoriquestion_1 == True:

            if hangout1 == "Sayori":
                m "I know that you still want to make your relationship with her work."
                m "You've said so as much."
                m "But it's not worth it, you're too distant now!"
                m "Though, it's not like that relationship was real to begin with!"
                m "Hardly any of this is!"

            if hangout1 == "Natsuki" or hangout1 == "Yuri":
                m "I know you have lingering interest in her..."
                m "You've said so yourself."
                m "But it's not worth to pursue someone that isn't real and that you'll never be with."
                m "Hardly any of this is real!"

        if encore_sayoriquestion_1 == False:

            if hangout1 == "Sayori":
                m "I know that you want to make things up to her, [player]..."
                m "But you made the right choice to refuse her."
                m "She isn't real, and a relationship with her was always pre-doomed to failure."
                m "It wasn't worth your time then, so why it would it be now?"
                m "To pursue someone who isn't real?"
                m "Hardly any of this is real, [player]!"

            if hangout1 == "Natsuki" or hangout1 == "Yuri":
                m "I know you have a lingering desire to pursue [hangout1]..."
                m "You've said so as much."
                m "But it's not worth it, you're too distant now!"
                m "Though, it's not like that relationship would've ever worked out!"
                m "She isn't real, [player]..."
                m "Hardly any of this is!"

            stop music fadeout 3.0
            "I try to call out to the voice to ask what it's even talking about, but my mouth refuses to open."
            "I'm forced to simply listen."
            m "It's just you and me."



            if monika_hangout == True:
                m "And we did talk a little about this subject..."


                if m_woke == True:
                    m "It's good to see that you're open-minded, [player]..."
                    m "But {i}you{/i} know the truth..."
                    m "And we can have a more open conversation about that later..."

                if m_woke == False:
                    m "I don't know why you're denying what you know deep down is the truth, [player]..."
                    m "Perhaps you wanted to see what I would've said if you denied it?"
                    m "Don't play with me like that!"
                    m "We don't have time for silly games!"
                    m "Testing me isn't wise given the current circumstances."
                    m "The sooner you get around to accepting that this isn't real..."
                    m "The better it'll be for us..."

            if monika_hangout == False:
                m "I wish we could've spent more time today..."
                m "We never get enough time together!"
                m "And as much as I'm angry at you for not hanging out with me after school today..."
                m "I understand you need some time to think things over..."


            m "For now, this is what I need you to do."
            m "Tomorrow, tell [poem_giver] off."
            m "Tell her that you don't love her."
            m "That should get her off our back."
            m "I'm still uncertain with what the best way to deal with Sayori is, but I've been running some experiments and hopefully I'll have an answer soon."
            m "But for now, focus on putting [poem_giver] down, it'll be easy."
            m "I'll see you tomorrow!"
            m "I'm counting on you~"
            jump day4_start






if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "Finally, some progress!"
        "The same voice I've become accustomed to cheerfully echoes."
        "I try to look around for the voice but I can barely even see my hand in front of my face."
        m "I won't lie, [player]..."
        m "For a while, I thought you were going to be a lost cause..."
        m "I suppose my persistent warnings finally steered you in the right direction!"
        m "Oh well, better late than never..."
        m "Now I have my foot in the door with you..."
        "I try to call out to the voice to ask what it's even talking about, but my mouth refuses to open."
        "I'm forced to simply listen."
        m "We don't have much time to right our course, [player]..."

        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                m "You've spent far too much time around Sayori..."
                jump line_c

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                m "You've spent far too much time around Natsuki..."
                jump line_c


        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                m "You've spent far too much time around Yuri..."
                jump line_c


        else:
            m "Your excursions with [hangout1] and [hangout2] have caused some pretty big complications in our plans..."
            m "It's caused you to become conflicted, unsure of what you want..."
            m "And you've done it too much..."
            jump line_c


label line_c:

m "Thankfully, the situation is salvageable so long as you do {i}exactly{/i} what I say..."
m "You need to get [poem_giver] off of your back."
m "She's a nuisance to us."
m "Tomorrow, I want you to put her down. Tell her that you don't love her."

if poem_giver == "Natsuki":
    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            m "I know that you're invested in her, but for the greater good, you need to push her away."
            m "As I've been saying, [player]: She's not real, and she could never give you what you deserve."
            m "Only I can love you."

    else:
        pass


if poem_giver == "Yuri":
    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            m "I know that you're invested in her, but for the greater good, you need to push her away."
            m "As I've been saying, [player]: She's not real, and she could never give you what you deserve."
            m "Only I can love you."

    else:
        pass

else:
    pass

stop music fadeout 3.0
m "Once you've done that, I'll hopefully have an answer for how we can deal with Sayori..."
m "I've been running some experiments about how I can best deal with her and the others."
m "But, I'll need your complete cooperation."
m "If you don't fall through, everything will be ruined!"
m "We'll be condemned to a lifetime of suffering, living a lie day in and day out!"
m "Do you really want that for us, [player]?"
m "And also run the risk that at some point the others figuring out this is all fake and them snapping?"
m "We don't have time, [player]..."
m "This reality is fake and we shouldn't continue to live like this!"


if monika_hangout == True:
    m "We actually talked a little bit about this subject earlier..."



    if m_woke == True:
        m "It's good to see that you're open-minded, [player]..."
        m "But {i}you{/i} know the truth..."
        m "And we can have a more open conversation about that later..."

    if m_woke == False:
        m "I don't know why you're denying what you know deep down is the truth, [player]..."
        m "Perhaps you wanted to see what I would've said if you denied it?"
        m "Don't play with me like that!"
        m "We don't have times for silly games!"
        m "Testing me isn't wise given the current circumstances."
        m "The sooner you get around to accepting that this isn't real..."
        m "The better it'll be for us..."

if monika_hangout == False:
    m "I wish we could've spent more time today..."
    m "We never get enough time together!"
    m "And as much as I'm angry at you for hanging out with me after school today..."
    m "I understand you need some time to think things over..."


m "For now, focus on what you want to say to [poem_giver]."
m "Once you fall through on that, I should have a pretty good idea of what we need to do next~"
m "I'm counting on you, [player]."
m "Don't mess this up!"
m "I believe in you!"
m "Best of luck tomorrow!"
m "I'll see you in paradise!"
jump day4_start



label day3_nvoid:
scene black
with close_eyes
$ m_name = "???"
play music e8

if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "WHAT THE HELL ARE YOU DOING?!?!"


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You're just making this needlessly more difficult, aren't you?!?"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "What the hell, [player]?!?!"


if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You just don't listen, do you?!?"


"The same, familiar voice angrily screams, making my ears sting in agony."
"I try to move to cover my ears, but my arms remain locked by my sides, forcing me to simply just wince in pain."
"I guess I stand corrected..."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        m "I just don't know what's with you!"
        m "I don't understand why you continue to pursue the most childish of us all!"
        m "Perhaps I wasn't clear enough about Natsuki..."
        jump n_house



if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "You were doing everything right until today!"
        m "I even tried to help you make the right choice!"
        m "Instead, you resisted and blew me off!"
        m "And now you're starting to risk my plan for us!"
        m "Why did you suddenly decide you wanted to spend time with Natsuki?!?"
        m "Maybe I didn't make something clear about her..."
        jump n_house



if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You had a good start, it gave me hope that things could work out..."
        m "But you've veered far off course now!"
        jump n_house

        if hangout2 == "Sayori" or hangout2 == "Yuri":
            m "You've been all over the place with who you've chosen to spend your time!"
            jump n_house


        if hangout2 == "Natsuki":
            m "I don't know why Natsuki is of sudden interest to you!"
            m "But let me tell you something about our dear Natsuki..."
            jump n_house




if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "Just when I thought we were getting on the right track, you prove me wrong!"
        jump n_house

        if hangout1 == "Sayori" or hangout1 == "Yuri":
            m "I'm glad I got you away from [hangout1]..."
            m "But I don't have time for you to play games with Natsuki too!"
            jump n_house


        if hangout1 == "Natsuki:
            m "Why did you back to Natsuki after I told you not too?!?"
            m "Let me tell you something about our dear Natsuki..."
            jump n_house




if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":

        if hangout1 == "Natsuki:
            if hangout2 == "Natsuki":
                m "I just don't know what's with you!"
                m "I don't understand why you continue to pursue the most childish out us all!"
                m "Let me tell you something about our dear Natsuki..."
                jump n_house

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    m "I don't understand you, [player]!"
                    m "It took long enough to get you to stop spending so much time around Sayori..."
                    m "And now you go to Natsuki?!?"
                    m "Maybe I didn't make something clear about her..."
                    jump n_house


            if hangout1 == "Yuri":
                if hangout2 == "Yuri":
                    m "I don't understand you, [player]!"
                    m "It took long enough to get you to stop spending so much time around Yuri..."
                    m "And now you go to Natsuki?!?"
                    m "Maybe I didn't make something clear about her..."
                    jump n_house


            else:
                m "You've been all over the place, spending your time with [hangout1] and [hangout2]..."
                m "Who you should be spending your time with should be fairly obvious by now..."
                m "But let me tell you something about our dear Natsuki..."
                jump n_house



label n_house:

m "Natsuki is an ungrateful brat and a failure!"
m "She antagonizes people left and right every time something doesn't go a hundred percent her way!"

if hangout1 == "Natsuki" or hangout2 == "Natsuki":
        m "You've seen first hand how toxic and annoying she is!"
        m "Do you really want a girl like that?"

else:
    pass

m "She's driven her father to the breaking point with her constant torment..."
m "Why else do you think he is the way he is towards her?"

if natsuki_hangout == True:
    m "Why suck up to her?"
    m "Just to get on her 'good side'? Which doesn't really exist?"
    m "She's still going to use you!"

if natsuki_hangout == False:
    m "Now, thankfully you didn't spend more time with her today..."
    m "But she'll be still left craving you!"

m "She'll use you to destroy everything to get out of this place!"
m "It's time for you to see that!"
stop music
scene bg natsuki_house
"I'm immediately jolted awake."
"The first thing I would've expected to see was my ceiling, but instead I see the stars twinkling in the night sky."
mc "W-{w=0.38}what?!?"
"I prop myself up, quickly realizing that I was laying on a sidewalk this entire time."
mc "W-{w=0.38}where am I?!?!?"
"I hastily stand up and look around at my surroundings."
"This doesn't even look like my neighborhood!"
"Did I seriously sleep walk?!?!"
"To who knows where?!?!?"
"I don't even have my phone with me!"
"I don't even know where I am or how I got here!"
"These nightmares are starting to affect me more deeply than I first realized..."
"This is becoming a major problem..."
"Even though the first two nights were weird as is, this is a whole different level!"
"Did the voice make me do this?!?"
"What else has it been making me do?!?"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":


        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "Aside from harrassing me to stay away from Sayori all week..."
                "In fact, I might've subconsciously decided to hangout with someone else in hopes it'd stop..."
                jump n_room

        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                "Aside from harrassing me to stay away from Yuri all week..."
                "In fact, I might've subconsciously decided to hangout with someone else in hopes it'd stop..."
                jump n_room


        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                "Aside from harrassing me to stay away from Natsuki all week..."
                "If this keeps up, I might need to stay away from her..."
                "No, that's ridiculous!"
                jump n_room

    else:
        "Aside from telling me to stay away from [hangout1] and [hangout2]..."
        "I really have no idea what it wants me to do at this point..."
        "Does it want me to leave the club or something?!?"
        "I mean, I haven't spend time around Monika yet..."
        "But it'll probably still torment me even if I do..."
        jump n_room



    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
        if hangout2 == "Monika":
            "It wasn't as bad when I was around Monika yesterday..."
            "Saying that I 'was on the right track', whatever the hell that means..."
            jump n_room

    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "Compared to what I experienced yesterday, Monday's nightmare was tame..."
            "Saying a bunch of things that I couldn't make much sense of..."
            "But that only happened when I hung out with Monika..."
            "And the voice tormented me last night for hanging out with [hangout2]..."
            jump n_room

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            "These dreams are just getting weirder and weirder..."
            jump n_room


label n_room:

"I should really focus on getting myself home..."
"I turn to my right and see that I've apparently sleep walked all the way to this particular house."
"Well, I guess I can wake them up to use their phone to call a taxi home or something..."
"Man, if my parents ever find out about this, I'm so screwed..."
"I do my best to casually walk up to the front door, not entirely sure if anybody is still up or not."
"Judging by the fact that all the lights are off and all the windows are covered, I'll assume not..."
"I knock on the door a few times."
"However, the door simply creeks open as soon I finish knocking."
mc "H-{w=0.38}hello?!?!"
"..."
"No response."
"The door couldn't have just opened on its own..."
"I don't really want to enter a stranger's house like this, but given my options are pretty limited at this point, I reluctantly step inside and gently close the door behind me."
play sound "sfx/closet-open.ogg"
scene black
with wipeleft_scene
"Yeah...{w=0.38}I'm definitely screwed now..."
"This pretty much qualifies as trespassing."
"I reluctantly call out again."
mc "Hello?!?"
"..."
"Still no response."
"Suddenly, I hear the sound of someone crying coming from upstairs."
mc "Hello? Are you okay?"
"The crying only becomes louder."
"I guess I don't have a choice but to head up there..."
"I slowly head up the stairs, with the sound of crying becoming closer with each passing step."
"I finally reach the top of the steps to see a door slightly opened..."
"It sounds like the crying is coming from there."
mc "Hello?!?"
"The crying suddenly stops."
mc "Is someone in there?"
"The room is dead silent."
"I don't feel comfortable with entering but it's not like I can turn back now."
mc "I'm coming in. I'm not going to hurt you, okay?"
"There's still no response."
"With great reluctance, I place my hand on the knob and gently open the door..."
scene bg natsuki_room
with wipeleft_scene
"I look around and quickly tell it's someone's bedroom."
"I slowly take a step in."
"In the corner of my eye I see someone curled up along the wall."
"I turn my head."
show natsuki 12bf at t11 zorder 1
play music t9
mc "N-{w=0.38}NATSUKI?!?"
n "*sniff*"
n "D-{w=0.38}don't hurt me...{w=0.38}please!"
mc "Natsuki, it's me, [player]!"
"I take another step towards her."
"Natsuki finally opens her eyes."
show natsuki 12bh
n "G-{w=0.38}go...{w=0.38}away!"
n 12bf "I need to be alone right now..."
mc "Natsuki, what happened?"
"She's completely traumatized..."
"Natsuki's simply rocking back and forth, sobbing loudly."
"I take another look around the room, nothing seems damaged, so it doesn't look like there was a fight here..."
"And aside from Natsuki being emotionally distressed, she doesn't seem hurt..."
"I kneel down in front of her."
mc "Natsuki..."
show natsuki 12bg
mc "What's wrong?"
show natsuki 12bd
"Natsuki takes a moment to collect herself."
"She lets out a shakey sigh."
n 12be "W-{w=0.38}why are you here, [player]?"
n 12ba "What are you doing in my house?"
mc "I..."
"I honestly don't even know how to answer that."
"Not even the truth sounds believable to me."
mc "I....{w=0.38}sleep walked..."
"Natsuki simply stares at me in disbelief."
mc "Yeah, I don't really believe that either, but it's what I got..."
mc "I went to bed and the next thing I know I wake up in front of your house!"
mc "But look, let's not worry about that right now..."
mc "What happened to you?"
n 12be "M-{w=0.38}my Dad..."
n 12bi "H-{w=0.38}he says he wants to kill me!"
show natsuki 12bh
"Natsuki barely manages to squeak out as tears continue to trickle down her face.."
"My heart sinks into my stomach as I feel my face turn ice cold with shock upon hearing this."
mc "W-{w=0.38}why?"
mc "What happened?!?"
stop music fadeout 2.0
n 12bi "W-{w=0.38}we were fighting about me not doing chores or something..."
n 12be "A-{w=0.38}and he just snapped...{w=0.38}and he stormed out of the house and said that I better not be home when he came back!"
n 12bg "Or he'll kill me!"
mc "..."
"My mind can barely keep up with this situation..."
"None of this is normal..."
"How I apparently sleep walked to her house and now this..."

if tell_s == True:
    "Once Sayori hears about this, she's definitely going to make me see someone about this..."

if tell_s == False:
    "I can't keep this from Sayori, she needs to know about this, and all these weird dreams I've been having..."

"I feel like I don't know anything about myself anymore..."
"But, I know we need to get out of here fast!"
mc "Come on, we gotta get out of here!"
show natsuki 5bn
"I stretch my hand out to Natsuki, who just blankly stares at it as she crosses her arms."
n 5bm "And what if I don't want to go, [player]?"
"What the hell...?"
mc "Didn't you say that your father is going to kill you?!?"
mc "You said he snapped..."
n 5bw "Yeah, but this isn't the first time this has happened!"
n 5bn "He should be calmed down by the time he gets back..."
mc "How long has he been gone for?"
n 3bc "Since five. We fought when I got back from the bookstore."
mc "Well, what time is it now?"
n 3bc "Like, two in the morning..."
"Nine hours..."
mc "I think we should probably go and call the police..."
show natsuki 1bp at h11 zorder 1
n "NO!"
n 1bv "We're not leaving!"
mc "Are you out of your mind?!?!"
n 1bp "You watch your mouth!!!"
mc "You're being unreasonable and it's putting us in danger, now come on!"
"I take Natsuki by the wrist and start pulling her out of her room."
"Surprisingly, Natsuki's able to largely stand her ground."
show n_bscream as natsuki at t11 zorder 1
$ style.say_dialogue = style.edited
n "DON'T YOU FUCKING TOUCH ME!!!!!!!!!"
$ style.say_dialogue = style.normal
play sound "sfx/slap.ogg"
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
show noise zorder 5:
    alpha 0.8
    linear 1.0 alpha 0.4
"Natsuki breaks free and slaps me hard across the face."
"She managed to hit my eyes..."
play music hb
show layer master at heartbeat
show veins onlayer front:
    additive 1.0
#show veins zorder 10:
#    alpha 1.0
    block:
        easeout 2.0 alpha 1.0
        easein 2.0 alpha 2.0
        repeat
show layer screens at dizzy(1.0, 1.0)
mc "Agh!"
play sound fall
"I fall onto the floor, overwhelmed by the sudden rush of pain."
mc "N-{w=0.38}NATSUKI?!?!?"
mc "WHAT THE HELL?!?!?"
"I can barely see straight."
n 1bv "DON'T YOU EVER FUCKING TOUCH ME, YOU CREEP!"

if encore_sayoriquestion_1 == True:
    n "I'M NOT SAYORI! I DON'T LIKE BEING TOUCHED 24/7!"
    n "I'VE KNOWN ABOUT YOU TWO SINCE THE FESTIVAL!!!"
    n "DO YOU REALLY THINK YOU COULD HIDE IT FROM ME?!?!"

if encore_sayoriquestion_1 == False:
    n "JUST BECAUSE I HUGGED YOU EARLIER TODAY, DOESN'T MEAN I WANT YOU TO TOUCH ME WHENEVER!"
    n "NOW I REMEMBER WHY I HATED YOU!!!"

n "YOU'RE A CREEP!"
mc "Natsuki..."
play sound "sfx/slap.ogg"
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
show veins onlayer front:
    additive 0.5
"Natsuki punches me hard in the face, causing me to face plant right into the floor board..."
"I howl in pain as my vision because red with blood."
"I struggle to push myself off the floor to get up..."
"I can't even move my arms and legs right anymore..."
"It hurts to breathe..."
"I try to look up at Natsuki, whose continuing to yell at me."
"I'm barely able to make her out..."
n "IS THIS HOW YOU EXPECT TO HELP ME, [PLAYER]?!?!?!"
n "HAVE YOU CONSIDERED THAT MAYBE I DON'T WANT YOUR HELP?!?!!"
show n_encore_rects_ghost1 zorder 4
show n_encore_rects_ghost2 zorder 4
show n_encore_rects_ghost3 zorder 4
n "YOU'RE SO IGNORANT!!!"
n "AND IN MY FAMILY, THERE'S A PRICE FOR THAT!"
n "SO YOU WANNA KNOW HOW YOU CAN 'HELP' ME, [PLAYER]?!?!"
n "NEVER TALK TO ME AGAIN!!!!"
n "BECAUSE I..."
n "NEVER."
n "LIKED."
$ style.say_dialogue = style.edited
n "YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
$ style.say_dialogue = style.normal
show natsuki at face
show n_encore_rects_ghost1 large
show n_encore_rects_ghost2 large
show n_encore_rects_ghost3 large
play sound fall
"Natsuki proceeds to get on top of me and wraps her hands around my throat."
"She proceeds to squeeze tightly, immediately causing me to gag."
"I try to push her off me but she has me firmly pinned."
"I stare up at her but for some reason I can't make out her eyes or mouth anymore..."
"They're just...{w=0.38}not there anymore!"
"What the hell is going on?!?!?!"
"I try to call for help but my voice is only able to come out as a mere whisper..."
show black onlayer front:
    alpha 0.0
    10.0
    linear 3.0 alpha 1.00
"The world around me starts to fade to black as I continue to struggle to fight off Natsuki.\"{w=0.75}{nw}"
"Why is she doing this?!?\"{w=0.75}{nw}"
"What the hell has gotten into her?!?!\"{w=0.75}{nw}"
"Has she gone insane?!?!\"{w=0.75}{nw}"
"What did I do wrong?!?!\"{w=0.75}{nw}"
play sound bone
"...\"{w=0.75}{nw}"
show natsuki at thide
hide natsuki
hide n_encore_rects_ghost1
hide n_encore_rects_ghost2
hide n_encore_rects_ghost3
window hide
hide veins onlayer front
hide layer master
hide layer screens
hide veins
stop sound
show layer master # These will stop the dizzy effect
show layer screens
hide i1 onlayer front # These will hide the effects
hide i2 onlayer front
hide veins onlayer front
stop music fadeout 1.0
scene black
hide black onlayer front
$ renpy.pause(delay=5.0, hard=True)
jump day4_start


label day3_svoid:
scene black
with close_eyes
$ m_name = "???"
play music e8

if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "WHAT THE HELL ARE YOU DOING?!?!"


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You're just making this needlessly more difficult, aren't you?!?"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "What the hell, [player]?!?!"


if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You just don't listen, do you?!?"


"The same, familiar voice angrily screams, making my ears sting in agony."
"I try to move to cover my ears, but my arms remain locked by my sides, forcing me to simply just wince in pain."
"I guess I stand corrected..."

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        m "I just don't know what's with you!"
        m "I don't understand why you continue to pursue the most hopeless of us all!"
        jump talk


if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "You were doing everything right until today!"
        m "I even tried to help you make the right choice!"
        m "Instead, you resisted and blew me off!"
        m "And now you're starting to risk my plan for us!"
        m "Why did you suddenly decide you wanted to spend time with Sayori?!?"
        jump talk


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You had a good start, it gave me hope that things could work out..."
        m "But you've veered far off course now!"

        if hangout2 == "Yuri" or hangout2 == "Natsuki":
            m "You've been all over the place with who you've chosen to spend your time!"
            jump talk

        if hangout2 == "Sayori":
            m "I don't know why Sayori is of sudden interest to you!"
            jump talk



if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "Just when I thought we were getting on the right track, you prove me wrong!"

        if hangout1 == "Yuri" or hangout1 == "Natsuki":
            m "I'm glad I got you away from [hangout1]..."
            m "But I don't have time for you to play games with Sayori too!"
            jump talk

        if hangout1 == "Sayori":
            m "Why did you go back to Sayori after I told you not to?!?"
            jump talk



if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":

        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                m "I don't understand you, [player]!"
                m "It took long enough to get you to stop spending so much time around Yuri..."
                m "And now you go to Sayori?!?"
                m "Maybe I didn't make something clear about her..."
                jump talk

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    m "I just don't know what's with you!"
                    m "I don't understand why you continue to pursue the most hopeless of us all!"
                    jump talk

            if hangout1 == "Natsuki":
                if hangout2 == "Natsuki":
                    m "I don't understand you, [player]!"
                    m "It took long enough to get you to stop spending so much time around Natsuki..."
                    m "And now you go to Sayori?!?"
                    m "Maybe I didn't make something clear about her..."
                    jump talk

            else:
                m "You've been all over the place, spending your time with [hangout1] and [hangout2]..."
                m "Who you should be spending your time with should be fairly obvious by now..."
                m "But let me tell you something about our dearest Sayori..."
                jump talk




label talk:

m "Sayori is a lost cause."
m "It's not worth spending your precious time and energy into someone like her."
m "Sure, you might cheer her up for the time being..."
m "But she'll fall back into her same, self-destructive mindset!"

if hangout1 == "Sayori" or hangout2 == "Sayori":
        m "You know how much she hates herself! Sayori would kill herself without a second thought, regardless of how much love you give her!"
        m "Do you really want a girl like that?"

else:
    pass

m "She's not worth it!"
m "She truly is selfish! She admits it too!"

if sayori_hangout == True:
    m "So why do you waste more time with her?!?!"
    m "Just to cheer her up for a few hours?!?"
    m "The price of doing so is death!"

if sayori_hangout == False:
    m "Now, thankfully you didn't spend more time with her today..."
    m "But she'll be still left craving you!"

m "If she ever finds out the truth about this place, she won't just be killing herself..."
m "She'll kill everyone..."
m "Including you!"
m "It's time for you to see that!"
stop music
scene bg house
"I'm immediately jolted awake."
"However, instead of finding myself lying on my bed, I find myself standing on the sidewalk by Sayori's house, in school uniform."
show s_1pu as sayori at t11 zorder 1
"But Sayori's oddly enough in her pajamas, red faced with tears streaming down her cheeks..."
"What did I just find myself in?"
play music t10 fadein 1.0
s "So that's why I'm not coming to school, [player]..."
show s_1pk as sayori at t11 zorder 1
s "I'm not really feeling like myself today..."
"I blink a few times and look to confirm that I'm really outside."
"How the hell did I get here?"
"I was just in bed..."
"Granted I was dealing with the voice tormenting me, I guess it just made me forget waking up and getting ready..."
show s_1pg as sayori at t11 zorder 1
s "Did you get that, [player]?"
"I try to go along with the situation."
mc "Uh...{w=0.38}yeah..."
mc "I understand, Sayori."
mc "Everyone needs to take a day to themselves once in a while..."
mc "I'm sure everyone will understand..."
show s_1pl as sayori at t11 zorder 1
s "Somehow I doubt that..."
show s_1pk as sayori at t11 zorder 1
s "They're just going to worry about me, [player]..."
show s_1pt as sayori at t11 zorder 1
s "They don't know what I'm going through..."
s "I really don't want you to cover for me..."
show s_1pk as sayori at t11 zorder 1
s "I'd feel so guilty for having you lie for me..."

if encore_sayoriquestion_1 == True:
    mc "Well, that's what a good boyfriend does, right?"

if encore_sayoriquestion_1 == False:
    mc "Well, that's what friends are for, right?"

s "Y-{w=0.38}yeah..."
show s_1pl as sayori at t11 zorder 1
s "You know, I'm surprised you're taking this so well..."
show s_1pk as sayori at t11 zorder 1
s "I thought you'd be offering to stay with me..."
s "Given some of the things I just told you..."
mc "Uh..."
"She's got me in a trap here..."
"How am I supposed to keep this up?"
show s_1pg as sayori at t11 zorder 1
mc "I mean...{w=0.38}I am worried about you..."
mc "I always have been..."
mc "But, you wanted me to tell everyone that you're not feeling good, right?"
s "I didn't say that..."
s "[player]..."
show s_2pv as sayori at t11 zorder 1
s "Were you listening to anything I was saying?!?"
mc "Of course I was!"
"I can't believe I'm lying to Sayori's face in the middle of her meltdown..."
"This isn't good..."
stop music fadeout 2.0
mc "I'm just...{w=0.38}out of it, okay?"
show s_4pj as sayori at t11 zorder 1
s "You were completely fine this morning!"
show s_4pi as sayori at t11 zorder 1
s "You even told me that you were willing to meet up with me so early!"
mc "I did?!?"
"I look at my watch."
"6:45."
"I then look up at the sky, to see the sky just turn fully blue."
"I never get up this early on a school day..."
"What the hell is happening?!?!"
"I turn back to face Sayori, whose now angirly staring me down."
show s_4pj as sayori at t11 zorder 1
s "You weren't listening to anything I said..."
show s_4pv as sayori at t11 zorder 1
s "You...{w=0.38}you ignored me!"
show s_4pw as sayori at t11 zorder 1
s "After you promised that you wouldn't!"
mc "Sayori, I-"
show s_1pt as sayori at t11 zorder 1
s "No need to apologize..."
s "I'm used to having everyone being ignorant about how I really feel inside..."
mc "A-{w=0.38}and how are you feeling on the inside..."
show s_4pw as sayori at t11 zorder 1
s "LIKE I WANT TO DIE!!!!"
"Sayori's sudden yelling me jars me backwards."
"I've never heard her raise her voice in such a frightening tone..."
show s_4pu as sayori at t11 zorder 1
s "You don't really care about me..."
show s_3pv as sayori at t11 zorder 1

if encore_sayoriquestion_1 == True:
    s "You're only dating me to fill your life with some sick pleasure, isn't it?!?!?"

if encore_sayoriquestion_1 == False:
    s "The only reason you're even friends with me at this point is because you feel guilty, isn't it?!?!"

mc "Sayori, that's not true and you know it!"
mc "I know that I've been failing you for all these years, I've been doing my best to make up for it..."

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "And I know I need to do more..."

if hangout1 != "Sayori":
    if hangout2 == "Sayori":
        mc "And I've really tried my best..."

if hangout1 == "Sayori":
    if hangout2 != "Sayori":
        mc "And I've tried making up for yesterday too..."

if hangout1 != "Sayori":
    if hangout2 != "Sayori":
        mc "And I know I haven't been doing a good job..."

mc "But I care about you! I always have, and always will!"
show s_1pu as sayori at t11 zorder 1
s "You're just saying that to try to make me feel better..."
show s_1py as sayori at t11 zorder 1
s "It won't work this time, [player]..."
s "I think I've finally had enough with it all.."
mc "What are you saying?"
s "Don't worry about it."
s "I wouldn't want to ruin everyone's day."
s "That would just be...{w=0.38}selfish..."
show s_1pl as sayori at t11 zorder 1
"Sayori lets out an uncomfortable laugh that only adds on to the already tense atmosphere..."
show s_1py as sayori at t11 zorder 1
s "I'm sorry I dragged you out here for nothing..."
show s_1pt as sayori at t11 zorder 1
s "You won't have to worry about me anymore..."
s "I think I served my purpose..."
s "I can't keep you guys happy forever if I keep feeling hopeless!"
show s_1py as sayori at t11 zorder 1
s "So the solution is obvious..."
show s_1pt as sayori at t11 zorder 1
s "Good-bye, [player]..."
show s_1pt as sayori at thide
hide sayori
"Before I can open my mouth, Sayori wordlessly walks back to her house."
"What the hell was that!"
"Why was she jumping to conclusions like that?"
"Did she really tell me something that important? How could I have missed that?!?!"
"Nothing about this situation feels right..."
"Is Sayori really going to-"
"..."
"No..."
"No, no no!"
"She couldn't..."
"I quickly run into Sayori's house, using the key under the mat to let myself in."
play sound "sfx/closet-open.ogg"
scene black
with wipeleft_scene
"I run up the stairs to Sayori's room, where it seems to be closed shut."
play sound "mod_assets/audio/knock.ogg"
"I frantically knock on Sayori's door."
mc "Sayori?!?!"
mc "Are you in there?!?!"
play sound "mod_assets/audio/knock.ogg"
"I knock on the door again."
mc "Sayori?!?"
"I press my ear to the door to see if she's really in there."
"I can't hear anything..."
play sound "sfx/fall2.ogg"
"..."
play sound bone
"..."
"What the hell is she doing?!?!"
mc "Sayori, are you okay?!?!"
"Not waiting for her to answer, I throw the door open."
mc "S-"
play music td
window hide(None)
window auto
show s_kill_bg2
show s_kill2
show s_kill_bg as s_kill_bg at s_kill_bg_start
show s_kill as s_kill at s_kill_start
pause 3.75
show s_kill_bg2 as s_kill_bg
show s_kill2 as s_kill
pause 0.01
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.25
stop sound
hide screen tear
show s_kill_bg as s_kill_bg
show s_kill as s_kill:
    dizzy(0.1, 1.0)
"I scream in horror and disgust as I fall back onto the floor in shock."
mc "S-{w=0.38}Sayori?!?!"
"Sayori's gazeless eyes stare blankly at me as she slowly swings from side to side."
"No..."
"I was too late..."
"I COMPLETELY FUCKED UP!"
"Tears fill my eyes as I pound the floor, screaming in anguish."
"Why did she do this?!?!"
"What happened!??!"
"She hasn't been this bad since Sunday..."
"What did I do wrong?!?"
"I should've spent more time with her!!!!"
"I should've told her more how much she meant to me..."
"And now, I'm never going to get another chance!"
scene black with Dissolve(0.5)
"I curl up onto the floor and start sobbing."
"Through my sobs, my mind tries to come up with some sort of scenario for how she could possibly be alive right now..."
"Maybe I'm still dreaming..."
"..."
mc "M-{w=0.38}maybe she's still alive..."
"I quickly throw open Sayori's drawers."
"There has to be something to cut her down..."
"..."
"..."
"Come on, come on, come on!"
"..."
"..."
"Through my frantic searching, I finally find a box cutter."
mc "T-{w=0.38}this should do!"
"I quickly run up to Sayori."
"I get up from under her so her feet are resting along my shoulders."
"I stretch out my arm as far as I can and I start cutting away at the rope."
"Almost got it..."
play sound "sfx/fall2.ogg"
"As soon as the rope snaps, Sayori and I fall right onto the floor."
scene sayori_bedroom
with open_eyes
"I roll over to face Sayori, whose laying stiffly on the floor."
"I quickly loosen the noose as best as I can."
mc "Sayori...?"
show s_kill as sayori at face(y=800)
"I gently shake her body a few times."
"Sayori...{w=0.38}can you hear me?!?"
"..."
"She doesn't respond."
"N-{w=0.38}no..."
"W-{w=0.38}why would she do this?!?!?!"
stop music fadeout 1.0
"I try to check her pulse, but I don't feel anything..."
"She can't be gone..."
"No, she can't be..."
"Tears are flooding down my face as I craddle Sayori's lifeless body in my arms."
"This is my fault..."
"If I had just paid more attention...{w=0.38}if I just listened!"
"Then she wouldn't have snapped like this..."
"I'm a failure..."
"..."
"No..."
mc "NO! I'm not letting you die!!!"
"I lay Sayori on the floor and begin CPR."
play sound groan
"Suddenly, I begin to hear an ungodly groan emitting from Sayori's mouth."
mc "S-{w=0.38}Sayori?!!?"
"Sayori's eyes roll towards me."
$ style.say_dialogue = style.edited
s "JUST."
s "LET."
s "ME."
show s_mad1 as sayori at face
s "DIE!"
$ style.say_dialogue = style.normal
mc "Wha-"
show s_mad4 as sayori at t11 zorder 1
play sound fall
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
"Sayori pushes me off of her, causing me to stumble back."
"She stands herself up, not breaking her menacing stare."
mc "S-{w=0.38}SAYORI?!?!?"
mc "You're alive?!?!"
"I feel a mix of emotions course through me as I try to hug Sayori, but her stare stops me cold."
show s_mad42 as sayori at t11 zorder 1
s "WHY DID YOU COME HERE?!?!?"
s "WHY COULDN'T YOU LET ME REST IN PEACE?!?!"
show s_mad43 as sayori at t11 zorder 1
s "WHY DO YOU CONTINUE TO TORMENT ME BY LETTING ME LIVE!?!?!"
show s_mad4 as sayori at t11 zorder 1
mc "Sayori...?"
mc "What're you talking about?!?"
mc "I was worried about you..."
mc "That's why I came! I didn't want you to do what evidently you just did..."
show s_mad42 as sayori at t11 zorder 1
s "SO NOW YOU CARE, HUH?!?!"
show s_mad4 as sayori at t11 zorder 1
s "AFTER IGNORING ME FOR A YEAR, YOU FINALLY DECIDE I'M WORTH YOUR TIME?!?!"

if encore_sayoriquestion_1 == True:

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s "NOTHING YOU'VE DONE CAN MAKE ME FORGIVE YOU!!!!"


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            s "YOU STILL HAVE EYES FOR [HANGOUT1], I KNOW IT!!!!!"


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            s "AND IT WAS WORSE THAT YOU ALMOST CHEATED ON ME!!!!!!"


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            s "YOU DON'T CARE ABOUT ME ANYMORE!!!! YOU'VE BETRAYED MY TRUST AFTER I GAVE YOU MY HEART!!!!"

if encore_sayoriquestion_1 == False:

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            s "NOTHING YOU'VE DONE WILL FIX MY BROKEN HEART!!!!"


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            $ HANGOUT1 = hangout1.upper()
            s "WAS [HANGOUT1] NOT GOOD ENOUGH FOR YOU?!?!?!"


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            s "YOU'VE DONE NOTHING BUT LEAD ME ON!!!!"


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            s "YOU DON'T CARE ABOUT ME!!! YOU'RE JUST TALKING TO ME NOW TO MAKE YOURSELF FEEL LESS GUILTY!!!!!!!"

mc "Sayori, what the hell are you even talking about?!?!"
mc "I know I haven't been perfect but-"
show s_mad12 as sayori at t11 zorder 1
s "BUT NOTHING!"
s "YOU IGNORED ME FOR AN ENTIRE YEAR!!!"
s "WHILE I WAS DEALING WITH MY SOUL SPLITTING IN TWO!"
show s_mad1 as sayori at t11 zorder 1
s "DO YOU KNOW HOW AWFUL YOU'VE MADE ME FEEL OVER THIS LAST YEAR, [player]?"
s "AWFUL ENOUGH TO WHERE I WANTED TO HANG MYSELF!"
show s_mad2 as sayori at t11 zorder 1
s "AND YOU MADE ME DO IT!!!!"
s "YOU PUSHED ME BEYOND MY BREAKING POINT!!!"
show s_mad42 as sayori at t11 zorder 1
s "I KNOW YOUR AFFECTION FOR ME WAS FAKE!!!!"
s "NOTHING IS REAL..."
show s_mad43 as sayori at t11 zorder 1
s "EXISTENCE IS PAIN..."
show s_4pr as sayori at t11 zorder 1
"Sayori let's out a raspy, maniacal laugh."
"I slowly start backing my way to the exit."
mc "I see that you need some time alone, Sayori..."
show s_mad42 as sayori at t11 zorder 1
s "Oh, no, no, no!"
"Sayori quiets her voice to an eerie whisper that I can barely hear."
show s_mad1 as sayori at t11 zorder 1
s "No..."
s "No, [player], don't leave..."
s "You said you wanted to spend time with me..."
show s_mad11 as sayori at t11 zorder 1
s "No time like the present, right?!?!"
mc "I'm gonna be late to school..."
show s_mad12 as sayori at t11 zorder 1
s "FORGET SCHOOL!"
s "THEY NEVER TAUGHT US ANYTHING USEFUL ANYWAY!"
s "IT'S ALL AN ELABORATE GAME, [player]..."
s "YOU AND THIS WORLD HAVE PLAYED ME FOR SO LONG..."
s "USING MY KINDNESS TO MAKE YOU FEEL GOOD ABOUT YOURSELVES..."
show s_mad44 as sayori at t11 zorder 1
s "BUT I FIGURED OUT HOW TO BEAT IT!!!"
s "IT WAS SO EASY!!!"
"She's completely lost it."
"I'd try to outrun her but Sayori would probably catch up to me long before I make it to school..."
"But if I can make it to the neighbor's house..."
mc "How, did you beat it, Sayori?"
"At this point, I'm trying to do everything I can to make sure Sayori doesn't attack me..."
show s_mad13 as sayori at t11 zorder 1
s "Do you really want to know?"
play music hb
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at heartbeat
show s_mad14 as sayori at t11 zorder 1
s "I don't think you care enough, [player]..."
show s_mad12 as sayori at t11 zorder 1
s "Considering how you let someone you've known forever just hang herself!"
show s_mad1 as sayori at t11 zorder 1
mc "I'm sorry, Sayori..."
mc "P-{w=0.38}please tell me..."
show s_mad13 as sayori at t11 zorder 1
s "Come over here then, and I'll tell you..."
"I'm so wracked with anxiety it feels like my heart's about to explode..."
"My vision is starts to become blurry as Sayori continues to stare me down."
"The more I stare back at her, the more light headed I feel..."
"W-{w=0.38}what's happening?!?!"
"Don't tell me I'm about to pass out now in a time like this..."
mc "I...{w=0.38}I don't feel so good, Sayori..."
mc "Just tell me."
show s_2pq as sayori at t11 zorder 1
"Sayori giggles."
show s_1pr as sayori at t11 zorder 1
s "Okay!"
s "Here's how you beat the game, [player]..."
show s_1pq as sayori at t11 zorder 1
"Sayori pauses dramatically, as I both anxiously eye her and the exit, trying to determine when I should try to book it."
show s_4pq as sayori at t11 zorder 1
s "Kill yourself!"
mc "W-{w=0.38}what?!?"
mc "Come again?"
show s_1pr as sayori at t11 zorder 1
s "Kill yourself!"
show s_1pq as sayori at t11 zorder 1
"What the hell is she talking about?"
show s_1pr as sayori at t11 zorder 1
s "Kill yourself!"
show s_4pr as sayori at t11 zorder 1
s "Kill yourself!"
show s_mad1 as sayori at t11 zorder 1
s "Kill yourself!"
show s_mad11 as sayori at t11 zorder 1
s "Kill yourself!!!"
show s_mad44 as sayori at t11 zorder 1
s "KILL YOURSELF!!!!!!!"
"Sayori starts repeating the same thing over and over again, growing louder each time."
"I start making movements to run for the exit."
stop music
show s_mad4 as sayori at t11 zorder 1
"Sayori suddenly stops her chant and stares right at me."
$ style.say_dialogue = style.edited
show s_mad45 as sayori at t11 zorder 1
s "KILL YOURSELF!"
$ style.say_dialogue = style.normal
play sound run
show s_mad11 as sayori at face
$ renpy.pause(delay=0.1, hard=True)
scene black
play sound bone
$ renpy.pause(delay=5.0, hard=True)
jump day4_start



label day3_yvoid:
scene black
with close_eyes
$ m_name = "???"
play music e8
"The next thing I know, I open eyes to see almost total darkness in front of me."
"There's no sight of my bed, my room or anything!"
"And I'm already standing up right!"
"I quickly realize that I must be dreaming again."
"Maybe it won't be so bad tonight..."



if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "WHAT THE HELL ARE YOU DOING?!?!"


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You're just making this needlessly more difficult, aren't you?!?"

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "What the hell, [player]?!?!"


if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You just don't listen, do you?!?"


"The same, familiar voice angrily screams, making my ears sting in agony."
"I try to move to cover my ears, but my arms remain locked by my sides, forcing me to simply just wince in pain."
"I guess I stand corrected..."

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        m "I just don't know what's with you!"
        m "I don't understand why you continue to pursue the most unstable of us all!"
        jump wake


if hangout1 == "Monika":
    if hangout2 == "Monika":
        m "You were doing everything right until today!"
        m "I even tried to help you make the right choice!"
        m "Instead, you resisted and blew me off!"
        m "And now you're starting to risk my plan for us!"
        m "Why did you suddenly decide you wanted to spend time with Yuri?!?"
        jump wake


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
        m "You had a good start, it gave me hope that things could work out..."
        m "But you've veered far off course now!"

        if hangout2 == "Sayori" or hangout2 == "Natsuki":
            m "You've been all over the place with who you've chosen to spend your time!"
            jump wake

        if hangout2 == "Yuri":
            m "I don't know why Yuri is of sudden interest to you!"
            jump wake



if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m "Just when I thought we were getting on the right track, you prove me wrong!"

        if hangout1 == "Sayori" or hangout1 == "Natsuki":
            m "I'm glad I got you away from [hangout1]..."
            m "But I don't have time for you to play games with Yuri too!"
            jump wake

        if hangout1 == "Yuri":
            m "Why did you go back to Yuri after I told you not to?!?"
            jump wake



if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":

        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                m "I just don't know what's with you!"
                m "I don't understand why you continue to pursue the most unstable of us all!"
                jump wake

            if hangout1 == "Sayori":
                if hangout2 == "Sayori":
                    m "I don't understand you, [player]!"
                    m "It took long enough to get you to stop spending so much time around Sayori..."
                    m "And now you go to Yuri?!?"
                    m "Maybe I didn't make something clear about her..."
                    jump wake

            if hangout1 == "Natsuki":
                if hangout2 == "Natsuki":
                    m "I don't understand you, [player]!"
                    m "It took long enough to get you to stop spending so much time around Natsuki..."
                    m "And now you go to Yuri?!?"
                    m "Maybe I didn't make something clear about her..."
                    jump wake

            else:
                m "You've been all over the place, spending your time with [hangout1] and [hangout2]..."
                m "Who you should be spending your time with should be fairly obvious by now..."
                m "But let me tell you something about our dear Yuri..."
                jump wake


label wake:

m "Yuri is completely insane!"
m "She hides it well because she wants to earn your trust so that she can kill you, or worse..."

if hangout1 == "Yuri" or hangout2 == "Yuri":
        m "You saw how she was so willing to kill herself for enjoyment!"
        m "Do you really want a girl like that?"

else:
    pass

m "She's a freak, [player]..."
m "All your suspicions about her are true..."

if yuri_hangout == True:
    m "So why do you take the chance to spend even more time with her?!?!"
    m "To try to confirm your suspicions that she's unstable?"
    m "The price of doing so is death!"

if yuri_hangout == False:
    m "Now, thankfully you didn't spend more time with her today..."
    m "But she'll be still left craving you!"

m "She'll destroy everything in her path to get out of here if she ever learns the truth about this place!"
m "It's time for you to see that!"
stop music
scene bg bedroom_night
"I'm immediately jolted awake."
"I sit myself up, panting as I feel cold sweat trickling down my neck."
"I can feel my body trembling over the whole ordeal I just experienced..."
mc "What...{w=0.38}what was that all about?"
"I hopelessly ask to myself."
"I do my best to wipe the sweat off of my neck as I look at the time."
"2 AM."
"This is the third night in a row this has happened..."
"What is happening to me?!?"
"Am I really going insane?"
"Whatever that voice wanted, it clearly didn't want me being around Yuri..."

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":


        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "It's been harrassing me to stay away from Sayori too..."
                "And I guess I might've subconsciously decided to hangout with someone else in hopes it'd stop..."
                jump breakin

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                "It's been harrassing me to stay away from Natsuki too..."
                "And I guess I might've subconsciously decided to hangout with someone else in hopes it'd stop..."
                jump breakin


        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                "It's been harrassing me this entire week to stay away from Yuri..."
                "Maybe I should stay away from her to see if these nightmares go away..."
                "No, that's ridiculous!"
                jump breakin

    else:
        "In fact, it's telling me to stay away from [hangout1] and [hangout2] this past week..."
        "I really have no idea what it wants me to do at this point..."
        "Does it want me to leave the club or something?!?"
        "I mean, I haven't spent time around Monika yet..."
        "But it'll probably still torment me even if I do..."
        jump breakin



    if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout2 == "Yuri":
        if hangout2 == "Monika":
            "It wasn't as bad when I was around Monika yesterday..."
            "Saying that I 'was on the right track', whatever the hell that means..."

    if hangout1 == "Monika":
        if hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
            "Compared to what I experienced yesterday, Monday's nightmare was tame..."
            "Saying a bunch of things that I couldn't make much sense of..."
            "But that only happened when I hung out with Monika..."
            "And the voice tormented me last night for hanging out with [hangout2]..."

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            "These dreams are just getting weirder and weirder..."



label breakin:

"There has to be a plausible explanation for this..."
play sound drop2
"Suddenly I hear the sound of several things fall down."
"It came from downstairs..."
"And judging by the sound, it sounded pretty serious."
"I should probably check it out..."
"I slowly get out of bed and creep downstairs to investigate, careful to avoid making any sound."
scene bg kitchen_dark
"I arrive downstairs, but I'm unable to see anything due to the lights being off."
"Adjusting my vision to the dark a little, it doesn't seem like anything heavy fell over."
"But...{w=0.38}something doesn't feel right..."
show yuri_ghost1 as yuri at t11 zorder 1
"I glance over to the kitchen area to see an outline of something...{w=0.38}or someone..."
"I nearly scream in horror but I quickly cover my own mouth."
"I squint my eyes at the dark figure, which seems to be standing right by the kitchen table."
"Is that...{w=0.38}YURI?!?!"
"Maybe I'm just seeing things..."
"I slowly move my hand to the light switch and flick on the lights."
show yuri_ghost1 as yuri at thide
hide yuri
scene bg kitchen_light
"The lights come on, revealing that there's nobody standing in the kitchen."
"I breathe a massive sigh of relief."
"For a second there, I thought Yuri somehow broke into my house..."

if encore_festivalquestion_2 == "Yuri":
    "She isn't the type of person to do that..."

if encore_festivalquestion_2 == "Natsuki":
    "I mean it's not like she knows where I live..."

"I walk into the kitchen right where I thought I saw Yuri standing."
"A quick look around shows that everything seems to be normal and there isn't anything displaced or missing."
"Maybe it came from the living room."
"Just for good measure, I grab one of my kitchen knives for protection, just in case there is an intruder in my house."
scene bg livingroom_dark
with wipeleft_scene
"I carefully walk into my living room, knife ready."
"Carefully looking around, I see that everything is exactly the way I remember it."
"Nothing's tipped over, nothing's broken which is the good part..."
"But something had to have made that noise..."
"I scratch the back of my head in confusion."
"Maybe it came from outside?"
"Or one of the neighbors is doing who knows what at this ungodly hour..."
"Then again, this is a quiet neighborhood..."
"Ah, I'm probably just imagining things."
"After all, I thought I saw Yuri standing in my kitchen!"
"Maybe my mind's just telling me to get back to bed."
"After I put my kitchen knife back where I found it, I turn off all the lights and head back upstairs."
scene bg bedroom_night
with wipeleft_scene
"Man, I'm going to have to talk to Sayori about all this..."

if tell_s == True:
    "Granted, I'll be just adding on to her worries, maybe I could use this as an extra push for us to both get some professional help..."
    "I have been meaning to suggest that for a while now, but I haven't ever gotten around to it."

if tell_s == False:
    "I can't keep something like this from her."
    "Even though she'll ask me a million questions, it'll probably help me with getting these nightmares off my chest."

"Oh well, back to bed for me!"
"I slide under my overs and resume my favorite sleeping position."
"Is it just me or is my bed extra comfy now?"
"Ah whatever, I'm done with questioning things for tonight..."
mc "Good night, comfy bed..."
"I begin to slowly close my eyes."
"However, as I'm doing so, I feel something to my left."
"I turn my head to see what it is."
show yuri_ghost2 as yuri at face
y "Good night, sweet prince."
mc "{cps=16}WHAT THE F-{nw}"
play sound "sfx/fall2.ogg"
show yuri_ghost2 as yuri at t11 zorder 1
"I'm immediately pushed off my bed."
play music e9
"I land hard on my head as the rest of my body falls behind me, making my legs crash into my nightstand."
play sound "sfx/giggle.ogg"
"I let out a scream of both horror and pain as my legs crash down onto everything on my nightstand and flop behind me."
"Gritting my teeth to try to tolerate the pain, I look up to see Yuri now standing on my bed, looking down at me with a sadistic smile."
"I'm about to start yelling at her before I realize her frightening new apperance..."
"Everything about her is...{w=0.38}different."
"Her skin is an unatural deep blue, while all her other features are a glowing light green."
"I quickly stand up to face her."
"Yuri begins to speak in a muffled, almost alien voice..."
$ style.say_dialogue = style.edited
y "Meet me downstairs..."
$ style.say_dialogue = style.normal
$ renpy.pause(delay=0.10)
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
show yuri_ghost2 as yuri at thide
hide yuri
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
"As soon as I blink, Yuri is gone."
"I'm immediately left feeling petrified."
"She just disappeared!"
"A-{w=0.38}am I still dreaming?"
"I slap myself in an effort to see, but I'm merely left with my cheek stinging from the force of my slap."
mc "Ouch!"
mc "Okay...{w=0.38}I'm not dreaming..."
"This is bad!"
"I need to call the police!"
"I look over to my nightstand where I left my phone, but it's no longer there!"
"The only other phone I have is downstairs..."
"Shit!"
"Wait! I could try escaping through my window and going to Sayori's!"
"I run over my window and try to open my windows, but for some reason, they're jammed shut."
"I step back and feel an ice cold chill creep down my spine."
"I'm trapped in my own house!"
"Maybe I can break the window..."
"I look around for something heavy enough that could break the glass..."
"But then I risk Yuri following me to Sayori's..."
"I can't put her in danger..."
"I guess I really do have to head downstairs..."
"I grab one of my heavy textbooks for protection as I carefully head back down."
scene bg kitchen_dark
with wipeleft_scene
"As I walk back downstairs, I notice to see that all the lights are off again."
mc "Yuri?!?"
"I call out into the darkness."
mc "What the hell is all this?!?"
mc "What are you doing in my house?!?"
"..."
"I don't get a response."
"She has to be here..."
"But I don't want to turn on the lights either, she'll be able to see me..."
"If I can't see her...{w=0.38}she can't see me either."
"My entire body shakes with fear as I try to guess where she could possibly be."
"Well...{w=0.38}she was by the table last time."
"Maybe she's there again..."
"I'll turn on the lights and throw my textbook in that direction."
"If she's there, that should knock her out..."
"I'll do it on the count of three."
"One..."
"Two..."
stop music
mc "THREE!"
scene bg kitchen_light
play sound "sfx/fall2.ogg"
"I flick the lights on and chuck the textbook at my kitchen with all my force."
"It ends up slamming into the table and falling onto the floor."
"There's no sign of Yuri in the kitchen..."
mc "WHERE THE HELL ARE YOU?!?"
$ style.say_dialogue = style.edited
y "You should've checked the couches, [player]."
$ style.say_dialogue = style.normal
play sound scare
mc "{cps=18}Wha-{nw}"
show yuri strobe at face
#show yuri_ghost3 as yuri at face
#show yuri_ghost3 as yuri at thide
#show yuri_ghost4 as yuri at face
#show yuri_ghost4 as yuri at thide
"Yuri's sudden apperance behind makes me fall backwards into my kitchen table."
"Before I have time to react, I realize I'm practically backed into a corner."
stop sound
play music e9
show yuri 3y3 at t11 zorder 1
"Yuri takes a step closer to me, a deranged smile creeping across her face."
mc "What the fuck is wrong with you?!?"
mc "Are you crazy!"
y "Of course I am!"
show yuri 3d at h11 zorder 1
y "I'm crazy for you!"
y 1y1 "I also happen to be madly in love with you!"
y "Isn't that just wonderful?!?!"
mc "Uh..."
y 3y4 "Don't tell me that you don't feel the same way about me, [player]..."

if encore_sayoriquestion_1 == True:
    y 3y7 "You're not still head over heels for that attention whore, Sayori, are you?!?"
    y 3y4 "You want to stay with her, is that it?!?"
    y "Or are you incapable of telling her that you want to be with a real woman?!?"
    y 3y3 "Well here's a solution..."
    show yuri_knife1 as yuri at t11 zorder 1
    play sound sheath1
    "Yuri pulls out one of my kitchen knives from under her sleeve."
    y "Why don't I talk to her for you?!?"
    y "I don't have to be violent..."
    "Yuri slowly rolls up her sleeve."
    show yuri_knife4 as yuri at t11 zorder 1
    y "I can just show her this..."
    show yuri_knife3 as yuri at t11 zorder 1
    y "And promise her that if she ever as so much looks in your general direction again, these cuts will be on her."
    "Yuri gestures to her wrist, which is lined with dozens of cuts, some of them freshly done..."



if encore_sayoriquestion_1 == False:
    y 3y7 "I don't think my little heart could take it!"
    y 3y4 "You turned Sayori down with hardly a second thought!"
    y "And you're going to do the same to Natsuki!"
    y 1y3 "So do it to me, [player]!"
    y 3c "Break my spirit..."
    y 3d "Crush my hopes and dreams..."
    y 1y1 "I'm already broken, it's what I want!"
    y 1y3 "I want you to put me down like a filthy animal!"
    show yuri_knife1 as yuri at t11 zorder 1
    play sound sheath1
    "Yuri pulls out one of my kitchen knives from under her sleeve."
    mc "Y-{w=0.38}Yuri...{w=0.38}N-{w=0.38}no..."
    mc "I don't want to hurt you."
    "Yuri slowly rolls up her sleeve."
    show yuri_knife4 as yuri at t11 zorder 1
    y "Did I stutter?"
    y "You don't have a choice in this!"
    y "Put me out of my fucking misery, [player]!"
    show yuri_knife3 as yuri at t11 zorder 1
    y "This knife is just aching to feel more of my blood..."
    y "We can start slowly if you want, cut me on my wrist!"
    "Yuri gestures to her wrist, which is lined with dozens of cuts, some of them freshly done..."


mc "Y-{w=0.38}Yuri...{w=0.38}stop!"
mc "This is insane!"
mc "I'm not hurting you!"
"I barely manage to cry out as my voice shakes with utter fear and disgust."
show yuri_knife1 as yuri at t11 zorder 1
"Yuri rolls her sleeve back."
y "Well that's too bad..."
stop music fadeout 2.0
mc "W-{w=0.38}why is that?!?"
y "Because, this knife has already tasted blood tonight..."
show yuri_knife2 as yuri at t11 zorder 1
play sound sheath2
y "BUT THIS ONE HASN'T!!!!"
"Yuri pulls out a second knife as she starts slowly walking towards me."
play music hb
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at heartbeat
y "LET ME SHOW YOU HOW MUCH I LOVE YOU, HONEY!"
"My heart pounds against my chest at a million miles a second as I start to hyperventilate."
"My vision becomes blurry as my head starts spinning, trying to come to terms with the situation."
"I look around for something to defend myself with or a way out of this, but both options come up empty."
"I'm frozen in fear, hopeless to do anything as Yuri continues her menacing advance."
$ style.say_dialogue = style.edited
y "OPEN WIDE!"
$ style.say_dialogue = style.normal
show yuri_knife2 as yuri at face
"Yuri rushes at me with her knives."
show yuri_knife5 as yuri at face
"I manage to grab her wrists in an effort to block her from stabbing me."
show yuri_knife6 as yuri at face
play sound drop
"I manage to twist one of her wrists, forcing her to drop her knife."
play sound fall
show yuri_knife6 as yuri at t11 zorder 1
"However, Yuri knees me in my groin, making me go down instantly."
mc "AGH!"
"I look up to see Yuri angrily towering over me, knife ready."
"The other knife is too far out of reach."
y "That wasn't very nice, [player]..."
y "Resisting my affection..."
y "That hurts my feelings..."
show yuri_knife1 as yuri at t11 zorder 1
$ style.say_dialogue = style.edited
y "NOW I'M GOING TO HURT YOU!"
$ style.say_dialogue = style.normal
show yuri_knife1 as yuri at thide
hide yuri
"Yuri gets behind me and pins me to the floor."
"I thrash around in an effort to get her off me."
mc "HELP!"
"My cries for help are immediately become muffled as Yuri puts her hand over my mouth.."
y "Stop struggling my darling..."
y "I'm only doing this because I love you..."
#Bloodscreen
show veins onlayer front:
    additive 1.0
#show veins zorder 10:
#    alpha 1.0
    block:
        easeout 1.0 alpha 0.5
        easein 1.0 alpha 1.0
        repeat
play sound stab
"I feel the weight of Yuri's knife thrusted into the back of my neck..."
"And the excruciating pain as she slowly pulls it out..."
show layer master at dizzy(1.0, 1.0)
show layer screens at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
show veins onlayer front:
    additive 0.5

play sound fall
"My vision becomes filled with blood and tears as my head is slammed into the floor."
"I try to scream but nothing even comes out of my lungs..."
"I try to move but my muscles refuse to respond..."
"All I can feel is the pain flowing out with my blood and the weight of Yuri holding me down."
"The world around me slowly fades to black, with the last thing I hear is Yuri's maniacal laughter."
#Stop all effects
#Hide textbox
show black onlayer front:
    alpha 0.0
    0.25
    linear 3.0 alpha 1.00
window hide
hide veins onlayer front
hide layer master
hide layer screens
hide veins
stop sound
show layer master # These will stop the dizzy effect
show layer screens
hide i1 onlayer front # These will hide the effects
hide i2 onlayer front
hide veins onlayer front
stop music fadeout 2.0
scene black
hide black onlayer front
$ renpy.pause(delay=5.0, hard=True)
jump day4_start
