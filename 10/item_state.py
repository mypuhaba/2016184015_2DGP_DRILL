from pico2d import *
import game_framework
import play_state

image = None


def enter():
    global image, logo_time
    image = load_image('item_select.png')
    logo_time = 0.0

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()



def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면,
    test_self()