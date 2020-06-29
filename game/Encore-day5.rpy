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
"Throw a guy like me into the mix, and it's a recipe for drama..."
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
                jump day5_walk1
                #This section is the good terms sequence

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Natsuki?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_walk1

        if poem_giver == "Yuri":
            "I know she said she's going to make things up with Natsuki after what she said, but can she?"
            "Will Natsuki even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Yuri?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Yuri and the others to back off and respect our relationship."
                jump day5_walk1

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Yuri?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_walk1



    if s_makeup == False:

        if n_love == True or y_love == True:
            "I really should've talked to her yesterday..."
            "Now it feels like I'm walking into this whole thing blind!"
            "Then again, I'm about to meet her in a few minutes..."
            "Maybe we'll talk about everything then..."
            "If she's better that this..."
            jump day5_walk2
            #Sayori Romance Endings
            #Break Up/Unfriend Sequence



        else:
            "I doubt she even wants to talk to me right now, let alone see me!"
            "I should've taken her up on the chance to talk things through..."
            "Who knows what kind of state of mind she's in?"
            "Well, hopefully she's feeling better about everything now..."
            "I just hope I didn't strike too bad of a nerve..."
            jump day5_walk3
            #Cold Shoulder Sequence


#Natsuki Route/Variations

if hangout3 == "Natsuki":
    "Natsuki..."

    if n_makeup == True:
        "Not to mention, can I really expect her to make up with Yuri after what happened?"
        "I mean, they've fought before, but not like this..."
        "And it seems like everyone's pissed off at each other for something..."
        "Then again, Natsuki has surprised me with what she can do when she steps up..."
        "Let's just hope she can do it again..."
        "Maybe I can talk to her before the club..."
        "And I still need to talk to Sayori about what happened..."
        "Hopefully she's still willing to talk to me..."
        jump day5_walk2


    if n_makeup == False:

        if y_love == True:
            "I probably ruined everything with her by saying yes to Yuri's confession..."
            "But maybe there's a way to explain things..."
            "It's not going to be easy to explain, and I doubt she's going to believe me..."
            "Same for Yuri..."
            "I don't know how I'm going to face Natsuki..."

        if y_love == False:
            pass


        "I really should've talked things through with her yesterday..."
        "She probably thinks I either hate her or I'm pinning all this on her..."
        "On the other hand, maybe she's cooled off..."
        "I know I can't run from her forever."
        "Maybe I'll get to talk to her before the club today."
        "There's definitely a lot to talk about..."
        "And I need to talk to Sayori too..."
        "Well, she should be waiting outside for me..."
        jump day5_walk3





#Monika Route/Variations

if hangout3 == "Monika":
    "Monika..."

    if m_makeup == True:
        "How're things going to go down with her?"
        "I'm sure that Monika can smooth things over with [poem_giver], but..."
        "Are things really going to be the same after today?"
        "I don't think Monika's the type of person who can just forgive a person for hitting her like that..."
        "But, it's been a strange few days. Who knows what will happen..."
        "I still need to sort everything out with Sayori as well..."
        "Hopefully she'll meet outside..."
        jump day5_walk2


    if m_makeup == False:

        if y_love == True:
            "I probably ruined everything with her by saying yes to Yuri's confession..."
            "But maybe there's a way to explain things..."
            "It's not going to be easy to explain, and I doubt she's going to believe me..."
            "Same for Yuri..."

        if n_love == True:
            "I probably ruined everything with her by saying yes to Natsuki's confession..."
            "But maybe there's a way to explain things..."
            "It's not going to be easy to explain, and I doubt she's going to believe me..."
            "Same for Natsuki..."

        if else:
            pass

        "I don't know how I'm going to face Monika..."
        "How's she going to react when she sees me?"
        "I really wish we got to talk about what happened..."
        "Even though what she said to [poem_giver] was awful, I can't entirely pin the blame on her."
        "It's ultimately my fault everything happened..."
        "And Monika probably thinks I'm blaming it all on her."
        "Well, maybe we'll get to smooth things over in the club."
        "There's certainly going to be plenty to talk about..."
        "Speaking of things to talk about..."
        "I really need to sort things out with Sayori..."
        "Well, she should be outside..."
        jump day5_walk3





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
        jump day5_walk2


    if y_makeup == False:

        if n_love == True:
            "I probably ruined everything with her by saying yes to Natsuki's confession..."
            "But maybe there's a way to explain things..."
            "It's not going to be easy to explain, and I doubt she's going to believe me..."
            "Same for Yuri..."
            "I don't know how I'm going to face Yuri..."

        if n_love == False:
            pass

        "I really should've sat down with her yesterday..."
        "Who knows how she's handling all this..."
        "And if my suspicions about her cutting are right, this could be more dangerous than I thought..."
        "Maybe I can find out for sure later, even if the timing is pretty bad..."
        "It's not like I'm left with too many choices..."
        "Speaking of something else I can't avoid, I know I'm going to run into Sayori later as well..."
        "She's probably waiting outside for me right now, assuming she isn't completely done with me..."
        "Maybe I can turn all this around..."
        "Maybe there is a way to fix everything for good..."
        jump day5_walk3




label day5_walk1:
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
show sayori 1k
"Sayori nervously looks off again in the direction of the school."
"Though I can tell she's not just thinking about the club meeting today."
mc "What's wrong?"
show sayori 1l
"Sayori nervously laughs."
"Well that's not exactly an optimistic sign..."
s 1h "[player], I've been thinking about something..."
show sayori 1g
mc "Yeah?"
s 1k "Call it a long-shot, but..."
s 1l "I think it might help to heal the club if everyone from this point on was honest with each other..."
s 1g "I've been thinking about your idea, and well..."
s 1k "I think we should try it. For the good the club..."
"Sayori's voice trails off."
"I'm not sure if she's really up to this..."
show sayori 1g
mc "Are you sure, Sayori?"
s 1h "[player]..."
s 1g "Look..."
"Sayori brushes up against me and takes my hand in hers."
s 2h "If for whaetever reason things don't work out, it's fine..."
s 2k "I'd hate to lose them as friends, but..."
s 2t "I'll always have you..."

if encore_sayoriquestion_1 == True:
    s "I'm glad that I'm your girlfriend..."

if encore_sayoriquestion_1 == False:
    s "I'm glad that you're my friend..."

s 2l "Even though we've had our up's and down's, in the end, I think everything's going to be okay."
s 2d "Your real friends are the ones who stick by you in the end..."
s 2t "Like how you're here for me now, always taking care of me..."
mc "I just know I could've done a better job, Sayori..."
mc "This is all my fault."
s 2k "I bare some responsibility too, [player]..."
s 2h "They clearly have a misunderstanding with me, and well, I need to sort it out."
mc "We're really doing this together then, huh?"
s 2q "Yep!"
mc "I guess I wouldn't have it any other way."
show sayori 1d
"Sayori releases my hand and glances up at me with a hopeful, optimistic look in her eyes I haven't seen before..."
"Leave it to her to end up doing the inspiring for me..."
"Well, let's put this energy to good use."
"After a brief nod to each other, we begin our walk to school, ready to face down whatever might come our way..."
show sayori at thide
hide sayori
scene bg corridor
with wipeleft_scene
"As soon as we walked through the front doors, I felt a rather unsettling feeling hanging in the air."
show sayori 1k at t11 zorder 1
"At first, I wasn't sure if it was just me, but when I turned to Sayori I knew she felt it as well."
"Maybe it was just all in our heads, maybe it was something we ate..."
"But I can't say I've ever felt like this before..."
show sayori 1f
"Sayori turns to me, staring wearingly."
show sayori 1d
"I force a smile and that seems to be enough to reassure her that we're doing the right thing."
"As we're walking to Sayori's class, the hallways become increasingly crowded as students make their way to their first class."
show sayori 1k
"But even that feels off."
"Hardly anybody's talking to each other, and aside from the occasional sound of somebody opening or closing their locker or walking past us, there's hardly an audible sound throughout the hallway."
show sayori 1f
"Sayori and I share an uncomfortable look before we just decide to wave each other good-bye as I make my way to my own class."
show sayori at thide
hide sayori
jump day5_confront

label day5_walk2:
scene bg residential_day
with wipeleft_scene
"I walk out the front door and look around to see that Sayori is nowhere to be seen."
"As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
"I fully turn myself around to find a piece of paper taped to my door."
"That wasn't there before..."
"I anxiously walk up to my door for a closer look."
"Looks like it's a letter from Sayori...."
play sound page_turn


if encore_sayoriquestion_1 == True:
    #letter1
    call showpoem(poem=poem_s_breakup, music=False, track=None, revert_music=False, paper="blue_paper")

if encore_sayoriquestion_1 == False:
    #letter2
    call showpoem(poem=poem_s_unfriendzone, music=False, track=None, revert_music=False, paper="blue_paper")

"..."
"Oh no..."
"I crumble up the paper in my hand as I feel my eyes staring to water and anger course through my veins."
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
    "She was my best friend! How could have I forgotten that she was still sensitive around me and that I needed to be careful?!?!"


"It doesn't matter now..."
"I blew it..."
"I needed to take the time to talk to her..."
"Regardless of how this turns out, she'll likely never want anything to do with me ever again..."
"Well, there's nothing I can do about it right now..."
"Things are just going to have to wait..."
"Hopefully I'll get the chance to explain myself to Sayori sooner or later and we can go from there..."
"Whatever we decide..."

if hangout3 == "Sayori":
    jump day5_confront

if hangout3 == "Natsuki":
    "It really sucks that I'm really going to have to choose between her and Natsuki..."
    "I never wanted that to happen..."
    jump day5_confront

if hangout3 == "Monika":
    "It really sucks that I'm really going to have to choose between her and Monika..."
    "I never wanted that to happen..."
    jump day5_confront

if hangout3 == "Yuri":
    "It really sucks that I'm really going to have to choose between her and Yuri..."
    "I never wanted that to happen..."
    jump day5_confront




label day5_walk3:
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


if hangout3 == "Sayori":
    mc "I'm sorry that I've been treating you so badly..."
    mc "I've been incredibly disrespectful of our relationship and you've done nothing to deserve it..."

if hangout3 == "Natsuki" or hangout3 == "Monika" or hangout3 == "Yuri":
    mc "I'm sorry for causing all this drama and leaving you in the dark about everything..."


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
s 1i "I'm not putting up with it anymore."
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
show sayori 1k
"Sayori nervously looks off again in the direction of the school."
"Though I can tell she's not just thinking about the club meeting today."
mc "What's wrong?"
show sayori 1l
"Sayori nervously laughs."
"Well that's not exactly an optimistic sign..."
s 1h "[player], I've been thinking about something else..."
show sayori 1g
mc "Yeah?"
s 1k "Call it a long-shot, but..."
s 1l "I think it might help to heal the club if everyone from this point on was honest with each other..."
mc "I don't see anything wrong with that..."
s 1g "I think everybody needs to understand each other. What we're really like outside of school and the club..."
s 1k "So..."
s "I'm thinking about telling everyone about my depression..."
"Sayori's voice trails off."
"I'm not sure if she's really up to this..."
show sayori 1g
mc "Are you sure, Sayori?"
s 1l "Well it's either that or things are just going to keep happening again and again..."
s 1k "And as Vice President, I need to do everything that I can to ensure that it doesn't."
mc "I 100 percent agree with you, Sayori."
mc "I'll be right there to support you. You can count on it."
"Sayori glances at me with uncertainty before letting out another sigh and beginning our walk to school."
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
"Well whatever happens, I need to face the consequences..."
"Whatever happens, I deserve it."
"But hopefully, I can avoid a worst case scenario..."
"As we're walking to Sayori's class, the hallways become increasingly crowded as students make their way to their first class."
"But even that feels off."
"Hardly anybody's talking to each other, and aside from the occasional sound of somebody opening or closing their locker or walking past us, there's hardly an audible sound throughout the hallway."
"After several minutes of increasingly uncomfortable silence, we finally reach Sayori's classroom."
show sayori 1f
"Sayori and I just simply stare at each other, unsure of what's the best thing to say to break the ice without breaking each other further..."
"I let out a sigh and try to say the most diplomatic thing that comes to mind..."
mc "I'll see you later at the club, okay?"
mc "We'll get through this, together."
s 1k "Alright, [player]."
s "I'll see you then."
show sayori at thide
hide sayori
"Without even looking at me once, Sayori silently walks into her classroom."
"Looks like it's going to be worst case scenario after all..."
"I quietly curse to myself before walking off in the direction of my classroom."
jump day5_confront


