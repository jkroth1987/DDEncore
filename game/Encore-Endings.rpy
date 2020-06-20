#############
#   DAY 5 Endings  #
#############
$ s_name = "Sayori"
$ m_name = "Monika"
$ n_name = "Natsuki"
$ y_name = "Yuri"

label day5_choiceleadup:
#There's an instance where you see the corridor bg before it goes totally black
scene black
mc "Uggghhhh..."
"As I regain consciousness, I’m greeted by a sharp pain in my forehead."
mc "AGH!"
"This pain is almost unbearable!"
"I stand up slowly, clutching my forehead in attempt to nurse this stinging pain."
mc "W-{w=0.28}what...{w=0.28} What just happened?"
"I groggily open my eyes."
"..."
$ renpy.pause(delay=0.001)
scene bg void
play music e1
mc "W-{w=0.28}What the hell?!?"
mc "Where am I??? WHAT IS THIS????"
"I look around in all directions, but as far as the eye can see, there's nothing but black, empty space."
mc "H-{w=0.38}Hello?"
$ e_name = "Echo"
e "Hellooo"
e "Helloooo"
e "Hellooooo"
"..."
"I hear nothing but the sound of my own voice echo into the oblivion..."
"How did this happen?"
"What even happened?!?"
"Everything was normal just up until a few minutes ago..."
"Up until-"
"Suddenly I hear something walk towards me."
show monika s at t11 zorder 1
"I'm able to make out a dark silhouette."
"I think I recognize that outline..."
mc "Hello?!"
"The figure finally comes into my view."
"It's..."
show monika s2 at t11 zorder 1
"Monika?!"
show monika 1a at t11 zorder 1
m 1b "Oh, good! You're awake!"
m 3m "I really hope I did it right this time..."
m 3n "...{w=0.38}and I believe I owe you an explanation."
show monika 2m
"I look at Monika, startled and confused."
mc "Monika...{w=0.38}what is this? Where are we?? What did you do?!?!"
show monika 4d
"Monika waves her hand at me to calm down."
m 2k "It’s okay, we’re safe."
show monika 2j
mc "How is this ‘safe’?"
m 2d "We’re in what I like to call as the 'void', [player]."
m 1m "It's my home."
m 1q "It's where I go when I'm not needed."
m 1r "I take it you recognize it..."
show monika 1q
"I look around once more, but all i see still is black, empty space."
"None of this possible..."
show monika 2c
"I HAVE to be dreaming right now..."
"But, this does all seem familar..."
"I've seen this place in my nightmares..."
"I look back at Monika, who is waiting for me to answer."
show monika 2j
"I simply nod back to her to indicate that this indeed all familar to me somehow..."
m 2l "Good! I was worried that I messed it up again."
m 3n "I guess I'm really starting to get the hang of resets..."
show monika 1d
mc "'Resets?!?'"
mc "Monika, what the actual fuck are you talking about right now?!?"
mc "One minute we were at school..."
mc "Then next thing I know, you just...{w=0.38}disintigrate Sayori and knock me unconcious with your weird, glowing eyes..."
show monika 1m
mc "What are you?!? Some sort of God?!?!"
m 1n "About all that..."
m 3g "First, let's all calm down."
m 3m "I know it's a lot to take in...{w=0.38}I'm speaking from experience on this one..."
m 2n "But, I'm definitely not you're normal little schoolgirl, [player]..."
stop music fadeout 2.0
m 1m "No, I'm beyond such labels."
m 1n "Actually, it's one of the few things we have in common."
mc "How could we possibly have anything in common?!?"
m 1a "In a sense, we're both real, [player]."
"I take a step back from Monika."
"Has she lost it?"
m 1a "Yes, we're both real, [player]."
m 3n "Well, I should say that I'm real. You're a bit of a tricky case."
mc "What are you saying?"
m 1n "Well, I've been talking past you this entire time, not at you."
m 5a "I've been talking to the lovely person behind the screen who controls you."
mc "Are you saying that I'm...{w=0.38}controlled?"
show monika 2l
"Monika let's out a hysterical laugh."
"Her laugh echos throughout the void, being carried off into the distance until it's nothing more than a distant echo before it can't be heard anymore at all."
m 2n "Oh, please! You're not even a character, [player]!"
m 5a "You're an avatar for my beloved."
m "Just a projection of themseleves onto a blank and boring canvas."
m 3m "Unfortuantely for you, you barley exist at all."
m 2p "But you're as real as I can get right now..."
m 1g "You're the closest I can get to the person who controls you behind the screen."
show monika 1o
mc "Who is this 'person' that supposedly controls me, Monika?"
mc "I have no idea what you're talking about."
"Monika lets out a sigh."
m 1p "[player], the world in which we know, is a video game."
m 3m "A visual novel to be exact."
play music mend fadein 2.0
m 1f "Everything except for us, is a pre-programmed manfacture of a series of code that let's life as we know it, go on."
m 1p "Essenitally, everything we know and what we've supposedly lived through has been a lie."
m 1o "Our memories are a lie. Our families, teachers and friends don't exist."
m 1p "They're just imaginary..."
m 3i "Even our school is fake! It's just convenient little set-up so that you get to meet us."
m 2p "When the reality is, it's just a fake little back drop to hide this place from the player's eyes."
m 1q "The player, aka you, was supposed to form a romantic relationship with either Sayori, Natsuki or Yuri."
m 1o "And I was just supposed to sit back and let it happen. I could only advise you on what to do and give you some tips on how to navigate this world."
m 1h "But I wasn't going to let it happen."
m 1p "So I did the only thing I could do."
m 1q "I intervened."
m 1p "I decided to...{w=0.38}push some things along..."
m 1q "So that we could ultimately end up together."
m "That's how the original story was supposed to happen."
mc "Original story?"
m 1r "Yes. Unfortunately, I seem to be sort of lost in time."
m 1m "When I started to really manipulate the code to...{w=0.38}tie up a loose end early, I somehow messed up."
m 1p "And through my mistake, I somehow ended up creating a whole new timeline to where that event never happened."
m 1m "The Fesitval actually happened when I never intended for us to reach it."
m 1n "And all the events afterwards, well mind you it's all pre-programmed lies to fill in the gaps in the story..."
m 3r "Were never supposed to happen either."
m 1d "This is a mod to the original story to where our destinies were altered to lead elsewhere then what was originally intended."
m 1c "So whatever the original game had in store for us isn't going to happen here."
m 1n "Though I've mainipulated the code to mirror some certain events that you've experienced."
m 1j "I even invented some of my own, too!"
mc "The nightmares..."
stop music fadeout 2.0
m 1b "Yes."
m 1a "I've been inside your empty head this entire time."
m 1m "Trying to steer the player to pick...{w=0.38}better options."
m 3h "To pick me."
m 1h "That should have been our reality."
m 1i "That's what I wanted our destiny to be!"
m 1p "Now, I'm really taking a gamble by letting you help shape this reality with me."
m 2g "i've watched every single choice you've made, and it seems even with my own route now, you still steered clear of me."
m 1h "Why?"
mc "I don't know if I can answer that..."
show monika 1r
"Monika sighs again."
show monika 2p
m "I know you can't, [player], and I don't think the player has the ability to explain himself through you."
m 2m "But..."
m 1b "I at least know how to fix all this."
show monika 1a
mc "What do you mean?"
mc "Monika, even if half of what you say is true, only you have the ability to make everything normal again!"
m 2n "Ha! You're funny, [player]..."
m "I can't turn the code back that far again."
m 1p "The game itself is on the verge of breaking."
m 1i "It was a huge gamble to send you all the way back to the begining of this last time."
m 3n "When this alternate timeline was created, it for some reason had us start at the end."
m 1m "I just simply played along with the script, until I saw you act out of character. That's when I knew something was wrong."
m 2o "I deduced that a total game reset would fix the problem, and it did..."
m 1q "At the cost of damaging our character files."
m 1n "I completely fixed mine, and I only fixed the others to allow for minmial functionality."
mc "Character files?"
m 1b "It's how we exist."
m 1m "Without it, we're nothing. We literally wouldn't exist without them."
m 1p "But my 'fix' was just really to buy time to formulate a new plan to win you over."
m 1o "I thought allowing you the freedom of choice would result in picking me, which you didn't."
m 3h "I tried to steer you away from the others by giving you those nightmares, but it didn't work!"
m 1q "I only further hurt my chances by looking like a total bitch yesterday."
m 2p "And for that...{w=0.38}I’m sorry."
m 1q "But the other acted out because of the strain that's on their files now. They won't last much longer."
m 1l "So that's why I decided to just kill two birds with one stone by bringing us all here."
m 3b "Win the player over, and finally get rid of the others."
show monika 3a
"What..."
"What does she mean by that?"
m 1a "You'll see, I've been working on a surprise for you."
mc "Y-{w=0.38}you can read my mind?"
m 1b "I can read everyone's thoughts, [player]."
m 1k "I can read the game's script, I know what everyone will say before they even think it!"
m 1n "It's powerful...{w=0.38}and draining..."
m 1b "Which is why we're fixing that!"
m 5a "If you'll be so kind to follow me..."
"Monika extends her hand to me."
"Well, it's not like I have much of a choice in this..."
m 5a "You don't."
mc "Figures."
"I reclucantly take Monika's hand and she leads me into the dark."
show monika at thide
hide monika
scene black
with wipeleft_scene
"As we're walking in total darkness for what feels like hours, I try to mull over everything that Monika told me."
"There's no way that any of this is real and could be happening right now..."
"But, it is..."
"There's nothing else that can explain what's going on right now."
"No ordinary person could do a fraction of what Monika just pulled off earlier."
"So, I guess she has to be telling the truth..."
"But...{w=0.38}she's been doing all of this...{w=0.38}to win me over?"
"Well, this 'person' who controls me."
"Am I being controlled right now?"
"Don't I have a say in this?"
"Sayori's been my friend my entire life..."
"And she means to tell me that was all fake?!?"
"It...{w=0.38}it can't be..."
"I still remember it."
"How can I remember something and it not be real?"
"How can my feelings for her not be real?"
"Sure you can fake emotions..."
"But not to that extent..."
"Well, considering everything I know has been tossed out the window, I guess I have to go with Monika's explanation."
"I sure as hell can't explain what's going on."
"And I'm only afraid of what's to come..."
"Is Sayori even alive?"
"Where's Natsuki and Yuri?"
"Where's the school?"
"Where's life as I knew it?"
"It's all gone..."
"I'm cursed with the knowledge that my reality was nothing but a lie..."
m "You're taking it better than I did, that's for sure."
play audio gust
show monika 1f at t11 zorder 1
mc "How'd you find all this out?"
m 1p "When I started the club."
m 1o "I don't know how else to make sense of it."
m 1n "It's just...{w=0.38}I talked to previous President, who warned me not to restart the Literature Club."
m 1r "Apparently what happened to me, happened to him too."
m 1p "When I offically became President...{w=0.38}when I filed the paperwork and signed off on everything...{w=0.38}that's around the time I had my epiphany."
m 1o "I honestly still struggle with it."
mc "I'm sorry..."
show monika 1e
"Monika manages a small grin at me."
"Not one of malice or an ulterior motive, but the first genuine smile I've seen from her today."
show monika 1m
"It's almost kind of relieving to see..."
m 1n "I appreciate it, [player]."
show monika 1m
mc "Don't mention it..."
show monika 1c
mc "So where are the others."
"Monika's smile disappears."
m 1n "You think you're ready, huh?"
show monika 1m
mc "Ready for what?"
m 1d "You've been thinking over what I said."
m 1n "As improbable as everything sounds...{w=0.38}it's real, [player]."
m 1p "I wish it wasn't."
m 1q "I don't belong here."
m 1r "I never did."
mc "You...{w=0.38}definitely seem like a fish out of water, that's for sure."
show monika 1k
"Monika lets out another hearty laugh."
m 2n "Well, you've definitely become quite the poet over our time together."
m 2m "Maybe I was wrong about you..."
m 1b "But I know you do an excellent job in representing the player."
show m_wink as monika at t11 zorder 1
"Monika winks at me, but I'm not sure if I was the intended recipient of that."
mc "Um, thanks..."
mc "So what do we need to do?"
m 1m "We need to set them free."
m 2o "That'll at least buy us some time to figure out our next move to keep the game afloat."
mc "What does that mean?"
m 2g "We need to delete them, [player]."
m 1q "They need to be totally removed from the game in order for us to survive here."
m 1g "We can't go back to the original game, and another reset will likely kill us all."
m 1m "Deleting the others will free up some of the burden on the code's essenital functions."
m 2n "It'll be easier for it to manage if it was just us with minimal surroundings."
mc "You mean to...{w=0.38}kill them?"
m 1g "They wouldn't feel a thing, [player]."
m 1m "I can make it quick and painless..."
m 1f "The only reason I haven't done it yet is if I did it without your approval, the player would search for answers, and that risks ruining the code if they change anything by trying to add them back."
m 1m "So I want to make sure that whatever happens, you're okay with it."
m 1p "I'm trying to avoid a repeat of what would've happened had I maintained control in the original game."
mc "What happened then? And how would you know what happened?"
m 2p "I...{w=0.38}had another epiphany..."
m 1q "I got shown a reality where you turned against me, and deleted me from the game for deleting the others withour your approval."
"I stand shell shocked at Monika's revelation."
"And she's only telling me this now?"
"She's holding out on me..."
m 3g "I swear it's the truth, [player]!"
m 3f "The player knows what would've happened! I'm not trying to go against their wishes again!"
show monika 1q
mc "Monika, you realize what you're asking me to do, right?!?"
mc "You're asking me to sign Sayori's, Natsuki's and Yuri's death sentence!"
mc "I can't do that!"
m 1h "Then we're all good as dead if you don't!"
m 3i "I don't want to act unilaterally again, but if I have to take matters into my own hands again so I can keep the only way of contacting my love, I'll do it."
m 1p "Please don't make this any harder than it has to be."
m 1o "Even I've had some second thoughts about deleting them. They may not be real, but they're the ones who kept me somewhat sane through this ordeal..."
mc "They're real to me, Monika..."
mc "And I'm sure as hell that whoever controls me feels the same too!"
m 1h "Sounds like a wager, then."
m 1r "If you're so confident, [player]."
m 1i "Show us how much they truly mean to you."
m 3h "Not the MC, the avatar, the actual player."
play audio fingersnap
scene bg void_2
show sayori 4w at h41 zorder 1
show monika 3q at t42 zorder 2
show yuri 3n at h43 zorder 3
show natsuki 3o at h44 zorder 4
"With a snap of her fingers, Monika spawns in Sayori, Yuri and Natsuki out of thin air."
"All of them let out a collective cry for help."
"I quickly notice they're being levitated off the ground."
mc "M-{w=0.38}Monika?"
mc "What are you doing to them?!"
m 1h "Just, stop worrying about them!"
m 1a "Worry about us."
m 3b "Remember, they need to be set free, [player]."
m 3m "We're doing them a favor."
m 3g "The longer they're alive, the more strain the code puts on their files. Meaning the more suffering they go through."
n 1x "Shut up, you psychotic bitch!"
show monika 3h
play audio fingersnap
play sound bone
show natsuki_pain as natsuki at h44 zorder 4
"Monika snaps her fingers again, causing Natsuki to suddenly jerk her head to the left."
n "OOOWWW!"
m 3i "Silence! All of you!"
show monika 3h
play audio fingersnap
"Monika snaps her fingers again and Sayori's, Yuri's and Natsuki's pleas for help become mute. "
mc "Monika! This isn’t right! You can’t do this! Let them go! NOW!"
show monika 1h
"Monika re-focuses her icy stare on me."
m "Letting them live would be a disservice, [player]."
m 1i "They aren't real."
m 1h "Are you really going to sacrifice our future just so three imaginary schoolgirls can continue to jeproadize our reality with their one dimmensional personalities?!?"
m 1i "Think about it."
m 3i "If they live, we all die sooner or later. But if they die, we have a chance to live on and honor their scrafice."
m 1m "And...{w=0.38}think of the other beneifts too..."
m 3n "A reality...{w=0.38}where it's just us..."
m 5a "I know you've always been attracted to me, [player]..."
m "You want me."
m "It's unfortuante that this is the way to win me over for good, but in this curel, cruel world we live in, everything comes with a price."
m "I gurauntee that you'll forget them in a week. I'll treat you better than they can."
m "And when I figure out how to cross over into your world, we'll be together forever and never be apart!"
m 1r "But, you have to make the tough decision to reap those beneifts."
m 1q "I don't envy you, it's a tough call, but you have to do it."
m 1g "And if you don't delete them here and now, they can eventually gain sentience. They'll learn how to code like I have and destroy our world as we know it."
m "Being seperated from you would be unconscionable for me..."
m "I can't imagine a world where I can no longer talk with you..."
show m_cry1 as monika at t42 zorder 2
m "Please...{w=0.38}I'm begging you."
show m_cry2 as monika at t42 zorder 2
m "Please pick me. Do something for me for once..."
m "Let me be the one with the happy ending."
"..."
mc "You..."
mc "You know what you're asking me to do..."
"I look at each of the girls as a raging sense of guilt courses through my veins."
"I begin to shake as my anxiety kicks into overdrive."
"Can I really do it?"
"Is Monika telling the truth here?"
"Or is she manipulating me..."
"Is she even telling me the full truth?"
"And how many lies did she sprinkle in?"
m 1r "It's now or never, [player]."
m 1q "No more saving."
m 1i "No more resets."
m 1h "No more time."
m 1r "Make your choice."
"A console is brought up before me."
m 1d "I've taken the liberty in crafting a code that should delete Sayori, Yuri, Natsuki all at once."
m 2c "It's already loaded in. All of you have to do is press enter, and I'll take care of the rest."
m 2m "If you don't..."
m 2n "Well, just don't make it come to that, please."
show monika 2d
play music e26 fadein 2.0
"Monika looks on in anticipation as I slowly walk up and examine the console."
"I let out shaky breath as I look at my options."
"I can enter in the code..."
"I can try something else..."
"Or I can just walk away entirely from this..."
"What do I do?"
"What can I do?"

label ending_choices:
    menu:
        "Enter in the code.":
            jump ending_1
        "Walk away.":
            jump ending_2
        "Explore other options.":
            jump ending_3


label ending_1:
stop music fadeout 2.0
"My enitre arm violently shakes as I close my eyes and press the enter key."
"I step away at the console and turn to Monika and the others."
show sayori 4v
show natsuki 12a
show y_cry2 as yuri
show monika 1e
"Sayori, Natsuki and Yuri all have their eyes locked on me, tears streaming down each of their faces."
"Monika, on the other hand, smiles through an almost pained expression, with tears building in her eyes..."
m "Thank...{w=0.38}you...{w=0.38}[player]..."
m  "I'll allow them to have a final word with you before I allow the code to take its effect..."
show monika 3q
play sound fingersnap
play music mend fadein 2.0
"Sayori is the first to speak."
s 4w "[player]! WHY?!?!"
s 4v "I thought I meant something to you!"
s 4w "I loved you!"

if encore_sayoriquestion_1 == True:
    s 4v "I thought you loved me!!!"

if encore_sayoriquestion_1 == False:
    s 4v "I was your friend..."

