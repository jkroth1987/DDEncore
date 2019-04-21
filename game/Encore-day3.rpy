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
"Grabbing the money from my bag, I head out to the cafteria, hoping to find Monika."
play music t6 fadein 2.0
show bg cafeteria
with wipeleft_scene
"Enterting the cafteria, I immediately begin to look around for Monika."
"Alright, if I was Monika, where would I be?"
"..."
"Probably towards the center with all the other popular kids."
"I start walking to the center of the cafteria."
show bg cafeteria
with wipeleft_scene
"Sure enough, it didn't take me long to spot Monika sitting at one tables at the center of the room."
show monika 2k at t11 zorder 2
"As I expected, she seems to be chatting away with some of her friends."
"This might be harder than I thought."
"Well, I'm not going to get another chance at talk to her until the club, so it's now or never."
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
m 3e "I'm always happy to time for you."
"I feel my face heat up with slight embarassment."
mc "T-{w=0.38}thank you, Monika! I really appreciate it!"
m 1b "We'll be right back girls!"
r "Have fun you two!"
show monika at thide
hide monika
"I lead Monika out of the cafteria and to somewhere where we might have a little more privacy."
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
show monika 2n
mc "And I have no idea what I'm going to say..."
show monika 2m
m "Well, [player], it all depends on how you feel about her..."
m 2g "Do you...{w=0.38}like [poem_giver] back in the same way she likes you?"
mc "I mean..."

if encore_sayoriquestion_1 == True:
    show monika 2f
    mc "I'm dating Sayori...{w=0.38}and she needs me now more than ever..."
    m 2g "Do you love Sayori, [player]?"
    m 2p "Do you...{w=0.38}enjoy her company?"

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 1p
        m "Yeah..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 2m
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2n
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."



if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
            mc "I do."
            mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 2m
        m "But you haven't been spending a lot of time around Sayori in the club lately."
        mc "I haven't been trying to avoid her or anything..."
        mc "I've just wanted to get to know the others a little bit better."
        mc "I had fun spend some time around Natsuki on Monday..."

        if encore_festivalquestion_2 == "Natsuki":
            mc "It was nice catching up with her since the festival."

        if encore_festivalquestion_2 == "Yuri":
            mc "I didn't really get much of a chance to spend time around her before..."

        show monika 2e
        mc "And I'm glad we've finally got to spend some time around each other too..."
        m 2m "Y-{w=0.38}yeah...{w=0.38}it was nice..."
        mc "Though, to be honest, I wasn't expecting us to be like that yesterday..."
        mc "You did catch me by surprise..."
        m 2l "Yeah...{w=0.38}me neither..."
        m 2m "It just kind of happened..."
        m 2e "It felt...{w=0.38}nice being with you like that..."
        show monika 2n
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."



if hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
            mc "I do."
            mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        show monika 2n
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
        show monika 1q
        mc "And if I ever did leave her...{w=0.38}we both know she'd be devestated..."
        mc "We do mean a lot to each other..."
        show monika 2f
        mc "That much has become more clear to me lately."
        mc "She needs me around until she gets better."
        show monika 1p
        m "I see..."
        "I see Monika's eyes glance downward towards the ground."
        mc "Hey, Monika..."
        m 1g "Yeah?"
        mc "It was nice that we got to finally spend some time together on Monday."
        m 1m "Yeah...{w=0.38}it was..."
        m 1n "Anyways..."


if hangout1 == "Monika":
    if hangout2 == "Natsuki":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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


if hangout1 == "Monika":
    if hangout2 == "Monika":
        mc "I do."
        mc "I'm very happy with her and I wouldn't want to ruin it..."
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
        show monika 2n
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


if encore_sayoriquestion_1 == False:
    show monika 2f
    mc "Well..."

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        show monika 2f
        mc "I really don't know..."
        mc "I've enjoyed spending time around [poem_giver] she's been fun to be around..."
        mc "And last Sunday, I did feel like maybe there was something there..."
        mc "But Sayori's been on my mind a lot lately..."
        m 2g "You're not having second thoughs about your answer to her confession, are you?"
        show monika 2f
        mc "I don't know..."
        mc "I'm worried about her..."
        mc "I've know her practically my whole life..."
        show monika 2o
        mc "Ever since last Sunday, she's been acting different around me..."
        mc "She really didn't handle my response well..."
        mc "And since then, I've tried making things right with her..."
        show monika 1q
        mc "We've made some progress, but I don't really know how I feel about her..."
        m 2r "[player], it's not smart of you to play around with her feelings if you don't know how you feel about her..."
        m 2e "I'm happy to hear that you guys are working to make things right..."
        m 2m "But you're probably better off just being friends with her..."
        m 2e "I don't think she can handle anything more right now..."
        mc "Yeah...{w=0.38}you're right..."


if hangout1 == "Sayori":
    if hangout2 == "Natsuki":
        "sample"

if hangout1 == "Sayori":
    if hangout2 == "Yuri":
        "sample"

if hangout1 == "Sayori":
    if hangout2 == "Monika":
        "sample"

if hangout1 == "Natsuki":
    if hangout2 == "Sayori":
        "sample"


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
            mc "But if I ever told her Yuri gave me this, she'd flip out."
            m 2m "Yeah...{w=0.38}she would..."

        if encore_festivalquestion_2 == "Yuri":
            "sample"




if hangout1 == "Natsuki":
    if hangout2 == "Yuri":
        "sample"

if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        "sample"

if hangout1 == "Natsuki":
    if hangout2 == "Yuri":
        "sample"

if hangout1 == "Natsuki":
    if hangout2 == "Monika":
        "sample"

if hangout1 == "Yuri":
    if hangout2 == "Sayori":
        "sample"

if hangout1 == "Yuri":
    if hangout2 == "Natsuki":
        "sample"

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        "sample"

if hangout1 == "Yuri":
    if hangout2 == "Monika":
        "sample"

if hangout1 == "Monika":
    if hangout2 == "Sayori":
        "sample"

if hangout1 == "Monika":
    if hangout2 == "Natsuki":
        "sample"

if hangout1 == "Monika":
    if hangout2 == "Yuri":
        "sample"

if hangout1 == "Monika":
    if hangout2 == "Monika":
        mc "I really don't know..."
        mc "I've enjoyed spending time around her, she's been fun to be around..."
        mc "And I had a blast with her last Sunday!"
        show monika u114311
        "But...{w=0.38}it's been nice getting to know you too, Monika."
        show monika 2m
        mc "Especially since we really haven't talked that much since recently..."
        m 2e "It's been...{w=0.38}nice getting to know you too, [player]..."
        m 2n "It must have taken a lot for you to muster up the courage to finally talk to me..."
        mc "Well..."
        m 1e "Come on, [player]..."
        m 5a "I've seen the way you've looked at me..."
        m "How you're always stumbling over your sentences when I compliment you..."
        m "How I take your breath away whenever I get close to you..."
        m "It's really sweet~"
        mc "Monika, I..."
        "I'm completely left speechless."
        mc "I really have always wanted to get to know you..."
        show monika 2m
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
