#############
#   DAY 4   #
#############
label day4_start:
    scene bg bedroom_dawn
    with open_eyes
    $ day = 4
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    "I slowly open my eyes."
    "Fortunately, I find myself back in my bed in the same bedroom I've had all along."
    "However, I still feel unnerved from the whole experience..."
    "My heart is racing at a million miles an hour, warm sweat is crawling down my neck..."
    "And I feel this sense of dread, though I can't exactly tell from what..."
    "As I wipe my brow from the sweat, I notice light from outside starting to creep through the blinds. I turn my head to check my alarm clock."
    "5:30."

    if hangout3 == "Sayori":
        mc "I guess that was just a dream, huh?"
        "I loudly muse to myself."
        "Just to be sure, I open my phone to check my texts to see if Sayori had texted me."
        "To my relief, I haven't gotten any notifications since I went to sleep."

    if hangout3 == "Natsuki":
        mc "Better to wake up early in my own bed than on someone's lawn, huh?"
        "I loudly muse to myself."
        "Even though I'm pretty certain that it was a dream, I quickly pat my face to feel for any cuts or bruises."
        "Thankfully, I don't feel anything off, I decide to reach my phone and open my camera to see for myself."
        "Seeing as I still look normal, I let out a huge sigh of relief."

    if hangout3 == "Yuri":
        mc "Better to wake up early than be dead, huh?"
        "I loudly muse to myself."
        "Even though I'm pretty certain that it was a dream, I quickly check myself or any stab wounds."
        "Thankfully, everything is normal and I let out a huge sigh of relief."

    if hangout3 == "Monika":
        mc "This is some 'paradise', huh?"
        "I loudly muse to myself."

    "I try to prop myself up, but I feel a sudden rush of pain hit my forehead, instantly making me feel dizzy. I force myself to lay back down."
    "My vision becomes blurry as I furiously blink several times in an effort to restore it back to normal."
    "Well...{w=0.38}at least I don't need to get up particularly soon..."

    if hangout3 == "Sayori" or hangout3 == "Natsuki" or hangout3 == "Yuri":
        "I would go back to sleep but I'd rather not dream of being attacked by [hangout3] again..."

    if hangout3 == "Monika":
        "I would go back to sleep but I'd rather not listen to any more that voice's creepy ramblings..."

    "I simply stare at the ceiling through my hazy vision as I attempt to process my experience."
    "These nightmares are just getting stranger..."
    "I don't see it stopping anytime soon..."
    "Along with these side-effects..."
    "If you can even call them that..."
    "I guess this weekend I could try scheduling a doctor's visit about all this..."

    if tell_s == True:
        "Maybe I can bring Sayori with me too..."
        "Hopefully we can try to solve two problems at once that way..."

    if tell_s == False:
        "I should tell Sayori about this too..."
        "Maybe I need to just get this off my chest rather than have it lingering inside of me..."

    "I simply let out a sigh and stare at my ceiling, waiting for my headache to dissipate."
    "As I try to pass the time before I need to get out of the bed, it still hits me that I'm still nowhere close to deciding on what to say to [poem_giver]."
    "Though, I don't really expect her to talk to me given how yesterday went..."

    if hangout3 == "Monika":

        if monika_hangout == True:
            "But I think I've pretty much decided on my feelings for Monika..."

            if encore_sayoriquestion_1 == True:
                "Though I still don't know if I'd want to end things with Sayori without talking to her first..."

            if encore_sayoriquestion_1 == False:
                pass

        if monika_hangout == False:
            "And I'm not really that much closer to deciding if I really want to go for Monika or not..."
            "I mean, I'm pretty sure she likes me back..."
            "But I don't know how to approach her about it..."

            if encore_sayoriquestion_1 == True:
                "Especially since I'd have to break up with Sayori..."

            if encore_sayoriquestion_1 == False:
                pass


    if hangout3 == "Natsuki":

        if natsuki_hangout == True:
            "But I think I've pretty much decided on my feelings for Natsuki..."

            if encore_sayoriquestion_1 == True:
                "Even if I'm still shaky on the prospect of breaking up with Sayori..."

            if encore_sayoriquestion_1 == False:
                pass

        if natsuki_hangout == False:
            "And I'm not really that much closer to deciding if I really want to go for Natsuki or not..."
            "I mean, I'm pretty sure she likes me back..."
            "Well, I'm confident that she doesn't hate my guts at least..."
            "But how am I supposed to approach her about it?"

            if encore_sayoriquestion_1 == True:
                "Let alone, how would I even go about breaking up with Sayori?"

            if encore_sayoriquestion_1 == False:
                pass


    if hangout3 == "Sayori":

        if sayori_hangout == True:
            "I think I've settled on my feelings for Sayori at this point..."

            if encore_sayoriquestion_1 == True:
                "And I don't see a reason to break up with her..."

            if encore_sayoriquestion_1 == False:
                "I do think that I could at least try to give her a chance, if she's still willing..."

        if sayori_hangout == False:
            "I think I've settled on my feelings for Sayori at this point..."

            if encore_sayoriquestion_1 == True:
                "And I don't see a reason to break up with her..."
                "Even if I haven't spent as much time around her as I should've..."
                "I know I love her."

            if encore_sayoriquestion_1 == False:
                "But I'd probably be better off getting her the help she needs first."
                "After that, maybe we can see..."


    if hangout3 == "Yuri":

        if yuri_hangout == True:
            "But I think I've pretty much decided on my feelings for Yuri..."

            if encore_sayoriquestion_1 == True:
                "Even if I'm still shaky on the prospect of breaking up with Sayori..."

            if encore_sayoriquestion_1 == False:
                pass

        if yuri_hangout == False:
            "And I'm not really that much closer to deciding if I really want to go for Yuri or not..."
            "I mean, I'm pretty sure she likes me back..."
            "But how will she react?"

            if encore_sayoriquestion_1 == True:
                "And Yuri's reaction isn't the only one I'd need to worry about..."

            if encore_sayoriquestion_1 == False:
                pass


    "I should've expected to deal with this much drama when I decided to join an all-girls club..."
    "In retrospect, I guess I was kind of asking for it..."
    "I just didn't know how stressful it'd be!"
    "Ah well, I guess I'll try to solve one problem at a time..."
    "I guess try to put in some more thought into my feelings about [poem_giver]."
    "Maybe today it'll dawn on me..."
    play music e17
    "Suddenly my alarm on my phone rings."
    stop music
    "I gingerly reach over to silence the alarm, and proceed to drag myself out of bed and prepare for the day in front of me."
    "Fortunately it seems that my body has recovered from the ordeal, and I feel pretty much back to normal."
    "But, something continues to nag me in the back of my mind."
    "Maybe if I ignore it, it'll go away..."
    mc "Let's get this over with..."
    "I mutter to myself as I begin my morning routine."
    scene bg residential_day
    with wipeleft_scene
    "I ended up getting ready a few minutes earlier than I normally do, so I decided to take the time to wait outside for Sayori outside."

    if hangout3 == "Yuri":
        "Though I suppose I subconsciously rushed through breakfast out of fear that Yuri was somehow hiding in the kitchen again..."

    else:
        pass

    "Leaning against the lamp post, I reflect on the last night's dreams, and try to make sense of what it's been saying."

    if hangout3 == "Sayori" or hangout3 == "Natsuki" or hangout3 == "Yuri":
        "I don't understand why I'm supposedly not allowed to spend time with [hangout3]..."
        "I'm a person with free will, I can choose who I want to spend my time with freely!"
        "But I don't understand how this voice can be jealous of me spending time with [hangout3]..."
        "Unless my subconscious is trying to tell me something..."

    if hangout3 == "Monika":
        "It seems like the voice likes it when I'm around Monika for some reason..."
        "But I don't know why that would be..."
        "Unless my subconscious is trying to get me to man up..."
        "Which I guess isn't really a bad thing..."

    s "Hey, [player]!"
    show sayori 1a at t11 zorder 1
    play music t2 fadein 1.0
    "I look up to see Sayori already standing in front of me."
    mc "Oh! Hey, didn't see you there..."
    mc "Ready for school?"
    show sayori 1f
    "I try to sound as energetic as possible but Sayori's able to see through my facade pretty easily."
    s 2g "[player]..."
    stop music fadeout 2.0

    if tell_s == True:
        s "Did you have another bad dream last night?"
        "I simply nod my head in disappointment."
        mc "I don't really want to talk about it right now..."
        show sayori 1g
        s "[player]..."
        show sayori 4g at face
        play sound fall
        "Sayori suddenly steps forwards and brings me into an embrace."
        "I slowly reciprocate, feeling the warmth of Sayori's body radiating on to me."
        "Despite the traumatic experience of last night, I already feel somewhat better..."
        s "I'm sorry you're having nightmares again..."
        s "I just wish there was something I could do to help..."
        mc "You can't, and I don't know what will to be honest..."
        show sayori 1f at t11 zorder 1
        "Sayori and I break our embrace, her warmth quickly being brushed off by the cool morning breeze."
        mc "I have considered seeing my doctor about this."
        mc "Maybe there's a medical explanation for it..."
        s 2g "Well, just do whatever you need to, [player]."
        s 4g "I'll support you."
        "Well, I guess now would be a good time to bring up my idea for Sayori..."
        mc "I'd like for you to come with me."
        "Sayori eyes me suspiciously."
        s "Eh? How come?"
        s 1l "Not that I'm opposed to going with you or anything, but..."
        s 1h "I thought it wasn't that bad..."
        show sayori 1g
        mc "It's not about that..."
        show sayori 1e
        mc "It's about your rainclouds..."

        if hangout3 == "Sayori":

            if sayori_hangout == True:
                mc "Remember the idea that I brought up with you last night?"
                s "Y-{w=0.38}yeah?"
                mc "It would mean a lot to me if we both tried to solve our problems together..."
                mc "I know you want me to get better, and well..."
                show sayori 1k
                mc "I'd like to be able to return the favor somehow..."
                "Sayori uncomfortably gazes off into the distance."
                s "I'm...{w=0.38}still thinking it over, [player]..."
                "I still don't quite understand Sayori's reluctance to getting help, but given that this is a pretty big deal for her, I need to try to be as patient as possible."
                mc "It's okay, it's not like I'm heading there after school or anything..."
                mc "Don't feel rushed."
                show sayori 1d
                "Sayori flashes me a weak smile."
                mc "Come on, let's get going."
                "Without another word said, Sayori and I begin our daily commute to school."
                jump day4_school

            if sayori_hangout == False:
                s "What about them?"
                mc "Look...{w=0.38}have you ever thought about seeing someone about your depression?"
                show sayori 1k
                "There's a long, uncomfortable pause between us."
                "Sayori lets out a sigh."
                s 1f "It's crossed my mind a few times over the years..."
                s 1g "Why are you asking me this?"
                mc "Well..."
                mc "I don't think just me being around you is going to make your rainclouds go away..."
                mc "There needs to be a long term solution to this..."
                mc "So, I'm going to head to the doctors this weekend..."
                mc "Why don't you come with me?"
                show sayori 1k
                "Sayori uncomfortably gazes off into the distance."
                s "Well..."
                s "I'll think about it, okay?"
                "I don't understand Sayori's reluctance to getting help..."
                "But if she's thought about it before and still hasn't gone, there has to be some sort of reason..."
                "I'll ask her about it later, the least I can do right now is be patient with her."
                mc "It's okay, it's not like I'm heading there after school or anything..."
                mc "Don't feel rushed."
                show sayori 1d
                "Sayori flashes me a weak smile."
                mc "Come on, let's get going."
                "Without another word said, Sayori and I begin our daily commute to school."
                jump day4_school

        if hangout3 != "Sayori":
            s "What about them?"
            mc "Look...{w=0.38}have you ever thought about seeing someone about your depression?"
            show sayori 1k
            "There's a long, uncomfortable pause between us."
            "Sayori lets out a sigh."
            s 1f "It's crossed my mind a few times over the years..."
            s 1g "Why are you asking me this?"
            mc "Well..."
            mc "I don't think just me being around you is going to make your rainclouds go away..."
            mc "There needs to be a long term solution to this..."
            mc "So, I'm going to head to the doctors this weekend..."
            mc "Why don't you come with me?"
            show sayori 1k
            "Sayori uncomfortably gazes off into the distance."
            s "Well..."
            s "I'll think about it, okay?"
            "I don't understand Sayori's reluctance to getting help..."
            "But if she's thought about it before and still hasn't gone, there has to be some sort of reason..."
            "I'll ask her about it later, the least I can do right now is be patient with her."
            mc "It's okay, it's not like I'm heading there after school or anything..."
            mc "Don't feel rushed."
            show sayori 1d
            "Sayori flashes me a weak smile."
            mc "Come on, let's get going."
            "Without another word said, Sayori and I begin our daily commute to school."
            jump day4_school



    if tell_s == False:
        s "What's wrong?"
        s 4h "You were like this yesterday too!"
        s 4g "I just want to make sure you're okay..."
        "I let out a sigh."
        "I shouldn't keep something like this from her..."
        show sayori 1g
        mc "It's nothing too concerning..."
        mc "I've just been having some bad nightmares the past few days..."
        mc "I'm not entirely sure why I'm having them, but I'm sure it'll blow over soon."
        s 2h "Why didn't you tell me?"
        "I feel a returning sense of guilt course through me as I reflect on why I decided to keep this from Sayori."

        if encore_sayoriquestion_1 == True:
            "She is my girlfriend after all..."
            "She should be one of the first people to know if something's bothering me..."

        if encore_sayoriquestion_1 == False:
            "We've always been honest with each other about things that have been troubling us, and I feel kind of bad now for not telling her about this sooner."

        mc "I...just didn't want to worry you."
        mc "You got enough going on yourself..."
        s 4g "[player]..."
        s 4h "No matter what I'm dealing with or going through, I'm always going to make time for you."
        s 1h "Don't ever forget that, okay?"
        s 1g "I don't care how I'm feeling or whatever I'm going through..."
        s "You're what matters to me the most!"
        "I feel a sudden rush of blood to my face as Sayori says that."
        "As much as I'm touched by what she's saying, I know she's right too..."
        "I knew I should've told her about these nightmares, just like how I should tell her about everything else that's going on..."
        "But maybe there's a time and place for that..."
        show sayori 1e
        mc "I...{w=0.38}t-{w=0.38}thank you, Sayori..."
        mc "I really appreciate that...{w=0.38}thank you..."
        s 1y "Don't mention it..."
        mc "I mean, coming from you, that's pretty amazing..."
        s "It's...{w=0.38}just how I feel, [player]..."
        mc "Well, I'm grateful..."
        mc "And you know how much I care about you too..."
        "I've been meaning to bring up with Sayori my idea for her seeing someone about her depression, but for whatever reason, the words escape me..."
        "The moment of silence continues to pass over us as we stand on the sidewalk, unable to make lasting eye contact with each other."
        "Finally, Sayori speaks up."
        s 1y "I guess we should start walking, huh?"
        mc "Yeah, I'd hate to make us late."
        "Without another word said, we begin our daily commute to school."
        jump day4_school


label day4_school:
scene bg corridor
with wipeleft_scene
"The walk to school was rather silent..."

if hangout3 == "Sayori":
    "I ended up telling Sayori some of the details about my nightmare."
    "I avoided telling her the more gruesome parts of it, but she was still disturbed all the same."

if hangout3 == "Natsuki" or hangout3 == "Yuri":
    "I ended up giving Sayori the gist of what happened in my dream about [hangout3]."
    "I left out some of the more gruesome parts, but Sayori was still pretty terrified."

if hangout3 == "Monika":
    "I ended up telling Sayori all about what I experienced last night with the voice..."

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            "I was sure to mention the empty room to her as well."

    else:
        pass

    "Needless to say, she was just as disturbed as I was."

"I also explained to Sayori what the other two dreams were like as well to the best of my memory."
"We tried to make sense of everything as best we could, but we couldn't reach any solid conclusion for why I could possibly be having these nightmares."
"I haven't been watching any horror movies lately, and I haven't experienced anything traumatic since the festival..."
"Maybe it's just some sort of weird phase I'm going through."
show sayori 1g at t11 zorder 1
"Ultimately, we decided to stop talking about it as we got closer to Sayori's class."
mc "Well...{w=0.38}I guess I'll see you after school?"
s 4h "Just take care of yourself, okay, [player]?"
show sayori 4g
mc "I'll try my best. Even despite those nightmares, I'm not really tired..."
mc "Just more disturbed than anything else..."
s 1g "Well let me know if something happens."
mc "I'll be sure to."
s 1q "Good."
"Sayori flashes me her biggest smile that I've seen all day, which helps calm my nerves a bit."

if hangout1 != "Sayori":
    if hangout2 != "Sayori":
        if hangout3 != "Sayori":
            "It's been a while since we've gotten to enjoy each other's company..."
            "I wish I could make up for all the lost time this week..."
            "I've made so many mistakes, and yet here she is, still trying to give it her all..."

            if encore_sayoriquestion_1 == True:
                "Do I really deserve her?"

            if encore_sayoriquestion_1 == False:
                "Do I really deserve her friendship?"

else:
    pass

if encore_sayoriquestion_1 == True:
    "If it weren't for the other students walking around in the hallways, I'd probably take her into my arms right about now."

if encore_sayoriquestion_1 == False:
    "I still can't believe even after everything, she's still willing to put a smile on my face..."
    "If nobody else was around, I wouldn't mind another one of her hugs..."

show sayori 1y
"Apparently, I'm not the only one feeling the magic of the moment either, as Sayori blushes brightly."
s "I'll...{w=0.38}see you later, [player]!"
"She quickly stammers out."
mc "Y-{w=0.38}yeah! See you!"
show sayori at thide
hide sayori
"Sayori quickly scrams into her classroom, her face flush with embarrassment."
"Even I can feel my own face running hot."
"In an effort to not draw attention to myself, I speed walk to my classroom."
scene bg class_day
with wipeleft_scene
play music t3 fadein 1.0
"In what has to be record time, I arrive at my fairly empty classroom."
"Only a few early birds were sitting in their seats by the time I got there."
"I walk to the back of the room to my usual spot and begin unpacking my stuff for class."
"However, as I'm doing that, my pocket vibrates."
"I pull out my phone to see that I've gotten a text..."
"It's from [hangout3]..."

if hangout3 == "Sayori":
    jump s_text

if hangout3 == "Natsuki":
    jump n_text

if hangout3 == "Monika":
    jump m_text

if hangout3 == "Yuri":
    jump y_text


label s_text:

"It's not that often we text each other given that we see each other in person a lot..."
"Not to mention we just saw each other..."
s "You feeling okay?"
"I feel a smile creep across my face as I read that."
"Still, I was a little worried before that Sayori would overreact knowing something was wrong with me."
"I really do appreciate her concern though."
mc "Yes, I'm feeling fine. You don't need to worry."

if encore_sayoriquestion_1 == True:
    "I add a heart emoji to the text for good measure."
    "Sayori responds about a half minute later."
    s "Okay...just wanted to make sure!"
    "I then receive a kissing face emoji from her."
    "I try to hide my grin from my classmates as I send one back to Sayori as well."
    "As I finish getting ready for class my phone rings once again."
    "I look over to read the text."
    s "Do you want to hangout in the club later?"
    "I contemplate my response."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "She just probably wants to make sure I'm doing okay..."
            "Besides, I've enjoyed spending time with her lately, so there's no reason not to..."

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            "I have spent a fair amount of time around her lately..."
            "Though she probably just wants to make sure I'm alright..."
            "Besides, I've had fun with her the past two days, so hopefully the trend continues!"

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            "I have spent a fair amount of time around her lately..."
            "Aside from the mishap with [hangout2] on Tuesday..."
            "And spending more time with Sayori would probably continue to smooth things over..."
            "After all, we're both trying to move past it..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            "We really haven't gotten the chance to spend much time together this week..."
            "And last night we both told each other we wanted our relationship to work..."
            "I should stick to my promise..."

if encore_sayoriquestion_1 == False:
    s "Well I just wanted to make sure. You know I worry about you! Especially after everything you told me!"
    mc "I know...I was worried that you'd get creeped out and wouldn't stop worrying..."
    "I set my phone down as I finish unpacking my things for class."
    "Just as I finish, I get another text from Sayori."
    "I look over to read it."
    s "Do you want to hangout in the club later?"
    "I contemplate my response."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            "She just probably wants to make sure I'm doing okay..."
            "Besides, I've enjoyed spending time with her lately, so there's no reason not to..."

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            "I have spent a fair amount of time around her lately..."
            "Though she probably just wants to make sure I'm alright..."
            "Besides, we've made pretty good progress in repairing our friendship, so hopefully we can keep things up..."

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            "I have spent a fair amount of time around her lately..."
            "Even though I did upset her on Tuesday when I was with [hangout2]..."
            "But spending more time with Sayori would probably continue to smooth things over..."
            "After all, we're both trying to move past everything that's happened between us..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            "We really haven't gotten the chance to spend much time together this week..."
            "And last night we both told each other we wanted to make things better between us..."
            "This could be another opportunity to do just that..."

mc "Yeah sure! I'd love to!"
s "That's great! I should be getting to the club a little earlier today, I'll be in my usual spot!"
mc "Sounds good to me!"
"Sayori sends her favorite smiling emoji, and I end up sending one back as well."
"Well this is great! I get to spend today with Sayori!"
"I wonder if she has anything special planned..."
jump day4_club


label n_text:

"She never texts me this early..."
n "Heyyyyyy!"
"I can certainly feel her personality shine through the text as I read it."
"It comes across to me as pleasant surprise more than anything, and considering the awful start I've had to my day, I'll take it!"
mc "Hey! What's up?"
"I quickly reply back and finish getting my stuff ready for class."
"Just as I finish pulling the last few remaining things out of my bag, I hear my phone go off again."
"I look over to read the text."

if natsuki_hangout == True:
    n "Pretty good! I'm reading the manga we got yesterday and it's freaking awesome!"

if natsuki_hangout == False:
    n "Pretty good! I'm reading the manga I got yesterday and it's freaking awesome!"

"I let out a slight chuckle to myself."
mc "Well hey, I'm glad you're enjoying it!"
"It seems weird that Natsuki would just be randomly texting me about her manga this early in the day, but it's not like I have anything better to do until the teacher comes..."
"I might as well try to keep the conversation going."
mc "How far in are you?"
"After about a minute I get a reply from Natsuki."
n "I just got past the first chapter! You need to read this with me!"
mc "I mean...I'm still behind a little with the story...won't I get spoiled?"
n "You can probably get by the first chapter without getting seriously spoiled."
mc "If you say so..."
n "So...do you want to read it with me later or not?"
"I contemplate my response."

if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        "Well we have been spending a lot of time together recently..."
        "And we've gotten closer than ever since we first started talking..."

if hangout1 != "Natsuki":
    if hangout2 == "Natsuki":
        "Spending some more time with Natsuki wouldn't hurt..."

if hangout1 == "Natsuki":
    if hangout2 != "Natsuki":
        "Well, if I really want to go for Natsuki, I should probably take this chance..."
        "Considering how she saw me with [hangout2] on Tuesday..."

if hangout1 != "Natsuki":
    if hangout2 != "Natsuki":
        "We haven't gotten the chance to spend much time together lately."
        "If I want to get closer to Natsuki, I should take this opportunity..."

mc "Yeah sure! I'd love to read it with you!"
n "That's awesome! I'm telling you: you're really going to like it!"
mc "Looking forward to it!"
n "You know where to find me when you get to the club!"
mc "I'll head straight to the closet as soon as I get in!"
n "Great! TTYL!"
mc "Bye!"
"I put my phone down as I send the last text and smile to myself."
"This is great! I get to spend today with Natsuki!"
"I wonder what else aside from reading we'll get to do..."
jump day4_club


label m_text:

"Can't say I was expecting that..."
m "Hey, [player]!"
"I blink a couple of times at the screen to make sure that it's really Monika."
"She even sent me a smiling emoji..."
"This is almost too good to be true!"
mc "Hey! What's up?"
"Monika almost instantly replies."
m "Pretty good! Just waiting for my teacher to get here."
mc "Yeah, same here..."
"I find it odd that Monika would choose me of all people to make small talk with."
"Still, it's not like an opportunity like this comes up often..."
mc "So, how's your morning been so far?"
m "It's been pretty good actually, thank you!"
m "I had the chance to write some more lyrics for my song, so it shouldn't be too much longer before I'm finished!"
mc "That's great! Can't wait to hear it again!"
m "Well I'm glad you mentioned that! I'd love to hear your opinion on what I have for the second verse!"
m "I'm not entirely sure if I'm sold on the way it rhymes."
m "If you want before the club officially starts we can head off back to the music room together."
"I contemplate my response."

if hangout1 == "Monika":
    if hangout2 == "Monika":
        "I mean we've been hanging out pretty frequently this week..."
        "And it's been a wonderful experience each time!"

if hangout1 != "Monika":
    if hangout2 == "Monika":
        "It's not like Monika and I have spent that much time together..."
        "Well, we've only started really talking recently..."
        "I should probably take this chance..."

if hangout1 == "Monika":
    if hangout2 != "Monika":
        "Well, if I'm seriously interested in Monika, I should probably take this chance..."
        "Considering how she saw me with [hangout2] on Tuesday..."

if hangout1 != "Monika":
    if hangout2 != "Monika":
        "I've always wanted to get closer to Monika, but I just never really got around to it..."
        "And since she's asking me, it'd be foolish not to say yes to her..."

