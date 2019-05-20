#############
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
        "I quickly prop myself, trying to supress it."
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
        "I don't feel like getting out of bed yet, so I just spend the rest of the time staring at the ceiling."
        "Though the memories of my nightmares slowly creep back into my mind."

        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "It was almost like what I saw two nights ago..."

        if hangout1 == "Sayori":
            if hangout2 == "Natsuki":
                "How I walked into Sayori's room and just seeing her hanging there..."
                "I don't know what was worse..."
                "Seeing Sayori like that..."
                "Or seeing how Natsuki in so much pain as her neck slowly bent..."

        if hangout1 == "Sayori":
            if hangout2 == "Yuri":
                "Remebering how I walked into Sayori's room and just seeing her hanging there..."
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
                "How that figure made Yuri kill herself..."
                "I don't know what was worse..."
                "Seeing Yuri like that...."
                "Or seeing Natsuki rush at me out of the closet like in the dream I had two nights ago..."

        if hangout1 == "Natsuki":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "I don't know what was worse..."
                "Seeing Sayori in so much pain..."
                "Or seeing Natsuki rush at me out of the closet like in the dream I had two nights ago..."

        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                "About how I couldn't save Yuri..."
                "How that figure made Yuri kill herself..."

        if hangout1 == "Yuri":
            if hangout2 == "Natsuki":
                "About how I couldn't save Natsuki..."
                "How I had to watch her neck slowly bend until it broke..."
                "I don't know what was worse..."
                "Seeing Natsuki in so much pain..."
                "Or seeing Yuri just go insane and stabbing herself like she did in my dream two nights ago..."

        if hangout1 == "Yuri":
            if hangout2 == "Sayori":
                "About how I couldn't save Sayori..."
                "How I just watched her slowly choke to death..."
                "I don't know what was worse..."
                "Seeing Sayori in so much pain..."
                "Or seeing Yuri just go insane and stabbing herself like she did in my dream two nights ago..."



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
        "I clutch my forehead to feel if I'm coming down with a fever."
        "No...{w=0.38}and the rest of me feels fine..."
        "What's going on with me?"
        "After a few minutes I stop shivering and look at the clock."
        "Great...{w=0.38}I don't have to be up for another hour."
        "Well...{w=0.38}I can try falling back asleep..."
        "But if I do, won't that voice still be there?"
        "If this keeps happening, I'm probably going to need a psychiatrist."
        "Maybe I'm actually starting to go crazy..."
        "I don't feel like getting out of bed yet, so I just spend the rest of the time staring at the ceiling."
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
        "I clutch my forehead to feel if I'm coming down with a fever."
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
        "I don't feel like getting out of bed yet, so I just spend the rest of the time staring at the ceiling."
        "Though the memories of my dreams slowly creep back into my mind."
        "What does it want with me?"
        "What's with these dreams?"
        "Why was that voice now thanking me after trying to scold me for something?"
        "And what the hell does it mean by \‘keep doing what you're doing\'?"
        "I don't even know what I'm doing..."


if hangout1 == "Monika":
    if hangout2 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri":
        "I suddenly wake up with the sudden urge to vomit."
        "I quickly prop myself, trying to supress it."
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
        "I don't feel like getting out of bed yet, so I just spend the rest of the time staring at the ceiling."
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


"Thankfully before I can think longer about it, my alarm sounds off."
"I sigh to myself as I walk over to silence my alarm and go about my daily morning routine of getting ready for school."



