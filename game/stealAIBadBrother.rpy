# Steal AI minigame ( Sc 11.2 / 12.2)

screen chipbot_badbrother():
    imagebutton:
        yalign 0.5
        xalign 0.5
        idle "chipbot"
        focus_mask True

        action Jump("endStealAIBadBrotherGame")

label initStealAIBadBrother:
    $ charactersList = {
        "kvin": { "distract" : 25, "thief" : 70 },
        "hans": { "distract" : 40, "thief" : 100 },
        "neonila": { "distract" : 45, "thief" : 120 },
        "lin": { "distract" : 40, "thief" : 120 },
        "sharon": { "distract" : 35, "thief" : 80 },
        "derek": { "distract" : 30, "thief" : 90 }
        }
    jump stealAIBadBrother

image thiefChr = "[thiefPath]"

label stealAIBadBrother:
    scene bg_storage:
        zoom 0.5
    play music "/audio/musique_suspens.mp3"

    show derek normal at right with moveinright
    derek "So, how are we going to take this AI?"

    show kvin normal at left with moveinleft:
        xzoom -1
        yalign 1.0
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
    show sharon normal at left with moveinleft:
        xzoom -1
        yalign 1.0
    sharon "We have to choose who will steal the chip, someone discreet will be more efficient."

    hide neonila
    hide sharon
    with None

    jump selectThiefBadBrother


label selectThiefBadBrother:
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

    show sharon normal at right with moveinright
    sharon "Now we have to choose who will distract the robot, I think we shouldn't send more than 3 people, it would be too suspicious."
    hide sharon with moveoutright
    $ distractTeam = []
    $ distractScore = 0

    jump selectDistractorsBadBrother



label selectDistractorsBadBrother:

    menu:
        "Who will distract the robot?"

        "Derek" if "derek" in charactersList:
            show derek normal at right with moveinright
            derek "I will ask him if he is ready for war."

            menu:
                derek "I will ask him if he is ready for war."
                "Choose Derek":
                    $ distractTeam.append([derek, charactersList["derek"]["distract"]])
                    $ distractScore += charactersList["derek"]["distract"]
                    $ charactersList.pop("derek")
                "Choose someone else":
                    $ nothing = ""


            hide derek with moveoutright

        "Hans" if "hans" in charactersList:
            show hans normal at right with moveinright
            hans "I will ask him about the reptilians..."

            menu:
                hans "I will ask him about the reptilians..."
                "Choose Hans":
                    $ distractTeam.append([hans, charactersList["hans"]["distract"]])
                    $ distractScore += charactersList["hans"]["distract"]
                    $ charactersList.pop("hans")
                "Choose someone else":
                    $ nothing = ""

            hide hans with moveoutright

        "Lin" if "lin" in charactersList:
            show lin normal at right with moveinright
            lin "I will ask him if he has a lens for my camera."

            menu:
                lin "I will ask him if he has a lens for my camera."
                "Choose Lin":
                    $ distractTeam.append([lin, charactersList["lin"]["distract"]])
                    $ distractScore += charactersList["lin"]["distract"]
                    $ charactersList.pop("lin")
                "Choose someone else":
                    $ nothing = ""

            hide lin with moveoutright

        "Kvin" if "kvin" in charactersList:
            show kvin normal at right with moveinright
            kvin "I will try to know more about him!"

            menu:
                kvin "I will try to know more about him!"
                "Choose Kvin":
                    $ distractTeam.append([kvin, charactersList["kvin"]["distract"]])
                    $ distractScore += charactersList["kvin"]["distract"]
                    $ charactersList.pop("kvin")
                "Choose someone else":
                    $ nothing = ""

            hide kvin with moveoutright

        "Neonila" if "neonila" in charactersList:
            show neonila normal at right with moveinright
            neonila "I'm going to film it, it will make a lot of views!"

            menu:
                neonila "I'm going to film it, it will make a lot of views!"
                "Choose Neonila":
                    $ distractTeam.append([neonila, charactersList["neonila"]["distract"]])
                    $ distractScore += charactersList["neonila"]["distract"]
                    $ charactersList.pop("neonila")
                "Choose someone else":
                    $ nothing = ""

            hide neonila with moveoutright

        "Sharon" if "sharon" in charactersList:
            show sharon normal at right with moveinright
            sharon "I will ask him what is happening on this train."

            menu:
                sharon "I will ask him what is happening on this train."
                "Choose Sharon":
                    $ distractTeam.append([sharon, charactersList["sharon"]["distract"]])
                    $ distractScore += charactersList["sharon"]["distract"]
                    $ charactersList.pop("sharon")
                "Choose someone else":
                    $ nothing = ""

            hide sharon with moveoutright


    if len(distractTeam) == 3:
        jump startStealGameBadBrother

    jump selectDistractorsBadBrother