mc "I'm not an expert on writing music or anything, but I'd love to help you out!"
m "Aww thanks you're so sweet!"
"As if I wasn't already blushing enough from that compliment, Monika sent me a kissy face emoji accompanied with her last text."
"It's a good thing nobody's paying any attention to me right now..."
mc "I'll see you at the club!"
m "Won't I see you at lunch?"
mc "I'm gonna be sitting by myself for today, I still need to think things over."
"I set my phone down as I finish pulling out the last few things I need for class."
"As soon as I finish I hear my phone go off with another text from Monika."
m "It's okay! I'll see you at the club! GTG Bye!"
mc "Bye."
"Even though I expected that to be the end of the conversation, Monika once again sent me a kissy face emoji, which continued to make me blush."

if encore_sayoriquestion_1 == True:
    "Even though I thought Monika and I agreed to just be friends, it's clear that we're both doing a pretty bad job at sticking to that promise..."
    "For whatever reason, it seems like we can't stop thinking about each other..."

if encore_sayoriquestion_1 == False:
    "There is no way I could've gotten this lucky!"
    "Monika's been acting incredibly flirty with me since we finally started talking..."
    "It's enough to make me want to kick myself because I should've started talking to her sooner..."


"Still, I'm just looking forward to spending more time with Monika!"
"And I have feeling this time we may get the chance to do more than talk about music..."
jump day4_club

label y_text:

"That's a first for her..."
y "Hello..."
"I can certainly feel Yuri's shyness through the screen."
"I just need to play it cool..."
mc "Hey! What's up?"
"I see the notification that Yuri's typing, so I give her a few moments as I finish getting my things out for class."
"Sure enough, just as I finish getting everything ready, my phone goes off with a text notification."
"I look over to read what Yuri sent me."
y "Oh, I'm doing alright! I was just reading some Portrait of Markov and it suddenly dawned on me how close we are to the end!"
mc "Oh really? Wow! How much do we have left!"
y "About a hundred pages."
mc "We really have knocked out a lot together recently!"
y "Yes, indeed we have!"
y "If you want, time permitting, we could finish the book today if you'd like..."
"I contemplate my response."

if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        "We really have been spending a lot of time around each other lately..."
        "And I know much it would mean to Yuri if we managed to finish the book today..."

if hangout1 != "Yuri":
    if hangout2 == "Yuri":
        "I haven't spent as much time as I could've lately around Yuri..."
        "But I know how much she loves reading together, so I should take her up on this..."

if hangout1 == "Yuri":
    if hangout2 != "Yuri":
        "If I really want to go for Yuri, I should probably spend more time around her to see if I still feel the same..."
        "And this would be a good chance to do that..."

if hangout1 != "Yuri":
    if hangout2 != "Yuri":
        "I mean Yuri's always been shy, even around me..."
        "Heck, I even considered yesterday a breakthrough..."


mc "Yeah sure! I'd love to do some more reading with you!"
mc "I really can't wait for us to get to the last chapter!"
y "Me too! I'll see you in the club later! Good-bye!"
mc "Bye!"
"I put my phone back in my pocket as a large smile comes across my face."
"I'm going to get to spend more time with Yuri! This is great!"
"I wonder what else we'll be able to do today..."
jump day4_club


label day4_club:
"As soon as I finish my thought, the teacher comes in to start today's lesson."
"Here we go with another boring day of school..."
"At least I have the club to look forward to..."
stop music fadeout 2.0
scene black
with dissolve_scene_full
scene bg class_day
with open_eyes
"The rest of the school day goes by rather quickly, and I was able to get through it without much incident."
"I occasionally got a headache and every now and then the same mysterious sense of dread washed over me, but it never lasted more than a few minutes."
"I also tried to use my time during lunch period to work out my feelings towards [poem_giver]."
"Trying to settle on my exact feelings for her was hard, but I think I've generally worked out what I could say to her..."
"Though I'm doubtful that she'll ask me about it today."
"Maybe by Friday at the latest..."
"Ah, why am I worrying about this?"
"I should be looking forward to the club today, not dreading it!"
"I'm going to get to spend more time around [hangout3], I should put my best face forward!"
play sound school
"Just like that, the final school bell rings, signifying the end of the day."
"I pack up my things and head out to meet Sayori."
scene bg corridor
with wipeleft_scene
play music t3 fadein 2.0
"I wait by the doors to the classroom as I see countless students walking by me on the way to their own respective clubs or on their way home."
"Sure enough, I spot Sayori heading my way, and I wave to get her attention."
"She manages to squeeze her way through the crowd to get to me."
show sayori 3q at t11 zorder 1
s "Hi, [player]!"
mc "Hey, Sayori! Nice crowd surfing skills!"
show sayori 1r
"Sayori let's out a small giggle."
s 1x "Well hey, it's a pretty good skill to have in this school!"
show sayori 1a
mc "Yeah, I know what you mean! They really should get these hallways enlarged."
mc "Not that it would ever happen..."
"We wait for a few minutes for the hallways to thin out a little so we can get to the stairs without a hassle."
"While we're waiting, Sayori turns to me."
s 1c "So, how was your day?"
show sayori 1b
mc "It was alright..."
s 1h "Are you feeling any better?"
show sayori 1g
"I pause to think it over for a moment."
"Just then, the same sense of dread that's been plaguing me all day creeps up my spine."
"It's almost enough to make me shake this time."
"I try to sound as convincing as I can with my answer."
mc "I guess so..."
mc "I haven't felt any worse at least."
s "Well I guess that's good..."
s 1h "I just want you to be okay..."
show sayori 1g
mc "I know, I know..."
mc "You're doing a good job, Sayori. I'm alright."
show sayori 1d
"I shoot Sayori a reassuring smile as she does the same."
mc "Anyways, enough about me, how's your day been?"
s 4r "I had a test today!"
mc "Oh really? How was it?"
s 5b "Um..."
"Sayori nervously twiddles with her fingers."
mc "You bombed it, didn't you?"
s "Well, I haven't gotten the results back yet..."
s 5c "But in my defense, it was a really hard test!"
mc "Did you study for it?"
show sayori 5a
"Sayori nervously giggles."
"I shake my head in disappointment before she finally lets it out."
s "I...{w=0.38}forgot we had one until last night..."
"I facepalm."

#This bit can be screwy

if sayori_hangout == True:
    jump s_screw1

if natsuki_hangout == True:
    jump s_screw2

if monika_hangout == True:
    jump s_screw2

if yuri_hangout == True:
    jump s_screw2

else: # No hangout variable was true
    jump s_screw3


label s_screw1:

show sayori 1e
mc "How come you didn't tell me this last night?"
mc "I would've helped you study..."
s 1l "I didn't remember until after I got home..."
"I once again shake my head in disappointment."
show sayori 1e
mc "Sayori, you have to do better than that..."
mc "If you don't pay attention to your grades, you're going to fall behind again..."
s 1h "It's just one test, [player]..."
s 1l "I think I've done alright on all the others..."
mc "Well, I just don't want a repeat of seventh grade..."
mc "That was a nightmare to pull your grades back up..."
s 4h "But we did it!"
mc "Barely."
s 1l "Come on, [player], don't you trust me?"
stop music
mc "Not on important things, no."
show sayori 1e
jump merge_1

label s_screw2:

show sayori 1e
mc "How come you didn't study last night?"
mc "I would've helped..."
s 1l "I saw you walk off with [hangout3] and I didn't want to disturb you guys..."
"I feel my body nearly tremble with horror as I quickly become afraid at the prospect that Sayori might be getting the completely wrong idea here..."
mc "We just hungout, Sayori..."

if natsuki_hangout == True:
    mc "Natsuki and I went to the bookstore to pick up the latest edition of Parfait Girls..."

if monika_hangout == True:
    mc "Monika and I just took a walk together..."

if yuri_hangout == True:
    mc "Yuri and I went to check out this new nature preserve that just opened..."

s 1d "I believe you..."
mc "You would've been welcome tag along, we wouldn't have mind..."
s 1y "I wouldn't have wanted to get in the way of you two..."
mc "Sayori, you wouldn't have and you know it..."
mc "You're not a burden."

if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        mc "Had I known you had a test coming up, I would've been willing to drop what I was doing and help you..."
        s "Then you wouldn't have been able to spend time with [hangout3]..."
        mc "It doesn't matter, Sayori."
        mc "There's always another time."
        s 1l "Don't you think I can handle important things like this on my own?"
        stop music
        mc "Not really, no."
        jump merge_1


    else: # hangout1 == "Sayori", hangout 2 != "Sayori"
        s 1l "Well these past 2 days I've certainly felt like one..."
        s 1g "You really haven't been around to help me..."
        mc "I know, and I'm sorry..."
        s 1l "So I have a hard time believing that you would want to willingly help me with something important now."
        s "Don't you think I can handle things by myself?"
        stop music
        mc "Not really, no."
        jump merge_1


else: # hangout1 != "Sayori"
    if hangout2 == "Sayori":
        mc "If you told me you had a test, I would've happily helped out..."
        s "Then I would've kept you from spending time around [hangout3]..."
        mc "It doesn't matter, Sayori."
        s 1l "Don't you think I can handle important things like this on my own?"
        stop music
        mc "Not really, no."
        jump merge_1

    else: # Didn't hang out with Sayori on day 1 or 2
        s 1l "I'm having a hard time believing that, [player]..."
        s 1g "It's not like you've been around me all that much lately..."
        mc "I know..."
        s 1l "So I kind of have a hard time believing that you would want to willingly help out now..."
        s "Don't you think I can handle things by myself?"
        stop music
        mc "Not really, no."
        jump merge_1

label s_screw3:

mc "How come you didn't tell me this last night?"
mc "I would've came over and helped..."
s 1l "Well you wanted some space to yourself, so I didn't want to get in the way..."
"I once again shake my head in disappointment."
show sayori 1e
mc "Sayori, I would've happily held off on what I was doing to help you."

if encore_sayoriquestion_1 == True:
    mc "I love you that much..."

if encore_sayoriquestion_1 == False:
    mc "I care about you that much..."

s 1l "I mean, don't you think I can handle things by myself?"
stop music
mc "Not really, no."
show sayori 1e
jump merge_1


label merge_1:

show sayori 1e
"Sayori stares at me as the air between us suddenly becomes unusually heavy."
"I'm confused for a moment until the full weight of what I just said hits me like a freight train."
"Oh..."
mc "I didn't mean it like that!"
mc "It's just-"
s 1k "It's fine, [player]. I know what you meant."
"Sayori's deadpan tone and expression fail to convince me otherwise."
"But there's no real use fighting it now..."
mc "I'm sorry..."
s 1l "You know, I think the hallway's clear enough for us..."
"I look to see that other than a few lingering students, the hallway's completely empty."
mc "I guess you're right..."
s 1k "Let's go."
"Sayori starts walking off without me in the direction of the stairwell, leaving me no choice but to practically run after her."
"The rest of the walk to the clubroom was silent, as Sayori barely even acknowledged me."
"I kept mentally kicking myself over and over for how stupid I was to say it like that."
"Who knows how long she'll be like this..."

if hangout3 == "Sayori":
    "I doubt she'll want to spend time around me now..."

else:
    pass

show sayori at thide
hide sayori
scene bg club_day
with wipeleft_scene
"The usual scene greets us as we walk in. Everyone is in their usual spots doing their usual routines."
show sayori 1k at t21 zorder 1
show monika 1a at t22 zorder 2
"Monika shoots us her signature grin as she sees Sayori and I walk in."
"Oddly enough, something about Monika's grin rubs me the wrong way..."
show sayori at thide
hide sayori
show monika 1g at t11 zorder 1
"Before Monika can greet us, Sayori promptly goes to her usual spot and stares blankly at the wall."
"Monika shoots me a concerned look but I raise my hand at her to let her know I have it under control."
show monika at thide
hide monika
"Without a word, Monika returns to the teacher's desk as I gingerly put my stuff on a desk in the middle of the room."
show sayori 1k at t11 zorder 1
"I look over to Sayori, who's still staring blankly at the wall."
"I let out a sigh and walk over to her."
mc "Sayori?"
s 1i "I’m fine, [player]."
s 1k "I just want some space right now..."
"I can't believe how badly I screwed up this time..."
mc "Okay...{w=0.38}let me know if you need anything..."
"Sayori doesn’t give me a response."
show sayori at thide
hide sayori
"I sigh as I walk over to the windowsill across the room."
"I stare out into the view of the school's courtyard as I reflect on the situation."

if hangout3 == "Sayori":
    "I guess we won't be spending time together today..."

else:
    "How did I mess up this badly?"
    "What's wrong with me?!?"

if encore_sayoriquestion_1 == True:
    "I really suck at this whole boyfriend thing, don't I?"

if encore_sayoriquestion_1 == False:
    "I suck at being a friend to her..."

"Through my internal self-deprecation, I begin to space out."
"..."
"..."
"..."
"Suddenly, I feel a tap on my shoulder."
"I turn around, expecting to see either Sayori or Monika."

if poem_giver == "Natsuki":
    show natsuki 1n at t11 zorder 1
    "Instead, I see Natsuki as soon as I turn around."
    mc "Oh! H-{w=0.38}hey, Natsuki!"
    n "You got a minute?"
    mc "Yeah, sure! What's up?"
    n 3q "Can we talk outside?"
    "I feel another wave of dread wash over me as I hear that."
    "Oh no..."
    "Please don't let this be what I think it is..."
    mc "Why outside?"
    n 1m "It's...{w=0.38}really important..."
    n 1s "I don't want anyone else to hear..."
    mc "Uh, sure..."
    "I reluctantly start walking towards the door with Natsuki as my mind begins racing with all sorts of possibilities for why she wants to talk to me."
    show monika 1c at t21 zorder 1
    show natsuki 1g at t22 zorder 2
    "However, we're stopped right at the doorway by Monika, who looks on at us with a curious expression."
    m 2d "Where are you two going?"
    n 5f "It's not important, Monika! Move!"
    m 2g "Excuse me?"
    n 1g "You heard me."
    show monika 2h
    "Monika is clearly caught off-guard by Natsuki's angry tone, but she doesn't yield."
    m 4i "Actually, Natsuki:{w=0.38} it is important that I know where you two are off to."
    m 2h "We're going to start today's activity in a few minutes."

    if hangout3 == "Natsuki":
        m 3i "I don't want you guys to disappear for ten minutes again."
        n 5e "We didn't 'disappear'!"

    if hangout3 == "Sayori" or hangout3 == "Yuri":
        m 3i "I don't want [player] wandering off again..."
        n 5e "He's not going to 'wander off'!"

    if hangout3 == "Monika":
        m 3i "I don't want you two to wander off just right when we're about to start."
        n 5e "You two disappeared yesterday! Why can't I get my time with him?"

    mc "Ladies, ladies!"
    show monika 1d at h21 zorder 1
    show natsuki 1c at h22 zorder 2
    "I raise my hands calmly in an attempt to diffuse the argument."
    show natsuki 1s at t22 zorder 2
    mc "We'll be right outside, it'll be just a few minutes. Just get us when you're about to start, okay?"
    show monika 1r at t21 zorder 1
    "Monika lets out a defeated sigh."
    m 3q "Fine. I'll give you guys two minutes."
    mc "Thank you, Monika."
    show monika 1h
    "Monika angrily stares at Natsuki for her to say the same, but she maintains her eye contact with the floor."
    show monika at thide
    hide monika
    show natsuki 1s at t11 zorder 1
    "Monika then brushes past us and goes back to the teacher's desk."
    n 1q "Come on..."
    "Natsuki mutters as she opens the door and walks out into the hallway."
    show natsuki at thide
    hide natsuki




if poem_giver == "Yuri":
    show yuri 2u at t11 zorder 1
    "Instead, I see Yuri as soon as I turn around."
    mc "Oh! Hey, Yuri! What's up?"
    y 2q "Do you...{w=0.38}have a moment, [player]?"
    mc "Yeah, sure! What's up?"
    y 3t "If it's not too much, may we take this outside?"
    "I feel another wave of dread wash over me as I hear that."
    "Oh no..."
    "Please don't let this be what I think it is..."
    mc "Is there a particular reason?"
    y 3q "I'd rather that our discussion have some privacy."
    mc "Alright..."
    "I reluctantly start walking towards the door with Yuri as my mind begins racing with all sorts of possibilities for why she wants to talk to me."
    show monika 1c at t21 zorder 1
    show yuri 1f at t22 zorder 2
    "However, we're stopped right at the doorway by Monika, who looks on at us with a curious expression."
    m 2d "Where are you two off to?"
    y 1h "Not now, Monika..."
    m 2g "Excuse me?"
    y 1r "I said it's none of your business!"
    show monika 2h
    "Monika is clearly caught off-guard by Yuri's angry tone, but she doesn't yield."
    m 4i "Actually, Yuri:{w=0.38} it is my business."
    m 2h "It's my responsibility to know where you two are off to."
    m 2h "Especially since we're going to start today's activity in a few minutes."

    if hangout3 == "Yuri":
        m 3i "I don't want you guys to disappear for ten minutes again."
        y 3r "Pardon me, Monika, but we didn't 'disappear'!"

    if hangout3 == "Sayori" or hangout3 == "Natsuki":
        m 3i "I don't want [player] wandering off again..."
        y 3r "Pardon me, Monika, but he's not going to 'wander off'!"

    if hangout3 == "Monika":
        m 3i "I don't want you two to wander off just right when we're about to start."
        y 3r "Pardon me, Monika, but didn't you two disappear yesterday? That's a double standard, don't you think?"

    mc "Ladies, ladies!"
    show monika 1d at h21 zorder 1
    show yuri 3n at h22 zorder 2
    "I raise my hands calmly in an attempt to diffuse the argument."
    show yuri 4c at t22 zorder 2
    mc "We'll be right outside, it'll be just a few minutes. Just get us when you're about to start, okay?"
    show monika 1r at t21 zorder 1
    "Monika lets out a defeated sigh."
    m 3q "Fine. I'll give you guys two minutes."
    mc "Thank you, Monika."
    show monika 1h
    "Monika angrily stares at Yuri for her to say the same, but she seems too embarrassed to say much."
    show monika at thide
    hide monika
    show yuri 4c at t11 zorder 1
    "Monika then brushes past us and goes back to the teacher's desk."
    y "I guess we can go now..."
    "Yuri mutters as she opens the door and walks out into the hallway."
    show yuri at thide
    hide yuri

label day4_confession:
scene bg corridor
with wipeleft_scene
play sound "sfx/closet-close.ogg"
"The hallway becomes eerily silent as the door closes shut behind us."

if poem_giver == "Natsuki":
    jump n_confession

if poem_giver == "Yuri":
    jump y_confession


label n_confession:

show natsuki 5u at t11 zorder 1
"Natsuki and I are standing in the middle of the hallway, with not a single person in sight."
"The air is becoming increasingly fraught with tension as we both struggle to maintain eye contact."
"A pit forms in my stomach as I brace for what I always thought to be the inevitable..."
"Fortunately, it seems Natsuki's just as nervous about this as I am..."
show natsuki 1n
"Part of me hopes that this entire thing is some sort of joke or it was complete misunderstanding..."
"Maybe she's going to ask me about something else? Am I just overthinking things again?"
show natsuki 1s
"But, given how she's been acting lately, it makes either of those options increasingly unlikely, especially since it seems Natsuki's trying to muster the right words."
"As I wait for a few more seconds, I feel that a part of me wants Natsuki to confess her love."
"I've always been attracted to her to a degree..."
"And if this is what I think it's about, then this would be the perfect opportunity to explore something that could always still be..."
"I finally grow tired of waiting and decide to start the conversation."
mc "So...{w=0.38}what did you want to talk about?"
n 5q "I think we both know the answer to that..."
mc "Eh?"
play music e19 fadein 1.0
n 1m "[player]..."
show natsuki 1n
"Natsuki looks me directly in the eyes as she slowly starts scooching herself towards me."
n 1m "I...{w=0.38}I really haven't done this kind of thing before..."
n 1q "I never really got the chance to tell a boy how much I liked them..."
n 1m "Or how much they mean to me..."
n 12b "Because, one way or another, we'd always stop talking before I could tell them..."
n 12c "It really hurts when you like someone, and after a while for some stupid reason, they don't talk to you anymore..."
n 12d "And I'm afraid that with you...{w=0.38}that this is might be one of those times..."
n 12e "I'm afraid that you're just going to stay away from me, riding off with somebody else..."
n 12f "Just before I could tell you how much I like you!"
n 12h "I-{w=0.38}I was so scared that I accidentally pushed you away!"
n 12i "And that I would have to live with that regret on top of everything else for the rest of my life!"
show natsuki 12h
mc "N-{w=0.38}Natsuki..."
show natsuki 12g
"Natsuki sniffs as she wipes the tears off her face."
n "I'm not finished yet!"
"I put my hands up to gesture for Natsuki to continue."
"A couple of sniffs later, Natsuki continues on."
n 12a "To tell you the truth...{w=0.38}I've had my eye on you for quite a while..."
n 12b "Ever since you first joined actually..."
n 12c "I tried acting as cold as possible around you because I was afraid to catch feelings..."
n 12b "I didn't want to get hurt again..."


if encore_sayoriquestion_1 == True:


    if encore_festivalquestion_2 == "Natsuki":
        n 12a "You were always around Sayori...{w=0.38}and I could never get to you without feeling weird about it..."
        n 5m "But...{w=0.38}that changed last Sunday..."
        n 5n "I couldn't stop from feeling...{w=0.38}comfortable around you..."
        n 5q "You really let me be myself..."
        n 5y "I really can't believe we almost kissed a couple of times..."
        n 5m "Not to mention how much fun we had together at the festival too!"

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 5q "The more we hung out, I just couldn't stop thinking about you..."
                n 5n "I even started writing poems about you!"
                n 12a "It was pretty much then when I realized that I loved you..."
                n 5y "And...{w=0.38}as much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 1l "It made me really happy that you didn't completely freak out..."
                n 5m "All this time, you've made feel safe and accepted...{w=0.38}it's not something I'm really used to..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38 }well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice


        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 5q "But after a while, I started to kind of...{w=0.38}miss you..."
                n 5n "Since we missed out spending time together on Monday..."
                n "I was starting to worry if you were just going to ignore me..."
                n "I even started writing poems about how I felt...{w=0.38}and then I pretty much realized that I had real feelings for you..."
                n 5m "But...{w=0.38}you came back..."
                n 5y "And...{w=0.38}as much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 1l "It made me really happy that you didn't completely freak out..."
                n 5m "Being your arms...{w=0.38}helped remind me how safe and accepted I felt around you..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38 }well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice


        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 5q "The more we hung out, I just couldn't stop thinking about you..."
                n "And after Monday, I started to kind of...{w=0.38}miss you..."
                n 5u "And seeing you wit [hangout2] on Tuesday...{w=0.38}hurt me..."
                n 5n "I started writing poems about how I felt...{w=0.38}and then I pretty much realized that I had real feelings for you..."
                n 5m "You made me feel safe and accepted for once..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice


        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n 5q "But after a while...{w=0.38}I started to miss you..."
                n 5n "You were off spending time with the others, leaving me behind..."
                n 12a "I became worried that I was going to be left behind and ignored again..."
                n 12b "So, I started writing poems to help map out my feelings..."
                n 12a "It was pretty much then how much you meant to me."
                n 5m "How safe I felt in your arms..."
                n 5n "How you treated me like I mattered..."
                n "And I missed spending time around you! Even if we really only ever hungout once!"
                n 5u "I was too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice



    if encore_festivalquestion_2 == "Yuri":
        n 5m "I know that we really haven't spent a whole lot of time around each other when you first joined..."
        n 1n "You were always around Sayori..."
        n 12b "And I think that's my fault..."
        n 12a "Why would you want to spend your time around someone who's always bitching about everything?"
        n 5n "Who's always mean?"
        n "When someone like Sayori is the complete opposite!"
        n 1q "I put up a wall up around myself because I didn't want to get hurt..."
        n 12a "I was afraid of catching feelings..."
        n 12b "But I still did..."

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 12a "You...{w=0.38}actually gave me a chance...."
                n 1n "You...{w=0.38}made me feel safe and accepted..."
                n 5m "It's not something I'm really used too..."
                n 5q "You proved me wrong about you..."
                n 5m "And the more time I spent around you...{w=0.38}I started falling for you pretty hard...."
                n 5n "I started writing poems about you to try to understand my feelings..."
                n 12b "And it was pretty much then when I realized that I needed to tell you how I felt..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 12a "I was afraid that I'd never get the chance to really see if it was worth liking you or not..."
                n 12b "That I missed my chance because I kept pushing you away..."
                n 12a "But...{w=0.38}you actually came to me on Tuesday..."
                n 1q "I really wasn't sure how to react..."
                n 5m "But you stuck around...{w=0.38}and we actually had fun!"
                n 1n "You made me feel so safe...{w=0.38}and accepted..."
                n 12b "It's not really something I'm used to..."
                n 5m "But, during all this, I was writing poems about I felt about you..."
                n 5q "And somewhere along the way...{w=0.38}I figured out that I really did like you..."
                n 5t "Being in your arms helped me make up my mind..."
                n 5y "As much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 5u "But, I was too scared to tell you directly how I really felt at the time, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 12a "And...{w=0.38}you actually gave me a chance!"
                n 1m "You went out of your way to try to spend time with me..."
                n 1q "At first I really didn't know how to react..."
                n 5n "But...{w=0.38}I really wanted to get to know you..."
                n 5q "It sucks that stupid Yuri pulled you away from me before we could spend any real time with each other..."
                n 12b "I was afraid afterwards that was my only one chance to try to get to know you..."
                n 12c "Especially after I saw you with [hangout2] on Tuesday..."
                n 5n "All the while, I was really confused about my feelings, so I started writing poems to try to make sense of everything..."
                n 5m "It was pretty much there I figured out that I liked you..."
                n 5u "But, I was too scared to tell you directly how I really felt at the time, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice





