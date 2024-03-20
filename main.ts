controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    for (let index = 0; index <= 0; index++) {
        Skud = imagesExt.createProjectileAtAngleFromSprite(img`
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
            `, Rumskib, 1000, 6, 15, index * 2)
        Skud = imagesExt.createProjectileAtAngleFromSprite(img`
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
            `, Rumskib, 1000, -6, 15, index * -2)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    sprites.destroy(otherSprite2, effects.fire, 500)
    sprites.destroy(sprite2)
    Penge += 1
})
let Alien: Sprite = null
let Penge = 0
let Skud: Sprite = null
let Rumskib: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
Rumskib = sprites.create(assets.image`Rumskib`, SpriteKind.Player)
tiles.placeOnTile(Rumskib, tiles.getTileLocation(10, 10))
info.setLife(5)
tiles.placeOnTile(Rumskib, tiles.getTileLocation(20, 48.5))
Rumskib.fx = 10
Rumskib.fy = 10
scene.cameraFollowSprite(Rumskib)
imagesExt.moveSpriteAngular(
Rumskib,
assets.image`Rumskib`,
-90,
-90,
65,
10,
7,
90
)

game.onUpdateInterval(2000, function () {
    Alien = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Alien.setStayInScreen(true)
    Alien.follow(Rumskib, 20)
    tiles.placeOnRandomTile(Alien, assets.tile`Galakse`)
})
