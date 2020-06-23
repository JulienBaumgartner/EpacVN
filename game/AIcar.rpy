# Sc 15
# AI car scenes

label enterAIroom:
    scene bg_ai_room
    play music "audio/ai_car_01.mp3"
    "Sc 15, discussion with the AI"
    scene bg_exit_door_closed
    "door closed"
    if takeGoodBrotherAI:
        jump uploadGoodBrother
    jump uploadBadBrother

label uploadGoodBrother:
    scene bg_ai_room_closeup
    "Sc 15.1, upload good brother."
    "Sc 15.1.2, good brother is crazy"
    jump escapegame

label uploadBadBrother:
    scene bg_ai_room_closeup
    "Sc 15.2, upload bad brother"
    jump escapegame


# label revelation:
    #scene bg_hangar_green
    #"Sc 16, revelation bunker"
    #"End"
    return
