#!/bin/python

import framework

from time import sleep
from math import sin, cos

game = framework.game_framework()

#constants
WIDTH = 500
HEIGHT = 500

game.spawn_window(width=WIDTH, height=HEIGHT)

circle = game.create_circle(50, 50, 300, 300, color=[255,0,0])

fps = game.create_text(x=5, y=10, text="FPS: -")

i:float = 0
while True:
    if (game.get_window_fps() != -1):
        fps.text = "FPS: " + str(game.get_window_fps())
    
    circle.x = int(WIDTH//2 - circle.width//2 + sin(i)*100)
    circle.y = int(HEIGHT//2 - circle.height//2 + cos(i)*100)

    i+=0.1
    
    sleep(1/30)