scene bg kitchen
with wipeleft_scene
play music t2 fadein 1.5
"After finishing my morning routine, I head downstairs to my kitchen with [poem_giver]'s poem in hand."
"I must've read it over a hundred times by now, hoping that this was some kind of sick joke."
"I sigh and let the paper flutter onto my dining room table."
"I'm not particularly hungry so I opt to just make a fruit bowl."
"While grabbing the bowl, I send Sayori a text to let her know that I'm up and she doesn't need to come wake me up again."
"Surprisingly, she responds back rather quickly and tells me that she's already waiting outside for me."
"I reply back that I'll meet her as soon as I'm done with my breakfast."
"I hastily assemble my furit bowl and quickly begin eating it."
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
"Sayori's already standing by the adjacent sidewalk to my house."
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
mc "I forgot how much you love Friday's..."

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
    s "[player], you okay?"
    show sayori 1g at face
    mc "I-{w=0.38}it's nothing, I'm-"
    "The pain gets worse just as I say that."
    show sayori 1g at h11 zorder 1
    "I end up having to take a step back from Sayori as I clutch my forehead tighter."
    mc "Just...{w=0.38}give me a second."
    show sayori 1e
    "After a few moments the pain subsides."
    s "[player], what's wrong?"
    mc "Ah, it's just a headache, don't worry about it."
    show sayori 1h
    s "Was it really just a headache though? You looked like you were in a lot of pain..."
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
    s "Come on, [player]! You know Friday's are the best!"
    show sayori 1y
    s "It's the best time to spend time with those you care about the most without having to worry about school and other things..."
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
    "Sayori continues to look worringly at me."
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
        mc "I watched you die..."
        mc "I couldn't save you."
        mc "All I could do was watch you, struggling to breathe..."
        s 1k "..."
        mc "I know it was just a dream, but it felt too close to reality for some reason..."
        mc "The way you frantically clawed at the rope..."
        stop music
        s u115232 "Rope...?"
        mc "You were hung in front of me..."
        show sayori 2g
        mc "It was...{w=0.38}hard to watch..."
        mc "I felt like I actually lost you..."
        mc "And the night before wasn't any better..."
        s 1g "How so?"

        if hangout1 == "Sayori":
            mc "I opened this door, and you were hanging right there in your bedroom..."

        if hangout1 == "Natsuki":
            mc "I opened this door, and I was back at the club, but everything was upside down..."
            mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
            mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah...{w=0.38}almost as bad as seeing you hanging..."
            mc "It's all really strange..."

        if hangout1 == "Yuri":
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
            mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah...{w=0.38}almost as bad as seeing you hanging..."
            mc "It's all really strange..."

        if hangout1 == "Monika":
            mc "I was in space or something..."
            mc "And the same voice was saying all these crazy these weird things telling me that I need to 'keep doing what I'm doing'..."
            mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
            show sayori 1k
            mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
            mc "And it didn't say a lot of nice things about you guys either..."
            mc "Stuff like 'you're going to die' or something crazy like that..."
            mc "Listening to all that was just as bad as seeing you hanging..."
            mc "It's all really strange..."



        show sayori 2l
        "Sayori nervously swallows."
        s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
        s "I would never do something like that..."
        show sayori 1k
        s "I couldn't..."
        "I don't exactly feel reassured by the way she's saying that..."

        if encore_sayoriquestion_1 == True:
            "Especially since she's said some rather concerning things to me latelty..."
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



        if encore_sayoriquestion_1 == False:
            "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."


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
        "I'm surprised by Sayori's sudden change of heart, but nevertheless, I choose to oblige."
        mc "Yeah...{w=0.38}let's just go."
        mc "It was just a stupid dream anyways, right?"
        show sayori 1k
        s "Yeah..."
        "We begin the walk to school without another word."
        show sayori at thide
        hide sayori
        jump day3_walktoschool




    if hangout2 == "Yuri":
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

        if hangout1 == "Natsuki":
            mc "I opened this door, and I was back at the club, but everything was upside down..."
            mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
            mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah...{w=0.38}almost as bad as seeing Yuri stab herself..."
            mc "It's all really strange..."

        if hangout1 == "Yuri":
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
            mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah..."
            mc "It's all really strange..."

        if hangout1 == "Monika":
            mc "I was in space or something..."
            mc "And the same voice was saying all these crazy these weird things telling me that I need to 'keep doing what I'm doing'..."
            mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
            show sayori 1k
            mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
            mc "And it didn't say a lot of nice things about you guys either..."
            mc "Stuff like 'you're going to die' or something crazy like that..."
            mc "Listening to all that was just as bad as seeing Yuri stab herself..."
            mc "It's all really strange..."



    if hangout1 == "Sayori":
        if hangout2 == "Yuri":
            show sayori 2l
            "Sayori nervously swallows."
            s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
            s "I would never do something like that..."
            show sayori 1k
            s "I couldn't..."
            "I don't exactly feel reassured by the way she's saying that..."

            if encore_sayoriquestion_1 == True:
                "Especially since she's said some rather concerning things to me latelty..."
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



            if encore_sayoriquestion_1 == False:
                "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."


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
            "I'm surprised by Sayori's sudden change of heart, but nevertheless, I choose to oblige."
            mc "Yeah...{w=0.38}let's just go."
            mc "It was just a stupid dream anyways, right?"
            show sayori 1k
            s "Yeah..."
            "We begin the walk to school without another word."
            show sayori at thide
            hide sayori
            jump day3_walktoschool



    if hangout1 == "Natsuki" or hangout1 == "Yuri" or hangout1 == "Monika":
        if hangout2 == "Yuri":
            show sayori 2l
            "Sayori nervously swallows."
            s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
            s "She would never do something like that..."
            show sayori 1k
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1d
            s "But...{w=0.38}I'm sure she apprecaites you worrying about her..."
            s 3g "Maybe you can talk to her abour your dream?"
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





    if hangout2 == "Natsuki":
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
        mc "Its as if she wasn't in control of her own body..."
        mc "And the night before wasn't any better..."
        s 1g "How so?"


        if hangout1 == "Sayori":
            mc "I opened this door, and you were hanging right there in your bedroom..."

        if hangout1 == "Natsuki":
            mc "I opened this door, and I was back at the club, but everything was upside down..."
            mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
            mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah..."
            mc "It's all really strange..."

        if hangout1 == "Yuri":
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
            mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah...{w=0.38}almost as bad as seeing Natsuki breaking her neck..."
            mc "It's all really strange..."

        if hangout1 == "Monika":
            mc "I was in space or something..."
            mc "And the same voice was saying all these crazy these weird things telling me that I need to 'keep doing what I'm doing'..."
            mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
            show sayori 1k
            mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
            mc "And it didn't say a lot of nice things about you guys either..."
            mc "Stuff like 'you're going to die' or something crazy like that..."
            mc "Listening to all that was just as bad as seeing Natsuki breaking her neck..."
            mc "It's all really strange..."



    if hangout1 == "Sayori":
        if hangout2 == "Natsuki":
            show sayori 2l
            "Sayori nervously swallows."
            s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
            s "I would never do something like that..."
            show sayori 1k
            s "I couldn't..."
            "I don't exactly feel reassured by the way she's saying that..."

            if encore_sayoriquestion_1 == True:
                "Especially since she's said some rather concerning things to me latelty..."
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



            if encore_sayoriquestion_1 == False:
                "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."


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
            "I'm surprised by Sayori's sudden change of heart, but nevertheless, I choose to oblige."
            mc "Yeah...{w=0.38}let's just go."
            mc "It was just a stupid dream anyways, right?"
            show sayori 1k
            s "Yeah..."
            "We begin the walk to school without another word."
            show sayori at thide
            hide sayori
            jump day3_walktoschool



    if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Monika":
        if hangout2 == "Natsuki":
            show sayori 2l
            "Sayori nervously swallows."
            s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
            s "She would never do something like that..."
            show sayori 1k
            $ renpy.pause(delay=0.8, hard=True)
            show sayori 1d
            s "But...{w=0.38}I'm sure she apprecaites you worrying about her..."
            s 3g "Maybe you can talk to her abour your dream?"
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




    if hangout2 == "Monika":
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

        if hangout1 == "Natsuki":
            mc "I opened this door, and I was back at the club, but everything was upside down..."
            mc "Then I was forced to walk over to the closet where I ran into Natsuki..."
            mc "She...{w=0.38}said a bunch of things, broke her own neck, then rushed out and attacked me..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah..."
            mc "It's all really strange..."

        if hangout1 == "Yuri":
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completely empty..."
            mc "Then Yuri came in, said a bunch of weird things, then just stabbed herself..."
            s 2h "Gee, [player]..."
            s "That sounds really scary!"
            mc "Yeah..."
            mc "It's all really strange..."

        if hangout1 == "Monika":
            mc "I was in space or something..."
            mc "And the same voice was saying all these crazy these weird things telling me that I need to 'keep doing what I'm doing'..."
            mc "Though it wasn't exactly happy with me last night, it was mad that I spent time with you for some reason..."
            show sayori 1k
            mc "Whatever that voice is, it doesn't seem that it wants me around you or any of the others..."
            mc "And it didn't say a lot of nice things about you guys either..."
            mc "Stuff like 'you're going to die' or something crazy like that..."
            mc "'Keep spending time with me.'..."
            mc "It's all really strange..."



    if hangout1 == "Sayori":
        if hangout2 == "Monika":
            show sayori 2l
            "Sayori nervously swallows."
            s 1l "W-{w=0.38}well I don't know why you'd be having dreams like that, [player]..."
            s "I would never do something like that..."
            show sayori 1k
            s "I couldn't..."
            "I don't exactly feel reassured by the way she's saying that..."

            if encore_sayoriquestion_1 == True:
                "Especially since she's said some rather concerning things to me latelty..."
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



            if encore_sayoriquestion_1 == False:
                "Though, now that I think about it, before we hungout yesterday, she was acting rather timid around me..."


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
            "I'm surprised by Sayori's sudden willingness to go, but nevertheless, I choose to oblige."
            mc "Yeah...{w=0.38}let's just go."
            mc "It was just a stupid dream anyways, right?"
            show sayori 1k
            s "Yeah..."
            "We begin the walk to school without another word."
            show sayori at thide
            hide sayori
            jump day3_walktoschool



    if hangout1 == "Sayori" or hangout1 == "Yuri" or hangout1 == "Natsuki":
        if hangout2 == "Monika":
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
            mc "I dobut spending time with you could possibly be causing these nightmares!"
            show sayori 1k
            "I feel pit form in my stomach."
            "No, that couldn't be the reason..."
            "It's impossible!"
            "And no figment of my imgaination is going to tell me otherwise!"
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
            s 1l "T-{w=0.38}thanks, [player]..."
            s 1k "I guess we can just go to school now..."
            mc "Ah! I guess so!"
            mc "Wouldn't want to be late!"
            "Sayori seems to completely ignore my comment as we begin our walk to school."
            show sayori at thide
            hide sayori
            jump day3_walktoschool





