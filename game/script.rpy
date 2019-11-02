define cal = Character("Callia", who_color="#ffccff")
define ler = Character("Lerona", who_color="#ffc34d")

label start:
    python:
        camera_reset()
        def initLayers():
            layer_move("background", 1500)
            layer_move("middle", 1100)
            layer_move("forward", 900)
        def focusLeft(t=0.5):
            camera_move(-4300, -3500, -200, 0, t)
        def focusRight(t=0.5):
            camera_move(4400, -4600, -200, 0, t)
        def unfocus(t=0.5):
            camera_move(534, -2150, -1100, 0, t)

    # Scene calls require reset of Z
    scene alley onlayer background
    $ initLayers()
    $ focusRight(0)
    show callia at left onlayer middle
    show lerona at right onlayer middle

    ler "..."
    ler "Have some wine."
    $ unfocus()
    cal "I don't see any wine."
    show lerona down at right onlayer middle
    ler "There isn’t any."
    show callia bleh at left onlayer middle
    cal "Then it wasn’t very civil of you to offer it."
    ler "It wasn't very civil of you to sit down without being invited."
    $ focusLeft()
    cal "I didn't know it was {i}your{/i} table."
    cal "It's laid for a great many more than three."
    $ unfocus()
    ler "..."
    show lerona concerned at right onlayer middle
    ler "Your hair wants cutting."
    cal "You should learn not to make personal remarks."
    cal "It's very rude."
    show lerona down at right onlayer middle
    ler "..."
    ler "Why is a raven like a writing-desk?"
    show callia curious at left onlayer middle
    $ focusLeft()
    cal "{i}Come, we shall have some fun now!{/i}"
    cal "I believe I can guess that."
    show lerona at right onlayer middle
    $ focusRight()
    ler "Do you mean that you think you can find out the answer to it?"
    show callia at left onlayer middle
    $ unfocus()
    cal "Exactly so."
    return
