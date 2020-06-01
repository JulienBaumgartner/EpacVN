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

screen passwordGame():
    frame:
        xalign 0.5 ypos 50
        xpadding 10
        ypadding 10

        vbox:
            spacing 10
            xalign 0.5

            text "Enter the password: ":
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

    "Be careful, after a certain number of errors, the security system can kill your characters."

    show screen passwordTuto
    call screen passwordGame

label passwordGameWin:
    hide screen passwordGame
    hide screen passwordTuto
    "Success, you leave the kitchen car."
    $ escapeKitchenCar = True
    jump explorationMap

label passwordGameLose:
    hide screen passwordGame
    hide screen passwordTuto

    "Bad end 1"
    return
