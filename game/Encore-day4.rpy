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
    "However, I still feel unerved from the whole experience..."
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

    "I simply stare at the celling through my hazy vision as I attempt to process my experience."
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
    "Fortunately it seems that my body has recovered from the ordeal, and I feel pretty much back to normal."
    "But, something continues to nag me in the back of my mind."
    "Maybe if I ignore it, it'll go away..."
    mc "Let's get this over with..."
    "I mutter to myself as I begin my morning routine."
    scene bg residential_day
    with wipeleft_scene
    "I ended up getting ready a few minutes earlier than I normally do, so I decided to take the time to wait outside for Sayori outside."

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
        "If I want to get closer to Natsuki, I should take ths opportunity..."

mc "Yeah sure! I'd love to read it with you!"
n "That's awesome! I'll tell you: you're really going to like it!"
mc "Looking forward to it!"
n "You know where to find me when you get to the club!"
mc "I'll head straight to the closest as soon as I get in!"
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

label y_text:

"That's a first for her..."
y "Hello..."
"I can certainly feel Yuri's shyness through the screen."
"I just need to play it cool..."
mc "Hey! What's up?"
"I see the notification that Yuri's typing, so I give her a few moment as I finish getting my things out for class."
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
"I put my phone back in my pocket as a large smile comes across my face."
"I'm going get to spend more time with Yuri! This is great!"
"I wonder what else we'll be able to do today..."
jump day4_club


label day4_club:
"As soon as I finish my thought, the teacher comes in and tell us to put away our phones as he prepares today's lesson."
"Here we go with another boring day of school..."
"At least I have the club to look forward to..."
stop music fadeout 2.0
scene black
with dissolve_scene_full
scene bg class_day
with open_eyes
"The rest of the school day goes by rather quickly, and I was able to get through it without much incident."
"I occasionally got a headache and every now and then the same mysterious sense of dread washed over me, but it never lasted more than a few minutes."
"I also tried to use my time druing lunch period to try to work out my feelings towards [poem_giver]."
"Trying to settle on my exact feelings for her was hard, but I think I've generally worked out what I could say to her..."
"Though I'm dobutful that she'll ask me about it today."
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
mc "Not that'll ever happen..."
"We wait for a few minutes for the hallways to thin out a little so we can get to the stairs without a hassle."
"While we're waiting, Sayori turns to me."
s 1c "So, how was your day?"
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

if sayori_hangout == True:
    show sayori 1e
    mc "How come you didn't tell me this last night?"
    mc "I would've helped you studied..."
    s 1l "I didn't remember until after I got home..."
    "I once again shake my head in disappointment."
    show sayori 1e
    mc "Sayori, you got to do better than that..."
    mc "If you don't pay attention to your grades, you're going to fall behind again..."
    s 1h "It's just one test, [player]..."
    s 1l "I think I've done alright on all the others..."
    mc "Well, I just don't want a repeat of seventh grade..."
    mc "That was a nightmare to pull your grades back up..."
    s 4h "But we did it!"
    mc "Barley."
    s 1l "Come on, [player], don't you trust me?"
    stop music
    mc "Not on important things, no."
    show sayori 1e

if sayori_hangout == False:
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



if natsuki_hangout == True or monika_hangout == True or yuri_hangout == True:
    show sayori 1e
    mc "How come you didn't study last night?"
    mc "I would've helped..."
    s 1l "I saw you walk off with [hangout3] and I didn't want to disturb you guys..."
    "I feel my body nearly tremble with horror as I quickly become afraid at the prospect that Sayori might be getting the completely wrong idea here..."
    mc "We just hungout, Sayori..."

    if natsuki_hangout == True:
        mc "Natsuki and I went to the bookstore to pick up the latest edition of Parafit girls..."

    if monika_hangout == True:
        mc "Monika and I just took a walk together..."

    if yuri_hangout == True:
        mc "Yuri and I went to check out this new nature perserve that just opened..."

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


    if hangout1 != "Sayori":
        if hangout2 == "Sayori":
            mc "If you told me you had a test, I would've happily helped out..."
            s "Then I would've kept you from spending time around [hangout3]..."
            mc "It doesn't matter, Sayori."
            s 1l "Don't you think I can handle important things like this on my own?"
            stop music
            mc "Not really, no."


    if hangout1 == "Sayori":
        if hangout2 != "Sayori":
            s 1l "Well these past 2 days I've certainly felt like one..."
            s 1g "You really haven't been around to help me..."
            mc "I know, and I'm sorry..."
            s 1l "So I have a hard time believing that you would want to willingly help me with something important now."
            s "Don't you think I can handle things by myself?"
            stop music
            mc "Not really, no."


    if hangout1 != "Sayori":
        if hangout2 != "Sayori":
            s 1l "I'm having a hard time believing that, [player]..."
            s 1g "It's not like you've been around me all that much lately..."
            mc "I know..."
            s 1l "So I kind of have a hard time believing that you would want to willingly help out now..."
            s "Don't you think I can handle things by myself?"
            stop music
            mc "Not really, no."



