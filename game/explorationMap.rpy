# Sc 08
# Exploration map

label explorationMap:
    scene bg map
    menu:
        "Exploration choices"

        "Storage car" if not takeBadBrotherAI and not failBadBrotherSteal :
            jump enterStorage #storage.rpy

        "Bar" if not takeGoodBrotherAI and not failGoodBrotherSteal:
            jump enterBar #bar.rpy
