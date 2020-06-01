# The script of the game goes in this file.

# Characters name
define neonila = Character("Neonila")
define kvin = Character("Kvin")
define lin = Character("Lin")
define hans = Character("Hans")
define sharon = Character("Sharon")
define derek = Character("Derek")
define stwin = Character("Twin")

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
    xalign -0.5
    yalign 1.0

label start:

    scene bg brochure

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

    jump brochure

label test:

    scene bg room

    show derek normal at left
    show kvin normal at center
    show sharon normal at right

    " "

    hide derek normal
    hide kvin normal
    hide sharon normal

    show lin normal at left
    show neonila normal at center
    show hans normal at right


    " "

    return
