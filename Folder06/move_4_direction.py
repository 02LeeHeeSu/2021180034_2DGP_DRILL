from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
running = True
dir_x, dir_y = 0, 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

def handle_events():
    global running
    global dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False



open_canvas(TUK_WIDTH, TUK_HEIGHT)

while running:
    clear_canvas()
    handle_events()

close_canvas()