label day3_notellsayori:
    "I decided not to tell her."
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
"Even though lately it's started to become the norm for our walks, it's still fustrating to be right back we were right after her confession."
"Especially since we started to move past last Sunday."
"Now she's thinking who knows what inside that head of hers..."
"And what does she mean she's had weird dreams too?"
"It's not like we've went through the same thing..."
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
"But, its still nice to know that she's there for me."
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
"It's not like we've both had the same kinds of dreams anyways."
"But, I appreciate knowing that she's still there for me."
jump day3_sayo2


label day3_sayo1:
show sayori 1k at t11 zorder 2
"I turn to Sayori, trying to smile hopefully at her, but she's just looking blankly down the road ahead of us as we walk in unison down the sidewalk."
"I let out a small sigh."
"I guess she's just not in a talkative mood..."
"And she did sound rather disturbed by what I told her too."
"Sayori's never been one to stomach horror very well, not that I blame her."
"Hopefully she'll get over this soon."
"However, I quickly realize that I have another problem brewing..."
"[poem_giver]'s letter..."
"I haven't really thought about how I'm really going to do handle that..."
"As I was thinking earlier, telling Monika about the situation seems like my best course of action."
show sayori 1g
"Normally I'd tell Sayori, but I don't think she'd take it very well right now..."
"I guess my only real option is to go to Monika before the club..."
"Knowing [poem_giver] will probably want to talk to me."
"I'm really not looking forward today..."
"What if someone else gives me another confession letter?"
show sayori 1h
s "[player]?"
"Sayori takes me out of my train of thought."
show sayori 1g
mc "Y-{w=0.38}yeah?"
show sayori 1h
s "You okay? You just suddenly stopped there for a second."
mc "I did?"
show sayori 2g
"Realizing that Sayori is more than a few steps ahead of me, I quickly run up to catch up to her."
jump day3_var1

