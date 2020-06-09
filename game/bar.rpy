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
        jump explorationMap #explorationMap.rpy

#Sc 08.2
label firstBar:
    show kais_normal with moveinright:
        zoom 0.4
    "First enter in the bar"
    $ firstEnterBar = False
    jump goodBrotherActions



label goodBrotherActions:
    if badBrotherAskHelp and not takeBadBrotherAI:
        menu:
            "What do you want to do with the good brother?"

            "Discuss":
                jump discussGoodBrother
            "Take AI":
                jump takeAIGoodBrother

    jump discussGoodBrother


label discussGoodBrother:
    if not goodBrotherAskHelp:

        goodbrother "Good brother request: take bad brother AI"
        $ goodBrotherAskHelp = True
    else:
        "You don't have the bad brother AI"

    if badBrotherAskHelp:
        menu:
            "Explore":
                jump explorationMap
            "Take AI":
                jump takeAIGoodBrother
    jump explorationMap #explorationMap.rpy

#Sc 11
label takeAIGoodBrother:
    jump initStealAIGoodBrother #stealAIGoodBrother.rpy
