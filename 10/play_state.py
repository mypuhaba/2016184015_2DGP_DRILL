from pico2d import *
import game_framework
import logo_state
import play_state
import title_state
import item_state
import add_delete_boy_state
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None


    def update(self):
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)

        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 0.2
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0


    def draw(self):
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_boy_state)


boy = None
grass = None
team = None

def enter():
    global boy, grass
    global team
    boy = Boy()
    grass = Grass()
    team = [Boy()]


def exit():
    global boy, grass
    global team
    del boy
    del grass
    del team


def update():
    global boy
    global team
    for boy in team:
        boy.update()



# 월드를 그린다.
def draw_world():
    grass.draw()
    for boy in team:
        boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass



def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면,
    test_self()