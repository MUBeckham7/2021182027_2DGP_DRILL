from pico2d import *
import game_framework
import menu_drill_state



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


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir *2
        if self.x > 800:
            self.dir = -1
            self.x=800
        elif self.x<0:
            self.dir=1
            self.x =0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else :
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.change_state(menu_drill_state)


#게임 초기화: 객체들을 생성
boy = None # C Null
grass = None
def enter():
    global boy,grass
    boy = Boy()
    grass = Grass()


def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

# 게임 종료 코드-객체를 소멸시키는 과정
def exit():
    global boy,grass
    del boy
    del grass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__': #만약 단독 실행중이라면,
    test_self()
