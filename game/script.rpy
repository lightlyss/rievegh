define cal = Character("Callia")
define ler = Character("Lerona")

label start:
    python:
        camera_reset()
        def initLayers():
            layer_move("background", 1500)
            layer_move("middle", 1100)
            layer_move("forward", 900)
        def focusLeft(t=0):
            camera_move(-4300, -3500, -200, 0, t)
        def focusRight(t=0):
            camera_move(4400, -4600, -200, 0, t)
        def unfocus(t=0):
            camera_move(534, -2150, -1100, 0, t)

    # Scene calls require reset of Z
    scene alley onlayer background
    $ initLayers()

    show callia at left onlayer middle
    show lerona at right onlayer middle

    $ unfocus(1)
    cal "..."
    cal "{i}It's getting cold out, huh...{/i}"
    $ focusRight(0.5)
    ler "It's not much farther, we'll probably make it."
    ler "I hope..."
    $ unfocus(1)
    cal "We could've just gone tomorrow..."
    cal "Honestly..."
    return
