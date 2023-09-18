from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=0
y=0

while True:
    
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)
        if x==800:
            break

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y=y+2
        if y==600:
            break

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x=x-2
        if x==0:
            break

    while(y>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y=y-2
        if y==0:
            break
close_canvas()