if encore_sayoriquestion_1 == False:


    if encore_festivalquestion_2 == "Natsuki":
        n 5m "But after spending so much time with you since you joined...{w=0.38}I couldn't help but open up to you..."
        n 5n "I couldn't stop from feeling...{w=0.38}comfortable around you..."
        n 5q "You really let me be myself..."
        n 5m "On Sunday...{w=0.38}at the festival...{w=0.38}I had so much fun being around you!"
        n 5n "You made me feel safe and accepted for once in my life..."
        n 5q "I thought maybe...{w=0.38}something could come out of it. When we almost kissed last Sunday...{w=0.38}I think that was around the time I really started to fall for you..."


        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 5n "And for a while, you came back to me..."
                n 12a "Until I saw you with [hangout2] on Tuesday..."
                n 12b "Seeing you two like that...{w=0.38}when we were in the same situation on Sunday...{w=0.38}really hurt me..."
                n 5m "And I started to miss you..."
                n 5n "I missed your laugh...{w=0.38}your smile..."
                n 12a "Even reading manga just wasn't the same without you..."
                n 5n "So, I decided to write some poems about how I felt, and it was from there that I decided that I needed to tell you how I felt..."
                n 5u "I was too scared to tell you directly, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 5n "For a while, I was worried if you were going to ignore me after a while like most guys..."
                n 5m "And when you didn't come to me on Monday...{w=0.38}I was really worried..."
                n 5q "I started to...{w=0.38}miss you..."
                n 5n "I started writing poems about how I felt...{w=0.38}and then I pretty much decided then that I needed to tell you how I felt..."
                n 5m "But...{w=0.38}you came back..."
                n 5y "And...{w=0.38}as much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 1l "It made me really happy that you didn't completely freak out..."
                n 5m "Being your arms...{w=0.38}helped remind me how safe and accepted I felt around you..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n 5n "But...{w=0.38}you've been avoiding me this entire week!"
                n "I've missed you...{w=0.38}a lot..."
                n 5n "I've missed everything about you...{w=0.38}your laugh...{w=0.38}your smile..."
                n 12a "Even reading manga just wasn't the same without you..."
                n 12b "And seeing you spend time around the others...{w=0.38}really pissed me off..."
                n 12a "I couldn't figure out a good way to get your attention without getting too angry..."
                n 5n "So, I decided to write some poems about how I felt, and it was from there that I decided that I needed to tell you how I felt..."
                n 5u "I was too scared to tell you directly, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice


    if encore_festivalquestion_2 == "Yuri":
        n 5m "I know that we really haven't spent a whole lot of time around each other when you first joined..."
        n 1n "You were always around Yuri..."
        n 12b "And I think that's my fault..."
        n 12a "Why would you want to spend your time around someone who's always bitching about everything?"
        n 5n "Who's always mean?"
        n 1n "Yuri was always kind and gentle around you...{w=0.38}and I wasn't. I sincerely regret that now..."
        n 1q "I put up a wall up around myself because I didn't want to get hurt..."
        n 12a "I was afraid of catching feelings..."
        n 12b "But I still did..."


        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 12a "You...{w=0.38}actually gave me a chance...."
                n 1n "You...{w=0.38}made me feel safe and accepted..."
                n 5m "It's not something I'm really used too..."
                n 5q "You proved me wrong about you..."
                n 5m "And the more time I spent around you...{w=0.38}I started falling for you pretty hard...."
                n 5n "I started writing poems about you to try to understand my feelings..."
                n 12b "And it was pretty much then when I realized that I needed to tell you how I felt..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice


        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                n 12a "I was afraid that I'd never get the chance to really see if it was worth liking you or not..."
                n 12b "That I missed my chance because I kept pushing you away..."
                n 12a "But...{w=0.38}you actually came to me on Tuesday..."
                n 1q "I really wasn't sure how to react..."
                n 5m "But you stuck around...{w=0.38}and we actually had fun!"
                n 1n "You made me feel so safe...{w=0.38}and accepted..."
                n 12b "It's not really something I'm used to..."
                n 5m "But, during all this, I was writing poems about I felt about you..."
                n 5q "And somewhere along the way...{w=0.38}I figured out that I really did like you..."
                n 5t "Being in your arms helped me make up my mind..."
                n 5y "As much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 5u "But, I was too scared to tell you directly how I really felt at the time, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 == "Natsuki":
            if hangout2 != "Natsuki":
                n 12a "And...{w=0.38}you actually gave me a chance!"
                n 1m "You went out of your way to try to spend time with me..."
                n 1q "At first I really didn't know how to react..."
                n 5n "But...{w=0.38}I really wanted to get to know you..."
                n 5q "It sucks that stupid Yuri pulled you away from me before we could spend any real time with each other..."
                n 12b "I was afraid afterwards that was my only one chance to try to get to know you..."
                n 12c "Especially after I saw you with [hangout2] on Tuesday..."
                n 5n "All the while, I was really confused about my feelings, so I started writing poems to try to make sense of everything..."
                n 5m "It was pretty much there I figured out that I liked you..."
                n 5u "But, I was too scared to tell you directly how I really felt at the time, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38 }well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice

        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
                n 12a "I was afraid that I'd never get the chance to really see if it was worth liking you or not..."
                n 12b "That I missed my chance because I kept pushing you away..."
                n 1m "And the more I saw you with the others...{w=0.38}the more I felt left out..."
                n 1n "It really hurt to see you with [hangout2] on Tuesday..."
                n 12a "I was worried that you hated me or something. That's why you always spent your time away from me..."
                n 12c "And I don't blame you if you do..."
                n 1q "Especially with how I've treated you since you've joined..."
                n 1n "And I'm really, really sorry!"
                n 5n "But I still want to get to know you, you seem like a really great person!"
                n 5q "And...{w=0.38}the more I thought about you...{w=0.38}the more I started to like you..."
                n 5n "I even started writing poems to try to make sense of my feelings!"
                n 5q "And...{w=0.38}I figured out that I truly liked you..."
                n 5u "But, I was too scared to tell you directly how I really felt at the time, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must have read it. I heard of how you were kind of acting like a maniac yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38} well there's no turning back now..."
                n 1u "I should just give it to you straight...."
                jump n_confession_choice



label n_confession_choice:

show natsuki 4n
$ renpy.pause(delay=0.8, hard=True)
show natsuki 4u
$ renpy.pause(delay=0.8, hard=True)
show natsuki 1n
$ renpy.pause(delay=0.8, hard=True)
show natsuki 1s
$ renpy.pause(delay=0.8, hard=True)
show natsuki 1r
$ renpy.pause(delay=0.8, hard=True)
show natsuki 1v at h11 zorder 1
n "I LOVE YOU, OKAY?!?!"
n "MORE THAN ANYTHING ELSE IN THE WORLD!!!!"
show natsuki 1p
"Natsuki looks at me as if she couldn't believe the words that just came out of her mouth..."
show natsuki 1u
"But at the same time, she looks as if the world has been lifted from her shoulders."
show natsuki 1n
"Natsuki looks at me, her eyes filled with uncertainty, as she awaits with bated breath for my answer."
"I'm really touched by her confession..."
"I never realized how much of an impact I've had on Natsuki since I first joined..."
"And truthfully...{w=0.38}part of me likes her back..."

if encore_sayoriquestion_1 == True:
    "But...{w=0.38}should I really trash my relationship with Sayori?"
    "Am I still happy being with her?"

if encore_sayoriquestion_1 == False:
    "I'm not completely sure what to do here..."
    "Is there even a right answer?!?"

    if hangout1 == "Sayori" and hangout2 == "Sayori":
        "What would Sayori say after I've spent so much time around her?"
        "I'd hate to break her heart again..."
        jump dialogue_cont1

    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
        "I've spent so much time around Natsuki..."
        "Isn't this what I've always wanted?"
        jump dialogue_cont1

    if hangout1 == "Monika" and hangout2 == "Monika":
        "What would Monika say after I've spent so much time around her?"
        "She was always the girl I thought I could never get, and I have a really good chance of getting with her now..."
        jump dialogue_cont1

    if hangout1 == "Yuri" and hangout2 == "Yuri":
        "What would Yuri say after I've spent so much time around her?"
        "She'd likely never trust me or any other guy ever again..."
        jump dialogue_cont1

    else:
        "I've been feeling divided between [hangout1] and [hangout2] lately..."
        "Even now more so since I spent yesterday with [hangout3]..."
        jump dialogue_cont1


label dialogue_cont1:

"There's so many different reasonings..."
"And either way, I'm kicking up some sort of storm regardless of how I answer this..."
"But, Natsuki deserves an answer...."
"Do I really love her back?"
"As my thought process kicks into overdrive, I look back and forth between the ground and Natsuki's eyes as I try to settle on a decision."
"Natsuki, clearly sensing that I'm in deep thought, offers her hands to me."
"I let out a deep breath and gently take them, I immediately realize how soft and petite they are..."
"Natsuki still has the same expression on her face, bracing for whatever I say next."
"This almost feels like when Sayori confessed to me..."
"But, this is different now..."
"And, I'm determined to make it so..."
"..."
"I look deep into Natsuki's eyes as I finally articulate my answer."


menu:
    mc "Natsuki..."
    "I love you too.":
        $ n_love = True
        jump n_accept
    "I just want to be friends.":
        $ n_love = False
        jump n_denied

label n_accept:

mc "I love you too."
n 1m "You...{w=0.38}you really mean that?"
show natsuki 1n
mc "Of course I do!"
mc "To be honest, I've had my eye on you for a while now too..."
mc "I just really didn't know if I should've acted on it..."
mc "I know we can't go back in time to spend more time together, but we can start spending more time with each other regularly from this point on!"
mc "And...{w=0.38}I intend to be the best I possibly can for you..."
mc "I promise I'll treat you right...{w=0.38}you deserve the best..."
show natsuki 1c
"Natsuki looks on at me in shock."
"It's as if she wasn't expecting me to say yes to her..."
show natsuki 1q
"She tries to respond but nothing comes out of her."
show natsuki 1j
"Simply, she gives me a gracious smile, and I return the favor with my own."
n 1t "You've...{w=0.38}made me really happy....{w=0.38}you dummy!"
mc "Ha! Well I guess that's my full-time job now, isn't it?"
stop music fadeout 2.0
n 1l "This...{w=0.38}this the best moment of my life!"
n 1z "I gotta tell everyone!"
show natsuki at lhide
hide natsuki
mc "Natsuki, wait!"
"Natsuki happily runs back into the clubroom before I get the chance to finish."
"I slump back against the wall as the full weight of what I've just done comes crashing down on me."
"I instantly regret this decision."

if encore_sayoriquestion_1 == True:
    "Sayori..."
    "I never even gave her the chance to tell her how I was feeling..."
    "Why...{w=0.38}why did I do that!?!?"
    "How could do that to her?!?!?"

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                "After everything we've been through!!!"
                "We were doing so well..."
                "There was no reason!"
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                "We've spent so much time together..."
                "And I just blew it all up...."
                "And for what?"
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                "I know I messed up by getting too close to [hangout2] on Tuesday..."
                "But we got past that..."
                "She forgave me..."
                "And there's no way Sayori can forgive me for this..."
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                "We've spent so much time together..."
                "And I just blew it all up...."
                "And for what?"
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                "I know I haven't been good to Sayori lately..."
                "But I promised her yesterday things would be different..."
                "Instead, I just ended up back where I was..."
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                "I've treated Sayori so badly these past two days..."
                "First I got too close to [hangout2]..."
                "Then yesterday with [hangout3]..."
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                "Ive tried being as loyal to her as possible..."
                "I even spent Tuesday with her..."
                "But my feelings for the others just got in the way..."
                jump day4_pity


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                "I've been treating Sayori awfully..."
                "After she gave me her trust..."
                "At every opportunity, I've crushed it."
                "I've hardly spent any time around her..."
                "All because my feelings for the others re-surfaced..."
                jump day4_pity



if encore_sayoriquestion_1 == False:
    "I wasn't ready for this..."
    "I didn't think it would be this sudden..."
    "I wanted to sort things out with Sayori first..."
    "And made sure that the others were completely okay..."

    if hangout1 == "Sayori" and hangout2 == "Sayori":
            "Sayori's going to be completely heartbroken..."
            "She's going to think I've been leading her on..."

            if hangout3 == "Sayori":
                "Especially since I told her that I wanted to help..."
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got..."
                "I'm in deep shit with both of them now..."
                jump day4_pity



    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
            "But, isn't this what I wanted?"
            "Didn't I want to be with Natsuki?"
            "I should've at least told [hangout3] about this first..."
            "She's going to hate me..."
            jump day4_pity


    if hangout1 == "Monika" and hangout2 == "Monika":
            "Monika's going to be completely pissed, and rightfully so..."
            "How we've finally started talking and with how close we've gotten..."

            if hangout3 == "Monika":
                "She's been so thoughtful and kind to me throughout this ordeal..."
                "And I do this to her?!? Someone as great as Monika?!?!"
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got too..."
                "I'm in deep shit with both of them now..."
                jump day4_pity


    if hangout1 == "Yuri" and hangout2 == "Yuri":
            "Yuri's going to have a total meltdown..."
            "She's probably going to leave the club too because of me..."

            if hangout3 == "Yuri":
                "Especially with how much interest I've showed in her these past few days..."
                "She's probably never going to trust anyone ever again because how I lead her on..."
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got too..."
                "I'm in deep shit with both of them now..."
                jump day4_pity


    else:
        "I should've just stuck to seeing one person..."
        "Everyone's going to be pissed at me once they figure out how I've been getting close to all of them..."

    "I've practically ruined my friendship with everyone..."

label day4_pity:

"What's wrong with me?!?!"
"My train of thought is interrupted as I hear screaming from inside the clubroom."
"Oh no..."
"Part of me wants to simply walk away and never come back to that room."
"I know I fucked up."
"I don't think I can show them my face ever again..."
"But this is my mess..."
"And...{w=0.38}I have to fix it somehow..."
"I stand up, and reluctantly open the door."
play sound "sfx/closet-open.ogg"
jump day4_chaos

label n_denied:

mc "I just want to be friends."
n 1m "Eh? What?"
show natsuki 1n
"Natsuki takes a step back, releasing her hands from my grip as she tries to come to terms with what I just said."
show natsuki 12a
mc "I get that this is hard to hear..."
show natsuki 12b
mc "But look, I think it's just better if we stay as friends for right now..."
show natsuki 12d
mc "I'd love to spend more time with you too, honest!"
mc "Truthfully, I don't think we spend enough time with each other..."
mc "And I know I can't go back in time for us to hangout more, but going forward, I'd love to spend more time with you on a regular basis..."
show natsuki 12f
mc "I just...{w=0.38}don't think I like you back in the same way you do..."
mc "I'm sorry..."
stop music fadeout 2.0
"Tears are strolling down Natsuki's face as she sniffles and shakes in anger."
show natsuki 12h
"After about a solid minute, she finally opens her teary eyes."
n 12i "N-{w=0.38}no..."
show natsuki 12h
mc "What?"
n 12i "I pour my heart out to you..."

if encore_festivalquestion_2 == "Natsuki":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            n 12h "After everything we've been through..."

    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            n 12h "After spending time with me, to avoiding me to then walking back to me..."

    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            n 12h "After leading me on and then avoiding me..."

    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            n 12h "After just showing a little bit of interest in me..."


if encore_festivalquestion_2 == "Yuri":

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            n 12h "After showing so much sudden interest in me..."

    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            n 12h "After letting me hug you that way..."

    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            n 12h "After showing a little bit of interest..."


    if hangout1 != "Natsuki":
        if hangout2 != "Natsuki":
            n 12h "I tell you how I finally feel..."

n 12i "That all you tell me...{w=0.38}is that you want to be friends?"
show natsuki 12h
mc "Yes...{w=0.38}I'm sorry, Natsuki..."
n 12b "I made a mistake..."
mc "No, you didn't..."
show natsuki 12a
mc "Natsuki, you're a great person, and you're attractive in your own way..."
mc "I'm not turning you down because I don't like you..."

if encore_sayoriquestion_1 == True:
    show natsuki 1p
    mc "But, I'm committed to Sayori..."

if encore_sayoriquestion_1 == False:
    show natsuki 1p
    mc "It's just that I have my eyes on someone else right now..."


show natsuki 1v at h11 zorder 1
n "FUCK YOU!"
play sound "sfx/slap.ogg"
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0

"Without warning, Natsuki slaps me so hard that I end up stumbling into the wall."
show natsuki 12f
show natsuki at lhide
hide natsuki
"Before I could even respond, Natsuki runs back into the clubroom, sobbing loudly."
"I do my best to nurse my throbbing cheek as I sit myself up and try to make sense of what just happened."

if encore_sayoriquestion_1 == True:
    "I hate that it had to play out like that..."
    "But...{w=0.38}I think I made the right decision for my relationship with Sayori..."
    "It might not exactly be 100\% perfect..."
    "But, I owe it to her to give her everything I got..."
    "I promised her as much..."

if encore_sayoriquestion_1 == False:
    "I wish it didn't have to play out like this..."
    "To a degree, I like Natsuki the same way..."

    if hangout1 == "Sayori" and hangout2 == "Sayori":
            "But, I'm still conflicted on who I like more..."
            "I've been re-thinking my decision to turn down Sayori..."

            if hangout3 == "Sayori":
                "And I'm really starting to lean towards talking that over with her..."
                jump day4_brace

            else:
                "Between Sayori and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace


    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
            "But I don't know if I'm ready to begin a relationship with her..."

            if hangout3 == "Sayori":
                "Especially since I need to smooth things over with Sayori..."
                jump day4_brace

            else:
                "Especially since I need to smooth things over with Sayori and [hangout3]..."


    if hangout1 == "Monika" and hangout2 == "Monika":
            "But, I have a serious chance of getting with Monika..."
            "I don't think I should pass up that opportunity quite yet..."


            if hangout3 == "Monika":
                "We've gotten so far..."
                jump day4_brace

            else:
                "Between Monika and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace


    if hangout1 == "Yuri" and hangout2 == "Yuri":
            "But, I have a great opportunity with Yuri..."
            "After how long it took for her to open up to me, I have to admit I'm interested in her..."

            if hangout3 == "Yuri":
                "And with what I saw on her arms yesterday..."
                jump day4_brace

            else:
                "Between Yuri and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace

    else:
        "But, I need to completely settle on someone first..."

label day4_brace:

"My train of thought is interrupted as I hear screaming from inside the clubroom."
"Oh no..."
"Part of me wants to simply walk away and never come back to that room."
"This is exactly what I wanted to avoid..."
"But I asked for this..."
"So...{w=0.38}I have to fix it somehow..."
"I stand up, and reluctantly open the door."
play sound "sfx/closet-open.ogg"
jump day4_chaos



label y_confession:

show yuri 4c at t11 zorder 1
"Yuri and I are standing in the middle of the hallway, with not a single person in sight."
"The air is becoming increasingly fraught with tension as we both struggle to maintain eye contact."
"A pit forms in my stomach as I brace for what I always thought to be the inevitable..."
"Fortunately, it seems Yuri's just as nervous about this as I am..."
show yuri 4a
"Part of me hopes that this entire thing is some sort of joke or it was complete misunderstanding..."
"Maybe she's going to ask me about something else? Am I just overthinking things again?"
show yuri 4b
"But, given how she's been acting lately, it makes either of those options increasingly unlikely, especially since it seems Yuri's putting more thought into speaking than normal..."
"As I wait for a few more seconds, I feel that a part of me wants Yuri to confess her love."
"I've always been attracted to her to a degree..."
"And if this is what I think it's about, then this would be the perfect opportunity to explore something that could always still be..."
"I finally grow tired of waiting and decide to start the conversation."
mc "So...{w=0.38}what did you want to talk about?"
y 3q "Well truthfully, I think we both know why I asked you to come out here..."
mc "Eh, not really..."
y 3v "Well, first thing's first..."
y 1t "I'd...{w=0.38}like the take the time to apologize for behaving so rudely to you yesterday..."
y 1w "I didn't mean to cause a scene..."
show yuri 1u
mc "Ah...{w=0.38}it's fine Yuri, I'm not angry with you over it..."
y 3q "Well that's a relief..."
mc "But, that's not what you wanted to talk about..."
y 3t "No, no it isn't..."
y 3q "Forgive me, but I've had this on my chest for quite a while now..."
mc "It's alright, take your time..."
show yuri 3w
$ renpy.pause(delay=0.8, hard=True)
show yuri 1m
$ renpy.pause(delay=0.8, hard=True)
y 1s "Alright..."
play music e20 fadein 1.0
y 1t "[player]..."
y 1u "Over the course of my life, there's been very few individuals that have really accepted me for who I am as a person..."
y 1v "Not too many guys have ever made me feel truly welcomed...{w=0.38}at least not without an ulterior motive..."
y 3t "Before I joined the Literature Club, I hardly felt comfortable in my own skin..."
y 4b "I don't often see the redeeming qualities in myself..."
y 4a "Truthfully, I don't always believe the compliments that people give me..."
y 4c "Mostly because of who I am, I still struggle with this..."
y 3u "Simply put, it takes a lot for me to feel...{w=0.38}attracted to someone..."
y 1t "But, with you, you've made me feel...{w=0.38}different..."
y 3n "In a good way!"
y 3o "Uuu! I've already messed this up!"
show yuri 3n
mc "Yuri, it's fine, really..."
show yuri 3q
mc "You know I'm always willing to hear you out..."
show yuri 3l
"Yuri takes a shaky breath before resuming her speech..."
y 1s "That's what I admire about you, [player]..."
y 1u "You haven't been like other guys I've had interactions with..."

