screen kitchenEscapeTuto():
    default valTuto = 20
    default currentValTuto = 10

    frame:
        xalign 0.5 ypos 50
        xsize 600

        vbox:
            spacing 10
            $ doorUnlockedTuto = True

            text "Move the slider until the light is green"
            hbox:
                spacing 10
                bar value ScreenVariableValue("currentValTuto", 30) style "slider" xsize 500 yalign 0.5
                if currentValTuto == valTuto:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlockedTuto = False


            button:
                if doorUnlockedTuto:
                    action Return(True)
                text _("Start") style "button_text"
                xalign 0.5

screen screenEscapeGame():
    default val1 = renpy.random.randint(1,30)
    default val2 = renpy.random.randint(1,30)
    default val3 = renpy.random.randint(1,30)
    default val4 = renpy.random.randint(1,30)
    default val5 = renpy.random.randint(1,30)


    default currentval1 = renpy.random.randint(1,30)
    default currentval2 = renpy.random.randint(1,30)
    default currentval3 = renpy.random.randint(1,30)
    default currentval4 = renpy.random.randint(1,30)
    default currentval5 = renpy.random.randint(1,30)


    frame:
        xalign 0.0 ypos 50
        xsize 601 ysize 443
        background "uibackground"

        vbox:
            spacing 10
            $ doorUnlocked = True
            hbox:
                spacing 25
                bar value ScreenVariableValue("currentval1", 30) style "slider" xsize 500 yalign 0.5
                if currentval1 == val1:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlocked = False

            hbox:
                spacing 25
                bar value ScreenVariableValue("currentval2", 30) style "slider" xsize 500 yalign 0.5
                if currentval2 == val2:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlocked = False

            hbox:
                spacing 25
                bar value ScreenVariableValue("currentval3", 30) style "slider" xsize 500 yalign 0.5
                if currentval3 == val3:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlocked = False

            hbox:
                spacing 25
                bar value ScreenVariableValue("currentval4", 30) style "slider" xsize 500 yalign 0.5
                if currentval4 == val4:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlocked = False

            hbox:
                spacing 25
                bar value ScreenVariableValue("currentval5", 30) style "slider" xsize 500 yalign 0.5
                if currentval5 == val5:
                    add "escape_unlock.png"
                else:
                    add "escape_lock.png"
                    $ doorUnlocked = False


            button:
                if doorUnlocked:
                    action Jump("escapewin")
                text _("Unlock") style "button_text"
                xalign 0.5
                top_margin 10


transform smoke_move:
    xalign 0.5 yalign -0.5
    linear 46.0 yalign 1.0

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump("escapelose")])

label escapegame:
    play sound "audio/gaz.mp3" loop
    show hans normal:
        xalign 0.4 yalign 1.0

    call screen kitchenEscapeTuto


    show toxic-smoke at smoke_move
    $ time = 45
    show screen countdown
    call screen screenEscapeGame

    jump escapelose

label escapewin:
    hide screen countdown
    hide stwin with moveoutright

    if takeGoodBrotherAI:
        scene bg_ai_room_end
        "Sc 15.1.3, force exit"
    else:
        scene bg_exit_door_opened
        play sound "audio/porte01.mp3"
        "Sc 15.2.1, bad brother grateful."
        "Sc 15.2.3, reveal exit"
    stop music fadeout 0.5
    jump revelation # bunker.rpy


label escapelose:
    if takeGoodBrotherAI:
        jump gameover2 # gameovers.rpy
    jump gameover3 # gameovers.rpy
