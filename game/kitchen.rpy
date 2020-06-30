# Sc 09, Sc 13
# Kitchen car scenes

# Enter from the map
label enterKitchen:
    play music "/audio/kitchen01.mp3"
    scene bg_kitchen_door_closed
    if firstEnterKitchen:
        jump kitchencar

    elif AIDoorReveal:

        if hasAiKey:
            jump openAiDoor
        else:
            jump searchAiDoorKey

    else:
        "Nothing to do here"
        jump explorationMap #explorationMap.rpy

#Sc 09
label kitchencar:

    $ firstEnterKitchen = False
    "Sc 09, kitchen car"
    scene bg_kitchen_bacameat
    "Old tourist group dead"
    play sound "/audio/porte01.mp3"
    "locked inside"
    scene bg_kitchen_door_back

    $ renpy.take_screenshot()
    $ renpy.save(renpy.newest_slot(), "In the kitchen")
    $ config.autosave_on_quit = False
    $ _game_menu_screen = "preferences"
    $ allowSave = False

    jump startpasswordgame #mastermind.rpy

#Sc 13
label goodBrotherRevealDoor:
    scene bg_kitchen_door_opened
    play sound "/audio/porte01.mp3"
    "Sc 13, The good brother reveal the door in the kitchen"
    jump inspectAiDoor

#Sc 13
label badBrotherRevealDoor:
    scene bg_kitchen_door_opened
    play sound "/audio/porte01.mp3"
    "Sc 13, The bad brother reveal the door in the kitchen"
    jump inspectAiDoor


#Sc 13.2 / 13.3
label inspectAiDoor:
    scene bg_kitchen_cardpass
    if hasAiKey:
        show cardchip with moveinright:
                yalign 0.6
                xalign 0.5
        "Sc 13.3, You have the key."
        jump openAiDoor
    jump searchAiDoorKey

#Sc 13.4
label searchAiDoorKey:
    "Sc 13.4, you don't have the key."
    "The key is in the parade car."
    jump startkeygame # searchTheKeyGame.rpy

#Sc 13.5
label openAiDoor:
    scene bg_kitchen_cardpass
    "Sc 13.5, you can open the door"
    scene bg_kitchen_dooropen
    "the door is open"
    jump enterAIroom #AIcar.rpy