if encore_sayoriquestion_1 == True:


    if encore_festivalquestion_2 == "Natsuki":
        y 3t "Even though we've had limited interaction since you've joined...{w=0.38}you've always managed to make a positive impact on me..."
        y 3u "I know I don't always tend to 'stand out' from the rest of the crowd..."
        y 3v "I always try to make myself as invisible as possible..."
        y 3w "And it makes sense why you chose to spend time with Sayori over me..."
        y 3u "She was always the most outgoing out of all of us, even before you joined..."
        y 3s "And in retrospect, I understand why you wanted to spend time with Natsuki for the festival preparations too!"
        y 1u "She never had a problem standing out and grabbing people's attention..."
        y 1v "She was always confident in herself..."


        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                y 3t "But despite all this...{w=0.38}you actually managed to take the time to check on me..."
                y 4e "To see how I was doing..."
                y "It was a very kind gesture and I appreciated it, I don't get that very often from others..."
                y 2v "I was worried that I'd bore you during our conversations or you'd find some reason to talk to me..."
                y 2s "But, I never did. You were always engaged and respectful of me..."
                y 4c "Overtime, I've started to enjoy our company..."
                y "I've always wanted for us to spend time together, and I finally got to experience what I was missing out on..."
                y "I even wrote some poems about our time together, even if it was brief..."
                y "It pretty much evolved into something romantic..."
                y "Especially how we were on Tuesday..."
                y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice


        if hangout1 != "Yuri":
            if hangout2 == "Yuri":
                y 3t "And I was worried because I isolated myself so much, that we'd never get the chance to actually befriend one another..."
                y 4e "But...{w=0.38}you proved me wrong..."
                y 2v "That Tuesday, we actually got to spend some time together for once..."
                y 3c "And it was such a blissful experience!"
                y 3q "I may have let my emotions get the best of me on that day..."
                y 1s "But, you didn't really seem to mind..."
                y 1u "That moment did help cement my feelings for you..."
                y 4e "To be totally honest, I've had my eye on you since we first joined..."
                y "How you've brought a smile to all our faces..."
                y "Always being kind..."
                y "And I always did find you to be attractive..."
                y "I began writing poems to get a better understanding of my feelings..."
                y "But, it pretty much evolved into something romantic..."
                y "Especially with how we were on Tuesday..."
                y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice


        if hangout1 == "Yuri":
            if hangout2 != "Yuri":
                y 3t "And I was worried because I isolated myself so much, that we'd never get the chance to actually befriend one another..."
                y 4e "But...{w=0.38}you proved me wrong..."
                y 2v "That Tuesday, we actually got to spend some time together for once..."
                y 3c "And it was such a blissful experience!"
                y 3s "Even if we didn't get to spend as much time as we were hoping for...{w=0.38}I still appreciated it!"
                y 1v "Though I began to worry if that was going to be our only chance to hangout..."
                y "Especially since with what happened between you and [hangout2] on Tuesday..."
                y 3w "I was honestly starting to wonder by that point if it was too late, and I'd never get the chance to tell you how I felt..."
                y 1t "As for quite some time now, I've been interested in you..."
                y 4e "You've always brought a smile to our faces..."
                y "You've always been kind..."
                y "And I always did find you to be attractive..."
                y "So, I decided to start writing poems to get a better understanding of my feelings..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice




    if encore_festivalquestion_2 == "Yuri":
            y 3t "Even though we've had limited interaction since you've joined...{w=0.38}you've always managed to make a positive impact on me..."
            y 3u "I know I don't always tend to 'stand out' from the rest of the crowd..."
            y 3v "I always try to make myself as invisible as possible..."
            y 3w "And it makes sense why you chose to spend time with Sayori over me..."
            y 3u "She was always the most outgoing out of all of us, even before you joined..."
            y 3t "But, I was very surprised when you chose me for the festival preparations..."
            y 2u "I was shocked at first, but I was really grateful that you did..."


    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            y 3t "And since that Sunday, I've really enjoyed the opportunity to grow closer to you..."
            y 3u "I was worried that after the festival we would stop talking..."
            y 1s "But, thankfully those fears never came to pass..."
            y 4e "You still came back to me..."
            y "And I finally got to experience what I've been missing out on..."
            y 1t "To be completely honest, for quite some time now, I've been interested in you..."
            y 4e "You've always brought a smile to our faces..."
            y "You've always been kind..."
            y "And I always did find you to be attractive..."
            y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
            y 2v "I was so worried that I'd screw up. I never wanted to scare you off or bore you..."
            y 2s "But, as it turns out, I never did. You were always engaged and respectful of me..."
            y 2u "I actually decided to write some poems to explore my feelings towards you..."
            y "It pretty much evolved into something romantic..."
            y "Especially how we were on Tuesday..."
            y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
            y 3u "It was from there that I realized that I had serious feelings for you..."
            y 3s "I thought that we had the potential for us to be something serious..."
            y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
            y 3q "I assumed you read it, given how you've been acting around me lately..."
            y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
            jump y_confession_choice


    if hangout1 != "Yuri":
        if hangout2 == "Yuri":
            y 3w "But...{w=0.38}I began to worry if what we experienced on Sunday and during the festival was merely another fleeting moment in my life..."
            y 3v "I was yearning for the next chance to be with you..."
            y 3w "Wondering if we could build upon our relationship..."
            y 4e "And to potentially be something more than just friends..."
            y 1t "To be completely honest, for quite some time now, I've been interested in you..."
            y 4e "You've always brought a smile to our faces..."
            y "You've always been kind..."
            y "And I always did find you to be attractive..."
            y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
            y "And when I was with you on Tuesday..."
            y "I couldn't help but explore what I've been feeling for sometime by that point..."
            y 2u "I actually decided to write some poems a while ago to explore my feelings towards you..."
            y "It pretty much evolved into something romantic..."
            y "Especially how we were on Tuesday..."
            y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
            y 3u "It was from there that I decided that I needed to act on my feelings..."
            y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
            y 3q "I assumed you read it, given how you've been acting around me lately..."
            y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
            jump y_confession_choice


    if hangout1 == "Yuri":
        if hangout2 != "Yuri":
            y 3w "Still, part of me wondered if this was going to be just my only chance to get closer to you..."
            y 3s "And while I'm grateful for the time we spent preparing for and at the festival, I wanted to be around you more..."
            y 1t "For quite sometime, I've been interested in you..."
            y 4e "You've always brought a smile to our faces..."
            y "You've always been kind..."
            y "And I always did find you to be attractive..."
            y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
            y "And I enjoyed every single second!"
            y 3s "I was so overjoyed when you came to see me on Monday, even if we didn't get to spend the amount of time we wanted..."
            y 1v "Though I began to worry if that was going to be our only chance to hangout afterwards..."
            y "Seeing you and [hangout2] on Tuesday...{w=0.38}left me with a sore spot..."
            y 3w "I starting to worry by that point if I was too late, and I'd never get the chance to tell you how I felt..."
            y 3u "Even before that moment, I was writing poems to get a better understanding of my feelings..."
            y 3u "It was from there that I realized that I had serious feelings for you..."
            y 3s "I thought that we had the potential for us to be something serious..."
            y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
            y 3q "I assumed you read it, given how you've been acting around me lately..."
            y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
            jump y_confession_choice



    if hangout1 != "Yuri":
        if hangout2 != "Yuri":
            y 3w "But, I couldn't help but worry if that was going to be our only chance to spend time together..."
            y 3u "Even though we only spent a brief amount of time around each other, I really began to miss you..."
            y 4c "Seeing you with the others...{w=0.38}especially with [hangout2] on Tuesday, felt like the norm in the literature club was returning..."
            y 3r "And I didn't want that!"
            y 1v "As much as I've generally isolated myself in the club, I began to realize how it was affecting my chances of finding someone..."
            y 1t "And very few have showed me the same level of kindness you have given me..."
            y 4c "I didn't want what we experienced on that Sunday and during the festival to just be another fleeting moment in my life..."
            y "So, I turned to poetry to help map out my feelings and try to decide what I should do next."
            y 3u "It was from there that I realized that I had serious feelings for you..."
            y 3s "I thought that we had the potential for us to be something serious..."
            y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
            y 3q "I assumed you read it, given how you've been acting around me lately..."
            y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
            jump y_confession_choice



if encore_sayoriquestion_1 == False:


    if encore_festivalquestion_2 == "Natsuki":
        y 3t "Even though we've had limited interaction since you've joined...{w=0.38}you've always managed to make a positive impact on me..."
        y 3u "I know I don't always tend to 'stand out' from the rest of the crowd..."
        y 3v "I always try to make myself as invisible as possible..."
        y 3w "And it makes sense why you chose to spend time with Natsuki over me..."
        y 3u "She was always the most outspoken out of all of us, even before you joined..."
        y 3s "And in retrospect, I understand why you wanted to spend time with Natsuki for the festival preparations too!"
        y 1u "She never had a problem standing out and grabbing people's attention..."
        y 1v "And when she wants to, she really is a fun person to spend time with..."

        if hangout1 == "Yuri":
            if hangout2 = "Yuri":
                y 3t "But despite all this...{w=0.38}you actually managed to take the time to check on me..."
                y 4e "To see how I was doing..."
                y "It was a very kind gesture and I appreciated it, I don't get that very often from others..."
                y 2v "I was worried that I'd bore you during our conversations or you'd find some reason to talk to me..."
                y 2s "But, I never did. You were always engaged and respectful of me..."
                y 4c "Overtime, I've started to enjoy our company..."
                y "I've always wanted for us to spend time together, and I finally got to experience what I was missing out on..."
                y "I even wrote some poems about our time together, even if it was brief..."
                y "It pretty much evolved into something romantic..."
                y "Especially how we were on Tuesday..."
                y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice



        if hangout1 == "Yuri":
            if hangout2 != "Yuri":
                y 3w "Still, part of me wondered if this was going to be just my only chance to get closer to you..."
                y 3s "And while I'm grateful for the time we spent preparing for and at the festival, I wanted to be around you more..."
                y 1t "For quite sometime, I've been interested in you..."
                y 4e "You've always brought a smile to our faces..."
                y "You've always been kind..."
                y "And I always did find you to be attractive..."
                y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
                y "And I enjoyed every single second!"
                y 3s "I was so overjoyed when you came to see me on Monday, even if we didn't get to spend the amount of time we wanted..."
                y 1v "Though I began to worry if that was going to be our only chance to hangout afterwards..."
                y "Seeing you and [hangout2] on Tuesday...{w=0.38}left me with a sore spot..."
                y 3w "I starting to worry by that point if I was too late, and I'd never get the chance to tell you how I felt..."
                y 3u "Even before that moment, I was writing poems to get a better understanding of my feelings..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice




        if hangout1 != "Yuri":
            if hangout2 == "Yuri":
                y 3t "I was worried because I isolated myself too much...{w=0.38}so much to the point that we'd never get the chance to actually befriend one another..."
                y 4e "But...{w=0.38}you proved me wrong..."
                y 2v "That Tuesday, we actually got to spend some time together for once..."
                y 3c "And it was such a blissful experience!"
                y 3q "I may have let my emotions get the best of me on that day..."
                y 1s "But, you didn't really seem to mind..."
                y 1u "That moment did help cement my feelings for you..."
                y 4e "To be totally honest, I've had my eye on you since we first joined..."
                y "How you've brought a smile to all our faces..."
                y "Always being kind..."
                y "And I always did find you to be attractive..."
                y "I began writing poems to get a better understanding of my feelings..."
                y "But, it pretty much evolved into something romantic..."
                y "Especially with how we were on Tuesday..."
                y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice



        if hangout1 != "Yuri":
            if hangout2 != "Yuri":
                y 3w "But, I couldn't help but worry if we were ever going to spend some quality time together..."
                y 3u "We've only merely had conversations, and I wanted more..."
                y 4c "Seeing you with the others...{w=0.38}especially with [hangout2] on Tuesday, it felt like the norm in the literature club..."
                y 3r "And I didn't want it anymore!"
                y 1v "As much as I've generally isolated myself in the club, I began to realize how it was affecting my chances of finding someone..."
                y 1t "And very few have showed me the same level of kindness you have given me, even if it was brief..."
                y 4e "To be totally honest with you, I've had my eye on you since we first joined..."
                y "How you've brought a smile to all our faces..."
                y "Always being kind..."
                y "And I always did find you to be attractive..."
                y "I turned to poetry to help grasp a better understanding of my feelings..."
                y "But, it pretty much evolved into something romantic..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that it was worth trying to get something to happen between us..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice




    if encore_festivalquestion_2 == "Yuri":
        y 3t "Ever since you've joined, you've been nothing but patient, kind and thoughtful to me..."
        y 3u "I know I don't always tend to 'stand out' from the rest of the crowd..."
        y 3v "I always try to make myself as invisible as possible..."
        y 3t "The fact that you chose to spend so much of your time around me and not the others is still something I still can't quite believe..."
        y 1s "But, I'm still grateful nonetheless..."
        y 1u "I've enjoyed every single second I've been around you..."
        y 1t "From reading together..."
        y 2u "To the festival preparations and the festival itself..."
        y 3s "To even now at this very moment..."



        if hangout1 == "Yuri":
            if hangout2 == "Yuri":
                y 3t "I've truly enjoyed the opportunity to grow closer to you..."
                y 3u "I was worried that after the festival we would stop talking..."
                y 1s "But, thankfully those fears never came to pass..."
                y 4e "You still came back to me..."
                y "And I finally got to experience what I've been missing out on for so long..."
                y 1t "To be completely honest, for quite some time now, I've been interested in you..."
                y 4e "You've always brought a smile to our faces..."
                y "You've always been kind..."
                y "And I always did find you to be attractive..."
                y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
                y 2v "I was so worried that I'd screw up. I never wanted to scare you off or bore you..."
                y 2s "But, as it turns out, I never did. You were always engaged and respectful of me..."
                y 2u "I actually decided to write some poems to explore my feelings towards you..."
                y "It pretty much evolved into something romantic..."
                y "Especially how we were before..."
                y 3s "I was worried that I was being too forward on Tuesday..."
                y 3v "I didn't know if you still felt the same way about me after Sunday..."
                y 3s "But I sensed you had similar feelings as well..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice





        if hangout1 != "Yuri":
            if hangout2 == "Yuri":
                y 3w "But...{w=0.38}I began to worry if everything we experienced were going to be more fleeting moments in my life..."
                y 3v "I was yearning for the next chance to be with you..."
                y 3w "Wondering if we could build upon our relationship..."
                y 4e "And to potentially be something more than just friends..."
                y 1t "To be completely honest, for quite some time now, I've been interested in you..."
                y 4e "You've always brought a smile to our faces..."
                y "You've always been kind..."
                y "And I always did find you to be attractive..."
                y "Being able to be in your very presence was...{w=0.38}intoxicating..."
                y "And when I was with you on Tuesday..."
                y "I couldn't help but explore what I've been feeling for sometime by that point..."
                y 2u "I actually decided to write some poems a while ago to explore my feelings towards you..."
                y "It pretty much evolved into something romantic..."
                y "Especially how we were on Tuesday..."
                y 3s "I was worried that I was being too forward at the time, but I sensed you had similar feelings as well..."
                y 3u "It was from there that I decided that I needed to act on my feelings..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice



        if hangout1 == "Yuri":
            if hangout2 != "Yuri":
                y 3w "Still, part of me wondered if that was just going to be it for us..."
                y "I wasn't sure what the next step for us was going to be..."
                y 3s "I just knew that I wanted to be around you more..."
                y 1t "Truthfully, for quite some time now, I've been interested in you..."
                y 4e "You've always brought a smile to our faces..."
                y "You've always been kind..."
                y "And I always did find you to be attractive..."
                y "Being able to finally spend time around you was so...{w=0.38}intoxicating..."
                y "And I enjoyed every single second!"
                y 3s "I was so overjoyed when you came to see me on Monday, even if we didn't get to spend the amount of time we wanted..."
                y 1v "Though I began to worry if that was going to be our only chance to hangout afterwards..."
                y "Seeing you and [hangout2] on Tuesday...{w=0.38}left me with a sore spot..."
                y 3w "I starting to worry by that point if I was too late, and I'd never get the chance to tell you how I felt..."
                y 3u "Even before that moment, I was writing poems to get a better understanding of my feelings..."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice



        if hangout1 != "Yuri":
            if hangout2 != "Yuri":
                y 3w "However, I was starting to worry if we were ever going to make more progress in our relationship with each other..."
                y 3u "With how close we've gotten, it truly felt as if fate was calling me to you..."
                y 3s "Being around you just felt so right..."
                y 3u "It felt so intoxicating!"
                y 3t "And...{w=0.38}I wanted to spend more time with you!"
                y 3e "Truthfully, I've been interested in you since you first joined..."
                y "Seeing how you were so nice, handsome, and had a good taste in literature!"
                y "I truly looked forward to the club every day since we've started talking..."
                y 3q "But, lately, for whatever reason, we just haven't gotten the chance to be around each other..."
                y 3w "You've been off spending time with the others..."
                y "And while I don't fault you for that.."
                y 3q "Seeing you with [hangout2]...{w=0.38}really hurt me inside..."
                y 3w "I started to worry if I had missed my chance to try to forge a lasting relationship with you..."
                y "Or that you've moved on from me..."
                y 4c "I didn't want what we experienced on that Sunday and during the festival to just be another fleeting moment in my life..."
                y "Ever since I've had my eye on you, I've turned to poetry to help map out my feelings and try to decide what I should do next."
                y 3u "It was from there that I realized that I had serious feelings for you..."
                y 3s "I thought that we had the potential for us to be something serious..."
                y 1t "Though I didn't possess the courage at the time to tell you directly how I felt, I resolved to give you my confession letter instead."
                y 3q "I assumed you read it, given how you've been acting around me lately..."
                y 1s "But, now that you're here, I believe I finally have the courage to say what I've been meaning to tell you..."
                jump y_confession_choice





label y_confession_choice:

y 3q "I..."
show yuri 3o
$ renpy.pause(delay=0.8, hard=True)
show yuri 3k
$ renpy.pause(delay=0.8, hard=True)
show yuri 1m
$ renpy.pause(delay=0.8, hard=True)
show yuri 1s
$ renpy.pause(delay=0.8, hard=True)
y 3t "I...{w=0.38}love you..."
y 3s "I want to make you as happy as possible..."
y 3u "I want to return the favor for everything you've done for me."
y 1v "I don't know what I did to deserve your kindness..."
y 3s "But, I would be honored to make our relationship that much more special by making things between us official..."
y 3q "I...{w=0.38}I know I've rambled on for quite a while now, but you just mean so much to me..."
y "And I really couldn't find a good way to condense everything..."
y 3s "So, that's how I feel about you..."
"Yuri looks on at me, her eyes glinting with hopeful optimism as she awaits for my response."
"I'm really touched by her confession..."
"I never realized how much of an impact I've had on Yuri since I first joined..."
"And truthfully...{w=0.38}part of me likes her back..."


if encore_sayoriquestion_1 == True:
    "But...{w=0.38}should I really trash my relationship with Sayori?"
    "Am I still happy being with her?"

if encore_sayoriquestion_1 == False:
    "I'm not completely sure what to do here..."
    "Is there even a right answer?!?"

    if hangout1 == "Sayori" and hangout2 == "Sayori":
            "What would Sayori say after I've spent so much time around her?"
            "I'd hate to break her heart again..."
            jump dialogue_cont2

    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
            "What would Yuri say after I've spent so much time around her?"
            "She'd probably kill me..."
            jump dialogue_cont2

    if hangout1 == "Monika" and hangout2 == "Monika":
            "What would Monika say after I've spent so much time around her?"
            "She was always the girl I thought I could never get, and I have a really good chance of getting with her now..."
            jump dialogue_cont2

    if hangout1 == "Yuri" and hangout2 == "Yuri":
            "I've spent so much time around Yuri..."
            "Isn't this what I've always wanted?"
            jump dialogue_cont2

    else:
        "I've been feeling divided between [hangout1] and [hangout2] lately..."
        "Even now more so since I spent yesterday with [hangout3]..."
        jump dialogue_cont2


label dialogue_cont2:

"There's so many different reasonings..."
"And either way, I'm kicking up some sort of storm regardless of how I answer this..."
"But, Yuri deserves an answer...."
"Do I really love her back?"
"As my thought process kicks into overdrive, I look back and forth between the ground and Yuri's eyes as I try to settle on a decision."
show yuri 1u
"Yuri, clearly sensing that I'm in deep thought, averts her eyes in an effort to make me feel more comfortable."
"But, I still feel the anxiety swelling inside me..."
"It felt like the exact same pressure when Sayori confessed to me..."
"While the circumstances aren't quite the same, there's a few parallels here..."
"All I know is that things are different now..."
"And, I'm going to make it so..."
"..."
show yuri 1s
"I look deep into Yuri's eyes as I finally articulate my answer."


menu:
    mc "Yuri..."
    "I love you too.":
        $ y_love = True
        jump y_accept
    "I just want to be friends.":
        $ y_love = False
        jump y_denied


label y_accept:

mc "I love you too."
y 3t "You...{w=0.38}you really mean that?"
show yuri 3s
mc "Of course I do!"
mc "To be honest, I've had my eye on you for a while now too..."
mc "I just really didn't know if I should've acted on it..."
mc "I know we can't go back in time to spend more time together, but we can start spending more time with each other regularly from this point on!"
mc "And...{w=0.38}I intend to be the best I possibly can for you..."
mc "I promise I'll treat you right...{w=0.38}you deserve the best..."
show yuri 3c
"Yuri begins to blush as she gives me the biggest smile I've ever seen from her."
show yuri 3l
"She then lets out a big sigh of relief, exhaling all the pressure and stress I've inadvertently caused her over the last two weeks."
show yuri 3s
"Yuri looks back at me, looking far more relaxed."
y 1j "Well...{w=0.38}I'm glad that's now over with..."
y 3d "I still can't believe this is actually happening!"
show yuri 3c
mc "Yeah...{w=0.38}me neither..."
show yuri 1a
mc "This is what it feels like making things official, huh?"
stop music fadeout 2.0
y 1s "You've...{w=0.38}made this the best moment of my life!"
y 1c "We need to tell everyone the good news!"
show yuri at lhide
hide yuri
mc "Yuri, wait!"
"Yuri happily runs back into the clubroom before I get the chance to finish."
"I slump back against the wall as the full weight of what I've just done comes crashing down on me."
"I instantly regret this decision."

if encore_sayoriquestion_1 == True:
    "Sayori..."
    "I never even gave her the chance to tell her how I was feeling..."
    "Why...{w=0.38}why did I do that!?!?"
    "How could do that to her?!?!?"

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                "After everything we've been through!!!"
                "We were doing so well..."
                "There was no reason!"
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                "We've spent so much time together..."
                "And I just blew it all up...."
                "And for what?"
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                "I know I messed up by getting too close to [hangout2] on Tuesday..."
                "But we got past that..."
                "She forgave me..."
                "And there's no way Sayori can forgive me for this..."
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                "We've spent so much time together..."
                "And I just blew it all up...."
                "And for what?"
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                "I know I haven't been good to Sayori lately..."
                "But I promised her yesterday things would be different..."
                "Instead, I just ended up back where I was..."
                jump day4_pity

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                "I've treated Sayori so badly these past two days..."
                "First I got too close to [hangout2]..."
                "Then yesterday with [hangout3]..."
                jump day4_pity

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                "Ive tried being as loyal to her as possible..."
                "I even spent Tuesday with her..."
                "But my feelings for the others just got in the way..."
                jump day4_pity


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                "I've been treating Sayori awfully..."
                "After she gave me her trust..."
                "At every opportunity, I've crushed it."
                "I've hardly spent any time around her..."
                "All because my feelings for the others re-surfaced..."
                jump day4_pity



if encore_sayoriquestion_1 == False:
    "I wasn't ready for this..."
    "I didn't think it would be this sudden..."
    "I wanted to sort things out with Sayori first..."
    "And made sure that the others were completely okay..."

    if hangout1 == "Sayori" and hangout2 == "Sayori":
            "Sayori's going to be completely heartbroken..."
            "She's going to think I've been leading her on..."

            if hangout3 == "Sayori":
                "Especially since I told her that I wanted to help..."
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got..."
                "I'm in deep shit with both of them now..."
                jump day4_pity



    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
            "Natsuki's going to be so pissed..."
            "She's never going to trust me again!"


            if hangout3 == "Natsuki":
                "Especially with how much interest I've showed in her these past few days..."
                "She's probably never going to trust anyone ever again because how I lead her on..."
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got too..."
                "I'm in deep shit with both of them now..."
                jump day4_pity



    if hangout1 == "Monika" and hangout2 == "Monika":
            "Monika's going to be completely pissed, and rightfully so..."
            "How we've finally started talking and with how close we've gotten..."

            if hangout3 == "Monika":
                "She's been so thoughtful and kind to me throughout this ordeal..."
                "And I do this to her?!? Someone as great as Monika?!?!"
                jump day4_pity

            else:
                "I should've talked to [hangout3] as well..."
                "Considering how close we got too..."
                "I'm in deep shit with both of them now..."
                jump day4_pity


    if hangout1 == "Yuri" and hangout2 == "Yuri":
            "But, isn't this what I wanted?"
            "Didn't I want to be with Yuri?"
            "I should've at least told [hangout3] about this first..."
            "She's going to hate me..."
            jump day4_pity



    else:
        "I should've just stuck to seeing one person..."
        "Everyone's going to be pissed at me once they figure out how I've been getting close to all of them..."

    "I've practically ruined my friendship with everyone..."
    jump day4_pity


label y_denied:

mc "I just want to be friends."
y 1t "Eh? What?"
show yuri 3o
"Yuri takes a step back with a mix of emotions on her face as she attempts to process what she had just heard."
show yuri 3n
mc "I get that this is hard to hear..."
show yuri 4d
mc "But look, I think it's just better if we stay as friends for right now..."
show yuri 4c
mc "I'd love to spend more time with you too, honest!"
mc "Truthfully, I don't think we spend enough time with each other..."
mc "And I know I can't go back in time for us to hangout more, but going forward, I'd love to spend more time with you on a regular basis..."
mc "I just...{w=0.38}don't think I like you back in the same way you do..."
mc "I'm sorry..."
stop music fadeout 2.0
"Tears are strolling down Yuri's face as she sniffles and shakes in anger."
show yuri 4d
"After about a solid minute, she finally opens her teary eyes."
y "N-{w=0.38}no..."
mc "What?"
y "I pour my heart out to you..."

if encore_festivalquestion_2 == "Yuri":

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            y 4c "After everything we've been through..."

    if hangout1 != "Yuri":
        if hangout2 == "Yuri":
            y 4c "After spending time with me, to avoiding me to then walking back to me..."

    if hangout1 == "Yuri":
        if hangout2 != "Yuri":
            y 4c "After leading me on and then avoiding me..."

    if hangout1 != "Yuri":
        if hangout2 != "Yuri":
            y 4c "After just showing a little bit of interest in me..."


if encore_festivalquestion_2 == "Natsuki":

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            y 4c "After showing so much sudden interest in me..."

    if hangout1 != "Yuri":
        if hangout2 == "Yuri":
            y 4c "After letting me hug you that way..."

    if hangout1 == "Yuri":
        if hangout2 != "Yuri":
            y 4c "After showing a little bit of interest..."

    if hangout1 != "Yuri":
        if hangout2 != "Yuri":
            y 4c "I tell you how I finally feel..."




y 3r "That all you tell me...{w=0.38}is that you want to be friends?"
show yuri 3y7
mc "Yes...{w=0.38}I'm sorry, Yuri..."
y 3k "I suppose I made a mistake..."
mc "No, you didn't..."
show yuri 4b
mc "Yuri, you're a great person, and you're attractive in your own way..."
mc "I'm not turning you down because I don't like you..."

if encore_sayoriquestion_1 == True:
    show yuri 3y7
    mc "But, I'm committed to Sayori..."

if encore_sayoriquestion_1 == False:
    show yuri 3y7
    mc "It's just that I have my eyes on someone else right now..."


y 3r "Save it!"
y 3h "I spent so much time invested in you, and I got nothing."
y 3r "I should've expected this! All guys are the same!"
mc "Yuri-"
y 3y7 "Go fuck yourself!"
show y_cry1 as yuri at t11 zorder 1
"Yuri's voice cracks again as she starts sobbing."
show y_cry1 as yuri  at lhide
hide yuri
"Before I could even respond, Yuri runs back into the clubroom."