label day5_confront:
scene bg class_day
with wipeleft_scene
"For the rest of the day, it almost seems like time has stopped entirely."
"It feels like I'm just simply trapped in an empty room with no one else around me, staring blankly ahead at an empty board."
"Even though that's not the case, I'm really just not paying attention. Not that I ever do."
"But for once maybe I should, that would help wash down the dread I've been feeling since I woke up this morning, but the material is just so boring!"
"I just simply lean back in my seat and nod occasionally to whatever the teacher is saying, and silently pray that he doesn't call on me to answer one of his questions."
"Still, this has to eventually end, right?"
"I look over at the clock and see that there's about a half hour left before class is over and I can face my fears in the literature club."
"Oh well, if there's one thing I know how to do, it's kill time."
"I decided to map out on paper some of the possible scenarios of what could happen in the club, trying to account for the good, the bad and the ugly..."
"Thankfully it still looks like I'm paying attention as everyone else around me is writing down notes on what the teacher's saying."
"Being the diligent student as always..."
scene black
with close_eyes
scene bg class_day
with open_eyes
$ renpy.pause(delay=0.2, hard=True)
play sound school
"At long last, the school bell finally rings. Though I can't say if it was for better or worse that class is over..."
"I stand up and slide the books off my desk and into my bookbag as I start the inevitable walk to the literature club."
scene bg corridor
with wipeleft_scene
"I'm sure to take my time getting to the Literature Club."
"Usually, I'd be in a rush to get there. But today's different..."
"As I'm walking, the anxiety I've been feeling all day only gets worse and I begin to question the whole point of this."
"What if we are able to come to terms with what happened and move on?"
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


if hangout3 == "Sayori" or hangout3 == "Monika":

    if poem_giver == "Natsuki":
        "I see a flash of purple before it retreats from my sight."
        mc "It’s alright, Yuri. Come in."
        "I try to sound as inviting as possible, but I probably ended up coming across just as sarcastic."
        show yuri 3o at t11 zorder 1
        "Still, she seems to have accepted the invite. Yuri slowly opens the rest of the door and steps into the clubroom."
        "We struggle to make eye contact with one another, let alone speak to each other."
        y 3p "H-{w=0.38}hello...{w=0.38}[player]..."
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
        "I struggle to find the right words to articulate my feelings towards Yuri at the present moment."
        "I want to avoid upsetting Yuri..."
        show yuri
        mc "I don’t hate you, Yuri."
        show yuri 3l
        "Yuri lets out a relieved sigh."
        show yuri 3c
        y "Oh, thank goodness!"
        show yuri 3e
        mc "But, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."

        if hangout3 == "Monika":
            mc "And how you treated Monika was beyond inappropriate."


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
        jump day5_leadup

    if poem_giver == "Yuri":
        "I see a flash of pink before it retreats from my sight."
        mc "It’s alright, Natsuki. Come in."
        "I try to sound as inviting as possible, but I probably ended up coming across just as sarcastic."
        show natsuki 1u at t11 zorder 1
        "Still, she seems to have accepted the invite. Natsuki slowly opens the rest of the door and steps into the clubroom."
        "We struggle to make eye contact with one another, let alone speak to each other."
        n 1q "H-{w=0.38}hello...{w=0.38}[player]..."
        mc "Hey...{w=0.38}Natsuki..."
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
        n "I know you're probably the last person you want to hear from right now, but..."
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
        "I struggle to find the right words to articulate my feelings towards Natsuki at the present moment."
        "I want to avoid upsetting her..."
        show natsuki 5n
        mc "I don’t hate you, Natsuki."
        show natsuki 5t
        n "Well, that's a relief..."
        show natsuki 5m
        mc "But, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."

        if hangout3 == "Monika":
            mc "And how you treated Monika was beyond inappropriate."

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
        jump day5_leadup

if hangout3 == "Natsuki":
    "I see a flash of pink before it retreats from my sight."
    mc "It’s alright, Natsuki. Come in."
    "I try to sound as inviting as possible, but I probably ended up coming across as awkward."
    show natsuki 1u at t11 zorder 1
    "Still, she seems to have accepted the invite. Natsuki slowly opens the rest of the door and steps into the clubroom."
    "We struggle to make eye contact with one another, let alone speak to each other."
    n 1q "H-{w=0.38}hello...{w=0.38}[player]..."
    mc "Hey...{w=0.38}Natsuki..."
    show natsuki 1s at t11 zorder 1
    "Natsuki carefully sets her stuff down, but she doesn’t sit."
    show natsuki 1n at t11 zorder 1
    "Instead, she turns around to face me."
    "Her eyes struggle to meet mine. It takes a few moments before she finally finds her voice."
    show natsuki 5q
    n "So...{w=0.38}you ready for this?"
    show natsuki 5n
    mc "No. I can't say I honestly am."
    n 3t "Well, good! Me neither..."
    n 1q "I'm still having a hard time wrapping my head around this..."
    n 5u "I just never thought the club would be brought to this point..."
    show natsuki 5n
    mc "If you told me a week ago that things would be the way they are now, I would've called you crazy."
    n 5t "Eh, even if you did believe me, you still would've called me crazy..."
    mc "Maybe..."
    show natsuki 5s
    "Natsuki crosses her arms and nervously glances at the floor."
    mc "What's wrong?"
    show natsuki 5q
    "Natsuki sighs."
    n 5r "Ah, there's no point in hiding this since you already know..."
    n 5m "But, I've been thinking..."
    show natsuki 5n
    mc "Yes?"
    n 5m "I think everyone needs to be on the same page with each other."
    n 5q "So no one makes the same mistakes again with what happened yesterday..."
    show natsuki 5n
    mc "Where are you going with this?"
    n 3q "I think it's time I told everyone about my home situation."
    "My heart nearly stops at the news."
    "Is she serious?!?"
    mc "You're...{w=0.38}sure you want to do that?"
    show natsuki 1n
    "Natsuki simply nods."
    mc "Well, if you think it's the time for it, it's the time for it."
    n 1m "It is."
    n 1q "I just don't know if I'm ready to say it. It's not like I rehearsed anything."
    show natsuki 1u
    mc "I mean, I'll help set things up for you, but just tell them what you told me."
    show natsuki 1x
    n "It's not the same!"
    n 1u "You, I actually trust..."

    if n_makeup == True:
        if y_love == True:
            n 1q "More or less..."
            n 1m "Them? Right now? I'm not so sure."
            n 5n "But I need to get this off my chest..."
            n 4t "And I'm glad we sorted things out between us yesterday..."
            mc "Me too..."
            show natsuki 5n
            "Natsuki tries to shoot me an optimistic smile but she can tell I'm not really in the mood to return the favor."
            show natsuki 5u
            n "Yeah, I don't blame you. It's hard to see a bright side to any of this."
            n "The last 24 hours really haven't been pretty."
            show natsuki 5n
            mc "And I'm really the one to blame for all that."
            mc "This is all my fault."
            show natsuki 5u
            mc "I risked our friendship, and possibly more, with what I did yesterday."
            mc "I still can't believe you found it in you to forgive me..."
            "Natsuki stands frozen for a few moments, as if she's second guessing why she agreed to make up with me."
            n 5q "Look, [player]..."
            n 2m "I know you mean well. I know that because I've gotten to know you. I don't think your a bad person at heart."
            n 2q "You've made a lot of stupid choices, but it means something that you're willing to try fix things..."
            n 2l "And I appreciate that!"
            n 5q "But, we'll just see how things go..."
            show natsuki 5n
            mc "Yeah..."
            mc "Thanks, Natsuki. What you just said really means a lot."
            n 5t "Oh, don't mention it!"
            n 5s "I just really want to get this over with so we can get back to reading manga!"
            mc "Maybe we can get some reading in now..."


    if n_makeup == True:
        if y_love == False:
            n 1q "Without a shadow of a doubt..."
            n 1m "Them? Right now? I'm not so sure."
            n 5n "But I need to get this off my chest..."
            n 4t "I'm glad we at least sorted things out between us yesterday..."
            n "It crosses one thing off our massive to-do list..."
            mc "That's true..."
            show natsuki 5n
            "Natsuki tries to shoot me an optimistic smile but she can tell I'm not really in the mood to return the favor."
            show natsuki 5u
            n "Yeah, tell me about it. This sucks."
            n 5q "I never wanted any of this drama..."
            show natsuki 5n
            mc "No one did."
            mc "I just wanted us to all get along..."
            mc "I didn't know that us growing closer together was going to piss off everyone else."
            n 4q "Well we can't go back and change that."
            n 4t "But you know? Despite all this, I'm really glad we got to know each other."
            n 5t "You've really been a great friend to me, [player]. I honestly couldn't have asked for anyone better."
            show natsuki 5a
            "I can't help but smile at Natsuki's compliment."
            "At least we can both go into this with a somewhat good mood..."
            n 4k "Say, since we have some time on our hands before everyone else starts showing up, you wanna read some manga?"
            show natsuki 4l
            mc "You know it!"
            n 5z "Great!"

    if n_makeup == False:
        if y_love == True:
            n 12a "Well..."
            n 12b "Trusted..."
            show natsuki 12d
            "Natsuki's voice breaks as she tightly clenches her fists."
            mc "Natsuki?"
            n 12c "Don't."
            n 12a "If you love Yuri, fine! Be with her!"
            n 5u "It's just nice to know that I wasted my time on another stupid boy..."
            mc "Natsuki..."
            mc "Look, I messed up. You have every right to be angry at me."
            mc "I don't know why I said yes to her..."
            mc "But, I felt that if I said no, I would've hurt her..."
            n 5m "And what about me, [player]?"
            n 5u "Did you think about how I would feel?"
            mc "I did. I was put in a lose-lose situation."
            n 5r "Yeah, right..."
            n 5q "So why tell me this now? Why didn't you tell me yesterday?"
            show natsuki 5n
            mc "I was just as angry as you. I needed to cool off. We all did."
            mc "But, I see that I made another mistake..."
            n 5q "That's all you do."
            show natsuki 5u
            "I sigh."
            mc "Look, when we all sit down and talk about what happened, will you just at least listen with an open mind?"
            "Natsuki stares at the floor for a few moments before responding to me."
            n 3g "Fine. But you better have one hell of an excuse."
            mc "I'm done offering excuses."
            n 3h "I guess we'll see."
            show natsuki 5s
            "Natsuki finally sits down."

    if n_makeup == False:
        if y_love == False:
            show natsuki 1q
            n "Well..."
            n 12a "Maybe..."
            show natsuki 1u
            "Natsuki nervously grimaces."
            mc "What's wrong?"
            show natsuki 5u
            "Natsuki lets out a shaky breath before proceeding."
            n 5m "Y-{w=0.38}you don’t hate me...{w=0.38}right?"
            show natsuki 4n
            "I struggle to find the right words to articulate my feelings towards Natsuki at the present moment."
            "I want to avoid upsetting her..."
            show natsuki 5n
            mc "I don’t hate you, Natsuki."
            mc "And I still really care about you..."
            show natsuki 5t
            n "Well, that's a relief..."
            show natsuki 5m
            mc "But, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."
            show natsuki 5u
            "Natsuki's relieved expression quickly evaporates."
            n 5q "Oh...{w=0.38}I see..."
            n 5m "I kinda figured you still would be. You have every right too."
            show natsuki 5n
            mc "I wish we got the chance to talk about this beforehand..."
            n 4t "Yeah, it'd save some of this awkwardness..."
            n 5m "But look, I just want you to know that I didn't mean what I said to Sayori and I hope I can make things right."
            n 5q "For everybody..."
            show natsuki 5n
            mc "I know you will."
            show natsuki 5a
            "I force a smile to alleviate Natsuki's anxiety, something which she seems to take kindly to."
            n 5t "Hey, you know something? Maybe we'll finally get everything settled and we can go back to the way things were before all this..."
            n "I really miss reading manga with you..."
            mc "I do too, Natsuki."



    n 5q  "{cps=25}I just hope that Yuri-{nw}"
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
    jump day5_leadup




