#!/bin/python

import framework

from time import sleep
from math import sin, cos

game = framework.game_framework()

#constants
WIDTH=800
HEIGHT=800


game.spawn_window(width=WIDTH, height=HEIGHT, color=[0,0,0], resizable=True)


line1 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[0,255,0], width=5)

line2 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[255,0,0], width=5)

line3 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[0,0,255], width=5)

line4 = game.create_line(x1=WIDTH//2, y1=HEIGHT//2, x2=0, y2=0, color=[255,255,0], width=5)


fps = game.create_text(x=5, y=10, text="FPS: -", color=[255,255,255])

i:float = 0
h:float = 0
while True:
    if (game.get_window_fps() != -1):
        fps.text = "FPS: " + str(game.get_window_fps())

    line1.x1 = WIDTH//2
    line1.y1 = HEIGHT//2
    line1.x2 = int((WIDTH//2) + sin(i)*300)
    line1.y2 = int((HEIGHT//2) + cos(i)*300)

    line2.x1 = WIDTH//2
    line2.y1 = HEIGHT//2
    line2.x2 = int((WIDTH//2) + sin(i)*300)
    line2.y2 = int((HEIGHT//2) + cos(h*2)*100)

    line3.x1 = WIDTH//2
    line3.y1 = HEIGHT//2
    line3.x2 = int((WIDTH//2) - sin(i+h)*200)
    line3.y2 = int((HEIGHT//2) - cos(i+h)*200)

    line4.x1 = WIDTH//2
    line4.y1 = HEIGHT//2
    line4.x2 = int((WIDTH//2) - sin(i-h)*200)
    line4.y2 = int((HEIGHT//2) + cos(i+h)*200)
    
    i+=0.1
    h+=0.05

    (WIDTH, HEIGHT) = game.get_window_resolution()
    
    sleep(1/30)
