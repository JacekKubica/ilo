from tkinter import *

WIDTH = None
HEIGHT = None
FPS = None
PIXEL_SPEED_PER_SECOND = None
def begin_drawing(width=800, height=600, fps=30):
    global WIDTH; global HEIGHT; global FPS; global PIXEL_SPEED_PER_SECOND; global canvas
    WIDTH = width
    HEIGHT = height
    FPS = fps
    PIXEL_SPEED_PER_SECOND = 600
    window = Tk()
    canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg="red")
    canvas.pack()
    def inner():
        canvas.clear("all")
        draw()
        window.after(int(1000 / FPS), inner())
    window.mainloop()


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)
    def __sub__(self, v):
        return Vec2(self.x - v.x, self.y - v.y)
    

def create_oval(canvas, lu, rd, fill="yellow"):
    canvas.create_oval(lu.x, lu.y, rd.x, rd.y, fill=fill)

animated_centre = Vec2(WIDTH / 2, HEIGHT / 2)
animated_speed = Vec2(0, 0)
def animate():
    canvas.delete("all")
    CIRC_SIZE = 40
    lu = Vec2(0, 0)
    ru = Vec2(WIDTH, 0)
    ld = Vec2(0, HEIGHT)
    rd = Vec2(WIDTH, HEIGHT)

    create_oval(canvas, lu, lu + Vec2(CIRC_SIZE, CIRC_SIZE))
    create_oval(canvas, ru, ru + Vec2(-CIRC_SIZE, CIRC_SIZE))
    create_oval(canvas, ld, ld + Vec2(CIRC_SIZE, -CIRC_SIZE))
    create_oval(canvas, rd, rd + Vec2(-CIRC_SIZE, -CIRC_SIZE))

    global animated_centre
    animated_centre += animated_speed
    create_oval(canvas, animated_centre - Vec2(CIRC_SIZE / 2, CIRC_SIZE / 2), animated_centre + Vec2(CIRC_SIZE / 2, CIRC_SIZE / 2))
    window.after(int(1000 / FPS), animate)

def start_move(event):
    if event.keycode == 39:
        animated_speed.x = PIXEL_SPEED_PER_SECOND / FPS
    if event.keycode == 37:
        animated_speed.x = -PIXEL_SPEED_PER_SECOND / FPS
    if event.keycode == 38:
        animated_speed.y = -PIXEL_SPEED_PER_SECOND / FPS
    if event.keycode == 40:
        animated_speed.y = PIXEL_SPEED_PER_SECOND / FPS

def stop_move(event):
    global animated_speed
    if event.keycode == 39:
        animated_speed.x = 0
    if event.keycode == 37:
        animated_speed.x = 0
    if event.keycode == 38:
        animated_speed.y = 0
    if event.keycode == 40:
        animated_speed.y = 0

def draw():


window.bind("<KeyPress>", start_move)
window.bind("<KeyRelease>", stop_move)
window.after(int(1000 / FPS), animate)
begin_drawing()
window.mainloop()