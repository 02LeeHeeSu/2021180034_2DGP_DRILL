from pico2d import *

open_canvas()

# 사진 크기가 577 * 500이므로 가로를 58(577 / 10) 세로를 62(500 / 8) 크기로 자르자
character = load_image('The_Legend_of_Zelda_Link_Sprite_Sheet.png')


def face_frame():
    frame_y = 7
    while frame_y > 3:
        frame_x = 0
        while frame_x < 3:
            clear_canvas()
            character.clip_draw(frame_x * 58, frame_y * 62, 58, 62, 400, 300)
            update_canvas()
            delay(1)
            get_events()
            frame_x += 1

        frame_y -= 1


def front_frame():
    frame = 0
    for y in range(550, 50 - 1, -5):
        clear_canvas()
        character.clip_draw(frame * 58, 3 * 62, 58, 62, 400, y)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()


def left_frame():
    frame = 0
    for x in range(750, 50 - 1, -5):
        clear_canvas()
        character.clip_draw(frame * 58, 2 * 62, 58, 62, x, 300)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()


def back_frame():
    frame = 0
    for y in range(50, 550 + 1, 5):
        clear_canvas()
        character.clip_draw(frame * 58, 1 * 62, 58, 62, 400, y)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()


def right_frame():
    print('Right')


#face_frame()

#front_frame()

#left_frame()

back_frame()

#right_frame()

close_canvas()