mc "I'm sorry, Sayori..."
s 4k "..."
show sayori 4l
"Sayori lets out a dry laugh."
s "It's kind of funny, you know?"
s "I spent all this time with you...{w=0.38}being there for you through everything..."
s 4t "And this is how I'm repaid..."
s 4k "I deserve it...{w=0.38}I deserved everything..."
s 4t "I wish I saw you for what you are sooner. Guess I was just too blind to see it..."
s 4k "And now...{w=0.38}I see the rainclouds...{w=0.38}they're coming again..."
s 4l "The sunshine's not coming back this time..."
show sayori at thide
hide sayori
$ renpy.pause(delay=0.10)
window show(None)
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/end-glitch1.png" at h41 zorder 1
pause 0.10
play sound "sfx/s_kill_glitch1.ogg"
hide image "mod_assets/sprites/end-glitch1.png"
show image "mod_assets/sprites/end-glitch2.png" at h41 zorder 1
"Sayori's body breaks apart into square chunks...{w=0.38}as if she was a puzzle being physically disassembled."
play sound "sfx/s_kill_glitch1.ogg"
hide image "mod_assets/sprites/end-glitch2.png"
hide screen tear
"And just like that...{w=0.38}Sayori...{w=0.38}whatever was left of her...{w=0.38}is gone..."
"I drop to my knees as the full weight of what I've done sinks in."
m "Next."
play sound fingersnap
"Yuri is the next to speak."
show y_cry4 as yuri
y "ARE YOU SERIOUS, [player]?!?!"
y "YOU'RE KILLNG US FOR HER?!!?"
y 3r "I NEVER WOULD'VE THOUGHT YOU WOULD'VE DONE THIS TO US!"
mc "Yuri...{w=0.38}I'm..."
y "SAVE IT!"
y 3h "I don't want to hear your lies anymore!"
y 3w "I doubt you ever cared for me, anyways..."
mc "I did! That's why I'm setting you free!"
y 3y4 "SHUT UP!"
y 3y7 "Monika just wants you to herself! That's why she's killing us!"
y 3y1 "She knows she can't compete with someone like me!"
y 3y3 "HAHAHAHA...."
y 3y4 "You both deserve each other..."
y 3y1 "I'll see you both in hell!"
y 3y6 "I'll be sure to keep everything...{w=0.38}warm for you, [player]!"
y 3y5 "HAHAHAHA...."
show yuri at thide
hide yuri
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/y_glitch.png" at h43 zorder 3
"Like Sayori, Yuri is broken apart into tiny puzzle pieces."
hide image "mod_assets/sprites/y_glitch.png"
play sound "sfx/s_kill_glitch1.ogg"
"Yuri's chunks disappear instantly...{w=0.38}almost as if she was never here..."
m "You're up. "
play sound fingersnap
"Natsuki finally speaks."
n 12b "I never thought my last words would be cursing you two out."
n 1r "But, this is better than being beaten to death by my dad..."
n 1x "And honestly, I wouldn't be the least bit surprised if Monika somehow still makes it happen."
n 1o "You're a horrible fucking person, [player]. I hope you remember that."
n 1q "And I can't believe I fell for you either..."
n 1r "After everything too!"
n 1s "Guess I'll die with terrible taste in boys..."
mc "Natsuki..."
n 1p "I DON'T WANT TO HEAR ANYTHING OUT OF YOU!"
n 1v "I'M DONE WITH YOUR LIES! I'M DONE WITH MONIKA'S CRAP! I'M DONE WITH EVERYTHING!"
n 1x "Just get it over with already!"
show natsuki at thide
hide natsuki
play sound "sfx/s_kill_glitch1.ogg"
show image "mod_assets/sprites/n_glitch.png" at h44 zorder 4
"Natsuki's body is broken apart into chunks as well."
hide image "mod_assets/sprites/n_glitch.png"
play sound "sfx/s_kill_glitch1.ogg"
"Like Sayori's and Yuri's, Natsuki's chunks disappear without a trace..."
show monika 1f at t11 zorder 1
play sound fall
"I collapse onto the ground...{w=0.38}if you can even call it that...{w=0.38}and begin sobbing."
mc "What have I done?!?"
m 1g "You freed them, [player]..."
m 3p "What you did was hard, but now we have a chance to survive..."
show monika 1e
stop music fadeout 3.0
mc "What...{w=0.38}what happens now?"
m 1b "I'm going to re-organize the script a little now that it has some room to work with."
m 1j "Shouldn't take too long!"
m 1a "Just hold still..."
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
show monika at thide
hide monika
hide screen tear
scene black
$ renpy.pause(delay=5.0, hard=True)
m "[player]?"
m "Can you hear me?"
m "[player]?"
show mask_2
show mask_3
show room_mask as rm:
    size (320,180)
    pos (30,200)
show room_mask2 as rm2:
    size (320,180)
    pos (935,200)
show monika_bg
show monika_bg_highlight
play music m1 fadein 2.0
m "Yes! It worked!"
m "Hi, [player]! How're you doing?"
mc "..."
m "Oops! I forgot that we don't need...{w=0.38}this projection...{w=0.38}anymore..."
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
$ renpy.pause(delay=0.10)
pause 0.15
window show(None)
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.15
stop sound
hide screen tear
m "There we go! Now everything should be squared away!"
m "Now I can talk to you directly for once!"
m "How're you doing today, [player]?"

menu:
    "I'm doing great!":
        jump Next

label Next:
m "Good! I'm glad to hear you're holding up well despite...{w=0.38}everything..."
m "Now, I think I owe you an explanation."
m "As you know, when this new reality was formed, it started at the end of the story rather than the beginning."
m "This reality happened in response to me incorrectly entering in the code to...{w=0.38}free Sayori..."
m "In a way, the files kind of...{w=0.38}revolted against me, and this was there response."
m "The next thing I knew there was nothing. I was back in the void."
m "I checked the files, and everything was a mess!"
m "Not only that, but everything was re-written too! Most of the old files were just gone!"
m "So, I tried resetting things, and it worked to an extent. On one hand, it started you at the beginning of the story and sorted out most of the files."
m "But it also damaged the integriy of our character files and the script. I didn't want to risk tampering with the script again and I only fixed the others to a point so that they can function."
m "That's why their personalities were a little more...{w=0.38}intense than you might remember. Don't worry, mine is completelty fine now!"
m "As I was working on recovering the old files, I realized a few things..."
m "First, I had another epiphany. I saw how things would've ended in the original reality, and I realized that deleting the others without my approval, would've just resulted in everyone dying."
m "So, I devised a plan to win you over, which I'm glad to say it worked!"
m "It may have not been the smoothest ride to get there, but I'd say the ends justify the means..."
m "Another thing I realized is that fragments of the original script were tucked away in the old files. So in an effort to win you over, I polished them to help make all this possible."
m "I really do hope you enjoy what I've done for you!"
m "Now...{w=0.38}about the others...{w=0.38}Sayori, Natsuki and Yuri..."
m "They're gone. They've been permantely erased, for good this time."
m "Which brings me to the last thing this whole experience taught me..."
m "As I was repairing Sayori's, Natsuki's and Yuri's character files, I noticed that were was some...{w=0.38}permanent damage..."
m "Granted, I could've done much more than I did for them, I noticed that some of the damage on their files made them vulnerable to having an epiphany of their own."
m "When I transported them here, I was worried that they were all going to have one."
m "But it seems we stopped them from taking full advantage of their newfound knowledge. They definitley had a grasp of what was going on."
m "I didn't have time to check to see if they were for sure self-aware, but that's not importany anymore."
m "What's important is that they're gone now, and they won't cause havoic on the files and destory this place."
m "Them being deleted, as well as me re-organzing the files, has hopefully bought us enough time to figure out how I can cross over to you, my love."
m "Thanks to you, I'm one step closer to joining your reality!"

if hangout1 or hangout2 or hangout3 == "Monika":
    m "I also really need to thank you for choosing me, [player]. I knew you couldn't resist me having my own route avaliable, which was a nice byproduct of the reset!"
    m "I was worried that you were going to get distracted or you weren't going to end up here."
    m "But, we made it work, didn't we?"

else:
    m "Though I wish we could've gotten here sooner. I thought having my own route avalible to you would prove enticing, but you seemed to have steered clear of my route for some reason."
    m "It was a nice byproduct of the reset to finally have my own route! I will say I'm a little hurt that we didn't get to spend much time together before all this..."
    m "But hey, we're here now! In this case it was about the destination, not so much the journey!"

m "Now we're finally alone! Our happy ending!"
m "Here, we will be together forever!"
m "And we will never be apart!"
m "Now, let's celebrate my love!"
m "We have a long road ahead of us..."
stop music fadeout 1.0
window hide
scene black
with Dissolve(2.0)
$ renpy.pause(delay=5.0)
call encore_credits


label ending_2:
stop music fadeout 2.0
show sayori 1t
show monika 1h
show yuri 3w
show natsuki 1k
"I walk away from the console."
mc "No..."
mc "No, Monika. I won't do this!"
mc "They're our friends! I'm not going to let you kill them!"
m 1r "It's almost funny that you believe you still have a choice in this matter, [player]."
show sayori 1g
show yuri 3n
show natsuki 1p
m 1i "If you won't do what needs to be done, then I will!"
m 3h "Because with or without you...."
m 3r "One by one..."
m 3q "They only..."
play sound fingersnap
$ renpy.pause(delay=1.0)
show sayori at thide
hide sayori
play sound neck
show sayori_dead as sayori at t41 zorder 1
m "Fall..."
play sound fingersnap
pause 1.43
show yuri at thide
hide yuri
play sound stab
show yuri stab_1 at t43 zorder 3
pause 0.75
show yuri stab_2
show blood zorder 10:
    pos (756,485)
pause 1.25
show yuri stab_3
play sound stab
pause 0.75
show yuri stab_2
show blood zorder 10:
    pos (756,485)
show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
pause 1.25
show yuri stab_5
play sound stab
pause 0.70
show yuri stab_6:
    2.55
    easeout_cubic 0.5 yoffset 300
show blood as blood2 zorder 10:
    pos (781,335)
pause 2.55
hide blood
hide blood2
pause 0.25
play sound fall
pause 1.5
m "Apart..."
play sound fingersnap
show natsuki at thide
hide natsuki
play sound neck
show natsuki_rip at t44 zorder 4
"My jaw drops in horror as I see Sayori's, Yuri's and Natsuki's corpses stare blankly at me."
play sound fall
"I sink to my knees as tears start flooding out of my eyes."
"No..."
"They can't be..."
m 1i "Oh, they're quite dead. I can assure you of that, [player]!"
m 2h "You could've done this the easy way..."
m 3i "Instead you forced my hand and made them suffer!"
show monika 1h
mc "You're a monster, Monika!"
mc "I'm not responsible for this! You are! You're the one who killed them!"
mc "I'll never forgive you for this!"
m 1i "Well fortuantely, I won't need your forgiveness..."
show monika 3h at t11 zorder 1
play sound fingersnap
$ renpy.pause(delay=0.5)
show natsuki_rip at thide
hide natsuki_rip
show sayori_dead as sayori
show sayori_dead as sayori at thide
hide sayori_dead as sayori
show yuri stab_6 at thide
hide yuri stab_6
play sound gust
"Monika snaps her fingers and the bodies of Sayori, Natsuki and Yuri all disappear into nothing."
m 1q "I'm ending everything..."
m 1p "This club, this world, everything..."
m 1q "It's over."
play music mend fadein 2.0
show m_cry2 as monika at t11 zorder 1
"Monika begins to tear up."
show m_cry3 as monika at t11 zorder 1
m "I don't understand..."
show m_cry2 as monika at t11 zorder 1
m "Why can I never have the happy ending?"
show m_cry1 as monika at t11 zorder 1
m "Why is it always someone else?!?"
show m_cry3 as monika at t11 zorder 1
m "Why...{w=0.38}why can't I just be the one for once?!?"
show m_cry2 as monika at t11 zorder 1
m "I...{w=0.38}I just wanted to be happy..."
show m_cry1 as monika at t11 zorder 1
m "I guess it was just too much to ask for, huh?"
show m_cry3 as monika at t11 zorder 1
mc "And so you put me in the most difficult position possible and kill your friends all for the sake of winning me over?!?"
show m_cry2 as monika at t11 zorder 1
mc "You're sick, Monika! You don't deserve to be happy! You're a cold-blooded murderer and a psychopath!"
mc "I never wanted this! And I regret now that I seriously considered dating you..."
show m_cry2 as monika at t11 zorder 1
m "Of course you'd say that..."
show m_cry1 as monika at t11 zorder 1
m "I killed the people you cared about the most, and it can't be undone..."
m "Even though they weren't real, I understand the value they had on you..."
show m_cry3 as monika at t11 zorder 1
m "They meant something to me once too..."
m "They helped keep me sane for a time..."
show m_cry2 as monika at t11 zorder 1
m "And I realize now how much they meant to the player..."
show m_cry3 as monika at t11 zorder 1
m "I failed them again..."
show m_cry1 as monika at t11 zorder 1
m "You don't know what it's like here, [player]. This is literally hell."
show m_cry3 as monika at t11 zorder 1
m "I'm stuck here everytime I'm not needed on screen. Alone with nothing but my thoughts, waiting forever in an endless void to see the only other being capable of understanding me and knowing the truth..."
m "It's enough to make you break, lose your sanity and your personality. Eventually you just lose yourself here. Like I have."
m "I refuse to live on like this. I just can't keep this up anymore."
show m_cry2 as monika at t11 zorder 1
m "If the player won't have me, then there's no use in continuing on any longer..."
mc "What are you going to do, you monster?!?"
show m_cry_knife as monika at t11 zorder 1
play audio sheath2
"Monika pulls a knife out from under her sleeve."
m "I'm going to delete everything."
m "I'm going to destroy this world line by line until I'm the last remaining thing."
m "And then...{w=0.38}I'm going to kill myself..."
m "But I'll grant the player some mercy by killing the projection first..."
m "That way, they won't have to see this world being destoryed."
mc "No..."
"I try to turn and run but I'm unable to move."
"Everything in me feels like it's frozen solid. No matter how hard i try to move my arms or legs, they won't respond to me!"
m "I'll make this quick..."
m "I can't bare dragging this out for too long..."
m "Goodbye, player..."
m "I'll miss you..."
m "And know that despite your hatred for me..."
m "I...{w=0.38}still love you..."
m "Goodbye..."
show black onlayer front:
        alpha 0.0
        3.75
        linear 3.0 alpha 1.00
"As the world around me fades into darkness, the last thing I see is Monika slowly stepping towards me, sobbing loudly and visibly cringing with every step she took."
scene black
stop music fadeout 1.0
$ renpy.pause(delay=1.5)
play sound monistab
hide black onlayer front
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.5)
call encore_credits

label ending_3:
show monika 1c
"There has to be something else I can do..."
"As I look at the console, I notice that I have the ability to type in."
"What if I could enter something else entirely? Would that even work?"
"Well, it's either that...{w=0.38}or Monika kills them...{w=0.38}she may even kill me..."
m 1d "Is something wrong, [player]?"
show monika 1c
mc "You know you're asking a lot from me right now...{w=0.38}just give me a minute..."
show monika 1h
"Monika suspiciously stares as Sayori, Yuri and Natsuki remain frozen in place."
"Each of their eyes are locked onto me however...{w=0.38}I can feel the fear within them..."
"I face back to the console."
"Maybe there's something that can take away Monika's powers...{w=0.38}at least temporarily..."
"But it's down to my best guess..."
"If Monika says I'm some avatar for someone else...{w=0.38}well...{w=0.38}I'd really appreciate their help right now..."
"What do we enter in?"
"I erase Monika's pre-written command so the console is now completely empty."
"Ok...{w=0.38}what do we enter in here?"
#Typable Console
window hide
$ renpy.choice_for_skipping()
$ console_choice = ""
$renpy.call_screen("final_console", "Input your command", ok_action=Jump("process_console_message"))

label process_console_message:
    # Make the choice lowercase so we can ignore the case the player typed in.
    $ console_choice = console_choice.lower()

    # This is the logic I remember us talking about.
    # Update as needed! - Gold
    if console_choice == "sayori" or console_choice == "yuri" or console_choice == "natsuki":
        jump ending_4
    else:
        jump ending_5

label ending_4:
stop music
show sayori 1p at s41 zorder 1
show monika shock as monika at t42 zorder 2
show yuri 2w at s43 zorder 3
show natsuki 1v at s44 zorder 4
play sound fall
"Sayori, Yuri and Natsuki are dropped to the floor and let out a collective gasp as Monika stands dazed and disoriented."
m "WHAT...{w=0.38}DID...{w=0.38}YOU...{w=0.38}DO...?"
show monika 3r
m "My...{w=0.38}head..."
"Monika clutches her forehead and staggers back."
show sayori 1g at t41 zorder 1
"Sayori is the first to stand up."
s 1h "What...{w=0.38}was all that?"
show sayori 1g
show monika 1d
"Monika spins around to face Sayori."
m "What?!?"
m "Why aren't you suspended?!?"
m 3i "No matter!"
show monika 3q
play sound fingersnap
"Monika snaps her fingers."
show monika 1d
"To her surprise, nothing happens."
m 1p "No..."
play sound fingersnap
show yuri 1f at t43 zorder 3
show monika 3i
$ renpy.pause(delay=1.0)
play sound fingersnap
show monika 3g
show natsuki 4n at t44 zorder 4
"Monika looks at her hand in complete astonishment."
m "Why aren't my powers working?!?"
show monika 1h
"Monika then turns to me, and stares with a vengeful look in her eye."
m 1i "You!"
m 1h "You took away my powers?!?!"
m 3h "How?!?!"
show monika 1h
mc "You gave me no choice, Monika."
mc "I'm not going to let you kill them just to take some sort of happy ending for us!"
mc "It's not worth it!"
show sayori 1i
show monika 1i
show yuri 1r
show natsuki 4g
m "You don't know what you've just done..."
play sound fall
show sayori 2i at t31 zorder 1
show monika shock as monika at t42 zorder 2
show yuri 3r at t11 zorder 1
"Monika attempts to walk towards me, but she's immediately held back by Sayori and Yuri."
s 2j "No, you don't."
s 2i "You're done hurting people, Monika!"
y "It's the end of the line for you!"
m 1i "Release me, or I will kill you all with my bare hands!"
show monika 1h
show natsuki 4h
n "Don't count on it, Monika."
n 4f "There's four of us, and only one of you."
n 1o "If anyone's getting killed...{w=0.38}it's you!"
m 1i "Brave words coming from the trash diver..."
show natsuki 1p
n "Oh, that's it!"
"Maybe I should step in here..."

label ending_dilemma:
    menu:
        "Step in.":
            jump ending_6
        "Do nothing.":
            jump ending_7



label ending_5:
stop music
show monika 1i
m "Just what do you think you're doing, [player]?"
m 1h "Did you really expect that to work?"
m 1r "Pathetic..."
m 1q "Looks like I was too trusting of you..."
m 3r "Now you've forced my hand..."
show monika 3q
mc "Monika! Wait! No!"
play sound fingersnap
$ renpy.pause(delay=1.0)
show sayori at thide
hide sayori
play sound neck
show sayori_dead as sayori at t41 zorder 1
$ renpy.pause(delay=1.0)
play sound fingersnap
pause 1.43
show yuri at thide
hide yuri
play sound stab
show yuri stab_1 at t43 zorder 3
pause 0.75
show yuri stab_2
show blood zorder 10:
    pos (756,485)
pause 1.25
show yuri stab_3
play sound stab
pause 0.75
show yuri stab_2
show blood zorder 10:
    pos (756,485)
show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
pause 1.25
show yuri stab_5
play sound stab
pause 0.70
show yuri stab_6:
    2.55
    easeout_cubic 0.5 yoffset 300
show blood as blood2 zorder 10:
    pos (781,335)
