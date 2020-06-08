# The script of the game goes in this file.

# Characters name
define neonila = Character("Neonila", color="ff69fd")
define kvin = Character("Kvin", color="c47b4e")
define lin = Character("Lin", color="efd693")
define hans = Character("Hans", color="b06560")
define sharon = Character("Sharon", color="46456b")
define derek = Character("Derek", color="c2bfa6")
define stwin = Character("Twin")
define service = Character("Service Bot")

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

    jump brochure #part1.rpy
