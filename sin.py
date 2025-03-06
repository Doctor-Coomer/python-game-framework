#!/bin/python

import framework

from time import sleep
from math import sin, cos

game = framework.game_framework()

#constants
WIDTH=800
HEIGHT=800


game.spawn_window(width=WIDTH, height=HEIGHT, color=[0,0,0], resizable=True)


line1 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[0,255,0])

box1 = game.create_rectangle(x=WIDTH//2 - 45, y=HEIGHT//2 - 45, width=90, height=90)

line2 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[255,0,0])

box2 = game.create_rectangle(x=WIDTH//2 - 45, y=HEIGHT//2 - 45, width=90, height=90)

line3 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[0,0,255])

box3 = game.create_rectangle(x=WIDTH//2 - 45, y=HEIGHT//2 - 45, width=90, height=90)


i:float = 0
h:float = 0
while True:

    box1.x = int((WIDTH//2 - 45) + sin(i)*200)
    box1.y = int((HEIGHT//2 - 45) + cos(i)*300)

    box1.color = [i*10%255, i*40%255, i*20%255]

    line1.x1=WIDTH//2
    line1.y1=HEIGHT//2
    line1.x2 = box1.x+45
    line1.y2 = box1.y+45

    box2.x = int((WIDTH//2 - 45) - sin(h)*300)
    box2.y = int((HEIGHT//2 - 45) - cos(i)*200)
    
    box2.color = [i*50%255, i*10%255, i*20%255]

    line2.x1=WIDTH//2
    line2.y1=HEIGHT//2
    line2.x2 = box2.x+45
    line2.y2 = box2.y+45

    box3.x = int((WIDTH//2 - 45) - sin(i)*100)
    box3.y = int((HEIGHT//2 - 45) - cos(h)*300)
        
    box3.color = [i*50%255, i*50%255, i*10%255]

    line3.x1=WIDTH//2
    line3.y1=HEIGHT//2
    line3.x2 = box3.x+45
    line3.y2 = box3.y+45

    
    i+=0.1
    h+=0.05

    (WIDTH, HEIGHT) = game.get_window_resolution()
    
    sleep(1/60)
