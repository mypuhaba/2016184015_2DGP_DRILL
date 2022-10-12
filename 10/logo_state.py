from pico2d import *

image = None
running = True
logo_time = 0.0

def enter():
    global image, logo_time
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    running = True
    pass

def exit():
    global image
    del image
    pass

def update():
    global running
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        running = False
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()