show sayori 1e
"Sayori stares at me as the air between us suddenly becomes unusally heavy."
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
"The rest of the walk to the clubroom was silent, as Sayori barley even acknowledged me."
"I kept mentally kicking myself over and over for how stupid I was to say it like that."
"Who knows how long she'll be like this..."

if hangout3 == "Sayori":
    "I dobut she'll want to spend time around me now..."

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
"Before Monika can greet us, Sayori promptly goes to her ususal spot and stares blankly at the wall."
"Monika shoots me a concerned look but I raise my hand at her to let her know I have it under control."
show monika at thide
hide monika
"Without a word, Monika returns to the teacher's desk as I gingerly put my stuff on a desk in the middle of the room."
show sayori 1k at t11 zorder 1
"I look over to Sayori, whose still staring blankly at the wall."
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
    "How could've I messed up this badly?"

if encore_sayoriquestion_1 == True:
    "I really suck at this whole boyfriend thing, don't I?"

if encore_sayoriquestion_1 == False:
    "I suck at being a friend to her..."

"Through my intenral self-deprication, I begin to space out."
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
    n 3q "Do you mind if we talked outside?"
    "I feel another wave of dread wash over me as I hear that."
    "Oh no..."
    "Please don't let this be what I think it is..."
    mc "Why outside?"
    n 1m "It's...{w=0.38}really important..."
    n 1s "I don't want anyone else to hear..."
    mc "Uh, sure..."
    "I recluctantly start walking towards the door with Natsuki as my mind begins racing with all sorts of possibilities for why she wants to talk to me."
    show monika 1c at t21 zorder 1
    show natsuki 1g at t22 zorder 2
    "However, were stopped right at the doorway by Monika, who looks on at us with a curious expression."
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

    mc "Laides, ladies!"
    show monika 1d at h21 zorder 1
    show natsuki 1c at h22 zorder 2
    "I raise my hands calmly in an attempt to diffuse the argument."
    show natsuki 1s at t22 zorder 2
    mc "We'll be right outside, it'll be just a few minutes. Just get us when we're about to start, okay?"
    show monika 1r at t21 zorder 1
    "Monika lets out a defeated sigh."
    m 3q "Fine. I'll give you guys two minutes."
    mc "Thank you, Monika."
    show monika 1h
    "Monika angirly stares at Natsuki for her to say the same, but she mantains her eye contact with the floor."
    show monika at thide
    hide monika
    show natsuki 1s at t11 zorder 1
    "Monika then brushes past us and goes back to the teacher's desk."
    n 1q "Come on..."
    "Natsuki mutters as she opens the door and walk out into the hallway."
    show natsuki at thide
    hide natsuki
    jump day4_confession



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
    "I recluctantly start walking towards the door with Yuri as my mind begins racing with all sorts of possibilities for why she wants to talk to me."

    show monika 1c at t21 zorder 1
    show yuri 1f at t22 zorder 2
    "However, were stopped right at the doorway by Monika, who looks on at us with a curious expression."
    m 2d "Where are you two off to?"
    y 1h "Not now, Monika..."
    m 2g "Excuse me?"
    y 1r "I said it's none of your bussiness!"
    show monika 2h
    "Monika is clearly caught off-guard by Yuri's angry tone, but she doesn't yield."
    m 4i "Actually, Yuri:{w=0.38} it is my business."
    m 2h "It's my responsbility to know where you two are off to."
    m 2h "Especially since we're going to start today's activity in a few minutes."

    if hangout3 == "Yuri":
        m 3i "I don't want you guys to disappear for ten minutes again."
        y 3r "Pardon me, Monika, but we didn't 'disappear'!"

    if hangout3 == "Sayori" or hangout3 == "Natsuki":
        m 3i "I don't want [player] wandering off again..."
        y 3r "Pardon me, Monika, but he's not going to 'wander off'!"

    if hangout3 == "Monika":
        m 3i "I don't want you two to wander off just right when we're about to start."
        y 3r "Pardon me, Monika, but didn't you two disappeared yesterday? That's a double standard, don't you think?"

    mc "Laides, ladies!"
    show monika 1d at h21 zorder 1
    show yuri 3n at h22 zorder 2
    "I raise my hands calmly in an attempt to diffuse the argument."
    show yuri 4c at t22 zorder 2
    mc "We'll be right outside, it'll be just a few minutes. Just get us when we're about to start, okay?"
    show monika 1r at t21 zorder 1
    "Monika lets out a defeated sigh."
    m 3q "Fine. I'll give you guys two minutes."
    mc "Thank you, Monika."
    show monika 1h
    "Monika angirly stares at Yuri for her to say the same, but she seems to embarrassed to say much."
    show monika at thide
    hide monika
    show yuri 4c at t11 zorder 1
    "Monika then brushes past us and goes back to the teacher's desk."
    y "I guess we can go now..."
    "Yuri mutters as she opens the door and walk out into the hallway."
    show yuri at thide
    hide yuri
    jump day4_confession



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
"The air is becoming increasingly fraught with tension as we both struggle to mantain eye contact."
"A pit forms in my stomach as my brace for what I always thought to be the inevitable..."
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
mc "So...{w=0.38}why did you want to talk about?"
n 5q "I think we both know the answer to that..."
mc "Eh?"
play music e19 fadein 1.0
n 1m "[player]..."
show natsuki 1n
"Natsuki looks me directly in the eyes as she slowly starts scootching herself torwards me."
n 1m "I...{w=0.38}I really haven't done this kind of thing before..."
n 1q "I never really got the chance to tell a boy how much I liked them..."
n 1m "Or how much they mean to me..."
n 12b "Because, one way or another, we'd always stop talking before I could tell them..."
n 12c "It really hurts when you like someone, and after a while for some stupid reason, they don't talk to you anymore..."
n 12d "And I'm afraid that with you...{w=0.38}that this is might be one of those times..."
n 12e "I'm afraid that you're just going to stay away me, riding off with somebody else..."
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
n 12c "I tried acting cold as possible around you because I was afraid to catch feelings..."
n 12b "I didn't want to get hurt again..."