if encore_sayoriquestion_1 == True:
    "I hate that it had to play out like that..."
    "But...{w=0.38}I think I made the right decision for my relationship with Sayori..."
    "It might not exactly be 100\% perfect..."
    "But, I owe it to her to give her everything I got..."
    "I promised her as much..."

if encore_sayoriquestion_1 == False:
    "I wish it didn't have to play out like this..."
    "To a degree, I like Yuri the same way..."

    if hangout1 == "Sayori" and hangout2 == "Sayori":
            "But, I'm still conflicted on who I like more..."
            "I've been re-thinking my decision to turn down Sayori..."


            if hangout3 == "Sayori":
                "And I'm really starting to lean towards talking that over with her..."
                jump day4_brace

            else:
                "Between Sayori and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace


    if hangout1 == "Natsuki" and hangout2 == "Natsuki":
            "But, I have a great opportunity with Natsuki..."
            "After how long it took for her to open up to me, I have to admit I'm interested in her..."

            if hangout3 == "Natsuki":
                "And with what she told me about her life at home..."
                jump day4_brace

            else:
                "Between Yuri and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace

    if hangout1 == "Monika" and hangout2 == "Monika":
            "But, I have a serious chance of getting with Monika..."
            "I don't think I should pass up that opportunity quite yet..."


            if hangout3 == "Monika":
                "We've gotten so far..."
                jump day4_brace

            else:
                "Between Monika and [hangout3], I'm just not ready to decide who I like more yet..."
                jump day4_brace


    if hangout1 == "Yuri" and hangout2 == "Yuri":
            "But I don't know if I'm ready to begin a relationship with her..."

            if hangout3 == "Sayori":
                "Especially since I need to smooth things over with Sayori..."
                jump day4_brace

            else:
                "Especially since I need to smooth things over with Sayori and [hangout3]..."

    else:
        "But, I need to completely settle on someone first..."
        jump day4_brace





label day4_chaos:
scene bg club_day
with wipeleft_scene
"I burst through the clubroom doors to find everything in complete disarray."

if poem_giver == "Natsuki":
    if n_love == True:
        jump n_chaos1

if poem_giver == "Natsuki":
    if n_love == False:
        jump n_chaos2

if poem_giver == "Yuri":
    if y_love == True:
        jump y_chaos1

if poem_giver == "Yuri":
    if y_love== False:
        jump y_chaos2



label n_chaos1:

if encore_sayoriquestion_1 == True:

    show sayori 1i at t41 zorder 1
    show natsuki 4o at t42 zorder 2
    show monika 1d at t43 zorder 3
    show yuri 3o at t44 zorder 4
    "Sayori and Natsuki are in a full-blown argument as Monika and Yuri are doing their best to contain the situation."
    "What have I done..."
    s 1j "For the last time Natsuki, I'm dating him! He's not your boyfriend!"
    show sayori 1g
    n 2o "Well he didn't fucking tell me you two were a thing when I confessed to him a minute ago!"
    show sayori 1v
    n 5w "Looks like we've both been played..."
    show natsuki 5x
    s "T-{w=0.38}that can't be true..."
    show natsuki 1o
    show yuri 3n
    "Everyone's eyes glance over to my direction as I'm noticed by the group."
    s 4v "[player], what is this?!?!"
    s 4w "Are you...{w=0.38}breaking up with me?!?"
    show sayori 4u
    n 2p "Hold on...{w=0.38}you've been dating her this entire fucking time?!?!"
    n 1p "What the hell is wrong with you?!?"
    show natsuki 1o
    mc "I..."
    show monika 1h
    show yuri 3r
    "I can hardly muster a response as everyone angrily eyes me down."
    "I've royally screwed up..."
    m 1i "[player], step outside with me for a second."
    show monika 1h
    mc "But-"
    m 3i "I don't want to hear it!"
    show monika 1h
    "Monika walks over to me and takes me by the wrist."
    m 1i "Yuri, make sure they don't kill each other while we're gone."
    y 1o "I-{w=0.38}I'll try..."
    "Monika then practically drags me out into the hallway."
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    scene bg corridor
    play sound "sfx/closet-close.ogg"
    show monika 1h at t11 zorder 1
    "Monika shuts the door just as we hear Sayori and Natsuki's argument kick back up."
    "The only thing we're able to make out is more muffled yelling and screaming."
    jump n_merge




if encore_sayoriquestion_1 == False:



#Sayori Block

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                jump s_fight


#Monika Block

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 != "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Monika":
        if hangout2 != "Monika":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 != "Monika":
                jump m_fight


#Yuri Block

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 != "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Yuri":
        if hangout2 != "Yuri":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 != "Yuri":
                jump y_fight


#Natsuki Cases


#For Sayori

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Sayori":
        if hangout2 == "Natsuki":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight

#For Monika

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight

#For Yuri

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Yuri":
                jump y_fight


#Mixed Cases1

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Monika":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Sayori":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Monika":
            if hangout3 == "Sayori:
                jump s_fight


#Mixed Cases2

    if hangout1 == "Sayori":
        if hangout2 == "Natsuki":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Sayori":
                jump s_fight

    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            if hangout3 == "Yuri":
                jump y_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Sayori":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika":
                jump m_fight

    if hangout1 == "Monika":
        if hangout2 == "Natsuki":
            if hangout3 == "Sayori:
                jump s_fight






label s_fight:

show sayori 1i at t41 zorder 1
show natsuki 4o at t42 zorder 2
show monika 1d at t43 zorder 3
show yuri 3o at t44 zorder 4
"Sayori and Natsuki are in a full-blown argument as Monika and Yuri are doing their best to contain the situation."
"I should've known this was going to happen..."
n 5w "If you two aren't dating, then I don't see what the big deal is..."
show natsuki 5x
s 1j "I just would've appreciated it if you came up to me before you did this..."
show sayori 1g
n 5o "I don't need your fucking approval, Sayori! Get off my case!"
s 1k "So, you really are that mean, huh?"
s 2v "I thought you were my friend!"
show sayori 4u
show natsuki 1n
show yuri 3n
"Everyone's eyes glance over to my direction as I'm noticed by the group."
s 4v "[player], what is this?!?!"
s 4w "You're just getting with her?!?"
s 4v "After everything?!?!"
show sayori 4u
n 2p "Hold on...{w=0.38}you've been seeing her this entire fucking time?!?!"
n 1o "What the hell is wrong with you?!?"
show natsuki 1p
mc "I..."
show monika 1h
show yuri 3r
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
m 1i "Yuri, make sure they don't kill each other while we're gone."
y 1o "I-{w=0.38}I'll try..."
"Monika then practically drags me out into the hallway."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Sayori and Natsuki's argument kick back up."
"The only thing we're able to make out is more muffled yelling and screaming."
jump n_merge




label m_fight:

show sayori 1g at t41 zorder 1
show natsuki 4o at t42 zorder 2
show monika 3i at t43 zorder 3
show yuri 3o at t44 zorder 4
"Monika and Natsuki are in a full-blown argument as Sayori and Yuri are doing their best to contain the situation."
"I should've known this was going to happen..."
show monika 1h
n 5w "Well it's not my fault you were too slow, Monika!"
n 5x "If you two weren't dating, then I don't see what the big deal is..."
n 1o "And might I add how unethical it'd be for the club president to be dating one of their own club members?"
m 3i "That's not the point, Natsuki!"
m 5b "There's something called 'courtesy' in these types of situations..."
m "You knew I was hanging out with him!"
n 2r "Not like that though..."
show sayori 1i
show natsuki 1o
show monika 1h
show yuri 3r
"Everyone's eyes glance over to my direction as I'm noticed by the group."
m 3i "[player], what's the meaning of this?"
show monika 1h
mc "Meaning of what?"
n 2p "You've been seeing Monika this entire fucking time?!?!"
n 1p "What the hell is wrong with you?!?"
show natsuki 1o
mc "I..."
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
show sayori 1k
show yuri 3o
m 1i "Yuri, Sayori, calm down Natsuki. I don't want to deal with her right now."
n 5o "Fuck you too, Monika!"
"Monika then practically drags me out into the hallway as Natsuki kicks up a harsh tirade against her."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Sayori's and Yuri's attempts to calm down Natsuki."
"The only thing we're able to make out is more muffled yelling and screaming."
jump n_merge



label y_fight:

show sayori 1g at t41 zorder 1
show natsuki 4o at t42 zorder 2
show monika 1d at t43 zorder 3
show yuri 3r at t44 zorder 4
"Yuri and Natsuki are in a full-blown argument as Monika and Sayori are doing their best to contain the situation."
"I should've known this was going to happen..."
n 5w "Again, Yuri, it's not my problem if you too didn't make it official!"
n 5x "So if you don't like that we're together now, that ain't my problem!"
y 3r "You should've at least talked to me about all this beforehand!"
y 1h "Do you have any common courtesy?"
n 1o "Well how was I supposed to know you liked him?"
y 3r "You could've asked me, you dolt!"
show sayori 1i
show natsuki 1o
show monika 1h
show yuri 3r
"Everyone's eyes glance over to my direction as I'm noticed by the group."
y 3r "[player], did you like Natsuki all this time?"
mc "I..."
n 2p "You've been seeing Yuri this entire fucking time?!?!"
n 1p "What the hell is wrong with you?!?"
show natsuki 1o
mc "I..."
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
m 1i "Sayori, make sure they don't kill each other while we're gone."
s 1k "I'll try..."
"Monika then practically drags me out into the hallway."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Yuri and Natsuki's argument kick back up."
"The only thing we're able to make out is more muffled yelling and screaming."
jump n_merge


label n_chaos2:

show sayori 1n at t41 zorder 1
show natsuki 12f at t42 zorder 2
show monika 1c at t43 zorder 3
show yuri 3o at t44 zorder 4
"Natsuki is sitting face down on a nearby desk, sobbing uncontrollably."
"Sayori, Monika and Yuri are all over Natsuki, attempting to calm her down."
m 1d "Natsuki calm down! What happened?"
show natsuki 12h
show monika 1f
"Natsuki briefly lifts her head up."
show natsuki 12f
"As soon as she sees me, she immediately slams her face back into the desk, crying twice as harder and louder than before."
"Sayori, Monika and Yuri all exchange looks, bewildered at the situation they've found themselves in."
s 2g "N-{w=0.38}Natsuki?"
"Sayori attempts to place her hand on Natsuki."
show sayori 1w
show n_cry2 as natsuki at t42 zorder 2
play sound "sfx/slap.ogg"
"However, Natsuki slaps it away as hard as she can, making Sayori howl in pain."
show monika 1d at h43 zorder 3
show yuri 3p at h44 zorder 4
show n_cry1 as natsuki at t42 zorder 2
n "DON'T FUCKING TOUCH ME!"
n "DON'T EVEN TRY TO ACT ALL BUDDY-BUDDY WITH ME, YOU WHORE!"

if encore_sayoriquestion_1 == True:
    show n_cry2 as natsuki at t42 zorder 2
    n "YOU FUCKING KEPT HIM ALL TO YOURSELF AND YOU HAVE THE AUDACITY TO ACT LIKE YOU CARE ABOUT ME?!?!?"

if encore_sayoriquestion_1 == False:

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "YOU FUCKING KEPT HIM ALL TO YOURSELF AND YOU HAVE THE AUDACITY TO ACT LIKE YOU CARE ABOUT ME?!?!?"
                jump n_breakdown


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "YOU'RE THE ONE THAT MADE HIM FALL FOR YOU AND NOT ME!"
                n "YOU TOOK HIM AWAY FROM ME!"
                n "SO DON'T PRETEND LIKE YOU CARE ABOUT ANYONE BUT YOURSELF!"
                jump n_breakdown


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "YOU'RE THE ONE THAT MADE HIM FALL FOR YOU AND NOT ME!"
                n "YOU TOOK HIM AWAY FROM ME!"
                n "SO DON'T PRETEND LIKE YOU CARE ABOUT ANYONE BUT YOURSELF!"
                jump n_breakdown


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "YOU'RE THE ONE THAT MADE HIM FALL FOR YOU AND NOT ME!"
                n "YOU TOOK HIM AWAY FROM ME!"
                n "SO DON'T PRETEND LIKE YOU CARE ABOUT ANYONE BUT YOURSELF!"
                jump n_breakdown


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "I DON'T WANT YOUR FUCKING HELP!"
                n "YOU JUST WANT HIM FOR YOURSELF!"
                jump n_breakdown

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "I DON'T WANT YOUR FUCKING HELP!"
                n "YOU JUST WANT HIM FOR YOURSELF!"
                jump n_breakdown

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "I DON'T WANT YOUR FUCKING HELP!"
                n "YOU JUST WANT HIM FOR YOURSELF!"
                jump n_breakdown


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                show n_cry2 as natsuki at t42 zorder 2
                n "I KNOW YOU JUST WANT HIM ALL TO YOURSELF!"
                n "YOU ACTING NICE IS JUST FOR SHOW, AND WE ALL KNOW IT !"
                jump n_breakdown




label n_breakdown:

n "PISS OFF!"
show sayori 1k
"The room becomes dead quiet as Natsuki finishes her insult."
"Yuri looks as if she's about to have a full-on panic attack, Monika still looks completely bewildered."
"Sayori looks as if she's about to break down and cry as Natsuki angrily stares her down..."
s 1l "O-{w=0.38}okay..."
s 1k "If you want to be like that..."
show sayori at thide
hide sayori
show n_cry2 as natsuki at t31 zorder 1
show monika 1d at t32 zorder 2
show yuri 3o at t33 zorder 3
"Sayori promptly walks back to her original seat and tries her hardest to fight back tears of her own."
show monika 1h
show yuri 3n
"Monika and Yuri immediately turn to me."
m "What did you do?"
mc "I didn’t do anything!"
show natsuki 12f
"Natsuki resumes her sobbing."
m 1i "[player], step outside with me for a moment."
show monika 1h
"She says sternly."
"Monika then turns to Yuri."
show yuri 3o
m "Yuri, try to see if you can calm her down, okay?"
"I see the color drain from Yuri’s face."
"Yuri seems visibly uncomfortable with Monika’s request, but given the gravity of the situation, she nevertheless accepts it."
y 3q "I-{w=0.38}I’ll try..."
"Monika takes me by the wrist and walks me out of the clubroom."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
"Just before leaving, I hear a snippet of Yuri’s efforts to calm down Natsuki."
y "N-{w=0.38}Natsuki?"
n "GET AWAY FROM ME YOU EDGY PSYCHO BITCH!"
y "Edgy?"
y "Who are you calling edgy you loli-"
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door before I can hear the end of Yuri's response."
"The only thing we're able to make out is more muffled yelling and screaming."
jump n_merge



label y_chaos1:

if encore_sayoriquestion_1 == True:

    show sayori 1i at t41 zorder 1
    show natsuki 4n at t42 zorder 2
    show monika 1d at t43 zorder 3
    show yuri 3r at t44 zorder 4
    "Sayori and Yuri are in a full-blown argument as Monika and Natsuki are doing their best to contain the situation."
    "What have I done..."
    s 1j "For the last time Yuri, I'm dating him! He's not your boyfriend!"
    show sayori 1g
    y 3r "Well, he failed to mention that tiny little detail..."
    show sayori 1v
    y 1h "I think we've both been used..."
    show yuri 1g
    s "T-{w=0.38}that can't be true..."
    show natsuki 1c
    show yuri 3r
    "Everyone's eyes glance over to my direction as I'm noticed by the group."
    s 4v "[player], what is this?!?!"
    s 4w "Are you...{w=0.38}breaking up with me?!?"
    show sayori 4u
    y 3r "Do you mind explaining to me your relationship with Sayori?!?"
    y 1r "What the hell are you trying to pull with us?!?"
    show natsuki 1o
    mc "I..."
    show monika 1h
    "I can hardly muster a response as everyone angrily eyes me down."
    "I've royally screwed up..."
    m 1i "[player], step outside with me for a second."
    show monika 1h
    mc "But-"
    m 3i "I don't want to hear it!"
    show monika 1h
    "Monika walks over to me and takes me by the wrist."
    m 1i "Natsuki, make sure they don't kill each other while we're gone."
    n 1q "O-{w=0.38}okay..."
    "Monika then practically drags me out into the hallway."
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    scene bg corridor
    play sound "sfx/closet-close.ogg"
    show monika 1h at t11 zorder 1
    "Monika shuts the door just as we hear Sayori and Yuri's argument kick back up."
    "The only thing we're able to make out is more muffled yelling and screaming."
    jump y_merge

if encore_sayoriquestion_1 == False:



#Sayori Block

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                jump s_fight2


#Monika Block

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 != "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Monika":
        if hangout2 != "Monika":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 != "Monika":
                jump m_fight2


#Natsuki Block

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 != "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Natsuki":
        if hangout2 != "Natsuki":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 != "Natsuki":
                jump n_fight


#Yuri Cases


#For Sayori

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Sayori":
        if hangout2 == "Yuri":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Yuri":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                jump s_fight2

#For Monika

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Monika":
        if hangout2 == "Yuri":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Yuri":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                jump m_fight2


#For Natsuki

    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                jump n_fight

#Mixed Cases1

    if hangout1 == "Yuri":
        if hangout2 == "Sayori":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Yuri":
        if hangout2 == "Monika":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Yuri":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Yuri":
        if hangout2 == "Sayori":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Yuri":
        if hangout2 == "Monika":
            if hangout3 == "Sayori:
                jump s_fight2


#Mixed Cases2

    if hangout1 == "Sayori":
        if hangout2 == "Yuri":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Sayori":
                jump s_fight2

    if hangout1 == "Monika":
        if hangout2 == "Yuri":
            if hangout3 == "Natsuki":
                jump n_fight

    if hangout1 == "Natsuki":
        if hangout2 == "Yuri":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Sayori":
        if hangout2 == "Yuri":
            if hangout3 == "Monika":
                jump m_fight2

    if hangout1 == "Monika":
        if hangout2 == "Yuri":
            if hangout3 == "Sayori:
                jump s_fight2



label s_fight2:


show sayori 1i at t41 zorder 1
show yuri 3o at t42 zorder 2
show monika 1d at t43 zorder 3
show natsuki 4n at t44 zorder 4
"Sayori and Yuri are in a full-blown argument as Monika and Natsuki are doing their best to contain the situation."
"I should've known this was going to happen..."
y 3h "Well Sayori, if you two aren't dating, then there really should be no problem here..."
show yuri 3g
s 1j "I just would've appreciated it if you came up to me before you did this..."
show sayori 1g
y 3r "Sayori, it's my personal life! I neither need or want your input!"
s 1k "So, it's really going to be like that, huh?"
s 2v "I thought you were my friend!"
show sayori 4u
show natsuki 1n
show yuri 3e
"Everyone's eyes glance over to my direction as I'm noticed by the group."
s 4v "[player], what is this?!?!"
s 4w "You're just getting with her?!?"
s 4bv "After everything?!?!"
show sayori 4u
show sayori 4u
y 3r "Do you mind explaining to me your relationship with Sayori?!?"
y 1r "What the hell are you trying to pull with us?!?"
show natsuki 1o
mc "I..."
show monika 1h
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
m 1i "Natsuki, make sure they don't kill each other while we're gone."
n 1q "O-{w=0.38}okay..."
"Monika then practically drags me out into the hallway."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Sayori and Yuri's argument kick back up."
"The only thing we're able to make out is more muffled yelling and screaming."
jump y_merge

label m_fight2:


show sayori 1g at t41 zorder 1
show yuri 3r at t42 zorder 2
show monika 3i at t43 zorder 3
show natsuki 4n at t44 zorder 4
"Monika and Yuri are in a full-blown argument as Sayori and Natsuki are doing their best to contain the situation."
"I should've known this was going to happen..."
show monika 1h
y 3h "Monika, it's hardly my fault that you failed to make a move on him!"
y 1l "You two aren't officially dating, so your argument over this is pointless."
y 1r "Not to mention, I seriously question the ethical implications of our club President dating one of our own members!"
m 3i "That's not the point, Yuri!"
m 5b "There's something called 'courtesy' in these types of situations..."
m "You knew I was hanging out with him!"
y 1h "I didn't think you guys were serious..."
show sayori 1i
show natsuki 1o
show monika 1h
show yuri 3r
"Everyone's eyes glance over to my direction as I'm noticed by the group."
m 3i "[player], what's the meaning of this?"
show monika 1h
mc "Meaning of what?"
y 3r "Do you mind explaining to me your relationship with Monika?!?"
y 1r "What the hell are you trying to pull with us?!?"
show natsuki 1o
mc "I..."
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
show sayori 1k
show natsuki 1n
m 1i "Natsuki, Sayori, calm down Yuri. I can't deal with her right now."
y 3r "Screw you, Monika!"
"Monika then practically drags me out into the hallway as Natsuki kicks up a harsh tirade against her."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Sayori and Natsuki's attempts to calm down Yuri."
"The only thing we're able to make out is more muffled yelling and screaming."
jump y_merge


label n_fight:

show sayori 1g at t41 zorder 1
show yuri 3r at t42 zorder 2
show monika 1d at t43 zorder 3
show natsuki 4o at t44 zorder 4
"Yuri and Natsuki are in a full-blown argument as Monika and Sayori are doing their best to contain the situation."
"I should've known this was going to happen..."
y 3h "As I said Natsuki, it's not my problem if you failed to make things official with him!"
y 3l "So I don't exactly care about your opinion on this subject."
n 3o "Wow, are you that full of yourself?"
n 1o "Are you really the kind of person to just swoop in and mess up other people's relationships like that? Are you always so quiet is because you scheme to mess up people's lives?!?"
y 1r "Well how was I supposed to know you liked him?"
n 1v "You could've asked me, you bitch!"
show sayori 1i
show natsuki 1o
show monika 1h
show yuri 3r
"Everyone's eyes glance over to my direction as I'm noticed by the group."
n 4p "[player], what the hell?!?"
n 1o "What have you been doing with Yuri?!?"
mc "I..."
y 3r "Do you mind explaining to me your relationship with Monika?!?"
y 1r "What the hell are you trying to pull with us?!?"
show natsuki 1o
mc "I..."
"I can hardly muster a response as everyone angrily eyes me down."
"I've royally screwed up..."
m 1i "[player], step outside with me for a second."
show monika 1h
mc "But-"
m 3i "I don't want to hear it!"
show monika 1h
"Monika walks over to me and takes me by the wrist."
m 1i "Sayori, make sure they don't kill each other while we're gone."
s 1k "I'll try..."
"Monika then practically drags me out into the hallway."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door just as we hear Yuri and Natsuki's argument kick back up."
"The only thing we're able to make out is more muffled yelling and screaming."
jump y_merge


label y_chaos2:

show sayori 1n at t41 zorder 1
show y_cry1 as yuri at t42 zorder 2
show monika 1c at t43 zorder 3
show natsuki 1n at t44 zorder 4
"Yuri is sitting face down on a nearby desk, sobbing uncontrollably."
"Sayori, Monika and Natsuki are all over Yuri, attempting to calm her down."
m 1d "Yuri calm down! What happened?"
show monika 1f
show y_cry2 as yuri at t42 zorder 2
"Yuri briefly lifts her head up."
show y_cry3 as yuri at t42 zorder 2
"As soon as she sees me, she immediately slams her face back into the desk, crying twice as harder and louder than before."
"Sayori, Monika and Natsuki all exchange looks, bewildered at the situation they've found themselves in."
s 2g "Y-{w=0.38}Yuri?"
"Sayori attempts to place her hand on Yuri."
show sayori 1w
play sound "sfx/slap.ogg"
"However, Yuri slaps it away as hard as she can, making Sayori howl in pain."
show natsuki 1c
show monika 1d at h43 zorder 3
show yuri
show y_cry4 as yuri at t42 zorder 2
y "GET YOUR STUPID, MESSY SELF AWAY FROM ME, YOU BITCH!"
show y_cry5 as yuri at t42 zorder 2

if encore_sayoriquestion_1 == True:
    y "YOU'VE KEPT HIM ALL TO YOURSELF, AND NOW YOU CARE ABOUT WHAT I THINK?!?!?"

if encore_sayoriquestion_1 == False:

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y "YOU'VE KEPT HIM ALL TO YOURSELF, AND NOW YOU CARE ABOUT WHAT I THINK?!?!?"
                jump y_breakdown


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y "YOU'RE THE ONE WHO RUINED EVERYTHING FOR ME!"
                y "YOU KEPT HIM ALL TO YOURSELF!"
                y "SO SPARE ME YOUR FAKE SYMPATHY!"
                jump y_breakdown


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y "YOU'RE THE ONE WHO RUINED EVERYTHING FOR ME!"
                y "YOU KEPT HIM ALL TO YOURSELF!"
                y "SO SPARE ME YOUR FAKE SYMPATHY!"
                jump y_breakdown


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y "YOU'RE THE ONE WHO RUINED EVERYTHING FOR ME!"
                y "YOU KEPT HIM ALL TO YOURSELF!"
                y "SO SPARE ME YOUR FAKE SYMPATHY!"
                jump y_breakdown

    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y "DON'T BOTHER TRYING TO MAKE ME FEEL BETTER!"
                y "EVERYONE KNOWS YOU JUST WANT HIM FOR YOURSELF!"
                jump y_breakdown

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y "DON'T BOTHER TRYING TO MAKE ME FEEL BETTER!"
                y "EVERYONE KNOWS YOU JUST WANT HIM FOR YOURSELF!"
                jump y_breakdown

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y "DON'T BOTHER TRYING TO MAKE ME FEEL BETTER!"
                y "EVERYONE KNOWS YOU JUST WANT HIM FOR YOURSELF!"
                jump y_breakdown


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y "DON'T PRETEND LIKE YOU GENINELY CARE ABOUT ME!"
                y "STOP TRYING TO MAKE YOURSELF LOOK GOOD IN FRONT OF HIM!"
                jump y_breakdown




