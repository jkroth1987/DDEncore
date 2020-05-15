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



#Sayori Route/Variations

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
                jump day5_swalk_s1
                #This section is the good terms sequence

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Natsuki?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk_s1

        if poem_giver == "Yuri":
            "I know she said she's going to make things up with Natsuki after what she said, but can she?"
            "Will Natsuki even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Yuri?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Yuri and the others to back off and respect our relationship."
                jump day5_swalk_s1

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Yuri?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk_s1



    if s_makeup == False:

        if n_love == True or y_love == True:
            "I really should've talked to her yesterday..."
            "Now it feels like I'm walking into this whole thing blind!"
            "Then again, I'm about to meet her in a few minutes..."
            "Maybe we'll talk about everything then..."
            "If she's better that this..."
            jump day5_swalk_s2
            #Sayori Romance Endings
            #Break Up/Unfriend Sequence



        else:
            "I dobut she even wants to talk to me right now, let alone see me!"
            "I should've taken her up on the chance to talk things through..."
            "Who knows what kind of state of mind she's in?"
            "Well, hopefully she's feeling better about everything now..."
            "I just hope I didn't struck too bad of a nerve..."
            jump day5_swalk_s3
            #Cold Shoulder Sequence


#Natsuki Route/Variations

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
        jump day5_swalk_s2



    if n_makeup == False:
        "I really should've talked things through with her yesterday..."
        "She probably thinks I either hate her or I'm pinning all this on her..."
        "On the other hand, maybe she's cooled off..."
        "I know I can't run from her forever."
        "Maybe I'll get to talk to her before the club today."
        "There's definitely a lot to talk about..."
        "And I need to talk to Sayori too..."
        "Well, she should be waiting outside for me..."
        jump day5_swalk_s3



#Monika Route/Variations

if hangout3 == "Monika":
    "Monika..."

    if m_makeup == True:
        "How're things going to go down with her?"
        "I'm sure that Monika can smooth things over with [poem_giver], but..."
        "Are things really going to be the same after today?"
        "I don't think Monika's the type of person who can just forgive a person for hitting her like that..."
        "But, it's been a strange few days. Who knows what will happen..."

        if encore_sayoriquestion_1 == True:
            jump

        if encore_sayoriquestion_1 == False:
            jump


    if m_makeup == False:
        "How's she going to react when she sees me?"
        "I really wish we got to talk about what happened..."
        "Even though what she said to [poem_giver] was awful, I can't entirely pin the blame on her."
        "It's ultimately my fault everything happened..."
        "And Monika probably thinks I'm blaming it all on her."
        "Well, maybe we'll get to smooth things over in the club."
        "There's certainly going to be plenty to talk about..."

        if encore_sayoriquestion_1 == True:
            jump

        if encore_sayoriquestion_1 == False:
            jump 




#Yuri Route/Variations


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
        jump day5_swalk_y


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
        jump day5_swalk_y




label day5_swalk_s1:
scene bg residential_day
with wipeleft_scene
"As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
show sayori 1d at t11 zorder 1
mc "Hey, Sayori..."
s 1k "Hello, [player]..."
"Sayori's voice drifts off into a whisper as she anxiously stares in the direction of school."
"I can't say I blame her..."
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
jump day5_confront_s

label day5_swalk_s2:
scene bg residential_day
with wipeleft_scene
"I walk out the front door and look around to see that Sayori is no where to be seen."
"As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
"I fully turn myself around to find a piece of paper taped to my door."
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
"For the first time in recent memory, I begin the trek to school alone."
scene bg class_day
with wipeleft_scene
"The walk to school was dreadful, but I somehow managed to keep my mind off of things long enough for me to get to school and through my first few classes."
"But as the day progressed, my feeling of self-worth only continued to dwindle with my interest in paying attention to my classes."
"At first, I thought they'd be a decent distraction for me to forget about the mess I'm going to have to deal with later..."
"But my mind always brings itself full circle to remind me how awful I've treated Sayori..."

if encore_sayoriquestion_1 == True:
    "She's my girlfriend! How could've I been so stupid to throw away what we had?!?"

if encore_sayoriquestion_1 == False:
    "She was my best friend! How could've I forgotten that she was still sensitive around me and that I needed to be careful?!?!"


"It doesn't matter now..."
"I blew it..."
"I needed to take the time to talk to her..."
"Regardless of how this turns out, she'll likely never want anything to do with me ever again..."
"Well, there's nothing I can do about it right now..."
"Things are just going to have to wait..."
"Hopefully I'll get the chance to explain myself to Sayori sooner or later and we can go from there..."
"Whatever we decide..."