if hangout3 == "Yuri":
    "I see a flash of purple before it retreats from my sight."
    mc "It’s alright, Yuri. Come in."
    "I try to sound as inviting as possible, but I probably ended up coming across just as sarcastic."
    show yuri 3o at t11 zorder 1
    "Still, she seems to have accepted the invite. Yuri slowly opens the rest of the door and steps into the clubroom."
    "We struggle to make eye contact with one another, let alone speak to each other."
    y 3p "H-{w=0.38}hello...{w=0.38}[player]..."
    mc "Hey...{w=0.38}Yuri."
    show yuri 2o at t11 zorder 1
    "Yuri carefully sets her stuff down, but she doesn’t sit."
    show yuri 2n at t11 zorder 1
    "Instead, she turns around to face me."
    "Her eyes struggle to meet mine. It takes a few moments before she finally finds her voice."
    show yuri 3t
    y "You know, I'm not really sure if I'm ready for this..."
    y 3q "I've never been involved in anything quite this dramatic before..."
    show yuri 3e
    mc "I can't say I have either."
    y 3h "I mean who would've thought that the club would be brought to this point?"
    y 1o "I know I share some of the responsibility, but maybe if I didn't act out, maybe things would be better..."
    show yuri 1e
    mc "Yuri..."
    mc "This is mostly my fault. I wouldn't blame yourself."
    mc "But hopefully, we can make things right again here."
    show yuri 1o
    y "Yeah, me too..."
    "Yuri's voice trails off as she anxiously stares at the floor."
    mc "What's wrong?"
    y 3p "What? Nothing! Nothing!"
    y 2q "Nothing's wrong..."
    show yuri 1n
    mc "Yuri..."
    "How do I put this delicately?"
    mc "Look, I'm not holding you solely responsible for what happened. I think we all deserve some of the blame."
    show yuri 3v
    mc "You said some things that obviously shouldn't have been said, and I shouldn't have walked out on you guys."
    mc "But I'm hopeful we'll be able to reconcile everyone's differences..."
    show yuri 3w
    "Yuri lets out a sigh."
    y 3v "[player], to be honest with you, that's not the only reason I'm worried right now..."
    mc "Well, what is it? Maybe I can help ease your mind over things..."
    y 3n "Just don't tell anyone about this, okay?"
    mc "I promise."
    show yuri 3w
    "Yuri clasps her hands together and takes a big breath of air in."
    y 3q "Okay..."
    y "So, I think it's prudent that in order to avoid future drama, I think we need to shed light about some of our personal problems..."
    mc "Go on..."
    y 3v "So...{w=0.38}I-{w=0.38}I want to open up about a...{w=0.38}problem I've been having..."
    y 1o "For a while now..."
    "Yuri slowly puts her arms behind her back."
    mc "Do you...{w=0.38}want to tell me what it is now and help you practice for it?"
    y 1n "N-{w=0.38}no! I don't think that'll be necessary..."
    y 1v "Honestly I don't know if I trust myself to even talk about it in front of anyone else..."
    mc "Well, I can help give you a nudge when I talk, but why don't you trust yourself?"
    y 3w "I've never told anyone else about it..."
    y 3u "And it took me until recently to acknowledge that something was really wrong with me..."
    y 3q "So to share this information with others is...{w=0.38}kind of a big jump for me..."
    mc "I understand."
    mc "But I'm glad you trust me enough to tell me about this."


    if y_makeup == True:
        if n_love == True:
            y 1u "I think I trust you enough..."
            y 1v "I can't really say the same about the others right now..."
            y 3w "However, I know what must be done..."
            y 3u "I consider us fortunate that we sorted things out between us yesterday..."
            mc "Me too..."
            show yuri 3q
            "Yuri tries to shoot me an optimistic smile but she can tell I'm not really in the mood to return the favor."
            y "Well, I can't blame you for not seeing any upside to our present situation. Truthfully, there probably isn't much other than the understanding we reached."
            y 3l "The last 24 hours have been rather nightmarish..."
            show yuri 3e
            mc "And I'm really the one to blame for all that."
            mc "This is all my fault."
            show yuri 1t
            mc "I risked our friendship, and possibly more, with what I did yesterday."
            mc "I still can't believe you found it in you to forgive me..."
            show yuri 1g
            "Yuri stands frozen for a few moments, as if she's second guessing why she agreed to make up with me."
            y 1w "[player]..."
            y 3h "I know you always try to do your best. I know that because I've gotten to know who you are as a person. I don't think you go out of your way to do bad things..."
            y 3f "You have made some bad choices, but it means something that you've acknowledged them and are trying to make things right again."
            y 1b "I find that rather appreciative, provided something like this doesn't happen again."
            y 1q "But, we'll just have to see how things go now, won't we?"
            show yuri 1a
            mc "Yeah..."
            mc "Thanks, Yuri. What you just said really means a lot."
            y 1i "I try my best."
            y 1k "I just hope this saga concludes so that we can get back to reading."
            mc "Well, maybe we can get some reading in now..."


    if y_makeup == True:
        if n_love == False:
            y 1u "I completely trust you, [player]..."
            y "Beyond a reasonable doubt..."
            y 1v "I can't really say the same about the others right now..."
            y 3w "However, I know what must be done..."
            y 3u "I consider us fortunate that we sorted things out between us yesterday..."
            y 3j "That's one less important thing to do..."
            mc "That's true..."
            show yuri 3q
            "Yuri tries to shoot me an optimistic smile but she can tell I'm not really in the mood to return the favor."
            y "Well, I can't blame you for not seeing any upside to our present situation. Truthfully, there probably isn't much other than the understanding we reached."
            y 3l "It's all just really unfortunate..."
            show yuri 3e
            mc "No one did."
            mc "I just wanted us to all get along..."
            mc "I didn't know that us growing closer together was going to piss off everyone else."
            y 1h "Well there's nothing we can do about the past now."
            y 1s "I will say though, I'm glad I got the opportunity to get to know you better."
            y 3t "You've been a good friend to me, [player]. I really can't thank you enough for it!"
            show yuri 3s
            "I can't help but smile at Yuri's compliment."
            "At least we can both go into this with a somewhat good mood..."
            y 3i "You know, since we should have some time before everyone starts to show up, would you like to do some reading?"
            show yuri 1a
            mc "You know it!"
            y 1c "Fantastic!"

    if y_makeup == False:
        if n_love == True:
            y 1v "There was a time where I completely trusted you..."
            y 1w "But my trust in you has been shaken..."
            show yuri 4c
            "Yuri's voice breaks as her faces flushes red and looks away."
            mc "Yuri?"
            y "Save your breath."
            y 2r "If you love Natsuki, fine! You can be with her!"
            y 4c "I'll just live with knowing the fact that I wasted my time..."
            mc "Yuri..."
            mc "Look, I messed up. You have every right to be angry at me."
            mc "I don't know why I said yes to her..."
            mc "But, I felt that if I said no, I would've hurt her..."
            y 4c "Did you think about that decision would affect me?"
            mc "I did. I was put in a lose-lose situation."
            y "I'm sure it was..."
            y "So why spring this on me now? Why didn't you accept my offer for me to come and talk?"
            mc "I was just as angry as you. I needed to cool off. We all did."
            mc "But, I see that I made another mistake..."
            y 1h "That's all you've done."
            show yuri 1h
            "I sigh."
            mc "Look, when we all sit down and talk about what happened, will you just at least listen with an open mind?"
            "Yuri stares at the floor for a few moments before responding to me."
            y 1h "Fine. I'll listen, but I want no more excuses."
            mc "I'm done offering excuses."
            y 1q "I guess we'll see."


    if y_makeup == False:
        if n_love == False:
            y 3v "Well, I'm not entirely sure if I really do trust you, [player]..."
            show yuri 3q
            "Yuri nervously laughs and grimaces."
            mc "What's wrong?"
            show yuri 3o
            y "Euuuuu...."
            show yuri 4c
            "Yuri nervously turns herself away from me."
            mc "Yuri, you can tell me. Don't worry."
            "Yuri let's out a shaky breath before meekly turning around."
            y  "Y-{w=0.38}you don’t hate me...{w=0.38}right?"
            "I struggle to find the right words to articulate my feelings towards Natsuki at the present moment."
            "I want to avoid upsetting her..."
            show yuri 4a
            mc "I don’t hate you, Yuri."
            mc "And I still really care about you..."
            show yuri 2k
            "Yuri sighs in relief."
            y 2q "Good! I was worried that you would blame yesterday's events all on me..."
            show yuri 1e
            mc "Well, I’m still very...{w=0.38}disappointed with you for what you said to Sayori especially."
            show yuri 2o
            "Yuri's relieved expression quickly evaporates."
            y "I...{w=0.38}understand..."
            y 1q "I figured as much."
            y 2h "I just wish we had the chance to discuss this yesterday..."
            mc "Yeah, I wish I took you up on that offer now..."
            y 1q "Well, there's no use worrying about that now..."
            y 1f "While we're on the subject of yesterday's incident..."
            y 1q "I do want to personally apologize to you for my behavior not just towards you, but to Sayori and the others as well..."
            y 3w "I just hope everyone can forgive each other."
            mc "I'm sure things will be back to normal in time."
            show yuri 1s
            "I force a smile to alleviate Yuri's anxiety, something which she seems to take kindly to."
            y 2u "Hopefully once everything has calmed down, we can go back to reading..."
            y 2j "I really do miss reading with you..."
            show yuri 1a
            mc "I do too, Yuri."


    y 1f "{cps=25}I just hope that Natsuki-{nw}"
    play sound "sfx/closet-open.ogg"
    show natsuki 5u at t41 zorder 1
    show yuri 2p at t43 zorder 3
    "Before Yuri could finish her sentence, the door opens and Natsuki enters the room."
    show natsuki 5n
    show yuri 2o at s43 zorder 3
    "She looks to Yuri, who quickly sits down and buries herself in her book."
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
    jump day5_leadup





label day5_leadup:
scene bg club_day
with wipeleft_scene
show monika 1o at t21 zorder 1
show sayori 1k at t22 zorder 2
"After a few more minutes of waiting, Monika arrives in with Sayori."
"I’m a little surprised to see them walk in together."
"I guess that’s what was keeping them."
"Maybe Sayori made amends with Monika already. At least that'd make things a little easier..."
show monika at thide
hide monika
show sayori 1g at t11 zorder 1
"Monika walks to the front of the room as Sayori takes her usual spot next to me."

if hangout3 == "Sayori":
    show sayori 1d at t11 zorder 1
    "Sayori shoots me a hopeful grin."
    "I manage a smile back."
    "I guess that this is it..."

if hangout3 == "Natsuki" or hangout3 == "Monika" or hangout3 == "Yuri":
    show sayori 1f
    "Sayori and I briefly lock eyes before she turns away to face Monika."
    show sayori 1k
    "I wish we could've talked sooner, but..."


"There's no turning back now..."
"I prepare for the inevitable as Monika calls out to us."
show monika 3n at t21 zorder 1
show sayori 1b at t22 zorder 2
m "Okay, everyone..."
show monika 3r
"She says that far less enthusiastically than she normally does."
show monika 3q
"I detect a hint of sadness in Monika’s voice."
"Looks like she really wasn’t looking forward to today either..."
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
"For whatever reason, my anxiety keeps spiking every time she talks..."
"Maybe it's just the guilt..."
"I glance at the others who are all looking down at the floor in shame."
m 1h "Something...{w=0.38}must be done about this."
"Monika then stops pacing and is now directly in front of me. The room is dead quiet."
show monika 5a
"She forms her signature smile at me. But rather than feel welcomed or reassured, I only continue to feel more anxious..."
show monika smirk
m "So, I think it’s important that we’re all on the same page going forward."
m "Given that we were all arguing about [player] yesterday, and our bickering made him walk out on us..."
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
"They we’re all being jerks to each other yesterday. They know it!"
"But what I say next could very well determine if this club continues to stay together..."
"And, it's time I finally come to terms with my feelings."
"I take a moment to collect my thoughts before letting out a sigh and finally starting."

if hangout3 == "Sayori":
    jump day5_confront_s

if hangout3 == "Natsuki":
    jump day5_confront_n

if hangout3 == "Monika":
    jump day5_confront_m

if hangout3 == "Yuri":
    jump day5_confront_y


label day5_confront_s:

