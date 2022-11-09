from pico2d import *
import random

import game_framework
import game_world


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 30 # 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.333333
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 14


class Bird:
    image = None
    y_frame = 0

    def __init__(self, x):
        self.x, self.y = x, 300
        self.frame = float(random.randint(0, 13))
        self.face_dir = 1

        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        if self.frame <= 4:
            Bird.y_frame = 2
        elif self.frame <= 9:
            Bird.y_frame = 1
        else:
            Bird.y_frame = 0

        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)

        if self.x >= 1600 - 25:
            self.face_dir = -1
        elif self.x <= 25:
            self.face_dir = 1

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 184, Bird.y_frame * 169, 184, 169, self.x, self.y)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 184, Bird.y_frame * 169, 184, 169, 0.0, 'h', self.x, self.y, 184, 169)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

