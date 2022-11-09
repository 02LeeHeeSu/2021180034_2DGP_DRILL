from pico2d import *

import game_framework
import game_world


class Bird:
    image = None

    def __init__(self):
        self.x, self.y = 100, 300
        self.frame = 0
        
        if Bird.image == None:
            image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        pass

    def draw(self):
        pass
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

