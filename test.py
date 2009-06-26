#!/usr/bin/env python

import animatedsprite
import pyglet
from pyglet.window import key

window = pyglet.window.Window()
res = pyglet.image.load('test_frames.png')

grid = pyglet.image.ImageGrid(res.get_region(0,7*32,32*8,32), 1, 8, 32, 32)
animation = pyglet.image.Animation.from_image_sequence(grid.get_texture_sequence(), 0.1, True )
sprite = animatedsprite.AnimatedSprite(animation, 0, 0)
sprite.add_lookup( [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,5,6,7] )
sprite.add_lookup( [1,2,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7] )
sprite.set_active_lookup(1)
@window.event
def on_draw():
    window.clear()
    sprite.draw()
@window.event
def on_key_press(symbol, mod):
    if symbol == 49:
        sprite.set_active_lookup(1)
    if symbol == 50:
        sprite.set_active_lookup(2)

pyglet.app.run()

