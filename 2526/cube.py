# github.com/JacekKubica/ilo

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

def draw_triangle(a, b, c, color="black"):
    vs = [Vec2(*p) if isinstance(p, tuple) else p for p in [a, b, c]]
    vs = [to_screen_coords(v) for v in vs]
    a, b, c = vs
    canvas.create_polygon([*a, *b, *c])

def draw_rectangle(bottom_left_corner, sizes, color="black"):
    if isinstance(bottom_left_corner, tuple):
        bottom_left_corner = Vec2(*bottom_left_corner)
    if isinstance(sizes, tuple):
        sizes = Vec2(*sizes)
    ld = bottom_left_corner 
    ru = bottom_left_corner + sizes
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
# def draw_rectangle(bottom_left_corner, sizes, color="black"):
#
#
# def pressed(key):
#     - checks if key is pressed
#     - currently handled keys are Key.LEFT, Key.RIGHT, Key.UP, KEY.DOWN



def to_screen(x, y, z):
    x, z = math.cos(angle) * x + math.sin(angle) * z, -math.sin(angle) * x + math.cos(angle) * z
    z += t
    x /= z
    x += 1
    x /= 2
    y /= z
    y += 1
    y /= 2
    return (x, y)


points = [
    # przednia ściana
    [-1, -1, 1], # lewy dolny róg
    [+1, -1, 1], # prawy dolny róg
    [+1, +1, 1], # prawy górny róg
    [-1, +1, 1], # lewy górny róg
    
    # tylnia ściana
    [-1, -1, -1], # lewy dolny róg
    [+1, -1, -1], # prawy dolny róg
    [+1, +1, -1], # prawy górny róg
    [-1, +1, -1], # lewy górny róg
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0], # połączenia w przedniej ścianie
    [4, 5], [5, 6], [6, 7], [7, 4], # połączenia w tylnej ścianie
    # połączenia między przednia a tylną ścianą
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]

import math
t = 5  # przesunięcie
angle = 0  # obrót 
def draw():
    global t
    global angle
    angle += .1
    for p in points:
        draw_circle(to_screen(*p), .0001)
    
    for e in edges:
        p = points[e[0]]
        q = points[e[1]]
        draw_line(to_screen(*p), to_screen(*q))


run()