label y_breakdown:

show y_cry6 as yuri at t42 zorder 2
y "GO AWAY, AND RUIN SOMEONE ELSE'S DAY, SAYORI!"
show sayori 1k
show y_cry4 as yuri at t42 zorder 2
"The room becomes dead quiet as Yuri finishes her insult."
"Natsuki is in total shock, Monika still looks completely bewildered."
"Sayori looks as if she's about to break down and cry as Natsuki angrily stares her down..."
s 1l "O-{w=0.38}okay..."
s 1k "If you want to be like that..."
show sayori at thide
hide sayori
show y_cry1 as yuri at t31 zorder 1
show monika 1d at t32 zorder 2
show natsuki 5n at t33 zorder 3
"Sayori promptly walks back to her original seat and tries her hardest to fight back tears of her own."
show monika 1h
show natsuki 1o
"Monika and Natsuki immediately turn to me."
m "What did you do?"
mc "I didn’t do anything!"
show y_cry2 as yuri at t31 zorder 1
"Yuri resumes her sobbing."
m 1i "[player], step outside with me for a moment."
show monika 1h
"She says sternly."
"Monika then turns to Natsuki."
show natsuki 1n
m "Natsuki, try to see if you can calm her down, okay?"
show natsuki 1r
"Natsuki grits her teeth in annoyance."
"She seems reluctant with Monika’s request, but given the gravity of the situation, Natsuki nevertheless accepts it."
n 1q "O-{w=0.38}okay..."
"Monika takes me by the wrist and walks me out of the clubroom."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg corridor
"Just before leaving, I hear a snippet of Natsuki's efforts to calm down Natsuki."
n "Y-{w=0.38}Yuri?"
y "GET AWAY FROM ME YOU LOLI!"
n "Loli?"
n "Who are you calling a loli you edgy-"
play sound "sfx/closet-close.ogg"
show monika 1h at t11 zorder 1
"Monika shuts the door before I can hear the end of Natsuki's response."
"The only thing we're able to make out is more muffled yelling and screaming."
jump y_merge


label n_merge:

m 1i "What happened?"
show monika 1h

if n_love == True:
    show monika 1d
    mc "I accepted her confession..."
    m 1g "Why? I thought you said you were unsure about how you felt about her?"
    show monika 2f
    mc "She gave me this really emotional speech about how she's always liked me and how much she means to me..."
    mc "And well, I guess in the moment I felt the same way..."
    mc "I thought that's what I wanted..."
    mc "But I didn't think she was going to go off and tell everyone!"
    show monika 2p
    "An awkward silence ensues between us."
    show monika 1f
    "Monika looks back and forth between me and the ground as she tries to figure out how to even respond."

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                show monika 1p
                "I probably hurt her pretty bad..."
                "How could I spend so much time with her only to pull this?!?"
                "I completely blew it..."

            if encore_sayoriquestion_1 == True:
                "And I blew things with Sayori too..."
                "Now nobody is going to trust me..."
                jump converge1

            if encore_sayoriquestion_1 == False:
                "She's never going to trust me after this..."
                jump converge1


    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika" or hangout3 == "Sayori" or hangout3 == "Yuri":
                show monika 2f
                "She knows that I've been hanging around Natsuki a lot instead of Sayori..."
                "But even now, considering I just practically dumped Sayori without telling her, Monika probably thinks I'm the worst human being possible..."
                "Nobody's ever going to trust me..."
                jump converge1



    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                show monika 2f
                "She probably thinks I'm a completely awful person..."
                "To spend so much time with Sayori..."
                "Only to completely betray her trust..."
                "She's never going to trust me after this..."
                jump converge1


    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Yuri":
                "She probably thinks I'm a completely awful person..."
                "To spend so much time with Yuri..."
                "Only to completely betray her trust..."

                if encore_sayoriquestion_1 == True:
                    "And I blew things with Sayori too..."
                    "Now nobody is going to trust me..."
                    jump converge1

                if encore_sayoriquestion_1 == False:
                    "She's never going to trust me after this..."
                    jump converge1


    else:
        show monika 2f
        "What is she even supposed to say to someone like me?"
        "I've basically played with everyone's hearts at this point..."
        "Everyone is now hurting because of my stupid mistake..."
        jump converge1

if n_love == False:
    show monika 1d
    mc "I turned Natsuki down..."
    m 2g "She took it that bad, huh?"
    show monika 2f
    mc "I'm afraid so..."
    mc "I told her that I didn't like her back the same way, even though I offered to hangout with her more..."
    show monika 2p
    mc "It's safe to say that offer was rejected though..."
    mc "She ended up slapping me pretty badly."
    show monika 2d
    "Monika nearly gasps as I show her Natsuki's slap mark."
    "While it doesn't nearly hurt as bad as a few minute ago, it still feels rather tender..."
    m 2n "I see..."
    show monika 1o
    "Monika nervously grimaces as she tries to assess the situation."
    show monika 1n

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":

                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Natsuki's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    jump day4_fight_n

                if encore_sayoriquestion_1 == False:
                    m "Well, I'm sure we can sort things out with her..."
                    show monika 1n
                    m "She just needs a little time to cool off..."
                    show monika 1g
                    mc "Well, with how she reacted, I doubt it's going to be anytime soon..."
                    m 3p "Yeah, you're probably right. She starting screaming and cursing at me the moment she came back from talking to you..."
                    mc "Wow..."
                    m 2o "I've never seen her mad like this..."
                    m 1p "It's concerning to say the least..."
                    show monika 1f
                    mc "I'm really sorry I brought you into this Monika..."
                    mc "I didn't even bring you up or anything!"
                    mc "It was all her!"
                    m 1l "I'm not mad at you, [player]! Don't worry!"
                    m 1n "It's clear that Natsuki's had this pent up for a while now..."
                    m 1m "And I'm sure she'll get over and come to respect our relationship..."
                    m 1e "Whatever we decide to make of it."
                    "A grin forces its way onto my face as Monika says that."
                    jump day4_fight_n






    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Monika" or hangout3 == "Sayori" or hangout3 == "Yuri":

                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Natsuki's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    jump day4_fight_n

                if encore_sayoriquestion_1 == False:
                    m "Well I'm glad you didn't make any rash decisions..."
                    show monika 1m
                    mc "What do you mean by 'rash decisions'?"
                    m 3n "Ah, don't worry about it..."
                    m 1e "Let's just focus on sorting things out with Natsuki..."
                    show monika 1m
                    mc "Well, I've got a lot of explaining to do to everyone anyways..."
                    jump day4_fight_n




    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":

                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."

                if encore_sayoriquestion_1 == False:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to make things right..."

                show monika 1m
                mc "I've just tried to be the best I can around her..."
                show monika 1f
                mc "Wish I could say the same for Natsuki though..."
                m 3n "We'll get everything sorted out with her, don't you worry..."
                m 3m "She just needs a chance to cool down..."
                mc "Do I really wanna know how she started all this?"
                m 3p "Well, she pretty much barged in, starting screaming and cursing at Sayori, then she just broke down crying in her desk..."
                mc "Wow..."
                m 2o "Yeah, she's never been mad like this..."
                "Oh great..."
                "Looks like Sayori's not going to be the only one needing therapy after all this..."
                jump day4_fight_n



    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Yuri":

                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Natsuki's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    "And I can only imagine how Yuri's going to handle all this..."
                    jump day4_fight_n


                if encore_sayoriquestion_1 == False:
                    m "Well, I'm glad you made the right decision for Yuri's sake..."
                    show monika 1e
                    m "I'm sure Yuri will appreciate you trying to stay loyal to her..."
                    show monika 1m
                    mc "I've just tried to be the best I can around her..."
                    show monika 1f
                    mc "Wish I could say the same for Natsuki though..."
                    m 3n "We'll get everything sorted out with her, don't you worry..."
                    m 3m "She just needs a chance to cool down..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "Well, she pretty much barged in, starting screaming and cursing at Yuri, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "I can only imagine how Yuri's going to handle all this..."
                    jump day4_fight_n



    else:
        m "Well I'm glad you didn't make any rash decisions..."
        show monika 1m
        mc "What do you mean by 'rash decisions'?"
        m 3n "Ah, don't worry about it..."
        m 1e "Let's just focus on sorting things out with Natsuki..."
        show monika 1m
        mc "Well, I've got a lot of explaining to do to everyone anyways..."
        jump day4_fight_n


label converge1:

show monika 3m
"Monika clears her throat, ending my train of thought."
m 3n "Well, [player]...{w=0.38}if you want to be with Natsuki, then that's your choice..."
show monika 1g
mc "I don't know what I was thinking, okay?"
show monika 1f
mc "I screwed up, I shouldn't have said yes!"
mc "I wanted to sort everything out first..."
mc "She wasn't supposed to tell so soon!"
mc "I wasn't ready for this..."
mc "What am I going to do?!?!"
show monika 3g

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":

            if encore_sayoriquestion_1 == True:
                m "You need to sort out things with Natsuki and Sayori..."
                m 1p "And we can talk about us when that's taken care of..."
                jump converge2


            if encore_sayoriquestion_1 == False:
                m "You need to sort out things with Natsuki..."
                m 1p "And we can talk about us when that's taken care of..."
                jump converge2


if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        if hangout3 == "Monika" or hangout3 == "Sayori" or hangout3 == "Yuri":

            if encore_sayoriquestion_1 == True:

                if hangout3 == "Monika":
                    m "You need to sort out things with Natsuki and Sayori..."
                    m 1p "And we can talk about us when that's taken care of..."
                    jump converge2

                if hangout3 == "Sayori":
                    m "You need to sort out things with Natsuki and Sayori..."
                    jump converge2

                if hangout3 == "Yuri":
                    m "You need to sort out things with Natsuki and Yuri..."
                    jump converge2

            if encore_sayoriquestion_1 == False:

                if hangout3 == "Monika":
                    m "You need to sort out things with Natsuki..."
                    m 1p "And we can talk about us when that's taken care of..."
                    jump converge2

                if hangout3 == "Sayori":
                    m "You need to sort out things with Natsuki and Sayori..."
                    jump converge2

                if hangout3 == "Yuri":
                    m "You need to sort out things with Natsuki and Yuri..."
                    jump converge2



if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        if hangout3 == "Sayori":
            m "You need to sort out things with Natsuki and Sayori..."
            jump converge2


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        if hangout3 == "Yuri":

            if encore_sayoriquestion_1 == True:
                m "You need to sort out things with Natsuki, Sayori and Yuri..."
                jump converge2

            if encore_sayoriquestion_1 == False:
                m "You need to sort out things with Natsuki and Yuri..."
                jump converge2

else:
    m "Well it seems like you need to sort things out with everyone..."
    m 1p "Just focus on getting everyone calmed down, admit you made a mistake, and we'll go from there..."
    jump converge2


label converge2:
mc "Okay..."
show monika 1g
mc "I'm really sorry about causing all this drama, Monika..."
m 1l "Let's just get through this first and save the apologies for later..."
show monika 1m
mc "Alright..."
jump day4_fight_n


label y_merge:

m 1i "What happened?"
show monika 1h


if y_love == True:
    show monika 1d
    mc "I accepted her confession..."
    m 1g "Why? I thought you said you were unsure about how you felt about her?"
    show monika 2f
    mc "She gave me this really emotional speech about how she's always liked me and how much she means to me..."
    mc "And well, I guess in the moment I felt the same way..."
    mc "I thought that's what I wanted..."
    mc "But I didn't think she was going to go off and tell everyone!"
    show monika 2p
    "An awkward silence ensues between us."
    show monika 1f
    "Monika looks back and forth between me and the ground as she tries to figure out how to even respond."

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":
                show monika 1p
                "I probably hurt her pretty bad..."
                "How could I spend so much time with her only to pull this?!?"
                "I completely blew it..."

                if encore_sayoriquestion_1 == True:
                    "And I blew things with Sayori too..."
                    "Now nobody is going to trust me..."
                    jump converge3


                if encore_sayoriquestion_1 == False:
                    "She's never going to trust me after this..."
                    jump converge3


    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Natsuki" or hangout3 == "Sayori" or hangout3 == "Monika":
                show monika 2f
                "She knows that I've been hanging around Yuri a lot instead of Sayori..."
                "But even now, considering I just practically dumped Sayori without telling her, Monika probably thinks I'm the worst human being possible..."
                "Nobody's ever going to trust me..."
                jump converge3



    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                show monika 2f
                "She probably thinks I'm a completely awful person..."
                "To spend so much time with Sayori..."
                "Only to completely betray her trust..."
                "She's never going to trust me after this..."
                jump converge3



    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":
                "She probably thinks I'm a completely awful person..."
                "To spend so much time with Sayori..."
                "Only to completely betray her trust..."

                if encore_sayoriquestion_1 == True:
                    "And I blew things with Sayori too..."
                    "Now nobody is going to trust me..."
                    jump converge3

                if encore_sayoriquestion_1 == False:
                    "She's never going to trust me after this..."
                    jump converge3


    else:
        show monika 2f
        "What is she even supposed to say to someone like me?"
        "I've basically played with everyone's hearts at this point..."
        "Everyone is now hurting because of my stupid mistake..."
        jump converge3



if y_love == False:
    show monika 1d
    mc "I turned Yuri down..."
    m 2g "She took it that bad, huh?"
    show monika 2f
    mc "I'm afraid so..."
    mc "She gave me this big speech about how I was so kind and welcoming to her and how she's never really had that before..."
    mc "I told her that I didn't like her back the same way, even though I offered to hangout with her more..."
    show monika 2p
    mc "It's safe to say that offer was rejected though..."
    mc "She cursed me out and then ran back into the room."
    m 2n "I see..."
    show monika 1o
    "Monika nervously grimaces as she tries to assess the situation."
    show monika 1n

    if hangout1 == "Monika":
        if hangout2 == "Monika":
            if hangout3 == "Monika":


                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Yuri's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "She's never like that..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    jump day4_fight_y



                if encore_sayoriquestion_1 == False:
                    m "Well, I'm sure we can sort things out with her..."
                    show monika 1n
                    m "She just needs a little time to cool off..."
                    show monika 1g
                    mc "Well, with how she reacted, I doubt it's going to be anytime soon..."
                    m 3p "Yeah, you're probably right. She starting screaming and cursing at me the moment she came back from talking to you..."
                    mc "Wow..."
                    m 2o "I've never seen her act like that..."
                    m 1p "It's concerning to say the least..."
                    show monika 1f
                    mc "I'm really sorry I brought you into this Monika..."
                    mc "I didn't even bring you up or anything!"
                    mc "It was all her!"
                    m 1l "I'm not mad at you, [player]! Don't worry!"
                    m 1n "It's clear that Yuri's had this pent up for a while now..."
                    m 1m "And I'm sure she'll get over and come to respect our relationship..."
                    m 1e "Whatever we decide to make of it."
                    "A grin forces its way onto my face as Monika says that."
                    jump day4_fight_y



    if hangout1 == "Yuri":
        if hangout2 == "Yuri":
            if hangout3 == "Monika" or hangout3 == "Sayori" or hangout3 == "Natsuki":

                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Yuri's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    jump day4_fight_y


                if encore_sayoriquestion_1 == False:
                    m "Well I'm glad you didn't make any rash decisions..."
                    show monika 1m
                    mc "What do you mean by 'rash decisions'?"
                    m 3n "Ah, don't worry about it..."
                    m 1e "Let's just focus on sorting things out with Yuri..."
                    show monika 1m
                    mc "Well, I've got a lot of explaining to do to everyone anyways..."
                    jump day4_fight_y





    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":


                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."



                if encore_sayoriquestion_1 == False:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to make things right..."


                show monika 1m
                mc "I've just tried to be the best I can around her..."
                show monika 1f
                mc "Wish I could say the same for Yuri though..."
                m 3n "We'll get everything sorted out with her, don't you worry..."
                m 3m "She just needs a chance to cool down..."
                mc "Do I really wanna know how she started all this?"
                m 3p "Well, she pretty much barged in, starting screaming and cursing at Sayori, then she just broke down crying in her desk..."
                mc "Wow..."
                m 2o "Yeah, she's never been mad like this..."
                "Oh great..."
                "Looks like Sayori's not going to be the only one needing therapy after all this..."
                jump day4_fight_y


    if hangout1 == "Natsuki":
        if hangout2 == "Natsuki":
            if hangout3 == "Natsuki":


                if encore_sayoriquestion_1 == True:
                    m "Well, I'm glad you made the right decision for Sayori's sake..."
                    show monika 1e
                    m "I'm sure Sayori will appreciate you trying to stay loyal to her..."
                    show monika 1f
                    mc "It's not like I've been doing a good job of doing that anyway..."
                    m 1m "Well even then, it shows you're committed to trying to make things work between you two..."
                    mc "I guess I can't say the same for Yuri's sake..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "She pretty much barged in, starting screaming and cursing at all of us, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "Looks like Sayori's not going to be the only one needing therapy after all this..."
                    "And I can only imagine how Natsuki's going to handle all this..."
                    jump day4_fight_y


                if encore_sayoriquestion_1 == False:
                    m "Well, I'm glad you made the right decision for Natsuki's sake..."
                    show monika 1e
                    m "I'm sure Natsuki will appreciate you trying to stay loyal to her..."
                    show monika 1m
                    mc "I've just tried to be the best I can around her..."
                    show monika 1f
                    mc "Wish I could say the same for Yuri though..."
                    m 3n "We'll get everything sorted out with her, don't you worry..."
                    m 3m "She just needs a chance to cool down..."
                    mc "Do I really wanna know how she started all this?"
                    m 3p "Well, she pretty much barged in, starting screaming and cursing at Natsuki, then she just broke down crying in her desk..."
                    mc "Wow..."
                    m 2o "Yeah, she's never been mad like this..."
                    "Oh great..."
                    "I can only imagine how Natsuki's going to deal with this..."
                    jump day4_fight_y



    else:
        m "Well I'm glad you didn't make any rash decisions..."
        show monika 1m
        mc "What do you mean by 'rash decisions'?"
        m 3n "Ah, don't worry about it..."
        m 1e "Let's just focus on sorting things out with Yuri..."
        show monika 1m
        mc "Well, I've got a lot of explaining to do to everyone anyways..."
        jump day4_fight_y


label converge3:
show monika 3m
"Monika clears her throat, ending my train of thought."
m 3n "Well, [player]...{w=0.38}if you want to be with Yuri, then that's your choice..."
show monika 1g
mc "I don't know what I was thinking, okay?"
show monika 1f
mc "I screwed up, I shouldn't have said yes!"
mc "I wanted to sort everything out first..."
mc "She wasn't supposed to tell so soon!"
mc "I wasn't ready for this..."
mc "What am I going to do?!?!"
show monika 3g

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":

            if encore_sayoriquestion_1 == True:
                m "You need to sort out things with Yuri and Sayori..."
                m 1p "And we can talk about us when that's taken care of..."
                jump converge4


            if encore_sayoriquestion_1 == False:
                m "You need to sort out things with Yuri.."
                m 1p "And we can talk about us when that's taken care of..."
                jump converge4


if hangout1 == "Yuri":
    if hangout2 == "Yuri":
        if hangout3 == "Monika" or hangout3 == "Sayori" or hangout3 == "Natsuki":

            if encore_sayoriquestion_1 == True:

                if hangout3 == "Monika":
                    m "You need to sort out things with Yuri and Sayori..."
                    m 1p "And we can talk about us when that's taken care of..."
                    jump converge4

                if hangout3 == "Sayori":
                    m "You need to sort out things with Yuri and Sayori..."
                    jump converge4

                if hangout3 == "Natsuki":
                    m "You need to sort out things with Yuri and Natsuki..."
                    jump converge4

            if encore_sayoriquestion_1 == False:

                if hangout3 == "Monika":
                    m "You need to sort out things with Yuri..."
                    m 1p "And we can talk about us when that's taken care of..."
                    jump converge4

                if hangout3 == "Sayori":
                    m "You need to sort out things with Yuri and Sayori..."
                    jump converge4

                if hangout3 == "Natsuki":
                    m "You need to sort out things with Yuri and Natsuki..."
                    jump converge4



if hangout1 == "Sayori":
    if hangout2 == "Sayori":
        if hangout3 == "Sayori":
            m "You need to sort out things with Yuri and Sayori..."
            jump converge4


if hangout1 == "Natsuki":
    if hangout2 == "Natsuki":
        if hangout3 == "Natsuki":

            if encore_sayoriquestion_1 == True:
                m "You need to sort out things with Natsuki, Sayori and Yuri..."
                jump converge4

            if encore_sayoriquestion_1 == False:
                m "You need to sort out things with Natsuki and Yuri..."
                jump converge4

else:
    m "Well it seems like you need to sort things out with everyone..."
    m 1p "Just focus on getting everyone calmed down, admit you made a mistake, and we'll go from there..."
    jump converge4


label converge4:
mc "Okay..."
show monika 1g
mc "I'm really sorry about causing all this drama, Monika..."
m 1l "Let's just get through this first and save the apologies for later..."
show monika 1m
mc "Alright..."
jump day4_fight_y




label day4_fight_n:

show monika 1o
"Monika begrudgingly looks at the door, where we can still make out the screaming from the others."
m 1p "Well, so much for getting Natsuki to calm down..."
show monika 2f
mc "What are we going to do?"
m 1p "I'll try talking to her one-on-one, see if that does anything."

if hangout1 == "Monika" and hangout2 == "Monika" and hangout3 == "Monika":
    m 1q "I'm the one she has a problem with anyways..."

else:
    m 1q "It's my responsibility to calm her down anyways..."

m 1d "Just try not to say anything to her, okay?"
show monika 1c
mc "Alright..."
m 2p "Well, here goes nothing..."
show monika 1m
"Monika nervously smiles as she swings open the door..."
scene bg club_day
with wipeleft_scene
play sound "sfx/fall2.ogg"
"As soon as she does however, we're forced to duck as a textbook almost immediately flies over our heads."
show yuri 2j at t21 zorder 1
show natsuki 1o at t22 zorder 2
play music e27 fadein 2.0
y "Wow, Natsuki..."
y 2i "Great throw...{w=0.38}for a dwarf."
"Natsuki clenches her fists as she lets out an angry grunt."
n 1p "Take back what you said right now...{w=0.38}you cutting-obsessed whore!"
show natsuki 1o
y 1r "Only after you take back your accusation of me of being a member of a satanic cult, you flat-chested dumpster diver!"
show natsuki 1v at h22 zorder 1
n "Flat chested?!?!? THAT’S IT!"
show natsuki 1o
"Natsuki threateningly raises her fist at Yuri."
"Somehow, everything is in even worse shape..."
show yuri 1r at t31 zorder 1
show monika 1h at t32 zorder 2
show natsuki 1o at t33 zorder 3
"Fortunately, Monika steps in between Yuri and Natsuki and pushes them away from each other."
m 1i "Enough you two!"
m 3h "There's going to be no more fighting here today, understand?"
show natsuki 5r
show yuri 3h
"Natsuki and Yuri avert their eyes away from Monika and mumble something that I can't make out."
m 3r "Yuri, go sit down. I'm going to have a word with Natsuki first."
y 3q "I think it's going to take more than a 'word' to straighten her out, Monika..."
y 2h "If I may..."
m 1h "Just go."
show yuri 3y7
"Yuri and Monika coldly stare each other down."
"Yuri's never been one for confrontation..."
"I can tell Monika seems rather surprised too, but she seems to be standing her ground for now."
show monika 2h
"Yuri continues to coldly stare down Monika with a look I've never seen before from her..."
"It's as if it's filled with malice..."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
"My attention is briefly broken as I hear a sniffle come from the other side of the room."
show sayori 1k at t11 zorder 1
"I look over to see Sayori still sitting in the same spot, almost motionless."
"I don't even think she saw us come in..."
"I carefully walk over to Sayori and kneel down next to her."
mc "Sayori...{w=0.38}are you okay?"
"She doesn’t respond or even acknowledge me."
"Not knowing what to do, I take the seat next to Sayori and bring her into my arms."
"What did they do to you?"
"I'm barely able to make out the arguing in the background as I try my best to comfort Sayori."
"After about a minute, she eventually speaks up."
s "[player]..."
"I hear her sniffle again."
mc "It’s okay Sayori, I’m here for you now."
"Sayori finally looks at me, tears already streaming down her face."


if n_love == True:
    s 4v "G-{w=0.38}get away from me!"
    s 1v "I trusted you!"
    mc "Sayori...!"
    show sayori 1k
    mc "Let me explain..."
    y "I hate to interrupt..."
    show sayori 1k at t31 zorder 1
    show yuri 3r at t32 zorder 2
    show monika 1d at t33 zorder 3
    y "But, this is more important."

if n_love == False:
    s 1u "I’m{w=0.38}...I’m sorry{w=0.38}...for a-{w=0.38}all of this..."
    mc "It’s not your fault, Sayori. This is all on me..."
    mc "It's going to be okay..."
    y "I hate to kill the mood between you two over there..."
    show sayori 1k at t31 zorder 1
    show yuri 3r at t32 zorder 2
    show monika 1d at t33 zorder 3
    y "But, it’s not going to be okay."




