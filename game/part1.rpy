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

#Sc 02
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

#Sc 02.3
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

#Sc 03
label departure:
    scene bg_parade_car_turned_seats:
        zoom 0.5
    play sound "/audio/door_closing.mp3"
    play music "/audio/train_roule.mp3" fadein 0.5
    "Sc 03, Departure"

    show neonila surprised with moveinright
    neonila "Wow just look at this scenery, I can’t even feel the train moving!"
    show neonila normal at right
    neonila "Of course, you’d feel it better if I had the last generation streaming camera, but for that I’ll need your help!"
    #neonila "Remember, I only take 95% of your donation for my daily expenses, so EVERYTHING ELSE goes straight to my material budget, just for your comfort! Crazy, right?!"
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

#Sc 04
label parade:
    scene bg_parade_car_confetti:
        zoom 0.5
    play music "audio/katy_edit_loop.mp3" fadein 0.5

    show nr_cara_guggen:
        zoom 0.2
        xalign 0.5
        easein 5.0 xalign 0.5 zoom 0.5
    "Sc 04, Parade"

    show nr_cara_guggen:
        zoom 0.2
        xalign 0.5
        easein 5.0 xalign 0.5 zoom 0.5

    "carnabots"

    stop music fadeout 1.0

    jump bar

#Sc 05
label bar:
    play music "/audio/bar_01.mp3"
    scene bg_bar:
        zoom 0.5

    show kais normal at topcenter with moveinright


    goodbrother "Welcome customers"
    stop music fadeout 1.0
    jump bug

#Sc 06
label bug:
    play music "/audio/alerte01.mp3"

    show animation_alerte:
    #scene in animation:
        zoom 0.5

    "bug"
    "description du bug"
    play sound "/audio/crash_dog.mp3"
    show charles broken with vpunch:
        yalign 0.7
        xalign 0.5
    "crack"
    hide charles

#Sc 07
label crazybot:
    play sound "audio/robot_glitch01.mp3"

    show nr_cara_guggen_crazy with moveinbottom:
        zoom 0.5
        xalign 0.5
        easein 5.0 xalign 0.5 zoom 1

    "Sc 07, Carnabots crazy, dog death"


    hide nr_cara_guggen_crazy with moveoutbottom

    show servicerobot_karen normal at center with moveinright
    service1 "are you ok"

    play sound "audio/robot_glitch02.mp3"
    show servicerobot_karen broken with vpunch:
        zoom 0.5

    service1 "jump on you"
    show servicerobot_karen:
        yalign 0.01 xalign 0.5 zoom 1.0
    pause
    hide servicerobot_karen with moveoutbottom
    pause


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
