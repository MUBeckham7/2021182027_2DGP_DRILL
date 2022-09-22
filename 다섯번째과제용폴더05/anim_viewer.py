from pico2d import*

open_canvas()

character=load_image('wonpun.png')

x,y=0,0

def ani_55(x,y):
    clear_canvas()
    character.clip_draw( 15 + x * 55 , y , 60, 120 , 400, 300)
    update_canvas()
    delay(0.2)
    get_events()

def ani_70(x,y):
    clear_canvas()
    character.clip_draw( x , y , 70, 120 , 400, 300)
    update_canvas()
    delay(0.2)
    get_events()

def ani_90(x,y):
    clear_canvas()
    character.clip_draw( x , y , 90, 120 , 400, 300)
    update_canvas()
    delay(0.2)
    get_events()

while True:
  for x in range(0,8):
    ani_55(x,680)

  ani_70(420,680)
  ani_90(480,680)
  ani_90(20,240)
  ani_90(100,240)
  ani_70(260,240)
  ani_70(330,240)
  ani_90(420,240)
  ani_90(25,100)
  ani_90(110,100) 
  ani_90(220,100)
  ani_90(320,100)
  ani_90(690,460)
  ani_90(20,360)
  ani_90(620,460)
  ani_90(580,100)
  ani_90(680,100)
  ani_90(40,-20)
  ani_90(180,-20)
  break
  


close_canvas()
