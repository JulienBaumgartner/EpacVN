# Sc 01 - 07
# Before exploration
#test
#Sc 01
label brochure:
    stop music
    scene bg brochure
    "Sc 01, tourist advert brochure"

    #Test for poses, to delete later
    show sharon normal at right with moveinright
    "sharon normal.png"
    show sharon angry
    "sharon angry.png"
    show sharon surprised
    "sharon surprised.png"
    hide sharon with moveoutright

    show derek normal at right with moveinright
    "derek normal.png"
    show derek angry
    "derek angry.png"
    show derek happy
    "derek happy.png"
    show derek scared
    "derek scared.png"
    hide derek with moveoutright

    show hans normal at right with moveinright
    "hans normal.png"
    show hans angry
    "hans angry.png"
    show hans curious
    "hans curious.png"
    hide hans with moveoutright

    show kvin normal at right with moveinright
    "kvin normal.png"
    show kvin angry
    "kvin angry.png"
    show kvin happy
    "kvin happy.png"
    show kvin scared
    "kvin scared.png"
    hide kvin with moveoutright

    show lin normal at right with moveinright
    "lin normal.png"
    show lin angry
    "lin angry.png"
    show lin surprised
    "lin surprised.png"
    hide lin with moveoutright

    show neonila normal at right with moveinright
    "neonila normal.png"
    show neonila angry
    "neonila angry.png"
    show neonila surprised
    "neonila surprised.png"
    hide neonila with moveoutright


    show kais normal at topcenter with moveintop
    "kais normal.png"
    show kais crazy
    "kais crazy.png"
    show kais deactivated
    "kais deactivated.png"
    show kais happy
    "kais happy.png"
    show kais sad
    "kais sad.png"
    show kais shocked
    "kais shocked.png"
    hide kais with moveouttop

    show kais_storage normal at topcenter with moveintop
    "kais_storage normal.png"
    show kais_storage angry
    "kais_storage angry.png"
    show kais_storage deactivated
    "kais_storage deactivated.png"
    hide kais_storage with moveouttop

    jump sitting

