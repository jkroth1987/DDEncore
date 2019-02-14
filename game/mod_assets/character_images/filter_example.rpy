# NOTE: These two lines should probably be in your definitions file instead of here.
# Including them here just so that this scene works out of the box if you want to see it!
image bg club_day sepia = sepia("bg/club.png")
image bg residential_day sunset = sunset("bg/residential.png")

label filter_example:
    scene bg residential_day
    show sayori s111111 at i21
    show yuri h111143 at i22
    with wipeleft
    
    pause 0.5
    play music t8
    pause 1.0
    show sayori s112111 at f21
    s "Okay, Yuri! What did you want to talk about?"
    s s225111 "Is... something bothering you?"
    
    show sayori s115111 at t21
    show yuri h124171 at f22
    y "No, no... That is, it's not bothering {i}me{/i} exactly."
    y h114131 "Sayori... {w=0.4} I'd like to understand your depression issues a little better."
    show yuri h11h135 at t22
    show sayori s227231 at hf21
    s "Guh...! Uh...!"
    s s112222 "You, uh... Ahaha... You don't need to worry about that!"
    s s112212 "It's under control, Yuri. Really it is."
    show sayori s111112 at t21
    show yuri h124171 at f22
    y "Be that as it may, I feel responsible as your friend for having at least a basic understanding of what I should and shouldn't do."
    y h115144 "I read online last night that people with depression feel much deeper cuts from harsh words than others..."
    show yuri h113131 at t22
    show sayori s112123 at f21
    s "Ha ha... {w=0.4} 'Read online.'{w=0.4} That's cute."
    s s115111 "Yuri, I get that you're being considerate, but depression isn't just a checklist of things wrong with someone."
    s s115122 "It's different for everyone. Some people just need love, others need medicine..."
    show sayori at t21
    show yuri h114131 at f22
    y "Medication."
    show yuri h113131 at t22
    show sayori s115111 at f21
    s "Huh?"
    show sayori at t21
    show yuri h224131 at f22
    y "Medicine refers to remedies for short term conditions. A regularly taken drug for long term uses would be medication."
    show yuri h113131 at t22
    show sayori s112122 at f21
    s "Oh, so {i}that's{/i} what the difference is..."
    show sayori s111112 at t21
    show yuri h124172 at f22
    y "Still, even if blanket advice is not the most effective, I understand that particular sentiment and want to adjust accordingly."
    y h114143 "I know I've said my share of harsh things to others, yourself included. 'Retribution' and all that..."
    show yuri h11h115 at t22
    show sayori s113111 at f21
    s "It's okay, Yuri. That kind of thing sucks to hear, but it passes."
    s s122111 "And people have said way meaner things to me! I'm not mad at you for anything!"
    show sayori s111111 at t21
    show yuri h224131 at f22
    y "Really? May I ask what sort of harsh things you've been made to suffer?"
    show yuri h223131 at t22
    show sayori s115222 at f21
    $ song_resume = get_pos() + 2.0
    stop music fadeout 2.0
    s "Uh... Well..."
    
    # FLASHBACK BEGINS HERE!
    # The background and each character sprite are marked with the sepia filter
    window hide
    scene bg club_day sepia
    show sayori u115113 sepia at i21
    show monika u113113 sepia at i22
    with dissolve
    
    pause 1.5
    
    show monika u117113 sepia at f22
    m "From now on when it comes to [player],{w=0.75} I want you to listen to your feelings."
    m u214113 sepia "Do whatever they tell you. Even if it doesn't seem right or you think it will make you sad, just trust your feelings."
    m u124123 sepia "If you can do that, I'm pretty sure it will turn out the best for everyone."
    show monika u123123 sepia at t22
    show sayori u113113 sepia at f21
    s "Just listen to my feelings..."
    s u113112 sepia "Are you sure about that?"
    show sayori u115113 sepia at t21
    show monika u123122 sepia at f22
    m "......."
    m u114122 sepia "Pretty sure..."
    m u114143 sepia "... Yeah, I'm sure."
    
    window hide
    show sayori u115122 sepia
    show monika u113143 sepia at rhide
    hide monika
    
    pause 1.5
    
    # END OF FLASHBACK
    
    $ audio.temp = "<from " + str(song_resume) + " loop 9.938>bgm/8.ogg"
    
    scene bg residential_day
    show sayori s11c222 at i21
    show yuri h223131 at i22
    with dissolve
    
    pause 1.5
    play music temp fadein 2.0
    show sayori at f21
    s "... Don't worry about it, Yuri."
    s s115122 "It's... in the past."
    s s113111 "I try not to hold grudges against people for things they've said or done to me before. Especially if they didn't mean it."
    s s122111 "Besides, I think people can change if you give them a second chance."
    show sayori s111111 at t21
    show yuri h112172 at f22
    y "Well, it's good to hear you're thinking that way, Sayori."
    
    # SUNSET BEGINS
    # Each background and sprite from this point forward has the sunset filter.
    
    show bg residential_day sunset
    show sayori s111111 sunset
    show yuri h112131 sunset
    with dissolve
    
    y "But don't be afraid to come to me if you need someone to talk to, all right?"
    show yuri h111131 sunset at t22
    show sayori s112111 sunset at f21
    s "Thanks, Yuri."
    s s112121 sunset "It looks like the sun is starting to go down. We should probably head home."
    show sayori s111111 sunset at t21
    show yuri h112172 sunset at f22
    y "I suppose..."
    show sayori s114111 sunset
    y h224131 sunset "Although..."
    y h222131 sunset "I would still like to talk more, so... Why don't we find a place to sit and watch the sunset together?"
    y h112144 sunset "You can tell me more about what I {i}should{/i} be looking for to read online."
    y h112131 sunset "Whatever might help you."
    show yuri h111131 sunset at t22
    show sayori s114121 sunset at f21
    s "Umm..."
    s s112111 sunset "Yeah... Yeah, I'd like that."
    s s113111 sunset "And, Yuri?"
    show sayori s11a111 sunset at t21
    show yuri h112131 sunset at f22
    y "Yes, Sayori?"
    show yuri h111131 sunset at t22
    show sayori s112112 sunset at f21
    s "Thank you for this.{w=0.4} It...{w=0.4} means a lot to me."
    show sayori s111112 sunset at t21
    show yuri h222171 sunset at f22
    y "It's my pleasure, Sayori. I will be there for you as long as you need me."
    show yuri h111131 sunset at t22
    show sayori s222111 sunset at f21
    s "Come on! We should get to the highest hill for the best view of the sunset!"
    show sayori s111141 sunset at lhide
    hide sayori
    
    show yuri h222161 sunset at f22
    y "Right behind you!"
    show yuri h221161 sunset at lhide
    hide yuri
    
    window hide
    pause 1.0
    
    return