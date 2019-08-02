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
    "Seeing as the light from outside is starting to creep through my blinds, I turn my head to check my alarm clock."
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

    "I try to prop myself up, but I feel a sudden rush of pain hit my forehead, forcing me to lay back down."
    "My vision becomes blurry as I furiously blink several times in an effort to restore it back to normal."
    "Well...{w=0.38}at least I don't need to get up particularly soon..."

    if hangout3 == "Sayori" or hangout3 == "Natsuki" or hangout3 == "Yuri":
        "I would go back to sleep but I'd rather not dream of being attacked by [hangout3] again..."

    if hangout3 == "Monika":
        "I would go back to sleep but I'd rather not listen to any more that voice's creepy ramblings..."

    "I simply stare at the celling as I attempt to process my experience."
    "These nightmares are just getting stranger and stranger..."
    "And I don't see it stopping anytime soon..."
    "On the bright side, I don't feel nearly as awful as I did yesterday. So I suppose that's progress..."
    "I guess this weekend I could try scheduling a doctor's visit about all this..."

    if tell_s == True:
        "Maybe I can bring Sayori with me too..."
        "Hopefully we can try to solve two problems at once that way..."

    if tell_s == False:
        "I should tell Sayori about this too..."
        "Maybe I need to just get this off my chest rather than have it lingering inside of me..."

    "I simply let out a sigh and stare at my celling, waiting for my headache to dissipate."
    "As I try to pass the time before I need to get out of the bed, it still hits me that I'm still no where close to deciding on what to say to [poem_giver]."
    "Though, I don't really expect her to talk to me given how yesterday went..."

    if hangout3 == "Monika":

        if monika_hangout == True:
            "But I think I've pretty much decided on my feelings for Monika..."

            if encore_sayoriquestion_1 == True:
                "Even if I'm still shaky on the prospect of breaking up with Sayori..."

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
            "I think I've settled on my feelingd for Sayori at this point..."

            if encore_sayoriquestion_1 == True:
                "And I don't see a reason to break up with her..."

            if encore_sayoriquestion_1 == False:
                "I do think that I could at least try to give her a chance, if she's still willing..."

        if sayori_hangout == False:
            "I think I've settled on my feelingd for Sayori at this point..."

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
    mc "Let's get this over with..."
    "I mutter to myself as I begin my morning routine."
    scene bg residential_day
    with wipeleft_scene
    "I ended up getting ready a few minutes earlier than I normally do, so I decided to take the time to wait for Sayori outside."

    if hangout3 == "Yuri":
        "Though I suppose I subconciously rushed through breakfast out of fear that Yuri was somehow hiding in the kitchen again..."

    else:
        pass

    "Leaning against the lamp post, I reflect on the last night's dreams, and try to make sense of what it's been saying."

    if hangout3 == "Sayori" or hangout3 == "Natsuki" or hangout3 == "Yuri":
        "I don't understand why I'm supposedly not allowed to spend time with [hangout3]..."
        "I'm a person with free will, I can choose who I want to spend my time with freely!"
        "But I don't understand how this voice can be jealous of me spending time with [hangout3]..."
        "Unless my subconcious is trying to tell me something..."

    if hangout3 == "Monika":
        "It seems like the voice likes it when I'm around Monika for some reason..."
        "But I don't know why that would be..."
        "Unless my subconcious is trying to get me to man up..."
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
        mc "It was the worst one yet..."
        mc "It felt so real and-"
        show sayori 1g
        s "[player]..."
        show sayori 4g at face
        play sound fall
        "Sayori suddenly steps forwards and brings me into an embrace."
        "I slowly reciprocate, feeling the warmth of Sayori's body radiating on to me."
        "Despite the tramuatic experience of last night, I already feel somewhat better..."
        s "I'm sorry you're having nightmares again..."
        s "I just wish there was something I could to help..."
        mc "You can't, and I don't know what will to be honest..."
        show sayori 1f at t11 zorder 1
        "Sayori and I break our embrace, her warmth quickly being brushed off by the cool morning breeze."
        mc "I have considered seeing my doctor about this."
        mc "Maybe there's a medical explanation for it..."
        s 2g "Well you need to do whatever you can to make it, [player]."
        s 4g "I'll support whatever you want to do."
        "Well, I guess now would be a good time to bring up my idea for Sayori..."
        mc "I'd like for you to come with me."
        "Sayori eyes me suspiciously."
        s "Eh? How come?"
        s 1l "Not that I'm opposed to going with you or anything, but..."
        s 1h "I thought it wasn't that bad..."
        mc "It's not about that..."
        show sayori 1e
        mc "It's about your rainclouds..."

        if sayori_hangout == True:
            mc "Remember the idea that I brought up with you last night?"
            s "Y-{w=0.38}yeah?"
            mc "It would mean alot to me if we both tried to solve our problems together..."
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
            mc "So, I'm going to head to the doctors this weekened..."
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
        mc "I'm noy entirley sure why I'm having them, but I'm sure it'll blow over soon."
        s 2h "Why didn't you tell me?"
        "I feel a returning sense of guilt course through me as I reflect on why I decided to keep this from Sayori."

        if encore_sayoriquestion_1 == True:
            "She is my girlfriend after all..."
            "She should be one of the first people to know if something's bothering me..."

        if encore_sayoriquestion_1 == False:
            "We've always been honest with each other about things that have been troubling us, and I feel kind of bad now for telling her about this sooner."

        mc "I...just didn't want to worry you."
        mc "You got enough going on yourself..."
        s 4g "[player]..."
        s 4h "No matter what I'm dealing with or going through, I'm always going to make time for you."
        s 1h "Don't ever forget that, okay?"
        s 1g "I don't care how I feeling or whatever I'm going through..."
        s "You're what matters to me the most!"
        "I feel a sudden rush of blood to my face as Sayri says that."
        "As much as I'm touched by what she's saying, I know she's right too..."
        "I knew I should've told her about these nightmares, just like how I should tell her about eveyrthing else that's going on..."
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
"The walk to school was a rather silent."

