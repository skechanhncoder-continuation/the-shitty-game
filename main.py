def on_left_pressed():
    pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

mySprite = sprites.create(assets.image("""
        Shitty Player
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)