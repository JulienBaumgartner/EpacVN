# Steal AI minigame ( Sc 11.2 / 12.2)

label initStealAIGoodBrother:
    $ charactersList = {
        "kvin": { "distract" : 25, "thief" : 70 },
        "hans": { "distract" : 40, "thief" : 100 },
        "neonila": { "distract" : 45, "thief" : 120 },
        "lin": { "distract" : 40, "thief" : 120 },
        "sharon": { "distract" : 35, "thief" : 80 },
        "derek": { "distract" : 30, "thief" : 90 }
        }
    jump stealAIGoodBrother

image distractChr = "[distractPath]"
image thiefChr = "[thiefPath]"

label stealAIGoodBrother:
    scene bg_bar:
        zoom 0.5
    show derek normal at right with moveinright
    derek "So, how are we going to take this AI?"

    show kvin normal at left with moveinleft
    kvin "The other robot said his AI is stored on a chip behind his back!"

    hide derek with moveoutright
    show hans normal at right with moveinright
    hans "In this case we just have to steal this chip..."

    hide kvin with moveoutleft
    show lin normal at left with moveinleft
    lin "It will desactivate him, he will not let us do."

    hide hans with moveoutright
    show neonila normal at right with moveinright
    neonila "We just have to distract him and it's good!"

    hide lin with moveoutleft
    show sharon normal at left with moveinleft
    sharon "We have to choose who will steal the chip, someone discreet will be more efficient."

    hide neonila
    hide sharon
    with None

    jump selectThiefGoodBrother


label selectThiefGoodBrother:
    scene bg_bar:
        zoom 0.5
    menu:
        "Who will steal the chip?"

        "Derek":
            $ thiefPath = "derek normal.png"
            $ thiefName = derek
            $ thiefScore = charactersList["derek"]["thief"]
            $ charactersList.pop("derek")

            show derek normal at right with moveinright
            derek "It's a dangerous mission, I'll do it."
            hide derek with moveoutright

        "Hans":
            $ thiefPath = "hans normal.png"
            $ thiefName = hans
            $ thiefScore = charactersList["hans"]["thief"]
            $ charactersList.pop("hans")

            show hans normal at right with moveinright
            hans "Me? I hope this is not a trap..."
            hide hans with moveoutright

        "Lin":
            $ thiefPath = "lin normal.png"
            $ thiefName = lin
            $ thiefScore = charactersList["lin"]["thief"]
            $ charactersList.pop("lin")

            show lin normal at right with moveinright
            lin "Sure, I can do it!"
            hide lin with moveoutright

        "Kvin":
            $ thiefPath = "kvin normal.png"
            $ thiefName = kvin
            $ thiefScore = charactersList["kvin"]["thief"]
            $ charactersList.pop("kvin")

            show kvin normal at right with moveinright
            kvin "It's cool! He won't see me!"
            hide kvin with moveoutright

        "Neonila":
            $ thiefPath = "neonila normal.png"
            $ thiefName = neonila
            $ thiefScore = charactersList["neonila"]["thief"]
            $ charactersList.pop("neonila")

            show neonila normal at right with moveinright
            neonila "I'm going to stream this, I'm sure my viewers will love it!"
            hide neonila with moveoutright

        "Sharon":
            $ thiefPath = "sharon normal.png"
            $ thiefName = sharon
            $ thiefScore = charactersList["sharon"]["thief"]
            $ charactersList.pop("sharon")

            show sharon normal at right with moveinright
            sharon "I better take care of it myself."


    jump selectDistractorsGoodBrother



