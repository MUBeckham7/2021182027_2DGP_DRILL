from pico2d import *
import game_framework
import play_drill_state

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    pass
    #game_framework.change_state(title_state)

def handle_events():
    global add_Boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_EQUALS:
                game_framework.change_state(play_drill_state)
            elif event.key == SDLK_MINUS:
                game_framework.change_state(play_drill_state)
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(play_drill_state)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


