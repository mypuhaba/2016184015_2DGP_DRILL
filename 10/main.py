import pico2d
import play_state
import logo_state
state = logo_state # 모듈을 변수로 취급

pico2d.open_canvas()

# game main loop code
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()


# finalization code
pico2d.close_canvas()