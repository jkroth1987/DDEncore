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

if hangout3 == "Monika":
    "Monika..."

    if m_makeup == True:
        "How're things going to go down with her?"
        "I'm sure that Monika can smooth things over with [poem_giver], but..."
        "Are things really going to be the same after today?"
        "I don't think Monika's the type of person who can just forgive a person for hitting her like that..."
        "But, it's been a strange few days. Who knows what will happen..."
        jump day5_swalk


    if m_makeup == False:
        "How's she going to react when she sees me?"
        "I really wish we got to talk about what happened..."
        "Even though what she said to [poem_giver] was awful, I can't entirely pin the blame on her."
        "It's ultimately my fault everything happened..."
        "And Monika probably thinks I'm blaming it all on her."
        "Well, maybe we'll get to smooth things over in the club."
        "There's certainly going to be plenty to talk about..."
        jump day5_swalk

if hangout3 == "Sayori":
    "Sayori..."

    if s_makeup == True:

        if poem_giver == "Natsuki":
            "I know she said she's going to make things up with Yuri after waht she said, but can she?"
            "Will Yuri even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Natsuki?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Natsuki and the others to back off and respect our relationship."
                jump day5_swalk

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Natsuki?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk



        if poem_giver == "Yuri":
            "I know she said she's going to make things up with Natsuki after what she said, but can she?"
            "Will Natsuki even give her that chance?"

            if encore_sayoriquestion_1 == True:
                "And how is she going to settle things with Yuri?"
                "She's clearly not comfortable with the idea of me being with somebody else..."
                "But, I trust Sayori. I'm sure she can convince Yuri and the others to back off and respect our relationship."
                jump day5_swalk

            if encore_sayoriquestion_1 == False:
                "And how is she going to react around Yuri?"
                "Sayori obviously still has feelings for me..."
                "She's clearly not ready to handle me being in a relationship with someone else quite yet..."
                "But, if I know Sayori, I'm sure she'll make peace with everyone."
                "She's probably the only one who's willing to try at least..."
                jump day5_swalk



    if s_makeup == False:

        if n_love == True or y_love == True:
            "I really should've talked to her yesterday..."
            "Now it feels like I'm walking into this whole thing blind!"
            "Then again, I'm about to meet her in a few minutes..."
            "Maybe we'll talk about everything then..."
            "If she's better that this..."
            jump day5_swalk



        else:
            "I dobut she even wants to talk to me right now, let alone see me!"
            "I should've taken her up on the chance to talk things through..."
            "Who knows what kind of state of mind she's in?"
            "Well, hopefully she's feeling better about everything now..."
            "I just hope I didn't struck too bad of a nerve..."
            jump day5_swalk


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
        jump day5_swalk

    if n_makeup == False:
        "I really should've talked things through with her yesterday..."
        "She probably thinks I either hate her or I'm pinning all this on her..."
        "On the other hand, maybe she's cooled off..."
        "I know I can't run from her forever."
        "Maybe I'll get to talk to her before the club today."
        "There's definitely a lot to talk about..."
        "And I need to talk to Sayori too..."
        "Well, she should be waiting outside for me..."
        jump day5_swalk



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
        jump day5_swalk


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
        jump day5_swalk



label day5_swalk:

"I finish putting the dishes away, grab my backpack, and headout to meet Sayori."
scene bg residential_day
with wipeleft_scene



if s_makeup == True:
    "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
    jump sd5_1



if s_makeup == False:


    if encore_sayoriquestion_1 == True:

        if n_love == True or y_love == True:
            "I walk out the front door and look around to see that Sayori is no where to be seen."
            "As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
            jump sd5_2


        if n_love == False or y_love == False:
            "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
            jump sd5_1


    if encore_sayoriquestion_1 == False:

        if n_love == True or y_love == True:
            "I walk out the front door and look around to see that Sayori is no where to be seen."
            "As I'm pulling out my phone to text her, I notice out of the corner of my eye something hanging on my door."
            jump sd5_2


        if n_love == False or y_love == False:
            "As soon as I walk out the front door, I already spot Sayori waiting for me on the sidewalk."
            jump sd5_1



label sd5_1:

label sd5_2:
