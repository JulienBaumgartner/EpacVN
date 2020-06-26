# The script of the game goes in this file.
# Characters name
define neonila = Character("Neonila", color="ff69fd", callback=partial(char_talking, "neonila"))
define kvin = Character("Kvin", color="c47b4e", callback=partial(char_talking, "kvin"))
define lin = Character("Lin", color="efd693", callback=partial(char_talking, "lin"))
define hans = Character("Hans", color="b06560", callback=partial(char_talking, "hans"))
define sharon = Character("Sharon", color="46456b", callback=partial(char_talking, "sharon"))
define derek = Character("Derek", color="c2bfa6", callback=partial(char_talking, "derek"))
define service1 = Character("Service Bot", callback=partial(char_talking, "servicerobot_karen"), who_font="font/Syncopate-Bold.ttf")
define goodbrother = Character("Bar Bot", callback=partial(char_talking, "Bar Bot"), who_font="font/Syncopate-Bold.ttf")
define badbrother = Character("kais_storage", callback=partial(char_talking, "Storage Bot"), who_font="font/Syncopate-Bold.ttf")
define carnabot = Character("Carnabot", callback=partial(char_talking, "Carnabot"), who_font="font/Syncopate-Bold.ttf")

#Effects
define flash = Fade(.25, 0.0, .25, color="#fff")

#Positions
transform center:
    xalign 0.5
    yalign 1.0

transform left:
    xalign 0.1
    yalign 1.0

transform right:
    xalign 0.9
    yalign 1.0

transform topleft:
    xalign 0.1
    yalign 0.0

transform topright:
    xalign 0.9
    yalign 0.0

transform topcenter:
    xalign 0.5
    yalign 0.0

transform outLeft:
    xalign -0.5
    yalign 1.0

transform outRight:
    xalign 1.5
    yalign 1.0

transform talking:
    linear 0.1 zoom 1.01

transform stopTalking:
    linear 0.1 zoom 1.00

default speaking_char = None

init -1 python:
    from functools import partial
    def char_talking(char, event_name, *args, **kwargs):
        if event_name == "begin" and char != store.speaking_char:
            if store.speaking_char != None and renpy.showing(store.speaking_char):
                tags = renpy.get_attributes(store.speaking_char)
                str_tags = " "
                if tags != None:
                    str_tags = " ".join(tags)
                #renpy.show(store.speaking_char + " " + str_tags, at_list=[stopTalking])
            if char != None and renpy.showing(char):
                tags = renpy.get_attributes(char)
                str_tags = " "
                if tags != None:
                    str_tags = " ".join(tags)
                #renpy.show(char + " " + str_tags, at_list=[talking])
            store.speaking_char = char


image white = "#ffffff"
label splashscreen:
    scene white
    $ renpy.pause(1, hard=True)

    show logo:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2, hard=True)



    hide logo with dissolve
    $ renpy.pause(0.5, hard=True)

    return

label start:

    scene bg brochure with dissolve

    jump initVariables

#Init the variables
label initVariables:

    $ hasAiKey = False

    $ firstEnterKitchen = True
    $ escapeKitchenCar = False
    $ AIDoorReveal = False

    $ firstEnterBar = True
    $ goodBrotherAskHelp = False
    $ takeGoodBrotherAI = False
    $ failGoodBrotherSteal = False

    $ firstEnterStorage = True
    $ badBrotherAskHelp = False
    $ takeBadBrotherAI = False
    $ failBadBrotherSteal = False

    jump brochure #part1.rpy
