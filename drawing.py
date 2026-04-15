from enum import Enum
from tkinter import *

WIDTH = None
HEIGHT = None
FPS = None
KEYS_PRESSED = []
def draw():
    raise RuntimeError("draw function not supplied")

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

def draw_rectangle(center, size, color="black"):
    ld = center - Vec2(size, size) / 2
    ru = center + Vec2(size, size) / 2
    canvas.create_rectangle(*to_screen_coords(ld), *to_screen_coords(ru), fill=color)


class Key(Enum):
    RIGHT = 39
    LEFT = 37
    UP = 38
    DOWN = 40

def pressed(key):
    return key in KEYS_PRESSED


# API:
# def run(width=700, height=700, fps=30, background_color="white")
#     - runs the program with given parameters
#     - requires that user supplies function named draw, taking no argument;
#       this function is used to put things on the screen
#
# def draw_circle(center, radius, color="black"):
# def draw_point(center, color="black"):
# def draw_line(begin, end, color="black"):
# def draw_rectangle(center, size, color="black"):
#
#
# def pressed(key):
#     - checks if key is pressed
#     - currently handled keys are Key.LEFT, Key.RIGHT, Key.UP, KEY.DOWN