label selectDistractorsGoodBrother:

    if len(charactersList) == 5:
        show sharon normal at right with moveinright
        sharon "Now we have to choose who will distract the robot, I think we shouldn't send more than 3 people, it would be too suspicious."
        hide sharon with moveoutright
        $ distractTeam = []
        $ distractScore = 0

    menu:
        "Who will distract the robot?"

        "Derek" if "derek" in charactersList:
            $ distractTeam.append([derek, "derek normal.png", charactersList["derek"]["distract"]])
            $ distractScore += charactersList["derek"]["distract"]
            $ charactersList.pop("derek")

            show derek normal at right with moveinright
            derek "I will ask him if he is ready for war."
            hide derek with moveoutright

        "Hans" if "hans" in charactersList:
            $ distractTeam.append([hans, "hans normal.png", charactersList["hans"]["distract"]])
            $ distractScore += charactersList["hans"]["distract"]
            $ charactersList.pop("hans")

            show hans normal at right with moveinright
            hans "I will ask him about the reptilians..."
            hide hans with moveoutright

        "Lin" if "lin" in charactersList:
            $ distractTeam.append([lin, "lin normal.png", charactersList["lin"]["distract"]])
            $ distractScore += charactersList["lin"]["distract"]
            $ charactersList.pop("lin")

            show lin normal at right with moveinright
            lin "I will ask him if he has a lens for my camera."
            hide lin with moveoutright

        "Kvin" if "kvin" in charactersList:
            $ distractTeam.append([kvin, "kvin normal.png", charactersList["kvin"]["distract"]])
            $ distractScore += charactersList["kvin"]["distract"]
            $ charactersList.pop("kvin")

            show kvin normal at right with moveinright
            kvin "I will try to know more about him!"
            hide kvin with moveoutright

        "Neonila" if "neonila" in charactersList:
            $ distractTeam.append([neonila, "neonila normal.png", charactersList["neonila"]["distract"]])
            $ distractScore += charactersList["neonila"]["distract"]
            $ charactersList.pop("neonila")

            show neonila normal at right with moveinright
            neonila "I'm going to film it, it will make a lot of views!"
            hide neonila with moveoutright

        "Sharon" if "sharon" in charactersList:
            $ distractTeam.append([sharon, "sharon normal.png", charactersList["sharon"]["distract"]])
            $ distractScore += charactersList["sharon"]["distract"]
            $ charactersList.pop("sharon")

            show sharon normal at right with moveinright
            sharon "I will ask him what is happening on this train."
            hide sharon with moveoutright


    if len(distractTeam) == 3:
        jump startStealGameGoodBrother

    jump selectDistractorsGoodBrother

label startStealGameGoodBrother:

    $ thiefX = 1.4

    scene bg_storage:
        zoom 0.5
    show stwin normal at topcenter zorder 10
    show thiefChr:
        xalign thiefX
        yalign 1.0
    with Dissolve(1)

    $ distractIndex = 0
    if thiefScore <= distractScore:
        $ thiefSpeed = 0.06
    else:
        $ thiefSpeed = 0.04
    jump distractRobotGoodBrother


define moveThief = { "master" : MoveTransition(0.5) }

label distractRobotGoodBrother:
    $ distractPath = distractTeam[distractIndex][1]
    show distractChr at left with moveinleft

    if distractTeam[distractIndex][0] == derek:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "Tell me robot, are you ready for war?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "A war? Nobody attacked us!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "Nobody for the moment, but the enemy can come anytime, you must always be ready!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "The security system is fully operational, I don't need your advice."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "All right, but you shouldn't complain if you lose the war..."
    elif distractTeam[distractIndex][0] == lin:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "I have a problem with my camera, I was wondering if I could look for a new lens here."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "No, this storage is not for you."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "This camera is very important for me you know? It's a gift from my grandfather and..."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "Enough! I will not help you!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "I will not insist, sorry for the inconvenience."
    elif distractTeam[distractIndex][0] == kvin:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "I like robots, you're so cool! What are you doing here?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "I take care of the inventory of our spare parts and I store them in this room."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "Cool! Since when have you been doing this? Did you do anything else before? How do you store the pieces?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "I don't have time to answer you kid, leave me alone."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "Okay..."
    elif distractTeam[distractIndex][0] == hans:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "I know you are like the others, your creator is a reptilian isn't it?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "A reptilian? What are you talking about?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "You play ignorance! That's what they all do! But I know the truth!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "You are just crazy, get out of here."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "Did I piss off the reptilians? I better leave..."
    elif distractTeam[distractIndex][0] == sharon:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "Can you tell us what's going on here? This train is not normal!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "I don't know what you mean, everything is as usual."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "As usual? The robots are crazy! Where are the human staff who take care of the contest?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "I said that everything is as usual, if you have nothing else to say, go away."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "It will not happen like that, I will file a complaint."
    elif distractTeam[distractIndex][0] == neonila:
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Hello everyone, today we’re going to explore a creepy train! Very strange things have happened since I arrived, this train probably hides a terrifying secret!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "Hey you! Filming here is not allowed, stop it."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Hello Mr. robot, some of your friends act very strangely, can you tell our viewers what's going on here?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        stwin "Stop it right now if you wanna leave alive!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Ok, ok ... Sorry my viewers, the live will be shorter than expected!"


    if distractIndex < 2:
        hide distractChr with moveoutleft
        $ distractIndex = distractIndex + 1
        jump distractRobotGoodBrother

    if thiefScore <= distractScore:
        stwin "{i}[[Error: AI chip missing. System shutdown...]{/i}"
        show thiefChr at right with move
        thiefName "I have the chip!"
        $ takeGoodBrotherAI = True
        jump badBrotherRevealDoor # kitchen.rpy
    else:
        show distractChr at outLeft
        show thiefChr at right
        show stwin at topleft
        with move
        stwin "Hey! You! What are you doing?!?"
        thiefName "I ..."
        stwin "Get out of here!"
        $ failGoodBrotherSteal = True
        if failBadBrotherSteal:
            jump gameover1 # gameovers.rpy
    jump explorationMap # explorationMap.rpy