label day3_sayo2:
show sayori 1k at t11 zorder 2
"I turn to Sayori, trying to smile hopefully at her, but she's just looking blankly down the road ahead of us as we walk in unison down the sidewalk."
"I let out a small sigh."
"I guess she's just not in a talkative mood..."
"She's probably overthinking again..."
"Hopefully she'll get over this soon."
"However, I quickly realize that I have another problem brewing..."
"[poem_giver]'s letter..."
"I haven't really thought about how I'm really going to do handle that..."
"As I was thinking earlier, telling Monika about the situation seems like my best course of action."
show sayori 1g
"Normally I'd tell Sayori, but I don't think she'd take it very well right now..."
"I guess my only real option is to go to Monika before the club..."
"Knowing [poem_giver] will probably want to talk to me."
"I'm really not looking forward today..."
"What if someone else gives me another confession letter?"
show sayori 1h
s "[player]?"
"Sayori takes me out of my train of thought."
show sayori 1g
mc "Y-{w=0.38}yeah?"
show sayori 1h
s "You okay? You just suddenly stopped there for a second."
mc "I did?"
show sayori 2g
"Realizing that Sayori is more than a few steps ahead of me, I quickly run up to catch up to her."
jump day3_var1



label day3_var1:

if tell_s == True:
    s 1l "Are you really sure you're okay?"
    s 1g "You've really been acting strange..."
    mc "I'll be fine..."
    mc "I've gone through worse."
    s 1h "Maybe you should stay home from school today."
    s 1k "I wouldn't want you to feel any worse..."
    show sayori 1f
    mc "I'll be fine, besides, I really need to talk to Monika."
    s 2h "M-{w=0.38}Monika?"
    s 2g "Why?"
    mc "It's...{w=0.38}something related for what we're doing for Monday."
    s 1k "Okay..."
    mc "Hey, Sayori..."
    s 1g "Yeah?"
    mc "Don't worry about me, if I feel worse, I'll go to the nurse's office and you can take me home, okay?"
    s 1l "Okay..."
    s 1i "But if you feel sick, you text me right away, okay?"
    mc "You have my word, emergency contact."
    show sayori 1y
    "I see Sayori blush slightly."

if tell_s == False:
    s 1l "Are you really sure you're okay?"
    s 1g "You've really been acting strange..."
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

s 1r "Come on, patient [player], or we're really going to be late!"
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
"Though I wouldn't be able to walk with Sayori to her class like usual, thanks to the time."
s 3c "So, I'll see you after your class, [player]."
mc "Alright, sounds good to me."

if tell_s == True:
    if encore_sayoriquestion_1 == True:
        "Sayori glances around the corridor to make sure we're alone."
        s 3g "Just...{w=0.38}please let me know if you feel worse or anything, okay?"
        mc "I will, Sayori. Don't worry."
        mc "I'm more worried about you."
        s 3h "M{w=0.38}-me? Why?"
        mc "Earlier you looked like you just saw a ghost."
        mc "I just hope I didn't scare you with any of the details..."
        show sayori 3k
        s "I-{w=0.38}it's not that player, really."
        s 1h "I'm just more worried about you..."

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
        mc "I promise."
        show sayori 1h
        mc "I'll see you later."
        s 1g "Okay..."
        show sayori 1d
        mc "Come here."
        show sayori 1q at face
        "Sayori walks up to me to give a brief hug before walking off towards her classroom."
        show sayori 4d at t11 zorder 2
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom while I head off in the opposite direction towards mine."
        jump day3_class



