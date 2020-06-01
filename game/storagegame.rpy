 # Storage game ( Sc 14)
screen storage_game_map():
    imagemap:
        idle "bg storage_game"
        hover "bg storage_game_selected"

        if 1 not in watchedAreas:
            hotspot (218, 248, 352, 514) action Jump("area1") alt "Area1"
        if 2 not in watchedAreas:
            hotspot (782, 562, 169, 291) action Jump("area2") alt "Area2"
        if 3 not in watchedAreas:
            hotspot (1096, 471, 210, 221) action Jump("area3") alt "Area3"
        if 4 not in watchedAreas:
            hotspot (972, 0, 147, 333) action Jump("area4") alt "Area4"
        if 5 not in watchedAreas:
            hotspot (1398, 345, 259, 183) action Jump("area5") alt "Area5"

label startstoragegame:
    scene bg paradeCar
    $ distractTeam = []
    $ researchTeam = []
    $ distractDialogueUsed = []
    $ lastDistraction = None
    $ watchedAreas = []
    $ lastResearch = None
    $ findKey = False
    $ findPiece = False

    $ distractTeam.append("lin")
    $ distractTeam.append("hans")
    $ distractDialogueUsed.append(False)
    $ distractDialogueUsed.append(False)

    $ researchTeam.append([kvin, "kvin normal.png"])
    $ researchTeam.append([neonila, "neonila normal.png"])
    jump distractTeamTurn

label distractTeamTurn:

    if lastDistraction == None:
        scene bg storage
        with Dissolve(1)
        show stwin normal at topleft with moveinleft

        stwin "You are not supposed to be here humans, what do you want?"

    elif lastDistraction == "lin":
        scene bg storage
        show stwin normal at topleft
        show lin normal at right
        with Dissolve(1)

        lin "This camera is very important for me you know? It's a gift from my grandfather and..."
        stwin "Enough! I will not help you!"
        lin "I will not insist, sorry for the inconvenience."
        hide lin with moveoutright

    elif lastDistraction == "hans":
        scene bg storage
        show stwin normal at topleft
        show hans normal at right
        with Dissolve(1)

        hans "And that's how I know the reptilians control this train!"
        stwin "You are just crazy, get out of here."
        hans "Did I piss off the reptilians? I better leave..."
        hide hans with moveoutright


    if False not in distractDialogueUsed:
        stwin "You talk too much, it's suspicious..."
        jump losestoragegame

    menu:
        "Kim: Can you help me to fix my camera?" if "lin" in distractTeam and distractDialogueUsed[distractTeam.index("lin")] == False:
            $ distractDialogueUsed[distractTeam.index("lin")] = True
            $ lastDistraction = "lin"
            show lin normal at right with moveinright
            lin "I have a problem with my camera, I was wondering if I could look for a new lens here."
            stwin "No, this storage is not for you."
            lin "I understand, maybe you can inspect my camera and try to fix my lens?"
            jump researchTeamTurn


        "Hanz: Is your creator a reptilian?" if "hans" in distractTeam and distractDialogueUsed[distractTeam.index("hans")] == False:
            $ distractDialogueUsed[distractTeam.index("hans")] = True
            $ lastDistraction = "hans"
            show hans normal at right with moveinright
            hans "I know you are like the others, your creator is a reptilian isn't it?"
            stwin "A reptilian? What are you talking about?"
            hans "You play ignorance! That's what they all do! But I know the truth!"
            jump researchTeamTurn


label researchTeamTurn:
    $ currentIndex = 0

    scene bg storage_game
    with Dissolve(1)

    jump researchTeamTurnContinue

label researchTeamTurnContinue:

    while currentIndex < len(researchTeam):
        $ lastResearch = researchTeam[currentIndex]
        $ currentIndex = currentIndex + 1
        lastResearch[0] "Where can I search?"
        call screen storage_game_map

    jump distractTeamTurn

image researchChr = "[path]"

label area1:
    $ watchedAreas.append(1)
    hide screen storage_game_map
    $ path = lastResearch[1]
    show researchChr at right with moveinright
    lastResearch[0] "It's just some disabled robots. Nothing useful here."
    hide researchChr with moveoutright
    jump researchTeamTurnContinue

label area2:
    $ watchedAreas.append(2)
    hide screen storage_game_map
    $ path = lastResearch[1]
    show researchChr at right with moveinright
    lastResearch[0] "Hanging robots? Perfect! One of them has the right piece! We can leave the room."
    $ findPiece = True
    hide researchChr with moveoutright
    jump finishstoragegame

label area3:
    $ watchedAreas.append(3)
    hide screen storage_game_map
    $ path = lastResearch[1]
    show researchChr at right with moveinright
    lastResearch[0] "There are many things here... What is that?"
    lastResearch[0] "Oops, a flash... I shouldn't have pressed it..." with flash

    scene bg storage
    show stwin normal at topleft
    with Dissolve(1)
    stwin "A flash?!? What is happening?"

    menu:
        stwin "A flash?!? What is happening?"
        "Kim: I took a photo" if "lin" in distractTeam:
            show lin normal at right with moveinright
            lin "It's just me, I took a photo."
            stwin "You are not allowed to take photos here, stop."
            lin "Sorry!"

            scene bg storage_game
            show researchChr at right
            with Dissolve(1)

            lastResearch[0] "I better be more careful..."
            hide researchChr with moveoutright

            jump researchTeamTurnContinue


        "Hanz: It's an alien" if "hans" in distractTeam:
            show hans normal at right with moveinright
            hans "It's an alien! Don't look at him!"
            stwin "I don't think so..."
            hide hans with moveoutright

            jump losestoragegame


label area4:
    $ watchedAreas.append(4)
    hide screen storage_game_map
    $ path = lastResearch[1]
    show researchChr at right with moveinright
    lastResearch[0] "I don't think the piece is here... Wait, is that a key? I don't know what it opens, but I'll keep it."
    $ findKey = True
    hide researchChr with moveoutright
    jump researchTeamTurnContinue

label area5:
    $ watchedAreas.append(5)
    hide screen storage_game_map
    $ path = lastResearch[1]
    show researchChr at right with moveinright
    lastResearch[0] "It's just broken parts. Nothing useful here."
    hide researchChr with moveoutright
    jump researchTeamTurnContinue

label losestoragegame:
    show researchChr at outLeft with None
    show researchChr at left
    show stwin at topright
    with move
    stwin "Hey! You! What are you doing?!?"
    lastResearch[0] "I ..."
    stwin "Get out of here!"

    jump gameover4 # gameovers.rpy

label finishstoragegame:

    "You have the key"
    jump openAiDoor # kitchen.rpy