#Sc 02-------------------------------------------------------------------------------------------------------------------------------------
label sitting:

    show hans normal at left with moveinleft

    hans "It can’t get any worse than this! “take some well-deserved holidays” as he says! “open yourself to the world” as he says! “Not everything is about the reptilians or the Illuminati” as he says!"
    hans "But what my therapist forgot to tell me is this winning lottery ticket he gave me would bring me right into the wolf’s mouth!"
    hans "A train full of robots, some other tourists that are more sheep than human, and not a single sane person in view! This is a nightmare. And I'm going to wake up in a reptilian laboratory!"

    hide hans with moveoutleft
    show lin normal at left with moveinleft

    lin "Oh wow, would you believe that! I’m so lucky to have won this travel!"
    lin "This lottery did look like a scam at first, but I sure am happy to have brought my photography equipment with me! I only could take half of usual, but I should be fine with it."
    lin "I just hope the others won’t bother me too much... I don’t want to waste any storage on my cameras, I've barely got what I need."
    lin "Here comes my full day of taking pictures around Switzerland, and... taking more pictures!"

    hide lin with moveoutleft
    show neonila normal at left with moveinleft

    neonila "Hello again Slowstagram! Looks like I need to thank again the fan who gave me this winning lottery ticket! We’re going to have so much fun together! So don’t forget to like, subscribe and buy my goodies “I <3 Switzerland edition”!"
    neonila "I even updated my K-9 unit with a “far from civilization” program, so he can make directly some spacebucks by himself!"
    neonila "But before I get to my seat, let’s take some selfies, also make sure to link you credit card as those are pay-per-view."

    hide neonila with moveoutleft
    show sharon normal at left with moveinleft:
        xzoom -1
        yalign 1.0

    sharon "What in the Lord’s name have I done to deserve this? I swear, sometimes I would think my son tries to kill me."
    sharon "My own blood, betraying me like so! I have so much to do back home, an empire to rule, money to gain, investor to manipulate, my husband’s possession to claim, and yet-"

    show kvin normal at right with moveinright

    kvin "Hey Granny! I told you I wanted a Bluebull before, but you didn’t want it and now I'm thirsty! And I know we have water but bweeh who would drink this?? It’s so tasteless!"
    kvin "And oh, this travel is going to be awesome! And there’s gonna be robots everywhere, and, and"

    sharon "OH LORD ALMIGHTY! Could you please pipe down for a second? Remembering how my own son forced me to go to this foolish travel with you and my half effective of a husband already employs my whole cogitation process!"
    sharon "Dear, please, could you for once do what you’re supposed to and wake up out of your little soldier fantasy to take care of our insufferable grandson? "

    hide kvin with moveoutright
    show derek normal at right with moveinright

    derek "You heard the Commander, private Kevin. Now stop running around, you’re an easy target for snipers, how many damn times do I need to tell you that!"
    derek "It’s already hard enough to secure an unknown area without a recruit like you ignoring orders! Now come back here or you’ll do me five!"

    sharon "Oh my, doesn’t he look ridiculous like this? At least he’s much easier to manipulate this way... Anyway, let’s get seated and hope the day passes on fast."

    derek "Oh uh... Sweetie what was I doing just now? I feel like I just..."
    show derek:
        xzoom -1
        yalign 1.0
    derek "Wait ROBOTS? THE WAR’S NEVER OVER! AARRGH!!"

    hide derek with moveoutright

    sharon "And here we go again... Holy, this is going to be take a while before home."

    scene bg_parade_car with dissolve :
        zoom 0.5

    play music "/audio/train_01.mp3" fadein 1.0

    show servicerobot_karen normal at center with moveinleft:

    service1 "hello"
    service1 "texte intro bienvenue"

    hide servicerobot_karen with moveoutleft

    show kvin normal at right with moveinright


    kvin "Wooow! Me first me first!"
    show charles normal :
            yalign 0.5
            xalign 0.5

    play sound "/audio/smalldogbark.mp3"

    kvin " Hey wow, is that a k-9 doggobot? Oh it almost weighs nothing! … Uh, is that coffee pouring down from him?"



    show neonila normal at left with moveinleft

    neonila "Look at this, chat, humanity’s worst creation that’s still strangely allowed outside at the same time as everyone: a child!"
    neonila "Let’s start a vote among my best subscriber, and I'll do whatever the winner wants! It’s best of course if it involves kicking him."

    kvin "Wow missy, that’s not very nice... uh, do you even know I'm here?"

    neonila "Haha, yeah I know the best thing with kids is nine months before they are born. But hey mistakes happen, I'm not judging. Or maybe I am."
    neonila "Well whatever thank you SimpLordxx for this joke, I'll promote you to “Lady’s Knight xoxo” since it was so funny."

    kvin "ooookeeey... weird girl... well let’s get somewhere el- OH HOW MANY CAMERAS DOES THIS GUY HAVE??"

    hide neonila with moveoutleft
    hide charles with moveoutleft
    show lin normal at left with moveinleft


    lin "DON’T EVEN DARE COMING NEAR ME YOU LITTLE -"

    hide kvin
    hide lin
    show hans normal at left:
        xzoom -1
        yalign 1.0
    with dissolve

    hans "Cmon man it’s not that hard... just one wrong move and you’re reptilian’s lunch... no pressure... my body is a temple... GODAMMIT HOW COULD I CALM DOWN IN THIS KIND OF SITUATION??"

    show derek normal at right with moveinright

    derek "Yeah soldier, I get how you feel..."

    hans "WHO ARE- wait, you do?"

    derek "Y’know, I spent my whole life fighting them... what’s left of my scarred life is a battlefield, an eternity in the middle of a minefield... the only life I can save is my own, surrounded by opponents that only want me dead. Name’s Derek by the way."

    hans "Wow, it sure feels like you’ve been fighting them for some times alright...I’m Hans, pleased to meet you. I wouldn’t have guessed someone like you was hiding in this mindless group. Maybe we do have a chance after all?"

    derek "No chance’s enough against them. But a battlefield brother might help? How about we bring our weapon together and -"

    show sharon normal at outRight with None
    show derek at center:
        xzoom -1
        yalign 1.0
    show sharon normal:
        xalign 0.95
        yalign 1.0
    with move

    sharon "Sorry to interrupt your worthless and pathetic conversation, {b}dear{/b} husband, but may I remind you that you are carrying my makeup station, and it’s already been 30 minutes?"
    sharon "Do you maybe think my body can simply generate mascara out of nothing? Or will you be handing me what I need to stay the beauty I am?"
    sharon "Oh... I didn’t see you were talking to such a handsome young man... Please excuse my husband’s clumsiness, he might’ve... hit his head in a war, if i dare say so."
    sharon "Now if you’ll excuse me, I need to... water the good-looking flower that I am."

    hide sharon with moveoutright

    hans "{i}Ok now that feels like danger… note to myself: don’t get anywhere near this overseer of a reptilien. No way she isn’t one of some kind.{/i}"
    derek "{i}Damn, why’s the commander so tense right when i find a new recruit to help our cause against those crazy robots?{/i}"
    derek "{i}Well, can’t be bad to be too cautious i guess{/i}"

    hide derek
    hide hans
    show lin normal at left
    with dissolve

    lin "Equipement set, seat reserved, snacks out… Everything ready to be the perfect travel!"

    show kvin normal at right with moveinright

    lin "IF THERE WASN’T AN ANNOYING KID BY MY SIDE!"
    lin "Leave me be kiddo, or you’ll break something!"

    kvin "No way, i just wanna see! Pleasepleasepleaseplease"

    lin "OK FINE! You win! But promise me to be careful, okay? It costs a lot!"

    kvin "Yeeaaah! Let me see let me see!"

    lin "Hey, not there that’s where my t.."
    with vpunch

    " CRACK-"



    kvin "What? But i didn’t even-"

    lin "Ok kid, now that went too far! I hope your parents can pay for it or else i’m calling -"

    kvin "Uuuh sorry to stop you but i think it’s actually the seat that broke?"

    lin "Yeah don’t try to- oh… you’re right…. Wait something was stuck below the cover? Hmm"

    jump findKey