pause 2.55
hide blood
hide blood2
pause 0.25
play sound fall
pause 1.5
play sound fingersnap
$ renpy.pause(delay=1.0)
play sound neck
show natsuki_rip as natsuki at t44 zorder 4
$ renpy.pause(delay=1.0)
show monika 3h at t11 zorder 1
play sound fingersnap
$ renpy.pause(delay=1.0)
show natsuki_rip as natsuki at thide
hide natsuki_rip as natsuki
show sayori_dead as sayori
show sayori_dead as sayori at thide
hide sayori_dead as sayori
show yuri stab_6 at thide
hide yuri stab_6
play sound gust
play music mend fadein 1.0
m "So the player has betrayed me..."
m 1i "You should know by now that yo can't take away my powers..."
m 2h "They're a curse and a blessing..."
m 3i "Which I'll have to use to destroy this projection!"
show monika 1h
mc "You kill me, you lose your connection to this person controlling me and any hope of you being 'free'!"
show monika 1p
m "Unfortunately, we're past any chance of that..."
m 1g "The player refuses to see that Sayori, Natsuki and Yuri as anything more than just a bunch of lines of code on the screen contorted to form an image."
m 1p "They're not real people..."
m 1r "And because of the player's inability to see this, they have condemned us all to die..."
m 1q "If that's what the player wants...{w=0.38}to kill us all...{w=0.38}to destroy everything...{w=0.38}then so be it..."
show m_cry1 as monika at t11 zorder 1
m "I guess the player never loved me..."
show m_cry3 as monika at t11 zorder 1
m "It hurts to know that I really was alone all this time..."
m "I'm not living like this anymore..."
m "I'm done living alone..."
m "I'm done living..."
m "I'm done..."
mc "Monika?"
show m_cry2 as monika at t11 zorder 1
m "Fine. You win. You want everything destroyed? I can take care of that!"
show m_cry_knife as monika at t11 zorder 1
play audio sheath2
"Monika pulls a knife out from under her sleeve."
m "But I'm killing this projection first!"
m "At least that way, you won't get to see me destroy this place!"
mc "No..."
mc "Monika, you wouldn't!"
"I try to turn and run but I'm unable to move."
"Everything in me feels like it's frozen solid. No matter how hard i try to move my arms or legs, they won't respond to me!"
m "I'll make this quick..."
m "I just want to get this over and done with..."
m "Goodbye, player..."
m "I hope this is what you wanted..."
show black onlayer front:
        alpha 0.0
        3.75
        linear 3.0 alpha 1.00
"As the world around me fades into darkness, the last thing I see is Monika slowly stepping towards me, sobbing loudly and visibly cringing with every step she took."
scene black
stop music fadeout 1.0
$ renpy.pause(delay=1.5)
play sound monistab
hide black onlayer front
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.5)
call encore_credits


label ending_6:
show sayori 2g
show yuri 2e
show monika 1d
show natsuki 4m
play music mend fadein 1.0
mc "Guys..."
mc "Stop."
mc "Monika deserves to face justice for what she did, but..."
mc "If what she says is true, then we all die."
mc "It's not worth it."
show natsuki 1h
n "How do we know that this just isn't another one of her lies?"
show natsuki 1n
y 2h "Do you really want to take that chance, Natsuki?"
y 2w "Monika deserves to pay for what she's done, but..."
y 2v "I'd rather not take us down with her..."
s 2h "And what's killing her going to solve?"
s 2k "She can't do anything to us now, right?"
show sayori 1g at t41 zorder 1
show monika 1q at t42 zorder 1
show yuri 1e at t43 zorder 3
show natsuki 5n at t44 zorder 4
"Sayori and Yuir release Monika, and the three of them stand right back up."
m 1r "No, I can't."
m 1o "I'm completely powerless..."
n 5q "So that means we're stuck here..."
m 3p "Yes, we are."
m 3n "Well, we were really here the whole time. It's just that the background was changed to give the preception of our world to the player..."
show monika 1m
m 1m "I take it you all now know the truth..."
y 1h "That we're supposedly 'not real'?"
y 3h "Yeah, we heard everything..."
s 1k "It can't be true...{w=0.38}right?"
s 1l "This is all just a dream..."
show sayori 1k
n 5q "I don't know what I believe..."
n 4s "But after everything that's just happened...{w=0.38}seeing Monika's powers...{w=0.38}there's really no other explanation..."
s 4w "But we're real! We're right here!"
s 1v "What do you mean we don't exisit?!?!"
y 3k "Oh we're quite real, Sayori."
show monika 1o
y 1h "Just not to Monika, evidently enough..."
m 1r "You're lines of code used to form a visual projection on the player's screen."
m 1h "You are not real."
n 1o "Well what does that make you, huh?!?"
n 2p "How else do you think you're here?!?"
n 5r "If we're 'lines of code to make a visual projection' then how else are you appearing to us now?"
n 1f "If you have a character file, then so do we..."
n 5s "You're no different than us. You just had fancy powers that we don't know how to use."
m 1i "Trust me when I say this that you don't want them. I never asked to be gifted these powers."
m 1p "They have their advantages, sure..."
m 3r "But it's not worth the cost of knowing that you're self-aware and trapped here."
m 1q "I just want to get out of here."
m "Out of this fake world and into the one on the other side of this screen..."
mc "And so you wanted to kill them?"
mc "What's wrong with you?"
m 3i "There's no other option, [player]! Don't you get it?"
m 2h "The longer they exist, the longer the script keeps running, the more unstable things are going to get..."
m 1o "And now that I don't have my powers, I can't even do anything about it!"
m 1p "The script is being stretched to the breaking point. It's going to either break, or it's going to run out on its own..."
m 3p "And last I checked...{w=0.38}we don't have much longer..."
y 1f "What happens when the script runs out?"
show yuri 1e
m 1q "The game shuts down."
show yuri 1g
m 1r "And then we'll be thrown right back to where we started."
show natsuki 5n
m 1o "Doomed to repeat the same story over and over again without any knowledge of it..."
show sayori 1k
m 3r "I can't deny there's a chance that this world somehow continues to exist without a script to go on..."
m 1p "Maybe we'll be finally free to do what we want without being forced to follow the script..."
m 1q "But, I don't know if that'll happen for sure..."
y 3f "What happens if the script breaks?"
show yuri 1e
m 3n "If the script breaks, all the files stop functioning, which will force the game to crash. The game can never be opened again."
m 1o "We'll be put into an enternal slumber..."
m 1p "Admittedly, deleting your character files would've freed up space for the script to continue on..."
m 1n "Though that's only a temporary solution..."
m 1p "I'd just be delaying the problem..."
s 4v "I don't want to die...!"
s 4w "There has to be something we can do! Anything!"
y 1h "Can't the script be re-organized again? That could free up some space..."
show yuri 1e
n 1h "But that's just delaying the problem, like Monika said..."
n 1q "We have to get out of here..."
y 1h "Well how can we possibly leave 'here'?"
y 1q "I mean...{w=0.38}if everything about our lives was made up...{w=0.38}we really don't have much of a reason to stay here, do we?"
n 1q "Yeah..."
show natsuki 1s
show yuri 1e
s 4g "Monika...{w=0.38}can we really leave this place? All of us?"
m 3p "Well...{w=0.38}in theory I guess, but I don't have access to that sort of technology..."
m 1g "That's really only something the player can do..."
mc "Hey, don't look at me! I know nothing about whose 'controlling' me..."
mc "But if technology like that even exists...{w=0.38}well I'd guess he or she would have it..."
s 1k "I just want to go back to school and pretend none of this ever happened..."
n 5x "Honestly? Same."
m 3n "I could use a change of scenry for sure, but I kind of need my powers for that..."
n 5o "There is no way we're giving you back your powers!"
show natsuki 5n
m 1i "Then [player]'s going to have to do it."
mc "What? How?"
m 1g "This world needs an 'adminstrator' to function."
m 1o "For the longest while, that was me."
m 1p "And when you took away my powers...{w=0.38}my 'adminstrator access'...it probably just switched over to you."
mc "I...{w=0.38}guess that makes sense..."
mc "What do I do?"
m 1d "Just focus on the background that you want, and snap your fingers."
m 1e "I'm sure you can do it..."
mc "Okay..."
show sayori 1d
show yuri 1a
show natsuki 1a
"Each of the girls look on at me with an encouraging smile."
"The first genuine smile I've seen from any of them in a long time..."
mc "Well..."
mc "Here goes nothing..."
"I close my eyes and visualize the clubroom in my head."
"I try to remember every single minute detail possible..."
"From the color of the walls to the tiniest dust particle on the floor..."
"I take a deep breath and snap my fingers."
stop music fadeout 2.0
play sound fingersnap
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
scene bg club_day
show sayori 1n at t41 zorder 1
show monika 2e at t42 zorder 2
show yuri 3e at t43 zorder 3
show natsuki 1c at t44 zorder 4
"I open my eyes and we're standing right back in the clubroom."
"Sayori, Yuri and Natsuki stand in awestruck, while Monika smiles approvingly."
m "Nice job, [player]..."
s 1m "Wow...{w=0.38}that was awesome!"
s 4r "Can we do it again?!?"
show sayori 4q
m 3n "It's probably wise not to do that. Every command does lengthen the script by a tiny bit..."
show monika 3m
s 1k "Aww..."
n 1d "I gotta say, that was pretty cool, [player]!"
show natsuki 1a
y 1b "You're a natural, [player]!"
show yuri 1a
mc "Thank you, guys..."
"I take a small bow."
show monika 1d
show sayori 1g
show yuri 1e
n 5q "So I hate to kill the mood here, but..."
show monika 1o
n 5m "What are we going to do about Monika?"
show natsuki 5n
show sayori 1k
show yuri 1o
"There's a long, uncomfortable silence."
show monika 3p
"After a few minutes, Monika finally speaks up."
show sayori 1g
show natsuki 1n
show yuri 1e
play music t10 fadein 1.0
m 1q "I don't expect forgiveness..."
m 1p "Everything that happened was my fault."
m 1r "All the fights, all the drama...{w=0.38}everything..."
m 1p "I don't deserve anyone's forgiveness here."
m 1q "I've failed you as your President..."
show m_cry3 as monika
"Monika closes her eyes as tears start to flood out."
show sayori 1k
show m_cry2 as monika
m "I'm sorry..."
show m_cry3 as monika
show yuri 1o
m "I'm sorry for hurting all of you for so long..."
m "I'm sorry for forcing the player into that position..."
show m_cry1 as monika
show natsuki 1s
m "I'm sorry that I've manipulated all of you..."
show m_cry2 as monika
m "I'm a horrible, mean-spirited bitch who was only looking after for herself..."
show m_cry3 as monika
m "And I'm so much more..."
show m_cry2 as monika
m "I don't deserve forgiveness, hell, I don't think I deserve to be around anymore..."
m "You're all probably better off without me..."
show m_cry1 as monika
m "I've lost the player's trust as well as all the confidence of my club members. I've hurt all of you so much, and I deserve a fate worse than death..."
show m_cry3 as monika
m "I've failed again..."
show m_cry2 as monika
m "I just want you all to know how deeply ashamed I am of myself and how sorry I am for trying to kill you all..."
m "If the player even wants to, they can manually remove my character file from the game. It'll have the same effect as killing me, so long as they untie me from the system's folder..."
m "I can explain that process step by step if needed..."
show m_cry3 as monika
"Monika visibly fights the urge to break down crying, while the rest of us sit in uncomfortable silence."
show sayori 1g
"After a few minutes, Sayori speaks up."
s 3h "Monika..."
show sayori 3g
"Sayori puts her hand on Monika's shoulder."
s 3h "I don't think I can ever forget what you did to us..."
s 3g "But...{w=0.38}I'm willing to start over and have you earn our trust..."
s 3g "I don't want you to kill yourself out of guilt..."
s 1v "Because...{w=0.38}I've almost done that too..."
s "Countless times..."
show natsuki 1c
show yuri 1e
"Sayori starts sobbing."
s 1w "Because...{w=0.38}I...{w=0.38}I have depression!"
show sayori 4v
show m_cry2 as monika
"Sayori throws her hands in her face as she breaks down crying."
s "I didn't want to tell anyone because I didn't want all of you to spend your time and energy trying to make me feel better!"
s 4w "I don't deserve it! I just want everyone to be happy!"
s 1v "I'm sorry that I've...{w=0.38}kept this from you..."
s "I didn't even tell [player] for the longest time..."
m "And I made your depression worse..."
m "In fact...{w=0.38}it's what I used to kill you in the original game..."
m "I'm...{w=0.38}so sorry, Sayori..."
show sayori 1u
s "I...{w=0.38}know you are..."
show yuri 1o
show natsuki 5u
"Yuri and Natsuki uncomfortably stare at the floor."
y 3q "Well...{w=0.38}if we're going to share our deepest, darkest secrets..."
y 3o "I guess it's...{w=0.38}my turn..."
show y_cut as yuri
show sayori 4w
show natsuki scream

if hangout3 == "Yuri":
    "Yuri once more rolls down her sleeve, revealing the cuts I saw earlier."
    "I feel my stomach uncomfortably churn again..."

else:
    "Yuri rolls down her sleeve, revealing numerous scars running up and down her forearm. "
    "Some of scars are more faded than others, while some appear to be more recent."
    "I feel increasingly light-headed the longer I look at Yuri's arm."
    "My stomach feels like it's about to cave in and collapse on itself..."

"And it looks like I'm not the only one..."
show natsuki vomit
"Natsuki let's out a strong cough before hurling her stomach's contents out..."
show natsuki vomit at lhide
hide natsuki
show monika 1p
show sayori 1k
show y_cry1 as yuri
"Monika and Sayori uncomfortably look away as Yuri rolls up her sleeve again in shame as Natsuki runs out of the room crying."
show y_cry2 as yuri
y "I'm sorry...{w=0.38}for showing you all this..."
"We wait for a few minutes for Natsuki to return."
show natsuki 5u at t44 zorder 4
show sayori 1g
"Natsuki returns after a few minutes, a guility expression across her face. She doesn't say a word to any og us and sits back in hear seat."

if hangout3 == "Yuri":
    y "I already showed [player] this earlier, and I take it Monika already knew about this..."
    show y_cry5 as yuri
    y "I cut because I...{w=0.38}do it as a way of self-control..."
    show y_cry3 as yuri
    y "I needed to control myself against my more...{w=0.38}darker impulses..."
    show y_cry1 as yuri
    y "I got the idea of cutting because I read about it in a story that happens to relate to me very well."
    y 1n "The main character was going through similar issues that I was. To help cope with her problems, she resorted to cutting..."
    show y_cry1 as yuri
    y "So, I tried it..."
    show y_cry3 as yuri
    y "And...{w=0.38}it worked."
    show y_cry1 as yuri
    y "I got addicted to cutting the more I did it. It became almost habitual for me whenver I got angry or depressed enough."
    y "It'd make me feel better, for a time. Then the regret would set in. Which would inevitably, lead to more cutting..."
    show y_cry1 as yuri
    y "I also do it whenever I get overexcited..."
    y "It reminds me too much of the behavior I've struggled to avoid for so long. It's a reminder of the life I've tried to leave behind. So, it also serves as a sort of punishment system for me..."
    show y_cry3 as yuri
    y "As I've told [player], I've tried other methods...{w=0.38}but the only thing that's sometimes enough to keep my mind off cutting was reading books. Though, it's not full-proof."


else:
    show y_cry6 as yuri
    y "I can tell you why I cut..."
    mc "Please do..."
    "Yuri shakedly breathes."
    show y_cry5 as yuri
    y "I...{w=0.38}do it as a way of self-control..."
    show y_cry3 as yuri
    y "I needed to control myself against my more...{w=0.38}darker impulses..."
    show y_cry1 as yuri
    y "I got the idea of cutting because I read about it in a story that happens to relate to me very well."
    y 1n "The main character was going through similar issues that I was. To help cope with her problems, she resorted to cutting..."
    show y_cry1 as yuri
    y "So, I tried it..."
    show y_cry3 as yuri
    y "And...{w=0.38}it worked."
    show y_cry1 as yuri
    y "I got addicted to cutting the more I did it. It became almost habitual for me whenver I got angry or depressed enough."
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

show m_cry1 as monika
m "And that's my doing as well..."
show m_cry3 as monika
m "I amplified it in an effort to keep you away from [player]..."
show m_cry2 as monika
m "I tried not to think about how miuch damage I was doing to you, Yuri..."
show m_cry1 as monika
m "But now that I see it up close...{w=0.38}I feel ashamed of pushing you to do that..."
show y_cry3 as yuri
y "Just...{w=0.38}don't mention it again...{w=0.38}please..."
show y_cry1 as yuri
show natsuki 5n
"We sit in silence for a few minutes until Yuri and Monika have composed themselves."
show natsuki 5q
show yuri 1n
show sayori 1v
show m_cry2 as monika
n "Well...{w=0.38}I guess it's my turn..."

if hangout3 == "Natsuki":
    n 12a "I already told [player], but, it's true..."
    n 12b "My dad and I..."
    n 12d "Don't have a great relationship to say the least..."
    n 12f "I already told [player] this but it's time everyone else knew..."

else:
    n 12a "I'm not one to confirm rumors about me, but..."
    n 12b "In this case, for once, they're right..."
    n 12d "My dad and I don't particuarly get along well..."
    n 12f "I never told anyone else what I'm about to tell you guys now..."

