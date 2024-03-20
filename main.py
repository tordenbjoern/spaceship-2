def on_a_pressed():
    global Skud
    for index in range(1):
        Skud = imagesExt.create_projectile_at_angle_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . 4 5 5 4 . . . . . . 
                            . . . . . . 2 5 5 2 . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Rumskib,
            1000,
            6,
            15,
            index * 2)
        Skud = imagesExt.create_projectile_at_angle_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . 4 5 5 4 . . . . . . 
                            . . . . . . 2 5 5 2 . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Rumskib,
            1000,
            -6,
            15,
            index * -2)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global Penge
    sprites.destroy(otherSprite2, effects.fire, 500)
    sprites.destroy(sprite2)
    Penge += 1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

Alien: Sprite = None
Skud: Sprite = None
Rumskib: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Rumskib = sprites.create(assets.image("""
    Rumskib
"""), SpriteKind.player)
tiles.place_on_tile(Rumskib, tiles.get_tile_location(10, 10))
info.set_life(5)
Penge = 0
tiles.place_on_tile(Rumskib, tiles.get_tile_location(20, 48.5))
Rumskib.fx = 10
Rumskib.fy = 10
camx = Rumskib.x
camy = Rumskib.y
imagesExt.move_sprite_angular(Rumskib,
    assets.image("""
        Rumskib
    """),
    -90,
    -90,
    65,
    10,
    7,
    90)

def on_on_update():
    global camx, camy
    if True:
        camx = Rumskib.x
        camy = Rumskib.y
        scene.center_camera_at(camx, camy)
game.on_update(on_on_update)

def on_update_interval():
    global Alien
    Alien = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f1111111dbf......
                    ......fd1111111ddf......
                    ......fd111111dddf......
                    ......fd111ddddddf......
                    ......fd111ddddddf......
                    ......fd1dddddddbf......
                    ......fd1dfbddbbff......
                    ......fbddfcdbbcf.......
                    .....ffffccddbfff.......
                    ....fcb1bbbfcffff.......
                    ....f1b1dcffffffff......
                    ....fdfdf..ffffffffff...
                    .....f.f.....ffffff.....
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    Alien.set_stay_in_screen(True)
    Alien.follow(Rumskib, 20)
    tiles.place_on_random_tile(Alien, assets.tile("""
        Galakse
    """))
game.on_update_interval(2000, on_update_interval)