if hangout3 == "Sayori":
    jump day5_confront_s

if hangout3 == "Natsuki":
    "It really sucks that I'm really going to have to choose between her and Natsuki..."
    "I never wanted that to happen..."
    jump day5_confront_n

if hangout3 == "Monika":
    "It really sucks that I'm really going to have to choose between her and Monika..."
    "I never wanted that to happen..."
    jump day5_confront_m

if hangout3 == "Yuri":
    "It really sucks that I'm really going to have to choose between her and Yuri..."
    "I never wanted that to happen..."
    jump day5_confront_y




label day5_swalk_s3:
scene bg residential_day
with wipeleft_scene
"As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
show sayori 1d at t11 zorder 1
mc "Hey, Sayori..."
s 1k "Hello, [player]..."
"Sayori's voice drifts off into a whisper as she anxiously stares in the direction of school."
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


if hangout3 == "Sayori":
    s "If you want to stay together, you need to commit yourself to that..."

if hangout3 == "Natsuki" or "Monika" or "Yuri":
    s "If you want to go to [hangout3], fine..."
    s "I'll learn to deal with it...."


s 1k "So, whatever you decide, just get it over with."
mc "I will."
show sayori 1f
"Sayori glances at me with uncertainty before letting out another sigh and begining our walk to school."
show sayori at thide
hide sayori
scene bg corridor
with wipeleft_scene
"The entire walk was uncomfortably silent."
"From our houses to school, to even when we were navigating the school's hallways, Sayori didn't utter a word to me once."
"In retrospect, she probably didn't want me to say anything. I probably would've just found a way to make it worse."
show sayori 1f at t11 zorder 1

if encore_sayoriquestion_1 == True:
    "She's my girlfriend! How could've I been so stupid to treat so terribly when her mental state is on the brink?!?"

if encore_sayoriquestion_1 == False:
    "She's my best friend! How could've I been so stupid to treat so terribly when her mental state is on the brink?!?"

"After today, it honestly wouldn't surprise me if Sayori and I end up splitting after this is all resolved..."
show sayori 1k
"She hasn't exactly been giving me encouraging signs either..."
"Well whatever happens, I need to face the consquences..."
"Whatever happens, I deserve it."
"But hopefully, I can avoid a worst case scenario..."
"As we're walking to Sayori's class, the hallways become increasingly crowded as students make their way to their first class."
"But even that feels off."
"Hardly anybody's talking to each other, and aside from the occasional sound of somebody opening or closing their locker or walking past us, there's hardly an audible sound throughout the hallway."
"After several minutes of increasingly uncomofrtable silence, we finally reach Sayori's classroom."
show sayori 1f
"Sayori and I just simply stare at each other, unsure of what's the best thing to say to break the ice without breaking each other further..."
"I let out a sigh and try to say the most diploamtic thing that comes to mind..."
mc "I'll see you later at the club, okay?"
mc "We'll get through this, together."
s 1k "Alright, [player]."
s "I'll see you then."
show sayori at thide
hide sayori
"Without even looking at me once, Sayori silently walks into her classroom."
"Looks like it's going to be worst case scenario after all..."
"I mutter some curse words to myself before walking off in the direction of my classroom."
jump day5_confront_s




label day5_confront_s:
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
    "{cps=20}She deserves to feel like that after what she did to Sayo-{nw}"
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
    jump day5_leadup1

