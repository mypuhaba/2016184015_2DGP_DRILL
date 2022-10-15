import pico2d
import play_state_ex
import logo_state

state = logo_state
pico2d.open_canvas()

states = [logo_state, play_state_ex]

for state in states:
    state.enter()
# game main loop code
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

# finalization code
pico2d.close_canvas()