from pico2d import *

import game_framework
import title_state
import add_delete_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.dir = 1
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1

        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_state)


boy = None
grass = None


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def update():
    boy.update()


def draw_world():
    grass.draw()
    boy.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def exit():
    global boy, grass
    del boy
    del grass


def pause():
    pass


def resume():
    pass