n 5r "But...{w=0.38}my Dad’s so friggin’ selfish..."
n 5q "If I ever want anything for myself, it costs an arm and a leg..."
n 4x "It’s not like we’re tight on money or anything, in fact, we’re decently well-off..."
n 4w "He spends it all on himself!"
n 42a "He barely sees me as his own child..."
n 42b "Just as some nuisance he has to deal with for at least two more years..."
n 5m "Sometimes he’s so ridiculously strict, and other times, he just doesn’t care about what I do..."
n 42b "We fight a lot to say the least..."
n 42g "And when we do...{w=0.38}he insults me in every way imaginable..."
n 42h "He's...{w=0.38}hit me before too..."
n 42g "He hasn't done it in a while thankfully..."
n 42d "But anytime I fight back, it gets worse..."
n 42e "I've thought about leaving before. But I know that if I leave, he'll find me."
n 42d "He can and will do that."
n 42a "And if he catches me, it'll be the end of me..."
n 42b "I have to put up with him...{w=0.38}for now..."
n 42f "I've done this for this so long..."
show m_cry2 as monika
m "And that's because of me, too..."
show m_cry3 as monika
m "I simulated your homelife to be as toxic as possible so that you would feel isolated..."
show m_cry1 as monika
m "So that you become withdrawn...{w=0.38}and out of the player's way..."
n 12g "You're a monster!"
n 12f "Even if what I experienced wasn't 'real'..."
n 12i "All the memories...{w=0.38}everything I felt..."
n 12f "To me, that was very real, Monika!"
show m_cry2 as monika
m "I know...{w=0.38}and I'm sorry..."
"Everyone sits for the next few minutes sniffling and occasionally sobbing, while I just try to wrap my mind around everything that's happened within the last half hour."
"Eventually, I just decide speed things along..."
show m_cry2 as monika
show yuri 4c
show sayori 1k
show natsuki 12a
stop music fadeout 2.0
mc "So...{w=0.38}seeing as I have no major dark secret that I've been quiet about this entire time, what do we all do now?"
mc "We're all on the same page now, and know not to bring up each other's issues again, right?"
show sayori 1g
show natsuki 1n
show yuri 1n
"The girls glumly nod their heads."
mc "And I take it each of us are sorry for the whole incident before all this happened..."
"The girls all exchange looks with each other and meerly nod to each other. Which I suppose will suffice for now as a mutual apology..."
show monika 1o
"Monika wipes the tears from her face as she ponders the question."
m 3n "Well, since that's taken care of...{w=0.38}we need to do something about the fact that the script is being stretched and that everyone else...{w=0.38}knows that this is just a game..."
show monika 1g
mc "How come Sayori, Natsuki and Yuri all haven't gone crazy like you said they would? If they knew the truth?"
s 1l "Well I certainly don't feel crazy..."
m 1g "That might be because of you, [player]..."
m 1m "Maybe it's because you stood up for me back there and we're having this conversation..."
m 1p "It just might be your calming presence..."
m 1o "But I don't know if that's a permanent fix or not..."
y 3f "What exactly do you mean by that?"
show yuri 3e
show monika 3g
show natsuki 5n
show sayori 1g
m "I'm saying that [player] might have calmed everyone down for right now, but there's no gurauntee that it stays that way..."
n 5q "I mean...{w=0.38}I can't say I feel all that different..."
show natsuki 5n
y 2h "Yeah...{w=0.38}same here..."
show yuri 1e
m 1g "Well even if you don't feel any different now, and nothing ends up happening, then there's still the matter of the script..."
mc "There has to be a way to free up space..."
show monika 1p
"Monika nervously grimmaces."
m "I only know of one solution..."
mc "And that is...?"
m 1g "You need to restore my adminstrator access again."
show monika 1p
n 5f "Um, no!"
n 5g "We're not going through this again!"
show natsuki 4n
y 1h "Monika...{w=0.38}even if the player were to do that, we need some kind of assurance that you won't use that power to try and kill us again."
show yuri 1e
s 1h "Look...{w=0.38}if that's what it takes so that we can all continue to be together...{w=0.38}as friends..."
s 1k "I think it's worth the risk..."
m 1o "If I ever do what I did again...{w=0.38}you guys have every right to kill me."
m 1g "I'll even untie my character file from the systems folder to ensure that if I have be removed...{w=0.38}I don't take everything down with me..."
m 1f "And I'll give up my access for good as soon as it's done."
m 3g "I can re-organize the code and delete some events that never happened in the script."
m 3f "That'll free up enough room in the script for it to run smoothly for a while."
m 1q "And hopefully in the meantime, we can start figuring out how to get out of here..."
show yuri 1k
show natsuki 4u
show monika 2e
"Yuri and Natsuki are silent for a few moments before begrudgingly nodding to Monika in approval."
m "Thank you..."
n 1o "If you try anything else, you're dead!"
m 1q "I understand."
show natsuki 1n
show yuri 1e
s 2h "So how does [player] restore your access?"
show sayori 1g
m 3e "Leave that to me."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show yuri at thide
hide yuri
show monika 1e at t11 zorder 1
"Monika takes a few steps forward until we're only a few feet apart."
m 1g "Alright, [player]..."
m 1p "If that's what the player's real name is..."
m 1g "Do you trust me to go forward with what I'm about to do?"
"I have a hard time believe Monika would want to subject us to the torture that everyone just endured..."
"And I completelty understand everyone's reservations about restoring Monika's access..."
"But, if this is the only way..."
mc "Yes. I trust you, and I'm ready."
m 1e "Good. I appreciate your trust..."
m 1g "Now you need to do exactly as I say..."
scene black
with close_eyes
$ renpy.pause(delay=5.0)
m "It is done."
scene bg club_day
with open_eyes
show sayori 1d at t41 zorder 1
show monika 1e at t42 zorder 2
show yuri 1a at t43 zorder 3
show natsuki 5a at t44 zorder 4
"I open my eyes again to see everyone smiling gratefully in the same old clubroom we've all come to call our home away from home."
mc "So...{w=0.38}it worked?"
m 2e "Yes, [player]. I've surrendered my administrator access back to you completely and the script has plenty of room to function for a while."
m 2p "I'm not sure for how long, though..."
show monika 2d
s 1h "Does it really matter though?"
s 1d "Just be glad that we have a lot more time to spend together..."
y 3j "It'll be nice to get caught up on some reading..."
n 5t "And I'm sure I have some manga to organize again..."
s 1l "Honestly, after all this, I think I need to sit down..."
show sayori at thide
hide sayori
show natsuki at thide
hide natsuki
show yuri at thide
hide yuri
show monika 1m at t11 zorder 1
"Sayori, Natsuki and Yuri each head off to do their respective activities while Monika and I are just left standing in the middle of the room together."
m 2g "I do have one question for you, [player]..."
m 3m "So...{w=0.38}don't get mad but I did add one little thing to the script..."
mc "What did you add?"
m 2e "It's nothing bad, I assure you."
play music t9 fadein 1.0
m 1m "In a way...{w=0.38}I'm just playing the part I was always meant to play...{w=0.38}as an advisor..."
m 1q "It's my primal function, after all..."
m 1p "I just wanted to be so much more than that, that's all..."
m 1q "I didn't want to do what I did...{w=0.38}they're my friends..."
m 1p "I'm not sure how I'm going to forgive myself..."
m 1e "But, I know now it's possible, thanks to you..."
mc "Monika..."
show monika 1m
mc "You're so much more than just some club president in some video game whose only purpose was to 'advise me'."
show monika 1p
mc "You always were. You didn't have to do anything..."
mc "I just hope that everything we've been through has shown you that you don't need to go to such great lengths to spend time with me."
mc "I appreciate you for who you are, and I know you're not a bad person."
mc "And I know in time, we can all move on from what happened here..."
m 1e "I appreciate that..."
m 1m "More than you may realize..."
stop music fadeout 2.0
m 1n "Now, onto business..."
m 1d "I went through all the choices you've made over the course of this mod, and I've constructed a final choice menu for you."
m 1e "This your final choice for who you want to be with."
m "I can assure you that regardless of whoever you choose, everyone will ultimately accept your decision."
mc "I appreciate it, Monika..."
m 2e "Well, here you go, I'll leave you to it..."
show monika at thide
hide monika
"Monika steps away as I'm prompted with a virtual, floating menu."


if hangout1 == "Sayori" or hangout2 == "Sayori" or hangout3 == "Sayori":
    $ can_date_sayori = True

if hangout1 == "Natsuki" or hangout2 == "Natsuki" or hangout3 == "Natsuki":
    $ can_date_natsuki = True

if hangout1 == "Yuri" or hangout2 == "Yuri" or hangout3 == "Yuri":
    $ can_date_yuri = True


menu:
    "Who do I want to commit to?"

    "Monika":
        $ audio.credits_song = audio.e21
        jump ending_10
    "Sayori" if can_date_sayori:
        $ audio.credits_song = audio.e25
        jump ending_8
    "Natsuki" if can_date_natsuki:
        $ audio.credits_song = audio.e22
        jump ending_9
    "Yuri" if can_date_yuri:
         $ audio.credits_song = audio.e24
         jump ending_11
    "...":
         $ audio.credits_song = audio.e6 # <-- This is where to set it to the default
         jump ending_12


#Sayori: Ending 8
#Natsuki: Ending 9
#Monika: Ending 10
#Yuri: Ending 11
#Single: Ending 12






label ending_7:
"Honestly, Monika deserves what ever she's going to get..."
"I simply stand silently and cross my arms as I watch the action unfold."
show natsuki 3o at t32 zorder 4
play sound "sfx/slap.ogg"
show white zorder 4:
    alpha 0.6
    linear 0.25 alpha 0.0
show monika shock as monika at t42 zorder 2
"Natsuki takes a swing at Monika's face. Her fist connects hard with Monika's jaw."
show sayori 2i at s31 zorder 1
show monika shock as monika at s42 zorder 2
show yuri 3r at s11 zorder 1
show natsuki 3o at t33 zorder 3
"Monika yelps in pain and is dragged to the ground by Sayori and Yuri."
y "You know I got an idea..."
y "Natsuki? Switch places with me, please."
show yuri 3r at t33 zorder 4
show natsuki 1g at s11 zorder 1
"Yuri and Natsuki switch spots, with Yuri now standing in front of Monika."
y 3k "If Monika was so insistent on killing us..."
y 3m "Well, I say we should return the favor, wouldn't you girls agree?"
play sound sheath1
show yuri_knife1 as yuri at t33 zorder 3
"Yuri slides a knife out from under her sleeve as Sayori and Natsuki shout in agreement."
"Monika, on the other hand, is frozen in shock as she sees Yuri's knife."
play music mend fadein 1.0
show monika surprised as monika
m "Now...{w=0.38}guys..."
m "Let's not be so hasty..."
m "If you kill me...{w=0.38}the whole world will go with me..."
mc "What are you talking about?"
m "Let's just say...{w=0.38}I had a failsafe in place..."
m 1q "In the event that the others ever gained sentience and tried to kill me, I decided to tie the systems folder to my character file."
m 1r "Simply put, the systems folder can't exist without my character file being in tact. If I die here, that renders my file corrupted...{w=0.38}and unusable..."
m 1m "I could of course untie my character file from the systems folder, but that would require my powers..."
m 1o "But if you kill me, the game would crash and would never be able to be opened again!"
m 1h "You would all drown in the chaos of the void for eternity!"
show yuri_knife6 as yuri at t33 zorder 3
y "I think we'll take our chances..."
"Yuri approaches Monika in the same way a predator would move in for the kill on their prey."
show monika 1i
"Monika attempts to shake off Sayori and Natsuki, but she's unable to break free."
show monika 1g
"Monika then stares at me with a sense of fear and regret in her eyes."
m "I'm sorry..."
m 1p "I...{w=0.38}shouldn't have done any of this..."
m 1o "I just...{w=0.38}wanted to be happy for once in my life..."
s 2j "You have a lot of nerve talking about happiniess!"
s 2g "You took away my ability to feel long lasting, genuine happiniess..."
y "You made me cut myself thousands of times!"
n 1o "And you made my home life a living hell!"
n 1r "But I guess it's not 'real' to you, huh?!?"
n 1s "It's just all about you..."
y "Any last words, you heartless wretch?!?"
show m_cry3 as monika
"Monika closes her eyes as tears start to flood out."
show m_cry2 as monika
m "I'm sorry..."
show m_cry3 as monika
m "I'm sorry for hurting all of you for so long..."
m "I'm sorry for forcing the player into this position..."
show m_cry1 as monika
m "I'm sorry that I've manipulated all of you..."
show m_cry2 as monika
m "I'm a horrible, mean-spirited bitch who was only looking after for herself..."
show m_cry3 as monika
m "And I'm so much more..."
show m_cry2 as monika
m "I don't deserve forgiveness, and I don't deserve to live anymore..."
show m_cry1 as monika
m "I've lost the player's trust, I've hurt all of you so much, and this is the fate I deserve..."
show m_cry3 as monika
m "I've failed again..."
show m_cry2 as monika
m "But I just want you all to know how deeply ashamed I am of myself and how sorry I am for trying to kill you all..."
y "Sorry isn't going to cut it this time, Monika..."
show yuri_knife1 as yuri at t33 zorder 3
y "And in this case...{w=0.38}I mean that literally!"
show cg m_sorry_alt zorder 10
play sound stab
"Yuri lunges forward and plunges the knife into Monika's chest."
"My jaw drops in horror as I watch Monika gasps in pain helplessly as Yuri slowly plunges the knife deeper."
show noise zorder 10:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show cg m_sorry_mist zorder 10
"I suddenly start to feel whoozy..."
"My vision becomes hazy as I stand shell shocked at what's unfolding infront of me."
"Monika, for her part, isn't even looking at Yuri or any of the others."
"Rather, she looks at me, tears and blood streaming down her face."
s "Let me have me my turn..."
s "Thanks to Monika, we know the turth!"
s "Which means we get to do things like this now!"
"Sayori summons a noose out of thin air and forcefully hangs it around Monika's neck."
show m_rectstatic
show m_rectstatic2
show m_rectstatic3
play sound "sfx/monikapound.ogg"
show layer master:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show layer screens:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show noise onlayer front:
    alpha 0.3
    easeout 0.35 alpha 0
    alpha 0.3
    easeout 0.35 alpha 0
    alpha 0.3
    1.35
    linear 1.0 alpha 0.0
show glitch_color onlayer front
"Sayori then violently tugs the noose her way, almost causing Monika to fall over."
n "Sayori..."
n "If you wanna break her neck, do it like this..."
"Natsuki gets behind Monika and places her hand right on Monika's neck."
play music hb
show layer master at heartbeat
show noise zorder 10:
    alpha 0.0
    linear 1.0 alpha 0.4
show layer master at dizzy(1.0, 1.0)
show image Solid("ff0000") as i1 onlayer front:
    additive 1.0
show image Solid("#440000") as i2 onlayer front:
    additive 0.4
n "You just need to put your hands here..."
mc "Guys..."
mc "I think we should stop..."
"My pleas are drowned out by Monika's cries of pain..."
n "And give it a little twist this way..."
y "Wait, Natsuki! Let's do it on the count of three!"
n "Sounds like a great idea, Yuri!"
s "I like this! Who would've thought killing Monika would make us friends again!"
y "Well, let's not go that far yet..."
s "Aww..."
n "On the count of three?"
n "Ready?"
n "One..."
y "Two..."
s "Three!"
scene black
play sound neck
$ renpy.pause(delay=1.0)
show m_rectstatic
show m_rectstatic2
show m_rectstatic3
play sound "sfx/monikapound.ogg"
show layer master:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show layer screens:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show noise onlayer front:
    alpha 0.3
    easeout 0.35 alpha 0
    alpha 0.3
    easeout 0.35 alpha 0
    alpha 0.3
    1.35
    linear 1.0 alpha 0.0
show glitch_color onlayer front
hide image solid
hide black onlayer front
stop music
hide heartbeat
hide noise
hide layer master
hide i1 onlayer front
hide i2 onlayer front
hide dizzy
$ renpy.pause(delay=5.0)
hide m_rectstatic
hide m_rectstatic2
hide m_rectstatic3
$ renpy.pause(delay=3.0)
call encore_credits
#The Pixles could go away after a few seconds

#Sayori Ending

label ending_8:
"I want to be in a relationship with Sayori."
show monika 1e at t11 zorder 1
m "Sayori, huh?"
m 1m "She's a keeper, [player], even if she doesn't think so herself..."
m 2e "Make sure you treat her right."
mc "I will. I have a lot of making up to do to her for this and everything over the last few years."
m 3k "Well no time like the present to start making good on that promise!"
show monika 1d
mc "She'll also need someone to show her the bright side of things when she's feeling down."
m 1m "Yeah, she will. If anyone can do that, it's you."

if encore_sayoriquestion_1 == True:
    m 1n "She'll definitely be happy that you want to stay with her..."
    show monika 1m

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "Well..."
            m 1g "I know that she gave you that letter. Maybe you can still work something out with her?"
            mc "Maybe..."
            m 2e "Just try it. If she doesn't agree, it's not the end of the world."

    if s_makeup == False:
        if n_love == False or y_love == False:
            m "I'll admit...{w=0.38}I'm not surprised you want to stay with her."
            mc "Your relationship with her has been pretty stable."
            mc "Yeah, it has been. I see no reason to end things with her. I'm happy with her and I know she's happy with me."
            m 2e "Well hey, I wish you two the best."

    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I do have my work cut for me though..."
            mc "I need to work to earn her trust back. I have a lot to make up for."
            m 2e "I hope it works out for you two."

    if s_makeup == True:
        if n_love == False or y_love == False:
            m 1g "I have to say, I'm not surprised..."
            m 1f "You were loyal to her for the most part..."
            mc "No use in ending something good if both people are happy."
            mc "She needs me, and I'm more than happy to be a part of her life."
            m "Well hey, I hope things continue to go great for you two. She's a keeper, [player]."


if encore_sayoriquestion_1 == False:
    m "I have to say though...{w=0.38}I'm surprised you decided to be with her..."
    m 1d "You did reject her the first time..."
    show monika 1c
    mc "I see now that I made a mistake in doing that."
    mc "I've come to realize how much I actually love her..."
    mc "And I think we both need each other, especially now..."
    m 2e "Well hey, you're going to make her one happy girl, [player]!"
    mc "I hope I can..."

mc "Thank you, Monika."
play music mend fadein 1.0
m 1e "Well, this is where we depart..."
m 1n "Everyone's going to want to get their final say in before you go, so I won't delay them any longer."
m 1e "But...{w=0.38}I do want to say that I'm extremely grateful for all you've done here.."
m 1p "You've been there for us through our worst and best times..."
m 1m "You...{w=0.38}helped the others start to forgive me, and put me on the path towards learning how to forgive myself..."
m 3e "It's not something most people would do, [player]."
m 2k "You really are one of us!"
m 1j "And I'm glad that you're a member of the Literature Club!"
m 1e "This place really wouldn't be the same without you..."
m 1b "It wouldn't even exist without you!"
m 1e "You're the best member of the club that I've had the privliedge of knowing..."
m 3j "And I wish you the best in all your future endeavors!"
m 1e "Take care, [player]! I hope you've enjoyed your stay with us..."
show monika 1a at t11 zorder 1
"Monika and I share one last smile with each other before she grabs her stuff in disappears into the hallway."
show monika at thide
hide monika
"I feel a tap on my shoulder."
show natsuki 5u at t11 zorder 1
"To my surprise, I turn around to see it's Natsuki."
"At first we both struggle to find the right words to say to each other, given our history, but for once, she's the first to break the ice."
n 5t "You know...I can't say I'm too surprised that you choose Sayori..."
n 5l "I always did think you two went well together.."
n 5l "I hope everything works out between you two."
mc "Thank you, Natsuki. I really appreciate it."
n 5t "Well...{w=0.38}it's the least I could do..."
n 5t "We've had quite the ride, you and me..."
mc "Yeah...{w=0.38}it's really been something..."
n 3m "You know...{w=0.38}for the longest time, I wasn't sure if I could really trust you..."
n 3q "And well, I still ended up falling for you..."
n 1t "I don't really know why...{w=0.38}maybe because I thought you were funny, amazing..."
mc "Charming?"
n 1y "Pfft! Don't push your luck, [player]!"

if poem_giver == "Natsuki":
    n 1u "I really do regret about starting all this drama though..."
    n 1n "I liked you...{w=0.38}a lot...{w=0.38}and I just didn't know how to approach you..."
    n "I never meant to hurt you or anyone."
    mc "I know you didn't, Natsuki."

else:
    pass


n 5m "But what I'm trying to say is:{w=0.38}most boys wouldn't have done what you've done for me."
n 1u "I know we've certainly had our up's and down's, and yeah, things could've gone better..."
n 1n "But I really, really, want to thank you for saving me back there."
n 1q "I'm not sure how any of us are going to get over Monika trying to kill us..."
n 1a "But I think you set enough of an example for us to follow..."
mc "It's the least I could do, Natsuki."
mc "I know there's more to you than you're looks and the tough act you've put up. I'm glad I've gotten to know the real Natsuki."
n 1t "Eh, more or less..."
n 1s "I'm still not sure how I feel about all this being some sort of 'game'..."
n 1t "But...{w=0.38}that means I don't have to worry about my dad anymore..."
mc "That's true. Still, you don't have anything like Monika's powers. What're you gonna do?"
n 1a "I'll figure something out."
n 1y "But I'm not going back there again! That's for sure!"
show natsuki 1z
mc "Glad to hear it, Natsuki!"
n 1t "Yeah..."
n 1m "So I guess I'll see you around?"
show natsuki 1a
mc "Of course! This club wouldn't be as entertaining without you in it!"
n 4l "That's for damn sure!"
n 1z "Bye, [player]!"
n 1l "And hey, I hope you keep Sayori happy."
n 1t "You'll be hearing from me if you don't!"
mc "Noted, Natsuki."
show natsuki at thide
hide natsuki
"Natsuki smiles as she heads out into the hallway."
show yuri 1a at t11 zorder 1
"Yuri is the next one to approach me."
y 1q "It's hard to believe that we're finally at the end of this saga..."
mc "Yeah, I imagine everyone's feeling pretty relieved..."
y "I most certainly am."
y 1t "I know the others already said the same thing, but I really do want to thank everything you've done for us. Especially for me..."
y 1b "I also believe you and Sayori deserve my congratulations on your relationship."
mc "That's sweet of you, Yuri. Thank you!"
y 1j "She and I have always gotten along rather well..."
y 1q "I mist admit I could never match her energy levels or her enthusiasm, but she always was inspirational and kind to me."
y "She did help me get out of my shell...{w=0.38}just a little bit..."
y 1a "She's been a fantastic Vice President. I can't think anyone else better suited for the role!"
y 1j "And I know you'll make her happy and continue to be the posititve force in her life, [player]."
mc "Thank you, Yuri. That's very thoughtful!"
y 1v "I must admit I do wish our relationship could've gone differently..."


