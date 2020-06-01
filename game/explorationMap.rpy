# Sc 08
# Exploration map

label explorationMap:
    scene bg map
    menu:
        "Exploration choices"

        "Kitchen car" if firstEnterKitchen or AIDoorReveal:
            jump enterKitchen

        "Storage car" if not takeBadBrotherAI and not failBadBrotherSteal :
            jump enterStorage

        "Bar" if not takeGoodBrotherAI and not failGoodBrotherSteal:
            jump enterBar