if poem_giver == "Yuri":
    "I see a flash of pink before it retreats from my sight."
    mc "It’s alright, Natsuki. Come in."
    "I try to sound as inviting as possible, but I probably ended up coming across just as sarcastic."
    show natsuki 1u at t11 zorder 1
    "Still, she seems to have accepted the invite. Natsuki slolwy opens the rest of the door and steps into the clubroom."
    "We struggle to make eye contact with one another, let alone speak to each other."
    n 1q "H-{w=0.38}hello...{w=0.38}[player]"
    mc "Hey...{w=0.38}Natsuki."
    show natsuki 1s at t11 zorder 1
    "Natsuki carefully sets her stuff down, but she doesn’t sit."
    show natsuki 1n at t11 zorder 1
    "Instead, she turns around to face me."
    "She looks restless, yet remorseful."
    "Can’t say I don't blame her."
    show natsuki 1u at t11 zorder 1
    "{cps=20}She deserves to feel like that after what she did to Sayo-{nw}"
    "I catch myself mid thought."
    show natsuki 1n
    "Now I see what Sayori meant. She didn’t want me to have these malicious and vengeful thoughts about the others."
    show natsuki 5m
    n "I know you're probably the last person you want to here from right now, but..."
    show natsuki 5r
    "Natsuki struggles to keep going. Her face lights up in embarrassment as I see tears start to form in her beautiful, pink eyes."
    "I'll lend her a hand here..."
    show natsuki 5n
    mc "It’s alright Natsuki. I think you should save it for later. I imagine we’ll probably all talk about what happened yesterday and try to find a way forward not just as a club...{w=0.38}but as friends."
    show natsuki 5q
    n "Okay..."
    show natsuki 1u
    "Natsuki walks to the back of the room and sets her stuff down, but not before turning to face me one last time."
    n 5m "Y-{w=0.38}you don’t hate me...{w=0.38}right?"
    show natsuki 4n
    "I struggle to find the right words to articulate my feelings torwards Natsuki at the present moment."
    "I want to avoid upsetting her..."
    show natsuki 5n
    mc "I don’t hate you, Natsuki."
    show natsuki 5t
    n "Well, that's a relief..."
    show natsuki 5m
    mc "But, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."
    show natsuki 5u
    "Natsuki's relieved expression quickly evaporates."
    n 5q "Oh...{w=0.38}I see..."
    n 5m "I kinda figured you still would be. You have every right too."
    n 5n "But, maybe we can all forgive each other and move past all this..."
    mc "I hope so, Natsuki."
    n 5m  "{cps=25}I just hope that Yuri-{nw}"
    play sound "sfx/closet-open.ogg"
    show yuri 3v at t41 zorder 1
    show natsuki 5p at t43 zorder 3
    "Before Natsuki could finish her sentence, the door opens and Yuri enters the room."
    show yuri 2n
    show natsuki 2s at t43 zorder 3
    "She looks to Natsuki, who quickly averts her eyes away from Yuri."
    show natsuki 5s
    "Yuri’s eyes then lock onto mine as I continue my icy stare."
    show yuri 2o
    "She tries to say something but she quickly catches herself and takes a seat on the far side of the room away from us."
    show yuri at thide
    hide yuri
    show natsuki 5u at t11 zorder 1
    "I quietly sigh to myself."
    "I am not looking forward to talking to her..."
    show natsuki at thide
    hide natsuki
    jump day5_leadup1



label day5_leadup1:

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

if s_makeup == False:
    "Even I have no excuse for how I've been treating her..."

if else:
    pass


"I decide to tell them just like it is..."

if encore_sayoriquestion_1 == True:
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

    if s_makeup == False:
        mc "I've messed up our relationship enough, and I just want to get us back to where we were before all this happened."
        mc "Those are my true feelings."

    if else:
        pass

if encore_sayoriquestion_1 == False:
    mc "Look...{w=0.38}Sayori's my best friend."
    mc "I care about her. Always have, always will."
    mc "I care about all of you, but some of the things you said to her and each other, is honestly disappointing."
    show monika 1h
    show sayori 1t
    show yuri 3v
    "One by one the girls shoot either and irritated or dejected look at me, but Sayori only smiles as she holds back tears."
    mc "I don't want anyone to ruin the friendship I have with her."
    mc "But I don't want to upset any of you either. That was never my intention and I'm sorry that it came across like that."
    mc "I have a lot of my mind and I don't know who I'm really settled on."
    show monika 2h
    show natsuki 4n
    mc "But I know that Sayori's my best friend, I care about her, and she needs me now more than ever."

    if s_makeup == False:
        mc "I've messed up our friendship enough, and I just want to get us back to where we were before all this happened."
        mc "That's how I really feel about all this..."

    if else:
        pass


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

if poem_giver == "Natsuki":
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
    jump day5_sayoricomfort

