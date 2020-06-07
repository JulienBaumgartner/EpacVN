# Sc 15 
# AI car scenes

label enterAIroom:
    scene bg_AI_Room
    "Sc 15, discussion with the AI"
    if takeGoodBrotherAI:
        jump uploadGoodBrother
    jump uploadBadBrother

label uploadGoodBrother:
    "Sc 15.1, upload good brother."
    "Sc 15.1.2, good brother is crazy"
    jump escapegame

label uploadBadBrother:
    "Sc 15.2, upload bad brother"
    jump escapegame


# label revelation:
    #scene bg_hangar_green
    #"Sc 16, revelation bunker"
    #"End"
    return