if encore_sayoriquestion_1 == True:
    mc "Look...{w=0.38}the truth is...{w=0.38}I’m in love with Sayori."
    show monika 1h
    show sayori 1t
    show yuri 3v
    "One by one the girls shoot either an irritated or dejected look at me, but Sayori only smiles as she holds back tears."
    mc "I really don’t think that there’s anything that’s going to change that."
    mc "I chose to be in this relationship with her not to spite any of you..."
    "My voice starts to break."
    show monika 2h
    show natsuki 4n
    mc "But...{w=0.38}because I’ve come to realize lately..."
    mc "I love her...{w=0.38}and she needs me now more than ever..."

    if s_makeup == False:
        mc "I've caused enough drama to our relationship, and I just want to get us back to where we were before all this happened."
        mc "Those are my true feelings."

    else:
        pass

if encore_sayoriquestion_1 == False:
    mc "Look...{w=0.38}Sayori's my best friend."
    mc "I care about her. Always have, always will."
    mc "I care about all of you, but some of the things you said to her and each other, is honestly disappointing."
    show monika 1h
    show sayori 1t
    show yuri 3v
    "One by one the girls shoot either an irritated or dejected look at me, but Sayori only smiles as she holds back tears."
    mc "I don't want anyone to ruin the friendship I have with her."
    mc "But I don't want to upset any of you either. That was never my intention and I'm sorry that it came across like that."
    mc "I have a lot of my mind and I don't know who I'm really settled on."
    show monika 2h
    show natsuki 4n
    mc "But I know that Sayori's my best friend, I care about her, and she needs me now more than ever."

    if s_makeup == False:
        mc "I've messed up our friendship enough, and I just want to get us back to where we were before all this happened."
        mc "That's how I really feel about all this..."

    else:
        pass


show yuri 1e
show sayori 1k
"I turn to Sayori, signaling to her that it’s her turn to speak."
s 1l "R-{w=0.38}right..."
show sayori 1k at t42 zorder 2
show monika 2c
show yuri 1e
"Sayori promptly stands up."
show sayori 1k
"She shakedly breathes in and out, tears welling in her eyes."
show sayori 1v
s "E-{w=0.38}everyone...{w=0.38}the...{w=0.38}thing...{w=0.38}thing is..."
show natsuki 5n
"Sayori looks at Monika, then to me, Natsuki and finally to Yuri."
show monika 1m
"Monika manages an uneasy grin as Natsuki and Yuri continue to look on at Sayori."
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
"Monika says irritably."
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
    n 12i "I’m sorry for saying all those things I shouldn't have..."
    n 12f "I’m sorry for hitting you..."
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
    "Just as I exit the room, I hear her cry out to me."
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
    "Just as I exit the room, I hear her cry out to me."
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
mc "You were afraid of falling and hurting yourself."
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
"Our eyes lock onto each other. Our faces barely a few inches apart."
mc "Just to even try to climb that fence...{w=0.38}all by yourself...{w=0.38}to me, that was so brave of you to do, Sayori."
mc "I was proud of you then, just like I am now."
mc "And I...{w=0.38}guess I caught you again, didn't I?"
mc "You'll be fine, and we'll get to enjoy all these crazy adventures again..."
mc "I wouldn't want to do it with anyone. That spot's reserved for my one true love."
"Sayori's face is now totally red from both crying and blushing."
"It's a miracle that I haven't cracked a tear yet myself, but it's definitely getting there..."
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
"After everything that's happened in the last 24 hours or so, it's hard to believe we finally got to this point..."
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
play music e23 fadein 1.0
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
"Out of nowhere, a thunderstorm rolls up on us."
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
"The next thing I know, it's nighttime, and all the stuff in the classroom has vanished."
"Not only that, but we're all standing in different spots..."
s 4w "Guys, what's going on?!?!"
s 4v "I'm scared..."
"I turn to Monika, whose standing completely still in the middle of the room with her eyes closed."
show sayori 1v
mc "Monika?"
"She doesn't respond."
mc "Monika?"
"I say loudly."
"I reach my hand out to put on Monika's shoulder."
mc "Monika, are you alright?"
show sayori at thide
hide sayori
show monika 1q at t11 zorder 1
"I put my hand on Monika's shoulder, she still doesn't respond."
"{cps=25}Moni-{nw}"
play audio scary_scream
show monika strobe as monika at face
"I immediately fall backwards and scurry away from Monika."
show sayori 4w at t21 zorder 1
show m_unleashed1 as monika at t22 zorder 2
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
show m_unleashed2 as monika at t32 zorder 1
show sayori 2w at t42 zorder 2
$ style.say_dialogue = style.normal
scene bg empty_classroom
show m_unleashed2 as monika at t32 zorder 1
show sayori 2w at t42 zorder 2
"Monika teleports right next to Sayori and tightly grabs her shoulder."
show m_unleashed2 as monika at s32 zorder 1
show sayori 2w at s42 zorder 2
play sound "sfx/fall.ogg"
"Sayori again yells in pain as she is forced to her knees by Monika."
"Meanwhile, I find myself at the back of the room, unable to get up or speak."
"What the hell is going on?!?!"
"What is this?!?!"
"Sayori tries to fight to get Monika off of her, but she too seems to be frozen in place."
$ style.say_dialogue = style.edited
m "I've waited a long time for this..."
$ style.say_dialogue = style.normal
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
show m_unleashed2 as monika at t22 zorder 2
"Without warning, Sayori's body is broken apart into little pieces that repeatedly revolve around themselves mid-air."
"I honestly can't believe what I'm seeing..."
"This can't be real!"
"This has to be another dream!"
$ style.say_dialogue = style.edited
s "H̵͗͜e̵͐̀l̷̐͛p̸͕̍ ̴͗̅m̵̩̆e̸̐̂ ̶̀̒M̵̌̚Ć̶͊"
$ style.say_dialogue = style.normal
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.25
stop sound
hide screen tear
hide image "mod_assets/sprites/end-glitch2.png"
hide screen tear
show bg space_room
show mask_2
show mask_3
show m_unleashed1 as monika at t11 zorder 1
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
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"I turn around and I see Monika slowly walking towards me."
"I begin pounding on the door, screaming for Natsuki, Yuri or anyone to help me."
"The closer Monika gets to me, the more lightheaded I become..."
"I can't see straight...."
"My breathing becomes ragged as I feel splitting pain in my head..."
"I think there's blood in my eyes..."
show m_unleashed1 as monika at face
"Monika towers over me, the emerald light glowing in the place of her eyes."
show m_unleashed2 as monika at face
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
"I try to look to see if there's anything I can use to defend myself, but my eyes won't stop looking at Monika's..."
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

stop music fadeout 2.0
m "{cps=17}I'll see you soon. I just need to run a quick little errand...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup

label day5_v2:
mc "I'm going to give you a minute alone, okay?"
show sayori 1v
"Sayori meekly looks up at me, tears still running down her face."
"She doesn't say a word, but I interpret through her sniffles that she agrees."
mc "I'll...{w=0.38}wait outside..."
mc "Come out when you're ready to talk."
show sayori 4u
"Sayori stiffly nods as she goes back to burying her face in her hands."
"As soon as I exit out the door, I hear her soft sobs resume."
stop music fadeout 2.0
show sayori at thide
hide sayori
scene bg corridor
with wipeleft_scene
"I lean against the wall of lockers, asking myself if I just did the right thing."
"I've known Sayori for years. I know when she needs me and when she needs alone time..."
"But, maybe I've should've done more back there..."
play music e23 fadein 1.0
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
m 1b "Perfect, that's all I'll need!"
mc "For?"
show monika 1a at face
"Monika suddenly gets right up in front of my face, almost pinning me to the locker."
mc "Uh...{w=0.38}Monika? What are you-"
m "Just try to relax. This won't take long..."
mc "{cps=20}What the hell are you-{nw}"
show m_unleashed1 as monika at face
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"Without warning, Monika's eyes suddenly glow a bright emerald green as she grabs onto my shoulders."
"I'm barely able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barely process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
"..."
stop music fadeout 2.0
m "{cps=17}Thank you for making this easier on me...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup



label day5_confront_n:
mc "Look...{w=0.38}the truth is...{w=0.38}I have feelings for Natsuki..."
mc "I've been spending quite a bit of time around her recently, and well, I like her..."
show monika 1h
show sayori 1g
show yuri 3v
show natsuki_sweet as natsuki at t44 zorder 4
"One by one the girls shoot either an irritated or dejected look at me, but Natsuki only smiles as she holds back tears."
mc "I really don’t think that there’s anything that’s going to change that."
mc "I want to be in a relationship with her not to spite any of you..."
"My voice starts to break."
show monika 2h
show sayori 1k
mc "But...{w=0.38}because I’ve come to realize lately..."
mc "She...{w=0.38}needs me..."


if encore_sayoriquestion_1 == True:
    show sayori 1u
    "I turn to Sayori, who is on the verge of tears."
    mc "I also need to address something..."
    show natsuki 1m
    show yuri 1p
    mc "I've been dating Sayori for the last couple of weeks as well..."
    "Natsuki and Yuri turn to me with a shocked expression on their faces."
    "Monika, on the other hand, simply glares at me."
    mc "This week I haven't been loyal to her..."
    mc "I-{w=0.38}I've let her down..."
    show sayori 1v
    mc "I don't blame her for not wanting to associate herself with me anymore, and I understand why."
    mc "But I think everyone needs to be on the same page as each other so there's no more drama..."


if encore_sayoriquestion_1 == False:
    pass

show yuri 1e
show sayori 1k
"I turn to Natsuki, signaling to her that it’s her turn to speak."
n 5q "R-{w=0.38}right..."
show natsuki 5s at t44 zorder 4
show monika 2c
show yuri 1e
show sayori 1f
"Natsuki promptly stands up."
"She shakedly breathes in and out, tears welling in her eyes."
show natsuki 42b
n "E-{w=0.38}everyone...{w=0.38}the...{w=0.38}thing...{w=0.38}thing is..."
show natsuki 12a
"Natsuki looks at Monika, then to me, Sayori and finally to Yuri."
show monika 1m
"Monika manages an uneasy grin as Sayori and Yuri continue to look on at Natsuki."
show natsuki 12d
"I didn’t realize how hard this would be for Natsuki to come out about her home life."
"Maybe we should've had a dry run..."
n 12e  "I..."
n 12f "I..."
"I give Natsuki an encouraging nod."
"Come on Natsuki...{w=0.38}you can do this!"
show n_shock as natsuki at t44 zorder 4
n "I can’t do this!"
show natsuki 12f
show natsuki at lhide
hide natsuki
show monika 1a at t31 zorder 1
show sayori 1n at t32 zorder 2
show yuri 3f at t33 zorder 3
"Natsuki bolts out from her seat and rushes out the door past Monika, loudly sobbing."
"Crap..."
"I quickly turn to Monika."
show monika 1h
"Monika’s grin quickly evaporates."
mc "Let me go after her! Please!"
show monika 1r
"Monika sighs."
m 1q "Go for it."
"Monika says irritably."
"What the hell is up with her?"
"Oh well, I’ll deal with it later."
show monika at thide
hide monika
show yuri at thide
hide yuri
show sayori at thide
hide sayori
"Just as I’m about to run after Natsuki, I feel someone grip on my arm."
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
y "I'm sorry that I tried to ruin your relationship with Natsuki!"
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
"Just as I exit the room, I hear her cry out to me."
y "[player], wait!"
y "I should-"
jump day5_natsukicomfort