#Sc 02.3-------------------------------------------------------------------------------------------------------------------------------------
label findKey:
    scene bg_parade_car :
        xalign 0.0 yalign 0.5
    show lin normal at left
    show kvin normal at right
    with dissolve

    lin "We should call a waiter to tell them what happe- hey are you even listening to what i say?"

    show cardchip with moveinright:
            yalign 0.6
            xalign 0.5

    kvin "I got it out! Looks like… an old card? Uh, booooring."

    lin "Give me this now!… This is an old employee card? It seems really old, and looks like an access card, there’s a chip at the end."

    kvin "An access card? So that means we could like… EXPLORE the whole train? Go see all those robots everywhere?"
    kvin "{i}Wait… he’s not planning on giving it back, right?{/i}"

    menu:
        "Take the card":
            $ hasAiKey = True

            show kvin happy
            kvin "No way I’m gonna pass up on this! Card’s mine! Hehe!"

            show kvin:
                xzoom -1
                yalign 1.0
            hide kvin with moveoutright

            lin "Wha- Come back with this you -! … Oh well, it’s his family’s problem now. And now he’s gone at last! I’m not going to complain on that!"

        "Give back the card":
            $ hasAiKey = False
            lin "I can see what you want to do with it just by looking at your eyes… But I won’t let you! I’m calling a waitress, just be happy that seat was already damaged, i won’t tell on you!"

            hide kvin with moveoutright

            show servicerobot_karen normal at right with moveinright

            service1 "hi thank you"

            hide cardchip

            hide servicerobot_karen with moveoutright

            show kvin normal at right with moveinright

            kvin "Oooh cmon you’re not fun… but where were we? Oh yeah i gotta take a look at those cameras!"

            lin "Oh god no it’s true that i promised him… "

    stop music fadeout 1.0

    jump departure

#Sc 03-------------------------------------------------------------------------------------------------------------------------------------
label departure:
    scene bg_parade_car_turned_seats:
        zoom 0.5
    play sound "/audio/door_closing.mp3"
    play music "/audio/train_roule.mp3" fadein 0.5
    "Sc 03, Departure"

    show neonila surprised at center with moveinright
    neonila "Wow just look at this scenery, I can’t even feel the train moving!"
    show neonila normal
    neonila "Of course, you’d feel it better if I had the last generation streaming camera, but for that I’ll need your help!"
    neonila "Remember, I only take 95\% of your donation for my daily expenses, so EVERYTHING ELSE goes straight to my material budget, just for your comfort! Crazy, right?!"
    neonila "Alright, I see we have a menu for drinks here, let’s make a vote on what I should order! "
    hide neonila with moveoutright

    show hans normal with moveinleft
    hans "This country is impressive though…there must be something going on, seeing at how clean the mountains are even after the war…"
    show hans angry
    hans "But wait! That girl…she’s russian I think? Did she just...order a drink? Is she crazy?? Who knows where that drink comes from, or if it’s gonna be poisoned or drugged?"
    hans "But wait a minute…who is she speaking to all the time? Maybe she’s…just recording everything? To whoever is in control of this train?"
    show hans curious
    hans "And that guy with the cameras… He’s the eyes! This whole plan has been thoroughly thought through! I’m right where they wanted me to be!"
    show hans normal
    hans "No, no…stay calm...breath…everything’s gonna be ok…also take your medication. "
    hans "If I ever get out of here alive, I promise I'll go see my mom one last time, and never go out of the house again."
    hide hans with moveoutleft

    jump parade

