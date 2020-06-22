# Sc 10, Sc 12, Sc 14
# Storage car scenes


# Enter from the map
label enterStorage:
    play music "/audio/storage 01.mp3"
    scene bg_storage:
        zoom 0.5
    if firstEnterStorage:
        jump firstStorage
    elif goodBrotherAskHelp or badBrotherAskHelp:
        jump badBrotherActions
    else:
        "Nothing to do here"
        stop music fadeout 1.0
        jump explorationMap # explorationMap.rpy

#Sc 08.2
label firstStorage:

    "Description du storage"



    "Sc 10, First entry in the storage"

    scene bg_storage_empty:
        yalign 0.1
        xalign 0.9

    show kais_storage_normal with moveintop:
        zoom 0.4

    $ firstEnterStorage = False
    jump badBrotherActions


label badBrotherActions:



    #show kais_storage_normal with moveintop:
        #zoom 0.4
    if goodBrotherAskHelp and not takeGoodBrotherAI:
        menu:
            "What do you want to do with the bad brother?"

            "Discuss":
                jump discussBadBrother
            "Take AI":
                jump takeAIBadBrother

    jump discussBadBrother


label discussBadBrother:
    if not badBrotherAskHelp:
        "Bad brother request: take good brother AI"
        $ badBrotherAskHelp = True
    else:
        "You don't have the good brother AI"

    if goodBrotherAskHelp:
        menu:
            "Explore":
                jump explorationMap # explorationMap.rpy
            "Take AI":
                jump takeAIBadBrother
    stop music fadeout 1.0
    jump explorationMap # explorationMap.rpy

#Sc 12
label takeAIBadBrother:
    stop music fadeout 1.0
    jump initStealAIBadBrother # stealAIBadBrother.rpy