if tell_s == True:
    if encore_sayoriquestion_1 == False:
        "Sayori glances around the corridor to make sure we're alone."
        s 3g "Just...{w=0.38}let me know if something happens with you, okay?"
        mc "I will, Sayori. Don't worry."
        mc "I'm more worried about you."
        s 3h "M{w=0.38}-me? Why?"
        mc "Earlier you looked like you just saw a ghost."
        mc "I just hope I didn't scare you with any of the details..."
        show sayori 3k
        s "I-{w=0.38}it's not that player, really."
        s 1h "I'm just more worried about you..."


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
        mc "I promise."
        show sayori 1k
        s "Okay..."
        show sayori 4d
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom while I head off in the opposite direction towards mine."
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
        "Sayori walks up to me to give a brief hug before walking off towards her classroom."
        show sayori 4d at t11 zorder 2
        s "I'll see you later, [player]."
        mc "Laters."
        show sayori at thide
        hide sayori
        "Sayori walks off towards her classroom while I head off in the opposite direction towards mine."
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
        "Sayori walks off towards her classroom while I head off in the opposite direction towards mine."
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
"Enterting the cafeteria, I immediately begin to look around for Monika."
"Alright, if I was Monika, where would I be?"
"..."
"Probably towards the center with all the other popular kids."
"I start walking to the center of the cafeteria."
show bg cafeteria
with wipeleft_scene
"Sure enough, it didn't take me long to spot Monika sitting at one tables at the center of the room."
show monika 2k at t11 zorder 2
"As I expected, she seems to be chatting away with some of her friends."
"This might be harder than I thought."
"Well, I'm not going to get another chance to talk to her until the club, so it's now or never."
"I carefully approach Monika's table."
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
m 2m "Ah, well, like I said, I was on that trip for debate club."
$ r_name = "Ria"
r "Oh, yeah! The debate club! That place has only gotten more toxic since you left!"
m 1g "It's gotten that bad, huh?"
r "Trust me, you left at the best possible time."
r "I miss the good ol' days..."
a "When Sora was President?"
r "Yeah! We were actually productive and went to all those cool events!"
r "And not always fighting with each other over petty crap..."
a "Yeah, that's when the club was in it's prime..."
m 1f "It's a real shame she transferred though..."
r "I know right?!? She was so nice!"
a "Yeah, but it sucks that we got suckered into voting for her brother to replace her..."
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
"I feel my face heat up with slight embarassment."
mc "T-{w=0.38}thank you, Monika! I really appreciate it!"
m 1b "We'll be right back girls!"
r "Have fun you two!"
show monika at thide
hide monika
"I lead Monika out of the cafeteria and to somewhere where we might have a little more privacy."
a "She's got him wrapped around her finger."
r "That's Monika for you."
show bg school_rooftop
with wipeleft_scene
stop music fadeout 3.0
"I lead Monika up to the rooftop of the school, where there's hardly anyone around that can hear us."
show monika 2d at t11 zorder 2
m "So, what's on your mind, [player]?"
mc "I think I'll just show you..."
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
m 1p "Usually some boy would just walk up to me and stammer his way through before trying to ask me out."
m 1q "A few have tried asking me out through text, but to me that's the cheap way..."
mc "Things would probably be worse had she chosen to text me or walked up to me and confessed."
mc "I'd have no idea how to handle that..."
m 2p "Yeah..."
mc "And I'm pretty sure [poem_giver] is going to try to talk to me later in the club about this."
m 2n "Well, there's really no reason to think she'd expect you to read her poem right away, right?"
mc "What do you mean?"
m 2c "I'm saying that I don't think [poem_giver] was expecting you to read her poem so soon."
m 2d "In all honesty, she probably thinks you'll read it this weekened when you're preparing the poems for the photoshoot."
mc "Yeah...{w=0.38}I guess you're right..."
mc "So i just tell [poem_giver] that I haven't read it yet?"
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
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
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
            m 2m "And it's more my fault than your's anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."


if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
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
            m 2n "Even though you guys have only started really talking recently, I think she really appreciates you for spending time wtih her..."
            m 4n "You seem to have gotten to know her quite well recently..."
            mc "Yeah...{w=0.38}we really have..."
            m 4m "I've seen the way she looks at you when you're reading manga together, [player]..."
            m 2n "And the way she's always acted around you..."
            m 2m "I suspect she liked you from the very begining..."
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
                m 2m "I suspect she liked you from the very begining..."
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
            m 2m "And it's more my fault than your's anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."



if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
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
            m 2m "I suspect she liked you from the very begining..."
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
                m 2m "I suspect she liked you from the very begining..."
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
            m 2m "And it's more my fault than your's anyways..."
            m 2e "So, don't beat yourself up over it too much."
            mc "Alright..."




if hangout1 == "Monika":
    if hangout2 == "Sayori":
        mc "I'm happy with Sayori..."
        mc "I wouldn't want to ruin what we have..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
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
            m 2m "And it's more my fault than your's anyways..."
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
        m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            mc "She caught be by surprise..."
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
            mc "She caught be by surprise..."
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
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
        m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            m 4h "Playing with their feelings like that is wrong and could have unforseen consquences."
            mc "I know..."
            mc "It's just that I feel like I'm being pulled all over the place."
            mc "I don't know what I want..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."