#Sc 04-------------------------------------------------------------------------------------------------------------------------------------
image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)
label parade:

    play music "audio/katy_edit_loop.mp3" fadein 2.0

    show derek scared at left with moveinleft:
        xzoom-1
        yalign 1.0
    derek "Hm? What’s that noise approaching us?"


    show servicerobot_karen normal  at right  with moveinbottom:

    service1 "We hope everyone is having a great time on this tour through Switzerland!"
    service1 "Edelweiss Corporation offers you this completely historically accurate traditional parade that was celebrated everywhere in this country no later than 40 years before our time!"
    service1 "Trust us, we know what we’re talking about!"
    service1 "Now, time to stop the talking and start the fun!"
    hide servicerobot_karen with moveoutbottom


    #scene bg_parade_car_confetti:
        #zoom 0.5
    #$ renpy.movie_cutscene("video/confettis01.webm")
    play movie "video/confettis01.webm" loop
    show movie behind derek
    derek "WE’RE UNDER ATTACK! EVERYONE, GET DO-"

    show sharon normal at right with moveinright
    sharon " NO! No no no! It’s just a nice parade! You won’t ruin the only thing that looks interesting on this trip! Now you will sit down and let me enjoy it!   "

    show derek normal at left
    derek " Oh…I…I’ll just keep an eye on it I guess…"
    hide derek with moveoutleft
    hide sharon with moveoutright

    show nr_cara_guggen:
        zoom 0.1
        xalign 0.5
        yalign 0.3
        easein 10.0 xalign 0.5 zoom 0.3
    pause

    hide nr_cara_guggen with moveoutbottom

    show kvin happy at right with moveinright
    kvin " Waah that’s totally wicked! There’s robots everywhere! And costumes! And confettis! And and…oh, I gotta get closer!"
    hide kvin with moveoutright




    show carnabot:
        zoom 0.2
        xalign 0.5
        yalign 0.4
        easein 5.0 xalign 0.5 zoom 0.5
    pause
    hide carnabot with moveoutbottom

    show lin surprised at left with moveinleft:
        xzoom -1
        yalign 1.0
    lin " Wait what? No, my cameras aren’t set up for that yet! Too fast! Could you start over please?"
    hide lin with moveoutleft

    show nr_cara_guggen:
        zoom 0.1
        xalign 0.5
        yalign 0.3
        easein 10.0 xalign 0.5 zoom 0.3
    pause

    show neonila surprised at right with moveinright
    neonila "Hey chat look at this! Wait, this is premium content, I’m turning off the camera for everyone who isn’t subbed!"
    neonila "Now I hope you’ll enjoy it while I take a sip of my much earned drink! Seriously, I should get paid more for the quality I bring you."

    show hans angry at left with moveinleft:
        xzoom -1
        yalign 1.0
    hans  "Ok…I’ll admit they look cool…they’re slowly invading the place and blocking the exit, but they do look cool…just stay calm and rush to the exit if anything were to happen… "
    hans "Let’s move slowly to the back, where I won't actually be safer, but will at least feel like I am."
    hide hans with moveoutleft

    hide hans
    hide neonila

    hide movie
    stop movie
    stop music fadeout 1.0

    jump bar