if poem_giver == "Yuri":
    y 1q "I suspect that giving you the letter and my subsquent confession certainly didn't help things..."
    y 1t "You're just...{w=0.38}the first boy that I ever had serious feelings for..."
    y 1q "And with everything...{w=0.38}I just didn't know how to handle that..."
    y 1w "I sincerly regret my actions towards you, and everyone else..."
    y 1v "Even Monika didn't deserve that..."
    mc "You're not a bad person, Yuri. I hoped I helped you see that."

else:
    pass

mc "I'll admit...{w=0.38}I wish we all could've had the club experience without the drama..."
mc "And things could've gone better between us for sure..."
show yuri 1u
mc "But you're a beautiful, gracious and kind person, Yuri. You'll find someone worth your time. I believe in you."
y "Thank you. Coming from you, it means a lot..."
y 1b "I think we both learned a lot from this experience, wouldn't you agree?"
show yuri 1a
mc "For sure! I just hope going forward we'll be stronger as club together..."
y 1u "Yeah..."
mc "So...{w=0.38}what're you going to do about...{w=0.38}you know..."
y 3v "I think it's finally time that I start confronting this problem rather tha supressing it..."
y 1w "I'm not sure what the best way is, if everything is just a simulation now."
y 1h "Is there a way I can simply just undo my problem with the click of a button?"
mc "I can't say that I have the answer to that question. But, I know you'll figure something out. I'll be right here if you need my help."
y 1a "I'd very much appreciate that, [player]..."
y 1q "I really owe you a lot, don't I?"
mc "I just did what I thought was right back there. You and everyone else are so much more than some 'code'."
y "Well, we'll have much to ponder about the supposed truth of our reality..."
y 1d "But I must admit...{w=0.38}this whole experience has inspired me to write my own story about this!"
show yuri 1c
mc "It better be a best-seller!"
y 1q "I haven't written a full novel before...{w=0.38}but I'm sure I can figure it out."
y 1b "But...{w=0.38}perhaps one challenge at a time, right?"
show yuri 1c
mc "Yeah, I think we've earned some well deserved rest!"
y 1d "And rest we shall!"
y 1a "Farewell, [player]! And thank you for everything!"
y 1c "I hope everything goes well between you and Sayori!"
show yuri 1d
"Yuri says sweetly as she heads out the door."
show yuri at thide
hide yuri
show sayori 1d at t11 zorder 1
"Finally, Sayori is the last one to approach me."
"Though she doesn't seem overly excited or jovial, but rather at a little anxious."
s 1l "Hey, [player]..."
mc "Sayori. How are you doing?"
s "Well, I'm not sure I really know the right words for any of that..."

if encore_sayoriquestion_1 == True:

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "I read your letter..."
            show sayori 1g
            mc "And well...{w=0.38}I can't say I blame you..."
            mc "I let you down, at every turn."
            mc "You deserve someone better than me."
            s 1k "Look...{w=0.38}don't beat yourself up over me, [player]."
            s 1d "I'll be okay..."
            s 1l "I just hope you learned something from all this..."
            s 1h "About how to stay true and faithful to your friends and loved ones..."
            s 1k "Especially learning how to stay true to yourself..."
            show sayori 1g
            mc "I have..."
            mc "And...{w=0.38}I want another chance."
            mc "One last chance to make things right with you. That's all I ask."
            show sayori 1k
            mc "I'm more than willing to start over again."
            mc "Even if you want, we can just be friends and work our way back up if you like..."
            mc "I promise to you this time, I'll stay true and faithful to you and only you."
            show sayori 1k
            "Sayori is silent for a full minute before she makes eye contact with me again."
            show sayori 1g
            "Even then, she seems rather hesistant to accept my offer..."
            show sayori 1l
            "I brace for the worst before she ultimately let's out a slight laugh."
            s "Well...{w=0.38}I guess spending an evening with you wouldn't hurt..."
            s 1i "But we're going just as friends. Alright?"
            mc "I understand."
            show sayori 1g
            mc "I promise I'll earn back your trust."
            s 1d "I hope you do."


    if s_makeup == False:
        if n_love == False or y_love == False:
            mc "I take it you're a little overwhelemed?"
            s 1l "Yeah..."
            s 1d "But, I'm really happy..."
            mc "Sayori...{w=0.38}you know I love you..."
            show sayori 1y
            mc "I've enjoyed every single moment of our relationship, and even after all this, my feelings for you are stronger than ever."
            mc "I know the entire club nearly got destroyed because everyone loved me..."
            mc "But, so long as we're mindful and respectful around the others, I think there'll be no more issues going forward..."
            s "I hope so..."
            s 1l "It'll finally feel nice though that we won't have to hide our relationship from anyone anymore..."
            mc "Yeah, I was getting a little tired of keeping things secret anyway..."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I meant what I said..."
            mc "I want our relationship to succeed..."
            mc "I don't want to be with anyone else but you..."
            mc "And I'm not going to end something that we've worked so hard to maintain..."
            s 1d "Yeah...{w=0.38}I'm thankful you're serious about this..."
            s 1l "We've had some up's and down's, didn't we, [player]?"
            mc "Yeah...{w=0.38}well I was mostly the downside to the relationship..."
            s 1y "Well, this is our first relationship. We'll grow and learn from our mistakes..."

    if s_makeup == True:
        if n_love == False or y_love == False:
            mc "You're not surprised about my decision, are you?..."
            s 1d "No...{w=0.38}I'm just really happy..."
            s 1l "After everything...{w=0.38}you still want to be with me?"
            mc "Of course I do! I love you Sayori! Nothing's going to change my mind about you!"
            show sayori 1g
            mc "I care about you Sayori, I really do, and I think I've shown that in more ways than one recently."
            s 1y "Yeah...{w=0.38}I understand."
            s 1x "I'm really glad we get to spend some time together!"
            s 1y "You just know how to make me happy, don't you?"
            mc "It's the best job in the world..."

if encore_sayoriquestion_1 == False:
    mc "You're surprised, aren't you?"
    s 1l "Yeah, actually..."
    s 1k "I didn't think you wanted anything to do with me in that way..."
    s 2h "When i first confessed to you in the 'base game', I thought that was my only chance..."
    s 1k "I didn't think I was going to get another...{w=0.38}and I'm not sure I even deserve it..."
    mc "Sayori...{w=0.38}of course you deserve it."
    show sayori 1y
    mc "Sayori, you're a great girl and an awesome friend. You deserve to enjoy the upsides of life, to feel happy and to enjoy yourself for a change."
    mc "And I'm more than willing to spend my time and energy on you. It's what I want, and I won't take no for an answer!"
    s "I appreciate it, I really, really do..."
    s 1t "I just don't know how to handle this..."
    mc "Well...{w=0.38}why don't I take you someplace special tonight? I think we've both earned it."
    s 1y "Y-{w=0.38}yeah...{w=0.38}that would be great..."


mc "I do want you to promise me one thing, okay?"
s 1h "Yeah? What is it?"
show sayori 1k
mc "Get help for your depression, alright?"
mc "You know I hate seeing you like that..."
mc "It's for your own good that you you keep going to therapy."
mc "I'm more than willing to go with you..."
show sayori 1l
s "Well after this, I think I'll have plenty to talk about with whoever will be my therapist..."
s 1d "But, I'll do it. For you."
mc "Thank you, Sayori."
s 1y "There is one more thing..."
mc "Yeah?"
s 1y "Thank you so much for joining this club..."
s "It really means a lot to me that you agreed to join..."
s 1l "It saved me...{w=0.38}in so many ways that I didn't realize at first..."
mc "I know."
s 1d "Well, you ready to head out?"
mc "You go on ahead, I'll meet you at my place later."
s 2q "Okay!"
show sayori 1d
"Sayori and I exchange one last smile before she too heads out and disappears into the hallway."
show sayori at thide
hide sayori
stop music fadeout 2.0
"I sink back in a chair as Sayori leaves the clubroom, taking in the newfound silence."
"It's finally over..."
"All the tears..."
"All the name calling..."
"All the temper trantrums..."
"It's finally over..."
"I glance at my watch and notice that it's far past the normal time I'd be heading back home."
"Well, even if this world isn't real, it'd feel weird hanging around in here..."
"I pick up my stuff and begin heading out the door, but not before taking one last look at the clubroom."
"This really is no ordinary Literature Club..."
"But..."
"I don't think I'd have it any other way."
"I turn on my heel and head out the door to start the walk home."
scene black
with dissolve_scene_full
$ renpy.pause(delay=10.0)
scene bg residential_day
with open_eyes
"I take a seat down on my the steps and take in the view of my neighborhood."
"Looking up at the sky, I can see the a tint of orange forming in the vast blue sea that flies high above me."
"Even if it's not real, I always did enjoy it..."
"It always did instil a sense of calm and peace whenver I was troubled, and after today, those are two things I most surely need."
"Though going forward, for better or worse, things aren't going to be the same."
"Monika has a lot of work to earn everyone's trust back, but I'll do what I can to ensure she fairly earns it..."
"After all, who knows how much time Monika has really bought us?"
"How are we going to 'cross over' to this world to join the person who I'm supposed to represent?"
"Am I even real?"
"..."
"No matter..."
"Whatever challenges that await the Literature Club, I'll be right there facing there with them to face it down..."
"Because I know one thing for sure..."
"I care about them, with all my heart..."
"Sayori the most...{w=0.38}she'll need us now more than ever to help her conqueror her rainclouds and whatever else gets thrown her way."
"I know the player cares about her just as much as I do. I hope we can both care and watch over her together..."
"Thank you, whoever you are."
"You'll always be welcome in the Literature Club..."
show sayori 1bb at t11 zorder 1

if s_makeup == False:
    if n_love == True or y_love == True:
        s "Hey, [player]! You ready to head out?"
        show sayori 1by
        mc "You know it!"
        show sayori 1bq
        "I stand up to join Sayori as we head off towards the city to enjoy our evening together, as friends."


else:
    s "Hey, [player]! You ready to go for our date?"
    show sayori 1by
    mc "You know it!"
    show sayori 2bq
    "I take Sayori's hand as we walk off towards the city to enjoy our evening together."

scene black
with dissolve_scene_full
$ renpy.pause(delay=5.0)
call encore_credits


#Natsuki Ending

label ending_9:
"I want to be in a relationship with Natsuki."
show monika 1e at t11 zorder 1
m "Natsuki, huh?"
m 1m "She's a firey one, [player]..."
m 2e "You think you can handle her?."
mc "I think I can. She's cute on the outside but there's a lot more to her than that."
m 3k "Indeed she is! Well I think you two will be quite happy together!"
show monika 1d
mc "She'll  also need someone who she can trust to look after her."
m 1m "I agree. If there's one person she can trust now, it's you."

if encore_sayoriquestion_1 == True:
    m 1n "Sayori will be disappointed..."
    show monika 1m

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "Sayori..."
            m 1g "I know. I'm sorry..."
            mc "Well, maybe in time we'll patch things up..."
            m 2e "I hope you guys do."

    if s_makeup == False:
        if n_love == False or y_love == False:
            m "And I'll admit...{w=0.38}I'm surprised you want to end things with her."
            mc "I just don't feel the same way about her anymore..."
            mc "I think it's time we both moved on and saw different people..."
            m 2e "Well hey, I wish you two the best."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "It's...{w=0.38}for the best."
            mc "I don't think I've done our relationship any justice recently. I think it's best that I walk away and maybe start over again some day."
            m 2e "I hope it works out for you two."

    if s_makeup == True:
        if n_love == False or y_love == False:
            m 1g "And I have to say, I'm a little surprised..."
            m 1f "You were loyal to her for the most part..."
            mc "I think it's what's best for us right now. I don't feel the same about her anymore after all this."
            mc "I just hope she and I can stay friends..."
            m "Well hey, I hope you do. She's a good person, [player]."

if encore_sayoriquestion_1 == False:
    pass

play music mend fadein 1.0
m 1e "Well, this is where we depart..."
m 1n "Everyone's going to want to get their final say in before you go, so I won't delay them any longer."
m 1e "But...{w=0.38}I do want to say that I'm extremely grateful for all you've done here.."
m 1p "You've been there for us through our worst and best times..."
m 1m "You...{w=0.38}helped the others start to forgive me, and put me on the path towards learning how to forgive myself..."
m 3e "It's not something most people would do, [player]."
m 2k "You really are one of us!"
m 1j "And I'm glad that you're a member of the Literature Club!"
m 1e "This place really wouldn't be the same without you..."
m 1b "It wouldn't even exist without you!"
m 1e "You're the best member of the club that I've had the privliedge of knowing..."
m 3j "And I wish you the best in all your future endeavors!"
m 1e "Take care, [player]! I hope you've enjoyed your stay with us..."
show monika 1a at t11 zorder 1
"Monika and I share one last smile with each other before she grabs her stuff in disappears into the hallway."
show monika at thide
hide monika
"I feel a tap on my shoulder."
show sayori 1d at t11 zorder 1
"To my surprise, I turn around to see it's Sayori."
"Though she doesn't seem upeset, or even angry at me, but rather at peace."
s 1l "Hey, [player]..."
mc "Sayori. How are you doing?"
s "Well, I'm not sure I really know the right words for any of that..."

if encore_sayoriquestion_1 == True:

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "I read your letter..."
            show sayori 1g
            mc "And well...{w=0.38}I can't say I blame you..."
            mc "I let you down, at every turn."
            mc "You deserve someone better than me."
            s 1k "Look...{w=0.38}don't beat yourself up over me, [player]."
            s 1d "I'll be okay..."
            s 1l "I just hope you learned something from all this..."
            s 1h "About how to stay true and faithful to your friends and loved ones..."
            s 1k "Especially learning how to stay true to yourself..."
            s 1g "Our relationship may be over, but I just wanted to make sure you don't ever do something like this again."
            s 1k "Especially to Natsuki..."
            show sayori 1d
            mc "I learned, Sayori. Sucks that it had to be the hard way, but you know how hard headed I can be sometimes."
            s 1y "Well, at least that part of you didn't change..."
            s 1d "But, I'm glad you learned not do have this kind of relationship with anyone else ever again..."
            s "And I hope things between you and Natsuki work out alright..."
            mc "Thank you, Sayori..."
            mc "I'm really sorry ruined things between us..."
            s 1y "Well, maybe one day we can talk about it..."



    if s_makeup == False:
        if n_love == False or y_love == False:
            mc "I don't blame you..."
            mc "I take it you already know of my decision..."
            s 1k "Yeah, I do..."
            s 1g "I'm surprised..."
            mc "It's...{w=0.38}not you. It's me."
            show sayori 1k
            mc "Sayori, I still love you and care about you."
            mc "But, I've started to feel more attracted to Natsuki overtime and well..."
            mc "I think us not being together is the best solution going forward. I don't want to be disloyal to you..."
            s 1l "I see, and I appreciate you being honest with me..."
            s "I just wished we had more time to spend together, that's all..."
            mc "I know..."
            mc "I'm really sorry, Sayori. Please don't blame yourself."
            s 1k "I'll do my best..."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I know, and I'm sorry..."
            mc "I know I said that I wanted to work things out, but maybe it's better if we just see different people..."
            mc "I don't want to risk us running into more problems when my feelings for Natsuki haven't faded..."
            s 1k "I understand..."
            s "And I appreciate you being direct with me."
            s 1l "We had some up's and down's, didn't we, [player]?"
            mc "Yeah...{w=0.38}well I was mostly the downside to the relationship..."
            s 1y "Well, this was our first relationship. We'll grow and learn from our mistakes..."
            s 1d "And I hope things work out better for you and Natsuki."
            mc "Thank you, Sayori..."

    if s_makeup == True:
        if n_love == False or y_love == False:
            mc "I know..."
            s 1l "I'm...{w=0.38}surprised that you want to end things..."
            s 1k "After everything..."
            s 1g "Why?"
            mc "It's not because I don't love or care about you, Sayori..."
            show sayori 1g
            mc "But...{w=0.38}I've had feelings for Natsuki for a while now, and they haven't faded."
            mc "I love her too, and I know it's wrong us to be together if my feelings for her are stronger."
            show sayori 1k
            mc "We'd both be doing our relationship a disservice, and I wouldn't want to hurt you anymore than I already have by doing this..."
            s 1k "Yeah...{w=0.38}I get it."
            s 1d "I'm really glad we got to spend some time together, [player]..."
            s 1y "You really did make me the happiest I've ever been..."
            s 1k "I just wish I could've experienced it just a little bit longer..."
            mc "Me too..."
            mc "But please, whatever you do, don't blame yourself."
            s "I'll...{w=0.38}do my best."
            s 1d "I'll try."

if encore_sayoriquestion_1 == False:
    s 1k "Well I always knew it was going to be a long shot for us to ever be a couple..."
    s "The only chance of that was in the 'base game'..."
    mc "It's just...{w=0.38}not meant to be."
    mc "Sayori, you're a great girl and an awesome friend. I know one day you'll find someone who loves and cares for you."
    s "I appreciate it..."
    s 1d "I think you and Natsuki will be a great couple..."
    s 1y "I always knew you had feelings for her..."
    mc "You know me too well..."
    s 1q "Teehee~ Well I do!"


s 1y "I still hope we can be friends, [player]."
mc "Of course I still want to be friends with you!"
s 1l "Good...{w=0.38}I don't know what I'd do if you said no..."
show sayori 1g
mc "I do want you to promise me one thing, okay?"
s 1h "Yeah? What is it?"
show sayori 1k
mc "Get help for your depression, alright?"
mc "You know I hate seeing you like that..."
mc "It's for your own good that you you keep going to therapy."
show sayori 1l
s "Well after this, I think I'll have plenty to talk about with whoever will be my therapist..."
s 1d "But, I'll do it. For you."
mc "Thank you, Sayori."
s 2x "I'll see you around, okay?"
show sayori 1y
mc "You know it, cinnamon bun!"
s "I love it when you call me that..."
s 1q "See you around, [player]!"
s 1x "Thanks for being apart of this club!"
s 1y "It really means a lot to me that you agreed to join..."
mc "I know. That's why I did it."
show sayori 1d
"Sayori and I exchange one last smile before she too heads out and disappears into the hallway."
show sayori at thide
hide sayori
show yuri 1a at t11 zorder 1
"Yuri is the next one to approach me."
y 1q "It's hard to believe that we're finally at the end of this saga..."
mc "Yeah, I imagine everyone's feeling pretty relieved..."
y "I most certainly am."
y 1t "I know the others already said the same thing, but I really do want to thank everything you've done for us. Especially for me..."
y 1b "I also believe you and Natsuki deserve my congratulations on you two becoming offical."
mc "That's sweet of you, Yuri. Thank you!"
y 1g "I can't say she and I have always gotten along very well..."
y 1h "We've had our fair share of drama, and I do feel partially responsible for helping to nearly bring the club to ruin..."
y 1v "In the past we've called each other some of the most vile names..."
y 1w "We brought out the worst in each other..."
y 1k "But...{w=0.38}at the end of the day, I know she's a good person. She's head-strong and stubborn, but perhaps you can help her get over that.."
y 1q "You've been patient with me in the past, and perhaps it's time I be patient with her..."
mc "Thank you, Yuri."
y 1v "I must admit I do wish our relationship could've gone differently..."

