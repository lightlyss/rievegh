init python:
    h = Character("Hiyori")
    hiyo = L2D("hiyo")

label l2d:
    # models/hiyori/Hiyori.model3.json
    $ hiyo.load("hiyori", "Hiyori")

    $ camera_reset()
    scene alley onlayer background
    $ initLayers()
    $ unfocus(0)

    show hiyo onlayer forward
    $ camera_move(225, -1366, -800, 0, 2, "easein")
    $ hiyo.model.start_motion(group = u"Idle", no = 2, priority = 3)
    h "Welcome to the Live2D demo!"
    h "It seems like this plugin is a little unstable..."

    $ camera_move(178, -383, -400, 0, 2, "ease")
    $ hiyo.model.start_motion(group = u"Idle", no = 7, priority = 3)
    h "Maybe someone else can do something with it."
    h "Anyway, I won't be saying too much here..."

    $ camera_move(225, -1366, -800, 0, 2, "easeout")
    $ hiyo.model.start_motion(group = u"TapBody", no = 0, priority = 3)
    h "Remember to add some interesting motions to your models!"
    h "That's all for now!"

    $ hiyo.__del__()
    return