#Sc 05-------------------------------------------------------------------------------------------------------------------------------------
label bar:
    play music "/audio/bar_01.mp3"
    scene bg_bar:
        zoom 0.5

    show kais normal at topcenter with moveinright


    goodbrother "Oh hello my good sir!"
    goodbrother "Could I interest you in some traditional delicacies?"
    goodbrother "Or maybe you’re hungry for more, in which case I can get you a delicious swiss meal... "
    goodbrother "...fresh from the kitchen!"

    show hans angry at right with moveinright
    hans "GET BACK! I’M FLUENT IN OVER 6 MILLION FORMS OF KICKING YOUR ASS!"
    goodbrother "Herm… Sir? I’m not sure if I am programmed to deal with this kind of situation…"
    hans "DID YOU NOT HEAR ME? GET B- Oh wait. You… can’t actually move away from there, can you?"
    show kais sad
    goodbrother " I’m sorry Sir, but what you’re saying is quite offensive towards me…"
    hans "Oh uh I’m…sorry I guess? So…what were you saying before this…embarrassing moment? "
    hans "{i}to himself: Since when are those waiter bots so…emotional?{/i}"
    goodbrother "Well since my code forces me to stay nice to you no matter the situation, I’ll repeat what I just said! No worries it is my job after all.  "
    show kais normal  at topcenter
    kais "My name is KAIS, your bartender on this incredible tour!"
    kais "Now to make sure you understand this time:..."
    show kais happy
    kais "“Oh hello my good sir! "
    kais "Could I interest you in some traditional delicacies? "
    kais " Or maybe you’re hungry for more, in which case I can get you a delicious swiss meal..."
    kais "... fresh from the kitchen!"
    show hans curious
    hans "{i}Oh my god, can I even refuse now?"
    hans "{i}It could be poisoned, but can I really anger him by saying no?"
    hans "{i}I would be suspicious if I didn’t accept it!"
    hans "{i}Well…I hope all these years building poison immunity are going to pay off!{/i}"
    show hans normal
    hans "So… I’m going to take uuh… an “Assiette Valaisanne” If that’s ok with you?"
    show kais normal
    kais "Coming right up, my good sir! "

    show kais happy
    kais " Here it is, the best of what we can offer!"
    kais "I hope you have a great meal, good sir, and if you’re thirsty you’ll notice a Fendant fountain on your right, feel free to take a glass!"
    show hans curious
    hans "Wait a fountain? Are you not supposed to be a waiter?"
    show kais sad
    kais "…It would seem that my creator forgot that I can’t move around,and put the glass too low for me to reach."
    kais " Please do forgive me, kind sir, as my little problem seems to cause trouble for BOTH of us…"
    hans "Ok I got it, I’ll just shut up and enjoy my food. "
    hans "How does the situation look like in the rest of the train though? "

    stop music fadeout 1.0
    scene bg_parade_car_turned_seats:
        zoom 0.5
    play music "audio/katy_edit_loop.mp3" fadein 2.0

    show kvin normal at left with moveinleft:
        xzoom -1
        yalign 1.0
    kvin "Wooohoo! Look, they’ve got a confetti bag under their cape!"
    show sharon normal with moveinright:
        xalign 0.5
        yalign 1.0
    sharon "Kevin get back here this instant! Please ,darling, be useful for once and say something!"
    show derek normal at right with moveinright
    derek " Sorry, too busy studying the enemy's position."
    hide kvin with moveoutleft
    hide sharon with moveoutright
    hide derek with moveoutright


    play movie "video/confettis01.webm" loop
    show movie behind neonila
    show neonila normal at left with moveinright
    neonila "*Sip* I sure hope you’re enjoying the view, and more so that you’re going to vote for me as the best streamer of the month!"


    show hans normal at right with moveinright
    hans "Yup, complete chaos."
    hide hans with moveoutright
    hide neonila
    stop music fadeout 1.0
    hide movie
    stop movie


    scene bg_bar:
        zoom 0.5
    play music "/audio/bar_01.mp3"



    show hans normal at right with moveinright
    hans "Oh well, let’s taste this meal that’s in front of me… "
    hans "Hey, this is actually pretty good!  "
    hans "I didn’t expect something so simple to taste this good. And no poison either, the day’s going better."
    hans "Wait! ...There’s something hard in the food!"
    hans "Is…is it a pill?"
    hans " I can’t let him see me spit it out!"
    hans "Ok…easy there...turn around and-"

# sc 5.03 find ring------------------------------------------------------------------
    show ring  with moveintop :
        yalign 0.2
        xalign 0.5

    show hans angry
    hans "Wait no this is...a ring? "
    hans "What’s it doing in there?"
    hans "It looks dirty and…THIS was in my food?"
    hans "Is it a warning?"
    hans "I…I can’t act recklessly! Now I just hope nothing too bad happens…"

    stop music fadeout 1.0
    hide bar_01 with fade
