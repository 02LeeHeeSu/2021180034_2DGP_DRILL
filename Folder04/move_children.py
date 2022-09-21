from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_square():
    x = 400
    y = 90
    
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.001)

    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.001)

    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.001)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.001)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.001)

def move_circle():
    angle = 0

    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + 210 * math.sin(angle / 360 * 2 * math.pi), 300 - 210 * math.cos(angle / 360 * 2 * math.pi))
        angle += 1
        delay(0.001)

