# Sc 01 - 07
# Before exploration
#test
#Sc 01
label brochure:
    scene bg brochure
    "Sc 01, tourist advert brochure"

    jump sitting

#Sc 02
label sitting:
    scene parade_car_2:
        zoom 0.5

    "Sc 02, Sitting int the train"

    jump findKey

#Sc 02.3
label findKey:
    scene parade_car_2:
        xalign 0.0 yalign 0.6


    "Sc 02.3, find old tourist item keycard"

    menu:
        "What do you want to do?"

        "Keep the key":
            $ hasAiKey = True
            "You keep the key"

        "Give back the key":
            $ hasAiKey = False
            "You give back the key"

    jump departure

#Sc 03
label departure:
    scene parade_car:
        zoom 0.5

    "Sc 03, Departure"

    jump parade

#Sc 04
label parade:

    "Sc 04, Parade"

    jump bar

#Sc 05
label bar:
    scene bg_bar:
        zoom 0.5

    "Sc 05, bar test"

    jump bug

#Sc 06
label bug:
    scene bg parade_car

#Sc 07
label crazybot:

    "Sc 07, Carnabots crazy, dog death"

    jump enterKitchen #kitchen.rpy