if encore_sayoriquestion_1 == True:


    if encore_festivalquestion_2 == "Natsuki":
        n 5m "But...{w=0.38}that changed last Sunday..."
        n 5n "I couldn't stop from feeling...{w=0.38}comfortable around you..."
        n 5q "You really let me be myself..."
        n 5m "Not to mention how much fun we had together at the festival too!"

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":
                n 5q "As we've hungout more, I just couldn't stop thinking about you..."
                n 5n "I even started writing poems about you!"
                n 12a "It was pretty much then when I realized that I loved you..."
                n 5y "And...{w=0.38}as much as I tried to control my feelings, I kinda let it slip on Tuesday just to see how you'd react..."
                n 1l "It made me really happy that you didn't completetly freak out..."
                n 5u "I was still too scared to tell you directly how I felt, so I decided to give you that special letter..."
                n 5n "My confession letter."
                n 5m "I figured you must of read it because I heard of how you were kind of acting like a manaic yesterday morning..."
                n 5q "And how awkward you've been acting around me lately..."
                n 3t "So I figured:{w=0.38}well there's no turning back now..."
                n 1u "I should just give it to you straight...."


        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":
                


        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":

if encore_sayoriquestion_1 == False:


    if encore_festivalquestion_2 == "Natsuki":

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":

        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":


if encore_sayoriquestion_1 == True:

    if encore_festivalquestion_2 == "Yuri":

        if hangout1 == "Natsuki":
            if hangout2 == "Natsuki":

        if hangout1 != "Natsuki":
            if hangout2 == "Natsuki":

        if hangout1 != "Natsuki":
            if hangout2 != "Natsuki":
