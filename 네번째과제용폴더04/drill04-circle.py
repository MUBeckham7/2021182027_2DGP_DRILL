from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x=400
y=90


while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x= x + math.radians(180)
    y=y+ math.radians(240)
    delay(0.01)


close_canvas()
