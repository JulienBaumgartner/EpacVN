 # Storage game ( Sc 14)
screen search_key_game_map():
    imagemap:
        idle "room-deactivated_onlyrobots-sansombre"

        if 1 not in watchedAreas:
            hotspot (531, 558, 258, 225) action Jump("karen1")
        if 2 not in watchedAreas:
            hotspot (851, 549, 98, 78) action Jump("karen2")
        if 3 not in watchedAreas:
            hotspot (850, 629, 217, 98) action Jump("guggen1")
        if 4 not in watchedAreas:
            hotspot (1079, 544, 140, 93) action Jump("guggen2")
        if 5 not in watchedAreas:
            hotspot (1220, 568, 228, 178) action Jump("guggen3")

label startkeygame:
    scene bg_parade_car :
        zoom 0.5
    show room-deactivated_onlyrobots
    $ watchedAreas = []
    jump researchContinue

label researchContinue:
    call screen search_key_game_map

label karen1:
    $ watchedAreas.append(1)
    show kvin normal at right with moveinright
    kvin "She looks like the Miss who was given the key, but I can't find it."
    hide kvin with moveoutright
    jump researchContinue

label karen2:
    $ watchedAreas.append(2)
    show lin normal at right with moveinright
    lin "Perfect, I found the key... It's a beautiful pose! Let me take a picture of this robot."
    show sharon normal at left with moveinleft:
        xzoom -1
        yalign 1.0
    sharon "We don't have time for that!"
    lin "It's good, I'm done, let's go!" with flash
    hide lin with moveoutright
    hide sharon with moveoutleft
    jump finishkeygame

label guggen1:
    $ watchedAreas.append(3)
    show derek normal at right with moveinright
    derek "This one didn't survive the war ... But he doesn't seem to have the key..."
    hide derek with moveoutright
    jump researchContinue

label guggen2:
    $ watchedAreas.append(4)
    show hans normal at right with moveinright
    hans "Stay calm... It's... WAIT, IT'S A TRAP! ... No? We will say that the key is not there, I will not take more risks for that..."
    hide hans with moveoutright
    jump researchContinue

label guggen3:
    $ watchedAreas.append(5)
    show neonila normal at right with moveinright
    neonila "Ok everyone, if you see the key don't hesitate to tell me with a donation, I will mention you on Slowstagram! But I don't see anything here..."
    hide neonila with moveoutright
    jump researchContinue

label finishkeygame:
    $ hasAiKey = True
    jump openAiDoor # kitchen.rpy
