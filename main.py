mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(assets.image("""
            shitty player1
            """),
        SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
    sprites.create(assets.image("""
            Shitty Player
            """),
        SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
    sprites.create(assets.image("""
            shitty player2
            """),
        SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
    sprites.create(assets.image("""
            shitty playerr
            """),
        SpriteKind.player))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.THREE))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.FOUR))