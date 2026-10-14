from drawing import *

# EXAMPLE USAGE
POS = Vec2(.5, .5)
def draw():
    global POS
    draw_line((.5, 0), (.5, 1))
    draw_line((0, .5), (1, .5))
    draw_circle(POS, .1)
    draw_rectangle(POS + Vec2(.3, .3), .2)
    if pressed(Key.LEFT): POS += Vec2(-.01, 0)
    if pressed(Key.RIGHT): POS += Vec2(.01, 0)
    if pressed(Key.UP): POS += Vec2(0, .01)
    if pressed(Key.DOWN): POS += Vec2(0, -.01)

run()