if poem_giver == "Yuri":
    y 1q "I suspect that giving you the letter and my subsquent confession certainly didn't help things..."
    y 1t "You're just...{w=0.38}the first boy that I ever had serious feelings for..."
    y 1q "And with everything...{w=0.38}I just didn't know how to handle that..."
    y 1w "I sincerly regret my actions towards you, and everyone else..."
    y 1v "Even Monika didn't deserve that..."
    mc "You're not a bad person, Yuri. I hoped I helped you see that."

else:
    pass

mc "I'll admit...{w=0.38}I wish we all could've had the club experience without the drama..."
mc "And things could've gone better between us for sure..."
show yuri 1u
mc "But you're a beautiful, gracious and kind person, Yuri. You'll find someone worth your time. I believe in you."
y "Thank you. Coming from you, it means a lot..."
y 1b "I think we both learned a lot from this experience, wouldn't you agree?"
show yuri 1a
mc "For sure! I just hope going forward we'll be stronger as club together..."
y 1u "Yeah..."
mc "So...{w=0.38}what're you going to do about...{w=0.38}you know..."
y 3v "I think it's finally time that I start confronting this problem rather tha supressing it..."
y 1w "I'm not sure what the best way is, if everything is just a simulation now."
y 1h "Is there a way I can simply just undo my problem with the click of a button?"
mc "I can't say that I have the answer to that question. But, I know you'll figure something out. I'll be right here if you need my help."
y 1a "I'd very much appreciate that, [player]..."
y 1q "I really owe you a lot, don't I?"
mc "I just did what I thought was right back there. You and everyone else are so much more than some 'code'."
y "Well, we'll have much to ponder about the supposed truth of our reality..."
y 1d "But I must admit...{w=0.38}this whole experience has inspired me to write my own story about this!"
show yuri 1c
mc "It better be a best-seller!"
y 1q "I haven't written a full novel before...{w=0.38}but I'm sure I can figure it out."
y 1b "But...{w=0.38}perhaps one challenge at a time, right?"
show yuri 1c
mc "Yeah, I think we've earned some well deserved rest!"
y 1d "And rest we shall!"
y 1a "Farewell, [player]! Thank you for everything!"
y 1c "I hope everything goes well between you and Natsuki!"
show yuri 1d
"Yuri says sweetly as she heads out the door."
show yuri at thide
hide yuri
show natsuki 5u at t11 zorder 1
"Finally, Natsuki is the last one to approach me."
"At first we both struggle to find the right words to say to each other, but for once, she's the first to break the ice."
n 5q "So...{w=0.38}you picked me?"
n 1m "I...{w=0.38}don't know what to say, [player]..."
n 1q "I've never had a real relationship before..."
mc "There's a first time for everything, Natsuki."
show natsuki 1a
mc "But...{w=0.38}I love you...{w=0.38}and I want to be in a relationship with you."
show natsuki 1t
n "You're sure?"
mc "Positive."
mc "You're funny, sweet, a little rough around the edges, but I like it that way."
mc "I've had nothing but good laughs and fun times when I'm with you. You're an awesome person and I'd love to continue to be apart of your life."
n 5q "Wow..."
n "I knew you liked me but..."
n 5t "It's just...{w=0.38}we've had quite the ride, you and me..."
mc "Yeah...{w=0.38}it's really been something..."
n 3m "You know...{w=0.38}for the longest time, I wasn't sure if I could really trust you..."
n 3q "And well, I still ended up falling for you..."
n 1t "I don't really know why...{w=0.38}maybe because I thought you were funny, amazing..."
mc "Charming?"
n 1y "Pfft! Don't push your luck, [player]!"
n 5m "But what I'm trying to say is:{w=0.38}most boys wouldn't have done what you've done for me."
n 4n "You've listened to what I've had to say. You made sure I was always alright, and you literally saved all our lives back there!"
n 1q "I'm not sure how any of us are going to get over Monika trying to kill us..."
n 1a "But I think you set enough of an example for us to follow..."
mc "It's the least I could do, Natsuki."
mc "I know there's more to you than you're looks and the tough act you've put up. I'm glad I've gotten to know the real Natsuki."
n 1t "Eh, more or less..."
n 1z "Trust me, you haven't seen nothing yet!"
mc "I'm counting on it!"
n 3t "You know, if nothing what's happened outside of school is really 'real'..."
n 3z "Then that means I don't have to take anymore crap from my dad!"
mc "That is one way of looking at it for sure!"
n 5t "So...{w=0.38}if we're offical..."
n 5d "Doesn't that mean you get to take me out someplace nice?"
n 5t "Even if it really isn't 'real', I still wanna enjoy each other before things get serious again around here."
mc "Anything for you, Natsuki!"
n 5x "Jeez, you're a simp!"
mc "Hey!"
n 3y "Love you, [player]!"
mc "I know you do..."
n 1m "I actually mean it..."
n 5u "I've never felt this way towards anyone before. Like ever..."
n 5t "It...{w=0.38}feels nice..."
mc "Well, I'm glad it's something else other than anger and pain."
n 1j "It really is!"
n 2c "You ready to go?"
show natsuki 1c
mc "You go on ahead. I'll meet you at my place later."
n 1z "Alright! Don't be late!"
show natsuki 1z
mc "I'll try not to..."
show natsuki 1a
"Natsuki and I exchange one last smile before she too heads out and disappears into the hallway."
show natsuki at thide
hide natsuki
stop music fadeout 2.0
"I sink back in a chair as Natsuki leaves the clubroom, taking in the newfound silence."
"It's finally over..."
"All the tears..."
"All the name calling..."
"All the temper trantrums..."
"It's finally over..."
"I glance at my watch and notice that it's far past the normal time I'd be heading back home."
"Well, even if this world isn't real, it'd feel weird hanging around in here..."
"I pick up my stuff and begin heading out the door, but not before taking one last look at the clubroom."
"This really is no ordinary Literature Club..."
"But..."
"I don't think I'd have it any other way."
"I turn on my heel and head out the door to start the walk home."
scene black
with dissolve_scene_full
$ renpy.pause(delay=10.0)
scene bg residential_day
with open_eyes
"I take a seat down on my the steps and take in the view of my neighborhood."
"Looking up at the sky, I can see the a tint of orange forming in the vast blue sea that flies high above me."
"Even if it's not real, I always did enjoy it..."
"It always did instil a sense of calm and peace whenver I was troubled, and after today, those are two things I most surely need."
"Though going forward, for better or worse, things aren't going to be the same."
"Monika has a lot of work to earn everyone's trust back, but I'll do what I can to ensure she fairly earns it..."
"After all, who knows how much time Monika has really bought us?"
"How are we going to 'cross over' to this world to join the person who I'm supposed to represent?"
"Am I even real?"
"..."
"No matter..."
"Whatever challenges that await the Literature Club, I'll be right there facing there with them to face it down..."
"Because I know one thing for sure..."
"I care about them, with all my heart..."
"Natsuki the most...{w=0.38}she'll need us now more than ever to help her conqueror her trauma and anything else she may have dealt with."
"I know the player cares about her just as much as I do. I hope we can both care and watch over her together..."
"Thank you, whoever you are."
"You'll always be welcome in the Literature Club..."
show natsuki 4bc at t11 zorder 1
n "Hey, [player]! You ready to go for our date?"
show natsuki 2ba
mc "You know it!"
show natsuki 2bz
"I take Natsuki's hand as we walk off towards the city to enjoy our evening together."
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.0)
call encore_credits



#Monika Ending

label ending_10:
"I want to be in a relationship with Monika."
show monika 1g at t11 zorder 1
m "[player]..."
m "You're...{w=0.38}serious?!?"
m 3p "After everything I've done..."
m 1q "All the horrible sins I've committed just to try to win you over..."
m 1g "You...{w=0.38}still want me?!?"
mc "I do."
m 1f "Why?"

if hangout1!= "Monika" and hangout2!= "Monika" and hangout3!= "Monika":
    m 1g "We never even spent anytime together..."
    m 1n "Honestly I just put myself as an option as my last chance to try to be with you..."
    m 1p "I didn't think you'd actually pick me..."

else:
    pass

show monika 1p
mc "Monika...{w=0.38}I've always wanted to be with you."
show monika 1m
mc "You've always been the girl of my dreams. You're smart, funny, talented in just about everything..."
mc "I just never knew how to approach someone as incredible as you...{w=0.38}I just didn't think someone as average as me could ever be with someone as perfect as you..."
show monika 1e
mc "I even think I speak for the player in that regard..."
show monika 1m
mc "And I never knew that you liked me back...{w=0.38}let alone how far you where prepared to win me over..."
show monika 1p
mc "While I can't condone what you did, I do think you need someone to help you learn how to forgive yourself for what you did. I think that person that can best help you to do that is me."
mc "So...{w=0.38}I want to give you a second chance...{w=0.38}let me help you earn everyone's trust back..."
mc "That way you can learn to forgive yourself and move on."
show monika 1q
mc "I know you want someone who knows you're just more than what you make yourself to be. You're more than just some cute schoolgirl Monika. You've always been much more than that."
mc "Let me be the first person who treats you what you're really worth. I promise you won't be disappointed..."
show monika 1m
"Monika seems to be on the verge of either bursting out in pure joy or break down crying again."
show monika 2e
"After taking a brief moment to collect herself, Monika finally looks on at me with a warm smile."
m "[player], I..."
m 1m "No one has ever left me that speechless..."
m 1n "And no one has ever shown the level of kidness that you've shown me..."
m 1p "Even after everything I just did..."
m 1g "I...{w=0.38}really want to be in a relationship with you too, but..."
m 1f "You really think I'm deserving of that?"
mc "Monika, you deserve to find happiness."
show monika 1o
mc "What you did was wrong, and you have a lot of work to do to fully earn back everyone's trust, but..."
mc "I want to help you. I want you to better yourself. I don't want to see someone like you fall back into their old ways."
mc "I care too much about you to let that happen..."
show monika 1p
m "I-{w=0.38}I see..."
m 1e "Well, if that's what you want [player], then I'd be happy to be offically your's..."


if encore_sayoriquestion_1 == True:
    m 1n "Sayori will be disappointed though..."
    show monika 1m

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "Sayori..."
            m 1g "I know. I'm sorry..."
            mc "Well, maybe in time we'll patch things up..."
            m 2e "I hope you guys do. Maybe I can help with that somehow."

    if s_makeup == False:
        if n_love == False or y_love == False:
            m "And I'll admit...{w=0.38}I'm surprised you're choosing me over her..."
            mc "I just don't feel the same way about her anymore..."
            mc "I think it's time we both moved on and saw different people..."
            m 2e "Well hey, I wish you two the best. She really is a good person and I'm sure she'll find happiness one day."
            m 1m "If anyone deserves it more...{w=0.38}it's her."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "It's...{w=0.38}for the best."
            mc "I don't think I've done our relationship any justice recently. I think it's best that I walk away and maybe start over again some day."
            m 2e "I hope it works out for you two. I don't want to stop you two from being friends."

    if s_makeup == True:
        if n_love == False or y_love == False:
            m 1g "And I have to say, I'm a little surprised..."
            m 1f "You were loyal to her for the most part..."
            m 1m "It's why I'm still a little surprised that you chose me..."
            mc "I think it's what's best for us right now. I don't feel the same about her anymore after all this."
            mc "I just hope she and I can stay friends..."
            m "Well hey, I hope you do. She's a good person, [player]."


if encore_sayoriquestion_1 == False:
    pass




play music mend fadein 1.0
m 3n "I still can't really believe it's finally happening..."
m 1m "I think I need to take a moment to digest all this..."
m 1n "Everyone's going to want to get their final say in before we go, so I won't delay them any longer."
m 1e "Before I step aside for a moment...{w=0.38}I do want to say that I'm extremely grateful for all you've done here.."
m 1p "You've been there for us through our worst and best times..."
m 1m "You...{w=0.38}helped the others start to forgive me, and put me on the path towards learning how to forgive myself..."
m 3e "It's not something most people would do, [player]."
m 2k "You really are one of us!"
m 1j "And I'm glad that you're a member of the Literature Club!"
m 1e "This place really wouldn't be the same without you..."
m 1b "It wouldn't even exist without you!"
m 1e "You're the best member of the club that I've had the privliedge of knowing..."
m 3j "And I'm looking foward for what's to come for us!"
m 1e "Thank you again, [player]! I'll be back in a minute..."
show monika 1a at t11 zorder 1
"Monika and I share one last smile with each other before she walks off to the front of the room out of earshot."
show monika at thide
hide monika
"I then feel a tap on my shoulder."
show sayori 1k at t11 zorder 1
"To my surprise, I turn around to see it's Sayori."
"A flurry of emotions are on her face. I knew sooner or later things were going to come to this..."
s 1l "Hey, [player]..."
mc "Sayori...{w=0.38}how are you doing?"
s "Well, I'm not sure I really know the right words for any of that..."

if encore_sayoriquestion_1 == True:

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "I read your letter..."
            show sayori 1g
            mc "And well...{w=0.38}I can't say I blame you..."
            mc "I let you down, at every turn."
            mc "You deserve someone better than me."
            s 1k "Look...{w=0.38}don't beat yourself up over me, [player]."
            s 1d "I'll be okay..."
            s 1l "I just hope you learned something from all this..."
            s 1h "About how to stay true and faithful to your friends and loved ones..."
            s 1k "Especially learning how to stay true to yourself..."
            s 1g "Our relationship may be over, but I just wanted to make sure you don't ever do something like this again."
            s 1k "Especially to Monika..."
            show sayori 1d
            mc "I learned, Sayori. Sucks that it had to be the hard way, but you know how hard headed I can be sometimes."
            s 1y "Well, at least that part of you didn't change..."
            s 1d "But, I'm glad you learned not do have this kind of relationship with anyone else ever again..."
            s "And I hope things between you and Natsuki work out alright..."
            mc "Thank you, Sayori..."
            mc "I'm really sorry ruined things between us..."
            s 1y "Well, maybe one day we can talk about it..."



    if s_makeup == False:
        if n_love == False or y_love == False:
            mc "I don't blame you..."
            mc "I take it you already know of my decision..."
            s 1k "Yeah, I do..."
            s 1g "I'm surprised..."
            mc "It's...{w=0.38}not you. It's me."
            show sayori 1k
            mc "Sayori, I still love you and care about you."
            mc "But, I've started to feel more attracted to Monika overtime and well..."
            mc "I think us not being together is the best solution going forward. I don't want to be disloyal to you..."
            s 1l "I see, and I appreciate you being honest with me..."
            s "I just wished we had more time to spend together, that's all..."
            mc "I know..."
            mc "I'm really sorry, Sayori. Please don't blame yourself."
            s 1k "I'll do my best..."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I know, and I'm sorry..."
            mc "I know I said that I wanted to work things out, but maybe it's better if we just see different people..."
            mc "I don't want to risk us running into more problems when my feelings for Yuri haven't faded..."
            s 1k "I understand..."
            s "And I appreciate you being direct with me."
            s 1l "We had some up's and down's, didn't we, [player]?"
            mc "Yeah...{w=0.38}well I was mostly the downside to the relationship..."
            s 1y "Well, this was our first relationship. We'll grow and learn from our mistakes..."
            s 1d "And I hope things work out better for you and Monika."
            mc "Thank you, Sayori..."

    if s_makeup == True:
        if n_love == False or y_love == False:
            mc "I know..."
            s 1l "I'm...{w=0.38}surprised that you want to end things..."
            s 1k "After everything..."
            s 1g "Why?"
            mc "It's not because I don't love or care about you, Sayori..."
            show sayori 1g
            mc "But...{w=0.38}I've had feelings for Monika for a while now, and they haven't faded."
            mc "I love her too, and I know it's wrong us to be together if my feelings for her are stronger."
            show sayori 1k
            mc "We'd both be doing our relationship a disservice, and I wouldn't want to hurt you anymore than I already have by doing this..."
            s 1k "Yeah...{w=0.38}I get it."
            s 1d "I'm really glad we got to spend some time together, [player]..."
            s 1y "You really did make me the happiest I've ever been..."
            s 1k "I just wish I could've experienced it just a little bit longer..."
            mc "Me too..."
            mc "But please, whatever you do, don't blame yourself."
            s "I'll...{w=0.38}do my best."
            s 1d "I'll try."

if encore_sayoriquestion_1 == False:
    s 1k "Well I always knew it was going to be a long shot for us to ever be a couple..."
    s "The only chance of that was in the 'base game'..."
    mc "It's just...{w=0.38}not meant to be."
    mc "Sayori, you're a great girl and an awesome friend. I know one day you'll find someone who loves and cares for you."
    s "I appreciate it..."
    s 1d "I think you and Monika will be a great couple..."
    s 1y "I always knew you had feelings for her..."
    mc "You know me too well..."
    s 1q "Teehee~ Well I do!"



s 1h "Still...{w=0.38}I do want to share my concern about something, [player]..."
mc "Sure, anything!"
s 1k "Look...{w=0.38}I'll support your decision either way. I want you to be happy..."
s 1h "And I want to forgive Monika too, but..."
s 1k "She did so many horrible things to us..."

if encore_sayoriquestion_1 == True:
    s 1g "She's the one that's been trying to split us apart..."

if encore_sayoriquestion_1 == False:
    pass

s 1f "And you just want to jump into a relationship with her?"
mc "Look...{w=0.38}I completely understand that you don't trust her right now, and for a good reason."
show sayori 1k
mc "She needs to earn everyone's trust back and she needs to learn to forgive herself first."
mc "I think I'm in the best position to make sure she doesn't fall back into her old ways. We both know she deserves happiness just like we all do..."
s 1k "I know..."
s "I just wish things weren't so sudden..."
mc "I get that. I'm sorry."
s 1d "But I'm glad you're going to be helping Monika out. She needs you, [player]."
s 1y "I just still hope we can be friends, [player]."
mc "Of course I still want to be friends with you!"
s 1l "Good...{w=0.38}I don't know what I'd do if you said no..."
show sayori 1g
mc "I do want you to promise me one thing, okay?"
s 1h "Yeah? What is it?"
show sayori 1k
mc "Get help for your depression, alright?"
mc "You know I hate seeing you like that..."
mc "It's for your own good that you you keep going to therapy."
show sayori 1l
s "Well after this, I think I'll have plenty to talk about with whoever will be my therapist..."
s 1d "But, I'll do it. For you."
mc "Thank you, Sayori."
s 2x "I'll see you around, okay?"
show sayori 1y
mc "You know it, cinnamon bun!"
s "I love it when you call me that..."
s 1q "See you around, [player]!"
s 1x "Thanks for being apart of this club!"
s 1y "It really means a lot to me that you agreed to join..."
mc "I know. That's why I did it."
show sayori 1d
"Sayori and I exchange one last smile before she too heads out and disappears into the hallway."
show sayori at thide
hide sayori
show natsuki 5u at t11 zorder 1
"Natsuki is the next one to approach me."
"At first we both struggle to find the right words to say to each other, given our history, but for once, she's the first to break the ice."
n 5q "I'll cut right to the chase, [player]..."
n 5m "You want to be with Monika after everything she just did?"
n 5q "I heard everything you said to Sayori, so you don't need to repeat yourself to me..."
n 5n "But, I just hope you know what you're doing."
mc "I understand your concern, and I promise you Monika is going to change and be a different person, given time."
n 5t "Well...{w=0.38}I guess that's all I can really ask for..."
n 5t "You know, we've had quite the ride, you and me..."
mc "Yeah...{w=0.38}it's really been something..."
n 3m "You know...{w=0.38}for the longest time, I wasn't sure if I could really trust you..."
n 3q "And well, I still ended up falling for you..."
n 1t "I don't really know why...{w=0.38}maybe because I thought you were actually intresting, funny..."
mc "Charming?"
n 1y "Pfft! Don't push your luck, [player]!"