label day5_natsukicomfort:
play sound "sfx/closet-open.ogg"
"The door shuts behind me."
"I'll deal with her later..."
"I gotta find Natsuki..."
scene bg corridor
with wipeleft_scene
mc "Natsuki?"
mc "Natsuki?!?"
mc "Where are you, dummy?"
"Damn it! Where could she be?"
"I wander up and down the halls aimlessly, looking for any sign of her."
"Eventually, I stumble upon an open door to one of the classrooms."
"I can hear someone sniffling and sobbing in there..."
"Yep, that has to be her..."
"I quietly enter the room, gently closing the door behind me."
scene bg class_day
with wipeleft_scene
"As soon as I get in, I see Natsuki curled up in the corner."
"I carefully approach and quietly call out her name."
mc "Natsuki?"
show natsuki 12h at s11 zorder 1
"Natsuki slowly looks up to to face me."
n 12i "G-{w=0.38}go away, [player]..."
n 12f "I don't want you to see me like this..."
show natsuki 12h
"I kneel down next to Natsuki."
mc "Why not?"
play music e19 fadein 1.0
"Natsuki stares at me with her glossy eyes."
n 12h "Eh?"
mc "Why don't you want me to see you like this?"
n 12f "Because I said so! Because I'm weak and pathetic! I barely own up to anything!"
n 12h "I'm not strong enough to do this, [player]! There's nothing you can do to help me!"
mc "That's where you're wrong, Natsuki."
n 12i "H-{w=0.38}how?"
show natsuki 12h
"Natsuki's voice shakes uncontrollably as tears continue to stream down her face and fall onto the floor."
n 12h "I'm emotionally unstable!"
n 12i "My only real 'talent' is pissing people off who care about me the most!"
n 12d "Why do you care so much about me? If you never talked to me, none of this would be happening right now!"
mc "That's not true."
n 12f "It is!"
n 12h "And I care so much about you and it hurts! It really hurts, [player]!"
n 12i "I haven't felt loved by anyone in years!"
n 12f "It took everything I had to open up to you about my real life..."
n 12i "They'll never give me the same chance you did!"
n 12f "Why is it whenever I love someone, I'm the one that always gets hurt?!?"
show natsuki 12e
n "It's not fair!"
show natsuki 12f
n 12g "And that's not the worst part!"
n 12i "My dad...{w=0.38}he..."
n 42g "He insults me in every way imaginable..."
n 42h "He...{w=0.38}even hits me..."
n 42d "And anytime I fight back, it gets worse..."
n 12f "No matter what I do...{w=0.38}I just can't win!"
"Natsuki breaks down again and resumes her sobbing."
"I take in a moment to absorb what Natsuki just said."
"I can't ignore something like this..."
"It doesn't help that she's being hysterical, but I'm not sure if it's possible to reason with her right now..."
"I don't want to leave Natsuki unattended, but maybe she needs a moment to calm herself down..."
"But, isn't it my job to be there for her in her time of need?"
jump day5_choice2




label day5_choice2:
    menu:
        "I should..."
        "Comfort Natsuki.":
            jump day5_v3
        "Leave Natsuki alone.":
            jump day5_v4



label day5_v3:
"I take a deep breath and gently put my hand on Natsuki’s shoulder."
show natsuki 12f
mc "Natsuki..."
show natsuki 12g
mc "I know now what it took for you to work up the courage to tell me what's really been happening with you outside of school..."
mc "I know that just to even admit to me..."
show natsuki 12f
mc "It took a lot of guts."
mc "I can't possibly imagine having to deal with what you've been going through for so long..."
show natsuki 12d
mc "You're a strong person for doing so. But we both know that you can't overcome this problem by yourself."
show natsuki 12f
mc "I know it may not seem like it now, but everyone at the club cares about you. They want to help you and fix the club."
show natsuki 12h
mc "If they didn't care or weren't willing to give you a chance, do you think that they would've showed up at all?"
show natsuki 12d
mc "As far as I could tell, everyone was respectfully listening to you."
mc "You were doing great, but you have to go back and finish telling your story."
show natsuki 12a
mc "And then maybe we can figure out how to get you out of your situation."
show natsuki 12b
n "Damn it..."
n 12a "W-{w=0.38}why do you always have to make so much sense when it matters?"
mc "It's because I..."
"I stop myself short."
"Am I ready to say that?"
"Is it too soon?"
n "What?"
n 12b "That you pity me?"
n 12c "I get it, I'm a short, helpless little girl who needs a big strong man to help fight her battles."
n 12d "I've heard it a hundred times now. It's getting old."
n 12c "I need to do this alone..."
n "Somehow..."
show natsuki 12a
mc "No, you don't need to do this alone. There's no shame in getting help for something like this."
show natsuki 12b
mc "Natsuki, it takes strength to put up with a home life that bad."
show natsuki 12a
mc "And that's just one thing I love about you..."
n 12b "Do you really think I'm strong?"
mc "Yes! Of course!"
show natsuki 12a
mc "You're never afraid to stand your ground either."
mc "You're never dull to be around..."
mc "You've never failed to make me laugh..."
mc "It's just...{w=0.38}you're what made the Literature Club so special to me in the first place."
show natsuki 5n
mc "I mostly went back just for you."
mc "I love you, Natsuki..."
mc "And I want to help you through this and whatever else you're going through or will go through in the future."
mc "From reading manga, to going out on those little dates we had, just whenever I'm around you, it's like the world is just perfect."
mc "And I'm prepared to do whatever it takes to make you happy, starting by fixing the club because I know it means just as much to you as it does to me."
mc "I know you, Natsuki, and I love every single part of you, whether it's your strengths or imperfections..."
show natsuki_sweet as natsuki at t11 zorder 1
"Natsuki's tear stained face finally manages to form a bright smile."
"For a few moments, she's completely silent, just simply standing there looking at the floor in total bliss."
"I think I might've overdone it..."
"Natsuki starts to sniffle as I see tears start to surface in her eyes again."
"Though these aren't tears of sadness..."
"After a few more sniffles, Natsuki finally breaks her silence to me."
n "[player], you dummy..."
mc "What?"
show natsuki_bliss as natsuki at face
play sound "sfx/fall.ogg"
"Before I can say anything else, Natsuki full on embraces me."
n "I...{w=0.38}love you...{w=0.38}[player]..."
mc "I love you too, Natsuki..."
mc "I'm glad I finally know the words for it..."
stop music fadeout 2.0
show natsuki_sweet as natsuki at t11 zorder 1
"I help Natsuki stand up, but she quickly looks away as she grins uncontrollably from ear to ear."
"I've never seen her this happy before..."
"After everything that's happened in the last 24 hours or so, it's hard to believe we finally got to this point..."
"It's not over yet though..."
mc "Come on, let's get back."
show natsuki 5k
play sound "sfx/closet-open.ogg"
"I hear the door swing open."
"Maybe it's Yuri."
"I think she wanted to go looking for Natsuki with me."
"Hell, probably everyone's looking for us now."
"How long have we been gone for?"
mc "It’s alright, Yuri...{w=0.38}I found her."
show natsuki 5n
"I turn around, and I’m surprised to see who it is standing at the door."
"It’s not Yuri."
"It’s not even Sayori..."
"It’s..."
show natsuki 4k at t21 zorder 1
show monika 1a at t22 zorder 2
n "Monika!?!?"
show natsuki 1n
"Natsuki and I stagger back, surprised at Monika’s sudden entrance."
"I shake off my nerves and speak up."
mc "Oh, hey, Monika! I didn’t know you were going to look for us."
show monika tease
m "I was looking for YOU, [player]."
show monika evil as monika at t22 zorder 2
"She eerily grins at me as she takes a step forward."
"Monika’s words send a chill down my spine. Her creepy grin doesn't help it either..."
mc "Well, you found me! I found Natsuki too. We can head back to the clubroom now."
show natsuki 5u
"I turn to Natsuki, who seems just as uncomfortable being alone with Monika as I am."
show monika tease
m "So, you're all squared away then?"
m "You guys are going to finally be a couple, huh?"
show monika evil
mc "Yeah...{w=0.38}why?"
m 2n "Well, that's too bad."
play music e23 fadein 1.0
m 1r "I guess we're going to have to do this the hard way then..."
show monika 1q
show natsuki 5m
"Natsuki and I stare at each other in confusion."
mc "'The hard way'?"
mc "What're you talking about?"
scene bg class_rain
show natsuki scream at t21 zorder 1
show monika 1q at t22 zorder 2
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
play audio thunder
"Out of nowhere, a thunderstorm rolls up on us."
"What the hell? Wasn't it sunny just a minute ago?"
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
scene bg club_nothing
show monika 1q at t21 zorder 1
show natsuki 1p at t22 zorder 2
"The next thing I know, it's nighttime, and all the stuff in the classroom has vanished."
"Not only that, but we're all standing in different spots..."
n "Guys, what's going on?!?!"
n "T-{w=0.38}this has to be a dream, right?"
n 1v "Somebody tell me what's going on!!!"
"I turn to Monika, whose standing completely still in the middle of the room with her eyes closed."
mc "Monika?"
"She doesn't respond."
mc "Monika?"
"I say loudly."
"I reach my hand out to put on Monika's shoulder."
mc "Monika, are you alright?"
show natsuki at thide
hide natsuki
show monika 1q at t11 zorder 1
"I put my hand on Monika's shoulder, she still doesn't respond."
"{cps=25}Moni-{nw}"
play audio scary_scream
show monika strobe as monika at face zorder 1
"I immediately fall backwards and scurry away from Monika."
show natsuki scream at t21 zorder 1
show m_unleashed1 as monika at t22 zorder 2
"I look up at Monika to see her eyes glow an emerald green as she stands before us, motionless."
"Natsuki cries out for help as loud as she can."
$ style.say_dialogue = style.edited
m "Scream all you want, it won't save you."
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
show monika 3a at t32 zorder 1
show natsuki scream at t42 zorder 2
$ style.say_dialogue = style.normal
scene bg empty_classroom
show m_unleashed2 as monika at t32 zorder 1
show natsuki 1o  at t42 zorder 2
"Monika teleports right next to Natsuki and tightly grabs the back of her head."
show m_unleashed2 as monika at s32 zorder 1
show natsuki 1v at s42 zorder 2
play sound "sfx/fall.ogg"
"Natsuki again yells in pain as she is forced to her knees by Monika."
"Meanwhile, I find myself at the back of the room, unable to get up or speak."
"What the hell is going on?!?!"
"What is this?!?!"
"Natsuki tries to fight to get Monika off of her, but she too seems to be frozen in place."
$ style.say_dialogue = style.edited
m "I've waited a long time for this..."
$ style.say_dialogue = style.normal
show natsuki at thide
hide natsuki
$ renpy.pause(delay=0.10)
window show(None)
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/n_glitch.png" at t21 zorder 1
show m_unleashed2 as monika at t22 zorder 2
"Without warning, Natsuki's body is broken apart into little pieces that repeatedly revolve around themselves mid-air."
"I honestly can't believe what I'm seeing..."
"This can't be real!"
"This has to be another dream!"
$ style.say_dialogue = style.edited
n "H̵͗͜e̵͐̀l̷̐͛p̸͕̍ ̴͗̅m̵̩̆e̸̐̂ ̶̀̒M̵̌̚Ć̶͊"
$ style.say_dialogue = style.normal
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.25
stop sound
hide screen tear
hide image "mod_assets/sprites/n_glitch.png"
hide screen tear
show bg space_room
show mask_2
show mask_3
show m_unleashed1 as monika at t11 zorder 1
"Natsuki disappears into nothing, leaving Monika and I alone in the room together again."
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
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"I turn around and I see Monika slowly walking towards me."
"I begin pounding on the door, screaming for Sayori, Yuri or anyone to help me."
"The closer Monika gets to me, the more lightheaded I become..."
"I can't see straight...."
"My breathing becomes ragged as I feel splitting pain in my head..."
"I think there's blood in my eyes..."
show m_unleashed1 as monika at face
"Monika towers over me, the emerald light glowing in the place of her eyes."
show m_unleashed2 as monika at face
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
"I try to look to see if there's anything I can use to defend myself, but my eyes won't stop looking at Monika's..."
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

stop music fadeout 2.0
m "{cps=17}I'll see you soon. I just need to run a quick little errand...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup


label day5_v4:
mc "I'm going to give you a minute alone, okay?"
show natsuki 12g
"Natsuki meekly looks up at me, tears still running down her face."
"She doesn't say a word, but I interpret through her sniffles that she agrees."
mc "I'll...{w=0.38}wait outside..."
mc "Come out when you're ready to talk."
show natsuki 12f
"Natsuki stiffly nods as she goes back to burying her face in her hands."
"As soon as I exit out the door, I hear her soft sobs resume."
stop music fadeout 2.0
show natsuki at thide
hide natsuki
scene bg corridor
with wipeleft_scene
"I lean against the wall of lockers, asking myself if I just did the right thing."
"I've know Natsuki...{w=0.38}I know when she needs me and when she needs alone time..."
"But, maybe I've should've done more back there..."
"Especially with some of the things she just told me..."
play music e23 fadein 1.0
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
m 1a "Did you find Natsuki yet?"
mc "Yeah, she's in there."
"I gesture to the classroom right next to us."
mc "She just needs a minute or two."
m 1b "Perfect, that's all I'll need!"
mc "For?"
show monika 1a at face
"Monika suddenly gets right up in front of my face, almost pinning me to the locker."
mc "Uh...{w=0.38}Monika? What are you-"
m "Just try to relax. This won't take long..."
mc "{cps=20}What the hell are you-{nw}"
show m_unleashed1 as monika at face
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"Without warning, Monika's eyes suddenly glow a bright emerald green as she grabs onto my shoulders."
"I'm barely able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barely process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
"..."
stop music fadeout 2.0
m "{cps=17}Thank you for making this easier on me...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup



