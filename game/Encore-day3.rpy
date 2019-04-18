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
"After finishing my morning routine, I head downstairs to my kitchen."
"I'm not particularly hungry so I decide to just make myself a fruit bowl for breakfast."
"While making it, I send Sayori a text to let her know that I'm up and she doesn't need to come wake me up again."
"Surprisingly, she responds back rather quickly and tells me that she's already waiting outside for me."
"I reply back that I'll meet her as soon as I'm done with my breakfast."
"As I'm eating, I come to the realization that I'll probably be getting everyone else's poems today..."

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


"Maybe I can ask Monika, maybe she knows how to handle this..."
"I sigh to myself as I pop the last piece of watermelon into my mouth, grab my backpack, and head outside to meet Sayori."



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
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completetly empty..."
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
            mc "And it didn't say alot of nice things about you guys either..."
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
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completetly empty..."
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
            mc "And it didn't say alot of nice things about you guys either..."
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
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completetly empty..."
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
            mc "And it didn't say alot of nice things about you guys either..."
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
            mc "I opened this door, and I was back at the club, but it was after hours and the room was completetly empty..."
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
            mc "And it didn't say alot of nice things about you guys either..."
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
            "I'm surprised by Sayori's sudden change of heart, but nevertheless, I choose to oblige."
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
"Especially since we started to move past on Sunday."
"Now she's thinking who knows what inside that head of hers..."
"And what does she mean she's had weird dreams too?"
"It's not like we've went through the same thing..."
show sayori 1k at t11 zorder 2
jump day3_sayo2

label day3_sayo1:
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
pass # Temporary

label day3_sayo2:
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
    mc "It's...{w=0.38}something related for what we're doing on Monday."
    s 1k "Okay..."
    mc "Hey, Sayori..."
    s 1g "Yeah?"
    mc "Don't worry about me, if I feel worse, I'll go to the nurse's office and you can take me home, okay?"
    s 1l "Okay..."
    s 1i "But if you feel sick, you text me right away, okay?"
    mc "You have my word, emergency contact."
    show sayori 1y
    "I see Sayori blush slightly."

    if encore_sayoriquestion_1 == True:
        s "You trust me that much, huh?"
        mc "Why wouldn't I?"
        mc "I mean we've been looking after each other for a while now..."
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

label day3_convo_3:
"I'm not used to it being this quiet, especially around Sayori."
"Lately, we've been more than happy to talk about whatever was on our minds, but today's different..."
show sayori 1k at t11 zorder 2
"She hasn't even looked at me once since we started walking."
"Part of me regrets not telling her about the last two nights."
"I didn't want her to get worked up about it, but instead I've got her now worrying about me."
show sayori 1f
"I really do appreciate her concern, but she can't really help me with this..."
"I just have to power through this!"
jump day3_sayo

label day3_sayo:
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


if tell_s == False:
    s 1l "Are you really sure you're okay?"
    s 1g "You've really been acting strange..."
    mc "I guess I just have alot on my mind."
    s 1k "I see..."


    if encore_sayoriquestion_1 == True:
        show sayori 2g
        "Even though I told Sayori not to worry about me, she keeps giving me glances every now and then."
        "As much as I appreciate her concern, she does need to learn when to focus on herself."
        show sayori 1k
        "That's her biggest flaw."
        "Well, I guess that's what it means to be in a relationship..."
        "Still, maybe I should've told her about these dreams..."

    if encore_sayoriquestion_1 == False:
        "Even though I told Sayori not to worry about me, she keeps giving me glances every now and then."
        "As much as I appreciate her concern, she does need to learn when to focus on herself."
        show sayori 1k
        "That's her biggest flaw."
        "Still, maybe I should've told her about these dreams..."
        show sayori 1g
        "Knowing how things are between us, I don't want her to feel that I'm purposefully closing myself off from her again."
        "Especially how we were able to open up to each other yesterday..."


show sayori 1k at t11 zorder 2
"I turn to Sayori, trying to smile hopefully at her, but she's just looking blankly down the road ahead of us as we walk in unison down the sidewalk."
"I let out a small sigh."
"I guess she's just not in a talkative mood..."
"Hopefully she'll get over this soon."
"However, I quickly realize that I have another problem brewing..."
"[poem_giver]'s letter..."
"I haven't even really had the time to think about how I'm going to handle that..."
"And I don't exactly feel prepared too either..."
show sayori 1g
"Telling Sayori right now doesn't seem like a good option either, considering how she is."
"I guess my only real option is to go to Monika..."
"I'm really not looking forward to the club today..."
"What if someone else gives me another confession letter?"
s "[player]?"
"Sayori takes me out of my train of thought."
mc "Y-{w=0.38}yeah?"
s "You okay? You just suddenly stopped there for a second."
mc "I did?"
"Realizing that Sayori is more than a few steps ahead of me, I quickly run up to catch up to her."

if tell_s == True:
    s 1l "Are you really sure you're okay?"
    s 1g "You've really been acting strange..."
    mc "I'll be fine..."
    mc "I've gone through worse."
    s 1h "Maybe you should stay home from school today."
    s 1k "I wouldn't want you to feel any worse..."
    show sayori 1f
    mc "I would if I could, but I really need to talk to Monika about something."
    s 2h "M-{w=0.38}Monika?"
    s 2g "Why?"
    mc "It's...{w=0.38}something related to the event."
    s 1k "Okay..."
    mc "Hey, Sayori..."
    s 1g "Yeah?"
    mc "Don't worry about me, if I feel worse, I'll go to the nurse's office and you can take me home, okay?"
    s 1l "Okay..."
    s 1i "But if you feel sick, you text me right away, okay?"
    mc "You have my word, emergency contact."
    show sayori 1y
    "I see Sayori blush slightly."

    if encore_sayoriquestion_1 == True:
        s "You trust me that much, huh?"
        mc "Why wouldn't I?"
        mc "I mean we've been looking after each other for a while now..."
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