if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":

        if encore_festivalquestion_2 == "Natsuki":
            show monika 2f
            mc "I mean to tell you the truth, I didn't even really knew that Yuri liked me..."
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
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            m 4h "Playing with their feelings like that is wrong and could have unforseen consquences."
            mc "I know..."
            mc "It's just that I feel like I'm being pulled all over the place."
            mc "I don't know what I want..."
            m 2e "I do think for now you're better off just being friends with them until you can make up your mind..."
            mc "Yeah...{w=0.38}you're right..."



        if encore_festivalquestion_2 == "Yuri":
            mc "I've enjoyed spending time around [poem_giver], she's fun to be with..."
            mc "And last Sunday, I did feel like maybe there was something there..."
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
            mc "I mean to tell you the truth, I didn't even really knew that Natsuki liked me..."
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
            mc "But Sayori's been on my mind lately..."
            show monika 2m
            mc "But Sayori's been on my mind lately..."
            m 2g "You're not having second thoughs about your answer to her confession, are you?"
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
m "Who have you been the most happy with?"
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
"Who would I be the most happy with?"
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
mc "Sure! Stressing all over this has worked up quite the appetite..."
m 1l "I'm sure it has, [player]."
m 1a "Come on, let's head back."
stop music fadeout 3.0
"Without another word, Monika and I head down the steps back to the cafeteria."
show monika at thide
hide monika
show bg cafeteria
with wipeleft_scene
"I really wasn't social with Monika and her friends when we came back to join them."
"Other then some occassional chatting, I mostly kept my mouth shut and zoned out."
"My mind was racing the entire time attempting to answer the questions Monika gave me."
"And I'm still a little paranoid that [poem_giver] is going to try to talk to me in the club later..."
"I don't feel prepared for this..."
"But, I guess I did sort of ask for this to happen..."
"Now, I just got to figure out what I want to do next..."
show monika 1e at t11 zorder 2
"I really need to thank Monika when this all over."
show monika cute
"Her advice has been pretty helpful so far, and I feel like I'll ultimately figure things out thanks to her..."
"She certainly has been dependable..."
show monika 1m
play audio school
"Before I can finish my thought, the school bell rings, singfying the end of lunch period for me."
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
"My face turns flush with embarassment."
mc "W-{w=0.38}well yeah..."
mc "You're the best person I know who could trust to help me through this!"
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
        "My heart races a million miles a second as soon as Monika finished her question."
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

if hangout1 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    if hangout2 == "Monika":
        m 2e "Do you want me to walk you back to class?"
        "My heart races a million miles a second as soon as Monika finished her question."
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
            "And what if Sayori sees us and gets the wrong idea?"

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
        "I'm not entirely sure why Monika wanted to walk with me so badly."
        "But hey, I'll oblige her, it wouldn't hurt to."
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
"I'm not entirely sure why Monika wanted to walk with me so badly."
"But hey, I'll oblige her, it wouldn't hurt to."
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
m 1m "A lot of people would tend to breakdown in these kinds of situations..."
show monika 1e
mc "Yeah...{w=0.38}but I'll be fine...{w=0.38}I think."
m 1b "Well you can always count on me if you need anything, [player]."
show monika 1j
mc "You're too kind, Monika, really..."
m 1k "I try, [player]!"
m 1e "It's important to me that you're always in the best state of mind."
show monika 1k
"I advert my gaze to hide my incoming smile."
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
"Wait a second...{w=0.38}I recongize that yelling anywhere..."
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
s 1x "I'm doing great! I was just went to get some water and I ran into you guys!"
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
            "I guess Monika has a point here..."
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
                "I guess Monika has a point here..."
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
m 2l "Ah, well, I don't think taking a slight detour from my normal route would make me late or anything."
show monika 2e
s 1r "Well, that's good!"
s 1g "I'd really love to stay and chat but I have to head back to class pretty soon..."
mc "It's alright, Sayori, we'll see you in the club!"
s 1q "Yeah! I can't wait!"
s 1x "I'll see you guys later!"
show sayori at thide
hide sayori
"We wave goodbye to Sayori as we head our seperate ways."
show monika at thide
hide monika
stop music fadeout 2.0
scene bg corridor
with wipeleft_scene
"Not too long after our run-in with Sayori, Monika and I finally make it to my classroom."
show monika 1a at t11 zorder 1
mc "Thanks for walking back wth me, Monika!"
m 1e "Anytime, [player]!"
m 5a "I hope you have a great rest of your day~"
mc "Y-{w=0.38}you too!"
show monika 5a at face
"Monika takes a step closer to me and leans into my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm completely left dazed as I watch Monika gracefully walk down the hallway and turn the corner towards the the otherside of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sitdown, refusing to make eye contact with anyone as I process what had just happened."
jump day3_mono



