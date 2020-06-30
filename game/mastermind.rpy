# Sc 09.3
# Mastermind minigame

init python:

    def changeNumber(index, value):
        currentPassword[index] = (currentPassword[index] + value) % 7
        passwordState[index] = "#ffffff"

    def sendPassword():
        passwordFind = True
        remainingNumbers = []
        for i in range(4):
            if currentPassword[i] == password[i]:
                passwordState[i] = "#00ff00"
            else:
                passwordState[i] = "#ff0000"
                remainingNumbers.append(password[i])
                passwordFind = False

        for i in range(4):
            if passwordState[i] != "#00ff00" and currentPassword[i] in remainingNumbers:
                remainingNumbers.remove(currentPassword[i])
                passwordState[i] = "#ffaa00"

        if passwordFind:
            renpy.jump("passwordGameWin")
        else:
            global badPasswords
            badPasswords += 1
            if badPasswords == 5:
                renpy.jump("passwordMistakes")
            elif badPasswords == 9:
                renpy.jump("passwordMistakes2")
            elif badPasswords == 10:
                renpy.jump("passwordGameLose")


screen passwordGame():
    frame:
        xpos 880 ypos 415
        xpadding 10
        ypadding 10
        background Solid("#00000000")

        vbox:
            spacing 4
            xalign 0.5

            hbox:
                spacing 10
                xalign 0.5


                for i in range(4):
                    vbox:
                        spacing 10

                        button:
                            action Function(changeNumber, index=i, value=1)
                            text _("▲") style "button_text"
                            xalign 0.5

                        text "{0}".format(currentPassword[i]):
                            xalign 0.5
                            color passwordState[i]

                        button:
                            action Function(changeNumber, index=i, value=6)
                            text _("▼") style "button_text"
                            xalign 0.5


            text "[badPasswords] mistakes":
                xalign 0.5

            button:
                action Function(sendPassword)
                text _("Send") style "button_text"
                xalign 0.5

screen passwordTuto():
    frame:
        xalign 0.5 yalign 0.9
        xpadding 10
        ypadding 10

        vbox:
            spacing 10

            text "When you send the password, the color of the numbers changes:"

            text "Green: The number is correct and well placed.":
                color "#00ff00"
                xpos 30

            text "Orange: The number is correct but misplaced.":
                color "#ffaa00"
                xpos 30

            text "Red: The number is incorrect.":
                color "#ff0000"
                xpos 30



label startpasswordgame:

    $ password = []
    $ password.append(4)
    $ password.append(renpy.random.randint(0,6))
    $ password.append(renpy.random.randint(0,6))
    $ password.append(renpy.random.randint(0,6))
    $ passwordFind = False
    $ passwordState = ["#ffffff", "#ffffff", "#ffffff", "#ffffff"]
    $ badPasswords = 0
    $ currentPassword = [0, 0, 0, 0]


    show screen passwordTuto
    call screen passwordGame

label passwordMistakes:
    hide screen passwordGame
    hide screen passwordTuto

    show sharon normal at right with moveinright
    sharon "I don't want to stress you out but ... We don't have much time left and it is out of the question for it to end this way, so hurry and get us out!"
    hide sharon with moveoutright

    show screen passwordTuto
    call screen passwordGame

label passwordMistakes2:
    hide screen passwordGame
    hide screen passwordTuto

    show hans normal at right with moveinright
    hans "THE END IS COMING! IT'S ALL THEIR FAULT! WHY CAN'T ANYONE OPEN THAT DAMN DOOR?!?"
    hide hans with moveoutright

    show screen passwordTuto
    call screen passwordGame

label passwordGameWin:
    hide screen passwordGame
    hide screen passwordTuto
    scene bg_kitchen_door_back_open
    play sound "/audio/porte01.mp3"

    $ config.autosave_on_quit = True
    $ _game_menu_screen = "save"
    $ allowSave = True

    "Success, you leave the kitchen car."
    $ escapeKitchenCar = True
    jump explorationMap # explorationMap.rpy

label passwordGameLose:
    hide screen passwordGame
    hide screen passwordTuto
    scene bg_badend
    "you are dead"

    $ config.autosave_on_quit = True
    $ _game_menu_screen = "save"
    $ allowSave = True

    jump gameover1 #gameovers.rpy
