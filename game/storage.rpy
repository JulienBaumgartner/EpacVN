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

    show kais_storage normal at topcenter with moveintop

    $ firstEnterStorage = False
    jump badBrotherActions


label badBrotherActions:
    if failBadBrotherSteal:
        show kais_storage angry at topcenter with moveintop
        badbrother "I hope you haven't come back to steal my chip again, otherwise it will be very bad!"
    else:
        show kais_storage normal at topcenter with moveintop
    if goodBrotherAskHelp and not takeGoodBrotherAI:
        $ renpy.take_screenshot()
        $ renpy.save(renpy.newest_slot(), "In the storage")
        menu:
            "What do you want to do with the bad brother?"

            "Discuss":
                jump discussBadBrother
            "Take AI" if not failBadBrotherSteal:
                jump takeAIBadBrother
            "Explore" if failBadBrotherSteal:
                jump explorationMap

    jump discussBadBrother


label discussBadBrother:
    show kais_storage normal
    if not badBrotherAskHelp:
        badbrother "Bad brother request: take good brother AI"
        $ badBrotherAskHelp = True
    else:
        "You don't have the good brother AI"

    if goodBrotherAskHelp and not failBadBrotherSteal:
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
    $ config.autosave_on_quit = False
    $ _game_menu_screen = "preferences"
    $ allowSave = False
    jump initStealAIBadBrother # stealAIBadBrother.rpy