label n_hallway_interaction:
show monika tease
$ n_name = "???"
m "{cps=15}Does Natsuki-{nw}"
show monika shock
stop music
n "Hey! What's up?!?"
"I hear someone yelling to us from across the hallway."
"Wait a second...{w=0.38}I recongize that voice..."
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
        "Other then online, there really isn't too many other people I talk to outside the club..."
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
        mc "Ah, well I really should be thanking you afterall..."
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
        mc "Oh, so you developed a tolerance around me, huh?"
        n 1a "Pretty much!"
        n 5t "You're not so bad when you get used to it..."
        mc "Well, thanks I guess..."
        m 5a "I can promise you, [player] was very well behaved!"
        m "Isn't that right?"
        mc "Aww come on..."
        "Handling both of their teasing is starting to be come a bit much for me to bare..."
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
m 2l "Ah, well, I don't think taking a slight detour from my normal route would make me late or anything."
show monika 2e
n 1q "Yeah, I guess..."
show monika 2m
"There's a bit of an awkard pause between us as the other students begin clearing the hallways."
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
"We wave goodbye to Natsuki as we head our seperate ways."
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
"Monika takes a step closer to me and leans into my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm completely left dazed as I watch Monika gracefully walk down the hallway and turn the corner towards the the otherside of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sitdown, refusing to make eye contact with anyone as I process what had just happened."
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
"Everyone in the hallway suddently turns towards me."
"I hastily turn to face who I just bumped into."
show monika surprised at t21 zorder 1
show yuri 3o at t22 zorder 2
play music e16 fadein 1.0
"It's Yuri!"
mc "Oh, no! Are you okay, Yuri?"
$ y_name = "Yuri"
y "Uuuu....{w=0.38}I'll be alright."
"I look down to see the pile of books that Yuri dropped."
"I'm able to recongize Portrait of Markov among her textbooks."
"She really doesn't leave home without it seems..."
mc "I'll get that for you..."
"I bend down to pick up Yuri's books."
m "Y-{w=0.38}Yuri!"
m "You startled us!"
y 3q "Sorry about!"
y "I should really pay more attention to where I'm going..."
m 2n "Ah, you have no reason to be sorry."
m 2e "I'm just glad you're okay."
mc "Well, if anyone should be apologizing it should be me, I'm the one that bumped into you."
y 2s "Well, I guess we both owe an apology to each other..."
mc "Yeah...{w=0.38}I'm really sorry..."
show yuri 2c
"I'm barley able to lift up all of Yuri's textbooks and hand it to her."
mc "Jeez...{w=0.38}are those advanced level course textbooks?"
y 3d "Yep! I'm taking three this semester!"
"Poor girl..."
mc "Well, I'm impressed you can carry all that!"
y 3i "It's a side beneift when you're taking these advanced classes!"
y 3d "It really builds up your arm strength!"
m 2l "Yeah, I know what you mean! Lifting those textbooks isn't for the feint of heart!"
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
        y 3q "T-{w=0.38}that's nice, [player]..."
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
        mc "I should probaby be thanking you..."
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
        m 2k "That way, we all get to spend more time together as club!"
        y 2d "I'd certainly love that!"
        "It's truly amazing that a few weeks ago, I probably wouldn't ever thought about any of this..."
        "Sharing a lunch period with the prettiest girls I've ever met..."
        "It's almost a dream come true!"
        mc "Yeah...{w=0.38}it'd be nice!"
        m 2e "Well, I'm really glad you got to join me for lunch, [player]..."
        mc "I should probaby be thanking you..."
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
        mc "I should probaby be thanking you..."
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
m 2l "Ah, well, I don't think taking a slight detour from my normal route would make me late or anything."
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
"We wave goodbye to Yuri as we head our seperate ways."
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
"Monika takes a step closer to me and leans into my ear."
show monika smirk
m "Try not to overthink~"
"She suddenly pulls on my tie."
m 5a "And make sure your tie is straight silly."
show monika 1j at t11 zorder 1
m "See you later~"
show monika at thide
hide monika
"I'm completely left dazed as I watch Monika gracefully walk down the hallway and turn the corner towards the the otherside of the school."
"I catch a few of my classmates smirking at me in the corner of my eye."
"Flustered, I just walk into my classroom and hastily sitdown, refusing to make eye contact with anyone as I process what had just happened."
jump day3_mono



label day3_hallway2:
scene bg corridor
with wipeleft_scene
"I make my up through the crowded hallways up towards the second floor."
"My eyes can't help but wander back and forth to the other various people walking with me."
"I can't help but focus on all the couples walking around me."
"What did it take for them to get together?"
"How big of a decision was it for them?"
"Did they have to to struggle like I did?"
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
"Wait a second...{w=0.38}I recongize that yelling anywhere..."
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
            show monika 2m
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
            "There's a bit of an awkard pause between us as the other students begin clearing the hallways."


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
                show monika 2m
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
                "There's a bit of an awkard pause between us as the other students begin clearing the hallways."





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
"I'm really lucky that Sayori's bad at detecting sarcasam..."
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
"I wave goodbye to Sayori as we head our seperate ways."
jump day3_mono



label n_hallway_interaction2:
$ n_name = "???"
n "Hey! What's up?!?"
"I hear someone yelling to me from across the hallway."
"Wait a second...{w=0.38}I recongize that voice..."
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
n 3x "Well you sure know how to complement a lady!"
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
        "Other then online, there really isn't too many other people I talk to outside the club..."
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
        mc "You're the best cook I know, so if we ever had a lunch together, I'd be set"
        n 5w "Well hangon! I didn't say you could mooch off of me!"
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
"I wave goodbye to Natsuki as we head our seperate ways."
jump day3_mono

label y_hallway_interaction2:
$ y_name = "???"
play sound "sfx/fall2.ogg"
y "EEEK!"
"While I wasn't looking, I bumped into someone, causing them to immediately drop all their textbooks."
"Everyone in the hallway suddently turns towards me."
"I hastily turn to face who I just bumped into."
show yuri 3o at t11 zorder 1
play music e16 fadein 1.0
"It's Yuri!"
mc "Oh, no! Are you okay, Yuri?"
$ y_name = "Yuri"
y "Uuuu....{w=0.38}I'll be alright."
"I look down to see the pile of books that Yuri dropped."
"I'm able to recongize Portrait of Markov among her textbooks."
"She really doesn't leave home without it seems..."
mc "I'll get that for you..."
"I bend down to pick up Yuri's books."
y 3q "Sorry about!"
y "I should really pay more attention to where I'm going..."
show yuri 2q
mc "What do you mean?"
mc "If anyone should be apologizing it should be me, I'm the one that bumped into you."
y 2s "Well, I guess we both owe an apology to each other..."
mc "Yeah...{w=0.38}I'm really sorry..."
show yuri 2c
"I'm barley able to lift up all of Yuri's textbooks and hand it to her."
mc "Jeez...{w=0.38}are those advanced level course textbooks?"
y 3d "Yep! I'm taking three this semester!"
"Poor girl..."
mc "Well, I'm impressed you can carry all that!"
y 3i "It's a side beneift when you're taking those advanced courses."
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
        y 3b "I have all sorts of recipies I've been meaning to share with the club..."
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
        y 3d "In the meantie, my books to keep me company!"
        y 3m "Besides, I'm always able to get a good amount of work done during lunch period."
        mc "Sounds like a learn a thing or two from you.."
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
"I wave goodbye to Yuri as we head our seperate ways."
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