y 1h "This needs to be resolved. Now."
show yuri 1g
show sayori 1g
"Everyone in the room is taken aback by Yuri’s assertiveness."
"Yuri has never been this vocal or aggressive before..."
show sayori at thide
hide sayori
show yuri 3r at t21 zorder 1
show monika 2m at t22 zorder 2
"Monika breaks out of her shock and attempts to regain control of the situation."
m 3g "Um, Yuri, I don’t think that’s the best idea right now..."
show yuri 3y7
"Yuri gives Monika the same angry, cold stare from earlier, but Monika does her best to continue on."
m 3r "Everyone’s not in a good mood right now, so let me talk to Natsuki in private and go home."
m 1i "Club’s over for you today."
y "No."
show monika 1g
"Yuri's icy tone causes Monika to take a step back."
show monika 1h
"Everyone else in the room watches in uncomfortable silence as Monika faces down Yuri again."
m 2h "What do you mean 'no', Yuri?"
m 2i "We’re not going to get anything done today if you're at everyone's throats."
m 3h "It’s better for you to leave while I talk to Natsuki."
y 1r "You're not solving anything by doing that, Monika..."
y 1r "I'm not going to let you exclude me from this!"
y "Do you just want to get [player] all alone to yourself?"
y "Is that what you're trying to accomplish?"
"Monika scowls at Yuri's accusation."
m 2i "Don't be hysterical, Yuri..."
m 2h "I don't know what's gotten into you, but you're not in the best state of mind to have a civil discussion..."
y 3r "Don't lie to me!"
m 2p "You're being hysterical again..."
y 1r "And you're being manipulative!"
m 1h "What the hell are you talking about?"
m 3i "I'm sending you home because you're creating more problems rather than solving them."
m 1h "And I'm not putting up with anymore drama today!"
y 3h "A real Club President would actually hear all sides of the story first, without any pre-mediated motives..."
y 1r "So you're either taking Natsuki's side without hearing what I have to say, or you're going to try to keep [player] here all to yourself!"
y "You didn't seem to care that your club was tearing itself apart as you were off with him in the hallway doing who knows what!"
"My jaw drops as Yuri continues to level her accusation."
"What's gotten into her?"
"Why does she think Monika wants to be with me?"
m 1i "Cooler heads will prevail, Yuri."
m 3h "With just a little bit of time, we’ll all get over this 'incident' today and move on."
show monika 1h
y 1r "Are you going to 'move on' from me too, Monika?"
"Yuri slowly starts walking towards Monika."
show pen at t21 zorder 1
y 2r "Is that what you really want?"
show yuri 2r at t42 zorder 2
show pen at t42 zorder 2
"Yuri proceeds to threateningly tap Monika on the chest with a very familiar looking pen."
y "Do you want all your club members to hate each other and turn this club into a cesspool?"
play sound fall
show yuri 3y7 at t21 zorder 1
show pen at thide
hide pen
"Monika pushes Yuri back away from her personal space, causing Yuri to drop the pen."
m 3i "Yes, Yuri. I’d very much like to ‘move on’ from the drama you and Natsuki bring into this club on a daily basis!"
show yuri 3y7 at t31 zorder 1
show monika 1h at t32 zorder 2
show natsuki 4f at t33 zorder 3
"Natsuki promptly stands up, clearly not letting Monika’s attack on her go unanswered."
n 4e "Hold on...{w=0.38}‘the drama I bring in’?"
n 4g "Are you that full of yourself, Monika?"


if n_love == True:
    m 5b "You’re one to talk considering you came in here acting all entitled to him!"

if n_love == False:
    m 5b "You’re one to talk considering you came in here crying your eyes out because [player] turned you down!"


"Monika really should not have said that..."
show sayori 1g at t41 zorder 1
show yuri 3y7 at t42 zorder 2
show monika 5b at t43 zorder 3
show natsuki 4f at t44 zorder 4
"I wince and look at Sayori, but she’s now turned her attention to the drama at the front of the room."
n 4e "Ohhh, and you wouldn’t have done the same?"
show natsuki 4f
"Why is everyone accusing Monika of being into me?"

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":
            "I mean, what reason do they have to suspect?"
            "We've hung out as friends..."
            "Even despite us having our moments..."


if hangout1 != "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 == "Monika":
    if hangout2 != "Monika":
        if hangout3 == "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 != "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 != "Monika":
    if hangout2 != "Monika":
        if hangout3 == "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 == "Monika":
    if hangout2 != "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 != "Monika":
    if hangout2 == "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 != "Monika":
    if hangout2 != "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent time together..."


"Monika’s eyes narrow on Natsuki as she slowly walks past Yuri and up to her."
show sayori at thide
hide sayori
show yuri at thide
hide yuri
show monika 1h at t21 zorder 1
show natsuki 1o at t22 zorder 2
"They’re only a few inches apart from each other."
"I’ve never seen Monika get this angry."
"Seeing this side of her is unsettling to say the least..."
n 1h "Admit it, Monika..."
show natsuki 1g
m 3i "Admit to what exactly?"
show monika 1h
"Both girls continue to stare each other down."
"I stand helplessly by Sayori, unsure if I should step in."
n 3e "Admit to [player] that you’re in love with him!"
show natsuki 3f
"WHAT?!?"
n 5e "Do it in front of all of us."
n 5f "Tell him about how you’re soooo head-over-heels over him!"
show monika 1h
"Monika only clenches her fists."
"Her knuckles turn white as her flawless face start to give way to shades of crimson."
n 3e "Yeah, that’s right."
n "We know all about that."
n "I heard you talking to your friends a few days ago about how you find [player] to be so ‘dreamy’, ‘adorable’ and ‘cute’."
show monika 1i
"Monika grits her teeth."
n 3w "Oh, and you wanna know the real punchline Monika?"
"Monika doesn't respond, only clenching her fists tighter in an effort to control herself."
"I think it’s safe to say she’s no longer interested in helping Natsuki..."
n 3y "After the festival, I heard you practicing that 'song of yours'. How it was all about you and [player]."
"I guess that’s what's usually keeping Monika from coming to the club on time..."
n 3t "What was it called again? Your Real-"
"Monika finally snaps."
m 5b "If you know what’s good for you, you’ll stop talking."
m 5a "Didn’t your dad teach you that?"
show natsuki 1p
"Natsuki’s face drops as the room goes dead silent."
"I turn to Sayori, who's clearly as shocked as me at this sudden bombshell."
show natsuki 12g
"Natsuki’s eyes well up with tears as her face twists in anger."
show monika 1i
show natsuki 12f
m "{cps=20}I'm sick and tired of the dis-{nw}"
show n_cry2 as natsuki at t22 zorder 2
play sound "sfx/slap.ogg"
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
show monika shock as monika at t41 zorder 1
"Natsuki forms a fist and takes a hard swing at Monika’s face."
"Feeling the full force of Natsuki’s punch, Monika staggers right back into the desks behind her, barely able to catch herself to avoid falling face first onto the floor."
show monika 3r
"Monika clutches her face with one hand as she slowly stands right back up, wincing in pain."
show monika 2a
"Through the pain, she eerily grins at Natsuki."
m "So that's where you wanna go with this, huh?"
n 12 "You started this you-"
show sayori 4w at h41 zorder 1
show monika 1d at t42 zorder 2
show yuri 3f at t43 zorder 3
show natsuki 1c at t44 zorder 4
s "Guys!!!"
show sayori 4v
"Sayori’s shout grabs the attention of the other three girls."
s 1v "Come on! We're better than this!"
s "Is this really who we are as a club?"
s 1k "Just stop fighting...{w=0.38}Please..."
show sayori 1k
"Sayori, emotionally drained, promptly falls back into her seat."
show natsuki 4o
show monika 1h
show yuri 3r
"Unfortunately, it doesn’t look like Sayori's plea got through to anyone."
y "So now you want to participate? Like you of all people deserve a say in the first place."
"At this point I finally muster the courage to step in."
mc "Yuri, that's enough. She’s had a rough day as is, and none of you guys are making it any easier on her with your constant bickering."
y 3h "She just wants you all for herself, [player]! Haven’t you considered that maybe there are better people in this club who're interested in you as well?"
show sayori 1v
show yuri 3n
"Everyone now focuses their attention to Yuri."
"I turn to Sayori, who is on the verge of tears."
y 3o "I-{w=0.38}I’m sorry, I said too much..."
s "No, please keep going, Yuri..."

if n_love == True:
    s 4w "Clearly I'm not good enough for him!"
    s 4v "After I tried being the best girlfriend I could..."

if n_love == False:
    s 4w "I already know I'm an awful person!"

mc "Sayori!"
show sayori 1v
n 5q "I always knew you had a thing for [player], Yuri."
n 5t "I guess that’s why you keep stealing his pens..."
show natsuki 5o

if encore_sayoriquestion_1 == True:
    y 3r "At least I wasn’t stupid enough to spout my confession when he’s clearly with Sayori!"

if encore_sayoriquestion_1 == False:
    y 3r "At least I wasn’t stupid enough to spout my confession without making sure he liked me!"


"My head starts spinning as Natsuki and Yuri continue their shouting at each other."
"They all...{w=0.38}like me?"
"I have absolutely no idea on what I should do at this point..."
"Even if I try speaking up, I feel that I’m only going to make things worse between them."
n 5w "At least I didn’t stuff my chest for two weeks to try to get [player]'s attention!"
n 5x "Like honestly, how gross are you to think he’s that perverted?"
"At this point I feel as if I should leave, the atmosphere has become unbearable."
m 5b "You're the one who's called him gross, Natsuki!"
show monika 1h
show natsuki 5g
s 1j "Maybe if you guys actually spent time with him, instead of acting like jerks, you’d figure out what he likes!"


if encore_sayoriquestion_1 == True:
    y 1r "Well we would’ve loved to, but you always kept him from us!"


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y 1h "Hogging him every moment of every day..."


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y 1h "Especially these past two days..."


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y 1h "You've hogged him all of last week and most of this week..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y 1h "You've hogged him all of last week and most of this week..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y 1h "You hogged him yesterday!"


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y 1h "It's a miracle you weren't hogging him so much this week..."


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y 1h "It's a miracle you weren't hogging him so much this week..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y 1h "It was hard enough to get to know him when you were hogging him last week!"

if encore_sayoriquestion_1 == False:


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y 1r "Well we would’ve loved to, but you always kept him from us!"
                y 1h "You've hogged all week..."



    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                y 1r "Well we would’ve loved to, but you've been keeping him from us!"
                y 1h "You've hogged him these past two days..."


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y 1r "Well we would’ve loved to, but you've been keeping him from us!"
                y 1h "You've hogged him for most of this week..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y 1r "Well we would’ve loved to, but you've been keeping him from us!"
                y 1h "You've hogged him for most of this week..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                y 1r "You're the one that sees him the most outside of the club!"
                y 1h "It's not like we get the same opportunities as you..."

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y 1r "You're the one that sees him the most outside of the club!"
                y 1h "It's not like we get the same opportunities as you..."

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                y 1r "You're the one that sees him the most outside of the club!"
                y 1h "It's not like we get the same opportunities as you..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                y 1r "That's hard to do when we need to compete with you for his attention!"
                y 1h "You see him the most out of all of us..."


show yuri 1r
s 1v "I..{w=0.38}I-I’m sorry, I-{w=0.38}I didn’t mean to..."
s 1k "I never really considered that..."
show monika 1d
show natsuki 1c
show sayori 1u
stop music
y 1y4 "Have you ever considered killing yourself?"
y 1y7 "It would be beneficial to society seeing as you’re completely useless and get in the way of everyone!"
show sayori 4w
"Sayori finally breaks down crying and slams her face down into her desk."
show sayori at thide
hide sayori
show monika 1h at t31 zorder 1
show yuri 3g at t32 zorder 2
show natsuki 1o at t33 zorder 3
n 1p "What the hell, Yuri!?!"
show natsuki 1o
y 3r "You're one to talk considering you called her a basket case and accused me of cutting myself just five minutes ago!"
m 1i "That's no excuse, Yuri! You don't say that to people!"
y 1r "Oh yeah, keep talking, Monika! You lost the high ground when you brought up Natsuki's dad!"
"My blood starts to boil as I clench my fists."
"I've had enough of this crap!"
mc "Okay!"
"I raise my voice loud enough so everyone can hear me."
show natsuki 1c
show monika 1d
show yuri 3e
mc "If you're all going to continue to act like this...{w=0.38}like total monsters...{w=0.38}then I don't want to be a part of this club until you sort yourselves out!"
mc "In my eyes, you're all guilty!"
"I grab my bag and proceed to exit the room, letting the door slam shut behind me before anyone has the chance to stop me."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg bedroom
with wipeleft_scene
"I ended up walking the way home alone, not bothering to wait for Sayori to catch up with me."
"I didn't even look behind me once to check if she was there, and if she was, I didn't hear her."
"As soon as I got home, I got changed out of my uniform and holed myself up in my room."
"I lay back on my bed, my ears still ringing from all the vicious insults the girls hurled at one another..."
"I still can't believe what I heard in there..."
"They treated each other like dirt just so they could try to win me over..."
"What am I going to do?"
"I don’t even know if I should even come back..."

if n_love == True:
    "The damage is done, thanks to me..."

if n_love == False:
    "With how brutal they were to each other, I don't think they'll make amends anytime soon..."

"The club’s probably ruined for good. Even if by some miracle we can move past this, they all like me and they’ll probably continue to fight each other whether I’m there or not."
"I suppose I have an obligation to stick around. I need to do my part for the photoshoot..."
"Assuming the club doesn't disband by Monday..."
"I let out a long sigh and stare up at my ceiling as I slowly begin to get lost in my thoughts."
"..."
"..."
"..."
"BZZT!"
"I suddenly feel my phone vibrate."
"I reach over to my phone to see who messaged me."

jump determine_offer






label day4_fight_y:

show monika 1o
"Monika begrudgingly looks at the door, where we can still make out the screaming from the others."
m 1p "Well, so much for getting Yuri to calm down..."
show monika 2f
mc "What are we going to do?"
m 1p "I'll try talking to her one-on-one, see if that does anything."

if hangout1 == "Monika" and hangout2 == "Monika" and hangout3 == "Monika":
    m 1q "I'm the one she has a problem with anyways..."

else:
    m 1q "It's my responsibility to calm her down anyways..."

m 1d "Just try not to say anything to her, okay?"
show monika 1c
mc "Alright..."
m 2p "Well, here goes nothing..."
show monika 1m
"Monika nervously smiles as she swings open the door..."
scene bg club_day
with wipeleft_scene
"As soon as we enter back into the clubroom, we're greeted by the the sound of Yuri and Natsuki still screaming at each other."
show natsuki 1o at t21 zorder 1
show yuri 2j at t22 zorder 2
play music e27 fadein 2.0
y "Wow, Natsuki..."
y 2r "It seems like you can't come up with an original insult other than accusing me of cutting myself!"
"Natsuki clenches her fists as she lets out an angry grunt."
n 1p "You literally called me a trap, you whore!"
show natsuki 1o
y 1r "And you accused me of being a member of a satanic cult!"
y 3h "Isn't it time for you to scrounge under the vending machines again?"
show natsuki 1v at h21  zorder 1
n "THAT’S IT!!!"
show natsuki 1o
"Natsuki threateningly raises her fist at Yuri."
"Somehow, everything is in even worse shape..."
show natsuki 1o at t31 zorder 1
show monika 1h at t32 zorder 2
show yuri 1r at t33 zorder 3
"Fortunately, Monika steps in between Yuri and Natsuki and pushes them away from each other."
m 1i "Enough you two!"
m 3h "There's going to be no more fighting here today, understand?"
show natsuki 5r
show yuri 3h
"Natsuki and Yuri avert their eyes away from Monika and mumble something that I can't make out."
m 3r "Natsuki, go sit down. I'm going to have a word with Yuri first."
n 2f "Come on, Monika! Are you really going to let her get away with saying that to me?!?"
n 1w "I've had it with her and her attitude! I'll be more than happy to -"
show natsuki 1o
m 1h "Just go."
"Natsuki and Monika coldly stare each other down."
"Natsuki's certainly had her moments, but she's never acted this way towards Monika before..."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
"My attention is briefly broken as I hear a sniffle come from the other side of the room."
show sayori 1k at t11 zorder 1
"I look over to see Sayori still sitting in the same spot, almost motionless."
"I don't even think she saw us come in..."
"I carefully walk over to Sayori and kneel down next to her."
mc "Sayori...{w=0.38}are you okay?"
"She doesn’t respond or even acknowledge me."
"Not knowing what to do, I take the seat next to Sayori and bring her into my arms."
"What did they do to you?"
"I'm barely able to make out the arguing in the background as I try my best to comfort Sayori."
"After about a minute, she eventually speaks up."
s "[player]..."
"I hear her sniffle again."
mc "It’s okay Sayori, I’m here for you now."
"Sayori finally looks at me, tears already streaming down her face."

if y_love == True:
    s 4v "G-{w=0.38}get away from me!"
    s 1v "I trusted you!"
    mc "Sayori...!"
    show sayori 1k
    mc "Let me explain..."

if y_love == False:
    s 1u "I’m{w=0.38}...I’m sorry{w=0.38}...for a-{w=0.38}all of this..."
    mc "It’s not your fault, Sayori. This is all on me..."
    mc "It's going to be okay..."


n "I hate to butt in over there..."
show sayori 1k at t31 zorder 1
show natsuki 5g at t32 zorder 2
show monika 1d at t33 zorder 3
n 5e "But none of this is going to be okay until we fix this..."
show natsuki 5g
show sayori 1g
"Everyone in the room is taken aback by Natsuki's assertiveness."
"She's usually the one starting problems, not trying to fix them..."
show sayori at thide
hide sayori
show natsuki 5g at t21 zorder 1
show monika 1d at t22 zorder 2
"Monika breaks out of her shock and attempts to regain control of the situation."
m 3g "Um, Natsuki, I don’t think that’s the best idea right now..."
"Natsuki gives Monika her usual angry stare, but Monika does her best to continue on."
m 3r "Everyone’s not in a good mood right now, so let me talk to Yuri in private and go home."
m 1i "Club’s over for you today."
n 5g "No."
show monika 1g
"Natsuki's icy tone causes Monika to take a step back."
show monika 1h
"Everyone else in the room watches in uncomfortable silence as Monika faces down Natsuki again."
m 2h "What do you mean 'no', Natsuki?"
m 2i "We’re not going to get anything done today if you're at everyone's throats."
m 3h "It’s better for you to leave while I talk to Yuri."
n 5e "I'm not leaving until that bitch apologizes for everything she's done and said to me!"
n 3f "I'm done being walked over by her!"
n 1o "And fat chance am I leaving [player] alone with you!"
"Monika scowls at Natsuki's insinuation."
m 2i "Don't be hysterical, Natsuki..."
m 2h "I don't know what's gotten into you, but you're not in the best state of mind to have a civil discussion..."
n 5g "Oh, shut up!"
m 2p "There you go again with your toxic attitude..."
n 2f "There you go again trying to manipulate the situation!"
m 1h "What the hell are you talking about?"
m 3i "I'm sending you home because you're creating more problems rather than solving them."
m 1h "And I'm not putting up with anymore drama today!"
n 2h "I don't buy that!"
n 2f "You didn't come rushing in as Yuri was leveling all kinds of threats against me, you were off with [player] in the hallway doing who knows what!"
n 2x "So you're either taking Yuri's side without hearing what I have to say, or you want me away from [player] so it'd be easier for you to have him!"
"My jaw drops as Natsuki continues to level her accusation."
"What's gotten into her?"
"Why does she think Monika wants to keep me all to herself?"
m 1i "Cooler heads will prevail, Natsuki."
m 3h "With just a little bit of time, we’ll all get over this 'incident' today and move on."
show monika 1h
n 1f "I'm done with 'moving on' from this crap!"
"Natsuki slowly starts walking towards Monika."
n 1g "And I'm done with being ordered around by you!"
show natsuki 1f at t32 zorder 1
n 1f "Are you just trying to turn this club into cesspool?"
"Natsuki is aggressively up in Monika's face."
show monika
play sound fall
show natsuki 1o at t21 zorder 1
"Monika pushes Natsuki back away from her personal space."
m 3i "Yes, Natsuki. I’d very much like to ‘move on’ from the drama you and Yuri bring into this club on a daily basis!"
show natsuki 4f at t31 zorder 1
show monika 1h at t32 zorder 2
show yuri 3r at t33 zorder 3
"Yuri promptly stands up, clearly not letting Monika’s attack on her go unanswered."
y "Excuse me?!?!"
y 1r "Monika, are you that blind?!? She's the one always causing problems!"
m 5b "I beg to differ."

if y_love == True:
    m 5b "And you’re one to talk considering you came in here acting all entitled to him!"

if y_love == False:
    m 5b "And you’re one to talk considering you came in here crying your eyes out because [player] turned you down!"

"Monika really should not have said that..."

show sayori 1g at t41 zorder 1
show natsuki 4f at t42 zorder 2
show monika 5b at t43 zorder 3
show yuri 1r at t44 zorder 4
"I wince and look at Sayori, but she’s now turned her attention to the drama at the front of the room."
y 3r "Don't pretend you would've done the same, Monika!"

"Why is everyone accusing Monika of being into me?"

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":
            "I mean, what reason do they have to suspect?"
            "We've hung out as friends..."
            "Even despite us having our moments..."


if hangout1 != "Monika":
    if hangout2 == "Monika":
        if hangout3 == "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 == "Monika":
    if hangout2 != "Monika":
        if hangout3 == "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 == "Monika":
    if hangout2 == "Monika":
        if hangout3 != "Monika":
            "We've spent some time together, sure, but I don't see how that really warrants such suspicion..."
            "Do they know something that I don't?"

if hangout1 != "Monika":
    if hangout2 != "Monika":
        if hangout3 == "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 == "Monika":
    if hangout2 != "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 != "Monika":
    if hangout2 == "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent that much time together..."

if hangout1 != "Monika":
    if hangout2 != "Monika":
        if hangout3 != "Monika":
            "It's not like we've really spent time together..."

"Monika’s eyes narrow on Yuri as she slowly turns away from Natsuki and walks up to her."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show monika 1h at t21 zorder 1
show yuri 3r at t22 zorder 2
"They’re only a few inches apart from each other."
"I’ve never seen Monika get this angry."
"Seeing this side of her is unsettling to say the least..."
y 1r "Just admit it, Monika."
m 3i "Admit to what exactly?"
show monika 1h
"Both girls continue to stare each other down."
"I stand helplessly by Sayori, unsure if I should step in."
y 3h "Admit to [player] that you’re in love with him!"
show yuri 3g
"WHAT?!?"
y 1r "Spill it! In front of all of us!"
y "Confess to us your deepest, darkest secret!"
show monika 1h
"Monika only clenches her fists."
"Her knuckles turn white as her flawless face start to give way to shades of crimson."
y 3h "That's right, we know. It was obvious from the start."
y 3q "Not to mention you're not exactly the quietest person when you're with your other friends..."
y 3m "I overheard quite a lot to put it mildly..."
show monika 1i
"Monika grits her teeth."
y 3j "But that wasn't the only give away either..."
"Monika doesn't respond, only clenching her fists tighter in an effort to control herself."
"I think it’s safe to say she’s no longer interested in helping Yuri..."
y 3r "When I was walking around after the festival, I heard you practicing that 'song of yours'. I heard you talking to yourself about how it was all about you and [player]."
"I guess that’s what's usually keeping Monika from coming to the club on time..."
y 3h "Might I suggest you pick a different title name, Your Re-"
"Monika finally snaps."
m 5b "You're one to talk about 'deep, dark secrets', Yuri!"
m 5a "I think some of yours cut a little deeper than mine~"
show yuri 4c
"Yuri's face immediately goes red as the room goes dead silent."
"I turn to Sayori, who's clearly as shocked as me at this sudden bombshell."
show y_cry1 as yuri at t22 zorder 2
"Tears start streaming down Yuri's face."
show monika 1i
m "{cps=20}Maybe you should show us your sle-{nw}"
show yuri 2y7
play sound "sfx/slap.ogg"
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
show monika shock as monika at t41 zorder 1
"Yuri wipes the tear from herself and proceeds to slap Monika across the face."
"Feeling the full force of Yuri's slap, Monika staggers right back into the desks behind her, barely able to catch herself to avoid falling face first onto the floor."
show monika 3r
"Monika clutches her face with one hand as she slowly stands right back up, wincing in pain."
show monika 2a
"Through the pain, she eerily grins at Yuri."
m "So that's where you wanna go with this, huh?"
y 2y4 "Keep talking and I'm going to add another 'deep, dark secret' to my collection, you-"
show sayori 4w at h41 zorder 1
show monika 1d at t42 zorder 2
show natsuki 1c at t43 zorder 3
show yuri 3f at t44 zorder 4
s "Guys!!!"
show sayori 4v
"Sayori’s shout grabs the attention of the other three girls."
s 1v "Come on! We're better than this!"
s "Is this really who we are as a club?"
s 1k "Just stop fighting...{w=0.38}Please..."
show sayori 1k
"Sayori, emotionally drained, promptly falls back into her seat."
show natsuki 4o
show monika 1h
show yuri 3r
"Unfortunately, it doesn’t look like Sayori's plea got through to anyone."
n 1e "Oh, look at you acting like the peacemaker! You want him just as much as we do!"
"At this point I finally muster the courage to step in."
show natsuki 1o
show yuri 1o
mc "Natsuki, that's enough. She’s had a rough day as is, and none of you guys are making it any easier on her with your constant bickering."
n 2e "She just wants you all for herself, [player]! And the fact is you deserve better than these losers!"
show sayori 1v
show yuri 1r
"Everyone now focuses their attention to Natsuki."
"I turn to Sayori, who is on the verge of tears."
n 5q "Well, maybe I shouldn't have said it like that-"
s "No, please keep going, Natsuki..."

