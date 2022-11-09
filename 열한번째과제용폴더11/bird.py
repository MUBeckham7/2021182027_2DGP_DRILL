from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH =30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 /60.0)
RUN_SPEED_MPS =(RUN_SPEED_MPM /60.0)
RUN_SPEED_PPS =(RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION =0.5
ACTION_PER_TIME =1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:

    def __init__(self):
        self.x, self.y = 100, 350
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')


    def do(self):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1580:
            self.dir = -1
        elif self.x < 20:
            self.dir =1
    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 180, 0, 175, 120,0,'', self.x, self.y,55,30)
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 180, 0, 175, 120,0, 'h', self.x, self.y,55,30)