"Espically considering how Monika was with me earlier..."
"Was she...{w=0.38}flirting with me?"
"She was incredibly helpful to me today, that's for sure..."

if encore_sayoriquestion_1 == True:
    "Though she seemed to keep to herself when Sayori was around."

if encore_sayoriquestion_1 == False:
    "And she did help make things less awkward between me and [day3_hallway]."

"I don't know...{w=0.38}I know Monika wants to help me..."
"But is that all she wants though?"
"I mean, I don't see much of a reason she'd be interested in me..."

if hangout1 == "Monika" and hangout2 == "Monika":
    "And I've only just gotten to know her a little more recently..."
    "Is she really all that interested in me?"

if hangout1 == "Monika" and hangout2 == "Sayori" or hangout2 == "Natsuki" or hangout2 == "Yuri":
    "Other then today, I've only spent time around Monika on Monday..."
    "Though she did seem pretty excited around me for some reason..."

if hangout1 == "Sayori" or hangout1 == "Natsuki" or hangout1 == "Yuri" and hangout2 == "Monika":
    "Other then today, I've only spent time around Monika yesterday..."
    "When we got unexpectedly close to each other..."
    "And it did feel nice to be with her..."

if encore_sayoriquestion_1 == True:
    "But it wasn't right either..."

if encore_sayoriquestion_1 == False:
    "Almost as if it was meant to happen..."

"Well, I guess this all just ties into the questions Monika said I should ask myself..."
"But right now, I can't really decide on who I'd be the most happy with..."
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
"After long last, the bell rings, signfying that the school day is offically over."
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
    "With slight hesistance, I begin the walk with Sayoru to the literature club."
    show sayori at thide
    hide sayori

if encore_sayoriquestion_1 == False:
    "I try to put on the most enthusatic smile I possibly can."
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
    "With slight hesistance, I begin the walk with Sayori to the literature club."
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
s "Hey, Monika!"
m "How're you two?"
s 1x "I'm doing pretty well! Looking forward to another great day with you guys!"
m 2m "Awww, Sayori..."
mc "She's always a charmer."
s 2q "Teehee~"
m 3a "I take it you already have her poems, [player]?"
show sayori 1a

if poem_giver == "Natsuki":
    mc "Yeah, I got her's yesterday, just need your's and Yuri's"

if poem_giver == "Yuri":
    mc "Yeah, I got her's yesterday, just need your's and Natsuki's"

m 2e "Fortunately, I remembered to bring them, I'll give them to you by the time club's over."
mc "Alright."
m 1b "Well you guys can go sit down, we're gonna get started in a few minutes."
s 1r "Sounds good to me!"
show sayori at thide
hide sayori
show monika 1a at t11 zorder 1
"Monika leans in to whisper something to me as Sayori goes to sit down."
m 1e "So how're you holding up?"
mc "Still thinking over alot of stuff..."
mc "Though in case [poem_giver] asks about her confession letter, I have an idea of what I want to say."
m 2e "Well that's good."
m 2d "Still, this is a pretty sensitive topic for you two, so just be careful with what you want to say."
mc "I'll try my best."
m 2j "Great!"
m 2b "Well, I'll be here if you want to talk more, [player]!"
mc "RIght now, I think I could use something to calm me down a bit..."
mc "It's been a fairly stressful day for me thinking about all this..."
m 2m "Whenever, I'm feeling stressed out, I find that music usually helps calm the nerves..."
m 2e "I've been working on something if you want to give it a listen..."
mc "I'll think about it, thank you Monika!"
m 2k "Anytime!"
show monika at thide
hide monika
"Monika goes back to the teacher's desk, leaving me standing in the middle of the room once again."
"Looking around the room, I try to figure out who I can talk to without completely melting down or making some sort of scene..."
"So, of course that leaves [poem_giver] out of question..."
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
        if hangout2 == "Monika:
            jump day3_choice5


#Just Monika, No Yuri

if poem_giver == "Yuri":
    if hangout1 == "Monika":
        if hangout2 == "Monika:
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
    madechoice = show_rigged_choice(narrator, "Who should I hang out with?", [("Monika.", "true"), ("Sayori.", "false"),("Yuri.", "false")],197)


#Rigged Choice, No Yuri
label day3_choice4:

python:
    #"Who should I hang out with?"
#        renpy.say(narrator, ""Who should I hang out with?", interact=False)
#        madechoice = renpy.display_menu[("Monika.", "true"), ("Natsuki.", "false"),("Yuri.", "false")]), screen="encore_rigged_choice")
    madechoice = show_rigged_choice(narrator, "Who should I hang out with?", [("Monika.", "true"), ("Natsuki.", "false"),("Sayori.", "false")],197)


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
