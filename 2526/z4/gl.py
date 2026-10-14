from enum import Enum
from tkinter import *

WIDTH = None
HEIGHT = None
FPS = None
KEYS_PRESSED = []
def run(width=700, height=700, fps=30, background_color="white"):
    global WIDTH; global HEIGHT; global FPS; global PIXEL_SPEED_PER_SECOND; global canvas
    WIDTH = width
    HEIGHT = height
    FPS = fps
    PIXEL_SPEED_PER_SECOND = 600
    window = Tk()
    canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg=background_color)
    canvas.pack()
    def inner():
        print(KEYS_PRESSED)
        canvas.delete("all")
        draw()
        window.after(int(1000 / FPS), inner)

    def kp(event):
        global KEYS_PRESSED
        try:
            k = Key(event.keycode)
            if not k in KEYS_PRESSED: KEYS_PRESSED.append(k)
        except:
            pass
    def kr(event):
        global KEYS_PRESSED
        KEYS_PRESSED = []
        # try:
            # k = Key(event.keycode)
            # if not k in KEYS_PRESSED: KEYS_PRESSED.remove(k)
        # except:
            # pass

    window.bind("<KeyPress>", kp)
    window.bind("<KeyRelease>", kr)
    window.after(int(1000 / FPS), inner)
    window.mainloop()

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)
    def __sub__(self, v):
        return Vec2(self.x - v.x, self.y - v.y)
    def __mul__(self, s):
        return Vec2(self.x * s, self.y * s)
    def __truediv__(self, s):
        return self * (1 / s)
    
def to_screen_coords(v):
    return v.x * WIDTH, (1 - v.y) * HEIGHT

def draw_circle(center, radius, color="black"):
    if isinstance(center, tuple):
        center = Vec2(*center)
    ld = center - Vec2(radius, radius)
    ru = center + Vec2(radius, radius)
    canvas.create_oval(*to_screen_coords(ld), *to_screen_coords(ru), fill=color)

def draw_point(center, color="black"):
    draw_circle(center, 0.001, color)

def draw_line(begin, end, color="black"):
    if isinstance(begin, tuple):
        begin = Vec2(*begin)
    if isinstance(end, tuple):
        end = Vec2(*end)
    canvas.create_line(*to_screen_coords(begin), *to_screen_coords(end), fill=color)


class Key(Enum):
    RIGHT = 39
    LEFT = 37
    UP = 38
    DOWN = 40

def pressed(key):
    return key in KEYS_PRESSED


# IMPLEMENTATION

def eval(f, min, max):
    H = 1 / 256
    ret = []
    while min <= max:
        ret.append((min, f(min)))
        min += H
    return ret

# EXAMPLE USAGE
# POS = Vec2(.5, .5)
# def draw():
    # global POS
    # draw_line((.5, 0), (.5, 1))
    # draw_line((0, .5), (1, .5))
    draw_circle(POS, .1)
    # if pressed(Key.LEFT): POS += Vec2(-.01, 0)
    # if pressed(Key.RIGHT): POS += Vec2(.01, 0)
    # if pressed(Key.UP): POS += Vec2(0, .01)
    # if pressed(Key.DOWN): POS += Vec2(0, -.01)
    # vs = eval(lambda x: x * x, -1, 1)

    # for v in vs:
        # draw_point((Vec2(*v) / 2 + Vec2(.5, .5))) 


# run()