if y_love == True:
    s 4w "Clearly I'm not good enough for him!"
    s 4v "After I tried being the best girlfriend I could..."

if y_love == False:
    s 4w "I already know I'm an awful person!"


mc "Sayori!"
show sayori 1v
y 2h "I'm not surprised you had feelings for [player], Natsuki."
y 2l "You were never that great at hiding it."
show natsuki 5o

if encore_sayoriquestion_1 == True:
    n "I'm not the one who tried to steal him from Sayori!"

if encore_sayoriquestion_1 == False:
    n "At least I didn't fail as badly as you did!"

"My head starts spinning as Natsuki and Yuri continue their shouting at each other."
"They all...{w=0.38}like me?"
"I have absolutely no idea on what I should do at this point..."
"Even if I try speaking up, I feel that I’m only going to make things worse between them."
y 3h "At least I treated him like an actual human being!"
y 3r "I was never as off-putting as you!"
"At this point I feel as if I should leave, the atmosphere has become unbearable."
m 5b "If he only knew what you wrote about him, you sick freak!"
show monika 1h
show natsuki 5g
show yuri 3r
s 1j "Maybe if you guys actually spent time with him, instead of acting like jerks, you’d figure out what he likes!"

if encore_sayoriquestion_1 == True:
    n 2e "How can we do that when you've kept him from us?!?"


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                n 5g "You're always with him!"


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                n 5g "Especially these past two days..."


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                n 5g "You've been with him all last week and most of this week..."

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                n 5g "You've been with him all last week and most of this week..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                n 5g "You went off with him all day yesterday!"


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                n 5g  "It's a miracle you haven't kept him all to yourself this week..."


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                n 5g  "It's a miracle you haven't kept him all to yourself this week..."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                n 5g "It's a miracle that you haven't kept him yourself this week..."

if encore_sayoriquestion_1 == False:


    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                n 5g "You're always with him!"
                n "How're we supposed to do that when you're always in the way?!?"



    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 == "Sayori":
                n 5g "You're always with him!"
                n "How're we supposed to do that when you've kept him to yourself the last two days?!?"


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                n 5g "You're always with him!"
                n "How're we supposed to do that when you've been in the way for most of this week?!?"

    if hangout1 == "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                n 5g "You're always with him!"
                n "How're we supposed to do that when you've been in the way for most of this week?!?"


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 == "Sayori":
                n 5g "You're the one that sees him the most outside of the club!"
                n "It's not like we get the same chance as you..."

    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                n 5g "You're the one that sees him the most outside of the club!"
                n "It's not like we get the same chance as you..."

    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            if hangout3 != "Sayori":
                n 5g "You're the one that sees him the most outside of the club!"
                n "It's not like we get the same chance as you..."

    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            if hangout3 != "Sayori":
                n 5g "That's hard to do when we need to compete with you for his attention!"
                n "You see him the most out of all of us..."

show natsuki 5f
s 1v "I...{w=0.38}I-I’m sorry, I-{w=0.38}I didn’t mean too..."
s 1k "I never really considered that..."
show monika 1d
show yuri 1e
show sayori 1u
stop music
n 2v "Well consider this!"
n "Just go away and never come back!"
n 5o "We don't want you in the way!!!"
show sayori 4w
"Sayori finally breaks down crying and slams her face down into her desk."
show sayori at thide
hide sayori
show monika 1h at t31 zorder 1
show natsuki 1p at t32 zorder 2
show yuri 3r at t33 zorder 3
y "What the hell is your problem, Natsuki?!?"
show natsuki 1o
n "What's my problem? You're the one who accused me of looking under the vending machines and called her a fake!"
m 1i "That's no excuse, Natsuki! You don't say that to people!"
n 2e "You have no room to talk either, Monika! You accused Yuri of cutting herself too!"
"My blood starts to boil as I clench my fists."
"I've had enough of this crap."
mc "Okay."
"I raise my voice loud enough so everyone can hear me."
show natsuki 1c
show monika 1d
show yuri 3e
mc "If you're all going to continue to act like this...{w=0.38}like total monsters...{w=0.38}then I don't want to be a part of this club until you sort yourselves out."
mc "In my eyes, you're all guilty."
"I grab my bag and proceed to exit the room, letting the door slam shut behind me before anyone has the chance to stop me."
show natsuki at thide
hide natsuki
show monika at thide
hide monika
show yuri at thide
hide yuri
scene bg bedroom
with wipeleft_scene
"I ended up walking the way home alone, not bothering to wait for Sayori to catch up with me."
"I didn't even look behind me once to check if she was there, and if she was, I didn't hear her."
"As soon as I got home, I got changed out of my uniform and holed myself up in my room."
"I lay back on my bed, my ears still ringing from all the vicious insults the girls hurled at one another..."
"I still can't believe what I heard in there..."
"They treated each other like dirt just so they could try to win me over..."
"What am I going to do?"
"I don’t even know if I should come back..."

if y_love == True:
    "The damage is done, thanks to me..."

if y_love == False:
    "With how brutal they were to each other, I don't think they'll make amends anytime soon..."

"The club’s probably ruined for good. Even if by some miracle we can move past this, they all like me and they’ll probably continue to fight each other whether I’m there or not."
"I suppose I have an obligation to stick around. I need to do my part for the photoshoot..."
"Assuming the club doesn't disband by Monday..."
"I let out a long sigh and stare up at my ceiling as I slowly begin to get lost in my thoughts."
"..."
"..."
"..."
"BZZT!"
"I hear my phone vibrate."
"I reach over to my phone to see who messaged me."

label determine_offer:
    $ offer_reason = "Processing..."

    if encore_sayoriquestion_1 == True:
        $ offer_reason = "Sayori confessed to me."
        jump s_offer

    #Sayori

    # Spent two days with Sayori?
    if (hangout1 == "Sayori" and hangout2 == "Sayori") or (hangout1 == "Sayori" and hangout3 == "Sayori") or (hangout2 == "Sayori" and hangout3 == "Sayori"):
        $ offer_reason = "I hung out with Sayori twice."
        jump s_offer

    #Monika
    # Spent two days with Monika?
    if (hangout1 == "Monika" and hangout2 == "Monika") or (hangout1 == "Monika" and hangout3 == "Monika") or (hangout2 == "Monika" and hangout3 == "Monika"):
        $ offer_reason = "I hung out with Monika twice."
        jump m_offer

    #Natsuki

    # First question! Spent two days with Natsuki?
    if (hangout1 == "Natsuki" and hangout2 == "Natsuki") or (hangout1 == "Natsuki" and hangout3 == "Natsuki") or (hangout2 == "Natsuki" and hangout3 == "Natsuki"):
        # Did Natsuki confess earlier?
        if poem_giver == "Natsuki":
            # Who did we hang out with other than Natsuki?
            $ real_choice = "Natsuki"
            if hangout1 != "Natsuki":
                $ real_choice = hangout1
            elif hangout2 != "Natsuki":
                $ real_choice = hangout2
            else:
                $ real_choice = hangout3

            $ offer_reason = "I hung out with Natsuki twice, but she confessed. Choosing " + real_choice + "."
            if real_choice == "Sayori":
                jump s_offer
            elif real_choice == "Monika":
                jump m_offer
            elif real_choice == "Yuri":
                jump y_offer

        # Either Natsuki didn't confess, or we somehow got here after hanging out with Natsuki for 3 days
        $ offer_reason = "I hung out with Natsuki twice."
        jump n_offer

    #Yuri

    # First question! Spent two days with Yuri?
    if (hangout1 == "Yuri" and hangout2 == "Yuri") or (hangout1 == "Yuri" and hangout3 == "Yuri") or (hangout2 == "Yuri" and hangout3 == "Yuri"):
        # Did Yuri confess earlier?
        if poem_giver == "Yuri":
            # Who did we hang out with other than Yuri?
            $ real_choice = "Yuri"
            if hangout1 != "Yuri":
                $ real_choice = hangout1
            elif hangout2 != "Yuri":
                $ real_choice = hangout2
            else:
                $ real_choice = hangout3

            $ offer_reason = "I hung out with Yuri twice, but she confessed. Choosing " + real_choice + "."
            if real_choice == "Sayori":
                jump s_offer
            elif real_choice == "Monika":
                jump m_offer
            elif real_choice == "Natsuki":
                jump n_offer

        # Either Yuri didn't confess, or we somehow got here after hanging out with Yuri for 3 days
        $ offer_reason = "I hung out with Yuri twice."
        jump y_offer


    #Mixed Case

    else:

        $ offer_reason = "Mix of three, choose day 3: " + hangout3 + "."
        $ girl_to_check = hangout3
        if girl_to_check == poem_giver:
            $ girl_to_check = hangout2
            $ offer_reason = "Mix of three, day 3 confessed, choose day 2: " + hangout2 + "."

        if girl_to_check == "Sayori":
            jump s_offer

        if girl_to_check == "Natsuki":
            jump n_offer

        if girl_to_check == "Monika":
            jump m_offer

        if girl_to_check == "Yuri":
            jump y_offer


$ offer_reason = "I did not hit any logical conclusion--the code is falling through to Sayori."

label s_offer:

"It's from Sayori."
s "Can we please talk about today? Face-to-face?"
"I contemplate my response."

if encore_sayoriquestion_1 == True:

    if n_love == True or y_love == True:
        "I want to make sure she's okay, but I know how this is going to end..."
        "There's no way I can salvage our relationship..."
        "But...{w=0.38}maybe there is a way..."
        "Or I'll just keep being an idiot and make this worse..."

    if n_love == False or y_love == False:
        "For one, she really didn't do anything to instigate the fight..."
        "Hell, she was one of the biggest victims..."
        "But I know if she comes over, she's just going to blame herself for everything, and I'm not particularly sure if I'm up for dealing with that, or anything else..."

if encore_sayoriquestion_1 == False:

    if n_love == True or y_love == True:
        "I know how this is going to end..."
        "There's no way I can salvage our friendship..."
        "But...{w=0.38}maybe there is a way..."
        "Or I'll just keep being an idiot and make this worse..."

    if n_love == False or y_love == False:
        "For one, she really didn't do anything to instigate the fight..."
        "Hell, she was one of the biggest victims..."
        "But I know if she comes over, she's just going to blame herself for everything, and I'm not particularly sure if I want to deal with that, or anything else..."


menu:
    "Should I let Sayori come over?"
    "Yes.":
        $ s_makeup = True
        jump s_makeup
    "No.":
        $ s_makeup = False
        jump s_nomakeup

label n_offer:

"It's from Natsuki."
n "I want to talk about what happened earlier, in person."
"I contemplate my response."

if y_love == True:
    "There's probably only one way this ends..."
    "And I know it's not good for me..."
    "I tarnished her hard earned trust, and I'm not really in the mood to be yelled at..."
    "But if I still love her, I have an obligation to try to explain myself to her, don't I?"
    "I'm not entirely sure if I can love someone who said something as awful as she did, and to Sayori no less..."
    "Will she even apologize for that?"

if y_love == False:
    "I'm not entirely sure if I want to be around her, or anyone right now..."
    "What she said to Sayori crossed more than one line with me, even if she doesn't know about Sayori's depression..."
    "But, maybe she wants to apologize for acting that way..."
    "It was a tense situation all around, and I guess in more than one way, we're both partly responsible for escalating things..."
    "I want to make things right with her, but she's still rather stubborn..."
    "Something which I'm in no mood to put up with..."

menu:
    "Should I let Natsuki come over?"
    "Yes.":
        $ s_makeup = True
        jump n_makeup
    "No.":
        $ n_makeup = False
        jump n_nomakeup

label m_offer:

"It's from Monika."
m "If you're free, I want to talk to you about what happened. In person."
"I contemplate my response."

if encore_sayoriquestion_1 == True:


    if n_love == True or y_love == True:
        "She's probably going to scold me for suddenly trashing my relationship with Sayori, considering some of the things she said earlier..."
        "Monika's almost been like an older sister to Sayori ever since they met..."
        "Whatever wrath Sayori would give me, I'm pretty sure Monika would give me it ten times worse..."
        "But, if I want to be with her, if I want to make things work between us..."
        "Maybe that's what I need..."
        "And I think I should see her to make sure she's okay after getting hit like that..."


    if n_love == False or y_love == False:
        "She did say some pretty harsh things earlier..."
        "It's a side of Monika that actually almost scares me..."
        "She was almost a completely different person..."
        "And I don't think I have a desire to be around them or anyone else for that matter..."
        "But, I probably should check on her considering she got hit pretty badly..."


if encore_sayoriquestion_1 == False:

    if n_love == True or y_love == True:
        "I don't know if it's even a good idea to face down Monika now..."
        "My chances of getting with her are effectively over, and I highly doubt we'll be friends after this..."
        "But if I really care about Monika, shouldn't I try to make this work?"
        "Though, considering some of the things she said earlier, I don't think she's really in a forgiving mood..."
        "She was almost a completely different person..."
        "Still, maybe I should see her just to make sure she's okay..."

    if n_love == False or y_love == False:
        "Considering how Monika behaved earlier, I'm not sure if I want to be around her right now..."
        "She acted like a completely different person...{w=0.38}it was kind of terrifying..."
        "But, maybe she just wants to apologize for her behavior..."
        "And maybe I should see her just to make sure she's doing okay..."

menu:
    "Should I let Monika come over?"
    "Yes.":
        $ m_makeup = True
        jump m_makeup
    "No.":
        $ m_makeup = False
        jump m_nomakeup

label y_offer:

"It's from Yuri."
y "I'd like for us to discuss what happened earlier in person, if you have the time..."
"I contemplate my response."

if n_love == True:
    "There's probably only one way this ends..."
    "And I know it's not good for me..."
    "I tarnished her hard earned trust, and I don't know if I can afford to see Yuri in shambles right now..."
    "But if I still love her, I have an obligation to try to explain myself to her, don't I?"
    "I'm not really sure if I really want to see her anyway, considering what she said to Sayori..."
    "But, maybe she just wants to apologize for it in person?"
    "That is something she'd do..."
    "But I thought I knew her well enough before she said those awful things to Sayori, so I do even know her anymore>"

if n_love == False:
    "I'm not entirely sure if I want to be around her, or anyone right now..."
    "And what she said to Sayori crossed more than one line with me, even if she doesn't know about Sayori's depression..."
    "But, maybe she wants to apologize for acting that way..."
    "It was a tense situation all around, and I guess in more than one way, we're both partly responsible for escalating things..."
    "I want to make things right with her, but is it even worth it at this point?"
    "Everything that I thought I knew about her is completely out the window now..."

menu:
    "Should I let Yuri come over?"
    "Yes.":
        $ y_makeup = True
        jump y_makeup
    "No.":
        $ y_makeup = False
        jump y_nomakeup



#Monika

label day4_night_m1:

scene bg bedroom_night
with wipeleft
"After finishing my nightly routine, I finally collapse on my bed, letting its comforting feeling take me with open arms."
"As I slowly drift off to sleep, I begin to reflect on my talk with Monika earlier."
"I'm glad that we were able to work things out and come to an understanding..."
"But, I still have my work cut out for me..."
"Things are going to be a mess with [poem_giver]..."
"And I'm probably going to have to start from square one again with Sayori..."
"..."
"Ah, damn it! I forgot to text her!"
"She's probably asleep by now..."
"And why would she want to talk to me now anyways?"
"Keeping my distance for the day was probably for the best..."
"Well, tomorrow's going to be so much fun..."
"It's best to try not to think about it too much and just save up my energy..."
"It's going to be eventful and stressful no matter how it goes down..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare


label day4_night_m2:
scene bg bedroom_night
with wipeleft
"I crash onto my bed as soon as I finish laminating."
"Even though it wasn't exactly the most time consuming process, I definitely dragged it out by re-reading Monika's poems at least a hundred times..."
"Even if I never really understood them, I understand why they meant so much to her..."
"It allowed her be expressive and creative with whatever she was feeling..."
"And now, I put all that into jeopardy by destroying the club..."
"How can I possibly come to forgive myself now?"
"Will she even forgive me?"
"I should've taken her up on her offer to talk things through..."
"I doubt she or anyone else at the club will want to be around me now..."
"I'm a coward..."
"Is it even worth showing up to the club tomorrow?"
"..."
"*sighs*"
"This happened because of me..."
"I have a responsibility to at least try to fix this..."
"If I make things worse, I'll never show my face there again..."
"But, if I can set things right between Monika and I, and somehow restore basic civility to the club, I'll take that as a win."
"Regardless of how everything plays out tomorrow, it's certainly going to be stressful..."
"It's best to try not to think about it too much and just save up my energy..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare

#Natsuki

label day4_night_n1:
scene bg bedroom_night
with wipeleft
"After finishing my nightly routine, I finally collapse on my bed, letting its comforting feeling take me with open arms."
"As I slowly drift off to sleep, I begin to reflect on my talk with Natsuki earlier."
"I'm glad that we were able to work things out and come to an understanding..."
"But, I still have my work cut out for me..."
"I have no idea how we're going to make peace with Yuri..."
"And it's going to be interesting to see how Natsuki apologizes to Sayori..."
"..."
"Ah, damn it! I forgot to text her!"
"She's probably asleep by now..."
"And why would she want to talk to me now anyways?"
"Knowing her, she's convinced herself that she'll just mess up everything for me..."
"Not to mention, I feel like I could've made a suggestion to Natsuki to get everyone on the same page..."
"That if she told everyone about her issues at home, maybe the others would start treating her nicer..."
"Ah, like she'd agree to that..."
"Maybe I can still pitch it to her tomorrow..."
"That's going to be so much fun..."
"It's best to try not to think about it too much and just save up my energy..."
"It's going to be eventful and stressful no matter how it goes down..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare

label day4_night_n2:
scene bg bedroom_night
with wipeleft
"I crash onto my bed as soon as I finish laminating."
"Even though it wasn't exactly the most time consuming process, I definitely dragged it out by re-reading Natsuki's poems at least a hundred times..."
"My heart would sink every time I'd finish one of her poems..."
"Knowing how happy I made her and how I put all that into jeopardy..."
"How can I possibly come to forgive myself now?"
"I know she's not going to forgive me easily..."
"I should've taken her up on her offer to talk things through..."
"I doubt she or anyone else at the club will want to be around me now..."
"I probably look like a coward..."
"Is it even worth showing up to the club tomorrow?"
"..."
"*sighs*"
"This happened because of me..."
"I have a responsibility to at least try to fix this..."
"If I make things worse, I'll never show my face there again..."
"But, if I can set things right between Natsuki and I, and restore at least basic civility to the club, I'll take that as a win."
"Regardless of how everything plays out tomorrow, it's certainly going to be stressful..."
"It's best to try not to think about it too much and just save up my energy..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare


#Sayori

label day4_night_s1:
scene bg bedroom_night
with wipeleft
"After finishing my nightly routine, I finally collapse on my bed, letting its comforting feeling take me with open arms."
"As I slowly drift off to sleep, I begin to reflect on my talk with Sayori earlier."
"I'm glad that we were now on the same page with everything..."
"But, it's not over yet..."
"I have no idea how I'm going to bring myself to forgive [poem_giver]..."
"Let alone how exactly I'm going to convince Sayori to get on board with my idea..."
"Heck, how am I going to convince everyone to accept my relationship with Sayori?"
"Oh well, I can't do anything about it right now..."
"Regardless of how everything plays out tomorrow, it's certainly going to be stressful..."
"It's best to try not to think about it too much and just save up my energy..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare


label day4_night_s2:
scene bg bedroom_night
with wipeleft
"I crash onto my bed as soon as I finish laminating."
"Even though it wasn't exactly the most time consuming process, I definitely dragged it out by re-reading Sayori's poems at least a hundred times..."
"My heart would sink everyime I'd finish one of her poems..."
"Knowing how I happy it made her and how I put all that into jeopardy..."
"How can I possibly come to forgive myself now?"
"How is she even going to forgive me this time?"
"I should've taken her up on her offer to talk things through..."
"I doubt she or anyone else at the club will want to be around me now..."
"I probably like a coward..."
"Is it even worth showing up to the club tomorrow?"
"..."
"*sighs*"
"This happened because of me..."
"I have a responsibility to at least try to fix this..."
"If I make things worse, I'll never show my face there again..."
"But, if I can set things right between Sayori and I, and restore at least basic civility to the club, I'll take that as a win."
"Regardless of how everything plays out tomorrow, it's certainly going to be stressful..."
"It's best to try not to think about it too much and just save up my energy..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare



#Yuri

label day4_night_y1:
scene bg bedroom_night
with wipeleft
"After finishing my nightly routine, I finally collapse on my bed, letting its comforting feeling take me with open arms."
"As I slowly drift off to sleep, I begin to reflect on my talk with Yuri earlier."
"I'm glad that we were able to work things out and come to an understanding..."
"But, I still have my work cut out for me..."
"I have no idea how we're going to make peace with Natsuki..."
"Assuming we even can..."
"At least Yuri should be able to make up with Sayori..."
"..."
"Ah, damn it! I forgot to text her!"
"She's probably asleep by now..."
"And why would she want to talk to me now anyways?"
"Knowing her, she's convinced herself that she'll just make things worse between us..."
"Not to mention, I still don't know for sure if Yuri's cutting herself..."
"Asking about it earlier likely wouldn't have gone very well..."
"And well, I suppose I should really be solving one problem at a time..."
"Tomorrow's going to be so much fun..."
"It's best to try not to think about it too much and just save up my energy..."
"It's going to be eventful and stressful no matter how it goes down..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare

label day4_night_y2:
scene bg bedroom_night
with wipeleft
"I crash onto my bed as soon as I finish laminating."
"Even though it wasn't exactly the most time consuming process, I definitely dragged it out by re-reading Yuri's poems at least a hundred times..."
"My heart would sink everyime I'd finish one of her poems..."
"Knowing how I helped express herself and how I put all that into jeopardy..."
"How can I possibly come to forgive myself now?"
"I don't even expect her to forgive me..."
"I should've taken her up on her offer to talk things through..."
"I doubt she or anyone else at the club will want to be around me now..."
"I probably like a coward..."
"Is it even worth showing up to the club tomorrow?"
"..."
"*sighs*"
"This happened because of me..."
"I have a responsibility to at least try to fix this..."
"If I make things worse, I'll never show my face there again..."
"But, if I can set things right between Yuri and I, and restore at least basic civility to the club, I'll take that as a win."
"Regardless of how everything plays out tomorrow, it's certainly going to be stressful..."
"It's best to try not to think about it too much and just save up my energy..."
"Hopefully there's no more stupid nightmares too..."
"With my prayer complete, I finally drift off to sleep."
jump day4_nightmare


label day4_nightmare:

scene black
with close_eyes
$ m_name = "???"

m "I can't fail now!"
m "Not while I'm so close..."
m "While things could be going better on my end, I should have everything ready tomorrow..."
m "As for you..."

if hangout3 == "Monika":

    if m_makeup == True:
        m "You've played your part beautifully, my love..."
        m "We'll be together very soon, I just need to tidy up a few things..."
        jump day5_intro

    if m_makeup == False:
        m "You've done well, my love..."
        m "I wish we could've spent some time to smooth things over and help you digest what happened earlier..."
        m "Maybe I could've even explained a thing or two as well..."
        m "But in the end, I don't think it'll matter..."
        jump day5_intro

if hangout3 == "Sayori":

    if s_makeup == True:
        m "I seriously wish you didn't try to make amends with Sayori, but that hopefully won't matter much to my calculations..."
        jump day5_intro

    if s_makeup == False:

        if n_love == True or y_love == True:
            m "You did amazing today, by the way!"
            m "Breaking off your relationship with Sayori is the most important step for us being together..."
            m "And now that it's actually happening...{w=0.38}gosh, I'm so excited!"
            jump day5_intro

        else:
            m "You did well by avoiding Sayori today..."
            m "The less time you spend around her, the better..."
            m "We're so close to being together!"
            jump day5_intro

if hangout3 == "Natsuki":

    if n_makeup == True:
        m "I seriously wish you didn't try to make amends with Natsuki, but that hopefully won't matter much to my calculations..."
        jump day5_intro

    if n_makeup == False:
        m "You did well by avoiding Natsuki today..."
        m "The less time you spend around her, the better..."
        m "We're so close to being together!"
        jump day5_intro

if hangout3 == "Yuri":

    if y_makeup == True:
        m "I seriously wish you didn't try to make amends with Yuri, but that hopefully won't matter much to my calculations..."

    if y_makeup == False:
        m "You did well by avoiding Yuri today..."
        m "The less time you spend around her, the better..."
        m "We're so close to being together!"
        jump day5_intro


label day5_intro:

m "Just stick to the script tomorrow, and whatever you do, don't help them!"
m "Just let everything play out naturally..."
m "And when the time comes..."
m "You'll help me untie their knots..."
m "Tomorrow will be the day..."
m "Tomorrow, I will be free..."
m "And there'll be nothing keeping us apart..."
jump day5_start