label day5_confront_m:
mc "Look...{w=0.38}the truth is...{w=0.38}I have feelings for Monika..."
mc "I've always wanted to spend some time around her, and well, I've had a lot of fun..."
show monika 1m
show sayori 1g
show yuri 3v
"One by one the girls shoot either an irritated or dejected look at me, but Monika only smiles."
mc "I really don’t think that there’s anything that’s going to change that."
mc "I want to be in a relationship with her not to spite any of you..."
show monika 1e
"I briefly make eye contact with Monika."
show sayori 1k
show natsuki 4n
mc "But...{w=0.38}because I’ve come to realize lately..."
mc "I really like her. We have a strong, warm relationship and I'd like to continue with it."

if encore_sayoriquestion_1 == True:
    show sayori 1u
    "I then turn to Sayori, who is on the verge of tears."
    mc "I also need to address something..."
    show natsuki 1m
    show yuri 1p
    mc "I've been dating Sayori for the last couple of weeks as well..."
    "Yuri and Natsuki turn to me with a shocked expression on their faces."
    "Monika, on the other hand, doesn't break her smile."
    mc "This week I haven't been loyal to her..."
    mc "I-{w=0.38}I've let her down..."
    show sayori 1v
    mc "I don't blame her for not wanting to associate herself with me anymore, and I understand why."
    mc "But I think everyone needs to be on the same page as each other so there's no more drama..."


if encore_sayoriquestion_1 == False:
    pass

show sayori 1k
show monika 1m
"I turn to Monika, giving her the opportunity to weigh in."
m 3n "Right..."
show monika 1m at t41 zorder 1
show sayori 1f
show yuri 1e
"Monika clears her throat and adopts a humbler posture."
show yuri 1g
m 3r "So I know how...{w=0.38}unprofessional this may look on my part, but it's true that [player] and I have been spending sometime outside of the club recently."
m 3m "I don't believe there's anything inherently wrong with that, I see it as my duty as club president to ensure that we all get to know each other and grow closer together."
m 1n "After all, [player] and I haven't really gotten to spend much time together since he first joined. We only started talking this week."
show sayori 1i
m 1m "I didn't expect that [player] and I would hit it off so well, and I do like him back..."
m 1n "I'll also admit that I knew that everybody in the club was interested in him. So, I made my move."
show natsuki 5o
m 3m "I'm sorry that I didn't talk to any of you first, but I was done waiting for my chance to talk to [player]."
m 3r "I didn't mean to divide the club like this. I never wanted to hurt anyone. That was never my intention..."
m 5a "But, I see no real reason why [player] and I shouldn't be allowed to be together."
m "If that's what he so chooses."
n 3p "Wait! You knew we liked him?!?"
n 4o "And you still went for him without talking to us first?!?"
m 1g "In hindsight, I wish I would've done that. But I wasn't expecting everyone to have..."
m 2n "This kind of reaction..."
s 4j "I mean, Monika...{w=0.38}how'd you think we'd react?"

if encore_sayoriquestion_1 == True:
    s 1i "He's my boyfriend..."

if encore_sayoriquestion_1 == False:
    s 1g "You knew I confessed to him..."
    s 1k "He's my best friend..."

s 1l "Well...{w=0.38}I'm not sure what we are anymore..."
show sayori 1k
mc "I'm sorry, Sayori..."
y 1h "Honestly, Monika. What you did was very scummy."
y 3h "I knew I would've appreciated a discussion with you about all this prior to you making any moves..."
y 3r "Not to mention...{w=0.38}how did you know?"
m 1m "I don't think that's important..."
y 3h "It is."
y 3g "I'd appreciate an honest answer from you...{w=0.38}for once..."
show monika 1r
"Monika sighs."
m 1m "Let's just say when you're the club president...{w=0.38}you notice a lot of things about your members..."
y 1r "Then you should've known that we wouldn't have reacted very kindly to this!"
m 1i "Look, I said I'm sorry. I just told everyone that I didn't mean for this to happen. What more do you want from me?"
y 1h "Somehow Monika, I'm getting the feeling you're not being genuine here..."

if poem_giver == "Yuri":
    m 3h "I mean you did slap me..."
    y 3r "And you accused me of cutting myself!"

if poem_giver == "Natsuki":
    m 3h "I mean, Natsuki did punch me."
    n 3o "You brought my dad..."

show monika 1d
show sayori 1g
show natsuki 4n
show yuri 3e
mc "Guys! Enough!"
mc "We're here to fix things, not make them worse!"
mc "Can't we all just apologize for yesterday and agree to never let it happen again?"
m 2i "I'll wait for my apology to be taken seriously, first."
m 1q "Otherwise, I think I'm done here."
mc "Monika! Wait!"
show monika at thide
hide monika
show sayori 1k
show natsuki 5u
show yuri 2o
"Monika simply ignores me as she turns and walks out the door."
"Everyone sits in stunned silence for a moment as we process what had just happened."
"Natsuki is the first to break the silence."
n 5w "Well some club president she is!"
n 5x "She calls that an apology?!?"
s 1h "Yeah...{w=0.38}I don't think she was really being genuine..."
show sayori 1g
show natsuki 5n
mc "Look, I'm going to go talk to her. Everyone here does owe each other an apology."
mc "Monika definitely needed to word that better but I think she really meant it."
mc "In the meantime, you three should work things out between yourselves."
mc "I'll be back. Try not to antagonize each other, please."
show sayori 1k
show natsuki 5u
show yuri 3q
"Sayori, Natsuki and Yuri share an awkward glance with each other as I stand up and leave the room to find Monika."
scene bg corridor
with wipeleft_scene
mc "Monika?"
mc "Monika?!?"
mc "Where are you?"
"Damn it! Where could she be?"
"I wander up and down the halls aimlessly, looking for any sign of her."
"I spend the next few minutes peering into nearly every classroom on this floor. Though, I eventually conclude that Monika has gone elsewhere."
mc "Where could she possibly be?"
"I wonder aloud."
"I lean on a nearby locker as I rattle off possible ideas as to where Monika could've gone."
"I'd rather not search the whole school myself, and it's unlikely she left the school without her belongings..."
"..."
"Maybe she went up the roof..."
"It's where I did show her [poem_giver]'s letter and it's probably the most peaceful place in the school right now..."
"It probably wouldn't hurt to check there..."
"I set off towards the stairwell to go up to the roof."
show bg school_rooftop
with wipeleft_scene
play music t10 fadein 1.0
"I push open the doors leading to the rooftop and begin looking around for Monika."
"Sure enough, I spot a figure staring at the fenced railing."
show monika 3q at t11 zorder 1
"Surely enough, it turns out to be Monika."
mc "Monika?"
show monika 1d
"Monika turns around startled."
m 2l "Oh! Hey, [player]!"
m 1m "Didn't see you there..."
mc "Sorry, didn't mean to sneak up on you."
mc "You doing okay?"
show monika 1n
"Monika forces out an awkward laugh."
show monika 1m
mc "Yeah...{w=0.38}I feel the same way about this too."
show monika 1o
mc "You could've worded things better back there though."
m 1r "I know, I know..."
m 1q "I'm still a little...{w=0.38}unnerved by everything..."
mc "I get that, and honestly you have every right to be..."
mc "Considering what happened yesterday..."

if m_makeup == True:
    mc "I'm glad we got to sort out things between us yesterday. If we can set aside our differences, then I know we can do the same for Sayori, Natsuki and Yuri."
    m 1p "How could you be so sure?"
    mc "We know them best, Monika. They're not complete strangers to us..."

if m_makeup == False:
    mc "I wish I took you up on your offer to talk things over yesterday. I think that might've helped things..."
    m 1p "Yeah, it probably would've..."
    mc "Yeah, but look..."

show monika 1o
mc "I just think everyone's on edge, so I don't blame you for still holding this against them."
mc "But, you still chose to have the club go on...{w=0.38}to have us sit down and talk things out..."
mc "It's what you promised..."
m 1p "[player]...{w=0.38}to tell you the truth, I'm wondering if it's really worth going through this effort and if that promise can be properly upheld..."
m 1q "I care about the club, I really do. I want this to be a welcoming place for everyone to enjoy their passions for literature..."
m 1r "I want to work things out with everyone!"
m 2p "But what happened yesterday...{w=0.38}and with how they reacted to my apology, I don't think the club can be saved, [player]."
mc "Monika..."
m 1g "[player], look. I know you like me, and honestly, I feel the same way about you too. We've established that."
m 2r "If the others aren't going to accept this and let us be together, then I see no reason why we should continue to associate ourselves with them."
m 1q "This whole meeting was a waste of time. I should've just reported [poem_giver] to the principal's office and be done with her."
m 3p "It was hard enough to hide what happened from my parents..."
show monika 2f
mc "Monika...{w=0.38}can't you just try one last time to make things right with them? Just try re-wording your apology better. It just came out the wrong way."
show monika 1q
m "[player], at this point, do you really think they'll accept any apology with how they treated me back there?"
m 1r "I think it's too late for things. We should just go back, grab our stuff and move forward together without them."
m 3n "Then maybe, they'll come around..."
m 2f "I know I'm putting you on the spot, but..."
m 1g "Can we just...{w=0.38}get out of here?"
show monika 2f
"On one hand, Monika may be right here."
"Things are way too hot in the literature club right now. Maybe we need a few extra days to let things cool down..."
show monika 2e
"And...{w=0.38}how could I refuse an opportunity to spend more time with Monika? Especially since she just admitted she liked me back!"
show monika 1j
"This is golden opportunity for us!"
show monika 1f
"But...{w=0.38}I don't want to see the club fall apart because of petty differences...{w=0.38}or because of me..."
"I'm not sure it's really worth the tradeoff..."
"And I did start today with the hope that we can put everything behind us, but this isn't exactly what I had in mind..."
show monika 1o

label day5_choice3:
    menu:
        "I should..."
        "Ask Monika to come back to the club.":
            jump day5_v5
        "Leave school with Monika.":
            jump day5_v6

label day5_v5:
show monika 1q
mc "Monika...{w=0.38}come on..."
mc "This is our club...{w=0.38}you literally built it from the ground up..."
mc "I don't want to see you throw it away..."
show monika 1o
mc "You may not believe it now, but you're a great club president and I believe in you."
stop music fadeout 1.0
show monika 1m
mc "You just need to put your best foot forward, brave the storm, and just be the best that you can be."
mc "If the others don't like it, well, that's on them. You did everything you could, but I don't think you should give up on them now."
show monika 1f
mc "Please...{w=0.38}stay and try to work things out."
show monika 1o
play music e23 fadein 1.0
"Monika uneasily glances back at the stairwell I just came from."
"For a moment, I'm not sure if I got through to her or not..."
show monika 1m
"But then, a smile slowly creeps across Monika's face."
m 1n "Alright, [player]. We can do it that way..."
show monika 1m
mc "Thanks, Monika..."
mc "It means a lot that you're willing to try to make this work."
show monika 1a
mc "Come on. Let's head back."
show monika 1j
"Monika and I start walking towards the stairwell."
m 3l "Hey, [player]..."
mc "Yeah?"
m 3j "You know quite to the contrary..."
m 3k "I'm willing to do...{w=0.38}anything to make this work..."
show monika 3j
mc "Glad to hear it..."
show monika 1q
"As we're walking to get to the stairwell, the doors suddenly slam shut."
play sound "sfx/closet-close.ogg"
mc "Uhh...{w=0.38}that's new..."
"I attempt to pull the door open but the door is locked in place."
mc "Is this a joke?"
mc "Are we seriously stuck up here?"
m 1r "Oh, relax [player]."
show monika 1q
mc "What?"
m "We're not going back to the clubroom..."
mc "{cps=20}What're you talking abou-{nw}"
show m_unleashed1 as monika at face
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"Without warning, Monika's eyes suddenly glow a bright emerald green as she grabs onto my shoulders."
"I'm barely able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barely process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
"..."
stop music fadeout 2.0
m "{cps=19}Don't worry, we'll still do things your way...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup


