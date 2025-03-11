#!/bin/python

import framework

from time import sleep
from random import randint

game = framework.game_framework()

#constants
WIDTH=800
HEIGHT=800


game.spawn_window(width=WIDTH, height=HEIGHT)

t = game.create_text(x=10, y=HEIGHT-20, text="FPS: -", color=[0,0,0])

while True:
    if (game.get_window_fps() != -1):
        t.text = "FPS: " + str(game.get_window_fps())
    game.create_line(x1=WIDTH//2, y1=HEIGHT, x2=randint(0,WIDTH), y2=0, color=[randint(0,255),randint(0,255),randint(0,255)])
    sleep(1/60)