#-----------------------------------------------------------------------------------
    play movie "video/confettis01.webm" loop
    show movie behind derek with fade
    play music "audio/katy_edit_loop.mp3"

    show nr_cara_guggen:
        zoom 0.1
        xalign 0.5
        yalign 0.3
        easein 4.0 xalign 0.5 zoom 0.3
    pause

    show kvin happy at left with moveinleft

    kvin "Waahaa! How did they stuff so much…stuff on these robots! Look grandma, they can do anything!"

    show kvin happy behind nr_cara_guggen:
        xalign 0.5
    with move
    hide kvin

    show sharon normal at right with moveinright
    sharon "Yeah, I’m sure they can, and now get back here before you break something!"

    sharon "Dear, could you look out for our grandson, and,"
    sharon " I don’t know,"
    sharon "put him on a leash or something before he ruins our already terrible vacation by breaking a robotic employee?"

    show derek normal at left with moveinleft:
        xzoom -1
        yalign 1.0

    derek "The…the robot got him and…his legs…we couldn’t find his legs!!"
    sharon "Oh gosh, he seems pretty deep in his delirium this time."
    kvin "No look for real! I swear I could just reach their-"

    hide derek with moveoutleft
    hide sharon with moveoutright
    hide movie
    stop movie



#Sc 06-------------------------------------------------------------------------------------------------------------------------------------
label bug:
    play music "/audio/alerte01.mp3"

    show animation_alerte:
    #scene in animation:
        zoom 0.5
    with vpunch
    show nr_cara_guggen_crazy:
        yalign 0.5 xalign 0.5 zoom 0.6


    show sharon angry at right with moveinright
    sharon "....KEVIN!"
    show kvin scared at left with moveinleft
    kvin "Wha-? But I-"
    hide sharon with moveoutright
    hide kvin with moveoutleft

    show animation_alerte:
    #scene in animation:
        zoom 0.5
    with vpunch


    show lin surprised at right with moveinright
    lin "What’s going on? I can’t take picture in these conditions! "
    show neonila surprised at left with moveinleft
    neonila " He-hey, what’s happening? Chat what’s going on?"
    neonila " …Chat??"
    neonila "Oh god I can’t reach it! "
    neonila "WHATAMIGONNADOICANTDOANYTHINGWITHOUTMYCHAT!"

    hide neonila with moveoutleft
    hide lin with moveoutright

    show animation_alerte:
        #scene in animation:
        zoom 0.5
    with vpunch

    show derek angry at left:
        xzoom -1
        yalign 1.0
    derek "so…it begins again…come at me you damn human shaped cans! I’m not scared!"

    hide derek

    hide nr_cara_guggen_crazy with moveoutbottom

    hide hans
    show hans angry with moveinright
    hans "hey…they’ve stopped working. All the robots are down."
    hans "Something’s coming for me. I know it…"
    hide hans with moveoutright

    show animation_alerte:
            #scene in animation:
        zoom 0.5
    with vpunch

    show kvin scared at left with moveinleft
    kvin "uuh… I didn’t touch anything tho?"


    show sharon angry at right with moveinright

    sharon "Sure young imbecile, and i guess those robots just fell down on their own!"

    hide hans


<<<<<<< HEAD

    kvin " No but for real this time "
    show servicerobot_karen normal at center with moveinbottom
    kvin " - hey look he’s getting up! See? Nothing bad happened!"
    hide kvin with moveoutleft
    show hans curious at left with moveinleft:
        xzoom -1
        yalign 1.0
=======
    kvin " No but for real this time, - hey look he’s getting up! See? Nothing bad happened!"
    hide kvin with moveoutleft
    show hans curious at left with moveinleft
>>>>>>> 2b17eca2c1aa1ae6f17e792d3c7071c41d55c2c7
    hans "one of them did get back up but… are you sure it’s not something bad happening? "
    sharon "He’s right that robot doesn’t look good"
    hide hans with moveoutleft
    show derek scared at left with moveinleft:
        xzoom -1
        yalign 1.0

    derek "Here it comes"
    sharon "Stop saying things like these you’ll actually start scaring me!"

#Sc 07-------------------------------------------------------------------------------------------------------------------------------------
label crazybot:

    service1 "..."

<<<<<<< HEAD
    #hide derek
    show kvin angry at left with moveinleft:
        xalign 0.4
        zoom 0.8
        xzoom -1

