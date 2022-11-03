from pico2d import *

class Grass:
    def __init__(self, depth=0):
        self.image = load_image('grass.png')
        self.depth = depth

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