if poem_giver == "Yuri":
    show yuri 2o at t11 zorder 1
    "It's Yuri."
    show yuri 3y2
    y "Wait!"
    "I brush Yuri's arm off of mine and turn to directly face her."
    y 3o "Uuu...{w=0.38}how do I put this?!?"
    mc "What're you talking about?"
    y 3t "I’m...{w=0.38}I'm..."
    show yuri 4c
    "Yuri breaks eye contact as her face flushes bright red, shutting her eyes in an effort to fight back tears."
    show y_cry1 as yuri at t11 zorder 1
    "It ultimately proves futile, as tears start running down Yuri's cheeks."
    "She finally lets it all out."
    show y_cry3 as yuri at t11 zorder 1
    y "I'm sorry!!!"
    show y_cry5 as yuri at t11 zorder 1
    y "I'm sorry that I tried to ruin your relationship with Sayori!"
    show y_cry6 as yuri at t11 zorder 1
    y "I'm sorry for saying all those horrible things about her!"
    show y_cry4 as yuri at t11 zorder 1
    y "I'm sorry for hitting you! I never meant to harm you!"
    show y_cry2 as yuri at t11 zorder 1
    y "I'm...{w=0.38}sorry for everything..."
    "I stop for a minute, taking in what Yuri had just said as she stands in front of me, on the verge of a total breakdown."
    mc "Yuri..."
    show y_cry4 as yuri at t11 zorder 1
    y "Y-{w=0.38}yes?"
    "Her voice squeaks."
    mc "I’m not the one you need to apologize to right now."
    show y_cry1 as yuri at t11 zorder 1
    "Yuri breaks down into a hysterical sob. Before she's able to properly speak again, I'm already out the door."
    scene bg corridor
    "Just as I exit the room, I hear her cry out out to me."
    y "[player], wait!"
    y "I should-"
    jump day5_sayoricomfort


label day5_sayoricomfort:

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
jump day5_choice1




label day5_choice1:
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
"I slowly lose my consciousness as I feel Monika's cold hand grab my throat."
"I begin to feel as if everything in my body is rushing to my throat."
"I would vomit, but my stomach feels entirely empty and my throat numb to the point where I can't even tell if it's still there..."
"I try to let out a cry for help, but not even a squeak comes out..."
"My lungs are on fire, begging for me to take a breath."
"I can't even feel my arms and legs..."
"My head is spinning at a million miles an hour, it feels totally weightless..."
"My vision is filled red with blood..."
"I try to look to see if there's anything I can use to defend myself against Monika, but they won't stop looking at Monika's glowing emerald eyes..."
"I can't feel my arms and legs, they've gone completely numb..."
"It's no use..."
"I can't do anything..."
"..."
"So this is what it feels like to die..."
"I finally lose consciousness, with the last thing I see before everything goes dark is Monika's glowing green eyes..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
m "{cps=17}I'll see you soon. I just need to run a quick little errand...{nw}"
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
with dissolve_scene_full
jump day5_choiceleadup

label day5_v2:

mc "I'm going to give you a minute alone, okay?"
show sayori 1v
"Sayori meekly looks up at me, tears still running down her face."
"She doesn't say a word, but I interpret through her sniffles that she agrees."
mc "I'll...{w=0.38}wait outside..."
mc "Come out when you're ready to talk."
show sayori 4u
"Sayori stiffly nods as she goes back to burrying her face in her hands."
"As soon I exit out the door, I hear her soft sobs resume."
stop music fadeout 2.0
show sayori at thide
hide sayori
scene bg corridor
with wipeleft_scene
"I lean against the wall of lockers, asking myself if I just did the right thing."
"I've known Sayori for years. I know when she needs me and when she needs alone time..."
"But, maybe I've should've done more back there..."
$ m_name = "???"
m "[player]?"
show monika 1d at t11 zorder 1
$ m_name = "Monika"
"I look up to see Monika right standing in front of me."
mc "Oh! Hey, Monika! Didn't see you there!"
"I'm surprised I didn't even hear her coming..."
"Am I that out of it today?"
m 1l "Sorry! Didn't mean to sneak up on you there!"
show monika 1a
mc "You're good. Did [poem_giver] calm down yet?"
m 1m "Oh, she's fine now..."
m 1a "Did you find Sayori yet?"
mc "Yeah, she's in there."
"I gesture to the classroom right next to us."
mc "She just needs a minute or two."
m 1b "Perfect, a minute's all I'll need!"
mc "For?"
show monika 1a at face
"Monika suddenly gets right up in front of my face, almost pinning me to the locker."
mc "Uh...{w=0.38}Monika? What are you-"
m "Just try to relax. This won't take long..."
mc "{cps=20}What the hell are you-{nw}"
#show monika's glowing green eyes
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
"Without warning, Monika's eyes suddenly glow a bright emerald green as she clasps onto my shoulders."
"I'm barley able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barley process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
"..."
m "{cps=17}Thank you for making this easier on me...{nw}"
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
with dissolve_scene_full
jump day5_choiceleadup
