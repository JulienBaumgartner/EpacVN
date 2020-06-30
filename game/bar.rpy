# Sc 08, Sc 11
# Bar parade scenes

# Enter from the map
label enterBar:
    play music "/audio/bar_01.mp3"
    scene bg_bar:
        zoom 0.5
    if firstEnterBar:
        jump firstBar
    elif goodBrotherAskHelp or badBrotherAskHelp:
        jump goodBrotherActions
    else:
        "Nothing to do here"
        stop music fadeout 1.0
        jump explorationMap #explorationMap.rpy

#Sc 08.2
label firstBar:
    show kais normal at topcenter with moveintop
    "First enter in the bar"
    $ firstEnterBar = False
    jump goodBrotherActions



label goodBrotherActions:
    if failGoodBrotherSteal:
        show kais crazy at topcenter with moveintop
        goodbrother "It's you again? Pay attention, I'm watching you."
    else:
        show kais normal at topcenter with moveintop

    if badBrotherAskHelp and not takeBadBrotherAI:
        $ renpy.take_screenshot()
        $ renpy.save(renpy.newest_slot(), "In the bar")
        menu:
            "What do you want to do with the good brother?"

            "Discuss":
                jump discussGoodBrother
            "Take AI" if not failGoodBrotherSteal:
                jump takeAIGoodBrother
            "Explore" if failGoodBrotherSteal:
                jump explorationMap

    jump discussGoodBrother


label discussGoodBrother:
    show kais normal
    if not goodBrotherAskHelp:

        goodbrother "Good brother request: take bad brother AI"
        $ goodBrotherAskHelp = True
    else:
        "You don't have the bad brother AI"

    if badBrotherAskHelp and not failGoodBrotherSteal:
        menu:
            "Explore":
                stop music fadeout 1.0
                jump explorationMap
            "Take AI":
                jump takeAIGoodBrother
    jump explorationMap #explorationMap.rpy

#Sc 11
label takeAIGoodBrother:
    $ config.autosave_on_quit = False
    $ _game_menu_screen = "preferences"
    $ allowSave = False
    jump initStealAIGoodBrother #stealAIGoodBrother.rpy
