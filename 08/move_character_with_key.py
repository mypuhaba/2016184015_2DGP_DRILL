from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x_dir, y_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir = 1
            elif event.key == SDLK_LEFT:
                x_dir = -1
            elif event.key == SDLK_UP:
                y_dir = 1
            elif event.key == SDLK_DOWN:
                y_dir = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            x_dir, y_dir = 0, 0
    pass


open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
x_dir, y_dir = 0, 0

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += x_dir*5
    if x > TUK_WIDTH or x < 0:
        # running = False
        x_dir = 0
    y += y_dir*5
    if y > TUK_HEIGHT or y < 0:
        # running = False
        y_dir = 0
    delay(0.01)

close_canvas()