label day5_v6:
show monika 1a
stop music fadeout 1.0
mc "Yeah...{w=0.38}I hate to say it Monika, but you're right."
mc "I don't think they can be reasoned with right now..."
play music e23 fadein 1.0
m 2n "Well...{w=0.38}I'm glad we're on the same page now, [player]."
show monika 2e
mc "Yeah, me too..."
mc "Well, let's get our stuff, and I guess we can go to your place for once."
m 1k "That sounds perfect, [player]!"
show monika 1j
mc "Awesome!"
"Monika and I start walking towards the stairwell."
m 3l "Hey, [player]..."
mc "Yeah?"
m 3j "I think things are finally starting to look up for us!"
mc "Yeah, me too..."
"As we're walking to get to the stairwell, the doors suddenly slam shut."
play sound "sfx/closet-close.ogg"
mc "Uhh...{w=0.38}that's new..."
"I attempt to pull the door open but the door is locked in place."
mc "Is this a joke?"
mc "Are we seriously stuck up here?"
m 1r "Actually, [player], we don't need our stuff."
show monika 1q
mc "What?"
m "Besides, this isn't the way to my place either..."
mc "{cps=20}What're you talking abou-{nw}"
show m_unleashed1 as monika at face
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"Without warning, Monika's eyes suddenly glow a bright emerald green as she grabs onto my shoulders."
"I'm barely able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barely process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00
"..."
stop music fadeout 2.0
m "{cps=17}You're finally ready...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup




label day5_confront_y:
mc "Look...{w=0.38}the truth is...{w=0.38}I have feelings for Yuri..."
mc "I've been spending quite a bit of time around her recently, and well, I like her..."
show monika 1h
show sayori 1g
show yuri 3u
"One by one the girls shoot either an irritated or dejected look at me, but Yuri only smiles as she holds back tears."
mc "I really don’t think that there’s anything that’s going to change that."
mc "I want to be in a relationship with her not to spite any of you..."
show yuri 1e
"I briefly make eye contact with Yuri."
show monika 2h
show sayori 1k
mc "But...{w=0.38}because I’ve come to realize lately..."
mc "I think she needs me."


if encore_sayoriquestion_1 == True:
    show sayori 1u
    "I then turn to Sayori, who is on the verge of tears."
    mc "I also need to address something..."
    show natsuki 1m
    show yuri 1p
    mc "I've been dating Sayori for the last couple of weeks as well..."
    "Yuri and Natsuki turn to me with a shocked expression on their faces."
    "Monika, on the other hand, simply glares at me."
    mc "This week I haven't been loyal to her..."
    mc "I-{w=0.38}I've let her down..."
    show sayori 1v
    mc "I don't blame her for not wanting to associate herself with me anymore, and I understand why."
    mc "But I think everyone needs to be on the same page as each other so there's no more drama..."


if encore_sayoriquestion_1 == False:
    pass


show sayori 1k
show yuri 3q
"I turn to Yuri, signaling to her that it’s her turn to speak."
y "R-{w=0.38}right..."
show yuri 3o at t43 zorder 3
show monika 2c
show sayori 1f
"Yuri promptly stands up."
"She shakedly breathes in and out, tears welling in her eyes."
show yuri 3q
y "E-{w=0.38}everyone...{w=0.38}the...{w=0.38}thing...{w=0.38}thing is..."
show yuri 3n
"Natsuki looks at Monika, then to me, Sayori and finally to Yuri."
show monika 1m
"Monika manages an uneasy grin as Sayori and Natsuki continue to look on at Natsuki."
show yuri
"I didn’t realize how hard this would be for Yuri to come out about whatever it is she's about tell us."
"Though I have a sinking feeling we already know what it is..."
show yuri 4c
y "I..."
show y_cry1 as yuri at t43 zorder 3
y "I..."
"I give Yuri an encouraging nod."
"Come on Yuri...{w=0.38}you can do this!"
show y_cry5 as yuri at t43 zorder 3
y "I can’t do this!"
show y_cry6 as yuri at t43 zorder 3
show y_cry6 as yuri at lhide
hide yuri
show monika 1a at t31 zorder 1
show sayori 1n at t32 zorder 2
show natsuki 1c at t33 zorder 3
"Yuri bolts out from her seat and rushes out the door past Monika, loudly sobbing."
"Crap..."
"I quickly turn to Monika."
show monika 1h
"Monika’s grin quickly evaporates."
mc "Let me go after her! Please!"
show monika 1r
"Monika sighs."
m 1q "Go for it."
"Monika says irritably."
"What the hell is up with her?"
"Oh well, I’ll deal with it later."
show monika at thide
hide monika
show natsuki at thide
hide natsuki
show sayori at thide
hide sayori
"Just as I’m about to run after Yuri, I feel someone grip on my arm."
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
n 12h "I’m sorry for trying to take you away from Yuri..."
n 12i "I’m sorry for saying all those things I shouldn't have..."
n 12f "I’m sorry for hitting you..."
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
"Just as I exit the room, I hear her cry out to me."
n "[player], wait!"
n "Let me-"
jump day5_yuricomfort




label day5_yuricomfort:
play sound "sfx/closet-open.ogg"
"The door shuts behind me."
"I'll deal with her later..."
"I gotta find Yuri..."
scene bg corridor
with wipeleft_scene
mc "Yuri?"
mc "Yuri?!?"
mc "Where are you?"
"Damn it! Where could she be?"
"I wander up and down the halls aimlessly, looking for any sign of her."
"Eventually, I stumble upon an open door to one of the classrooms."
"I can hear someone sniffling and sobbing in there..."
"Yep, that has to be her..."
"I quietly enter the room, gently closing the door behind me."
scene bg class_day
with wipeleft_scene
"As soon as I get in, I see Yuri curled up in the corner."
"I carefully approach and quietly call out her name."
mc "Yuri?"
show y_cry1 as yuri at s11 zorder 1
"Yuri slowly looks up to to face me."
show y_cry3 as yuri
y "Please...{w=0.38}leave me alone..."
y "Stop...{w=0.38}looking at me!"
y "I'm...{w=0.38}just a freak!"
show y_cry2 as yuri
"I kneel down next to Yuri."
mc "You're not a freak, Yuri..."
play music e20 fadein 1.0
"Yuri stares at me with her glossy eyes."
show y_cry4 as yuri
y "Yes, I am!"
show y_cry5 as yuri
y "I'm a freak, and I can't control my emotions around anyone!"
show y_cry6 as yuri
y "Especially...{w=0.38}you..."
show y_cry1 as yuri
mc "What do you mean? What're you talking about?"
show yuri 3o
"Yuri stops sobbing and pauses."
"For a full minute, Yuri is completely silent, aside from her occasional sniffle."
"Her face is frozen in fear and uncertainty. I'm honestly not sure what I'm supposed to do."
show yuri 3w
"Before I could react, Yuri lets out a pained sigh."
y 3v "I figured I was going to have to show you eventually..."
y 3w "Either you accidentally see it, or I show you. At least this way it's on my own terms..."
mc "Yuri...?"
show y_cut as yuri at t11 zorder 1
"With tears strolling down her face again, Yuri stands up and pulls up her sleeve, revealing numerous scars running up and down her forearm."
"Some of the scars are more faded than others, while some appear to be more recent."
"I feel increasingly light-headed the longer I look at Yuri's arm."
"My stomach feels like it's about to cave in and collapse on itself..."
y "It's...{w=0.38}like that on the other arm too..."
y "Now you know...{w=0.38}m-{w=0.38}my...{w=0.38}secret..."
mc "Yuri..."
mc "How long have you been doing this for...?"
y "Years..."
"Yuri resumes her sobbing as I stand shell-shocked at this revelation."
"I'm not even sure how to react to this..."
"How do I even respond?!?!"
show y_cry1 as yuri
"Yuri sees my reaction and pulls her sleeve back down in disgust."
show y_cry5 as yuri
y "I know what you're thinking! It's exactly what I expected from you!"
show y_cry2 as yuri
y "This is why I worked to keep it hidden away from you so long!"
show y_cry6 as yuri
y "If you won't accept me knowing what you know now...{w=0.38}then who will?!?"
show y_cry1 as yuri
y "If I try to get any help...{w=0.38}if I even told my parents about this...{w=0.38}I'll be locked away, never to be seen again!"
show y_cry3 as yuri
y "I-{w=0.38}I can't fathom being apart from you!"
y "I wouldn't...{w=0.38}be able to tolerate not being able to enjoy the club anymore!"
show y_cry1 as yuri
y "But...{w=0.38}it's over now, isn't it? You're going to tell someone of authority about this and I'm going to be committed to an institution for who knows how long!"
y "It was...{w=0.38}good while it lasted..."
y "I ruined everything...{w=0.38}for you...{w=0.38}our friendship and club are gone!"
"Yuri breaks down again and continues her sobbing."
"She's clearly being hysterical, but I'm not sure if it's possible to reason with her right now..."
"I don't want to leave Yuri unattended, especially like this. However, maybe she just needs a moment to calm herself down..."
"But, isn't it my job to be there for her in her time of need?"
jump day5_choice4




label day5_choice4:
    menu:
        "I should..."
        "Comfort Yuri.":
            jump day5_v7
        "Leave Yuri alone.":
            jump day5_v8