if hangout3 == "Sayori":
    "I ended up telling Sayori some of the details about my nightmare."
    "I avoided telling her the more guresome parts of it, but she was still disturbed all the same."

if hangout3 == "Natsuki" or hangout3 == "Yuri":
    "I ended up giving Sayori the gist of what happened in my dream about [hangout3]."
    "I left out some of the more guresome parts, but Sayori was still pretty terrified."

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
"I haven't been watching any horror movies lately, and I haven't experienced anything tramuatic since the festival..."
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
"Sayori flashes me her biggest smile that I've seen all day, which helps calms my nerves a bit."

if hangout1 != "Sayori":
    if hangout2 != "Sayori":
        if hangout3 != "Sayori":
            "It's been a while since we've goten to enjoy each other's company..."
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
"Sayori quickly scrams into her classroom, her face flush with embrassment."
"Even I can feel my own face running hot."
"In an effort to not draw attention to myself, I speedwalk to my classroom."
scene bg classroom
with wipeleft_scene
play music t3 fadein 1.0
"In what has to be record time, I arrive at my fairly empty classroom."
"Only a few early birds were sitting in their seats by the time I got there."
"I walk to the back of the room to my usual spot and begin unpacking my stuff for class."
"However, as I'm doing that, my pocket vibrates."
"I pull out my phone to see that I've gotten a text..."
"It's from [hangout3]..."

if hangout3 == "Sayori":
    "It's not that often we text each other given that we see each other in person a lot..."
    "Not to mention we just saw each other..."
    s "You feeling okay?"
    "I feel a smile creep across my face as I read that."
    "Still, I was a little worried before that Sayori would overeact that something was wrong with me."
    "I really do appreciate her concern though."
    mc "Yes, I'm feeling fine. You don't need to worry."

    if encore_sayoriquestion_1 == True:
        "I add a heart emoji to the text for good measure as I send the text."
        "Sayori responds about a half minute later."
        s "Okay...just wanted to make sure!"
        "I then get a kissing face emoji from her."
        "I try to hide my grin from my classmates as I send one back to Sayori as well."
        "As I finish getting ready for class my phone rings once again."
        "I look over to read the text."
        s "Do you want to hangout in the club later?"
        "I contemplate my response."

        if hangout1 == "Sayori":
            if hangout2 == "Sayori":
                "She just porbably wants to make sure I'm doing okay..."
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
                "After all, we're both trying to move past everything that's happened betweem us..."


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



if hangout3 == "Natsuki":
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
            "If I want to get closer to Natsuki, I should take ths opportunity..."

mc "Yeah sure! I'd love to read it with you!"
n "That's awesome! I'll tell you: you're really going to like it!"
mc "Looking foward to it!"
n "You know where to find me when you get to the club!"
mc "I'll head straight to the closest as soon as I get in!"
n "Great! TTYL!"
mc "Bye!"
"I put my phone down as I send the last text and smile to myself."
"This is great! I get to spend today with Natsuki!"
"I wonder what else aside from reading we'll get to do..."
jump day4_club


if hangout3 == "Monika":
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
    m "If you want before the club offically starts we can head off back to the music room together."
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

if hangout3 == "Yuri":
    "That's a first for her..."
    y "Hello..."
    "I can certainly feel Yuri's shyness through the screen."
    "I just need to play it cool..."
    mc "Hey! What's up?"
    "I see the notifcation that Yuri's typing, so I give her a few moment as I finish getting my things out for class."
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
            "We really have been spending alot of time around each other lately..."
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
"I put my phone back in my pocket as a large smile comes across my face"
"I'm going get to spend more time with Yuri! This is great!"
"I wonder what else we'll be able to do today..."
jump day4_club


label day4_club:
"As soon as I finish my thought, the teacher comes in and tell us to put away our phones as he prepares today's lesson."
"Here we go with another boring day of school..."
"At least I have the club to look foward to..."
stop music fadeout 2.0
scene bg black
with fadeout
scene bg classroom
with fadein