label startStealGameBadBrother:

    $ thiefX = 1.4

    scene bg_storage:
        zoom 0.5
    show kais_storage normal at topcenter zorder 10 with moveintop
    show thiefChr:
        xalign thiefX
        yalign 1.0
    with Dissolve(1)

    $ distractIndex = 0
    if thiefScore <= distractScore:
        $ thiefSpeed = 0.06
    else:
        $ thiefSpeed = 0.04
    jump distractRobotBadBrother


define moveThief = { "master" : MoveTransition(0.5) }

label distractRobotBadBrother:
    if distractTeam[distractIndex][0] == derek:
        show derek normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "Tell me robot, are you ready for war?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "A war? Nobody attacked us!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "Nobody for the moment, but the enemy can come anytime, you must always be ready!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "The security system is fully operational, I don't need your advice."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        derek "All right, but you shouldn't complain if you lose the war..."
        hide derek with moveoutleft
    elif distractTeam[distractIndex][0] == lin:
        show lin normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "I have a problem with my camera, I was wondering if I could look for a new lens here."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "No, this storage is not for you."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "This camera is very important for me you know? It's a gift from my grandfather and..."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "Enough! I will not help you!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        lin "I will not insist, sorry for the inconvenience."
        hide lin with moveoutleft
    elif distractTeam[distractIndex][0] == kvin:
        show kvin normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "I like robots, you're so cool! What are you doing here?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "I take care of the inventory of our spare parts and I store them in this room."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "Cool! Since when have you been doing this? Did you do anything else before? How do you store the pieces?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "I don't have time to answer you kid, leave me alone."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        kvin "Okay..."
        hide kvin with moveoutleft
    elif distractTeam[distractIndex][0] == hans:
        show hans normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "I know you are like the others, your creator is a reptilian isn't it?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "A reptilian? What are you talking about?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "You play ignorance! That's what they all do! But I know the truth!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "You are just crazy, get out of here."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        hans "Did I piss off the reptilians? I better leave..."
        hide hans with moveoutleft
    elif distractTeam[distractIndex][0] == sharon:
        show sharon normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "Can you tell us what's going on here? This train is not normal!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "I don't know what you mean, everything is as usual."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "As usual? The robots are crazy! Where are the human staff who take care of the contest?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "I said that everything is as usual, if you have nothing else to say, go away."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        sharon "It will not happen like that, I will file a complaint."
        hide sharon with moveoutleft
    elif distractTeam[distractIndex][0] == neonila:
        show neonila normal at left with moveinleft:
            xzoom -1
            yalign 1.0
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Hello everyone, today we’re going to explore a creepy train! Very strange things have happened since I arrived, this train probably hides a terrifying secret!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "Hey you! Filming here is not allowed, stop it."
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Hello Mr. robot, some of your friends act very strangely, can you tell our viewers what's going on here?"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        badbrother "Stop it right now if you wanna leave alive!"
        show thiefChr:
            xalign thiefX yalign 1.0
        with moveThief
        $ thiefX = thiefX - thiefSpeed
        neonila "Ok, ok ... Sorry my viewers, the live will be shorter than expected!"
        hide neonila with moveoutleft


    if distractIndex < 2:
        $ distractIndex = distractIndex + 1
        jump distractRobotBadBrother

    $ config.autosave_on_quit = True
    $ _game_menu_screen = "save"
    $ allowSave = True

    if thiefScore <= distractScore:
        stop music fadeout 1.0
        show kais_storage deactivated
        play sound "/audio/robot_power_off.mp3"
        badbrother "{i}[[Error: AI chip missing. System shutdown...]{/i}"
        hide kais_storage with moveouttop
        show chipbot with moveinbottom:
            yalign 0.5
            xalign 0.5

        show thiefChr at right with move
        thiefName "I have the chip!"
        call screen chipbot_badbrother
    else:
        show thiefChr at right
        show kais_storage angry:
            xalign 0.4
            yalign 0.0
        with move
        badbrother "Hey! You! What are you doing?!?"
        thiefName "I ..."
        badbrother "Get out of here!"
        $ failBadBrotherSteal = True
        if failGoodBrotherSteal:
            jump gameover1 # gameovers.rpy
    jump explorationMap # explorationMap.rpy

label endStealAIBadBrotherGame:
    hide chipbot with moveoutbottom

    $ takeBadBrotherAI = True

    jump goodBrotherRevealDoor # kitchen.rpy
