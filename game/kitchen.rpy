# Sc 09, Sc 13
# Kitchen car scenes

# Enter from the map
label enterKitchen:
    scene bg kitchen
    if firstEnterKitchen:
        jump kitchencar

    elif AIDoorReveal:

        if hasAiKey:
            jump openAiDoor
        else:
            jump searchAiDoorKey

    else:
        "Nothing to do here"
        jump explorationMap

#Sc 09
label kitchencar:

    $ firstEnterKitchen = False
    "Sc 09, kitchen car"
    "Old tourist group dead"
    "locked inside"
    jump startpasswordgame

#Sc 13
label goodBrotherRevealDoor:
    "Sc 13, The good brother reveal the door in the kitchen"
    jump inspectAiDoor

#Sc 13
label badBrotherRevealDoor:
    "Sc 13, The bad brother reveal the door in the kitchen"
    jump inspectAiDoor


#Sc 13.2 / 13.3
label inspectAiDoor:
    if hasAiKey:
        "Sc 13.3, You have the key."
        jump openAiDoor
    jump searchAiDoorKey

#Sc 13.4
label searchAiDoorKey:
    "Sc 13.4, you don't have the key."
    "The key is in the parade car."
    jump startstoragegame

#Sc 13.5
label openAiDoor:
    "Sc 13.5, the door is open"
    jump enterAIroom