=======
    hide derek with moveoutleft
    show kvin scared at left with moveinleft
>>>>>>> 2b17eca2c1aa1ae6f17e792d3c7071c41d55c2c7
    kvin "uuh.. Hello? Someone in there?"
    service1 "..."

    hide sharon with moveoutright

    show neonila angry at right with moveinright
    neonila "OMG i can’t reach internet! "
    neonila "Where’s my money going to come from if i can’t stream my day? "
    hide neonila with moveouttop
    show charles surprised with moveinbottom:
        xalign 0.85
        yalign 0.5

    neonila "Even my K-9 unit antenna can’t connect!"
    neonila "Hey stupid robot how about you do something about it! "

    service1 "..."

    show charles angry

    show servicerobot_karen with move:
        xalign 0.6
    neonila "h- hey… what are you…?"

    service1 "{b}Tentative to communicate to an unknown receptor in a quarantine situation detected{/b}"

    neonila "M- my k9! Where are you taking him!"

    service1 "{b}Removal of the threat in progress{/b}"

<<<<<<< HEAD

    show derek scared at left :
=======
    hide kvin with moveoutleft
    show derek scared at left with moveinleft:
>>>>>>> 2b17eca2c1aa1ae6f17e792d3c7071c41d55c2c7
            xzoom -1
            yalign 1.0
    derek "GET DOWN!"
    hide kvin with moveoutbottom
    hide derek with moveoutbottom

    show servicerobot_karen broken :
        zoom 0.5
    play sound "/audio/crash_dog.mp3"
    show charles broken with vpunch:
        xalign 1.0
        yalign 0.5


    "CRACK"
    hide charles with moveoutbottom

    show neonila surprised at right with moveintop

    show servicerobot_karen broken with move:
        xalign 0.6


    neonila "Haaa!"


    show hans angry at left with moveinleft:
        xzoom -1
        yalign 1.0

    hans "Get away from him!"
    hans "He’s become completely crazy!"
    hide hans with moveoutleft

    show lin surprised at left with moveinleft
    lin "What’s this bot doing!"
    lin " Without the old man’s intervention that throw would have killed her!"

    show servicerobot_karen broken with move:
        xalign 0.7
        zoom 0.5


    service1 "{b}Another communication threat has been detected. Removal engaged{/b}"

    neonila "Hey let me go!"
    hide lin  with moveoutleft
    show derek angry at left with moveinleft:
        xzoom -1
        yalign 1.0
    derek "Why don’t I have my gun right when something like this happens! "
    show derek angry with move :
        xalign 0.5
    show derek angry with move :
        xalign 0.2

    derek "Take this you damn can!"

    neonila "H-Help! He’s going to kill me!"

    show servicerobot_karen broken with move:
        xalign 0.8
        zoom 0.5

    service1 "{b}Removal of the threat in progress"
    service1 "{b}TING! The virus database has been uptateeeed* bzzp{/b}"with vpunch

    neonila "Wait… what? He let his grip go!"
    hide servicerobot_karen with moveoutbottom

    hide derek with moveoutleft

    show kvin happy at left with moveinleft
    kvin "Hello there! Missed me?"

    hide neonila with moveoutright

    show kvin happy at right with move
    show derek normal at left with moveinleft:
            xzoom -1
            yalign 1.0
    derek "Uh… no but how did yo-"
    kvin "The system was so old i just had to open the command pannel on the back and -"
    derek "Robotic sorcery, understood."

    hide derek with moveoutleft
    show kvin happy at left with move
    show neonila normal at right with moveinright
    neonila "This… THING almost killed me and all you’re talking about is nerd stuff? Are you guys for real?"

    hide kvin with moveoutleft
    show sharon normal at left with moveinleft:
        xzoom -1
        yalign 1.0
    sharon "Okay everybody CALM DOWN! None of these abomination seems to be coming back up, so it is grand time we take our leave!"


















label returnnormal:
    stop music fadeout 1.0
    play music "/audio/train_roule.mp3"

    scene bg_parade_car with dissolve:
        zoom 0.5

    show room-deactivated_onlyrobots

    "all robots drops"

    scene bg_parade_car:
        xalign 0.6
        yalign 0.4

    "let's go to the kitchen"


    stop music fadeout 1.0
    jump enterKitchen #kitchen.rpy