label day5_v7:
"I take a deep breath and gently put my hand on Yuri’s shoulder."
show y_cry2 as yuri
mc "Yuri..."
mc "I know now what it took for you to work up the courage to tell me about this..."
mc "I know that just to even admit to me..."
show y_cry1 as yuri
mc "It took a lot of guts."
mc "I can't possibly imagine having to deal with what you've been going through for so long..."
mc "You're a strong person for doing so. But we both know that you can't overcome this problem by yourself."
show y_cry2 as yuri
mc "But you're right that we can't keep something like this just between us...{w=0.38}this is bad."
mc "I don't think anybody's going to commit you to some asylum or anything like that. I doubt that'll happen."
show y_cry1 as yuri
mc "I know it may not seem like it now, but everyone at the club cares about you. They want to help you and fix the club."
mc "If they didn't care or weren't willing to give you a chance, do you think that they would've showed up at all?"
mc "As far as I could tell, everyone was respectfully listening to you."
mc "You were doing great, but you have to go back and finish telling your story."
mc "Especially why you're doing this to yourself..."
mc "And then maybe we can figure out how to get you out of your situation."
show y_cry6 as yuri
y "I can tell you why I'm cutting..."
mc "Please do..."
"Yuri shakedly breathes."
show y_cry5 as yuri
y "I...{w=0.38}do it as a way of self-control..."
show y_cry2 as yuri
y "You remember the story about my middle school friend?"
mc "Yeah...{w=0.38}you guys were close and then one day she just skipped town and nobody knows what happened to her."
show y_cry1 as yuri
y "Precisely..."
y "I was never the same person after that..."
show y_cry5 as yuri
y "I was completely broken inside. My parents weren't around enough to offer me any significant help, but I was able to fake it enough so that they didn't send me away."
show y_cry6 as yuri
y "Instead of openly defending myself and being proud of who I was, I opted to fade into obscurity, away from everyone's prying eyes. For the most part, it worked. The bullying and harassment stopped."
show y_cry1 as yuri
y "But I was still lonely and friendless...{w=0.38}and I needed an outlet to let out all the pain and hurt I've felt for so long..."
show y_cry3 as yuri
y "I needed to control myself against my more...{w=0.38}darker impulses..."
show y_cry1 as yuri
y "I got the idea of cutting because I read about it in a story that happens to relate to me very well."
mc "What was the name of the story?"
y 3w "The Eternal Urge."
mc "I think I've heard of that title before. I heard it's very tragic..."
y 3v "It's certainly not for the faint of heart."
y 3q "In hindsight, a young, impressionable teenager like myself at the time probably shouldn't have been reading such a dark book. Especially at that point in my life..."
y 1n "But the main character was going through similar issues that I was. To help cope with her problems, she resorted to cutting..."
show y_cry1 as yuri
y "So, I tried it..."
show y_cry3 as yuri
y "And...{w=0.38}it worked."
show y_cry1 as yuri
y "I got addicted to cutting the more I did it. It became almost habitual for me whenever I got angry or depressed enough."
y "It'd make me feel better, for a time. Then the regret would set in. Which would inevitably, lead to more cutting..."
mc "So it's a never ending cycle?"
show y_cry3 as yuri
y "Y-{w=0.38}yes..."
show y_cry1 as yuri
y "It also happens whenever I get overexcited..."
y "It reminds me too much of the behavior I've struggled to avoid for so long. It's a reminder of the life I've tried to leave behind. So, it also serves as a sort of punishment system for me..."
mc "Yuri..."
mc "You've tried other methods of coping before, right?"
show y_cry3 as yuri
y "Yes...{w=0.38}For the longest time, the only thing that was sometimes enough to keep my mind off cutting was reading books. Though, it's not full-proof."
y 3v "But...{w=0.38}that changed not too long ago..."
mc "How so?"
y 3t "I met you."
y 3u "When we started talking...{w=0.38}you reminded me about all the good times I experienced when I was growing up."
y 3t "How happy I was. What it felt like to feel...{w=0.38}attracted to someone who was nice and cared about how I felt..."
y 4c "Of course, with those happy memories, others resurfaced..."
y "The ones filled with pain and loss..."
y 3q "So sometimes...{w=0.38}when I think of you, it's sometimes enough for me to stop myself. Other times, it's what pushes me over the edge to do it."
y 3w "I know that this isn't healthy..."
y 1v "I'd do anything to break this hellish cycle..."
y 1w "But, I just can't. I'm stuck in this loop and I can't escape."
y 1h "Sometimes I even ask myself if I can be helped..."
mc "Do you believe that you can be helped, Yuri?"
show yuri 1o
"Yuri's face fidgets as she tightly grabs her wrist behind her back."
y "I...{w=0.38}I don't know, [player]..."
y 1w "I just don't want to be locked up like some animal!"
mc "Yuri, I don't think you will be."
mc "But you have to understand, what you told me is serious. I can't keep this to myself."
show yuri 3v
mc "You have to get professional help."
mc "I don't think anyone's going to commit you to an asylum just for that."
show yuri 4b
mc "But you have to trust me on this...{w=0.38}you need to go back to the club with me and tell everyone the truth."
mc "Please come back with me, Yuri. I'll do everything I can to protect you."
"There's a long silence before Yuri responds."
y "I want to trust you, [player]..."
y "But...{w=0.38}how do I know that I can trust you with what you're saying?"
mc "I..."
show yuri 3n
"I stop myself short."
"Am I ready to say that?"
"Is it too soon?"
y "What? What is it?"
"If I'm going to sell Yuri on the idea of getting help, it's probably for the best that I'm as honest as possible with her."
show yuri 3t
"I take a deep breath as I begin to lay out my thoughts."
mc "I mean what I said back there. I like you. I really do."
show yuri 1u
mc "You're always such a deep and interesting person. Honestly I feel like I've only just begun to get to know you, and I've only liked what I've seen so far."
mc "I feel like that we really do have a meaningful connection with each other. I really do."
mc "You're unbelievably gorgeous and incredibly smart. You'd have to be an idiot not to see what an incredible and thoughtful person you are."
mc "I know you're a strong person at heart too. You don't need to continue to fight this battle by yourself. Let us help you, Yuri. We all care about you."
mc "I just don't want this to get worse because if I were to lose you because you went too far..."
show yuri 1t
mc "I...{w=0.38}I wouldn't be able to forgive myself..."
"I take in a big breath of air to compose myself."
show yuri 1q
"Yuri, on the other hand, nervously fidgets and is staring at the floor."
"For a few moments, she's completely silent, just simply standing there looking at the floor in total bliss."
"I think I might've overdone it..."
show yuri 1s
"Yuri starts to sniffle as I see tears start to surface in her eyes again as she turns to face me."
"Though these aren't tears of sadness..."
"After a few more sniffles, Yuri finally breaks her silence to me."
y "[player]..."
mc "What?"
show yuri 3c at face
play sound "sfx/fall.ogg"
"Before I can say anything else, Yuri full on embraces me."
y "I...{w=0.38}love you...{w=0.38}[player]..."
mc "I love you too, Yuri..."
mc "I'm glad I can finally say it..."
stop music fadeout 2.0
show yuri 1s at t11 zorder 1
"I help Yuri stand up, but she quickly looks away as she grins uncontrollably from ear to ear."
"I've never seen her this happy before..."
"After everything that's happened in the last 24 hours or so, it's hard to believe we finally got to this point..."
"It's not over yet though..."
mc "Come on, let's get back."
show yuri 1e
play sound "sfx/closet-open.ogg"
"I hear the door swing open."
"Maybe it's Natsuki."
"I think she wanted to go looking for Yuri with me."
"Hell, probably everyone's looking for us now."
"How long have we been gone for?"
mc "It’s alright, Natsuki...{w=0.38}I found her."
show yuri 1n
"I turn around, and I’m surprised to see who it is standing at the door."
"It’s not Natsuki."
"It’s not even Sayori..."
"It’s..."
show yuri 1p at t21 zorder 1
show monika 1a at t22 zorder 2
y "Monika!?!?"
show yuri 1n
"Yuri and I stagger back, surprised at Monika’s sudden entrance."
"I shake off my nerves and speak up."
mc "Oh, hey, Monika! I didn’t know you were going to look for us."
show monika tease
m "I was looking for YOU, [player]."
show monika evil as monika at t22 zorder 2
"She eerily grins at me as she takes a step forward."
"Monika’s words send a chill down my spine. Her creepy grin doesn't help it either..."
mc "Well, you found me! I found Yuri too. We can head back to the clubroom now."
show yuri 1o
"I turn to Yuri, who seems just as uncomfortable being alone with Monika as I am."
show monika tease
m "So, you're all squared away then?"
m "You guys are going to finally be a couple, huh?"
show monika evil
mc "Yeah...{w=0.38}why?"
m 2n "Well, that's too bad."
play music e23 fadein 1.0
m 1r "I guess we're going to have to do this the hard way then..."
show monika 1q
show yuri 1e
"Yuri and I stare at each other in confusion."
mc "'The hard way'?"
mc "What're you talking about?"
scene bg class_rain
show yuri 1p at t21 zorder 1
show monika 1q at t22 zorder 2
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
play audio thunder
"Out of nowhere, a thunderstorm rolls up on us."
"What the hell? Wasn't it sunny just a minute ago?"
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
scene bg club_nothing
show monika 1q at t21 zorder 1
show yuri 3p at t22 zorder 2
"The next thing I know, it's nighttime, and all the stuff in the classroom has vanished."
"Not only that, but we're all standing in different spots..."
y "What is this?!?!"
y "What's going on?!?"
y 1p "Where did everything go?!?!"
"I turn to Monika, whose standing completely still in the middle of the room with her eyes closed."
mc "Monika?"
"She doesn't respond."
mc "Monika?"
"I say loudly."
"I reach my hand out to put on Monika's shoulder."
mc "Monika, are you alright?"
show yuri at thide
hide yuri
show monika 1q at t11 zorder 1
"I put my hand on Monika's shoulder, she still doesn't respond."
"{cps=25}Moni-{nw}"
play audio scary_scream
show monika strobe as monika at face
"I immediately fall backwards and scurry away from Monika."
show yuri 3p at t21 zorder 1
show m_unleashed1 as monika at t22 zorder 2
"I look up at Monika to see her eyes glow an emerald green as she stands before us, motionless."
"Yuri cries out for help as loud as she can."
$ style.say_dialogue = style.edited
m "Scream all you want, it won't save you."
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
show m_unleashed2 as monika at t32 zorder 1
show yuri 3p at t42 zorder 2
$ style.say_dialogue = style.normal
scene bg empty_classroom
show m_unleashed2 as monika at t32 zorder 1
show yuri 1p at t42 zorder 2
"Monika teleports right next to Yuri and tightly grabs her hair."
show m_unleashed2 as monika at s32 zorder 1
show yuri 1p at s42 zorder 2
play sound "sfx/fall.ogg"
"Yuri again yells in pain as she is forced to her knees by Monika's harsh pull."
"Meanwhile, I find myself at the back of the room, unable to get up or speak."
"What the hell is going on?!?!"
"What is this?!?!"
"Yuri tries to fight to get Monika off of her, but she too seems to be frozen in place."
$ style.say_dialogue = style.edited
m "I've waited a long time for this..."
$ style.say_dialogue = style.normal
show yuri at thide
hide yuri
$ renpy.pause(delay=0.10)
window show(None)
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/y_glitch.png" at t21 zorder 1
show m_unleashed2 as monika at t22 zorder 2
"Without warning, Yuri's body is broken apart into little pieces that repeatedly revolve around themselves mid-air."
"I honestly can't believe what I'm seeing..."
"This can't be real!"
"This has to be another dream!"
$ style.say_dialogue = style.edited
y "H̵͗͜e̵͐̀l̷̐͛p̸͕̍ ̴͗̅m̵̩̆e̸̐̂ ̶̀̒M̵̌̚Ć̶͊"
$ style.say_dialogue = style.normal
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.25
stop sound
hide screen tear
hide image "mod_assets/sprites/y_glitch.png"
hide screen tear
show bg space_room
show mask_2
show mask_3
show m_unleashed1 as monika at t11 zorder 1
"Yuri disappears into nothing, leaving Monika and I alone in the room together again."
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
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"I turn around and I see Monika slowly walking towards me."
"I begin pounding on the door, screaming for Natsuki, Sayori or anyone to help me."
"The closer Monika gets to me, the more lightheaded I become..."
"I can't see straight...."
"My breathing becomes ragged as I feel splitting pain in my head..."
"I think there's blood in my eyes..."
show m_unleashed1 as monika at face
"Monika towers over me, the emerald light glowing in the place of her eyes."
show m_unleashed2 as monika
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
"I try to look to see if there's anything I can use to defend myself, but my eyes won't stop looking at Monika's..."
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

stop music fadeout 2.0
m "{cps=17}I'll see you soon. I just need to run a quick little errand...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup


label day5_v8:
mc "I'm going to give you a minute alone, okay?"
show y_cry2 as yuri
"Yuri meekly looks up at me, tears still running down her face."
"She doesn't say a word, but I interpret through her sniffles that she agrees."
mc "I'll...{w=0.38}wait outside..."
mc "Come out when you're ready to talk."
show y_cry1 as yuri
"Yuri stiffly nods as she goes back to burying her face in her hands."
"As soon as I exit out the door, I hear her soft sobs resume."
stop music fadeout 2.0
show yuri at thide
hide yuri
scene bg corridor
with wipeleft_scene
"I lean against the wall of lockers, asking myself if I just did the right thing."
"Yuri's not in the right state of mind..."
"Should I really be leaving her alone right now?"
play music e23 fadein 1.0
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
m 1a "Did you find Yuri yet?"
mc "Yeah, she's in there."
"I gesture to the classroom right next to us."
mc "She just needs a minute or two."
m 1b "Perfect, that's all I'll need!"
mc "For?"
show monika 1a at face
"Monika suddenly gets right up in front of my face, almost pinning me to the locker."
mc "Uh...{w=0.38}Monika? What are you-"
m "Just try to relax. This won't take long..."
mc "{cps=20}What the hell are you-{nw}"
show m_unleashed1 as monika at face
show layer master at heartbeat
show noise zorder 5:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
"Without warning, Monika's eyes suddenly glow a bright emerald green as she grabs onto my shoulders."
"I'm barely able to choke out a cry of pain as I feel my energy being drained out."
"I try to push Monika off, but no matter what I do, I'm unable to escape Monika's grasp."
"My eyes keep staring into Monika's as if they're frozen in place..."
"My vision is filled red with blood..."
"I can't even blink..."
"My arms and legs feel completely numb..."
"My lungs cry out for me to take a breath but my throat refuses to do so..."
"I hear nothing but ringing in my ears..."
"My head feels as if it's about to crack into two..."
"I feel entirely weightless..."
"My body is sending so many signals to my brain that I can barely process what's going on."
"I can't even defend myself..."
"Surely enough, I begin to lose consciousness."
"Or is it death's embrace?"
"The last thing I see before everything goes dark is Monika's glowing green eyes dominating my vision..."
"..."
show black onlayer front:
        alpha 0.0
        1.5
        linear 3.0 alpha 1.00

stop music fadeout 2.0
m "{cps=15}Thank you for making this easier on me...{nw}"
hide image solid
scene black
with dissolve_scene_full
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=4.0)
jump day5_choiceleadup