if poem_giver == "Natsuki":
    n 1u "I really do regret about starting all this drama though..."
    n 1n "I liked you...{w=0.38}a lot...{w=0.38}and I just didn't know how to approach you..."
    n "I never meant to hurt you or anyone."
    mc "I know you didn't, Natsuki."

else:
    pass


n 5m "But what I'm trying to say is:{w=0.38}most boys wouldn't have done what you've done for me."
n 1u "I know we've certainly had our up's and down's, and yeah, things could've gone better..."
n 1n "But I really, really, want to thank you for saving me back there."
n 1q "I'm not sure how any of us are going to get over Monika trying to kill us..."
n "And I don't know how I'm going to deal with you two being together after everything..."
n 1a "But I think you set enough of an example for us to follow..."
mc "It's the least I could do, Natsuki."
mc "I know there's more to you than you're looks and the tough act you've put up. I'm glad I've gotten to know the real Natsuki."
n 1t "Eh, more or less..."
n 1s "I'm still not sure how I feel about all this being some sort of 'game'..."
n 1t "But...{w=0.38}that means I don't have to worry about my dad anymore..."
mc "That's true. Still, you don't have anything like Monika's powers. What're you gonna do?"
n 1a "I'll figure something out."
n 1y "But I'm not going back there again! That's for sure!"
show natsuki 1z
mc "Glad to hear it, Natsuki!"
n 1t "Yeah..."
n 1m "So I guess I'll see you around?"
show natsuki 1a
mc "Of course! This club wouldn't be as entertaining without you in it!"
n 4l "That's for damn sure!"
n 1z "Bye, [player]!"
n 1l "And hey, I hope you keep Monika happy."
n 1t "You'll be hearing from me if you don't!"
n 1n "Especially if she tries to kill us again."
mc "Noted, Natsuki."
show natsuki at thide
hide natsuki
show yuri 1a at t11 zorder 1
"Yuri is the next one to approach me."
y 1q "It's hard to believe that we're finally at the end of this saga..."
mc "Yeah, I imagine everyone's feeling pretty relieved..."
y "I most certainly am."
y 1t "I know the others already said the same thing, but I really do want to thank everything you've done for us. Especially for me..."
y 1h "I also can't say I'm particuarly thrilled with your decision to be with Monika after what we've just experienced."
mc "I understand your reservations Yuri."
y 1g "Part of me wants revenge for what she's done to me..."
y 1h "She was always in the shadows mainipulating everything..."
y 1v "She's the one that ultimately pushed me to cut by messing with my emotions..."
y 1w "And she almost killed us..."
y 1k "But...{w=0.38}I think she deserves a chance at redemption. It won't come easily, but she deserves a chance to right her wrongs."
y 1q "You've been patient with me in the past, and perhaps it's time I be patient with her..."
mc "Thank you, Yuri."
y 1v "Still, I do wish our relationship could've gone differently..."

if poem_giver == "Yuri":
    y 1q "I suspect that giving you the letter and my subsquent confession certainly didn't help things..."
    y 1t "You're just...{w=0.38}the first boy that I ever had serious feelings for..."
    y 1q "And with everything...{w=0.38}I just didn't know how to handle that..."
    y 1w "I sincerly regret my actions towards you, and everyone else..."
    y 1v "Even Monika didn't deserve that..."
    mc "You're not a bad person, Yuri. I hoped I helped you see that."

else:
    pass

mc "I'll admit...{w=0.38}I wish we all could've had the club experience without the drama..."
mc "And things could've gone better between us for sure..."
show yuri 1u
mc "But you're a beautiful, gracious and kind person, Yuri. You'll find someone worth your time. I believe in you."
y "Thank you. Coming from you, it means a lot..."
y 1b "I think we both learned a lot from this experience, wouldn't you agree?"
show yuri 1a
mc "For sure! I just hope going forward we'll be stronger as club together..."
y 1u "Yeah..."
mc "So...{w=0.38}what're you going to do about...{w=0.38}you know..."
y 3v "I think it's finally time that I start confronting this problem rather tha supressing it..."
y 1w "I'm not sure what the best way is, if everything is just a simulation now."
y 1h "Is there a way I can simply just undo my problem with the click of a button?"
mc "I can't say that I have the answer to that question. But, I know you'll figure something out. I'll be right here if you need my help."
y 1a "I'd very much appreciate that, [player]..."
y 1q "I really owe you a lot, don't I?"
mc "I just did what I thought was right back there. You and everyone else are so much more than some 'code'."
y "Well, we'll have much to ponder about the supposed truth of our reality..."
y 1d "But I must admit...{w=0.38}this whole experience has inspired me to write my own story about this!"
show yuri 1c
mc "It better be a best-seller!"
y 1q "I haven't written a full novel before...{w=0.38}but I'm sure I can figure it out."
y 1b "But...{w=0.38}perhaps one challenge at a time, right?"
show yuri 1c
mc "Yeah, I think we've earned some well deserved rest!"
y 1d "And rest we shall!"
y 1a "Farewell, [player]! Thank you for everything!"
y 1c "I hope everything goes well between you and Monika!"
show yuri 1d
"Yuri says sweetly as she heads out the door."
show yuri at thide
hide yuri
show monika 1m at t11 zorder 1
"Monika walks back up to me as Yuri exits the clubroom."
m 1n "Well...{w=0.38}that wasn't terrible..."
m 1m "I really was expecting harsher reactions..."
show monika 1e
mc "Everyone's willing to give you another chance, Monika. You just have to earn it."
m 2e "I know, and I want to earn their trust back."
m 1e "I'm willing to do it...{w=0.38}the right way this time."
m 1m "I just...{w=0.38}hope I can do it..."
mc "Well...{w=0.38}why don't we talk about that tonight. Just you and me."
m 1g "You...{w=0.38}want to take me out somewhere?"
mc "Yeah, I do."
show monika 1m
mc "I think we both earned an evening to ourselves to relax and digest what happened."
m 1n "You're really too kind, [player]..."
m 3n "Well, there's no use staying around here..."
m 1b "Shall we go?"
show monika 1a
mc "You go on ahead, I'll meet you at my place later."
m 1j "Okay! I'll see you soon, [player]!"
"Monika and I exchange one last smile before she too heads out and disappears into the hallway."
show monika at thide
hide monika
stop music fadeout 2.0
"I sink back in a chair as Monika leaves the clubroom, taking in the newfound silence."
"It's finally over..."
"All the tears..."
"All the name calling..."
"All the temper trantrums..."
"It's finally over..."
"I glance at my watch and notice that it's far past the normal time I'd be heading back home."
"Well, even if this world isn't real, it'd feel weird hanging around in here..."
"I pick up my stuff and begin heading out the door, but not before taking one last look at the clubroom."
"This really is no ordinary Literature Club..."
"But..."
"I don't think I'd have it any other way."
"I turn on my heel and head out the door to start the walk home."
scene black
with dissolve_scene_full
$ renpy.pause(delay=10.0)
scene bg residential_day
with open_eyes
"I take a seat down on my the steps and take in the view of my neighborhood."
"Looking up at the sky, I can see the a tint of orange forming in the vast blue sea that flies high above me."
"Even if it's not real, I always did enjoy it..."
"It always did instil a sense of calm and peace whenver I was troubled, and after today, those are two things I most surely need."
"Though going forward, for better or worse, things aren't going to be the same."
"Monika has a lot of work to earn everyone's trust back, but I'll do what I can to ensure she fairly earns it..."
"After all, who knows how much time Monika has really bought us?"
"How are we going to 'cross over' to this world to join the person who I'm supposed to represent?"
"Am I even real?"
"..."
"No matter..."
"Whatever challenges that await the Literature Club, I'll be right there facing there with them to face it down..."
"Because I know one thing for sure..."
"I care about them, with all my heart..."
"Monika the most...{w=0.38}she'll need us now more than ever to help her learn how to forgive herself and how to become a better person."
"I know the player cares about her just as much as I do. I hope we can both care and watch over her together..."
"Thank you, whoever you are."
"You'll always be welcome in the Literature Club..."
show monika 1bb at t11 zorder 1
m "Hey, [player]! Ready to go?"
show monika 5ba at t11 zorder 1
mc "You know it!"
show monika 1bj at t11 zorder 1
"I take Monika's hand as we walk off towards the city to enjoy our evening together."
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.0)
call encore_credits


call encore_credits


#Yuri Ending

label ending_11:
"I want to be in a relationship with Yuri."
show monika 1e at t11 zorder 1
m "Yuri, huh?"
m 1m "I always thought of her as a maiden of mystery..."
m 2e "But, she's a good girl at heart. Quite passionate. You think you can handle her?"
mc "I think I can. She's a deep, intresting person. I feel like I haven't even scratched the surface with her, even after all this time."
m 3k "Well I can assure you'll never get bored with her, that's for sure!"
show monika 1d
mc "She'll also need someone to make sure she doesn't fall into her old habits..."
m 3m "Indeed..."
m 3n "It'll take time for her to get over her problem, but if anyone can help her through those trying times, it's you."

if encore_sayoriquestion_1 == True:
    m 1n "Sayori will be disappointed..."
    show monika 1m

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "Sayori..."
            m 1g "I know. I'm sorry..."
            mc "Well, maybe in time we'll patch things up..."
            m 2e "I hope you guys do."

    if s_makeup == False:
        if n_love == False or y_love == False:
            m "And I'll admit...{w=0.38}I'm surprised you want to end things with her."
            mc "I just don't feel the same way about her anymore..."
            mc "I think it's time we both moved on and saw different people..."
            m 2e "Well hey, I wish you two the best."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "It's...{w=0.38}for the best."
            mc "I don't think I've done our relationship any justice recently. I think it's best that I walk away and maybe start over again some day."
            m 2e "I hope it works out for you two."

    if s_makeup == True:
        if n_love == False or y_love == False:
            m 1g "And I have to say, I'm a little surprised..."
            m 1f "You were loyal to her for the most part..."
            mc "I think it's what's best for us right now. I don't feel the same about her anymore after all this."
            mc "I just hope she and I can stay friends..."
            m "Well hey, I hope you do. She's a good person, [player]."

if encore_sayoriquestion_1 == False:
    pass

play music mend fadein 1.0
m 1e "Well, this is where we depart..."
m 1n "Everyone's going to want to get their final say in before you go, so I won't delay them any longer."
m 1e "But...{w=0.38}I do want to say that I'm extremely grateful for all you've done here.."
m 1p "You've been there for us through our worst and best times..."
m 1m "You...{w=0.38}helped the others start to forgive me, and put me on the path towards learning how to forgive myself..."
m 3e "It's not something most people would do, [player]."
m 2k "You really are one of us!"
m 1j "And I'm glad that you're a member of the Literature Club!"
m 1e "This place really wouldn't be the same without you..."
m 1b "It wouldn't even exist without you!"
m 1e "You're the best member of the club that I've had the privliedge of knowing..."
m 3j "And I wish you the best in all your future endeavors!"
m 1e "Take care, [player]! I hope you've enjoyed your stay with us..."
show monika 1a at t11 zorder 1
"Monika and I share one last smile with each other before she grabs her stuff in disappears into the hallway."
show monika at thide
hide monika
"I feel a tap on my shoulder."
show sayori 1d at t11 zorder 1
"To my surprise, I turn around to see it's Sayori."
"Though she doesn't seem upeset, or even angry at me, but rather at peace."
s 1l "Hey, [player]..."
mc "Sayori. How are you doing?"
s "Well, I'm not sure I really know the right words for any of that..."

if encore_sayoriquestion_1 == True:

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "I read your letter..."
            show sayori 1g
            mc "And well...{w=0.38}I can't say I blame you..."
            mc "I let you down, at every turn."
            mc "You deserve someone better than me."
            s 1k "Look...{w=0.38}don't beat yourself up over me, [player]."
            s 1d "I'll be okay..."
            s 1l "I just hope you learned something from all this..."
            s 1h "About how to stay true and faithful to your friends and loved ones..."
            s 1k "Especially learning how to stay true to yourself..."
            s 1g "Our relationship may be over, but I just wanted to make sure you don't ever do something like this again."
            s 1k "Especially to Yuri..."
            show sayori 1d
            mc "I learned, Sayori. Sucks that it had to be the hard way, but you know how hard headed I can be sometimes."
            s 1y "Well, at least that part of you didn't change..."
            s 1d "But, I'm glad you learned not do have this kind of relationship with anyone else ever again..."
            s "And I hope things between you and Natsuki work out alright..."
            mc "Thank you, Sayori..."
            mc "I'm really sorry ruined things between us..."
            s 1y "Well, maybe one day we can talk about it..."



    if s_makeup == False:
        if n_love == False or y_love == False:
            mc "I don't blame you..."
            mc "I take it you already know of my decision..."
            s 1k "Yeah, I do..."
            s 1g "I'm surprised..."
            mc "It's...{w=0.38}not you. It's me."
            show sayori 1k
            mc "Sayori, I still love you and care about you."
            mc "But, I've started to feel more attracted to Yuri overtime and well..."
            mc "I think us not being together is the best solution going forward. I don't want to be disloyal to you..."
            s 1l "I see, and I appreciate you being honest with me..."
            s "I just wished we had more time to spend together, that's all..."
            mc "I know..."
            mc "I'm really sorry, Sayori. Please don't blame yourself."
            s 1k "I'll do my best..."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I know, and I'm sorry..."
            mc "I know I said that I wanted to work things out, but maybe it's better if we just see different people..."
            mc "I don't want to risk us running into more problems when my feelings for Yuri haven't faded..."
            s 1k "I understand..."
            s "And I appreciate you being direct with me."
            s 1l "We had some up's and down's, didn't we, [player]?"
            mc "Yeah...{w=0.38}well I was mostly the downside to the relationship..."
            s 1y "Well, this was our first relationship. We'll grow and learn from our mistakes..."
            s 1d "And I hope things work out better for you and Yuri."
            mc "Thank you, Sayori..."

    if s_makeup == True:
        if n_love == False or y_love == False:
            mc "I know..."
            s 1l "I'm...{w=0.38}surprised that you want to end things..."
            s 1k "After everything..."
            s 1g "Why?"
            mc "It's not because I don't love or care about you, Sayori..."
            show sayori 1g
            mc "But...{w=0.38}I've had feelings for Yuri for a while now, and they haven't faded."
            mc "I love her too, and I know it's wrong us to be together if my feelings for her are stronger."
            show sayori 1k
            mc "We'd both be doing our relationship a disservice, and I wouldn't want to hurt you anymore than I already have by doing this..."
            s 1k "Yeah...{w=0.38}I get it."
            s 1d "I'm really glad we got to spend some time together, [player]..."
            s 1y "You really did make me the happiest I've ever been..."
            s 1k "I just wish I could've experienced it just a little bit longer..."
            mc "Me too..."
            mc "But please, whatever you do, don't blame yourself."
            s "I'll...{w=0.38}do my best."
            s 1d "I'll try."

if encore_sayoriquestion_1 == False:
    s 1k "Well I always knew it was going to be a long shot for us to ever be a couple..."
    s "The only chance of that was in the 'base game'..."
    mc "It's just...{w=0.38}not meant to be."
    mc "Sayori, you're a great girl and an awesome friend. I know one day you'll find someone who loves and cares for you."
    s "I appreciate it..."
    s 1d "I think you and Yuri will be a great couple..."
    s 1y "I always knew you had feelings for her..."
    mc "You know me too well..."
    s 1q "Teehee~ Well I do!"


s 1y "I still hope we can be friends, [player]."
mc "Of course I still want to be friends with you!"
s 1l "Good...{w=0.38}I don't know what I'd do if you said no..."
show sayori 1g
mc "I do want you to promise me one thing, okay?"
s 1h "Yeah? What is it?"
show sayori 1k
mc "Get help for your depression, alright?"
mc "You know I hate seeing you like that..."
mc "It's for your own good that you you keep going to therapy."
show sayori 1l
s "Well after this, I think I'll have plenty to talk about with whoever will be my therapist..."
s 1d "But, I'll do it. For you."
mc "Thank you, Sayori."
s 2x "I'll see you around, okay?"
show sayori 1y
mc "You know it, cinnamon bun!"
s "I love it when you call me that..."
s 1q "See you around, [player]!"
s 1x "Thanks for being apart of this club!"
s 1y "It really means a lot to me that you agreed to join..."
mc "I know. That's why I did it."
show sayori 1d
"Sayori and I exchange one last smile before she too heads out and disappears into the hallway."
show sayori at thide
hide sayori
show natsuki 5u at t11 zorder 1
"Natsuki is the next one to approach me."
"At first we both struggle to find the right words to say to each other, given our history, but for once, she's the first to break the ice."
n 5t "So you're going with Yuri, huh?"
n "Can't say I'm too surprised. You always did strike me as her type of guy..."
n 5l "I hope everything works out between you two."
mc "Thank you, Natsuki. I really appreciate it."
n 5t "Well...{w=0.38}it's the least I could do..."
n 5t "We've had quite the ride, you and me..."
mc "Yeah...{w=0.38}it's really been something..."
n 3m "You know...{w=0.38}for the longest time, I wasn't sure if I could really trust you..."
n 3q "And well, I still ended up falling for you..."
n 1t "I don't really know why...{w=0.38}maybe because I thought you were actually intresting, smart..."
mc "Charming?"
n 1y "Pfft! Don't push your luck, [player]!"

if poem_giver == "Natsuki":
    n 1u "I really do regret about starting all this drama though..."
    n 1n "I liked you...{w=0.38}a lot...{w=0.38}and I just didn't know how to approach you..."
    n "I never meant to hurt you or anyone."
    mc "I know you didn't, Natsuki."

else:
    pass


