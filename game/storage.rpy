# Sc 10, Sc 12, Sc 14
# Storage car scenes


# Enter from the map
label enterStorage:
    scene bg_storage:
        zoom 0.5
    if firstEnterStorage:
        jump firstStorage
    elif goodBrotherAskHelp or badBrotherAskHelp:
        jump badBrotherActions
    else:
        "Nothing to do here"
        jump explorationMap # explorationMap.rpy

#Sc 08.2
label firstStorage:
    "Sc 10, First entry in the storage"
    $ firstEnterStorage = False
    jump badBrotherActions


label badBrotherActions:
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
    jump explorationMap # explorationMap.rpy

#Sc 12
label takeAIBadBrother:
    jump initStealAIBadBrother # stealAIBadBrother.rpy
