# Sc 09, Sc 13
# Kitchen car scenes

# Enter from the map
label enterKitchen:
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
    "Old tourist group dead"
    "locked inside"
    jump startpasswordgame #mastermind.rpy

#Sc 13
label goodBrotherRevealDoor:
    scene bg_Exit_Door_closed
    "Sc 13, The good brother reveal the door in the kitchen"
    jump inspectAiDoor

#Sc 13
label badBrotherRevealDoor:
    scene bg_Exit_Door_closed
    "Sc 13, The bad brother reveal the door in the kitchen"
    jump inspectAiDoor


#Sc 13.2 / 13.3
label inspectAiDoor:
    scene bg_Exit_Door_closed
    if hasAiKey:
        "Sc 13.3, You have the key."
        jump openAiDoor
    jump searchAiDoorKey

#Sc 13.4
label searchAiDoorKey:
    "Sc 13.4, you don't have the key."
    "The key is in the parade car."
    jump startstoragegame # storagegame.rpy

#Sc 13.5
label openAiDoor:
    "Sc 13.5, the door is open"
    jump enterAIroom #AIcar.rpy