n 5m "But what I'm trying to say is:{w=0.38}most boys wouldn't have done what you've done for me."
n 1u "I know we've certainly had our up's and down's, and yeah, things could've gone better..."
n 1n "But I really, really, want to thank you for saving me back there."
n 1q "I'm not sure how any of us are going to get over Monika trying to kill us..."
n 1a "But I think you set enough of an example for us to follow..."
mc "It's the least I could do, Natsuki."
mc "I know there's more to you than you're looks and the tough act you've put up. I'm glad I've gotten to know the real Natsuki."
n 1t "Eh, more or less..."
n 1s "I'm still not sure how I feel about all this being some sort of 'game'..."
n 1t "But...{w=0.38}that means I don't have to worry about my dad anymore..."
mc "That's true. Still, you don't have anything like Monika's powers. What're you gonna do?"
n 1a "I'll figure something out."
n 1y "But I'm not going back there again! That's for sure!"
show natsuki 1z
mc "Glad to hear it, Natsuki!"
n 1t "Yeah..."
n 1m "So I guess I'll see you around?"
show natsuki 1a
mc "Of course! This club wouldn't be as entertaining without you in it!"
n 4l "That's for damn sure!"
n 1z "Bye, [player]!"
n 1l "And hey, I hope you keep Yuri happy."
n 1t "You'll be hearing from me if you don't!"
mc "Noted, Natsuki."
show natsuki at thide
hide natsuki
show yuri 3q at t11 zorder 1
"Finally, Yuri is the last one to approach me."
y "[player]...{w=0.38}I'm a little surprised..."
y 3t "I can't say I was really expecting you to pick me..."
y 1q "Even though I was hoping you would..."
show yuri 1u
mc "Yuri, why wouldn't I choose you?"
mc "I love you...{w=0.38}and I want to be in a relationship with you."
y 2t "May I inquire as to why?"
show yuri 1t
mc "You're passionate, sweet, a little reserved and timid, but I like it that way."
mc "I've had nothing but rich and wonderful experiences when I'm with you. You're an awesome person and I'd love to continue to be apart of your life."
y 3q "Wow..."
y "I knew you liked me but..."
y "It's just...{w=0.38}we've had quite an adventure together..."
mc "Yeah...{w=0.38}it's really been something..."
y 1t "I must confess..{w=0.38}for the longest time, I wasn't sure if I was really wise to open up to you..."
y 1q "Such instances of doing that in the past hardly ever worked out for me in the long run but..."
y 1s "You've been different..{w=0.38}you always listened to what I had to say and showed that you actually cared about me..."
mc "It's also because I'm such a charmer..."
y 1q "I'm sure that was a factor..."
y 3s "But really...{w=0.38}I can't think of too many people that would risk their lives to save me..."
y 1u "And I can't think of any non-fiction persons that have shown the level of genuiene intrest and empathy for someone like me..."
y 1v "A girl whose alaways tried to stay in the background as much as possible...{w=0.38}yet I couldn't escape your notice.."
y 1s "I'm incredibly thankful that you're giving me a chance, [player]."
show yuri 1d
mc "It's my pleasure, Yuri!"
show yuri 1e
mc "So...{w=0.38}what're you going to do about...{w=0.38}you know..."
y 3v "I think it's finally time that I start confronting this problem rather tha supressing it..."
y 1w "I'm not sure what the best way is, if everything is just a simulation now."
y 1h "Is there a way I can simply just undo my problem with the click of a button?"
mc "I can't say that I have the answer to that question. But, I know you'll figure something out. I'll be right here if you need my help."
y 1a "I'd very much appreciate that, [player]..."
y 1q "I really owe you a lot, don't I?"
mc "I just did what I thought was right back there. You and everyone else are so much more than some 'code'."
y "Well, we'll have much to ponder about the supposed truth of our reality..."
y 1d "But I must admit...{w=0.38}this whole experience has inspired me to write my own story about this!"
show yuri 1c
mc "It better be a best-seller!"
y 1q "I haven't written a full novel before...{w=0.38}but I'm sure I can figure it out."
y 1b "But...{w=0.38}perhaps one challenge at a time, right?"
show yuri 1c
mc "Yeah, I think we've earned some well deserved rest!"
y 1d "And rest we shall!"
y 1s "But I think we've earned an evening to enjoy ourselves, wouldn't you agree?"
mc "That sounds lovely Yuri! I'd love to take you out someplace nice!"
y 1d "That's fantastic!"
y 1b "Shall we go?"
show yuri 1a
mc "You go on ahead, I'll meet you at my place later."
y 1c "Alright then! I'll see you later!"
show yuri 1d
"Yuri says sweetly as she heads out the door."
show yuri at thide
hide yuri
stop music fadeout 2.0
"I sink back in a chair as Yuri leaves the clubroom, taking in the newfound silence."
"It's finally over..."
"All the tears..."
"All the name calling..."
"All the temper trantrums..."
"It's finally over..."
"I glance at my watch and notice that it's far past the normal time I'd be heading back home."
"Well, even if this world isn't real, it'd feel weird hanging around in here..."
"I pick up my stuff and begin heading out the door, but not before taking one last look at the clubroom."
"This really is no ordinary Literature Club..."
"But..."
"I don't think I'd have it any other way."
"I turn on my heel and head out the door to start the walk home."
scene black
with dissolve_scene_full
$ renpy.pause(delay=10.0)
scene bg residential_day
with open_eyes
"I take a seat down on my the steps to my house and lay my backpack right next to me."
"Looking up at the sky, I can see the a tint of orange forming in the vast blue sea that flies high above me."
"Even if it's not real, I always did enjoy it..."
"It always did instil a sense of calm and peace whenver I was troubled, and after today, those are two things I most surely need."
"Though going forward, for better or worse, things aren't going to be the same."
"Monika has a lot of work to earn everyone's trust back, but I'll do what I can to ensure she fairly earns it..."
"After all, who knows how much time Monika has really bought us?"
"How are we going to 'cross over' to this world to join the person who I'm supposed to represent?"
"Am I even real?"
"..."
"No matter..."
"Whatever challenges that await the Literature Club, I'll be right there facing there with them to face it down..."
"Because I know one thing for sure..."
"I care about them, with all my heart..."
"And I know the player does too."
"Thank you, whoever you are."
"You'll always be welcome in the Literature Club..."
show yuri 1bb at t11 zorder 1
y "Hello, [player]! You ready to enjoy our evening out?"
show yuri 1ba
mc "You know it!"
show yuri 1bc
"I take Yuri's hand as we walk off towards the city to enjoy our evening together."
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.0)
call encore_credits




#Single Ending

label ending_12:
"..."
"I think it's best that I stay single for right now..."
show monika 1e at t11 zorder 1
m "So...{w=0.38}that's your choice, huh?"
m 1m "I will say I wasn't expecting that one."
m 2e "But I think that in the interest of the club, it's the right thing to do."
mc "This club nearly tore itself apart because of me."
mc "I think I should just not be involved with anyone like that for right now."
mc "Maybe I'll take a look into that again some other day, but not after this..."
m 1m "I understand, [player]."

if encore_sayoriquestion_1 == True:
    m 1n "Sayori will be disappointed..."
    show monika 1m

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "Sayori..."
            m 1g "I know. I'm sorry..."
            mc "Well, maybe in time we'll patch things up..."
            m 2e "I hope you guys do."

    if s_makeup == False:
        if n_love == False or y_love == False:
            m "And I'll admit...{w=0.38}I'm surprised you want to end things with her."
            mc "It's what's in the best interests of the club right now."
            mc "Maybe when we all really do move on from this, then maybe I'll take a look at it again."
            m 2e "Well hey, I wish you two the best."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "It's...{w=0.38}for the best."
            mc "I don't think I've done our relationship any justice recently. I think it's best that I walk away and maybe start over again some day."
            m 2e "I hope it works out for you two."

    if s_makeup == True:
        if n_love == False or y_love == False:
            m 1g "And I have to say, I'm a little surprised..."
            m 1f "You were loyal to her for the most part..."
            mc "I think it's best for the club that I'm not in a relationship with anyone for now."
            mc "Maybe one day that'll change, but for right now, I think it's for the best."
            m "Well hey, I hope you do. She's a good one, [player]."

if encore_sayoriquestion_1 == False:
    pass

play music mend fadein 1.0
m 1e "Well, this is where we depart..."
m 1n "Everyone's going to want to get their final say in before you go, so I won't delay them any longer."
m 1e "But...{w=0.38}I do want to say that I'm extremely grateful for all you've done here.."
m 1p "You've been there for us through our worst and best times..."
m 1m "You...{w=0.38}helped the others start to forgive me, and put me on the path towards learning how to forgive myself..."
m 3e "It's not something most people would do, [player]."
m 2k "You really are one of us!"
m 1j "And I'm glad that you're a member of the Literature Club!"
m 1e "This place really wouldn't be the same without you..."
m 1b "It wouldn't even exist without you!"
m 1e "You're the best member of the club that I've had the privliedge of knowing..."
m 3j "And I wish you the best in all your future endeavors!"
m 1e "Take care, [player]! I hope you've enjoyed your stay with us..."
show monika 1a at t11 zorder 1
"Monika and I share one last smile with each other before she grabs her stuff in disappears into the hallway."
show monika at thide
hide monika
"I feel a tap on my shoulder."
show sayori 1d at t11 zorder 1
"To my surprise, I turn around to see it's Sayori."
"Though she doesn't seem upeset, or even angry at me, but rather at peace."
s 1l "Hey, [player]..."
mc "Sayori. How are you doing?"
s "Well, I'm not sure I really know the right words for any of that..."

if encore_sayoriquestion_1 == True:

    if s_makeup == False:
        if n_love == True or y_love == True:
            mc "I read your letter..."
            show sayori 1g
            mc "And well...{w=0.38}I can't say I blame you..."
            mc "I let you down, at every turn."
            mc "You deserve someone better than me."
            s 1k "Look...{w=0.38}don't beat yourself up over me, [player]."
            s 1d "I'll be okay..."
            s 1l "I just hope you learned something from all this..."
            s 1h "About how to stay true and faithful to your friends and loved ones..."
            s 1k "Especially learning how to stay true to yourself..."
            s 1g "Our relationship may be over, but I just wanted to make sure you don't ever do something like this again."
            show sayori 1d
            mc "I learned, Sayori. Sucks that it had to be the hard way, but you know how hard headed I can be sometimes."
            s 1y "Well, at least that part of you didn't change..."
            s 1d "But, I'm glad you learned not do have this kind of relationship with anyone else ever again..."
            mc "I'm really sorry ruined things..."
            s 1y "Well, maybe one day we can talk about it..."



    if s_makeup == False:
        if n_love == False or y_love == False:
            mc "I don't blame you..."
            mc "I take it you already know of my decision..."
            s 1k "Yeah, I do..."
            s 1g "I'm a little surprised..."
            mc "It's...{w=0.38}for the good of the club."
            show sayori 1k
            mc "Sayori, I still love you and care about you."
            mc "But the entire club nearly got destroyed because everyone loved me..."
            mc "I think us not being together is the best solution going forward. That way there's really no competition..."
            s "I see, and I don't blame you..."
            s "I just wished we had more time to spend together, that's all..."
            mc "I know..."


    if s_makeup == True:
        if n_love == True or y_love == True:
            mc "I know, and I'm sorry..."
            mc "But I think it's in the best interest of the club if I'm not dating any of you guys."
            mc "I don't want to risk what just happened ever happening again down the line..."
            s 1k "I understand..."
            s 1l "We had some up's and down's, didn't we, [player]?"
            mc "Yeah...{w=0.38}well I was mostly the downside to the relationship..."
            s 1y "Well, this was our first relationship. We'll grow and learn from our mistakes..."

    if s_makeup == True:
        if n_love == False or y_love == False:
            mc "I know..."
            s 1l "I'm...{w=0.38}sorry that we have to end things..."
            s 1k "But I think I know why..."
            mc "It's for the best intrest of the club. It's not because I don't love you..."
            show sayori 1g
            mc "I care about you Sayori, I really do. But I think everyone needs the chance to recover from this before there's anymore relationship talk..."
            s 1k "Yeah...{w=0.38}I get it."
            s 1d "I'm really glad we got to spend some time together, [player]..."
            s 1y "You really did make me the happiest I've ever been..."
            s 1k "I just wish I could've experienced it just a little bit longer..."
            mc "Me too..."

if encore_sayoriquestion_1 == False:
    s 1k "Well I always knew it was going to be a long shot for us to ever be a couple..."
    s "The only chance of that was in the 'base game'..."
    mc "It's just...{w=0.38}not meant to be."
    mc "Sayori, you're a great girl and an awesome friend. I know one day you'll find someone who loves and cares for you."
    s "I appreciate it..."



s 1d "I'm still willing to be your friend, [player]."
mc "I'd like that very much..."
s 1y "Good...{w=0.38}I don't know what I'd do if you said no..."
show sayori 1g
mc "I do want you to promise me one thing, okay?"
s 1h "Yeah? What is it?"
show sayori 1k
mc "Get help for your depression, alright?"
mc "You know I hate seeing you like that..."
mc "It's for your own good that you you keep going to therapy."
show sayori 1l
s "Well after this, I think I'll have plenty to talk about with whoever will be my therapist..."
s 1d "But, I'll do it. For you."
mc "Thank you, Sayori."
s 2x "I'll see you around, okay?"
show sayori 1y
mc "You know it, cinnamon bun!"
s "I love it when you call me that..."
s 1q "See you around, [player]!"
s 1x "Thanks for being apart of this club!"
s 1y "It really means a lot to me that you agreed to join..."
mc "I know. That's why I did it."
show sayori 1d
"Sayori and I exchange one last smile before she too heads out and disappears into the hallway."
show sayori at thide
hide sayori
show natsuki 5u at t11 zorder 1
"Natsuki is the next one to approach me."
"At first we both struggle to find the right words to say to each other, given our history, but for once, she's the first to break the ice."
n 5m "I have to say, you do nothing but surprise me..."
n 5q "You go through all that and not choose any of us?"
n 5n "Why?"
mc "It's not your's or anyone's fault, Natsuki. I just need to think about what's good for the club rather than what's good for me for a change."
n 5t "Well...{w=0.38}I guess I can get behind that..."
n 5t "We've had quite the ride, you and me..."
mc "Yeah...{w=0.38}it's really been something..."
n 3m "You know...{w=0.38}for the longest time, I wasn't sure if I could really trust you..."
n 3q "And well, I still ended up falling for you..."
n 1t "I don't really know why...{w=0.38}maybe because I thought you were funny, amazing..."
mc "Charming?"
n 1y "Pfft! Don't push your luck, [player]!"

if poem_giver == "Natsuki":
    n 1u "I really do regret about starting all this drama though..."
    n 1n "I liked you...{w=0.38}a lot...{w=0.38}and I just didn't know how to approach you..."
    n "I never meant to hurt you or anyone."
    mc "I know you didn't, Natsuki."

else:
    pass


n 5m "But what I'm trying to say is:{w=0.38}most boys wouldn't have done what you've done for me."
n 1u "I know we've certainly had our up's and down's, and yeah, things could've gone better..."
n 1n "But I really, really, want to thank you for saving me back there."
n 1q "I'm not sure how any of us are going to get over Monika trying to kill us..."
n 1a "But I think you set enough of an example for us to follow..."
mc "It's the least I could do, Natsuki."
mc "I know there's more to you than you're looks and the tough act you've put up. I'm glad I've gotten to know the real Natsuki."
n 1t "Eh, more or less..."
n 1s "I'm still not sure how I feel about all this being some sort of 'game'..."
n 1t "But...{w=0.38}that means I don't have to worry about my dad anymore..."
mc "That's true. Still, you don't have anything like Monika's powers. What're you gonna do?"
n 1a "I'll figure something out."
n 1y "But I'm not going back there again! That's for sure!"
show natsuki 1z
mc "Glad to hear it, Natsuki!"
n 1t "Yeah..."
n 1m "So I guess I'll see you around?"
show natsuki 1a
mc "Of course! This club wouldn't be as entertaining without you in it!"
n 4l "That's for damn sure!"
n 1z "Bye, [player]!"
show natsuki at thide
hide natsuki
"Natsuki smiles as she heads out into the hallway."
show yuri 1a at t11 zorder 1
"Finally, Yuri is the last one to approach me."
y 1q "It's hard to believe that we're finally at the end of this saga..."
mc "Yeah, I imagine everyone's feeling pretty relieved..."
y "I most certainly am."
y 1t "I know the others already said the same thing, but I really do want to thank everything you've done for us. Especially for me..."
y 1v "I wish our relationship could've gone differently..."

if poem_giver == "Yuri":
    y 1q "I suspect that giving you the letter and my subsquent confession certainly didn't help things..."
    y 1t "You're just...{w=0.38}the first boy that I ever had serious feelings for..."
    y 1q "And with everything...{w=0.38}I just didn't know how to handle that..."
    y 1w "I sincerly regret my actions towards you, and everyone else..."
    y 1v "Even Monika didn't deserve that..."
    mc "You're not a bad person, Yuri. I hoped I helped you see that."

else:
    pass

mc "I'll admit...{w=0.38}I wish we all could've had the club experience without the drama..."
mc "And things could've gone better between us for sure..."
show yuri 1u
mc "But you're a beautiful, gracious and kind person, Yuri. You'll find someone worth your time. I believe in you."
y "Thank you. Coming from you, it means a lot..."
y 1b "I think we both learned a lot from this experience, wouldn't you agree?"
show yuri 1a
mc "For sure! I just hope going forward we'll be stronger as club together..."
y 1u "Yeah..."
mc "So...{w=0.38}what're you going to do about...{w=0.38}you know..."
y 3v "I think it's finally time that I start confronting this problem rather tha supressing it..."
y 1w "I'm not sure what the best way is, if everything is just a simulation now."
y 1h "Is there a way I can simply just undo my problem with the click of a button?"
mc "I can't say that I have the answer to that question. But, I know you'll figure something out. I'll be right here if you need my help."
y 1a "I'd very much appreciate that, [player]..."
y 1q "I really owe you a lot, don't I?"
mc "I just did what I thought was right back there. You and everyone else are so much more than some 'code'."
y "Well, we'll have much to ponder about the supposed truth of our reality..."
y 1d "But I must admit...{w=0.38}this whole experience has inspired me to write my own story about this!"
show yuri 1c
mc "It better be a best-seller!"
y 1q "I haven't written a full novel before...{w=0.38}but I'm sure I can figure it out."
y 1b "But...{w=0.38}perhaps one challenge at a time, right?"
show yuri 1c
mc "Yeah, I think we've earned some well deserved rest!"
y 1d "And rest we shall!"
y 1a "Farewell, [player]! And thank you for everything!"
show yuri 1d
"Yuri says sweetly as she heads out the door."
show yuri at thide
hide yuri
stop music fadeout 2.0
"I sink back in a chair as Yuri leaves the clubroom, taking in the newfound silence."
"It's finally over..."
"All the tears..."
"All the name calling..."
"All the temper trantrums..."
"It's finally over..."
"I glance at my watch and notice that it's far past the normal time I'd be heading back home."
"Well, even if this world isn't real, it'd feel weird hanging around in here..."
"I pick up my stuff and begin heading out the door, but not before taking one last look at the clubroom."
"This really is no ordinary Literature Club..."
"But..."
"I don't think I'd have it any other way."
"I turn on my heel and head out the door to start the walk home."
scene black
with dissolve_scene_full
$ renpy.pause(delay=10.0)
scene bg residential_day
with open_eyes
"I take a seat down on my the steps to my house and lay my backpack right next to me."
"Looking up at the sky, I can see the a tint of orange forming in the vast blue sea that flies high above me."
"Even if it's not real, I always did enjoy it..."
"It always did instil a sense of calm and peace whenver I was troubled, and after today, those are two things I most surely need."
"Though going forward, for better or worse, things aren't going to be the same."
"Monika has a lot of work to earn everyone's trust back, but I'll do what I can to ensure she fairly earns it..."
"After all, who knows how much time Monika has really bought us?"
"How are we going to 'cross over' to this world to join the person who I'm supposed to represent?"
"Am I even real?"
"..."
"No matter..."
"Whatever challenges that await the Literature Club, I'll be right there facing there with them to face it down..."
"Because I know one thing for sure..."
"I care about them, with all my heart..."
"And I know the player does too."
"Thank you, whoever you are."
"You'll always be welcome in the Literature Club..."
scene black
with dissolve_scene_full
$ renpy.pause(delay=5.0)
call encore_credits
