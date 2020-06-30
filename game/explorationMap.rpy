# Sc 08
# Exploration map

label explorationMap:
    stop music fadeout 1.0
    scene bg_map
    menu:
        "Exploration choices"

        "Storage car" if not takeBadBrotherAI:
            jump enterStorage #storage.rpy

        "Bar" if not takeGoodBrotherAI:
            jump enterBar #bar.rpy
