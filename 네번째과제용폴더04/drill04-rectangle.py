from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
a=0

  
while(True):
  while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+2
    delay(0.001)
    if(x==800):
      while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.001)
    if(y==600):
      while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.001)
    if(x==0):
      while(y>30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.001)

close_canvas()
